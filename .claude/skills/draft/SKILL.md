---
name: draft
description: Limitado de Magic (draft e selado) por coleção — cria ou atualiza o guia de draft de uma coleção, recomenda um pick dado um pacote e as cartas já escolhidas, e monta o deck de 40 cartas a partir de um pool. Use quando o usuário pedir "estratégia de draft para a coleção X", perguntar pelas melhores comuns ou pares de cores de uma coleção, pedir ajuda com um pick ou mandar um pool de draft ou selado para montar. Não use para formatos de construído nem para Commander/Brawl.
---

# Especialista em draft

Ferramentas em `.venv\Scripts\mtg` (ver `CLAUDE.md`). Leia antes
`knowledge/limitado-e-draft.md` — princípios de limitado e a seção "Ler dados de win
rate", com as métricas e os vieses do 17Lands — e as lições em `knowledge/licoes/README.md`.

Regras fixas: toda carta citada pertence à coleção e foi consultada; todo número vem com
**fonte, data, modo e tamanho da amostra**; dados de um modo não valem para outro.

## 0. Identificar a coleção e o modo

- `mtg sets "<nome ou código>"`. Se a coleção for recente, rode `mtg sync` antes.
- Modo: `premier` (padrão), `quick`, `trad` (BO3), `sealed`, `tradsealed`, `picktwo`.
  Se o usuário não disser, use Premier Draft e diga isso. Em Quick Draft, lembre que os
  bots escolhem diferente de humanos.
- `mtg draft update <coleção> --mode all` coleta o 17Lands (no máximo uma vez por dia).
  - **Com dados:** siga com os números.
  - **Sem dados** (coleção recém-lançada, só de papel, ou modo sem amostra): trabalhe em
    **modo teórico** e declare isso no começo da resposta e do guia.

## A. Guia da coleção

Salve em `drafts/<código>.md`. Use `drafts/fra.md` como modelo de estrutura.

1. **Leitura da coleção:** `mtg draft set <coleção>` (cartas por cor e raridade, curva de
   criaturas e remoção nas comuns e incomuns, palavras-chave). Leia com `mtg card` o
   texto das mecânicas e das cartas que for citar. A coluna de remoção é classificação
   automática: confira.
2. **Com dados**, colete:
   - `mtg draft colors <coleção>` — pares de cores;
   - `mtg draft cards <coleção> --color <W|U|B|R|G|multi|colorless> --rarity <common|uncommon>` — rankings;
   - `mtg draft cards <coleção> --limit 15` — bombas;
   - `mtg draft gaps <coleção>` — subestimadas e superestimadas;
   - os mesmos comandos com `--mode` para os outros modos que tiverem dados.
3. **Escreva o guia** com estas seções: cabeçalho (fonte, data, modo, jogos, média dos
   usuários, aviso de amostra); visão geral (mecânicas, velocidade, cores fortes e
   fracas, remoção); os dez pares (win rate, sinalizadoras, plano); ranking de comuns e
   incomuns por cor; bombas; prioridade de picks e sinais; armadilhas; construção do
   deck; outros modos; limites do guia. Se o usuário indicar artigos ou guias externos,
   ingira-os pelo processo de `knowledge/COMO-ADICIONAR.md` e acrescente a seção "O que
   dizem os guias externos", confrontando cada afirmação com os dados (modelo em
   `drafts/fra.md`); o Untapped.gg serve de segunda fonte de dados (como obter em
   `knowledge/fontes.md`, seção 6).
4. **Interprete, não só transcreva:** compare cada número com a média dos usuários do
   snapshot; ranqueie dentro da cor; desconte o viés de cartas caras; trate como incerto
   o que tiver poucos jogos e diga quantos são.
5. **Modo teórico:** mesmas seções, preenchidas pela leitura das cartas e pelos
   princípios do livro; as que dependem de dados dizem explicitamente que não podem ser
   preenchidas. Modelo: `drafts/trk.md`.

## B. Recomendar um pick

Entrada: as cartas do pacote, as já escolhidas e o número do pacote e do pick.

1. `mtg draft pick <coleção> "Carta A" "Carta B" ... --pack N --pick M --picked "X" "Y"`
   (as cartas do pacote vêm logo depois da coleção; com `--state <arquivo>` o comando
   acumula os picks entre chamadas e dispensa `--picked`). A tabela traz a nota de cada
   carta e os componentes: **poder** (fonte: `17lands`, `untapped`, `draftsim*` ou
   `teorica*`; asterisco = sem amostra de partidas), **encaixe** nas cores já escolhidas
   (peso cresce com o pick), **par**, **necessidade** (função vazia no deck),
   **sinal** (ALSA contra o pick, cores que já passaram), **flexibilidade**, **sinergia**
   (payoff ou enabler do arquétipo do par escolhido, pelos padrões de
   `archetypes/<coleção>.json`; a coluna "arquétipos" lista os pares que a carta serve,
   com `+` para payoff) e a chance estimada de a carta dar a volta.
   `mtg draft synergy <coleção>` mostra os dez arquétipos, as cartas marcadas e se a
   marcação carrega sinal nos dados (em FRA, quase nenhum: a sinergia desempata, não
   decide).
2. A tabela é ponto de partida, não veredito: confira o texto das cartas com `mtg card`
   quando a diferença for pequena ou a nota for teórica, e pese o que o motor não vê
   (sinergias da coleção, splash, o que o guia `drafts/<código>.md` diz do par).
3. Responda com **um pick**, a justificativa em duas ou três frases citando os
   componentes, a segunda opção e o que o pacote sinaliza. Diga a fonte e a data dos dados.

## D. Acompanhar um draft ao vivo no Arena

Pré-requisitos: no Arena, *Opções > Conta > Detailed Logs (Plugin Support)* ligado; para
a janela flutuante, Arena em modo janela ou tela cheia sem bordas. Nada sai da máquina.

O caminho normal é o **Oráculo** (`mtg arena companion`), instalado como tarefa agendada
do Windows em 2026-11-07: dispara no login, espera o Arena abrir, mostra a janela sozinho
e nela aparecem tanto o ranking de cada pacote quanto a partida em curso (mão, campos,
cemitérios, exílio, dicas). `--status` diz se está rodando; `--start` reabre; `--stop`
encerra; o registro fica em `data/companion.log`. Os passos abaixo valem para rodar à mão.

1. Antes de gastar a ficha: `mtg draft watch --check --set <coleção>` confere o log, a
   opção de logs detalhados, a base de cartas do Arena e os dados da coleção.
2. Antes de entrar no evento: `mtg draft watch --window` (sem `--window`, a saída vai
   para o terminal). A cada pacote a janela mostra o ranking da seção B; cada pick fica
   registrado em `data/drafts/<data>-<evento>.json`. Teclas: Esc fecha, + e - mudam a
   fonte, F troca de canto.
3. Se o primeiro pick não aparecer antes da escolha (há relato de que o Arena não grava
   o evento do P1P1), a mensagem combinada registra o pacote e o pick depois; para
   pontuar antes, digite o pacote em `mtg draft pick`.
4. No fim: `mtg draft pool <estado> --to arena` e siga a seção C. Registre no `tasks.md`
   da spec 010 se o P1P1 apareceu e quantos picks foram reconhecidos; guarde um trecho
   anonimizado do log em `tests/fixtures/`.

Testes sem ficha: `mtg draft watch --file tests/fixtures/player-log-premier-fra-sintetico.txt`
reproduz um draft de 42 picks; `mtg arena watch --window` numa partida comum mostra deck
enviado, oponente, turnos, vida e resultado (prova que o log está sendo lido ao vivo);
`mtg draft sim <coleção>` treina picks contra sete bots (`--booster paper` usa a colação
do Play Booster de papel; `--auto N` mede o que a mesa deixa aberto).

## C. Montar o deck de 40 a partir de um pool

1. Salve o pool em arquivo e rode `mtg draft rate <coleção> --file <pool>`: a saída vem
   agrupada por cor.
2. Escolha as duas cores com mais cartas acima da média e a melhor remoção; confira o par
   em `mtg draft colors`. Splash só para bombas ou remoção de um símbolo colorido, com
   fontes para isso.
3. Monte 23 mágicas e 17 terrenos (16 em curva muito baixa, 18 em curva alta ou pool
   curto): criaturas na curva, remoção, e corte primeiro o que está abaixo da média.
4. Salve em `decks/limited/<nome>.md` e rode `mtg deck validate <arquivo> --format limited`
   e `mtg deck analyze <arquivo>`. A análise não tem o conceito de splash: um alerta de
   cor para a carta do splash é esperado e deve ser explicado. Terrenos que entram
   virados "a menos que" são contados como desvirados.
5. Entregue a lista, o porquê das cores, o que ficou de fora e os compromissos assumidos.
   A lista entregue é a saída de `mtg deck export <arquivo> --to arena`: o Arena recusa
   cartas de duas faces escritas com os dois nomes.

## Entrega e honestidade

Diga sempre de quando são os dados e quantos jogos sustentam cada afirmação. Guia e deck
são propostas: peça o retorno das partidas e registre como lição
(`knowledge/COMO-ADICIONAR.md`). Guias devem ser regenerados quando os dados mudarem.
