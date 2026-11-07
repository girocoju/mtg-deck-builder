import gzip
import json
from pathlib import Path

from mtg_builder import arena_game, arena_log, arena_match

NAMES = {101: "Bear", 102: "Forest", 103: "Elk", 104: "Imp", 105: "Drake"}


def zone(zone_id, kind, owner=None, ids=()):
    data = {"zoneId": zone_id, "type": f"ZoneType_{kind}", "visibility": "Visibility_Public"}
    if owner:
        data["ownerSeatId"] = owner
    if ids:
        data["objectInstanceIds"] = list(ids)
    return data


def obj(instance, grp, zone_id, owner, types=("CardType_Creature",), power=None, toughness=None, **extra):
    data = {"instanceId": instance, "grpId": grp, "type": "GameObjectType_Card", "zoneId": zone_id,
            "visibility": "Visibility_Public", "ownerSeatId": owner, "controllerSeatId": owner,
            "cardTypes": [f"{t}" for t in types]}
    if power is not None:
        data["power"], data["toughness"] = {"value": power}, {"value": toughness}
    data.update(extra)
    return data


def ann(kind, affected, details=None, affector=None):
    data = {"id": 1, "type": [f"AnnotationType_{kind}"], "affectedIds": list(affected), "details": []}
    if affector is not None:
        data["affectorId"] = affector
    for key, value in (details or {}).items():
        field = "valueString" if isinstance(value, str) else "valueInt32"
        data["details"].append({"key": key, field: [value]})
    return data


def full():
    return {"type": "GameStateType_Full", "gameInfo": {"gameNumber": 1},
            "zones": [zone(27, "Stack"), zone(28, "Battlefield"), zone(29, "Exile"), zone(31, "Hand", 1),
                      zone(32, "Library", 1, range(1000, 1060)), zone(33, "Graveyard", 1), zone(35, "Hand", 2),
                      zone(36, "Library", 2, range(2000, 2060)), zone(37, "Graveyard", 2)],
            "players": [{"systemSeatNumber": 1, "lifeTotal": 20}, {"systemSeatNumber": 2, "lifeTotal": 20}],
            "turnInfo": {"turnNumber": 1, "activePlayer": 2, "phase": "Phase_Beginning", "step": "Step_Upkeep"}}


def tracker():
    return arena_game.GameTracker(lambda grp: NAMES.get(grp, f"#{grp}"), my_seat=1, seat_names={2: "Rival"})


def test_full_state_then_draws_plays_and_casts():
    t = tracker()
    assert t.apply(full()) == ["jogo 1 · turno 1 (1º de Rival) · ativo: Rival · vida: você 20 × Rival 20"]
    draw = {"type": "GameStateType_Diff", "zones": [zone(31, "Hand", 1, [101]), zone(32, "Library", 1, range(1000, 1059))],
            "gameObjects": [obj(101, 101, 31, 1, visibility="Visibility_Private")],
            "annotations": [ann("ZoneTransfer", [101], {"zone_src": 32, "zone_dest": 31, "category": "Draw"})]}
    assert t.apply(draw) == ["você compra Bear"]
    opp_draw = {"type": "GameStateType_Diff", "zones": [zone(35, "Hand", 2, [500])],
                "annotations": [ann("ZoneTransfer", [500], {"zone_src": 36, "zone_dest": 35, "category": "Draw"})]}
    assert t.apply(opp_draw) == ["Rival compra uma carta"]
    land = {"type": "GameStateType_Diff", "zones": [zone(28, "Battlefield", ids=[102])],
            "gameObjects": [obj(102, 102, 28, 1, types=("CardType_Land",))],
            "annotations": [ann("ZoneTransfer", [102], {"zone_src": 31, "zone_dest": 28, "category": "PlayLand"})]}
    assert t.apply(land) == ["você joga Forest"]
    cast = {"type": "GameStateType_Diff", "zones": [zone(27, "Stack", ids=[103])],
            "gameObjects": [obj(103, 103, 27, 1, power=4, toughness=4)],
            "annotations": [ann("ZoneTransfer", [103], {"zone_src": 31, "zone_dest": 27, "category": "CastSpell"})]}
    assert t.apply(cast) == ["você conjura Elk"]
    resolve = {"type": "GameStateType_Diff", "zones": [zone(27, "Stack"), zone(28, "Battlefield", ids=[102, 203])],
               "gameObjects": [obj(203, 103, 28, 1, power=4, toughness=4, hasSummoningSickness=True)],
               "annotations": [ann("ObjectIdChanged", [103], {"orig_id": 103, "new_id": 203}),
                               ann("ZoneTransfer", [203], {"zone_src": 27, "zone_dest": 28, "category": "Resolve"})]}
    assert t.apply(resolve) == ["Elk entra em campo"]
    assert 103 not in t.objects and t.objects[203]["grpId"] == 103
    board = t.board_text()
    assert "sua mão (1): Bear" in board and "seu campo: Forest | Elk 4/4 (enjoo)" in board
    assert "Rival: mão 1 · biblioteca 60 · mana aberta 0  |  você: biblioteca 59 · mana aberta 1" in board
    assert "cemitério: —" in board and "exílio: —" in board


def test_attack_damage_death_exile_and_game_over():
    t = tracker()
    t.apply(full())
    t.apply({"type": "GameStateType_Diff", "zones": [zone(28, "Battlefield", ids=[203, 300])],
             "gameObjects": [obj(203, 103, 28, 1, power=4, toughness=4), obj(300, 104, 28, 2, power=2, toughness=2)]})
    turn = {"type": "GameStateType_Diff", "turnInfo": {"turnNumber": 3, "activePlayer": 1, "phase": "Phase_Main1"},
            "players": [{"systemSeatNumber": 1, "lifeTotal": 20}, {"systemSeatNumber": 2, "lifeTotal": 3}]}
    assert t.apply(turn) == ["jogo 1 · turno 3 (1º seu) · ativo: você · vida: você 20 × Rival 3"]
    assert t.own_turns == {2: 1, 1: 1} and t.snapshot()["own_turn"] == 1
    hints = t.hints()
    assert hints[0].startswith("LETAL na mesa: 4 de poder podem atacar contra 3 de vida (sem contar 1 bloqueador")
    attack = {"type": "GameStateType_Diff", "turnInfo": {"turnNumber": 3, "activePlayer": 1, "phase": "Phase_Combat",
                                                         "step": "Step_DeclareAttack"},
              "gameObjects": [obj(203, 103, 28, 1, power=4, toughness=4, isTapped=True,
                                  attackState="AttackState_Declared", attackInfo={"targetId": 2})]}
    assert t.apply(attack) == ["você ataca com Elk 4/4 (virada, atacando)"]
    assert t.apply(attack) == []                                   # mesmo ataque não repete
    damage = {"type": "GameStateType_Diff",
              "players": [{"systemSeatNumber": 1, "lifeTotal": 20}, {"systemSeatNumber": 2, "lifeTotal": -1}],
              "annotations": [ann("DamageDealt", [2], {"damage": 4, "type": 3}, affector=203),
                              ann("ModifiedLife", [2], {"life": -4})]}
    assert t.apply(damage) == ["Elk causa 4 de dano em Rival", "vida de Rival: -1 (-4)"]
    death = {"type": "GameStateType_Diff", "zones": [zone(28, "Battlefield", ids=[203]), zone(37, "Graveyard", 2, [301])],
             "gameObjects": [obj(301, 104, 37, 2)],
             "annotations": [ann("ObjectIdChanged", [300], {"orig_id": 300, "new_id": 301}),
                             ann("ZoneTransfer", [301], {"zone_src": 28, "zone_dest": 37, "category": "SBA_Damage"})]}
    assert t.apply(death) == ["Imp morre"]
    exile = {"type": "GameStateType_Diff", "zones": [zone(37, "Graveyard", 2), zone(29, "Exile", ids=[302])],
             "gameObjects": [obj(302, 104, 29, 2)],
             "annotations": [ann("ObjectIdChanged", [301], {"orig_id": 301, "new_id": 302}),
                             ann("ZoneTransfer", [302], {"zone_src": 37, "zone_dest": 29, "category": "Unknown"})]}
    assert t.apply(exile) == ["Imp: cemitério de Rival → exílio (Unknown)"]
    over = {"type": "GameStateType_Diff", "gameInfo": {"gameNumber": 1, "stage": "GameStage_GameOver",
                                                        "results": [{"scope": "MatchScope_Game", "winningTeamId": 1}]}}
    assert t.apply(over) == ["fim do jogo — game: vitória"]
    board = t.board_text()
    assert "exílio: Rival — Imp" in board and "cartas vistas de Rival: Imp" in board
    record = t.record()
    assert record["result"] == "game: vitória" and record["turns"] == 3 and len(record["events"]) == 8
    assert [e["turn"] for e in record["events"]][:2] == [1, 3]
    text = t.markdown("Teste")
    assert "**Turno 3**" in text and "- Elk causa 4 de dano em Rival" in text and "## Mesa final" in text


def test_real_ladder_match_replays_without_errors(tmp_path):
    """Partida real de 2026-11-07 (anonimizada): o rastreador segue mão, campos, ataques e
    dano do começo ao fim sem a base de cartas (nomes como #grpId)."""
    fixture = Path(__file__).parent / "fixtures" / "player-log-ladder-2026-11-07.txt.gz"
    log = tmp_path / "Player.log"
    log.write_bytes(gzip.decompress(fixture.read_bytes()))
    follower = arena_log.LogFollower(log, from_start=True, classifier=arena_match.classify_match)
    session = arena_match.MatchSession(records_dir=tmp_path / "games")
    lines = []
    for event in follower.poll():
        text = session.handle(event)
        if text:
            lines.append(text)
    joined = "\n".join(lines)
    assert "partida em Ladder: você (lugar 1) × Oponente (lugar 2" in joined
    assert "turno 10 (5º seu) · ativo: você" in joined and "causa 15 de dano" in joined
    assert "você ataca com" in joined and "você conjura" in joined and "Oponente joga" in joined
    assert joined.rstrip().endswith("match: vitória") or "fim do jogo — game: vitória" in joined
    tracker = session.tracker
    assert tracker.life == {1: 16, 2: -11} and tracker.over
    draws = [e for e in tracker.events if e["text"].startswith("você compra")]
    assert len(draws) == 5 and [e["turn"] for e in draws] == [2, 4, 6, 8, 10]   # jogou depois: compra nos pares
    record = json.loads(next((tmp_path / "games").glob("*.json")).read_text("utf-8"))
    assert record["result"] and record["deck"]["name"] == "Turn 2 Kill" and len(record["events"]) > 60
