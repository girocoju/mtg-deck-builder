import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from mtg_builder import advisor
from test_decks import conn  # noqa: F401

SNAPSHOT = {"turn": 4, "life": {1: 20, 2: 14}, "hand": ["Bear", "Elk"], "my_field": ["Forest ×3", "Imp 1/1"],
            "opp_field": ["Island ×2", "Drake 2/2 (virada)"], "my_graveyard": [], "opp_graveyard": [],
            "opp_hand": 5, "open_mana": {"me": 3, "opp": 0},
            "hints": ["sem letal no ataque: 1 de poder podem atacar contra 14 de vida (sem contar 0 bloqueador(es))"],
            "text": "jogo 1 · turno 4 · principal 1 · ativo: você · vida: você 20 × Rival 14\nsua mão (2): Bear · Elk"}
EVENTS = [{"turn": 3, "phase": "principal 1", "step": "", "text": "Rival conjura Drake"},
          {"turn": 4, "phase": "início", "step": "compra", "text": "você compra Elk"}]


class FakeOllama(BaseHTTPRequestHandler):
    answer = {"jogada": "Jogue Forest e conjure Elk", "motivo": "maior ameaça disponível", "risco": "Rival tem 5 cartas",
              "confianca": "media"}
    seen = []

    def do_GET(self):
        self._reply({"models": [{"name": "qwen2.5:7b"}]})

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        FakeOllama.seen.append(body)
        self._reply({"message": {"role": "assistant", "content": json.dumps(self.answer)}, "done": True,
                     "eval_count": 40, "eval_duration": 4_000_000_000})

    def _reply(self, data):
        payload = json.dumps(data).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        pass


@pytest.fixture
def server():
    httpd = HTTPServer(("127.0.0.1", 0), FakeOllama)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{httpd.server_port}"
    httpd.shutdown()


def test_context_has_plan_cards_board_hints_and_events(conn):  # noqa: F811
    context = advisor.build_context(SNAPSHOT, EVENTS, conn, plan="## Estratégia\nBater forte.", deck_name="Ursos")
    assert "PLANO DO DECK (Ursos)" in context and "Bater forte." in context
    assert "TEXTO DAS CARTAS VISÍVEIS" in context and "- Bear" in context and "- Drake" in context
    assert "- Forest" in context                                   # nome sem o "×3"
    assert "MESA AGORA" in context and "FATOS CALCULADOS" in context and "sem letal" in context
    assert "ÚLTIMOS LANCES" in context and "você compra Elk" in context
    assert context.rstrip().endswith("Responda só o JSON pedido.")


def test_ask_parses_json_and_measures_speed(server):
    client = advisor.OllamaAdvisor("qwen2.5:7b", server)
    assert client.available() and client.models() == ["qwen2.5:7b"]
    answer = client.ask("contexto")
    assert answer["jogada"] == "Jogue Forest e conjure Elk" and answer["confianca"] == "media"
    assert answer["tokens_s"] == 10.0 and answer["modelo"] == "qwen2.5:7b"
    sent = FakeOllama.seen[-1]
    assert sent["format"] == "json" and sent["stream"] is False and sent["messages"][0]["role"] == "system"
    assert "Responda SOMENTE um JSON" in sent["messages"][0]["content"] and sent["messages"][1]["content"] == "contexto"
    text = advisor.format_answer(answer)
    assert text.startswith("» opinião do modelo local (qwen2.5:7b") and "jogada: Jogue Forest" in text


class FakeOpenAI(BaseHTTPRequestHandler):
    seen = []

    def do_GET(self):
        self._reply({"object": "list", "data": [{"id": "qwen2.5-7b-instruct", "object": "model"}]})

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        FakeOpenAI.seen.append((self.path, body))
        content = "Claro! " + json.dumps(FakeOllama.answer)          # texto em volta do JSON: o cliente extrai
        self._reply({"model": "qwen2.5-7b-instruct", "choices": [{"message": {"role": "assistant", "content": content}}],
                     "usage": {"completion_tokens": 30}})

    _reply = FakeOllama._reply
    log_message = FakeOllama.log_message


@pytest.fixture
def openai_server():
    httpd = HTTPServer(("127.0.0.1", 0), FakeOpenAI)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{httpd.server_port}"
    httpd.shutdown()


def test_openai_compatible_api_for_localai(openai_server):
    client = advisor.make_advisor("openai", "qwen2.5-7b-instruct", openai_server)
    assert isinstance(client, advisor.OpenAICompatibleAdvisor)
    assert client.available() and client.models() == ["qwen2.5-7b-instruct"]
    answer = client.ask("contexto")
    assert answer["jogada"] == "Jogue Forest e conjure Elk" and answer["modelo"] == "qwen2.5-7b-instruct"
    path, body = FakeOpenAI.seen[-1]
    assert path == "/v1/chat/completions" and body["response_format"] == {"type": "json_object"}
    assert body["max_tokens"] == 220 and body["messages"][1]["content"] == "contexto"
    assert advisor.make_advisor("openai").url == "http://localhost:8080"
    with pytest.raises(RuntimeError, match="API desconhecida"):
        advisor.make_advisor("outra")


def test_unavailable_server_fails_softly():
    client = advisor.OllamaAdvisor("x", "http://127.0.0.1:9", timeout=2)
    assert client.available() is False and client.models() == []
    answer = client.ask("contexto")
    assert "erro" in answer and "indisponível" in answer["erro"]
    assert advisor.format_answer(answer).startswith("» conselheiro local:")


def test_record_context_and_deck_match(tmp_path, conn):  # noqa: F811
    decks = tmp_path / "decks" / "standard"
    decks.mkdir(parents=True)
    (decks / "ursos.md").write_text("# Ursos\n\n```\nDeck\n4 Bear\n4 Elk\n4 Imp\n20 Forest\n```\n\n## Estratégia\n\nBater.\n",
                                    encoding="utf-8")
    (decks / "outro.md").write_text("# Outro\n\n```\nDeck\n4 Drake\n20 Island\n```\n", encoding="utf-8")
    record = {"deck": {"name": "Turn 2 Kill", "cards": {"Bear": 4, "Elk": 4, "Imp": 4, "Forest": 20}},
              "events": EVENTS, "snapshots": {"2": {**SNAPSHOT, "turn": 2}, "4": SNAPSHOT}}
    context, turn, path = advisor.context_from_record(record, None, conn, decks_dir=tmp_path / "decks")
    assert turn == 4 and path.name == "ursos.md" and "Bater." in context and "turno 4" in context
    _context, turn, _path = advisor.context_from_record(record, 2, conn, decks_dir=tmp_path / "decks")
    assert turn == 2
    with pytest.raises(RuntimeError, match="turnos disponíveis"):
        advisor.context_from_record(record, 3, conn, decks_dir=tmp_path / "decks")
    with pytest.raises(RuntimeError, match="instantâneos"):
        advisor.context_from_record({"snapshots": {}}, None, conn)
