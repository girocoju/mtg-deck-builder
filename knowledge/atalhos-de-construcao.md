# Atalhos de construção e de escolha de deck

Este documento reúne as heurísticas ("atalhos") que permitem tomar boas decisões de
deckbuilding sem testar todas as possibilidades. O agente deve consultá-lo **no
início de qualquer pedido de construção** (para decidir por onde começar), ao
**avaliar uma lista encontrada em outra fonte** e ao **escolher entre cartas ou
decks concorrentes**. A parte de draft é só um resumo; o tema terá documento próprio.

## Por que atalhos: o gargalo de informação

**O que é.** Em Magic, cada decisão (qual carta incluir, qual deck jogar, qual pick
fazer) tem mais consequências possíveis do que dá para avaliar. O ideal seria testar
cada variante em milhares de partidas; na prática há pouco tempo. Um atalho é uma
regra sistemática que leva a uma boa decisão rapidamente. A tese do livro é que quem
dispõe de mais atalhos, e de atalhos melhores, tende a vencer.

**Quando se aplica.** Sempre que o espaço de opções for grande demais: o conjunto de
cartas legais de um formato, as dezenas de listas publicadas, as 14 cartas de um
booster.

**Como usar na construção.**

- Trate cada heurística deste documento como um **gatilho**: uma condição que, quando
  ocorre, obriga a parar e fazer uma pergunta específica.
- Prefira atalhos preparados **antes** da decisão (plano de sideboard já definido,
  lista de categorias a verificar, modelos de arquétipo) a raciocínio improvisado.
- Atalhos economizam esforço, não substituem verificação: a lista final ainda
  precisa ser testada e validada.

## Primeiro atalho: "o que estou tentando realizar?"

**O que é.** Diante de uma situação nova ou confusa, a primeira pergunta é qual é o
objetivo. Definir o objetivo reorganiza toda a informação disponível: os mesmos
dados levam a decisões diferentes conforme o que se quer alcançar.

**Quando se aplica.** No começo de todo pedido e sempre que houver dúvida entre
duas opções razoáveis.

**Como usar na construção.** Antes de escolher qualquer carta, o agente deve fixar:

- O que o usuário quer do deck? (Vencer um torneio competitivo, bater o meta local,
  jogar um tema, aprender o formato, respeitar um orçamento.)
- Qual é o formato e qual é o campo esperado?
- "Melhor deck" segundo qual critério? O termo muda de sentido conforme o objetivo.

Se o pedido não deixar o objetivo claro, perguntar ao usuário é o atalho correto.
Na dúvida entre duas cartas, volte à pergunta: qual delas serve melhor ao que o
deck está tentando fazer?

**Exemplo.** "Devo incluir mais remoção ou mais ameaças?" não tem resposta em
abstrato. Se o objetivo é sobreviver a um campo agressivo, a pergunta se resolve de
um jeito; se é pressionar decks de controle, de outro.

## Atalho complementar: foco no que é útil

**O que é.** Concentrar esforço apenas no que muda o resultado. Horas focadas de
construção rendem mais que o dobro de horas dispersas, e existe "progresso
negativo": trabalho que afasta do objetivo.

**Quando se aplica.** Ao decidir onde gastar o tempo de análise e de teste.

**Como usar na construção.**

- Gaste mais análise nas decisões de maior impacto (plano de jogo, base de mana,
  confrontos contra os decks mais jogados) e menos em detalhes cosméticos.
- Um erro já cometido na lista não se discute; corrige-se e segue-se com o que
  importa agora.
- Estude o que venceu: a primeira pergunta ao analisar um torneio é quem ganhou e
  com qual lista, porque o histórico do que funcionou orienta o que tende a funcionar.

## Avaliar uma lista considerando a fonte

**O que é.** Ao examinar uma decklist pronta, leve em conta quem a construiu e que
resultados ela obteve.

**Quando se aplica.** Ao usar listas de sites de metagame, artigos ou resultados de
torneios como ponto de partida (netdecking).

**Como usar na construção.**

- Se a lista vem de um construtor com histórico consistente de resultados, presuma
  que escolhas estranhas têm razão de ser; investigue a razão antes de "corrigir".
- Se a origem é desconhecida, é mais provável que uma escolha aparentemente
  subótima seja de fato subótima.
- Não exagere em nenhuma direção: listas excelentes surgem de lugares improváveis,
  e todo mundo tem algo a ensinar. Histórico altera probabilidade, não prova nada.
- Cuidado com o viés do piloto: uma lista pode ter ido bem porque foi jogada por
  alguém muito forte.
- Copiar uma lista não encerra o trabalho. Ainda é preciso responder: qual das
  listas disponíveis é a melhor para este campo? Como atualizá-la para as mudanças
  das últimas semanas? Sem fundamentos, netdecking não basta.

Perguntas a fazer: quem construiu? Venceu o quê, quando e contra qual campo? O que
mudou no metagame desde então? Para cada escolha incomum: que problema ela resolve?

## Templating: construir a partir de precedentes

**O que é.** O número de arquétipos básicos em Magic é pequeno. *Templating* é
tomar um deck bem-sucedido de um arquétipo como molde e reconstruí-lo com as cartas
legais no formato atual, em vez de partir do zero.

**Quando se aplica.** Ao construir um deck novo, sobretudo em formato recém-rotacionado
ou quando não há listas estabelecidas para a ideia.

**Como usar na construção.**

1. Identifique o arquétipo da ideia (aggro de uma cor, controle, combo, midrange,
   híbridos).
2. Busque listas vencedoras desse arquétipo — do formato atual, de formatos vizinhos
   e do passado.
3. Extraia do molde a **estrutura**, não as cartas: número de terrenos e proporção
   de cores, formato da curva de mana, quantidade de ameaças, de remoção e de
   vantagem de cartas, composição do sideboard.
4. Preencha cada espaço com o melhor equivalente legal.
5. Para ideias que fundem duas estratégias, procure decks que já fizeram essa fusão
   com sucesso e veja como resolveram a mana e a contagem de espaços.
6. Anote o que os moldes **nunca** fazem: uma ausência repetida em todas as listas
   vencedoras de um arquétipo é informação tão forte quanto uma presença.

O que vale tomar emprestado: bases de mana de decks parecidos, curvas, proporções
de cores, ideias de sideboard.

**Exemplo histórico.** Quem monta um deck vermelho agressivo de dano direto aprende,
estudando as versões vencedoras de várias épocas, que remoção pontual que não causa
dano ao jogador quase nunca aparece nelas: cada espaço serve ao plano de reduzir a
vida do oponente.

## Atalhos preparados antes do jogo que afetam a lista

**O que é.** Decisões que bons jogadores tomam antes do torneio para não precisar
improvisar. Várias delas são, na prática, decisões de construção.

**Quando se aplica.** Ao fechar as 75 cartas e ao escrever o guia que acompanha o deck.

**Como usar na construção.**

- **Plano de sideboard pronto.** Para cada estratégia comum do campo, defina o que
  entra e o que sai antes de fechar a lista. Uma carta de sideboard sem um plano
  claro de troca é candidata a corte.
- **Jogar ou comprar primeiro.** Saiba a preferência padrão do deck no formato.
- **Alvo prioritário contra combos populares.** Saiba qual peça do combo adversário
  as respostas do deck devem atingir; isso orienta quais respostas incluir.
- **Vulnerabilidade da base de mana.** Fontes de mana mais frágeis a disrupção são
  recursos menos confiáveis; considere isso ao escolher terrenos e ao ordenar o uso.
- **Ordem de preferência em Limited.** Ter uma ordem geral de picks memorizada.

Ao entregar um deck, o agente deve incluir esses atalhos como orientação de uso
(plano de sideboard por confronto, preferência de jogar/comprar, alvos prioritários).

## Escolha de deck: honestidade e ousadia

**O que é.** Derrotas costumam ser atribuídas a falta de mana, a topdecks do
oponente ou a confrontos ruins. Esses fatores existem, mas a escolha do deck é uma
variável sob controle que pode reduzi-los: um deck diferente pode ter menos
confrontos ruins e pode vencer mesmo com compras medianas.

**Quando se aplica.** Ao escolher o deck para um evento e ao revisar resultados.

**Como usar na construção.**

- Ao analisar um resultado ruim, pergunte primeiro o que a lista ou a escolha do
  deck poderiam ter feito de diferente, antes de culpar a variância.
- Verifique se a escolha não foi conservadora demais: a opção "segura" que garante
  um resultado mediano pode ter teto baixo. Um deck visto como arriscado pode ser a
  melhor escolha se o campo não estiver preparado.
- Pergunte: este deck consegue vencer partidas em que tropeça na mana? Tem cartas
  que viram o jogo sozinhas?

**Exemplo histórico.** Um jogador profissional, depois de um resultado apenas
razoável com uma escolha conservadora, concluiu que o problema era a falta de
ousadia na seleção do deck; no Pro Tour seguinte optou por um combo considerado
arriscado e venceu o torneio.

## Encaixe na curva: julgar a carta pela sequência real

**O que é.** Uma carta deve ser avaliada pelo que faz dentro das aberturas típicas
do deck, não pelo valor isolado.

**Quando se aplica.** Ao escolher entre cartas de mesmo custo e ao definir
redundância para peças-chave.

**Como usar na construção.** Simule a abertura ideal e a abertura sem a peça-chave.
A carta escolhida precisa ser aceitável nas duas. Peças das quais o plano depende
merecem cópias funcionais extras. O detalhamento está na perspectiva Front-Back, em
[metodo-quatro-perspectivas.md](metodo-quatro-perspectivas.md).

## Draft (resumo)

**O que é.** Em draft há dois atalhos simples e incompletos: escolher sempre a carta
mais forte ou escolher sempre a que encaixa no arquétipo. O atalho bom combina os
dois: pesar o poder intrínseco da carta contra o valor de sinergia no deck que está
sendo montado.

**Quando se aplica.** Em pedidos de estratégia de draft e de avaliação de picks.

**Como usar.**

- Ordens de pick publicadas são ponto de partida, não a única ferramenta.
- Para cada arquétipo do formato, liste quais cartas ganham e quais perdem valor
  nele; isso permite decidir em segundos.
- Descubra antes como são os melhores decks do formato (número de criaturas, curva,
  tipos de mágica). Com o alvo definido, cada pick é só a coleta de peças de um
  deck já conhecido.
- Em drafts de treino, entre uma comum razoável e uma rara desconhecida que não
  seja obviamente forte, pegue a rara: a informação obtida vale o risco, e raras
  obscuras costumam ser subestimadas pela mesa.
- Se a análise mostrar que uma cor ou arquétipo é muito superior, comprometer-se
  cedo com ele pode render mais do que dividir os picks.

**Exemplo histórico.** Em um formato de draft dos anos 1990 em que uma cor era
claramente a mais forte, equipes preparadas forçaram essa cor a ponto de preferir
cartas medianas dela a cartas excelentes de outras, empurrando os vizinhos para
outras cores e recebendo mais da cor desejada nas voltas seguintes.

## Referências

*Next Level Magic* (Chapin, 2015):

- Gargalo de informação e atalhos como gatilhos — Seção 1, "Shortcuts", p. 14–19.
- Atalhos preparados antes do jogo — Seção 1, p. 18–19.
- Escolha de deck, honestidade sobre derrotas — Seção 1, "Shortcuts in the Mental
  Game", p. 22–23.
- Avaliar a lista pela fonte; templating — Seção 1, "Shortcuts in Deckbuilding",
  p. 26–28.
- Draft (resumo) — Seção 1, "Shortcuts in Draft", p. 29–30; "The Impact of Building
  a Magic Team on Draft", p. 46–47.
- "O que estou tentando realizar?" e foco no útil — Seção 1, "Picking the Right
  Shortcut at the Right Time", p. 31–34; p. 35–37 e 41–42.
- Encaixe na curva — Seção 2, "The Four Perspectives", p. 56–57.
