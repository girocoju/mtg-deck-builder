# Método das quatro perspectivas (e o conceito de trump)

Este documento descreve um método de análise em quatro ângulos — Top-Down, Bottom-Up,
Back-Front e Front-Back — e o conceito de *trump* (a carta ou combinação que decide a
partida). O agente deve consultá-lo sempre que for **construir um deck do zero**,
**ajustar uma lista existente** ou **explicar por que uma carta entra ou sai**. Ele
funciona como roteiro: cada perspectiva gera um tipo diferente de pergunta, e usar as
quatro em sequência evita as falhas típicas de quem olha o deck por um ângulo só.

## Visão geral: quatro ângulos, um objetivo

**O que é.** Quatro modos de olhar para o mesmo problema:

| Perspectiva | Pergunta central | Papel na construção |
|---|---|---|
| Top-Down | O que existe e é forte? | Levantar o que é poderoso e montar o núcleo do deck |
| Bottom-Up | O que falta, o que não funciona? | Cortar os elos fracos e ler as ausências do ambiente |
| Back-Front | Como a vitória acontece, de trás para a frente? | Planejar: da posição vencedora até o turno 1 |
| Front-Back | Como o jogo se desenrola do turno 1 em diante? | Aplicar e testar: curva, mãos iniciais, bateria de testes |

**Quando se aplica.** Em qualquer análise: avaliar uma coleção nova, montar uma lista,
revisar um deck depois de jogar, comparar opções de sideboard. Observações de ângulo
único ("perdi por falta de mana", "é só pegar remoção e bombas") mostram um pedaço do
quadro; cruzar os ângulos multiplica a informação aproveitada.

**Como usar na construção.**

1. Defina o objetivo antes de tudo (formato, tipo de evento, o que o deck precisa
   vencer). As perspectivas servem para chegar ao objetivo, não para escolhê-lo.
2. Siga a ordem natural: Top-Down → Bottom-Up → Back-Front → Front-Back.
3. Não existe pergunta "oficial" para cada perspectiva; colocar-se no ângulo já
   produz as perguntas. Invista em formular boas perguntas antes de buscar respostas.
4. Depois do Front-Back (teste), volte ao início com o que aprendeu. O ciclo é
   iterativo.

## Trumps: cartas que decidem a partida

**O que é.** Um *trump* é uma carta ou combinação que, resolvida no contexto certo,
praticamente vence sozinha contra determinadas estratégias. É mais preciso que "bomba":
o que importa não é a força bruta da carta, e sim o fato de o oponente não conseguir
superar aquele elemento do jogo. Conceitos vizinhos:

- **Hard lock:** o oponente não tem como vencer com o que tem no deck. Não importa
  se existe uma resposta em algum lugar do formato; importa se *aquele oponente* a tem.
- **Soft lock:** o oponente provavelmente não vence; tem saídas, mas perde se não
  as encontrar a tempo.
- **Trump:** coloca você em um estágio de jogo acima do oponente no começo da
  partida, ou supera a estratégia inteira dele mais tarde.

**Quando se aplica.** Ao escolher o núcleo de um deck e ao avaliar confrontos. Três
propriedades precisam ser lembradas:

- **Trump depende de contexto.** A mesma carta pode dominar no turno 2 e ser
  irrelevante no turno 10, ou o contrário. Avalie carta + turno + oponente.
- **Trumps têm hierarquia.** Quando os dois lados jogam um trump, um costuma passar
  por cima do outro. Pergunte qual trump vence no confronto direto.
- **Trump não precisa ser caro.** Cartas baratas que entregam mais do que custam
  podem dominar o primeiro estágio do jogo por pura eficiência.

**Estágios do jogo.** O livro trabalha com três estágios (desenvolvimento inicial,
meio de jogo, fim de jogo) e observa que cada jogador está no *seu* estágio: você
pode estar no meio de jogo enquanto o oponente ainda está travado no início. Quem
opera um estágio acima tem vantagem enorme — é por isso que ficar sem mana é tão
grave. Duas rotas para explorar isso: **subir de estágio mais rápido** (aceleração,
motores de mana) ou **prender o oponente em um estágio inferior** (negação de recursos).

**Como usar na construção.**

- Regra prática para reconhecer um candidato a trump: a carta gera cerca de uma
  carta de vantagem por turno, ou cria uma posição da qual o oponente raramente se
  recupera.
- Para cada deck relevante do campo, responda: qual é o meu trump contra ele, em que
  estágio ele entra, e qual é o trump dele contra mim?
- Verifique se o trump do oponente passa por cima do seu; se passar, você precisa de
  resposta, de velocidade ou de um trump maior.
- Nem todo deck gira em torno de trumps; estratégias de sinergia vencem pela soma
  das partes (ver Top-Down, abaixo).

**Exemplo histórico.** No Standard de 2014, Blood Baron of Vizkopa era um fim de jogo
forte, mas Elspeth, Sun's Champion passava por cima dele: destruía a criatura e
assumia a mesa. Em formatos com terrenos especiais que geram muita mana, Blood Moon
segura o oponente no estágio inicial enquanto você avança.

## Top-Down: partir do que é forte

**O que é.** Olhar para o que existe. Levantar tudo o que é poderoso, eficiente ou
que funciona no ambiente e construir de cima (as melhores cartas) para baixo (o
suporte que as acompanha). É mais do que "ver o quadro geral": é também um
brainstorm amplo de detalhes, ainda sem organização.

**Quando se aplica.** No início de qualquer projeto de deck e na leitura de um
formato novo ou de uma coleção recém-lançada.

**Como usar na construção.** Há dois pontos de partida típicos:

- **Poder bruto.** Liste as cartas que entregam mais do que custam e monte o deck
  em torno do melhor conjunto delas, completando com o suporte mais lógico
  (remoção eficiente, base de mana que as sustente).
- **Sinergia linear.** Algumas cartas são medianas isoladas e escalam conforme o
  deck se dedica a um tema (um tipo de criatura, artefatos, cemitério). Ao
  encontrar uma carta-recompensa assim, teste até onde o tema pode ser levado,
  inclusive com o deck inteiro dedicado a ele.

Perguntas a fazer:

- O que já sei que é forte/eficiente/funcional neste formato?
- Qual é o melhor motor de vantagem de cartas? A melhor remoção barata? A melhor
  base de mana disponível e o que ela permite jogar?
- Qual é o "melhor time" de cartas que consigo imaginar para este plano?

**Limite da perspectiva.** O quadro geral responde por volta de 80% do caminho, e os
20% restantes separam uma lista boa de uma lista vencedora. Saber qual é o núcleo
forte de um arquétipo não basta: os detalhes (quais finalizadores, quais respostas,
quais cartas da coleção mais recente) decidem o resultado.

**Exemplo histórico.** No Pro Tour Kyoto 2009, dezenas de jogadores usaram a mesma
base de mana de cinco cores e os mesmos motores de card advantage. A lista campeã se
diferenciou nas escolhas finas: finalizador, defesa inicial, contramágicas e adoção
de cartas da coleção nova que outros ignoraram.

## Bottom-Up: cortar os elos fracos e ler o que não está lá

**O que é.** Olhar para o que *não* existe ou *não* funciona. Tem três usos:
(1) identificar as cartas da lista que não rendem; (2) notar os efeitos ausentes em
um formato e deduzir as consequências; (3) reconhecer cartas do ambiente que tornam
certo tipo de deck inviável.

**Quando se aplica.** Logo depois do Top-Down, a cada rodada de ajuste da lista e
sempre que o metagame mudar.

**Como usar na construção.**

*Cortes na lista.* Uma carta que não gera vantagem não é neutra: ela ocupou um
espaço e consumiu mana. Depois de cada sessão, pergunte quais cartas se destacaram
e quais ficaram na mão ou não fizeram diferença. Candidatas a corte:

- custam demais para o que fazem;
- são difíceis de conjurar com a base de mana;
- não contribuem para o que o deck realmente tenta fazer;
- são respostas que falham justamente contra as ameaças que importam.

Prefira a carta que **sempre cumpre a função necessária** a uma carta em tese mais
forte que só cobre parte dos casos. Desconfie de cartas de estimação: gostar de uma
carta não é argumento; ao mesmo tempo, não descarte uma convicção só porque alguém
discordou. O critério é o desempenho.

*Ausências do formato.* Mantenha um checklist de categorias e registre, para cada
uma, o que existe e o que falta (o checklist completo está em
[preparacao-e-metagame.md](preparacao-e-metagame.md)). Uma ausência pode liberar
estratégias inteiras: sem contramágica eficiente, feitiços caros passam a ser
viáveis; sem descarte barato, segurar cartas na mão fica seguro.

*Cartas que eliminam arquétipos.* Antes de investir tempo em um deck, verifique se
há no campo uma carta amplamente adotada que o invalida. E pense nos efeitos em
cadeia: se uma resposta expulsa certas ameaças do formato, (a) os decks que sofriam
contra essas ameaças melhoram, e (b) a própria resposta perde alvos e pode ser
cortada — o que, mais adiante, reabre espaço para as ameaças voltarem.

**Exemplo histórico.** A adoção em massa de Path to Exile tirou de circulação
criaturas caras e resistentes que antes dominavam o Standard. Uma equipe chegou a
cortar a remoção da própria lista por prever que os alvos teriam sumido. Com decks
de cemitério vale a mesma leitura: contra Rest in Peace ou Leyline of the Void eles
quase não jogam, então a decisão de usá-los depende de quantas cópias dessas cartas
o campo traz e se estão no deck principal ou no sideboard.

## Back-Front: engenharia reversa da vitória

**O que é.** Planejamento estratégico de trás para a frente. Parte-se da posição
final (o jogo ganho) e pergunta-se, passo a passo, qual era a situação
imediatamente anterior, até chegar ao turno 1.

**Quando se aplica.** Ao definir o plano de jogo de um deck, ao decidir quantas
condições de vitória incluir e ao analisar partidas (suas ou de outros) para
descobrir o que realmente as decidiu.

**Como usar na construção.**

- **Procure as vantagens, não o golpe final.** A carta que causa o último dano
  raramente é a que venceu. Volte turno a turno e localize as jogadas que mudaram o
  tempo ou a card advantage; essas são as cartas que o deck precisa garantir.
- **Poucas condições de vitória bastam.** Mesmo decks de controle precisam de alguma
  forma de vencer, mas o erro comum é incluir finalizadores demais. A vitória vem
  depois de acumulada vantagem suficiente; nesse ponto, até um finalizador lento
  resolve.
- **Pense em pacotes, não em cartas isoladas.** Uma carta dominante depende das
  cartas de suporte que a deixam chegar viva ao momento em que domina. Identifique
  o conjunto que forma um plano fechado.
- **Seja realista.** Ao imaginar a jogada vencedora, pergunte qual precisa ser o
  estado da mesa para ela funcionar e o que o oponente teria feito nos turnos
  anteriores. Muitos decks fracos nascem de quem só imagina o melhor cenário.

Perguntas a fazer: como este deck vence, concretamente? O que precisa ter acontecido
um turno antes? E dois antes? Quais cartas constroem essa posição e quantas cópias
garantem que ela aconteça com frequência?

**Exemplo histórico.** Uma remoção em massa barata como Anger of the Gods não mata
ninguém, mas anula vários turnos de investimento de um deck de criaturas; depois
disso, qualquer ameaça lenta fecha o jogo. Da mesma forma, Sphinx's Revelation
definiu o controle do Standard de 2012–2014 apenas porque havia remoção em massa e
respostas flexíveis que sustentavam o jogo até ela.

## Front-Back: simular do turno 1 e aprender com o feedback

**O que é.** A perspectiva da aplicação: imaginar (e depois jogar de fato) a mão
inicial e o desenrolar turno a turno. É onde as hipóteses das três perspectivas
anteriores são testadas e onde o aprendizado acontece.

**Quando se aplica.** Ao definir a curva e as jogadas de cada turno, ao escolher
entre cartas concorrentes para o mesmo espaço e durante toda a fase de testes.

**Como usar na construção.**

- Pergunte em ordem: que mão inicial quero ver? O que quero fazer no turno 1? No
  turno 2? No 3?
- Para cada jogada-chave, pergunte: **e se ela não acontecer?** (a peça morreu ou
  não veio). O deck precisa de plano reserva e de redundância para as peças das
  quais depende.
- Escolha cartas pela forma como **se encaixam na sequência real do deck**, não
  pelo valor isolado. Uma carta boa "na curva" pode ser ruim se a sua abertura
  ideal pula justamente aquele ponto da curva; prefira cartas que rendem tanto no
  turno planejado quanto mais tarde.
- Teste a hipótese contra uma bateria (gauntlet) dos decks esperados e meça o quão
  realista é chegar do início à posição desejada no formato como ele é de fato
  jogado. O procedimento de bateria está em
  [preparacao-e-metagame.md](preparacao-e-metagame.md).
- Ao terminar, registre o que rendeu e o que não rendeu e reinicie o ciclo.

**Exemplo histórico.** Um deck que abria com Noble Hierarch no turno 1 queria
jogar uma carta de custo 3 no turno 2. Por isso seus espaços de custo 2 foram
ocupados por criaturas de utilidade como Tidehollow Sculler — boas no turno 2 se a
aceleração falhasse e ainda úteis no turno 3 ao lado de outra mágica — em vez de
criaturas agressivas de custo 2, que perdiam valor nas melhores aberturas.

## Roteiro resumido para o agente

1. **Objetivo:** formato, campo esperado, o que o deck precisa vencer.
2. **Top-Down:** listar o que é forte; escolher núcleo (poder bruto ou sinergia
   linear) e seus trumps por estágio.
3. **Bottom-Up:** cortar cartas caras, inconsistentes ou fora do plano; checar
   ausências do formato e cartas do campo que invalidam o deck.
4. **Back-Front:** descrever a posição vencedora e retroceder; confirmar que a
   lista tem as cartas que constroem a vantagem, sem excesso de finalizadores.
5. **Front-Back:** simular mãos e turnos; garantir plano reserva; testar contra a
   bateria; anotar o feedback e repetir.

## Referências

*Next Level Magic* (Chapin, 2015):

- Visão geral das quatro perspectivas — Seção 2, "The Four Perspectives", p. 51–57.
- Trumps, hard lock/soft lock e estágios do jogo — Seção 2, "Top-Down Perspective
  on Trumps", p. 58–62.
- Top-Down (poder bruto, sinergia linear, limite dos 80%) — Seção 2, p. 62–68.
- Bottom-Up (elos fracos, ausências, cartas que eliminam arquétipos) — Seção 2,
  p. 52–54 e "Bottom-Up Thinking (Removing the Weakest Links)", p. 69–75.
- Back-Front — Seção 2, p. 55 e "Reverse Engineering Victory", p. 76–78.
- Front-Back — Seção 2, p. 56–57 e "Learning from Feedback", p. 79–83.
