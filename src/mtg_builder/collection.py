"""Coleção do usuário, aproximada (spec 011, requisito 8).

O cliente atual do Arena não grava a coleção no log (conferido em 2026-11-07, inclusive
com a aba Coleção aberta). O que ele grava, na resposta de abertura (`StartHook`), são
as listas completas dos decks salvos; e cada carta que entra num deck salvo é, quase
sempre, uma carta que o jogador tem. Este módulo junta essas fontes em
`data/collection.json`, por `grpId` do Arena, com a quantidade máxima vista em cada
fonte: decks salvos, boosters abertos (quando o log mostrar) e lançamentos manuais.
É uma aproximação por baixo: tudo o que está aqui o usuário tem (salvo deck salvo com
carta faltando); o que não está pode ter também.
"""

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from . import db, decklist

PATH = db.DATA_DIR / "collection.json"
SECTIONS = ("MainDeck", "Sideboard", "CommandZone", "Companions")


def load(path=None):
    path = Path(path or PATH)
    if not path.exists():
        return {"updated_at": None, "sources": {}, "cards": {}}
    return json.loads(path.read_text("utf-8"))


def save(data, path=None):
    path = Path(path or PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = datetime.now().isoformat(timespec="seconds")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=0), encoding="utf-8")
    return path


def cards_in_decks(decks_internal):
    """{grpId: maior quantidade em algum deck} a partir de `DecksInternal` do StartHook."""
    need = Counter()
    for deck in (decks_internal or {}).values():
        if not isinstance(deck, dict):
            continue
        for section in SECTIONS:
            for item in deck.get(section) or []:
                try:
                    grp, qty = int(item["cardId"]), int(item.get("quantity", 1))
                except (KeyError, TypeError, ValueError):
                    continue
                need[grp] = max(need[grp], qty)
    return dict(need)


def update(data, quantities, source, resolve, mode=None):
    """Aplica {grpId: quantidade} de uma fonte. `mode` "max" (decks: quantidade máxima
    vista) ou "add" (booster: soma); sem `mode`, booster soma e o resto é máximo.
    `resolve(grp_ids)` vem da base do Arena. Devolve quantas entradas mudaram."""
    mode = mode or ("add" if source == "booster" else "max")
    cards = data.setdefault("cards", {})
    ids = [int(g) for g in quantities]
    info = {r["grp"]: r for r in resolve(ids)} if ids else {}
    changed = 0
    for grp in ids:
        entry = cards.get(str(grp))
        qty = int(quantities[grp] if grp in quantities else quantities[str(grp)])
        if entry is None:
            meta = info.get(grp) or {}
            entry = cards[str(grp)] = {"name": meta.get("name") or f"#{grp}", "set": meta.get("set"),
                                       "number": meta.get("number"), "rarity": meta.get("rarity"), "qty": 0, "sources": []}
        before = entry["qty"]
        entry["qty"] = max(entry["qty"], qty) if mode == "max" else entry["qty"] + qty
        if source not in entry["sources"]:
            entry["sources"].append(source)
        changed += entry["qty"] != before
    data.setdefault("sources", {})[source] = {"at": datetime.now().isoformat(timespec="seconds"),
                                              "cards": sum(1 for e in cards.values() if source in e["sources"])}
    return changed


def import_csv(data, path, conn=None, source="csv"):
    """Importa uma exportação de coleção em CSV (colunas com nome e quantidade; coleção e
    número de colecionador quando houver), como a de rastreadores externos. Linhas sem
    carta reconhecida na base entram só pelo nome. Devolve (importadas, não reconhecidas)."""
    import csv
    from . import decklist as decklist_module
    text = Path(path).read_text("utf-8-sig")
    reader = csv.DictReader(text.splitlines())
    fields = {f.lower(): f for f in reader.fieldnames or []}

    def pick(*names):
        for name in names:
            if name in fields:
                return fields[name]
        return None

    col_name = pick("name", "card name", "card", "nome", "carta")
    col_qty = pick("quantity", "qty", "count", "owned", "quantidade", "cópias", "copias")
    col_set = pick("set", "set code", "expansion", "coleção", "colecao", "edição")
    col_num = pick("collector number", "number", "collector_number", "número", "numero")
    if not col_name or not col_qty:
        raise RuntimeError(f"CSV sem colunas de nome e quantidade; colunas: {reader.fieldnames}")
    index = decklist_module._name_index(conn) if conn is not None else {}
    cards = data.setdefault("cards", {})
    imported, unknown = 0, []
    for row in reader:
        name = (row.get(col_name) or "").strip()
        try:
            qty = int(float(row.get(col_qty) or 0))
        except ValueError:
            continue
        if not name or qty <= 0:
            continue
        set_code = (row.get(col_set) or "").strip().lower() if col_set else ""
        number = (row.get(col_num) or "").strip() if col_num else ""
        card = index.get(decklist_module._key(name)) or index.get(decklist_module._key(name.split(" // ")[0]))
        if card is None:
            unknown.append(name)
        key = f"csv:{set_code or '?'}:{number or '?'}:{decklist_module._key(name.split(' // ')[0])}"
        entry = cards.setdefault(key, {"name": card["name"] if card else name, "set": set_code or None,
                                       "number": number or None, "rarity": None, "qty": 0, "sources": []})
        entry["qty"] = max(entry["qty"], qty)
        if source not in entry["sources"]:
            entry["sources"].append(source)
        imported += 1
    data.setdefault("sources", {})[source] = {"at": datetime.now().isoformat(timespec="seconds"),
                                              "cards": sum(1 for e in cards.values() if source in e["sources"])}
    return imported, unknown


def by_name(data):
    """{nome (face da frente, minúsculas): quantidade somada entre impressões}."""
    totals = Counter()
    for entry in data.get("cards", {}).values():
        totals[decklist._key(entry["name"].split(" // ")[0])] += entry["qty"]
    return totals


def owned(data, name):
    return by_name(data).get(decklist._key(name.split(" // ")[0]), 0)


def summary(data, set_code=None):
    cards = [e for e in data.get("cards", {}).values() if not set_code or e.get("set") == set_code.lower()]
    sets = Counter(e.get("set") for e in cards)
    rarities = Counter(e.get("rarity") for e in cards)
    return {"cards": len(cards), "copies": sum(e["qty"] for e in cards), "sets": sets.most_common(),
            "rarities": dict(rarities), "updated_at": data.get("updated_at"), "sources": data.get("sources", {})}


def format_summary(data, set_code=None, limit=12):
    stats = summary(data, set_code)
    lines = [f"coleção aproximada: {stats['cards']} cartas distintas, {stats['copies']} cópias"
             + (f" em {set_code.upper()}" if set_code else "") + f" · atualizada em {stats['updated_at'] or '—'}",
             "fontes: " + (", ".join(f"{k} ({v['cards']} cartas, {v['at'][:16]})" for k, v in stats["sources"].items()) or "nenhuma"),
             "aproximação por baixo: tudo o que está aqui você tem (salvo deck salvo com carta faltando); "
             "o que não está pode ter também"]
    if not set_code:
        lines.append("coleções mais presentes: " + ", ".join(f"{s or '?'} {n}" for s, n in stats["sets"][:limit]))
    else:
        rows = sorted((e for e in data.get("cards", {}).values() if e.get("set") == set_code.lower()),
                      key=lambda e: (e.get("rarity") or "", e["name"]))
        for e in rows:
            lines.append(f"  {e['qty']} {e['name']} ({(e.get('rarity') or '?')[:1].upper()})")
    return "\n".join(lines)
