"""Leitura, resolução, exportação e custo de decklists."""

import difflib
import re
import unicodedata
from dataclasses import dataclass, field

from .query import EXTRA_LAYOUTS

SECTIONS = ("commander", "main", "sideboard")
HEADERS = {
    "deck": "main", "main": "main", "maindeck": "main", "mainboard": "main",
    "sideboard": "sideboard", "side": "sideboard",
    "commander": "commander", "commanders": "commander",
    "companion": "companion", "about": "about",
}
LINE = re.compile(
    r"^(?P<sb>SB:\s*)?(?P<qty>\d+)x?\s+(?P<name>.+?)"
    r"(?:\s+\((?P<set>[A-Za-z0-9]{2,6})\)(?:\s+(?P<number>\S+))?)?$"
)
RARITIES = ("common", "uncommon", "rare", "mythic")


@dataclass
class Entry:
    qty: int
    name: str
    set_code: str | None = None
    number: str | None = None
    card: object = None  # linha de `cards`, preenchida por resolve()


@dataclass
class Deck:
    commander: list = field(default_factory=list)
    main: list = field(default_factory=list)
    sideboard: list = field(default_factory=list)
    companion: list = field(default_factory=list)  # só nomes; a carta já está no sideboard

    def entries(self, *sections):
        return [e for s in (sections or SECTIONS) for e in getattr(self, s)]

    def count(self, *sections):
        return sum(e.qty for e in self.entries(*sections))


def _code_block(text):
    """Em arquivos Markdown, a lista é o primeiro bloco de código."""
    match = re.search(r"```[^\n]*\n(.*?)```", text, flags=re.S)
    return match.group(1) if match else text


def parse(text, markdown=False):
    """Lê listas no formato do Arena, do MTGO (.txt) ou texto simples (`4 Nome`).

    Sem cabeçalhos, a primeira linha em branco depois do deck principal inicia o sideboard.
    """
    if markdown:
        text = _code_block(text)
    deck = Deck()
    section, explicit = "main", False
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            if not explicit and section == "main" and deck.main:
                section = "sideboard"
            continue
        if line.startswith(("#", "//")):
            continue
        header = HEADERS.get(line.rstrip(":").lower())
        if header:
            section, explicit = header, True
            continue
        match = LINE.match(line)
        if not match or section == "about":
            continue
        name = re.sub(r"\s*/{1,3}\s*", " // ", match["name"]) if "/" in match["name"] else match["name"]
        entry = Entry(int(match["qty"]), name, match["set"], match["number"])
        if section == "companion":
            deck.companion.append(name)
        else:
            getattr(deck, "sideboard" if match["sb"] else section).append(entry)
    return deck


def _key(name):
    """Chave de comparação de nomes: minúsculas e sem acentos (Mjölnir = Mjolnir)."""
    folded = unicodedata.normalize("NFKD", name)
    return "".join(c for c in folded if not unicodedata.combining(c)).lower()


def _name_index(conn):
    """nome (minúsculo) → carta. Cartas jogáveis em algum formato têm prioridade em
    nomes repetidos; faces da frente também são chaves."""
    rows = conn.execute(
        "SELECT c.*, EXISTS (SELECT 1 FROM legalities l WHERE l.oracle_id = c.oracle_id) AS playable "
        f"FROM cards c WHERE c.layout NOT IN ({','.join('?' * len(EXTRA_LAYOUTS))}) "
        "ORDER BY playable DESC",
        EXTRA_LAYOUTS,
    ).fetchall()
    index = {}
    for row in rows:
        index.setdefault(_key(row["name"]), row)
    for row in rows:
        if " // " in row["name"]:
            index.setdefault(_key(row["name"].split(" // ")[0]), row)
    return index


def _by_printing(conn, entry):
    """Carta pela coleção e pelo número de colecionador da linha (`(HOB) 4`). É o que
    permite ler listas exportadas pelo Arena em outro idioma, cujos nomes não estão na base."""
    if not entry.set_code or not entry.number:
        return None
    return conn.execute(
        "SELECT c.* FROM printings p JOIN cards c ON c.oracle_id = p.oracle_id "
        "WHERE p.collector_number = ?1 AND p.set_code IN ("
        "  SELECT code FROM sets WHERE code = ?2 COLLATE NOCASE OR arena_code = ?2 COLLATE NOCASE"
        "  UNION SELECT lower(?2)) LIMIT 1",
        (entry.number, entry.set_code),
    ).fetchone()


def resolve(conn, deck):
    """Associa cada linha a uma carta da base. Devolve [(entrada, sugestões)] das não encontradas."""
    index = _name_index(conn)
    unknown = []
    for entry in deck.entries():
        entry.card = index.get(_key(entry.name)) or _by_printing(conn, entry)
        if entry.card is None:
            close = difflib.get_close_matches(_key(entry.name), index.keys(), n=3, cutoff=0.75)
            unknown.append((entry, [index[c]["name"] for c in close]))
    return unknown


def merged(entries):
    """Soma quantidades por carta, preservando a ordem de aparição."""
    totals = {}
    for entry in entries:
        key = entry.card["oracle_id"] if entry.card is not None else entry.name.lower()
        if key in totals:
            totals[key].qty += entry.qty
        else:
            totals[key] = Entry(entry.qty, entry.name, entry.set_code, entry.number, entry.card)
    return list(totals.values())


def export_name(entry, target):
    """Nome como a plataforma espera. No Arena, cartas de duas faces usam só a face da
    frente; cartas split mantêm os dois nomes."""
    card = entry.card
    if card is None:
        return entry.name
    if target == "arena" and " // " in card["name"] and card["layout"] != "split":
        return card["name"].split(" // ")[0]
    return card["name"]


def export(deck, target="text"):
    """Exporta para `arena`, `mtgo` ou `text`. Só nomes, sem coleção: é o que os
    importadores aceitam com mais segurança."""
    def lines(section):
        return [f"{e.qty} {export_name(e, target)}" for e in merged(getattr(deck, section))]

    if target == "mtgo":
        # No .txt do MTGO o comandante vai no bloco do sideboard.
        blocks = [lines("main"), lines("sideboard") + lines("commander")]
        return "\n\n".join("\n".join(b) for b in blocks if b) + "\n"

    titles = {"commander": "Commander", "main": "Deck", "sideboard": "Sideboard"}
    blocks = []
    if deck.companion and target == "arena":
        blocks.append(["Companion"] + [f"1 {name}" for name in deck.companion])
    blocks += [[titles[s]] + lines(s) for s in SECTIONS if getattr(deck, s)]
    return "\n\n".join("\n".join(b) for b in blocks) + "\n"


def diff(before, after):
    """Diferença entre duas listas já resolvidas, por seção: [(variação, nome)], com
    variação negativa para o que saiu e positiva para o que entrou."""
    result = {}
    for section in SECTIONS:
        counts = {}
        for sign, deck in ((-1, before), (1, after)):
            for entry in merged(getattr(deck, section)):
                name = entry.card["name"] if entry.card is not None else entry.name
                counts[name] = counts.get(name, 0) + sign * entry.qty
        changes = sorted(((n, name) for name, n in counts.items() if n), key=lambda x: (x[0] > 0, x[1]))
        if changes:
            result[section] = changes
    return result


def is_basic(card):
    return "Basic" in (card["type_line"] or "").split(" // ")[0].split("—")[0]


def cost(conn, deck):
    """Custo da lista: menor preço em USD/EUR (papel) e tix (MTGO), e wildcards do Arena
    pela menor raridade disponível lá. Terrenos básicos não entram."""
    out = {"usd": 0.0, "eur": 0.0, "tix": 0.0,
           "wildcards": dict.fromkeys(RARITIES, 0),
           "sem_preco": {"usd": [], "eur": [], "tix": []}, "fora_do_arena": []}
    for entry in merged(deck.entries()):
        if entry.card is None or is_basic(entry.card):
            continue
        prints = conn.execute(
            "SELECT games, rarity, usd, eur, tix FROM printings WHERE oracle_id = ?",
            (entry.card["oracle_id"],),
        ).fetchall()
        for key in ("usd", "eur", "tix"):
            prices = [p[key] for p in prints if p[key] is not None]
            if prices:
                out[key] += entry.qty * min(prices)
            else:
                out["sem_preco"][key].append(entry.card["name"])
        rarities = [RARITIES.index(p["rarity"]) for p in prints
                    if "arena" in p["games"] and p["rarity"] in RARITIES]
        if rarities:
            out["wildcards"][RARITIES[min(rarities)]] += entry.qty
        else:
            out["fora_do_arena"].append(entry.card["name"])
    for key in ("usd", "eur", "tix"):
        out[key] = round(out[key], 2)
    return out
