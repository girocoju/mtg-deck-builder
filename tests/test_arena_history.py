import json

from mtg_builder import arena_history, arena_log, arena_match
from test_arena_log import H, gre, room

STAMP = "[UnityCrossThreadLogger]06/11/2026 23:16:36"


def rank(won, lost):
    return (f"{H}07/11/2026 02:15:49\n<== RankGetCombinedRankInfo(r1)\n" + json.dumps(
        {"playerId": "ME", "constructedSeasonOrdinal": 95, "constructedClass": "Gold", "constructedLevel": 2,
         "constructedMatchesWon": won, "constructedMatchesLost": lost, "limitedSeasonOrdinal": 95, "limitedLevel": 4}))


def inventory():
    return (f"{H}07/11/2026 05:05:09\n<== StartHook(s1)\n" + json.dumps(
        {"InventoryInfo": {"SeqId": 1, "Gems": 5, "Gold": 5625, "TotalVaultProgress": 848, "WildCardCommons": 48,
                           "WildCardUnCommons": 34, "WildCardRares": 1, "WildCardMythics": 2,
                           "CustomTokens": {"DraftToken": 9, "PlayInToken": 1}}}))


def decks():
    return (f"{H}07/11/2026 02:15:50\n<== DeckGetDeckSummariesV3(d1)\n" + json.dumps(
        {"Summaries": [{"DeckId": "x", "Name": "Turn 2 Kill", "Attributes": [
            {"name": "Format", "value": "Standard"}, {"name": "LastPlayed", "value": "\"2026-11-07T01:33:00-03:00\""}]}]}))


def match(opponent, winner, deck="Turn 2 Kill", when="06/11/2026 23:16:36"):
    request = json.dumps({"EventName": "Ladder", "Summary": {"Name": deck}, "Deck": {"MainDeck": [{"cardId": 101, "quantity": 4}]}})
    body_room = room("Playing").replace("Rival", opponent).replace("06/11/2026 23:16:36", when)
    body_end = room("MatchCompleted", [("Game", winner), ("Match", winner)]).replace("Rival", opponent)
    return "\n".join([f"{H}==> EventSetDeckV3 " + json.dumps({"id": "d", "request": request}),
                      body_room, gre(turn=1, active=2, life={1: 20, 2: 20}), gre(turn=2, active=1), body_end])


def test_scan_rows_rank_inventory_and_timestamps(tmp_path):
    text = "\n".join([f"{H}x\n<== Auth\n" + json.dumps({"authenticateResponse": {"clientId": "ME"}}), rank(10, 8),
                      inventory(), decks(), match("Alpha", 1), match("Beta", 2, when="07/11/2026 00:39:33")])
    log = tmp_path / "Player.log"
    log.write_text(text, encoding="utf-8")
    data = arena_history.scan([log])
    rows = data["rows"]
    assert [(r["opponent"], r["result"], r["deck"], r["event"]) for r in rows] == [
        ("Alpha", "vitória", "Turn 2 Kill", "Ladder"), ("Beta", "derrota", "Turn 2 Kill", "Ladder")]
    assert rows[0]["at"] == "2026-11-06T23:16:36" and rows[1]["at"] == "2026-11-07T00:39:33"
    assert rows[0]["own_turns"] == 1 and rows[0]["match_id"] == "m"
    assert data["rank"]["won"] == 10 and data["rank"]["class"] == "Gold"
    assert data["inventory"]["gold"] == 5625 and data["inventory"]["wildcards"]["rare"] == 1
    assert data["decks"][0]["last_played"].startswith("2026-11-07") and data["decks"][0]["format"] == "Standard"


def test_store_dedupes_and_summarizes(tmp_path):
    path = tmp_path / "matches.jsonl"
    a = {"match_id": "m1", "at": "2026-11-07T00:39:33", "event": "Ladder", "deck": "Turn 2 Kill", "opponent": "A", "result": "vitória"}
    b = {"match_id": "m2", "at": "2026-11-07T01:33:43", "event": "Ladder", "deck": "Turn 2 Kill", "opponent": "B", "result": "derrota"}
    c = {"match_id": "m3", "at": "2026-11-06T23:16:36", "event": "Play_Brawl_Historic", "deck": "Norin", "opponent": "C", "result": "vitória"}
    assert arena_history.append(a, path) and arena_history.append(b, path) and not arena_history.append(a, path)
    assert [r["match_id"] for r in arena_history.load(path)] == ["m1", "m2"]
    rows = arena_history.merge(arena_history.load(path), [c, {**b, "turns": 9}])
    assert [r["match_id"] for r in rows] == ["m3", "m1", "m2"] and rows[2]["turns"] == 9
    stats = arena_history.summary(rows)
    assert stats["decks"]["Turn 2 Kill"] == {"won": 1, "lost": 1, "last": "2026-11-07T01:33:43", "matches": 2, "win_rate": 0.5}
    assert stats["events"]["Ladder"]["matches"] == 2 and stats["decks"]["Norin"]["win_rate"] == 1.0
    only = arena_history.summary(rows, deck="turn 2 kill")
    assert list(only["decks"]) == ["Turn 2 Kill"]
    text = arena_history.format_history(rows, stats, {"season": 95, "class": "Gold", "level": 2, "won": 13, "lost": 9},
                                        {"gold": 1, "gems": 2, "wildcards": {"common": 3, "uncommon": 4, "rare": 5, "mythic": 6},
                                         "tokens": {"DraftToken": 9}})
    assert "3 partida(s)" in text and "Turn 2 Kill                  1–1  50%" in text
    assert "13–9 na temporada" in text and "DraftToken 9" in text


def test_live_session_appends_history(tmp_path):
    path = tmp_path / "matches.jsonl"
    session = arena_match.MatchSession(records_dir=tmp_path / "games", history_path=path)
    text = "\n".join([f"{H}x\n<== Auth\n" + json.dumps({"authenticateResponse": {"clientId": "ME"}}), match("Zeta", 1)])
    for event in arena_log.events_from_text(text, arena_match.classify_match):
        session.handle(event)
    stored = arena_history.load(path)
    assert len(stored) == 1 and stored[0]["opponent"] == "Zeta" and stored[0]["result"] == "vitória"
    assert session.rows == stored
