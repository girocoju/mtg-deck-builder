from mtg_builder import draft_deck, draft_pick
from test_decks import conn  # noqa: F401
from test_draft import site, snap  # noqa: F401


def engine_for(conn, site):  # noqa: F811
    return draft_pick.Engine(conn, draft_pick.Ratings(snap(conn, site)), "tst")


def test_pips_and_land_production():
    assert draft_deck._pips("{1}{G}{G}") == {"G": 2.0}
    assert draft_deck._pips("{1}{G/U}") == {"G": 0.5, "U": 0.5}
    assert draft_deck._pips("{X}{R}") == {"R": 1.0} and draft_deck._pips(None) == {}
    dual = {"oracle_text": "This land enters tapped unless you control a planeswalker.\n{T}: Add {U} or {R}."}
    assert draft_deck._produces(dual) == ({"U", "R"}, False)
    refuge = {"oracle_text": "As it enters, choose a color.\n{T}: Add one mana of the chosen color."}
    assert draft_deck._produces(refuge) == (set("WUBRG"), True)
    assert draft_deck._produces({"oracle_text": "{T}: Add {C}."}) == (set(), False)


def test_splash_rules_on_synthetic_entries():
    def card(name, colors, cmc, power, pips):
        return {"name": name, "colors": colors, "cmc": cmc, "power": power, "pips": pips, "land": False, "body": False}
    entries = [card("Bolt", "R", 3, 3.0, {"R": 1.0}), card("Double", "R", 3, 4.0, {"R": 2.0}),
               card("Cheap", "R", 2, 3.0, {"R": 1.0}), card("Weak", "R", 4, 1.0, {"R": 1.0}),
               card("Gold", "WR", 3, 5.0, {"W": 1.0, "R": 1.0}), card("Black", "B", 3, 2.5, {"B": 1.0})]
    color, chosen = draft_deck.splash_candidates(entries, "UG")
    assert color == "R" and [e["name"] for e in chosen] == ["Bolt"]        # dois símbolos, custo 2, nota baixa e duas cores ficam fora
    assert draft_deck.splash_candidates([card("Blue", "U", 3, 5.0, {"U": 1.0})], "UG") == (None, [])


def test_build_picks_pair_bodies_and_lands(conn, site, tmp_path):  # noqa: F811
    engine = engine_for(conn, site)
    pool = (["Bear"] * 6 + ["Elk", "Wolf", "Tana", "Seven Gnomes", "Ivy", "Kraum", "Jace", "Delver // Aberration"]
            + ["Drake"] * 2 + [f"Filler {i}" for i in range(1, 8)]
            + ["Rat Swarm"] * 2 + ["Fire // Ice", "Broken Orb", "Old Relic", "Forest", "Carta Inventada"])
    result = draft_deck.build(engine, pool)
    assert result["pair"] == "UG" and result["splash"] is None            # Fire // Ice: custo 1, não vale splash
    assert result["size"] == 40 and result["stats"]["magicas"] == 23 and result["stats"]["terrenos"] == 17
    main = dict((name, qty) for name, qty in result["main"])
    assert main["Elk"] == 1 and main["Bear"] == 6 and main["Wolf"] == 1 and "Drake" not in main     # Drake rende 52%: fica fora
    assert "Rat Swarm" not in main and "Fire // Ice" not in main
    assert result["stats"]["corpos"] >= draft_deck.MIN_BODIES
    lands = dict(result["lands"])
    assert set(lands) == {"Forest", "Island"} and lands["Forest"] + lands["Island"] == 17 and lands["Forest"] >= 6 and lands["Island"] >= 6
    assert ("Rat Swarm", 2) in result["sideboard"] and ("Drake", 2) in result["sideboard"] and result["unknown"] == ["Carta Inventada"]
    assert result["reasons"][0].startswith("Par UG") and any("Não encontradas" in r for r in result["reasons"])
    lines = draft_deck.arena_lines(result)
    assert lines[0] == "Deck" and "1 Delver" in lines and f"{lands['Forest']} Forest" in lines and sum(int(l.split()[0]) for l in lines[1:]) == 40
    summary = "\n".join(draft_deck.summary_lines(result))
    assert summary.startswith("DECK PROPOSTO: UG · 23 mágicas, 17 terrenos") and "• Par UG" in summary and "de interação" in summary
    text = draft_deck.markdown(result, "Test Set", "tst", event="PremierDraft_TST", sources="17Lands teste")
    assert text.startswith("# Test Set — deck de 40 montado pelo Oráculo (UG)") and "```\nDeck\n" in text and "## Reserva" in text
    path = draft_deck.write(result, "Test Set", "tst", event="PremierDraft_TST", path=tmp_path / "deck.md")
    assert path.exists() and "6 Bear" in path.read_text("utf-8")
    first = draft_deck.deck_path("tst", "PremierDraft_TST", result, day="2026-11-09")
    assert first.name == "tst-premierdraft-tst-2026-11-09-ug.md"


def test_build_with_short_pool_adds_lands(conn, site):  # noqa: F811
    engine = engine_for(conn, site)
    result = draft_deck.build(engine, ["Bear"] * 4 + ["Elk", "Drake", "Drake", "Kraum", "Imp"])
    assert result["stats"]["magicas"] == 9 and result["stats"]["terrenos"] == draft_deck.MAX_LANDS   # pool curto: no máximo 18 terrenos
    assert result["size"] == 9 + draft_deck.MAX_LANDS and any("Enchimento" in r for r in result["reasons"])   # Imp entra fora das cores


def test_rare_bonus_only_in_leftover_picks(conn, site):  # noqa: F811
    engine = engine_for(conn, site)
    state = draft_pick.DraftState("tst")
    early = {r["name"]: r for r in engine.rank(state, 1, 2, ["Elk", "Wolf", "Bear"])["cartas"]}
    assert early["Elk"]["colecao"] == 0 and early["Wolf"]["colecao"] == 0            # pick de verdade: só o poder manda
    late = engine.rank(state, 1, draft_pick.WEIGHTS["sobra_a_partir"], ["Elk", "Wolf", "Bear"])
    rows = {r["name"]: r for r in late["cartas"]}
    assert rows["Elk"]["colecao"] == draft_pick.WEIGHTS["sobra_rara"] and rows["Wolf"]["colecao"] == draft_pick.WEIGHTS["sobra_mitica"]
    assert rows["Bear"]["colecao"] == 0 and rows["Wolf"]["total"] - rows["Bear"]["total"] > early["Wolf"]["total"] - early["Bear"]["total"]
    text = draft_pick.format_ranking(late)
    assert text.startswith("► PEGUE: ") and " col " in text.splitlines()[2]
    assert "que falta na coleção" in draft_pick.headline(late) or late["cartas"][0]["colecao"] == 0
