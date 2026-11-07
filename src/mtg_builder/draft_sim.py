"""Simulador de draft (spec 010): pacotes pela colação declarada da coleção e sete bots
que escolhem com o motor de picks, com ruído e preferência de cor.

Serve para treinar fora do jogo e para medir o que uma mesa deixa aberto. Bots não são
humanos nem os bots do Quick Draft do Arena, e a colação é uma aproximação declarada no
arquivo `boosters/<coleção>.json` (fonte e data dentro dele).
"""

import json
import random
from pathlib import Path

from . import analysis, decklist, draft, draft_pick

BOOSTERS_DIR = Path(__file__).parent / "boosters"
SEATS = 8
EXTRA_LAYOUTS = ("token", "double_faced_token", "emblem", "art_series")


def load_booster(set_code, profile=None):
    """Colação da coleção (`<coleção>.json`, ou `<coleção>-<perfil>.json` com `profile`),
    ou a genérica do Play Booster do Arena (marcada `generic`)."""
    name = f"{set_code.lower()}-{profile}.json" if profile else f"{set_code.lower()}.json"
    path = BOOSTERS_DIR / name
    if profile and not path.exists():
        raise RuntimeError(f"Perfil de colação não encontrado: {name}. Existem: "
                           + ", ".join(sorted(p.stem for p in BOOSTERS_DIR.glob("*.json"))))
    generic = not path.exists()
    data = json.loads((BOOSTERS_DIR / "default.json" if generic else path).read_text("utf-8"))
    data["generic"] = generic
    return data


def card_pools(conn, set_code, snapshot=None, arena=None):
    """Cartas draftáveis por raridade. Ordem de preferência: lista de cartas do 17Lands;
    `DraftContent` da base do Arena; impressões de booster da base; toda a coleção."""
    rows = conn.execute(
        "SELECT c.*, MIN(p.rarity) AS set_rarity, MAX(p.booster) AS booster FROM cards c "
        "JOIN printings p ON p.oracle_id = c.oracle_id WHERE p.set_code = ? "
        f"AND c.layout NOT IN ({','.join('?' * len(EXTRA_LAYOUTS))}) GROUP BY c.oracle_id",
        (set_code.lower(), *EXTRA_LAYOUTS),
    ).fetchall()
    rarity_of, basis = {}, None
    if snapshot and snapshot.get("cards"):
        rarity_of = {decklist._key(c["name"]): c["rarity"] for c in snapshot["cards"]}
        basis = "lista de cartas do 17Lands"
    elif arena is not None and arena.draftable(set_code):
        rarity_of = {decklist._key(c["name_en"]): c["rarity"] for c in arena.draftable(set_code)}
        basis = "DraftContent da base do Arena"
    pools = {"common": [], "uncommon": [], "rare": [], "mythic": [], "land": [], "basic": []}
    in_booster = [r for r in rows if r["booster"]]
    for row in rows:
        key = decklist._key(row["name"])
        if rarity_of:
            rarity = rarity_of.get(key) or rarity_of.get(decklist._key(row["name"].split(" // ")[0]))
            if rarity is None:
                continue
        else:
            if in_booster and not row["booster"]:
                continue
            rarity = row["set_rarity"]
        if analysis.is_land(row) and ("Basic" in (row["type_line"] or "") or rarity == "common"):
            # a posição de terreno traz básicos e os terrenos comuns; terrenos raros saem na raridade deles
            pools["basic" if "Basic" in (row["type_line"] or "") else "land"].append(row["name"])
        elif rarity in pools:
            pools[rarity].append(row["name"])
    if basis is None:
        basis = "impressões de booster na base" if in_booster else "todas as cartas da coleção na base"
    for key in pools:
        pools[key].sort()
    return pools, basis


def _choose_rarity(rng, odds):
    roll, total = rng.random() * sum(odds.values()), 0.0
    for rarity, weight in odds.items():
        total += weight
        if roll <= total:
            return rarity
    return next(iter(odds))


def make_pack(rng, pools, booster):
    """Um pacote pela colação: cada posição sorteia a raridade e uma carta dessa raridade
    que ainda não esteja no pacote."""
    pack = []
    for slot in booster["slots"]:
        for _ in range(slot["count"]):
            rarity = _choose_rarity(rng, slot["odds"])
            if rarity == "land":
                rarity = "land" if pools["land"] and rng.random() < booster.get("nonbasic_land_share", 0.55) else "basic"
            candidates = [c for c in pools.get(rarity, []) if c not in pack]
            if not candidates:                              # raridade sem cartas: cai para a mais comum
                for fallback in ("common", "uncommon", "rare", "mythic", "basic"):
                    candidates = [c for c in pools.get(fallback, []) if c not in pack]
                    if candidates:
                        break
            if candidates:
                pack.append(rng.choice(candidates))
    return pack


class Bot:
    def __init__(self, engine, rng, seat, noise=1.5, preference_bonus=1.0):
        self.engine, self.rng, self.seat = engine, rng, seat
        self.state = draft_pick.DraftState(engine.set_code, engine.mode, f"bot-{seat}")
        self.preference = "".join(sorted(rng.sample(draft_pick.COLOR_ORDER, 2),
                                         key=draft_pick.COLOR_ORDER.index))
        self.noise, self.preference_bonus = noise, preference_bonus

    def pick(self, pack, pick, names):
        result = self.engine.rank(self.state, pack, pick, names)
        weight = result["compromisso"]
        best, best_score = None, None
        for row in result["cartas"]:
            score = row["total"] + self.rng.gauss(0, self.noise)
            if row["cor"] != "-" and set(row["cor"]) <= set(self.preference):
                score += self.preference_bonus * (1 - weight)
            if best is None or score > best_score:
                best, best_score = row["name"], score
        self.state.record_pack(pack, pick, names)
        self.state.record_pick(pack, pick, best)
        return best


def run_table(conn, engine, set_code, rng, pools=None, booster=None, human_seat=None, choose=None, snapshot=None,
              arena=None):
    """Uma mesa de oito. `choose(result, names)` decide o pick do humano (se houver) e
    devolve o nome; sem humano, só bots. Devolve os estados dos oito lugares."""
    if pools is None:
        pools, _basis = card_pools(conn, set_code, snapshot, arena)
    booster = booster or load_booster(set_code)
    bots = {seat: Bot(engine, rng, seat) for seat in range(SEATS) if seat != human_seat}
    human = draft_pick.DraftState(set_code, engine.mode, "simulado") if human_seat is not None else None
    for pack_no in range(1, draft_pick.PACKS + 1):
        packs = [make_pack(rng, pools, booster) for _ in range(SEATS)]
        direction = 1 if pack_no % 2 else -1
        for pick_no in range(1, draft_pick.PACK_SIZE + 1):
            for seat in range(SEATS):
                names = packs[seat]
                if not names:
                    continue
                if seat == human_seat:
                    result = engine.rank(human, pack_no, pick_no, names)
                    chosen = choose(result, names)
                    human.record_pack(pack_no, pick_no, names, result["cartas"])
                    human.record_pick(pack_no, pick_no, chosen)
                else:
                    chosen = bots[seat].pick(pack_no, pick_no, names)
                names.remove(chosen)
            packs = [packs[(seat - direction) % SEATS] for seat in range(SEATS)]
    states = [human if seat == human_seat else bots[seat].state for seat in range(SEATS)]
    return states


def summarize(engine, states):
    """Cores de cada lugar (par mais forte) e contagem de raridades por pool."""
    seats = []
    for seat, state in enumerate(states):
        strength = engine.color_strength(state.picked_names())
        _top, pair = engine.top_pair(strength)
        rarities = {}
        for name in state.picked_names():
            rarity = engine.power(name).get("rarity") or engine.rarity(name) or "?"
            rarities[rarity] = rarities.get(rarity, 0) + 1
        seats.append({"seat": seat, "event": state.event, "pair": pair, "picks": len(state.picked_names()),
                      "rarities": rarities})
    return seats
