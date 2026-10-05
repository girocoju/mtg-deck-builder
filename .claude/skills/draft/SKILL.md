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
   deck; outros modos; limites do guia.
4. **Interprete, não só transcreva:** compare cada número com a média dos usuários do
   snapshot; ranqueie dentro da cor; desconte o viés de cartas caras; trate como incerto
   o que tiver poucos jogos e diga quantos são.
5. **Modo teórico:** mesmas seções, preenchidas pela leitura das cartas e pelos
   princípios do livro; as que dependem de dados dizem explicitamente que não podem ser
   preenchidas. Modelo: `drafts/trk.md`.

## B. Recomendar um pick

Entrada: as cartas do pacote e as já escolhidas (e o número do pick, se informado).

1. `mtg draft rate <coleção> "Carta A" "Carta B" ...` para o pacote, e de novo com
   `--file` para as já escolhidas.
2. Decida pesando, nesta ordem: poder bruto (GIH WR contra a média; bombas e remoção);
   cores já escolhidas e o quanto o jogador está comprometido (picks 1 a 4 priorizam
   poder, do meio do segundo pacote em diante priorizam o deck); força do par de cores;
   o que o deck ainda precisa (curva, remoção, criaturas); sinais (ALSA da carta contra
   o pick atual).
3. Responda com **um pick**, a justificativa em duas ou três frases, a segunda opção e o
   que o pacote sinaliza. Cartas sem dados: avalie pelo texto e diga que é avaliação teórica.

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

## Entrega e honestidade

Diga sempre de quando são os dados e quantos jogos sustentam cada afirmação. Guia e deck
são propostas: peça o retorno das partidas e registre como lição
(`knowledge/COMO-ADICIONAR.md`). Guias devem ser regenerados quando os dados mudarem.
