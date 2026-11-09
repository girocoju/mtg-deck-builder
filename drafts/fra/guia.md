# Reality Fracture (FRA) — guia de draft

- **Dados:** 17Lands, coletados em 2026-10-12. Modo de referência: **Premier Draft**
  (433.815 jogos; win rate médio dos usuários do 17Lands: 54,8%). Snapshot anterior do
  guia: 2026-10-05 (220.847 jogos); as diferenças relevantes estão anotadas.
- **Fontes complementares:** Untapped.gg (Premier Draft, ranks bronze a platina,
  coletado em 2026-10-12; média ponderada dos usuários 52,2%) e cinco guias externos
  indicados pelo usuário, confrontados com os dados na seção "O que dizem os guias
  externos". Registro em `knowledge/fontes.md`, seção 6.
- **Como ler os números:** GIH WR é o win rate dos jogos em que a carta esteve na mão.
  Compare sempre com os 54,8% da média do 17Lands: uma carta de 57% é boa, uma de 53% é
  fraca. Números do Untapped se comparam aos 52,2% da média dele, não aos do 17Lands.
  ALSA é o pick médio em que a carta ainda aparece no pacote (quanto maior, mais tarde sai).
- **Atenção à amostra:** a coleção saiu no Arena em 2026-09-29. As comuns têm de 1.000 a
  6.800 jogos em mão e os rankings delas são confiáveis até a casa de 1 ponto. Raras e
  míticas têm de 500 a 1.100; para várias míticas o 17Lands ainda não publica GIH WR, e
  o guia usa o Untapped como apoio.
- **Regerar:** `mtg draft update fra --mode all --force` e os comandos citados em cada seção.

## Visão geral

| O que | Leitura |
| --- | --- |
| Mecânica central | **Empower Jace N** (35 cartas): põe N contadores de lealdade em uma ficha de Jace que você controla; se não houver, cria a ficha, um planeswalker azul com "−1: Surveil 1" e "−3: compre uma carta". É vantagem de cartas embutida em cartas comuns |
| Outras mecânicas | **Surveil** (43 cartas, sobretudo azul e branco); **prepared** (24 cartas: criaturas que entram "preparadas" e permitem conjurar uma cópia da mágica associada; cada par aliado tem a sua: Peer Review em WU, Omit Variables em UB, Vicious Verse em BR, Seed Suture em GW, Soul Tether em RG); **fichas Heartwood** (artefato que gera R ou G); ciclos de terrenos Annex e Commons, que entram desvirados se você controla um planeswalker (a ficha de Jace conta) |
| Velocidade | Formato de valor, não de corrida, e **lento**: o guia da Draftsim, após uma semana de drafts, descreve as partidas mais longas das coleções recentes, decididas por quem acumula mais recursos. A leitura só das cartas (LimitedMTG: custo médio 3,2 e 68% das mágicas custando até 3) sugeria velocidade usual; prevalece o que as partidas mostram |
| Cor mais forte | **Azul**, com folga: cinco comuns entre 56,6% e 60,6% e seis incomuns acima de 57% |
| Cores mais fracas | **Vermelho e verde nas comuns**, próximos entre si (melhor criatura comum de cada: 55,4% e 56,6%); o vermelho vale pela remoção, o verde pelos cyclers e por Something Worth Saving |
| Remoção | Concentrada em preto e vermelho; branco tem remoção condicional; azul tem Unsummon, anulação e a aura Infinite Coursework |
| Correção de mana | Acima da média: dez terrenos duplos comuns, Murmuring Volume (comum, mana de qualquer cor), cinco comuns caros com basic landcycling e as fichas Heartwood. Splash é parte do formato (ver "Construção") |

Remoção em comuns e incomuns, pela leitura da base (`mtg draft set fra`; a classificação é
automática e inclui algumas criaturas com efeito de remoção): branco 5, azul 3, preto 5,
vermelho 7, verde 3, multicoloridas 8. A contagem do LimitedMTG, feita a partir do texto
de cada carta em todas as raridades: 61 remoções (branco 7, azul 5, preto 14, vermelho 11,
verde 5, multicoloridas e incolores 19), 15 delas comuns e 22 em velocidade de instantânea;
3 de dano matam 68% das criaturas da coleção e 32% têm resistência 4 ou mais, iguais à
média de nove coleções recentes.

## Os dez pares de cores

Win rate do par em Premier Draft e as cartas que sinalizam o arquétipo
(`mtg draft colors fra`, `mtg draft cards fra --color multi --limit 40`, `mtg draft rate`).
As duas últimas colunas vêm das fontes complementares: a posição no tier list da Draftsim
(2026-10-09) e a parcela dos jogos de Premier Draft do Untapped em que o deck era desse par.

| Par | Win rate | Jogos | Sinalizadoras (GIH WR) | Plano | Draftsim | Untapped |
| --- | --- | --- | --- | --- | --- | --- |
| WU (Fatehold) | **56,6%** | 52.639 | Fatehold Charm 57,1%; Fatehold Chronologist (comum) 55,1%; Desperate Futurescribe 55,0%; Prudent Fateseer 54,3% | Tempo: voadores baratos, bounce e surveil. Vence pela qualidade das comuns azuis e brancas, não pelas sinalizadoras, que estão na média. O par que menos precisa de splash | 1º | 11,7% |
| UB (Theorix) | **56,1%** | 61.505 | Recursive Recruitment 60,9%; Theorix Charm 58,4%; Null Summoner (rara) 63,1%; Paradox Shaper 54,6% | Controle de cemitério: remoção preta, compra azul e threshold (sete cartas no cemitério). Não há hate de cemitério no formato. O par mais jogado | 2º | 10,2% |
| BG | 55,5% | 30.136 | Hapatra, the Desert Fang 60,0%; Primal Witchstalker 59,3%; Vraska, the Cutting Glare (rara) 63,0% | Pilha de boas cartas com splash: criaturas de valor, remoção e recursão leve de cemitério | 3º | 5,3% |
| RG (Konstrari) | 55,4% | 43.859 | Craftwork Crusher 62,5%; Heartwood Crafter 56,6%; Konstrari Charm 55,9%; Konstrari Improviser (comum) 54,4% | Rampa com fichas Heartwood para criaturas grandes. Muito disputado para o que rende | 4º | 10,1% |
| UR | 55,3% | 35.440 | Clash of Elements 59,5%; Twinned Vision (comum) 58,2%; Saheeli, Jewel of Avishkar 56,7% | Mágicas: controle com veia de tempo, prowess e cantrips | 5º | 6,6% |
| GW (Vigorbloom) | 54,1% | 39.324 | Bloombrute 59,6%; Vigorbloom Vanguard 57,5% | Ganho de vida vira contadores e cartas; midrange que sofre contra remoção em quantidade | 6º | 10,1% |
| BR (Stingerquill) | 53,7% | 28.921 | Grim Repriser 60,6% (731 jogos); Stingerquill Charm 55,9%; Stingerquill Voxmancer 51,7% | Dano não combate; poucos enablers e muito ganho de vida no formato | 8º | 7,4% |
| WB | 53,4% | 17.299 | Twisted Fates 59,4%; Winter, Tormented Loner 50,8%; Edgar, Ancient Bloodlord sem amostra (330 jogos) | Sacrifício no papel; na prática, remoção preta com corpos brancos | 10º | 3,8% |
| RW | 53,4% | 18.033 | Warrior's Blades 54,7%; Mabel, Valley Hero 51,6% | Aggro com contadores +1/+1; o tema tem poucos payoffs e o formato não favorece atacar | 9º | 3,9% |
| GU | 52,9% | 18.540 | Mind Meanderer 56,8%; Kiora of Salt and Sand 53,9% | Empower Jace grande, com muito splash; o par com menos remoção | 7º | 2,6% |

Leitura: os cinco melhores pares têm azul ou preto; os quatro piores não têm azul, ou o
combinam com verde. Entre o melhor e o pior par há 3,7 pontos. A ordem dos dados e a do
tier list da Draftsim coincidem nos seis primeiros e nos quatro últimos (a Draftsim só
troca GU, BR, RW e WB entre si). No Untapped, cerca de 28% dos jogos foram de decks com
uma só cor ou com três ou mais (calculado): os quatro trios mais comuns, WUB, BRG, WRG e
UBG, têm de 3,2% a 3,8% cada, parcela igual à de WB ou RW.

## Ranking de comuns e incomuns por cor

GIH WR em Premier Draft (`mtg draft cards fra --color U --rarity common`).

### Azul — a cor a disputar

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Mindseeker Oculus | 60,6% | 3,0 | Plan for All Outcomes | 60,4% | 2,8 |
| Protege's Awakening | 58,0% | 4,7 | Fblthp, Impossibly Lost | 60,0% | 3,8 |
| Icy Reception | 57,9% | 4,9 | Countersculpt | 59,7% | 3,5 |
| Unsummon | 57,1% | 5,0 | Way of the Mind Sculptor | 58,3% | 2,9 |
| Surveillance Phantasm | 56,6% | 4,6 | Proft, Consulting Detective | 57,6% | 3,5 |
| Undulating Witness | 56,5% | 4,9 | Geist of Saint Thalia | 57,4% | 4,0 |
| Divining Duelist | 56,2% | 6,9 | | | |
| Infinite Coursework | 55,1% | 4,2 | | | |
| Sphinx's Approach | 55,0% | 7,0 | | | |

Até as piores comuns azuis ficam perto da média (Cryotheory Adept 52,7%). **Sphinx's
Approach caiu de 62,9% para 55,0%** entre os dois snapshots: a amostra de 1.032 jogos e o
viés de múltiplas cópias, apontados no guia anterior, inflavam o número. Uma cópia isolada
é "compre duas cartas" por três manas.

### Preto — a melhor remoção

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Extended Absence | 60,2% | 3,0 | Break Under Pressure | 61,1% | 2,8 |
| Last Gasp | 56,8% | 3,6 | Rewrite Regrets | 58,7% | 3,6 |
| Apex Witchstalker | 56,6% | 5,1 | Multiply by Zero | 58,2% | 2,5 |
| Screeching Soulbreaker | 56,6% | 6,4 | Gallia, Tragic Host | 57,0% | 4,9 |
| Cast Away Doubt | 55,9% | 7,1 | Tinybones, Pocket Nuisance | 55,9% | 4,9 |
| Theoretical Necromancer | 55,5% | 6,3 | | | |
| Rank Rat | 54,8% | 6,0 | | | |

Piores comuns: Void Extrapolator 54,3%, Silence the Echo 52,4%, Solve for Disappointment
52,9%. Screeching Soulbreaker subiu (53,7% no snapshot anterior); segundo a Draftsim, ela
só rende em BR e em decks pretos com ganho de vida.

### Branco

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Hexhaven Battalion | 58,4% | 4,2 | Teyo, Lightshield Expert | 60,0% | 4,2 |
| Surgical Precision | 57,7% | 4,3 | Generous Revival | 59,3% | 4,4 |
| Blossom-Blessed Angel | 56,9% | 5,0 | Your Fate Ends Here | 58,3% | 3,0 |
| Memory Trap | 55,5% | 3,3 | Way of the Healer | 57,5% | 3,3 |
| Campus Crier | 55,4% | 5,5 | Prophesied End | 55,0% | 3,1 |
| Shatterwing Pegasus | 55,2% | 6,8 | Thalia, the Survivor | 54,9% | 4,4 |

Piores comuns: Unflinching Hortimancer 53,6%, Graft Surgeon 53,1%, Fateshaper Aspirant
52,5%; Predictive Preparations não tem amostra (289 jogos) e a Draftsim a descreve como
decepção. Memory Trap sai cedo (ALSA 3,3) e rende menos que Battalion e Precision.

### Vermelho

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| No Admittance | 56,9% | 3,4 | Kiora of Fire and Ashes | 59,2% | 2,2 |
| Wrath of the Bloodmane | 55,4% | 4,0 | Violent Echoes | 57,7% | 2,8 |
| Awaken the Inferno | 55,2% | 4,5 | Fulminous Forte | 57,4% | 3,0 |
| Heartstring Puller | 55,1% | 6,3 | Marwyn, the Clearcutter | 56,6% | 6,0 |
| | | | Pia, Determined Rebuilder | 56,5% | 4,4 |

As três melhores comuns são remoção; as criaturas comuns vermelhas estão todas na média ou
abaixo (Chandra's Emberling 52,6%, Skilled Battlecarver 52,3%, Hallway Heckler 51,6%,
Tether Technician 51,2%). Way of the Pyromancer rende 48,9% e sai no pick 4,4.

### Verde

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Something Worth Saving | 57,9% | 6,8 | Fblthp, Knows the Way | 58,5% | 3,9 |
| Vinelasher Adept | 56,6% | 5,4 | Way of the Paradox | 58,0% | 4,6 |
| Arcane Amphisbaena | 55,7% | 4,4 | Heartwood Crafter | 56,6% | 3,5 |
| Bestial Incursion | 55,1% | 4,8 | Jiang Yanggu, Never Alone | 55,0% | 4,2 |
| Wrecking Gecko | 54,2% | 6,6 | Marwyn, the Preserver | 54,8% | 5,5 |
| Compel Brutality | 53,8% | 4,3 | Ruric Thar, Magecrusher | 54,2% | 4,1 |

Piores comuns: Greenhouse Propagator 52,7%, Budding Insurgent 51,9%, Inspired Tethermage
51,5%. Compel Brutality caiu de 55,0% para 53,8%: remoção que depende de criatura perde
para a remoção em instantânea do formato (ver dicas de jogo).

### Incolores e terrenos

Meticulous Commons 58,3%, Innovative Commons 57,2%, Keeper of the Quiet Hour 57,1%,
Murmuring Volume 56,8% (pedra de mana de qualquer cor), Theorix Annex 56,7%, Room of Refuge
55,4%, Medic's Kitesail 55,4%. Os terrenos refletem em parte a força do par que os usa.

## Bombas

GIH WR com 500 jogos ou mais: Ajani Unrelenting 71,8%; Uldaros Theorix 69,9%; The
Theorist, Jace Beleren 66,8%; Sphinx of False Conclusions (rara) 63,8%; Sanctum Lurker
(rara) 63,4%; Lich's Relic (rara) 63,1%; Null Summoner (rara) 63,1%; Vraska, the Cutting
Glare (rara) 63,0%; Gideon the Oathless (rara) 62,2%; Simulacrum Shaper (rara) 61,8%;
Kindred Judgment (rara) 61,6%; Hungering Puppetbeast (rara) 61,4%. Garruk, Veiled Butcher,
Garruk, Curse Breaker e Overwrite the Multiverse ficaram abaixo do corte de amostra do
17Lands neste snapshot; no Untapped rendem 64,8%, 63,4% e 63,9% em mão (8 mil jogos cada,
contra a média de 52,2%), o que os confirma como bombas.

Entre as incomuns, jogam como raras: Craftwork Crusher 62,5%, Break Under Pressure 61,1%,
Recursive Recruitment 60,9%, Grim Repriser 60,6% (731 jogos), Plan for All Outcomes 60,4%,
Fblthp, Impossibly Lost 60,0%, Hapatra, the Desert Fang 60,0%, Teyo, Lightshield Expert
60,0%. Duas comuns ficam no mesmo patamar: Mindseeker Oculus 60,6% e Extended Absence 60,2%.

## Prioridade de picks e sinais

1. **Bombas e incomuns de 60% ou mais**, em qualquer cor: a correção do formato permite
   fazer splash delas (ver "Construção").
2. **Remoção preta e as melhores comuns azuis:** Extended Absence, Mindseeker Oculus,
   Break Under Pressure, Multiply by Zero, Countersculpt, Plan for All Outcomes.
3. **Empower Jace barato e os "Way of" bons** (Mindseeker Oculus, Protege's Awakening,
   Way of the Mind Sculptor, Way of the Paradox, Way of the Healer): a ficha de Jace rende
   cartas e liga os terrenos Annex e Commons.
4. **Correção comum que rende por si:** Murmuring Volume, os terrenos duplos do seu par,
   os cyclers (Awaken the Inferno, Vinelasher Adept) e Something Worth Saving.
5. **Sinalizadoras do par** (tabela dos pares), para confirmar a segunda cor.
6. Criaturas de curva e truques, por último: o formato tem poucas comuns boas de custo 2.

Sinais (`knowledge/limitado-e-draft.md`, seção de sinais): Mindseeker Oculus e Extended
Absence saem em média no pick 3,0; Break Under Pressure no 2,8; Multiply by Zero no 2,5.
Ver uma delas depois do pick 6 indica que a cor está livre à direita. Azul é a cor que
todos querem (WU e UB são os pares mais jogados nas duas fontes); se as comuns azuis de 57%
ou mais não aparecem até o pick 5 ou 6, a cor está sendo cortada. Preto é o melhor plano B,
pela remoção; verde chega mais aberto (Something Worth Saving sai no pick 6,8 rendendo 57,9%).

## Armadilhas: dados contra impressão

`mtg draft gaps fra` compara o ranking de GIH WR com o de ALSA.

**Subestimadas (rendem e saem tarde):** Grim Repriser (60,6%, ALSA 6,6, só 731 jogos);
Meticulous Commons (58,3%, ALSA 6,7) e Innovative Commons (57,2%, ALSA 6,3); Something
Worth Saving (57,9%, ALSA 6,8); Keeper of the Quiet Hour (57,1%, ALSA 6,3); Clash of
Elements (59,5%, ALSA 5,3); Divining Duelist (56,2%, ALSA 6,9); Cast Away Doubt (55,9%,
ALSA 7,1).

**Superestimadas (saem cedo e rendem pouco):** Woodwork Prodigy (50,8%, ALSA 3,7); Way of
the Wildspeaker (52,3%, ALSA 3,4); Way of the Pyromancer (48,9%, ALSA 4,4); Ghalta the
Unstoppable (50,6%, ALSA 4,2); Yoshimaru, Scrappy Stray (51,1%, ALSA 4,2); Ruric Thar,
Biomagus (53,1%, ALSA 3,7); Loot, the Nexus (50,4%, ALSA 4,6); Edgar, Moonlit Sovereign
(47,8%, ALSA 4,9). Memory Trap (55,5%, ALSA 3,3) e Prophesied End (55,0%, ALSA 3,1) são
remoções brancas que saem cedo e rendem só um pouco acima da média.

**Mudanças entre snapshots** que mostram o peso da amostra: Sphinx's Approach de 62,9% para
55,0%; Living Library de 58,7% (545 jogos) para sem amostra; Yoshimaru, Beloved Companion
segue a pior incomum com números (51,4%).

## O que dizem os guias externos

Cinco páginas indicadas pelo usuário em 2026-10-12, lidas por inteiro e confrontadas com
os dados. Hierarquia adotada quando divergem: partidas (17Lands, Untapped) > relato de
jogador com dados (Draftsim) > leitura das cartas (LimitedMTG) > pré-lançamento (PreconForge).

| Fonte | O que é | Data | Vale para |
| --- | --- | --- | --- |
| Draftsim, "The Ultimate Guide to Reality Fracture Draft" (Bryan Hohns, Veveil) | Relato de uma semana de drafts no Arena, com dados do 17Lands | 2026-10-09 | Arquétipos, splash, comuns, dicas de jogo |
| Untapped.gg, guia de FRA (Premier Draft) | Dados de partidas por carta e por combinação de cores, ranks bronze a platina | coletado em 2026-10-12 | Checagem dos rankings e popularidade dos pares |
| Draftsim, simulador e pick order de FRA | Notas de 0 a 5 por carta, sem data nem método na página | sem data | Só como contraste: destoa dos dados |
| LimitedMTG, guia de FRA | Gerado a partir do arquivo de cartas, sem partidas | outubro de 2026 | Contagens de remoção, curva e correção |
| PreconForge, guia de draft e sealed | Pré-lançamento, sem dados; texto comercial | 2026-09-22 | Princípios de sealed e de enabler/payoff |

### Como o formato joga (Draftsim)

- **Vantagem de cartas e bombas decidem.** Jogos longos; quem para de gerar recursos
  perde. Compra de cartas com empower Jace, flashback de Twinned Vision e mana sinks
  (Shatterwing Pegasus, Tenured Tethermage) valem mais do que em coleções normais.
- **Ganho de vida é abundante** fora de GW, o que alonga as partidas e enfraquece os
  planos agressivos (BR, RW).
- **Prepared pesa pouco.** As mágicas das criaturas preparadas são efeitos pequenos e
  pontuais; servem para as sinergias do par, não como razão de pick.
- **Heartwood serve de splash.** As fichas geram R ou G: Konstrari Improviser permite
  conjurar Craftwork Crusher fora de RG. Todos os geradores, menos Tenured Tethermage,
  criam a ficha desvirada, o que permite duas jogadas no mesmo turno.
- **Quase nunca duas cores.** O autor relata não ter terminado nenhum draft em duas cores
  puras e diz ter errado ao subestimar o splash no guia de sealed. A correção (cyclers,
  Murmuring Volume, terrenos duplos) é bem acima da média de coleções recentes. Splash
  também por sinergia, não só por poder (Generous Revival com Proft, Sinister Mastermind;
  Bloombrute com Screeching Soulbreaker). O Untapped confirma a parcela de decks com três
  ou mais cores (tabela dos pares).
- **A pilha de boas cartas é o décimo primeiro arquétipo**, que costuma emprestar um ou
  dois temas dos pares.

### Os dez pares, segundo a Draftsim, e o que os dados dizem

Payoffs e enablers citados pelo autor (nomes conferidos na base), com a nossa leitura.

- **WU Surveil (1º na Draftsim; 1º nos dados).** Deck de tempo: criaturas baratas, bounce
  e dano incremental. Payoffs: Denzilore Fatehold (mítica), Proft, Consulting Detective,
  Saheeli, Consul of Oversight, Diviner of Victory, Desperate Futurescribe, Prudent
  Fateseer; a única comum que premia surveil é Surveillance Phantasm. Enablers: toda
  carta com empower Jace (a ficha faz surveil), Fatehold Chronologist, Semester Foreseer,
  Way of the Healer. Dica: proteger uma ficha de Jace de pouca lealdade para um surveil
  imediato; os primeiros seis terrenos importam (duas mágicas de custo 3 por turno), depois
  descartar terrenos com surveil. Nos dados, as sinalizadoras de WU estão na média
  (54% a 57%): o par vence pelas comuns e incomuns monocoloridas.
- **UB Self-mill (2º; 2º).** Beneficia-se da ausência de hate de cemitério (Afterthought
  Sentry é a única carta que impede o flashback de Recursive Recruitment). Payoffs:
  Recursive Recruitment, Gallia, Tragic Host, Proft, Sinister Mastermind, Rewrite Regrets,
  Theoretical Necromancer, Null Summoner, Uldaros Theorix, Blessed Ghoul, Twinned Vision,
  Fblthp, Impossibly Lost (condição de vitória em self-mill). Enabler-chave: Paradox
  Shaper, que recicla mágicas e evita o deck-out. Nos dados, Paradox Shaper rende 54,6% e
  Theorix Metamage 54,1%: os enablers são medianos, os payoffs é que carregam o par.
- **BG Graveyard (3º; 3º).** Pilha de boas cartas que faz splash dos melhores cards de
  outras cores e pega toda Recursive Recruitment que vê. Hapatra, the Desert Fang e
  Vraska, the Cutting Glare precisam de pouco apoio. Primal Witchstalker com Something
  Worth Saving garante os terrenos. Ferocity of the Hunt é bom truque com criaturas de
  efeito ao entrar. Nos dados, é o terceiro par e o terceiro menos jogado dos seis
  melhores: boa relação entre força e disputa.
- **RG Ramp (4º; 4º).** Craftwork Crusher e Kiora of Fire and Ashes bastam para entrar no
  par; Aerid Konstrari (mítica) é condição de vitória e valor ao mesmo tempo. Enablers:
  Heartwood Crafter (Floresta no turno 1 e Crafter no 2 é a melhor abertura do formato,
  segundo o autor), Konstrari Improviser, Woodwork Prodigy (lento). Completar com
  defensores (Arcane Amphisbaena, Pia, Determined Rebuilder) e remoção vermelha.
  Konstrari Charm é fraco em RG, que joga atrás enquanto monta as fichas. Nos dados,
  Woodwork Prodigy rende 50,8% e sai cedo (ALSA 3,7): a pior armadilha do par.
- **UR Spells (5º; 5º).** Controle com veia de tempo; Clash of Elements, Saheeli, Jewel of
  Avishkar e as bombas azuis e vermelhas são as razões de estar no par. Unsummon é a
  mágica típica (salva criatura, anula truque, ganha tempo); Twinned Vision é cantrip,
  vantagem de cartas e fonte de terrenos. Não ponha ficha no topo contra Clash of Elements.
- **GW Lifegain (6º; 6º).** Loop simples: payoffs Kwia Vigorbloom, Ajani Resolute,
  Enlightened Confidant, Lyra, Archangel of Dawn, Bloombrute, Titanbones, Towering Heart,
  Unflinching Hortimancer; enablers repetíveis Blessed Ghoul, Medic's Kitesail (um ou dois
  exemplares, inevitabilidade contra decks de remoção), Koth of the Homestead, Liliana the
  Faultless, Greenhouse Propagator. Sofre contra remoção e vantagem de cartas; o autor
  costuma fazer splash de preto (Extended Absence, Sanctum Lurker) para mais gatilhos.
- **GU Empower (7º; 10º nos dados).** Deck que "não faz nada" e faz splash de tudo; Mind
  Meanderer e Kiora of Salt and Sand são as incomuns boas, as raras do par são fracas. Ordem
  dos "Way of" para splash: Mind Sculptor, Paradox, Healer, Wildspeaker, Warlord,
  Cryomancer; evitar Deathbringer, Pyromancer, Mentor e Necromancer. Enablers: Mindseeker
  Oculus, Arcane Amphisbaena, Keeper of the Quiet Hour, Protege's Awakening. Dica: não
  gastar o Jace em surveil sem necessidade, para ativar o −3 o máximo de vezes. Divergência:
  o autor o põe em 7º; nos dados é o último (52,9%) e o LimitedMTG, só pela leitura das
  cartas, também o aponta como armadilha (menos remoção de todos os pares). Prevalecem os dados.
- **BR Aggro (8º; 7º).** A "zona morta" do aggro: poucas Vicious Verse, payoffs fracos,
  ganho de vida no formato e fichas de Jace que dividem o dano. Payoffs: Ingris
  Stingerquill, Stingerquill Charm, Tomik, Izzet Sparkmage (com Fulminous Forte), Command
  the Stage, Grim Repriser, Master of Barbs. Enablers: Stingerquill Voxmancer, Screeching
  Soulbreaker, Cast Away Doubt, Extended Absence, Hallway Heckler. Nos dados, Grim
  Repriser rende 60,6% com 731 jogos (incerto) e Voxmancer 51,7%.
- **WB Sacrifice (10º; 8º).** "Promessa não cumprida": pouco fodder e poucos payoffs
  (Winter, Tormented Loner, Edgar, Ancient Bloodlord, Way of the Deathbringer; as míticas
  Bloodline Recollector e Darklight Phoenix). Twisted Fates é ótima mas fora do tema.
  Winter e Silence the Echo podem sacrificar planeswalkers (fichas de Jace gastas). O
  conselho do autor coincide com os dados: ignorar o tema e jogar as melhores cartas
  brancas e pretas com splash.
- **RW Aggro (9º; 9º).** O tema de contadores +1/+1 tem só quatro payoffs (Tomik, Orzhov
  Lawmage, Yoshimaru, Beloved Companion, Gallia, the Merrymaker, Warrior's Blades) e só
  Warrior's Blades é bom. Montar como aggro de curva: Campus Crier e Skilled Battlecarver
  nos dois, remoção barata, truques, Medic's Kitesail, cerca de 15 criaturas. Predictive
  Preparations decepcionou. Alternativa: RW midrange quando as bombas puxam para as cores.

A PreconForge, antes do lançamento, apontava UB, BR e RG como os três planos mais
coerentes no papel; UB e RG se confirmaram, BR não. O LimitedMTG, só pelas cartas, escolhia
BR (mais remoção) e evitava GU; acertou GU e errou BR. Lição registrada em
`knowledge/limitado-e-draft.md`: leitura das cartas não mede velocidade nem ganho de vida.

### As comuns: três fontes lado a lado

Quatro melhores comuns de cada cor segundo a Draftsim (lista revisada após uma semana),
com GIH WR do 17Lands (2026-10-12), win rate em mão do Untapped (2026-10-12, média 52,2%)
e a nota do simulador da Draftsim (0 a 5).

| Cor | Carta | Draftsim (revisão) | 17Lands GIH | Untapped em mão | Nota do simulador |
| --- | --- | --- | --- | --- | --- |
| W | Hexhaven Battalion | 1ª | 58,4% | 55,7% | 3,4 |
| W | Surgical Precision | 2ª | 57,7% | 55,1% | 2,8 |
| W | Memory Trap | 3ª | 55,5% | 53,9% | 3,4 |
| W | Blossom-Blessed Angel | 4ª (entrou; "jogo em todo deck branco") | 56,9% | 54,5% | 2,3 |
| W | Campus Crier | 5ª (saiu) | 55,4% | 53,5% | 2,5 |
| U | Mindseeker Oculus | 1ª | 60,6% | 57,2% | 3,4 |
| U | Protege's Awakening | 2ª (entrou) | 58,0% | 56,9% | 2,6 |
| U | Icy Reception | 3ª | 57,9% | 55,3% | 2,7 |
| U | Surveillance Phantasm | 4ª | 56,6% | 54,4% | 2,0 |
| U | Infinite Coursework | saiu | 55,1% | 54,4% | 3,2 |
| B | Extended Absence | 1ª | 60,2% | 57,1% | 2,9 |
| B | Last Gasp | 2ª | 56,8% | 54,6% | 3,4 |
| B | Theoretical Necromancer | 3ª (entrou) | 55,5% | 53,6% | 2,7 |
| B | Apex Witchstalker | 4ª (entrou) | 56,6% | 53,4% | 2,5 |
| B | Solve for Disappointment | saiu | 52,9% | 50,5% | 2,3 |
| R | No Admittance | 1ª | 56,9% | 54,5% | 3,2 |
| R | Wrath of the Bloodmane | 2ª | 55,4% | 54,4% | 3,2 |
| R | Awaken the Inferno | 3ª (entrou; "6 de dano mata quase tudo") | 55,2% | 54,4% | 2,8 |
| R | Heartstring Puller | 4ª | 55,1% | 52,4% | 2,7 |
| R | Skilled Battlecarver | saiu | 52,3% | 51,2% | 2,8 |
| G | Bestial Incursion | 1ª | 55,1% | 54,8% | 2,7 |
| G | Arcane Amphisbaena | 2ª | 55,7% | 53,7% | 2,9 |
| G | Compel Brutality | 3ª (caiu) | 53,8% | 53,3% | 3,2 |
| G | Something Worth Saving | 4ª (entrou) | 57,9% | 55,6% | 2,8 |
| G | Greenhouse Propagator | saiu | 52,7% | 52,8% | 3,0 |

Leitura:

- **As três fontes com partidas concordam.** A revisão do autor da Draftsim, o 17Lands e
  o Untapped apontam as mesmas cartas no topo de cada cor; o Untapped tem a mesma ordem com
  números 3 a 4 pontos mais baixos, por ter população mais ampla. Única divergência de
  ordem: em verde, os dados põem Something Worth Saving e Vinelasher Adept acima de
  Bestial Incursion.
- **O simulador erra o que os dados acertam.** Surveillance Phantasm (nota 2,0),
  Protege's Awakening (2,6), Blossom-Blessed Angel (2,3) e Keeper of the Quiet Hour (1,5)
  estão entre as melhores comuns nos dados; Way of the Mind Sculptor tem nota 1,5 e rende
  58,3% (o próprio guia da Draftsim a chama de primeiro pick fácil). No sentido oposto,
  Infinite Coursework (3,2), Greenhouse Propagator (3,0), Yoshimaru, Scrappy Stray (3,7) e
  Woodwork Prodigy (3,4) têm nota alta e rendem na média ou abaixo. As notas parecem
  anteriores aos dados; use o simulador para treinar picks, não para ranquear.
- **Incomuns no Untapped** (em mão; média 52,2%): azul Countersculpt 57,5%, Plan for All
  Outcomes 56,3%, Fblthp 56,1%, Way of the Mind Sculptor 56,0%; preto Break Under Pressure
  57,5%, Rewrite Regrets 56,5%, Multiply by Zero 56,4%; vermelho Kiora of Fire and Ashes
  60,5%, Violent Echoes 57,1%, Fulminous Forte 55,0%; branco Your Fate Ends Here 55,7%,
  Generous Revival 54,9%, Way of the Healer 54,3%, Teyo 54,3%; verde Fblthp, Knows the Way
  54,9%, Way of the Paradox 53,6%, Ruric Thar, Magecrusher 53,6%; multicoloridas Craftwork
  Crusher 60,8%, Recursive Recruitment 59,0%, Hapatra 57,3%, Mind Meanderer 56,7%, Twinned
  Vision (comum) 56,3%. Mesma ordem do 17Lands.

### Dicas de jogo e interações (Draftsim e LimitedMTG)

- **Parada no upkeep** para matar The Theorist, Jace Beleren antes da ativação, com Wrath
  of the Bloodmane, Violent Echoes ou Extended Absence.
- **Multiply by Zero na fase principal:** truques de combate e contadores +1/+1 punem o
  uso em combate.
- **Sphinx of False Conclusions** (rara azul) é a carta a respeitar: guardar Icy
  Reception ou Extended Absence para ela. Teyo, Lightshield Expert com flash embosca
  criaturas pequenas; Prophesied End pune atacar; Rise of the Deathbringer não mata X/4.
- **A ficha de Jace é recurso:** Compel Brutality pode usar a lealdade dela como dano;
  Silence the Echo e Winter, Tormented Loner a sacrificam; um Jace de 1 lealdade guardado
  vira uma carta futura com um empower 2. Violent Echoes no Jace do oponente costuma ser
  compensado pelo seu.
- **Terrenos Annex e Commons** entram desvirados com qualquer planeswalker, inclusive a
  ficha: Arcane Amphisbaena e Academic Ascent fazem empower por duas manas, Campus Crier
  do cemitério por uma.
- **Fblthp, Impossibly Lost** compra duas com um voador barato (Geist of Saint Thalia,
  Tetsuko Umezawa, Fugitive) e vence o self-mill; Generous Revival, Theoretical
  Necromancer e Rewrite Regrets o trazem de volta.
- **Countersculpt** é a melhor resposta a bombas do formato; manter a base de mana o mais
  azul possível para conjurá-la.
- No Arena, a habilidade ativada de Theorist's Sanctum fica à esquerda, ao contrário de
  Room of Refuge.

### Sealed (PreconForge e Draftsim)

- Separar o pool por cor e identificar três coisas: melhores ameaças, melhor remoção e
  cores mais fundas. Não começar pela rara favorita: cinco comuns boas e duas remoções
  valem mais que uma mítica com oito cartas fracas na mesma cor.
- Montar o deck funcional primeiro e só depois melhorar a sinergia; não forçar um
  arquétipo (RG sem rampa é só um deck lento).
- 17 terrenos; não descer a 16 porque o deck "parece barato": perder o terceiro terreno
  custa mais que comprar um terreno a mais.
- Splash: a PreconForge (pré-lançamento) só para bomba ou remoção de primeira; a Draftsim,
  com partidas, diz que o splash é fácil e rende também em sealed. Com os dados do
  Untapped sobre decks de três cores, prevalece a Draftsim, mantida a exigência de fontes
  (tabela de 40 cartas em `knowledge/base-de-mana.md`).
- Remoção primeiro, truques estreitos depois: criaturas caras precisam gerar valor ao
  entrar, porque morrem para mágicas de duas ou três manas.

## Construção do deck

- **17 terrenos em 40 cartas** é o padrão (`knowledge/base-de-mana.md`); o formato é
  lento o bastante para não descer a 16, salvo em decks de curva muito baixa.
- **Duas cores com splash.** O guia anterior recomendava duas cores; os dados e a Draftsim
  mostram que o splash é parte do formato. Fontes de splash em ordem de preferência:
  terreno duplo do par com a cor do splash (entra desvirado só com planeswalker), Murmuring
  Volume, fichas Heartwood (para R ou G), basic landcycling (Awaken the Inferno, Vinelasher
  Adept) e um ou dois básicos. Splash de uma carta com um símbolo colorido; evitar custos
  com dois símbolos da cor do splash.
- **Fontes por cor:** 9 para conjurar um custo de uma mana colorida no turno certo, 14
  para custos com dois símbolos da mesma cor; para o splash, 3 ou 4 fontes de uma carta
  de custo 4 ou mais (tabela de 40 cartas de Karsten).
- **Criaturas:** o livro recomenda mais do que o instinto sugere; aqui, decks azuis
  podem trocar algumas por compra de cartas, desde que tenham como sobreviver aos
  primeiros turnos (Surveillance Phantasm, Icy Reception, remoção). Decks agressivos (RW)
  querem cerca de 15.
- **Enabler antes de payoff:** em UB, GW e BR, conte os enablers baratos antes de aceitar
  payoffs; um payoff que liga no turno nove não é payoff.
- Confira a lista com `mtg deck validate --format limited` e `mtg deck analyze`.

## Outros modos

Os números de um modo não valem para outro; o guia acima é de Premier Draft.

| Modo | Jogos | Média dos usuários | Melhores pares | Observação |
| --- | --- | --- | --- | --- |
| Traditional Draft (BO3) | 48.707 | 61,5% | WU 63,7%; UR 62,7%; RG 61,9%; BG 61,8%; UB 61,5% | População mais forte (média 7 pontos acima). UR sobe para o segundo lugar e UB cai para o quinto em relação ao Premier: tratar como hipótese |
| Pick Two Draft | 68.448 | 55,4% | WU 57,5%; UB 56,8%; RG 56,7%; WB 56,3%; UR 56,2% | WB sobe muito (53,4% no Premier); amostra de 2.457 jogos |
| Quick Draft | 35.186 | 55,6% | UR 56,9%; BG 56,8%; WU 56,8%; RG 56,4%; UB 56,3% | Bots escolhem diferente de humanos; cinco pares em menos de 1 ponto |
| Sealed | — | — | WU 58,5%; BG 58,0%; GU 57,4%; UB 57,4% (snapshot de 2026-10-05) | O 17Lands não devolveu dados de Sealed em 2026-10-12; os números são do snapshot anterior |
| Traditional Sealed | — | — | — | Sem dados |

WU é o melhor ou o segundo melhor par em todos os modos com dados; UB é o mais jogado em
todos eles.

## Limites deste guia

- Dados de 13 dias: ordem das cartas dentro de uma faixa de 1 ponto não é confiável; raras
  e míticas têm de 500 a 1.100 jogos, e várias míticas ainda não têm GIH WR no 17Lands.
- O GIH WR infla cartas caras e de fim de jogo e reflete a força do par em que a carta
  entra (`knowledge/limitado-e-draft.md`, "Ler dados de win rate").
- Os planos de cada par vêm das sinalizadoras e do guia da Draftsim, não foram jogados
  por nós; a descrição das mecânicas vem do texto das cartas na base local.
- A tabela de pares do Untapped com taxa de 6 ou mais vitórias não foi alcançada (a página
  a carrega de um endpoint não localizado); a coluna do Untapped é popularidade, não
  desempenho.
- As notas do simulador da Draftsim não têm data nem método publicados; são tratadas como
  avaliação pré-lançamento.
- 31 cartas da lista do 17Lands não foram casadas com a coleção `fra` da base (terrenos
  básicos e cartas de folha bônus) e ficaram fora da contagem por cor. Quatro cartas do
  simulador (Mind Twist, Austere Command, Sublime Epiphany, Flesh Duplicate) não constam
  da coleção `fra` na base.
