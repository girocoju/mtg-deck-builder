# Dimir Sphinx's Approach — Standard (BO1), v8 "Charm"

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-10-14
- **Pedido:** combo que compra o grimório inteiro e vence com Fblthp, Impossibly Lost.
  Modelo de partida (templating, `knowledge/base-de-mana.md`, Parte 1): a lista "Oh No"
  do criador de conteúdo Sloth, vista em captura do usuário (18 Approach, 4 Omniscience,
  4 Theorix Charm, 4 Does Machines, 4 Dark Matter Manipulator, 3 Unraveler, 20 terrenos);
  o fechamento dele é North Wind Avatar buscando Terror of the Peaks de fora do jogo, e o
  deste deck é Fblthp
- **Histórico:** v1 a v3 perderam três partidas em três (Landfall, Reanimator, Lifegain);
  lições em `knowledge/licoes/2026-10-14-*`. A v4 (remoção em massa) não foi jogada: o
  usuário preferiu ir para o combo puro
- **Versão atual = a que venceu em 2026-10-14** (captura "Approach v5" do usuário): o usuário
  manteve 4 Paradox Shaper e 3 Omniscience no lugar dos 4 Theorix Charm e da 2ª Omniscience
  da proposta, com 21 terrenos. Vitória contra Mono-White Lifegain com o oponente em 32 de
  vida: biblioteca em zero, Fblthp na mesa, três Omniscience em jogo. Lição em
  `knowledge/licoes/2026-10-14-sphinxs-approach-bo1-vitoria-fblthp.md`
- **v6 (2026-10-14):** o usuário apontou a fragilidade do Fblthp (precisa de dano de
  combate). O fechamento passa a ser sem combate: Cornered by Black Mages e Circle of
  Power criam fichas de Wizard 0/1 com "sempre que você conjurar uma mágica não criatura,
  esta ficha causa 1 de dano a cada oponente". Saem 2 Fblthp, 1 Into the Flood Maw e 1
  Paradox Shaper. A v5 vencedora fica registrada no histórico do arquivo
- **v8 (2026-10-14, após a derrota para Dryad Militant):** 3 Theorix Charm entram; saem
  1 Omniscience, 1 Does Machines e Wisdom of Ages. O Charm responde às três cartas que
  decidiram as derrotas do combo puro: −2/−2 mata Dryad Militant (2/1) e anula Deadly
  Cover-Up ou Soul-Guide Lantern a menos que paguem 2 a mais; o terceiro modo (mói 3,
  compra 1) é cadeia sob Omniscience. Lição em
  `knowledge/licoes/2026-10-14-sphinxs-approach-bo1-v7-cover-up.md`
- **Meta de referência:** Untapped.gg, Standard BO1, capturas do usuário de 2026-10-05
  (`mtg meta show standard --mode bo1`)

```
Deck
2 Circle of Power
3 Conspiracy Unraveler
2 Cornered by Black Mages
2 Dark Matter Manipulator
1 Does Machines
4 Gloomlake Verge
1 Hidden Grotto
1 Inspiration from Beyond
6 Island
2 Omniscience
1 Paradox Shaper
22 Sphinx's Approach
2 Swamp
3 Theorix Charm
4 Undercity Sewers
4 Watery Grave
```

## O combo, passo a passo

1. **Encher o cemitério de Approach** sem conjurá-las: Dark Matter Manipulator (mói 3),
   Paradox Shaper (todo turno, Omit Variables por {U/B}: mói 3; o {2} devolve ao fundo do
   grimório uma Omniscience ou um Unraveler moídos), Does Machines (mói 2, compra 2,
   descarta 2 Approach), Undercity Sewers e Hidden Grotto. Com 18 Approach, 30% do
   grimório é Approach.
2. **A busca.** Approach é instantânea: no fim do turno do oponente, a quinta Approach
   (contando a conjurada) traz Conspiracy Unraveler.
3. **Omniscience de graça.** Com Unraveler em jogo, Omniscience (valor 10) é conjurada
   exilando 10 de valor do cemitério: quatro Approach, ou três e um Manipulator. Nunca
   exile um Unraveler como evidência.
4. **As fichas.** Cornered by Black Mages (o oponente sacrifica uma criatura) e Circle of
   Power (compra 2) criam, cada uma, um Wizard 0/1 que causa 1 de dano a cada oponente
   sempre que você conjura uma mágica não criatura. Sob Omniscience saem de graça.
5. **A metralhadora.** Cada Approach da mão é grátis, compra duas e dispara todas as
   fichas. Com duas fichas, cada mágica são 2 de dano: 10 Approach matam de 20; 16, um
   oponente de 32. A cadeia tem 18 Approach, 4 Does Machines, as Omniscience e as
   próprias feitiçarias das fichas, mais de 25 mágicas não criatura. Nada disso passa
   por combate, bloqueador, Settle the Wreckage ou ganho de vida.
6. **Sem Omniscience** o plano ainda anda: uma ficha no turno 3 ou 4 transforma cada
   Approach pagada em compra de 2 mais 1 de dano, e Cornered é remoção de edito contra a
   criatura única com hexproof dos decks de Auras.

Regra de pilotagem: a ficha precisa estar em jogo **antes** da cadeia. Ordem sob
Omniscience: Cornered e Circle primeiro, Approach depois.

**Deck-out (partida de 2026-10-14, grimório em 7 cartas).** A cadeia compra 2 por
Approach e Does Machines e Inspiration ainda moem; conte o grimório antes de cada uma.
Com Omniscience, Paradox Shaper é a válvula: {2} devolve uma Approach do cemitério ao
fundo do grimório, e a próxima Approach a compra de volta; cada 2 manas é uma mágica a
mais sem gastar grimório. Pare a cadeia quando o dano acumulado bastar, não quando as
cartas acabarem. v7.1: 2 Circle of Power (eram 1; demorava a achar as fichas) no lugar de
uma Inspiration from Beyond.

**Feitiçarias moídas (pergunta do usuário).** Três caminhos, do mais barato ao mais forte:

- Paradox Shaper manda a carta para o fundo do grimório, e isso basta no turno da cadeia:
  a sequência de Approach compra o grimório inteiro, fundo incluído. Antes da Omniscience
  não resolve.
- Inspiration from Beyond ({2}{U}, feitiço): mói 3 e devolve uma instantânea ou feitiçaria
  do cemitério à mão. Resgata Cornered, Circle ou uma Approach em qualquer momento do jogo
  e ainda mói; sob Omniscience é grátis.
- Wisdom of Ages ({4}{U}{U}{U}, feitiço): devolve **todas** as instantâneas e feitiçarias
  do cemitério à mão e tira o limite de mão. Sob Omniscience, é o botão de reinício: toda
  Approach moída e descartada e as feitiçarias das fichas voltam de uma vez, e a cadeia
  recomeça. Uma cópia, porque fora da cadeia custa 7.

## A cadeia morre em terrenos: a conta e a correção (v7)

O usuário mostrou a falha: Omniscience na mesa e a mão com seis terrenos. É esperado.
Cada Approach compra 2 cartas; com 18 Approach em 60, cada compra tem 30% de chance de
ser outra Approach, então uma Approach gera em média 0,6 Approach. Menos que 1: a cadeia
não se sustenta sozinha, só com o estoque da mão. Simulação da cadeia (5.000 tentativas
a partir de Omniscience em jogo, uma ficha de Black Mage, 13 cartas vistas, 5 Approach já
exiladas pela busca; modelo simplificado, serve para comparar, não como número absoluto):

| Lista | Mata 20 na cadeia | Compra o grimório | Mediana de mágicas | Mão inicial com 1 terreno ou menos |
| --- | --- | --- | --- | --- |
| v6: 18 Approach, 21 terrenos | 50% | 39% | 11 | 11% |
| **v7: 22 Approach, 21 terrenos** (−2 Manipulator, −1 Does Machines, −1 Shaper) | 58% | 49% | 21 | 11% |
| 22 Approach, 20 terrenos | 60% | 50% | 21 | 13% |
| 24 Approach, 20 terrenos (−1 Unraveler a mais) | 69% | 63% | 21 | 12% |

Terrenos com cycling (Capital City) não mudaram nada: 2 manas por carta é lento demais
dentro da cadeia. O que muda é a densidade de Approach. A v7 adota 22 com 21 terrenos,
sem piorar a mão inicial; se a cadeia continuar morrendo, o passo seguinte é 24 Approach
e 20 terrenos, cortando o terceiro Unraveler.

## Lista vencedora do usuário ("Approach v3" no Arena, 2026-10-14)

Primeira vitória do deck, antes de a v5 ser jogada, contra um deck vermelho e branco de
remoção e anulação (Abrade, Broadside Barrage, Sound the Trumpets, Demolition Field,
Soul-Guide Lantern e Ajani's Anguish vistos). Diferenças para a v5: 4 Paradox Shaper no
lugar de 4 Theorix Charm e 1 Into the Flood Maw, 2 Unraveler em vez de 3, 24 terrenos em
vez de 22 e sem Hidden Grotto. Validada em Standard para o Arena, sem alertas de cor.

```
Deck
4 Dark Matter Manipulator
4 Does Machines
2 Fblthp, Impossibly Lost
4 Paradox Shaper
18 Sphinx's Approach
2 Conspiracy Unraveler
2 Omniscience
6 Island
4 Swamp
4 Gloomlake Verge
2 Shipwreck Marsh
4 Undercity Sewers
4 Watery Grave
```

Nos prints: Unraveler e Omniscience na mesa no turno em que o oponente tinha Soul-Guide
Lantern desvirada e não a usou a tempo; no exílio, cinco Approach da busca mais Does
Machines, Manipulator, Shaper e um Fblthp pagos como evidência, com o segundo Fblthp na
mão. Duas leituras: a Lantern do oponente é o relógio real do combo (buscar e conjurar
Omniscience na mesma rodada, antes que ela seja sacrificada), e nunca pagar evidência
com o último Fblthp.

## Papel das cartas

| Grupo | Cartas | Função |
| --- | --- | --- |
| Motor | Sphinx's Approach 22 | Compra, busca, combustível da evidência e a própria cadeia |
| Moagem e seleção | Dark Matter Manipulator 2, Does Machines 2, Paradox Shaper 1, Inspiration from Beyond 2, Undercity Sewers 4, Hidden Grotto 1 | Põem Approach no cemitério; Does Machines também descarta Approach da mão |
| Alvo da busca | Conspiracy Unraveler 3 | Paga Omniscience; bloqueador 6/6 voador enquanto a cadeia não vem |
| Fechamento | Omniscience 3, Cornered by Black Mages 2, Circle of Power 2 | A cadeia e o dano por mágica conjurada |
| Interação | Theorix Charm 3 (anula não criatura por {2} a mais; −2/−2; ou mói 3 e compra 1), Cornered by Black Mages 2 (edito) | Barata; com Omniscience, grátis no turno do combo para tirar bloqueadores |
| Bloqueadores | Manipulator 1/2 (cresce +2/+0 a cada sete cartas no cemitério) | Único corpo barato; o deck aceita levar dano para montar o combo |

## O que mudou em relação à v3 e por quê

- **18 Approach (eram 12).** No combo puro, a Approach é motor, evidência e a própria
  cadeia; 30% do grimório garante a busca mais cedo e a cadeia sem falhas. A conta que
  valia contra "mais Approach" na v2 (23% contra 20%) muda quando se vai a 30%.
- **2 Omniscience (era 1).** A cadeia precisa dela na mão quando o Unraveler entra; com
  uma cópia, dependia de moê-la e devolvê-la com Shaper. Com Unraveler, custa zero mana.
  A lista modelo usa 4; a simulação de mãos mostrou que a terceira cópia custava mais em
  mãos mortas do que rendia, e a vaga virou terreno.
- **Does Machines e Theorix Charm** no lugar de Paradox Shaper, Picklock Prankster,
  Deathcap Marionette, Bitter Triumph, Break Under Pressure e Soul-Guide Lantern: loot de
  2 manas que descarta Approach, e uma carta de 2 manas que é anulação, remoção pequena ou
  moagem com compra. O deck perde remoção de criatura grande e hate de cemitério:
  escolha consciente pelo combo.
- **22 terrenos (eram 24; a lista modelo usa 20).** Com 20, a simulação de 1.000 mãos
  deu 13% de mãos com um terreno ou menos e só 66% de três terrenos no turno 3, o turno da
  Approach. Com 22, os números da seção seguinte.

## Base de mana e conferência

22 terrenos: 4 Watery Grave, 4 Gloomlake Verge, 4 Undercity Sewers, 1 Hidden Grotto,
6 Island, 3 Swamp. Fontes: U 19 (Approach pede 18 no turno 3 segundo o analisador), B 16.
Único alerta do analisador: 12 fontes pretas desviradas para Manipulator no turno 1, contra
14 da tabela; aceito, porque ele é bom em qualquer turno e o azul tem prioridade.
A fórmula de Karsten pede 23,6 porque conta as duas Omniscience de valor 10 na média; elas
nunca são pagas com mana, então a média real do deck é mais baixa e 22 é o número.

Simulação de 1.000 mãos (suavização do BO1, jogando primeiro), 22 terrenos:

| Medida | Resultado |
| --- | --- |
| 2 a 4 terrenos | 95% |
| 1 terreno ou menos | 4% |
| 3 terrenos no turno 3 | 85% |
| 4 terrenos no turno 4 | 60% |
| Pelo menos 1 Approach | 93% |
| 2 ou mais Approach | 68% |
| Manipulator no turno 1 | 40% |
| Does Machines ou Charm na mão | 63% |
| 2 ou mais cartas mortas cedo (Omniscience, Unraveler) | 10% |

## Guia de sideboard

BO1, sem sideboard. North Wind Avatar e a busca "de fora do jogo" da lista modelo não
fazem sentido aqui: o fechamento está no deck principal.

## Pontos fracos

- **Zero resposta a criaturas grandes e a cemitério do oponente.** Contra Reanimator e
  Landfall, é corrida pura: o combo tem de acontecer antes do turno 5 ou 6 deles.
- **Hate de cemitério** desmonta o deck inteiro.
- **Omniscience na mão sem Unraveler** é carta morta; são 3 cópias.
- **As fichas 0/1 morrem para qualquer coisa**: jogue-as no turno da cadeia, não antes,
  salvo quando o plano for o dano incremental com Approach pagas.
- Lista não testada nesta configuração; três versões anteriores perderam três partidas.

## O que observar nos testes

- Turno médio da busca e turno médio da vitória. Se a busca sair depois do turno 6, o
  deck não compete em BO1 e a conversa passa a ser outra.
- Se Omniscience sobrar na mão: 2 cópias e o 21º terreno.
- Se faltou atacante no turno do combo: Marang River Regent (bounce de dois bloqueadores,
  grátis com Omniscience) no lugar de um Into the Flood Maw.
