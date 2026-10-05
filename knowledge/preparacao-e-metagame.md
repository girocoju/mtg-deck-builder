# Preparação para um formato e leitura de metagame

Este documento descreve como estudar um formato, montar a bateria de testes
(gauntlet), ler o metagame e decidir como posicionar um deck contra o campo —
incluindo quando ficar com o "melhor deck" e quando ir de anti-meta. O agente deve
consultá-lo em pedidos do tipo "crie um deck anti-meta", "qual deck jogar neste
formato", "como ajustar esta lista para o meta atual" e sempre que for avaliar uma
coleção nova. Lembrete da constituição do projeto: dado de metagame tem fonte e
data; sem snapshot recente, a análise é teórica e isso deve ser dito ao usuário.

## Ponto de partida: o que se quer do deck

**O que é.** A preparação começa por definir o objetivo. "O melhor deck" significa
coisas diferentes para quem quer vencer um torneio grande, bater o meta de uma loja
ou jogar um formato casual.

**Quando se aplica.** Antes de qualquer pesquisa de listas.

**Como usar na construção.** Fixe formato, tipo de evento, nível do campo e
restrições do usuário. O gargalo é sempre o mesmo: opções demais para tempo de
menos. Ninguém encontra o melhor deck testando todas as combinações; chega-se a ele
por atalhos — estudar o que venceu, somar esforço com outras pessoas e testar só o
que importa. (Ver [atalhos-de-construcao.md](atalhos-de-construcao.md).)

## Mapear o formato: checklist de presenças e ausências

**O que é.** Um inventário, por categoria, do que o formato oferece e do que ele
não oferece. As ausências informam tanto quanto as presenças.

**Quando se aplica.** A cada coleção nova, rotação ou primeiro contato com um formato.

**Como usar na construção.** Percorra a lista abaixo consultando a base de cartas
e o snapshot de metagame. Para cada item, anote as melhores opções **e** se a
categoria está vazia ou fraca.

- Criaturas dominantes.
- Remoção barata; remoção em massa.
- Manipulação de biblioteca e tutores.
- Fontes de card advantage.
- Aceleração de mana.
- Contramágicas.
- Uso do cemitério.
- Artefatos, encantamentos e planeswalkers dominantes.
- Feitiços poderosos.
- Condições de vitória mais fortes.
- Combos poderosos.
- Destruição de terrenos (e se é preciso conseguir destruir algum terreno).
- Velocidade dos decks agressivos (em que turno costumam vencer).
- Descarte.
- Dano direto.
- Cartas que mudam as regras do jogo de formas novas.
- A pior coisa que pode acontecer a um deck sem remoção.

Regras práticas:

- Mantenha a lista por escrito e acrescente categorias conforme surgirem, para não
  recomeçar do zero a cada coleção.
- Compare com formatos anteriores parecidos: se o ambiente é semelhante a um já
  conhecido, exceto por um efeito ausente, siga a cadeia de consequências. Decks
  antes inviáveis podem passar a funcionar.
- A composição do formato muda o valor relativo das cores e das respostas: uma
  resposta só vale o que valem os alvos que existem para ela.

**Exemplo histórico.** Em um bloco com pouquíssimos artefatos relevantes, e em que
os poucos existentes também eram encantamentos, a remoção de artefatos de uma cor
ficou quase sem uso, enquanto as cores com remoção de encantamentos ganharam valor.
No mesmo ambiente, a presença de um descarte de um mana muito eficiente tornou
arriscado o plano de segurar cartas na mão para montar uma jogada.

## Estudar o que venceu

**O que é.** O histórico de resultados é a matéria-prima da preparação. Jogadores
de alto nível começam a análise de qualquer torneio perguntando quem venceu e com
qual lista; saber quem pilotou ajuda a entender o que foi necessário para vencer.

**Quando se aplica.** Ao levantar os decks do campo e ao procurar moldes para um
deck novo.

**Como usar na construção.**

- Colete os resultados recentes de eventos grandes do formato e identifique os
  decks mais jogados e os mais bem colocados.
- Em cada arquétipo, compare as listas bem-sucedidas com as medianas: as diferenças
  finas (finalizador, mistura de respostas, cartas da coleção mais nova) costumam
  ser o que separa os resultados.
- Avalie cada carta e cada deck novo pelo que ele é, não pelo que a expectativa
  dizia. Cartas muito anunciadas geram dois erros simétricos: superestimar por
  comparação com um clássico e depois descartar porque "não é o clássico". Uma
  carta pode não ser a segunda vinda de uma carta antiga e ainda assim definir o
  formato.
- O erro inverso é igualmente comum: muitas cartas que depois definiram formatos
  foram desprezadas no lançamento. "Ninguém joga isso" não é argumento; alguém
  precisa testar primeiro.

## Leitura de formato: mana ruim e remoção dominante

**O que é.** Duas perguntas que, respondidas cedo, orientam todos os decks de um
formato: quão boa é a mana disponível e qual é a interação ou remoção que define o
ambiente.

**Quando se aplica.** Logo depois do checklist de presenças e ausências, antes de
escolher cores e ameaças.

**Como usar na construção.**

- **Terrenos multicoloridos fracos ou que entram virados.** O custo de jogar várias
  cores sobe. Há três saídas: (a) ficar em uma cor só, trocando alcance por uma base
  estável; (b) apoiar-se em terrenos que consertam exatamente as cores do deck; (c)
  se a opção for por três cores, compensar o turno perdido com mágicas de custo 1
  muito fortes, que usam bem o mana que sobra nos turnos de terreno virado, e com
  seleção barata de cartas, que ajuda a achar as cores.
- **Em formato de terrenos virados, a qualidade do que se joga por um mana pesa
  mais.** Os melhores drops de 1 do formato são ponto de partida para os decks
  agressivos e também para os lentos.
- **Identifique a remoção ou interação dominante e escolha ameaças que escapam
  dela.** Se o formato gira em torno de uma remoção recorrente de dano baixo, valem
  criaturas de resistência alta, criaturas baratas que crescem além do alcance dela
  e bônus globais que tiram o time inteiro da faixa de dano.
- A mesma leitura serve a decks diferentes: uma equipe pode chegar a listas
  distintas partindo das mesmas duas conclusões sobre o formato.

(Os números de fontes por cor estão em [base-de-mana.md](base-de-mana.md).)

**Exemplo histórico.** No Extended de 2010, um grupo de teste concluiu que uma
interação recorrente de dois de dano definia o formato e que a mana era ruim. Dali
saíram três decks bem-sucedidos no mesmo torneio: um agressivo de uma cor só, com
drops de 1 que cresciam e um bônus global; um de criaturas de resistência alta,
apoiado em um terreno que consertava suas três cores; e um controle de três cores
sustentado por remoção e seleção de custo 1.

## Gauntlet: a bateria de testes

**O que é.** Um conjunto representativo dos decks importantes do campo, contra o
qual toda ideia nova é testada.

**Quando se aplica.** Na preparação para qualquer evento e sempre que o agente
precisar justificar que um deck é competitivo.

**Como usar na construção.**

1. **Monte a bateria** com pelo menos os quatro ou cinco decks mais prováveis de
   aparecer, a partir de resultados recentes.
2. **Garanta variedade:** ao menos um representante de cada grande estilo de deck.
   Testar contra cinco variações do mesmo deck agressivo rende menos do que testar
   contra decks diferentes entre si em aspectos importantes. Exceção: um deck
   muito popular entra de qualquer forma.
3. **Use as listas que os oponentes realmente vão jogar**, não versões idealizadas.
4. **Teste em ordem de filtro.** Eleja o deck mais popular como primeiro teste. Se
   a ideia nova não consegue números ao menos respeitáveis contra ele, pare e
   conserte antes de gastar tempo com o restante. Só depois avance pelos demais.
5. **Não teste ideia nova contra ideia nova.** Saber que uma lista experimental
   vence outra lista experimental que ninguém vai jogar não informa nada. O tempo de
   teste é escasso; gaste-o contra o que se espera enfrentar.
6. **Papéis no teste:** um lado pilota o deck estabelecido, o outro o experimento.
   Os dois precisam jogar a sério para o resultado valer.
7. Proxies (cartas substitutas marcadas) são legítimos no teste: não há motivo para
   deixar de treinar contra as melhores cartas por não possuí-las.
8. **Teste de fato o que foi listado.** Saber que uma interação "existe" não é
   o mesmo que jogá-la. Grupos organizados dividem a fila de ideias para chegar
   até as últimas; às vezes é uma delas que define o formato.
9. **Divergência se resolve com série combinada.** Quando alguém ajustou uma lista
   para um confronto dado como perdido e o resto do grupo não acredita, combine
   antes o tamanho da série e a consequência do resultado, e ponha o mais cético
   pilotando o outro lado.
10. **Lista afinada vale mais que invenção da véspera.** Um deck testado contra
    toda a bateria e ajustado por semanas supera, em média, uma ideia nova montada
    na última noite, mesmo vinda das mesmas pessoas.

Para o agente, que não joga partidas: aplique o mesmo raciocínio como análise de
confronto. Para cada deck da bateria, descreva o plano dele, os trumps de cada
lado e o que a lista proposta faz nos primeiros turnos contra ele; aponte os
confrontos em que a lista não tem plano.

**Exemplo histórico.** Uma equipe em preparação para um Pro Tour de 2009 adotou a
regra de que todo deck novo enfrentava primeiro o deck mais popular do formato. A
maioria das ideias caía ali, o que poupou muito tempo de teste. Em 2014, o filtro
equivalente no Standard era um trio de decks dominantes; só depois vinham os decks
agressivos de segunda linha.

## Melhor deck ou deck anti-meta

**O que é.** A decisão entre jogar a estratégia dominante e jogar algo desenhado
para vencê-la.

**Quando se aplica.** Ao escolher o deck e em todo pedido de "deck anti-meta".

**Como usar na construção.**

- **Formato com um deck dominante.** Qualquer candidato precisa, no mínimo,
  competir de igual para igual com ele. Um deck que perde para o dominante só se
  justifica se esmagar todo o resto do campo — e mesmo assim é uma escolha de risco.
- **Formato dominado por um só deck e você decide jogá-lo.** A vantagem vem de ter
  a melhor *versão* para aquele torneio: escolhas incomuns voltadas ao espelho e
  aos predadores esperados.
- **Deck anti-meta.** Antes de se comprometer, confira: (a) vence de fato o deck
  mais jogado, e não só no papel; (b) não perde para os demais decks da bateria;
  (c) continua funcionando se o campo for mais variado do que o previsto.
- **Não invista em deck que não tem chance contra os melhores.** Verifique isso
  cedo, antes de semanas de ajuste fino.

## Popularidade, força e escolha de deck

**O que é.** Critérios para não confundir "o deck mais jogado" com "o melhor deck"
e para decidir entre copiar uma lista consagrada e levar algo próprio.

**Quando se aplica.** Ao interpretar um snapshot de metagame, ao recomendar um deck
para um evento específico e em pedidos de anti-meta.

**Como usar na construção.**

- **Taxa de conversão, não contagem.** Um deck muito jogado acumula bons
  resultados só por volume. Compare a fatia de resultados de topo com a fatia do
  campo: o deck menos popular que converte mais é o melhor sinal. Se o snapshot só
  traz contagem, diga isso ao usuário.
- **Mais fraco em abstrato, melhor para o campo.** Um deck de cartas inferiores
  pode ser a escolha certa se vence os decks que a maioria vai levar. A vantagem
  depende de a previsão do campo se confirmar.
- **Valor de surpresa existe e acaba.** Estratégias e cartas inesperadas ganham
  pontos enquanto os oponentes não sabem jogar contra elas; em poucas semanas isso
  some. Avalie o deck supondo um oponente informado.
- **"O deck certo para aquele dia".** Uma versão pode ser a melhor para um torneio
  e deixar de ser depois: a variante mais rápida de um combo vence o espelho e os
  decks sem interação, mas resiste menos ao ódio quando o formato se adapta.
  Registre para qual campo a lista foi afinada.
- **Copiar ou inovar.** Listas consagradas são, em média, melhores que ideias
  novas. Quem sempre copia fica sem vantagem sobre quem copiou igual; quem sempre
  inventa joga com listas piores do que pensa. Regra do livro: quem costuma copiar
  deve inovar mais, e quem costuma inventar deve imitar mais. Inove quando o
  resultado importa pouco e imite mais, sem ser às cegas, quando importa. Com
  listas públicas, a vantagem obtida só pelo deck é limitada.
- **Deck de plano fixo ou deck com espaço de decisão.** Um deck linear pode ter os
  melhores números contra o campo, mas deixa pouca margem para o piloto ganhar
  pontos jogando: resta não perder pontos por erro. Um deck com várias linhas
  possíveis e jogos mais longos tem números brutos um pouco piores e rende mais
  para quem joga melhor que o campo. Leve em conta quem vai pilotar.

O mecanismo pelo qual um deck mediano passa a ser visto como o melhor (imitação em
cadeia) e as defesas contra ele estão em
[jogo-mental-e-mentalidade.md](jogo-mental-e-mentalidade.md), seção 3.

**Exemplo histórico.** Em um Standard de meados dos anos 2000, entre duas variantes da mesma dupla
de cores, a mais chamativa era de longe a mais jogada e por isso somava mais vagas;
a menos popular classificava uma fração maior de seus pilotos toda semana.

## Pensar um nível à frente

**O que é.** O metagame funciona como um pedra-papel-tesoura entre cartas e decks,
e ele se move: cada resposta popular altera o que vale a pena jogar. Copiar as
listas vencedoras da semana anterior mantém o jogador sempre um passo atrás, porque
todos leem as mesmas fontes.

**Quando se aplica.** Ao ajustar uma lista ao campo esperado e ao definir remoção,
respostas e sideboard.

**Como usar na construção.** Siga a cadeia em três passos:

1. **Nível 0 — o que venceu.** Quais decks e cartas estão em alta?
2. **Nível 1 — a reação.** O que as pessoas vão adotar para vencê-los? Quais
   ameaças e arquétipos saem de cena por causa dessa reação?
3. **Nível 2 — a oportunidade.** Com essas ameaças fora, quais respostas ficam sem
   alvo (e podem ser cortadas)? Quais decks, antes contidos por essas ameaças,
   melhoram? Se uma resposta começar a sumir das listas, quais ameaças podem voltar?

Perguntas para cada espaço de resposta na lista:

- Quais alvos reais esta carta terá no campo previsto para *este* evento?
- A popularidade da própria carta já afastou os alvos dela?
- Qual é o tipo de ameaça que a maioria vai jogar, e existe uma carta que a
  neutraliza melhor do que a resposta padrão?

**Exemplo histórico.** Uma remoção branca de um mana tornou-se tão comum em um
Standard que as criaturas grandes contra as quais ela brilhava desapareceram; uma
equipe então a retirou da lista. Prevendo um campo de criaturas pequenas voadoras e
dano direto, a mesma equipe usou no deck principal uma criatura defensiva que ganha
vida, Wall of Reverence, no lugar da remoção em massa tradicional.

## Cartas de ódio e decks vulneráveis

**O que é.** Alguns arquétipos (o caso clássico é o de cemitério) são tão fortes
que atropelam oponentes despreparados e, ao mesmo tempo, perdem quase
automaticamente para certas cartas específicas de ódio.

**Quando se aplica.** Ao considerar um deck linear ou de combo com ponto fraco
conhecido, e ao decidir quanto ódio incluir no próprio sideboard.

**Como usar na construção.**

- A pergunta decisiva é **quantos oponentes trazem a carta de ódio, e onde**: deck
  principal ou sideboard.
- Se o ódio está só nos sideboards, o deck vulnerável tende a vencer o primeiro
  jogo; o sideboard dele deve então trazer respostas ao ódio suficientes para
  ganhar um dos dois jogos seguintes.
- Avalie a qualidade do ódio disponível: há cartas que entram em jogo antes de
  qualquer interação ou que deixam efeito mesmo se removidas; contra essas, as
  respostas comuns não bastam.
- Do outro lado: se um deck vulnerável cresce porque o campo relaxou no ódio, é
  hora de voltar a incluí-lo.

**Exemplo histórico.** Decks de dredge e de reanimação oscilam conforme a presença
de Rest in Peace e Leyline of the Void: a primeira exila o cemitério inteiro ao
entrar, a segunda pode começar a partida já em jogo. Quando o campo as esquece,
esses decks voltam a ser ótimas escolhas.

## Preparar-se em grupo

**O que é.** Os melhores resultados de construção vêm de grupos de teste, não de
indivíduos isolados: mais pessoas com o mesmo objetivo multiplicam o foco e cobrem
mais ideias.

**Quando se aplica.** Como contexto para avaliar listas de equipes e como
recomendação ao usuário.

**Como usar na construção.** Listas saídas de grupos de teste fortes merecem
confiança extra nos detalhes. Para o deck builder, o equivalente é combinar fontes:
base de cartas, teoria de `knowledge/`, dados de metagame e o retorno do usuário
sobre partidas reais (que vira lição registrada). A formação de equipes em si é
tratada adiante no livro e está fora deste documento.

## Checklist rápido de posicionamento

1. Objetivo e formato definidos; snapshot de metagame com data.
2. Checklist de presenças e ausências preenchido.
3. Bateria de 4–5 decks, variada, com as listas reais.
4. O candidato passa pelo deck mais popular? Se não, parar e corrigir.
5. Cada resposta da lista tem alvos reais no campo previsto.
6. Reação do campo antecipada (níveis 1 e 2).
7. Exposição a cartas de ódio avaliada, com plano para os jogos pós-sideboard.

## Referências

*Next Level Magic* (Chapin, 2015):

- Ponto de partida e gargalo de opções — Seção 1, "How to Prepare for a Format",
  p. 42–43.
- Estudar o que venceu — Seção 1, p. 35–37; Seção 2, p. 67–68 e 72–73.
- Preparar-se em grupo — Seção 1, p. 43–45.
- Checklist de presenças e ausências — Seção 2, "The Four Perspectives", p. 53–54.
- Pensar um nível à frente; cartas que eliminam arquétipos — Seção 2, "Bottom-Up
  Thinking", p. 69 e 71–74.
- Cartas de ódio e decks vulneráveis — Seção 2, p. 74–75.
- Gauntlet, ordem de teste, proxies, melhor deck vs. alternativa — Seção 2,
  "Learning from Feedback", p. 79–82; papéis no teste, Seção 1, p. 49.
- Cartas subestimadas no lançamento — Seção 2, "Applying the Perspectives to Build
  a Magic Team", p. 92.
- Leitura de formato: mana ruim e remoção dominante — Seção 2, "Applying the
  Perspectives to Build a Magic Team", p. 103–105.
- Gauntlet, itens 8 a 10 (testar o que foi listado, série combinada, véspera) —
  Seção 2, "Applying the Perspectives to Build a Magic Team", p. 100–103 e 106–108.
- Popularidade, força e escolha de deck — Seção 2, "Information Cascades in
  Magic", p. 151–152, 155–156 e 160–161; "deck certo para aquele dia", p. 99; deck
  de plano fixo ou com espaço de decisão, Seção 4, "How to Jedi", p. 279–280 e 291;
  listas públicas, Seção 4, "Building Rapport", p. 315.
