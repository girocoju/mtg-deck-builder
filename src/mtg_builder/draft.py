"""Dados de limitado: estatísticas do 17Lands por coleção e modo, e leitura da coleção
a partir da base local.

O 17Lands não documenta uma API; este módulo lê os mesmos arquivos JSON que as páginas
públicas de "Card Ratings" e "Color Ratings" carregam, com cache de 24 horas e uma
requisição por coleção e modo. Cada modo (Premier, Quick, Traditional, Sealed...) fica
em arquivo próprio: os números de um não valem para outro.
"""

import json
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta

from . import analysis, db, decklist

BASE = "https://www.17lands.com"
USER_AGENT = "MTGDeckBuilder/0.1 (projeto pessoal; github.com/girocoju/mtg-deck-builder)"
MODES = {
    "premier": "PremierDraft", "quick": "QuickDraft", "trad": "TradDraft",
    "sealed": "Sealed", "tradsealed": "TradSealed", "picktwo": "PickTwoDraft",
}
MAX_AGE_HOURS = 24
MIN_GAMES = 500  # abaixo disso o win rate de uma carta é ruído
COLOR_ORDER = "WUBRG"


def _download(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.load(response)


def _mode(mode):
    if mode not in MODES:
        raise RuntimeError(f"Modo desconhecido: {mode}. Use um de: {', '.join(MODES)}.")
    return MODES[mode]


def find_set(conn, term):
    """Coleção por código ou nome; entre várias com o nome, prefere expansões."""
    rows = conn.execute(
        "SELECT * FROM sets WHERE code = ?1 COLLATE NOCASE OR name LIKE '%' || ?1 || '%' "
        "ORDER BY (code = ?1 COLLATE NOCASE) DESC, "
        "(set_type IN ('expansion', 'core', 'masters', 'draft_innovation')) DESC, released_at DESC",
        (term,),
    ).fetchall()
    if not rows:
        raise RuntimeError(f"Coleção não encontrada: {term}.")
    return rows[0]


def _path(set_code, mode):
    return db.DATA_DIR / "17lands" / set_code.lower() / f"{mode}.json"


def cached(set_code, mode):
    path = _path(set_code, mode)
    return json.loads(path.read_text("utf-8")) if path.exists() else None


def _row(card):
    return {
        "name": card["name"], "color": card.get("color") or "", "rarity": card.get("rarity"),
        "games": card.get("game_count") or 0, "gih_games": card.get("ever_drawn_game_count") or 0,
        "gih": card.get("ever_drawn_win_rate"), "oh": card.get("opening_hand_win_rate"),
        "gd": card.get("drawn_win_rate"), "gp": card.get("win_rate"),
        "iwd": card.get("drawn_improvement_win_rate"),
        "alsa": card.get("avg_seen"), "ata": card.get("avg_pick"),
    }


def update(conn, set_term, mode="premier", force=False, fetch=_download, today=None):
    """Coleta as estatísticas de cartas e de cores do 17Lands para a coleção e o modo.
    Devolve o snapshot; se a coleção não tem dados nesse modo, `cards` vem vazio."""
    event = _mode(mode)
    info = find_set(conn, set_term)
    code = (info["arena_code"] or info["code"]).upper()
    previous = cached(info["code"], mode)
    if previous and not force:
        age = datetime.now() - datetime.fromisoformat(previous["collected_at"])
        if age < timedelta(hours=MAX_AGE_HOURS):
            return previous

    today = today or date.today()
    released = date.fromisoformat(info["released_at"]) if info["released_at"] else today
    start = released - timedelta(days=10)  # o Arena recebe a coleção alguns dias antes do papel
    cards_url = f"{BASE}/card_ratings/data?" + urllib.parse.urlencode({"expansion": code, "format": event})
    colors_url = f"{BASE}/color_ratings/data?" + urllib.parse.urlencode({
        "expansion": code, "event_type": event, "start_date": start.isoformat(),
        "end_date": today.isoformat(), "combine_splash": "true"})
    try:
        cards = [_row(c) for c in fetch(cards_url)]
        colors = fetch(colors_url)
    except (OSError, ValueError) as error:
        raise RuntimeError(f"Falha ao acessar o 17Lands ({cards_url}): {error}") from error

    with_data = [c for c in cards if c["gih"] is not None]
    total = next((c for c in colors if c.get("color_name") == "All Decks"), None)
    snapshot = {
        "source": "17lands", "set": info["code"], "set_name": info["name"], "mode": mode, "event": event,
        "url": cards_url, "collected_at": datetime.now().isoformat(timespec="seconds"),
        "has_data": bool(with_data),
        "games": total["games"] if total else None,
        "baseline": round(total["wins"] / total["games"], 4) if total and total["games"] else None,
        "cards": cards,
        "colors": [
            {"name": c["color_name"], "short": c.get("short_name"), "summary": bool(c.get("is_summary")),
             "games": c["games"], "win_rate": round(c["wins"] / c["games"], 4) if c["games"] else None}
            for c in colors
        ],
    }
    path = _path(info["code"], mode)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(snapshot, ensure_ascii=False), encoding="utf-8")
    return snapshot


def ranking(snapshot, color=None, rarity=None, min_games=MIN_GAMES, sort="gih", limit=None):
    """Cartas ordenadas por uma métrica. `color`: uma letra (mono daquela cor), "multi"
    ou "colorless". Cartas com menos de `min_games` jogos em mão ficam de fora."""
    rows = []
    for card in snapshot["cards"]:
        if card["gih"] is None or card["gih_games"] < min_games:
            continue
        if rarity and card["rarity"] != rarity:
            continue
        if color:
            c = card["color"]
            if color == "multi" and len(c) < 2:
                continue
            if color == "colorless" and c:
                continue
            if color not in ("multi", "colorless") and c != color.upper():
                continue
        rows.append(card)
    reverse = sort not in ("alsa", "ata")
    rows.sort(key=lambda c: (c[sort] is None, -(c[sort] or 0) if reverse else (c[sort] or 0)))
    return rows[:limit] if limit else rows


def color_pairs(snapshot, min_games=2000):
    """Pares de cores (e mono) com win rate, do melhor para o pior."""
    rows = [c for c in snapshot["colors"]
            if not c["summary"] and c["games"] >= min_games and c["win_rate"] is not None
            and len(str(c["short"])) <= 2]
    return sorted(rows, key=lambda c: -c["win_rate"])


def rate(snapshot, names):
    """Estatísticas das cartas citadas (para avaliar um pacote ou um pool). Nomes são
    comparados sem acentos nem maiúsculas; aceita só a face da frente."""
    index = {}
    for card in snapshot["cards"]:
        index[decklist._key(card["name"])] = card
        index.setdefault(decklist._key(card["name"].split(" // ")[0]), card)
    found, missing = [], []
    for name in names:
        card = index.get(decklist._key(name))
        (found if card else missing).append(card or name)
    return found, missing


def over_under(snapshot, min_games=MIN_GAMES, top=8):
    """Cartas que a comunidade pega tarde e rendem muito (subestimadas) e o contrário.
    Compara a posição no ranking de GIH WR com a posição no ranking de ALSA."""
    cards = [c for c in snapshot["cards"]
             if c["gih"] is not None and c["alsa"] is not None and c["gih_games"] >= min_games
             and c["rarity"] in ("common", "uncommon")]
    by_gih = {c["name"]: i for i, c in enumerate(sorted(cards, key=lambda c: -c["gih"]))}
    by_alsa = {c["name"]: i for i, c in enumerate(sorted(cards, key=lambda c: c["alsa"]))}
    gap = sorted(cards, key=lambda c: by_alsa[c["name"]] - by_gih[c["name"]])
    return {"subestimadas": gap[::-1][:top], "superestimadas": gap[:top]}


def set_overview(conn, set_term, snapshot=None):
    """Leitura da coleção pela base: cartas por cor e raridade, curva de criaturas e
    interação nas comuns e incomuns, palavras-chave mais frequentes. Se houver snapshot
    do 17Lands, o conjunto draftável é a lista de cartas dele; senão, as impressões
    marcadas como de booster (ou todas, se a coleção não tiver a marcação)."""
    info = find_set(conn, set_term)
    rows = conn.execute(
        "SELECT c.*, MIN(p.rarity) AS set_rarity, MAX(p.booster) AS booster FROM cards c "
        "JOIN printings p ON p.oracle_id = c.oracle_id WHERE p.set_code = ? "
        "AND c.layout NOT IN ('token', 'double_faced_token', 'emblem', 'art_series') "
        "GROUP BY c.oracle_id", (info["code"],),
    ).fetchall()
    if snapshot and snapshot.get("cards"):
        names = {decklist._key(c["name"]) for c in snapshot["cards"]}
        rarities = {decklist._key(c["name"]): c["rarity"] for c in snapshot["cards"]}
        cards = [(r, rarities[decklist._key(r["name"])]) for r in rows if decklist._key(r["name"]) in names]
        basis = "lista de cartas do 17Lands"
    else:
        in_booster = [r for r in rows if r["booster"]]
        cards = [(r, r["set_rarity"]) for r in (in_booster or rows)]
        basis = "impressões de booster na base" if in_booster else "todas as cartas da coleção na base"
    cards = [(r, rarity) for r, rarity in cards if "Basic" not in (r["type_line"] or "")]

    def group(card):
        colors = card["colors"] or ""
        return colors if len(colors) == 1 else "multi" if colors else "incolor"

    table, keywords = {}, {}
    for card, rarity in cards:
        entry = table.setdefault(group(card), {
            "total": 0, "common": 0, "uncommon": 0, "rare": 0, "mythic": 0,
            "criaturas_cu": 0, "remocao_cu": [], "curva_criaturas_cu": {}})
        entry["total"] += 1
        if rarity in entry:
            entry[rarity] += 1
        for keyword in json.loads(card["keywords"] or "[]"):
            keywords[keyword] = keywords.get(keyword, 0) + 1
        if rarity in ("common", "uncommon"):
            roles = analysis.roles(card)
            if "Creature" in (card["type_line"] or "").split(" // ")[0]:
                entry["criaturas_cu"] += 1
                bucket = str(min(int(card["cmc"] or 0), 6))
                entry["curva_criaturas_cu"][bucket] = entry["curva_criaturas_cu"].get(bucket, 0) + 1
            if "remoção pontual" in roles or "remoção em massa" in roles:
                entry["remocao_cu"].append(card["name"])
    order = [c for c in COLOR_ORDER if c in table] + [g for g in ("multi", "incolor") if g in table]
    return {
        "set": info["code"], "name": info["name"], "released_at": info["released_at"],
        "cards": len(cards), "basis": basis,
        "colors": {g: table[g] for g in order},
        "keywords": sorted(keywords.items(), key=lambda kv: -kv[1])[:16],
    }
