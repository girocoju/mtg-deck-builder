"""Snapshots de metagame de construído.

Coleta automática: MTGGoldfish (resultados de torneios de MTGO e papel, ou seja, BO3).
Importação manual: qualquer fonte, em CSV — é o caminho para o meta BO1 do Arena
(ex.: Untapped.gg), que não tem coleta automática.

Cada snapshot é um JSON em data/meta/<formato>/<modo>/<data>-<fonte>.json e nunca é
sobrescrito por outro dia: o histórico fica para comparar a evolução.
"""

import csv
import html
import json
import re
import time
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

from . import analysis, db, decklist

GOLDFISH = "https://www.mtggoldfish.com"
USER_AGENT = "MTGDeckBuilder/0.1 (projeto pessoal; github.com/girocoju/mtg-deck-builder)"
# formato (chave do Scryfall) → caminho no MTGGoldfish
GOLDFISH_FORMATS = {
    "standard": "standard", "pioneer": "pioneer", "modern": "modern", "legacy": "legacy",
    "vintage": "vintage", "pauper": "pauper", "historic": "historic", "timeless": "timeless",
    "alchemy": "alchemy", "explorer": "explorer", "premodern": "premodern", "penny": "penny_dreadful",
}
MODES = ("bo1", "bo3")
REQUEST_DELAY = 2.0
MAX_AGE_HOURS = 24
STALE_DAYS = 14

MACRO_BY_NAME = (
    ("control", "controle"), ("combo", "combo"), ("storm", "combo"), ("reanimator", "combo"),
    ("midrange", "midrange"), ("aggro", "aggro"), ("burn", "aggro"), ("prowess", "aggro"),
    ("ramp", "ramp"), ("landfall", "ramp"), ("tempo", "tempo"), ("delver", "tempo"),
)


def meta_dir(fmt, mode):
    return db.DATA_DIR / "meta" / fmt / mode


def _get(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_goldfish_metagame(page):
    """Arquétipos da página /metagame/<formato>/full."""
    archetypes = []
    for tile in re.split(r"<div class='archetype-tile' id='", page)[1:]:
        link = re.search(r'<a href="(/archetype/[^"#]+)#paper">([^<]+)</a>', tile)
        share = re.search(
            r"metagame-percentage.*?archetype-tile-statistic-value'>\s*([\d.]+)%.*?\((\d+)\)", tile, re.S)
        if not link or not share:
            continue
        colors = re.search(r"aria-label='colors: ([^']*)'", tile)
        archetypes.append({
            "name": html.unescape(link[2]).strip(),
            "share": float(share[1]),
            "decks": int(share[2]),
            "colors": colors[1] if colors else "",
            "key_cards": [html.unescape(c) for c in re.findall(r"<li>([^<]+)</li>", tile)],
            "url": GOLDFISH + link[1],
        })
    return archetypes


def parse_goldfish_deck(page):
    """Decklist de referência de uma página de arquétipo (campo oculto do formulário)."""
    match = re.search(r'id="deck_input_deck" value="([^"]*)"', page)
    return html.unescape(match[1]).strip() if match else None


def latest(fmt, mode, source=None):
    """Snapshot mais recente do formato/modo (opcionalmente de uma fonte), ou None."""
    files = sorted(meta_dir(fmt, mode).glob(f"*-{source or '*'}.json"))
    if not files:
        return None
    snapshot = json.loads(files[-1].read_text("utf-8"))
    snapshot["file"] = str(files[-1])
    return snapshot


def age_days(snapshot):
    return (datetime.now() - datetime.fromisoformat(snapshot["collected_at"])).days


def save(snapshot):
    folder = meta_dir(snapshot["format"], snapshot["mode"])
    folder.mkdir(parents=True, exist_ok=True)
    day = snapshot["collected_at"][:10]
    path = folder / f"{day}-{snapshot['source']}.json"
    path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=1), encoding="utf-8")
    return path


def _enrich(conn, archetype, deck_text):
    """Confere a lista com a base e anexa números da análise ao arquétipo."""
    deck = decklist.parse(deck_text)
    unknown = decklist.resolve(conn, deck)
    data = analysis.analyze(deck)
    archetype["deck"] = deck_text
    archetype["unknown_cards"] = [entry.name for entry, _ in unknown]
    archetype["stats"] = {
        "avg_mv": data["valor_de_mana_medio"], "lands": data["terrenos"],
        "creatures": sum(row["criaturas"] for row in data["curva"].values()),
        "roles": data["papeis"],
    }
    archetype["macro"] = guess_macro(archetype["name"], archetype["stats"])


def guess_macro(name, stats):
    """Macroarquétipo aproximado: pelo nome quando ele diz, senão pela curva. Heurística."""
    lowered = name.lower()
    for word, macro in MACRO_BY_NAME:
        if word in lowered:
            return macro
    if stats["creatures"] <= 10:
        return "controle"
    if stats["avg_mv"] <= 2.2 and stats["creatures"] >= 14:
        return "aggro"
    return "midrange"


def update_goldfish(conn, fmt, top=12, force=False, log=print, fetch=_get, delay=REQUEST_DELAY):
    """Coleta o meta do formato no MTGGoldfish e salva um snapshot BO3.

    Não repete a coleta se já existe snapshot com menos de 24 h (a não ser com `force`).
    Em caso de falha de rede ou de layout, levanta RuntimeError e o snapshot anterior
    continua valendo.
    """
    if fmt not in GOLDFISH_FORMATS:
        raise RuntimeError(f"Formato sem coleta no MTGGoldfish: {fmt}. "
                           f"Disponíveis: {', '.join(sorted(GOLDFISH_FORMATS))}")
    previous = latest(fmt, "bo3", "mtggoldfish")
    if previous and not force:
        age = datetime.now() - datetime.fromisoformat(previous["collected_at"])
        if age < timedelta(hours=MAX_AGE_HOURS):
            log(f"{fmt}: snapshot de {previous['collected_at'][:16]} ainda é recente; nada a fazer.")
            return previous

    url = f"{GOLDFISH}/metagame/{GOLDFISH_FORMATS[fmt]}/full"
    try:
        archetypes = parse_goldfish_metagame(fetch(url))
    except OSError as error:
        raise RuntimeError(f"Falha ao acessar {url}: {error}") from error
    if not archetypes:
        raise RuntimeError(f"Nenhum arquétipo encontrado em {url}: o layout da página pode ter mudado.")

    log(f"{fmt}: {len(archetypes)} arquétipos; baixando as {min(top, len(archetypes))} listas principais...")
    for archetype in archetypes[:top]:
        time.sleep(delay)
        try:
            deck_text = parse_goldfish_deck(fetch(archetype["url"]))
        except OSError as error:
            log(f"  {archetype['name']}: falha ao baixar a lista ({error})")
            continue
        if deck_text:
            _enrich(conn, archetype, deck_text)

    snapshot = {
        "source": "mtggoldfish", "url": url, "format": fmt, "mode": "bo3",
        "collected_at": datetime.now().isoformat(timespec="seconds"),
        "note": "Resultados de torneios (MTGO e papel), jogados em melhor-de-três.",
        "archetypes": archetypes,
    }
    path = save(snapshot)
    snapshot["file"] = str(path)
    log(f"{fmt}: snapshot salvo em {path}")
    return snapshot


def _key_cards(index, archetype, text):
    """Cartas mais usadas do arquétipo: `Nome 99.8; Outro Nome 86` (o número, opcional, é
    a porcentagem das listas que usam a carta). Nomes fora da base ficam à parte."""
    cards, unknown = [], []
    for item in text.split(";"):
        match = re.match(r"\s*(.+?)(?:\s+([\d.,]+)%?)?\s*$", item)
        if not match or not match[1]:
            continue
        card = index.get(decklist._key(match[1]))
        if card is None:
            unknown.append(match[1])
            continue
        cards.append({"name": card["name"],
                      "inclusion": float(match[2].replace(",", ".")) if match[2] else None})
    archetype["key_cards"] = cards
    if unknown:
        archetype["unknown_cards"] = unknown


def import_csv(conn, csv_path, fmt, mode, source, decks_dir=None, url=None, collected=None, note=None):
    """Importa um meta de qualquer fonte a partir de um CSV com colunas
    `archetype,share[,winrate][,games][,tier][,minutes][,key_cards]` (percentuais com ou
    sem %). `key_cards` é uma lista `Nome 99.8; Nome 86`, conferida com a base. Se
    `decks_dir` for dado, `<nome do arquétipo>.txt` nessa pasta vira a lista de referência."""
    if mode not in MODES:
        raise RuntimeError(f"Modo inválido: {mode}. Use bo1 ou bo3.")
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or "archetype" not in rows[0] or "share" not in rows[0]:
        raise RuntimeError("O CSV precisa das colunas 'archetype' e 'share'.")

    def number(value):
        value = (value or "").replace("%", "").replace(",", ".").strip()
        return float(value) if value else None

    index = decklist._name_index(conn)
    archetypes = []
    for row in rows:
        archetype = {"name": row["archetype"].strip(), "share": number(row["share"])}
        for key in ("winrate", "games", "minutes"):
            if number(row.get(key)) is not None:
                archetype[key] = number(row[key])
        if (row.get("tier") or "").strip():
            archetype["tier"] = row["tier"].strip()
        if (row.get("key_cards") or "").strip():
            _key_cards(index, archetype, row["key_cards"])
        deck_file = Path(decks_dir) / f"{archetype['name']}.txt" if decks_dir else None
        if deck_file and deck_file.exists():
            _enrich(conn, archetype, deck_file.read_text("utf-8-sig"))
        archetypes.append(archetype)
    archetypes.sort(key=lambda a: -(a["share"] or 0))

    snapshot = {
        "source": source, "url": url, "format": fmt, "mode": mode,
        "collected_at": (collected or date.today().isoformat()) + "T00:00:00",
        "note": note or "Importado manualmente de CSV.", "archetypes": archetypes,
    }
    snapshot["file"] = str(save(snapshot))
    return snapshot


def summarize(conn, snapshot, top_cards=20):
    """Resumo do meta: macroarquétipos, velocidade, cartas mais jogadas e interação.
    Só os arquétipos com lista de referência entram nas médias; pesos = fatia do meta."""
    with_deck = [a for a in snapshot["archetypes"] if a.get("stats")]
    covered = sum(a["share"] or 0 for a in with_deck)
    macros, cards, interaction = {}, {}, {}
    avg_mv = lands = 0.0
    for archetype in with_deck:
        weight = (archetype["share"] or 0) / covered if covered else 0
        macros[archetype["macro"]] = macros.get(archetype["macro"], 0) + (archetype["share"] or 0)
        avg_mv += archetype["stats"]["avg_mv"] * weight
        lands += archetype["stats"]["lands"] * weight
        for role in ("remoção pontual", "remoção em massa", "anulação"):
            interaction[role] = interaction.get(role, 0) + archetype["stats"]["roles"].get(role, 0) * weight
        deck = decklist.parse(archetype["deck"])
        decklist.resolve(conn, deck)
        for entry in decklist.merged(deck.main):
            if entry.card is not None and not analysis.is_land(entry.card):
                item = cards.setdefault(entry.card["name"], {"share": 0.0, "decks": 0, "copies": 0})
                item["share"] += archetype["share"] or 0
                item["decks"] += 1
                item["copies"] += entry.qty
    ranked = sorted(cards.items(), key=lambda kv: -kv[1]["share"])[:top_cards]
    return {
        "format": snapshot["format"], "mode": snapshot["mode"], "source": snapshot["source"],
        "collected_at": snapshot["collected_at"], "age_days": age_days(snapshot),
        "stale": age_days(snapshot) > STALE_DAYS,
        "archetypes": len(snapshot["archetypes"]), "with_deck": len(with_deck),
        "share_covered": round(covered, 1),
        "macros": {k: round(v, 1) for k, v in sorted(macros.items(), key=lambda kv: -kv[1])},
        "avg_mv": round(avg_mv, 2), "avg_lands": round(lands, 1),
        "interaction_per_deck": {k: round(v, 1) for k, v in interaction.items()},
        "top_cards": [{"name": name, "meta_share": round(v["share"], 1),
                       "avg_copies": round(v["copies"] / v["decks"], 1)} for name, v in ranked],
    }


def report(snapshot, summary, limit=20):
    lines = [
        f"{snapshot['format']} ({snapshot['mode'].upper()}) | fonte: {snapshot['source']} | "
        f"coletado em {snapshot['collected_at'][:10]} ({summary['age_days']} dias)",
    ]
    if summary["stale"]:
        lines.append(f"ATENÇÃO: snapshot com mais de {STALE_DAYS} dias; atualize antes de confiar nele.")
    if snapshot.get("note"):
        lines.append(snapshot["note"])
    lines += ["", "Arquétipos:"]
    for archetype in snapshot["archetypes"][:limit]:
        extra = ""
        if archetype.get("stats"):
            extra = (f" | {archetype['macro']}, VM médio {archetype['stats']['avg_mv']:.2f}, "
                     f"{archetype['stats']['lands']:g} terrenos")
        if archetype.get("winrate") is not None:
            extra += f" | win rate {archetype['winrate']:g}%"
        if archetype.get("games"):
            extra += f" em {archetype['games']:g} partidas"
        if archetype.get("tier"):
            extra += f" | tier {archetype['tier']}"
        if archetype.get("minutes"):
            extra += f" | {archetype['minutes']:g} min por partida"
        if isinstance((archetype.get("key_cards") or [None])[0], dict):
            extra += "\n           cartas: " + ", ".join(
                c["name"] + (f" {c['inclusion']:g}%" if c["inclusion"] is not None else "")
                for c in archetype["key_cards"])
        if archetype.get("unknown_cards"):
            extra += f" | fora da base: {', '.join(archetype['unknown_cards'])}"
        share = f"{archetype['share']:>5.1f}%" if archetype.get("share") is not None else "    ?"
        lines.append(f"  {share}  {archetype['name']}{extra}")
    if summary["with_deck"]:
        lines += [
            "", f"Resumo ({summary['with_deck']} arquétipos com lista, {summary['share_covered']}% do meta):",
            "  Macroarquétipos (heurística): " + ", ".join(f"{k} {v}%" for k, v in summary["macros"].items()),
            f"  Velocidade: valor de mana médio {summary['avg_mv']:.2f}, {summary['avg_lands']:g} terrenos em média",
            "  Interação por deck (média): " + ", ".join(
                f"{k} {v:g}" for k, v in summary["interaction_per_deck"].items()),
            "  Cartas mais jogadas (fatia do meta que as usa, cópias médias):",
        ]
        lines += [f"    {c['meta_share']:>5.1f}%  {c['avg_copies']:g}x {c['name']}" for c in summary["top_cards"]]
    return "\n".join(lines)
