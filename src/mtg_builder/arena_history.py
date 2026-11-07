"""Histórico de partidas (spec 011): o Arena guarda em disco só as duas últimas sessões
(`Player.log` e `Player-prev.log`), então o projeto acumula as partidas que vê em
`data/matches.jsonl`, uma por linha, sem repetir (chave: id da partida). O Oráculo
acrescenta ao fim de cada partida; `mtg arena history` varre os logs que ainda existem,
acrescenta o que faltar e resume o win rate por deck.
"""

import json
from datetime import datetime
from pathlib import Path

from . import arena_log, arena_match, db

PATH = db.DATA_DIR / "matches.jsonl"


def load(path=None):
    path = Path(path or PATH)
    if not path.exists():
        return []
    rows = []
    for line in path.read_text("utf-8").splitlines():
        try:
            rows.append(json.loads(line))
        except ValueError:
            continue
    return rows


def key(row):
    return row.get("match_id") or f"{row.get('at')}|{row.get('opponent')}"


def append(row, path=None):
    """Grava a partida se ainda não estiver no arquivo. Devolve True se gravou."""
    path = Path(path or PATH)
    if any(key(r) == key(row) for r in load(path)):
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return True


INVENTORY_PATH = db.DATA_DIR / "inventory.jsonl"
VAULT_POINTS = {"common": 1, "uncommon": 3}     # décimos de por cento por 5ª cópia ou mais (baú abre em 1000)
DUPLICATE_GEMS = {"rare": 20, "mythic": 40}     # raras e míticas repetidas viram gemas, não baú


def append_inventory(event, path=None):
    """Guarda o cofre de cada abertura do Arena (ouro, gemas, curingas, baú), sem repetir."""
    path = Path(path or INVENTORY_PATH)
    row = {"at": event.get("at"), "gold": event.get("gold"), "gems": event.get("gems"), "vault": event.get("vault"),
           "vault_pct": event.get("vault_pct"), "wildcards": event.get("wildcards"), "tokens": event.get("tokens")}
    existing = load(path)
    if any((r.get("at"), r.get("vault"), r.get("gold")) == (row["at"], row["vault"], row["gold"]) for r in existing):
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return True


def vault_estimate(cards, data):
    """Estimativa do avanço do baú com um booster: `cards` [(grpId, raridade)], `data` a
    coleção aproximada (quantidades antes do booster). Devolve (décimos de %, gemas,
    detalhes). É estimativa: a coleção é aproximada e o cliente arredonda."""
    from . import collection as collection_module
    owned = {int(k): v["qty"] for k, v in data.get("cards", {}).items()}
    points, gems, details = 0, 0, []
    seen = {}
    for grp, rarity in cards:
        count = owned.get(grp, 0) + seen.get(grp, 0) + 1
        seen[grp] = seen.get(grp, 0) + 1
        if count <= 4:
            continue
        if rarity in VAULT_POINTS:
            points += VAULT_POINTS[rarity]
            details.append((grp, rarity, "baú", VAULT_POINTS[rarity]))
        elif rarity in DUPLICATE_GEMS:
            gems += DUPLICATE_GEMS[rarity]
            details.append((grp, rarity, "gemas", DUPLICATE_GEMS[rarity]))
    return points, gems, details


def merge(*lists):
    """Junta listas de partidas sem repetir; entre duas iguais, fica a que tem mais dados."""
    seen = {}
    for rows in lists:
        for row in rows:
            k = key(row)
            if k not in seen or sum(v is not None for v in row.values()) > sum(v is not None for v in seen[k].values()):
                seen[k] = row
    return sorted(seen.values(), key=lambda r: r.get("at") or "")


def default_logs():
    folder = arena_log.default_log_dir()
    return [p for p in (folder / "Player-prev.log", folder / "Player.log") if p.exists()]


def scan(paths, conn=None, arena=None):
    """Partidas, último rank e último cofre vistos nos logs dados."""
    rows, rank, inventory, decks = [], None, None, []
    for path in paths:
        follower = arena_log.LogFollower(path, from_start=True, classifier=arena_match.classify_match)
        session = arena_match.MatchSession(conn, arena, records_dir=None, history_path=None, save_records=False)
        for event in follower.finish():
            session.handle(event)
        rows += session.rows
        rank = session.rank or rank
        inventory = session.inventory or inventory
        decks = session.deck_list or decks
    return {"rows": rows, "rank": rank, "inventory": inventory, "decks": decks}


def summary(rows, deck=None):
    """Vitórias, derrotas e win rate por deck (e por evento)."""
    by_deck, by_event = {}, {}
    for row in rows:
        if deck and (row.get("deck") or "").lower() != deck.lower():
            continue
        for table, name in ((by_deck, row.get("deck") or "?"), (by_event, row.get("event") or "?")):
            entry = table.setdefault(name, {"won": 0, "lost": 0, "last": None})
            if row.get("result") == "vitória":
                entry["won"] += 1
            elif row.get("result") == "derrota":
                entry["lost"] += 1
            entry["last"] = max(entry["last"] or "", row.get("at") or "")
    for table in (by_deck, by_event):
        for entry in table.values():
            total = entry["won"] + entry["lost"]
            entry["matches"] = total
            entry["win_rate"] = round(entry["won"] / total, 3) if total else None
    return {"decks": by_deck, "events": by_event}


def _when(value):
    try:
        return datetime.fromisoformat(value).strftime("%d/%m %H:%M")
    except (TypeError, ValueError):
        return (value or "?")[:16]


def format_history(rows, stats, rank=None, inventory=None, deck=None, limit=30):
    lines = []
    shown = [r for r in rows if not deck or (r.get("deck") or "").lower() == deck.lower()]
    lines.append(f"{len(shown)} partida(s) conhecida(s)" + (f" com \"{deck}\"" if deck else "") +
                 " (só o que passou pelos logs ou pelo Oráculo; partidas anteriores não ficam na máquina)")
    for row in shown[-limit:]:
        turns = f" · {row['own_turns']} turnos seus" if row.get("own_turns") else ""
        lines.append(f"  {_when(row.get('at'))}  {row.get('event') or '?':<20} {row.get('deck') or '?':<24} "
                     f"× {row.get('opponent') or '?':<16} {row.get('result') or '?'}{turns}")
    if stats["decks"]:
        lines += ["", "por deck:"]
        for name, e in sorted(stats["decks"].items(), key=lambda kv: -kv[1]["matches"]):
            wr = f"{e['win_rate']:.0%}" if e["win_rate"] is not None else "—"
            lines.append(f"  {name:<28} {e['won']}–{e['lost']}  {wr}")
    if rank:
        lines += ["", f"ranqueada construída (temporada {rank.get('season')}): {rank.get('class')} {rank.get('level')}, "
                      f"{rank.get('won')}–{rank.get('lost')} na temporada inteira (todos os decks, pelo cliente)"]
    if inventory:
        wc = inventory.get("wildcards") or {}
        lines.append(f"cofre: {inventory.get('gold')} ouro · {inventory.get('gems')} gemas · curingas C{wc.get('common')} "
                     f"U{wc.get('uncommon')} R{wc.get('rare')} M{wc.get('mythic')}"
                     + (f" · baú {inventory['vault_pct']:.1f}%" if inventory.get("vault_pct") is not None else "")
                     + " · fichas: "
                     + ", ".join(f"{k} {v}" for k, v in (inventory.get("tokens") or {}).items() if "Draft" in k or "Play" in k))
    history = load(INVENTORY_PATH)
    vaults = [r for r in history if r.get("vault_pct") is not None]
    if len(vaults) >= 2:
        first, last = vaults[0], vaults[-1]
        lines.append(f"baú: {first['vault_pct']:.1f}% em {_when(first.get('at'))} → {last['vault_pct']:.1f}% em "
                     f"{_when(last.get('at'))} ({last['vault_pct'] - first['vault_pct']:+.1f} pontos; "
                     "5ª cópia de comum +0,1, de incomum +0,3; raras e míticas repetidas viram gemas)")
    return "\n".join(lines)
