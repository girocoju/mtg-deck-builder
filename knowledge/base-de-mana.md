# Base de mana

Como dimensionar e conferir a base de mana de qualquer deck: quantos terrenos, quantas
fontes de cada cor, como contar aceleração, cantrips, MDFCs e terrenos que entram virados.
O agente consulta este documento ao montar a base de mana de um deck, ao responder
perguntas como "por que 24 terrenos?" e ao revisar uma lista cuja mana parece frágil.

O documento junta duas fontes, com papéis diferentes:

- **Parte 1 — Princípios** (Patrick Chapin, *Next Level Magic*): o raciocínio. Por que
  não economizar terrenos, como partir de um modelo, que riscos pesar.
- **Parte 2 — Números** (Frank Karsten, artigos de 2017 a 2024): fórmulas e tabelas
  obtidas por regressão sobre decks reais e por simulação.

**Quando as duas divergem, prevalecem os números da Parte 2**, por serem mais recentes e
apoiados em dados. Os números da Parte 1 estão marcados como "números do livro (2015)" e
servem como contexto histórico: as faixas de terrenos do livro são, em geral, 1 a 2
terrenos mais baixas que as recomendações atuais, e os pesos de aceleração e cantrips
são diferentes.

## Resposta rápida

Para 60 cartas (detalhes, hipóteses e outros tamanhos de deck na Parte 2):

1. **Terrenos:** `19,59 + 1,90 × valor de mana médio − 0,28 × mágicas baratas de compra/ramp`.
   Na prática: cerca de 23 para aggro de curva baixa, 25–26 para midrange, mais para
   controle; 17 em 40 cartas; 38–39 mais ~8 fontes extras em Commander.
2. **Fontes por cor**, pela carta mais exigente de cada cor: 14 para conjurar `C` no
   turno 1 (fontes desviradas), 13 para `1C`, 21 para `CC`, 18 para `1CC`, 23 para `CCC`.
3. **Na dúvida entre um terreno e uma mágica, o terreno.** Cortar terrenos é uma fonte
   de derrotas que não aparece em nenhum jogo isolado (Parte 1, seção 4).

## Parte 1 — Princípios (Chapin, *Next Level Magic*)

Este documento reúne o raciocínio de Patrick Chapin para dimensionar uma base de mana:
quantos terrenos, quantas fontes por cor, como contar aceleração e cantrips, e quais
riscos pesar. O agente deve consultá-lo ao definir ou justificar a base de mana de
qualquer deck de construído, ao responder perguntas como "por que 24 terrenos?" e ao
revisar uma lista cuja mana parece frágil.

Chapin avisa que não existe fórmula: montar base de mana é uma habilidade que se treina.
Quem escreve "23 terrenos" no fim da lista sem especificar quais nunca desenvolve essa
habilidade.

### 1. Partir de um modelo (templating)

**O que é.** Usar como ponto de partida a base de mana de um deck bem-sucedido e parecido
com o seu, em vez de tirar números do nada. É, segundo o autor, o conselho mais importante
do capítulo.

**Quando se aplica.** Sempre, e mais ainda em decks de controle, que são difíceis de
resumir em regra geral.

**Como usar na construção.**
- Procure listas vencedoras do mesmo arquétipo, com curva e exigência de cores
  semelhantes. Para um aggro com um splash leve, veja quantas fontes do splash os aggro
  com splash leve usam.
- Adapte ao que o seu deck pede de diferente (curva mais alta, custo colorido mais pesado,
  mais terrenos virados).
- No projeto: os dados de metagame são a fonte natural de modelos; cite o modelo usado.

### 2. A qualidade possível depende do formato

**O que é.** Quão boa a mana pode (e deve) ser é função do fixing disponível no formato.

**Como usar na construção.** Antes de escolher o número de cores, verifique na base de
cartas quais terrenos duplos e de fixing são legais no formato. Com fixing fraco, reduza
cores ou alivie os custos coloridos; com fixing forte, três ou mais cores passam a ser
viáveis, pagando o preço em terrenos virados ou em vida.

### 3. Quantos terrenos

**O que é.** O número de terrenos decorre do que o deck exige: quantos terrenos ele
precisa ter em jogo para funcionar e até que ponto da curva ele precisa chegar.

**Números do livro (2015)**, deck de 60 cartas:

| Perfil do deck | Terrenos |
|---|---|
| Aggro que funciona com um ou dois terrenos | 20-21 |
| Curva com várias jogadas de custo 3 e algumas de custo 4 | 23-24 |
| Midrange ou controle, curva até custos 4 e 5 | 25-26 |
| Controles mais pesados | 26-27 |
| Combo que quer um terreno, de preferência dois, sem inundar | 16-18 |
| Combo de formatos com mana rápida extrema, em que um terreno basta | 10-14 |
| Combo que precisa baixar terreno nos quatro primeiros turnos | como midrange/controle |

**Como usar na construção.**
- Pergunta-guia: "quantos terrenos este deck precisa comprar para operar, e em que turno?"
- Para combo, a faixa é enorme (o livro fala de zero a 42 terrenos); ignore o rótulo do
  arquétipo e responda só à pergunta-guia.
- Confira contra um modelo (seção 1) antes de fechar.

### 4. Não economizar terrenos

**O que é.** Cortar terrenos para abrir espaço para mágicas é, para Chapin, uma grande
fonte **oculta** de derrotas: o custo não aparece em nenhum jogo específico, só na soma
dos jogos em que o deck travou.

**Quando se aplica.** Toda vez que a lista está com 61 ou 62 cartas boas e o corte mais
fácil parece ser um terreno.

**Como usar na construção.**
- Jogue o número de terrenos que o deck pede, dado o que você exige dele. Se quer cortar um
  terreno, antes reduza a exigência (baixe a curva) ou acrescente cantrips ou aceleração
  que justifiquem o corte (seções 6 e 7).
- Uma base ruim contamina os testes: ideias boas são descartadas porque a mana falhou,
  não porque o conceito era fraco. Desconfie da mana antes de condenar o deck.

### 5. Fontes por cor

**O que é.** Além do total de terrenos, importa quantas fontes produzem cada cor.

**Números do livro (2015)**, para decks aggro:

| Necessidade | Fontes da cor |
|---|---|
| Cor principal, precisando de duas manas dessa cor | pelo menos 18-19 |
| Apenas uma mana de cada cor | 13-16 costumam bastar |

No estudo de caso de um controle de quatro cores, o autor queria **19-20 terrenos**
ajudando com as duas cores mais pesadas da sua mágica de sete manas (três símbolos de uma
cor, dois de cada uma das outras duas).

**Como usar na construção.**
- Conte fontes de verdade. Um acelerador que busca terreno de qualquer cor ajuda as
  **outras** cores, mas não conta como fonte da cor que ele próprio custa: Rampant Growth
  não é fonte de verde.
- Trabalhe de trás para frente a partir das cartas mais exigentes: qual mágica precisa
  estar conjurável em qual turno? Essas exigências determinam a base.
- Conte os básicos buscáveis: terrenos e mágicas que buscam básicos precisam de alvos
  suficientes de cada tipo, inclusive no fim do jogo, quando vários já saíram do deck.
- Verifique conflitos internos: um terreno que produz só um par de cores pode atrapalhar
  quando o deck tem mágicas de três cores de trios diferentes.

### 6. Tempo certo: terrenos virados e jogadas de turno específico

**O que é.** Não basta ter a cor; é preciso tê-la **no turno em que a carta rende**.

**Como usar na construção.**
- Para cada jogada-chave de turno fixo, conte quantos terrenos a permitem naquele turno.
  Um elfo de mana de custo 1 é muito melhor no turno 1 do que em qualquer outro: quantos
  terrenos desvirados produzem verde no turno 1?
- Para mágicas de turno 2 com duas cores, conte os terrenos que entram virados: dá para
  baixar terreno no turno 2 e ainda conjurar a mágica com consistência?
- Decks sem jogada de turno 1 toleram mais terrenos virados nesse turno.
- Posição de Chapin sobre o dilema: é muito pior não conseguir conjurar as mágicas do que
  estar sempre um turno atrás. Mas o tempo perdido precisa ser recuperado em outro lugar,
  com interação barata (remoção de um mana, counters baratos).
- Terrenos também têm retornos decrescentes, e cada tipo tem a sua curva: o primeiro
  terreno lento de cinco cores é bem-vindo, o segundo é péssimo; por isso o número certo
  pode ser 3, 2 ou 1 em vez de 4 (ver `quantidade-de-copias.md`).

**Exemplo histórico.** No controle de quatro cores de 2009 (26 terrenos, somando a lista
do livro), o autor usou oito terrenos de três cores que entram virados e três cópias de
um terreno de cinco cores ainda mais lento, compensando com remoção barata como
Lightning Bolt. Limitou certo fetch land a três cópias porque os básicos buscáveis
acabavam, e certo terreno duplo a duas porque cópias demais deixavam a mesa com excesso
de uma cor e sem as outras para a mágica mais cara.

### 7. Aceleração que não é terreno

**O que é.** Pedras de mana, mágicas de ramp e criaturas de mana contribuem para a mana,
mas valem menos que um terreno.

**Números do livro (2015):**

| Fonte | Vale | Piso de terrenos |
|---|---|---|
| Acelerador não-criatura (ex.: Mind Stone, Rampant Growth) | 1/2 terreno | — |
| Criatura de mana (ex.: Birds of Paradise, Elvish Mystic) | 1/4 terreno | — |
| Deck com aceleradores de custo 2 | — | mínimo 23-24 terrenos |
| Deck com aceleradores de custo 1 | — | mínimo 21-22 terrenos |

**Como usar na construção.**
- Criaturas de mana valem menos porque são frágeis: morrem para qualquer remoção e para
  varreduras. Não ancore a base nelas.
- O piso existe porque o acelerador precisa de terrenos para ser conjurado; aceleração
  não conserta mão sem terreno.
- Cálculo: terrenos efetivos = terrenos + 0,5 × aceleradores não-criatura + 0,25 ×
  criaturas de mana, respeitando o piso.

### 8. Cantrips e manipulação de biblioteca

**O que é.** Cantrips baratos que escolhem cartas ajudam a achar terrenos (e a não achar
quando sobram).

**Números do livro (2015).** Um cantrip barato de seleção vale entre 50% e 100% da
proporção de terrenos do deck. Com 24 terrenos em 60 cartas (40%), cada cantrip equivale a
0,2-0,4 terreno. Regra de bolso: **quatro cantrips do tipo Ponder permitem cortar um
terreno**.

**Como usar na construção.** Aplique só a cantrips baratos e com seleção real; compra
cara não substitui terreno, pois você precisa dos terrenos para conjurá-la.

### 9. Estudar bases alheias: quatro olhares

**O que é.** O método de treino recomendado, usando as quatro perspectivas do livro.

**Como usar na construção.**
1. **O que está lá:** em listas vencedoras, que padrões de terrenos e quantidades se repetem?
2. **O que não está:** que terrenos e que fixing os bons jogadores evitam? Por quê?
3. **De trás para frente:** que exigências (carta X no turno N) explicam os números do modelo?
4. **De frente para trás:** imagine as mãos e os primeiros turnos com a sua base. Onde
   emperra? Um problema potencial não inviabiliza a base, mas precisa ser decidido de
   forma consciente.

### 10. Terrenos utilitários (lacuna da fonte)

O capítulo praticamente não trata de terrenos utilitários (os que geram valor além de
mana). O que dele se aproveita para o tema: todo terreno que não entra desvirado
produzindo as cores necessárias cobra um custo em tempo ou em consistência de cor, e esse
custo tem de ser contado como o de qualquer terreno lento (seção 6); e a quantidade de
cópias segue a lógica de retornos decrescentes. Regras numéricas sobre quantos terrenos
utilitários cabem devem vir de outra fonte.

### Checklist de custos e riscos

- [ ] O total de terrenos corresponde ao perfil de curva (seção 3) e a um modelo real?
- [ ] Cada cor tem fontes suficientes para o custo colorido mais exigente?
- [ ] Aceleradores e cantrips foram contados como frações, com o piso respeitado?
- [ ] As jogadas de turno 1 e 2 são conjuráveis apesar dos terrenos virados?
- [ ] O tempo perdido com terrenos lentos é compensado por interação barata?
- [ ] Há básicos suficientes para tudo que busca básicos?
- [ ] Algum terreno produz combinações que conflitam com as mágicas multicoloridas?
- [ ] Alguma cópia extra de terreno especial é ruim quando comprada em dobro?
- [ ] Um terreno foi cortado só para caber mais uma mágica? Reverta ou justifique.

### Referências

*Next Level Magic* (Chapin, 2015).

| Seção deste documento | Capítulo | Páginas |
|---|---|---|
| 1, 2 | All Your Manabase Are Belong To Us | 239-240 |
| 3 | All Your Manabase Are Belong To Us | 241-242 |
| 4 | All Your Manabase Are Belong To Us | 240, 243 |
| 5 | All Your Manabase Are Belong To Us; Knowing How Many of Each Card To Use (terrenos do estudo de caso) | 240, 243, 254-256 |
| 6 | All Your Manabase Are Belong To Us; Knowing How Many of Each Card To Use | 240, 254-256 |
| 7 | All Your Manabase Are Belong To Us | 241 |
| 8 | All Your Manabase Are Belong To Us | 242 |
| 9 | All Your Manabase Are Belong To Us | 242-243 |
| 10 | Lacuna: não coberto no intervalo 239-243 | — |
| Abertura ("23 terrenos") | It Takes 75, Not 60... | 237 |

---

## Parte 2 — Números (Frank Karsten)

> Todos os números abaixo foram lidos das fontes em 2026-10-04 (ver Referências da Parte 2).
> Onde aparece **"calculado"**, o valor é uma conta feita aqui a partir de uma fórmula do
> artigo, não um número publicado. Onde aparece **"não verificado"**, o dado não foi lido
> na fonte e não deve ser usado como fato.

### Conceito

Duas perguntas separadas, respondidas em ordem:

1. **Quantos terrenos?** Depende do valor de mana médio do deck e de quantas mágicas
   baratas de compra/ramp ele tem. Resposta: uma fórmula de regressão [K1].
2. **Quantas fontes de cada cor?** Depende do custo colorido mais exigente de cada cor.
   Resposta: uma tabela de fontes mínimas por custo [K2].

A tabela de fontes **pressupõe** que o número de terrenos já está certo. Sempre resolver
(1) antes de (2).

### Quando se aplica

- Qualquer deck construído de 60 cartas, decks de 80 cartas (Yorion), Commander de 99
  cartas + comandante, e Limited de 40 cartas (só a parte de fontes e land drops; ver
  ressalva sobre a fórmula de terrenos).
- Os modelos de Commander supõem mesa casual multiplayer, com mulligan grátis e compra no
  primeiro turno. Karsten avisa que não servem para cEDH [K3].
- São pontos de partida. O próprio autor mostra decks reais 1 a 2 terrenos acima ou
  abaixo da fórmula por motivos legítimos (ver "Ajustes").

---

### 1. Quantos terrenos

#### 1.1 Fórmulas [K1]

Base: regressão linear sobre 95.143 decks de 60 cartas com mais vitórias que derrotas
(MTG Melee e Magic Online, 2020-07-01 a 2022-07-01). R² = 0,395 e erro quadrático médio
de 2,75 terrenos, ou seja, a fórmula explica a tendência, não cada deck.

| Tamanho | Fórmula (terrenos, contando MDFCs como fração) | Origem |
|---|---|---|
| 60 cartas | `19,59 + 1,90 × VMM − 0,28 × baratas + 0,27 × companion` | Regressão direta [K1] |
| 80 cartas (Yorion) | `80/60 × (19,59 + 1,90 × VMM + 0,27) − 0,28 × baratas` | Escala proposta no artigo [K1] |
| 99 cartas (Commander) | `31,42 + 3,13 × VMM − 0,28 × baratas` | Escala + ajuste de −1,35 pelo mulligan grátis e pela compra no turno 1 [K1] |
| 40 cartas (Limited) | **Não há fórmula no artigo de 2022.** Usar 17 terrenos como padrão (ver 1.5) | — |

Onde:

- **VMM** = valor de mana médio das cartas que não são terrenos (soma dos valores de mana
  dividida pelo número de não-terrenos). MDFCs terreno/mágica entram pelo custo da face
  da frente, como faz o MTG Arena.
- **baratas** = número de mágicas baratas de compra ou de ramp (definição em 1.2).
- **companion** = 1 se o deck tem companion, senão 0. Na fórmula de 80 cartas já vem
  embutido como 1; na de 99 o comandante é tratado como um pseudo-companion.

Leitura rápida dada pelo autor: com VMM 3, um deck de 60 começa em 25–26 terrenos e um
de 99 em 40–41; corta-se 1 terreno a cada 3–4 mágicas baratas de compra/ramp.

Karsten classifica a versão de 99 cartas como estimativa "de guardanapo" (ele não tinha
dados de desempenho de Commander); a de 80 também é aproximada.

#### 1.2 O que conta como "mágica barata de compra ou ramp" [K1]

Critério usado na regressão (aplicável direto sobre o texto Oracle):

- **Compra barata:** carta não-terreno de valor de mana ≤ 2 cujo texto compra cartas
  ("draw a card", "draw two cards" etc.). Se for criatura, só conta se a compra vier de
  um gatilho de entrada ("when ... enters"). Também contam mágicas não-criatura de VM ≤ 2
  que olham o grimório e põem carta na mão, e qualquer carta com cycling por 1 mana.
  Ficam de fora: efeitos que custam {4} para ativar, Blood tokens e investigate.
- **Ramp barato:** carta não-terreno de VM ≤ 2 (que já não seja compra barata) cujo texto
  gera mana ("add "), busca terreno no grimório sem exigir sacrifício, encanta terreno
  para gerar mana extra, ou põe criatura da mão no campo. Criaturas que só geram mana ao
  morrer não contam.

Observação: os nomes das cartas-exemplo não vieram no texto extraído da página; a
classificação acima é a regra, não a lista.

#### 1.3 MDFCs e terrenos que contam como fração

| Carta | Conta como (para o **número de terrenos**) | Fonte |
|---|---|---|
| MDFC terreno/mágica não-mítica (terreno entra virado) | 0,38 terreno | Regressão [K1] |
| MDFC terreno/mágica mítica (terreno pode entrar desvirado) | 0,74 terreno | Regressão [K1] |

Exemplo do artigo: 21 terrenos puros + 4 MDFCs míticas + 4 não-míticas = 25,48 terrenos.

Regra prática anterior do mesmo autor (2020), que os dados confirmaram: não-mítica ≈
meio terreno, mítica ≈ três quartos [K4]. Na hora de **encaixar** MDFCs num deck pronto:
para cada 2 não-míticas, tirar 1 terreno e 1 mágica; para cada 4 míticas, tirar 3
terrenos e 1 mágica [K4].

Para contar MDFCs como **fonte de cor** os pesos são outros (ver 2.4).

#### 1.4 Ajustes

**Qualidade das mágicas baratas [K1].** O 0,28 é uma média. Se a compra/ramp do deck é
eficiente e confiável (cantrips de 1 mana que cavam fundo, mana rocks, busca de
terreno), cortar 1 terreno a cada 2–3 delas. Se é fraca ou frágil (cantrips de 2 manas,
mana dorks que morrem para remoção), cortar 1 a cada 4–5.

**Motivos para ficar acima da fórmula [K1].** No exemplo de Esper Midrange a fórmula dá
25,10 e a lista real usa 26,74. Razões apontadas: cartas que na prática gastam mais mana
do que o custo impresso (mana sinks, custos alternativos), exigência de cor alta por ser
tricolor, e terrenos utilitários que tornam o excesso de terrenos menos doloroso.

**Play/draw [K5, modelo de 2017 com mulligan Vancouver — histórico].** Quem compra
primeiro precisa de menos terrenos: no modelo, 3 terrenos no turno 3 com 90% e 4 no
turno 4 com 75% exigem 26 terrenos na play e só 23 na draw. Mesmo assim o autor
recomenda cortar no máximo 1 (às vezes 2) terrenos ao sideboardar na draw, porque cortar
mais aumenta mulligans e quem está na draw tende a ter uma carta a mais para gastar. Em
Limited vale o mesmo, conferindo antes se as fontes de cor continuam suficientes.

**Commander: mana rocks e o custo do comandante [K3].** Modelo de simulação separado
(otimiza mana gasta nos sete primeiros turnos). Conselho resultante: partir de
**42 terrenos + Sol Ring**, cortar 1 terreno a cada 2–3 mana rocks adicionais, 1 a cada
3–4 cantrips baratos e 1 a cada 3–4 mana dorks, e **não descer de 37** em decks midrange
de poder médio. Decks com menos de 38 terrenos e mais de 9 mana rocks provavelmente
melhoram trocando uma rock por um terreno.

Em 2024 Karsten resumiu a recomendação como **38–39 terrenos + cerca de 8 fontes
adicionais** (rocks, ramp, dorks), dizendo que é imprudente ir abaixo de 38 fora de
cEDH [K7].

**MTG Arena melhor-de-um [K4].** O algoritmo de suavização de mão inicial não é público;
Karsten declara não saber como ajustar a base de mana para ele. Não há número.

**Brawl.** Nenhum dos artigos lidos trata de Brawl especificamente. Para Brawl de 100
cartas, usar os números de 99 cartas como aproximação (a regra 103.4c citada em [K2] dá
mulligan grátis a qualquer jogo de Brawl). Para Standard Brawl (60 cartas com
comandante): **não verificado** — nenhuma fonte lida cobre.

#### 1.5 Resultados típicos

**Publicados pelos artigos:**

| Contexto | Terrenos | Fonte |
|---|---|---|
| 60 cartas, VMM 3 | 25 ou 26 | [K1] |
| 60 cartas, midrange em 2022 | 26 ("é o padrão agora") | [K3] |
| 60 cartas, aggro em 2022 | 24 ou 25 | [K3] |
| 60 cartas, modelo de curva ótima (2020) | 26 | [K3] citando o artigo de 2020 |
| 99 cartas, VMM 3 | 40 ou 41 | [K1] |
| 99 cartas, comandante de 2–3 manas (modelo) | 42 + Sol Ring | [K3] |
| 99 cartas, comandante de 4–5 manas (modelo) | 39 + Sol Ring + 7–8 rocks | [K3] |
| 99 cartas, comandante de 6 manas (modelo) | 38 + Sol Ring + 9 rocks | [K3] |
| 99 cartas, recomendação geral de 2024 | 38–39 + ~8 fontes extras | [K7] |
| 40 cartas, modelo de curva ótima (2020) | 17 | [K3] citando o artigo de 2020 |
| 40 cartas, land drops | 17 ("o padrão de sempre parece bom") | [K5] |
| Hipótese usada na tabela de fontes | 17 / 25 / 35 / 41 para 40 / 60 / 80 / 99 cartas | [K2] |

**Calculados aqui pelas fórmulas de 1.1** (sem mágicas baratas, sem companion no de 60):

| VMM | 60 cartas | 80 cartas (Yorion) | 99 cartas |
|---|---|---|---|
| 1,5 | 22,4 | 30,3 | 36,1 |
| 2,0 | 23,4 | 31,5 | 37,7 |
| 2,5 | 24,3 | 32,8 | 39,2 |
| 3,0 | 25,3 | 34,1 | 40,8 |
| 3,5 | 26,2 | 35,3 | 42,4 |
| 4,0 | 27,2 | 36,6 | 43,9 |

Subtrair 0,28 por mágica barata de compra/ramp (4 delas ≈ −1,1; 8 ≈ −2,2; 12 ≈ −3,4).

**40 cartas.** O artigo de 2022 não dá fórmula. O artigo de 2017 diz que multiplicar a
recomendação de 60 cartas por 40/60 chega perto [K5]. Aplicar essa escala à fórmula de
2022 é uma extrapolação nossa (calculado: `13,06 + 1,27 × VMM`, ou seja 16,2 com VMM
2,5; 16,9 com VMM 3,0; 17,5 com VMM 3,5). Usar apenas como conferência do padrão de 17.

#### 1.6 Exemplos de cálculo

Do artigo [K1]:

- **Boros Aggro**, VMM 2,2, sem baratas, sem companion:
  `19,59 + 1,90 × 2,2 = 23,77`. A lista real usa 23.
- **Esper Midrange**, VMM 2,9, sem baratas, sem companion:
  `19,59 + 1,90 × 2,9 = 25,10`. A lista real usa 26,74 (motivos em 1.4).

Ilustrativos (calculados aqui):

- **60 cartas, tempo azul**, VMM 2,6, com 8 cantrips de 1 mana:
  `19,59 + 1,90 × 2,6 − 0,28 × 8 = 22,29` → 22 terrenos.
- **Commander**, VMM 3,2, com 10 peças de ramp/compra de VM ≤ 2:
  `31,42 + 3,13 × 3,2 − 0,28 × 10 = 38,64` → 39 terrenos.
- **Commander com MDFCs**: se o alvo é 39 e o deck tem 3 MDFCs não-míticas
  (3 × 0,38 = 1,14), bastam 38 terrenos puros.

---

### 2. Quantas fontes por cor

#### 2.1 Tabela principal [K2]

Número mínimo de fontes de uma cor para conjurar a mágica "consistentemente" no turno
igual ao seu valor de mana. `C` = um símbolo de mana colorido qualquer; o número = mana
genérica. Ordenada da menos para a mais exigente (pela coluna de 60 cartas).

| Custo | Exemplo no artigo | 40 cartas | 60 cartas | 80 cartas | 99 cartas |
|---|---|---|---|---|---|
| 5C | Drowner of Hope | 6 | 9 | 12 | 14 |
| 4C | Doubling Season | 6 | 9 | 14 | 15 |
| 3C | Collected Company | 7 | 10 | 15 | 16 |
| 2C | Reckless Stormseeker | 8 | 12 | 16 | 18 |
| 5CC | Hullbreaker Horror | 8 | 12 | 17 | 20 |
| 1C | Ledger Shredder | 9 | 13 | 18 | 19 |
| 4CC | Primeval Titan | 9 | 13 | 19 | 22 |
| C | Monastery Swiftspear | 9 | 14 | 19 | 19 |
| 3CC | Baneslayer Angel | 10 | 15 | 20 | 23 |
| 4CCC | Nyxbloom Ancient | 10 | 16 | 22 | 26 |
| 2CC | Wrath of God | 11 | 16 | 23 | 26 |
| 3CCC | Massacre Wurm | 11 | 17 | 24 | 28 |
| 1CC | Narset, Parter of Veils | 12 | 18 | 25 | 28 |
| 2CCC | Garruk, Primal Hunter | 13 | 19 | 26 | 30 |
| CC | Lord of Atlantis | 14 | 21 | 28 | 30 |
| 1CCC | Cryptic Command | 14 | 21 | 29 | 33 |
| 1CCCC | Unnatural Growth | 15 | 22 | 31 | 36 |
| CCC | Goblin Chainwhirler | 16 | 23 | 32 | 36 |
| CCCC | Dawn Elemental | 17 | 24 | 34 | 39 |

A mesma tabela, vista por valor de mana e número de símbolos (60 cartas / 99 cartas):

| Valor de mana | 1 símbolo | 2 símbolos | 3 símbolos | 4 símbolos |
|---|---|---|---|---|
| 1 | 14 / 19 | — | — | — |
| 2 | 13 / 19 | 21 / 30 | — | — |
| 3 | 12 / 18 | 18 / 28 | 23 / 36 | — |
| 4 | 10 / 16 | 16 / 26 | 21 / 33 | 24 / 39 |
| 5 | 9 / 15 | 15 / 23 | 19 / 30 | 22 / 36 |
| 6 | 9 / 14 | 13 / 22 | 17 / 28 | não verificado |
| 7 | não verificado | 12 / 20 | 16 / 26 | não verificado |

("não verificado" = custo que não aparece na tabela-resumo do artigo. O artigo traz
ainda quatro imagens com a probabilidade para cada quantidade de fontes; elas **não
foram transcritas**.)

#### 2.2 Como ler

- **Probabilidade-alvo:** `89 + VM` por cento. Ou seja, 90% para mágicas de 1 mana, 91%
  para as de 2, 92% para as de 3, até 96% para as de 7. Quanto mais cara a carta, mais
  grave é não conseguir conjurá-la, por isso o alvo sobe.
- **Turno:** o turno igual ao valor de mana (conjurar "na curva"), jogando primeiro
  (on the play).
- **Probabilidade condicional:** é a chance de ter os símbolos coloridos **dado que**
  você já comprou terrenos suficientes para o custo. Falta de terreno é problema da
  seção 1, não desta.
- **Hipóteses do modelo:** 17 terrenos em 40 cartas, 25 em 60, 35 em 80 e 41 em 99;
  mulligan London com política fixa; em 99 cartas, mulligan grátis e compra no turno 1;
  só terrenos como fonte, sem seleção de cartas. Os números continuam bons como regra
  prática para decks próximos disso (60 cartas com 22 a 28 terrenos; até 4 cantrips ou
  dorks).
- **Como o agente usa:** para cada cor, achar a carta mais exigente daquela cor (incluir
  o sideboard), ler a linha correspondente e conferir se a base atinge o número. O
  requisito da cor é o **maior** entre as cartas, não a soma.
- **Mudança em relação a edições anteriores:** os números de 60 e 80 cartas subiram 1
  em vários custos (contagem de terrenos assumida maior); os de 99 cartas caíram, até 3
  ou 4 a menos para cartas de 1 e 2 manas, por causa do mulligan grátis e da compra
  extra. Tabelas antigas de Commander que circulam pela internet são mais altas.

#### 2.3 Decks com poucos ou muitos terrenos (60 cartas) [K2]

| Custo | 20 terrenos | 25 terrenos | 30 terrenos |
|---|---|---|---|
| 5C | 7 | 9 | 10 |
| 4C | 8 | 9 | 11 |
| 3C | 9 | 10 | 12 |
| 2C | 10 | 12 | 13 |
| 5CC | 10 | 12 | 15 |
| 1C | 11 | 13 | 14 |
| 4CC | 11 | 13 | 16 |
| C | 12 | 14 | 15 |
| 3CC | 12 | 15 | 17 |
| 4CCC | 12 | 16 | 19 |
| 2CC | 13 | 16 | 19 |
| 3CCC | 14 | 17 | 20 |
| 1CC | 15 | 18 | 21 |
| 2CCC | 15 | 19 | 22 |
| CC | 18 | 21 | 23 |
| 1CCC | 17 | 21 | 24 |
| 1CCCC | 18 | 22 | 26 |
| CCC | 19 | 23 | 27 |
| CCCC | 20 | 24 | 29 |

Interpolar entre colunas. Para esta escolha de coluna, cada 3–4 mágicas baratas de
compra/ramp valem 1 terreno. Atalho mental do autor para decks fora da faixa: pensar em
**fração dos terrenos** (por exemplo, 1CC pede cerca de 18/25 dos terrenos produzindo
a cor).

#### 2.4 Como contar fontes [K2]

Salvo indicação, os pesos vêm de [K2]. Somar frações e comparar com a tabela.

| Tipo de carta | Conta como | Observações |
|---|---|---|
| Terreno básico | 1 fonte da sua cor | |
| Dual, tri-land (shock, fast, check, Triome...) | 1 fonte de **cada** cor que produz | |
| Fetchland que busca duals com tipo básico | 1 fonte de cada cor que consegue buscar | |
| Fabled Passage, Pathways e similares (obrigam a escolher) | 1 fonte de cada cor em deck de 2 cores; **2/3** de cada cor em deck de 3+ cores com exigências altas em mais de uma | Em [K4] ele estima ~0,9 por Pathway em bicolor e arredonda para 1 |
| Terreno que entra virado | **Não conta para o turno 1.** Do turno 2 em diante conta inteiro | Vale enquanto o total de tap-lands for moderado (ver limites abaixo) |
| Verge lands (Duskmourn) | Cor principal: 1. Cor secundária: 3/4 com 8+ terrenos de tipo básico habilitador (60 cartas, ~24 terrenos); 1 com 12+ | [K6]; ver 4.3 |
| MDFC terreno/mágica não-mítica | 0,8 fonte da cor | Peso de **cor**, diferente do 0,38 usado na contagem de terrenos |
| MDFC terreno/mágica mítica | 1 fonte da cor | |
| Mana dork frágil (Llanowar Elves, Birds of Paradise, Noble Hierarch) | 1/2 fonte de cada cor que produz | Só para mágicas de VM ≥ 2, e só se o deck conjura o dork com consistência (14+ fontes verdes desviradas em 60 cartas) |
| Mana rock de 2 manas (Arcane Signet, Signets) | 3/4 de fonte de cada cor | Só para mágicas de VM ≥ 3 |
| Ramp de 2 manas que busca terreno (Farseek, Rampant Growth, Sakura-Tribe Elder) | 3/4 de fonte de cada cor que pode buscar | Só para VM ≥ 3; exige 13+ fontes verdes em 60 cartas |
| Ramp de 3 manas (Cultivate, Myriad Landscape) | 1/2 fonte de cada cor que pode buscar | Só para mágicas de VM ≥ 5 |
| Tesouro de gerador de 2 manas e uso único (Prosperous Innkeeper) | 1/4 de fonte de qualquer cor, por Tesouro | Só para VM ≥ 3 |
| Dockside Extortionist | 1/4 por Tesouro, estimando o X mais provável | |
| Exotic Orchard | 1 fonte da cor se souber que um oponente a joga; 3/4 de qualquer cor se não souber | Commander |
| Fellwar Stone | 3/4 da cor se souber; 1/2 de qualquer cor se não souber | Commander |
| Cantrip de VM ≤ 2 que compra carta | (fontes da cor ÷ tamanho do deck), arredondado para baixo | Ex.: 18 fontes em 60 → 18/60 ≈ 1/4. Só se o próprio cantrip é conjurável com consistência |
| Scry 1 barato | ~0,2 fonte (cor com 18 terrenos em 60, ou 30 em 99); ~0,1 (9 em 60, ou 15 em 99) | |
| Scry 2 barato | ~0,3 e ~0,15 nas mesmas condições | |
| Efeitos que contornam cor (ex.: Fires of Invention) | 0 | Construir a base para os jogos em que o plano não funciona |

Outros valores de referência do artigo, para cor com 18 terrenos em 60 cartas: Opt ≈
0,45; Serum Visions ou Omen of the Sea ≈ 0,55; Brainstorm ou Ponder ≈ 0,50; Mishra's
Bauble ≈ 0,25; um Temple (scry 1) ≈ 0,2 da cor que ele não produz. **Retorno
decrescente:** contar só os 10 primeiros efeitos de compra/seleção.

**Limite de terrenos virados (60 cartas):** no máximo ~3 em aggro com drops de 1 mana e
~9 em midrange/control sem drops de 1. Um tri-land que sempre entra virado conta 1; um
terreno condicional do tipo check land pode contar ~1/4; uma MDFC não-mítica conta 1/2
[K2, K4].

#### 2.5 Custos especiais [K2]

- **Cartas multicoloridas (ouro):** separar o custo por cor, olhar cada parte na tabela
  e **somar 1 a cada requisito**, incluindo o requisito combinado. Exemplo do artigo
  (60 cartas): uma carta 1WU pede 13 fontes brancas, 13 azuis e 19 fontes que produzam
  branco e/ou azul (12 + 1, 12 + 1, 18 + 1). O acréscimo só é necessário quando as duas
  cores são preocupação; um splash num deck em que todo terreno produz a cor principal
  equivale a um custo simples.
- **Híbrido:** somar as fontes de qualquer uma das duas cores.
- **Convoke, delve, X, redutores de custo:** modelar pelo número de terrenos que se
  espera virar de fato e ler essa linha.
- **Custo alternativo (evoke etc.):** se quase nunca é conjurada pelo custo normal,
  ignorar; se é com frequência, tratar pelo custo normal aceitando ficar um pouco abaixo.
- **Incolor específico e snow:** tratar como uma cor própria.
- **MDFC mágica/mágica:** satisfazer os dois custos.

#### 2.6 Exemplo de conferência (resumo do exemplo do artigo [K2])

Rakdos Midrange de 60 cartas, 24 terrenos + 1 MDFC:

- Mágicas pretas de 1 mana para o turno 1 → 14 fontes pretas **desviradas**.
- Carta de sideboard de custo 1BB → 18 fontes pretas (a mais exigente em preto).
- Planeswalker de custo 2RR → 16 fontes vermelhas (a mais exigente em vermelho).
- Cartas BR de 2 manas → 14 pretas, 14 vermelhas e 22 de qualquer das duas (com o +1).
- Um playset de carta que gera Tesouro/compra de forma condicional foi contado como ~1
  fonte de cada cor para mágicas de 4+, baixando o vermelho necessário para 15.
- A base real entrega 19 fontes pretas e 18 vermelhas, 14 de cada desviradas no turno 1:
  todos os requisitos atendidos, com folga para trocar um tap-land por um básico.

---

### 3. Regras práticas para o agente conferir uma base de mana

1. **Terrenos primeiro.** Calcular a fórmula de 1.1 com o VMM real e a contagem de
   baratas pela definição de 1.2. Diferença de mais de ~2 terrenos em relação ao
   resultado precisa de justificativa explícita (mana sinks, terrenos utilitários,
   muitas cores → para cima; compra/ramp excepcional → para baixo).
2. **Contar MDFCs como fração:** 0,38 (não-mítica) e 0,74 (mítica) no total de terrenos;
   0,8 e 1,0 como fonte de cor.
3. **Uma checagem por cor, pela carta mais exigente** (principal + sideboard), lendo a
   tabela 2.1 na coluna do tamanho do deck. Cartas de ouro: +1 em cada requisito.
4. **Drops de 1 mana pedem fontes desviradas:** 14 em 60 cartas, 9 em 40, 19 em 99.
   Terrenos que entram virados não contam para essa checagem.
5. **Custos CC no turno 2 e CCC no turno 3 são os mais caros da tabela** (21 e 23 fontes
   em 60 cartas). Em deck de duas ou mais cores, apontar essas cartas como risco antes
   de qualquer outra coisa.
6. **Fontes não-terreno valem fração e têm pré-requisito:** dork 1/2, rock 3/4, Tesouro
   1/4, ramp de 2 manas 3/4; só para mágicas mais caras que a própria fonte, e só se a
   fonte é conjurável com consistência.
7. **Limitar terrenos virados:** ~3 em aggro com drops de 1, ~9 em midrange/control
   (60 cartas). Acima disso, a simplificação "tap-land conta inteiro do turno 2 em
   diante" deixa de valer.
8. **Commander:** partir de 38–39 terrenos + ~8 fontes extras, ou 42 + Sol Ring se o
   deck quase não tem rocks; não descer de 37–38 em deck casual. Reduzir o número de
   cartas com o mesmo valor de mana do comandante. Usar a coluna de 99 cartas da 2.1,
   não uma escala da coluna de 60.
9. **Deck fora da faixa de terrenos** (60 cartas com menos de 22 ou mais de 28): usar a
   tabela 2.3 ou pensar em fração dos terrenos.
10. **Na dúvida entre um terreno e uma mágica, pôr o terreno.** Os campeões analisados
    em [K5] estavam acima da linha de regressão, e [K3] argumenta que flood custa menos
    que screw com os terrenos utilitários atuais.

---

### 4. Outras tabelas úteis

#### 4.1 Probabilidade de bater land drops — 60 cartas [K5]

**Histórico:** modelo de 2017, com o mulligan Vancouver (scry 1 após mulligan). Os
valores exatos mudariam um pouco com o mulligan London; servem como ordem de grandeza.
Cada célula: **draw / play**. "Flood" = 8+ terrenos comprados até o turno 7, na draw.

| Terrenos | 2 no turno 2 | 3 no turno 3 | 4 no turno 4 | 5 no turno 5 | Mão inicial média | Flood |
|---|---|---|---|---|---|---|
| 17 | 96,8% / 95,6% | 77,2% / 69,1% | 51,1% / 41,0% | 28,8% / 20,8% | 6,458 | 1,2% |
| 18 | 97,7% / 96,8% | 80,7% / 73,0% | 56,3% / 45,9% | 33,8% / 24,9% | 6,530 | 1,9% |
| 19 | 98,4% / 97,7% | 83,8% / 76,5% | 61,2% / 50,6% | 39,0% / 29,2% | 6,594 | 2,8% |
| 20 | 98,9% / 98,3% | 86,4% / 79,6% | 65,8% / 55,2% | 44,1% / 33,7% | 6,649 | 3,9% |
| 21 | 99,2% / 98,8% | 88,6% / 82,3% | 70,0% / 59,6% | 49,3% / 38,3% | 6,697 | 5,4% |
| 22 | 99,5% / 99,2% | 90,5% / 84,7% | 73,9% / 63,7% | 54,3% / 43,0% | 6,738 | 7,3% |
| 23 | 99,6% / 99,4% | 92,1% / 86,8% | 77,4% / 67,7% | 59,1% / 47,6% | 6,772 | 9,5% |
| 24 | 99,8% / 99,6% | 93,5% / 88,7% | 80,6% / 71,3% | 63,8% / 52,2% | 6,801 | 12,2% |
| 25 | 99,8% / 99,7% | 94,6% / 90,4% | 83,5% / 74,7% | 68,2% / 56,7% | 6,825 | 15,2% |
| 26 | 99,9% / 99,8% | 95,6% / 91,8% | 86,0% / 77,9% | 72,3% / 61,1% | 6,844 | 18,7% |
| 27 | 99,9% / 99,8% | 96,4% / 93,1% | 88,3% / 80,8% | 76,0% / 65,3% | 6,858 | 22,6% |
| 28 | 99,9% / 99,9% | 97,1% / 94,2% | 90,2% / 83,4% | 79,5% / 69,2% | 6,868 | 26,8% |

Política de mulligan do modelo: mulligan com 0, 1, 6 ou 7 terrenos em 7 cartas; com 0,
1, 5 ou 6 em 6 cartas; com 0 ou 5 em 5 cartas; mantém qualquer mão de 4.

Dado mais recente, já com mulligan London (play/draw sorteado, sem compra/scry): chance
de 4 terrenos no turno 4 em 60 cartas = 73,3% com 23 terrenos, 79,6% com 25 e 84,9% com
27 [K4]. Mostra retorno decrescente: +6,3 pontos nos dois primeiros terrenos extras,
+5,5 (texto do artigo; a diferença dos números é 5,3) nos dois seguintes.

#### 4.2 Probabilidade de bater land drops — 40 cartas [K5]

Mesmas ressalvas e mesmo formato (draw / play).

| Terrenos | 2 no turno 2 | 3 no turno 3 | 4 no turno 4 | 5 no turno 5 | Mão inicial média | Flood |
|---|---|---|---|---|---|---|
| 12 | 97,9% / 97,0% | 80,9% / 72,9% | 55,5% / 44,7% | 31,9% / 23,0% | 6,547 | 1,0% |
| 13 | 98,8% / 98,2% | 85,5% / 78,2% | 63,2% / 52,2% | 40,1% / 29,8% | 6,639 | 2,1% |
| 14 | 99,3% / 99,0% | 89,0% / 82,6% | 70,1% / 59,3% | 48,4% / 37,0% | 6,714 | 3,9% |
| 15 | 99,6% / 99,4% | 91,8% / 86,2% | 76,2% / 65,8% | 56,4% / 44,4% | 6,772 | 6,5% |
| 16 | 99,8% / 99,7% | 94,0% / 89,2% | 81,3% / 71,7% | 64,0% / 51,8% | 6,817 | 10,2% |
| 17 | 99,9% / 99,8% | 95,6% / 91,6% | 85,6% / 77,0% | 70,9% / 59,0% | 6,851 | 14,9% |
| 18 | 99,9% / 99,9% | 96,9% / 93,6% | 89,2% / 81,6% | 77,1% / 65,8% | 6,873 | 20,8% |
| 19 | 100% / 99,9% | 97,8% / 95,2% | 92,1% / 85,5% | 82,3% / 72,0% | 6,887 | 27,6% |
| 20 | 100% / 99,9% | 98,5% / 96,4% | 94,3% / 88,9% | 86,8% / 77,6% | 6,891 | 35,3% |

Para Commander o artigo não traz tabela; diz apenas que 25 terrenos em 60 equivalem a
cerca de 41,25 em 99 e que os números ficam próximos.

#### 4.3 Verge lands: chance de produzir a segunda cor [K6]

Deck de 60 cartas, 24 terrenos, 3 Verge lands, mulligan London, play/draw sorteado.
Probabilidade de já ter um terreno com o tipo básico habilitador, dado que comprou um
Verge. Aproximação válida para 20–28 terrenos e 2–4 Verges.

| Terrenos de tipo básico habilitador | Turno 2 | Turno 3 | Turno 4 |
|---|---|---|---|
| 4 | 45,0% | 49,6% | 53,8% |
| 5 | 53,1% | 58,0% | 62,5% |
| 6 | 60,3% | 65,3% | 69,7% |
| 7 | 66,5% | 71,5% | 75,7% |
| 8 | 71,9% | 76,7% | 80,6% |
| 9 | 76,6% | 81,1% | 84,7% |
| 10 | 80,7% | 84,8% | 88,1% |
| 11 | 84,2% | 87,9% | 90,8% |
| 12 | 87,2% | 90,5% | 92,9% |
| 13 | 89,8% | 92,6% | 94,7% |
| 14 | 91,9% | 94,3% | 96,1% |
| 15 | 93,7% | 95,8% (*) | 97,1% |
| 16 | 95,3% | 96,9% | 98,0% |
| 17 | 96,5% | 97,8% | 98,6% |
| 18 | 97,5% | 98,5% | 99,1% |

(*) A célula da tabela publicada mostra 98,5%, o que quebra a sequência; o texto do
mesmo artigo cita 95,8% para 15 terrenos no turno 3. Registrado o valor do texto.

Limiares para outros tamanhos (turno 3): 75% de consistência pede 8 terrenos
habilitadores em 60 cartas, 11 em 80 e 14 em 99; 90% pede 12, 17 e 21. Fetchlands
contam como habilitadores.

#### 4.4 Curvas de mana ótimas (modelo de simulação) [K3]

Modelo abstrato: cartas são só permanentes com um custo, sem cores; otimiza a mana
gasta acumulada nos sete primeiros turnos.

| Deck | 1 | 2 | 3 | 4 | 5 | 6 | Mana rocks | Terrenos |
|---|---|---|---|---|---|---|---|---|
| 40 cartas (Limited) | 2 | 7 | 7 | 4 | 3 | — | — | 17 |
| 60 cartas (Standard) | 3 | 10 | 10 | 7 | 4 | — | — | 26 |
| 99, comandante de 2 manas | 9 | 0 | 20 | 14 | 9 | 4 | Sol Ring + 0 | 42 |
| 99, comandante de 3 manas | 8 | 19 | 0 | 16 | 10 | 3 | Sol Ring + 0 | 42 |
| 99, comandante de 4 manas | 6 | 12 | 13 | 0 | 13 | 8 | Sol Ring + 7 | 39 |
| 99, comandante de 5 manas | 6 | 12 | 10 | 13 | 0 | 10 | Sol Ring + 8 | 39 |
| 99, comandante de 6 manas | 6 | 12 | 10 | 14 | 9 | 0 | Sol Ring + 9 | 38 |

Leitura: concentrar a curva em 2, 3 e 4; o zero na coluna do custo do comandante
significa "reduzir", não "proibir"; comandantes caros pedem mais rocks; desvios pequenos
custam quase nada (um deck vizinho ficou em 99,96% do ótimo), desvios grandes como
trocar 6 terrenos por 6 mágicas custam cerca de 2%.

#### 4.5 Probabilidade de comprar cópias de uma carta

Só foram encontrados valores pontuais (nenhuma tabela "N cópias × turno" foi lida):

| Situação (60 cartas) | Probabilidade | Fonte |
|---|---|---|
| Pelo menos 1 cópia de um 4-of até o turno 4, na play, sem mulligan | 52,8% (citado como 53% em [K7]) | [K4] |
| 2 ou mais cópias de um 4-of até o turno 4, mesmas condições | 12,6% | [K4] |
| Comprar o 3º terreno em duas compras após manter mão de 2 terrenos (24 terrenos restantes em 53 cartas, ou 15 em 33) | pouco mais de 70% | [K7] |

Demais combinações (1, 2 ou 3 cópias; outros turnos; 40 e 99 cartas): **não verificado**
em artigo de Karsten. São contas hipergeométricas que o código do projeto pode calcular
com exatidão em vez de depender de tabela.

---

### Pendências ("não verificado")

- Fórmula de número de terrenos específica para 40 cartas (não existe em [K1]).
- Custos fora da tabela-resumo de [K2] (6C, 6CC, CCCCC etc.) e as tabelas completas de
  probabilidade por quantidade de fontes (estão em imagens, não transcritas).
- Tabela de land drops para 99 cartas e versão com mulligan London das tabelas 4.1/4.2.
- Tabela geral de probabilidade de comprar N cópias até o turno T.
- Qualquer número específico para Brawl, Standard Brawl ou Arena melhor-de-um.
- Artigo de Karsten dedicado a mulligans: não localizado. As políticas de mulligan
  registradas aqui são as hipóteses dos modelos em [K2] e [K5].
- Os artigos de 2020 "How Many Lands Do You Need in a 60-Card Deck or 80-Card Deck?" e
  "What Is an Optimal Mana Curve for Decks With or Without Companions?" não foram lidos
  diretamente; os números de 2020 citados vêm do resumo que o próprio autor faz em [K3].

### Referências

Data de acesso de todas: **2026-10-04**. Os artigos do ChannelFireball hoje ficam
hospedados no TCGplayer; o corpo de cada um foi lido pela API de conteúdo do site
(`https://infinite-api.tcgplayer.com/c/article/<uuid>/`), que devolve o mesmo texto da
página.

- **[K1]** Frank Karsten, "How Many Lands Do You Need in Your Deck? An Updated
  Analysis". ChannelFireball / TCGplayer, 2022-07-29 (atualizado em 2025-02-13).
  <https://www.tcgplayer.com/content/article/How-Many-Lands-Do-You-Need-in-Your-Deck-An-Updated-Analysis/cd1c1a24-d439-4a8e-b369-b936edb0b38a/>
- **[K2]** Frank Karsten, "How Many Sources Do You Need to Consistently Cast Your
  Spells? A 2022 Update". ChannelFireball / TCGplayer, 2022-08-02 (atualizado em
  2025-02-13).
  <https://www.tcgplayer.com/content/article/How-Many-Sources-Do-You-Need-to-Consistently-Cast-Your-Spells-A-2022-Update/dc23a7d2-0a16-4c0b-ad36-586fcca03ad8/>
  — Cópia de apoio usada para os nomes de cartas (a tabela-resumo lá é só um link):
  <https://www.peasant-magic.com/articles/magic-deckbuilding/how-many-sources-do-you-need-to-consistently-cast-your-spells>
- **[K3]** Frank Karsten, "What's an Optimal Mana Curve and Land/Ramp Count for
  Commander?". ChannelFireball / TCGplayer, 2022-07-15 (atualizado em 2025-08-28).
  <https://www.tcgplayer.com/content/article/What-s-an-Optimal-Mana-Curve-and-Land-Ramp-Count-for-Commander/e22caad1-b04b-4f8a-951b-a41e9f08da14/>
- **[K4]** Frank Karsten, "Mana Bases with Zendikar Rising's Modal Double-Faced Cards".
  ChannelFireball / TCGplayer, 2020-09-16 (atualizado em 2025-02-13).
  <https://www.tcgplayer.com/content/article/Mana-Bases-with-Zendikar-Rising-s-Modal-Double-Faced-Cards/66175fdc-d033-4873-af99-3b8e61ac6a83/>
- **[K5]** Frank Karsten, "How Many Lands Do You Need to Consistently Hit Your Land
  Drops?". ChannelFireball, 2017-05-30. Lido em cópia PDF de terceiros (o original não
  foi localizado no ar):
  <https://orkerhulen.dk/onewebmedia/How%20Many%20Lands%20Do%20You%20Need%20to%20Consistently%20Hit%20Your%20Land%20Drops.pdf>
- **[K6]** Frank Karsten, "Building Mana Bases with Duskmourn's New Verge Lands".
  TCGplayer, 2024-10-18 (atualizado em 2025-02-13).
  <https://www.tcgplayer.com/content/article/Building-Mana-Bases-with-Duskmourn-s-New-Verge-Lands/02256252-047e-458a-92b3-bed999bd3364/>
- **[K7]** Frank Karsten, "Eight intriguing numbers in Magic: the Gathering". Ultimate
  Guard (blog), 2024-11-14.
  <https://ultimateguard.com/en/blog/eight-intriguing-numbers-in-magic-the-gathering-magic-the-gathering>

Código e dados do autor citados nos artigos (não consultados): repositório
`frankkarsten/MTG-Math` no GitHub e o conjunto de dados `frankkarsten/mtg-lands` no
Kaggle.
