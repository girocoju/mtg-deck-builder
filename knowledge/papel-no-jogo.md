# Papel no jogo: quem é o beatdown, quem é o controle

Este documento explica como identificar, em cada matchup, qual deck deve atacar e qual deve
segurar o jogo, e como essa leitura muda a construção, o sideboard e o plano de jogo. O
agente deve consultá-lo ao posicionar um deck contra um metagame, ao escrever planos por
matchup, ao construir decks midrange ou anti-meta (cujo papel muda de confronto para
confronto) e ao avaliar decks de combo.

A base é o artigo *Who's the Beatdown?*, de Michael Flores, que Chapin considera
provavelmente o texto mais importante já escrito sobre o jogo, resumido na máxima
"Misassignment of role = game loss".

## 1. Em todo jogo há um beatdown e um controle

**O que é.** O rótulo do arquétipo (aggro, controle, combo, midrange) não define o que o
deck deve fazer numa partida específica. Em qualquer confronto, cada jogador ocupa um de
dois papéis: **beatdown** (quer que o jogo acabe logo) ou **controle** (quer que o jogo
se alongue). Os dois jogadores sempre respondem a essa pergunta com suas jogadas, mesmo
sem perceber; quem responde errado perde jogos que podia ganhar.

**Quando se aplica.** Em todo matchup, e com mais força entre decks parecidos (aggro
contra aggro, controle contra controle), onde o papel não é óbvio.

**Como usar na construção.** Um deck não tem um papel; tem um papel **por matchup**. Ao
listar os principais decks do metagame, anote ao lado de cada um: "contra este, sou
beatdown" ou "contra este, sou controle". Essa anotação orienta o sideboard e a
explicação entregue ao usuário.

## 2. Mais rápido contra maior

**O que é.** O livro descreve o jogo em três estágios (definidos em capítulo anterior):
o Estágio Um, em que os jogadores ainda estão limitados pela mana; o Estágio Dois, o
meio do jogo, em que as mágicas saem normalmente; e o Estágio Três, em que um dos lados
executa o seu fim de jogo dominante.
- Um deck **rápido** explora o Estágio Um: quer vencer antes que o oponente se desenvolva.
- Um deck **grande** mira o Estágio Três: quer chegar a um fim de jogo que o oponente não
  supera.

Regra geral: no confronto, o deck **maior faz o papel de controle** e o **mais rápido faz
o de beatdown**, mesmo que o deck rápido não tenha nenhuma criatura.

**Quando se aplica.** É a primeira aproximação para qualquer matchup.

**Como usar na construção.**
- "Maior" significa o maior plano **viável**. Sempre dá para trocar uma defesa por mais
  uma finalizadora cara e ficar "maior" no papel, mas o deck precisa sobreviver até lá.
- Se o seu deck é ao mesmo tempo maior e mais rápido que o do oponente, a vantagem é
  enorme. Nesse caso, pergunte onde está a melhor chance **dele** (ir por cima ou ir por
  baixo) e prepare-se para ela.
- Regra de sobrevivência: se você perde o jogo longo, não deixe o jogo ser longo. Se não
  pode ser o maior num matchup, tem de ser o mais rápido, mesmo que o deck não tenha sido
  desenhado para isso.

**Exemplo histórico.** O controle clássico dos primórdios do jogo usava remoção e
counters baratos para sobreviver ao início, cartas de vantagem acumulada para dominar o
meio e só então, com o jogo trancado, baixava uma única criatura para vencer devagar.
É o modelo do deck que aposta tudo no Estágio Três.

## 3. Como identificar o papel: seis perguntas

**O que é.** Uma lista de sinais para matchups entre estratégias semelhantes. Compare as
duas listas item a item.

**Como usar na construção (checklist).**

| Pergunta | Leitura |
|---|---|
| 1. Quem tem inevitabilidade? | O sinal mais importante. Quem melhora de posição quanto mais o jogo dura é o maior e pode jogar como controle. O outro precisa encurtar o jogo. |
| 2. Quem tem mais maneiras de causar dano? | Quanto mais fontes de dano um deck paga para ter (criaturas, burn, terrenos que atacam, planeswalkers ofensivos), mais provável que seja o beatdown. |
| 3. Quem tem mais criaturas? | Costuma indicar o beatdown, mas olhe **quais**: criaturas que só atacam apontam para agressão; criaturas que geram valor ou bloqueiam bem apontam para midrange ou controle. |
| 4. Quem tem mais remoção? | Depende do tipo: varreduras e remoção defensiva indicam plano grande; bounce e remoção que só ganha tempo indicam plano de tempo. |
| 5. Quem tem mais counters? | Mesma distinção: counters para dominar o jogo longo ou para proteger uma vantagem de tempo? |
| 6. Quem compra mais cartas? | Quase sempre o deck maior. Exceções: motores de compra tão fortes que até decks agressivos usam, e decks de combo. |

Se as respostas divergirem, a pergunta 1 decide.

## 4. O beatdown também controla o jogo

**O que é.** Uma estratégia rápida aceita perder posição de mesa, quantidade ou qualidade
de cartas para aproximar o fim do jogo, e ataca mesmo se expondo ao contra-ataque. Chapin
insiste que isso é uma forma de controle com meios opostos: quem pressiona o total de
vida desde o turno 1 dita as regras da partida.

**Quando se aplica.** Ao avaliar se um deck agressivo é coerente e ao montar a defesa
contra ele.

**Como usar na construção.**
- Pressão sobre a vida gera vantagem virtual: com o oponente em seis de vida, todo burn
  de três de dano é uma carta excelente, e ele passa a gastar mana e cartas só para não
  morrer (por exemplo, segurando mana para counters em vez de desenvolver o jogo).
- Num deck beatdown, cada carta deve responder: "isto aproxima o fim do jogo?". Cartas
  de valor lento diluem o plano.
- O beatdown propõe uma corrida: "quem executa o plano primeiro?". Só entre nela se o seu
  deck for de fato o mais rápido do confronto.

## 5. Midrange: maior que os rápidos, mais rápido que os grandes

**O que é.** O midrange existe para trocar de papel: age como o deck maior contra decks
rápidos e como o mais rápido contra decks grandes. Para Chapin o nome engana: o que
define esses decks é irem bem no meio do jogo (Estágio Dois), e não um "alcance
intermediário". Um midrange pode vencer no turno 4 ou no 24 e, às vezes, planeja jogos
mais longos que os de certos controles. Também não se define por inevitabilidade: há
aggros com inevitabilidade sobre midranges e controles sem ela.

**Quando se aplica.** Ao construir midrange e anti-meta.

**Como usar na construção.**
- O deck precisa de cartas para os dois papéis: defesa barata e corpos resistentes para
  segurar aggro; pressão e disrupção para punir controle e combo.
- O sideboard é o que completa a troca de papel: tire as cartas do papel errado e traga
  as do papel certo.
- Teste de coerência por matchup: "sou realmente maior que os decks rápidos do meta e
  realmente mais rápido que os grandes?" Se um deck do meta é mais rápido **e** maior que
  o seu, o matchup é ruim e exige um plano específico.

## 6. O mesmo deck, papéis diferentes

**O que é.** O papel depende do oponente e pode até se inverter durante o jogo.

**Quando se aplica.** Em confrontos entre decks do mesmo tipo e sempre que o estado do
jogo muda de forma brusca.

**Como usar na construção e no plano de jogo.**
- Para cada matchup, escreva o plano em uma frase que comece por "sou o beatdown porque..."
  ou "sou o controle porque...".
- Traduza o papel em um relógio (clock). Como beatdown, conte quantos turnos faltam para
  matar e jogue para reduzir esse número: cada turno a mais é uma compra a mais para o
  oponente sair da situação. Como controle, estime quantos turnos o oponente lhe dá antes
  de matar: essa conta diz se há tempo para uma jogada de valor (comprar cartas) ou se a
  mana tem de ir para a resposta imediata. Na construção, a mesma conta mostra se a
  lista tem jogadas de valor demais para o tempo que os decks rápidos do meta concedem.
- O papel muda decisões pequenas: baixar um terreno desvirado pagando vida para causar
  dano antes, ou baixá-lo virado para preservar a vida e alongar o jogo.
- O papel pode mudar no meio da partida: uma carta poderosa comprada do topo, ou a
  transição de um estágio para outro, pode inverter quem tem inevitabilidade. Trocar de
  papel é legítimo; não ter consciência do papel atual é o erro.
- Jogue o que a mesa e a mão pedem: o deck de controle com uma abertura explosiva pode
  e deve atacar.

**Exemplo histórico.** Um aggro verde-branco enfrentava dois decks vermelho-verdes. Contra
a versão de criaturas pequenas e muito rápidas, o correto era assumir o papel maior:
acompanhar o início, proteger a vida para não morrer no burn e vencer com criaturas mais
gordas. Contra a versão de monstros caros e planeswalkers, que era maior, o correto era
atacar logo, antes que as cartas pesadas dominassem a mesa.

## 7. Exceções: interações que invertem o papel

**O que é.** Às vezes o deck mais rápido vira o controle por causa de cartas específicas,
interações não planejadas ou efeitos secundários.

**Como usar na construção.**
- Criaturas baratas com efeito de disrupção permitem que um aggro seja o controle contra
  combo: ele trava o oponente e vence devagar, em vez de apostar corrida.
- Negação de recursos é outra forma de controlar: destruição em massa de terrenos ou
  travas de mana prendem o oponente no Estágio Um. As cartas na mão dele deixam de valer
  porque não podem ser conjuradas, o que é vantagem virtual de cartas. A mesma carta
  serve a um deck ofensivo (impede o oponente de chegar ao fim de jogo dele) e a um deck
  de prisão (que mantém a própria mana com fontes que não são terrenos).

**Exemplo histórico.** Zoo com Thalia, Guardian of Thraben e criaturas semelhantes era o
controle contra o combo de storm. Armageddon foi usado tanto por decks agressivos brancos
quanto por decks de prisão.

## 8. Decks de combo

**O que é.** Combo não é um terceiro papel. Há **combo beatdown**, que só quer correr, e
**combo-control**, que segura o jogo e combina no fim.

**Quando se aplica.** Ao construir combo e ao construir contra combo.

**Como usar na construção.**
- **Combo beatdown:** quase tudo no deck é mana, compra e proteção para resolver as peças;
  a resposta a qualquer ameaça é vencer antes. Contra ele, o oponente é o controle, mesmo
  sendo um deck agressivo: precisa de disrupção e defesa, pois na corrida pura perde.
- **Combo-control:** usa counters, descarte e remoção para sobreviver e combina tarde
  (mesmo que "tarde" seja o turno 4 ou 5 num formato rápido), muitas vezes no turno
  anterior ao que morreria.
- Entre dois combos, o mais lento não deve apostar corrida. Compare: velocidade sem
  interação (goldfish), custo da disrupção de cada lado e número de cartas que vencem
  sozinhas se não forem respondidas. Quem perde nesses três critérios é o controle.
- Mesmo o combo-control aproveita a janela: com mão para vencer cedo, vença.
- Ao posicionar um combo no meta, pergunte: "contra quais decks sou o mais rápido e
  contra quais preciso de interação para sobreviver?" Isso define quantas vagas vão para
  proteção e disrupção e quantas para velocidade.

**Exemplo histórico.** Na época do combo de Tolarian Academy, os decks vermelhos que
venceram foram os que entenderam que eram o controle naquele confronto e adotaram
elementos disruptivos e defensivos; os que tentaram queimar o oponente antes do combo
perderam. High Tide funcionava como o deck mais controlador de um formato muito rápido.

## 9. Do papel para a lista e para o sideboard

**O que é.** A aplicação prática: o papel determina que cartas são boas.

**Como usar na construção.**
- **Quando você é o controle no matchup:** valem as cartas que neutralizam ameaças e
  cartas da mão do oponente. Saem as condições de vitória excedentes ou lentas: uma
  finalizadora medíocre vale menos do que uma carta que tira duas ameaças do caminho.
- **Quando você é o beatdown:** saem as cartas de valor lento e as respostas reativas;
  entram pressão, alcance (dano que ignora bloqueio) e proteção para as ameaças.
- **Aggro com inevitabilidade:** se o controle adversário não tem como vencer o jogo longo
  contra o seu alcance, não ataque no desespero. Acumule burn na mão ou espere a mana para
  um burn que não pode ser anulado, como Banefire.
- **Controle sem inevitabilidade:** contra um combo que vence o jogo longo, o controle
  precisa de um modo beatdown: ameaça rápida apoiada em disrupção.
- Para cada matchup importante, o guia de sideboard deve registrar: papel, cartas do papel
  errado que saem, cartas do papel certo que entram (ver `sideboard.md`).

**Exemplo histórico.** Num controle enfrentando aggro vermelho-verde, o conselho que
funcionou foi tirar uma condição de vitória lenta e manter o descarte duplo: cada uso
eliminava duas cartas com que se preocupar, e vencer podia ficar para depois.

## Perguntas de fechamento

- Quem tem inevitabilidade neste matchup?
- Quem é o beatdown?
- O meu plano de jogo e o meu sideboard estão de acordo com essas duas respostas?

## Referências

*Next Level Magic* (Chapin, 2015). O capítulo desenvolve o artigo *Who's the Beatdown?*,
de Michael Flores.

| Seção deste documento | Capítulo | Páginas |
|---|---|---|
| 1, 2 | Your Role In A Game: Who's the Beatdown? | 260-262 |
| 3 | Your Role In A Game: Who's the Beatdown? | 267-268 |
| 4 | Your Role In A Game: Who's the Beatdown? | 264-265 |
| 5 | Your Role In A Game: Who's the Beatdown? | 262-263 |
| 6 | Your Role In A Game: Who's the Beatdown?; So What About Combo Decks? | 265-267, 270-272 |
| 6 (relógio/clock) | Developing the Perfect Mindset (Seção 2) | 177 |
| 7 | Your Role In A Game: Who's the Beatdown? | 260-261, 263-264 |
| 8 | So What About Combo Decks? | 269-271 |
| 9 | So What About Combo Decks? | 271-272 |
