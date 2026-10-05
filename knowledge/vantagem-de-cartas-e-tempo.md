# Vantagem de cartas, tempo e Philosophy of Fire: as três moedas do jogo

Este documento reúne os três blocos fundamentais da teoria de Magic (card advantage, tempo e Philosophy of Fire), explica como cada "moeda" se converte nas outras e dá critérios para medir e planejar isso em uma lista. Consulte-o ao avaliar o custo real de uma carta, ao escolher respostas e fontes de vantagem, ao montar decks de tempo, burn ou controle, ao decidir quanto lifegain ou quantos terrenos utilitários usar e ao justificar por que uma troca de recursos é boa para o plano do deck.

## Os três tipos de recurso

**O que é.** Os recursos do jogo se dividem pela forma como ficam disponíveis:

| Bloco | Recurso | Como se obtém | Exemplos |
|---|---|---|---|
| Philosophy of Fire | Recursos com que se começa e que não se renovam sozinhos | Estoque inicial; só aumenta pagando com cartas específicas | Pontos de vida, cartas no grimório, marcadores de veneno que ainda se pode receber, o mulligan |
| Tempo | Recursos que não existem no início e surgem a cada turno | Passagem dos turnos | Land drop, mana disponível, etapa de desvirar, fase de ataque, habilidades de uso por turno |
| Card advantage (card economy) | Recurso misto: há um estoque inicial e uma renda por turno | Sete cartas iniciais mais uma compra por turno | Cartas na mão e permanentes úteis na mesa |

Por ocupar os dois territórios, a economia de cartas é o centro da gestão de recursos e a linguagem mais usada para descrever o resto.

O objetivo de todos eles é o mesmo: ter mais e melhores **opções** do que o adversário, ou tirar opções dele. Comprar cartas dá opções; descarte, destruição de terrenos e contramágicas tiram; reduzir a vida do adversário a zero é a forma extrema de negar todas as opções que ele ainda teria.

**Quando se aplica.** Como vocabulário de base em qualquer análise de carta, troca ou plano.

**Como usar na construção.** Para cada carta, identifique qual moeda ela gasta e qual ela compra. Um deck coerente compra de forma consistente a moeda que o seu plano transforma em vitória.

## Card advantage (economia de cartas)

**O que é.** Card advantage é o lado positivo da economia de cartas: terminar uma troca com mais recursos permanentes do que o adversário. "Permanente" aqui significa vantagem que não some sozinha; toda vantagem duradoura acaba medida em "cartas".

Pontos centrais:

- **O custo embutido de uma carta.** Jogar uma carta custa o mana e também a própria carta, que sai da mão. Por isso muitas criaturas de um mana e auras de bônus pequeno são ruins: o efeito não vale uma carta, quanto mais uma carta e um mana. Um truque de combate custa uma carta, mas, se salva a sua criatura e mata a do adversário, o saldo é positivo.
- **Nada é de graça.** Cantrips (mágicas que se repõem comprando uma carta) e cartas de custo zero ainda custam mana, tempo e vaga na lista. O uso legítimo das mais baratas é "encolher" o deck para achar com mais frequência as cartas que importam.
- **Dois por um.** Cartas que valem por duas: compram duas, removem duas, ou entregam um corpo mais um efeito.
- **Utilidade pesa tanto quanto contagem.** Sete terrenos na mão valem menos do que dois terrenos e três mágicas conjuráveis. Efeitos de filtragem (comprar e descartar) melhoram a mão sem aumentar o número de cartas. O livro prefere o termo "economia" de cartas justamente por isso.
- **Quanto vale uma carta?** Depende do formato: onde compra de cartas é abundante e barata, pagar três manas por uma carta extra não impressiona; onde é escassa, pode ser das melhores jogadas. Regra de bolso antiga citada no livro: uma carta vale em torno de dois manas. O livro registra também a visão alternativa (AJ Sacher, Michael Flores) de avaliar tudo em mana.
- **Desvantagem de cartas pode ser o preço certo.** Quando a disputa em torno de uma mágica decide o jogo (resolver ou impedir uma fonte enorme de cartas, por exemplo), gastar duas cartas para vencê-la não é prejuízo: o que está em jogo vale mais do que uma carta. Exemplo histórico: Force of Will foi criticada no início por custar uma carta extra da mão e acabou reconhecida como obrigatória nos formatos em que essas disputas acontecem nos primeiros turnos.
- **Mana não escala em linha reta.** Seis manas são bem mais do que quatro mais dois, e oito bem mais do que seis mais dois: o custo real de uma carta cresce mais rápido do que o número impresso. E mana não usado no turno é perdido: gastar dois de quatro terrenos equivale, na prática, a ter gasto quatro.

**Quando se aplica.** Quanto mais reativo o deck, mais ele precisa de card advantage: quem responde a ameaças precisa de mais opções do que o adversário, pois parte das respostas compradas não será a certa. Decks agressivos dependem menos disso. Em qualquer caso, cartas extras são meio, não fim: em controle, servem para chegar ao Estágio Três com um trunfo que supera o plano adversário (ver `fases-do-jogo.md`).

**Como usar na construção.**

- Para cada carta, calcule o saldo típico: quantas cartas minhas ela consome e quantas cartas (compradas, removidas, descartadas, postas na mesa) ela rende.
- Não inclua cartas cujo efeito não vale uma carta, por mais baratas que sejam.
- Conte as fontes de vantagem da lista (compra, dois por um, motores recorrentes) e confira se a quantidade condiz com o papel: alta em controle, moderada em midrange, baixa em aggro.
- Avalie cantrips pelo que realmente fazem no deck (consistência, sinergia), não como "grátis".
- Confira se a curva usa o mana de cada turno; mana que sobra sistematicamente é recurso desperdiçado.

## Virtual card advantage

**O que é.** Vantagem de cartas que não aparece na contagem literal de cartas compradas:

- **Fichas e corpos.** Uma ficha de criatura deve ser tratada como uma carta, embora muitas vezes fraca. O valor depende do estado do jogo: com efeitos que aproveitam qualquer corpo, ou contra um adversário que só tem remoção pontual, cada corpo conta inteiro; numa mesa em que todas as criaturas superam uma 1/1, vale pouco. Referências do livro: uma 0/1 normalmente não vale uma carta; uma 2/1 ou maior, ou um corpo com boa habilidade (voar, tipo relevante), vale uma carta ou mais; uma 1/1 genérica vale cerca de dois terços de carta, porque o padrão de comparação é a 2/2 de dois manas e são precisas duas 1/1 para trocar com ela.
- **Cartas afetadas.** O saldo de uma carta inclui tudo o que ela afeta: cada permanente útil que entra do seu lado, cada permanente tirado do adversário, cada carta que ele descarta, e até efeitos que atuam de zonas incomuns, como o cemitério.
- **Grimório não conta.** Triturar cartas do topo do grimório adversário não é card advantage: cartas ainda não compradas são um estoque fixo, assunto da Philosophy of Fire. Pode até ajudar o adversário se o deck dele usa o cemitério.
- **Compras vivas.** Terrenos comprados tarde costumam ser compras mortas. Terrenos que fazem algo (viram criatura, filtram compras, removem, criam fichas) transformam essas compras em opções reais, o que equivale a uma carta a mais. O preço é entrar virado, produzir mana incolor ou ocupar a vaga de outro terreno.
- **Não desperdiçar corpos.** Bloquear só para absorver dano (chump block) troca uma carta por alguns pontos de vida. Em geral só compensa quando o ataque seria letal, quando evita uma quantidade de dano excepcional, quando o ataque daria outra vantagem ao adversário (por exemplo, um gatilho de dano de combate que lhe rende uma carta) ou quando a vida, naquele confronto, vale mais do que o corpo.

**Quando se aplica.** Ao avaliar geradores de fichas, sweepers, descarte, terrenos utilitários e cartas com valor recorrente.

**Como usar na construção.**

- Avalie fichas pelo tamanho e pela utilidade no metagame esperado, não pela contagem bruta: duas 1/1 por dois manas só são "dois por um" se corpos pequenos importarem naquela mesa.
- Estime quantas compras do deck são mortas no fim de jogo e considere terrenos utilitários para reduzir esse número, pesando o custo na base de mana (cores, terrenos virados).
- Meça sweepers e remoção em massa pelo número de cartas que tipicamente removem em relação ao custo.
- Cartas de trituração só entram como plano de vitória ou sinergia, nunca como "vantagem de cartas".

**Exemplo.** Celestial Colonnade entra virada, mas no fim do jogo é um terreno que ameaça como criatura; um terreno básico comprado no mesmo momento não ofereceria opção alguma.

## Tempo

**O que é.** Tempo trata dos recursos que se ganham a cada turno e não existem no começo; o principal é o mana, limitado pela regra de um terreno por turno. Vantagens de tempo são temporárias: dissipam-se sozinhas se não forem convertidas em algo duradouro.

- **Quebrar o limite de um terreno por turno tem valor.** Por isso aceleradores custam mana e uma carta. Trocar uma carta por um salto de mana é desvantagem de cartas na superfície e lucro se o salto antecipar algo que vale mais do que uma carta.
- **Trocas de mana.** Responder a uma ameaça gastando menos mana do que o adversário gastou nela gera tempo. Um atraso de dois manas que devolve a mágica à mão do dono ganha tempo contra mágicas de três ou mais, e perde contra mágicas de um ou dois, porque exige segurar mana aberto antes de saber o que virá. A força desse tipo de carta sobe e desce com o custo médio das mágicas do formato.
- **Negar tempo.** Destruir terrenos, devolver permanentes à mão, anular com atraso: tudo isso tira turnos do adversário. Só compensa quando o resto do turno rende o suficiente (por exemplo, atacando) ou quando o deck tem massa crítica para manter o adversário preso no Estágio Um.
- **A regra de ouro.** "Tempo is only worth what you can do with it." Atrasar o adversário em vários turnos e não fazer nada com isso equivale a comprar sete cartas e serem todas terrenos. O mana economizado numa troca também só conta se for usado.

**Quando se aplica.** Em decks de tempo (ameaça barata mais interação barata), em qualquer escolha de respostas e ao avaliar aceleração de mana.

**Como usar na construção.**

- Um deck de tempo precisa responder: **o que eu ganho a cada turno que compro?** Normalmente uma fonte de vantagem que rende enquanto está na mesa (gerador de fichas, compra recorrente, um relógio de criaturas baratas). Sem ela, as cartas de atraso não compram nada.
- A estrutura clássica: sair rápido do Estágio Um, instalar a fonte de vantagem e gastar as demais cartas atrasando o adversário para que ele não alcance o Estágio Três.
- **Escolha de respostas:** contra uma ameaça específica, prefira respostas que custem o mesmo ou menos do que ela, ou que tragam um bônus (comprar carta, deixar um corpo, scry). Trocar um por um pagando mais mana é perder tempo, mesmo quando a jogada é correta.
- Para cada carta de tempo, compare o mana que ela custa com o mana típico das mágicas do metagame. Se o formato gira em torno de mágicas de um e dois manas, atrasos de dois manas perdem valor.
- Aceleração só entra se houver algo que valha a pena antecipar; num deck que joga do topo do grimório, mana extra não vale nada.
- Contra um deck de tempo, identifique o que exatamente ele faz com o tempo que ganha e ataque isso: remoção para o motor, ameaças que não podem ser anuladas ou que entram em velocidade instantânea contra contramágicas baratas.

**Exemplo histórico.** O deck Faeries do Standard de 2008 instalava cedo um motor como Bitterblossom e tratava quase todas as outras cartas como "turnos extras" tirados do adversário. O livro observa que bons pilotos desse deck faziam mulligan de mãos sem motor: tempo sem nada para aproveitar não vale a mão. Outro caso citado: sob Winter Orb, uma contramágica de atraso como Memory Lapse deixa de valer dois manas e passa a valer vários turnos, cada um deles pago em dano pelas criaturas que já estão atacando.

## Philosophy of Fire: vida como recurso, dano como unidade

**O que é.** A vida é um estoque inicial que não se renova. O total em si é só um número: o que importa é não chegar a zero e o que se pode comprar com os pontos restantes. O bloco tem duas faces:

1. **Gastar a própria vida** para obter cartas, tempo ou opções: custos pagos em vida (terrenos, compra de cartas) e também decisões como aceitar dano agora para conseguir uma troca melhor depois (esperar o adversário comprometer mais criaturas antes do sweeper) ou para ganhar informação.
2. **Gastar cartas e mana para reduzir a vida do adversário.** Cada mágica de dano troca uma carta e algum mana por pontos de vida dele. A mesma mágica vale pouco com o adversário em vinte e muito quando o deixa ao alcance: a partir daí ele não pode mais virar tudo com segurança, o que atrasa os trunfos dele.

Consequências:

- **Dano como unidade de conta.** Uma criatura que fica na mesa vale o dano que ainda causará; perdê-la num ataque pode ser correto se isso causar mais dano do que uma mágica de burn causaria. Do outro lado, um bloqueio que absorve três de dano contra burn funciona como "anular" uma mágica de três de dano.
- **Lifegain é contextual.** É fraco em geral e forte contra quem conta dano. Kitchen Finks contra um deck vermelho representa dois corpos a atravessar (por causa de persist) e, a cada entrada, dois pontos de dano desfeitos, o que anula parte das mágicas de burn já gastas sem comprar carta alguma; num deck que paga vida para os próprios efeitos, a mesma vida significa turnos extras de uso desses efeitos.
- **Prioridade de respostas.** Em vida baixa, anular a mágica de dano maior pode poupar várias respostas que seriam obrigatórias contra as menores: é card advantage obtida pela gestão da vida.
- **Outros estoques.** Cartas no grimório e tolerância a veneno seguem a mesma lógica, e o valor desses estoques muda quando surgem cartas que os usam como custo.
- **Planeswalkers.** São vulneráveis a criaturas atacando e a dano direto; dano passou a ser também defesa contra eles.

**Quando se aplica.** Em decks de burn e aggro (alcance), em decks que pagam vida por eficiência, na decisão sobre lifegain e na avaliação de quanto dano a base de mana pode custar.

**Como usar na construção.**

- **Burn e aggro:** conte o dano total que a lista entrega de forma realista e compare com vinte. Mágicas de dano direto são o alcance que fecha o jogo depois que o adversário estabiliza; verifique se há alcance suficiente para os últimos pontos.
- **Custos em vida:** some o dano autoinfligido esperado (terrenos, compra, motores) e compare com a agressividade do metagame. Contra decks que não pressionam a vida, esses pontos são quase gratuitos; contra burn, cada ponto é parte de uma carta do adversário.
- **Lifegain:** inclua quando o metagame contém decks que vencem contando dano e quando o lifegain vem acoplado a algo útil (um corpo, uma remoção). Avalie-o como "quantas cartas do adversário isto desfaz".
- **Remoção por dano** ganha valor em formatos com planeswalkers relevantes.
- Pergunta constante: quanto vão valer os pontos de vida, para mim e para o adversário, à medida que o jogo avança neste confronto?

## Como as moedas se trocam

| Troca | Como acontece | Só vale a pena se |
|---|---|---|
| Carta por tempo | Aceleração de mana, atrasos que não resolvem a ameaça de vez | O tempo ganho vira algo que vale mais do que uma carta |
| Tempo por carta | Gastar um turno comprando ou jogando uma fonte lenta de vantagem | O deck sobrevive ao turno "perdido" |
| Vida por carta | Custos em vida para comprar; aceitar dano para conseguir um dois por um | O adversário não consegue punir a vida gasta |
| Vida por tempo | Terrenos que entram desvirados a custo de vida; não bloquear para manter o desenvolvimento | Idem; depende da pressão do confronto |
| Carta por vida do adversário | Burn no rosto; atacar sacrificando criaturas | O total de dano fecha o jogo antes de as cartas acabarem |
| Carta por vida própria | Chump block, lifegain | A vida, no confronto, vale mais do que a carta |
| Mana por carta | Compra de cartas (referência de bolso: cerca de dois manas por carta) | O formato não oferece o mesmo efeito por menos |

Uma troca é boa quando o recurso entregue vale menos, naquele contexto, do que o recebido. Jogadores fracos sacrificam recursos demais por ganhos temporários; jogadores medianos evitam sempre; os bons procuram os momentos em que é certo.

## Checklist para medir uma lista

1. **Moeda principal.** Em qual moeda o deck vence (cartas, tempo, dano)? As cartas compram essa moeda de forma consistente?
2. **Saldo de cartas.** Quantas fontes de vantagem real e virtual há? É compatível com o papel (reativo precisa de mais)?
3. **Custo embutido.** Há cartas cujo efeito não vale uma carta?
4. **Eficiência das respostas.** As respostas custam o mesmo ou menos do que as ameaças do metagame, ou trazem bônus?
5. **Uso do tempo.** Se o deck gera tempo, o que ele faz com os turnos ganhos? Há motores ou relógio suficientes?
6. **Uso do mana.** A curva permite gastar o mana de cada turno? Há utilidade para o mana no fim de jogo (terrenos utilitários, habilidades)?
7. **Orçamento de vida.** Quanto de vida o próprio deck consome e quão agressivo é o metagame?
8. **Alcance.** Se o plano é dano, a soma realista de dano chega a vinte? Há dano direto para os últimos pontos?
9. **Compras mortas.** Quantas cartas ficam inúteis no fim de jogo, e o que reduz esse número?

## Referências

Next Level Magic (Chapin, 2015), Seção 3, "In-Game Magic Strategy":

- Os três tipos de recurso: "The Building Blocks of Magic Theory", p. 192-193.
- Economia de cartas, custo embutido, cantrips, opções, valor de uma carta, escala do mana, dois por um: "Card Advantage", p. 194-200.
- Fichas, cartas afetadas, grimório, chump block, quem precisa de card advantage, terrenos utilitários: "Virtual Card Advantage", p. 201-207.
- Tempo, trocas de mana, negação de tempo, decks de tempo, escolha de respostas: "Tempo", p. 208-216.
- Vida como recurso, burn, lifegain, outros estoques, planeswalkers, prioridade de respostas: "The Philosophy of Fire", p. 217-223.
- Desvantagem de cartas como preço certo (debate sobre Force of Will): Seção 2, "Applying the Perspectives to Build a Magic Team", p. 90-92.
- Mulligan como recurso não renovável: "Less Can Be More: The Art of the Mulligan", p. 224 (detalhado em `mulligan.md`).

A tabela "Como as moedas se trocam" e o checklist final são uma síntese organizada a partir desses capítulos; o livro não os apresenta nesse formato.
