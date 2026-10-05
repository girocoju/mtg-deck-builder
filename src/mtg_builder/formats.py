"""Regras de construção por formato (como dados) e validação de decklists."""

import json
import re

from . import decklist

SIXTY = {"min_main": 60, "max_side": 15, "max_copies": 4}
SINGLETON_100 = {"exact": 100, "max_side": 0, "max_copies": 1, "commander": True}

# Chaves = nomes de formato do Scryfall, mais "limited" (draft/selado).
# `notes` lista regras do formato que o validador NÃO confere.
RULES = {
    **dict.fromkeys(
        ("standard", "pioneer", "modern", "legacy", "vintage", "pauper", "historic",
         "timeless", "alchemy", "explorer", "future", "premodern", "oldschool", "penny"),
        SIXTY,
    ),
    "gladiator": {"exact": 100, "max_side": 0, "max_copies": 1},
    "commander": SINGLETON_100,
    "duel": SINGLETON_100,
    "predh": SINGLETON_100,
    "paupercommander": {**SINGLETON_100, "commander": "any",
                        "notes": ["comandante precisa ser criatura incomum (não conferido)"]},
    "brawl": {**SINGLETON_100, "planeswalker_commander": True},
    "competitivebrawl": {**SINGLETON_100, "planeswalker_commander": True},
    "standardbrawl": {**SINGLETON_100, "exact": 60, "planeswalker_commander": True},
    "oathbreaker": {"exact": 60, "max_side": 0, "max_copies": 1, "commander": "any",
                    "notes": ["oathbreaker (planeswalker) e signature spell não são conferidos"]},
    "limited": {"min_main": 40, "max_side": None, "max_copies": None, "legality": False},
}

NUMBER_WORDS = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                "eight": 8, "nine": 9, "ten": 10}


def copy_limit(card, default):
    """Limite de cópias de uma carta: básicos e "any number" não têm limite; cartas
    como Seven Dwarves trazem o próprio limite no texto."""
    text = card["oracle_text"] or ""
    if default is None or decklist.is_basic(card) \
            or "A deck can have any number of cards named" in text:
        return None
    match = re.search(r"A deck can have up to (\w+) cards named", text)
    if match:
        return NUMBER_WORDS.get(match[1], default)
    return default


def _front(card, key):
    return (card[key] or "").split(" // ")[0]


def can_be_commander(card, planeswalker_ok=False):
    types = _front(card, "type_line").split("—")[0]
    if "can be your commander" in (card["oracle_text"] or ""):
        return True
    if "Legendary" not in types:
        return False
    if "Creature" in types or (planeswalker_ok and "Planeswalker" in types):
        return True
    return ("Vehicle" in _front(card, "type_line") or "Spacecraft" in _front(card, "type_line")) \
        and card["power"] is not None


def can_pair(a, b):
    """Dois comandantes: partner, partner with, friends forever, background ou Doctor's companion."""
    ka, kb = set(json.loads(a["keywords"] or "[]")), set(json.loads(b["keywords"] or "[]"))
    if "Partner with" in ka or "Partner with" in kb:
        return (f"Partner with {_front(b, 'name')}" in (a["oracle_text"] or "")
                or f"Partner with {_front(a, 'name')}" in (b["oracle_text"] or ""))
    if "Partner" in ka and "Partner" in kb:
        return True
    if "Friends forever" in ka and "Friends forever" in kb:
        return True
    for x, kx, y in ((a, ka, b), (b, kb, a)):
        if "Choose a background" in kx and "Background" in (y["type_line"] or ""):
            return True
        if "Doctor's companion" in kx and "Time Lord Doctor" in (y["type_line"] or ""):
            return True
    return False


def validate(conn, deck, fmt, game=None):
    """Confere a lista contra as regras do formato. Devolve (erros, avisos), listas de
    textos; a lista é válida se `erros` estiver vazia. Chama decklist.resolve()."""
    fmt = fmt.lower()
    if fmt not in RULES:
        return [f"Formato desconhecido: {fmt}. Conhecidos: {', '.join(sorted(RULES))}"], []
    rules = RULES[fmt]
    errors, warnings = [], [f"{fmt}: {n}" for n in rules.get("notes", [])]

    for entry, suggestions in decklist.resolve(conn, deck):
        hint = f" Você quis dizer: {'; '.join(suggestions)}?" if suggestions else ""
        errors.append(f"Carta não encontrada: {entry.name}.{hint}")
    known = [e for e in deck.entries() if e.card is not None]

    # Tamanho
    size = deck.count("main", "commander") if rules.get("commander") else deck.count("main")
    if "exact" in rules and size != rules["exact"]:
        errors.append(f"O deck precisa ter exatamente {rules['exact']} cartas "
                      f"(contando o comandante); tem {size}.")
    if "min_main" in rules and size < rules["min_main"]:
        errors.append(f"O deck principal precisa de pelo menos {rules['min_main']} cartas; tem {size}.")
    # O limite de sideboard é o mesmo em BO1 e BO3 (no Arena, BO1 também aceita até 15).
    max_side = rules.get("max_side")
    if max_side is not None and deck.count("sideboard") > max_side:
        errors.append(f"Sideboard com {deck.count('sideboard')} cartas; o máximo é {max_side}.")

    # Cópias (deck principal + sideboard + comandante)
    restricted = set()
    if rules.get("legality", True):
        status = dict(conn.execute(
            "SELECT oracle_id, status FROM legalities WHERE format = ?", (fmt,)).fetchall())
        if not status:
            errors.append(f"A base não tem legalidades para o formato {fmt}.")
        for entry in decklist.merged(known):
            card_status = status.get(entry.card["oracle_id"], "not_legal")
            if card_status == "banned":
                errors.append(f"{entry.card['name']} é banida em {fmt}.")
            elif card_status == "not_legal":
                errors.append(f"{entry.card['name']} não é legal em {fmt}.")
            elif card_status == "restricted":
                restricted.add(entry.card["oracle_id"])
    for entry in decklist.merged(known):
        limit = copy_limit(entry.card, rules.get("max_copies"))
        if entry.card["oracle_id"] in restricted:
            limit = 1
        if limit is not None and entry.qty > limit:
            reason = " (restrita)" if entry.card["oracle_id"] in restricted else ""
            errors.append(f"{entry.qty} cópias de {entry.card['name']}; o máximo é {limit}{reason}.")

    # Comandante e identidade de cor
    if rules.get("commander"):
        commanders = [e.card for e in deck.commander if e.card is not None]
        if not deck.commander:
            errors.append("Falta a seção Commander com o comandante do deck.")
        elif deck.count("commander") > 2:
            errors.append("Um deck pode ter no máximo dois comandantes.")
        if rules["commander"] is True:
            for card in commanders:
                if not can_be_commander(card, rules.get("planeswalker_commander", False)):
                    errors.append(f"{card['name']} não pode ser comandante em {fmt} "
                                  f"({_front(card, 'type_line')}).")
            if len(commanders) == 2 and not can_pair(*commanders):
                errors.append(f"{commanders[0]['name']} e {commanders[1]['name']} "
                              "não podem ser comandantes juntos (sem partner ou equivalente).")
        if commanders:
            identity = set("".join(c["color_identity"] for c in commanders))
            for entry in decklist.merged(known):
                extra = set(entry.card["color_identity"]) - identity
                if extra:
                    errors.append(f"{entry.card['name']} está fora da identidade de cor do "
                                  f"comandante ({''.join(sorted(identity)) or 'incolor'}): "
                                  f"tem {entry.card['color_identity']}.")

    # Disponibilidade na plataforma
    if game:
        for entry in decklist.merged(known):
            available = conn.execute(
                "SELECT 1 FROM printings WHERE oracle_id = ? AND instr(games, ?) > 0 LIMIT 1",
                (entry.card["oracle_id"], game),
            ).fetchone()
            if not available:
                errors.append(f"{entry.card['name']} não existe em {game}.")

    if deck.companion:
        warnings.append("A condição de construção do companion não é conferida.")
    return errors, warnings
