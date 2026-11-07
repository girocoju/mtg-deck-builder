"""CLI `mtg`: sincroniza e consulta a base local de cartas."""

import argparse
import json
import random
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

from . import (advisor, analysis, archetypes, arena_history, arena_log, arena_match, collection, companion, db,
               decklist, draft, draft_pick, draft_sim, edhrec, formats, meta, overlay, query, scryfall)


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
    if getattr(args, "set", None):
        decklist.resolve(conn, deck)
        sc = decklist.set_count(conn, deck, args.set)
        data["set_count"] = sc
        minimum = args.min_set
        missing = [f"{c['qty']} {c['name']}" for c in sc["cards"] if not c["in_set"] and not c["land"]]
        lines.append(f"Cartas não terreno de {sc['set']} no deck principal: {sc['count']} de {sc['nonland']}"
                     + (f" (mínimo {minimum})" if minimum is not None else ""))
        if missing:
            lines.append(f"  não contam ({len(missing)} linhas): " + ", ".join(missing))
        if minimum is not None and sc["count"] < minimum:
            errors.append(f"A tarefa pede pelo menos {minimum} cards não terrenos de {sc['set']} "
                          f"no deck principal; a lista tem {sc['count']}.")
            data["valid"] = False
    lines += [f"ERRO: {e}" for e in errors] + [f"aviso: {w}" for w in warnings]
    lines.append("Lista válida." if not errors else f"Lista inválida ({len(errors)} problemas).")
    _emit(args, data, lines)
    if errors:
        sys.exit(1)


def cmd_deck_setcount(args):
    conn = db.connect(readonly=True)
    deck = _read_deck(args.file)
    decklist.resolve(conn, deck)
    sc = decklist.set_count(conn, deck, args.set)
    lines = []
    for c in sc["cards"]:
        tag = "terreno" if c["land"] else (sc["set"].upper() if c["in_set"] else "não conta")
        sets = ", ".join(c["sets"][:8]) + (" ..." if len(c["sets"]) > 8 else "")
        lines.append(f"{tag:>10}  {c['qty']} {c['name']}  [{sets or 'carta não encontrada'}]")
    lines.append(f"Total de cartas não terreno de {sc['set']}: {sc['count']} de {sc['nonland']}")
    _emit(args, sc, lines)


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
                                   decks_dir=args.decks, url=args.url, collected=args.date,
                                   note=args.note)
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


# --- spec 010: assistente de draft -----------------------------------------------------

def _ratings(conn, set_code, mode, allow_update=True, day=None, log=print):
    """Fontes do motor de picks: snapshot do 17Lands (do dia pedido, ou o mais recente,
    renovado se tiver mais de 24 h e a rede permitir), Untapped e Draftsim quando existirem."""
    snapshot = draft.cached(set_code, mode, day)
    if day is None and allow_update:
        fresh = snapshot and (datetime.now() - datetime.fromisoformat(snapshot["collected_at"])
                              < timedelta(hours=draft.MAX_AGE_HOURS))
        if not fresh:
            try:
                snapshot = draft.update(conn, set_code, mode)
            except RuntimeError as error:
                log(f"17Lands indisponível ({error}). "
                    + ("Usando o snapshot guardado." if snapshot else "Sem dados de partidas: notas teóricas."))
    return draft_pick.Ratings(snapshot, draft.untapped_ratings(set_code, mode), draft.draftsim_ratings(set_code))


def _pack_cards(args):
    cards = list(args.cards)
    if getattr(args, "file", None):
        cards += [e.name for e in _read_deck(args.file).entries()]
    return cards


def cmd_draft_pick(args):
    conn = db.connect(readonly=True)
    info = draft.find_set(conn, args.set)
    ratings = _ratings(conn, info["code"], args.mode, allow_update=not args.offline, day=args.snapshot)
    engine = draft_pick.Engine(conn, ratings, info["code"], args.mode)
    if args.state and Path(args.state).exists():
        state = draft_pick.DraftState.load(args.state)
    else:
        state = draft_pick.DraftState(info["code"], args.mode, snapshot=(ratings.snapshot or {}).get("collected_at"))
    if args.picked:
        state.add_picks(args.picked)
    pack, pick = (args.pack, args.pick) if args.pack and args.pick else state.next_position()
    cards = _pack_cards(args)
    if not cards:
        sys.exit("Informe as cartas do pacote (nomes) ou --file.")
    result = engine.rank(state, pack, pick, cards)
    if args.state:
        state.record_pack(pack, pick, cards, result["cartas"])
        state.save(args.state)
    _emit(args, result, [draft_pick.format_ranking(result, title=f"{info['name']} · ", sources=ratings.describe())])


class _DraftSession:
    """Estado do acompanhamento ao vivo: resolve as cartas, pontua cada pacote, grava o
    estado e devolve o texto a mostrar."""

    def __init__(self, conn, arena, set_code=None, mode=None, state_path=None, offline=False, day=None, log=print):
        self.conn, self.arena, self.log = conn, arena, log
        self.set_code, self.mode, self.day, self.offline = set_code, mode, day, offline
        self.state_path = Path(state_path) if state_path else None
        self.state = draft_pick.DraftState.load(self.state_path) if self.state_path and self.state_path.exists() else None
        self.engine, self.ratings = None, None
        self.text = "aguardando um draft no Arena... (entre no evento e abra o primeiro pacote)"
        self.seen = set()
        self.events = 0

    def resolve(self, ids):
        if self.arena is not None:
            return self.arena.resolve(self.conn, ids)
        return arena_log.resolve_by_arena_id(self.conn, ids)

    def ensure_engine(self, set_code=None, mode=None, cards=None):
        set_code = self.set_code or set_code
        if set_code is None and cards:
            codes = [c["set"] for c in cards if c.get("set")]
            set_code = max(set(codes), key=codes.count) if codes else None
        if set_code is None:
            return False
        mode = self.mode or mode or "premier"
        if self.engine is None or self.engine.set_code != set_code or self.engine.mode != mode:
            info = draft.find_set(self.conn, set_code)
            self.ratings = _ratings(self.conn, info["code"], mode, allow_update=not self.offline, day=self.day,
                                    log=self.log)
            self.engine = draft_pick.Engine(self.conn, self.ratings, info["code"], mode)
            if self.state is None or self.state.set_code != info["code"]:
                self.state = draft_pick.DraftState(info["code"], mode, snapshot=(self.ratings.snapshot or {}).get("collected_at"))
            self.state.mode = mode
            self.log(f"coleção {info['name']} ({info['code']}), modo {mode}; dados: {self.ratings.describe()}")
        return True

    def save(self):
        if self.state is None:
            return
        if self.state_path is None:
            self.state_path = draft_pick.DraftState.default_path(self.state.set_code, self.state.mode, self.state.event)
        self.state.save(self.state_path)

    def handle(self, event):
        kind = event["type"]
        self.events += 1
        if kind == "join":
            if self.engine is not None and self.state is not None and self.state.event == event.get("event"):
                return None                      # pedido e resposta do mesmo evento
            mode, set_code = arena_log.parse_event_name(event.get("event"))
            if self.ensure_engine(set_code, mode):
                self.state.event = event.get("event")
                self.text = f"entrou em {event['event']} · {self.ratings.describe()}\naguardando o primeiro pacote..."
            return self.text
        if kind in ("pack", "pack_and_pick"):
            key = (event["pack"], event["pick"], tuple(event["cards"]))
            if key in self.seen:
                return None
            self.seen.add(key)
            cards = self.resolve(event["cards"])
            mode, set_code = arena_log.parse_event_name(event.get("event"))
            if not self.ensure_engine(set_code, mode, cards):
                self.text = "pacote recebido, mas não sei a coleção: rode com --set <código>."
                return self.text
            if event.get("event"):
                self.state.event = event["event"]
            result = self.engine.rank(self.state, event["pack"], event["pick"], cards)
            self.state.record_pack(event["pack"], event["pick"], [c["name"] for c in cards], result["cartas"])
            unresolved = [c["grp"] for c in cards if c["card"] is None]
            note = f"\n! {len(unresolved)} carta(s) sem nome na base: {unresolved}" if unresolved else ""
            self.text = draft_pick.format_ranking(result, sources=self.ratings.describe()) + note
            if kind == "pack_and_pick":
                picked = self.resolve([event["card"]])[0]["name"]
                self.state.record_pick(event["pack"], event["pick"], picked)
                self.text += f"\n✔ pick registrado (mensagem combinada, chegou após a escolha): {picked}"
            self.save()
            return self.text
        if kind == "pick":
            if self.state is None or event.get("card") is None:
                return None
            name = self.resolve([event["card"]])[0]["name"]
            self.state.record_pick(event["pack"], event["pick"], name)
            self.save()
            self.text += f"\n✔ pick registrado: {name}  (pool: {len(self.state.picked_names())})"
            return self.text
        if kind == "complete":
            if self.state is None:
                return None
            self.save()
            pool = self.state.picked_names()
            self.text = (f"draft encerrado: {len(pool)} cartas no pool · estado em {self.state_path}\n"
                         f"próximo passo: mtg draft pool \"{self.state_path}\" e a seção C da skill draft")
            return self.text
        if kind == "unknown":
            self.log(f"[linha de draft não reconhecida] {event['header']} chaves={event['keys']}")
        return None


def _preflight(args, log_path, arena_db):
    lines = []
    if log_path:
        enabled = arena_log.detailed_logs_enabled(log_path)
        status = {True: "ligada", False: "DESLIGADA (ligue em Opções > Conta > Detailed Logs)", None: "não informada no log"}[enabled]
        lines.append(f"log: {log_path} ({log_path.stat().st_size // 1024} KB) · Detailed Logs: {status}")
    else:
        lines.append("log: NÃO ENCONTRADO (informe --log <caminho do Player.log>)")
    lines.append(f"base do Arena: {arena_db or 'NÃO ENCONTRADA (informe --arena-dir); cairá no arena_id do Scryfall'}")
    if args.set:
        conn = db.connect(readonly=True)
        info = draft.find_set(conn, args.set)
        ratings = _ratings(conn, info["code"], args.mode or "premier", allow_update=not args.offline, day=args.snapshot)
        lines.append(f"coleção {info['name']} ({info['code']}): {ratings.describe()}")
    else:
        lines.append("coleção: será lida do nome do evento no log (ou informe --set)")
    return lines


def cmd_draft_watch(args):
    log_path = Path(args.file) if args.file else arena_log.find_log(args.log)
    arena_db = arena_log.find_arena_db(args.arena_dir)
    for line in _preflight(args, log_path, arena_db):
        print(line)
    if args.check:
        return
    if log_path is None:
        sys.exit("Sem log para ler.")
    conn = db.connect(readonly=True)
    arena = arena_log.ArenaCards(arena_db) if arena_db else None
    session = _DraftSession(conn, arena, args.set, args.mode, args.state, offline=args.offline, day=args.snapshot)
    follower = arena_log.LogFollower(log_path, from_start=bool(args.file) or args.from_start)

    if args.file:
        packs = picks = 0
        for event in follower.finish():
            text = session.handle(event)
            if event["type"] in ("pack", "pack_and_pick"):
                packs += 1
                picks += event["type"] == "pack_and_pick"
                print("\n" + text)
            elif event["type"] == "pick":
                picks += 1
            elif text:
                print("\n" + text)
        print(f"\nreprodução: {packs} pacotes, {picks} picks, {session.events} eventos de draft, "
              f"{follower.parser.unparsed} entradas de draft não decodificadas")
        if session.state:
            print(f"pool ({len(session.state.picked_names())}): " + ", ".join(session.state.picked_names()))
        return

    def poll():
        changed = None
        for event in follower.poll():
            text = session.handle(event)
            if text:
                changed = text
        return changed

    print("acompanhando o log... (Ctrl+C para sair)")
    if args.window:
        overlay.run_window(poll, title="Draft — assistente")
        return
    try:
        while True:
            text = poll()
            if text:
                print("\n" + datetime.now().strftime("%H:%M:%S") + "\n" + text)
            time.sleep(0.5)
    except KeyboardInterrupt:
        session.save()
        if session.state_path:
            print(f"\nestado salvo em {session.state_path}")


def cmd_draft_synergy(args):
    """Arquétipos da coleção: cartas marcadas por par e se a marcação tem sinal nos dados."""
    conn = db.connect(readonly=True)
    info = draft.find_set(conn, args.set)
    data = archetypes.load(info["code"])
    if not data:
        sys.exit(f"Sem arquivo de arquétipos para {info['code']} (src/mtg_builder/archetypes/{info['code']}.json).")
    ratings = _ratings(conn, info["code"], args.mode, allow_update=not args.offline, day=args.snapshot)
    report = archetypes.report(conn, info["code"], ratings, archetypes.Tagger(data), top=args.limit)
    _emit(args, report, [archetypes.format_report(report)])


def cmd_draft_pool(args):
    state = draft_pick.DraftState.load(args.state)
    names = state.picked_names()
    lines = [f"{state.set_code} · {state.mode} · {state.event or ''} · {len(names)} cartas"]
    counts = {}
    for name in names:
        shown = name.split(" // ")[0] if args.to == "arena" else name
        counts[shown] = counts.get(shown, 0) + 1
    lines += [f"{qty} {name}" for name, qty in counts.items()]
    _emit(args, {"set": state.set_code, "mode": state.mode, "pool": names}, lines)


def cmd_draft_sim(args):
    conn = db.connect(readonly=True)
    info = draft.find_set(conn, args.set)
    ratings = _ratings(conn, info["code"], args.mode, allow_update=not args.offline, day=args.snapshot)
    engine = draft_pick.Engine(conn, ratings, info["code"], args.mode)
    arena = None
    arena_db = arena_log.find_arena_db(args.arena_dir)
    if arena_db:
        try:
            arena = arena_log.ArenaCards(arena_db)
        except Exception:  # base do cliente é opcional aqui
            arena = None
    pools, basis = draft_sim.card_pools(conn, info["code"], ratings.snapshot, arena)
    try:
        booster = draft_sim.load_booster(info["code"], args.booster)
    except RuntimeError as error:
        sys.exit(str(error))
    rng = random.Random(args.seed)
    print(f"{info['name']} ({info['code']}) · {args.mode} · dados: {ratings.describe()}")
    print(f"cartas draftáveis ({basis}): " + ", ".join(f"{k} {len(v)}" for k, v in pools.items() if v))
    print(f"colação: {booster['name']}" + (" [genérica]" if booster.get("generic") else "") + f" — {booster['source']}")

    if args.auto:
        pairs, rarities, total = {}, {}, 0
        for _ in range(args.auto):
            states = draft_sim.run_table(conn, engine, info["code"], rng, pools, booster)
            for seat in draft_sim.summarize(engine, states):
                pairs[seat["pair"]] = pairs.get(seat["pair"], 0) + 1
                for rarity, n in seat["rarities"].items():
                    rarities[rarity] = rarities.get(rarity, 0) + n
                total += 1
        lines = [f"{args.auto} mesas, {total} drafters (só bots, com ruído e preferência de cor):",
                 "pares mais escolhidos: " + ", ".join(f"{p or '?'} {n}" for p, n in sorted(pairs.items(), key=lambda kv: -kv[1])),
                 "raridades por pool de 42: " + ", ".join(f"{r} {n / total:.1f}" for r, n in sorted(rarities.items()))]
        _emit(args, {"pairs": pairs, "rarities": rarities, "drafters": total}, lines)
        return

    def choose(result, names):
        print("\n" + draft_pick.format_ranking(result))
        while True:
            answer = input("pick (número, nome, Enter = 1º, q = sair): ").strip()
            if answer.lower() == "q":
                raise KeyboardInterrupt
            if not answer:
                return result["cartas"][0]["name"]
            if answer.isdigit() and 1 <= int(answer) <= len(result["cartas"]):
                return result["cartas"][int(answer) - 1]["name"]
            match = [n for n in names if decklist._key(n).startswith(decklist._key(answer))]
            if len(match) == 1:
                return match[0]
            print("não entendi; tente o número da linha")

    try:
        states = draft_sim.run_table(conn, engine, info["code"], rng, pools, booster, human_seat=0, choose=choose)
    except KeyboardInterrupt:
        print("\nsimulação interrompida")
        return
    human = states[0]
    path = draft_pick.DraftState.default_path(info["code"], args.mode, "simulado")
    human.save(path)
    summary = draft_sim.summarize(engine, states)
    print("\nmesa: " + ", ".join(f"lugar {s['seat']} {s['pair'] or '?'}" for s in summary))
    print(f"seu pool ({len(human.picked_names())}): " + ", ".join(human.picked_names()))
    print(f"estado salvo em {path} — monte o deck com a seção C da skill draft")


def cmd_arena_watch(args):
    """Leitor de partidas: teste do log em um jogo comum, sem gastar fichas."""
    log_path = Path(args.file) if args.file else arena_log.find_log(args.log)
    arena_db = arena_log.find_arena_db(args.arena_dir)
    for line in _preflight(args, log_path, arena_db):
        print(line)
    if log_path is None:
        sys.exit("Sem log para ler.")
    conn = db.connect(readonly=True)
    arena = arena_log.ArenaCards(arena_db) if arena_db else None
    session = arena_match.MatchSession(conn, arena, history_path=arena_history.PATH, collection_path=collection.PATH)
    follower = arena_log.LogFollower(log_path, from_start=bool(args.file) or args.from_start,
                                     classifier=arena_match.classify_match)
    if args.file:
        count = 0
        for event in follower.finish():
            count += 1
            text = session.handle(event)
            if text:
                print(text)
        print(f"\nreprodução: {count} eventos de partida reconhecidos")
        if session.tracker is not None:
            print("\n" + session.board())
        return
    print("acompanhando o log... (Ctrl+C para sair)")
    lines = []

    def poll():
        changed = False
        for event in follower.poll():
            text = session.handle(event)
            if text:
                lines.append(datetime.now().strftime("%H:%M:%S ") + text)
                changed = True
        return "\n".join(lines[-40:]) if changed else None

    if args.window:
        overlay.run_window(poll, title="Arena — partida")
        return
    try:
        while True:
            text = poll()
            if text:
                print(lines[-1])
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass


def cmd_arena_history(args):
    """Partidas conhecidas (logs que ainda existem + o que o Oráculo acumulou), por deck."""
    paths = [Path(p) for p in args.log] if args.log else arena_history.default_logs()
    scanned = {"rows": [], "rank": None, "inventory": None, "decks": []}
    if not args.no_scan and paths:
        conn = db.connect(readonly=True)
        arena_db = arena_log.find_arena_db(args.arena_dir)
        arena = arena_log.ArenaCards(arena_db) if arena_db else None
        scanned = arena_history.scan(paths, conn, arena)
        added = sum(arena_history.append(row, arena_history.PATH) for row in scanned["rows"])
        if added:
            print(f"{added} partida(s) nova(s) guardada(s) em {arena_history.PATH}")
    rows = arena_history.merge(arena_history.load(arena_history.PATH), scanned["rows"])
    stats = arena_history.summary(rows, args.deck)
    text = arena_history.format_history(rows, stats, scanned["rank"], scanned["inventory"], args.deck, args.limit)
    if args.decks and scanned["decks"]:
        text += "\n\ndecks na conta (nome · formato · última partida):\n" + "\n".join(
            f"  {d['name']:<32} {d.get('format') or '?':<22} {(d.get('last_played') or '')[:10]}"
            for d in sorted(scanned["decks"], key=lambda d: d.get("last_played") or "", reverse=True))
    _emit(args, {"matches": rows, "summary": stats, "rank": scanned["rank"], "inventory": scanned["inventory"],
                 "decks": scanned["decks"]}, [text])


def cmd_arena_collection(args):
    """Coleção aproximada: decks salvos (resposta de abertura do Arena) e, depois, boosters."""
    conn = db.connect(readonly=True)
    arena_db = arena_log.find_arena_db(args.arena_dir)
    arena = arena_log.ArenaCards(arena_db) if arena_db else None
    data = collection.load(collection.PATH)
    if not args.no_scan:
        paths = [Path(p) for p in args.log] if args.log else arena_history.default_logs()
        found = 0
        for path in paths:
            follower = arena_log.LogFollower(path, from_start=True, classifier=arena_match.classify_match)
            for event in follower.finish():
                if event["type"] == "inventory" and event.get("deck_cards"):
                    session = arena_match.MatchSession(conn, arena)
                    collection.update(data, event["deck_cards"], "decks", session.resolve)
                    found += 1
        if found:
            collection.save(data, collection.PATH)
            print(f"decks salvos lidos em {found} abertura(s) do Arena; coleção gravada em {collection.PATH}")
        else:
            print("nenhuma resposta de abertura do Arena nos logs (abra o Arena uma vez e repita)")
    if args.find:
        for name in args.find:
            print(f"{name}: {collection.owned(data, name)} cópia(s) na coleção aproximada")
        return
    _emit(args, collection.summary(data, args.set), [collection.format_summary(data, args.set)])


def cmd_arena_advise(args):
    """Conselheiro local sobre um registro de partida (teste fora do jogo, spec 012)."""
    try:
        record = json.loads(Path(args.record).read_text("utf-8"))
    except (OSError, ValueError) as error:
        sys.exit(f"Não consegui ler o registro: {error}")
    conn = db.connect(readonly=True)
    try:
        context, turn, deck_file = advisor.context_from_record(record, args.turn, conn, deck_file=args.deck)
    except RuntimeError as error:
        sys.exit(str(error))
    print(f"registro: {args.record} · turno {turn} · plano do deck: {deck_file or 'não encontrado em decks/'}")
    if args.dry_run:
        print("\n" + context)
        return
    try:
        client = advisor.make_advisor(args.api, args.model, args.url)
    except RuntimeError as error:
        sys.exit(str(error))
    if not client.available():
        hint = ("Instale o Ollama (https://ollama.com) e rode `ollama pull <modelo>`" if args.api == "ollama"
                else "Suba o LocalAI (ou outro servidor compatível com a API da OpenAI) e confira a porta")
        sys.exit(f"Servidor não responde em {client.url}. {hint}; `--dry-run` mostra o contexto sem chamar o modelo.")
    models = client.models()
    if models and args.model not in models and not any(m.startswith(args.model) for m in models):
        sys.exit(f"Modelo {args.model} não está disponível. No servidor: {', '.join(models)}.")
    answer = client.ask(context)
    _emit(args, answer, [advisor.format_answer(answer)])


def cmd_arena_companion(args):
    """Oráculo: espera o Arena abrir e mostra a janela com draft e partida."""
    if args.uninstall:
        removed = companion.uninstall()
        print("tarefa removida" if removed else "não havia tarefa (processos soltos foram encerrados)")
        return
    if args.stop:
        print(f"{companion.stop()} processo(s) encerrado(s)")
        return
    if args.install or args.start:
        try:
            if args.install:
                companion.install()
                print(f"tarefa agendada \"{companion.TASK}\" criada: dispara no login e roda fora do terminal; "
                      f"registro em {companion.LOG_FILE}")
            if not (args.install and args.no_start):
                companion.stop()
                companion.start()
                print(f"{companion.NAME} iniciado; a janela aparece quando o Arena estiver aberto "
                      "(fecha com o Arena e volta quando ele reabrir)")
        except RuntimeError as error:
            sys.exit(str(error))
        return
    if args.status:
        state = companion.task_state()
        print(f"tarefa agendada: {state or 'não instalada'} · instâncias do Oráculo: {companion.running_instances()}")
        print(f"Arena: {'aberto' if companion.arena_running() else 'fechado'}")
        if companion.LOG_FILE.exists():
            tail = companion.LOG_FILE.read_text("utf-8", errors="replace").splitlines()[-8:]
            print("últimas linhas do registro:\n  " + "\n  ".join(tail))
        return

    log = companion.configure_logging()
    conn = db.connect(readonly=True)
    arena_db = arena_log.find_arena_db(args.arena_dir)
    arena = arena_log.ArenaCards(arena_db) if arena_db else None
    if arena is None:
        log.warning("base de cartas do Arena não encontrada; usando arena_id do Scryfall")

    def make_sessions():
        draft_session = _DraftSession(conn, arena, args.set, args.mode, None, offline=args.offline, log=log.info)
        return draft_session, arena_match.MatchSession(conn, arena, history_path=arena_history.PATH,
                                                       collection_path=collection.PATH)

    companion.run(make_sessions, log, once=args.once)


def main(argv=None):
    if sys.stdout is not None:              # sob pythonw (Oráculo pela tarefa agendada) não há console
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
    p.add_argument("--set", help="conta as cartas não terreno desta coleção (pela impressão), ex.: fra")
    p.add_argument("--min-set", type=int, help="mínimo exigido de cartas não terreno da coleção de --set; "
                   "abaixo disso a lista é reprovada (tarefas do Arena)")
    p.set_defaults(func=cmd_deck_validate)

    p = deck_sub.add_parser("setcount", help="quais cartas da lista têm impressão em uma coleção")
    p.add_argument("file", help=file_help)
    p.add_argument("--set", required=True, help="código da coleção, ex.: fra")
    p.set_defaults(func=cmd_deck_setcount)

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
    p.add_argument("--note", help="ressalvas sobre os dados (recorte, filtros, o que 'share' mede)")
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

    def sources_args(parser_):
        parser_.add_argument("--snapshot", help="data do snapshot do 17Lands (AAAA-MM-DD); padrão: o mais recente")
        parser_.add_argument("--offline", action="store_true", help="não tenta renovar o snapshot")

    p = draft_parser("pick", "pontua as cartas de um pacote dado o que já foi escolhido", cmd_draft_pick)
    p.add_argument("cards", nargs="*", help="cartas do pacote")
    p.add_argument("--file", help="arquivo com as cartas do pacote")
    p.add_argument("--pack", type=int, help="número do pacote (1 a 3)")
    p.add_argument("--pick", type=int, help="número do pick (1 a 14)")
    p.add_argument("--picked", nargs="*", default=[], help="cartas já escolhidas (sem --state)")
    p.add_argument("--state", help="arquivo de estado do draft (lê, acumula e grava)")
    sources_args(p)

    p = draft_sub.add_parser("watch", help="acompanha um draft ao vivo pelo Player.log do Arena")
    p.add_argument("--set", help="código da coleção (padrão: lido do nome do evento)")
    p.add_argument("--mode", choices=tuple(draft.MODES), help="padrão: lido do nome do evento")
    p.add_argument("--log", help="caminho do Player.log (padrão: o do Windows)")
    p.add_argument("--file", help="reproduz um log gravado do começo ao fim, sem esperar")
    p.add_argument("--from-start", action="store_true", help="lê o log desde o começo (draft já em andamento)")
    p.add_argument("--arena-dir", help="pasta de instalação do Arena (base de cartas)")
    p.add_argument("--state", help="arquivo de estado (padrão: data/drafts/<data>-<evento>.json)")
    p.add_argument("--window", action="store_true", help="janela flutuante sempre no topo, em vez do terminal")
    p.add_argument("--check", action="store_true", help="só confere log, base do Arena e dados, e sai")
    sources_args(p)
    p.set_defaults(func=cmd_draft_watch)

    p = draft_parser("synergy", "arquétipos da coleção: cartas marcadas por par e o sinal nos dados", cmd_draft_synergy)
    p.add_argument("--limit", type=int, default=8, help="cartas por arquétipo")
    sources_args(p)

    p = draft_sub.add_parser("pool", help="lista o pool de um estado de draft")
    p.add_argument("state", help="arquivo de estado")
    p.add_argument("--to", choices=["text", "arena"], default="text")
    p.set_defaults(func=cmd_draft_pool)

    p = draft_parser("sim", "simula um draft contra sete bots (treino sem gastar fichas)", cmd_draft_sim)
    p.add_argument("--auto", type=int, help="N mesas só de bots, com resumo")
    p.add_argument("--seed", type=int, help="semente do sorteio")
    p.add_argument("--booster", help="perfil de colação (ex.: paper = Play Booster de papel); padrão: o do Arena")
    p.add_argument("--arena-dir", help="pasta de instalação do Arena (lista de cartas draftáveis)")
    sources_args(p)

    arena_cmd = sub.add_parser("arena", help="leitura do cliente do Arena (log de partidas)")
    arena_sub = arena_cmd.add_subparsers(dest="arena_command", required=True)
    p = arena_sub.add_parser("watch", help="mostra deck enviado, oponente, turnos e resultado de uma partida")
    p.add_argument("--log", help="caminho do Player.log")
    p.add_argument("--file", help="reproduz um log gravado")
    p.add_argument("--from-start", action="store_true")
    p.add_argument("--arena-dir", help="pasta de instalação do Arena")
    p.add_argument("--window", action="store_true", help="janela flutuante sempre no topo")
    p.add_argument("--set", help=argparse.SUPPRESS)
    p.add_argument("--mode", help=argparse.SUPPRESS)
    p.add_argument("--snapshot", help=argparse.SUPPRESS)
    p.add_argument("--offline", action="store_true", help=argparse.SUPPRESS)
    p.set_defaults(func=cmd_arena_watch)

    p = arena_sub.add_parser("history", help="partidas conhecidas por deck, rank da temporada e cofre")
    p.add_argument("--deck", help="só este deck (nome no Arena)")
    p.add_argument("--log", nargs="*", help="logs a varrer (padrão: Player-prev.log e Player.log)")
    p.add_argument("--no-scan", action="store_true", help="só o que já está em data/matches.jsonl")
    p.add_argument("--decks", action="store_true", help="lista os decks da conta com a última partida")
    p.add_argument("--limit", type=int, default=30, help="partidas mostradas")
    p.add_argument("--arena-dir", help="pasta de instalação do Arena")
    p.set_defaults(func=cmd_arena_history)

    p = arena_sub.add_parser("collection", help="coleção aproximada (decks salvos, boosters) em data/collection.json")
    p.add_argument("--set", help="lista as cartas de uma coleção (código)")
    p.add_argument("--find", nargs="*", help="quantas cópias destas cartas há na coleção aproximada")
    p.add_argument("--log", nargs="*", help="logs a varrer (padrão: Player-prev.log e Player.log)")
    p.add_argument("--no-scan", action="store_true", help="só o que já está em data/collection.json")
    p.add_argument("--arena-dir", help="pasta de instalação do Arena")
    p.set_defaults(func=cmd_arena_collection)

    p = arena_sub.add_parser("advise", help="conselheiro local (Ollama) sobre um registro de partida gravado")
    p.add_argument("record", help="arquivo .json em data/games/")
    p.add_argument("--turn", type=int, help="turno seu a analisar (padrão: o último com instantâneo)")
    p.add_argument("--api", choices=sorted(advisor.APIS), default="ollama",
                   help="ollama (API nativa, porta 11434) ou openai (LocalAI na 8080, LM Studio, llama.cpp, Ollama em /v1)")
    p.add_argument("--model", default=advisor.DEFAULT_MODEL, help=f"nome do modelo no servidor (padrão {advisor.DEFAULT_MODEL})")
    p.add_argument("--url", help="servidor; padrão http://localhost:11434 (ollama) ou http://localhost:8080 (openai)")
    p.add_argument("--deck", help="arquivo do deck em decks/ (padrão: o de maior coincidência com o deck enviado)")
    p.add_argument("--dry-run", action="store_true", help="só mostra o contexto que o modelo receberia")
    p.set_defaults(func=cmd_arena_advise)

    p = arena_sub.add_parser("companion", help="Oráculo: abre a janela sozinho quando o Arena abre (draft e partida)")
    p.add_argument("--install", action="store_true", help="cria a tarefa agendada (login) e inicia agora")
    p.add_argument("--start", action="store_true", help="inicia a tarefa agora, fora do terminal")
    p.add_argument("--stop", action="store_true", help="encerra o Oráculo")
    p.add_argument("--no-start", action="store_true", help="com --install: só cria a tarefa")
    p.add_argument("--uninstall", action="store_true", help="encerra e remove a tarefa")
    p.add_argument("--status", action="store_true", help="tarefa, processos, Arena e últimas linhas do registro")
    p.add_argument("--once", action="store_true", help="encerra quando a janela fechar (teste)")
    p.add_argument("--set", help="código da coleção do draft (padrão: lido do evento)")
    p.add_argument("--mode", choices=tuple(draft.MODES), help="padrão: lido do evento")
    p.add_argument("--arena-dir", help="pasta de instalação do Arena")
    p.add_argument("--offline", action="store_true", help="não renova o snapshot do 17Lands")
    p.set_defaults(func=cmd_arena_companion)

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
