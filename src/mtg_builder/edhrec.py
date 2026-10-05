"""Dados de sinergia do EDHREC para um comandante, com cache local.

O EDHREC não tem API oficial; este módulo lê os mesmos arquivos JSON que as páginas
públicas do site carregam (json.edhrec.com), com cache de 7 dias e uma requisição por
página. Os dados refletem Commander de papel: toda carta é conferida na base local
contra o formato e a plataforma pedidos antes de ser sugerida.
"""

import json
import re
import unicodedata
import urllib.error
import urllib.request
from datetime import datetime, timedelta

from . import db, decklist, formats

BASE = "https://json.edhrec.com/pages"
USER_AGENT = "MTGDeckBuilder/0.1 (projeto pessoal; github.com/girocoju/mtg-deck-builder)"
MAX_AGE_DAYS = 7


def slug(name):
    """'Ivy, Gleeful Spellthief' → 'ivy-gleeful-spellthief' (só a face da frente)."""
    front = unicodedata.normalize("NFKD", name.split(" // ")[0])
    front = "".join(c for c in front if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", front.replace("'", "")).strip("-")


def _download(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def load(kind, commander_names, force=False, fetch=_download):
    """Página do EDHREC (`commanders` ou `average-decks`) para um ou dois comandantes.
    Devolve o JSON com `fetched_at` e `url`; usa o cache se tiver menos de 7 dias."""
    key = "-".join(slug(name) for name in commander_names)
    path = db.DATA_DIR / "edhrec" / kind / f"{key}.json"
    if path.exists() and not force:
        cached = json.loads(path.read_text("utf-8"))
        if datetime.now() - datetime.fromisoformat(cached["fetched_at"]) < timedelta(days=MAX_AGE_DAYS):
            return cached
    url = f"{BASE}/{kind}/{key}.json"
    try:
        data = fetch(url)
    except urllib.error.HTTPError as error:
        if error.code in (403, 404):
            raise RuntimeError(f"O EDHREC não tem página para '{' + '.join(commander_names)}' ({url}).") from error
        raise RuntimeError(f"Falha ao acessar {url}: {error}") from error
    except OSError as error:
        raise RuntimeError(f"Falha ao acessar {url}: {error}") from error
    data["fetched_at"] = datetime.now().isoformat(timespec="seconds")
    data["url"] = url
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


def _check(conn, index, name, fmt, game, identity):
    """Situação de uma carta do EDHREC no formato pedido: 'ok' ou o motivo da exclusão."""
    card = index.get(decklist._key(name))
    if card is None:
        return None, "fora da base"
    if identity is not None and not set(card["color_identity"]) <= identity:
        return card, "fora da identidade"
    if fmt:
        row = conn.execute("SELECT status FROM legalities WHERE oracle_id = ? AND format = ?",
                           (card["oracle_id"], fmt)).fetchone()
        if row is None or row[0] not in ("legal", "restricted"):
            return card, "banida" if row and row[0] == "banned" else "não legal"
    if game and not conn.execute(
            "SELECT 1 FROM printings WHERE oracle_id = ? AND instr(games, ?) > 0 LIMIT 1",
            (card["oracle_id"], game)).fetchone():
        return card, f"fora de {game}"
    return card, "ok"


def _commander_identity(index, commander_names):
    cards = [index.get(decklist._key(name)) for name in commander_names]
    if any(card is None for card in cards):
        return None
    return set("".join(card["color_identity"] for card in cards))


def recommendations(conn, commander_names, fmt=None, game=None, force=False, fetch=_download):
    """Cartas que o EDHREC associa ao comandante, com sinergia e inclusão, conferidas na base."""
    page = load("commanders", commander_names, force=force, fetch=fetch)
    index = decklist._name_index(conn)
    identity = _commander_identity(index, commander_names)
    info = page["container"]["json_dict"]
    cards, seen = [], set()
    for cardlist in info.get("cardlists", []):
        for view in cardlist.get("cardviews", []):
            if view["name"] in seen:
                continue
            seen.add(view["name"])
            card, status = _check(conn, index, view["name"], fmt, game, identity)
            potential = view.get("potential_decks") or 0
            cards.append({
                "name": card["name"] if card is not None else view["name"],
                "category": cardlist.get("header"),
                "synergy": round(view.get("synergy") or 0, 2),
                "inclusion": round(100 * view.get("num_decks", 0) / potential, 1) if potential else None,
                "status": status,
                "game_changer": bool(card["game_changer"]) if card is not None else False,
                "roles": analysis_roles(card) if card is not None else [],
            })
    return {
        "commander": info.get("card", {}).get("name") or " + ".join(commander_names),
        "decks": info.get("card", {}).get("num_decks"),
        "source": "edhrec", "url": page["url"], "fetched_at": page["fetched_at"],
        "format": fmt, "game": game,
        "average_types": {k: page.get(k) for k in
                          ("creature", "instant", "sorcery", "artifact", "enchantment", "planeswalker", "land")},
        "themes": [(t.get("value"), t.get("count")) for t in page.get("tag_counts", [])[:8]],
        "brackets": page.get("bracket_counts", {}),
        "cards": cards,
    }


def analysis_roles(card):
    from . import analysis  # import tardio: analysis não depende deste módulo
    return [r for r in analysis.roles(card) if r not in ("outros", "ameaça")]


def average_deck(conn, commander_names, fmt=None, game=None, force=False, fetch=_download):
    """Deck médio do EDHREC para o comandante: um modelo de partida, com cada carta
    marcada como utilizável ou não no formato/plataforma pedidos."""
    page = load("average-decks", commander_names, force=force, fetch=fetch)
    index = decklist._name_index(conn)
    identity = _commander_identity(index, commander_names)
    kept, dropped = [], []
    for card_type, entries in page["deck"]["cards"].items():
        for name, qty in entries:
            card, status = _check(conn, index, name, fmt, game, identity)
            item = {"qty": qty, "name": card["name"] if card is not None else name,
                    "type": card_type, "status": status}
            (kept if status == "ok" else dropped).append(item)
    return {
        "commander": page["deck"]["commander"], "source": "edhrec", "url": page["url"],
        "fetched_at": page["fetched_at"], "format": fmt, "game": game,
        "kept": kept, "dropped": dropped,
        "kept_count": sum(i["qty"] for i in kept), "dropped_count": sum(i["qty"] for i in dropped),
    }


def commander_report(conn, names, fmt):
    """Diz se a(s) carta(s) pode(m) comandar um deck no formato, e por quê."""
    fmt = fmt.lower()
    rules = formats.RULES.get(fmt)
    if not rules or not rules.get("commander"):
        return {"ok": False, "problems": [f"{fmt} não é um formato com comandante."], "identity": None}
    index = decklist._name_index(conn)
    cards, problems = [], []
    for name in names:
        card = index.get(decklist._key(name))
        if card is None:
            problems.append(f"Carta não encontrada: {name}.")
            continue
        cards.append(card)
        row = conn.execute("SELECT status FROM legalities WHERE oracle_id = ? AND format = ?",
                           (card["oracle_id"], fmt)).fetchone()
        if row is None:
            problems.append(f"{card['name']} não é legal em {fmt}.")
        elif row[0] == "banned":
            problems.append(f"{card['name']} é banida em {fmt}.")
        if rules["commander"] is True and not formats.can_be_commander(
                card, rules.get("planeswalker_commander", False)):
            problems.append(f"{card['name']} não pode ser comandante em {fmt}: é "
                            f"{card['type_line'].split(' // ')[0]}, e o formato exige criatura lendária"
                            + (" ou planeswalker lendário." if rules.get("planeswalker_commander") else "."))
    if len(cards) == 2 and not formats.can_pair(*cards):
        problems.append(f"{cards[0]['name']} e {cards[1]['name']} não podem ser comandantes juntos.")
    if len(names) > 2:
        problems.append("Um deck pode ter no máximo dois comandantes.")
    identity = "".join(c for c in "WUBRG" if any(c in card["color_identity"] for card in cards))
    return {"ok": not problems, "problems": problems, "identity": identity,
            "commanders": [card["name"] for card in cards],
            "deck_size": rules.get("exact"), "format": fmt}
