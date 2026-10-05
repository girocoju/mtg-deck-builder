# Reality Fracture (FRA) — guia de draft

- **Dados:** 17Lands, coletados em 2026-10-05. Modo de referência: **Premier Draft**
  (220.847 jogos; win rate médio dos usuários do 17Lands: 55,1%).
- **Como ler os números:** GIH WR é o win rate dos jogos em que a carta esteve na mão.
  Compare sempre com os 55,1% da média: uma carta de 57% é boa, uma de 53% é fraca.
  ALSA é o pick médio em que a carta ainda aparece no pacote (quanto maior, mais tarde sai).
- **Atenção à amostra:** a coleção saiu no Arena há menos de uma semana. Só 220 das 290
  cartas têm 500 jogos ou mais em mão; raras e míticas têm amostras de 500 a 1.300 jogos.
  Os rankings de comuns são os mais confiáveis; tudo aqui deve ser regenerado em duas semanas.
- **Regerar:** `mtg draft update fra --mode all --force` e os comandos citados em cada seção.

## Visão geral

| O que | Leitura |
| --- | --- |
| Mecânica central | **Empower Jace N** (35 cartas): põe N contadores de lealdade em uma ficha de Jace que você controla; se não houver, cria a ficha, um planeswalker azul com "−1: Surveil 1" e "−3: compre uma carta". É vantagem de cartas embutida em cartas comuns |
| Outras mecânicas | **Surveil** (39 cartas); **prepared** (criaturas que entram "preparadas" e permitem conjurar uma cópia da mágica associada); ciclos de terrenos Annex e Commons, que entram desvirados se você controla um planeswalker (a ficha de Jace conta) |
| Velocidade | Formato de valor, não de corrida: as melhores comuns são compra de cartas e remoção, e várias criaturas agressivas de custo baixo estão abaixo da média |
| Cor mais forte | **Azul**, com folga: sete comuns entre 57,7% e 62,9%. Nenhuma outra cor tem uma comum acima de 60,1% |
| Cor mais fraca | **Verde** nas comuns (a melhor tem 56,9%) e **vermelho** logo acima |
| Remoção | Concentrada em preto e vermelho nas comuns; branco tem remoção condicional; azul tem Unsummon e anulação |

Remoção em comuns e incomuns, pela leitura da base (`mtg draft set fra`; a classificação é
automática e inclui algumas criaturas com efeito de remoção): branco 5, azul 3, preto 5,
vermelho 7, verde 3, multicoloridas 8.

## Os dez pares de cores

Win rate do par em Premier Draft e as cartas que sinalizam o arquétipo
(`mtg draft colors fra`, `mtg draft cards fra --color multi --limit 40`).

| Par | Win rate | Jogos | Sinalizadoras (GIH WR) | Plano |
| --- | --- | --- | --- | --- |
| WU (Fatehold) | **57,1%** | 25.438 | Desperate Futurescribe 59,6%; Prudent Fateseer 58,3%; Fatehold Charm 58,2%; Fatehold Chronologist (comum) 57,1% | Voadores e surveil; a melhor dupla do formato |
| UB (Theorix) | **56,8%** | 28.117 | Recursive Recruitment 62,3%; Theorix Charm 59,3%; Null Summoner (rara) 62,4% | Controle: remoção preta mais compra azul. O par mais jogado |
| BG | 56,6% | 15.729 | Hapatra, the Desert Fang 58,4%; Primal Witchstalker 57,4% | Midrange de cemitério; rende apesar de o verde ser fraco sozinho |
| RG (Konstrari) | 55,9% | 24.969 | Craftwork Crusher 62,6%; Konstrari Charm 56,9%; Konstrari Improviser (comum) 55,4% | Criaturas grandes; muito disputado para o que rende |
| UR | 55,4% | 18.362 | Clash of Elements 59,6%; Twinned Vision (comum) 59,2%; Saheeli, Jewel of Avishkar 57,0% | Mágicas; na média |
| GW (Vigorbloom) | 54,2% | 22.059 | Vigorbloom Vanguard 57,8%; Bloombrute 55,0% | Abaixo da média |
| RW | 53,7% | 10.650 | Warrior's Blades 55,8%; Mabel, Valley Hero 52,1% | Aggro; o formato não o favorece |
| BR (Stingerquill) | 53,6% | 16.368 | Stingerquill Charm 56,2%; Grim Repriser 55,2% | Abaixo da média |
| GU | 53,6% | 9.300 | Mind Meanderer 59,1%; Kiora of Salt and Sand 54,9% | Abaixo da média, apesar do azul |
| WB | 53,5% | 10.005 | Twisted Fates 57,9%; Edgar, Ancient Bloodlord 49,7% | O pior par |

Leitura: os três melhores pares têm azul ou preto; os quatro piores não têm azul, ou o
combinam com verde. Entre o melhor e o pior par há 3,6 pontos — o formato pune a escolha
de cores, mas não a ponto de abandonar um pacote aberto de bombas.

## Ranking de comuns e incomuns por cor

GIH WR em Premier Draft (`mtg draft cards fra --color U --rarity common`).

### Azul — a cor a disputar

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Sphinx's Approach | 62,9% | 8,0 | Fblthp, Impossibly Lost | 61,6% | 4,7 |
| Mindseeker Oculus | 61,3% | 3,5 | Countersculpt | 61,2% | 4,0 |
| Protege's Awakening | 60,2% | 5,6 | Way of the Mind Sculptor | 59,1% | 3,6 |
| Icy Reception | 58,8% | 5,4 | Plan for All Outcomes | 58,9% | 3,3 |
| Surveillance Phantasm | 58,5% | 5,0 | Proft, Consulting Detective | 58,0% | 3,6 |
| Undulating Witness | 58,1% | 5,6 | Arni, Humble Scribe | 57,7% | 4,9 |
| Unsummon | 57,7% | 5,5 | | | |

Até as piores comuns azuis (Divining Duelist 54,6%, Cryotheory Adept 53,4%) ficam perto
da média. Sphinx's Approach tem amostra pequena (1.032 jogos) e um viés: o deck pode ter
qualquer número de cópias, então quem a joga costuma ter várias; uma cópia isolada é só
"compre duas cartas" por três manas.

### Preto — a melhor remoção

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Extended Absence | 60,1% | 3,4 | Break Under Pressure | 61,4% | 3,1 |
| Last Gasp | 56,5% | 3,6 | Rewrite Regrets | 60,2% | 4,2 |
| Theoretical Necromancer | 56,0% | 6,7 | Multiply by Zero | 59,6% | 2,7 |
| Apex Witchstalker | 55,9% | 5,5 | Tinybones, Pocket Nuisance | 57,1% | 4,8 |
| Void Extrapolator | 55,7% | 7,1 | Gallia, Tragic Host | 55,9% | 4,8 |
| Cast Away Doubt | 55,5% | 7,0 | | | |

Piores comuns: Screeching Soulbreaker 53,7%, Solve for Disappointment 52,2%.

### Branco

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Campus Crier | 57,3% | 5,6 | Way of the Healer | 56,9% | 3,2 |
| Hexhaven Battalion | 57,1% | 4,6 | Your Fate Ends Here | 56,2% | 3,0 |
| Surgical Precision | 56,6% | 4,4 | Generous Revival | 56,1% | 4,7 |
| Memory Trap | 56,3% | 3,2 | Thalia, the Survivor | 56,0% | 4,2 |
| Unflinching Hortimancer | 55,6% | 5,1 | Teyo, Lightshield Expert | 55,3% | 4,1 |

Piores comuns: Graft Surgeon 50,1%, Predictive Preparations 46,7%.

### Vermelho

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Wrath of the Bloodmane | 57,0% | 4,0 | Kiora of Fire and Ashes | 61,6% | 2,5 |
| No Admittance | 56,5% | 3,4 | Violent Echoes | 58,6% | 3,0 |
| Awaken the Inferno | 55,6% | 4,8 | Pia, Determined Rebuilder | 56,7% | 4,2 |
| Tether Technician | 54,7% | 7,4 | Fulminous Forte | 55,4% | 3,1 |

As três melhores comuns são remoção; as criaturas comuns vermelhas estão todas abaixo da
média. Piores: Hallway Heckler 52,6%, Eardrum Rattler 48,0%.

### Verde

| Comuns | GIH | ALSA | Incomuns | GIH | ALSA |
| --- | --- | --- | --- | --- | --- |
| Bestial Incursion | 56,9% | 4,9 | Way of the Paradox | 57,1% | 4,6 |
| Arcane Amphisbaena | 55,8% | 4,3 | Fblthp, Knows the Way | 56,4% | 3,9 |
| Vinelasher Adept | 55,5% | 5,6 | Jiang Yanggu, Never Alone | 56,0% | 3,9 |
| Wrecking Gecko | 55,1% | 6,6 | Ruric Thar, Magecrusher | 56,0% | 4,0 |
| Compel Brutality | 55,0% | 4,4 | | | |

Piores comuns: Greenhouse Propagator 52,8%, Inspired Tethermage 51,8%.

### Incolores e terrenos

Theorix Annex 58,8%, Murmuring Volume 57,7% (pedra de mana de qualquer cor), Innovative
Commons 56,9%, Room of Refuge 56,0%, Keeper of the Quiet Hour 55,5%. Os terrenos refletem
em parte a força do par que os usa, não o terreno em si.

## Bombas

Com amostras ainda pequenas (500 a 1.300 jogos), mas com diferença grande demais para
ser ruído: Ajani Unrelenting 75,0%; The Theorist, Jace Beleren 72,2%; Uldaros Theorix
71,4%; Garruk, Veiled Butcher 66,6%; Garruk, Curse Breaker 66,2%; Sphinx of False
Conclusions (rara) 65,6%; Overwrite the Multiverse 64,9%; Lich's Relic (rara) 63,6%.
Entre as incomuns, jogam como raras: Craftwork Crusher 62,6%, Recursive Recruitment 62,3%,
Kiora of Fire and Ashes 61,6%, Fblthp, Impossibly Lost 61,6%, Break Under Pressure 61,4%.

## Prioridade de picks e sinais

1. **Bombas e incomuns de 61% ou mais**, em qualquer cor.
2. **Remoção preta e as melhores comuns azuis:** Extended Absence, Mindseeker Oculus,
   Break Under Pressure, Multiply by Zero, Countersculpt.
3. **Empower Jace barato** (Mindseeker Oculus, Protege's Awakening, as incomuns "Way of
   the ..."): a ficha de Jace rende cartas e liga os terrenos Annex e Commons.
4. **Sinalizadoras do par** (tabela dos pares), para confirmar a segunda cor.
5. Criaturas de curva e truques, por último: o formato tem poucas comuns boas de custo 2.

Sinais (`knowledge/limitado-e-draft.md`, seção de sinais): Mindseeker Oculus sai em
média no pick 3,5 e Extended Absence no 3,4. Ver uma delas depois do pick 6 indica que a
cor está livre à direita. Azul é a cor que todos querem; se as comuns azuis de 58% ou
mais não aparecem até o pick 5 ou 6, a cor está sendo cortada e insistir custa caro.
Preto é o melhor plano B, pela remoção.

## Armadilhas: dados contra impressão

`mtg draft gaps fra` compara o ranking de GIH WR com o de ALSA.

**Subestimadas (rendem e saem tarde):** Sphinx's Approach (62,9%, ALSA 8,0, com a
ressalva acima); Protege's Awakening (60,2%, ALSA 5,6); Theorix Annex (58,8%, ALSA 6,2);
Murmuring Volume (57,7%, ALSA 6,6); Clash of Elements (59,6%, ALSA 5,5); Living Library
(58,7%, mas só 545 jogos).

**Superestimadas (saem cedo e rendem pouco):** Yoshimaru, Beloved Companion (46,5%, a
pior da lista); Way of the Pyromancer (51,4%, ALSA 3,9); Koth of the Homestead (53,5%,
ALSA 3,4); Woodwork Prodigy (53,4%, ALSA 3,6); Way of the Wildspeaker (54,2%, ALSA 3,2);
Prophesied End (54,6%, ALSA 3,1) — remoção barata branca que rende abaixo da média,
provavelmente por dar uma carta ao oponente.

## Construção do deck

- **17 terrenos em 40 cartas** é o padrão (`knowledge/base-de-mana.md`); o formato é
  lento o bastante para não descer a 16, salvo em decks de curva muito baixa.
- **Duas cores.** Os terrenos Annex e Commons ajudam um splash leve, mas entram virados
  sem um planeswalker em jogo.
- **Fontes por cor:** 9 para conjurar um custo de uma mana colorida no turno certo, 14
  para custos com dois símbolos da mesma cor (tabela de 40 cartas de Karsten).
- **Criaturas:** o livro recomenda mais do que o instinto sugere; aqui, decks azuis
  podem trocar algumas por compra de cartas, desde que tenham como sobreviver aos
  primeiros turnos (Surveillance Phantasm, Icy Reception, remoção).
- Confira a lista com `mtg deck validate --format limited` e `mtg deck analyze`.

## Outros modos

Os números de um modo não valem para outro; o guia acima é de Premier Draft.

| Modo | Jogos | Média dos usuários | Melhores pares | Observação |
| --- | --- | --- | --- | --- |
| Traditional Draft (BO3) | 23.030 | 62,3% | WU 65,2%; UR 63,1%; BR 62,9%; WR 62,6% | População mais forte (média 7 pontos acima); amostras de 500 a 1.100 jogos por carta. BR e WR sobem muito em relação ao Premier: tratar como hipótese |
| Sealed | 44.089 | 56,1% | WU 58,6%; BG 58,0%; UB 57,6%; UG 57,0% | Mindseeker Oculus, Surveillance Phantasm e Extended Absence seguem no topo das comuns |
| Pick Two Draft | 30.417 | 55,8% | UB 57,6%; WU 57,5%; RG 57,5% | Remoção cara sobe (Awaken the Inferno 59,9%) |
| Quick Draft | — | — | — | Sem dados em 2026-10-05; quando houver, lembrar que os bots escolhem diferente de humanos |
| Traditional Sealed | — | — | — | Sem dados |

WU é o melhor ou o segundo melhor par em todos os modos com dados.

## Limites deste guia

- Dados de seis dias: ordem das cartas dentro de uma faixa de 1 ou 2 pontos não é confiável.
- O GIH WR infla cartas caras e de fim de jogo e reflete a força do par em que a carta
  entra (`knowledge/limitado-e-draft.md`, "Ler dados de win rate").
- Os planos de cada par na tabela são leitura das cartas sinalizadoras, não foram
  jogados; a descrição das mecânicas vem do texto das cartas na base local.
- 31 cartas da lista do 17Lands não foram casadas com a coleção `fra` da base (terrenos
  básicos e cartas de folha bônus) e ficaram fora da contagem por cor.
