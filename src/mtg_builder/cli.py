"""CLI `mtg`: sincroniza e consulta a base local de cartas."""

import argparse
import json
import sys

from . import analysis, db, decklist, draft, edhrec, formats, meta, query, scryfall


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


def _read_deck(path):
    try:
        text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8-sig").read()
    except OSError as error:
        sys.exit(f"Não foi possível ler a lista: {error}")
    return decklist.parse(text, markdown=path.lower().endswith(".md"))


def cmd_deck_validate(args):
    conn = db.connect(readonly=True)
    deck = _read_deck(args.file)
    errors, warnings = formats.validate(conn, deck, args.format, game=args.game)
    data = {"valid": not errors, "format": args.format.lower(),
            "main": deck.count("main"), "sideboard": deck.count("sideboard"),
            "commander": [e.name for e in deck.commander], "errors": errors, "warnings": warnings}
    lines = [f"{args.format.lower()}: {data['main']} no deck principal, "
             f"{data['sideboard']} no sideboard"
             + (f", comandante: {' + '.join(data['commander'])}" if deck.commander else "")]
    lines += [f"ERRO: {e}" for e in errors] + [f"aviso: {w}" for w in warnings]
    lines.append("Lista válida." if not errors else f"Lista inválida ({len(errors)} problemas).")
    _emit(args, data, lines)
    if errors:
        sys.exit(1)


def cmd_deck_export(args):
    conn = db.connect(readonly=True)
    deck = _read_deck(args.file)
    unknown = decklist.resolve(conn, deck)
    for entry, _ in unknown:
        print(f"aviso: carta não encontrada, exportada como está: {entry.name}", file=sys.stderr)
    print(decklist.export(deck, args.to), end="")


def cmd_deck_cost(args):
    conn = db.connect(readonly=True)
    deck = _read_deck(args.file)
    decklist.resolve(conn, deck)
    data = decklist.cost(conn, deck)
    wild = ", ".join(f"{n} {r}" for r, n in data["wildcards"].items())
    lines = [
        f"Papel: US$ {data['usd']:.2f} | € {data['eur']:.2f}   MTGO: {data['tix']:.2f} tix",
        f"Arena (wildcards, sem contar o que você já tem): {wild}",
    ]
    for key, names in data["sem_preco"].items():
        if names:
            lines.append(f"Sem preço em {key} ({len(names)}): {', '.join(names[:10])}"
                         + (" ..." if len(names) > 10 else ""))
    if data["fora_do_arena"]:
        lines.append(f"Fora do Arena ({len(data['fora_do_arena'])}): "
                     + ", ".join(data["fora_do_arena"][:10]))
    _emit(args, data, lines)


def cmd_deck_diff(args):
    conn = db.connect(readonly=True)
    before, after = _read_deck(args.before), _read_deck(args.after)
    decklist.resolve(conn, before)
    decklist.resolve(conn, after)
    data = decklist.diff(before, after)
    titles = {"commander": "Comandante", "main": "Deck principal", "sideboard": "Sideboard"}
    lines = []
    for section, changes in data.items():
        lines.append(f"{titles[section]}:")
        lines += [f"  {'saiu ' if n < 0 else 'entrou'} {abs(n)} {name}" for n, name in changes]
    for label, deck in (("antes", before), ("depois", after)):
        lines.append(f"{label}: {deck.count('main')} no principal, {deck.count('sideboard')} no sideboard")
    _emit(args, data, lines or ["As listas são iguais."])


def cmd_deck_analyze(args):
    conn = db.connect(readonly=True)
    deck = _read_deck(args.file)
    unknown = decklist.resolve(conn, deck)
    data = analysis.analyze(deck)
    data["nao_encontradas"] = [entry.name for entry, _ in unknown]
    lines = [analysis.report(data)]
    if unknown:
        lines.append("Cartas não encontradas (fora da análise): " + ", ".join(data["nao_encontradas"]))
    _emit(args, data, lines)


def cmd_odds(args):
    seen = analysis.cards_seen(args.turn, on_the_play=not args.draw)
    chance = analysis.hypergeom_at_least(args.deck, args.copies, seen, args.min)
    data = {"deck": args.deck, "copies": args.copies, "turn": args.turn, "cards_seen": seen,
            "at_least": args.min, "probability": chance}
    _emit(args, data, [f"{chance:.1%} de ter pelo menos {args.min} de {args.copies} cópias até o "
                       f"turno {args.turn} ({seen} cartas vistas de {args.deck}, sem mulligan)"])


def cmd_meta_update(args):
    conn = db.connect(readonly=True)
    try:
        meta.update_goldfish(conn, args.format.lower(), top=args.top, force=args.force)
    except RuntimeError as error:
        previous = meta.latest(args.format.lower(), "bo3")
        hint = (f" O snapshot anterior ({previous['collected_at'][:10]}) continua disponível."
                if previous else " Não há snapshot anterior; use a busca na web e declare isso.")
        sys.exit(f"Coleta falhou: {error}{hint}")


def cmd_meta_show(args):
    conn = db.connect(readonly=True)
    fmt = args.format.lower()
    modes = meta.MODES if args.mode == "all" else (args.mode,)
    data, lines = {}, []
    for mode in modes:
        snapshot = meta.latest(fmt, mode)
        if snapshot is None:
            data[mode] = None
            lines.append(f"{fmt} ({mode.upper()}): sem snapshot. "
                         + ("Rode `mtg meta update`." if mode == "bo3" else
                            "Não há coleta automática de BO1; importe com `mtg meta import`."))
        else:
            summary = meta.summarize(conn, snapshot)
            data[mode] = {"snapshot": snapshot, "summary": summary}
            lines.append(meta.report(snapshot, summary, limit=args.limit))
        lines.append("")
    _emit(args, data, lines)


def cmd_meta_import(args):
    conn = db.connect(readonly=True)
    try:
        snapshot = meta.import_csv(conn, args.file, args.format.lower(), args.mode, args.source,
                                   decks_dir=args.decks, url=args.url, collected=args.date)
    except (RuntimeError, OSError) as error:
        sys.exit(f"Importação falhou: {error}")
    print(f"{len(snapshot['archetypes'])} arquétipos importados em {snapshot['file']}")


def _commander_names(args):
    return [args.commander] + ([args.partner] if args.partner else [])


def cmd_commander(args):
    conn = db.connect(readonly=True)
    data = edhrec.commander_report(conn, _commander_names(args), args.format)
    if data["ok"]:
        lines = [f"{' + '.join(data['commanders'])}: comandante válido em {data['format']} "
                 f"({data['deck_size']} cartas). Identidade de cor: {data['identity'] or 'incolor'}."]
    else:
        lines = ["Comandante inválido:"] + [f"  {p}" for p in data["problems"]]
    _emit(args, data, lines)
    if not data["ok"]:
        sys.exit(1)


def cmd_edhrec(args):
    conn = db.connect(readonly=True)
    names = _commander_names(args)
    fmt = args.format.lower() if args.format else None
    try:
        if args.average:
            data = edhrec.average_deck(conn, names, fmt, args.game, force=args.force)
        else:
            data = edhrec.recommendations(conn, names, fmt, args.game, force=args.force)
    except RuntimeError as error:
        sys.exit(f"EDHREC indisponível: {error} Use a busca na base (`mtg search`) e declare a falta dos dados.")

    scope = f"filtrado para {fmt or 'qualquer formato'}" + (f", {args.game}" if args.game else "")
    head = (f"{' + '.join(names)} | fonte: EDHREC (Commander de papel) | coletado em "
            f"{data['fetched_at'][:10]} | {scope}")
    if args.average:
        lines = [head, f"Deck médio: {data['kept_count']} cartas utilizáveis, "
                       f"{data['dropped_count']} descartadas pelo filtro.", "", "Commander"]
        lines += [f"1 {name}" for name in data["commander"]] + ["", "Deck"]
        lines += [f"{i['qty']} {i['name']}" for i in data["kept"]]
        if data["dropped"]:
            lines += ["", "# Descartadas: " + "; ".join(f"{i['name']} ({i['status']})" for i in data["dropped"])]
    else:
        usable = [c for c in data["cards"] if c["status"] == "ok"
                  and (c["inclusion"] or 0) >= args.min_inclusion]
        usable.sort(key=lambda c: -c["synergy"])
        excluded = [c for c in data["cards"] if c["status"] != "ok"]
        lines = [head, f"{data['decks']} decks no EDHREC | temas: "
                 + ", ".join(f"{t} ({n})" for t, n in data["themes"]),
                 "Média por tipo: " + ", ".join(f"{k} {v}" for k, v in data["average_types"].items() if v),
                 "", "sinergia | inclusão | carta [papéis] (categoria)"]
        lines += [f"  {c['synergy']:+.2f} | {c['inclusion']:>5}% | {c['name']}"
                  + (f" [{', '.join(c['roles'])}]" if c["roles"] else "")
                  + (" [GAME CHANGER]" if c["game_changer"] else "") + f" ({c['category']})"
                  for c in usable]
        reasons = {}
        for c in excluded:
            reasons[c["status"]] = reasons.get(c["status"], 0) + 1
        lines += ["", f"{len(usable)} cartas utilizáveis; {len(excluded)} excluídas pelo filtro: "
                  + ", ".join(f"{n} {r}" for r, n in reasons.items())]
        if args.all:
            lines += [f"  {c['name']} — {c['status']}" for c in excluded]
    _emit(args, data, lines)


def _pct(value):
    return f"{value:6.1%}" if value is not None else "     —"


def _draft_snapshot(conn, args):
    try:
        snapshot = draft.update(conn, args.set, args.mode, force=getattr(args, "force", False))
    except RuntimeError as error:
        sys.exit(f"17Lands indisponível: {error} Trabalhe em modo teórico "
                 "(`mtg draft set`) e declare a falta dos dados.")
    return snapshot


def _draft_head(snapshot):
    if not snapshot["has_data"]:
        return (f"{snapshot['set_name']} ({snapshot['event']}): o 17Lands não tem dados para esta "
                "coleção neste modo. Use o modo teórico (`mtg draft set`) e declare isso.")
    return (f"{snapshot['set_name']} | {snapshot['event']} | fonte: 17Lands | coletado em "
            f"{snapshot['collected_at'][:10]} | {snapshot['games']} jogos, "
            f"win rate médio dos usuários {_pct(snapshot['baseline']).strip()}")


def _draft_table(rows):
    lines = ["   GIH     OH     GD    IWD  ALSA   ATA   jogos  raridade  cor  carta"]
    for c in rows:
        lines.append(
            f"{_pct(c['gih'])} {_pct(c['oh'])} {_pct(c['gd'])} "
            + (f"{c['iwd'] * 100:+5.1f}pp" if c["iwd"] is not None else "     —")
            + f" {c['alsa'] or 0:5.2f} {c['ata'] or 0:5.2f} {c['gih_games']:>7}  "
            f"{(c['rarity'] or '?'):<8}  {c['color'] or '-':<3}  {c['name']}")
    return lines


def cmd_draft_update(args):
    conn = db.connect(readonly=True)
    modes = list(draft.MODES) if args.mode == "all" else [args.mode]
    for mode in modes:
        args.mode = mode
        print(_draft_head(_draft_snapshot(conn, args)))


def cmd_draft_set(args):
    conn = db.connect(readonly=True)
    snapshot = draft.cached(draft.find_set(conn, args.set)["code"], args.mode)
    data = draft.set_overview(conn, args.set, snapshot)
    lines = [f"{data['name']} ({data['set']}), lançada em {data['released_at']} | {data['cards']} cartas "
             f"| conjunto draftável: {data['basis']}", "",
             "cor       total  C   U   R   M | comuns+incomuns: criaturas (curva 1..6+) | remoção"]
    for group, e in data["colors"].items():
        curve = " ".join(str(e["curva_criaturas_cu"].get(str(i), 0)) for i in range(1, 7))
        lines.append(f"{group:<9} {e['total']:>4} {e['common']:>3} {e['uncommon']:>3} {e['rare']:>3} "
                     f"{e['mythic']:>3} | {e['criaturas_cu']:>2} ({curve}) | "
                     f"{len(e['remocao_cu'])}: {', '.join(e['remocao_cu'])}")
    lines += ["", "Palavras-chave mais frequentes: " + ", ".join(f"{k} ({n})" for k, n in data["keywords"])]
    _emit(args, data, lines)


def cmd_draft_cards(args):
    conn = db.connect(readonly=True)
    snapshot = _draft_snapshot(conn, args)
    rows = draft.ranking(snapshot, args.color, args.rarity, args.min_games, args.sort, args.limit)
    _emit(args, rows, [_draft_head(snapshot)] + (_draft_table(rows) if snapshot["has_data"] else []))


def cmd_draft_colors(args):
    conn = db.connect(readonly=True)
    snapshot = _draft_snapshot(conn, args)
    rows = draft.color_pairs(snapshot)
    lines = [_draft_head(snapshot)] + [
        f"{_pct(c['win_rate'])}  {c['games']:>7} jogos  {c['name']}" for c in rows]
    _emit(args, rows, lines)


def cmd_draft_rate(args):
    conn = db.connect(readonly=True)
    snapshot = _draft_snapshot(conn, args)
    names = list(args.cards)
    if args.file:
        deck = _read_deck(args.file)
        names += [e.name for e in deck.entries()]
    found, missing = draft.rate(snapshot, names)
    found.sort(key=lambda c: (c["color"], -(c["gih"] or 0)))
    lines = [_draft_head(snapshot)] + _draft_table(found)
    if missing:
        lines.append("Sem dados no 17Lands: " + ", ".join(missing))
    _emit(args, {"cards": found, "missing": missing}, lines)


def cmd_draft_gaps(args):
    conn = db.connect(readonly=True)
    snapshot = _draft_snapshot(conn, args)
    data = draft.over_under(snapshot, args.min_games)
    lines = [_draft_head(snapshot), "", "Subestimadas (rendem muito, saem tarde):"]
    lines += _draft_table(data["subestimadas"]) + ["", "Superestimadas (saem cedo, rendem pouco):"]
    lines += _draft_table(data["superestimadas"])
    _emit(args, data, lines)


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

    deck = sub.add_parser("deck", help="valida, exporta e calcula o custo de decklists")
    deck_sub = deck.add_subparsers(dest="deck_command", required=True)
    file_help = "arquivo da lista (.txt, ou .md com a lista em bloco de código); '-' lê da entrada padrão"

    p = deck_sub.add_parser("validate", help="confere a lista contra as regras do formato")
    p.add_argument("file", help=file_help)
    p.add_argument("--format", required=True, help=f"um de: {', '.join(sorted(formats.RULES))}")
    p.add_argument("--game", choices=["paper", "arena", "mtgo"],
                   help="exige que toda carta exista na plataforma")
    p.set_defaults(func=cmd_deck_validate)

    p = deck_sub.add_parser("export", help="exporta para Arena, MTGO ou texto")
    p.add_argument("file", help=file_help)
    p.add_argument("--to", choices=["arena", "mtgo", "text"], default="arena")
    p.set_defaults(func=cmd_deck_export)

    p = deck_sub.add_parser("cost", help="preço em papel/MTGO e wildcards do Arena")
    p.add_argument("file", help=file_help)
    p.set_defaults(func=cmd_deck_cost)

    p = deck_sub.add_parser("diff", help="o que saiu e o que entrou entre duas versões de uma lista")
    p.add_argument("before", help="lista original")
    p.add_argument("after", help="lista nova")
    p.set_defaults(func=cmd_deck_diff)

    p = deck_sub.add_parser("analyze", help="curva, base de mana, papéis e probabilidades")
    p.add_argument("file", help=file_help)
    p.set_defaults(func=cmd_deck_analyze)

    meta_cmd = sub.add_parser("meta", help="snapshots de metagame de construído")
    meta_sub = meta_cmd.add_subparsers(dest="meta_command", required=True)

    p = meta_sub.add_parser("update", help="coleta o meta no MTGGoldfish (torneios, BO3)")
    p.add_argument("format", help=f"um de: {', '.join(sorted(meta.GOLDFISH_FORMATS))}")
    p.add_argument("--top", type=int, default=12, help="quantas listas de referência baixar")
    p.add_argument("--force", action="store_true", help="coleta mesmo com snapshot recente")
    p.set_defaults(func=cmd_meta_update)

    p = meta_sub.add_parser("show", help="mostra o snapshot mais recente e o resumo do meta")
    p.add_argument("format")
    p.add_argument("--mode", choices=["bo1", "bo3", "all"], default="all")
    p.add_argument("--limit", type=int, default=20, help="arquétipos listados")
    p.set_defaults(func=cmd_meta_show)

    p = meta_sub.add_parser("import", help="importa um meta de CSV (ex.: BO1 do Arena)")
    p.add_argument("file", help="CSV com colunas archetype,share[,winrate][,games]")
    p.add_argument("--format", required=True)
    p.add_argument("--mode", required=True, choices=["bo1", "bo3"])
    p.add_argument("--source", required=True, help="nome curto da fonte, ex.: untapped")
    p.add_argument("--decks", help="pasta com '<arquétipo>.txt' para as listas de referência")
    p.add_argument("--url", help="endereço de onde os dados foram tirados")
    p.add_argument("--date", help="data dos dados (AAAA-MM-DD); padrão: hoje")
    p.set_defaults(func=cmd_meta_import)

    draft_cmd = sub.add_parser("draft", help="dados de limitado: 17Lands e leitura da coleção")
    draft_sub = draft_cmd.add_subparsers(dest="draft_command", required=True)

    def draft_parser(name, help_text, func, mode_default="premier", modes=tuple(draft.MODES)):
        parser_ = draft_sub.add_parser(name, help=help_text)
        parser_.add_argument("set", help="código ou nome da coleção")
        parser_.add_argument("--mode", choices=modes, default=mode_default,
                             help="premier, quick, trad (BO3), sealed, tradsealed, picktwo")
        parser_.set_defaults(func=func)
        return parser_

    p = draft_parser("update", "coleta os dados do 17Lands (no máximo 1x por dia)", cmd_draft_update,
                     modes=tuple(draft.MODES) + ("all",))
    p.add_argument("--force", action="store_true")
    draft_parser("set", "leitura da coleção pela base: cores, raridades, curva, remoção", cmd_draft_set)
    p = draft_parser("cards", "ranking de cartas por win rate", cmd_draft_cards)
    p.add_argument("--color", help="W, U, B, R, G, multi ou colorless")
    p.add_argument("--rarity", choices=["common", "uncommon", "rare", "mythic"])
    p.add_argument("--sort", choices=["gih", "oh", "gd", "iwd", "alsa", "ata", "gp"], default="gih")
    p.add_argument("--min-games", type=int, default=draft.MIN_GAMES)
    p.add_argument("--limit", type=int, default=15)
    draft_parser("colors", "win rate por par de cores", cmd_draft_colors)
    p = draft_parser("rate", "estatísticas das cartas de um pacote ou pool", cmd_draft_rate)
    p.add_argument("cards", nargs="*", help="nomes das cartas")
    p.add_argument("--file", help="arquivo de lista com o pool")
    p = draft_parser("gaps", "cartas subestimadas e superestimadas (GIH WR vs. ALSA)", cmd_draft_gaps)
    p.add_argument("--min-games", type=int, default=draft.MIN_GAMES)

    p = sub.add_parser("commander", help="confere se uma carta pode ser comandante no formato")
    p.add_argument("commander")
    p.add_argument("--partner", help="segundo comandante")
    p.add_argument("--format", required=True, help="commander, brawl, standardbrawl...")
    p.set_defaults(func=cmd_commander)

    p = sub.add_parser("edhrec", help="sinergias do EDHREC para um comandante, filtradas pela base")
    p.add_argument("commander")
    p.add_argument("--partner", help="segundo comandante")
    p.add_argument("--format", help="só cartas legais no formato (ex.: brawl)")
    p.add_argument("--game", choices=["paper", "arena", "mtgo"], help="só cartas da plataforma")
    p.add_argument("--average", action="store_true", help="deck médio do EDHREC, como modelo de partida")
    p.add_argument("--min-inclusion", type=float, default=0, help="inclusão mínima, em %%")
    p.add_argument("--all", action="store_true", help="lista também as cartas excluídas")
    p.add_argument("--force", action="store_true", help="ignora o cache de 7 dias")
    p.set_defaults(func=cmd_edhrec)

    p = sub.add_parser("odds", help="chance de comprar N cópias até um turno (hipergeométrica)")
    p.add_argument("--deck", type=int, default=60, help="cartas no deck (padrão 60)")
    p.add_argument("--copies", type=int, required=True, help="cópias da carta (ou terrenos) no deck")
    p.add_argument("--turn", type=int, required=True)
    p.add_argument("--min", type=int, default=1, help="quantas cópias pelo menos (padrão 1)")
    p.add_argument("--draw", action="store_true", help="jogando depois (uma carta a mais)")
    p.set_defaults(func=cmd_odds)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
