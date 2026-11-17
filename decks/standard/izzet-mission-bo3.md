# Izzet Mission (BO3), lista de Stefan Schütz

- **Formato:** standard (BO3) · **Plataforma:** Arena · **Data:** 2026-11-17
- **Origem:** lista colada pelo usuário (exportação do Arena em PT-BR, traduzida por coleção
  e número na base). É a lista com que Stefan Schütz venceu o Magic World Championship 32,
  catalogada como Izzet Mission
  ([Star City Games](https://articles.starcitygames.com/magic-the-gathering/schutz-izzet-mission-wins-magic-world-championship-32/),
  [MTGGoldfish](https://www.mtggoldfish.com/tournament/magic-world-championship-32)).
- **Meta de referência:** MTGGoldfish, BO3, coletado em 2026-11-17 (12 listas, 74,5% do
  meta). É o campo de hoje, não o campo exato do torneio.
- **Versão BO1:** [izzet-mission-bo1.md](izzet-mission-bo1.md)

```
Deck
3 Ral, Crackling Wit
4 Anthropological Mission
4 Opt
4 Sleight of Hand
2 Consult the Star Charts
4 Flashback
1 Burst Lightning
1 Traumatic Critique
1 Impractical Joke
2 Torch the Tower
1 Sear
1 Fire Magic
1 Engineered Explosives
3 Into the Flood Maw
2 Spell Pierce
2 Spell Snare
2 Long River's Pull
4 Steam Vents
4 Spirebluff Canal
4 Riverpyre Verge
1 Stormcarved Coast
1 Multiversal Passage
2 Great Hall of the Biblioplex
6 Island

Sideboard
3 Bothersome Noisemaker
2 Stock Up
2 Annul
2 Essence Burn
1 Spell Snare
1 Flashfreeze
1 Impractical Joke
1 Fire Magic
1 Ghost Vacuum
1 Petrified Hamlet
```

`mtg deck validate --format standard --game arena`: lista válida (60 + 15).
`mtg deck analyze`: 22 terrenos (recomendado 20,6), valor de mana médio 1,58, 21 fontes
azuis (pede 21) e 15 vermelhas (pede 14), nenhum alerta.

## Plano de jogo

Combo-controle sem criaturas ([papel-no-jogo.md](../../knowledge/papel-no-jogo.md),
seção 8): segura o jogo com mágicas de uma mana e combina no fim.

- **Motor.** Anthropological Mission compra uma carta a cada mágica não criatura e para de
  exigir descarte no terceiro marcador. Ral, Crackling Wit ganha um marcador de lealdade a
  cada mágica não criatura. Das 38 mágicas, 24 custam uma mana.
- **Vitória.** O −10 de Ral dá o emblema "mágicas instantâneas e feitiços têm storm". A
  partir daí Burst Lightning ou Traumatic Critique, copiadas pelo storm, fecham o jogo.
  Flashback conjura de novo a mesma carta do cemitério. As mágicas conjuradas no mesmo
  turno antes do −10 contam para o storm.
- **Reserva.** Fichas de Otter com prowess (+1 de Ral) e Great Hall of the Biblioplex como
  criatura 2/4.

## Papel das cartas

| Grupo | Cartas |
| --- | --- |
| Motor | 3 Ral, Crackling Wit, 4 Anthropological Mission |
| Compra e seleção | 4 Opt, 4 Sleight of Hand, 2 Consult the Star Charts |
| Finalização | 1 Burst Lightning, 1 Traumatic Critique, 4 Flashback |
| Remoção pontual | 1 Impractical Joke, 2 Torch the Tower, 1 Sear, 3 Into the Flood Maw |
| Remoção em massa | 1 Fire Magic, 1 Engineered Explosives |
| Anulação | 2 Spell Pierce, 2 Spell Snare, 2 Long River's Pull |

## O sideboard, carta a carta

Leitura do agente, feita pelo texto das cartas e pela contagem de alvos nas 12 listas do
snapshot BO3. Não é o guia do Schütz, que não temos.

| Carta | Contra quem entra | Alvos nas listas do snapshot |
| --- | --- | --- |
| 3 Bothersome Noisemaker | Controle sem criaturas e o espelho | Azorius Control tem 1 criatura; 4c Control e Jeskai Artifacts, nenhuma |
| 2 Stock Up | Jogos de atrito: Dimir Midrange e controles | entra no lugar da remoção que não tem alvo |
| 2 Annul | Decks de artefatos e encantamentos | Jeskai Artifacts 29 mágicas, Boros Dwarves 18, Jund Sacrifice 10, Mono-Green Landfall 7 (Earthbender Ascension, Sapling Nursery), e a Anthropological Mission do espelho |
| 2 Essence Burn | Criaturas pretas e verdes | Mono-Green Landfall 25, Jund Sacrifice 21, Dimir Reanimator 14, Lifegain 13, Dimir Midrange 8: decks que somam 45,4% do snapshot |
| 1 Spell Snare (a terceira) | Decks cheios de custo 2 | Jund Sacrifice 24 mágicas de custo 2, Lifegain 16, Dimir Midrange 15, Azorius Control 15, Izzet Spellementals 13 |
| 1 Flashfreeze | Vermelho e verde | Mono-Green Landfall 33 (todas as mágicas), Boros Dragons 21, 4c Control 20, Jund Sacrifice 17 |
| 1 Impractical Joke, 1 Fire Magic (as segundas) | Aggro de criaturas pequenas | resistência 2 ou menos: Lifegain 25 de 29 criaturas, Jund Sacrifice 18 de 24, Dimir Midrange 17 de 21, Azorius Momo 16 de 24 |
| 1 Ghost Vacuum | Cemitério | Dimir Reanimator (7,6% do snapshot) e o Flashback do espelho |
| 1 Petrified Hamlet | Terrenos com habilidade ativada | Restless Reef (4 no Dimir Reanimator, 2 no Dimir Midrange), Great Hall of the Biblioplex (4 no 4c Control e 2 no espelho), Soulstone Sanctuary |

Três ideias organizam as 15 ([sideboard.md](../../knowledge/sideboard.md)):

- **Plano transformacional (seção 6).** O deck não tem criaturas, então a remoção do
  oponente é carta morta no jogo 1 e ele a tira. Bothersome Noisemaker entra justamente
  quando a remoção saiu, e cresce com as mesmas mágicas baratas do motor (seção 5).
- **Contar cartas mortas (seção 2).** Contra controle sem criaturas, Fire Magic,
  Impractical Joke, Sear e as duas Torch the Tower quase não têm alvo. São cinco cartas, e
  entram cinco: três Noisemaker e duas Stock Up. Contra aggro saem as duas Spell Pierce.
- **Cópias únicas de cartas estreitas (seção 4).** Flashfreeze, Ghost Vacuum, Petrified
  Hamlet e a terceira Spell Snare são uma de cada: a segunda cópia de uma carta estreita
  rende pouco, e a seleção do deck (10 mágicas de busca, mais a Mission) acha a cópia única.

## Pontos fracos

- Uma só Burst Lightning e uma só Traumatic Critique causam dano no jogador. Anulação que
  exila (No More Lies) ou exílio do cemitério tira a finalização.
- Sem Ral em jogo o deck só vence por fichas de Otter e pelo Great Hall.
- Sheltered by Ghosts exila Ral ou a Mission.
