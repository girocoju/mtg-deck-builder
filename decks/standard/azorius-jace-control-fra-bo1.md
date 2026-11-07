# Azorius Jace Control — "Conquistador do Padrão: Reality Fracture" (BO1)

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-10-13
- **Objetivo:** tarefa do Arena: vencer 25 partidas de Standard com pelo menos 20 cards
  não terrenos de Reality Fracture no deck principal. Esta lista tem **22**, conferidos
  pela impressão na base com `mtg deck validate --set fra --min-set 20`; use as versões de FRA de
  cada uma, porque a tarefa conta a impressão
- **Premissa:** deck novo, sem restrição de coleção, construído a partir das cartas mais
  fortes de FRA para construído e do arquétipo do meta BO1 que já as usa
- **Meta de referência:** Untapped.gg, Standard BO1, capturas do usuário de 2026-10-05
  (8 dias; `mtg meta show standard --mode bo1`). O snapshot BO3 (MTGGoldfish, 2026-10-04)
  é anterior ao lançamento de FRA no Arena e não traz nenhuma carta da coleção

```
Deck
3 Countersculpt
4 Day of Judgment
4 Deserted Beach
2 Erode
4 Floodfarm Verge
2 Get Lost
4 Hallowed Fountain
2 Icy Reception
5 Island
2 Memory Trap
4 Meticulous Archive
3 No More Lies
4 Plains
4 Prophesied End
4 Sphinx of False Conclusions
3 The Theorist, Jace Beleren
2 Theorist's Proxy
2 Three Steps Ahead
2 Your Fate Ends Here
```

## Cards de Reality Fracture (22)

Prophesied End 4, Your Fate Ends Here 2, Memory Trap 2, Icy Reception 2, Countersculpt 3,
The Theorist, Jace Beleren 3, Theorist's Proxy 2, Sphinx of False Conclusions 4.

Não contam, e por isso ficam em poucas cópias: Erode (Secrets of Strixhaven), Day of
Judgment, No More Lies, Get Lost, Three Steps Ahead. Conferência pela ferramenta, que
conta pela impressão na base e reprova a lista abaixo do mínimo (saída de 2026-10-13):

    mtg deck validate decks/standard/azorius-jace-control-fra-bo1.md --format standard --game arena --set fra --min-set 20
    standard: 60 no deck principal, 0 no sideboard
    Cartas não terreno de fra no deck principal: 22 de 35 (mínimo 20)
      não contam (5 linhas): 4 Day of Judgment, 2 Erode, 2 Get Lost, 3 No More Lies, 2 Three Steps Ahead
    Lista válida.

`mtg deck setcount <arquivo> --set fra` mostra carta a carta as coleções de cada impressão.

## Por que este arquétipo

- **É o arquétipo do meta BO1 que mais se beneficia de FRA sem mudar de plano.** Azorius
  Control está no snapshot com 4,3% do campo e 53,7% de vitórias (tier B); suas
  cartas-chave já incluem The Theorist, Jace Beleren (52,3% dos decks) e Countersculpt
  (40,5%). Boros Superfriends usa três cartas de FRA (Ajani Unrelenting, Chandra, Torch of
  Defiance, Way of the Pyromancer), mas tem 50,5% e tier C. Chegar a 22 aqui é trocar as
  peças genéricas (Settle the Wreckage, Seam Rip, Consult the Star Charts, parte dos Erode)
  pelas equivalentes de FRA.
- **O campo é de criaturas pequenas.** Mono-White Auras (13,0%), Mono-White Lifegain
  (6,0%), Orzhov Lifegain (5,7%) e Mono-Green Landfall (5,0%) somam 30% dos decks
  identificados (`knowledge/preparacao-e-metagame.md`: ler o que o campo tem em comum).
  Day of Judgment e Prophesied End não se importam com ward nem hexproof das Auras.
- **As melhores cartas de FRA para construído são azuis e brancas:** Jace é um motor de
  compra que o oponente precisa responder; Countersculpt anula qualquer coisa por {U}{U}
  quando há um Jace na mesa ou na mão; Prophesied End mata qualquer criatura por 2 manas;
  Sphinx of False Conclusions é um finalizador que volta quando morre.
- **Papel** (`knowledge/papel-no-jogo.md`): controle em todos os confrontos. O deck não
  corre; ele responde, estabiliza e vence com inevitabilidade (Jace comprando no draw step
  do oponente, Sphinx copiando a si mesma).

## Plano de jogo

1. **Turnos 1 a 3:** Erode, Prophesied End e Get Lost na primeira ameaça (Prophesied End
   em criatura atacando não dá carta ao oponente); Icy Reception anula uma criatura ou
   lenda por {3} a mais ou tira 5 de poder de um atacante. No More Lies e Countersculpt
   (pagando {1}, ou com Jace na mão) nas mágicas que importam. Meticulous Archive faz
   surveil para filtrar terrenos.
2. **Turno 4:** Day of Judgment se a mesa encheu; senão, The Theorist, Jace Beleren. Jace
   compra uma carta no draw step de cada oponente e faz uma Ilusão por turno com +1 para
   bloquear; o −2 devolve a criatura encantada das Auras para a mão, o que desfaz todas as
   Auras de uma vez.
3. **Jace token:** Theorist's Proxy (flash, 0/3, empower 3) e Countersculpt criam e
   carregam a ficha de Jace; o −3 dela compra cartas. Proxy também sacrifica para a próxima
   mágica não poder ser anulada.
4. **Fechamento:** Sphinx of False Conclusions com flash no fim do turno do oponente; 4/2
   voadora que filtra ao atacar e, se morrer, deixa uma cópia. Duas Sphinx fecham em três
   ataques; Day of Judgment com Sphinx na mão é a sequência padrão (limpa, depois ameaça).

## Papel das cartas

| Grupo | Cartas | Função |
| --- | --- | --- |
| Remoção pontual | Prophesied End 4, Erode 2, Get Lost 2, Your Fate Ends Here 2, Memory Trap 2 | 12 respostas a permanentes; Get Lost e Memory Trap pegam encantamentos e artefatos (Jeskai Artifacts, Auras) |
| Remoção em massa | Day of Judgment 4 | A resposta ao campo de criaturas pequenas e ao reanimator |
| Anulação | No More Lies 3, Countersculpt 3, Icy Reception 2, Three Steps Ahead 2 (modo anular) | Contra bombas e mágicas de combo; Three Steps Ahead também compra ou copia uma Sphinx |
| Motor de compra | The Theorist, Jace Beleren 3, Theorist's Proxy 2, ficha de Jace, Three Steps Ahead | Vantagem de cartas contínua |
| Finalizadores | Sphinx of False Conclusions 4, Ilusões de Jace | Poucos, resilientes |

## Base de mana

25 terrenos: 4 Hallowed Fountain, 4 Floodfarm Verge, 4 Deserted Beach, 4 Meticulous
Archive, 5 Island, 4 Plains. Fontes: W 20, U 21. A fórmula de Karsten dá 21,6 para esta
curva, porque conta 10 mágicas baratas de compra; a diferença é deliberada e fica
registrada: controle quer o quarto terreno no turno 4 em toda partida (Day of Judgment e
Jace custam 4), e 4 Meticulous Archive com surveil mais Three Steps Ahead descartam o
excesso. Com 25, 4 terrenos no turno 4 em 68% das mãos jogando primeiro, antes da
suavização de mão do BO1 (`knowledge/base-de-mana.md`, seções "Resposta rápida" e 1.4).

## Guia de sideboard

BO1, sem sideboard (`knowledge/licoes/2026-10-04-sideboard-bo1-arena.md`). A lista
principal já leva as respostas a encantamentos e artefatos que iriam para o sideboard.

## Leitura do meta e pontos fracos

- **Mono-White Auras (13,0%, 57,7%):** Day of Judgment e Prophesied End ignoram ward e
  hexproof; o −2 de Jace devolve a criatura e as Auras caem. Risco: a partida é decidida
  nos turnos 2 a 4; mão sem remoção barata perde.
- **4-Color Reanimator (5,5%, 58,5%):** No More Lies e Countersculpt nas peças de setup;
  Your Fate Ends Here e Prophesied End no reanimado; Day of Judgment limpa. Jace ganha o
  jogo longo.
- **Jeskai Artifacts (4,1%, 57,6%):** o pior confronto: remoção de criatura e Day não
  pegam artefatos não criaturas. Memory Trap e Get Lost são as únicas respostas (4 cartas);
  anular Simulacrum Synthesizer é prioridade.
- **Azorius Control (espelho) e Boros Superfriends:** Countersculpt e Your Fate Ends Here
  (pega planeswalkers) decidem; Jace é a carta que o espelho não pode deixar resolver.
- **Prophesied End dá carta** quando o alvo não estava atacando: contra decks que não
  atacam (controle, artefatos), prefira Erode, Get Lost e Your Fate Ends Here.
- **Partidas longas:** o arquétipo tem 7,5 minutos por partida no snapshot. Para 25
  vitórias, isso é mais tempo que um aggro, com a compensação de um plano que vence por
  controle, não por corrida.
- Lista não testada em jogo.

## O que observar nos testes

- Quantas vezes faltou remoção nos turnos 2 e 3 contra Auras: se for frequente, o quarto
  Erode no lugar de um Three Steps Ahead (a contagem de FRA não muda).
- Se Jeskai Artifacts aparecer muito: subir Memory Trap para 3 no lugar de um Day of Judgment.
- Se Sphinx morrer para remoção com exílio (Get Lost do oponente): Elspeth, Storm Slayer
  no lugar da quarta Sphinx (a contagem de FRA cai para 21).
