import gzip
import json

import pytest

from mtg_builder import db, meta, scryfall
from test_analysis import card

CARDS = [
    card("Mountain", type_line="Basic Land — Mountain", produced="R", identity="R"),
    card("Island", type_line="Basic Land — Island", produced="U", identity="U"),
    card("Goblin", "{R}"),
    card("Shock Like", "{R}", "Instant", "This spell deals 2 damage to any target."),
    card("Sphinx", "{4}{U}{U}"),
    card("Cancel Like", "{1}{U}{U}", "Instant", "Counter target spell."),
    card("Wrath Like", "{2}{U}{U}", "Sorcery", "Destroy all creatures."),
]

TILE = """<div class='archetype-tile' id='{id}'>
<a class='card-image-tile-link-overlay' href='/archetype/{slug}'></a>
<div class='archetype-tile-title'>
<span class='deck-price-online'><a href="/archetype/{slug}#online">{name}</a></span>
<span class='deck-price-paper'><a href="/archetype/{slug}#paper">{name}</a></span>
</div>
<span class='manacost' aria-label='colors: {colors}'></span>
<ul>
<li>{key}</li>
</ul>
<div class='archetype-tile-statistic metagame-percentage'>
<div class='archetype-tile-statistic-name'>META%</div>
<div class='archetype-tile-statistic-value'>
{share}%
<span class='archetype-tile-statistic-value-extra-data'>
({decks})
</span></div></div></div>
"""
METAGAME = ("<div class='archetype-tile-container'>"
            + TILE.format(id=1, slug="std-red", name="Mono-Red Aggro", colors="red", key="Goblin", share="20.5", decks=41)
            + TILE.format(id=2, slug="std-blue", name="Blue Sphinxes", colors="blue", key="Sphinx", share="10.0", decks=20)
            + TILE.format(id=3, slug="std-other", name="Rock &amp; Roll", colors="", key="Goblin", share="2.5", decks=5)
            + "</div>")
DECKS = {
    "std-red": "20 Goblin\n18 Shock Like\n22 Mountain\nsideboard\n2 Shock Like\n1 Carta Inexistente\n",
    "std-blue": "8 Sphinx\n14 Cancel Like\n10 Wrath Like\n28 Island\n",
}


def deck_page(text):
    return f'<input type="hidden" name="deck_input[deck]" id="deck_input_deck" value="{text}" autocomplete="off" />'


class FakeSite:
    def __init__(self, fail=False):
        self.calls, self.fail = [], fail

    def __call__(self, url):
        self.calls.append(url)
        if self.fail:
            raise OSError("sem rede")
        if "/metagame/" in url:
            return METAGAME
        return deck_page(DECKS.get(url.rsplit("/", 1)[1], ""))


@pytest.fixture
def conn(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DATA_DIR", tmp_path / "data")
    path = tmp_path / "cards.jsonl.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        f.writelines(json.dumps(c) + "\n" for c in CARDS)
    conn = db.connect(tmp_path / "test.sqlite")
    with conn:
        scryfall.ingest_cards(conn, path)
    return conn


def update(conn, site, **kw):
    return meta.update_goldfish(conn, "standard", fetch=site, delay=0, log=lambda *_: None, **kw)


def test_parse_metagame_page():
    archetypes = meta.parse_goldfish_metagame(METAGAME)
    assert [(a["name"], a["share"], a["decks"]) for a in archetypes] == [
        ("Mono-Red Aggro", 20.5, 41), ("Blue Sphinxes", 10.0, 20), ("Rock & Roll", 2.5, 5)]
    assert archetypes[0]["url"] == "https://www.mtggoldfish.com/archetype/std-red"
    assert archetypes[0]["colors"] == "red" and archetypes[0]["key_cards"] == ["Goblin"]


def test_update_saves_dated_bo3_snapshot_with_checked_decks(conn):
    snapshot = update(conn, FakeSite())
    assert snapshot["mode"] == "bo3" and snapshot["source"] == "mtggoldfish"
    assert snapshot["collected_at"] and snapshot["url"].endswith("/metagame/standard/full")
    red, blue, other = snapshot["archetypes"]
    assert red["macro"] == "aggro" and red["unknown_cards"] == ["Carta Inexistente"]
    assert blue["macro"] == "controle" and blue["stats"]["lands"] == 28
    assert "deck" not in other
    saved = meta.latest("standard", "bo3")
    assert saved["archetypes"][0]["name"] == "Mono-Red Aggro" and saved["file"].endswith("-mtggoldfish.json")


def test_second_update_uses_cache_and_force_refetches(conn):
    site = FakeSite()
    update(conn, site)
    calls = len(site.calls)
    update(conn, site)
    assert len(site.calls) == calls
    update(conn, site, force=True)
    assert len(site.calls) == 2 * calls


def test_network_failure_is_clear_and_keeps_previous_snapshot(conn):
    update(conn, FakeSite())
    with pytest.raises(RuntimeError, match="Falha ao acessar"):
        update(conn, FakeSite(fail=True), force=True)
    assert meta.latest("standard", "bo3")["archetypes"][0]["name"] == "Mono-Red Aggro"


def test_layout_change_and_unknown_format_raise(conn):
    with pytest.raises(RuntimeError, match="layout"):
        meta.update_goldfish(conn, "standard", fetch=lambda url: "<html></html>", delay=0, log=lambda *_: None)
    with pytest.raises(RuntimeError, match="sem coleta"):
        meta.update_goldfish(conn, "brawl")


def test_bo1_import_is_kept_separate_from_bo3(conn, tmp_path):
    update(conn, FakeSite())
    csv_file = tmp_path / "bo1.csv"
    csv_file.write_text("archetype,share,winrate\nBlue Sphinxes,\"8,5%\",52.1\nMono-Red Aggro,31%,55\n", "utf-8")
    decks = tmp_path / "decks"
    decks.mkdir()
    (decks / "Mono-Red Aggro.txt").write_text(DECKS["std-red"], "utf-8")
    snapshot = meta.import_csv(conn, csv_file, "standard", "bo1", "untapped", decks_dir=decks,
                               collected="2026-10-01")
    assert [a["name"] for a in snapshot["archetypes"]] == ["Mono-Red Aggro", "Blue Sphinxes"]
    assert snapshot["archetypes"][0]["winrate"] == 55 and snapshot["archetypes"][1]["share"] == 8.5
    bo1, bo3 = meta.latest("standard", "bo1"), meta.latest("standard", "bo3")
    assert bo1["source"] == "untapped" and bo1["mode"] == "bo1" and bo1["collected_at"].startswith("2026-10-01")
    assert bo3["source"] == "mtggoldfish" and len(bo3["archetypes"]) == 3
    assert meta.latest("pioneer", "bo1") is None


def test_import_checks_key_cards_against_the_base(conn, tmp_path):
    csv_file = tmp_path / "bo1.csv"
    csv_file.write_text(
        "archetype,share,winrate,games,tier,minutes,key_cards\n"
        'Blue Sphinxes,13,57.7,36000,A,4.6,"Sphinx 99.9; cancel like 86,2%; Carta Inventada 50; Wrath Like"\n'
        "Só Win Rate,,55.0,,,,\n", "utf-8")
    snapshot = meta.import_csv(conn, csv_file, "standard", "bo1", "untapped", note="recorte de teste")
    blue, other = snapshot["archetypes"]
    assert blue["key_cards"] == [{"name": "Sphinx", "inclusion": 99.9}, {"name": "Cancel Like", "inclusion": 86.2},
                                 {"name": "Wrath Like", "inclusion": None}]
    assert blue["unknown_cards"] == ["Carta Inventada"]
    assert blue["tier"] == "A" and blue["minutes"] == 4.6 and blue["games"] == 36000
    assert other["share"] is None and "key_cards" not in other and snapshot["note"] == "recorte de teste"
    text = meta.report(snapshot, meta.summarize(conn, snapshot))
    assert "tier A" in text and "cartas: Sphinx 99.9%, Cancel Like 86.2%, Wrath Like" in text
    assert "fora da base: Carta Inventada" in text and "    ?  Só Win Rate | win rate 55%" in text


def test_summary_weights_by_meta_share(conn):
    snapshot = update(conn, FakeSite())
    summary = meta.summarize(conn, snapshot)
    assert summary["with_deck"] == 2 and summary["share_covered"] == 30.5
    assert summary["macros"] == {"aggro": 20.5, "controle": 10.0}
    assert summary["top_cards"][0] == {"name": "Goblin", "meta_share": 20.5, "avg_copies": 20.0}
    assert summary["avg_lands"] == pytest.approx((22 * 20.5 + 28 * 10) / 30.5, abs=0.05)
    assert summary["stale"] is False
    text = meta.report(snapshot, summary)
    assert "fonte: mtggoldfish" in text and "coletado em" in text and "fora da base: Carta Inexistente" in text


def test_old_snapshot_is_flagged_stale(conn):
    snapshot = update(conn, FakeSite())
    snapshot["collected_at"] = "2026-01-01T00:00:00"
    assert meta.summarize(conn, snapshot)["stale"] is True
    assert "ATENÇÃO" in meta.report(snapshot, meta.summarize(conn, snapshot))
