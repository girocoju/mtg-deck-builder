"""CLI `mtg`: sincroniza e consulta a base local de cartas."""

import argparse
import json
import sys

from . import db, query, scryfall


def _card_dict(row):
    card = {k: row[k] for k in row.keys() if row[k] is not None and k != "faces"}
    card["keywords"] = json.loads(card.get("keywords") or "[]")
    return card


def _card_line(row):
    stats = ""
    if row["power"] is not None:
        stats = f" {row['power']}/{row['toughness']}"
    elif row["loyalty"] is not None:
        stats = f" [{row['loyalty']}]"
    text = (row["oracle_text"] or "").replace("\n", " / ")
    return f"{row['name']} {row['mana_cost'] or ''} | {row['type_line']}{stats} | {text}"


def _emit(args, data, lines):
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=1))
    else:
        print("\n".join(lines))


def cmd_sync(args):
    conn = db.connect()
    scryfall.sync(conn, force=args.force)


def cmd_stats(args):
    data = query.stats(db.connect(readonly=True))
    _emit(args, data, [f"{k}: {v}" for k, v in data.items()])


def cmd_search(args):
    conn = db.connect(readonly=True)
    rows = query.search(
        conn, name=args.name, text=args.text, type_line=args.type, identity=args.identity,
        colors=args.colors, fmt=args.format, set_code=args.set, rarity=args.rarity,
        game=args.game, booster=args.booster, cmc_min=args.cmc_min, cmc_max=args.cmc_max,
        include_extras=args.all, order=args.order, limit=args.limit,
    )
    _emit(args, [_card_dict(r) for r in rows],
          [_card_line(r) for r in rows] + [f"({len(rows)} cartas)"])


def cmd_card(args):
    conn = db.connect(readonly=True)
    row, candidates = query.find_card(conn, args.name)
    if row is None:
        if not candidates:
            sys.exit(f"Carta não encontrada: {args.name}")
        print("Carta não encontrada com esse nome exato. Candidatas:")
        print("\n".join(f"  {c['name']}" for c in candidates))
        sys.exit(1)

    legal = query.legalities(conn, row["oracle_id"])
    prints = query.printings(conn, row["oracle_id"])
    rules = query.rulings(conn, row["oracle_id"])
    data = _card_dict(row)
    data["legalities"] = legal
    data["printings"] = [
        {k: p[k] for k in ("set_code", "collector_number", "rarity", "released_at", "games",
                           "usd", "eur", "tix")}
        for p in prints
    ]
    data["rulings"] = [dict(r) for r in rules]

    lines = [
        f"{row['name']}  {row['mana_cost'] or ''}",
        f"{row['type_line']}" + (f"  {row['power']}/{row['toughness']}" if row["power"] is not None else "")
        + (f"  [lealdade {row['loyalty']}]" if row["loyalty"] is not None else ""),
        row["oracle_text"] or "",
        f"Identidade de cor: {row['color_identity'] or 'incolor'} | CMC: {row['cmc']:g}"
        + (f" | EDHREC rank: {row['edhrec_rank']}" if row["edhrec_rank"] else ""),
        "Legal em: " + (", ".join(f for f, s in legal.items() if s == "legal") or "nenhum formato"),
    ]
    other = [f"{f} ({s})" for f, s in legal.items() if s != "legal"]
    if other:
        lines.append("Restrições: " + ", ".join(other))
    lines.append(f"Impressões ({len(prints)}): " + ", ".join(
        f"{p['set_code']}#{p['collector_number']} {p['rarity']}" for p in prints[:15]
    ) + (" ..." if len(prints) > 15 else ""))
    if args.rulings:
        lines += [f"- [{r['published_at']}] {r['comment']}" for r in rules]
    elif rules:
        lines.append(f"Rulings: {len(rules)} (use --rulings para ver)")
    _emit(args, data, lines)


def cmd_sets(args):
    conn = db.connect(readonly=True)
    rows = query.find_sets(conn, args.term)
    if args.type:
        rows = [r for r in rows if r["set_type"] == args.type]
    rows = rows[: args.limit]
    data = [dict(r) for r in rows]
    for item in data:
        if args.term:
            # Coleções recém-lançadas podem vir do Scryfall sem a marcação de booster.
            item["booster_rarities"] = query.set_rarity_counts(conn, item["code"])
            if not item["booster_rarities"]:
                item["all_rarities"] = query.set_rarity_counts(conn, item["code"], booster_only=False)
    lines = [
        f"{s['code']:<6} {s['released_at'] or '?':<10} {s['set_type'] or '':<16} "
        f"{s['card_count'] or 0:>4}  {s['name']}"
        + (f"  booster: {s['booster_rarities']}" if s.get("booster_rarities") else "")
        + (f"  sem marcação de booster; todas: {s['all_rarities']}" if s.get("all_rarities") else "")
        for s in data
    ]
    _emit(args, data, lines)


def cmd_sql(args):
    conn = db.connect(readonly=True)
    rows = conn.execute(args.query).fetchall()
    _emit(args, [dict(r) for r in rows],
          ["\t".join("" if v is None else str(v) for v in r) for r in rows])


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(prog="mtg", description=__doc__)
    parser.add_argument("--json", action="store_true", help="saída em JSON")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("sync", help="baixa/atualiza a base a partir do Scryfall")
    p.add_argument("--force", action="store_true", help="reimporta mesmo se já estiver em dia")
    p.set_defaults(func=cmd_sync)

    p = sub.add_parser("stats", help="resumo da base local")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("search", help="busca cartas por filtros")
    p.add_argument("--name", help="trecho do nome")
    p.add_argument("--text", help="busca full-text (sintaxe FTS5) em nome, tipo e texto")
    p.add_argument("--type", help="palavras da linha de tipo, ex.: 'legendary creature'")
    p.add_argument("--identity", help="identidade de cor contida em, ex.: GU ('' ou C = incolor)")
    p.add_argument("--colors", help="carta tem todas estas cores, ex.: UR")
    p.add_argument("--format", help="legal no formato, ex.: standard, brawl, modern")
    p.add_argument("--set", help="código da coleção")
    p.add_argument("--rarity", choices=["common", "uncommon", "rare", "mythic", "special", "bonus"])
    p.add_argument("--game", choices=["paper", "arena", "mtgo"])
    p.add_argument("--booster", action="store_true", help="só impressões que saem em booster")
    p.add_argument("--cmc-min", type=float)
    p.add_argument("--cmc-max", type=float)
    p.add_argument("--all", action="store_true", help="inclui tokens, emblemas e afins")
    p.add_argument("--order", choices=sorted(query.ORDERS), default="name")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("card", help="detalhes de uma carta pelo nome")
    p.add_argument("name")
    p.add_argument("--rulings", action="store_true")
    p.set_defaults(func=cmd_card)

    p = sub.add_parser("sets", help="lista coleções (por código ou trecho do nome)")
    p.add_argument("term", nargs="?")
    p.add_argument("--type", help="set_type do Scryfall, ex.: expansion, core, masters")
    p.add_argument("--limit", type=int, default=30)
    p.set_defaults(func=cmd_sets)

    p = sub.add_parser("sql", help="consulta SQL somente leitura na base")
    p.add_argument("query")
    p.set_defaults(func=cmd_sql)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
