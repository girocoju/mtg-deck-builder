"""Leitura de partidas no `Player.log` do Arena: deck enviado, oponente e, pelo rastreador
de `arena_game.py`, o estado inteiro do jogo (mão, campos, cemitérios, exílio, pilha,
turnos, ataques, dano, vida, resultado). Serve de teste do leitor de log sem gastar
fichas, alimenta a janela do Oráculo e grava cada partida em `data/games/` (spec 011).

Mensagens usadas (vistas no log do usuário em 2026-11-07):

- `authenticateResponse` → `clientId` (quem é "você");
- `EventSetDeckV3` (pedido, com `request` embutido) → `EventName`, `Summary.Name`,
  `Deck.MainDeck` [{cardId, quantity}];
- `matchGameRoomStateChangedEvent` → `gameRoomInfo.gameRoomConfig.reservedPlayers`
  (userId, playerName, systemSeatId, teamId, eventId), `stateType` (Playing,
  MatchCompleted) e `finalMatchResult.resultList` (scope, winningTeamId);
- `greToClientEvent.greToClientMessages[].gameStateMessage` → tudo o que o rastreador lê.
"""

import json
import re
from datetime import datetime
from pathlib import Path

from . import arena_game, arena_history, arena_log, collection, db


def _find_deck(obj, depth=0):
    if depth > 3 or not isinstance(obj, dict):
        return None
    if isinstance(obj.get("MainDeck"), list):
        return obj
    for key in ("Deck", "CourseDeck", "deck"):
        found = _find_deck(obj.get(key), depth + 1)
        if found:
            return found
    return None


def _cards(entries):
    out = []
    for entry in entries or []:
        try:
            out.append((int(entry["cardId"]), int(entry.get("quantity", 1))))
        except (KeyError, TypeError, ValueError):
            continue
    return out


def classify_match(header, obj):
    if not isinstance(obj, dict):
        return None
    marker = header.lower()
    auth = obj.get("authenticateResponse")
    if isinstance(auth, dict):
        return {"type": "login", "user": auth.get("clientId"), "name": auth.get("screenName")}
    room = obj.get("matchGameRoomStateChangedEvent")
    if isinstance(room, dict):
        info = room.get("gameRoomInfo") or {}
        config = info.get("gameRoomConfig") or {}
        players = [{"user": p.get("userId"), "name": p.get("playerName"), "seat": p.get("systemSeatId"),
                    "team": p.get("teamId"), "event": p.get("eventId"), "platform": p.get("platformId")}
                   for p in config.get("reservedPlayers") or []]
        results = [{"scope": r.get("scope"), "winner": r.get("winningTeamId"), "reason": r.get("reason")}
                   for r in (info.get("finalMatchResult") or {}).get("resultList") or []]
        return {"type": "room", "state": (info.get("stateType") or "").replace("MatchGameRoomStateType_", ""),
                "match_id": config.get("matchId"), "players": players, "results": results}
    gre = obj.get("greToClientEvent")
    if isinstance(gre, dict):
        messages = [m["gameStateMessage"] for m in gre.get("greToClientMessages") or []
                    if isinstance(m, dict) and isinstance(m.get("gameStateMessage"), dict)]
        return {"type": "game_state", "messages": messages} if messages else None
    if "setdeck" in marker.replace("_", "") and obj.get("EventName"):
        deck = _find_deck(obj)
        if deck:
            return {"type": "deck", "event": obj.get("EventName"), "name": (obj.get("Summary") or {}).get("Name"),
                    "main": _cards(deck.get("MainDeck")), "sideboard": _cards(deck.get("Sideboard")),
                    "commander": _cards(deck.get("CommandZone") or deck.get("Commander"))}
    if "constructedSeasonOrdinal" in obj:
        return {"type": "rank", "season": obj.get("constructedSeasonOrdinal"), "class": obj.get("constructedClass"),
                "level": obj.get("constructedLevel"), "won": obj.get("constructedMatchesWon"),
                "lost": obj.get("constructedMatchesLost"), "limited_class": obj.get("limitedClass"),
                "limited_level": obj.get("limitedLevel")}
    inventory = obj.get("InventoryInfo")
    if isinstance(inventory, dict) and "Gold" in inventory:
        vault = inventory.get("TotalVaultProgress")
        return {"type": "inventory", "gold": inventory.get("Gold"), "gems": inventory.get("Gems"),
                "vault": vault, "vault_pct": round(vault / 10, 1) if isinstance(vault, (int, float)) else None,
                "wildcards": {"common": inventory.get("WildCardCommons"), "uncommon": inventory.get("WildCardUnCommons"),
                              "rare": inventory.get("WildCardRares"), "mythic": inventory.get("WildCardMythics")},
                "tokens": {k: v for k, v in (inventory.get("CustomTokens") or {}).items() if isinstance(v, int)},
                "deck_cards": collection.cards_in_decks(obj.get("DecksInternal")) if obj.get("DecksInternal") else None}
    summaries = obj.get("Summaries")
    if isinstance(summaries, list) and summaries and isinstance(summaries[0], dict) and "Name" in summaries[0]:
        decks = []
        for item in summaries:
            attributes = {a.get("name"): (a.get("value") or "").strip('"') for a in item.get("Attributes") or []}
            decks.append({"name": item.get("Name"), "format": attributes.get("Format"),
                          "last_played": attributes.get("LastPlayed"), "last_updated": attributes.get("LastUpdated")})
        return {"type": "decks", "decks": decks}
    return None


class MatchSession:
    """Transforma os eventos de partida em linhas de texto, mantém o rastreador do jogo e
    grava o registro de cada jogo em `records_dir` (padrão `data/games/`)."""

    def __init__(self, conn=None, arena=None, records_dir=None, history_path=None, save_records=True,
                 collection_path=None):
        self.conn, self.arena = conn, arena
        self.records_dir, self.history_path, self.save_records = records_dir, history_path, save_records
        self.collection_path = collection_path
        self.me, self.my_seat, self.players = None, None, []
        self.tracker = None
        self.event_name, self.deck, self.match_id, self.started_at = None, None, None, None
        self.rank, self.inventory, self.deck_list = None, None, []
        self.rows = []               # partidas concluídas nesta sessão (linhas do histórico)
        self.saved = []
        self._names = {}

    # --- nomes ------------------------------------------------------------------------------
    def resolve(self, ids):
        if self.arena is not None:
            return self.arena.resolve(self.conn, ids)
        if self.conn is not None:
            return arena_log.resolve_by_arena_id(self.conn, ids)
        return [{"grp": i, "name": f"#{i}", "card": None} for i in ids]

    def card_name(self, grp):
        if grp not in self._names:
            self._names[grp] = self.resolve([grp])[0]["name"]
        return self._names[grp]

    def seat_names(self):
        return {p["seat"]: p["name"] or f"lugar {p['seat']}" for p in self.players}

    def new_tracker(self):
        self.tracker = arena_game.GameTracker(self.card_name, self.my_seat, self.seat_names())
        return self.tracker

    def opponent_name(self):
        for player in self.players:
            if player["seat"] != self.my_seat:
                return player["name"] or "oponente"
        return "oponente"

    def match_deck(self):
        """O deck enviado para o evento desta partida. None quando o último deck visto foi de
        outro evento: o Oráculo fica aberto entre a Ladder e o draft, e o registro não pode
        herdar o deck anterior (aconteceu em 2026-11-09: quatro partidas de Premier Draft
        gravadas com o deck de Ladder)."""
        if not self.deck:
            return None
        if self.event_name and self.deck.get("event") and self.deck["event"] != self.event_name:
            return None
        return self.deck

    # --- eventos ----------------------------------------------------------------------------
    def handle(self, event):
        kind = event["type"]
        if kind == "login":
            self.me = event.get("user") or self.me
            return f"conta: {event.get('name') or self.me}"
        if kind == "deck":
            resolved = self.resolve([grp for grp, _q in event["main"]])
            total = sum(q for _g, q in event["main"])
            unknown = [r["grp"] for r in resolved if r["card"] is None]
            names = {}
            for (grp, qty), card in zip(event["main"], resolved):
                names[card["name"]] = names.get(card["name"], 0) + qty
            self.deck = {"event": event.get("event"), "name": event.get("name"), "cards": names}
            top = ", ".join(f"{q} {n}" for n, q in sorted(names.items(), key=lambda kv: -kv[1])[:6])
            tail = f" · {len(unknown)} sem nome na base ({unknown[:3]})" if unknown else " · todas resolvidas"
            return (f"deck enviado para {event.get('event')}: \"{event.get('name')}\" — {total} cartas{tail}\n"
                    f"   {top}, ...")
        if kind == "rank":
            self.rank = event
            return (f"ranqueada construída: {event.get('class')} {event.get('level')}, "
                    f"{event.get('won')}–{event.get('lost')} na temporada {event.get('season')}")
        if kind == "inventory":
            self.inventory = event
            wc = event["wildcards"]
            line = (f"cofre: {event.get('gold')} ouro · {event.get('gems')} gemas · curingas C{wc.get('common')} "
                    f"U{wc.get('uncommon')} R{wc.get('rare')} M{wc.get('mythic')}"
                    + (f" · baú {event['vault_pct']:.1f}%" if event.get("vault_pct") is not None else ""))
            if self.history_path:
                arena_history.append_inventory(event, Path(self.history_path).with_name("inventory.jsonl"))
            if event.get("deck_cards") and self.collection_path:
                data = collection.load(self.collection_path)
                changed = collection.update(data, event["deck_cards"], "decks", self.resolve)
                collection.save(data, self.collection_path)
                line += f"\ncoleção aproximada pelos decks salvos: {len(event['deck_cards'])} cartas distintas, {changed} atualizada(s)"
            return line
        if kind == "decks":
            self.deck_list = event["decks"]
            return f"{len(event['decks'])} decks na conta"
        if kind == "room":
            if event["players"]:
                self.players = event["players"]
                mine = next((p for p in self.players if p["user"] == self.me), None)
                self.my_seat = mine["seat"] if mine else self.my_seat
                self.event_name = self.players[0]["event"]
            if event["state"] == "Playing":
                self.new_tracker()
                self.match_id, self.started_at = event.get("match_id"), event.get("at")
                others = [p for p in self.players if p["seat"] != self.my_seat]
                versus = " × ".join(f"{p['name']} (lugar {p['seat']}, {p.get('platform') or '?'})" for p in others)
                deck = self.match_deck()
                tail = f' · deck "{deck["name"]}"' if deck and deck.get("name") else                     (" · deck deste evento não visto no log" if self.deck else "")
                return f"partida em {self.event_name or '?'}: você (lugar {self.my_seat}) × {versus}{tail}"
            if event["state"] == "MatchCompleted":
                mine = next((p for p in self.players if p["seat"] == self.my_seat), None)
                my_team = mine["team"] if mine else None
                parts, match_result = [], None
                for result in event["results"]:
                    scope = (result["scope"] or "").replace("MatchScope_", "").lower()
                    outcome = "?" if my_team is None else ("vitória" if result["winner"] == my_team else "derrota")
                    parts.append(f"{scope}: {outcome}")
                    if scope == "match":
                        match_result = outcome
                row = self.match_row(match_result or (parts[-1].split(": ")[1] if parts else None), event)
                self.rows.append(row)
                if self.history_path:
                    arena_history.append(row, self.history_path)
                saved = self.save_record()
                return "fim da partida — " + ", ".join(parts) + (f"\nregistro: {saved}" if saved else "")
            return f"sala: {event['state']}"
        if kind == "game_state":
            if self.tracker is None:
                self.new_tracker()
            lines = []
            for gsm in event["messages"]:
                game_before = self.tracker.game
                if game_before and (gsm.get("gameInfo") or {}).get("gameNumber") not in (None, game_before):
                    self.save_record()
                    self.new_tracker()
                lines += self.tracker.apply(gsm)
            if self.tracker.over:
                saved = self.save_record()
                if saved:
                    lines.append(f"registro: {saved}")
            return "\n".join(lines) if lines else None
        return None

    # --- visão e registro --------------------------------------------------------------------
    def match_row(self, result, event=None):
        """Linha do histórico (`data/matches.jsonl`)."""
        tracker = self.tracker
        return {"match_id": self.match_id or (event or {}).get("match_id"), "at": self.started_at or (event or {}).get("at"),
                "event": self.event_name, "deck": (self.match_deck() or {}).get("name"), "opponent": self.opponent_name(),
                "result": result, "turns": tracker.turn["number"] if tracker else None,
                "own_turns": tracker.own_turns.get(self.my_seat) if tracker else None,
                "life": {str(seat): total for seat, total in tracker.life.items()} if tracker else None}

    def board(self):
        if self.tracker is None:
            return "aguardando uma partida..."
        return self.tracker.board_text()

    def save_record(self):
        """Grava JSON e Markdown do jogo corrente (uma vez por jogo). Devolve o caminho ou None."""
        if not self.save_records or self.tracker is None or not self.tracker.events or self.tracker in self.saved:
            return None
        folder = self.records_dir or (db.DATA_DIR / "games")
        folder.mkdir(parents=True, exist_ok=True)
        opponent = re.sub(r"[^A-Za-z0-9_-]+", "", self.opponent_name()) or "oponente"
        stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
        base = folder / f"{stamp}-{self.event_name or 'partida'}-{opponent}-g{self.tracker.game or 1}"
        deck = self.match_deck()
        record = {"event": self.event_name, "opponent": self.opponent_name(), "deck": deck,
                  "recorded_at": datetime.now().isoformat(timespec="seconds"), **self.tracker.record()}
        base.with_suffix(".json").write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
        title = f"{self.event_name or 'Partida'} contra {self.opponent_name()}" + \
                (f" com \"{deck['name']}\"" if deck and deck.get("name") else "")
        base.with_suffix(".md").write_text(self.tracker.markdown(title), encoding="utf-8")
        self.saved.append(self.tracker)
        return base.with_suffix(".md")
