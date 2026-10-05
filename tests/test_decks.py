import gzip
import json

import pytest

from mtg_builder import db, decklist, formats, scryfall


def card(name, type_line="Creature — Bear", identity="G", text="", legal=("standard", "brawl", "commander"),
         banned=(), restricted=(), games=("paper", "arena", "mtgo"), rarity="common", usd="0.10",
         tix="0.01", **extra):
    legalities = {f: "legal" for f in legal}
    legalities.update({f: "banned" for f in banned})
    legalities.update({f: "restricted" for f in restricted})
    slug = name.lower().replace(" ", "-")
    return {
        "id": f"p-{slug}", "oracle_id": f"o-{slug}", "name": name, "layout": "normal",
        "mana_cost": "{1}", "cmc": 1.0, "type_line": type_line, "oracle_text": text,
        "colors": list(identity), "color_identity": list(identity), "keywords": [],
        "legalities": legalities, "set": "tst", "collector_number": "1", "rarity": rarity,
        "lang": "en", "games": list(games), "booster": True,
        "prices": {"usd": usd, "tix": tix}, **extra,
    }


CARDS = [
    card("Forest", "Basic Land — Forest", usd="0.05"),
    card("Island", "Basic Land — Island", identity="U"),
    card("Bear", rarity="common"),
    card("Elk", rarity="rare", usd="2.00"),
    card("Wolf", rarity="mythic", usd="10.00", games=("paper",), tix=None),
    card("Drake", identity="U", rarity="uncommon"),
    card("Imp", identity="B"),
    card("Rat Swarm", identity="B", text="A deck can have any number of cards named Rat Swarm."),
    card("Seven Gnomes", text="A deck can have up to seven cards named Seven Gnomes."),
    card("Broken Orb", "Artifact", identity="", banned=("standard",), restricted=("vintage",),
         legal=("commander",)),
    card("Old Relic", "Artifact", identity="", legal=("commander",)),
    card("Ivy", "Legendary Creature — Faerie", identity="GU", legal=("brawl", "commander")),
    card("Jace", "Legendary Planeswalker — Jace", identity="U", legal=("brawl", "commander")),
    card("Tana", "Legendary Creature — Elf", identity="G", keywords=["Partner"]),
    card("Kraum", "Legendary Creature — Zombie", identity="U", keywords=["Partner"]),
    {**card("Fire // Ice", "Instant // Instant", identity="RU"), "layout": "split"},
    {**card("Delver // Aberration", "Creature — Wizard // Creature — Insect", identity="U"),
     "layout": "transform"},
]
FILLER = [card(f"Filler {i}", identity="G", legal=("standard", "brawl", "commander")) for i in range(100)]


@pytest.fixture
def conn(tmp_path):
    path = tmp_path / "cards.jsonl.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        f.writelines(json.dumps(c) + "\n" for c in CARDS + FILLER)
    conn = db.connect(tmp_path / "test.sqlite")
    with conn:
        scryfall.ingest_cards(conn, path)
    return conn


def check(conn, text, fmt, **kw):
    return formats.validate(conn, decklist.parse(text), fmt, **kw)[0]


def sixty(*extra, lands=24):
    """Lista de 60: `extra` + básicos + fillers em playsets."""
    lines = list(extra) + [f"{lands} Forest"]
    total = sum(int(line.split()[0]) for line in lines)
    i = 0
    while total < 60:
        n = min(4, 60 - total)
        lines.append(f"{n} Filler {i}")
        total, i = total + n, i + 1
    return "\n".join(lines)


def singleton(commander, size=100, *extra):
    lines = ["Commander", commander, "", "Deck", *extra]
    count = sum(int(line.split()[0]) for line in [commander, *extra])
    lines += [f"1 Filler {i}" for i in range(size - count - 20)] + ["20 Forest"]
    return "\n".join(lines)


# --- leitura ---

def test_parse_arena_format_with_sections():
    deck = decklist.parse(
        "About\nName Teste\n\nCompanion\n1 Bear\n\nCommander\n1 Ivy (DMU) 201\n\n"
        "Deck\n4 Bear (TST) 1\n20 Forest\n\nSideboard\n1 Bear\n2 Elk\n"
    )
    assert [(e.qty, e.name, e.set_code, e.number) for e in deck.commander] == [(1, "Ivy", "DMU", "201")]
    assert deck.count("main") == 24 and deck.count("sideboard") == 3
    assert deck.companion == ["Bear"]


def test_parse_plain_list_uses_blank_line_and_sb_prefix():
    deck = decklist.parse("4 Bear\n4x Elk\n\n2 Drake\n")
    assert deck.count("main") == 8 and deck.count("sideboard") == 2
    deck = decklist.parse("4 Bear\nSB: 3 Drake\n4 Elk\n")
    assert deck.count("main") == 8 and deck.count("sideboard") == 3


def test_parse_markdown_reads_first_code_block():
    deck = decklist.parse("# Meu deck\n\n4 Não é carta\n\n```\n4 Bear\n```\n\ntexto\n", markdown=True)
    assert [(e.qty, e.name) for e in deck.main] == [(4, "Bear")]


def test_resolve_ignores_accents(conn):
    conn.execute("UPDATE cards SET name = 'Mjölnir Bear' WHERE name = 'Bear'")
    deck = decklist.parse("1 Mjolnir Bear\n1 MJÖLNIR BEAR\n")
    assert decklist.resolve(conn, deck) == []
    assert deck.main[0].card["name"] == deck.main[1].card["name"] == "Mjölnir Bear"


def test_resolve_translated_names_by_set_and_collector_number(conn):
    conn.execute("UPDATE printings SET collector_number = '77' WHERE name = 'Elk'")
    conn.execute("INSERT INTO sets (code, name, arena_code) VALUES ('tst', 'Test', 'TS1')")
    deck = decklist.parse("2 Alce (TST) 77\n1 Alce (TS1) 77\n1 Urso (TST) 999\n1 Lobo\n")
    unknown = decklist.resolve(conn, deck)
    assert [e.card["name"] for e in deck.main[:2]] == ["Elk", "Elk"]
    assert [e.name for e, _ in unknown] == ["Urso", "Lobo"]
    assert decklist.export(deck, "arena").startswith("Deck\n3 Elk\n")


def test_resolve_front_face_split_slash_and_suggestion(conn):
    deck = decklist.parse("1 delver\n1 Fire/Ice\n1 Beer\n")
    unknown = decklist.resolve(conn, deck)
    assert deck.main[0].card["name"] == "Delver // Aberration"
    assert deck.main[1].card["name"] == "Fire // Ice"
    assert [(e.name, s) for e, s in unknown] == [("Beer", ["Bear"])]


# --- validação: construído de 60 ---

def test_valid_sixty_card_deck(conn):
    assert check(conn, sixty("4 Bear") + "\n\nSideboard\n4 Elk\n", "standard") == []


def test_sixty_card_problems_are_reported_individually(conn):
    errors = check(conn, "5 Bear\n1 Broken Orb\n1 Old Relic\n1 Beer\n20 Forest\n", "standard")
    text = "\n".join(errors)
    assert "Carta não encontrada: Beer. Você quis dizer: Bear?" in text
    assert "pelo menos 60 cartas; tem 28" in text
    assert "5 cópias de Bear; o máximo é 4." in text
    assert "Broken Orb é banida em standard." in text
    assert "Old Relic não é legal em standard." in text
    assert len(errors) == 5


def test_copies_count_main_plus_sideboard_and_exceptions(conn):
    errors = check(conn, sixty("3 Bear", "7 Seven Gnomes") + "\n\nSideboard\n2 Bear\n", "standard")
    assert errors == ["5 cópias de Bear; o máximo é 4."]
    assert any("8 cópias de Seven Gnomes; o máximo é 7." in e
               for e in check(conn, sixty("8 Seven Gnomes"), "standard"))


def test_restricted_and_sideboard_limits(conn):
    errors = check(conn, sixty("2 Broken Orb"), "vintage")
    assert "2 cópias de Broken Orb; o máximo é 1 (restrita)." in errors
    side = "\n\nSideboard\n" + "\n".join(f"1 Filler {i}" for i in range(20, 35))
    assert check(conn, sixty("4 Bear") + side, "standard") == []
    assert check(conn, sixty("4 Bear") + side + "\n1 Filler 40", "standard") == [
        "Sideboard com 16 cartas; o máximo é 15."
    ]


def test_platform_availability(conn):
    assert check(conn, sixty("4 Wolf"), "standard", game="arena") == ["Wolf não existe em arena."]


# --- validação: singleton com comandante ---

def test_valid_brawl_deck(conn):
    assert check(conn, singleton("1 Ivy", 100, "1 Drake", "5 Island"), "brawl") == []


def test_brawl_rejects_card_outside_color_identity(conn):
    errors = check(conn, singleton("1 Ivy", 100, "1 Imp"), "brawl")
    assert errors == ["Imp está fora da identidade de cor do comandante (GU): tem B."]


def test_commander_rules(conn):
    assert "exatamente 100 cartas (contando o comandante); tem 99" in check(
        conn, singleton("1 Ivy", 99), "commander")[0]
    assert any("2 cópias de Bear" in e for e in check(conn, singleton("1 Ivy", 100, "2 Bear"), "commander"))
    assert "Falta a seção Commander com o comandante do deck." in check(
        conn, "Deck\n80 Filler 1\n20 Forest\n", "commander")
    assert any("Bear não pode ser comandante" in e for e in check(conn, singleton("1 Bear"), "commander"))


def test_planeswalker_commander_only_in_brawl(conn):
    deck = singleton("1 Jace").replace("Filler", "Filler").replace("20 Forest", "20 Island")
    brawl = check(conn, deck, "brawl")
    assert not any("não pode ser comandante" in e for e in brawl)
    assert any("Jace não pode ser comandante em commander" in e for e in check(conn, deck, "commander"))


def test_partner_commanders(conn):
    partners = "Commander\n1 Tana\n1 Kraum\n\nDeck\n" + "\n".join(
        f"1 Filler {i}" for i in range(78)) + "\n20 Forest\n"
    assert check(conn, partners, "commander") == []
    errors = check(conn, partners.replace("1 Kraum", "1 Ivy"), "commander")
    assert any("não podem ser comandantes juntos" in e for e in errors)


def test_standard_brawl_has_sixty_cards(conn):
    assert any("exatamente 60" in e for e in check(conn, singleton("1 Ivy", 100), "standardbrawl"))


# --- validação: limitado ---

def test_limited_needs_forty_and_has_no_copy_or_legality_limit(conn):
    assert check(conn, "17 Forest\n6 Bear\n17 Old Relic\n", "limited") == []
    assert "pelo menos 40 cartas; tem 39" in check(conn, "17 Forest\n22 Bear\n", "limited")[0]


def test_unknown_format(conn):
    assert check(conn, "60 Forest", "tiny-leaders")[0].startswith("Formato desconhecido")


# --- exportação e custo ---

def test_arena_export_roundtrip(conn):
    source = decklist.parse(
        "Commander\n1 Ivy\n\nDeck\n2 Bear\n2 Bear\n1 Delver // Aberration\n1 Fire // Ice\n\nSideboard\n1 Elk\n")
    decklist.resolve(conn, source)
    exported = decklist.export(source, "arena")
    assert exported == "Commander\n1 Ivy\n\nDeck\n4 Bear\n1 Delver\n1 Fire // Ice\n\nSideboard\n1 Elk\n"
    again = decklist.parse(exported)
    assert decklist.resolve(conn, again) == []
    assert decklist.export(again, "arena") == exported


def test_mtgo_export_puts_sideboard_after_blank_line(conn):
    deck = decklist.parse("Deck\n4 Bear\n1 Delver\n\nSideboard\n2 Elk\n")
    decklist.resolve(conn, deck)
    assert decklist.export(deck, "mtgo") == "4 Bear\n1 Delver // Aberration\n\n2 Elk\n"


def test_diff_lists_what_left_and_what_came_in(conn):
    before = decklist.parse("Deck\n4 Bear\n2 Elk\n20 Forest\n\nSideboard\n2 Drake\n1 Imp\n")
    after = decklist.parse("Deck\n4 Bear\n1 Elk\n2 Drake\n19 Forest\n\nSideboard\n1 Imp\n")
    decklist.resolve(conn, before)
    decklist.resolve(conn, after)
    assert decklist.diff(before, after) == {
        "main": [(-1, "Elk"), (-1, "Forest"), (2, "Drake")],
        "sideboard": [(-2, "Drake")],
    }
    assert decklist.diff(before, before) == {}


def test_cost(conn):
    deck = decklist.parse("4 Bear\n2 Elk\n1 Wolf\n1 Drake\n20 Forest\n")
    decklist.resolve(conn, deck)
    result = decklist.cost(conn, deck)
    assert result["usd"] == pytest.approx(4 * 0.10 + 2 * 2.00 + 10.00 + 0.10)
    assert result["wildcards"] == {"common": 4, "uncommon": 1, "rare": 2, "mythic": 0}
    assert result["fora_do_arena"] == ["Wolf"]
    assert result["sem_preco"]["tix"] == ["Wolf"]
