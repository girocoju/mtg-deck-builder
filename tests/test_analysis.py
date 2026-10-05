import gzip
import json

import pytest

from mtg_builder import analysis, db, decklist, scryfall


def card(name, cost="", type_line="Creature — Bear", text="", produced=(), layout="normal", **extra):
    symbols = [s for s in cost.replace("}", "").split("{") if s]
    colors = sorted({s for s in symbols if s in "WUBRG"} | set(extra.pop("identity", "")))
    cmc = sum(int(s) if s.isdigit() else 0 if s == "X" else 1 for s in symbols)
    slug = name.lower().replace(" ", "-").replace("/", "")
    return {
        "id": f"p-{slug}", "oracle_id": f"o-{slug}", "name": name, "layout": layout,
        "mana_cost": cost, "cmc": float(cmc), "type_line": type_line, "oracle_text": text,
        "colors": colors, "color_identity": colors, "keywords": [],
        "produced_mana": list(produced), "legalities": {"standard": "legal"},
        "set": "tst", "collector_number": "1", "rarity": "common", "lang": "en",
        "games": ["paper"], "prices": {}, **extra,
    }


CARDS = [
    card("Forest", type_line="Basic Land — Forest", produced="G", identity="G"),
    card("Island", type_line="Basic Land — Island", produced="U", identity="U"),
    card("Tapped Dual", type_line="Land", text="This land enters tapped.\n{T}: Add {G} or {U}.",
         produced="GU", identity="GU"),
    card("Wilds", type_line="Land",
         text="{T}, Sacrifice this land: Search your library for a basic land card, put it onto "
              "the battlefield tapped, then shuffle."),
    card("Elf", "{G}", text="{T}: Add {G}.", produced="G"),
    card("Bear", "{1}{G}"),
    card("Ogre", "{2}{G}{G}"),
    card("Wurm", "{4}{G}{G}"),
    card("Hydra", "{X}{G}{G}"),
    card("Opt Like", "{U}", "Instant", "Scry 1.\nDraw a card."),
    card("Cancel Like", "{1}{U}{U}", "Instant", "Counter target spell."),
    card("Wrath Like", "{2}{U}{U}", "Sorcery", "Destroy all creatures."),
    card("Shock Like", "{R}", "Instant", "This spell deals 2 damage to any target."),
    card("Growth Spiral Like", "{G}{U}", "Instant", "Draw a card. You may put a land card from your hand onto the battlefield."),
    {**card("Fire // Ice", "{1}{R} // {1}{U}", "Instant // Instant", identity="RU", layout="split"),
     "card_faces": [{"name": "Fire", "mana_cost": "{1}{R}", "type_line": "Instant", "oracle_text": ""},
                    {"name": "Ice", "mana_cost": "{1}{U}", "type_line": "Instant", "oracle_text": ""}]},
    {**card("Spell // Pathland", "{2}{G}", "Sorcery // Land", produced="G", layout="modal_dfc"),
     "card_faces": [{"name": "Spell", "mana_cost": "{2}{G}", "type_line": "Sorcery", "oracle_text": ""},
                    {"name": "Pathland", "mana_cost": "", "type_line": "Land",
                     "oracle_text": "This land enters tapped.\n{T}: Add {G}."}]},
]


@pytest.fixture
def conn(tmp_path):
    path = tmp_path / "cards.jsonl.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        f.writelines(json.dumps(c) + "\n" for c in CARDS)
    conn = db.connect(tmp_path / "test.sqlite")
    with conn:
        scryfall.ingest_cards(conn, path)
    return conn


def run(conn, text):
    deck = decklist.parse(text)
    assert decklist.resolve(conn, deck) == []
    return analysis.analyze(deck)


def test_hypergeometric_matches_reference_values():
    # Karsten: 4 cópias em 60, turno 4 jogando primeiro (10 cartas) = 52,8%; 2+ cópias = 12,6%
    assert analysis.hypergeom_at_least(60, 4, analysis.cards_seen(4)) == pytest.approx(0.528, abs=0.001)
    assert analysis.hypergeom_at_least(60, 4, 10, 2) == pytest.approx(0.126, abs=0.001)
    # 1 cópia em 60, mão de 7 = 7/60; todas as cartas vistas = certeza
    assert analysis.hypergeom_at_least(60, 1, 7) == pytest.approx(7 / 60)
    assert analysis.hypergeom_at_least(40, 17, 40, 17) == pytest.approx(1.0)
    assert analysis.cards_seen(3, on_the_play=False) == 10


def test_requirement_key_handles_x_hybrid_and_generic():
    assert analysis.requirement_key("{1}{U}{U}", "U") == ("1CC", 3)
    assert analysis.requirement_key("{X}{G}{G}", "G") == ("CC", 2)
    assert analysis.requirement_key("{G/U}{G}", "G") == ("1C", 2)
    assert analysis.requirement_key("{2}{R}", "U") == (None, 0)


def test_sources_table_and_fallback():
    assert analysis.sources_needed("CC", 60) == (21, False)
    assert analysis.sources_needed("1CC", 99) == (28, False)
    assert analysis.sources_needed("C", 40) == (9, False)
    assert analysis.sources_needed("6CC", 60) == (12, True)      # usa 5CC
    assert analysis.sources_needed("CCCCC", 60) == (24, True)    # usa CCCC


def test_curve_average_and_land_formula(conn):
    data = run(conn, "4 Elf\n8 Bear\n8 Ogre\n4 Wurm\n12 Opt Like\n24 Forest\n")
    assert data["tamanho_de_referencia"] == 60 and data["magicas"] == 36
    assert data["curva"]["1"] == {"criaturas": 4, "outras": 12}
    assert data["curva"]["2"] == {"criaturas": 8, "outras": 0}
    assert data["curva"]["6"] == {"criaturas": 4, "outras": 0}
    avg = (4 * 1 + 8 * 2 + 8 * 4 + 4 * 6 + 12 * 1) / 36
    assert data["valor_de_mana_medio"] == pytest.approx(avg, abs=0.01)
    assert data["compra_ou_ramp_barato"] == 16  # 4 Elf (ramp) + 12 Opt Like (compra)
    assert data["terrenos_recomendados"] == pytest.approx(19.59 + 1.90 * avg - 0.28 * 16, abs=0.05)


def test_two_color_deck_with_few_sources_raises_alert(conn):
    data = run(conn, "16 Bear\n8 Ogre\n4 Cancel Like\n8 Opt Like\n18 Forest\n6 Island\n")
    blue = data["cores"]["U"]
    assert blue["exigencia"]["carta"] == "Cancel Like" and blue["exigencia"]["fontes_necessarias"] == 18
    assert blue["fontes_terrenos"] == 6
    assert any("Cor U: 18 fontes recomendadas para Cancel Like" in a for a in data["alertas"])
    assert any("mágicas de 1 mana pedem 14 fontes desviradas" in a for a in data["alertas"])
    assert not any("Cor G" in a for a in data["alertas"])


def test_source_counting_duals_fetch_tapped_and_dorks(conn):
    data = run(conn, "4 Elf\n20 Ogre\n8 Wrath Like\n4 Opt Like\n8 Forest\n4 Island\n8 Tapped Dual\n4 Wilds\n")
    green, blue = data["cores"]["G"], data["cores"]["U"]
    assert green["fontes_terrenos"] == 20 and blue["fontes_terrenos"] == 16   # básicos + dual + Wilds
    assert blue["fontes_desviradas"] == 8                                     # Island + Wilds
    assert green["fontes_extras"] == 2.0                                      # 4 Elf × 1/2
    assert data["terrenos_virados"] == 8


def test_gold_split_x_and_mdfc_are_counted_as_documented(conn):
    data = run(conn, "4 Growth Spiral Like\n4 Fire // Ice\n4 Hydra\n4 Spell // Pathland\n"
                     "20 Bear\n12 Forest\n12 Island\n")
    # ouro: +1 no requisito (1C em 60 = 13... aqui CC? não: {G}{U} vira "1C" por cor → 13 + 1)
    assert data["cores"]["U"]["exigencia"]["fontes_necessarias"] == 14
    # split: cada metade conta sozinha, então há exigência de vermelho vinda de Fire
    assert data["cores"]["R"]["exigencia"]["chave"] == "1C"
    # X vale zero: Hydra é CC
    assert data["cores"]["G"]["exigencia"] == {
        "carta": "Hydra", "custo": "{X}{G}{G}", "chave": "CC", "valor_de_mana": 2,
        "fontes_necessarias": 21, "aproximado": False}
    # MDFC mágica/terreno que entra virado: 0,38 terreno e 0,8 fonte cada
    assert data["terrenos"] == pytest.approx(24 + 4 * 0.38)
    assert data["cores"]["G"]["fontes_terrenos"] == pytest.approx(12 + 4 * 0.8)
    assert data["curva"]["3"]["outras"] == 4


def test_roles_are_classified_by_text(conn):
    data = run(conn, "4 Elf\n4 Cancel Like\n4 Wrath Like\n4 Shock Like\n4 Opt Like\n20 Bear\n20 Forest\n")
    roles = data["papeis"]
    assert roles["terreno"] == 20 and roles["ameaça"] == 24
    assert roles["anulação"] == 4 and roles["remoção em massa"] == 4
    assert roles["remoção pontual"] == 4 and roles["compra de cartas"] == 4 and roles["aceleração"] == 4


def test_size_parameters_for_40_and_99(conn):
    limited = run(conn, "23 Bear\n13 Forest\n")
    assert limited["tamanho_de_referencia"] == 40
    assert any("o padrão é 17" in a for a in limited["alertas"])
    commander = decklist.parse("Commander\n1 Ogre\n\nDeck\n59 Bear\n40 Forest\n")
    commander.main[0].qty = 59  # singleton não é conferido aqui; só o tamanho importa
    assert analysis.size_class(100) == 99
    assert analysis.recommended_lands(99, 3.0, 0) == pytest.approx(40.81)
    assert analysis.recommended_lands(60, 3.0, 0) == pytest.approx(25.29)


def test_report_is_text(conn):
    text = analysis.report(run(conn, "36 Bear\n24 Forest\n"))
    assert "Terrenos: 24" in text and "Alertas:" in text and "G:" in text
