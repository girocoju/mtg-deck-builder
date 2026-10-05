# Sideboard: construir e usar as 15 cartas

Este documento explica como montar um sideboard e como trocar cartas entre os jogos de uma
partida melhor-de-três. O agente deve consultá-lo sempre que entregar uma lista de
construído com sideboard, quando o usuário pedir um plano de sideboard por matchup, quando
for avaliar se uma carta merece vaga nas 15 e quando for construir um deck anti-meta
(em que parte das respostas mora no sideboard e parte na lista principal).

Ideia central de Chapin: o deck tem 75 cartas, não 60. O sideboard é um recurso do jogo,
tão real quanto cartas na mão ou mana, e serve para **ajustar a estratégia** durante a
partida, não para guardar uma coleção de cartas de ódio famosas.

## 1. O sideboard serve ao plano do deck, não o contrário

**O que é.** O erro mais comum é encher as 15 vagas com as cartas "clássicas de sideboard"
do formato sem perguntar se aquele tipo de efeito é o que este deck precisa. Uma carta pode
ser excelente em abstrato e ainda assim ser a ferramenta errada para o seu plano.

**Quando se aplica.** Sempre que uma carta for candidata ao sideboard.

**Como usar na construção.**
- Comece de cima para baixo: o que o deck precisa conseguir em cada matchup importante?
  Só depois escolha a carta que faz isso.
- Compare alternativas pelo que o deck consegue aproveitar. Um deck com muita manipulação
  barata de biblioteca, que só precisa ganhar um ou dois turnos contra o cemitério, pode
  preferir um efeito pontual de custo zero a um efeito permanente e caro.
- Pergunta de corte: "esta é a maneira ideal de *este deck* resolver este problema?"

**Exemplo histórico.** Chapin critica quem começa todo sideboard com quatro
Leyline of the Void por reflexo: é das melhores cartas contra cemitério, mas há decks para
os quais Tormod's Crypt faz o serviço necessário por menos.

## 2. Contar as cartas mortas de cada matchup

**O que é.** Além de trazer cartas boas, o sideboard permite **tirar cartas inúteis**.
Remoção de criaturas contra um combo sem criaturas, efeitos de roubo de criatura contra
burn, punição a terrenos não básicos contra um deck monocolorido de básicos: tudo isso é
carta morta na mão.

**Quando se aplica.** Na montagem das 15 e na hora de cada troca.

**Como usar na construção.**
- Para cada matchup relevante, liste quantas cartas da lista principal ficam mortas ou
  fracas. Esse número define quantas vagas de sideboard o matchup "pede".
- Não é obrigatório ter substituta para cada carta morta, mas ter algumas vale pontos
  percentuais.
- Critério de desempate entre duas cartas parecidas: prefira a que também entra em
  matchups onde suas outras cartas morrem. Num deck cheio de remoção de criatura, uma
  remoção que também destrói artefatos tem valor extra porque continua útil quando as
  demais não são.

## 3. Entradas e saídas têm de fechar a conta

**O que é.** Não adianta ter dez cartas para entrar se só cinco podem sair. As vagas
excedentes foram desperdiçadas.

**Quando se aplica.** Na revisão final do sideboard, matchup por matchup.

**Como usar na construção.**
- Monte uma tabela por matchup: **entra / sai**. As duas colunas devem ter o mesmo tamanho.
- Se só dá para tirar cinco, escolha as cinco entradas mais eficazes e libere as outras
  vagas para outro matchup.
- Se o matchup é tão ruim que você realmente precisa de dez entradas, mexa na **lista
  principal**: troque cartas que são apenas razoáveis nesse matchup por cartas melhores em
  outros confrontos, já planejando tirá-las quando enfrentar o deck problemático. Assim o
  jogo 1 melhora contra o resto do campo e as dez trocas passam a caber.
- Quanto o deck aguenta trocar depende da sua estrutura: há decks em que tirar oito cartas
  desmonta o motor, e decks modulares que trocam quinze sem problema.

**Exemplo histórico.** Uma lista de controle levava duas remoções pretas baratas, em parte
por causa de um matchup em que, depois do sideboard, uma delas saía de qualquer jeito. A
segunda cópia foi trocada na lista principal por uma remoção mais útil contra os decks
agressivos do campo: perdeu-se pouco no jogo 1 daquele matchup e ganhou-se nos demais.

## 4. Ferramentas estreitas ou versáteis

**O que é.** Cartas de ódio estreitas e devastadoras são instrumentos de precisão. Cartas
flexíveis fazem menos em cada matchup, mas servem contra o que você não previu.

**Quando se aplica.** Ao decidir a composição geral das 15.

**Como usar na construção.**
- Metagame concentrado, com um alvo claro: use a ferramenta estreita que mais pune.
- Campo aberto ou desconhecido: reserve parte do sideboard a cartas versáteis, para ter
  opções contra decks inesperados.
- Contra decks agressivos, várias cartas modestas (ganho de vida com corpo, remoção
  barata) somam muito rápido; não é preciso uma bala de prata.
- Cartas estreitas de alto impacto têm retorno decrescente brutal: a segunda cópia
  costuma não fazer nada. Com pouco espaço, **uma cópia de cada uma de duas cartas**
  costuma valer mais do que duas da mesma (ver `quantidade-de-copias.md`). É por isso que
  sideboards de jogadores de elite têm tantas cópias únicas.

## 5. Preferir cartas com sinergia com o plano principal

**O que é.** A melhor carta de sideboard atrapalha o oponente **e** avança o seu plano.

**Quando se aplica.** Na escolha entre duas respostas para o mesmo problema.

**Como usar na construção.**
- Deck agressivo de criaturas: prefira o efeito de disrupção que vem num corpo que ataca.
  Você compra a ferramenta e continua batendo.
- Deck que controla a mesa com varreduras: não traga criaturas pequenas de disrupção que
  morrem para as suas próprias varreduras.
- Deck apoiado em planeswalkers: evite proteções que cuidam só do jogador e deixam os
  planeswalkers expostos.
- Pergunta: "depois da troca, minhas cartas ainda trabalham juntas?"

**Exemplo histórico.** Decks Zoo usavam criaturas de disrupção como
Thalia, Guardian of Thraben contra combo: o corpo mantinha a pressão. Chapin conta que
trouxe Ethersworn Canonist contra um combo de elfos num deck cuja interação principal eram
varreduras, e se arrependeu.

## 6. Manter o núcleo ou transformar

**O que é.** Trocar cartas demais dilui o deck até ele não fazer mais o que faz. A
alternativa deliberada é o sideboard transformacional, que muda o plano por inteiro.

**Quando se aplica.** Em todo plano de troca; é a regra mais importante do capítulo.

**Como usar na construção.**
- Se o plano principal é bom no matchup, **mantenha-o** e troque só o necessário.
- Se o plano principal não vence o matchup, não remende: vire o confronto de cabeça para
  baixo com um plano diferente e imprevisível.
- Decks de combo e de sinergia são os mais frágeis: onze cartas de resposta no lugar de
  peças do motor podem impedir o combo de funcionar.
- Use as trocas também para **ajustar a composição** sem mudar o plano: trocar as
  condições de vitória pelas melhores contra aquele oponente, ou os counters genéricos
  pelos certos para o que ele joga.

**Exemplo histórico.** Num controle de quatro cores de 2009, as criaturas da lista
principal eram as melhores para o jogo 1 (filtravam respostas erradas); o sideboard trazia
outras finalizadoras, cada uma para um grupo de matchups, mantendo sempre três ou quatro
criaturas no total. O mesmo valia para os counters: um pacote variado, com mais cópias do
counter de não-criaturas, porque era ele que substituía a remoção morta contra decks sem
criaturas.

## 7. Antecipar o sideboard do oponente

**O que é.** Você não joga os jogos 2 e 3 contra a lista do jogo 1, e sim contra a lista
dele depois das trocas.

**Como usar na construção.**
- Pergunte: "no lugar dele, o que eu traria contra mim?" Guarde respostas para isso.
- Cuidado com a emboscada clássica: o deck sem criaturas que traz criaturas depois que
  você tirou toda a sua remoção.
- Usar poucas cópias de uma ameaça de sideboard pode ser proposital: com duas criaturas
  grandes em vez de quatro, a remoção do oponente continua ruim; com quatro, ele mantém a
  remoção sem medo de ela ficar morta.
- Variar os nomes das ameaças e respostas protege contra efeitos que nomeiam uma carta e
  dificulta que o oponente jogue em volta.

## 8. Play ou draw

**O que é.** O plano de troca pode mudar conforme quem começa.

**Como usar na construção.** Ao escrever o guia de sideboard, anote variações: tirar um
terreno quando estiver no draw; trazer certas cartas de tempo apenas quando estiver no
play, onde elas rendem mais.

## 9. Processo: quando pensar no sideboard e como testar

**O que é.** Em um deck novo, primeiro verifique se a lista principal é viável; a maioria
das ideias morre no primeiro teste e não precisava de sideboard. Mas o sideboard nunca sai
totalmente da conversa: as cartas de ódio disponíveis no formato decidem se um conceito
sobrevive.

**Como usar na construção.**
- Ordem de trabalho: núcleo do deck → teste rápido → sideboard → muitos jogos pós-sideboard.
- Jogadores de torneio quase sempre testam poucos jogos com sideboard. O livro estima que
  o sideboard afeta cerca de 60% das partidas (números do livro, 2015).
- Decks muito lineares ou muito visados (os que todo mundo traz ódio contra) devem ser
  testados **principalmente** pós-sideboard, porque o jogo 1 deles é mecânico e pouco
  representativo.
- Use modelos: sideboards de listas vencedoras parecidas são ponto de partida legítimo,
  assim como bases de mana.
- Visualize a partida: o que há no matchup, o que falta, onde você quer chegar, como o
  oponente reage.

## 10. Informação durante a troca (resumo)

Pouco afeta a construção, mas vale registrar: não revele quantas cartas trocou (embaralhe
as 15 no deck e retire 15); finja trocar mesmo sem nada para trazer; observe quantas
cartas o oponente troca e com que segurança, pois quem troca rápido e decidido
provavelmente tem um plano ensaiado e a carta de ódio que você teme.

## Erros comuns (checklist de revisão)

- [ ] Cartas de ódio famosas incluídas sem um matchup e um papel definidos.
- [ ] Mais entradas do que saídas possíveis em algum matchup.
- [ ] Cartas mortas na lista principal sem substituta para o matchup em que morrem.
- [ ] Entradas que não combinam com o plano (criaturas pequenas num deck de varreduras).
- [ ] Trocas que desmontam o núcleo de um deck de combo ou sinergia.
- [ ] Remendos num matchup invencível, em vez de um plano transformacional.
- [ ] Plano ignorando o que o oponente traz contra você.
- [ ] Só ferramentas estreitas num campo aberto, ou só genéricas num campo concentrado.
- [ ] Nenhum jogo pós-sideboard testado.

## Atualização posterior ao livro: melhor-de-um (BO1)

**Atualização posterior ao livro.** Em filas melhor-de-um, comuns no MTG Arena, não há
troca de sideboard entre jogos. Consequências para a construção: a lista principal precisa
ser mais robusta, com menos cartas que morrem em matchups frequentes; respostas flexíveis
ganham valor sobre respostas estreitas; e cartas de ódio só entram na lista principal
quando o alvo é realmente comum. A contagem de cartas mortas por matchup (seção 2)
continua valendo, mas passa a orientar a lista principal, já que não há como corrigir
depois. O agente deve sempre perguntar ou inferir se o pedido é BO1 ou BO3 antes de montar
as 15.

## Referências

*Next Level Magic* (Chapin, 2015).

| Seção deste documento | Capítulo | Páginas |
|---|---|---|
| 1, 2, 4 | It Takes 75, Not 60... | 230-233 |
| 3 | It Takes 75, Not 60... | 233-234 |
| 5 | It Takes 75, Not 60... | 232-233 |
| 6 | It Takes 75, Not 60...; Knowing How Many of Each Card To Use (sideboard do estudo de caso) | 236-237, 256-259 |
| 7 | It Takes 75, Not 60...; Knowing How Many of Each Card To Use | 234, 257-258 |
| 8 | It Takes 75, Not 60... | 236 |
| 9 | It Takes 75, Not 60... | 236-238 |
| 10 | It Takes 75, Not 60... | 234-236 |
| BO1 | Atualização posterior ao livro (não consta na fonte) | — |
