import json
import sqlite3

from mtg_builder import arena_log, arena_match
from test_decks import conn  # noqa: F401

H = "[UnityCrossThreadLogger]"


def notify(pack, pick, cards):
    return f"{H}Draft.Notify\n" + json.dumps(
        {"draftId": "d-1", "SelfPack": pack, "SelfPick": pick, "PackCards": ",".join(map(str, cards))})


def make_pick(pack, pick, card):
    request = json.dumps({"DraftId": "d-1", "GrpIds": [card], "Pack": pack, "Pick": pick})
    return f"{H}==> EventPlayerDraftMakePick " + json.dumps({"id": "r-1", "request": request})


def business(pack, pick, cards, picked):
    return f"{H}LogBusinessEvents\n" + json.dumps(
        {"EventId": "PremierDraft_TST_20261107", "DraftId": "d-1", "PackNumber": pack, "PickNumber": pick,
         "CardsInPack": cards, "PickGrpId": picked})


def bot_pack(pack, pick, cards):
    return (f"{H}07/11/2026 02:15:49\n<== BotDraftDraftStatus(abc)\n" + json.dumps(
        {"DraftStatus": "PickNext", "PackNumber": pack, "PickNumber": pick, "DraftPack": [str(c) for c in cards],
         "EventName": "QuickDraft_TST_20261107"}))


def bot_pick(pack, pick, card):
    request = json.dumps({"PickInfo": {"EventName": "QuickDraft_TST_20261107", "CardIds": [str(card)],
                                       "PackNumber": pack, "PickNumber": pick}})
    return f"{H}==> BotDraft_DraftPick " + json.dumps({"id": "x", "request": request})


def join(name):
    return f"{H}==> EventJoin " + json.dumps({"id": "j", "request": json.dumps({"EventName": name})})


def complete():
    return f"{H}==> Draft_CompleteDraft " + json.dumps({"id": "c", "request": json.dumps({"DraftId": "d-1"})})


NOISE = [f"{H}==> GetFormats " + json.dumps({"id": "n", "request": "{ }"}),
         f"{H}07/11/2026 02:15:49", "<== GetFormats(n)", json.dumps({"formats": [1, 2]}),
         f"{H}STATE CHANGED " + json.dumps({"old": "A", "new": "B"}), "Linha solta sem cabeçalho"]


def test_event_name_gives_mode_and_set():
    assert arena_log.parse_event_name("PremierDraft_FRA_20261106") == ("premier", "fra")
    assert arena_log.parse_event_name("QuickDraft_FRA_20261001") == ("quick", "fra")
    assert arena_log.parse_event_name("TradDraft_TST_20261107") == ("trad", "tst")
    assert arena_log.parse_event_name("Sealed_FRA_20261001") == ("sealed", "fra")
    assert arena_log.parse_event_name("Play_Brawl_Historic") == (None, None)
    assert arena_log.parse_event_name(None) == (None, None)


def test_human_draft_events_in_order():
    text = "\n".join(NOISE + [join("PremierDraft_TST_20261107"), notify(1, 1, [101, 102, 103]), make_pick(1, 1, 102),
                              notify(1, 2, [104, 105]), business(0, 1, [104, 105], 105), complete()])
    events = arena_log.events_from_text(text)
    kinds = [(e["type"], e.get("pack"), e.get("pick")) for e in events]
    assert kinds == [("join", None, None), ("pack", 1, 1), ("pick", 1, 1), ("pack", 1, 2),
                     ("pack_and_pick", 1, 2), ("complete", None, None)]
    assert events[0]["event"] == "PremierDraft_TST_20261107"
    assert events[1]["cards"] == [101, 102, 103] and events[1]["source"] == "Draft.Notify"
    assert events[2]["card"] == 102
    assert events[4]["cards"] == [104, 105] and events[4]["card"] == 105


def test_bot_draft_events():
    events = arena_log.events_from_text("\n".join([bot_pack(1, 3, [7, 8]), bot_pick(1, 3, 8)]))
    assert [(e["type"], e["pack"], e["pick"]) for e in events] == [("pack", 2, 4), ("pick", 2, 4)]
    assert events[0]["cards"] == [7, 8] and events[0]["event"] == "QuickDraft_TST_20261107"
    assert events[1]["card"] == 8


def test_pack_cards_as_list_and_unknown_draft_lines():
    entry = f"{H}Draft.Notify\n" + json.dumps({"draftId": "d", "SelfPack": 2, "SelfPick": 13, "PackCards": [5, "6", "x"]})
    event = arena_log.events_from_text(entry)[0]
    assert (event["pack"], event["pick"], event["cards"]) == (2, 13, [5, 6])
    unknown = arena_log.events_from_text(f"{H}==> DraftSomethingNew " + json.dumps({"id": 1, "Foo": 2}))
    assert unknown[0]["type"] == "unknown" and "Foo" in unknown[0]["keys"]


def test_follower_reads_incrementally_and_survives_rotation(tmp_path):
    path = tmp_path / "Player.log"
    path.write_text("Mono path\nDETAILED LOGS: ENABLED\n", encoding="utf-8")
    assert arena_log.detailed_logs_enabled(path) is True
    follower = arena_log.LogFollower(path)                    # começa do fim
    assert follower.poll() == []
    with open(path, "a", encoding="utf-8") as handle:         # cabeçalho sem o JSON ainda
        handle.write(f"{H}Draft.Notify\n")
    assert follower.poll() == []
    with open(path, "a", encoding="utf-8") as handle:         # JSON pela metade
        handle.write('{"draftId": "d-1", "SelfPack": 1, "SelfPick": 1, "Pack')
    assert follower.poll() == []
    with open(path, "a", encoding="utf-8") as handle:
        handle.write('Cards": "1,2,3"}\n')
    events = follower.poll()
    assert [e["type"] for e in events] == ["pack"] and events[0]["cards"] == [1, 2, 3]
    with open(path, "a", encoding="utf-8") as handle:         # a mesma entrada não sai duas vezes
        handle.write(make_pick(0, 0, 2) + "\n")
    assert [e["type"] for e in follower.poll()] == ["pick"]
    path.write_text(f"{H}Draft.Notify\n" + json.dumps({"draftId": "d-2", "SelfPack": 1, "SelfPick": 1, "PackCards": "9"}) + "\n",
                    encoding="utf-8")                           # arquivo recriado, menor
    events = follower.poll()
    assert len(events) == 1 and events[0]["cards"] == [9]


def test_synthetic_premier_fixture_has_42_packs_and_picks():
    from pathlib import Path
    text = (Path(__file__).parent / "fixtures" / "player-log-premier-fra-sintetico.txt").read_text("utf-8")
    events = arena_log.events_from_text(text)
    packs = [e for e in events if e["type"] in ("pack", "pack_and_pick")]
    picks = [e for e in events if e["type"] in ("pick", "pack_and_pick")]
    assert len(packs) == 42 and len(picks) == 42
    assert [(e["pack"], e["pick"]) for e in packs] == [(p, k) for p in (1, 2, 3) for k in range(1, 15)]
    assert [len(e["cards"]) for e in packs][:3] == [14, 13, 12] and packs[0]["type"] == "pack_and_pick"
    assert events[0]["type"] == "join" and events[-1]["type"] == "complete"
    assert all(pick["card"] in pack["cards"] for pack, pick in zip(packs, picks))


def test_real_premier_fixture_2026_11_09():
    """Trecho anonimizado do Player.log do primeiro draft real (Premier Draft de FRA, 2026-11-09):
    o P1P1 apareceu antes do pick, SelfPack/SelfPick e Pack/Pick começam em 1, e o fim do
    draft chega como DraftCompleteDraft sem DraftId."""
    from pathlib import Path
    text = (Path(__file__).parent / "fixtures" / "player-log-premier-fra-2026-11-09.txt").read_text("utf-8")
    events = arena_log.events_from_text(text)
    packs = [e for e in events if e["type"] == "pack"]
    picks = [e for e in events if e["type"] == "pick"]
    assert len(packs) == 42 and len(picks) == 42 and not [e for e in events if e["type"] == "pack_and_pick"]
    assert [(e["pack"], e["pick"]) for e in packs] == [(p, k) for p in (1, 2, 3) for k in range(1, 15)]
    assert [(e["pack"], e["pick"]) for e in picks] == [(e["pack"], e["pick"]) for e in packs]
    assert [len(e["cards"]) for e in packs][:3] == [14, 13, 12] and len(packs[-1]["cards"]) == 1
    assert packs[0]["source"] == "Draft.Notify" and picks[0]["card"] == 106314 and picks[0]["card"] in packs[0]["cards"]
    assert all(pick["card"] in pack["cards"] for pack, pick in zip(packs, picks))
    complete = [e for e in events if e["type"] == "complete"]
    assert complete and complete[0]["event"] == "PremierDraft_FRA_20260929"
    assert all(e["type"] != "unknown" for e in events)


def fake_arena_db(path):
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE Cards (GrpId INTEGER, ExpansionCode TEXT, CollectorNumber TEXT, Rarity INTEGER, "
               "DraftContent INTEGER, IsToken INTEGER, TitleId INTEGER)")
    db.execute("CREATE TABLE Localizations_enUS (LocId INTEGER, Formatted INTEGER, Loc TEXT)")
    db.execute("CREATE TABLE Localizations_ptBR (LocId INTEGER, Formatted INTEGER, Loc TEXT)")
    rows = [(101, "TST", "1", 2, 1, 0, 1), (102, "TST", "1", 4, 1, 0, 2), (103, "ZZZ", "9", 3, 1, 0, 3),
            (104, "TST", "1", 1, 0, 1, 4)]
    db.executemany("INSERT INTO Cards VALUES (?,?,?,?,?,?,?)", rows)
    db.executemany("INSERT INTO Localizations_enUS VALUES (?,?,?)",
                   [(1, 0, "Bear"), (1, 1, "Bear"), (2, 0, "Elk"), (3, 0, "Nameless Wonder"), (4, 0, "Bear Token")])
    db.executemany("INSERT INTO Localizations_ptBR VALUES (?,?,?)", [(1, 0, "Urso"), (2, 0, "Alce")])
    db.commit()
    db.close()


def test_arena_cards_resolve_by_name_then_printing(conn, tmp_path):  # noqa: F811
    path = tmp_path / "Raw_CardDatabase_abc.mtga"
    fake_arena_db(path)
    arena = arena_log.ArenaCards(path)
    assert len(arena) == 4 and [c["name_en"] for c in arena.draftable("tst")] == ["Bear", "Elk"]
    out = arena.resolve(conn, [101, 103, 999])
    assert out[0]["name"] == "Bear" and out[0]["card"]["name"] == "Bear" and out[0]["name_pt"] == "Urso"
    assert out[0]["rarity"] == "common"
    assert out[1]["name"] == "Nameless Wonder" and out[1]["card"] is None and out[1]["rarity"] == "uncommon"
    assert out[2]["name"] == "#999" and out[2]["card"] is None and out[2]["token"] is False
    token = arena.resolve(conn, [104])[0]        # ficha TST #1: mesmo número da carta real, fica com o nome dela
    assert token["name"] == "Bear Token" and token["card"] is None and token["token"] is True


def test_find_arena_db_picks_newest(tmp_path):
    raw = tmp_path / "MTGA_Data" / "Downloads" / "Raw"
    raw.mkdir(parents=True)
    (raw / "Raw_CardDatabase_old.mtga").write_bytes(b"1")
    newest = raw / "Raw_CardDatabase_new.mtga"
    newest.write_bytes(b"2")
    import os
    os.utime(raw / "Raw_CardDatabase_old.mtga", (1, 1))
    assert arena_log.find_arena_db(tmp_path) == newest
    assert arena_log.find_arena_db(tmp_path / "nada") is None


# --- partidas (teste do leitor sem gastar fichas) ---------------------------------------

def gre(turn=None, active=None, life=None, game=1):
    state = {"gameInfo": {"gameNumber": game}}
    if turn or active:
        state["turnInfo"] = {k: v for k, v in (("turnNumber", turn), ("activePlayer", active), ("phase", "Phase_Main1")) if v}
    if life:
        state["players"] = [{"systemSeatNumber": s, "lifeTotal": t} for s, t in life.items()]
    body = json.dumps({"transactionId": "t", "greToClientEvent": {"greToClientMessages": [{"gameStateMessage": state}]}})
    return f"{H}06/11/2026 23:16:36: Match to ME: GreToClientEvent\n" + body


def room(state, results=()):
    players = [{"userId": "ME", "playerName": "Eu", "systemSeatId": 1, "teamId": 1, "eventId": "Ladder", "platformId": "Windows"},
               {"userId": "OP", "playerName": "Rival", "systemSeatId": 2, "teamId": 2, "eventId": "Ladder", "platformId": "iOS"}]
    info = {"gameRoomConfig": {"reservedPlayers": players, "matchId": "m"}, "stateType": f"MatchGameRoomStateType_{state}"}
    if results:
        info["finalMatchResult"] = {"resultList": [{"scope": f"MatchScope_{s}", "winningTeamId": w} for s, w in results]}
    return f"{H}06/11/2026 23:16:36: Match to ME: MatchGameRoomStateChangedEvent\n" + json.dumps(
        {"matchGameRoomStateChangedEvent": {"gameRoomInfo": info}})


def test_match_session_from_log(conn, tmp_path):  # noqa: F811
    path = tmp_path / "Raw_CardDatabase_abc.mtga"
    fake_arena_db(path)
    deck_request = json.dumps({"EventName": "Ladder", "Summary": {"Name": "Ursos"},
                               "Deck": {"MainDeck": [{"cardId": 101, "quantity": 4}, {"cardId": 102, "quantity": 1}]}})
    text = "\n".join([
        f"{H}x\n<== Auth\n" + json.dumps({"authenticateResponse": {"clientId": "ME", "screenName": "Eu#123"}}),
        f"{H}==> EventSetDeckV3 " + json.dumps({"id": "d", "request": deck_request}),
        room("Playing"), gre(life={1: 20, 2: 20}), gre(turn=1, active=2), gre(turn=1, active=2),
        gre(turn=2, active=1, life={2: 17}), room("MatchCompleted", [("Game", 1), ("Match", 1)]),
    ])
    events = arena_log.events_from_text(text, arena_match.classify_match)
    assert [e["type"] for e in events] == ["login", "deck", "room", "game_state", "game_state", "game_state",
                                           "game_state", "room"]
    session = arena_match.MatchSession(conn, arena_log.ArenaCards(path), records_dir=tmp_path / "games")
    lines = [session.handle(e) for e in events]
    assert lines[0] == "conta: Eu#123"
    assert lines[1].startswith('deck enviado para Ladder: "Ursos" — 5 cartas · todas resolvidas') and "4 Bear" in lines[1]
    assert lines[2] == 'partida em Ladder: você (lugar 1) × Rival (lugar 2, iOS) · deck "Ursos"'
    assert lines[3] is None                                   # vida sem turno: ainda nos mulligans
    assert lines[4] == "jogo 1 · turno 1 (1º de Rival) · ativo: Rival · vida: você 20 × Rival 20"
    assert lines[5] is None                                   # repetição não sai de novo
    assert lines[6] == "jogo 1 · turno 2 (1º seu) · ativo: você · vida: você 20 × Rival 17"
    assert lines[7].startswith("fim da partida — game: vitória, match: vitória\nregistro: ")
    assert session.board().startswith("jogo 1 · turno 2") and "sua mão (0)" in session.board()
    saved = list((tmp_path / "games").glob("*-Ladder-Rival-g1.*"))
    assert sorted(p.suffix for p in saved) == [".json", ".md"]


def test_match_record_ignores_deck_of_another_event(conn, tmp_path):  # noqa: F811
    """2026-11-09: o Oráculo ficou aberto da Ladder ao draft e gravou as partidas do Premier
    Draft com o deck de Ladder. O deck só vale para o evento em que foi enviado."""
    path = tmp_path / "Raw_CardDatabase_abc.mtga"
    fake_arena_db(path)
    deck_request = json.dumps({"EventName": "PremierDraft_FRA_20260929", "Summary": {"Name": "Deck Draft"},
                               "Deck": {"MainDeck": [{"cardId": 101, "quantity": 23}]}})
    text = "\n".join([
        f"{H}x\n<== Auth\n" + json.dumps({"authenticateResponse": {"clientId": "ME", "screenName": "Eu#123"}}),
        f"{H}==> EventSetDeckV3 " + json.dumps({"id": "d", "request": deck_request}),
        room("Playing"), gre(life={1: 20, 2: 20}), gre(turn=1, active=2),
        room("MatchCompleted", [("Game", 1), ("Match", 1)]),
    ])
    events = arena_log.events_from_text(text, arena_match.classify_match)
    session = arena_match.MatchSession(conn, arena_log.ArenaCards(path), records_dir=tmp_path / "games")
    lines = [session.handle(e) for e in events]
    assert lines[1].startswith('deck enviado para PremierDraft_FRA_20260929: "Deck Draft"')
    assert lines[2].endswith(" · deck deste evento não visto no log")
    assert session.match_deck() is None and session.rows[-1]["deck"] is None
    record = json.loads(next((tmp_path / "games").glob("*.json")).read_text(encoding="utf-8"))
    assert record["deck"] is None
    assert next((tmp_path / "games").glob("*.md")).read_text(encoding="utf-8").startswith("# Ladder contra Rival\n")
