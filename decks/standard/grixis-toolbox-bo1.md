# Grixis Toolbox — Standard (BO1)

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-10-05
- **Meta de referência:** Untapped.gg, Standard BO1, capturas enviadas pelo usuário em
  2026-10-05 (`mtg meta show standard --mode bo1`). Fatias: 11/08 a 05/10, Bronze a Mythic,
  2,9 milhões de partidas. Win rates e cartas: 29/09 a 05/10, Bronze a Platinum, 390 mil.
  Sem decklists completas nem win rate por confronto.
- **Molde da base:** Dimir Midrange e Dimir Excruciator do snapshot **BO3** do MTGGoldfish
  (2026-10-04), usados só como fonte de remoção, compra e terrenos, não como leitura de campo.

```
Deck
4 Extrapolate the Impossible
4 North Wind Avatar
4 Requiting Hex
3 Bitter Triumph
3 Shoot the Sheriff
2 Nowhere to Run
2 Tithing Blade
2 Day of Black Sun
2 Deadly Cover-Up
4 Stock Up
2 Quantum Riddler
2 Deceit
4 Watery Grave
4 Gloomlake Verge
4 Steam Vents
4 Blood Crypt
1 Riverpyre Verge
2 Starting Town
2 Undercity Sewers
2 Restless Reef
3 Swamp

Sideboard
1 Day of Black Sun
1 Villainous Wrath
1 Malicious Eclipse
1 Harvester of Misery
1 Tithing Blade
1 Momentum Breaker
1 Strategic Betrayal
1 Ghost Vacuum
1 Abrade
1 Suplex
1 Qarsi Revenant
1 Oildeep Gearhulk
1 Outrageous Robbery
1 Duress
1 Negate
```

## Por que Grixis

Em BO1 o sideboard só serve a cartas que buscam de fora do jogo. A base tem três no
Standard:

| Carta | Custo | O que faz | Decisão |
| --- | --- | --- | --- |
| Extrapolate the Impossible | {1}{B} | Você revela duas cartas de nomes diferentes; o oponente escolhe qual vai para a sua mão | 4 cópias |
| North Wind Avatar | {2}{U}{U}{R} | 5/5 voador; ao ser conjurado, busca qualquer carta | 4 cópias |
| Turtles Forever | {3}{W} | Busca quatro criaturas lendárias; o oponente escolhe duas | Fora: pediria uma quarta cor e um sideboard só de lendárias |

Preto + azul + vermelho juntam as duas melhores: 8 buscas no principal, 82% de ter ao
menos uma até o turno 5.

## Como o sideboard foi montado

Extrapolate deixa o oponente escolher, então **toda carta do sideboard tem uma gêmea de
mesma função**: você revela as duas e qualquer escolha serve. North Wind Avatar busca a
melhor sem restrição.

| Contra | Fatia do campo | Par a revelar com Extrapolate | Melhor alvo do Avatar |
| --- | --- | --- | --- |
| Mono-White Auras | 13,0% | Tithing Blade + Momentum Breaker (sacrifício ignora ward e hexproof) | Day of Black Sun |
| Lifegain branco e Orzhov | 11,7% | Day of Black Sun + Villainous Wrath, ou Malicious Eclipse + Harvester of Misery | Villainous Wrath |
| Mono-Green Landfall | 5,0% | Day of Black Sun + Villainous Wrath | Villainous Wrath |
| 4-Color Reanimator | 5,5% | Strategic Betrayal + Ghost Vacuum | Strategic Betrayal |
| Jeskai Artifacts | 4,1% | Abrade + Suplex | Villainous Wrath (Constructs) |
| Azorius Control e espelhos de controle | 4,3% | Duress + Negate, ou Outrageous Robbery + Oildeep Gearhulk | Outrageous Robbery |
| Aggro em geral, vida baixa | — | Qarsi Revenant + Oildeep Gearhulk (lifelink) | Oildeep Gearhulk |

## Plano de jogo

Papel: controle contra os decks de criaturas (30% do campo identificado), beatdown
tardio contra controle. Rota "um pouco maior" de `knowledge/arquetipos.md`.

- **Turnos 1–2:** remoção barata (Requiting Hex, Bitter Triumph, Shoot the Sheriff) ou
  Extrapolate já buscando o par do confronto.
- **Turno 3:** Stock Up, ou a carta buscada.
- **Turno 4:** Day of Black Sun com X=2 destrói todas as criaturas de custo 2 ou menos e
  tira as habilidades antes: é o deck inteiro do Auras e quase todo o Lifegain.
- **Turno 5 em diante:** North Wind Avatar (ameaça + busca), Quantum Riddler, Deceit,
  Deadly Cover-Up.

Contra Auras, Nowhere to Run desliga ward e hexproof das criaturas do oponente enquanto
estiver na mesa: depois dela, toda a remoção com alvo volta a funcionar.

## Papel das cartas

- **Buscas (8):** 4 Extrapolate the Impossible, 4 North Wind Avatar.
- **Remoção pontual (12):** 4 Requiting Hex, 3 Bitter Triumph, 3 Shoot the Sheriff,
  2 Nowhere to Run.
- **Sacrifício (2):** Tithing Blade.
- **Remoção em massa (4):** 2 Day of Black Sun, 2 Deadly Cover-Up.
- **Compra (4):** Stock Up.
- **Ameaças (8):** 4 North Wind Avatar, 2 Quantum Riddler, 2 Deceit; Restless Reef como
  terreno que ataca.

## Pontos fracos

- **Extrapolate custa tempo:** 2 manas para buscar, mais o custo da carta. No turno 2
  jogando depois contra Auras, pode ser tarde.
- **Avatar exige {U}{U}{R} num deck de base preta:** 19 fontes azuis e 11 vermelhas
  cumprem a tabela, mas é a carta mais difícil de conjurar da lista.
- **Vida:** 12 terrenos que cobram 2 de vida, Starting Town e Bitter Triumph. Contra
  aggro, entre virado quando der.
- **Encantamentos:** Grixis não remove encantamento na mesa (Leyline of Hope, Authority
  of the Consuls). Só Negate, antes de resolver.
- **Reanimator:** o ódio está no sideboard; depende de achar uma das 8 buscas.
- **Arquétipos sem lista no snapshot** (Temur Kona, Orzhov Skeletons, Rakdos Fling,
  Orzhov Sacrifice): não considerados.

## Conferência (2026-10-05)

- `mtg deck validate --format standard --game arena`: lista válida, 60 + 15.
- `mtg deck analyze`: 26 terrenos para 25,2 recomendados; valor de mana médio 2,94;
  azul 19 fontes para 16, preto 21 para 21, vermelho 11 para 10; nenhum alerta. A
  primeira versão tinha 19 fontes pretas; troquei 1 Riverpyre Verge e 1 Island por
  1 Blood Crypt e 1 Swamp.
- `mtg deck cost`: 7 comuns, 19 incomuns, 36 raras, 10 míticas (sem contar o que você já tem).

## Honestidade

Deck construído do zero em torno de duas cartas de busca; não é um arquétipo do snapshot
e não foi testado em jogo. O que observar: quantas vezes Extrapolate no turno 2 chegou a
tempo, se o Avatar saiu no turno 5, quais pares do sideboard nunca foram buscados (são
os primeiros candidatos a troca) e a vida perdida para os próprios terrenos.
