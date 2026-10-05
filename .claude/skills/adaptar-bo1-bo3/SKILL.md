---
name: adaptar-bo1-bo3
description: Adapta um deck de construído de 60 cartas entre melhor-de-três (BO3) e melhor-de-um (BO1), nos dois sentidos — "adapte o deck em questão BO3 para BO1", "quero jogar esta lista de torneio na ranqueada BO1", "monte o sideboard para jogar este deck em BO3". Use quando já existe uma lista (da conversa, de um arquivo em decks/ ou colada) e o pedido é mudar o modo de jogo, não criar um deck novo nem mudar de formato.
---

# Adaptação de deck entre BO3 e BO1

Ferramentas em `.venv\Scripts\mtg` (ver `CLAUDE.md`). Leia antes `knowledge/sideboard.md`,
`knowledge/papel-no-jogo.md` e a seção 1.4 de `knowledge/base-de-mana.md` (mão inicial em
BO1), além das lições em `knowledge/licoes/README.md`.

O que muda de um modo para o outro:

- **BO3:** os jogos 2 e 3 são corrigidos pelo sideboard, então a lista principal pode ser
  especializada.
- **BO1:** não há troca entre jogos. Carta morta fica morta; respostas flexíveis valem
  mais que respostas estreitas. O sideboard (até 15) só serve a efeitos que buscam cartas
  de fora do jogo. No Arena, a mão inicial é suavizada (só a quantidade de terrenos, não
  as cores), e o campo costuma ter mais aggro e decks lineares.

## 1. Receber a lista e a direção

- Origem: deck da conversa, arquivo em `decks/` ou lista colada (salve em arquivo).
  Direção padrão: BO3 → BO1. Confirme o formato.
- Valide a origem: `mtg deck validate <arquivo> --format <formato>`. Se houver erro,
  aponte antes de adaptar.

## 2. Diagnosticar a origem

- `mtg deck analyze <arquivo>`; leia o texto das cartas que não conhecer (`mtg card`).
- Escreva: plano de jogo, papel de cada grupo de cartas e, para cada carta do sideboard,
  **contra que matchup ela entra**.
- Pergunta decisiva: o deck **depende** do sideboard (plano transformacional, ou perde o
  jogo 1 de propósito contra parte do campo)? Se sim, diga isso logo e, em BO3 → BO1,
  sugira alternativa em vez de entregar uma adaptação ruim sem aviso.

## 3. Ler o meta do modo de destino

`mtg meta show <formato> --mode <bo1|bo3>`.

- **Há snapshot:** adapte contra o campo medido e cite fonte, data e modo.
- **Não há** (hoje, todo BO1): adapte por princípios e **declare a adaptação como
  teórica**. O meta do outro modo pode ser citado só como indício, com esse nome.

## 4a. BO3 → BO1

1. **Corte o que é estreito** na lista principal: ódio dedicado e cartas que só servem
   contra uma fatia do campo — a não ser que o snapshot BO1 mostre que o alvo é grande.
2. **Promova do sideboard** o que vale contra a maior parte do campo; prefira respostas
   que tenham alvo em qualquer deck.
3. **Terrenos:** aggro de curva baixa pode cortar 1 ou 2 em relação à fórmula; midrange,
   controle e ramp não cortam. Cores não são suavizadas: mantenha as fontes por cor.
4. **Sideboard:** mantenha só se o deck tiver efeitos que buscam cartas de fora do jogo,
   e monte-o em função deles; senão, entregue sem sideboard.

## 4b. BO1 → BO3

1. **Reponha os terrenos** cortados para BO1, se houver.
2. **Revise a lista principal:** cartas que estavam lá só por flexibilidade podem dar
   lugar ao melhor plano do jogo 1; respostas situacionais descem para o sideboard.
3. **Monte o sideboard de 15** contra os arquétipos do snapshot BO3
   (`knowledge/sideboard.md`): para cada matchup principal, o que entra e o que sai —
   **as quantidades têm de fechar**.

## 5. Conferir

- `mtg deck validate <novo> --format <formato> --game <plataforma>` até passar.
- `mtg deck analyze <novo>` e compare a base de mana com a da origem (antes e depois).
- `mtg deck diff <origem> <novo>` para a tabela de trocas.
- Toda carta nova foi consultada com `mtg card` e é legal no formato.

## 6. Entregar

Salve ao lado da origem (`decks/<formato>/<nome>-bo1.md` ou `-bo3.md`) e entregue:

1. lista adaptada, exportável (`mtg deck export`);
2. tabela **saiu / entrou / por quê**;
3. o que o deck ganha e o que perde com a adaptação, e os matchups que pioram;
4. base de mana antes e depois;
5. em BO3: guia de sideboard por matchup;
6. fonte, data e **modo** do snapshot usado — ou a declaração de que a adaptação é teórica;
7. o aviso da etapa 2, se o deck depende do sideboard;
8. honestidade: não testado; o que observar; pedir o retorno e registrar como lição.
