from datetime import date

import pytest

from mtg_builder import db, draft
from test_decks import conn  # noqa: F401  (cartas na coleção "tst")


def rating(name, color, rarity, gih, alsa, games=2000, oh=None, iwd=0.02):
    return {"name": name, "color": color, "rarity": rarity, "game_count": games * 2,
            "ever_drawn_game_count": games, "ever_drawn_win_rate": gih, "opening_hand_win_rate": oh or gih,
            "drawn_win_rate": gih, "win_rate": 0.55, "drawn_improvement_win_rate": iwd,
            "avg_seen": alsa, "avg_pick": alsa}


CARDS = [
    rating("Bear", "G", "common", 0.60, 7.5),          # rende muito, sai tarde
    rating("Elk", "G", "rare", 0.63, 1.8),
    rating("Drake", "U", "uncommon", 0.52, 2.0),       # sai cedo, rende pouco
    rating("Imp", "B", "common", 0.56, 4.0),
    rating("Wolf", "G", "common", 0.58, 5.0, games=100),   # amostra pequena
    rating("Fire // Ice", "UR", "uncommon", 0.59, 3.0),
    {**rating("Rat Swarm", "B", "common", None, 6.0, games=10), "ever_drawn_win_rate": None},
]
COLORS = [
    {"is_summary": True, "color_name": "All Decks", "short_name": "All", "wins": 5500, "games": 10000},
    {"is_summary": True, "color_name": "Two-color", "short_name": 2, "wins": 4000, "games": 7000},
    {"is_summary": False, "color_name": "Simic (GU)", "short_name": "GU", "wins": 1800, "games": 3000},
    {"is_summary": False, "color_name": "Dimir (UB)", "short_name": "UB", "wins": 1300, "games": 2600},
    {"is_summary": False, "color_name": "Rare pair", "short_name": "WR", "wins": 90, "games": 100},
]


class Fake17Lands:
    def __init__(self, cards=CARDS):
        self.calls, self.cards = [], cards

    def __call__(self, url):
        self.calls.append(url)
        return COLORS if "color_ratings" in url else self.cards


@pytest.fixture
def site(conn, tmp_path, monkeypatch):  # noqa: F811
    monkeypatch.setattr(db, "DATA_DIR", tmp_path / "data")
    conn.execute("INSERT INTO sets (code, name, set_type, released_at, arena_code) "
                 "VALUES ('tst', 'Test Set', 'expansion', '2026-10-02', 'tst')")
    return Fake17Lands()


def snap(conn, site, mode="premier", **kw):  # noqa: F811
    return draft.update(conn, "tst", mode, fetch=site, today=date(2026, 10, 5), **kw)


def test_update_builds_dated_snapshot_with_baseline(conn, site):  # noqa: F811
    s = snap(conn, site)
    assert s["source"] == "17lands" and s["mode"] == "premier" and s["event"] == "PremierDraft"
    assert s["has_data"] and s["games"] == 10000 and s["baseline"] == 0.55 and s["collected_at"]
    assert "expansion=TST&format=PremierDraft" in site.calls[0]
    assert "start_date=2026-09-22" in site.calls[1] and "end_date=2026-10-05" in site.calls[1]


def test_modes_are_cached_separately(conn, site):  # noqa: F811
    snap(conn, site)
    snap(conn, site)
    assert len(site.calls) == 2                      # segunda chamada usa o cache
    quick = snap(conn, site, mode="quick")
    assert quick["event"] == "QuickDraft" and len(site.calls) == 4
    assert draft.cached("tst", "premier")["event"] == "PremierDraft"
    assert draft.cached("tst", "trad") is None
    snap(conn, site, force=True)
    assert len(site.calls) == 6
    with pytest.raises(RuntimeError, match="Modo desconhecido"):
        draft.update(conn, "tst", "cube", fetch=site)


def test_set_without_data_is_flagged(conn, site):  # noqa: F811
    site.cards = [{**c, "ever_drawn_win_rate": None} for c in CARDS]
    assert snap(conn, site)["has_data"] is False
    with pytest.raises(RuntimeError, match="Coleção não encontrada"):
        draft.update(conn, "inexistente", fetch=site)


def test_ranking_filters_small_samples_color_and_rarity(conn, site):  # noqa: F811
    s = snap(conn, site)
    assert [c["name"] for c in draft.ranking(s)] == ["Elk", "Bear", "Fire // Ice", "Imp", "Drake"]
    assert [c["name"] for c in draft.ranking(s, color="G", rarity="common")] == ["Bear"]
    assert [c["name"] for c in draft.ranking(s, color="G", min_games=50)] == ["Elk", "Bear", "Wolf"]
    assert [c["name"] for c in draft.ranking(s, color="multi")] == ["Fire // Ice"]
    assert [c["name"] for c in draft.ranking(s, sort="alsa", limit=2)] == ["Elk", "Drake"]


def test_color_pairs_and_rate(conn, site):  # noqa: F811
    s = snap(conn, site)
    assert [(c["short"], c["win_rate"]) for c in draft.color_pairs(s)] == [("GU", 0.6), ("UB", 0.5)]
    found, missing = draft.rate(s, ["bear", "Fire", "Carta Que Não Existe"])
    assert [c["name"] for c in found] == ["Bear", "Fire // Ice"] and missing == ["Carta Que Não Existe"]


def test_over_and_under_rated(conn, site):  # noqa: F811
    gaps = draft.over_under(snap(conn, site), top=1)
    assert gaps["subestimadas"][0]["name"] == "Bear" and gaps["superestimadas"][0]["name"] == "Drake"


def test_set_overview_uses_17lands_list_or_falls_back_to_the_base(conn, site):  # noqa: F811
    theory = draft.set_overview(conn, "tst")
    assert theory["basis"] == "impressões de booster na base" and theory["cards"] > 100
    assert theory["colors"]["G"]["common"] > 0
    data = draft.set_overview(conn, "tst", snap(conn, site))
    assert data["basis"] == "lista de cartas do 17Lands" and data["cards"] == 7
    green = data["colors"]["G"]
    assert green["total"] == 3 and green["common"] == 2 and green["rare"] == 1   # raridade do 17Lands
    assert green["criaturas_cu"] == 2 and green["curva_criaturas_cu"] == {"1": 2}
    assert list(data["colors"]) == ["U", "B", "G", "multi"]
