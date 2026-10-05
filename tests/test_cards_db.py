import gzip
import json
from pathlib import Path

import pytest

from mtg_builder import db, query, scryfall

CARDS = json.loads((Path(__file__).parent / "fixtures" / "default_cards.json").read_text("utf-8"))


@pytest.fixture
def bulk_file(tmp_path):
    path = tmp_path / "default_cards.jsonl.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        f.writelines(json.dumps(card) + "\n" for card in CARDS)
    return path


@pytest.fixture
def conn(tmp_path, bulk_file):
    conn = db.connect(tmp_path / "test.sqlite")
    with conn:
        scryfall.ingest_cards(conn, bulk_file)
    return conn


def names(rows):
    return [r["name"] for r in rows]


def test_ingest_dedupes_cards_and_keeps_printings(conn):
    assert conn.execute("SELECT COUNT(*) FROM cards").fetchone()[0] == 4
    assert conn.execute("SELECT COUNT(*) FROM printings").fetchone()[0] == 5


def test_reingest_is_idempotent(conn, bulk_file):
    with conn:
        assert scryfall.ingest_cards(conn, bulk_file) == (4, 5)
    assert len(query.search(conn, text="flying", include_extras=True)) == 3


def test_double_faced_card_uses_front_face(conn):
    card, _ = query.find_card(conn, "Delver of Secrets")
    assert card["mana_cost"] == "{U}"
    assert card["colors"] == "U"
    assert card["power"] == "1"
    assert "Flying" in card["oracle_text"]


def test_find_card_is_case_insensitive_and_suggests(conn):
    card, _ = query.find_card(conn, "lightning bolt")
    assert card["name"] == "Lightning Bolt"
    card, candidates = query.find_card(conn, "Ivy")
    assert card is None
    assert names(candidates) == ["Ivy, Gleeful Spellthief"]


def test_legalities_skip_not_legal(conn):
    card, _ = query.find_card(conn, "Lightning Bolt")
    assert query.legalities(conn, card["oracle_id"]) == {
        "modern": "legal", "oldschool": "banned", "vintage": "legal"
    }


def test_search_by_format_excludes_banned(conn):
    assert "Lightning Bolt" in names(query.search(conn, fmt="modern"))
    assert query.search(conn, fmt="oldschool") == []


def test_search_identity_is_subset(conn):
    assert names(query.search(conn, identity="GU")) == [
        "Delver of Secrets // Insectile Aberration", "Ivy, Gleeful Spellthief"
    ]
    assert query.search(conn, identity="") == []


def test_search_colors_requires_all(conn):
    assert names(query.search(conn, colors="GU")) == ["Ivy, Gleeful Spellthief"]


def test_search_text_type_and_extras(conn):
    assert names(query.search(conn, text="flying", type_line="faerie rogue")) == [
        "Ivy, Gleeful Spellthief"
    ]
    assert "Faerie Rogue" in names(query.search(conn, type_line="faerie", include_extras=True))


def test_search_by_printing_filters(conn):
    assert names(query.search(conn, set_code="DMU", rarity="rare", booster=True)) == [
        "Ivy, Gleeful Spellthief"
    ]
    assert names(query.search(conn, game="arena")) == ["Ivy, Gleeful Spellthief"]
    assert names(query.search(conn, cmc_max=1, order="cmc")) == [
        "Delver of Secrets // Insectile Aberration", "Lightning Bolt"
    ]
