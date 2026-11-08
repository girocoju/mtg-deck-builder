from mtg_builder import archetypes, draft_map, draft_pick
from test_archetypes import DATA
from test_decks import conn  # noqa: F401
from test_draft import site, snap  # noqa: F401

HOOKS = {**DATA, "hooks": {"fichas": {"needs": ["re:up to seven"], "provides": ["type:Planeswalker", "type:Instant"]}}}


def index_of(conn):  # noqa: F811
    return {row["name"]: row for row in conn.execute("SELECT * FROM cards")}


def test_links_and_direct_synergy(conn):  # noqa: F811
    cards, tagger = index_of(conn), archetypes.Tagger(HOOKS)
    assert tagger.links(cards["Rat Swarm"]) == {"needs": {"BG": 1.0}, "provides": {}}        # payoff pede
    assert tagger.links(cards["Tana"]) == {"needs": {"GU": 1.0}, "provides": {"BG": 1.0}}    # lenda pede GU; Partner oferece BG
    assert tagger.links(cards["Bear"]) == {"needs": {}, "provides": {"BG": archetypes.GENERIC_ENABLER}}   # só por custo
    assert tagger.links(cards["Seven Gnomes"])["needs"] == {"fichas": 1.0}                    # gancho
    assert tagger.links(cards["Jace"]) == {"needs": {"GU": 1.0}, "provides": {"fichas": 1.0}}
    assert tagger.synergy(cards["Rat Swarm"], cards["Tana"]) == 1.0                           # pede BG ↔ oferece BG pleno
    assert tagger.synergy(cards["Tana"], cards["Rat Swarm"]) == 1.0                           # simétrica
    assert tagger.synergy(cards["Rat Swarm"], cards["Bear"]) == archetypes.GENERIC_ENABLER    # qualquer corpo barato
    assert tagger.synergy(cards["Tana"], cards["Ivy"]) == archetypes.SHARED_PAYOFF            # duas payoffs de GU
    assert tagger.synergy(cards["Seven Gnomes"], cards["Jace"]) == 1.0                        # G + U: duas cores
    assert tagger.synergy(cards["Seven Gnomes"], cards["Fire // Ice"]) == archetypes.SPLASH_FACTOR   # G + RU: três
    assert tagger.synergy(cards["Rat Swarm"], cards["Rat Swarm"]) == 0 and tagger.synergy(None, cards["Bear"]) == 0
    assert tagger.synergy(cards["Bear"], cards["Imp"]) == 0                                   # dois enablers: nada
    assert tagger.link_scores(cards["Rat Swarm"], cards["Tana"]) == {"BG": 1.0}               # um elo, contado uma vez
    assert tagger.links_between(cards["Rat Swarm"], cards["Bear"]) == ["BG"]
    assert tagger.links_between(cards["Tana"], cards["Ivy"]) == ["GU"]
    assert archetypes.Tagger.label_links(tagger.links(cards["Tana"])) == "pede GU · oferece BG"
    assert archetypes.Tagger.label_links(tagger.links(cards["Broken Orb"])) == ""


def test_partners_component_in_ranking(conn, site):  # noqa: F811
    engine = draft_pick.Engine(conn, draft_pick.Ratings(snap(conn, site)), "tst", archetype_data=HOOKS)
    state = draft_pick.DraftState("tst")
    state.add_picks(["Rat Swarm"])
    result = engine.rank(state, 1, 2, ["Tana", "Bear", "Fire // Ice"])
    by_name = {r["name"]: r for r in result["cartas"]}
    assert by_name["Tana"]["parceiros"] == draft_pick.WEIGHTS["parceiro"] and by_name["Tana"]["elos"] == [("Rat Swarm", 1.0)]
    assert by_name["Bear"]["parceiros"] == round(draft_pick.WEIGHTS["parceiro"] * archetypes.GENERIC_ENABLER, 2)
    assert by_name["Fire // Ice"]["parceiros"] == 0 and by_name["Fire // Ice"]["elos"] == []     # sem elo com Rat Swarm
    tana = by_name["Tana"]
    parts = tana["poder"] + tana["encaixe"] + tana["par"] + tana["necessidade"] + tana["sinal"] + tana["flexibilidade"] \
        + tana["sinergia"] + tana["parceiros"]
    assert abs(tana["total"] - parts) < 0.02                                                    # componentes arredondados um a um
    state.add_picks(["Rat Swarm"] * 6)
    capped = engine.rank(state, 1, 8, ["Tana"])
    assert capped["cartas"][0]["parceiros"] == draft_pick.WEIGHTS["parceiros_max"]              # teto
    text = draft_pick.format_ranking(capped)
    assert " parc " in text and "↔ Rat Swarm 1" in text


def test_set_map_orders_pairs_and_follow_ups(conn, site, tmp_path):  # noqa: F811
    ratings = draft_pick.Ratings(snap(conn, site))
    setmap = draft_map.SetMap(conn, "tst", ratings, tagger=archetypes.Tagger(HOOKS))
    assert set(setmap.cards) == {"Bear", "Elk", "Drake", "Imp", "Wolf", "Fire // Ice", "Rat Swarm"}   # lista do 17Lands, sem básicos
    assert setmap.coverage() == {"17lands": 5, "teorica*": 2}
    order = setmap.pick_order()
    assert [e["name"] for e in order][:3] == ["Elk", "Bear", "Wolf"] and order[0]["posicao"] == 1 and order[0]["poder"] == 8.0
    assert order[2]["teorica"] and [e["name"] for e in setmap.pick_order("rare")] == ["Elk"]
    assert setmap.pick_order(top=1)[0]["name"] == "Elk"

    pairs = setmap.pairs()
    assert len(pairs) == 5 and {pairs[0]["a"], pairs[0]["b"]} == {"Elk", "Rat Swarm"} and pairs[0]["elos"] == ["BG"]
    assert pairs[0]["sinergia"] == archetypes.GENERIC_ENABLER                                   # criaturas de custo 1: corpos
    assert [p["name"] for p in setmap.partners("Rat Swarm", top=2)] == ["Elk", "Bear"]
    assert setmap.partner_totals()["Rat Swarm"] == 5 * archetypes.GENERIC_ENABLER
    assert next(e for e in order if e["name"] == "Rat Swarm")["elos"] > 1

    result = setmap.follow_ups(["rat swarm"], top=3)
    names = [r["name"] for r in result["cartas"]]
    assert result["pack"] == 1 and result["pick"] == 2 and result["picks"] == ["Rat Swarm"] and result["desconhecidas"] == []
    assert "Rat Swarm" not in names and names[0] == "Elk" and result["cartas"][0]["parceiros"] > 0
    assert setmap.follow_ups(["Carta Inventada"], 1, 2)["desconhecidas"] == ["Carta Inventada"]

    tree = setmap.tree(top=2)
    assert [t["primeiro"]["name"] for t in tree] == ["Elk", "Wolf"] and len(tree[0]["seguintes"]) == 2
    tables = setmap.archetype_tables()
    bg = next(t for t in tables if t["pair"] == "BG")
    assert [e["name"] for e in bg["payoffs"]] == ["Rat Swarm"] and bg["enablers"][0]["name"] == "Elk" and bg["total_enablers"] == 5

    central = setmap.centrality()
    assert central["Rat Swarm"] == 100.0 and 0 < central["Fire // Ice"] < central["Drake"] < central["Elk"]   # hub; isolada no mínimo
    assert setmap.communities() == []                                                            # só elos genéricos: sem grupo
    groups = setmap.communities(min_weight=archetypes.GENERIC_ENABLER)
    assert len(groups) == 1 and groups[0]["tamanho"] == 6 and groups[0]["cartas"][0] == "Elk" and groups[0]["cores"][0][0] == "G"
    assert groups[0]["pares"][0][0] == "BG" and "Fire // Ice" not in groups[0]["cartas"]

    text = draft_map.markdown(setmap, "Test Set", ratings.describe())
    assert text.startswith("# Test Set (TST) — mapa de picks") and "### Raras (1)" in text and "## 2." in text
    assert "**Elk**" in text and "| Rat Swarm |" in text and "### BG Enxame" in text
    assert "## 3." in text and "| 0.25 | +8.0 | Elk | Rat Swarm | BG |" in text
    assert "## 5." in text and "| 1 | 100 | 1.25 | " in text and "| Rat Swarm | pede BG |" in text and "0 grupos" in text
    assert "Rat Swarm" in draft_map.format_graph(setmap, top=3) and "1. 6 cartas" in "\n".join(draft_map._community_lines(setmap, groups))
    path = draft_map.write_markdown(setmap, "Test Set", path=tmp_path / "tst-mapa.md")
    assert path.exists() and path.read_text("utf-8") == text or "Test Set" in path.read_text("utf-8")
    assert "Elk" in draft_map.format_order(setmap, order, "Test Set") and "↔" in draft_map.format_pairs(setmap, pairs)
