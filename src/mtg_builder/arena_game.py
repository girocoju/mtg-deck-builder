"""Rastreador do estado de uma partida (spec 011), a partir das `GameStateMessage` que o
Arena grava no `Player.log`: zonas, objetos (cartas, fichas, habilidades), vida, turno,
fase e passo, e as anotações que viram eventos legíveis ("você conjura X", "X causa 15
de dano em Y"). A mão do oponente chega só como contagem; a nossa, inteira.

Estrutura conferida na partida de 2026-11-07: uma mensagem `Full` (zonas e jogadores) e
depois `Diff`s com `gameObjects` (estado completo dos objetos que mudaram), `zones`
(lista de instâncias das zonas que mudaram; sem a lista = vazia), `annotations`,
`diffDeletedInstanceIds`, `turnInfo`, `players` e `gameInfo`. Quando uma carta troca de
zona ela ganha outra instância, anunciada por `AnnotationType_ObjectIdChanged`.
"""

import json
from collections import Counter
from datetime import datetime

ZONE_NAMES = {
    "ZoneType_Hand": "mão", "ZoneType_Battlefield": "campo", "ZoneType_Graveyard": "cemitério",
    "ZoneType_Exile": "exílio", "ZoneType_Stack": "pilha", "ZoneType_Library": "biblioteca",
    "ZoneType_Limbo": "limbo", "ZoneType_Revealed": "revelado", "ZoneType_Command": "comando",
    "ZoneType_Sideboard": "sideboard", "ZoneType_Pending": "pendente", "ZoneType_Suppressed": "suprimido",
}
PHASES = {"Phase_Beginning": "início", "Phase_Main1": "principal 1", "Phase_Combat": "combate",
          "Phase_Main2": "principal 2", "Phase_Ending": "final"}
STEPS = {"Step_Upkeep": "manutenção", "Step_Draw": "compra", "Step_BeginCombat": "início do combate",
         "Step_DeclareAttack": "atacantes", "Step_DeclareBlock": "bloqueadores",
         "Step_FirstStrikeDamage": "dano de iniciativa", "Step_CombatDamage": "dano", "Step_EndCombat": "fim do combate",
         "Step_End": "final", "Step_Cleanup": "limpeza"}
TYPES = {"CardType_Creature": "criatura", "CardType_Land": "terreno", "CardType_Artifact": "artefato",
         "CardType_Enchantment": "encantamento", "CardType_Planeswalker": "planeswalker",
         "CardType_Instant": "instantânea", "CardType_Sorcery": "feitiço", "CardType_Battle": "batalha"}
VERBS = {"CastSpell": "conjura", "PlayLand": "joga", "Draw": "compra", "Sacrifice": "sacrifica",
         "Discard": "descarta", "Mill": "mói"}
DEATHS = {"SBA_Damage": "morre", "SBA_Deathtouch": "morre (toque mortífero)", "SBA_ZeroToughness": "morre",
          "Destroy": "é destruída", "Countered": "é anulada", "Exile": "é exilada"}
RECENT = 8


def _detail(annotation, key, default=None):
    for item in annotation.get("details", []):
        if item.get("key") == key:
            for field in ("valueInt32", "valueInt64", "valueUInt32", "valueString", "valueDouble", "valueBool"):
                if field in item:
                    value = item[field]
                    return value[0] if isinstance(value, list) and value else value
    return default


def _value(field):
    return field.get("value", 0) if isinstance(field, dict) else (field or 0)


class GameTracker:
    def __init__(self, names=None, my_seat=None, seat_names=None):
        self.names = names or (lambda grp: f"#{grp}")
        self.my_seat, self.seat_names = my_seat, dict(seat_names or {})
        self.zones, self.objects, self.life = {}, {}, {}
        self.turn = {"number": None, "phase": "", "step": "", "active": None}
        self.own_turns = {}          # lugar → quantos turnos desse jogador já começaram (contagem do goldfish)
        self.game, self.over, self.results = None, False, []
        self.events, self.attackers_logged, self.over_logged = [], set(), False
        self.seen = Counter()
        self.snapshots = {}          # turno → visão da mesa no começo dos seus turnos (spec 012)
        self._cache = {}

    # --- rótulos ---------------------------------------------------------------------------
    def label(self, seat):
        if seat is not None and seat == self.my_seat:
            return "você"
        return self.seat_names.get(seat) or f"jogador {seat}"

    def opponent_seat(self):
        seats = set(self.life) | set(self.seat_names)
        others = [s for s in seats if s != self.my_seat]
        return others[0] if len(others) == 1 else None

    def card_name(self, grp):
        if grp not in self._cache:
            self._cache[grp] = self.names(grp) if grp else "uma carta"
        return self._cache[grp]

    def obj_name(self, instance):
        obj = self.objects.get(instance)
        return self.card_name(obj.get("grpId")) if obj and obj.get("grpId") else "uma carta"

    def zone(self, kind, owner=None):
        for zone in self.zones.values():
            if zone["type"] == kind and (owner is None or zone["owner"] == owner):
                return zone
        return {"type": kind, "owner": owner, "ids": []}

    def zone_name(self, zone_id):
        zone = self.zones.get(zone_id)
        if not zone:
            return "?"
        base = ZONE_NAMES.get(zone["type"], zone["type"])
        return f"{base} de {self.label(zone['owner'])}" if zone["owner"] else base

    # --- aplicação de uma mensagem ---------------------------------------------------------------
    def apply(self, gsm):
        """Aplica uma GameStateMessage e devolve as linhas de evento geradas."""
        previous_turn, previous_life = self.turn["number"], dict(self.life)
        annotations = gsm.get("annotations", [])
        for zone in gsm.get("zones", []):
            self.zones[zone["zoneId"]] = {"type": zone.get("type"), "owner": zone.get("ownerSeatId"),
                                          "ids": list(zone.get("objectInstanceIds", []))}
        for annotation in annotations:
            if "AnnotationType_ObjectIdChanged" in annotation["type"]:
                orig, new = _detail(annotation, "orig_id"), _detail(annotation, "new_id")
                if orig in self.objects and new is not None and new != orig:
                    self.objects[new] = {**self.objects.pop(orig), "instanceId": new}
        for obj in gsm.get("gameObjects", []):
            self.objects[obj["instanceId"]] = obj
        for instance in gsm.get("diffDeletedInstanceIds", []):
            self.objects.pop(instance, None)
        self._update_seen()
        info = gsm.get("turnInfo")
        if info:
            self.turn.update(number=info.get("turnNumber", self.turn["number"]), phase=info.get("phase", self.turn["phase"]),
                             step=info.get("step", ""), active=info.get("activePlayer", self.turn["active"]))
        for player in gsm.get("players", []):
            if "lifeTotal" in player and "systemSeatNumber" in player:
                self.life[player["systemSeatNumber"]] = player["lifeTotal"]
        game = gsm.get("gameInfo") or {}
        if game.get("gameNumber"):
            self.game = game["gameNumber"]
        if game.get("stage") == "GameStage_GameOver":
            self.over, self.results = True, game.get("results", self.results)

        lines = []
        if self.turn["number"] and self.turn["number"] != previous_turn:
            self.attackers_logged = set()
            active = self.turn["active"]
            self.own_turns[active] = self.own_turns.get(active, 0) + 1
            lines.append(self.turn_line())
        if (self.my_seat is not None and self.turn["active"] == self.my_seat and self.turn["number"]
                and self.turn["phase"] == "Phase_Main1" and self.turn["number"] not in self.snapshots):
            self.snapshots[self.turn["number"]] = self.snapshot()
        for annotation in annotations:
            text = self.describe(annotation)
            if text:
                lines.append(text)
        attackers = [o for o in self.objects.values() if o.get("attackState") == "AttackState_Declared"
                     and o["instanceId"] not in self.attackers_logged]
        if attackers:
            self.attackers_logged.update(o["instanceId"] for o in attackers)
            controller = attackers[0].get("controllerSeatId")
            lines.append(f"{self.label(controller)} ataca com " + ", ".join(self.short(o) for o in attackers))
        if previous_life and self.life != previous_life and not any("vida" in line for line in lines):
            lines.append("vida: " + self.life_text())
        if self.over and not self.over_logged:
            self.over_logged = True
            lines.append("fim do jogo" + (f" — {self.result_text()}" if self.results else ""))
        for text in lines:
            self.events.append({"turn": self.turn["number"], "phase": PHASES.get(self.turn["phase"], ""),
                                "step": STEPS.get(self.turn["step"], ""), "text": text})
        return lines

    def _update_seen(self):
        opponent = self.opponent_seat()
        if opponent is None:
            return
        current = Counter(o.get("grpId") for o in self.objects.values()
                          if o.get("ownerSeatId") == opponent and o.get("grpId") and o.get("type") == "GameObjectType_Card")
        for grp, count in current.items():
            self.seen[grp] = max(self.seen[grp], count)

    def describe(self, annotation):
        kinds = annotation.get("type", [])
        affected = annotation.get("affectedIds") or []
        if "AnnotationType_ZoneTransfer" in kinds:
            category = _detail(annotation, "category") or ""
            src, dest = _detail(annotation, "zone_src"), _detail(annotation, "zone_dest")
            obj = self.objects.get(affected[0]) if affected else None
            dest_zone, src_zone = self.zones.get(dest, {}), self.zones.get(src, {})
            owner = (obj or {}).get("ownerSeatId") or dest_zone.get("owner") or src_zone.get("owner")
            name = self.card_name(obj["grpId"]) if obj and obj.get("grpId") else "uma carta"
            if category in VERBS:
                return f"{self.label(owner)} {VERBS[category]} {name}"
            if category == "Resolve":
                return f"{name} entra em campo" if dest_zone.get("type") == "ZoneType_Battlefield" else f"{name} resolve"
            if category in DEATHS:
                return f"{name} {DEATHS[category]}"
            return f"{name}: {self.zone_name(src)} → {self.zone_name(dest)}" + (f" ({category})" if category else "")
        if "AnnotationType_DamageDealt" in kinds:
            amount = _detail(annotation, "damage", 0)
            source = self.obj_name(annotation.get("affectorId"))
            targets = ", ".join(self.target_name(i) for i in affected) or "?"
            return f"{source} causa {amount} de dano em {targets}"
        if "AnnotationType_ModifiedLife" in kinds:
            delta = _detail(annotation, "life", 0)
            seat = affected[0] if affected else None
            who = "sua vida" if seat == self.my_seat else f"vida de {self.label(seat)}"
            return f"{who}: {self.life.get(seat, '?')} ({delta:+d})"
        if "AnnotationType_CounterAdded" in kinds:
            amount = _detail(annotation, "transaction_amount", 1)
            return f"{self.obj_name(affected[0]) if affected else 'uma permanente'} recebe {amount} marcador(es)"
        if "AnnotationType_TokenCreated" in kinds:
            obj = self.objects.get(affected[0]) if affected else None
            if obj:
                return f"{self.label(obj.get('controllerSeatId'))} cria {self.short(obj)}"
        return None

    def target_name(self, instance):
        if instance in self.objects:
            return self.obj_name(instance)
        if instance in self.life or instance in self.seat_names or instance == self.my_seat:
            return self.label(instance)
        return f"#{instance}"

    # --- textos ---------------------------------------------------------------------------------
    def short(self, obj):
        name = self.card_name(obj.get("grpId")) if obj.get("grpId") else "ficha"
        if "CardType_Creature" in obj.get("cardTypes", []):
            name += f" {_value(obj.get('power'))}/{_value(obj.get('toughness'))}"
        flags = []
        if obj.get("isTapped"):
            flags.append("virada")
        if obj.get("hasSummoningSickness"):
            flags.append("enjoo")
        if obj.get("attackState") == "AttackState_Declared":
            flags.append("atacando")
        if obj.get("blockState") == "BlockState_Blocking":
            flags.append("bloqueando")
        if obj.get("damage"):
            flags.append(f"{obj['damage']} de dano")
        return name + (f" ({', '.join(flags)})" if flags else "")

    def life_text(self):
        return " × ".join(f"{self.label(seat)} {total}" for seat, total in sorted(self.life.items()))

    def turn_text(self):
        """`turno 10 (seu 5º)`: o Arena numera os turnos do jogo; a contagem entre parênteses
        é a do goldfish e dos nomes de deck ("Turn 2 Kill"), só os turnos de quem joga."""
        active = self.turn["active"]
        own = self.own_turns.get(active)
        if own is None or active is None:
            return f"turno {self.turn['number'] or '?'}"
        who = "seu" if active == self.my_seat else f"de {self.label(active)}"
        return f"turno {self.turn['number']} ({own}º {who})"

    def turn_line(self):
        game = f"jogo {self.game} · " if self.game else ""
        return f"{game}{self.turn_text()} · ativo: {self.label(self.turn['active'])} · vida: {self.life_text()}"

    def result_text(self):
        parts = []
        for result in self.results:
            scope = (result.get("scope") or "").replace("MatchScope_", "").lower()
            winner = result.get("winningTeamId")
            outcome = "?" if self.my_seat is None else ("vitória" if winner == self.my_seat else "derrota")
            parts.append(f"{scope}: {outcome}")
        return ", ".join(parts)

    def permanents(self, seat):
        return [o for o in self.objects.values()
                if o.get("controllerSeatId") == seat
                and self.zones.get(o.get("zoneId"), {}).get("type") == "ZoneType_Battlefield"
                and o.get("type") in ("GameObjectType_Card", "GameObjectType_Token")]

    def in_zone(self, kind, owner):
        return [o for o in self.objects.values()
                if o.get("ownerSeatId") == owner and self.zones.get(o.get("zoneId"), {}).get("type") == kind
                and o.get("type") in ("GameObjectType_Card", "GameObjectType_Token", "GameObjectType_Adventure")]

    @staticmethod
    def _group(objects, names):
        counts = Counter(names(o) for o in objects)
        return " · ".join(f"{name} ×{n}" if n > 1 else name for name, n in counts.items()) or "—"

    def field_text(self, seat):
        permanents = self.permanents(seat)
        lands = [o for o in permanents if "CardType_Land" in o.get("cardTypes", [])]
        creatures = [o for o in permanents if "CardType_Creature" in o.get("cardTypes", [])]
        others = [o for o in permanents if o not in lands and o not in creatures]
        parts = []
        if lands:
            tapped = sum(1 for o in lands if o.get("isTapped"))
            parts.append(self._group(lands, lambda o: self.card_name(o.get("grpId"))) + (f" ({tapped} virados)" if tapped else ""))
        if creatures:
            parts.append(" · ".join(self.short(o) for o in creatures))
        if others:
            parts.append(" · ".join(self.short(o) for o in others))
        return " | ".join(parts) or "—"

    def open_mana(self, seat):
        return sum(1 for o in self.permanents(seat) if "CardType_Land" in o.get("cardTypes", []) and not o.get("isTapped"))

    def hints(self):
        """Conselhos calculáveis: letal na mesa e mana aberta do oponente."""
        out = []
        opponent = self.opponent_seat()
        if self.my_seat is None or opponent is None:
            return out
        if self.turn["active"] == self.my_seat and self.turn["step"] not in ("Step_CombatDamage", "Step_EndCombat") \
                and self.turn["phase"] not in ("Phase_Main2", "Phase_Ending"):
            attackers = [o for o in self.permanents(self.my_seat) if "CardType_Creature" in o.get("cardTypes", [])
                         and not o.get("isTapped") and not o.get("hasSummoningSickness")]
            power = sum(_value(o.get("power")) for o in attackers)
            blockers = [o for o in self.permanents(opponent) if "CardType_Creature" in o.get("cardTypes", []) and not o.get("isTapped")]
            life = self.life.get(opponent)
            if attackers and life is not None:
                verdict = "LETAL na mesa" if power >= life else "sem letal no ataque"
                out.append(f"{verdict}: {power} de poder podem atacar contra {life} de vida"
                           f" (sem contar {len(blockers)} bloqueador(es) desvirado(s) do oponente)")
        mana = self.open_mana(opponent)
        if mana:
            out.append(f"{self.label(opponent)} tem {mana} terreno(s) desvirado(s): pode responder")
        return out

    def board_text(self, recent=RECENT):
        opponent = self.opponent_seat()
        phase = PHASES.get(self.turn["phase"], self.turn["phase"] or "")
        step = STEPS.get(self.turn["step"], "")
        head = (f"jogo {self.game} · " if self.game else "") + f"{self.turn_text()} · {phase}" + \
               (f" ({step})" if step else "") + f" · ativo: {self.label(self.turn['active'])} · vida: {self.life_text()}"
        lines = [head]
        if self.my_seat is not None:
            hand = self.in_zone("ZoneType_Hand", self.my_seat)
            lines.append(f"sua mão ({len(hand)}): " + self._group(hand, lambda o: self.card_name(o.get("grpId"))))
            lines.append("seu campo: " + self.field_text(self.my_seat))
        if opponent is not None:
            lines.append(f"campo de {self.label(opponent)}: " + self.field_text(opponent))
        for kind, title in (("ZoneType_Graveyard", "cemitério"), ("ZoneType_Exile", "exílio")):
            parts = []
            for seat in sorted(set([self.my_seat, opponent]) - {None}):
                cards = self.in_zone(kind, seat)
                if cards:
                    parts.append(f"{self.label(seat)} — " + self._group(cards, lambda o: self.card_name(o.get("grpId"))))
            lines.append(f"{title}: " + (" | ".join(parts) or "—"))
        stack = [o for o in self.objects.values() if self.zones.get(o.get("zoneId"), {}).get("type") == "ZoneType_Stack"]
        if stack:
            lines.append("pilha: " + " · ".join(self.short(o) for o in stack))
        if opponent is not None:
            lines.append(f"{self.label(opponent)}: mão {len(self.zone('ZoneType_Hand', opponent)['ids'])} · "
                         f"biblioteca {len(self.zone('ZoneType_Library', opponent)['ids'])} · mana aberta {self.open_mana(opponent)}"
                         + (f"  |  você: biblioteca {len(self.zone('ZoneType_Library', self.my_seat)['ids'])} · "
                            f"mana aberta {self.open_mana(self.my_seat)}" if self.my_seat is not None else ""))
            seen = [f"{self.card_name(grp)}" + (f" ×{n}" if n > 1 else "") for grp, n in self.seen.most_common(12)]
            if seen:
                lines.append(f"cartas vistas de {self.label(opponent)}: " + ", ".join(seen))
        for hint in self.hints():
            lines.append("» " + hint)
        if self.events:
            lines.append("últimos lances:")
            lines += ["  " + e["text"] for e in self.events[-recent:]]
        return "\n".join(lines)

    # --- registro -------------------------------------------------------------------------------
    def snapshot(self):
        """Estado estruturado do começo de um turno seu, para o conselheiro (spec 012)."""
        opponent = self.opponent_seat()
        names = lambda objects: [self.card_name(o.get("grpId")) for o in objects if o.get("grpId")]  # noqa: E731
        return {
            "turn": self.turn["number"], "own_turn": self.own_turns.get(self.my_seat), "life": dict(self.life),
            "hand": names(self.in_zone("ZoneType_Hand", self.my_seat)) if self.my_seat is not None else [],
            "my_field": [self.short(o) for o in self.permanents(self.my_seat)] if self.my_seat is not None else [],
            "opp_field": [self.short(o) for o in self.permanents(opponent)] if opponent is not None else [],
            "my_graveyard": names(self.in_zone("ZoneType_Graveyard", self.my_seat)) if self.my_seat is not None else [],
            "opp_graveyard": names(self.in_zone("ZoneType_Graveyard", opponent)) if opponent is not None else [],
            "opp_hand": len(self.zone("ZoneType_Hand", opponent)["ids"]) if opponent is not None else None,
            "open_mana": {"me": self.open_mana(self.my_seat) if self.my_seat is not None else None,
                          "opp": self.open_mana(opponent) if opponent is not None else None},
            "hints": self.hints(), "text": self.board_text(recent=0),
        }

    def record(self):
        opponent = self.opponent_seat()
        return {
            "game": self.game, "my_seat": self.my_seat, "players": {str(s): self.label(s) for s in sorted(self.life)},
            "result": self.result_text() if self.results else None, "life": dict(self.life),
            "turns": self.turn["number"], "own_turns": self.own_turns.get(self.my_seat), "events": self.events,
            "seen_opponent": {self.card_name(g): n for g, n in self.seen.most_common()} if opponent is not None else {},
            "snapshots": {str(k): v for k, v in self.snapshots.items()},
            "final_board": self.board_text(recent=0),
        }

    def markdown(self, title=""):
        lines = [f"# {title or 'Partida'}", ""]
        rec = self.record()
        own = f" ({rec['own_turns']} seus)" if rec.get("own_turns") else ""
        lines.append(f"- Resultado: {rec['result'] or 'em andamento'} · turnos do jogo: {rec['turns']}{own} · "
                     f"vida final: {self.life_text()}")
        if rec["seen_opponent"]:
            lines.append("- Cartas vistas do oponente: " + ", ".join(f"{k} ×{v}" if v > 1 else k for k, v in rec["seen_opponent"].items()))
        lines += ["", "## Lances", ""]
        current = None
        for event in self.events:
            if event["turn"] != current:
                current = event["turn"]
                lines.append(f"**Turno {current}**" if current else "**Antes do primeiro turno**")
            lines.append(f"- {event['text']}" + (f" _({event['phase']}{', ' + event['step'] if event['step'] else ''})_" if event["phase"] else ""))
        lines += ["", "## Mesa final", "", "```", rec["final_board"], "```", ""]
        return "\n".join(lines)
