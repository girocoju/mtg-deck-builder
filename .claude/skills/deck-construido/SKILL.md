---
name: deck-construido
description: Constrói ou ajusta um deck de Magic de 60 cartas com sideboard para formatos de construído (Standard, Pioneer, Modern, Legacy, Vintage, Pauper, Historic, Timeless, Alchemy). Use quando o usuário pedir para criar, montar ou ajustar um deck nesses formatos, inclusive "deck anti meta", "deck barato", "deck em volta da carta X" ou "ajuste minha lista para o meta". Não use para Commander/Brawl nem para draft.
---

# Deck builder de construído

Siga as etapas na ordem. As ferramentas ficam em `.venv\Scripts\mtg` (ver `CLAUDE.md`).
Princípios que não se negociam: carta citada é carta consultada na base; lista entregue
é lista validada; meta é dado com data.

## 1. Entender o pedido

Extraia do pedido: **formato**, **plataforma** (Arena, MTGO, papel), **BO1 ou BO3** e
restrições (cores, orçamento, cartas obrigatórias, arquétipo desejado).

- Pergunte só o que for indispensável e não puder ser assumido. Se faltar o modo, assuma
  BO1 para pedidos do Arena sem menção a torneio e BO3 nos demais casos, e diga o que assumiu.
- Leia as lições do formato em `knowledge/licoes/README.md`.

## 2. Ler o meta e a teoria

- `mtg meta show <formato> --mode <bo1|bo3>`. Se o snapshot BO3 não existir ou tiver mais
  de 14 dias, rode `mtg meta update <formato>`.
- **Sem snapshot do modo pedido** (hoje, todo BO1): diga isso ao usuário. Use o BO3 apenas
  como indício, nomeando-o como tal, ou trabalhe por princípios; nunca apresente o meta
  BO3 como se fosse BO1.
- Leia em `knowledge/`: `arquetipos.md` (sempre; para anti-meta, as seções "Como os
  arquétipos se relacionam" e "Roteiro anti-meta"), `preparacao-e-metagame.md`,
  `papel-no-jogo.md`. O índice `knowledge/README.md` aponta o resto.
- Para os 6 a 10 arquétipos principais, leia as listas de referência (campo `deck` do
  snapshot, via `mtg --json meta show`) e o texto das cartas-chave com `mtg card`.

## 3. Definir o plano

Escreva, antes de escolher cartas:

- o que o campo tem em comum (remoção pontual ou em massa? anulações? cemitério? velocidade?),
  com números do snapshot;
- o arquétipo escolhido, o papel (beatdown ou controle) contra cada deck principal, e como
  o deck vence;
- **modo anti-meta:** para cada deck dominante, que fraqueza é explorada e como ele
  responderá. Prefira um plano proativo cujas cartas naturais já sejam ruins para o campo;
  decida entre "bem mais rápido" e "um pouco maior"; ódio estreito só no principal quando
  o alvo é grande parte do meta.

Quando existir no snapshot um arquétipo próximo do plano, **use a lista dele como modelo**
(templating, `knowledge/base-de-mana.md` Parte 1) e registre cada alteração e o motivo.

## 4. Selecionar as cartas

- Busque na base: `mtg search --format <formato> --game <plataforma> ...` e confira o
  texto de toda carta com `mtg card`. Nenhuma carta entra de memória.
- Número de cópias: `knowledge/quantidade-de-copias.md`. Avaliação de cartas:
  `knowledge/valor-das-cartas.md`.
- Orçamento: `mtg deck cost` (USD, EUR, tix, wildcards). Mostre o custo e que o limite
  pedido foi respeitado.

## 5. Base de mana

- Salve a lista em `decks/<formato>/<nome>.md` (modelo em `decks/README.md`; sufixo `-bo1`
  para listas de melhor-de-um) e rode `mtg deck analyze`.
- Resolva ou justifique cada alerta. Terrenos pela fórmula e fontes pela tabela de
  `knowledge/base-de-mana.md`; em BO1 no Arena, aplique a seção 1.4 (aggro de curva baixa
  pode cortar 1 a 2 terrenos; os demais não).

## 6. Sideboard

- 15 cartas, com plano contra cada arquétipo principal: o que entra, o que sai, por quê
  (`knowledge/sideboard.md`). Entradas e saídas têm de fechar em número.
- Em BO1 não há troca entre jogos: a lista principal precisa ser mais robusta, e o
  sideboard só serve a efeitos que buscam cartas de fora do jogo.

## 7. Validar

`mtg deck validate <arquivo> --format <formato> --game <plataforma>` até passar sem erros.

## 8. Entregar

**Nomes para o Arena:** a lista que vai para o usuário e para o bloco de código do arquivo
do deck é sempre a saída de `mtg deck export <arquivo> --to arena`, nunca nomes digitados
à mão. O Arena recusa cartas de duas faces escritas com os dois nomes (`Tithing Blade //
Consuming Sepulcher`): ele quer só a face da frente (`Tithing Blade`). Depois de trocar o
bloco, rode a validação de novo; ela avisa se sobrar algum nome assim.

Na resposta e no arquivo do deck:

1. lista exportável (`mtg deck export --to arena|mtgo|text`);
2. leitura do meta, com **fonte, data e modo** do snapshot;
3. por que este deck (raciocínio deck a deck, no modo anti-meta) e o plano de jogo;
4. papel de cada grupo de cartas;
5. guia de sideboard por matchup;
6. pontos fracos;
7. custo;
8. honestidade: é uma proposta fundamentada, não testada em jogo; diga o que observar nos testes.

Peça o retorno dos testes e registre o que o usuário relatar como lição
(`knowledge/COMO-ADICIONAR.md`).
