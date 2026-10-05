import urllib.error

import pytest

from mtg_builder import analysis, db, decklist, edhrec
from test_decks import conn  # noqa: F401  (fixture com Ivy, Jace, Tana, Kraum, Bear, Imp, Wolf...)

COMMANDER_PAGE = {
    "creature": 23, "land": 35, "tag_counts": [{"value": "Auras", "count": 640}],
    "bracket_counts": {"2": 961},
    "container": {"json_dict": {
        "card": {"name": "Ivy", "num_decks": 1000},
        "cardlists": [
            {"header": "Top Cards", "cardviews": [
                {"name": "Drake", "synergy": 0.71, "num_decks": 700, "potential_decks": 1000},
                {"name": "Imp", "synergy": 0.50, "num_decks": 500, "potential_decks": 1000},
                {"name": "Broken Orb", "synergy": 0.10, "num_decks": 300, "potential_decks": 1000},
                {"name": "Wolf", "synergy": 0.30, "num_decks": 200, "potential_decks": 1000},
                {"name": "Carta Que Não Existe", "synergy": 0.2, "num_decks": 1, "potential_decks": 1000},
            ]},
            {"header": "Creatures", "cardviews": [
                {"name": "Drake", "synergy": 0.71, "num_decks": 700, "potential_decks": 1000},
                {"name": "Bear", "synergy": -0.05, "num_decks": 100, "potential_decks": 1000},
            ]},
        ]}},
}
AVERAGE_PAGE = {"deck": {"commander": ["Ivy"], "cards": {
    "Creature": [["Drake", 1], ["Imp", 1], ["Wolf", 1]], "Land": [["Forest", 12], ["Island", 11]]}}}


class FakeEdhrec:
    def __init__(self):
        self.calls = []

    def __call__(self, url):
        self.calls.append(url)
        if "nao-existe" in url:
            raise urllib.error.HTTPError(url, 403, "Forbidden", None, None)
        return dict(AVERAGE_PAGE if "average-decks" in url else COMMANDER_PAGE)


@pytest.fixture
def site(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DATA_DIR", tmp_path / "data")
    return FakeEdhrec()


def test_slug():
    assert edhrec.slug("Ivy, Gleeful Spellthief") == "ivy-gleeful-spellthief"
    assert edhrec.slug("Yuriko, the Tiger's Shadow") == "yuriko-the-tigers-shadow"
    assert edhrec.slug("Dáin // Outra Face") == "dain"


def test_recommendations_are_checked_against_format_platform_and_identity(conn, site):
    data = edhrec.recommendations(conn, ["Ivy"], "brawl", "arena", fetch=site)
    status = {c["name"]: c["status"] for c in data["cards"]}
    assert status == {
        "Drake": "ok", "Bear": "ok",
        "Imp": "fora da identidade",       # preta num deck GU
        "Broken Orb": "não legal",          # só legal em commander
        "Wolf": "fora de arena",
        "Carta Que Não Existe": "fora da base",
    }
    drake = next(c for c in data["cards"] if c["name"] == "Drake")
    assert drake["inclusion"] == 70.0 and drake["synergy"] == 0.71 and drake["category"] == "Top Cards"
    assert data["source"] == "edhrec" and data["fetched_at"] and data["decks"] == 1000
    assert site.calls == ["https://json.edhrec.com/pages/commanders/ivy.json"]
    # em Commander de papel o filtro muda: Broken Orb e Wolf passam
    paper = {c["name"]: c["status"] for c in edhrec.recommendations(conn, ["Ivy"], "commander", "paper", fetch=site)["cards"]}
    assert paper["Broken Orb"] == "ok" and paper["Wolf"] == "ok"


def test_cache_avoids_second_request_and_force_refetches(conn, site):
    edhrec.recommendations(conn, ["Ivy"], fetch=site)
    edhrec.recommendations(conn, ["Ivy"], "brawl", fetch=site)
    assert len(site.calls) == 1
    edhrec.recommendations(conn, ["Ivy"], force=True, fetch=site)
    assert len(site.calls) == 2


def test_missing_commander_page_is_a_clear_error(conn, site):
    with pytest.raises(RuntimeError, match="não tem página"):
        edhrec.recommendations(conn, ["Nao Existe"], fetch=site)


def test_average_deck_separates_usable_cards(conn, site):
    data = edhrec.average_deck(conn, ["Ivy"], "brawl", "arena", fetch=site)
    assert [(i["qty"], i["name"]) for i in data["kept"]] == [(1, "Drake"), (12, "Forest"), (11, "Island")]
    assert {i["name"]: i["status"] for i in data["dropped"]} == {"Imp": "fora da identidade", "Wolf": "fora de arena"}
    assert data["kept_count"] == 24 and data["dropped_count"] == 2


def test_commander_report_accepts_and_refuses_with_reason(conn):
    ok = edhrec.commander_report(conn, ["Ivy"], "brawl")
    assert ok["ok"] and ok["identity"] == "UG" and ok["deck_size"] == 100
    assert edhrec.commander_report(conn, ["Jace"], "brawl")["ok"]
    bad = edhrec.commander_report(conn, ["Jace"], "commander")
    assert not bad["ok"] and "exige criatura lendária." in bad["problems"][0]
    assert "não é legal em standardbrawl" in edhrec.commander_report(conn, ["Ivy"], "standardbrawl")["problems"][0]
    assert "Carta não encontrada" in edhrec.commander_report(conn, ["Ivi"], "brawl")["problems"][0]
    assert "não podem ser comandantes juntos" in edhrec.commander_report(conn, ["Ivy", "Tana"], "commander")["problems"][0]
    assert edhrec.commander_report(conn, ["Tana", "Kraum"], "commander")["ok"]
    assert "não é um formato com comandante" in edhrec.commander_report(conn, ["Ivy"], "standard")["problems"][0]


def test_analysis_reports_commander_proportions_scaled_by_deck_size(conn):
    deck = decklist.parse("Commander\n1 Ivy\n\nDeck\n" + "\n".join(f"1 Filler {i}" for i in range(63))
                          + "\n18 Forest\n18 Island\n")
    assert decklist.resolve(conn, deck) == []
    lands = analysis.analyze(deck)["proporcoes"][0]
    assert lands == {"categoria": "Terrenos", "tem": 36, "alvo": [36, 38], "situacao": "dentro"}
    small = decklist.parse("Commander\n1 Ivy\n\nDeck\n" + "\n".join(f"1 Filler {i}" for i in range(39))
                           + "\n10 Forest\n10 Island\n")
    decklist.resolve(conn, small)
    by_name = {p["categoria"]: p for p in analysis.analyze(small)["proporcoes"]}
    assert by_name["Terrenos"]["alvo"] == [22, 23] and by_name["Terrenos"]["situacao"] == "abaixo"
    assert by_name["Aceleração"]["alvo"] == [5, 7]
    no_commander = decklist.parse("36 Bear\n24 Forest\n")
    decklist.resolve(conn, no_commander)
    assert analysis.analyze(no_commander)["proporcoes"] == []
