# Gruul Ghalta "Burn Together" (BO1)

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-11-03
- **Origem:** lista colada pelo usuário (exportação do Arena em português, traduzida pela
  base por código de coleção e número de colecionador), vista no vídeo de um jogador
  japonês: https://www.youtube.com/watch?v=KqEhJnqztcA. Título do vídeo: "MTG Arena:
  normalmente mata no turno 3, raríssimo no turno 2! Combo ultrarrápido de poder alto e
  Agni Kai [Standard]". A lista original está no fim do arquivo
- **Modo assumido:** BO1 (lista sem sideboard, vídeo de Arena)
- **Meta de referência:** BO3 MTGGoldfish, coletado em 2026-11-03 (`mtg meta show standard
  --mode bo3`); BO1 Untapped.gg, capturas de 2026-10-05 (29 dias; só como indício)

```
Deck
4 Llanowar Elves
4 Slumbering Trudge
4 Bebop & Rocksteady
4 Pugnacious Hammerskull
4 Ghalta the Unstoppable
2 Ghalta, Primal Hunger
4 Callous Sell-Sword
4 Wild Ride
4 The Last Agni Kai
4 Bulk Up
4 Starting Town
4 Stomping Ground
4 Thornspire Verge
5 Forest
2 Rockfall Vale
1 Mountain
2 Multiversal Passage
```

## O que mudou em relação ao vídeo e por quê

| Saiu | Entrou | Motivo |
| --- | --- | --- |
| 2 Hazoret, Godseeker | 2 Slumbering Trudge (4ª e 3ª) | Hazoret é 5 de poder: deixa Ghalta the Unstoppable a {3}{G}, o que não cabe no turno 3 com Wild Ride. Trudge é 6 por {1}{G} (ou por {G}, com X = 0): Ghalta a {2}{G} no turno 3 mesmo sem Elves, e dois Trudge com X = 0 somam poder 13 para Ghalta, Primal Hunger a {G}{G}. Hazoret nunca ataca (precisa de speed 4) |
| 2 Ghalta, Primal Hunger | 2 Pugnacious Hammerskull (4º e 3º) | Oito Ghaltas lendárias na mão é a mão que não joga; a Primal Hunger só é barata quando a mesa já ganha. Hammerskull é o único corpo que ataca de verdade (6/6 por 3, sem stun com qualquer Ghalta em jogo) e deixa Ghalta a {2}{G} |

Medido por goldfish (simulação abaixo, 3000 partidas por linha, suavização de mão do BO1):
a lista do vídeo mata até o turno 4 em 43% das partidas jogando primeiro e 56% na draw; a
proposta, em 50% e 63%. Até o turno 5: de 74% / 82% para 83% / 89%.

## A estratégia: um corpo gigante, arremessado duas vezes

É um **combo de poucas cartas** embutido em casca de aggro (`knowledge/arquetipos.md`,
seção 5: combo de duas ou três cartas, papel de beatdown). Três engrenagens, todas
conferidas em `mtg card`:

1. **Corpos de poder alto por pouca mana.** Slumbering Trudge ({X}{G}, 6/6; entra com
   3 − X stun e virada se X ≤ 2), Bebop & Rocksteady ({1}{B/G}{B/G}, 7/5; o híbrido se
   paga com verde), Pugnacious Hammerskull ({2}{G}, 6/6). Eles quase não atacam: servem
   de **desconto** e de **munição**.
2. **As duas Ghaltas.** Ghalta the Unstoppable custa {8}{G} menos o maior poder entre
   suas criaturas (com Bebop na mesa, {1}{G}; a redução não passa de {G}, regra da
   carta). Ghalta, Primal Hunger custa {10}{G}{G} menos o poder total (Ghalta 8 + Bebop
   7 + Elves 1 = 16: custa {G}{G}). São nomes diferentes, então as duas convivem.
3. **Dano direto igual ao poder.** Burn Together, a aventura de Callous Sell-Sword ({R},
   feitiço): sua criatura causa dano igual ao poder a qualquer alvo e é sacrificada.
   Wild Ride ({R}: +3/+0 e ímpeto) e Bulk Up ({1}{R}, instantânea: dobra o poder) fazem o
   mesmo corpo **bater e depois ser arremessado**: Ghalta 8 → 11 (Wild Ride) → 22 (Bulk
   Up) → ataca com atropelar por 22 e Burn Together causa mais 22.

**The Last Agni Kai** é a carta que dá nome ao vídeo: sua criatura luta com uma do oponente
e o dano excedente vira mana vermelha que **não some até o fim do turno**. Ghalta 8/8 luta
com um 1/1: 7 manas vermelhas, que pagam Wild Ride + Bulk Up + Burn Together no mesmo
turno. É remoção e aceleração na mesma carta; sem criatura adversária, é carta morta.

### As linhas de jogo

| Linha | Turno 1 | Turno 2 | Turno 3 | Turno 4 | Mana no turno da morte |
| --- | --- | --- | --- | --- | --- |
| **Turno 3 (a "normal" do vídeo)** | Llanowar Elves | Bebop & Rocksteady | Ghalta the Unstoppable ({1}{G}) + Wild Ride + Burn Together: 11 no ataque + 11 arremessados = 22 | | 4 (3 terrenos + Elves) |
| **Turno 3 com Agni Kai** | Elves | Bebop | Ghalta + Agni Kai contra um X/1 ou X/2 (6 a 7 {R}) → Wild Ride, Bulk Up, Burn Together: 22 + 22 | | 4 |
| **Turno 3 pela Primal Hunger** | Elves | Trudge + Trudge (X = 0 nas duas): poder total 13 | Primal Hunger ({G}{G}, 12/12) + Wild Ride + Burn Together: 15 + 15 | | 4 |
| **Turno 4 sem Elves** | — | Trudge (X = 1) | Ghalta ({2}{G}) | Wild Ride + Bulk Up + Burn Together: 22 + 22 | 4 |
| **Turno 2 (raríssima)** | Elves | Trudge (X = 0, 1 mana) + Agni Kai contra um X/1 (5 {R}) → Wild Ride, Bulk Up, Burn Together na Trudge: 18 | | | 3 |

A linha de turno 2 só mata se o oponente já pagou 2 de vida (shockland). As de turno 3
exigem Elves no turno 1 **e** a criatura de 7 poder no turno 2 **e** Ghalta **e** o par
haste + arremesso: o "normalmente mata no turno 3" do título é a melhor mão, não a
média. Na simulação, o turno 3 acontece em 5% a 10% das partidas; o turno 4 é a regra.

Detalhes de regras que mudam jogadas (rulings em `mtg card --rulings`):

- Trudge virada e com stun continua servindo: luta com Agni Kai, é alvo de Burn Together e
  conta para os descontos. X = 0 ({G}) já dá um 6/6 para isso; X = 3 (4 manas) entra
  desvirada e sem stun, para quando sobrar mana.
- Harmonize de Wild Ride ({4}{R}, menos o poder de uma criatura que você vira): com uma
  Trudge desvirada ou uma Ghalta que não vai atacar, a recompra sai por {R}. A criatura
  virada pode estar com enjoo de invocação.
- Bulk Up tem flashback {4}{R}{R}: a mana de Agni Kai paga.
- Hammerskull leva stun ao atacar sem outro Dinossauro; as duas Ghaltas são Dinossauros.
- Bebop ao atacar exige descartar uma carta ou sacrificar uma permanente: descarte o
  terreno sobrando. Se a mão estiver vazia, não ataque com ele; arremesse.
- Burn Together é feitiço: não responde a remoção. Bulk Up é instantânea: responde.
- Na pilha, a aventura tem valor de mana 1: Spell Snare não a anula.

## Papel das cartas

| Grupo | Cartas | Função |
| --- | --- | --- |
| Aceleração | Llanowar Elves 4 | O turno 3 depende dela; com Elves no turno 1, o turno 3 tem 4 manas |
| Corpos de desconto | Bebop & Rocksteady 4, Slumbering Trudge 4, Pugnacious Hammerskull 4 | Poder 6 a 7 por 1 a 3 manas; deixam Ghalta the Unstoppable a {1}{G} ou {2}{G}; Hammerskull também ataca |
| Ameaça / motor | Ghalta the Unstoppable 4, Ghalta, Primal Hunger 2 | 8/8 e 12/12 com atropelar; a primeira dá atropelar a todas |
| Ímpeto | Wild Ride 4 | Faz a Ghalta do turno bater no mesmo turno; recompra por harmonize |
| Dobro | Bulk Up 4 | 8 vira 16, 11 vira 22; instantânea |
| Arremesso | Callous Sell-Sword 4 (Burn Together) | A finalização: dano igual ao poder, ignora bloqueadores e passa por cima do ganho de vida quando o número é grande |
| Luta e mana | The Last Agni Kai 4 | Remoção que paga o resto do turno |

## Base de mana

22 terrenos + 4 Elves. `mtg deck analyze` pede 24,5 pela fórmula, mas a fórmula conta as
Ghaltas pelo custo impresso (9 e 12); na prática elas custam 2 e a curva real para no 3.
Para um deck cuja jogada mais cara é de 3 manas e que quer o terceiro terreno no turno 3
(71,9% jogando primeiro, antes da suavização de mão do BO1), 22 é o número de um aggro de
curva baixa (`knowledge/base-de-mana.md`, "Resposta rápida" e seção 1.4). A simulação
confirmou: com 21 terrenos as mãos de 0 a 1 ou 6 a 7 terrenos sobem de 5% para 12% sem
ganho de velocidade; com 23, nenhum ganho.

Fontes: G 19 (Elves no turno 1 pede 14; Primal Hunger {G}{G} pede 21, mas ela nunca é
jogada no turno 2), R 15 (Wild Ride e Burn Together pedem 14). O turno da morte gasta
dois ou três símbolos vermelhos (Wild Ride, Burn Together, Bulk Up) com 3 ou 4 terrenos:
a mana de Agni Kai é vermelha e resolve isso quando há luta. O alerta de preto do
`analyze` é falso: Callous Sell-Sword entra pela aventura ({R}); a criatura {1}{B} só sai
por Starting Town ou Multiversal Passage e não faz parte do plano. Thornspire Verge só dá
verde com Montanha ou Floresta em jogo: Stomping Ground, Forest, Mountain e Multiversal
Passage contam.

## Simulação (goldfish, 3000 partidas por linha)

Script: `scripts/goldfish-ghalta.py`. Oponente passivo, sem bloqueadores; mão inicial com
suavização BO1 (duas mãos, fica com a mais próxima da média de terrenos), sem mulligan;
sem cores; a cada turno o modelo enumera as ordens de conjuração e as sequências de
mágicas e mata se há letal. Dois cenários: sem criatura adversária (Agni Kai morta) e com
uma criatura X/2 do oponente a partir do turno 2 (Agni Kai vira mana). Erro padrão
de cerca de ±1 ponto em 50%.

Partidas vencidas **até** o turno indicado, jogando primeiro / na draw:

| Lista | Cenário | ≤ T3 | ≤ T4 | ≤ T5 | ≤ T6 |
| --- | --- | --- | --- | --- | --- |
| Vídeo | sem criatura | 5 / 9 | 43 / 56 | 74 / 82 | 84 / 89 |
| Vídeo | com X/2 | 6 / 11 | 44 / 57 | 75 / 84 | 86 / 90 |
| **Proposta** (−2 Hazoret −2 Primal Hunger, +2 Trudge +2 Hammerskull) | sem criatura | 6 / 10 | 50 / 63 | 83 / 89 | 91 / 95 |
| **Proposta** | com X/2 | 5 / 11 | 50 / 62 | 85 / 91 | 92 / 96 |
| Só −2 Hazoret +2 Trudge | sem criatura | 6 / 9 | 45 / 58 | 79 / 86 | 87 / 91 |
| Só −2 Primal Hunger +2 Trudge | sem criatura | 5 / 9 | 45 / 59 | 80 / 87 | 90 / 94 |
| Proposta com −2 Hammerskull +2 Snakeskin Veil | sem criatura | 5 / 10 | 44 / 57 | 78 / 83 | 87 / 90 |
| Vídeo com −2 Hammerskull +2 Felonious Rage | sem criatura | 4 / 8 | 39 / 51 | 64 / 75 | 76 / 83 |
| Proposta com 21 terrenos | sem criatura | 5 / 9 | 42 / 59 | 73 / 83 | 86 / 90 |

Leituras:

- **O gargalo são os corpos de desconto, não o ímpeto.** Trocar corpos por uma segunda
  mágica de ímpeto (Felonious Rage) piora tudo; Wild Ride em 4 já basta.
- **Elves no turno 1 sai em 40% das partidas** (44% na draw). É o que separa o turno 3 do
  turno 4; nenhuma troca muda isso, porque não existe outro acelerador de 1 mana em
  Standard que valha o espaço (Gene Pollinator e Molt Tender pedem outra permanente).
- **Proteção custa pouco:** Snakeskin Veil no lugar de 2 Hammerskull perde 5 a 6 pontos no
  turno 4 em goldfish, mas o goldfish não vê a remoção do oponente. Fica como a primeira
  adaptação a testar se Erode, Bitter Triumph e Sheltered by Ghosts aparecerem muito.

## Leitura do meta

Snapshot BO3 (MTGGoldfish, 2026-11-03): Mono-Green Landfall 12,4%, Dimir Midrange 10,9%,
Dimir Reanimator 8,8%, Lifegain 8,0%, Izzet Spellementals 7,9%, Azorius Control 6,4%, 4c
Control 5,1%, Jeskai Artifacts 4,9%. Não há arquétipo com Ghalta no snapshot (Gruul
Delirium 0,3% e Gruul Leyline Aggro 0,1% são outros decks): a lista é **fora do radar**,
a primeira condição para um combo de poucas cartas prosperar (`arquetipos.md`, seção 5).
Snapshot BO1 (Untapped, 2026-10-05, 29 dias, só indício): Mono-White Auras 13,0%, Mono-White
e Orzhov Lifegain 11,7% somados, 4-Color Reanimator 5,5%, Mono-Green Landfall 5,0%.

O que o campo tem em comum, pelas cartas mais jogadas do BO3:

- **Remoção pontual barata** (7,5 por deck em média): Erode em 25,8% dos decks, Bitter
  Triumph 19,7%, Get Lost. Toda mata Ghalta por 1 ou 2 manas, em velocidade instantânea.
- **Strategic Betrayal** (24,8%): o oponente escolhe o que exila; ele exila Elves, não
  Ghalta. Pouco relevante.
- **Spell Snare** (18,8%): anula valor de mana 2: Bulk Up e Agni Kai. Não pega Ghalta (VM 9
  e 12), Wild Ride (1), Trudge (1) nem Burn Together (1 na pilha).
- **Requiting Hex** (19,7%): destrói VM ≤ 2: Elves e Trudge. Não pega Bebop, Hammerskull
  nem Ghalta.
- **Day of Judgment** (Azorius Control 6,4%; Boros Superfriends no BO1): sweeper no turno 4,
  quando o deck já quer ter matado.
- **Ganho de vida** (Lifegain 8,0% BO3; 11,7% BO1): 20 de dano não bastam, e é por isso que
  a dupla pancada (ataque + arremesso, 22 + 22) importa mais que a primeira.

Papel (`knowledge/papel-no-jogo.md`): beatdown em todos os confrontos. O deck não tem
plano B; vence antes do turno 5 ou perde para a primeira remoção bem colocada.

## Pontos fracos

- **Elves no turno 1 decide o turno da morte.** Sem ela, o deck é de turno 4 ou 5.
- **Nenhuma proteção.** Remoção em resposta ao Bulk Up (ou no fim do turno em que Ghalta
  entrou) custa duas cartas e o turno. Burn Together é feitiço, não salva nada.
- **Agni Kai morta sem criatura adversária** (controle, combo): 4 cartas que não fazem nada.
- **Lendas:** Bebop e as Ghaltas são lendárias; a segunda cópia na mão vira descarte de Bebop.
- **Bebop custa carta para atacar;** Trudge entra virada. Em jogo "normal", sem Ghalta, só
  Hammerskull ataca.
- Sem Hazoret, nada sobrevive a Day of Judgment; a proposta aposta em matar antes.

## Guia de sideboard

BO1, sem sideboard (`knowledge/licoes/2026-10-04-sideboard-bo1-arena.md`).

## Custo (`mtg deck cost`)

Papel US$ 133 | € 119 | MTGO 53 tix | Arena: 8 comuns, 12 incomuns, 34 raras, 0 míticas
(a lista do vídeo: 32 raras e 2 míticas).

## O que observar nos testes

Lista proposta não testada em jogo; a do vídeo tem as partidas do autor. Anotar:

- Em quantas partidas Ghalta morreu para remoção antes de bater: se for frequente,
  −2 Hammerskull +2 Snakeskin Veil (hexproof em resposta, {G}).
- Quantas vezes a segunda Primal Hunger fez falta (mão com 12/12 e mesa pronta): se nunca,
  as 2 cópias bastam; se sempre, voltar uma no lugar de um Hammerskull.
- Mãos com Agni Kai morta contra controle: se o oponente nunca tem criatura, Hard-Hitting
  Question ({G}, feitiço: dano igual ao poder a uma criatura ou planeswalker) não ajuda;
  o que ajuda é velocidade, então não trocar.
- Se Bebop ficar preso na mão sem Elves (3 manas no turno 3 em vez de Ghalta), é o sinal
  de que o deck está mais lento do que a simulação sugere.

## Lista original do vídeo

Para referência e para `mtg deck diff`:

```
Deck
4 Llanowar Elves
2 Slumbering Trudge
4 Bebop & Rocksteady
2 Pugnacious Hammerskull
4 Ghalta the Unstoppable
4 Callous Sell-Sword
4 Wild Ride
4 The Last Agni Kai
4 Bulk Up
4 Ghalta, Primal Hunger
4 Starting Town
4 Stomping Ground
4 Thornspire Verge
5 Forest
2 Rockfall Vale
1 Mountain
2 Multiversal Passage
2 Hazoret, Godseeker
```
