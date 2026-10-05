"""Sincronização da base local a partir dos bulk data do Scryfall.

Docs: https://scryfall.com/docs/api/bulk-data
O Scryfall pede User-Agent e Accept explícitos e que os bulk files sejam
baixados no máximo uma vez por dia (eles são regenerados a cada ~12h).
"""

import gzip
import json
import shutil
import urllib.request
from pathlib import Path

from . import db

API = "https://api.scryfall.com"
HEADERS = {"User-Agent": "MTGDeckBuilder/0.1", "Accept": "application/json"}
WUBRG = "WUBRG"


def _open(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=120)


def _get_json(url):
    with _open(url) as resp:
        return json.load(resp)


def _download(url, dest):
    part = dest.with_suffix(dest.suffix + ".part")
    with _open(url) as resp, open(part, "wb") as out:
        shutil.copyfileobj(resp, out, length=1024 * 1024)
    part.replace(dest)


def _read_jsonl(path):
    """Um objeto JSON por linha; aceita arquivo .gz ou texto puro."""
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def _colors(values):
    return "".join(sorted(values or [], key=WUBRG.index))


def _price(value):
    return float(value) if value else None


def _card_row(card):
    faces = card.get("card_faces") or []
    first = faces[0] if faces else {}

    def pick(key):
        value = card.get(key)
        return value if value is not None else first.get(key)

    oracle_text = card.get("oracle_text")
    if oracle_text is None:
        oracle_text = "\n//\n".join(f.get("oracle_text", "") for f in faces)
    colors = card.get("colors")
    if colors is None:
        colors = {c for f in faces for c in f.get("colors", [])}

    return (
        pick("oracle_id") or card["id"],
        card["name"],
        card.get("layout"),
        pick("mana_cost"),
        pick("cmc"),
        pick("type_line"),
        oracle_text,
        _colors(colors),
        _colors(card.get("color_identity")),
        json.dumps(card.get("keywords", [])),
        _colors(card.get("produced_mana")) if set(card.get("produced_mana") or []) <= set(WUBRG)
        else "".join(card.get("produced_mana")),
        pick("power"),
        pick("toughness"),
        pick("loyalty"),
        pick("defense"),
        card.get("edhrec_rank"),
        int(bool(card.get("reserved"))),
        int(bool(card.get("game_changer"))),
        json.dumps(faces) if faces else None,
    )


def _printing_row(card, oracle_id):
    prices = card.get("prices") or {}
    images = card.get("image_uris") or (card.get("card_faces") or [{}])[0].get("image_uris") or {}
    return (
        card["id"],
        oracle_id,
        card["name"],
        card["set"],
        card.get("collector_number"),
        card.get("rarity"),
        card.get("lang"),
        card.get("released_at"),
        ",".join(card.get("games", [])),
        card.get("arena_id"),
        card.get("mtgo_id"),
        int(bool(card.get("booster"))),
        int(bool(card.get("digital"))),
        int(bool(card.get("reprint"))),
        int(bool(card.get("promo"))),
        _price(prices.get("usd")),
        _price(prices.get("usd_foil")),
        _price(prices.get("eur")),
        _price(prices.get("tix")),
        images.get("normal"),
    )


def ingest_cards(conn, path):
    """Recarrega cards/printings/legalities a partir de um arquivo default_cards (.jsonl.gz)."""
    for table in ("cards", "printings", "legalities", "cards_fts"):
        conn.execute(f"DELETE FROM {table}")
    seen = set()
    count = 0
    for card in _read_jsonl(path):
        row = _card_row(card)
        oracle_id = row[0]
        if oracle_id not in seen:
            seen.add(oracle_id)
            conn.execute(f"INSERT INTO cards VALUES ({','.join('?' * len(row))})", row)
            conn.executemany(
                "INSERT INTO legalities VALUES (?, ?, ?)",
                [(oracle_id, fmt, status)
                 for fmt, status in (card.get("legalities") or {}).items()
                 if status != "not_legal"],
            )
        printing = _printing_row(card, oracle_id)
        conn.execute(
            f"INSERT OR REPLACE INTO printings VALUES ({','.join('?' * len(printing))})", printing
        )
        count += 1
    conn.execute(
        "INSERT INTO cards_fts (name, type_line, oracle_text, oracle_id) "
        "SELECT name, type_line, oracle_text, oracle_id FROM cards"
    )
    return len(seen), count


def ingest_rulings(conn, path):
    conn.execute("DELETE FROM rulings")
    rows = [
        (r["oracle_id"], r.get("published_at"), r.get("source"), r.get("comment"))
        for r in _read_jsonl(path)
    ]
    conn.executemany("INSERT INTO rulings VALUES (?, ?, ?, ?)", rows)
    return len(rows)


def ingest_sets(conn, sets):
    conn.execute("DELETE FROM sets")
    conn.executemany(
        "INSERT INTO sets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (s["code"], s["name"], s.get("set_type"), s.get("released_at"), s.get("card_count"),
             int(bool(s.get("digital"))), s.get("block"), s.get("parent_set_code"),
             s.get("arena_code"), s.get("mtgo_code"))
            for s in sets
        ],
    )
    return len(sets)


def _fetch_sets():
    sets, url = [], f"{API}/sets"
    while url:
        page = _get_json(url)
        sets.extend(page["data"])
        url = page.get("next_page") if page.get("has_more") else None
    return sets


def sync(conn, data_dir=None, force=False, log=print):
    """Baixa os bulk data do Scryfall e atualiza a base. Pula o que já está em dia."""
    data_dir = Path(data_dir or db.DATA_DIR)
    data_dir.mkdir(parents=True, exist_ok=True)
    bulk = {b["type"]: b for b in _get_json(f"{API}/bulk-data")["data"]}

    for kind, ingest in (("default_cards", ingest_cards), ("rulings", ingest_rulings)):
        info = bulk[kind]
        meta_key = f"scryfall_{kind}_updated_at"
        if not force and db.get_meta(conn, meta_key) == info["updated_at"]:
            log(f"{kind}: já atualizado ({info['updated_at']})")
            continue
        dest = data_dir / f"{kind}.jsonl.gz"
        log(f"{kind}: baixando {info.get('compressed_size', 0) / 1e6:.0f} MB...")
        _download(info["jsonl_download_uri"], dest)
        log(f"{kind}: importando...")
        with conn:
            result = ingest(conn, dest)
            db.set_meta(conn, meta_key, info["updated_at"])
        dest.unlink()
        log(f"{kind}: ok ({result})")

    with conn:
        log(f"sets: ok ({ingest_sets(conn, _fetch_sets())})")
