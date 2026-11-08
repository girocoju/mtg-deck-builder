"""Arquétipos de uma coleção (spec 010, componente "sinergia"): os dez pares de cores com
nome, plano e padrões que marcam, no texto de regras de cada carta, se ela é payoff (1,0)
ou enabler (0,5) do par. Os arquivos ficam em `archetypes/<coleção>.json` e citam a
fonte (para FRA, a tela do evento no Arena). `report()` confronta a marcação com os
dados do 17Lands: se as cartas marcadas rendem mais que as outras nas mesmas cores.

Elos diretos entre cartas (spec 014, componente "parceiros" e mapa da coleção): cada
arquétipo é um elo em que a payoff *pede* e a enabler *oferece*; o arquivo pode declarar
`hooks` (ganchos) fora dos dez pares, com padrões `needs` e `provides` (fichas de criatura
e quem as aproveita, planeswalkers e quem os pede...). `Tagger.synergy(a, b)` soma os
elos em que uma carta pede o que a outra oferece; duas payoffs do mesmo arquétipo dividem
o plano e valem metade; se as cores das duas juntas passam de duas, só com splash, e o
elo vale um quarto.
"""

import json
import re
from pathlib import Path

from . import analysis, decklist

ARCHETYPES_DIR = Path(__file__).parent / "archetypes"
PAYOFF, ENABLER = 1.0, 0.5
SHARED_PAYOFF = 0.5       # duas payoffs do mesmo arquétipo: mesmo plano, sem alimentar uma à outra
SPLASH_FACTOR = 0.25      # as duas cartas juntas exigem três cores ou mais
GENERIC_ENABLER = 0.25    # enabler só por estatística (`stat:`: criatura barata, criatura grande): qualquer corpo serve
COLOR_ORDER = "WUBRG"


def load(set_code):
    path = ARCHETYPES_DIR / f"{set_code.lower()}.json"
    return json.loads(path.read_text("utf-8")) if path.exists() else None


def card_text(card):
    text = card["oracle_text"] or ""
    if not text and card["faces"]:
        text = "\n".join((face.get("oracle_text") or "") for face in analysis._faces(card))
    return text.lower()


def _stat(card, name):
    value = card[name]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):       # poder "*" ou "1+*"
        return None


def matches(card, pattern):
    """`re:` texto, `kw:` palavra-chave, `type:` linha de tipo, `stat:` número, `creature`;
    `&` exige todas as condições."""
    if "&" in pattern:
        return all(matches(card, part) for part in pattern.split("&"))
    kind, _, value = pattern.partition(":")
    if kind == "re":
        return re.search(value, card_text(card)) is not None
    if kind == "kw":
        return value.lower() in {k.lower() for k in json.loads(card["keywords"] or "[]")}
    if kind == "type":
        return value in (card["type_line"] or "")
    if kind == "creature":
        return "Creature" in (card["type_line"] or "")
    if kind == "stat":
        match = re.match(r"(power|toughness|cmc)(>=|<=|==)(\d+)", value)
        if not match:
            return False
        actual = _stat(card, match.group(1))
        if actual is None:
            return False
        wanted = float(match.group(3))
        return {">=": actual >= wanted, "<=": actual <= wanted, "==": actual == wanted}[match.group(2)]
    return False


class Tagger:
    def __init__(self, data):
        self.data = data or {"archetypes": {}}
        self.archetypes = self.data.get("archetypes", {})
        self.hooks = self.data.get("hooks", {})      # {nome: {"needs": [...], "provides": [...], "weight": 1.0}}
        self._cache = {}
        self._links = {}

    def __bool__(self):
        return bool(self.archetypes)

    def name(self, pair):
        return (self.archetypes.get(pair) or {}).get("name", "")

    def links(self, card):
        """{"needs": {elo: peso}, "provides": {elo: peso}}. Elos: os pares (payoff pede com
        peso 1; enabler oferece com peso 1, ou `GENERIC_ENABLER` quando só um padrão `stat:`
        a marca) e os ganchos do arquivo (`needs` com o peso do gancho, `provides` com 1)."""
        if card is None:
            return {"needs": {}, "provides": {}}
        key = card["name"]
        if key not in self._links:
            needs, provides = {}, {}
            for pair, spec in self.archetypes.items():
                if any(matches(card, p) for p in spec.get("payoffs", [])):
                    needs[pair] = 1.0
                    continue
                enablers = spec.get("enablers", [])
                if any(matches(card, p) for p in enablers if not p.startswith("stat:")):
                    provides[pair] = 1.0
                elif any(matches(card, p) for p in enablers if p.startswith("stat:")):
                    provides[pair] = GENERIC_ENABLER
            for hook, spec in self.hooks.items():
                if any(matches(card, p) for p in spec.get("needs", [])):
                    needs[hook] = float(spec.get("weight", 1.0))
                if any(matches(card, p) for p in spec.get("provides", [])):
                    provides[hook] = 1.0
            self._links[key] = {"needs": needs, "provides": provides}
        return self._links[key]

    def link_scores(self, a, b):
        """{elo: valor} entre duas cartas, cada elo contado uma vez: peso de quem pede × peso
        de quem oferece quando uma pede o que a outra oferece; `SHARED_PAYOFF` quando as duas
        são payoff do mesmo arquétipo e nenhuma oferece."""
        if a is None or b is None or a["name"] == b["name"]:
            return {}
        la, lb = self.links(a), self.links(b)
        scores = {}
        for first, second in ((la, lb), (lb, la)):
            for link, weight in first["needs"].items():
                if link in second["provides"]:
                    scores[link] = max(scores.get(link, 0.0), weight * second["provides"][link])
                elif link in second["needs"] and link in self.archetypes:
                    scores[link] = max(scores.get(link, 0.0), weight * SHARED_PAYOFF)
        return scores

    def synergy(self, a, b):
        """Elos diretos entre duas cartas, em unidades (1,0 = payoff com enabler pleno de um
        elo), vezes `SPLASH_FACTOR` se as cores das duas juntas passam de duas."""
        scores = self.link_scores(a, b)
        if not scores:
            return 0.0
        total = sum(scores.values())
        colors = set(a["colors"] or "") | set(b["colors"] or "")
        return total * SPLASH_FACTOR if len(colors) > 2 else total

    def links_between(self, a, b):
        """Nomes dos elos que ligam as duas cartas, do mais forte para o mais fraco."""
        scores = self.link_scores(a, b)
        return sorted(scores, key=lambda link: (-scores[link], link))

    @staticmethod
    def label_links(links):
        """`pede WR, fichas · oferece WB` para a tabela do mapa."""
        parts = []
        if links["needs"]:
            parts.append("pede " + ", ".join(sorted(links["needs"])))
        if links["provides"]:
            parts.append("oferece " + ", ".join(sorted(links["provides"])))
        return " · ".join(parts)

    def tags(self, card):
        """{par: 1.0 payoff | 0.5 enabler} para os pares que a carta serve."""
        if card is None:
            return {}
        key = card["name"]
        if key not in self._cache:
            found = {}
            for pair, spec in self.archetypes.items():
                if any(matches(card, p) for p in spec.get("payoffs", [])):
                    found[pair] = PAYOFF
                elif any(matches(card, p) for p in spec.get("enablers", [])):
                    found[pair] = ENABLER
            self._cache[key] = found
        return self._cache[key]

    @staticmethod
    def label(tags):
        """`UB+ WU` (+ = payoff), em ordem de peso."""
        return " ".join(f"{pair}{'+' if score >= PAYOFF else ''}" for pair, score in sorted(tags.items(), key=lambda kv: -kv[1]))


def report(conn, set_code, ratings, tagger, top=8, min_games=500):
    """Por arquétipo: quantas cartas marcadas por raridade, as mais fortes e a diferença,
    em pontos acima da média da fonte (17Lands ou Untapped), entre cartas marcadas e não
    marcadas nas cores do par. `ratings` é um `draft_pick.Ratings`."""
    rows = conn.execute(
        "SELECT c.*, MIN(p.rarity) AS set_rarity FROM cards c JOIN printings p ON p.oracle_id = c.oracle_id "
        "WHERE p.set_code = ? AND c.layout NOT IN ('token', 'double_faced_token', 'emblem', 'art_series') "
        "GROUP BY c.oracle_id", (set_code.lower(),)).fetchall()
    snapshot = ratings.snapshot or {}
    listed = {decklist._key(c["name"]) for c in snapshot.get("cards", [])}
    listed |= {decklist._key(c["name"].split(" // ")[0]) for c in snapshot.get("cards", [])}
    cards = []
    for row in rows:
        if listed and decklist._key(row["name"]) not in listed and decklist._key(row["name"].split(" // ")[0]) not in listed:
            continue
        power = ratings.power(row["name"], row, row["set_rarity"])
        measured = not power["theoretical"] and (power.get("games") or 0) >= min_games
        cards.append((row, power if measured else None))
    out = []
    for pair, spec in tagger.archetypes.items():
        colors = set(pair)
        in_colors = [(row, power) for row, power in cards if row["colors"] and set(row["colors"]) <= colors]
        tagged = [(row, power, tagger.tags(row)[pair]) for row, power in in_colors if pair in tagger.tags(row)]
        untagged = [(row, power, 0.0) for row, power in in_colors if pair not in tagger.tags(row)]

        def mean(items):
            weighted = [(p["points"], p["games"]) for _r, p, _s in items if p]
            games = sum(g for _w, g in weighted)
            return (sum(w * g for w, g in weighted) / games, len(weighted)) if games else (None, 0)

        tagged_mean, tagged_n = mean(tagged)
        untagged_mean, untagged_n = mean(untagged)
        rarities = {}
        for row, _power, _score in tagged:
            rarities[row["set_rarity"]] = rarities.get(row["set_rarity"], 0) + 1
        best = sorted([t for t in tagged if t[1]], key=lambda t: -t[1]["points"])[:top]
        out.append({
            "pair": pair, "name": spec.get("name", ""), "plan": spec.get("plan", ""),
            "win_rate": ratings.pairs.get(pair),
            "tagged": len(tagged), "payoffs": sum(1 for *_, s in tagged if s >= PAYOFF),
            "rarities": rarities, "in_colors": len(in_colors),
            "tagged_mean": tagged_mean, "tagged_n": tagged_n, "untagged_mean": untagged_mean, "untagged_n": untagged_n,
            "best": [{"name": r["name"], "rarity": r["set_rarity"], "points": round(p["points"], 1),
                      "gih": p.get("gih"), "games": p["games"], "source": p["source"],
                      "role": "payoff" if score >= PAYOFF else "enabler"} for r, p, score in best],
        })
    return {"set": set_code, "sources": ratings.describe(), "source": tagger.data.get("source", ""), "archetypes": out}


def format_report(data):
    lines = [f"Arquétipos de {data['set'].upper()} · fonte: {data['source']}",
             f"dados: {data['sources']}",
             "números em pontos percentuais acima da média da fonte da carta; a diferença entre marcadas e não "
             "marcadas, nas cores do par, mede se a marcação carrega sinal"]
    for a in data["archetypes"]:
        wr = f" · par {a['win_rate']:.1%}" if a["win_rate"] else ""
        rar = ", ".join(f"{k[:1].upper()} {v}" for k, v in sorted(a["rarities"].items()))
        lines += ["", f"{a['pair']} {a['name']}{wr}", f"  {a['plan']}",
                  f"  marcadas: {a['tagged']} de {a['in_colors']} cartas nas cores ({a['payoffs']} payoffs; {rar})"]
        if a["tagged_mean"] is not None and a["untagged_mean"] is not None:
            lines.append(f"  marcadas {a['tagged_mean']:+.1f} pp ({a['tagged_n']} com dados) × não marcadas "
                         f"{a['untagged_mean']:+.1f} pp ({a['untagged_n']}) → diferença {a['tagged_mean'] - a['untagged_mean']:+.1f} pp")
        for b in a["best"]:
            lines.append(f"    {b['points']:+5.1f} {b['games']:>5} {b['source']:<9} {b['rarity'][:1].upper()} "
                         f"{b['role']:<7} {b['name']}")
    return "\n".join(lines)
