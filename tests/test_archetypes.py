from mtg_builder import archetypes, draft_pick
from test_decks import conn  # noqa: F401
from test_draft import site, snap  # noqa: F401

DATA = {"set": "tst", "source": "teste", "archetypes": {
    "BG": {"name": "Enxame", "plan": "muitas cartas iguais", "payoffs": ["re:any number of cards named"],
           "enablers": ["kw:Partner", "stat:cmc<=1&creature"]},
    "GU": {"name": "Lendas", "plan": "", "payoffs": ["type:Legendary"], "enablers": []},
}}


def test_patterns_and_tags(conn):  # noqa: F811
    index = {row["name"]: row for row in conn.execute("SELECT * FROM cards")}
    tagger = archetypes.Tagger(DATA)
    assert tagger.tags(index["Rat Swarm"]) == {"BG": 1.0}                   # payoff pelo texto
    assert tagger.tags(index["Tana"]) == {"BG": 0.5, "GU": 1.0}              # enabler (Partner) e lenda
    assert tagger.tags(index["Bear"]) == {"BG": 0.5}                         # criatura de custo 1
    assert tagger.tags(index["Broken Orb"]) == {}                            # artefato sem nada
    assert archetypes.Tagger.label(tagger.tags(index["Tana"])) == "GU+ BG"
    assert tagger.name("BG") == "Enxame" and not archetypes.Tagger(None)
    assert archetypes.matches(index["Fire // Ice"], "type:Instant")
    assert archetypes.load("nao-existe") is None and archetypes.load("fra")["set"] == "fra"


def test_synergy_component_in_ranking(conn, site):  # noqa: F811
    engine = draft_pick.Engine(conn, draft_pick.Ratings(snap(conn, site)), "tst", archetype_data=DATA)
    state = draft_pick.DraftState("tst")
    state.add_picks(["Elk", "Bear", "Bear", "Imp", "Imp", "Imp"])             # par BG
    result = engine.rank(state, 2, 8, ["Rat Swarm", "Seven Gnomes"])
    by_name = {r["name"]: r for r in result["cartas"]}
    assert result["par"] == "BG" and result["arquetipo"] == "Enxame"
    assert by_name["Rat Swarm"]["sinergia"] == draft_pick.WEIGHTS["sinergia"]        # payoff, compromisso pleno
    assert by_name["Seven Gnomes"]["sinergia"] == draft_pick.WEIGHTS["sinergia"] / 2  # custo 1: enabler
    assert by_name["Rat Swarm"]["arquetipos"] == "BG+"
    text = draft_pick.format_ranking(result)
    assert "(Enxame)" in text and "· BG+" in text and " sin " in text
    early = engine.rank(draft_pick.DraftState("tst"), 1, 1, ["Rat Swarm"])
    assert early["cartas"][0]["sinergia"] == 0 and early["cartas"][0]["arquetipos"] == "BG+"


def test_report_measures_signal(conn, site):  # noqa: F811
    ratings = draft_pick.Ratings(snap(conn, site))
    data = archetypes.report(conn, "tst", ratings, archetypes.Tagger(DATA), top=3)
    bg = next(a for a in data["archetypes"] if a["pair"] == "BG")
    assert bg["name"] == "Enxame" and bg["win_rate"] is None and bg["tagged"] >= 2 and bg["payoffs"] >= 1
    assert [b["name"] for b in bg["best"][:2]] == ["Elk", "Bear"]                 # +8 e +5 pontos, com amostra
    assert bg["best"][0]["role"] == "enabler" and bg["best"][0]["points"] == 8.0
    assert bg["tagged_mean"] is not None and bg["tagged_n"] >= 2
    text = archetypes.format_report(data)
    assert "BG Enxame" in text and "marcadas:" in text and "Bear" in text and "diferença" in text


def test_shipped_archetype_files_compile():
    """Todo arquivo real em archetypes/ tem dez pares, padrões válidos (regex compilável, prefixo
    conhecido) e ganchos com needs, provides e peso."""
    import json
    import re
    from mtg_builder.archetypes import ARCHETYPES_DIR

    def check(pattern):
        for part in pattern.split("&"):
            kind, _, value = part.partition(":")
            assert kind in ("re", "kw", "type", "stat", "creature"), part
            if kind == "re":
                re.compile(value)
            if kind == "stat":
                assert re.match(r"(power|toughness|cmc)(>=|<=|==)\d+", value), part

    files = sorted(ARCHETYPES_DIR.glob("*.json"))
    assert {p.stem for p in files} >= {"fra", "trk"}
    for path in files:
        data = json.loads(path.read_text("utf-8"))
        assert data["set"] == path.stem and data["source"]
        assert len(data["archetypes"]) == 10 and set(data["archetypes"]) == {"WU", "UB", "BR", "RG", "WG", "WB", "UR", "BG", "WR", "UG"}
        for pair, spec in data["archetypes"].items():
            assert spec["name"] and spec["plan"] and spec["payoffs"] and spec["enablers"], pair
            for pattern in spec["payoffs"] + spec["enablers"]:
                check(pattern)
        for hook, spec in data.get("hooks", {}).items():
            assert spec["needs"] and spec["provides"] and 0 < float(spec.get("weight", 1.0)) <= 1.0, hook
            for pattern in spec["needs"] + spec["provides"]:
                check(pattern)
