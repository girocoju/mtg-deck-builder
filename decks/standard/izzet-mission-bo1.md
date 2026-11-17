# Izzet Mission (BO1)

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-11-17
- **Origem:** [izzet-mission-bo3.md](izzet-mission-bo3.md), lista de Stefan Schütz, campeão
  do Magic World Championship 32.
- **Meta de referência:** Untapped.gg, BO1, coletado em 2026-10-05 (43 dias, anterior a
  Star Trek). Está vencido: vale como indício, e a adaptação é **teórica**. O snapshot BO3
  (MTGGoldfish, 2026-11-17) não foi usado como se fosse BO1.
- **Situação:** proposta não testada em jogo.

```
Deck
3 Ral, Crackling Wit
4 Anthropological Mission
4 Opt
4 Sleight of Hand
2 Consult the Star Charts
4 Flashback
1 Burst Lightning
1 Boltwave
1 Traumatic Critique
2 Impractical Joke
2 Torch the Tower
1 Sear
2 Fire Magic
1 Engineered Explosives
3 Into the Flood Maw
2 Spell Snare
1 Long River's Pull
4 Steam Vents
4 Spirebluff Canal
4 Riverpyre Verge
1 Stormcarved Coast
1 Multiversal Passage
2 Great Hall of the Biblioplex
6 Island
```

`mtg deck validate --format standard --game arena`: lista válida (60 + 0).
`mtg deck analyze`: nenhum alerta.

## O que mudou

| Saiu | Entrou | Por quê |
| --- | --- | --- |
| 2 Spell Pierce | 1 Fire Magic, 1 Impractical Joke | Spell Pierce só anula mágica não criatura, e o campo de BO1 é de criaturas baratas. As duas que entram vêm do sideboard e nunca ficam sem uso: Fire Magic não tem alvo e Impractical Joke diz "até um alvo". |
| 1 Long River's Pull | 1 Boltwave | Segunda carta de finalização. Em BO3 a reserva de vitória é a Bothersome Noisemaker do sideboard; em BO1 ela não existe. |
| Sideboard inteiro | nada | Em BO1 não há troca entre jogos e o deck não busca cartas de fora do jogo. |

Critério ([sideboard.md](../../knowledge/sideboard.md), seção 2 e atualização de BO1):
contar as cartas mortas e trocá-las por respostas que servem em qualquer mesa. Neste deck
uma mágica de uma mana que pode ser conjurada sem alvo nunca é morta, porque ainda dá um
marcador a Ral e uma carta pela Anthropological Mission. Anulação precisa de alvo, então é
a que mais corre o risco de sobrar na mão.

## Boltwave ou Burst Lightning

Com o emblema de Ral, a mágica de número k do turno acontece k vezes. A tabela mostra
quantas mágicas o turno precisa ter, no total, para zerar o oponente:

| Vida do oponente | Só Burst Lightning | Só Boltwave | Burst + 1 Flashback | Boltwave + 1 Flashback | As duas, sem Flashback |
| --- | --- | --- | --- | --- | --- |
| 20 | 10 | 7 | 6 | 5 | 5 |
| 26 | 13 | 9 | 8 | 6 | 6 |
| 30 | 15 | 10 | 9 | 6 | 7 |

- Boltwave fecha com menos mágicas, e a diferença cresce contra ganho de vida.
- Burst Lightning é instantânea e tem qualquer alvo: mata criatura de resistência 2 no
  começo do jogo e, depois do emblema, vence no turno do oponente. Boltwave é feitiço e só
  acerta o jogador.
- Decisão: **as duas**. Com ambas o deck vence sem depender de Flashback e continua com
  uma finalização se a outra for exilada (No More Lies exila a mágica anulada; Veteran
  Survivor exila carta do cemitério).
- Boltwave parada na mão antes do emblema vai para o descarte da Mission ou do −3 de Ral,
  e Flashback a conjura do cemitério depois.
- Chance de ter uma finalização na mão até o turno 4 sem cavar: 16,7% com uma cópia,
  30,8% com duas (`mtg odds`).

## Plano de jogo

Combo-controle ([papel-no-jogo.md](../../knowledge/papel-no-jogo.md), seção 8). Contra
aggro você é o controle: troque remoção por criatura, baixe a Mission ou Ral quando a mesa
estiver segura e só então pense no emblema. Contra controle e combo você é quem tem a
inevitabilidade: resolva Ral e proteja-o.

- Turnos 1 a 3: Opt, Sleight of Hand e remoção de uma mana; Mission no turno 3.
- Turnos 4 em diante: Ral, e cada mágica barata vale um marcador e uma carta.
- Ral em 10: as mágicas conjuradas antes do −10 no mesmo turno já contam para o storm.

## Base de mana, antes e depois

| | BO3 | BO1 |
| --- | --- | --- |
| Terrenos | 22 (recomendado 20,6) | 22 (recomendado 20,9) |
| Fontes azuis | 21 (pede 21) | 21 (pede 21) |
| Fontes vermelhas | 15 (pede 14) | 15 (pede 14) |
| Símbolos U / R | 29 / 14 | 25 / 17 |
| Mágicas de uma mana | 24 | 25 |

Nenhum terreno foi cortado: controle não corta terreno em BO1
([base-de-mana.md](../../knowledge/base-de-mana.md), seção 1.4), e a suavização de mão não
olha cores.

## O que o deck ganha e o que perde

- **Ganha** contra aggro branco (Mono-White Auras 13%, Mono-White Lifegain 6% e Orzhov
  Lifegain 5,7% no snapshot de BO1): duas remoções em massa de uma mana e dez remoções
  pontuais, contra uma e nove.
- **Ganha** uma segunda finalização e uma vitória mais curta contra ganho de vida.
- **Perde** contra controle e combo: três anulações no lugar de seis, sem Stock Up, Annul
  nem Bothersome Noisemaker. No mesmo snapshot, Azorius Control, Jeskai Artifacts e Boros
  Superfriends somam 12,3%.
- O oponente não tem como tirar a remoção de criatura dele, que continua morta contra um
  deck sem criaturas. Em BO1 isso vale o jogo inteiro.

## Pontos fracos

- Sheltered by Ghosts exila Ral ou a Mission. Respostas: Spell Snare, matar a criatura em
  resposta à Aura, Engineered Explosives com dois marcadores.
- Veteran Survivor exila uma carta do cemitério por turno e atrapalha o Flashback. É 2/1:
  Fire Magic no modo de custo zero o mata.
- Controle com anulação: sobraram três anulações para proteger Ral.
- Sem Ral o deck só vence por fichas de Otter e pelo Great Hall of the Biblioplex.

## O que observar nos testes

- Quantas vezes Boltwave ficou sem uso na mão antes do emblema.
- Se a falta de Spell Pierce custou partidas contra controle ou reanimator.
- Se dois Fire Magic bastam contra as mesas largas de Mono-White.
