import json

from mtg_builder import draft, draft_pick
from test_decks import conn  # noqa: F401
from test_draft import site, snap  # noqa: F401


def engine_for(conn, site):  # noqa: F811
    snapshot = snap(conn, site)
    ratings = draft_pick.Ratings(snapshot)
    return draft_pick.Engine(conn, ratings, "tst", "premier"), ratings


def test_first_pick_is_raw_power(conn, site):  # noqa: F811
    engine, ratings = engine_for(conn, site)
    state = draft_pick.DraftState("tst")
    result = engine.rank(state, 1, 1, ["Bear", "Elk", "Drake", "Imp"])
    names = [r["name"] for r in result["cartas"]]
    assert names[0] == "Elk" and result["compromisso"] == 0 and result["par"] is None
    top = result["cartas"][0]
    assert top["poder"] == 8.0 and top["encaixe"] == 0 and top["necessidade"] == 0 and top["fonte"] == "17lands"
    assert top["flexibilidade"] == draft_pick.WEIGHTS["flex_mono"]      # mono mantém o draft aberto
    assert ratings.describe().startswith("17Lands 2026-")


def test_commitment_pulls_towards_chosen_colors(conn, site):  # noqa: F811
    engine, _ = engine_for(conn, site)
    state = draft_pick.DraftState("tst")
    state.add_picks(["Elk", "Bear", "Bear", "Bear", "Imp", "Imp"])
    result = engine.rank(state, 2, 8, ["Drake", "Bear", "Seven Gnomes"])
    by_name = {r["name"]: r for r in result["cartas"]}
    assert result["compromisso"] == 1.0 and result["par"] == "BG" and set(result["cores"]) == {"G", "B"}
    assert by_name["Drake"]["encaixe"] == draft_pick.WEIGHTS["nao_cabe"]
    assert by_name["Bear"]["encaixe"] == draft_pick.WEIGHTS["cabe"]
    assert by_name["Bear"]["necessidade"] > 0                             # criaturas ainda faltam
    assert [r["name"] for r in result["cartas"]][0] == "Bear"


def test_cards_without_sample_fall_back_in_order(conn, site):  # noqa: F811
    snapshot = snap(conn, site)
    untapped = {"source": "untapped", "collected_at": "2026-10-12", "baseline": 0.5,
                "cards": {"rat swarm": {"name": "Rat Swarm", "games": 900, "wr": 0.58}}}
    draftsim = {"source": "draftsim", "cards": {"wolf": 4.0}}
    ratings = draft_pick.Ratings(snapshot, untapped, draftsim)
    engine = draft_pick.Engine(conn, ratings, "tst")
    result = engine.rank(draft_pick.DraftState("tst"), 1, 1, ["Rat Swarm", "Wolf", "Old Relic"])
    by_name = {r["name"]: r for r in result["cartas"]}
    assert by_name["Rat Swarm"]["fonte"] == "untapped" and by_name["Rat Swarm"]["poder"] == 8.0
    assert by_name["Wolf"]["fonte"] == "draftsim*" and by_name["Wolf"]["poder"] == 3.0 and by_name["Wolf"]["teorica"]
    assert by_name["Old Relic"]["fonte"] == "teorica*"
    text = draft_pick.format_ranking(result, title="T · ", sources=ratings.describe())
    assert "nota teórica" in text and "Untapped 2026-10-12" in text and "Rat Swarm" in text


def test_signal_and_wheel():
    assert draft_pick.wheel_probability(None, 1) is None
    assert draft_pick.wheel_probability(9.0, 7) == 0.0
    assert abs(draft_pick.wheel_probability(9.0, 1) - 0.5) < 1e-6
    assert draft_pick.commitment(0) == 0 and draft_pick.commitment(10) == 0.5 and draft_pick.commitment(40) == 1


def test_late_strong_card_is_a_signal(conn, site):  # noqa: F811
    engine, _ = engine_for(conn, site)
    state = draft_pick.DraftState("tst")
    result = engine.rank(state, 1, 6, ["Elk", "Imp"])                  # Elk costuma sair no pick 1,8
    elk = next(r for r in result["cartas"] if r["name"] == "Elk")
    assert elk["sinal"] == round(min(draft_pick.WEIGHTS["sinal_max"], (6 - 1.8) * draft_pick.WEIGHTS["sinal_por_pick"]), 2)


def test_state_round_trip(tmp_path):
    state = draft_pick.DraftState("tst", "quick", "QuickDraft_TST_20261107", snapshot="2026-11-07")
    state.record_pack(1, 1, ["Bear", "Elk"], [{"name": "Elk"}])
    state.record_pick(1, 1, "Elk")
    state.record_pick(1, 2, "Bear")
    path = state.save(tmp_path / "d.json")
    loaded = draft_pick.DraftState.load(path)
    assert loaded.picked_names() == ["Elk", "Bear"] and loaded.next_position() == (1, 3)
    assert loaded.view(1, 1)["seen"] == ["Bear", "Elk"] and loaded.event == "QuickDraft_TST_20261107"
    assert json.loads(path.read_text("utf-8"))["pool"] == ["Elk", "Bear"]
    full = draft_pick.DraftState("tst")
    full.add_picks(["Bear"] * 14)
    assert full.next_position() == (2, 1)


def test_dated_snapshots_migrate_and_keep_history(conn, site):  # noqa: F811
    from mtg_builder import db
    legacy = db.DATA_DIR / "17lands" / "tst" / "premier.json"
    legacy.parent.mkdir(parents=True)
    legacy.write_text(json.dumps({"collected_at": "2026-10-12T10:00:00", "cards": [], "colors": [],
                                  "has_data": False, "event": "PremierDraft"}), encoding="utf-8")
    assert draft.cached("tst", "premier")["collected_at"].startswith("2026-10-12") and not legacy.exists()
    assert draft.snapshots("tst", "premier") == ["2026-10-12"]
    fresh = snap(conn, site, force=True)
    assert draft.snapshots("tst", "premier")[0] == fresh["collected_at"][:10]
    assert draft.cached("tst", "premier", "2026-10-12")["has_data"] is False
    assert draft.cached("tst", "premier")["has_data"] is True


def test_secondary_sources_are_read_from_disk(conn, site):  # noqa: F811
    from mtg_builder import db
    folder = db.DATA_DIR / "untapped" / "tst" / "premier"
    folder.mkdir(parents=True)
    raw = {"metadata": {}, "data": {"7": {"ALL": {"b": [[10, 5, 10, [10]], [600, 330], [1]],
                                                  "g": [[10, 5, 10, [10]], [400, 210]]}},
                                     "8": {"ALL": {"b": [[1, 1, 1, [1]], [1]]}}}}
    (folder / "2026-11-07-card-stats.json").write_text(json.dumps(raw), encoding="utf-8")
    (folder / "titles.json").write_text(json.dumps({"7": ["Bear", 2, "o1oG", "1"], "8": ["Elk", 4, "", "2"]}),
                                        encoding="utf-8")
    untapped = draft.untapped_ratings("tst", "premier")
    assert untapped["cards"]["bear"] == {"name": "Bear", "games": 1000, "wr": 0.54}
    assert untapped["cards"]["elk"]["games"] == 1                      # amostra ínfima: o motor filtra
    assert untapped["baseline"] == round(540 / 1001, 4)
    sim = db.DATA_DIR / "fontes" / "draft-tst-2026" / "draftsim-pickorder"
    sim.mkdir(parents=True)
    (sim / "TST.tsv").write_text("Name\tName_2\tRating\nBig_Bear\t\t3.5\nFire\tIce\t4.1\nBroken\t\tx\n", encoding="utf-8")
    draftsim = draft.draftsim_ratings("tst")
    assert draftsim["cards"] == {"big bear": 3.5, "fire": 4.1}
    assert draft.untapped_ratings("zzz") is None and draft.draftsim_ratings("zzz") is None
