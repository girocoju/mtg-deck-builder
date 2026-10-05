# Commander e Brawl

Referência para construir e ajustar decks singleton com comandante: Commander (papel e
MTGO, multiplayer) e Brawl / Standard Brawl (MTG Arena, um contra um). O agente consulta
este documento ao receber pedidos como "monte um deck de Brawl com o commander X", ao
estimar o nível de poder de uma lista e ao sugerir melhorias em um deck pré-construído.

**Confiabilidade:** as duas fontes deste documento são guias de divulgação (um blog de
plataforma de jogos e um blog de loja), não fontes oficiais nem estudos com dados. Regras
e listas de banidas descritas aqui devem ser tratadas como "segundo a fonte, em tal
data"; a legalidade de cada carta vem **sempre** da base local. O que foi conferido na
base está indicado. Para números de base de mana, a referência é
[base-de-mana.md](base-de-mana.md).

## 1. Os formatos e suas diferenças

| | Commander | Brawl (Arena) | Standard Brawl (Arena) |
| --- | --- | --- | --- |
| Tamanho | 100 cartas (comandante + 99) | 100 cartas | 60 cartas |
| Cartas permitidas | Quase todas as do jogo | Acervo do Arena | Só cartas legais em Standard |
| Mesa | Multiplayer (em geral 4) | Um contra um | Um contra um |
| Vida inicial | 40 | 25 [B] | não informado pela fonte |
| Chave na base | `commander` | `brawl` (e `competitivebrawl` para a ranqueada) | `standardbrawl` |

Regras comuns: cópia única de cada carta, exceto terrenos básicos; todas as cartas dentro
da identidade de cor do comandante.

Regras de Brawl segundo [B] (agosto de 2026):

- um comandante, ou dois com a habilidade partner;
- London mulligan com um mulligan gratuito;
- cada vez que o comandante é conjurado de novo, custa 2 a mais;
- podem ser comandantes: criaturas lendárias, planeswalkers, e veículos e espaçonaves
  lendários que tenham poder e resistência. A validade de um comandante específico deve
  ser conferida pelo validador (spec 003), não presumida.

**Como usar na construção.** O formato muda o deck mais do que o comandante:

- **Brawl joga como um duelo, não como Commander de mesa.** Com 25 de vida e um só
  oponente, decks agressivos são de fato fortes e as partidas são mais curtas. A curva
  deve ser mais baixa que a de um Commander de papel, e a remoção pontual vale mais que
  efeitos pensados para vários oponentes [B].
- **Commander multiplayer** dilui a agressão (são 120 pontos de vida de oponentes) e
  valoriza vantagem de cartas contínua, remoção em massa e política de mesa.
- Dados de sinergia vindos de Commander de papel (ex.: EDHREC) precisam ser filtrados por
  essa diferença: uma carta ótima em mesa de quatro pode ser lenta demais em Brawl.

## 2. Brawl no Arena: pareamento por peso e fila ranqueada

**O que é.** Segundo [B], o Arena atribui a cada deck de Brawl um "peso" a partir do
comandante e das cartas, e pareia decks de peso parecido. Existe também uma fila
ranqueada, mais rápida e competitiva, com lista de banidas própria.

**Como usar na construção.**

- Acrescentar cartas muito fortes a um deck casual não garante mais vitórias: leva o
  deck a enfrentar oponentes mais fortes. Ao montar um deck temático, vale manter o
  conjunto coerente em vez de enxertar meia dúzia de cartas de alto poder.
- Perguntar ao usuário se o deck é para a fila casual ou a ranqueada. Para a ranqueada,
  validar contra `competitivebrawl`.
- **Conferido na base (2026-10-04):** `competitivebrawl` tem 10 cartas banidas, e 7
  delas são legais em `brawl`: Ajani, Nacatl Pariah; Old Stickfingers; Ragavan, Nimble
  Pilferer; Rusko, Clockmaker; Tajic, Legion's Valor; Tamiyo, Inquisitive Student; Wrenn
  and Six. Ou seja, são comandantes ou cartas liberados no casual e proibidos na
  ranqueada. A fonte cita quatro delas; a base é a referência e deve ser reconsultada.

## 3. Roteiro de construção

Consolidação das recomendações de [B] e [T], na ordem em que o agente as aplica:

1. **Comece pelo comandante.** Ele define as cores e o plano de jogo inteiro. Antes de
   escolher qualquer carta, responda: o que o comandante faz, de que tipo de carta ele
   precisa, e como o deck vence com ele e sem ele.
2. **Curva conforme o formato.** Mais baixa em Brawl; em Commander, concentrada em
   custos 2 a 4 (ver curvas de referência em [base-de-mana.md](base-de-mana.md)).
3. **Terrenos e aceleração.** [B] recomenda 36 a 40 terrenos em Brawl de 100 cartas,
   conforme a curva, com aceleração para sustentar mágicas caras. Isso é compatível com
   os números de Karsten para 99 cartas (38–39 terrenos mais cerca de 8 fontes extras);
   na dúvida, prevalece o cálculo de [base-de-mana.md](base-de-mana.md).
4. **Interação.** Em Brawl, priorizar remoção pontual em boa quantidade [B]. Em
   Commander, somar ao menos uma remoção em massa confiável [T].
5. **Funções que todo deck precisa cobrir**, derivadas das perguntas de diagnóstico de
   [T]: mana suficiente, compra de cartas, remoção de permanentes problemáticas,
   proteção do comandante, plano B e condição de vitória clara. As quantidades-alvo
   estão na tabela abaixo.
6. **Singleton pede redundância por função**, não por cópia: ver a nota em
   [quantidade-de-copias.md](quantidade-de-copias.md).

### Proporções de referência para 100 cartas [S]

| Categoria | Quantidade | Observação |
| --- | --- | --- |
| Terrenos | 36–38 | Karsten recomenda 38–39 mais ~8 fontes extras; ver nota abaixo |
| Aceleração (ramp) | 8–12 | Pedras de mana, criaturas de mana, busca de terreno |
| Compra de cartas | 8–12 | Preferir motores contínuos a cantrips de uso único |
| Remoção pontual | 8–10 | De preferência em velocidade de instantânea; cobrir criaturas, artefatos e encantamentos |
| Remoção em massa | 2–4 | Para redefinir a mesa |
| Condições de vitória | 2–4 | Peças de finalização |
| Sinergia com o comandante | 25–30 | O que faz o deck ser "deste" comandante |

**Como usar na construção.**

- É o ponto de partida do agente para qualquer deck de 100 cartas: montar por categoria,
  conferir as contagens com `mtg deck analyze` (papéis) e justificar cada desvio.
- **Terrenos:** as duas fontes divergem. [S] dá 36–38; Karsten, com base em simulação,
  dá 38–39 mais cerca de 8 fontes extras, e a fórmula dele desce quando a curva é baixa
  e há muita compra/ramp barato. Prevalece o cálculo de [base-de-mana.md](base-de-mana.md);
  a faixa de [S] serve de conferência.
- **As categorias se sobrepõem:** uma carta de sinergia que também compra cartas conta
  nas duas. O total não precisa fechar em 100 por soma simples.
- **Desvios legítimos:** um comandante que já é motor de compra dispensa parte da compra;
  um deck de curva muito baixa precisa de menos aceleração; um deck que protege uma única
  ameaça troca remoção em massa por proteção.
- **Brawl (interpretação nossa, não da fonte):** a tabela foi escrita para Commander de
  mesa. Em Brawl, um contra um e com 25 de vida, faz sentido ficar no piso de remoção em
  massa (ou abaixo, em decks agressivos) e no teto de remoção pontual, com curva mais
  baixa. A confirmar com testes e registrar como lição.

Arquétipos que [B] apresenta como exemplos de planos de Brawl, úteis como vocabulário
(todos os comandantes abaixo foram conferidos na base como legais em `brawl`):

| Plano | Exemplo de comandante | Ideia |
| --- | --- | --- |
| Ramp para um comandante grande | Etali, Primal Conqueror | Aceleração para conjurar cedo um comandante que vence sozinho; simples de pilotar |
| Midrange com interação | Grenzo, Crooked Jailer | Remoção e descarte baratos mais geração de valor constante |
| Fichas e agressão | Ajani, Nacatl Pariah | Muitos corpos baratos e efeitos de reforço; termina o jogo rápido (banido na ranqueada) |
| Motor de sinergia | Sythis, Harvest's Hand | Um tipo de carta (encantamentos) que alimenta compra e mana |
| Partners agressivos | Tymna the Weaver + Bruse Tarl, Boorish Herder | Dois comandantes ampliam as cores; curva baixa com compra de cartas |

A fonte aponta como comandantes fortes na ranqueada, em agosto de 2026: Katara,
Waterbending Master; Nashi, Illusion Gadgeteer; Yuriko, the Tiger's Shadow. É dado de
metagame datado, não princípio.

## 4. Nível de poder: Brackets e Game Changers (Commander)

**O que é.** Um vocabulário de cinco faixas para os jogadores combinarem, antes da
partida, que tipo de jogo querem [T]:

| Bracket | Ideia geral |
| --- | --- |
| 1 – Exhibition | Decks muito casuais ou temáticos; vencer é secundário |
| 2 – Core | A vizinhança de muitos decks pré-construídos atuais |
| 3 – Upgraded | Decks ajustados, com algumas cartas de poder mais alto |
| 4 – Optimized | Commander altamente otimizado |
| 5 – cEDH | Competitivo, construído para vencer com a máxima eficiência |

Limites por bracket, segundo [K] (agosto de 2026):

| Bracket | Game Changers | Turnos extras | Combos infinitos de 2 cartas | Negação de terrenos em massa | Duração esperada |
| --- | --- | --- | --- | --- | --- |
| 1 – Exhibition | 0 | Não | Não | Não | 9+ turnos |
| 2 – Core | 0 | Poucos | Não | Não | 8+ turnos |
| 3 – Upgraded | Até 3 | Sim | Só os que não saem no começo do jogo | Não | 6+ turnos |
| 4 – Optimized | Sem limite | Sim | Sim | Sim | 4+ turnos |
| 5 – cEDH | Sem limite | Sim | Sim | Sim | Qualquer turno |

Tutores deixaram de ter restrição geral em outubro de 2025: só contam os que estão na
própria lista de Game Changers [K]. Os brackets são vocabulário para a conversa antes do
jogo, não uma regra aplicada por juiz.

**Game Changers** são cartas listadas oficialmente por mudarem o tipo de jogo (ex.:
Rhystic Study, Smothering Tithe, Cyclonic Rift). A base local marca essas cartas na
coluna `game_changer` (53 cartas em 2026-10-04, mesmo número que [K] informa):
`mtg sql "SELECT name FROM cards WHERE game_changer = 1 ORDER BY name"`.
**Sol Ring não é Game Changer** e é legal em todos os brackets (conferido na base e em
[K]; o material de apoio que indicou esta fonte dizia o contrário).

**Como usar na construção.**

- Perguntar ou propor o bracket alvo antes de montar um Commander, e declarar na entrega
  qual bracket a lista pretende e por quê. É uma estimativa explicada, não um cálculo.
- Contar os Game Changers da lista pela base e informar o número: nenhum para brackets
  1 e 2, até 3 para o bracket 3.
- Conferir também os outros critérios da tabela (turnos extras, combos de 2 cartas,
  negação de terrenos) lendo o texto das cartas; a base não os marca.
- O que desloca um deck para cima não é a quantidade de trocas, e sim o tipo [T]: mana
  rápida, tutores eficientes, interação gratuita poderosa, combinações que encerram o
  jogo e negação de recursos em massa. Evitar essas categorias quando o alvo é bracket
  baixo, mesmo que as cartas sejam legais.
- Um pré-construído não é automaticamente bracket 2: alguns trazem cartas mais fortes, e
  dez trocas já podem mudar a faixa [T].

## 5. Melhorar um deck existente ou pré-construído

**O que é.** O método de [T] para evoluir um deck: jogar antes de trocar, e trocar pelo
que o deck demonstrou precisar.

**Como usar.**

1. **Jogar várias partidas antes de mexer.** Uma carta que parece fraca pode cumprir uma
   função essencial no plano.
2. **Diagnosticar com sete perguntas:** fico sem cartas na mão? tenho mana suficiente?
   que cartas ficam mortas na mão? consigo remover permanentes problemáticas? meu
   comandante sobrevive? o que o deck faz quando o plano A falha? como ele de fato vence?
3. **Priorizar o que é estrutural**, não o que é vistoso: mana melhor, mais compra de
   cartas, remoção mais barata, uma remoção em massa confiável, mais proteção e alguns
   terrenos com sinergia costumam render mais que uma mítica cara. Conjurar as cartas
   fortes vale mais do que tê-las.
4. **Reavaliar o nível de poder** depois das trocas (seção 4).
5. **Preço não é qualidade:** um bom deck de Commander não depende de staples caras.

Quando o usuário pedir melhorias para uma lista, o agente faz as perguntas do passo 2
(ou as responde com a análise da spec 004) antes de sugerir trocas, e registra o que o
usuário relatar como lição em `licoes/`.

**Comprar pronto ou montar do zero [T]:** partir de um pré-construído faz sentido para
quem é novo no formato, gosta do tema e quer evoluir aos poucos; montar carta a carta,
para quem já sabe o comandante e a estratégia e aproveitaria poucas cartas do produto.

## 6. Produtos de Commander de 2026 (dado datado)

Lista de [T], publicada em setembro de 2026. Serve para reconhecer nomes que o usuário
citar; datas de lançamento conferidas com a tabela `sets` da base onde indicado.

| Lançamento | Decks | Data | Conferido na base |
| --- | --- | --- | --- |
| Lorwyn Eclipsed | Dance of the Elements, Blight Curse | 2026-01-23 | sim (`ecc`) |
| Teenage Mutant Ninja Turtles | Turtle Power! | 2026-03-06 | data da coleção `tmt` |
| Secrets of Strixhaven | Silverquill Influence, Prismari Artistry, Witherbloom Pestilence, Lorehold Spirit, Quandrix Unlimited | 2026-04-24 | sim (`soc`) |
| Marvel Super Heroes | Avengers Assemble, Wakanda Forever, The Fantastic Four, Doom Prevails | 2026-06-26 | sim (`msc`) |
| Reality Fracture | Multiverse Reforged (quatro cores) | 2026-10-02 | sim (`frc`) |
| Foundations Commander | Calling All Angels, Keen Engineering, Wretched Ranks, Reign of Dragons, Tramplesaurus Rex | 2026-10-02 | não localizado como coleção própria |

Os nomes dos decks e seus temas são da fonte; as listas de cartas de cada deck não foram
conferidas. As cartas dessas coleções estão na base e são consultáveis pelo código.

## Lacunas

- **Proporções específicas de Brawl** (um contra um, 25 de vida): a tabela de [S] é de
  Commander; a adaptação para Brawl é interpretação nossa, ainda sem fonte nem teste.
- **Proporções para Standard Brawl (60 cartas):** sem fonte.
- **Standard Brawl:** as fontes só o mencionam; vida inicial e particularidades não informadas.
- **Política de mesa e ameaça percebida em multiplayer:** não cobertas.
- **Fonte oficial dos Brackets:** os limites vêm de um guia de terceiros [K], não do
  anúncio da Wizards.

## Referências

Data de acesso: 2026-10-04.

- **[B]** BlueStacks Content Team, "Magic The Gathering Arena Brawl Decks Guide".
  BlueStacks (blog), 2026-08-27.
  <https://www.bluestacks.com/blog/game-guides/magic-the-gathering-arena/mtga-best-brawl-decks-en.html>
  — Usado nas seções 1, 2 e 3. Lido por extração automática da página; cartas-chave de
  cada deck não foram transcritas.
- **[T]** Tistaminis, "MTG Commander Decks 2026: New Releases & Best Picks". Tistaminis
  (blog de loja), setembro de 2026.
  <https://tistaminis.com/blogs/blog/mtg-commander-decks-2026-new-releases-best-picks>
  — Usado nas seções 3, 4, 5 e 6. Texto de caráter comercial; as partes sobre mercado,
  colecionismo e lojas ficaram fora do escopo.
- **[S]** Dan A., "Commander Deck Building Guide". Spellweave, atualizado em abril de 2026.
  <https://spellweave.app/guides/commander-deck-building>
  — Usado na tabela de proporções da seção 3. Indicado pelo usuário; números conferidos
  na página.
- **[K]** Kraken The Meta, "MTG Commander Brackets Guide". 2026-08-08.
  <https://krakenthemeta.com/blog/mtg-commander-brackets/>
  — Usado na seção 4. Indicado pelo usuário; limites conferidos na página.
- Números de terrenos e curva: [base-de-mana.md](base-de-mana.md) (Frank Karsten).
