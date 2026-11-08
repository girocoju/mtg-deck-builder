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

`markdown()` escreve tudo em `drafts/<coleção>-mapa.md`. Tudo é intrínseco à coleção e
aos dados de partidas: só muda quando eles mudam, não com o draft em curso.
"""

from collections import Counter
from datetime import datetime
from pathlib import Path

from . import analysis, archetypes, decklist, draft_pick
from .draft_sim import EXTRA_LAYOUTS

DRAFTS_DIR = Path(__file__).resolve().parents[2] / "drafts"
RARITY_ORDER = ("mythic", "rare", "uncommon", "common")
RARITY_PT = {"mythic": "míticas", "rare": "raras", "uncommon": "incomuns", "common": "comuns"}
DAMPING = 0.85            # centralidade: chance de o passeio seguir um elo em vez de recomeçar em carta aleatória
POWER_SHIFT = 5.0         # poder deslocado para ficar positivo ao pesar parceiras (−5 pontos ≈ carta injogável)
COMMUNITY_MIN_WEIGHT = 1.5   # comunidades só sobre pares ligados por mais de um elo; com 1,0 FRA vira um grupo só


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
    groups = setmap.communities()
    lines += ["", f"comunidades (propagação de rótulos sobre pares com peso ≥ {COMMUNITY_MIN_WEIGHT:g}; {len(groups)} com 3 cartas ou mais):"]
    lines += _community_lines(setmap, groups)
    return "\n".join(lines)


def markdown(setmap, set_name="", sources="", top_follow=6, top_pairs=40, top_archetype=10):
    """Documento completo do mapa, para `drafts/<coleção>-mapa.md`."""
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
    groups = setmap.communities()
    lines += ["", f"**Comunidades** (propagação de rótulos sobre os pares ligados por mais de um elo, peso {COMMUNITY_MIN_WEIGHT:g} ou",
              f"mais; {len(groups)} grupos com 3 cartas ou mais, do maior para o menor). Grupo que junta cartas de pares",
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
    path = Path(path or DRAFTS_DIR / f"{setmap.set_code}-mapa.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown(setmap, set_name, sources, **kw), encoding="utf-8")
    return path
