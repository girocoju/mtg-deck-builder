# Valor das cartas: relativo, médio e a ilusão do valor fixo

Este documento explica como avaliar uma carta: não por uma nota absoluta, mas pelo que ela vale dentro de um deck, de um formato e de um metagame específicos, e sempre em comparação com a carta que sairia para lhe dar lugar. Consulte-o ao decidir se uma carta entra na lista, ao comparar duas candidatas para a mesma vaga, ao priorizar escolhas em draft e sempre que a justificativa para uma carta for apenas "ela é boa".

## Valor fixo é uma armadilha

**O que é.** "Valor fixo" é a crença de que uma carta tem uma força própria, independente de onde é jogada. O livro trata isso como erro: o valor é sempre determinado pelo contexto. Perguntar "quão boa é esta carta?" não tem resposta sem saber o formato, a situação de jogo em que ela será usada, a curva e a base de mana do deck e o que precisaria sair para ela entrar.

**Quando se aplica.** Em toda avaliação de carta. É especialmente importante com cartas famosas, que tendem a ser incluídas por reputação.

**Como usar na construção.**

- Nunca justifique uma inclusão só pela qualidade abstrata da carta. A justificativa deve nomear o contexto: o papel no plano do deck, o estágio do jogo em que ela atua e contra o que ela é boa.
- Verifique as condições de uso: o deck produz as cores e a quantidade de mana que ela pede, no turno em que ela importa?
- Desconfie do critério "só tem vantagens". Uma carta sem desvantagem aparente ainda custa mana, uma carta da mão e uma vaga na lista (ver "o custo embutido de uma carta" em `vantagem-de-cartas-e-tempo.md`).

## Valor relativo e valor médio

**O que é.** Dois valores são úteis de verdade:

- **Valor relativo:** quanto a carta vale neste contexto concreto (este deck, estas sinergias, este metagame, este estágio do jogo).
- **Valor médio:** quanto a carta vale em geral no formato, sem conhecer o deck. É uma estimativa abstrata, calibrada pelo formato e pelo estilo de quem joga.

A regra do livro: usar o valor relativo sempre que possível e o valor médio só quando faltar informação.

**Quando se aplica.**

- Valor médio: primeiras escolhas de um draft, primeira triagem de um conjunto grande de cartas candidatas, avaliação de cartas novas antes de existir um deck para elas.
- Valor relativo: assim que houver contexto (cartas já escolhidas, arquétipo definido, metagame conhecido).

**Como usar na construção.**

- Em construído, a triagem inicial de candidatas pode usar valor médio (cartas reconhecidamente fortes no formato), mas a decisão final de cada vaga é sempre por valor relativo.
- Em draft, a ordem de escolha muda ao longo do draft: no início vale a força geral; depois, cada carta já escolhida altera o valor das próximas. Reavalie as sinergias e as antissinergias a cada escolha.
- Ao explicar uma escolha, diga qual dos dois valores sustentou a decisão e por quê.

**Exemplo histórico.** No livro, uma remoção barata é a primeira escolha natural sobre uma carta de nicho. Mas, se as primeiras escolhas já foram cartas que combinam com a carta de nicho, o valor relativo dela sobe a ponto de superar a remoção. O princípio: sinergia com o que já está no deck pode inverter a ordem dada pelo valor médio.

## Custo de oportunidade: a carta que sai

**O que é.** Incluir uma carta significa excluir outra. A comparação correta não é "esta carta é boa?", e sim "esta carta é melhor, neste deck, do que a que sairia?". Muitos jogadores imaginam a carta nova no vácuo e não fazem a comparação.

O mesmo raciocínio explica por que jogar acima do tamanho mínimo do deck costuma ser erro: cada carta além do mínimo reduz a chance de comprar as melhores cartas na mesma medida em que aumenta a chance de comprar a pior, que é justamente a carta excedente. O livro admite exceções raras (ajuste fino da proporção de mana, plano de vencer por esgotamento do grimório), mas afirma que, na grande maioria dos casos, quem joga acima do mínimo está se enganando sobre os motivos.

**Quando se aplica.** Em toda troca de cartas em uma lista, ao fechar as últimas vagas e ao montar o sideboard.

**Como usar na construção.**

- Para cada inclusão proposta, nomeie a carta que sai e compare as duas no contexto do deck.
- Em formatos com tamanho mínimo (60 em construído, 40 em limitado), use o mínimo como padrão. Só exceda com um motivo concreto e declarado. Em formatos de tamanho exato (Commander, Brawl) a pergunta não existe, mas o custo de oportunidade por vaga continua valendo.
- Ordene as cartas da lista da melhor para a pior no contexto do deck. A pior é a referência: toda candidata nova precisa superá-la.

## O erro do jogador experiente: preferir o que já conhece

**O que é.** Iniciantes erram ao adicionar cartas sem considerar o que perdem. Jogadores bons cometem um erro mais sutil: escolhem as cartas "claramente boas" e deixam de fora aquelas cujo valor não sabem estimar, como uma rara estranha que nunca jogaram, por falta de experiência com ela e com as interações dela com o resto do deck. Os melhores jogadores buscam avaliar todas as cartas com precisão, sempre em relação ao contexto.

**Quando se aplica.** Ao avaliar cartas novas, cartas pouco jogadas ou efeitos incomuns; ao procurar tecnologia contra um metagame estabelecido.

**Como usar na construção.**

- Não descarte uma carta só por ser desconhecida ou difícil de avaliar. Estime o valor relativo: o que ela faz neste deck, em que estágio, contra quais adversários.
- Ao pesquisar a base de cartas, inclua na análise candidatas fora do repertório habitual do formato e avalie-as pelo mesmo critério das conhecidas.
- Quando a incerteza for alta, registre-a explicitamente na justificativa em vez de recorrer automaticamente à opção conhecida.

## O estágio em que a carta é jogada

**O que é.** Parte central do contexto é o estágio da partida em que a carta chega à mesa (ver `fases-do-jogo.md`). Uma carta cara só entra no Estágio Três; ali ela concorre com os trunfos do formato. Se for um trunfo fraco para o formato, ela é ruim, por mais impressionante que pareça isoladamente. A mesma carta pode ser um trunfo decisivo em um ambiente onde os trunfos concorrentes são mais fracos.

**Quando se aplica.** Ao avaliar cartas de custo alto, bombas de limitado transportadas para construído, e cartas de início de jogo em decks lentos.

**Como usar na construção.**

- Para cada carta, pergunte: em que turno e em que estágio ela será conjurada? O que o adversário típico está fazendo nesse mesmo momento?
- Compare cartas caras com os trunfos reais do formato, não com cartas do mesmo custo em geral.
- O valor muda entre formatos: reavalie do zero ao levar uma carta de limitado para construído, ou de um formato com poucas cartas legais para um com muitas.

**Exemplo histórico.** Shivan Dragon: em limitado, um voador grande de seis manas costuma decidir a partida; em construído, chega tarde e perde para os trunfos do formato. A carta é a mesma; o contexto mudou o valor.

## O metagame como contexto

**O que é.** O valor de uma carta também depende de quem está do outro lado. Uma carta pode ser excelente contra burn e aggro de certa cor e quase inútil contra controle ou contra criaturas grandes. O que define se ela merece vaga é a proporção de adversários prováveis contra os quais ela supera o plano do oponente. Da mesma forma, o preço justo de um efeito varia com o formato: comprar uma carta extra por três manas pode ser ótimo em um formato e irrelevante em outro, onde há formas muito mais baratas de fazer o mesmo.

**Quando se aplica.** Ao construir contra um metagame conhecido (pedidos "anti-meta"), ao dividir cartas entre maindeck e sideboard e ao comparar a mesma carta em formatos diferentes.

**Como usar na construção.**

- Para cartas situacionais, liste contra quais decks do metagame ela é forte, neutra e fraca, e pondere pela fatia de cada deck. Dados de metagame têm fonte e data; sem eles, declare que a avaliação é teórica.
- Forte contra grande parte do campo: maindeck. Forte contra uma fatia relevante, fraca contra o resto: sideboard.
- Compare o custo de um efeito com as alternativas disponíveis no mesmo formato, não com uma tabela universal.

## Perguntas de avaliação (resumo)

1. Qual é o papel desta carta no plano do deck?
2. Em que estágio do jogo ela é jogada, e o que ela enfrenta nesse momento?
3. O deck consegue conjurá-la a tempo (curva, cores)?
4. Com quais cartas da lista ela tem sinergia ou antissinergia?
5. Contra quais decks do metagame ela é boa, e qual a fatia deles?
6. Qual carta sai para ela entrar, e por que a troca melhora o deck?
7. A avaliação usa valor relativo ou, por falta de contexto, valor médio?

## Referências

Next Level Magic (Chapin, 2015), Seção 3, "In-Game Magic Strategy":

- Valor fixo, valor relativo e valor médio; custo de oportunidade; tamanho mínimo do deck; erro do jogador experiente: "Relative vs. Fixed Values of Cards", p. 188-189.
- Estágio em que a carta é jogada (Shivan Dragon); valor médio e relativo em draft: "Relative vs. Fixed Values of Cards", p. 189-191.
- Metagame como contexto (trunfos situacionais): "The Stages of the Game", p. 182-183; valor de uma carta extra conforme o formato: "Card Advantage", p. 198.
