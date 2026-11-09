"""Mapa de picks de uma coleção (spec 014): o peso de cada carta, pronto antes do draft.

Para toda carta draftável da coleção: o poder pelas fontes (17Lands → Untapped →
Draftsim → teórica), os arquétipos que serve e os elos que pede e oferece
(`archetypes.Tagger.links`). Daí saem:

1. a **ordem de pick** geral e por raridade (o que se compara no P1P1: a rara do pacote
   contra a melhor incomum e a melhor comum);
2. para qualquer sequência de picks, o **ranking da coleção inteira como próximo pick**,
   pelo motor da spec 010 com o componente `parceiros`: é a árvore de escolhas (raras e
   míticas no primeiro pick, os melhores segundos picks para cada uma, e os picks
   seguintes sob demanda, com `--card A --card B ...`);
3. os **pares de cartas com mais sinergia direta** e, por carta, os parceiros.

`overview()` e `analysis_lines()` fazem a leitura da coleção (cores, curva, remoção,
mecânicas, correção de mana, profundidade de cada arquétipo). `draft_map_pdf.render()`
desenha tudo, com o guia da coleção, no documento único `drafts/<coleção>/<coleção>.pdf`;
`markdown()` é a versão em texto para uso interno (`data/maps/`). Tudo é intrínseco à
coleção e aos dados de partidas: só muda quando eles mudam, não com o draft em curso.
"""

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from . import analysis, archetypes, db, decklist, draft_pick
from .draft_sim import EXTRA_LAYOUTS

DRAFTS_DIR = Path(__file__).resolve().parents[2] / "drafts"   # um diretório por coleção: guia.md e <código>.pdf
MAPS_DIR = db.DATA_DIR / "maps"                                 # Markdown do mapa, uso interno (fora do git)
RARITY_ORDER = ("mythic", "rare", "uncommon", "common")
RARITY_PT = {"mythic": "míticas", "rare": "raras", "uncommon": "incomuns", "common": "comuns"}
COLOR_GROUPS = ("W", "U", "B", "R", "G", "multi", "incolor")
COLOR_PT = {"W": "branco", "U": "azul", "B": "preto", "R": "vermelho", "G": "verde",
            "multi": "multicoloridas", "incolor": "incolores"}
CURVE_SPLIT = (0.65, 0.5)    # parcela das criaturas C+U que custam até 3: curva baixa / média / alta
DEPTH_DEEP, DEPTH_SHALLOW = 6, 3   # payoffs em comum e incomum: arquétipo profundo / raso (depende da rara)


def color_group(colors):
    """`W`..`G`, `multi` ou `incolor`, a partir da string de cores da base."""
    colors = colors or ""
    return colors if len(colors) == 1 else "multi" if colors else "incolor"
DAMPING = 0.85            # centralidade: chance de o passeio seguir um elo em vez de recomeçar em carta aleatória
POWER_SHIFT = 5.0         # poder deslocado para ficar positivo ao pesar parceiras (−5 pontos ≈ carta injogável)
COMMUNITY_MIN_WEIGHT = 1.5   # comunidades só sobre pares ligados por mais de um elo; com 1,0 FRA vira um grupo só
COMMUNITY_WEIGHTS = (1.5, 2.0, 2.5)   # limiares testados por `communities_auto`: fica o que dá mais grupos (empate: o menor)


def draftable(conn, set_code, snapshot=None):
    """Cartas draftáveis da coleção (linhas da base com `set_rarity`), sem terrenos básicos:
    as da lista do 17Lands quando há snapshot; senão as impressões de booster; senão todas."""
    rows = conn.execute(
        "SELECT c.*, MIN(p.rarity) AS set_rarity, MAX(p.booster) AS booster FROM cards c "
        "JOIN printings p ON p.oracle_id = c.oracle_id WHERE p.set_code = ? "
        f"AND c.layout NOT IN ({','.join('?' * len(EXTRA_LAYOUTS))}) GROUP BY c.oracle_id",
        (set_code.lower(), *EXTRA_LAYOUTS)).fetchall()
    listed = set()
    for card in (snapshot or {}).get("cards", []):
        listed.add(decklist._key(card["name"]))
        listed.add(decklist._key(card["name"].split(" // ")[0]))
    in_booster = any(r["booster"] for r in rows)
    out = []
    for row in rows:
        if "Basic" in (row["type_line"] or ""):
            continue
        key, front = decklist._key(row["name"]), decklist._key(row["name"].split(" // ")[0])
        if listed and key not in listed and front not in listed:
            continue
        if not listed and in_booster and not row["booster"]:
            continue
        out.append(row)
    return out


class SetMap:
    def __init__(self, conn, set_code, ratings, mode="premier", tagger=None):
        self.conn, self.set_code, self.ratings, self.mode = conn, set_code.lower(), ratings, mode
        self.tagger = tagger or archetypes.Tagger(archetypes.load(self.set_code))
        self.engine = draft_pick.Engine(conn, ratings, self.set_code, mode, archetype_data=self.tagger.data)
        self.engine.tagger = self.tagger
        self.rows = {row["name"]: row for row in draftable(conn, self.set_code, ratings.snapshot)}
        self.cards = {}
        for name, row in self.rows.items():
            power = ratings.power(name, row, row["set_rarity"])
            links = self.tagger.links(row)
            self.cards[name] = {
                "name": name, "raridade": row["set_rarity"] or "?", "cor": row["colors"] or "-",
                "custo": row["mana_cost"] or "", "cmc": row["cmc"], "tipo": analysis._front(row, "type_line"),
                "poder": round(power["points"], 2), "fonte": power["source"], "teorica": power["theoretical"],
                "gih": power.get("gih"), "jogos": power.get("games", 0), "alsa": power.get("alsa"),
                "arquetipos": self.tagger.label(self.tagger.tags(row)),
                "pede": sorted(links["needs"]), "oferece": sorted(links["provides"]),
                "funcoes": sorted(draft_pick.functions(row)),
            }
        self._pairs = None
        self._totals = None

    # --- leitura -------------------------------------------------------------------------

    def coverage(self):
        """Quantas cartas vêm de cada fonte de poder."""
        counts = {}
        for entry in self.cards.values():
            counts[entry["fonte"]] = counts.get(entry["fonte"], 0) + 1
        return dict(sorted(counts.items(), key=lambda kv: -kv[1]))

    def resolve(self, name):
        """Nome canônico na coleção, ou None."""
        card = self.engine.card(name)
        return card["name"] if card is not None and card["name"] in self.cards else None

    # --- ordem de pick -------------------------------------------------------------------

    def pick_order(self, rarity=None, top=None):
        """Cartas em ordem de poder (o que decide o P1P1), com a soma dos elos na coleção."""
        rows = [dict(e) for e in self.cards.values() if not rarity or e["raridade"] == rarity]
        rows.sort(key=lambda e: (-e["poder"], e["name"]))
        totals = self.partner_totals()
        for position, row in enumerate(rows, 1):
            row["posicao"] = position
            row["elos"] = round(totals.get(row["name"], 0.0), 1)
        return rows[:top] if top else rows

    # --- sinergia direta -----------------------------------------------------------------

    def pairs(self):
        """[{a, b, sinergia, elos, poder}] para todo par com sinergia > 0, do maior para o menor
        (empate pela soma de poder). Calculado uma vez."""
        if self._pairs is None:
            linked = [row for row in self.rows.values() if any(self.tagger.links(row).values())]
            out = []
            for i, a in enumerate(linked):
                for b in linked[i + 1:]:
                    score = self.tagger.synergy(a, b)
                    if score > 0:
                        out.append({"a": a["name"], "b": b["name"], "sinergia": round(score, 2),
                                    "elos": self.tagger.links_between(a, b),
                                    "poder": round(self.cards[a["name"]]["poder"] + self.cards[b["name"]]["poder"], 1)})
            out.sort(key=lambda p: (-p["sinergia"], -p["poder"], p["a"]))
            self._pairs = out
        return self._pairs

    def partner_totals(self):
        """{carta: soma das sinergias com toda a coleção}."""
        if self._totals is None:
            totals = {}
            for pair in self.pairs():
                totals[pair["a"]] = totals.get(pair["a"], 0.0) + pair["sinergia"]
                totals[pair["b"]] = totals.get(pair["b"], 0.0) + pair["sinergia"]
            self._totals = totals
        return self._totals

    def partners(self, name, top=8):
        """Cartas da coleção com elo direto com `name`, da maior sinergia (e poder) para a menor."""
        found = []
        for pair in self.pairs():
            if name in (pair["a"], pair["b"]):
                other = pair["b"] if pair["a"] == name else pair["a"]
                entry = self.cards[other]
                found.append({"name": other, "sinergia": pair["sinergia"], "elos": pair["elos"],
                              "poder": entry["poder"], "raridade": entry["raridade"], "cor": entry["cor"]})
        found.sort(key=lambda p: (-p["sinergia"], -p["poder"]))
        return found[:top] if top else found

    # --- árvore de picks -----------------------------------------------------------------

    def follow_ups(self, picked, pack=None, pick=None, top=None):
        """Ranking da coleção inteira como próximo pick depois de `picked` (nomes, em ordem),
        pelo motor da spec 010. Sem pacote e pick, o seguinte ao último pick."""
        names = [self.resolve(n) or n for n in picked]
        state = draft_pick.DraftState(self.set_code, self.mode)
        state.add_picks(names)
        if not (pack and pick):
            pack, pick = state.next_position()
        taken = {decklist._key(n) for n in names}
        candidates = [n for n in self.cards if decklist._key(n) not in taken]
        result = self.engine.rank(state, pack, pick, candidates)
        if top:
            result["cartas"] = result["cartas"][:top]
        result["picks"] = names
        result["desconhecidas"] = [n for n in picked if self.resolve(n) is None]
        return result

    def tree(self, firsts=None, top=6):
        """Para cada candidato a primeiro pick (padrão: raras e míticas, em ordem de poder),
        os melhores segundos picks da coleção."""
        if firsts is None:
            firsts = [e["name"] for e in self.pick_order() if e["raridade"] in ("rare", "mythic")]
        return [{"primeiro": self.cards[name], "seguintes": self.follow_ups([name], 1, 2, top)["cartas"]}
                for name in firsts]

    # --- grafo de elos -------------------------------------------------------------------

    def graph(self):
        """Lista de adjacência {carta: {parceira: sinergia}}: as cartas são os nós, os elos
        diretos são as arestas com peso."""
        adjacency = {name: {} for name in self.cards}
        for pair in self.pairs():
            adjacency[pair["a"]][pair["b"]] = pair["sinergia"]
            adjacency[pair["b"]][pair["a"]] = pair["sinergia"]
        return adjacency

    def strength(self, name):
        return max(0.5, self.cards[name]["poder"] + POWER_SHIFT)

    def centrality(self, iterations=60):
        """Centralidade no grafo de elos (0 a 100, máximo = 100): um passeio aleatório que, em
        cada carta, segue um elo com chance proporcional ao peso do elo vezes a força da
        parceira (PageRank com pesos), ou recomeça em carta aleatória. Carta central é a que
        liga muitas parceiras fortes que, por sua vez, ligam outras; carta sem elo fica no
        mínimo."""
        adjacency = self.graph()
        names = list(adjacency)
        if not names:
            return {}
        total = len(names)
        weight = {n: {m: w * self.strength(m) for m, w in adjacency[n].items()} for n in names}
        out = {n: sum(weight[n].values()) for n in names}
        score = {n: 1.0 / total for n in names}
        for _ in range(iterations):
            new = {n: (1 - DAMPING) / total for n in names}
            for m in names:
                if not out[m]:
                    continue
                share = DAMPING * score[m] / out[m]
                for n, w in weight[m].items():
                    new[n] += share * w
            score = new
        peak = max(score.values()) or 1.0
        return {n: round(100 * v / peak, 1) for n, v in score.items()}

    def communities(self, min_size=3, iterations=30, min_weight=COMMUNITY_MIN_WEIGHT):
        """Agrupamentos por propagação de rótulos com pesos (cada carta adota o rótulo que
        pesa mais entre as parceiras, até estabilizar), só sobre as arestas de peso
        `min_weight` ou mais (pares ligados por mais de um elo: um elo só, e sobretudo o
        enabler genérico, não define grupo). Devolve os grupos com `min_size` cartas ou mais,
        do maior para o menor, com cores, pares oficiais e elos dominantes. Comunidades que
        cruzam os dez pares são o que o mapa por arquétipo não mostra."""
        adjacency = {n: {m: w for m, w in links.items() if w >= min_weight} for n, links in self.graph().items()}
        label = {n: n for n in adjacency}
        order = sorted(adjacency)
        for _ in range(iterations):
            changed = False
            for n in order:
                if not adjacency[n]:
                    continue
                votes = {}
                for m, w in adjacency[n].items():
                    votes[label[m]] = votes.get(label[m], 0.0) + w
                votes[label[n]] = votes.get(label[n], 0.0) + 1e-9      # desempate a favor do rótulo atual
                best = sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
                if best != label[n]:
                    label[n], changed = best, True
            if not changed:
                break
        groups = {}
        for n, tag in label.items():
            if adjacency[n]:
                groups.setdefault(tag, []).append(n)
        out = []
        for members in groups.values():
            if len(members) < min_size:
                continue
            members.sort(key=lambda n: -self.cards[n]["poder"])
            colors = Counter(c for n in members for c in self.cards[n]["cor"] if c in "WUBRG")
            pairs = Counter(tag.rstrip("+") for n in members for tag in self.cards[n]["arquetipos"].split())
            links = Counter(link for n in members for link in self.cards[n]["pede"] + self.cards[n]["oferece"])
            out.append({"cartas": members, "tamanho": len(members),
                        "poder": round(sum(self.cards[n]["poder"] for n in members) / len(members), 1),
                        "cores": colors.most_common(3), "pares": pairs.most_common(3), "elos": links.most_common(3)})
        out.sort(key=lambda g: (-g["tamanho"], -g["poder"]))
        return out

    def communities_auto(self, min_size=3):
        """Comunidades com o limiar de peso, entre `COMMUNITY_WEIGHTS`, que dá mais grupos legíveis
        (empate: o menor limiar). Em FRA fica 1,5 (quatro grupos); em TRK, com mais ganchos,
        1,5 dá um grupo de 135 cartas e 2,0 dá seis grupos. Devolve (grupos, limiar)."""
        best = None
        for weight in COMMUNITY_WEIGHTS:
            groups = self.communities(min_size=min_size, min_weight=weight)
            if best is None or len(groups) > len(best[0]):
                best = (groups, weight)
        return best

    def archetype_tables(self, top=10):
        """Por par: payoffs e enablers marcados, em ordem de poder."""
        out = []
        for pair, spec in self.tagger.archetypes.items():
            payoffs, enablers = [], []
            for name, row in self.rows.items():
                score = self.tagger.tags(row).get(pair)
                if score is None:
                    continue
                (payoffs if score >= archetypes.PAYOFF else enablers).append(self.cards[name])
            payoffs.sort(key=lambda e: -e["poder"])
            enablers.sort(key=lambda e: -e["poder"])
            out.append({"pair": pair, "name": spec.get("name", ""), "plan": spec.get("plan", ""),
                        "win_rate": self.ratings.pairs.get(pair), "payoffs": payoffs[:top], "enablers": enablers[:top],
                        "total_payoffs": len(payoffs), "total_enablers": len(enablers)})
        return out

    # --- leitura da coleção --------------------------------------------------------------

    def overview(self):
        """Leitura da coleção sobre as cartas do mapa (mesmo modelo de `draft.set_overview`):
        por grupo de cor, contagem por raridade, criaturas de comum e incomum com a curva e a
        parcela até custo 3, remoção de comum e incomum (classificação automática de
        `analysis.roles`, a conferir); palavras-chave com os grupos em que aparecem; correção
        de mana; multicoloridas por par. Calculada uma vez."""
        if getattr(self, "_overview", None) is not None:
            return self._overview
        groups = {g: {"total": 0, **{r: 0 for r in RARITY_ORDER}, "criaturas_cu": 0, "baratas_cu": 0,
                      "curva_cu": {str(i): 0 for i in range(1, 7)}, "remocao_cu": []} for g in COLOR_GROUPS}
        keywords, pairs = {}, {}
        fixing = {"terrenos": [], "landcycling": [], "qualquer_cor": []}
        for name, row in self.rows.items():
            entry = self.cards[name]
            group = color_group(row["colors"])
            table = groups[group]
            table["total"] += 1
            if entry["raridade"] in table:
                table[entry["raridade"]] += 1
            words = json.loads(row["keywords"] or "[]")
            for keyword in words:
                keywords.setdefault(keyword, Counter())[group] += 1
            text = archetypes.card_text(row)
            if analysis.is_land(row):
                fixing["terrenos"].append(name)
            if any("landcycling" in word.lower() for word in words):
                fixing["landcycling"].append(name)
            if "mana of any color" in text or "mana of any one color" in text:
                fixing["qualquer_cor"].append(name)
            if group == "multi" and len(row["colors"]) == 2:
                pairs.setdefault(row["colors"], []).append(name)
            if entry["raridade"] in ("common", "uncommon"):
                if "Creature" in analysis._front(row, "type_line"):
                    table["criaturas_cu"] += 1
                    cmc = int(row["cmc"] or 0)
                    table["curva_cu"][str(min(max(cmc, 1), 6))] += 1
                    if cmc <= 3:
                        table["baratas_cu"] += 1
                roles = analysis.roles(row)
                if "remoção pontual" in roles or "remoção em massa" in roles:
                    table["remocao_cu"].append(name)
        ordered = sorted(keywords.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))
        self._overview = {
            "grupos": groups,
            "palavras": [(word, sum(count.values()), count.most_common(3)) for word, count in ordered[:16]],
            "correcao": fixing, "pares_multicor": pairs,
            "raridades": {r: sum(1 for e in self.cards.values() if e["raridade"] == r) for r in RARITY_ORDER},
        }
        return self._overview

    def archetype_summary(self):
        """Por par: quantas payoffs e enablers (e quantas delas comuns ou incomuns), a payoff e o
        enabler mais fortes, as multicoloridas do par (sinalizadoras) e a profundidade: profundo
        com `DEPTH_DEEP` payoffs ou mais em comum e incomum, raso com `DEPTH_SHALLOW` ou menos
        (depende de abrir a rara)."""
        multi = self.overview()["pares_multicor"]
        out = []
        for table in self.archetype_tables(top=None):
            def cu(rows):
                return sum(1 for e in rows if e["raridade"] in ("common", "uncommon"))
            payoffs_cu = cu(table["payoffs"])
            depth = "profundo" if payoffs_cu >= DEPTH_DEEP else "raso" if payoffs_cu <= DEPTH_SHALLOW else "médio"
            out.append({"pair": table["pair"], "name": table["name"], "plan": table["plan"], "win_rate": table["win_rate"],
                        "payoffs": table["total_payoffs"], "enablers": table["total_enablers"],
                        "payoffs_cu": payoffs_cu, "enablers_cu": cu(table["enablers"]),
                        "top_payoff": table["payoffs"][0] if table["payoffs"] else None,
                        "top_enabler": table["enablers"][0] if table["enablers"] else None,
                        "sinalizadoras": multi.get(table["pair"], []), "profundidade": depth})
        return out

    def hook_summary(self):
        """Por gancho: quantas cartas pedem e quantas oferecem."""
        out = []
        for hook in self.tagger.hooks:
            needs = sum(1 for e in self.cards.values() if hook in e["pede"])
            provides = sum(1 for e in self.cards.values() if hook in e["oferece"])
            out.append({"hook": hook, "pedem": needs, "oferecem": provides})
        return out


# --- apresentação ------------------------------------------------------------------------

def _mark(entry):
    return "*" if entry.get("teorica") else ""


def _links(entry):
    return archetypes.Tagger.label_links({"needs": entry["pede"], "provides": entry["oferece"]})


def format_order(setmap, rows, set_name="", sources=""):
    coverage = ", ".join(f"{k} {v}" for k, v in setmap.coverage().items())
    lines = [f"{set_name or setmap.set_code.upper()} · mapa de picks · {len(setmap.cards)} cartas draftáveis · "
             f"fonte do poder: {coverage}"]
    if sources:
        lines.append(f"dados: {sources}")
    lines.append("  #   nota fonte     rar cor  custo      carta · arquétipos · elos · Σ sinergia na coleção")
    for row in rows:
        tags = f" · {row['arquetipos']}" if row["arquetipos"] else ""
        links = _links(row)
        lines.append(f"{row['posicao']:3d} {row['poder']:+6.1f} {row['fonte']:<9} {row['raridade'][:1].upper()}   "
                     f"{row['cor']:<4} {row['custo']:<10} {row['name']}{tags}"
                     + (f" · {links}" if links else "") + (f" · Σ{row['elos']:g}" if row["elos"] else ""))
    if any(r["teorica"] for r in rows):
        lines.append("* nota teórica (sem amostra nos dados de partidas)")
    return "\n".join(lines)


def format_pairs(setmap, rows):
    lines = [f"{setmap.set_code.upper()} · pares com mais sinergia direta (unidades de elo; empate pela soma de poder)",
             " sin   poder  carta A ↔ carta B (elos)"]
    for pair in rows:
        lines.append(f"{pair['sinergia']:4.1f}  {pair['poder']:+6.1f}  {pair['a']} ↔ {pair['b']} ({', '.join(pair['elos'])})")
    return "\n".join(lines)


def _community_lines(setmap, groups, members=8):
    lines = []
    for i, group in enumerate(groups, 1):
        colors = "".join(c for c, _n in group["cores"])
        pairs = ", ".join(f"{p} {n}" for p, n in group["pares"]) or "nenhum par marcado"
        links = ", ".join(f"{l} {n}" for l, n in group["elos"])
        lines.append(f"{i}. {group['tamanho']} cartas, poder médio {group['poder']:+.1f}, cores {colors or '-'} · pares {pairs} · "
                     f"elos {links}: " + ", ".join(group["cartas"][:members]) + (" …" if group["tamanho"] > members else ""))
    return lines


def analysis_lines(setmap):
    """Leitura da coleção e dos arquétipos em frases, a partir de `overview()`,
    `archetype_summary()` e do grafo; cada frase cita a seção da teoria
    (`knowledge/limitado-e-draft.md`) que a sustenta. Usada no Markdown e no PDF."""
    ov = setmap.overview()
    groups, rarities = ov["grupos"], ov["raridades"]
    lines = []
    lines.append(f"**Composição.** {len(setmap.cards)} cartas draftáveis ("
                 + ", ".join(f"{rarities[r]} {RARITY_PT[r]}" for r in RARITY_ORDER) + "). Por cor: "
                 + ", ".join(f"{COLOR_PT[g]} {groups[g]['total']}" for g in COLOR_GROUPS if groups[g]["total"])
                 + f". As {groups['multi']['uncommon']} multicoloridas incomuns são as sinalizadoras dos pares "
                 "(teoria: `limitado-e-draft.md` §4, arquétipos).")
    creatures = {c: groups[c]["criaturas_cu"] for c in "WUBRG"}
    total_creatures = sum(groups[g]["criaturas_cu"] for g in COLOR_GROUPS)
    cheap = sum(groups[g]["baratas_cu"] for g in COLOR_GROUPS)
    share = cheap / total_creatures if total_creatures else 0.0
    speed = ("curva baixa: o formato tende a ser rápido" if share >= CURVE_SPLIT[0]
             else "curva média" if share >= CURVE_SPLIT[1]
             else "curva alta: o formato tende a ser lento, com mais espaço para valor")
    best, worst = max(creatures, key=creatures.get), min(creatures, key=creatures.get)
    lines.append(f"**Criaturas de comum e incomum.** {total_creatures} no total; {COLOR_PT[best]} tem mais ({creatures[best]}) "
                 f"e {COLOR_PT[worst]} menos ({creatures[worst]}). {share:.0%} custam até 3 ({speed}; §2 custo e curva, "
                 "§8 parâmetros do formato). Curva por cor, custo 1 a 6+: "
                 + "; ".join(f"{c} {' '.join(str(groups[c]['curva_cu'][str(i)]) for i in range(1, 7))}" for c in "WUBRG") + ".")
    removal = {g: groups[g]["remocao_cu"] for g in COLOR_GROUPS if groups[g]["remocao_cu"]}
    lines.append("**Remoção de comum e incomum** (classificação automática pelo texto; confira com `mtg card`): "
                 + "; ".join(f"{COLOR_PT[g]} {len(names)}: {', '.join(names)}" for g, names in removal.items())
                 + ". Remoção é a prioridade de pick depois das bombas (§2 removal, §3 prioridades); a cor com menos "
                 "remoção depende da segunda cor.")
    lines.append("**Mecânicas e palavras-chave** (ocorrências e grupos de cor): "
                 + "; ".join(f"{word} {n} ({', '.join(f'{g} {m}' for g, m in top)})" for word, n, top in ov["palavras"][:10]) + ".")
    fixing = ov["correcao"]
    lines.append(f"**Correção de mana.** {len(fixing['terrenos'])} terrenos não básicos draftáveis, "
                 f"{len(fixing['landcycling'])} cartas com landcycling e {len(fixing['qualquer_cor'])} fontes de mana de "
                 "qualquer cor" + (": " + ", ".join(fixing["qualquer_cor"][:8]) if fixing["qualquer_cor"] else "")
                 + ". Quanto mais correção, mais compensa o splash de uma bomba ou remoção (§2 card advantage e correção "
                 "de mana; §7 construção).")
    if setmap.ratings.pairs and setmap.ratings.baseline:
        base = setmap.ratings.baseline
        ranked = sorted(setmap.ratings.pairs.items(), key=lambda kv: -kv[1])
        lines.append(f"**Pares nos dados** ({setmap.ratings.describe().split(' · ')[0]}; win rate do par e diferença para a "
                     f"média {base:.1%}): " + ", ".join(f"{p} {wr:.1%} ({(wr - base) * 100:+.1f})" for p, wr in ranked)
                     + f". Entre o melhor e o pior par há {(ranked[0][1] - ranked[-1][1]) * 100:.1f} pontos.")
    else:
        lines.append("**Pares nos dados.** Sem dados de partidas para esta coleção: a leitura dos pares é teórica, pela "
                     "contagem de payoffs e enablers marcados no texto das cartas, e deve ser refeita com "
                     f"`mtg draft update {setmap.set_code}` quando o 17Lands publicar.")
    parts = []
    for s in setmap.archetype_summary():
        top = s["top_payoff"]
        parts.append(f"{s['pair']} {s['name']}: {s['payoffs']} payoffs ({s['payoffs_cu']} C/U) e {s['enablers']} enablers "
                     f"({s['enablers_cu']} C/U), {s['profundidade']}"
                     + (f"; melhor payoff {top['name']} {top['poder']:+.1f}{_mark(top)}" if top else "")
                     + (f"; sinalizadoras {', '.join(s['sinalizadoras'])}" if s["sinalizadoras"] else ""))
    lines.append(f"**Arquétipos** (profundo = {DEPTH_DEEP} ou mais payoffs em comum e incomum; raso = {DEPTH_SHALLOW} ou menos, "
                 "depende de abrir a rara; §4 arquétipos e deck perfeito): " + " · ".join(parts) + ".")
    hooks = setmap.hook_summary()
    if hooks:
        lines.append("**Ganchos fora dos dez pares** (quem pede / quem oferece): "
                     + ", ".join(f"{h['hook']} {h['pedem']}/{h['oferecem']}" for h in hooks) + ".")
    central = sorted(setmap.centrality().items(), key=lambda kv: -kv[1])[:5]
    communities, weight = setmap.communities_auto()
    lines.append("**Grafo.** Cartas mais centrais (portas de entrada para a coleção): "
                 + ", ".join(f"{n} {v:g}" for n, v in central)
                 + f". {len(communities)} comunidades com 3 cartas ou mais (elos de peso ≥ {weight:g})"
                 + (": " + "; ".join(f"{g['tamanho']} cartas ({''.join(c for c, _n in g['cores']) or '-'}; elos "
                                     f"{', '.join(l for l, _n in g['elos'][:2])})" for g in communities[:4]) if communities else "")
                 + ".")
    return lines


def format_graph(setmap, top=20):
    central = setmap.centrality()
    totals = setmap.partner_totals()
    ranked = sorted(central.items(), key=lambda kv: -kv[1])[:top]
    lines = [f"{setmap.set_code.upper()} · grafo de elos: {len(setmap.cards)} cartas, {len(setmap.pairs())} arestas",
             "centralidade (0–100): passeio aleatório pelos elos preferindo parceiras fortes; Σ = soma das sinergias",
             " centr.    Σ   nota  rar cor  carta · elos"]
    for name, value in ranked:
        entry = setmap.cards[name]
        lines.append(f"{value:6.1f} {totals.get(name, 0.0):5.1f} {entry['poder']:+6.1f}{_mark(entry)} {entry['raridade'][:1].upper()}   "
                     f"{entry['cor']:<4} {name}" + (f" · {_links(entry)}" if _links(entry) else ""))
    groups, weight = setmap.communities_auto()
    lines += ["", f"comunidades (propagação de rótulos sobre pares com peso ≥ {weight:g}; {len(groups)} com 3 cartas ou mais):"]
    lines += _community_lines(setmap, groups)
    return "\n".join(lines)


def markdown(setmap, set_name="", sources="", top_follow=6, top_pairs=40, top_archetype=10):
    """Mapa completo em Markdown (uso interno, `data/maps/<coleção>-mapa.md`; o documento da
    coleção para leitura é o PDF)."""
    code = setmap.set_code.upper()
    today = datetime.now().strftime("%Y-%m-%d")
    coverage = ", ".join(f"{k} {v}" for k, v in setmap.coverage().items())
    by_rarity = {r: sum(1 for e in setmap.cards.values() if e["raridade"] == r) for r in RARITY_ORDER}
    hooks = ", ".join(setmap.tagger.hooks) or "nenhum"
    w = draft_pick.WEIGHTS
    lines = [
        f"# {set_name or code} ({code}) — mapa de picks",
        "",
        f"Gerado por `mtg draft map {setmap.set_code} --write` em {today}. Dados: {sources or 'sem dados de partidas'}.",
        f"Fonte do poder, por carta: {coverage}. Cartas draftáveis: {len(setmap.cards)} "
        + "(" + ", ".join(f"{by_rarity[r]} {RARITY_PT[r]}" for r in RARITY_ORDER) + ").",
        "",
        "**Como ler.** A nota é em pontos percentuais de win rate acima da média da fonte da carta",
        "(17Lands: GIH WR − média dos usuários; Untapped: idem com a média dele; `draftsim*` e",
        "`teorica*` são notas sem amostra de partidas). Raridade não entra na conta: ela só aparece",
        "porque raras e míticas costumam ter mais poder, e porque cada pacote tem uma rara ou mítica,",
        "cerca de três incomuns e dez comuns. No P1P1 compare a rara do pacote com a melhor incomum e a",
        "melhor comum (seção 1); do P1P2 em diante, a rara quase sempre já saiu e a escolha é entre",
        "incomuns e comuns (seção 2). Arquétipos: pares que a carta serve (`+` = payoff). Elos: o que a",
        f"carta *pede* e *oferece* (os dez pares e os ganchos {hooks}); Σ é a soma das sinergias diretas com",
        "toda a coleção (quantas parceiras ela tem e quão fortes são os elos).",
        "",
        f"**Como o motor combina.** `mtg draft pick` soma: poder + encaixe nas cores (peso cresce do P1P1 até",
        f"o pick {w['compromisso_pleno_em'] + 1}) + par + necessidade + sinal + flexibilidade + sinergia do par + **parceiros**",
        f"({w['parceiro']:g} ponto por unidade de elo com cada carta já escolhida, teto {w['parceiros_max']:g}). Por isso um elo",
        "direto desempata cartas próximas e não vira uma carta fraca em bomba. Teoria:",
        "`knowledge/limitado-e-draft.md`, seções 3 (prioridades), 4 (arquétipos e deck perfeito) e 6",
        "(compromisso).",
        "",
        "## 0. Leitura da coleção e dos arquétipos",
        "",
    ]
    lines += [f"- {line}" for line in analysis_lines(setmap)]
    lines += [
        "",
        "## 1. Ordem de pick da coleção inteira",
        "",
        "Nota (fonte), cor, custo, arquétipos, elos e Σ sinergia. Ordem dentro da raridade.",
    ]
    for rarity in RARITY_ORDER:
        rows = setmap.pick_order(rarity)
        if not rows:
            continue
        lines += ["", f"### {RARITY_PT[rarity].capitalize()} ({len(rows)})", "",
                  "| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for row in rows:
            lines.append(f"| {row['posicao']} | {row['poder']:+.1f}{_mark(row)} | {row['fonte'].rstrip('*')} | {row['cor']} | "
                         f"{row['custo'].replace('{', '').replace('}', '')} | {row['name']} | {row['arquetipos'] or ''} | "
                         f"{_links(row)} | {row['elos']:g} |".replace(" | 0 |", " |  |"))
    lines += ["", "## 2. Depois da primeira escolha: os melhores segundos picks", "",
              "Para cada rara ou mítica, em ordem de poder, as cartas da coleção que o motor mais quer no",
              f"P1P2 (nota = poder + parceiros + o pouco de encaixe que o pick 2 já pesa). Para o terceiro",
              f"pick em diante: `mtg draft map {setmap.set_code} --card \"Primeira\" --card \"Segunda\"`, ou o motor ao",
              "vivo (`mtg draft watch`, Oráculo)."]
    for entry in setmap.tree(top=top_follow):
        first = entry["primeiro"]
        links = _links(first)
        lines += ["", f"**{first['name']}** ({first['raridade'][:1].upper()}, {first['cor']}, {first['custo']}, "
                  f"{first['poder']:+.1f}{_mark(first)} {first['fonte'].rstrip('*')})"
                  + (f" · {first['arquetipos']}" if first["arquetipos"] else "") + (f" · {links}" if links else "")]
        for row in entry["seguintes"]:
            elos = " ↔ " + ", ".join(f"{o} {s:g}" for o, s in row["elos"][:2]) if row.get("elos") else ""
            lines.append(f"- {row['total']:+.1f} {row['name']} ({(row['raridade'] or '?')[:1].upper()}, {row['cor']}) "
                         f"poder {row['poder']:+.1f}{'*' if row['teorica'] else ''} · parceiros {row['parceiros']:+.1f} · "
                         f"encaixe {row['encaixe']:+.1f}{elos}")
    pairs = setmap.pairs()
    lines += ["", "## 3. Pares de cartas com mais sinergia direta", "",
              f"{len(pairs)} pares com elo na coleção; os {min(top_pairs, len(pairs))} primeiros (sinergia em unidades de elo;",
              "empate pela soma de poder das duas). Elo entre duas cartas que juntas pedem três cores vale um quarto.", "",
              "| sin | poder | carta A | carta B | elos |", "| --- | --- | --- | --- | --- |"]
    for pair in pairs[:top_pairs]:
        lines.append(f"| {pair['sinergia']:g} | {pair['poder']:+.1f} | {pair['a']} | {pair['b']} | {', '.join(pair['elos'])} |")
    lines += ["", "## 4. Arquétipos: payoffs e enablers em ordem de poder", ""]
    for table in setmap.archetype_tables(top_archetype):
        wr = f" · par {table['win_rate']:.1%}" if table["win_rate"] else ""
        lines += [f"### {table['pair']} {table['name']}{wr}", "", f"{table['plan']}", "",
                  f"Payoffs ({table['total_payoffs']}): " + ", ".join(f"{e['name']} {e['poder']:+.1f}{_mark(e)}" for e in table["payoffs"]),
                  "", f"Enablers ({table['total_enablers']}): " + ", ".join(f"{e['name']} {e['poder']:+.1f}{_mark(e)}" for e in table["enablers"]), ""]
    central = setmap.centrality()
    totals = setmap.partner_totals()
    lines += ["## 5. Grafo de elos: centralidade e comunidades", "",
              f"As cartas são os nós e os elos diretos, as arestas ({len(pairs)}). **Centralidade** (0 a 100): um passeio",
              "aleatório que segue um elo com chance proporcional ao peso do elo vezes a força da parceira, ou",
              f"recomeça em carta aleatória ({DAMPING:.0%} de seguir); a carta central liga muitas parceiras fortes que",
              "ligam outras. É o que a soma Σ não vê: Σ conta elos, a centralidade pesa a qualidade de quem está",
              "do outro lado. Não torna cada elo mais certo (isso só dados de co-ocorrência em partidas fariam);",
              "diz quais cartas são as melhores *portas de entrada* para uma coleção no começo do draft.", "",
              "| # | centr. | Σ | nota | rar | cor | carta | elos |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for position, (name, value) in enumerate(sorted(central.items(), key=lambda kv: -kv[1])[:25], 1):
        entry = setmap.cards[name]
        lines.append(f"| {position} | {value:g} | {totals.get(name, 0.0):g} | {entry['poder']:+.1f}{_mark(entry)} | "
                     f"{entry['raridade'][:1].upper()} | {entry['cor']} | {name} | {_links(entry)} |")
    groups, weight = setmap.communities_auto()
    lines += ["", f"**Comunidades** (propagação de rótulos sobre os pares ligados por mais de um elo, peso {weight:g} ou",
              f"mais, limiar escolhido entre {', '.join(f'{w:g}' for w in COMMUNITY_WEIGHTS)} pelo que dá mais grupos;",
              f"{len(groups)} grupos com 3 cartas ou mais, do maior para o menor). Grupo que junta cartas de pares",
              "diferentes é um tema transversal (por exemplo, planeswalkers e quem os pede), que vale como",
              "arquétipo extra ao ler os sinais da mesa. Sobre todos os elos a coleção vira um grupo só.", ""]
    lines += _community_lines(setmap, groups, members=10)
    lines += ["", "## Limites", "",
              "- A nota de poder depende da fonte: só o 17Lands mede partidas com a amostra declarada; o",
              "  Untapped é de outra data e de outros ranks; `*` é leitura teórica.",
              "- Os elos vêm de padrões sobre o texto de regras (`src/mtg_builder/archetypes/<coleção>.json`):",
              "  marcam pertencimento, não qualidade. `mtg draft synergy` mede se a marcação carrega sinal.",
              "- O mapa não vê a mesa: sinais do draft (cores abertas, o que passou) só existem ao vivo.",
              f"- Regerar: `mtg draft update {setmap.set_code}` e `mtg draft map {setmap.set_code} --write`."]
    return "\n".join(lines) + "\n"


def write_markdown(setmap, set_name="", sources="", path=None, **kw):
    """Grava o Markdown do mapa em `data/maps/<coleção>-mapa.md` (uso interno: o documento
    da coleção para leitura é o PDF em `drafts/<coleção>/`)."""
    path = Path(path or MAPS_DIR / f"{setmap.set_code}-mapa.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown(setmap, set_name, sources, **kw), encoding="utf-8")
    return path
