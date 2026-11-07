import random

from mtg_builder import draft_pick, draft_sim
from test_decks import conn  # noqa: F401
from test_draft import site, snap  # noqa: F401


def test_boosters_have_fourteen_cards():
    for code in ("fra", "nao-existe"):
        booster = draft_sim.load_booster(code)
        assert sum(s["count"] for s in booster["slots"]) == 14
        assert booster["source"] and booster["collected_at"]
    assert draft_sim.load_booster("fra")["generic"] is False
    assert draft_sim.load_booster("nao-existe")["generic"] is True
    paper = draft_sim.load_booster("fra", "paper")
    assert paper["profile"] == "paper" and sum(s["count"] for s in paper["slots"]) == 14
    import pytest
    with pytest.raises(RuntimeError, match="Perfil de colação"):
        draft_sim.load_booster("fra", "inexistente")


def test_pools_and_packs_from_the_base(conn):  # noqa: F811
    pools, basis = draft_sim.card_pools(conn, "tst")
    assert basis == "impressões de booster na base"
    assert "Elk" in pools["rare"] and "Wolf" in pools["mythic"] and "Drake" in pools["uncommon"]
    assert "Forest" in pools["basic"] and len(pools["common"]) > 100
    rng = random.Random(1)
    booster = draft_sim.load_booster("tst")
    for _ in range(20):
        pack = draft_sim.make_pack(rng, pools, booster)
        assert len(pack) == 14 and len(set(pack)) == 14
        assert sum(1 for c in pack if c in pools["rare"] + pools["mythic"]) >= 1


def test_pools_follow_the_17lands_list(conn, site):  # noqa: F811
    pools, basis = draft_sim.card_pools(conn, "tst", snap(conn, site))
    assert basis == "lista de cartas do 17Lands"
    assert sorted(pools["common"]) == ["Bear", "Imp", "Rat Swarm", "Wolf"] and pools["rare"] == ["Elk"]


def test_full_table_with_bots(conn, site):  # noqa: F811
    engine = draft_pick.Engine(conn, draft_pick.Ratings(snap(conn, site)), "tst")
    rng = random.Random(7)
    chosen = []

    def choose(result, names):
        chosen.append(result["cartas"][0]["name"])
        return result["cartas"][0]["name"]

    states = draft_sim.run_table(conn, engine, "tst", rng, human_seat=0, choose=choose)
    assert len(states) == 8 and all(len(s.picked_names()) == 42 for s in states)
    assert states[0].picked_names() == chosen and states[0].event == "simulado"
    summary = draft_sim.summarize(engine, states)
    assert all(s["picks"] == 42 for s in summary) and sum(sum(s["rarities"].values()) for s in summary) == 336
