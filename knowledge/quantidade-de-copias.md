# Quantidade de cópias: 4, 3, 2 ou 1

Este documento explica como decidir quantas cópias de cada carta entram em um deck. O
agente deve consultá-lo ao fechar os números de uma lista, ao justificar por que uma carta
forte aparece com menos de quatro cópias, ao cortar cartas para chegar a 60 e ao distribuir
as vagas do sideboard. Vale para formatos com limite de quatro cópias; para singleton, ver
a nota no final.

Princípio geral: o número de cópias é uma forma de **controlar a probabilidade de comprar
a carta**. Nem toda carta boa é uma carta que você quer comprar o máximo possível.

## 1. Retornos decrescentes (o conceito que organiza tudo)

**O que é.** Cada cópia adicional de uma carta no deck costuma valer um pouco menos que a
anterior. A primeira cópia acrescenta uma opção que o deck não tinha; a quarta só aumenta
um pouco a chance de ver algo que você já provavelmente veria. Além disso, cópias
repetidas na mão podem valer menos (a segunda não muda o jogo) ou até atrapalhar (carta
cara presa na mão enquanto você apanha).

Poucas cartas fogem disso por melhorarem com mais cópias: as que se alimentam de cópias
da mesma carta no cemitério (Accumulated Knowledge), burn que soma até 20
(Lava Spike) e criaturas que se reforçam mutuamente.

**Quando se aplica.** Sempre. Toda carta tem um ponto em que a cópia extra deixa de
compensar; a questão é se esse ponto fica acima de quatro (use quatro e talvez procure
substitutas) ou abaixo (use três, duas ou uma).

**Como usar na construção.** Para cada carta, faça duas perguntas:
1. Quanto vale comprar a **segunda** cópia no mesmo jogo? (vale igual / vale menos / é morta / me prejudica)
2. Quanto custa **não** comprar nenhuma? (perco o jogo / sinto falta / tanto faz)

A curva de queda é diferente para cada carta e não depende só do custo de mana: uma
remoção barata e excelente também sofre retorno decrescente, porque o deck não precisa de
tantas quanto consegue comprar.

**Exemplo histórico.** Cruel Ultimatum, mágica de sete manas que costuma decidir o jogo
sozinha: os decks vencedores usavam duas ou três, porque uma resolvida basta e duas na mão
inicial são um desastre contra agressão. Da mesma forma, controles usavam três cópias da
melhor criatura finalizadora: se o deck só quer três condições de vitória, a quarta cópia
não acrescenta nada.

## 2. Quatro cópias

**O que é.** O máximo: você quer ver a carta em todo jogo e o mais cedo possível.

**Quando se aplica.**
- A carta está entre as melhores do deck e cópias repetidas continuam boas.
- O plano depende dela cedo (jogadas de turno 1 a 3, peça de motor, remoção barata que
  recupera tempo).
- Em decks agressivos e lineares, o ponto de saturação costuma ficar acima de quatro:
  se pudesse, você jogaria cinco.

**Como usar na construção.** Pergunta de teste: "eu jogaria uma quinta cópia?" Se sim, são
quatro, e vale procurar as cópias 5 a 8 (seção 6). Se a resposta for "quatro com certeza,
cinco talvez", ainda são quatro.

**Exemplo histórico.** Lightning Bolt num controle com muitos terrenos virados: quatro
cópias porque é barata, flexível, instantânea e devolve o tempo perdido pela mana lenta.

## 3. Três cópias

**O que é.** Você gosta de comprar a carta na maioria dos jogos, mas comprar duas ou três
é ruim em parte deles.

**Quando se aplica.**
- Varreduras e respostas situacionais em controle: ótimas contra alguns decks, um peso
  em dobro contra outros. Três é o número típico para esse tipo de efeito.
- Cartas lendárias ou em que a segunda cópia fica parada na mão.
- Finalizadoras caras: quer achar uma, não duas no começo.
- O número "ideal" seria fracionário. Chapin descreve querer algo como 3,3 cópias de uma
  criatura defensiva e concluir, testando, que três se aproxima mais disso do que quatro.
- Decks com wish (mágicas que buscam cartas fora do jogo): três na lista e a quarta no
  sideboard como alvo.

**Como usar na construção.** Se uma carta "obviamente de quatro cópias" tem matchups em
que a segunda cópia é fraca, teste três e use a vaga para algo barato.

## 4. Duas cópias

**O que é.** Você quer acesso à carta ao longo de um jogo longo, mas não precisa dela cedo
e não quer vê-la repetida.

**Quando se aplica.**
- Decks que compram muitas cartas: duas cópias aparecem com frequência razoável até o meio
  do jogo.
- Complemento de uma função já coberta por outras cartas (a "sétima e oitava" remoção).
- Carta que resolve problemas que a sua carta preferida da mesma função não resolve.
- A versão mais fraca usada para completar um pacote (seções 6 e 7).
- Cartas poderosas, mas caras, quando o topo da curva já está cheio.
- Ameaças de sideboard que você quer comprar sem revalidar a remoção do oponente.

**Como usar na construção.** A segunda cópia rende muito mais que a quarta. **Números do
livro (2015):** ir de uma para duas cópias aumenta em cerca de 70% a chance de ver a carta
nas primeiras vinte cartas; ir de três para quatro aumenta em apenas cerca de 23% a
chance de tê-la no turno 3.

## 5. Uma cópia

**O que é.** Dar ao deck acesso a um efeito, minimizando a chance de comprá-lo quando não
serve.

**Quando se aplica.**
- **Alvo de tutor:** o deck busca a carta quando precisa (bala de prata para um tutor de
  artefatos baratos, a condição de vitória de um combo com tutores).
- **"Uma é muito mais que zero":** respostas estreitas e potentes cuja segunda cópia não
  faz nada. Com duas vagas, uma cópia de cada uma de duas cartas cobre dois problemas em
  vez de um. **Números do livro (2015):** depois de ver metade do deck, uma cópia de cada
  dá 50% de chance de ver cada uma; duas cópias da mesma dão 75% para ela e zero para a outra.
- **Divisão de uma vaga:** a quarta carta de um pacote é diferente das outras três
  (seção 8).
- **Finalizadora alternativa:** um jeito de vencer que escapa das respostas que param o
  seu plano principal.
- **Terrenos e cartas péssimos em dobro:** quando comprar dois seria muito ruim.

**Como usar na construção.** Cópia única sem tutor nem muita compra é uma carta que você
verá em poucos jogos: só vale se o efeito for de alto impacto quando aparece e não for
essencial ao plano. Uma lista cheia de cópias únicas sem motivo é inconsistente; o livro
é explícito em que o argumento não é "tudo singleton", e sim avaliar cada cópia.

## 6. Furar a regra de quatro: cópias 5 a 8

**O que é.** Quando o deck quer mais de quatro de um efeito, completa-se com a segunda
melhor carta que faz o mesmo, mesmo sendo mais fraca.

**Quando se aplica.** Efeito central do plano, com saturação acima de quatro.

**Como usar na construção.** Quatro da melhor + duas ou mais da substituta. O número de
cópias da substituta responde a "quantos deste efeito eu quero ao todo?", e não à
qualidade dela.

**Exemplo histórico.** Um deck que queria seis mágicas de custo 4 com cascade usou quatro
Bloodbraid Elf e duas Kathari Remnant, bem inferior. Um controle que queria seis mágicas
de compra usou quatro Esper Charm e duas Divination; o total de seis saiu de testes entre
quatro e nove.

## 7. Contar por função e por curva, não por carta

**O que é.** O deck tem necessidades agregadas (N remoções baratas, N criaturas de custo 1,
N counters que respondem a qualquer coisa) que raramente são múltiplos de quatro.

**Como usar na construção.**
1. Defina quantas vagas cada função precisa. Use três perguntas: quanto quero comprar uma
   contra quase todos? Quantas não posso comprar em excesso contra alguns? Que outras
   cartas do deck aliviam essa função?
2. Preencha da melhor carta para a pior: as melhores com quatro, a mais fraca com o resto.
3. Confira a curva: entre duas cartas da mesma função, a distribuição pode ser decidida
   pelo custo de mana. Com topo de curva forte, prefira a cópia extra da carta barata.

**Exemplo.** Curva pedindo catorze criaturas de custo 1: três cartas com quatro cópias e a
mais fraca com duas. **Exemplo histórico:** o controle de 2009 queria nove respostas
baratas a criaturas e chegou a 4 + 3 + 2 entre três cartas diferentes; queria no mínimo
quatro counters capazes de responder a qualquer mágica, pois cair para três reduziria em
24% a chance de ter um no turno 5, e subir para cinco renderia só 14% a mais (números do
livro, 2015).

## 8. Dividir entre cartas parecidas

**O que é.** Em vez de 4 + 0, usar 3 + 1 entre duas cartas da mesma função.

**Quando se aplica.** A carta principal sofre retorno decrescente e a alternativa cobre
casos que ela não cobre.

**Como usar na construção.** Benefícios: menos mãos com duas cópias da carta condicional;
a combinação "uma de cada" costuma ser melhor que "duas iguais"; nunca se compram duas da
carta mais fraca; uma única carta cumpre duas contagens (por exemplo, quarta resposta
barata e quarta resposta universal); o oponente precisa respeitar a possibilidade da
carta diferente; e nomes variados resistem a efeitos que nomeiam uma carta. Não divida
quando a alternativa é apenas medíocre em tudo, em vez de ótima em alguns casos.

## 9. Compra e seleção reduzem o número de cópias

**O que é.** Decks com muita compra e manipulação de biblioteca veem mais cartas por jogo.

**Como usar na construção.**
- Precisam de menos cópias para achar cada efeito, e têm menos espaço, porque boa parte
  das vagas vai para compra e mana.
- Estrutura típica de controle: três de cada resposta em vez de quatro, e as vagas
  liberadas viram compra. O deck encontra a resposta certa com mais frequência mesmo com
  menos cópias, e a vantagem de cartas compensa as respostas erradas e o excesso de
  terrenos.
- Por isso controles terminam cheios de "dois e três", e aggros cheios de "quatro".

## Tabela-resumo de decisão

| Cópias | Use quando | Sinal de alerta |
|---|---|---|
| 4 | Entre as melhores do deck; necessária cedo; cópias repetidas continuam boas; você jogaria a quinta | Segunda cópia na mão é fraca ou injogável |
| 4 + substitutas | O efeito é central e você quer 5 a 8 dele | A substituta é fraca demais para justificar a função |
| 3 | Quer ver na maioria dos jogos, mas duas na mão é ruim em vários matchups; lendárias; varreduras; finalizadoras; alvo de wish no sideboard | Você sente falta dela com frequência (suba para 4) |
| 2 | Quer achar no jogo longo, não no início; completa um pacote por função; versão mais fraca de um efeito; topo de curva já cheio | O plano depende de comprá-la cedo |
| 1 | Alvo de tutor; resposta estreita de alto impacto; finalizadora alternativa; divisão 3 + 1; péssima em dobro | Não há tutor nem compra e o efeito é essencial |
| 0 | A melhor carta da função já ocupa as vagas que a função merece | — |

Perguntas rápidas antes de fechar o número:
- Preciso dela na mão inicial ou só em algum momento do jogo?
- A segunda cópia comprada vale quanto?
- Quantas vagas a **função** merece, e que outras cartas a cumprem?
- Quantas cartas o deck vê por jogo?
- A curva tem espaço para mais uma nesse custo?
- A primeira cópia de outra carta valeria mais que esta cópia adicional?

## Atualização posterior ao livro: formatos singleton

**Atualização posterior ao livro.** Em Commander e Brawl só se pode usar uma cópia de cada
carta (exceto terrenos básicos), de modo que a consistência não vem de cópias, e sim de
**redundância funcional**: várias cartas diferentes que cumprem a mesma função (ramp,
compra, remoção pontual, varredura, proteção), além de tutores e do comandante, que está
sempre disponível. O raciocínio das seções 6 e 7 continua válido, levado ao extremo: conte
vagas por função e preencha da melhor carta para a pior. A lógica de retornos decrescentes
passa a valer para a função como um todo: quantas varreduras o deck quer comprar por jogo,
e não quantas cópias de uma varredura.

## Referências

*Next Level Magic* (Chapin, 2015).

| Seção deste documento | Capítulo | Páginas |
|---|---|---|
| 1 | Knowing How Many of Each Card To Use | 244-246 |
| 2 | Knowing How Many of Each Card To Use | 244, 246, 248 |
| 3 | Knowing How Many of Each Card To Use | 247-248, 251-253 |
| 4 | Knowing How Many of Each Card To Use | 249-250, 252, 257 |
| 5 | Knowing How Many of Each Card To Use | 244, 253-254, 256, 258-259 |
| 6 | Knowing How Many of Each Card To Use | 246-247, 251 |
| 7 | Knowing How Many of Each Card To Use | 247, 249-250 |
| 8 | Knowing How Many of Each Card To Use | 250-251, 257-258 |
| 9 | Knowing How Many of Each Card To Use | 247-249 |
| Singleton | Atualização posterior ao livro (não consta na fonte) | — |
