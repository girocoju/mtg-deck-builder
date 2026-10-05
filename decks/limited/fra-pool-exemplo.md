# Reality Fracture — deck de 40 a partir de um pool de 45 cartas (exemplo)

- **Formato:** limited (40 cartas) · **Coleção:** FRA · **Data:** 2026-10-05
- **Dados:** 17Lands, Premier Draft, coletados em 2026-10-05
- **Origem do pool:** três pacotes sorteados por script (10 comuns, 4 incomuns e 1 rara
  cada), sem escolha de picks. É um teste do fluxo de montagem, mais difícil que um draft
  real, em que o pool já vem concentrado em duas cores.

```
Deck
1 Kiora of Fire and Ashes
1 Wrath of the Bloodmane
1 No Admittance
2 Chandra's Emberling
1 Tetsuko Umezawa, Pursuer
1 Winter, Team Player
1 Whiplash Wordsmith
1 Eardrum Rattler
1 Mindseeker Oculus
1 Icy Reception
1 Infinite Coursework
1 Divining Duelist
1 Cryotheory Adept
1 Theorix Metamage
1 Fatehold Chronologist
1 Saheeli, Jewel of Avishkar
1 Archive Arbiter
1 Medic's Kitesail
2 Afterthought Sentry
1 Surgical Precision
1 Innovative Commons
2 Fatehold Annex
1 Dedicated Commons
7 Island
7 Mountain
```

## Escolha das cores

`mtg draft rate fra --file <pool>` agrupou o pool por cor. Azul e vermelho têm as
melhores cartas e o maior número de jogáveis:

- **Vermelho:** Kiora of Fire and Ashes (61,6%, a melhor carta do pool), Wrath of the
  Bloodmane (57,0%) e No Admittance (56,5%) — as duas melhores remoções.
- **Azul:** Mindseeker Oculus (61,3%), Icy Reception (58,8%), Infinite Coursework (57,2%).
- **Liga as duas:** Saheeli, Jewel of Avishkar (57,0%) e o terreno Innovative Commons.
- Branco tinha Kindred Judgment (60,4%), mas a {5}{W}{W}; verde e preto, só cartas
  abaixo da média além de Gideon the Oathless.

UR é um par mediano no formato (55,4%), mas era o que o pool sustentava.

## O que ficou de fora e por quê

- Gideon the Oathless (58,3%) e Kindred Judgment (60,4%): fora das cores.
- Konstrari Charm (56,9%): pede verde.
- Verdes e pretas restantes: todas abaixo de 56%.

## Compromissos desta lista

- **22 mágicas e 18 terrenos.** O pool só tinha 21 cartas conjuráveis em UR, três delas
  híbridas (Whiplash Wordsmith, Theorix Metamage, Fatehold Chronologist). Com a curva
  subindo até custos 5 e 6, o 18º terreno é melhor que uma carta fora das cores.
- **Splash de uma carta:** Surgical Precision ({1}{W}) entra apoiada nos três terrenos
  duplos que já estariam no deck (2 Fatehold Annex, 1 Dedicated Commons). `mtg deck
  analyze` acusa falta de fontes brancas: a ferramenta mede a exigência de cor principal
  (9 fontes) e não tem o conceito de splash. O alerta é aceito; a carta tem um modo de
  compra e fica na mão até a fonte aparecer.
- **Terrenos duplos lentos:** os Annex e Commons entram virados sem um planeswalker em
  jogo, e o deck só tem duas cartas que criam a ficha de Jace (Mindseeker Oculus e No
  Admittance). A análise os conta como desvirados.
- **Recheio fraco:** Eardrum Rattler (48,0%) e Afterthought Sentry (52,2%) entram por
  falta de opção.

## Honestidade

Deck de exemplo, não jogado. Um pool sorteado de 45 cartas não representa um draft; o
objetivo foi verificar que o fluxo (avaliar o pool com dados, escolher cores, montar,
validar e analisar) funciona de ponta a ponta.

## Pool completo (45 cartas)

Theorix Annex, Innovative Commons, Medic's Kitesail, 2 Fatehold Annex, Archive Arbiter,
Dedicated Commons, Overgrown Farmland, 2 Afterthought Sentry, Gideon the Oathless,
Screeching Soulbreaker, Solve for Disappointment, Whiplash Wordsmith, Ruric Thar,
Magecrusher, Vinelasher Adept, Ghalta the Unstoppable, Greenhouse Propagator, Titanbones,
Towering Heart, Edgar, Moonlit Sovereign, Hunter's Axe, Kiora of Fire and Ashes, Wrath of
the Bloodmane, No Admittance, 2 Chandra's Emberling, Tetsuko Umezawa, Pursuer, Eardrum
Rattler, Winter, Team Player, Konstrari Charm, Mindseeker Oculus, Icy Reception, Infinite
Coursework, Divining Duelist, Cryotheory Adept, Theorix Metamage, Saheeli, Jewel of
Avishkar, Kindred Judgment, Surgical Precision, Unflinching Hortimancer, Tomik, Orzhov
Lawmage, Blossom-Blessed Angel, Academic Ascent, Emergency Phytomedic, Fatehold Chronologist.
