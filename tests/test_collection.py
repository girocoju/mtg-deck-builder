import json

import pytest

from mtg_builder import arena_log, arena_match, collection
from test_arena_log import H, fake_arena_db
from test_decks import conn  # noqa: F401

DECKS = {"d1": {"MainDeck": [{"cardId": 101, "quantity": 4}, {"cardId": 102, "quantity": 20}], "CardSkins": []},
         "d2": {"MainDeck": [{"cardId": 101, "quantity": 2}, {"cardId": 103, "quantity": 1}],
                "Sideboard": [{"cardId": 103, "quantity": 2}]},
         "lixo": "não é deck"}


def test_cards_in_decks_takes_the_maximum():
    assert collection.cards_in_decks(DECKS) == {101: 4, 102: 20, 103: 2}
    assert collection.cards_in_decks(None) == {}


def test_update_from_decks_then_booster(conn, tmp_path):  # noqa: F811
    path = tmp_path / "Raw_CardDatabase_abc.mtga"
    fake_arena_db(path)
    session = arena_match.MatchSession(conn, arena_log.ArenaCards(path))
    data = collection.load(tmp_path / "collection.json")
    changed = collection.update(data, {101: 4, 102: 20, 103: 2}, "decks", session.resolve)
    assert changed == 3
    assert data["cards"]["101"] == {"name": "Bear", "set": "tst", "number": "1", "rarity": "common", "qty": 4, "sources": ["decks"]}
    assert data["cards"]["103"]["name"] == "Nameless Wonder" and data["cards"]["103"]["qty"] == 2
    assert collection.update(data, {101: 2}, "decks", session.resolve) == 0            # máximo não diminui
    assert collection.update(data, {101: 1, 999: 1}, "booster", session.resolve) == 2  # booster soma
    assert data["cards"]["101"]["qty"] == 5 and data["cards"]["101"]["sources"] == ["decks", "booster"]
    assert data["cards"]["999"]["name"] == "#999"
    saved = collection.save(data, tmp_path / "collection.json")
    loaded = collection.load(saved)
    assert loaded["updated_at"] and loaded["sources"]["booster"]["cards"] == 2
    assert collection.owned(loaded, "bear") == 5 and collection.owned(loaded, "Elk") == 20   # 102 é Elk na base falsa
    assert collection.owned(loaded, "Drake") == 0
    text = collection.format_summary(loaded)
    assert "4 cartas distintas" in text and "decks (3 cartas" in text
    assert "  4 Bear (C)" not in text and "Bear" not in collection.format_summary(loaded, "zzz")
    assert "  2 Nameless Wonder (U)" in collection.format_summary(loaded, "zzz")


def test_import_csv_from_an_external_tracker(conn, tmp_path):  # noqa: F811
    csv_path = tmp_path / "colecao.csv"
    csv_path.write_text("Name,Set,Collector Number,Quantity\nBear,TST,1,4\nElk,TST,1,2\nCarta Inventada,ZZZ,9,1\n",
                        encoding="utf-8")
    data = collection.load(tmp_path / "collection.json")
    imported, unknown = collection.import_csv(data, csv_path, conn)
    assert imported == 3 and unknown == ["Carta Inventada"]
    assert collection.owned(data, "Bear") == 4 and collection.owned(data, "Carta Inventada") == 1
    assert data["cards"]["csv:tst:1:bear"]["sources"] == ["csv"] and data["sources"]["csv"]["cards"] == 3
    with pytest.raises(RuntimeError, match="sem colunas"):
        (tmp_path / "ruim.csv").write_text("a,b\n1,2\n", encoding="utf-8")
        collection.import_csv(data, tmp_path / "ruim.csv", conn)


def test_startup_message_feeds_the_collection(conn, tmp_path):  # noqa: F811
    path = tmp_path / "Raw_CardDatabase_abc.mtga"
    fake_arena_db(path)
    startup = {"InventoryInfo": {"Gems": 5, "Gold": 100, "WildCardCommons": 1, "WildCardUnCommons": 2,
                                 "WildCardRares": 3, "WildCardMythics": 4, "CustomTokens": {"DraftToken": 1}},
               "DecksInternal": DECKS}
    text = f"{H}07/11/2026 05:05:09\n<== StartHook(s1)\n" + json.dumps(startup)
    events = arena_log.events_from_text(text, arena_match.classify_match)
    assert events[0]["type"] == "inventory" and events[0]["deck_cards"] == {101: 4, 102: 20, 103: 2}
    session = arena_match.MatchSession(conn, arena_log.ArenaCards(path), collection_path=tmp_path / "collection.json")
    line = session.handle(events[0])
    assert line.startswith("cofre: 100 ouro") and "coleção aproximada pelos decks salvos: 3 cartas distintas, 3 atualizada(s)" in line
    assert collection.owned(collection.load(tmp_path / "collection.json"), "Bear") == 4
