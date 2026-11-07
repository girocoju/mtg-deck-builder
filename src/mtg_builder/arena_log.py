"""Leitura do `Player.log` do MTG Arena (só o draft) e da base de cartas do próprio cliente.

O Arena não tem API de plugins: o Draftsmith do Untapped e o cliente do 17Lands leem o
log que o jogo grava quando a opção *Detailed Logs (Plugin Support)* está ligada. Este
módulo faz o mesmo, só em leitura, e resolve os identificadores (GrpId) pela base SQLite
que o cliente baixa em `MTGA_Data/Downloads/Raw/Raw_CardDatabase_*.mtga`.

Marcadores (nomes dos clientes abertos consultados em 2026-11-06; o Arena muda os nomes
sem aviso, por isso a comparação ignora sublinhados e maiúsculas):

| Modo                  | Pacote mostrado                                   | Pick feito                                |
| --------------------- | ------------------------------------------------- | ----------------------------------------- |
| Premier / Traditional | `Draft.Notify` (SelfPack, SelfPick, PackCards)    | `EventPlayerDraftMakePick` (GrpIds, Pack, Pick) |
|                       | `LogBusinessEvents` (CardsInPack, PickGrpId): pacote e pick juntos, cobre o P1P1 |      |
| Quick Draft           | `DraftStatus == PickNext` (DraftPack)             | `BotDraft_DraftPick` (PickInfo.CardIds)   |
| Qualquer              | `Event_Join` / `Course` (entrou no evento), `Draft_CompleteDraft` (acabou) |          |

Pacote e pick vêm indexados a partir de zero no log; aqui saem de 1 a 3 e de 1 a 14.
"""

import json
import os
import re
import sqlite3
from pathlib import Path

from . import decklist

ENTRY_START = re.compile(r"^\[(UnityCrossThreadLogger|Client GRE)\]")
TIMESTAMP = re.compile(r"^\[(?:UnityCrossThreadLogger|Client GRE)\](\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}:\d{2}(?: [AP]M)?)")
JSON_START = re.compile(r"[\[{]")
EVENT_NAME = re.compile(r"^(?P<kind>[A-Za-z]+?)_(?P<set>[A-Za-z0-9]{2,6})_(?P<date>\d{6,10})")
MODES_BY_EVENT = {
    "premierdraft": "premier", "quickdraft": "quick", "traddraft": "trad", "compdraft": "premier",
    "picktwodraft": "picktwo", "sealed": "sealed", "tradsealed": "tradsealed",
}
RARITY_CODES = {1: "basic", 2: "common", 3: "uncommon", 4: "rare", 5: "mythic"}
PACK_SIZE = 14
PACKS = 3


# --- localização dos arquivos -----------------------------------------------------------

def default_log_dir():
    home = Path(os.environ.get("USERPROFILE") or Path.home())
    return home / "AppData" / "LocalLow" / "Wizards Of The Coast" / "MTGA"


def find_log(path=None):
    """Caminho do `Player.log` (o informado, ou o padrão do Windows). None se não existir."""
    candidate = Path(path) if path else default_log_dir() / "Player.log"
    return candidate if candidate.exists() else None


def detailed_logs_enabled(path):
    """True/False conforme o cabeçalho do log; None se o log não diz."""
    try:
        with open(path, "rb") as handle:
            head = handle.read(256 * 1024).decode("utf-8", errors="replace")
    except OSError:
        return None
    if "DETAILED LOGS: ENABLED" in head:
        return True
    if "DETAILED LOGS: DISABLED" in head:
        return False
    return None


def arena_dirs():
    env = os.environ.get("MTGA_DIR")
    roots = [Path(env)] if env else []
    for base in (os.environ.get("ProgramFiles"), os.environ.get("ProgramFiles(x86)")):
        if base:
            roots.append(Path(base) / "Wizards of the Coast" / "MTGA")
    return roots


def find_arena_db(arena_dir=None):
    """Base de cartas do cliente: o `Raw_CardDatabase_*.mtga` mais recente. None se não achar."""
    roots = [Path(arena_dir)] if arena_dir else arena_dirs()
    found = []
    for root in roots:
        found += list((root / "MTGA_Data" / "Downloads" / "Raw").glob("Raw_CardDatabase_*.mtga"))
    return max(found, key=lambda p: p.stat().st_mtime) if found else None


# --- nomes de eventos --------------------------------------------------------------------

def parse_event_name(name):
    """`PremierDraft_FRA_20261106` → (modo, coleção). (None, None) se não for um draft."""
    match = EVENT_NAME.match(name or "")
    if not match:
        return None, None
    kind = match.group("kind").lower()
    mode = MODES_BY_EVENT.get(kind)
    if mode is None and "draft" in kind:
        mode = "premier"
    return mode, match.group("set").lower()


# --- mensagens ---------------------------------------------------------------------------

def _ids(value):
    if isinstance(value, str):
        value = value.split(",")
    if not isinstance(value, list):
        return []
    ids = []
    for item in value:
        try:
            ids.append(int(str(item).strip()))
        except ValueError:
            continue
    return ids


def _decode_payload(obj, depth=0):
    """Mensagens de pedido embutem o JSON como texto em `request`/`Payload`; desembrulha."""
    if depth > 4 or not isinstance(obj, dict):
        return obj
    for key in ("payload", "Payload", "request"):
        if key in obj:
            value = obj[key]
            if isinstance(value, str):
                try:
                    value = json.loads(value)
                except ValueError:
                    return obj
            return _decode_payload(value, depth + 1)
    return obj


def _normalize(header):
    return re.sub(r"[^a-z.]", "", header.lower())


def _number(obj, *keys):
    for key in keys:
        if key in obj:
            try:
                return int(obj[key])
            except (TypeError, ValueError):
                continue
    return 0


def classify(header, obj):
    """Transforma uma mensagem decodificada em um evento de draft, ou None."""
    if not isinstance(obj, dict):
        return None
    marker = _normalize(header)
    if obj.get("PackCards") is not None and any(k in obj for k in ("SelfPack", "SelfPick", "draftId", "DraftId")):
        return {"type": "pack", "source": "Draft.Notify", "draft_id": obj.get("draftId") or obj.get("DraftId"),
                "pack": _number(obj, "SelfPack") + 1, "pick": _number(obj, "SelfPick") + 1,
                "cards": _ids(obj["PackCards"]), "event": obj.get("EventName") or obj.get("EventId")}
    if "CardsInPack" in obj and "PickGrpId" in obj:
        return {"type": "pack_and_pick", "source": "LogBusinessEvents", "draft_id": obj.get("DraftId"),
                "pack": _number(obj, "PackNumber") + 1, "pick": _number(obj, "PickNumber") + 1,
                "cards": _ids(obj["CardsInPack"]), "card": _number(obj, "PickGrpId"),
                "event": obj.get("EventId") or obj.get("EventName")}
    if "GrpIds" in obj and ("Pack" in obj or "Pick" in obj):
        ids = _ids(obj["GrpIds"])
        return {"type": "pick", "source": "EventPlayerDraftMakePick", "draft_id": obj.get("DraftId"),
                "pack": _number(obj, "Pack") + 1, "pick": _number(obj, "Pick") + 1,
                "card": ids[0] if ids else None, "cards": ids}
    if obj.get("DraftStatus") == "PickNext" and "DraftPack" in obj:
        return {"type": "pack", "source": "DraftStatus", "event": obj.get("EventName"),
                "pack": _number(obj, "PackNumber") + 1, "pick": _number(obj, "PickNumber") + 1,
                "cards": _ids(obj["DraftPack"])}
    info = obj.get("PickInfo")
    if isinstance(info, dict) and ("CardIds" in info or "CardId" in info):
        ids = _ids(info.get("CardIds") if "CardIds" in info else [info.get("CardId")])
        return {"type": "pick", "source": "BotDraft_DraftPick", "event": info.get("EventName") or obj.get("EventName"),
                "pack": _number(info, "PackNumber", "Pack") + 1, "pick": _number(info, "PickNumber", "Pick") + 1,
                "card": ids[0] if ids else None, "cards": ids}
    course = obj.get("Course")
    if isinstance(course, dict) and course.get("InternalEventName"):
        name = course["InternalEventName"]
        if "draft" in name.lower() or "sealed" in name.lower():
            return {"type": "join", "source": "Course", "event": name}
    if "eventjoin" in marker and obj.get("EventName"):
        return {"type": "join", "source": "Event_Join", "event": obj["EventName"]}
    if "completedraft" in marker and (obj.get("DraftId") or obj.get("draftId")):
        return {"type": "complete", "source": "Draft_CompleteDraft", "draft_id": obj.get("DraftId") or obj.get("draftId")}
    if "draft" in marker:
        return {"type": "unknown", "header": header.strip()[:120], "keys": sorted(obj)[:12]}
    return None


def parse_entry(text, classifier=classify):
    """Uma entrada completa do log (cabeçalho e linhas seguintes) → evento ou None.
    Devolve também se o JSON estava completo (para o leitor ao vivo esperar o resto)."""
    start = ENTRY_START.match(text)
    position = start.end() if start else 0
    decoder = json.JSONDecoder()
    obj = None
    for _ in range(3):
        match = JSON_START.search(text, position)
        if not match:
            return None, False
        try:
            obj, _end = decoder.raw_decode(text, match.start())
            break
        except ValueError:
            position = match.start() + 1
    if obj is None:
        return None, False
    header = text[:200].split("\n")
    header = " ".join(header[:3])
    return classifier(header, _decode_payload(obj)), True


class LogParser:
    """Junta as linhas do log em entradas (cada uma começa com `[UnityCrossThreadLogger]`)
    e extrai os eventos com o classificador dado (draft por padrão; partidas em
    `arena_match.classify_match`)."""

    def __init__(self, classifier=classify):
        self.classifier = classifier
        self.buffer = []
        self.events = []
        self.unparsed = 0
        self.stamp = None          # último horário visto num cabeçalho (`dd/mm/aaaa hh:mm:ss`, hora local)

    def feed(self, line):
        line = line.rstrip("\r\n")
        if ENTRY_START.match(line):
            self._complete()
            self.buffer = [line]
            match = TIMESTAMP.match(line)
            if match:
                self.stamp = _iso(match.group(1))
        elif self.buffer:
            self.buffer.append(line)

    def _emit(self, event):
        event.setdefault("at", self.stamp)
        self.events.append(event)

    def _complete(self):
        if not self.buffer:
            return
        event, decoded = parse_entry("\n".join(self.buffer), self.classifier)
        if event:
            self._emit(event)
        elif not decoded and "draft" in self.buffer[0].lower():
            self.unparsed += 1
        self.buffer = []

    def flush(self):
        """Eventos acumulados. Tenta também a entrada pendente, para não esperar a linha
        seguinte do log quando o JSON já está completo."""
        if self.buffer:
            event, decoded = parse_entry("\n".join(self.buffer), self.classifier)
            if decoded:
                if event:
                    self._emit(event)
                self.buffer = []
        events, self.events = self.events, []
        return events


def _iso(stamp):
    """`06/11/2026 23:16:36` (formato da máquina, dia/mês/ano) → ISO; sem conversão, o texto."""
    from datetime import datetime
    for fmt in ("%d/%m/%Y %H:%M:%S", "%m/%d/%Y %H:%M:%S", "%d/%m/%Y %I:%M:%S %p", "%m/%d/%Y %I:%M:%S %p"):
        try:
            return datetime.strptime(stamp, fmt).isoformat(timespec="seconds")
        except ValueError:
            continue
    return stamp


def events_from_text(text, classifier=classify):
    parser = LogParser(classifier)
    for line in text.splitlines():
        parser.feed(line)
    parser._complete()
    return parser.flush()


class LogFollower:
    """Lê o log incrementalmente (de meio segundo em meio segundo, por quem chama), a partir
    do fim ou do começo, e detecta quando o Arena recria o arquivo."""

    def __init__(self, path, from_start=False, classifier=classify):
        self.path = Path(path)
        self.classifier = classifier
        self.parser = LogParser(classifier)
        self.offset = 0 if from_start else self._size()
        self.tail = ""

    def _size(self):
        try:
            return self.path.stat().st_size
        except OSError:
            return 0

    def poll(self):
        size = self._size()
        if size < self.offset:                      # arquivo recriado
            self.offset, self.tail, self.parser = 0, "", LogParser(self.classifier)
        if size > self.offset:
            with open(self.path, "rb") as handle:
                handle.seek(self.offset)
                chunk = handle.read(size - self.offset)
            self.offset = size
            text = self.tail + chunk.decode("utf-8", errors="replace")
            lines = text.split("\n")
            self.tail = lines.pop()                 # linha ainda incompleta
            for line in lines:
                self.parser.feed(line)
        return self.parser.flush()

    def finish(self):
        """Fim de um log gravado (reprodução): a última linha pode não ter quebra de linha
        e a última entrada ainda está no buffer; entrega os dois."""
        events = self.poll()
        if self.tail:
            self.parser.feed(self.tail)
            self.tail = ""
        self.parser._complete()
        return events + self.parser.flush()


# --- base de cartas do Arena -------------------------------------------------------------

def _plain(name):
    """Os nomes na base do Arena trazem marcação (`<nobr>Blossom-Blessed</nobr> Angel`)."""
    return re.sub(r"<[^>]+>", "", name or "").strip()


class ArenaCards:
    """GrpId → carta, pela base SQLite do cliente, com os nomes em inglês e português."""

    def __init__(self, path):
        self.path = Path(path)
        conn = sqlite3.connect(f"file:{self.path.as_posix()}?mode=ro", uri=True)
        tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
        has_pt = "Localizations_ptBR" in tables
        rows = conn.execute(
            "SELECT c.GrpId, c.ExpansionCode, c.CollectorNumber, c.Rarity, c.DraftContent, c.IsToken, "
            "MIN(en.Loc) AS name_en" + (", MIN(pt.Loc) AS name_pt" if has_pt else ", NULL AS name_pt") +
            " FROM Cards c LEFT JOIN Localizations_enUS en ON en.LocId = c.TitleId" +
            (" LEFT JOIN Localizations_ptBR pt ON pt.LocId = c.TitleId" if has_pt else "") +
            " GROUP BY c.GrpId"
        ).fetchall()
        conn.close()
        self.cards = {}
        for grp, set_code, number, rarity, draft_content, is_token, name_en, name_pt in rows:
            self.cards[int(grp)] = {
                "grp": int(grp), "set": (set_code or "").lower(), "number": str(number or ""),
                "rarity": RARITY_CODES.get(rarity, str(rarity)), "draft": bool(draft_content),
                "token": bool(is_token), "name_en": _plain(name_en), "name_pt": _plain(name_pt),
            }
        self._index = None

    def __len__(self):
        return len(self.cards)

    def draftable(self, set_code):
        return [c for c in self.cards.values() if c["set"] == set_code.lower() and c["draft"] and not c["token"]]

    def resolve(self, conn, grp_ids):
        """Cartas da base do projeto para os GrpIds: pelo nome em inglês e, se o nome não
        existir na base, pela impressão (coleção e número de colecionador)."""
        if self._index is None:
            self._index = decklist._name_index(conn) if conn is not None else {}
        out = []
        for grp in grp_ids:
            info = self.cards.get(int(grp))
            if info is None:
                out.append({"grp": int(grp), "name": f"#{grp}", "rarity": None, "card": None,
                            "set": None, "number": None, "name_pt": ""})
                continue
            card = self._index.get(decklist._key(info["name_en"])) if info["name_en"] else None
            if card is None and conn is not None and info["set"] and info["number"]:
                card = _by_printing(conn, info["set"], info["number"])
            out.append({"grp": info["grp"], "name": card["name"] if card else info["name_en"] or f"#{grp}",
                        "rarity": info["rarity"], "card": card, "set": info["set"],
                        "number": info["number"], "name_pt": info["name_pt"]})
        return out


def _by_printing(conn, set_code, number):
    return conn.execute(
        "SELECT c.* FROM printings p JOIN cards c ON c.oracle_id = p.oracle_id "
        "WHERE p.collector_number = ?1 AND p.set_code IN ("
        "  SELECT code FROM sets WHERE code = ?2 COLLATE NOCASE OR arena_code = ?2 COLLATE NOCASE"
        "  UNION SELECT lower(?2)) LIMIT 1",
        (number, set_code),
    ).fetchone()


def resolve_by_arena_id(conn, grp_ids):
    """Sem a base do Arena: tenta o `arena_id` que o Scryfall traz para algumas impressões."""
    out = []
    for grp in grp_ids:
        row = conn.execute(
            "SELECT c.*, p.rarity AS printing_rarity FROM printings p JOIN cards c ON c.oracle_id = p.oracle_id "
            "WHERE p.arena_id = ? LIMIT 1", (int(grp),)).fetchone()
        out.append({"grp": int(grp), "name": row["name"] if row else f"#{grp}",
                    "rarity": row["printing_rarity"] if row else None, "card": row,
                    "set": None, "number": None, "name_pt": ""})
    return out
