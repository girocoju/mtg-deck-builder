# 012 — Conselheiro local (Ollama)

**Status:** ⏸️ Adiada pelo usuário em 2026-11-07 ("vai onerar muito a máquina com o jogo rodando junto"). Cliente, contexto e comando de teste ficam prontos para quando houver outra máquina ou GPU; nada roda por padrão.

## Objetivo

Dar ao Oráculo (specs 010 e 011) uma opinião de jogada ao vivo sem custo por chamada e
sem chave de API: um modelo de linguagem rodando na própria máquina, pelo
[Ollama](https://github.com/ollama/ollama), que recebe a visão da partida do rastreador
(mão, campos, cemitérios, exílio, vida, dicas calculáveis) e o plano do deck, e devolve
uma sugestão curta, marcada como opinião, na janela.

Pedido do usuário em 2026-11-07: "podemos construir uma IA local com Ollama para isso?
Assim fica mais barato e rápido."

## O que é possível na máquina do usuário (conferido em 2026-11-07)

- CPU Intel i5-12400F (6 núcleos), 31,7 GB de RAM, GPU AMD Radeon RX 6400 (4 GB).
- O Ollama não está instalado.
- A RX 6400 (gfx1034) não está na lista oficial de GPUs AMD do Ollama no Windows (só
  RX 7000 e PRO W7000); o caminho possível é o backend Vulkan, sem confirmação encontrada
  para este modelo; na dúvida, o Ollama cai para a CPU sem avisar (`ollama ps` mostra a
  coluna PROCESSOR). Fontes: [docs.ollama.com/gpu](https://docs.ollama.com/gpu.md),
  [ollama-for-amd (fork comunitário)](https://github.com/likelovewant/ollama-for-amd/wiki).
- Na CPU, modelos de 3 a 8 bilhões de parâmetros em quantização de 4 bits cabem com
  folga na RAM; a velocidade esperada é de poucos tokens por segundo (uma resposta de 80
  palavras leva de 10 a 30 s). É aceitável para "no começo do seu turno", não para cada
  prioridade. Medir antes de prometer.
- API: `POST http://localhost:11434/api/chat` com `model`, `messages` (role, content),
  `stream: false`, `options` (`temperature`, `num_predict`), `format: "json"` ou um
  esquema JSON, `keep_alive`; resposta em `message.content`, com `eval_count` e
  `eval_duration` para medir tokens por segundo. `GET /api/tags` lista os modelos.

## O que o modelo local sabe e o que não sabe

Um modelo de 7 bilhões não conhece as cartas de Reality Fracture nem as regras finas; vai
inventar textos de carta se não os receber. Por isso o conselheiro **recebe tudo pronto**:
o texto de regras das cartas visíveis (base local), o plano e as linhas do deck (arquivo
em `decks/`), a visão da partida e as dicas calculáveis (letal, mana aberta), e é
instruído a só escolher entre jogadas que o rastreador listou como possíveis. A opinião
sai sempre com o rótulo "opinião do modelo local" e nunca substitui as dicas calculáveis.

## Histórias de uso

- "No começo do meu turno, me diga em uma frase o que jogar e por quê."
- "Tenho letal? Se não, atacar com o quê?" (a conta é do rastreador; o modelo explica
  e escolhe entre as opções)
- "Depois da partida, reveja o registro e aponte o lance em que eu errei." (fora do
  tempo real, pode usar um modelo maior)

## LocalAI como alternativa (pergunta do usuário em 2026-11-07)

O [LocalAI](https://github.com/mudler/LocalAI) serve para o mesmo papel: roda modelos
GGUF na máquina e expõe a API no formato da OpenAI (`GET /v1/models`,
`POST /v1/chat/completions`, porta 8080). Diferenças que pesam aqui:

- **Windows:** a versão v4.12.1 (2026-10-23) só tem binários para Linux (amd64, arm64)
  e macOS; no Windows ele roda por Docker Desktop (WSL2), com a imagem `localai/localai:latest`
  (CPU) ou `latest-gpu-vulkan`. O Ollama tem instalador nativo para Windows.
- **GPU:** a RX 6400 não é suportada oficialmente em nenhum dos dois; no Docker do
  Windows o caminho prático é só a CPU.
- **API:** o cliente do projeto fala as duas: `--api ollama` (nativa, `/api/chat`) e
  `--api openai`, que atende LocalAI, LM Studio, o servidor do llama.cpp e o próprio
  Ollama em `/v1`. Trocar de servidor é trocar a opção e a porta, sem mexer no contexto
  nem no formato da resposta.

Recomendação para esta máquina: Ollama, por ser instalação nativa. LocalAI fica como
opção pronta se o usuário preferir o padrão OpenAI ou um servidor com vários modelos.

## Requisitos

1. **Cliente local** (`advisor.py`): descobre se o servidor responde, lista modelos,
   chama o modelo sem streaming com limite de tokens e temperatura baixa, mede a
   latência e os tokens por segundo, e falha em silêncio (a janela segue sem conselho).
   Duas APIs: a nativa do Ollama e a compatível com a OpenAI (LocalAI e outros).
2. **Montagem do contexto:** visão da partida (`board_text`), textos de regras das cartas
   na sua mão e nos dois campos (`mtg card` pela base), plano do deck (seção "Estratégia"
   e "Linhas" do arquivo do deck em `decks/`, encontrado pelo nome do deck enviado),
   dicas calculáveis, e a lista de ações possíveis que o log traz (`actions`: conjurar,
   jogar terreno, ativar). Tamanho limitado (cerca de 2.000 tokens).
3. **Quando perguntar:** uma vez por turno seu, ao entrar na primeira fase principal, e
   quando o usuário pedir (tecla na janela). Nunca no turno do oponente.
4. **Formato da resposta:** JSON com `jogada` (uma frase), `motivo` (uma frase), `risco`
   (uma frase) e `confianca` (baixa, média, alta), mostrado na janela sob o rótulo
   "» opinião do modelo local (<modelo>, <segundos>)".
5. **Comando de teste fora do jogo:** `mtg arena advise <registro.json> --turn N` monta
   o contexto a partir de uma partida gravada (spec 011) e imprime a resposta, para
   avaliar modelos e prompts sem jogar.
6. **Avaliação antes de confiar:** com os registros de partidas reais, comparar a
   sugestão do modelo com o lance que venceu ou perdeu; registrar em `knowledge/licoes/`
   o que o modelo acerta e erra. Só ligar por padrão na janela depois disso.
7. **Honestidade:** modelo, latência e tokens por segundo aparecem com cada resposta;
   sem Ollama ou sem modelo, a janela diz "conselheiro desligado" uma vez e segue.

## Critérios de aceite

- [ ] Com um servidor Ollama simulado nos testes, o cliente monta o contexto de um
      registro real (spec 011), recebe o JSON e o mostra formatado; sem servidor, nada
      quebra.
- [ ] `mtg arena advise` sobre o registro da partida de 2026-11-07 no turno 10 produz uma
      resposta em menos de 30 s na máquina do usuário, com o modelo e a velocidade
      impressos (registrar modelo, tempo e resposta em `tasks.md`).
- [ ] Em cinco turnos de partidas reais, a sugestão é comparada com o que aconteceu e o
      resultado fica registrado como lição.

## Dependências

Specs 010 e 011; instalação do Ollama e de ao menos um modelo pelo usuário
(`ollama pull <modelo>`); base de cartas (001) para os textos.

## Fora do escopo

- Decidir pelo usuário ou agir no jogo.
- Treinar ou ajustar modelos.
- Rodar o modelo durante o draft (o motor de picks já cobre; pode entrar depois).

## Questões em aberto

- Modelo inicial: começar pelo menor que responda de forma coerente (3 a 4 bilhões de
  parâmetros) e medir; subir para 7 a 8 bilhões se a latência couber.
- GPU: testar o backend Vulkan com a RX 6400; se cair na CPU, aceitar a CPU.
- Trigger por tecla na janela (tkinter) e no PowerShell: definir a tecla (sugestão: "?").
