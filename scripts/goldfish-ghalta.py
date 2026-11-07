"""Goldfish do Gruul Ghalta Burn Together: em que turno a lista mata um oponente passivo.

Modelo (simplificado, sem cores, sem bloqueadores):
- Mão inicial com suavização BO1 (duas mãos; fica com a de contagem de terrenos mais
  próxima da média do deck). Sem mulligan.
- Terrenos sempre desvirados. Llanowar Elves produz mana a partir do turno seguinte.
- Criaturas: poder, custo e regras especiais de cada carta (texto de `mtg card`).
  Ghalta the Unstoppable custa max(1, 9 - maior poder); Ghalta, Primal Hunger custa
  max(2, 12 - poder total). Slumbering Trudge entra virada com 3 - X stun se X <= 2.
  Hazoret não ataca (nunca chega a speed 4 no horizonte). Bebop ataca se houver carta
  para descartar. Hammerskull leva stun ao atacar sem outro Dinossauro.
- Mágicas: Wild Ride (+3, haste, 1 mana; harmonize {4}{R} menos o poder de uma criatura
  virada que não ataca), Bulk Up (dobra, 2; flashback 6), The Last Agni Kai (2; luta
  contra uma criatura do oponente de resistência T, excesso vira mana vermelha; uma por
  turno, só no cenário "com alvo"), Burn Together (1; dano igual ao poder, sacrifica).
- A cada turno, enumera as ordens de conjuração de criaturas e as sequências de mágicas
  no melhor alvo; se há letal, mata. Senão, desenvolve maximizando (maior poder, poder
  total) e ataca com o que pode; usa Wild Ride fora do letal se render >= 8 de dano.
"""
import random
import sys
from collections import Counter
from itertools import permutations

LAND = "Terreno"

CREATURES = {
    "Llanowar Elves": dict(power=1, cost=1, dork=True, noattack=True),
    "Slumbering Trudge": dict(power=6, cost="X"),
    "Bebop & Rocksteady": dict(power=7, cost=3, bebop=True),
    "Pugnacious Hammerskull": dict(power=6, cost=3, dino=True, hammer=True),
    "Hazoret, Godseeker": dict(power=5, cost=2, noattack=True),
    "Ghalta the Unstoppable": dict(power=8, cost="U", dino=True),
    "Ghalta, Primal Hunger": dict(power=12, cost="P", dino=True),
    "Regal Imperiosaur": dict(power=5, cost=3, dino=True),
}
SPELLS = {"Wild Ride", "Bulk Up", "The Last Agni Kai", "Callous Sell-Sword", "Snakeskin Veil", "Felonious Rage"}


def smoothed_hand(lib, avg):
    h1 = lib[:7]
    lib2 = lib[:]
    random.shuffle(lib2)
    h2 = lib2[:7]
    d1 = abs(h1.count(LAND) - avg)
    d2 = abs(h2.count(LAND) - avg)
    if d2 < d1:
        return h2, lib2[7:]
    return h1, lib[7:]


def creature_cost(name, board, mana_left):
    c = CREATURES[name]
    if c["cost"] == "X":
        return 1  # X = 0 por padrão; X extra decidido depois
    if c["cost"] == "U":
        best = max([b["power"] for b in board], default=0)
        return max(1, 9 - best)
    if c["cost"] == "P":
        total = sum(b["power"] for b in board)
        return max(2, 12 - total)
    return c["cost"]


def make_creature(name, x=0):
    c = CREATURES[name]
    cr = dict(name=name, power=c["power"], sick=True, tapped=False, stun=0,
              noattack=c.get("noattack", False), dino=c.get("dino", False),
              bebop=c.get("bebop", False), hammer=c.get("hammer", False), dork=c.get("dork", False))
    if c["cost"] == "X":
        cr["stun"] = max(0, 3 - x)
        cr["tapped"] = x <= 2
    return cr


def can_attack(cr, hand_size):
    if cr["sick"] or cr["tapped"] or cr["noattack"]:
        return False
    if cr["bebop"] and hand_size < 1:
        return False
    return True


def kill_search(board, mana, hand, grave, target_t, hand_size_after):
    """Maior dano possível neste turno. Devolve (dano, usou_wild_ride_em, plano)."""
    wr_hand = hand.count("Wild Ride")
    fr_hand = hand.count("Felonious Rage")
    bu_hand = hand.count("Bulk Up")
    ak_hand = hand.count("The Last Agni Kai")
    bt_hand = hand.count("Callous Sell-Sword")
    wr_grave = grave["Wild Ride"]
    bu_grave = grave["Bulk Up"]
    best = (0, None)
    for ci, c in enumerate(board):
        others = [b for j, b in enumerate(board) if j != ci]
        other_attack = sum(b["power"] for b in others if can_attack(b, hand_size_after))
        # criatura para pagar o harmonize: a maior que não ataca e não está virada
        tappers = [b["power"] for b in others if not b["tapped"] and not can_attack(b, hand_size_after)]
        tapper = max(tappers, default=0)
        hc = max(1, 5 - tapper)
        base_attack_ok = can_attack(c, hand_size_after)
        hasteable = (not c["tapped"]) and (not c["noattack"])

        # busca em profundidade sobre a sequência de mágicas
        def dfs(p, m, haste, wr, fr, bu, ak, bt, wrg, bug, ak_used):
            attack = p if (base_attack_ok or (haste and hasteable)) else 0
            res = attack + other_attack
            if bt > 0 and m >= 1:
                res = max(res, attack + other_attack + p)
            if wr > 0 and m >= 1:
                res = max(res, dfs(p + 3, m - 1, True, wr - 1, fr, bu, ak, bt, wrg, bug, ak_used))
            if fr > 0 and m >= 1:
                res = max(res, dfs(p + 2, m - 1, True, wr, fr - 1, bu, ak, bt, wrg, bug, ak_used))
            if wrg > 0 and m >= hc:
                res = max(res, dfs(p + 3, m - hc, True, wr, fr, bu, ak, bt, wrg - 1, bug, ak_used))
            if bu > 0 and m >= 2:
                res = max(res, dfs(p * 2, m - 2, haste, wr, fr, bu - 1, ak, bt, wrg, bug, ak_used))
            if bug > 0 and m >= 6:
                res = max(res, dfs(p * 2, m - 6, haste, wr, fr, bu, ak, bt, wrg, bug - 1, ak_used))
            if ak > 0 and m >= 2 and target_t is not None and not ak_used:
                gain = max(0, p - target_t)
                res = max(res, dfs(p, m - 2 + gain, haste, wr, fr, bu, ak - 1, bt, wrg, bug, True))
            return res

        dmg = dfs(c["power"], mana, False, wr_hand, fr_hand, bu_hand, ak_hand, bt_hand, wr_grave, bu_grave, False)
        if dmg > best[0]:
            best = (dmg, ci)
    return best


def develop_options(hand, board, mana):
    """Enumera ordens de conjuração de criaturas da mão; devolve lista de (board, mana_restante, usadas)."""
    creatures = [c for c in hand if c in CREATURES]
    seen = set()
    results = [(list(board), mana, [])]
    n = len(creatures)
    idxs = list(range(n))
    for r in range(1, n + 1):
        for perm in permutations(idxs, r):
            key = tuple(creatures[i] for i in perm)
            if key in seen:
                continue
            seen.add(key)
            b = [dict(x) for x in board]
            m = mana
            ok = True
            used = []
            for i in perm:
                name = creatures[i]
                cost = creature_cost(name, b, m)
                if cost > m:
                    ok = False
                    break
                m -= cost
                b.append(make_creature(name, 0))
                used.append(name)
            if ok:
                results.append((b, m, used))
    return results


def play_game(deck, on_play, target_t, max_turn=8, wr_threshold=8):
    lib = deck[:]
    random.shuffle(lib)
    avg = deck.count(LAND) * 7 / len(deck)
    hand, lib = smoothed_hand(lib, avg)
    opening_lands = hand.count(LAND)
    board = []
    lands = 0
    opp = 20
    grave = Counter()
    t1_elves = False
    for t in range(1, max_turn + 1):
        for c in board:
            c["sick"] = False
            if c["tapped"]:
                if c["stun"] > 0:
                    c["stun"] -= 1
                else:
                    c["tapped"] = False
        if t > 1 or not on_play:
            if lib:
                hand.append(lib.pop(0))
        if LAND in hand:
            hand.remove(LAND)
            lands += 1
        dorks = sum(1 for c in board if c["dork"] and not c["sick"] and not c["tapped"])
        mana = lands + dorks
        # opções de desenvolvimento e busca de letal
        best_plan = None
        for b, m, used in develop_options(hand, board, mana):
            rest = list(hand)
            for u in used:
                rest.remove(u)
            dmg, ci = kill_search(b, m, rest, grave, target_t if t >= 2 else None, len(rest))
            if dmg >= opp:
                best_plan = ("kill", b, m, used, rest)
                break
        if best_plan:
            return t, opening_lands, t1_elves
        # sem letal: desenvolver maximizando maior poder, depois poder total
        cands = develop_options(hand, board, mana)

        def score(opt):
            b, m, used = opt
            rest = list(hand)
            for u in used:
                rest.remove(u)
            # Elves primeiro (mana no turno seguinte), depois maior poder, poder total, sobra
            return (used.count("Llanowar Elves"), max([x["power"] for x in b], default=0), sum(x["power"] for x in b), m)

        b, m, used = max(cands, key=score)
        for u in used:
            hand.remove(u)
        if t == 1 and "Llanowar Elves" in used:
            t1_elves = True
        # Trudge recém-conjurada: gastar sobra de mana em X (até 3) para tirar stun
        for c in b:
            if c["name"] == "Slumbering Trudge" and c["sick"] and c["tapped"] and c["stun"] == 3 and m > 0:
                x = min(m, 3)
                m -= x
                c["stun"] = 3 - x
                c["tapped"] = x <= 2
        board = b
        # ataque sem letal
        attackers = [c for c in board if can_attack(c, len(hand))]
        dmg = sum(c["power"] for c in attackers)
        # Wild Ride fora do letal: na maior criatura que possa ganhar haste, se render >= limiar
        wr_target = None
        if "Wild Ride" in hand and m >= 1:
            hasteable = [c for c in board if c["sick"] and not c["tapped"] and not c["noattack"]]
            if hasteable:
                c = max(hasteable, key=lambda x: x["power"])
                if c["power"] + 3 >= wr_threshold:
                    wr_target = c
        if wr_target is not None:
            hand.remove("Wild Ride")
            grave["Wild Ride"] += 1
            m -= 1
            dmg += wr_target["power"] + 3
        opp -= dmg
        for c in attackers:
            if c["bebop"]:
                # descarta a pior carta: um terreno se houver, senão a última
                if LAND in hand:
                    hand.remove(LAND)
                elif hand:
                    hand.pop()
            if c["hammer"] and not any(o["dino"] for o in board if o is not c):
                c["tapped"] = True
                c["stun"] = 1
        if opp <= 0:
            return t, opening_lands, t1_elves
    return None, opening_lands, t1_elves


def build(spec):
    deck = []
    for name, n in spec.items():
        deck += [name] * n
    assert len(deck) == 60, len(deck)
    return deck


BASE = {
    LAND: 22, "Llanowar Elves": 4, "Slumbering Trudge": 2, "Bebop & Rocksteady": 4,
    "Pugnacious Hammerskull": 2, "Ghalta the Unstoppable": 4, "Callous Sell-Sword": 4,
    "Wild Ride": 4, "The Last Agni Kai": 4, "Bulk Up": 4, "Ghalta, Primal Hunger": 4,
    "Hazoret, Godseeker": 2,
}


def variant(**changes):
    d = dict(BASE)
    for k, v in changes.items():
        d[k] = d.get(k, 0) + v
        if d[k] == 0:
            del d[k]
    return d


VARIANTS = {
    "A lista do vídeo": BASE,
    "B -2 Hazoret +2 Trudge": variant(**{"Hazoret, Godseeker": -2, "Slumbering Trudge": 2}),
    "C -2 Hammerskull +2 Trudge": variant(**{"Pugnacious Hammerskull": -2, "Slumbering Trudge": 2}),
    "D C + (-2 Hazoret +2 Snakeskin Veil)": variant(**{"Pugnacious Hammerskull": -2, "Slumbering Trudge": 2, "Hazoret, Godseeker": -2, "Snakeskin Veil": 2}),
    "E C com 21 terrenos +1 Hazoret": variant(**{"Pugnacious Hammerskull": -2, "Slumbering Trudge": 2, LAND: -1, "Hazoret, Godseeker": 1}),
    "G A -2 Primal Hunger +2 Trudge": variant(**{"Ghalta, Primal Hunger": -2, "Slumbering Trudge": 2}),
    "H A -2 Hammerskull +2 Felonious Rage": variant(**{"Pugnacious Hammerskull": -2, "Felonious Rage": 2}),
    "K B + (-2 Primal Hunger +2 Snakeskin Veil)": variant(**{"Hazoret, Godseeker": -2, "Slumbering Trudge": 2, "Ghalta, Primal Hunger": -2, "Snakeskin Veil": 2}),
    "L B + (-2 Primal Hunger +2 Hammerskull)": variant(**{"Hazoret, Godseeker": -2, "Slumbering Trudge": 2, "Ghalta, Primal Hunger": -2, "Pugnacious Hammerskull": 2}),
    "N A -2 Primal Hunger +2 Snakeskin Veil": variant(**{"Ghalta, Primal Hunger": -2, "Snakeskin Veil": 2}),
}


def run(spec, games, on_play, target_t):
    deck = build(spec)
    kills = Counter()
    bad_hands = 0
    elves = 0
    for _ in range(games):
        kt, ol, t1e = play_game(deck, on_play, target_t)
        kills[kt] += 1
        if ol <= 1 or ol >= 6:
            bad_hands += 1
        if t1e:
            elves += 1
    cum = 0
    out = {}
    for t in range(2, 7):
        cum += kills[t]
        out[t] = cum / games
    out["none"] = kills[None] / games
    out["bad"] = bad_hands / games
    out["elves"] = elves / games
    return out


if __name__ == "__main__":
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    random.seed(7)
    for target_t, label in ((None, "sem criatura adversária (Agni Kai morta)"), (2, "oponente com uma criatura X/2 a partir do turno 2")):
        print(f"\n=== {label} | {games} partidas por linha ===")
        print(f"{'variante':42s} {'play/draw':9s} {'<=T2':>6s} {'<=T3':>6s} {'<=T4':>6s} {'<=T5':>6s} {'<=T6':>6s} {'>T8':>6s} | Elves T1  mão 0-1/6-7")
        for name, spec in VARIANTS.items():
            for on_play in (True, False):
                r = run(spec, games, on_play, target_t)
                print(f"{name:42s} {'play' if on_play else 'draw':9s} "
                      f"{r[2]*100:5.1f}% {r[3]*100:5.1f}% {r[4]*100:5.1f}% {r[5]*100:5.1f}% {r[6]*100:5.1f}% {r['none']*100:5.1f}% | "
                      f"{r['elves']*100:5.1f}%   {r['bad']*100:5.1f}%")
