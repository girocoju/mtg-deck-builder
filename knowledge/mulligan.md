# Mulligan: princípios de decisão e o que eles exigem da construção

Este documento resume como decidir entre manter e trocar a mão inicial e, principalmente, o que essa decisão revela sobre a qualidade de uma lista: consistência, proporção de mãos jogáveis, número de terrenos e fontes de cor, peso das cartas baratas. Consulte-o ao avaliar a consistência de um deck, ao testar mãos de exemplo de uma lista, ao justificar a quantidade de terrenos e de jogadas de início de jogo e ao escrever orientações de "que mãos manter" para um deck entregue ao usuário.

> **Atualização posterior ao livro (regra de mulligan).** O livro é de 2015 e descreve o mulligan como embaralhar a mão e comprar uma nova com uma carta a menos. A regra atual, adotada em 2019, é o **London mulligan**: a cada mulligan compram-se sete cartas e, em seguida, colocam-se no fundo do grimório tantas cartas quantos mulligans foram feitos. Alguns formatos (como partidas multijogador de Commander) ainda concedem o primeiro mulligan sem custo. Esta nota e a seção "O que mudou com o London mulligan" não vêm do livro; todo o restante vem. Antes de afirmar a regra de um formato específico, confirme nas regras vigentes.

## O mulligan é um recurso

**O que é.** O livro trata o mulligan como mais um recurso do grupo "começa-se com ele e não se renova" (ver Philosophy of Fire em `vantagem-de-cartas-e-tempo.md`): no início da partida, o jogador pode pagar uma carta para trocar a mão inteira. A tese central é que esse recurso é subutilizado. Jogadores profissionais fazem bem mais mulligans do que amadores, que tendem a manter automaticamente qualquer mão que tenha terrenos e mágicas.

**Quando se aplica.** Em toda mão inicial, e na construção sempre que se avalia a frequência com que o deck entrega mãos que funcionam.

**Como usar na construção.** Um deck deve ser julgado também pela proporção de mãos iniciais que valem a pena manter. Mulligan frequente é um custo real, pago em cartas, e uma lista que o exige muito está pagando esse custo em quase toda partida.

## A mão precisa levar a algum lugar

**O que é.** O critério de decisão não é "tenho terrenos e mágicas?", e sim "como a partida vai se desenrolar se eu mantiver isto?". Uma mão que permite conjurar as mágicas, mas não faz nada a tempo de disputar o jogo, deve ser trocada. O raciocínio tem dois sentidos: partir do ponto em que se precisa estar para vencer e voltar até a mão; e partir da mão e projetar os próximos turnos.

A mesma mão muda de valor conforme o papel do deck no confronto. Uma mão de remoção sem ameaças é ruim para um deck agressivo que precisa pressionar, mas pode ser aceitável se, naquele confronto, o deck é quem assume o papel de controle.

**Quando se aplica.** Na decisão em jogo e, na construção, ao simular mãos de uma lista.

**Como usar na construção.**

- Ao testar mãos de exemplo, pergunte de cada uma: qual é o plano dos três ou quatro primeiros turnos? Se muitas mãos "conjuráveis" não têm plano, a lista tem um problema de composição, não de sorte.
- Decks cujo plano depende de um tipo específico de carta (uma criatura de um mana, um motor de vantagem) precisam de cópias e redundância suficientes para que a mão típica contenha esse elemento. O livro nota que bons pilotos de decks de tempo trocavam mãos sem motor, porque o tempo ganho não serviria para nada.
- Orientações de mulligan entregues junto com um deck devem ser escritas em termos de plano ("mantenha mãos com uma ameaça de custo um ou dois e ao menos dois terrenos"), não só de contagem de terrenos.

**Exemplo histórico.** No livro, um deck agressivo de três cores recebe uma mão com três terrenos, três remoções e uma carta de quatro manas. A mão é conjurável e, ainda assim, não faz o que o deck precisa nos primeiros turnos; só seria mantida se o deck fosse o lado controlador do confronto.

## Play ou draw e quantos terrenos o deck tolera

**O que é.** Duas regras de bolso:

- Mãos com mana um pouco curto são mais aceitáveis no draw do que no play (há uma compra a mais antes de o terreno fazer falta).
- Mãos lentas são mais aceitáveis no play do que no draw.

O quanto de terreno uma mão precisa depende do deck. Com um único terreno e estando no draw, há duas compras antes de perder um land drop: um deck agressivo de curva muito baixa pode aceitar o risco; um deck de controle de muitas cores não pode. Cores contam tanto quanto quantidade: uma mão com terrenos que não produzem a cor das mágicas é, na prática, uma mão sem mana para elas.

**Quando se aplica.** Na decisão em jogo; na construção, ao definir curva e base de mana.

**Como usar na construção.**

- Quanto mais baixo o limiar de funcionamento do deck (ver `fases-do-jogo.md`), mais mãos de poucos terrenos são jogáveis. Curva baixa é, entre outras coisas, uma ferramenta de consistência.
- Decks de muitas cores ou de curva alta têm menos mãos jogáveis; isso precisa ser compensado com mais terrenos, mais fontes por cor ou filtragem. Os números de referência ficam em [base-de-mana.md](base-de-mana.md).
- Avalie a lista nos dois cenários (play e draw): um deck lento sofre mais no draw, um deck de mana apertado sofre mais no play.

## Calcular a chance de "chegar lá"

**O que é.** Para decidir se uma mão incompleta vale o risco, identifique o que falta comprar para ela se tornar jogável e estime a chance de isso acontecer até o turno em que importa. O método do livro: calcular a chance de **errar** todas as compras e subtrair de 100%.

- Para uma compra: chance de errar = (cartas que não servem) / (cartas restantes no grimório).
- Para várias compras: multiplique as chances de errar de cada compra, lembrando que o grimório diminui uma carta por vez, e subtraia o produto de 100%.
- Somar as chances de acertar de cada compra é erro: superestima o resultado.
- Arredondar as frações para fazer a conta de cabeça é aceitável.
- Com o grimório pequeno, cada compra errada aumenta bastante a chance da seguinte.

Tabela de apoio, calculada com esse método para um deck de 60 cartas depois da mão inicial de sete (53 cartas no grimório), dando a chance de comprar ao menos uma das cartas necessárias:

| Cartas que servem no grimório | 1 compra | 2 compras | 3 compras | 4 compras |
|---|---|---|---|---|
| 4 | 8% | 15% | 21% | 28% |
| 8 | 15% | 28% | 39% | 49% |
| 12 | 23% | 40% | 54% | 65% |
| 15 | 28% | 49% | 64% | 75% |
| 18 | 34% | 57% | 72% | 82% |
| 22 | 42% | 66% | 81% | 89% |

No play, o número de compras até o turno N é N-1; no draw, é N.

**Quando se aplica.** Na decisão de manter uma mão a que falta uma cor ou um terreno; na construção, ao dimensionar fontes de cor e número de cópias de cartas-chave.

**Como usar na construção.**

- Use a tabela ao contrário: quantas fontes de uma cor o deck precisa para que uma mão sem essa cor ainda a encontre a tempo com probabilidade aceitável? Com 15 fontes restantes, uma mão sem a cor só a encontra até o turno dois em 28% das partidas no play e 49% no draw.
- Para cartas-chave em quatro cópias, a chance de comprá-las nos primeiros turnos depois de uma mão sem elas é baixa (linha "4"); se o plano depende delas, é preciso redundância (efeitos equivalentes, busca, filtragem).
- Para cálculos exatos de mãos iniciais e bases de mana, use ferramentas determinísticas e [base-de-mana.md](base-de-mana.md); este método é a aproximação para decisões rápidas.

**Exemplo histórico.** O caso do livro é uma mão de sete com dois terrenos de uma cor e cinco mágicas que pedem outra cor, num deck com 15 fontes dessa segunda cor. No play, a mão tem chance alta de não fazer nada por vários turnos; no draw, as chances melhoram o bastante para mudar a avaliação.

## Seis cartas boas contra sete ruins

**O que é.** A pergunta final é comparativa: uma mão aleatória com uma carta a menos tem mais chance de vencer do que esta? Segundo o livro, a resposta é "sim" com mais frequência do que a maioria imagina. Vale também pensar um passo adiante: que mãos de seis eu manteria, e quais mandaria de volta?

Ir a cinco cartas não é derrota automática. Se a mão atual não tem como vencer, trocar por uma chance pequena é melhor do que manter uma chance nula. E, depois do mulligan, é preciso manter a disciplina: jogar da forma que maximiza a chance restante, por menor que seja, sem deixar a frustração piorar as decisões.

**Quando se aplica.** Em mãos marginais e depois de um primeiro mulligan.

**Como usar na construção.**

- Decks com muitas cartas individualmente fortes e baratas se recuperam melhor de mulligans do que decks que precisam de várias peças específicas ao mesmo tempo. Ao comparar duas listas, considere como cada uma joga com seis e com cinco cartas.
- Fontes de vantagem de cartas e filtragem ajudam a repor o que o mulligan custou.

## O que mudou com o London mulligan (atualização posterior ao livro)

**Continua válido:**

- Decidir pela projeção da partida, não pela simples presença de terrenos e mágicas.
- Considerar o papel do deck no confronto e a diferença entre play e draw.
- O método de probabilidade para as compras seguintes.
- A comparação "esta mão contra a mão que eu teria com uma carta a menos".
- Não temer o mulligan e não desistir depois dele.
- A tese de que manter mãos medíocres por inércia é um erro comum.

**Está datado ou precisa de ajuste:**

- O custo do mulligan caiu. No livro, a mão nova é uma mão aleatória menor. Hoje veem-se sete cartas e escolhem-se as que ficam, de modo que a mão de seis é, em média, melhor do que seis cartas ao acaso. A conclusão do livro (fazer mais mulligans do que o instinto manda) fica ainda mais forte.
- A comparação correta deixou de ser "sete ruins contra seis aleatórias" e passou a ser "sete ruins contra as melhores seis de sete novas".
- Procurar cartas específicas ficou mais viável: cada mulligan mostra sete cartas novas. Isso favorece decks que dependem de uma peça-chave e cartas de sideboard de alto impacto, e deve ser levado em conta ao avaliar essas estratégias no metagame.
- Cartas redundantes ou mortas no confronto podem ir para o fundo, o que reduz um pouco o custo de incluí-las; excesso ou falta de terrenos numa mão de sete pós-mulligan também pode ser corrigido na escolha do que fica.
- Os exemplos de mãos e decks do livro são de formatos antigos; servem como ilustração do raciocínio, não como referência de listas.

## Implicações para a construção (síntese)

O capítulo é sobre decisões em jogo; as regras abaixo são as consequências para quem monta a lista, derivadas dos princípios acima.

1. **Meça a taxa de mãos jogáveis.** Simule mãos iniciais e classifique-as pelo critério do plano (a mão leva a algum lugar?), não só pela contagem de terrenos. Faça isso para play e draw.
2. **Dimensione terrenos e fontes pelo limiar do deck.** O alvo é atingir o número de terrenos e as cores de que o deck precisa no turno em que o plano exige. Limiar mais alto ou mais cores exigem mais terrenos e mais fontes.
3. **Cartas baratas dão consistência.** Elas reduzem o limiar, tornam jogáveis as mãos de poucos terrenos e melhoram as mãos de seis e de cinco.
4. **Redundância para o que é essencial.** Se o plano depende de um tipo de carta nos primeiros turnos, tenha cópias e equivalentes suficientes para que a mão típica o contenha.
5. **Evite mãos que conjuram e não fazem nada.** Excesso de cartas reativas num deck proativo, ou de cartas caras num deck rápido, produz mãos "mantíveis" que perdem.
6. **Considere o desempenho pós-mulligan.** Listas que funcionam com menos cartas são mais robustas do que listas que precisam de todas as peças.
7. **Entregue orientação de mulligan com o deck.** Descreva as mãos a manter e a trocar em termos do plano, com a ressalva da regra vigente no formato.

## Referências

Next Level Magic (Chapin, 2015), Seção 3, "In-Game Magic Strategy", capítulo "Less Can Be More: The Art of the Mulligan":

- Mulligan como recurso; a mão precisa levar a algum lugar; papel no confronto: p. 224-225.
- Play ou draw; tolerância a poucos terrenos; cores: p. 225-226.
- Método de probabilidade (chance de errar, várias compras, arredondamento, grimório pequeno): p. 226-227.
- Seis contra sete; mulligan a cinco; disciplina depois do mulligan: p. 227-229.
- Mulligan de mãos sem motor em decks de tempo: capítulo "Tempo", p. 215-216.

Fora do livro: a nota de atualização e a seção "O que mudou com o London mulligan" (regra adotada em 2019), a tabela de probabilidades (calculada com o método do livro) e a síntese "Implicações para a construção".
