"""Montagem automática do deck de 40 a partir do pool (spec 010, requisito 6).

Pedido do usuário no fim do primeiro draft real (2026-11-09): "Insira a montagem do deck
no Oráculo também. Assim fica tudo concentrado no mesmo." O Oráculo chama `build()` quando
o draft termina e mostra a lista pronta para o Arena; `mtg draft build <estado>` faz o
mesmo pela linha de comando. O método é o da skill `draft`, seção C, e da teoria
(`knowledge/limitado-e-draft.md` §7; `knowledge/base-de-mana.md`, 40 cartas):

1. escolher o par de cores pela soma do poder das 23 melhores jogáveis (penalizando pares
   com menos de nove corpos);
2. admitir um splash de até três cartas de uma terceira cor, cada uma com um só símbolo
   dela, custo 3 ou mais e nota alta, com três ou quatro fontes para a cor;
3. 23 mágicas: corpos primeiro até doze (criaturas e geradores de ficha), depois as mais
   fortes; 17 terrenos (os não básicos do pool que produzem as cores entram primeiro,
   básicos divididos pelos símbolos de mana).

A proposta é um ponto de partida: a explicação diz o que ficou de fora e por quê.
"""

import re
from collections import Counter
from datetime import datetime
from pathlib import Path

from . import analysis, draft_pick

DECK_SIZE, SPELLS, MAX_LANDS = 40, 23, 18
MIN_BODIES = 12            # criaturas ou geradores de ficha entre as 23
MIN_INTERACTION = 4        # remoções e anulações entre as 23, quando o pool tem
MIN_BODIES_PAIR = 9        # abaixo disso o par é penalizado na escolha
BODY_PENALTY = 1.5
FILLER_POWER = -3.0        # nota de uma vaga sem jogável do par (enchimento ou 18º terreno)
SPLASH_MAX, SPLASH_MIN_POWER, SPLASH_MIN_CMC = 3, 2.0, 3
SPLASH_SOURCES = {1: 3, 2: 3, 3: 4}    # fontes fixas da cor do splash por número de cartas
MAX_NONBASIC = 3
DECKS_DIR = Path(__file__).resolve().parents[2] / "decks" / "limited"
COLOR_ORDER = "WUBRG"
BASIC = {"W": "Plains", "U": "Island", "B": "Swamp", "R": "Mountain", "G": "Forest"}
PAIRS = [a + b for i, a in enumerate(COLOR_ORDER) for b in COLOR_ORDER[i + 1:]]
TOKEN_MAKER = re.compile(r"create (a|an|two|three|x) [^.]*creature tokens?")
PRODUCES = re.compile(r"add (\{[wubrgc]\}(?:,? (?:or )?\{[wubrgc]\})*)")


def _pips(mana_cost):
    """Símbolos coloridos do custo: {G} conta 1 para G; híbrido {G/U} conta meio para cada."""
    pips = Counter()
    for token in re.findall(r"\{([^}]+)\}", mana_cost or ""):
        letters = [c for c in token.split("/") if c in COLOR_ORDER]
        for letter in letters:
            pips[letter] += 1.0 / len(letters)
    return pips


def _produces(card):
    text = (card["oracle_text"] or "").lower()
    if "mana of any color" in text or "mana of the chosen color" in text:
        return set(COLOR_ORDER), True
    colors = set()
    for group in PRODUCES.findall(text):
        colors |= {c.upper() for c in re.findall(r"\{([wubrg])\}", group)}
    return colors, False


def entry(engine, name):
    """Uma cópia de uma carta do pool com o que a montagem precisa; None se não está na base."""
    card = engine.card(name)
    if card is None:
        return None
    power = engine.ratings.power(name, card, engine.rarity(name))
    types = analysis._front(card, "type_line")
    text = (card["oracle_text"] or "").lower()
    produces, any_color = _produces(card) if analysis.is_land(card) else (set(), False)
    return {"name": card["name"], "card": card, "colors": draft_pick.card_colors(card), "cmc": card["cmc"] or 0.0,
            "power": round(power["points"], 2), "fonte": power["source"], "teorica": power["theoretical"],
            "land": analysis.is_land(card), "basic": "Basic" in types, "creature": "Creature" in types,
            "body": "Creature" in types or bool(TOKEN_MAKER.search(text)), "pips": _pips(card["mana_cost"]),
            "funcs": draft_pick.functions(card), "produces": produces, "any": any_color,
            "interaction": "remocao" in draft_pick.functions(card) or "anulação" in analysis.roles(card)}


def _playable(entries, colors):
    return [e for e in entries if not e["land"] and set(e["colors"]) <= set(colors)]


def evaluate_pair(entries, pair):
    """Soma do poder das 23 melhores jogáveis do par, com as vagas que faltam preenchidas por
    `FILLER_POWER` (o que uma carta de enchimento rende), menos a penalidade por corpos de menos."""
    playable = sorted(_playable(entries, pair), key=lambda e: -e["power"])
    top = playable[:SPELLS]
    bodies = sum(1 for e in top if e["body"])
    score = sum(e["power"] for e in top) + FILLER_POWER * (SPELLS - len(top))   # vaga sem jogável: carta de enchimento
    if bodies < MIN_BODIES_PAIR:
        score -= (MIN_BODIES_PAIR - bodies) * BODY_PENALTY
    return round(score, 2), playable


def splash_candidates(entries, pair):
    """Cartas de uma terceira cor que valem o splash: um símbolo da cor, custo 3+, nota alta.
    Devolve (cor, [cartas]) da cor com maior soma de poder, ou (None, [])."""
    by_color = {}
    for e in entries:
        if e["land"] or set(e["colors"]) <= set(pair):
            continue
        off = set(e["colors"]) - set(pair)
        if len(off) != 1:
            continue
        color = off.pop()
        if e["pips"].get(color, 0) > 1 or e["cmc"] < SPLASH_MIN_CMC or e["power"] < SPLASH_MIN_POWER:
            continue
        by_color.setdefault(color, []).append(e)
    if not by_color:
        return None, []
    color = max(by_color, key=lambda c: sum(e["power"] for e in by_color[c]))
    chosen = sorted(by_color[color], key=lambda e: -e["power"])[:SPLASH_MAX]
    return color, chosen


def choose_main(playable, splash):
    """23 mágicas: corpos primeiro até `MIN_BODIES`, interação (remoção e anulação) até
    `MIN_INTERACTION`, depois as mais fortes do que sobrou."""
    pool = sorted(playable + splash, key=lambda e: -e["power"])
    chosen, used = [], set()
    for e in pool:
        if e["body"] and len(chosen) < MIN_BODIES:
            chosen.append(e)
            used.add(id(e))
    interaction = 0
    for e in pool:
        if id(e) not in used and e.get("interaction") and interaction < MIN_INTERACTION and len(chosen) < SPELLS:
            chosen.append(e)
            used.add(id(e))
            interaction += 1
    for e in pool:
        if len(chosen) >= SPELLS:
            break
        if id(e) not in used:
            chosen.append(e)
            used.add(id(e))
    return chosen


def choose_lands(entries, main, pair, splash_color, total):
    """Não básicos do pool que produzem as cores do deck (até três), depois básicos: a cor
    do splash recebe o que falta para as fontes-alvo, o resto se divide pelos símbolos."""
    needed = set(pair) | ({splash_color} if splash_color else set())
    nonbasic = [e for e in entries if e["land"] and not e["basic"] and (e["any"] or e["produces"] & needed)]
    nonbasic.sort(key=lambda e: -(len(e["produces"] & needed) + (len(needed) if e["any"] else 0)))
    nonbasic = nonbasic[:min(MAX_NONBASIC, total)]
    sources = Counter()
    for e in nonbasic:
        for color in (needed if e["any"] else e["produces"] & needed):
            sources[color] += 1
    remaining = total - len(nonbasic)
    basics = Counter()
    if splash_color:
        count = sum(1 for e in main if splash_color in e["colors"] and not set(e["colors"]) <= set(pair))
        want = SPLASH_SOURCES.get(min(count, 3), 3) if count else 0
        basics[splash_color] = max(0, min(remaining, want - sources[splash_color]))
        remaining -= basics[splash_color]
    pips = Counter()
    for e in main:
        for color, n in e["pips"].items():
            if color in pair:
                pips[color] += n
    a, b = pair[0], pair[1]
    pa, pb = pips[a] or 0.5, pips[b] or 0.5
    na = round(remaining * pa / (pa + pb))
    floor = min(6, remaining // 2)
    na = max(floor, min(remaining - floor, na))
    basics[a] += na
    basics[b] += remaining - na
    for color in needed:
        sources[color] += basics[color]
    return nonbasic, basics, sources


def build(engine, pool, size=DECK_SIZE):
    """Monta o deck a partir dos nomes do pool. Devolve dicionário com par, splash, listas
    (principal, terrenos, reserva), estatísticas e razões em texto."""
    entries, unknown = [], []
    for name in pool:
        e = entry(engine, name)
        if e is None:
            unknown.append(name)
        elif not e["basic"]:               # básicos são livres na montagem
            entries.append(e)
    present = {c for e in entries for c in e["colors"]}
    scored = [(evaluate_pair(entries, pair), pair) for pair in PAIRS if set(pair) & present]
    if not scored:
        scored = [(evaluate_pair(entries, "WU"), "WU")]
    scored.sort(key=lambda item: (-item[0][0], item[1]))
    (score, playable), pair = scored[0]
    splash_color, splash = splash_candidates(entries, pair)
    main = choose_main(playable, splash)
    splash_in = [e for e in main if splash_color and splash_color in e["colors"] and not set(e["colors"]) <= set(pair)]
    if not splash_in:
        splash_color = None
    fill = []
    if len(main) < size - MAX_LANDS:              # pool curto: fecha 22 mágicas com o melhor que houver, fora das cores
        used_ids = {id(e) for e in main}
        extras = sorted((e for e in entries if not e["land"] and id(e) not in used_ids), key=lambda e: -e["power"])
        fill = extras[:size - MAX_LANDS - len(main)]
        main = main + fill
    lands_total = max(min(size - len(main), MAX_LANDS), 0)
    nonbasic, basics, sources = choose_lands(entries, main, pair, splash_color, lands_total)
    used = {id(e) for e in main} | {id(e) for e in nonbasic}
    side = [e for e in entries if id(e) not in used]
    main_counts = Counter(e["name"] for e in main)
    land_counts = Counter(e["name"] for e in nonbasic)
    for color in COLOR_ORDER:
        if basics[color]:
            land_counts[BASIC[color]] += basics[color]
    bodies = sum(1 for e in main if e["body"])
    removal = sum(1 for e in main if e.get("interaction"))
    avg = round(sum(e["cmc"] for e in main) / len(main), 2) if main else 0.0
    runner_up = scored[1] if len(scored) > 1 else None
    reasons = [f"Par {pair}: soma de poder das jogáveis {score:+.1f}"
               + (f", contra {runner_up[1]} {runner_up[0][0]:+.1f}" if runner_up else "")
               + f"; {len(playable)} jogáveis no par."]
    if splash_color:
        reasons.append(f"Splash {splash_color} para " + ", ".join(f"{e['name']} ({e['power']:+.1f})" for e in splash_in)
                       + f": um símbolo cada, {sources[splash_color]} fontes.")
    reasons.append(f"{len(main)} mágicas ({bodies} corpos, {removal} de interação, custo médio {avg:.2f}) e "
                   f"{sum(land_counts.values())} terrenos; fontes: "
                   + ", ".join(f"{c} {sources[c]}" for c in COLOR_ORDER if sources[c]) + ".")
    left = sorted(side, key=lambda e: -e["power"])
    out_strong = [e for e in left if e["power"] >= 1.0 and not e["land"]][:6]
    if out_strong:
        reasons.append("Fora, por cor ou por vaga: " + ", ".join(f"{e['name']} ({e['colors'] or '-'}, {e['power']:+.1f})"
                                                                for e in out_strong) + ".")
    if fill:
        reasons.append("Enchimento fora das cores, por falta de jogáveis: " + ", ".join(f"{e['name']} ({e['colors'] or '-'})" for e in fill) + ".")
    if unknown:
        reasons.append("Não encontradas na base: " + ", ".join(sorted(set(unknown))) + ".")
    return {"pair": pair, "splash": splash_color, "splash_cards": [e["name"] for e in splash_in],
            "main": sorted(main_counts.items(), key=lambda kv: (-_cmc_of(main, kv[0]), kv[0])),
            "lands": sorted(land_counts.items(), key=lambda kv: (kv[0] in BASIC.values(), kv[0])),
            "sideboard": sorted(Counter(e["name"] for e in side).items()),
            "stats": {"magicas": len(main), "corpos": bodies, "remocao": removal, "cmc_medio": avg,
                      "terrenos": sum(land_counts.values()), "fontes": {c: sources[c] for c in COLOR_ORDER if sources[c]},
                      "jogaveis_no_par": len(playable), "nota_par": score},
            "reasons": reasons, "unknown": unknown, "size": sum(main_counts.values()) + sum(land_counts.values())}


def _cmc_of(entries, name):
    return next((e["cmc"] for e in entries if e["name"] == name), 0)


def arena_lines(result):
    """Lista no formato do Arena (só a face da frente)."""
    lines = ["Deck"]
    for name, qty in result["main"]:
        lines.append(f"{qty} {name.split(' // ')[0]}")
    for name, qty in result["lands"]:
        lines.append(f"{qty} {name.split(' // ')[0]}")
    return lines


def summary_lines(result):
    """Texto curto para a janela do Oráculo e para o terminal."""
    label = result["pair"] + (f" + splash {result['splash']}" if result["splash"] else "")
    s = result["stats"]
    lines = [f"DECK PROPOSTO: {label} · {s['magicas']} mágicas, {s['terrenos']} terrenos · {s['corpos']} corpos, "
             f"{s['remocao']} de interação, custo médio {s['cmc_medio']:.2f}", ""]
    lines += arena_lines(result)
    lines.append("")
    lines += [f"• {r}" for r in result["reasons"]]
    return lines


def deck_path(set_code, event=None, result=None, day=None):
    day = day or datetime.now().strftime("%Y-%m-%d")
    tag = (event or "draft").lower().replace("_", "-")
    colors = (result["pair"].lower() + (f"-splash-{result['splash'].lower()}" if result["splash"] else "")) if result else ""
    stem = "-".join(part for part in (set_code.lower(), tag, day, colors) if part)
    path = DECKS_DIR / f"{stem}.md"
    n = 2
    while path.exists():
        path = DECKS_DIR / f"{stem}-{n}.md"
        n += 1
    return path


def markdown(result, set_name, set_code, event=None, sources="", pool_path=None):
    """Arquivo do deck na convenção de decks/README.md: lista exportável e explicação."""
    label = result["pair"] + (f" com splash {result['splash']}" if result["splash"] else "")
    s = result["stats"]
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [f"# {set_name} — deck de 40 montado pelo Oráculo ({label})", "",
             f"- **Formato:** limited (40 cartas) · **Coleção:** {set_code.upper()}"
             + (f" · **Evento:** {event}" if event else "") + f" · **Data:** {today}",
             f"- **Dados:** {sources or 'sem dados de partidas (notas teóricas)'}",
             f"- **Origem do pool:** {pool_path or 'pool informado'}; montagem automática (`draft_deck.py`, método da skill "
             "`draft`, seção C). Proposta a revisar: confira com `mtg deck analyze` e ajuste pela curva e pelas partidas.",
             "", "```"] + arena_lines(result) + ["```", "", "## Por quê", ""]
    lines += [f"- {r}" for r in result["reasons"]]
    lines += ["", "## Reserva (o que ficou de fora)", "",
              ", ".join(f"{qty} {name}" for name, qty in result["sideboard"]) or "nada", "",
              "## Limites", "",
              "- A escolha do par soma o poder das jogáveis; não vê sinergias finas nem a curva turno a turno.",
              "- Splash só com um símbolo da cor e custo 3 ou mais; fontes pela tabela de 40 cartas (`knowledge/base-de-mana.md`).",
              "- Rode `mtg deck validate <arquivo> --format limited` e `mtg deck analyze <arquivo>`; o alerta de cor do splash é esperado."]
    return "\n".join(lines) + "\n"


def write(result, set_name, set_code, event=None, sources="", pool_path=None, path=None):
    path = Path(path or deck_path(set_code, event, result))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown(result, set_name, set_code, event, sources, pool_path), encoding="utf-8")
    return path
