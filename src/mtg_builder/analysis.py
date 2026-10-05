"""Análise numérica de uma decklist: curva, base de mana, papéis e probabilidades.

Fórmulas e tabelas de Frank Karsten, registradas em knowledge/base-de-mana.md (Parte 2).
A classificação por papel e a contagem de fontes são heurísticas sobre o texto das
cartas: servem de ponto de partida e podem ser corrigidas por quem lê o relatório.
"""

import json
import re
from math import comb

from . import decklist

WUBRG = "WUBRG"
BASIC_TYPES = {"Plains": "W", "Island": "U", "Swamp": "B", "Mountain": "R", "Forest": "G"}

# Fontes mínimas por custo colorido (Karsten 2022), para decks de 40 / 60 / 80 / 99 cartas.
SOURCES = {
    "C": (9, 14, 19, 19), "1C": (9, 13, 18, 19), "2C": (8, 12, 16, 18), "3C": (7, 10, 15, 16),
    "4C": (6, 9, 14, 15), "5C": (6, 9, 12, 14),
    "CC": (14, 21, 28, 30), "1CC": (12, 18, 25, 28), "2CC": (11, 16, 23, 26),
    "3CC": (10, 15, 20, 23), "4CC": (9, 13, 19, 22), "5CC": (8, 12, 17, 20),
    "CCC": (16, 23, 32, 36), "1CCC": (14, 21, 29, 33), "2CCC": (13, 19, 26, 30),
    "3CCC": (11, 17, 24, 28), "4CCC": (10, 16, 22, 26),
    "CCCC": (17, 24, 34, 39), "1CCCC": (15, 22, 31, 36),
}
SIZES = (40, 60, 80, 99)

ROLES = {
    "remoção pontual": r"(destroy|exile) (up to \w+ )?(other )?target (?!land)|deals? \w+ damage to "
                       r"(any target|target creature|up to)|target creature gets -|fights? |"
                       r"return target (nonland permanent|creature)[^.]* to its owner's hand",
    "remoção em massa": r"(destroy|exile) (all|each) (?!graveyards)|all creatures get -|"
                        r"deals? \w+ damage to each (creature|opponent's creature)|each creature gets -",
    "anulação": r"counter target",
    "compra de cartas": r"draws? (a|two|three|four|x|that many) cards?|draw cards equal",
    "aceleração": r"add (\{|one mana|two mana|x mana|an amount)|search your library for (a|an|up to \w+) "
                  r"(basic )?(land|forest|plains|island|swamp|mountain)|create (a|two|x) treasure",
    "proteção": r"gains? (hexproof|indestructible|protection|ward)|phases? out|can't be countered",
    "tutor": r"search your library for (a|an|up to \w+) (?!basic|land|forest|plains|island|swamp|mountain)",
    "recursão": r"return (target|up to \w+ target|a|all) [^.]*from your graveyard",
}


def hypergeom_at_least(population, successes, draws, k=1):
    """P(pelo menos k sucessos em `draws` cartas de um deck de `population` com `successes` cópias)."""
    draws = min(draws, population)
    total = comb(population, draws)
    below = sum(comb(successes, i) * comb(population - successes, draws - i) for i in range(k))
    return 1 - below / total


def cards_seen(turn, on_the_play=True):
    """Cartas vistas até o turno (mão de 7, sem mulligan)."""
    return 7 + turn - (1 if on_the_play else 0)


def hand_land_distribution(deck, lands, hand=7):
    """P(k terrenos) em uma mão de `hand` cartas, sorteio puro. Lista indexada por k."""
    total = comb(deck, hand)
    return [comb(lands, k) * comb(deck - lands, hand - k) / total for k in range(hand + 1)]


def smoothed_land_distribution(deck, lands, hands=2, hand=7):
    """Modelo da mão inicial em BO1 no Arena: sorteia `hands` mãos e fica com a de
    quantidade de terrenos mais próxima da média do deck. O Arena só "tende" a escolher
    a mais próxima (o peso exato não é público), então isto é o LIMITE SUPERIOR do efeito."""
    raw = hand_land_distribution(deck, lands, hand)
    target = hand * lands / deck
    groups = {}
    for k in range(hand + 1):
        groups.setdefault(round(abs(k - target), 9), []).append(k)
    result, worse_or_equal = [0.0] * (hand + 1), 1.0
    for distance in sorted(groups):  # da mais próxima para a mais distante
        group_p = sum(raw[k] for k in groups[distance])
        worse = worse_or_equal - group_p
        chosen = worse_or_equal ** hands - max(worse, 0.0) ** hands
        for k in groups[distance]:
            result[k] = chosen * raw[k] / group_p if group_p else 0.0
        worse_or_equal = worse
    return result


def _front(card, key):
    return (card[key] or "").split(" // ")[0]


def is_land(card):
    return "Land" in _front(card, "type_line")


def _faces(card):
    return json.loads(card["faces"]) if card["faces"] else []


def mdfc_land_fraction(card):
    """MDFC mágica/terreno: 0,38 terreno se o terreno entra virado, 0,74 se pode entrar desvirado."""
    faces = _faces(card)
    if card["layout"] != "modal_dfc" or len(faces) < 2 or is_land(card):
        return 0.0
    if "Land" not in faces[1].get("type_line", ""):
        return 0.0
    return 0.38 if re.search(r"enters tapped\.", faces[1].get("oracle_text", "")) else 0.74


def cost_parts(card):
    """Custos de mana da carta, um por metade (split) ou só o da frente (demais)."""
    cost = card["mana_cost"] or ""
    if card["layout"] == "split" and card["faces"]:
        return [f.get("mana_cost", "") for f in _faces(card) if f.get("mana_cost")]
    return [cost.split(" // ")[0]] if cost else []


def requirement_key(cost, color):
    """Custo no formato da tabela ("1CC") visto da cor dada. X vale zero; símbolos
    híbridos e Phyrexian contam como mana genérica (não exigem a cor)."""
    symbols = re.findall(r"\{([^}]+)\}", cost)
    pips = symbols.count(color)
    if not pips:
        return None, 0
    total = sum(int(s) if s.isdigit() else 0 if s in "XYZ" else 1 for s in symbols)
    generic = total - pips
    return (str(generic) if generic else "") + "C" * pips, total


def sources_needed(key, size):
    """Fontes exigidas pela tabela; custos fora dela usam o vizinho mais exigente."""
    column = SIZES.index(size)
    if key in SOURCES:
        return SOURCES[key][column], False
    pips = min(key.count("C"), 4)
    generic = int(key.rstrip("C") or 0)
    known = sorted(int(k.rstrip("C") or 0) for k in SOURCES if k.count("C") == pips)
    nearest = max((g for g in known if g <= generic), default=known[0])
    return SOURCES[(str(nearest) if nearest else "") + "C" * pips][column], True


def land_colors(card, deck_colors):
    produced = set(card["produced_mana"] or "") & set(WUBRG)
    if produced:
        return produced
    text = card["oracle_text"] or ""
    if "search your library" in text.lower():
        found = {c for name, c in BASIC_TYPES.items() if name in text}
        return found or (set(deck_colors) if "basic land" in text else set())
    return set()


def enters_tapped(card):
    text = card["oracle_text"] or ""
    return bool(re.search(r"enters tapped\.", text)) and "unless" not in text and "you may" not in text


def roles(card):
    if is_land(card):
        return ["terreno"]
    text = (card["oracle_text"] or "").lower()
    found = [role for role, pattern in ROLES.items() if re.search(pattern, text)]
    types = _front(card, "type_line")
    if "Creature" in types or "Planeswalker" in types:
        found.append("ameaça")
    return found or ["outros"]


def is_cheap_draw_or_ramp(card):
    """Definição de Karsten para a fórmula de terrenos: não-terreno de valor de mana ≤ 2
    que compra carta ou gera mana/busca terreno."""
    if is_land(card) or (card["cmc"] or 0) > 2:
        return False
    text = (card["oracle_text"] or "").lower()
    draws = re.search(ROLES["compra de cartas"], text)
    if draws and ("Creature" not in _front(card, "type_line") or "enters" in text):
        return True
    return bool(re.search(ROLES["aceleração"], text)) and "treasure" not in text


def size_class(cards):
    return 40 if cards <= 45 else 60 if cards <= 70 else 80 if cards <= 90 else 99


def recommended_lands(size, avg_mv, cheap, companion=False):
    """Fórmulas de Karsten (2022). Para 40 cartas não há fórmula publicada: 17 é o padrão."""
    if size == 60:
        return 19.59 + 1.90 * avg_mv - 0.28 * cheap + (0.27 if companion else 0)
    if size == 80:
        return 80 / 60 * (19.59 + 1.90 * avg_mv + 0.27) - 0.28 * cheap
    if size == 99:
        return 31.42 + 3.13 * avg_mv - 0.28 * cheap
    return 17.0


def analyze(deck):
    """Analisa um deck já resolvido (decklist.resolve). Devolve um dicionário serializável."""
    main = [e for e in decklist.merged(deck.main) if e.card is not None]
    commanders = [e for e in decklist.merged(deck.commander) if e.card is not None]
    total = sum(e.qty for e in main) + sum(e.qty for e in commanders)
    size = size_class(total)
    spells = [e for e in main if not is_land(e.card)]
    lands = [e for e in main if is_land(e.card)]

    # Curva e valor de mana médio (comandante fora: ele não é comprado)
    curve = {str(i) if i < 7 else "7+": {"criaturas": 0, "outras": 0} for i in range(8)}
    for e in spells:
        bucket = min(int(e.card["cmc"] or 0), 7)
        kind = "criaturas" if "Creature" in _front(e.card, "type_line") else "outras"
        curve[str(bucket) if bucket < 7 else "7+"][kind] += e.qty
    n_spells = sum(e.qty for e in spells)
    avg_mv = sum((e.card["cmc"] or 0) * e.qty for e in spells) / n_spells if n_spells else 0.0

    # Terrenos
    land_cards = sum(e.qty for e in lands)
    land_count = land_cards + sum(mdfc_land_fraction(e.card) * e.qty for e in spells)
    cheap = sum(e.qty for e in spells if is_cheap_draw_or_ramp(e.card))
    target = recommended_lands(size, avg_mv, cheap, bool(deck.companion))
    tapped = sum(e.qty for e in lands if enters_tapped(e.card))

    # Cores: exigência (carta mais exigente) e fontes
    deck_colors = [c for c in WUBRG if any(c in (e.card["color_identity"] or "")
                                           for e in main + commanders)]
    colors = {}
    for color in deck_colors:
        pips, worst = 0, None
        for e in spells + commanders:
            for cost in cost_parts(e.card):
                key, mv = requirement_key(cost, color)
                if not key:
                    continue
                pips += key.count("C") * e.qty
                needed, approx = sources_needed(key, size)
                if len(set(re.findall(r"\{([WUBRG])\}", cost))) > 1:
                    needed += 1  # cartas de ouro: +1 em cada requisito
                if worst is None or needed > worst["fontes_necessarias"]:
                    worst = {"carta": e.card["name"], "custo": cost, "chave": key, "valor_de_mana": mv,
                             "fontes_necessarias": needed, "aproximado": approx}
        from_lands = sum(e.qty for e in lands if color in land_colors(e.card, deck_colors))
        untapped = sum(e.qty for e in lands
                       if color in land_colors(e.card, deck_colors) and not enters_tapped(e.card))
        mdfc = sum(0.8 * e.qty for e in spells
                   if mdfc_land_fraction(e.card) and color in (e.card["produced_mana"] or ""))
        extra = 0.0  # dorks 1/2 e pedras de mana 3/4, de custo ≤ 2: só valem para mágicas de custo ≥ 3
        for e in spells:
            if (e.card["cmc"] or 0) <= 2 and color in (e.card["produced_mana"] or "") \
                    and not mdfc_land_fraction(e.card):
                extra += e.qty * (0.5 if "Creature" in _front(e.card, "type_line") else 0.75)
        colors[color] = {
            "simbolos": pips, "exigencia": worst,
            "fontes_terrenos": round(from_lands + mdfc, 1), "fontes_desviradas": untapped,
            "fontes_extras": round(extra, 2),
        }

    # Papéis
    role_cards = {}
    for e in main:
        for role in roles(e.card):
            role_cards.setdefault(role, []).append((e.qty, e.card["name"]))
    role_counts = {role: sum(q for q, _ in cards) for role, cards in role_cards.items()}

    # Probabilidades (hipergeométrica, mão de 7 sem mulligan, jogando primeiro)
    deck_cards = sum(e.qty for e in main)
    n_lands = round(land_count)
    odds = {
        "mao_inicial_2_a_4_terrenos": sum(
            comb(n_lands, k) * comb(deck_cards - n_lands, 7 - k) for k in (2, 3, 4)
        ) / comb(deck_cards, 7) if deck_cards >= 7 else None,
        "terrenos_no_turno": {
            str(t): hypergeom_at_least(deck_cards, n_lands, cards_seen(t), t) for t in (2, 3, 4, 5)
        } if deck_cards >= 12 else {},
    }
    if size == 60 and deck_cards >= 7:
        # Só construído de 60 tem fila BO1 com suavização de mão no Arena.
        smoothed = smoothed_land_distribution(deck_cards, n_lands)
        odds["mao_inicial_bo1_2_a_4_terrenos_ate"] = sum(smoothed[2:5])

    # Alertas
    alerts = []
    diff = land_count - target
    if size == 40:
        if not 16 <= land_count <= 18:
            alerts.append(f"Terrenos: {land_count:g} em deck de 40; o padrão é 17 (16 a 18).")
    elif abs(diff) > 2:
        alerts.append(f"Terrenos: a lista tem {land_count:g} e a fórmula sugere {target:.1f} "
                      f"({'faltam' if diff < 0 else 'sobram'} {abs(diff):.1f}). "
                      "Diferença acima de 2 pede justificativa.")
    for color, info in colors.items():
        need = info["exigencia"]
        if not need:
            continue
        have = info["fontes_terrenos"] + (info["fontes_extras"] if need["valor_de_mana"] >= 3 else 0)
        if have < need["fontes_necessarias"]:
            alerts.append(
                f"Cor {color}: {need['fontes_necessarias']} fontes recomendadas para {need['carta']} "
                f"({need['custo']}); a lista tem {have:g}.")
        one_drops = [e for e in spells if (e.card["cmc"] or 0) == 1 and color in (e.card["mana_cost"] or "")]
        first_turn = sources_needed("C", size)[0]
        if sum(e.qty for e in one_drops) >= 4 and info["fontes_desviradas"] < first_turn:
            alerts.append(f"Cor {color}: mágicas de 1 mana pedem {first_turn} fontes desviradas; "
                          f"a lista tem {info['fontes_desviradas']}.")
    tapped_limit = {40: 6, 60: 9, 80: 12, 99: 15}[size]
    if tapped > tapped_limit:
        alerts.append(f"{tapped} terrenos entram virados; acima de ~{tapped_limit} a base fica lenta.")

    return {
        "cartas": total, "tamanho_de_referencia": size,
        "magicas": n_spells, "valor_de_mana_medio": round(avg_mv, 2),
        "terrenos": round(land_count, 2), "cartas_de_terreno": land_cards,
        "terrenos_virados": tapped, "compra_ou_ramp_barato": cheap,
        "terrenos_recomendados": round(target, 1),
        "curva": curve, "cores": colors,
        "papeis": role_counts, "cartas_por_papel": role_cards,
        "probabilidades": odds, "alertas": alerts,
    }


def report(data):
    """Relatório em texto do resultado de analyze()."""
    lines = [
        f"{data['cartas']} cartas (referência: deck de {data['tamanho_de_referencia']}) | "
        f"{data['magicas']} mágicas, valor de mana médio {data['valor_de_mana_medio']:.2f}",
        f"Terrenos: {data['terrenos']:g} (recomendado {data['terrenos_recomendados']:.1f}; "
        f"{data['compra_ou_ramp_barato']} mágicas baratas de compra/ramp; "
        f"{data['terrenos_virados']} entram virados)",
        "", "Curva (criaturas + outras):",
    ]
    for mv, row in data["curva"].items():
        count = row["criaturas"] + row["outras"]
        lines.append(f"  {mv:>2}: {'#' * count:<24} {count:>2}  ({row['criaturas']} + {row['outras']})")
    lines += ["", "Cores:"]
    for color, info in data["cores"].items():
        need = info["exigencia"]
        demand = (f"pede {need['fontes_necessarias']} por {need['carta']} ({need['custo']})"
                  + (" [aprox.]" if need["aproximado"] else "")) if need else "sem exigência"
        lines.append(f"  {color}: {info['simbolos']} símbolos | {info['fontes_terrenos']:g} fontes "
                     f"({info['fontes_desviradas']} desviradas, +{info['fontes_extras']:g} não-terreno) | {demand}")
    lines += ["", "Papéis (uma carta pode ter mais de um):"]
    lines += [f"  {role}: {count}" for role, count in sorted(data["papeis"].items(), key=lambda x: -x[1])]
    odds = data["probabilidades"]
    if odds["terrenos_no_turno"]:
        lines += ["", "Probabilidades (mão de 7, sem mulligan, jogando primeiro):",
                  f"  mão inicial com 2 a 4 terrenos: {odds['mao_inicial_2_a_4_terrenos']:.1%}"
                  + (f" (em BO1 no Arena: até {odds['mao_inicial_bo1_2_a_4_terrenos_ate']:.1%}, "
                     "pela suavização de mão)" if "mao_inicial_bo1_2_a_4_terrenos_ate" in odds else ""),
                  "  " + " | ".join(f"{t} terrenos no turno {t}: {p:.1%}"
                                    for t, p in odds["terrenos_no_turno"].items())]
    lines += ["", "Alertas:"] + ([f"  ! {a}" for a in data["alertas"]] or ["  nenhum"])
    return "\n".join(lines)
