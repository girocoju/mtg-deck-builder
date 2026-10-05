# Fases do jogo: os três estágios e o que cada deck quer de cada um

Este documento descreve o modelo de três estágios de uma partida (início, meio e fim de jogo) e o que ele implica para a construção: em que estágio o deck pretende vencer, quantos terrenos ele precisa para "funcionar", quais cartas pertencem a qual estágio e qual é o trunfo que sustenta o plano. Consulte-o ao definir o plano de jogo de um deck novo, ao desenhar a curva de mana, ao decidir se uma carta cara ou uma carta de início de jogo merece vaga, e ao posicionar um deck contra um metagame (ser mais rápido ou ser maior).

Nota de vocabulário: o livro prefere "estágio" (stage) a "fase" porque "fase" já tem sentido nas regras (fases do turno). Aqui, "estágio" é sempre o momento estratégico da partida, não uma fase do turno.

## Os três estágios

**O que é.** Uma partida passa por três momentos estratégicos:

- **Estágio Um (início de jogo):** o deck ainda não tem mana para operar. Na prática, o jogador está "mana-screwed": só uma pequena parte das cartas pode ser conjurada, então poucas cartas importam.
- **Estágio Dois (meio de jogo):** a maior parte das mágicas já pode ser conjurada e as disputas ainda importam. É onde há mais decisões relevantes e onde mais se erra.
- **Estágio Três (fim de jogo):** o deck opera em capacidade plena e entram em cena os trunfos, cartas ou sequências que praticamente decidem a partida. Aqui, poucas cartas do adversário ainda conseguem mudar o resultado.

Cada jogador tem o seu próprio estágio: um lado pode já estar no Dois enquanto o outro continua preso no Um.

**Quando se aplica.** Sempre que for preciso responder "como este deck ganha e em que momento". Vale para qualquer formato; o que muda é a velocidade com que cada formato atravessa os estágios.

**Como usar na construção.**

- Declare, antes de escolher cartas, em qual estágio o deck pretende obter a vantagem decisiva.
- Classifique cada carta da lista pelo estágio em que ela rende mais. Uma lista sem cartas para o estágio escolhido, ou com cartas espalhadas igualmente pelos três, não tem plano.
- Para cada adversário relevante do metagame, estime em que turno ele sai do Estágio Um e em que turno alcança o trunfo dele.

## Limiar mínimo de funcionamento (Minimum Game Threshold)

**O que é.** O número de terrenos (e de cores) a partir do qual o deck consegue conjurar a maior parte das suas cartas. Abaixo dele o deck está no Estágio Um. O livro dá como referência que muitos decks aggro funcionam com três terrenos, enquanto decks de controle costumam precisar de pelo menos quatro. O limiar é propriedade da lista, não do arquétipo: há decks midrange que também não funcionam com menos de quatro.

Cores contam. Ter quatro terrenos que não produzem as cores necessárias equivale a continuar no Estágio Um.

**Quando se aplica.** Ao dimensionar curva e base de mana, e ao avaliar se uma mão inicial é jogável (ver `mulligan.md`).

**Como usar na construção.**

- Pergunta-chave: quantos land drops o deck precisa acertar para não estar travado? Esse número é o limiar.
- A curva deve concentrar a maior parte das mágicas em custos menores ou iguais ao limiar. O que custa mais do que o limiar é carta de Estágio Três e precisa se justificar como trunfo.
- A base de mana (quantidade de terrenos e de fontes por cor) deve ser dimensionada para atingir o limiar no turno em que o plano exige, com as cores certas. Os números ficam em [base-de-mana.md](base-de-mana.md); este conceito diz qual é o alvo.
- Aceleração de mana serve para sair do Estágio Um antes do previsto; ela reduz o turno em que o limiar é alcançado, não o limiar em si.
- Limiar baixo é uma vantagem estrutural: o deck passa menos turnos sem poder jogar e tolera mãos com menos terrenos.

## Estágio Um: vencer cedo ou apenas sobreviver

**O que é.** Como quase nada pode ser conjurado, as poucas cartas baratas que entram em jogo têm peso desproporcional. Há dois usos opostos desse estágio:

- **Decks rápidos** tentam construir ali a vantagem que ganha o jogo. Para eles, uma criatura eficiente de um mana no primeiro turno é uma das melhores jogadas possíveis, mesmo sendo uma compra fraca mais tarde. O que importa é a chance de vencer antes de o adversário funcionar; não faz diferença o quão poderoso é o fim de jogo dele se ele não chega lá.
- **Decks grandes** só querem atravessar o estágio vivos e com o mínimo de dano acumulado.

**Quando se aplica.** Ao escolher as cartas de custo um e dois e ao decidir quanto do deck é dedicado ao começo da partida.

**Como usar na construção.**

- Em aggro: priorize cartas que rendem ao máximo nos primeiros turnos e limite fortemente as cartas caras de fim de jogo. Os melhores decks agressivos gastam quase toda a energia em vencer cedo, em vez de tentar competir também no Estágio Três.
- Em controle e combo: as cartas baratas existem para sobreviver (remoção barata, sweepers, interação) ou para acelerar a saída do estágio.
- Uma carta de vantagem incremental barata (por exemplo, uma criatura de dois manas que compra cartas a cada turno) é forte contra quem demora a funcionar e fraca contra quem é mais rápido do que ela. Avalie-a contra a velocidade do metagame.

**Exemplo histórico.** O livro usa Wild Nacatl: excelente no turno um de um deck agressivo de três cores, quase irrelevante comprada no meio ou no fim da partida. A queda de utilidade é aceita porque a carta maximiza a chance de vencer no Estágio Um.

## Estágio Três: trunfos e seu contexto

**O que é.** Um trunfo (trump) é a carta ou jogada que, quando resolve, praticamente vence a partida ou impede o adversário de vencer. O Estágio Três é limitado pelo maior trunfo envolvido: se o trunfo do adversário é maior, o seu deixa de ser trunfo. Nenhuma carta é trunfo em abstrato: "A trump requires context."

**Quando se aplica.** Ao escolher as condições de vitória de decks grandes, ao avaliar bombas e ao montar sideboard.

**Como usar na construção.**

- Para cada candidato a trunfo, pergunte: contra quais decks prováveis do formato isto de fato supera o melhor que o adversário faz em capacidade plena? Uma carta vira trunfo do formato se supera o plano de alguns ou de muitos adversários prováveis.
- Uma carta pode superar um deck não por responder a uma carta específica dele, mas porque o fim de jogo daquele deck é simplesmente mais fraco do que ela. A mesma carta pode ser inócua contra decks com respostas fartas ou com um trunfo maior.
- Decks de fim de jogo se beneficiam de ser construídos a partir dos trunfos: primeiro escolha o que vence o Estágio Três do formato, depois monte o restante (sobrevivência, mana, vantagem de cartas) para chegar lá. É uma alternativa aos pontos de partida mais óbvios (cores, agressividade, cartas "fortes", sinergia).
- Cartas situacionais (por exemplo, uma criatura com lifelink e proteção contra remoção de certas cores) podem ser trunfo contra burn e aggro e peso morto contra controle. Elas pertencem ao maindeck só se os alvos forem grande parte do metagame; senão, ao sideboard.

**Exemplo histórico.** Em um Standard antigo, Cruel Ultimatum era o topo dos planos de fim de jogo dos decks de controle porque quase nada do formato o superava depois de resolvido. No mesmo formato, um dragão caro era trunfo contra decks de fichas voadoras (o fim de jogo deles era mais fraco) e irrelevante contra controle, que tinha respostas de sobra e um trunfo maior.

## Estágio Dois: o meio de jogo precisa de propósito

**O que é.** O estágio das pequenas batalhas, em que se ganham e perdem pontos percentuais. A armadilha é se encantar com cartas boas de meio de jogo (trocas de dois por um, criaturas com valor ao entrar) e esquecer que o deck precisa estar posicionado como **maior** ou **mais rápido** do que o adversário. Acumular pequenas vantagens não adianta se o adversário chega a um trunfo que anula todas elas; estabilizar com pouca vida não adianta se o adversário agressivo só precisa de uma mágica de dano para fechar.

**Quando se aplica.** Ao avaliar listas midrange e listas "cheias de valor", e ao definir o papel do deck em cada confronto.

**Como usar na construção.** O Estágio Dois é usado de três formas:

| Tipo de deck | O que faz no Estágio Dois |
|---|---|
| Rápido (aggro) | Termina o jogo ali, antes de o adversário alcançar um trunfo que o deck não vence. |
| Grande (controle) | Avança a posição passo a passo (remoção, sweepers, contramágicas) para chegar vivo ao próprio trunfo, conjurado naturalmente. |
| Combo | Quer um Estágio Dois o mais curto possível: gasta recursos para trazer o Estágio Três até si. Costuma ficar preso no Dois apenas quando o adversário interage (descarte, peças de "hate"). |
| Tempo (ver `vantagem-de-cartas-e-tempo.md`) | Sai rápido do Um, instala uma fonte de vantagem por turno e mantém o adversário longe do Três com atrasos sucessivos. |

Checklist:

- O deck sabe se é o mais rápido ou o maior em cada confronto importante? Se não é nenhum dos dois, o meio de jogo dele não leva a lugar nenhum.
- As cartas de valor de meio de jogo servem a esse propósito (ganhar tempo para o trunfo, ou manter pressão até fechar)?
- Contra aggro: o deck sai do Estágio Um com folga de vida suficiente para não morrer para o alcance (dano direto) do adversário?
- Contra decks maiores: há um relógio (clock) que vence antes do trunfo deles, ou uma forma de impedir o trunfo?

## Quem costuma vencer quem

**O que é.** Regra prática do livro sobre confrontos entre decks focados em estágios diferentes:

- Decks de meio de jogo tendem a levar vantagem sobre decks de início de jogo: são um pouco maiores e ainda rápidos o bastante.
- Decks de fim de jogo tendem a vencer os de meio de jogo, pela mesma razão.
- Os decks mais rápidos frequentemente vencem os maiores, porque estes dedicam tanto ao Estágio Três que ficam expostos antes de chegar lá.

**Quando se aplica.** Ao escolher um deck para um metagame conhecido ou ao ajustar uma lista para "subir" ou "descer" de tamanho.

**Como usar na construção.**

- Identifique em que estágio a maior parte do metagame concentra forças e posicione o deck um degrau acima (um pouco maior) ou dê a volta (bem mais rápido que os decks mais gulosos).
- Tornar-se "o maior" tem custo: cada vaga dedicada ao Estágio Três é uma vaga a menos para sobreviver ao Um. Verifique se o ganho contra decks médios compensa a perda contra os rápidos.
- Tentar ser competitivo nos três estágios ao mesmo tempo costuma render menos do que parece; prefira foco.

## Referências

Next Level Magic (Chapin, 2015), Seção 3, "In-Game Magic Strategy":

- Os três estágios, limiar mínimo e Estágio Um: "The Stages of the Game", p. 178-180.
- Estágio Três e trunfos em contexto; construir sobre trunfos: "The Stages of the Game", p. 180-183.
- Estágio Dois, propósito do meio de jogo, combo e controle: "What about Stage Two?", p. 184-186.
- Quem vence quem: "What about Stage Two?", p. 187.
- Faeries como deck de Estágio Dois (linha "Tempo" da tabela): "Tempo", p. 212-213.

O livro credita a origem do modelo de estágios a Michael J. Flores ("The Breakdown of Theory").
