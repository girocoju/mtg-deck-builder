"""Motor de pontuação de picks de draft (spec 010) e estado de um draft.

A nota de cada carta é a soma de componentes em pontos percentuais de win rate, para ser
comparável ao GIH WR do 17Lands. Cada componente sai na tabela com a fonte; o julgamento
final e a explicação continuam com o agente (`.claude/skills/draft/SKILL.md`).

| Componente     | O que mede                                                            | Teoria |
| -------------- | --------------------------------------------------------------------- | ------ |
| poder          | GIH WR − média dos usuários (17Lands); Untapped; Draftsim; teórica     | limitado-e-draft §2 |
| encaixe        | a carta cabe nas cores já escolhidas, com peso que cresce com o pick  | §3 e §6 |
| par            | força do par de cores mais provável, se a carta cabe nele             | §4 |
| necessidade    | função vazia no "deck perfeito" (criaturas na curva, remoção, truques)| §4 |
| sinal          | carta que costuma sair cedo chegando tarde; cores que já passaram     | §5 |
| flexibilidade  | carta mono mantém o draft aberto no primeiro pacote                   | §3 |
| sinergia       | payoff ou enabler do arquétipo do par escolhido (`archetypes/<col>.json`) | §4 |
| parceiros      | elos diretos com as cartas já escolhidas: payoff pede, enabler oferece, mais os ganchos do arquivo (spec 014) | §4 |
"""

import json
import math
import re
from datetime import datetime
from pathlib import Path

from . import analysis, archetypes, collection, db, decklist, draft

PACK_SIZE = 14
PACKS = 3
COLOR_ORDER = "WUBRG"

WEIGHTS = {
    "cabe": 2.0,              # encaixe pleno (fit 1) com compromisso pleno
    "nao_cabe": -4.0,         # fora das cores (fit 0) com compromisso pleno
    "par": 0.5,               # × (win rate do par − média) em pontos
    "necessidade": 1.5,       # × fração da função ainda vazia
    "sinal_por_pick": 0.4,    # × (pick atual − ALSA)
    "sinal_max": 2.5,
    "cores_abertas": 1.0,     # × abertura normalizada da cor
    "flex_mono": 0.3,
    "flex_ouro": -0.5,
    "sinergia": 1.5,          # × 1,0 payoff ou 0,5 enabler do arquétipo do par, com compromisso pleno
    "parceiro": 0.6,          # × soma dos elos diretos (Tagger.synergy) com as cartas já escolhidas
    "parceiros_max": 3.0,     # teto do componente: muitos parceiros não transformam carta fraca em bomba
    "compromisso_pleno_em": 20,   # índice (de 0) do pick em que o deck manda: P2P7
    "peso_minimo_cor": 0.5,   # quanto uma carta fraca ainda puxa para a sua cor
    "sobra_a_partir": 9,      # do pick 9 de cada pacote em diante, rara ou mítica que falta na coleção ganha bônus
    "sobra_rara": 1.5,        # (pedido do usuário em 2026-11-09: 42 picks sem uma rara; no Arena, rara é coringa)
    "sobra_mitica": 2.5,
    "colecao_playset": 4,     # com quatro cópias conhecidas, o bônus some
}
TARGETS = {"criaturas": 15, "cmc2": 4, "cmc3": 4, "cmc4": 3, "remocao": 3, "truques": 2}
THEORY_BY_RARITY = {"mythic": 4.0, "rare": 2.5, "uncommon": 0.5, "common": -0.5}


def commitment(pick_index):
    """0 no P1P1, cresce linearmente até 1 no pick `compromisso_pleno_em` e fica em 1."""
    return max(0.0, min(1.0, pick_index / WEIGHTS["compromisso_pleno_em"]))


def pick_index(pack, pick):
    return (pack - 1) * PACK_SIZE + (pick - 1)


def wheel_probability(alsa, pick):
    """Chance estimada de a carta ainda estar no pacote quando ele voltar (8 picks depois),
    pela ALSA: logística centrada no pick de retorno. É uma estimativa, não uma medição."""
    if alsa is None:
        return None
    back = pick + 8
    if back > PACK_SIZE:
        return 0.0
    return 1 / (1 + math.exp(-(alsa - back) / 1.5))


# --- cartas ------------------------------------------------------------------------------

def blank_card(name):
    return {"name": name, "layout": "normal", "mana_cost": None, "cmc": None, "type_line": "",
            "oracle_text": "", "colors": "", "color_identity": "", "keywords": "[]", "faces": None,
            "power": None, "toughness": None}


def card_colors(card):
    return (card["colors"] or "") if card is not None else ""


def functions(card):
    """Funções de limitado que a carta preenche (modelo do deck perfeito)."""
    found = set()
    if card is None or analysis.is_land(card):
        return found
    types = analysis._front(card, "type_line")
    text = (card["oracle_text"] or "").lower()
    roles = analysis.roles(card)
    if "Creature" in types:
        found.add("criaturas")
        cmc = int(card["cmc"] or 0)
        if cmc <= 2:
            found.add("cmc2")
        elif cmc == 3:
            found.add("cmc3")
        elif cmc == 4:
            found.add("cmc4")
    if "remoção pontual" in roles or "remoção em massa" in roles:
        found.add("remocao")
    if "Instant" in types and re.search(r"gets? \+\d+/\+\d+", text):
        found.add("truques")
    return found


def theoretical_power(card, rarity):
    """Nota sem dados: raridade, remoção, custo. Sempre marcada como teórica."""
    points = THEORY_BY_RARITY.get(rarity or "", 0.0)
    if card is None:
        return points
    if analysis.is_land(card):
        return -5.0 if "Basic" in (card["type_line"] or "") else -1.5
    found = functions(card)
    if "remocao" in found:
        points += 2.0
    if "criaturas" in found and (card["cmc"] or 0) <= 4:
        points += 0.5
    if (card["cmc"] or 0) >= 6:
        points -= 1.0
    return points


class Ratings:
    """Poder de cada carta pelas fontes disponíveis, na ordem 17Lands → Untapped → Draftsim
    → teórica. Cada resposta diz a fonte."""

    def __init__(self, snapshot=None, untapped=None, draftsim=None, min_games=draft.MIN_GAMES):
        self.snapshot = snapshot if snapshot and snapshot.get("cards") else None
        self.untapped, self.draftsim, self.min_games = untapped, draftsim, min_games
        self.baseline = (self.snapshot or {}).get("baseline")
        self.index = {}
        for row in (self.snapshot or {}).get("cards", []):
            self.index[decklist._key(row["name"])] = row
            self.index.setdefault(decklist._key(row["name"].split(" // ")[0]), row)
        self.pairs = {c["short"]: c["win_rate"] for c in (self.snapshot or {}).get("colors", [])
                      if not c.get("summary") and c.get("win_rate") is not None and len(str(c["short"])) == 2}

    def describe(self):
        parts = []
        if self.snapshot:
            parts.append(f"17Lands {self.snapshot['collected_at'][:10]} ({self.snapshot['event']}, "
                         f"{self.snapshot.get('games') or '?'} jogos, média {self.baseline:.1%})"
                         if self.baseline else f"17Lands {self.snapshot['collected_at'][:10]} (sem média)")
        if self.untapped:
            parts.append(f"Untapped {self.untapped['collected_at']} (média {self.untapped['baseline']:.1%})")
        if self.draftsim:
            parts.append("Draftsim (notas teóricas)")
        return " · ".join(parts) or "sem dados: avaliação teórica"

    def row(self, name):
        return self.index.get(decklist._key(name)) or self.index.get(decklist._key(name.split(" // ")[0]))

    def power(self, name, card=None, rarity=None):
        row = self.row(name)
        alsa = row.get("alsa") if row else None
        rarity = rarity or (row.get("rarity") if row else None)
        if row and row.get("gih") is not None and (row.get("gih_games") or 0) >= self.min_games and self.baseline:
            return {"points": (row["gih"] - self.baseline) * 100, "source": "17lands", "gih": row["gih"],
                    "games": row["gih_games"], "alsa": alsa, "rarity": rarity, "theoretical": False}
        key = decklist._key(name)
        if self.untapped and self.untapped.get("baseline"):
            entry = self.untapped["cards"].get(key) or self.untapped["cards"].get(decklist._key(name.split(" // ")[0]))
            if entry and entry["games"] >= self.min_games:
                return {"points": (entry["wr"] - self.untapped["baseline"]) * 100, "source": "untapped",
                        "gih": entry["wr"], "games": entry["games"], "alsa": alsa, "rarity": rarity,
                        "theoretical": False}
        if self.draftsim:
            rating = self.draftsim["cards"].get(key) or self.draftsim["cards"].get(decklist._key(name.split(" // ")[0]))
            if rating is not None:
                return {"points": (rating - 2.5) * 2.0, "source": "draftsim*", "gih": None, "games": 0,
                        "alsa": alsa, "rarity": rarity, "theoretical": True, "rating": rating}
        return {"points": theoretical_power(card, rarity), "source": "teorica*", "gih": None, "games": 0,
                "alsa": alsa, "rarity": rarity, "theoretical": True}


# --- estado do draft ---------------------------------------------------------------------

class DraftState:
    """Pacotes vistos, picks feitos e o que foi passado, para retomar e auditar."""

    def __init__(self, set_code=None, mode="premier", event=None, snapshot=None, path=None):
        self.set_code, self.mode, self.event, self.snapshot = set_code, mode, event, snapshot
        self.started_at = datetime.now().isoformat(timespec="seconds")
        self.packs = []          # [{"pack", "pick", "seen": [nomes], "picked": nome|None, "ranking": [...]}]
        self.path = Path(path) if path else None

    # serialização
    def to_dict(self):
        return {"set": self.set_code, "mode": self.mode, "event": self.event, "snapshot": self.snapshot,
                "started_at": self.started_at, "packs": self.packs, "pool": self.picked_names()}

    def save(self, path=None):
        path = Path(path or self.path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=1), encoding="utf-8")
        self.path = path
        return path

    @classmethod
    def load(cls, path):
        data = json.loads(Path(path).read_text("utf-8"))
        state = cls(data.get("set"), data.get("mode", "premier"), data.get("event"), data.get("snapshot"), path)
        state.started_at = data.get("started_at") or state.started_at
        state.packs = data.get("packs", [])
        return state

    @staticmethod
    def default_path(set_code, mode, event=None):
        stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
        tag = (event or f"{set_code}-{mode}").replace("/", "-")
        return db.DATA_DIR / "drafts" / f"{stamp}-{tag}.json"

    # registro
    def view(self, pack, pick):
        for entry in self.packs:
            if entry["pack"] == pack and entry["pick"] == pick:
                return entry
        return None

    def record_pack(self, pack, pick, seen, ranking=None):
        entry = self.view(pack, pick)
        if entry is None:
            entry = {"pack": pack, "pick": pick, "seen": list(seen), "picked": None, "ranking": ranking or []}
            self.packs.append(entry)
            self.packs.sort(key=lambda e: (e["pack"], e["pick"]))
        else:
            entry["seen"] = list(seen)
            if ranking is not None:
                entry["ranking"] = ranking
        return entry

    def record_pick(self, pack, pick, name):
        entry = self.view(pack, pick) or self.record_pack(pack, pick, [])
        entry["picked"] = name
        return entry

    def add_picks(self, names, pack=1):
        """Picks informados sem pacote (uso do `mtg draft pick --picked`)."""
        for name in names:
            number = len(self.packs) + 1
            self.record_pick((number - 1) // PACK_SIZE + 1, (number - 1) % PACK_SIZE + 1, name)

    def picked_names(self):
        return [e["picked"] for e in self.packs if e.get("picked")]

    def next_position(self):
        """(pacote, pick) seguinte ao último registrado."""
        if not self.packs:
            return 1, 1
        last = self.packs[-1]
        index = pick_index(last["pack"], last["pick"]) + 1
        return index // PACK_SIZE + 1, index % PACK_SIZE + 1


# --- motor -------------------------------------------------------------------------------

class Engine:
    def __init__(self, conn, ratings, set_code=None, mode="premier", index=None, archetype_data=None):
        self.conn, self.ratings, self.set_code, self.mode = conn, ratings, set_code, mode
        self.index = index if index is not None else (decklist._name_index(conn) if conn is not None else {})
        self.extra = {}      # nome → {"card", "rarity"} informado por quem chama (base do Arena)
        data = archetype_data if archetype_data is not None else (archetypes.load(set_code) if set_code else None)
        self.tagger = archetypes.Tagger(data)
        self._functions = {}

    def functions(self, name, card):
        """`functions(card)` com cache por nome (o mapa da coleção pontua centenas de vezes)."""
        if name not in self._functions:
            self._functions[name] = functions(card)
        return self._functions[name]

    def card(self, name):
        if name in self.extra and self.extra[name].get("card") is not None:
            return self.extra[name]["card"]
        return self.index.get(decklist._key(name)) or self.index.get(decklist._key(name.split(" // ")[0]))

    def rarity(self, name):
        """Raridade pela base do Arena quando veio do log; senão pela impressão na coleção do
        motor (ou em qualquer coleção), como o mapa da coleção faz. Sem ela, a nota teórica
        não tinha a base por raridade e o bônus de sobra não via raras."""
        if name in self.extra and self.extra[name].get("rarity"):
            return self.extra[name]["rarity"]
        cache = self.__dict__.setdefault("_rarities", {})
        if name not in cache:
            card = self.card(name)
            found = None
            if self.conn is not None and card is not None and "oracle_id" in card.keys():
                if self.set_code:
                    row = self.conn.execute("SELECT MIN(rarity) AS r FROM printings WHERE oracle_id = ? AND set_code = ?",
                                            (card["oracle_id"], self.set_code)).fetchone()
                    found = row["r"] if row else None
                if not found:
                    row = self.conn.execute("SELECT MIN(rarity) AS r FROM printings WHERE oracle_id = ?",
                                            (card["oracle_id"],)).fetchone()
                    found = row["r"] if row else None
            cache[name] = found
        return cache[name]

    def collection_bonus(self, name, rarity, pick):
        """Bônus de sobra: do pick `sobra_a_partir` de cada pacote em diante, rara ou mítica de
        que a coleção conhecida (`data/collection.json`, aproximação por baixo) tem menos que
        um playset. Só pesa quando o pacote já não tem jogável que valha mais: no Arena, uma
        rara que ninguém jogaria ainda é progresso de coleção e de coringa."""
        if pick < WEIGHTS["sobra_a_partir"] or rarity not in ("rare", "mythic"):
            return 0.0
        if getattr(self, "_collection", None) is None:
            try:
                self._collection = collection.by_name(collection.load(db.DATA_DIR / "collection.json"))
            except (OSError, ValueError):
                self._collection = {}
        if self._collection.get(decklist._key(name.split(" // ")[0]), 0) >= WEIGHTS["colecao_playset"]:
            return 0.0
        return WEIGHTS["sobra_mitica"] if rarity == "mythic" else WEIGHTS["sobra_rara"]

    def power(self, name):
        return self.ratings.power(name, self.card(name), self.rarity(name))

    def color_strength(self, names):
        """Quanto cada cor pesa nos picks feitos: poder da carta (mínimo configurado),
        dividido entre as cores dela."""
        strength = {c: 0.0 for c in COLOR_ORDER}
        for name in names:
            colors = card_colors(self.card(name))
            if not colors:
                continue
            weight = max(WEIGHTS["peso_minimo_cor"], self.power(name)["points"] + 3.0)
            for color in colors:
                if color in strength:
                    strength[color] += weight / len(colors)
        return strength

    @staticmethod
    def top_pair(strength):
        ordered = sorted(COLOR_ORDER, key=lambda c: -strength[c])
        top = [c for c in ordered[:2] if strength[c] > 0]
        pair = "".join(c for c in COLOR_ORDER if c in top) if len(top) == 2 else None
        return top, pair

    def open_colors(self, state, pack):
        """Cores que chegaram abertas nos pacotes já vistos na mesma direção (1 e 3 vs. 2):
        média, por cor, do melhor poder visto do pick 3 em diante."""
        totals, views = {c: 0.0 for c in COLOR_ORDER}, 0
        for entry in state.packs:
            if entry["pick"] < 3 or entry["pack"] % 2 != pack % 2 or not entry["seen"]:
                continue
            views += 1
            best = {c: 0.0 for c in COLOR_ORDER}
            for name in entry["seen"]:
                colors = card_colors(self.card(name))
                if len(colors) == 1:
                    best[colors] = max(best[colors], self.power(name)["points"])
            for color in COLOR_ORDER:
                totals[color] += max(0.0, best[color])
        if not views:
            return {c: 0.0 for c in COLOR_ORDER}
        peak = max(totals.values()) or 1.0
        return {c: totals[c] / peak for c in COLOR_ORDER}

    def counts(self, names, pair):
        counts = {k: 0 for k in TARGETS}
        allowed = set(pair) if pair else None
        for name in names:
            card = self.card(name)
            colors = card_colors(card)
            if allowed is not None and colors and not set(colors) <= allowed:
                continue
            for function in self.functions(name, card):
                counts[function] += 1
        return counts

    def rank(self, state, pack, pick, cards):
        """`cards`: nomes, ou dicionários {"name", "rarity", "card"} vindos da base do Arena."""
        names = []
        for item in cards:
            if isinstance(item, dict):
                names.append(item["name"])
                self.extra[item["name"]] = {"card": item.get("card"), "rarity": item.get("rarity")}
            else:
                names.append(item)
        picked = state.picked_names()
        picked_cards = [(other, self.card(other)) for other in picked]
        weight = commitment(pick_index(pack, pick))
        strength = self.color_strength(picked)
        top, pair = self.top_pair(strength)
        peak = max(strength.values()) or 0.0
        share = {c: (strength[c] / peak if peak else 0.0) for c in COLOR_ORDER}
        pair_wr = self.ratings.pairs.get(pair) if pair else None
        pair_bonus = (pair_wr - self.ratings.baseline) * 100 if pair_wr and self.ratings.baseline else 0.0
        counts = self.counts(picked, pair)
        open_colors = self.open_colors(state, pack)

        rows = []
        for name in names:
            card = self.card(name)
            power = self.power(name)
            colors = card_colors(card)
            fit = sum(share[c] for c in colors if c in share) / len(colors) if colors else 1.0
            fits_pair = (not colors) or (pair is not None and set(colors) <= set(pair)) or \
                        (pair is None and top and set(colors) <= set(top))
            encaixe = weight * (fit * (WEIGHTS["cabe"] - WEIGHTS["nao_cabe"]) + WEIGHTS["nao_cabe"]) if colors else 0.0
            par = weight * WEIGHTS["par"] * pair_bonus if (colors and pair and set(colors) <= set(pair)) else 0.0
            found = self.functions(name, card)
            fill = (sum(max(0.0, 1 - counts[f] / TARGETS[f]) for f in found) / len(found)) if found else 0.0
            necessidade = weight * WEIGHTS["necessidade"] * fill if fits_pair else 0.0
            sinal = 0.0
            alsa = power.get("alsa")
            if alsa and pick >= 2 and alsa + 0.5 < pick:
                sinal = min(WEIGHTS["sinal_max"], (pick - alsa) * WEIGHTS["sinal_por_pick"])
            if colors:
                sinal += WEIGHTS["cores_abertas"] * (sum(open_colors[c] for c in colors) / len(colors)) * (1 - weight / 2)
            flex = 0.0
            if pack == 1 and colors:
                flex = (1 - weight) * (WEIGHTS["flex_mono"] if len(colors) == 1 else WEIGHTS["flex_ouro"])
            tags = self.tagger.tags(card)
            sinergia = weight * WEIGHTS["sinergia"] * tags.get(pair, 0.0) if pair else 0.0
            elos = sorted(((other, round(self.tagger.synergy(card, other_card), 2))
                           for other, other_card in picked_cards if other_card is not None), key=lambda t: -t[1])
            elos = [(other, score) for other, score in elos if score > 0]
            parceiros = min(WEIGHTS["parceiros_max"], WEIGHTS["parceiro"] * sum(score for _o, score in elos))
            rarity = power.get("rarity") or self.rarity(name) or "?"
            colecao = self.collection_bonus(name, rarity, pick)
            total = power["points"] + encaixe + par + necessidade + sinal + flex + sinergia + parceiros + colecao
            rows.append({
                "name": name, "total": round(total, 2), "poder": round(power["points"], 2),
                "encaixe": round(encaixe, 2), "par": round(par, 2), "necessidade": round(necessidade, 2),
                "sinal": round(sinal, 2), "flexibilidade": round(flex, 2), "sinergia": round(sinergia, 2),
                "parceiros": round(parceiros, 2), "elos": elos[:3], "colecao": round(colecao, 2),
                "arquetipos": self.tagger.label(tags), "fonte": power["source"],
                "teorica": power["theoretical"], "gih": power.get("gih"), "jogos": power.get("games", 0),
                "alsa": alsa, "volta": wheel_probability(alsa, pick), "cor": colors or "-",
                "raridade": rarity,
                "custo": (card["mana_cost"] if card else None) or "",
                "funcoes": sorted(found),
            })
        rows.sort(key=lambda r: -r["total"])
        for position, row in enumerate(rows, 1):
            row["posicao"] = position
        return {
            "pack": pack, "pick": pick, "compromisso": round(weight, 2),
            "cores": {c: round(strength[c], 1) for c in COLOR_ORDER if strength[c] > 0},
            "par": pair, "par_win_rate": self.ratings.pairs.get(pair) if pair else None,
            "arquetipo": self.tagger.name(pair) if pair else "",
            "contagens": counts, "abertas": {c: round(v, 2) for c, v in open_colors.items() if v > 0},
            "cartas": rows,
        }


# --- apresentação ------------------------------------------------------------------------

def _pct(value, width=6):
    return f"{value:{width}.1%}" if value is not None else " " * (width - 1) + "—"


TIE_MARGIN = 0.5          # diferença de nota abaixo da qual a recomendação avisa que é empate técnico


def headline(result):
    """Uma linha de decisão para a janela: `► PEGUE: carta (nota; por quê) · 2º: ... · 3º: ...`.
    Pedido do usuário no primeiro draft real (2026-11-09): a tabela só mostrava métricas."""
    rows = result.get("cartas") or []
    if not rows:
        return ""
    top = rows[0]
    why = [f"{top['fonte'].rstrip('*')} {top['gih']:.1%}" if top.get("gih") else "nota teórica"]
    if top.get("encaixe", 0) >= 0.5:
        why.append("na sua cor")
    if top.get("elos"):
        why.append(f"elo com {top['elos'][0][0]}")
    if top.get("sinergia", 0) >= 0.5:
        why.append("sinergia do par")
    if top.get("colecao", 0) > 0:
        why.append(f"{'mítica' if top.get('raridade') == 'mythic' else 'rara'} que falta na coleção, pacote de sobras")
    line = f"► PEGUE: {top['name']}  ({top['total']:+.1f}; {', '.join(why)})"
    for position, row in enumerate(rows[1:3], 2):
        line += f"   ·   {position}º: {row['name']} ({row['total']:+.1f})"
    if len(rows) > 1 and top["total"] - rows[1]["total"] < TIE_MARGIN:
        line += "   ·   empate técnico: decida pela curva e pelas cores"
    return line


def format_ranking(result, title="", sources=""):
    """Tabela de texto do ranking, usada no terminal e na janela flutuante; a primeira linha
    é a recomendação (`headline`)."""
    colors = " ".join(f"{c} {v:g}" for c, v in result["cores"].items()) or "nenhuma ainda"
    pair = f" · par {result['par']}" + (f" {result['par_win_rate']:.1%}" if result["par_win_rate"] else "") \
        + (f" ({result['arquetipo']})" if result.get("arquetipo") else "") if result["par"] else ""
    lines = [headline(result),
             f"{title}P{result['pack']} pick {result['pick']} · compromisso {result['compromisso']:.0%} · "
             f"cores: {colors}{pair}"]
    if sources:
        lines.append(f"dados: {sources}")
    lines.append(" #   nota  poder   enc   par  need sinal  flex  sin parc  col fonte       GIH  ALSA volta cor  rar carta · arquétipos ↔ parceiros")
    for row in result["cartas"]:
        volta = f"{row['volta']:4.0%}" if row["volta"] is not None else "   —"
        alsa = f"{row['alsa']:5.1f}" if row["alsa"] else "    —"
        tags = f" · {row['arquetipos']}" if row.get("arquetipos") else ""
        elos = " ↔ " + ", ".join(f"{other} {score:g}" for other, score in row["elos"][:2]) if row.get("elos") else ""
        lines.append(
            f"{row['posicao']:2d} {row['total']:+6.1f} {row['poder']:+6.1f} {row['encaixe']:+5.1f} "
            f"{row['par']:+5.1f} {row['necessidade']:+5.1f} {row['sinal']:+5.1f} {row['flexibilidade']:+5.1f} "
            f"{row.get('sinergia', 0):+4.1f} {row.get('parceiros', 0):+4.1f} {row.get('colecao', 0):+4.1f} {row['fonte']:<9} "
            f"{_pct(row['gih'])} {alsa} {volta} {row['cor']:<4} "
            f"{(row['raridade'] or '?')[:1].upper()}   {row['name']}{tags}{elos}")
    if any(r["teorica"] for r in result["cartas"]):
        lines.append("* nota teórica (sem amostra nos dados de partidas)")
    return "\n".join(lines)
