# 012 — Tarefas

- [x] `advisor.py`: cliente do Ollama (`/api/tags`, `/api/chat` sem streaming, JSON,
      latência e tokens por segundo, falha em silêncio), montagem do contexto (plano do
      deck por coincidência de lista em `decks/`, textos das cartas visíveis, mesa, fatos
      calculados, últimos lances)
- [x] Instantâneos de turno no registro da partida (`snapshots`, spec 011) para testar
      fora do jogo
- [x] `mtg arena advise <registro> [--turn N] [--dry-run]`; testes com servidor simulado
- [x] API compatível com a OpenAI (`--api openai`: LocalAI, LM Studio, llama.cpp, Ollama em
      `/v1`), com teste de servidor simulado; LocalAI avaliado: sem binário para Windows
      (v4.12.1), só Docker; Ollama recomendado nesta máquina
- [ ] Usuário instala o Ollama (https://ollama.com) e um modelo (`ollama pull qwen2.5:7b`,
      ou um de 3 a 4 bilhões se a CPU for lenta); conferir com `ollama ps` se roda na GPU
      (RX 6400 não é oficialmente suportada no Windows) ou na CPU
- [ ] Medir: `mtg arena advise` sobre a partida de 2026-11-07 (precisa de um registro novo
      com instantâneos: as partidas gravadas antes desta spec não os têm), registrar
      modelo, segundos, tokens/s e a resposta
- [ ] Avaliar em cinco turnos reais antes de ligar na janela
- [ ] Integração na janela do Oráculo (uma pergunta por turno seu, em segundo plano, com
      rótulo de opinião) — só depois da avaliação
