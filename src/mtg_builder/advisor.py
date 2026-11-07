"""Conselheiro local (spec 012): opinião de jogada por um modelo rodando na máquina, pelo
Ollama (`http://localhost:11434`). O modelo recebe tudo pronto (visão da partida, textos
de regras das cartas visíveis, plano do deck, dicas calculáveis) e responde um JSON curto.
A resposta é opinião: sai rotulada e nunca substitui as dicas calculáveis do rastreador.
"""

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

from . import db, decklist

DEFAULT_URL = "http://localhost:11434"
DEFAULT_MODEL = "qwen2.5:7b"
MAX_CARD_TEXT = 420
MAX_PLAN_CHARS = 2500
SYSTEM = (
    "Você é um conselheiro de Magic: The Gathering acompanhando uma partida no MTG Arena. "
    "Use apenas as cartas, textos de regras e fatos fornecidos; não invente cartas nem regras. "
    "Os fatos calculados (letal, mana aberta) são verdade e têm prioridade sobre a sua impressão. "
    "Responda SOMENTE um JSON com as chaves: jogada (uma frase, a ação concreta deste turno), "
    "motivo (uma frase), risco (uma frase: o que o oponente pode fazer), "
    "confianca (baixa, media ou alta). Português do Brasil, nomes de cartas em inglês."
)


class OllamaAdvisor:
    def __init__(self, model=DEFAULT_MODEL, url=DEFAULT_URL, timeout=90, num_predict=220, temperature=0.2):
        self.model, self.url, self.timeout = model, url.rstrip("/"), timeout
        self.num_predict, self.temperature = num_predict, temperature

    def _get(self, path):
        with urllib.request.urlopen(self.url + path, timeout=5) as response:
            return json.load(response)

    def available(self):
        try:
            self._get("/api/tags")
            return True
        except (OSError, ValueError):
            return False

    def models(self):
        try:
            return [m.get("name") for m in self._get("/api/tags").get("models", [])]
        except (OSError, ValueError):
            return []

    def ask(self, context):
        """Devolve {"jogada", "motivo", "risco", "confianca", "modelo", "segundos", "tokens_s"}
        ou {"erro": ...} se o servidor não responder ou a resposta não for JSON."""
        body = json.dumps({
            "model": self.model, "stream": False, "format": "json", "keep_alive": "30m",
            "options": {"temperature": self.temperature, "num_predict": self.num_predict},
            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": context}],
        }).encode("utf-8")
        request = urllib.request.Request(self.url + "/api/chat", data=body, headers={"Content-Type": "application/json"})
        started = time.time()
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = json.load(response)
        except urllib.error.HTTPError as error:
            return {"erro": f"Ollama respondeu {error.code}: {error.read()[:200].decode('utf-8', 'replace')}"}
        except (OSError, ValueError) as error:
            return {"erro": f"Ollama indisponível em {self.url}: {error}"}
        seconds = time.time() - started
        content = (data.get("message") or {}).get("content") or data.get("response") or ""
        try:
            answer = json.loads(content)
        except ValueError:
            match = re.search(r"\{.*\}", content, re.S)
            try:
                answer = json.loads(match.group(0)) if match else {}
            except ValueError:
                answer = {}
        if not isinstance(answer, dict) or not answer.get("jogada"):
            return {"erro": "resposta sem JSON utilizável", "bruto": content[:300], "segundos": round(seconds, 1)}
        tokens = data.get("eval_count") or 0
        duration = (data.get("eval_duration") or 0) / 1e9
        return {"jogada": str(answer.get("jogada", "")), "motivo": str(answer.get("motivo", "")),
                "risco": str(answer.get("risco", "")), "confianca": str(answer.get("confianca", "?")),
                "modelo": self.model, "segundos": round(seconds, 1),
                "tokens_s": round(tokens / duration, 1) if duration else None}


class OpenAICompatibleAdvisor(OllamaAdvisor):
    """Mesmo conselheiro pela API no formato da OpenAI (`/v1/models`, `/v1/chat/completions`),
    que o LocalAI (porta 8080), o próprio Ollama (porta 11434), o LM Studio e o servidor
    do llama.cpp expõem. Sem chave de API; `response_format` JSON quando o servidor aceita,
    e extração do JSON do texto quando não."""

    def models(self):
        try:
            return [m.get("id") for m in self._get("/v1/models").get("data", [])]
        except (OSError, ValueError):
            return []

    def available(self):
        try:
            self._get("/v1/models")
            return True
        except (OSError, ValueError):
            return False

    def ask(self, context):
        body = json.dumps({
            "model": self.model, "stream": False, "temperature": self.temperature, "max_tokens": self.num_predict,
            "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": context}],
        }).encode("utf-8")
        request = urllib.request.Request(self.url + "/v1/chat/completions", data=body,
                                         headers={"Content-Type": "application/json", "Authorization": "Bearer local"})
        started = time.time()
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = json.load(response)
        except urllib.error.HTTPError as error:
            return {"erro": f"servidor respondeu {error.code}: {error.read()[:200].decode('utf-8', 'replace')}"}
        except (OSError, ValueError) as error:
            return {"erro": f"servidor indisponível em {self.url}: {error}"}
        seconds = time.time() - started
        choices = data.get("choices") or [{}]
        content = ((choices[0].get("message") or {}).get("content")) or choices[0].get("text") or ""
        try:
            answer = json.loads(content)
        except ValueError:
            match = re.search(r"\{.*\}", content, re.S)
            try:
                answer = json.loads(match.group(0)) if match else {}
            except ValueError:
                answer = {}
        if not isinstance(answer, dict) or not answer.get("jogada"):
            return {"erro": "resposta sem JSON utilizável", "bruto": content[:300], "segundos": round(seconds, 1)}
        tokens = (data.get("usage") or {}).get("completion_tokens") or 0
        return {"jogada": str(answer.get("jogada", "")), "motivo": str(answer.get("motivo", "")),
                "risco": str(answer.get("risco", "")), "confianca": str(answer.get("confianca", "?")),
                "modelo": data.get("model") or self.model, "segundos": round(seconds, 1),
                "tokens_s": round(tokens / seconds, 1) if tokens and seconds else None}


APIS = {"ollama": (OllamaAdvisor, DEFAULT_URL), "openai": (OpenAICompatibleAdvisor, "http://localhost:8080")}


def make_advisor(api="ollama", model=DEFAULT_MODEL, url=None, **kw):
    """`ollama` (API nativa, porta 11434) ou `openai` (LocalAI na 8080, Ollama em
    /v1, LM Studio, llama.cpp)."""
    if api not in APIS:
        raise RuntimeError(f"API desconhecida: {api}. Use ollama ou openai.")
    cls, default_url = APIS[api]
    return cls(model, url or default_url, **kw)


# --- contexto ----------------------------------------------------------------------------------

def _card_texts(conn, names):
    if conn is None:
        return []
    index = decklist._name_index(conn)
    out, done = [], set()
    for name in names:
        base = re.sub(r"(\s+\d+/\d+)?(\s*\(.*\))?(\s*×\d+)?$", "", name).split(" // ")[0].strip()
        key = decklist._key(base)
        card = index.get(key)
        if card is None or key in done:
            continue
        done.add(key)
        text = (card["oracle_text"] or "").replace("\n", " ")
        stats = f" {card['power']}/{card['toughness']}" if card["power"] else ""
        out.append(f"- {card['name']} {card['mana_cost'] or ''} ({card['type_line']}{stats}): {text[:MAX_CARD_TEXT]}")
    return out


def find_deck_file(deck_cards, decks_dir=None):
    """Arquivo em `decks/` cuja lista mais coincide com o deck enviado ao Arena (o nome no
    Arena, como "Turn 2 Kill", não bate com o nome do arquivo)."""
    folder = Path(decks_dir) if decks_dir else Path(__file__).resolve().parents[2] / "decks"
    wanted = {decklist._key(n.split(" // ")[0]) for n in (deck_cards or {})}
    if not wanted or not folder.exists():
        return None
    best, best_score = None, 0
    for path in folder.rglob("*.md"):
        try:
            deck = decklist.parse(path.read_text("utf-8"), markdown=True)
        except (OSError, ValueError):
            continue
        names = {decklist._key(e.name.split(" // ")[0]) for e in deck.entries()}
        score = len(names & wanted)
        if score > best_score:
            best, best_score = path, score
    return best if best_score >= max(3, len(wanted) // 2) else None


def deck_plan(path):
    """Trechos do arquivo do deck que explicam o plano (seções com 'estratégia', 'plano',
    'linha' ou 'como' no título), limitados em tamanho."""
    if path is None:
        return ""
    text = Path(path).read_text("utf-8")
    sections = re.split(r"(?m)^(#{2,3} .*)$", text)
    chosen = []
    for i in range(1, len(sections) - 1, 2):
        title = sections[i].lower()
        if any(word in title for word in ("estrat", "plano", "linha", "como ", "papel", "jogar")):
            chosen.append(sections[i] + "\n" + sections[i + 1].strip())
    plan = "\n\n".join(chosen) or text
    return plan[:MAX_PLAN_CHARS]


def build_context(snapshot, events=None, conn=None, plan="", deck_name=""):
    """Texto que o modelo recebe: plano, cartas com texto, mesa, dicas e últimos lances."""
    parts = []
    if plan:
        parts.append(f"PLANO DO DECK{(' (' + deck_name + ')') if deck_name else ''}:\n{plan}")
    visible = list(snapshot.get("hand", [])) + snapshot.get("my_field", []) + snapshot.get("opp_field", [])
    texts = _card_texts(conn, visible)
    if texts:
        parts.append("TEXTO DAS CARTAS VISÍVEIS:\n" + "\n".join(texts))
    parts.append("MESA AGORA (começo do seu turno):\n" + snapshot.get("text", ""))
    if snapshot.get("hints"):
        parts.append("FATOS CALCULADOS:\n" + "\n".join(f"- {h}" for h in snapshot["hints"]))
    if events:
        recent = [e["text"] for e in events if e.get("turn") and e["turn"] <= snapshot.get("turn", 0)][-12:]
        if recent:
            parts.append("ÚLTIMOS LANCES:\n" + "\n".join(f"- {t}" for t in recent))
    parts.append("Pergunta: qual é a melhor jogada neste turno? Responda só o JSON pedido.")
    return "\n\n".join(parts)


def context_from_record(record, turn=None, conn=None, decks_dir=None, deck_file=None):
    """Contexto a partir de um registro de partida (spec 011). Sem `turn`, o último turno
    seu com instantâneo. Devolve (contexto, turno, arquivo do deck)."""
    snapshots = record.get("snapshots") or {}
    if not snapshots:
        raise RuntimeError("O registro não tem instantâneos de turno (gravado antes da spec 012).")
    turns = sorted(int(k) for k in snapshots)
    chosen = turn if turn is not None else turns[-1]
    if str(chosen) not in snapshots:
        raise RuntimeError(f"Sem instantâneo do turno {chosen}; turnos disponíveis: {turns}")
    deck = record.get("deck") or {}
    path = Path(deck_file) if deck_file else find_deck_file(deck.get("cards"), decks_dir)
    plan = deck_plan(path)
    context = build_context(snapshots[str(chosen)], record.get("events"), conn, plan, deck.get("name") or "")
    return context, chosen, path


def format_answer(answer):
    if "erro" in answer:
        return f"» conselheiro local: {answer['erro']}"
    speed = f", {answer['tokens_s']} tokens/s" if answer.get("tokens_s") else ""
    return (f"» opinião do modelo local ({answer['modelo']}, {answer['segundos']} s{speed}; confiança {answer['confianca']}):\n"
            f"  jogada: {answer['jogada']}\n  motivo: {answer['motivo']}\n  risco: {answer['risco']}")


def default_records_dir():
    return db.DATA_DIR / "games"
