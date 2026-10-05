"""Conexão e schema do banco SQLite local."""

import os
import sqlite3
from pathlib import Path

DATA_DIR = Path(os.environ.get("MTG_DATA_DIR", Path(__file__).resolve().parents[2] / "data"))
DB_PATH = DATA_DIR / "mtg.sqlite"

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Uma linha por carta "oracle" (independente de impressão).
CREATE TABLE IF NOT EXISTS cards (
    oracle_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    layout TEXT,
    mana_cost TEXT,
    cmc REAL,
    type_line TEXT,
    oracle_text TEXT,
    colors TEXT,            -- ex.: "WU" (ordem WUBRG), "" para incolor
    color_identity TEXT,    -- idem
    keywords TEXT,          -- JSON array
    produced_mana TEXT,
    power TEXT,
    toughness TEXT,
    loyalty TEXT,
    defense TEXT,
    edhrec_rank INTEGER,
    reserved INTEGER,
    game_changer INTEGER,
    faces TEXT              -- JSON das faces (cartas dupla-face, split, adventure...)
);
CREATE INDEX IF NOT EXISTS idx_cards_name ON cards(name COLLATE NOCASE);

-- Só guarda status diferentes de not_legal (legal, restricted, banned).
CREATE TABLE IF NOT EXISTS legalities (
    oracle_id TEXT NOT NULL,
    format TEXT NOT NULL,
    status TEXT NOT NULL,
    PRIMARY KEY (format, oracle_id)
) WITHOUT ROWID;
CREATE INDEX IF NOT EXISTS idx_legalities_oracle ON legalities(oracle_id);

-- Uma linha por impressão (carta em uma coleção).
CREATE TABLE IF NOT EXISTS printings (
    id TEXT PRIMARY KEY,
    oracle_id TEXT NOT NULL,
    name TEXT,
    set_code TEXT NOT NULL,
    collector_number TEXT,
    rarity TEXT,
    lang TEXT,
    released_at TEXT,
    games TEXT,             -- ex.: "paper,arena,mtgo"
    arena_id INTEGER,
    mtgo_id INTEGER,
    booster INTEGER,
    digital INTEGER,
    reprint INTEGER,
    promo INTEGER,
    usd REAL,
    usd_foil REAL,
    eur REAL,
    tix REAL,
    image_uri TEXT
);
CREATE INDEX IF NOT EXISTS idx_printings_oracle ON printings(oracle_id);
CREATE INDEX IF NOT EXISTS idx_printings_set ON printings(set_code);

CREATE TABLE IF NOT EXISTS sets (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    set_type TEXT,
    released_at TEXT,
    card_count INTEGER,
    digital INTEGER,
    block TEXT,
    parent_set_code TEXT,
    arena_code TEXT,
    mtgo_code TEXT
);

CREATE TABLE IF NOT EXISTS rulings (
    oracle_id TEXT NOT NULL,
    published_at TEXT,
    source TEXT,
    comment TEXT
);
CREATE INDEX IF NOT EXISTS idx_rulings_oracle ON rulings(oracle_id);

CREATE VIRTUAL TABLE IF NOT EXISTS cards_fts USING fts5(
    name, type_line, oracle_text, oracle_id UNINDEXED
);
"""


def _subset(a, b):
    return set(a or "") <= set(b or "")


def connect(path=None, readonly=False):
    path = Path(path or DB_PATH)
    if readonly:
        conn = sqlite3.connect(f"{path.as_uri()}?mode=ro", uri=True)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(path)
        conn.executescript(SCHEMA)
    conn.row_factory = sqlite3.Row
    conn.create_function("subset", 2, _subset, deterministic=True)
    return conn


def get_meta(conn, key):
    row = conn.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
    return row[0] if row else None


def set_meta(conn, key, value):
    conn.execute("INSERT OR REPLACE INTO meta (key, value) VALUES (?, ?)", (key, value))
