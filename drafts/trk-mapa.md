# Star Trek (TRK) — mapa de picks

Gerado por `mtg draft map trk --write` em 2026-11-09. Dados: sem dados: avaliação teórica.
Fonte do poder, por carta: teorica* 306. Cartas draftáveis: 306 (26 míticas, 79 raras, 110 incomuns, 91 comuns).

**Como ler.** A nota é em pontos percentuais de win rate acima da média da fonte da carta
(17Lands: GIH WR − média dos usuários; Untapped: idem com a média dele; `draftsim*` e
`teorica*` são notas sem amostra de partidas). Raridade não entra na conta: ela só aparece
porque raras e míticas costumam ter mais poder, e porque cada pacote tem uma rara ou mítica,
cerca de três incomuns e dez comuns. No P1P1 compare a rara do pacote com a melhor incomum e a
melhor comum (seção 1); do P1P2 em diante, a rara quase sempre já saiu e a escolha é entre
incomuns e comuns (seção 2). Arquétipos: pares que a carta serve (`+` = payoff). Elos: o que a
carta *pede* e *oferece* (os dez pares e os ganchos fichas, virar, oficiais, vida, tesouros, klingons, equipamentos, teletransporte); Σ é a soma das sinergias diretas com
toda a coleção (quantas parceiras ela tem e quão fortes são os elos).

**Como o motor combina.** `mtg draft pick` soma: poder + encaixe nas cores (peso cresce do P1P1 até
o pick 21) + par + necessidade + sinal + flexibilidade + sinergia do par + **parceiros**
(0.6 ponto por unidade de elo com cada carta já escolhida, teto 3). Por isso um elo
direto desempata cartas próximas e não vira uma carta fraca em bomba. Teoria:
`knowledge/limitado-e-draft.md`, seções 3 (prioridades), 4 (arquétipos e deck perfeito) e 6
(compromisso).

## 0. Leitura da coleção e dos arquétipos

- **Composição.** 306 cartas draftáveis (26 míticas, 79 raras, 110 incomuns, 91 comuns). Por cor: branco 45, azul 45, preto 46, vermelho 45, verde 44, multicoloridas 33, incolores 48. As 20 multicoloridas incomuns são as sinalizadoras dos pares (teoria: `limitado-e-draft.md` §4, arquétipos).
- **Criaturas de comum e incomum.** 111 no total; verde tem mais (20) e azul menos (16). 59% custam até 3 (curva média; §2 custo e curva, §8 parâmetros do formato). Curva por cor, custo 1 a 6+: W 2 5 4 4 4 0; U 1 4 3 3 3 2; B 2 4 5 3 3 1; R 1 4 5 3 2 2; G 1 4 6 3 3 3.
- **Remoção de comum e incomum** (classificação automática pelo texto; confira com `mtg card`): branco 6: Command Decision, Malfunctioning Holodeck, The Measure of a Man, 70,000 Light-Years from Home, U.S.S. Excelsior, Cutting Edge, Ghost of Illyria; azul 3: Energize, Interstellar Effigy, Test of Priorities; preto 7: Resistance Is Futile, Commander Raffi Musiker, Test of Loyalty, Blastoneuron, Eject the Warp Core, Impossible Choice, He's Dead, Jim; vermelho 7: Munitions Enthusiast, Planetary Bombardment, Plasma Cascade, Transporter Malfunction, Dahar Master, Genesis Effect, Perils of the Past; verde 3: Test of Courage, Amok Time, Dominion Assault Force; multicoloridas 2: Locutus, the One Who Speaks, Kirk, Commanding Officer. Remoção é a prioridade de pick depois das bombas (§2 removal, §3 prioridades); a cor com menos remoção depende da segunda cor.
- **Mecânicas e palavras-chave** (ocorrências e grupos de cor): Surveil 22 (incolor 7, multi 5, U 4); Station 17 (incolor 4, U 4, W 3); Strange new worlds 13 (G 5, U 4, B 1); Flying 9 (U 3, B 2, W 2); Landfall 9 (G 4, R 3, multi 2); Face a dilemma 8 (B 4, U 3, multi 1); Flash 7 (U 3, G 2, R 1); Menace 7 (B 5, multi 1, R 1); Trample 7 (R 4, multi 2, G 1); Vigilance 7 (U 3, G 2, W 1).
- **Correção de mana.** 32 terrenos não básicos draftáveis, 5 cartas com landcycling e 15 fontes de mana de qualquer cor: Saurian Explorer, David and Carol Marcus, Creators, Subspace Anomaly, Gaseous Anomaly, Class-F Shuttlecraft, Culber and Stamets, Star-Crossed, Quark, Humble Proprietor, Grand Nagus Zek. Quanto mais correção, mais compensa o splash de uma bomba ou remoção (§2 card advantage e correção de mana; §7 construção).
- **Pares nos dados.** Sem dados de partidas para esta coleção: a leitura dos pares é teórica, pela contagem de payoffs e enablers marcados no texto das cartas, e deve ser refeita com `mtg draft update trk` quando o 17Lands publicar.
- **Arquétipos** (profundo = 6 ou mais payoffs em comum e incomum; raso = 3 ou menos, depende de abrir a rara; §4 arquétipos e deck perfeito): WU Frota Estelar: espaçonaves: 9 payoffs (6 C/U) e 54 enablers (33 C/U), profundo; melhor payoff Captain Jean-Luc Picard +4.5*; sinalizadoras Constable Odo, Hemmer, Fixing What Is Broken, Live Long and Prosper · UB Dilemas: 9 payoffs (6 C/U) e 39 enablers (28 C/U), profundo; melhor payoff Elim Garak, Simple Tailor +3.0*; sinalizadoras Mirror Universe Intrusion, Seven of Nine, Lore, Positronic Provocateur · BR Klingons: morte com honra: 17 payoffs (10 C/U) e 73 enablers (48 C/U), profundo; melhor payoff Khan, Vengeful Heart +4.5*; sinalizadoras The Duras Sisters, Gowron, Eager for Battle, L'Rell, Fierce Visionary · RG Landfall: novos planetas: 9 payoffs (9 C/U) e 27 enablers (21 C/U), profundo; melhor payoff Dal R'El, Augment Orphan +1.0*; sinalizadoras Hit It!, Dal R'El, Augment Orphan, Cleveland Booker, Empath · WG Enfermaria: marcadores +1/+1: 9 payoffs (6 C/U) e 31 enablers (24 C/U), profundo; melhor payoff Dr. Joseph M'Benga +4.5*; sinalizadoras The Inner Light, The Doctor, EMH, Phlox, Unorthodox Doctor · WB Coletivo Borg: criaturas artefato: 17 payoffs (11 C/U) e 43 enablers (31 C/U), profundo; melhor payoff Borg Cube +5.0*; sinalizadoras Locutus, the One Who Speaks, The City on the Edge of Forever, Zero, Incorporeal Sensate, Borg Cube · UR Laboratório: mágicas não criatura: 15 payoffs (9 C/U) e 58 enablers (49 C/U), profundo; melhor payoff Infinite Diversity +5.0*; sinalizadoras Gray and Adira, Forever Joined, Year of Hell, Spock, Always Your Friend · BG Cemitério: vigiar e reciclar: 29 payoffs (18 C/U) e 39 enablers (32 C/U), profundo; melhor payoff Sela, Tal Shiar Paradox +5.0*; sinalizadoras Daniels, Temporal Agent, Nog, Ambitious Cadet, Vash, Freelance Archaeologist · WR Alerta vermelho: poder total 8: 17 payoffs (13 C/U) e 59 enablers (36 C/U), profundo; melhor payoff Captain Jean-Luc Picard +4.5*; sinalizadoras Worf, Honor-Bound Warrior, Kirk, Commanding Officer, Kira Nerys, Firebrand · UG Novos mundos: terrenos de nomes diferentes: 14 payoffs (7 C/U) e 50 enablers (29 C/U), profundo; melhor payoff The Destruction of Praxis +4.5*; sinalizadoras All Good Things..., D'Vana Tendi, Optimistic Ensign, The Traveler.
- **Ganchos fora dos dez pares** (quem pede / quem oferece): fichas 16/39, virar 8/26, oficiais 3/44, vida 3/39, tesouros 2/5, klingons 3/16, equipamentos 3/4, teletransporte 14/57.
- **Grafo.** Cartas mais centrais (portas de entrada para a coleção): Captain Jean-Luc Picard 100, Scotty, Miracle Worker 86.4, Excalbian Gamemaster 75.7, Captain Benjamin Sisko 73.3, The Destruction of Praxis 65.4. 9 comunidades com 3 cartas ou mais (elos de peso ≥ 2): 57 cartas (RBW; elos fichas, BR); 19 cartas (URG; elos BG, UR); 16 cartas (UWG; elos WB, WU); 14 cartas (BUG; elos BG, UB).

## 1. Ordem de pick da coleção inteira

Nota (fonte), cor, custo, arquétipos, elos e Σ sinergia. Ordem dentro da raridade.

### Míticas (26)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +5.0* | teorica | WB | 5WB | Borg Cube | WB+ WU | pede WB · oferece WU, virar | 45.1 |
| 2 | +5.0* | teorica | - | 8 | Crystalline Entity | WU WB WR | oferece WB, WR, WU, teletransporte | 34 |
| 3 | +5.0* | teorica | R | 7RR | Infinite Diversity | UR+ BG+ | pede BG, UR | 112.4 |
| 4 | +4.5* | teorica | R | 2R | Captain James T. Kirk | WR+ UB BR BG | pede WR · oferece BG, BR, UB, fichas, oficiais | 114.2 |
| 5 | +4.5* | teorica | W | 2W | Captain Jean-Luc Picard | WU+ WR+ BR | pede WR, WU, fichas, oficiais · oferece BR, fichas, oficiais, virar | 174.5 |
| 6 | +4.5* | teorica | G | 3G | Captain Kathryn Janeway | RG WG UG | oferece RG, UG, WG, oficiais | 34.2 |
| 7 | +4.5* | teorica | W | 2W | Dr. Beverly Crusher | WG | pede vida · oferece WG | 37.1 |
| 8 | +4.5* | teorica | G | 2GG | Dr. Joseph M'Benga | WG+ | pede WG | 32.8 |
| 9 | +4.5* | teorica | G | 1G | Jadzia Dax, Living Legacy | WG+ BR | pede WG · oferece BR | 36.4 |
| 10 | +4.5* | teorica | B | 2BB | Khan, Vengeful Heart | BR+ WU WR | pede BR · oferece WR, WU, teletransporte | 65 |
| 11 | +4.5* | teorica | U | 2U | Lieutenant Commander Data | WG+ UR+ WB | pede UR, WG · oferece WB | 112.1 |
| 12 | +4.5* | teorica | U | 2U | Lt. Cmdr. Geordi La Forge | WU+ | pede WU | 29.3 |
| 13 | +4.5* | teorica | U | 2UU | Mr. Spock, Science Officer |  |  |  |
| 14 | +4.5* | teorica | R | 2RR | Q, Stacking the Deck | WU WR | oferece WR, WU, teletransporte | 16.6 |
| 15 | +4.5* | teorica | R | 2R | Quark, Humble Proprietor |  | pede tesouros · oferece tesouros | 1.6 |
| 16 | +4.5* | teorica | U | 1UU | Scotty, Miracle Worker | UR+ BG+ | pede BG, UR, teletransporte | 156.4 |
| 17 | +4.5* | teorica | U | 1U | Seven of Nine, Unassimilated | UG+ BR WB BG | pede UG · oferece BG, BR, WB, oficiais | 103.2 |
| 18 | +4.0* | teorica | U | 1UU | Kobayashi Maru Scenario | UB BR WR | oferece BR, UB, WR, fichas, oficiais | 54.5 |
| 19 | +4.0* | teorica | W | 3WW | U.S.S. Enterprise-A, Free Spirit | WU BR WB WR | oferece BR, WB, WR, WU, fichas, oficiais, virar | 83.2 |
| 20 | +3.0* | teorica | B | 6BB | Death Is Irrelevant | WB+ | pede WB | 50.2 |
| 21 | +3.0* | teorica | - | 9 | Deep Space 9 | WR+ WU WB | pede WR · oferece WB, WU, virar | 80.8 |
| 22 | +3.0* | teorica | W | 5W | Excalbian Gamemaster | BR+ UG+ WU WG WR | pede BR, UG · oferece WG, WR, WU, fichas, oficiais, teletransporte | 159.1 |
| 23 | +3.0* | teorica | B | 4BB | Georgiou, Terran Emperor | WU BR WR | oferece BR, WR, WU, fichas, oficiais | 50.6 |
| 24 | +3.0* | teorica | B | 4BBB | Gul Dukat, Colonial Prefect | WU WR | oferece WR, WU, vida | 8 |
| 25 | +3.0* | teorica | G | 4GG | Rok-Tahk, Budding Scientist | WU BR WR | oferece BR, WR, WU, fichas, teletransporte | 56.6 |
| 26 | -1.5* | teorica | - |  | Starfleet Academy | UG | oferece UG | 14 |

### Raras (79)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +5.0* | teorica | B | 3B | Sela, Tal Shiar Paradox | BG+ BR WR | pede BG · oferece BR, WR, fichas | 97.4 |
| 2 | +5.0* | teorica | U | 2UU | Wesley Crusher, Starfleet Cadet | UB | oferece UB, oficiais, teletransporte | 21.8 |
| 3 | +4.5* | teorica | R | 1RR | Encounter the Unknown | UB UR | oferece UB, UR | 22.5 |
| 4 | +4.5* | teorica | - | X | Engineered Explosives |  |  |  |
| 5 | +4.5* | teorica | B | 3BB | The Destruction of Praxis | UG+ BR UR WR | pede UG · oferece BR, UR, WR, fichas, klingons | 117.4 |
| 6 | +4.5* | teorica | R | 2R | The Wrath of Khan |  | oferece virar | 6.5 |
| 7 | +3.5* | teorica | B | 5BB | Armus, Skin of Evil | WU WR | oferece WR, WU | 5.7 |
| 8 | +3.0* | teorica | W | 1W | Antagonist Incorporator | WB+ BR WR | pede WB · oferece BR, WR, fichas | 97.2 |
| 9 | +3.0* | teorica | W | 1W | Captain Benjamin Sisko | UB+ BR WR | pede UB, fichas, oficiais · oferece BR, WR, fichas, oficiais | 151 |
| 10 | +3.0* | teorica | G | 2G | Captain Jonathan Archer | BR WR | oferece BR, WR, fichas, oficiais, teletransporte | 56.8 |
| 11 | +3.0* | teorica | G | 1GG | Captain Pike, Fullness of Time | UG+ RG | pede UG · oferece RG, oficiais | 67.8 |
| 12 | +3.0* | teorica | B | B | Collation Trimatrix | WB+ BR | pede WB, fichas · oferece BR, virar | 99.2 |
| 13 | +3.0* | teorica | URG | GUR | Dathon, His Heart Open | UR+ | pede UR · oferece oficiais | 16.8 |
| 14 | +3.0* | teorica | W | 1W | Deanna Troi, Psychic Counsel | BR WG | oferece BR, WG | 12.9 |
| 15 | +3.0* | teorica | G | 1GG | Dr. Leonard "Bones" McCoy | BG+ UB | pede BG · oferece UB, teletransporte | 69.5 |
| 16 | +3.0* | teorica | B | 2B | Elim Garak, Simple Tailor | UB+ | pede UB · oferece vida | 44.5 |
| 17 | +3.0* | teorica | B | B | General Chang, Cold Warrior | BR+ WG | pede BR, klingons · oferece WG, klingons, oficiais | 69.9 |
| 18 | +3.0* | teorica | BR | 2BR | Gowron, Eager for Battle | BR+ WG | pede BR, klingons · oferece WG, klingons | 44.9 |
| 19 | +3.0* | teorica | B | 2B | Grand Nagus Zek | BR+ | pede BR, tesouros · oferece tesouros | 50.4 |
| 20 | +3.0* | teorica | U | 1U | Gwyndala, the Progeny | BR | pede equipamentos, fichas · oferece BR, teletransporte | 52.2 |
| 21 | +3.0* | teorica | G | 2GG | Holo-Engineer | BR WB WR | pede fichas · oferece BR, WB, WR, fichas, teletransporte | 100.2 |
| 22 | +3.0* | teorica | B | 1B | Kai Winn, Faithless Leader | BR | oferece BR | 4.2 |
| 23 | +3.0* | teorica | WR | 1RW | Kira Nerys, Firebrand | WU WR | pede fichas · oferece WR, WU | 37.8 |
| 24 | +3.0* | teorica | R | 1R | Lwaxana Troi, Charming Guest | BR | oferece BR | 4.1 |
| 25 | +3.0* | teorica | G | G | MACO Strike Team | BR WR | oferece BR, WR, fichas, oficiais | 46.2 |
| 26 | +3.0* | teorica | W | 2W | Miles O'Brien, Transporter Ops |  | pede teletransporte · oferece teletransporte | 49.3 |
| 27 | +3.0* | teorica | BG | BG | Nog, Ambitious Cadet | BG+ BR RG UG | pede BG, virar · oferece BR, RG, UG | 63.6 |
| 28 | +3.0* | teorica | U | 2U | Nyota Uhura, Communications |  | oferece oficiais | 2.2 |
| 29 | +3.0* | teorica | B | 2B | Overflow Submatrix | WB+ BG+ | pede BG, WB | 101.4 |
| 30 | +3.0* | teorica | W | 3W | Primary Unimatrix Adjunct | WB+ | pede WB | 49.5 |
| 31 | +3.0* | teorica | B | 1B | Salt Vampire | BR | oferece BR, teletransporte, vida | 17 |
| 32 | +3.0* | teorica | WUG | 1GWU | Sarek, Federation Ambassador | WG | oferece WG | 2.2 |
| 33 | +3.0* | teorica | U | 2U | Subcommander T'Pol | UB | oferece UB, teletransporte | 19.5 |
| 34 | +3.0* | teorica | W | 1W | Sulu, Space Swashbuckler | BR | pede equipamentos, virar · oferece BR | 31.1 |
| 35 | +3.0* | teorica | R | 1R | Tasha Yar, Out of Time | BG+ BR | pede BG · oferece BR, fichas, oficiais | 83.7 |
| 36 | +3.0* | teorica | W | 2W | Troubling Tribbles |  | oferece fichas | 16 |
| 37 | +3.0* | teorica | R | 3R | Will Riker, First in the Field | WU RG WR UG | oferece RG, UG, WR, WU, oficiais | 30.6 |
| 38 | +3.0* | teorica | R | 2R | Worf, Intelligence Contractor |  | oferece klingons, teletransporte | 12.8 |
| 39 | +2.5* | teorica | UG | 3GU | All Good Things... |  | oferece vida | 1.7 |
| 40 | +2.5* | teorica | R | RR | Brazen Bluff | UR+ | pede UR | 63.1 |
| 41 | +2.5* | teorica | R | 1R | D-7 Battle Cruiser | WU BR WB WR | oferece BR, WB, WR, WU, fichas, klingons, virar | 81 |
| 42 | +2.5* | teorica | R | XRRR | Dominion Infiltration | UR | oferece UR, fichas | 30.2 |
| 43 | +2.5* | teorica | W | 1W | Federation Resupply | WU+ UR BG | pede WU, equipamentos, teletransporte · oferece BG, UR | 112.8 |
| 44 | +2.5* | teorica | G | 2G | Genesis Device | RG UG | oferece RG, UG | 23 |
| 45 | +2.5* | teorica | U | 4U | H.M.S. Bounty, Unlikely Timeship | WU WB | oferece WB, WU, virar | 31.8 |
| 46 | +2.5* | teorica | RG | 1RG | Hit It! | WR | oferece WR | 10.2 |
| 47 | +2.5* | teorica | UB | 1UB | Mirror Universe Intrusion | UR | oferece UR, fichas | 19 |
| 48 | +2.5* | teorica | W | 3W | Peace in Our Time |  |  |  |
| 49 | +2.5* | teorica | - | 2 | Replicator |  | pede fichas · oferece vida | 41.2 |
| 50 | +2.5* | teorica | U | 1U | Romulan Bird-of-Prey | UR+ WU WB | pede UR · oferece WB, WU, virar | 96.4 |
| 51 | +2.5* | teorica | G | 2G | Stable Wormhole | RG UG | oferece RG, UG | 23 |
| 52 | +2.5* | teorica | WB | 3WB | The City on the Edge of Forever | BR+ WR | pede BR · oferece WR, fichas, vida | 52.8 |
| 53 | +2.5* | teorica | WG | 3GW | The Inner Light | BG+ | pede BG · oferece tesouros, vida | 30.3 |
| 54 | +2.5* | teorica | W | 1W | The Needs of the Many | BR+ UR | pede BR · oferece UR | 60.2 |
| 55 | +2.5* | teorica | G | 3GG | U.S.S. Discovery, at Black Alert | WU WB | oferece WB, WU, virar | 31 |
| 56 | +2.5* | teorica | - | 3 | U.S.S. Enterprise-D, Galaxy-Class | WU WB | oferece WB, WU, virar | 34 |
| 57 | +2.5* | teorica | B | 2BB | U.S.S. Reliant, From Hell's Heart | BG+ WU WB | pede BG · oferece WB, WU, virar | 83.6 |
| 58 | +2.5* | teorica | UR | 1UR | Year of Hell |  |  |  |
| 59 | +1.5* | teorica | G | 6GG | Branching Timeline | UG+ UR | pede UG · oferece UR | 69.2 |
| 60 | +1.5* | teorica | U | 4UU | Deep Space Scan | UG+ UR | pede UG · oferece UR | 70 |
| 61 | +1.5* | teorica | WU | 5WU | Live Long and Prosper | UR | oferece UR | 9 |
| 62 | +1.5* | teorica | R | 5RR | Pah-Wraith | WR+ UG+ WU | pede UG, WR · oferece WU | 102.9 |
| 63 | +1.5* | teorica | U | 5U | The Caretaker | UB+ WU WR | pede UB · oferece WR, WU | 48.7 |
| 64 | +1.5* | teorica | - | 7 | The Holodeck | BG+ | pede BG | 53 |
| 65 | -1.5* | teorica | - |  | Blood Crypt | UG | oferece UG | 14 |
| 66 | -1.5* | teorica | - |  | Breeding Pool | UG | oferece UG | 14 |
| 67 | -1.5* | teorica | - |  | Federation Outpost | UB BG UG | oferece BG, UB, UG, vida | 54.2 |
| 68 | -1.5* | teorica | - |  | Godless Shrine | UG | oferece UG | 14 |
| 69 | -1.5* | teorica | - |  | Hallowed Fountain | UG | oferece UG | 14 |
| 70 | -1.5* | teorica | - |  | Ni'Var Science Academy | UB BG UG | oferece BG, UB, UG | 52 |
| 71 | -1.5* | teorica | - |  | Overgrown Tomb | UG | oferece UG | 14 |
| 72 | -1.5* | teorica | - |  | Q Continuum | UB BG UG | oferece BG, UB, UG | 52 |
| 73 | -1.5* | teorica | - |  | Quark's Bar | UB BG UG | oferece BG, UB, UG | 52 |
| 74 | -1.5* | teorica | - |  | Sacred Foundry | UG | oferece UG | 14 |
| 75 | -1.5* | teorica | - |  | Steam Vents | UG | oferece UG | 14 |
| 76 | -1.5* | teorica | - |  | Stomping Ground | UG | oferece UG | 14 |
| 77 | -1.5* | teorica | - |  | Temple Garden | UG | oferece UG | 14 |
| 78 | -1.5* | teorica | - |  | The Unicomplex | BG+ UB UG | pede BG · oferece UB, UG | 76 |
| 79 | -1.5* | teorica | - |  | Watery Grave | UG | oferece UG | 14 |

### Incomuns (110)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +3.0* | teorica | B | 3B | Blastoneuron | BG+ BR | pede BG · oferece BR, fichas, teletransporte, vida | 95.4 |
| 2 | +3.0* | teorica | B | 2B | Commander Raffi Musiker | UB | oferece UB, oficiais, teletransporte, vida | 24 |
| 3 | +3.0* | teorica | W | 3W | Ghost of Illyria |  | pede teletransporte · oferece teletransporte | 49.3 |
| 4 | +3.0* | teorica | WR | 1RW | Kirk, Commanding Officer | WR+ | pede WR · oferece oficiais | 29.6 |
| 5 | +3.0* | teorica | WB | WB | Locutus, the One Who Speaks | WB+ WR+ BR | pede WB, WR · oferece BR, vida | 66.8 |
| 6 | +3.0* | teorica | R | 1R | Munitions Enthusiast | BR | oferece BR, klingons | 18.5 |
| 7 | +2.5* | teorica | W | 1W | 70,000 Light-Years from Home | UR | oferece UR | 12.8 |
| 8 | +2.5* | teorica | G | 2G | Amok Time | BG+ | pede BG · oferece vida | 53 |
| 9 | +2.5* | teorica | U | 1U | Energize | UR BG | pede teletransporte · oferece BG, UR | 81.3 |
| 10 | +2.5* | teorica | B | 2B | Impossible Choice | UB UR | oferece UB, UR, oficiais | 24 |
| 11 | +2.5* | teorica | B | 1B | Resistance Is Futile | WB+ BG+ UB UR | pede BG, WB · oferece UB, UR | 123.1 |
| 12 | +2.5* | teorica | G | G | Test of Courage | UB UR BG | oferece BG, UB, UR, vida | 52.2 |
| 13 | +2.5* | teorica | B | B | Test of Loyalty | BG+ UB UR | pede BG · oferece UB, UR | 72.9 |
| 14 | +2.5* | teorica | U | 1U | Test of Priorities | UB UR BG | pede teletransporte · oferece BG, UB, UR | 90.3 |
| 15 | +2.5* | teorica | W | 2W | The Measure of a Man |  | oferece vida | 2.2 |
| 16 | +2.5* | teorica | R | 1R | Transporter Malfunction | UR BG | pede teletransporte · oferece BG, UR | 80.2 |
| 17 | +2.5* | teorica | W | 3W | U.S.S. Excelsior, Cutting Edge | WU WB | oferece WB, WU, virar | 33.2 |
| 18 | +1.0* | teorica | R | 2R | Academy Instructor | UR+ BR WR | pede UR, fichas, oficiais · oferece BR, WR, fichas, oficiais | 175.8 |
| 19 | +1.0* | teorica | W | 1W | Assembly Specialist | BR WB WR | oferece BR, WB, WR, fichas, teletransporte | 75.2 |
| 20 | +1.0* | teorica | R | 1R | Beckett Mariner, Impetuous Ensign | BR | pede virar · oferece BR, oficiais | 30.8 |
| 21 | +1.0* | teorica | W | 1W | Brad Boimler, Eager Ensign | WG+ BR | pede WG, virar · oferece BR, oficiais, vida | 67.1 |
| 22 | +1.0* | teorica | R | 2R | Captain Michael Burnham | RG+ WG | pede RG · oferece WG, oficiais | 40 |
| 23 | +1.0* | teorica | RG | 2R/GR/G | Cleveland Booker, Empath | RG+ WR+ BR | pede RG, WR · oferece BR, fichas | 71.9 |
| 24 | +1.0* | teorica | B | 1B | Collective Drone | WB+ BR | pede WB · oferece BR | 54.5 |
| 25 | +1.0* | teorica | W | W | Command Subadjunct | WB+ BR | pede WB · oferece BR | 53.4 |
| 26 | +1.0* | teorica | G | 3G | Culber and Stamets, Star-Crossed | UB WG | oferece UB, WG, teletransporte | 27.8 |
| 27 | +1.0* | teorica | B | 2B | D'Ghor Bloodletter | UB | oferece UB, klingons, teletransporte | 21.8 |
| 28 | +1.0* | teorica | UG | 1G/UG/U | D'Vana Tendi, Optimistic Ensign | BG | oferece BG, virar | 19 |
| 29 | +1.0* | teorica | RG | 1RG | Dal R'El, Augment Orphan | RG+ | pede RG | 27.2 |
| 30 | +1.0* | teorica | BG | 2B/GB/G | Daniels, Temporal Agent | BG+ | pede BG · oferece teletransporte, vida | 40.6 |
| 31 | +1.0* | teorica | U | 1U | Data, New Life | BR WG WB | oferece BR, WB, WG | 26.7 |
| 32 | +1.0* | teorica | G | 2G | David and Carol Marcus, Creators | RG UG | oferece RG, UG, teletransporte | 33.5 |
| 33 | +1.0* | teorica | W | 2WW | Dr. McCoy, Surly Surgeon | WG+ | pede WG · oferece teletransporte | 44 |
| 34 | +1.0* | teorica | U | 3U | Ensign Pavel Chekov | UG+ | pede UG · oferece teletransporte | 66.2 |
| 35 | +1.0* | teorica | R | 3R | Erica Ortegas, Plucky Pilot | RG | pede virar · oferece RG | 33.5 |
| 36 | +1.0* | teorica | UR | 2U/RU/R | Gray and Adira, Forever Joined | UR+ BR | pede UR · oferece BR, fichas, oficiais | 60.5 |
| 37 | +1.0* | teorica | WU | WU | Hemmer, Fixing What Is Broken | WU+ BR BG | pede WU, virar · oferece BG, BR | 51.3 |
| 38 | +1.0* | teorica | W | 2W | Hologram Janeway | WR+ WG WB | pede WR · oferece WB, WG, oficiais | 72.4 |
| 39 | +1.0* | teorica | G | 1G | Jake Sisko, War Correspondent | RG+ BR | pede RG · oferece BR, vida | 36.9 |
| 40 | +1.0* | teorica | U | 1U | Jett Reno, Problem Solver | UB+ BR WG BG | pede UB, virar · oferece BG, BR, WG | 104.7 |
| 41 | +1.0* | teorica | BR | 1BR | L'Rell, Fierce Visionary | BR+ BG WR | pede BR · oferece BG, WR, fichas, klingons | 73.7 |
| 42 | +1.0* | teorica | R | 2RR | La'An Noonien-Singh, Security | WR+ WU | pede WR · oferece WU | 47.5 |
| 43 | +1.0* | teorica | UB | 1U/BU/B | Lore, Positronic Provocateur | UB WB BG | oferece BG, UB, WB, teletransporte | 44.7 |
| 44 | +1.0* | teorica | G | 1G | Neelix, Moral Support | BR WG | pede vida · oferece BR, WG, teletransporte, vida | 50.8 |
| 45 | +1.0* | teorica | B | 2B | Organic Avulsion Unit | WB+ | pede WB | 50.2 |
| 46 | +1.0* | teorica | WG | 2GW | Phlox, Unorthodox Doctor | WG+ | pede WG | 26.4 |
| 47 | +1.0* | teorica | W | 1W | Picard, Leading by Example | BR | oferece BR, oficiais | 6.1 |
| 48 | +1.0* | teorica | W | 2W | Rutherford, Upgraded Ensign | WU+ WB+ WG | pede WB, WU · oferece WG, teletransporte | 99.2 |
| 49 | +1.0* | teorica | G | 2G | Saru, Unthreatened |  | oferece oficiais, teletransporte | 12.8 |
| 50 | +1.0* | teorica | UB | 2UB | Seven of Nine | UB+ WB | pede UB · oferece WB | 43.9 |
| 51 | +1.0* | teorica | UR | UR | Spock, Always Your Friend | UR+ BR | pede UR · oferece BR, teletransporte | 49.9 |
| 52 | +1.0* | teorica | B | B | Storied Veteran | BR BG | oferece BG, BR, klingons | 34.8 |
| 53 | +1.0* | teorica | G | 2G | Sylvia Tilly, Joy of Discovery | BG+ WG | pede BG · oferece WG, teletransporte | 70.2 |
| 54 | +1.0* | teorica | R | 2R | Targ Wrangler | BR+ WU WR | pede BR · oferece WR, WU, klingons | 58.2 |
| 55 | +1.0* | teorica | BR | B/RB/R | The Duras Sisters | BR WR | oferece BR, WR, fichas, klingons | 38 |
| 56 | +1.0* | teorica | UG | GU | The Traveler | UG+ BR | pede UG · oferece BR | 50.4 |
| 57 | +1.0* | teorica | BG | 1BG | Vash, Freelance Archaeologist | BG+ | pede BG | 34.6 |
| 58 | +1.0* | teorica | WR | R/WR/W | Worf, Honor-Bound Warrior | WR+ BR WG | pede WR, fichas · oferece BR, WG, klingons, oficiais, virar | 64.9 |
| 59 | +1.0* | teorica | U | 2U | Zefram Cochrane, Warp Pioneer | WU+ WB+ | pede WB, WU | 78.1 |
| 60 | +1.0* | teorica | WB | 1W/BW/B | Zero, Incorporeal Sensate | WB | oferece WB, teletransporte, vida | 24 |
| 61 | +0.5* | teorica | G | 2G | Adversary by Algorithm | BR WB UR BG WR | pede teletransporte · oferece BG, BR, UR, WB, WR, fichas | 141.8 |
| 62 | +0.5* | teorica | U | 2U | Anthropological Mission | UR+ BG | pede UR · oferece BG | 90.6 |
| 63 | +0.5* | teorica | B | 2B | Bat'leth | UR | pede fichas · oferece UR, equipamentos | 51.8 |
| 64 | +0.5* | teorica | - | 3 | Combadge | UR | pede fichas · oferece UR, equipamentos | 54.8 |
| 65 | +0.5* | teorica | W | 2W | Conquest Mission | WB+ BR WR | pede WB · oferece BR, WR, fichas | 97.2 |
| 66 | +0.5* | teorica | WU | 3W/UW/U | Constable Odo | WU UB WR | oferece UB, WR, WU, teletransporte | 17.2 |
| 67 | +0.5* | teorica | B | 1B | De-evolve | BG+ UR | pede BG · oferece UR | 63.9 |
| 68 | +0.5* | teorica | U | 4U | Dominion Saboteur |  |  |  |
| 69 | +0.5* | teorica | U | 3U | Enterprise NX-01 | WU WB | oferece WB, WU, virar | 31.8 |
| 70 | +0.5* | teorica | R | 2RR | Exploratory Mission | RG+ | pede RG | 30.2 |
| 71 | +0.5* | teorica | B | 4B | Gabriel Lorca, Mirror Menace | UB+ BG+ WU WR | pede BG, UB · oferece WR, WU, oficiais | 101.4 |
| 72 | +0.5* | teorica | U | 1U | Highly Illogical | UR | oferece UR | 14.2 |
| 73 | +0.5* | teorica | B | 4B | Hive Mind Coprocessor | WB+ WU WR | pede WB · oferece WR, WU | 56 |
| 74 | +0.5* | teorica | U | 4U | Hoshi Sato, Exolinguist |  | oferece teletransporte | 10.5 |
| 75 | +0.5* | teorica | B | 3BB | In the Pale Moonlight | BR+ WR | pede BR · oferece WR, fichas | 78 |
| 76 | +0.5* | teorica | - | 2 | Isolinear Processor | WB+ BG | pede WB · oferece BG | 80 |
| 77 | +0.5* | teorica | R | XR | Khaaaaaaaaaaaannn! | UR | oferece UR | 14.2 |
| 78 | +0.5* | teorica | R | 4R | Khan, Despot by Design | WU WR | oferece WR, WU, teletransporte | 16.6 |
| 79 | +0.5* | teorica | G | 3GG | Mugato | WU WR | oferece WR, WU | 5.7 |
| 80 | +0.5* | teorica | R | 2R | Red Alert! | WR+ UR | pede WR · oferece UR | 59.7 |
| 81 | +0.5* | teorica | U | 3UU | Rules of Acquisition | UB UR | oferece UB, UR | 23.2 |
| 82 | +0.5* | teorica | W | 4W | Saavik, Stoic Student |  | oferece teletransporte | 10.5 |
| 83 | +0.5* | teorica | R | 2R | Sarcophagus, Ship of the Dead | BR+ WR+ WU WB | pede BR, WR · oferece WB, WU, virar | 125.6 |
| 84 | +0.5* | teorica | - | 5 | Sickbay | WG | pede fichas, vida · oferece WG, vida | 77.2 |
| 85 | +0.5* | teorica | G | 2G | Support Mission | WG | pede fichas · oferece WG | 44.2 |
| 86 | +0.5* | teorica | G | 4G | Syndicate Liquidators | RG+ WU WG WR | pede RG · oferece WG, WR, WU | 45.7 |
| 87 | +0.5* | teorica | B | 1B | Tell Me What You See | UB+ BG | pede UB · oferece BG | 70.5 |
| 88 | +0.5* | teorica | W | 1W | Test of Conviction | UB WG UR | oferece UB, UR, WG | 30 |
| 89 | +0.5* | teorica | R | 1R | Test of Identity | UB UR BG | pede klingons · oferece BG, UB, UR | 60.5 |
| 90 | +0.5* | teorica | WG | 3G/WG/W | The Doctor, EMH | WG+ WB | pede WG · oferece WB, teletransporte | 41.7 |
| 91 | +0.5* | teorica | R | 1R | The Naked Time | RG WG UG | pede fichas · oferece RG, UG, WG | 67.2 |
| 92 | +0.5* | teorica | W | 1W | There's Coffee in that Nebula | UR BG | pede teletransporte · oferece BG, UR | 80.6 |
| 93 | +0.5* | teorica | U | 2U | Those Old Scientists | UR+ BG+ | pede BG, UR | 115.4 |
| 94 | +0.5* | teorica | - | 2 | Type-2 Phaser | UR | pede fichas · oferece UR, equipamentos | 54.8 |
| 95 | +0.5* | teorica | - | 5 | U.S.S. Cerritos, Following Up | WU BR WB WR | oferece BR, WB, WR, WU, fichas, oficiais, virar | 86.2 |
| 96 | +0.5* | teorica | G | 3G | U.S.S. Voyager, Lone Wanderer | WU RG WB UG | oferece RG, UG, WB, WU, virar | 54 |
| 97 | +0.5* | teorica | W | 4W | Una Chin-Riley, Number One | WR+ WU | pede WR · oferece WU, oficiais | 48.6 |
| 98 | +0.5* | teorica | B | 2B | Vengeance Mission | BR+ | pede BR | 48.7 |
| 99 | +0.5* | teorica | U | U | Vulcan Mind-Meld | UR | oferece UR | 14.2 |
| 100 | +0.5* | teorica | G | 2G | Warp Speed | UG+ RG | pede UG · oferece RG | 65.5 |
| 101 | -0.5* | teorica | U | 8U | Cloak and Phaser | UG+ BR UR BG WR | pede UG · oferece BG, BR, UR, WR, fichas | 139.2 |
| 102 | -0.5* | teorica | G | 4GG | Hologram Stalker | BG+ BR WB WR | pede BG · oferece BR, WB, WR, fichas, teletransporte | 120.8 |
| 103 | -0.5* | teorica | R | 5R | Ravenous Cosmozoan | UR+ BG+ | pede BG, UR | 112.4 |
| 104 | -0.5* | teorica | G | 4GG | Species 8472 | UG+ WU WR | pede UG · oferece WR, WU, teletransporte, vida | 75 |
| 105 | -0.5* | teorica | U | 6U | V'Ger, the Intruder | WU UB WB WR | oferece UB, WB, WR, WU | 30.2 |
| 106 | -1.5* | teorica | - |  | Artificial Anomaly | RG UG | oferece RG, UG, vida | 25.2 |
| 107 | -1.5* | teorica | - |  | Gaseous Anomaly | RG UG | oferece RG, UG | 23 |
| 108 | -1.5* | teorica | - |  | Spatial Anomaly | RG UG | oferece RG, UG | 23 |
| 109 | -1.5* | teorica | - |  | Subspace Anomaly | BR RG WR UG | oferece BR, RG, UG, WR, fichas, oficiais | 75.2 |
| 110 | -1.5* | teorica | - |  | Temporal Anomaly | RG BG UG | oferece BG, RG, UG | 52 |

### Comuns (91)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +2.0* | teorica | R | 3R | Dahar Master | BR+ WU WR | pede BR · oferece WR, WU, klingons, teletransporte | 68.7 |
| 2 | +2.0* | teorica | G | 3G | Dominion Assault Force | WU UB BG WR | oferece BG, UB, WR, WU, teletransporte | 53.5 |
| 3 | +1.5* | teorica | W | 1W | Command Decision | UB UR | oferece UB, UR | 21 |
| 4 | +1.5* | teorica | B | 1B | Eject the Warp Core | BR+ UR | pede BR · oferece UR | 61.5 |
| 5 | +1.5* | teorica | R | 4R | Genesis Effect | RG UR UG | oferece RG, UG, UR | 36.5 |
| 6 | +1.5* | teorica | B | 3B | He's Dead, Jim | UR BG | oferece BG, UR | 41 |
| 7 | +1.5* | teorica | U | 4U | Interstellar Effigy | WU WB WR | oferece WB, WR, WU, teletransporte | 31.7 |
| 8 | +1.5* | teorica | W | 2W | Malfunctioning Holodeck |  |  |  |
| 9 | +1.5* | teorica | R | 1R | Perils of the Past | UB UR | oferece UB, UR | 22.5 |
| 10 | +1.5* | teorica | R | R | Planetary Bombardment | BR+ UR | pede BR · oferece UR | 64.1 |
| 11 | +1.5* | teorica | R | 2R | Plasma Cascade | UR BG | oferece BG, UR | 40.2 |
| 12 | +0.0* | teorica | W | 2W | Andromedan Automatons | WB | oferece WB, teletransporte | 27.5 |
| 13 | +0.0* | teorica | B | 3B | Assault Drone | WB+ WR+ | pede WB, WR | 94.2 |
| 14 | +0.0* | teorica | G | 1G | Astute Terraformer | UG+ BR | pede UG · oferece BR | 60.2 |
| 15 | +0.0* | teorica | B | 2B | Automated Warfare System | BR+ WB | pede BR · oferece WB | 65.7 |
| 16 | +0.0* | teorica | B | 1B | Battle-Scarred Survivalist | BR+ WG | pede BR · oferece WG, klingons | 58.5 |
| 17 | +0.0* | teorica | R | 2R | Cantankerous Captain | WR+ | pede WR · oferece oficiais | 47.7 |
| 18 | +0.0* | teorica | U | 3U | Cetacean Ops | UR+ WG | pede UR · oferece WG, oficiais | 74.4 |
| 19 | +0.0* | teorica | U | 1U | Cloistered Telepath | BR BG | oferece BG, BR, teletransporte | 40.2 |
| 20 | +0.0* | teorica | - | 2 | Cybernetic Specialist | BG+ BR WB | pede BG · oferece BR, WB, teletransporte | 84.8 |
| 21 | +0.0* | teorica | W | 3W | DOT-7 Repair Squad | WB | oferece WB, virar | 24.2 |
| 22 | +0.0* | teorica | G | 2G | Dominion Supervisor | WG+ | pede WG · oferece teletransporte | 43.2 |
| 23 | +0.0* | teorica | U | 3U | Emergency Holographic Crew | WU+ BG+ UB WB | pede BG, WU · oferece UB, WB, oficiais, teletransporte | 117.3 |
| 24 | +0.0* | teorica | W | W | Emergency Medical Hologram | BR WG WB | oferece BR, WB, WG, teletransporte, vida | 42.6 |
| 25 | +0.0* | teorica | W | 3W | Federation Field Medic | WG+ UB | pede WG · oferece UB, teletransporte | 52.2 |
| 26 | +0.0* | teorica | U | U | Federation Probe | UB BR WB BG | oferece BG, BR, UB, WB, teletransporte | 64.7 |
| 27 | +0.0* | teorica | B | 2B | Fugitive Listener |  | oferece teletransporte | 10.5 |
| 28 | +0.0* | teorica | U | 2U | Melkotian Adjudicator | UB+ WG | pede UB · oferece WG | 50.5 |
| 29 | +0.0* | teorica | G | G | Moopsy | BR | oferece BR | 3.7 |
| 30 | +0.0* | teorica | B | 3B | Obsidian Order Operative | UB+ | pede UB · oferece oficiais, vida | 46.8 |
| 31 | +0.0* | teorica | W | 2W | Pet Sehlat | WU WR | oferece WR, WU | 6.3 |
| 32 | +0.0* | teorica | R | 1R | Planetary Patrol | RG+ BR | pede RG · oferece BR | 34.3 |
| 33 | +0.0* | teorica | B | B | Relentless Drednok | BG+ BR WB | pede BG · oferece BR, WB, vida | 74.6 |
| 34 | +0.0* | teorica | G | 3G | Saurian Explorer | RG+ WU WR UG | pede RG · oferece UG, WR, WU | 50.7 |
| 35 | +0.0* | teorica | R | 1R | Savvy Profiteer | BR | oferece BR, tesouros | 5.1 |
| 36 | +0.0* | teorica | R | R | Starfleet Security | BR | oferece BR, oficiais | 6.3 |
| 37 | +0.0* | teorica | U | 1U | Starfleet Spanner Jockey | UR+ BR | pede UR · oferece BR | 68.3 |
| 38 | +0.0* | teorica | U | 2U | Suus Mahna Practitioner | UG+ | pede UG · oferece oficiais | 58 |
| 39 | +0.0* | teorica | W | 1W | Tactical Officer | WR+ BR WG | pede WR · oferece BR, WG, oficiais, virar | 66.5 |
| 40 | +0.0* | teorica | R | 2R | Tal Shiar Analyst | UR+ | pede UR | 63.1 |
| 41 | +0.0* | teorica | B | 1B | Tal Shiar Operative | UB BR BG | oferece BG, BR, UB, oficiais | 43.8 |
| 42 | +0.0* | teorica | G | 2G | Temporal Conqueror | BG+ RG | pede BG · oferece RG, teletransporte, tesouros | 71.2 |
| 43 | +0.0* | teorica | B | 1B | Tenacious Drone | BR WB WR | oferece BR, WB, WR, fichas | 63.2 |
| 44 | +0.0* | teorica | W | 1W | Vexing Drone | BR WB | oferece BR, WB, teletransporte | 31.4 |
| 45 | +0.0* | teorica | G | 1G | Xenobotanist | BR | oferece BR | 3.7 |
| 46 | +0.0* | teorica | G | 2G | Xindi Surveyors | RG+ WG | pede RG · oferece WG | 40 |
| 47 | -0.5* | teorica | B | B | A Good Day to Die | UR | oferece UR | 12.8 |
| 48 | -0.5* | teorica | R | 1R | Boarding Action | BR UR BG WR | pede teletransporte · oferece BG, BR, UR, WR, fichas, klingons | 130.9 |
| 49 | -0.5* | teorica | R | 1R | Captain's Tutelage | UR | oferece UR | 14.2 |
| 50 | -0.5* | teorica | B | 4B | Cha'DIch Investigator | WU BR WR | oferece BR, WR, WU, fichas, klingons, teletransporte | 61.1 |
| 51 | -0.5* | teorica | - | 3 | Class-F Shuttlecraft | WU WB | oferece WB, WU, virar | 34 |
| 52 | -0.5* | teorica | G | 1G | Common Goal | UR | oferece UR | 12.8 |
| 53 | -0.5* | teorica | U | 2U | Consider the Prime Directive | UB UR | oferece UB, UR | 23.2 |
| 54 | -0.5* | teorica | G | 2G | Dathon and Picard at El-Adrel | UB UR | oferece UB, UR | 21 |
| 55 | -0.5* | teorica | G | 2G | Final Frontier | RG UR BG UG | pede teletransporte · oferece BG, RG, UG, UR | 105.3 |
| 56 | -0.5* | teorica | G | 1G | First Contact | UR BG | oferece BG, UR, vida | 44 |
| 57 | -0.5* | teorica | W | 3WW | Free Borg Revolutionaries | WR+ WU RG WB UG | pede WR · oferece RG, UG, WB, WU, teletransporte | 94.6 |
| 58 | -0.5* | teorica | U | 3U | Guidance Failure | UR | oferece UR | 14.2 |
| 59 | -0.5* | teorica | G | G | I'm a Doctor, Not a . . . | WG UR | oferece UR, WG, virar | 29 |
| 60 | -0.5* | teorica | U | 3U | Make It So | UB BR UR WR | oferece BR, UB, UR, WR, fichas, oficiais, virar | 76 |
| 61 | -0.5* | teorica | U | U | Marooned | UR | oferece UR | 14.2 |
| 62 | -0.5* | teorica | W | 1W | Oberth-Class Starship | WU RG WB UG | oferece RG, UG, WB, WU, virar | 54 |
| 63 | -0.5* | teorica | U | U | Open Communications | UR BG | pede teletransporte · oferece BG, UR | 81.3 |
| 64 | -0.5* | teorica | B | 1B | Pattern Buffer Preservation | UR BG | pede teletransporte · oferece BG, UR | 82.1 |
| 65 | -0.5* | teorica | G | 4G | Photosynthetic Physician | BG+ WU BR WR | pede BG · oferece BR, WR, WU, fichas, oficiais | 99.1 |
| 66 | -0.5* | teorica | W | 1W | Pure Energy | WG UR BG | pede teletransporte · oferece BG, UR, WG | 89.6 |
| 67 | -0.5* | teorica | R | 1R | Reckless Impulse | UR | oferece UR | 14.2 |
| 68 | -0.5* | teorica | W | W | Set Phasers to . . . | UB UR | oferece UB, UR | 21 |
| 69 | -0.5* | teorica | W | 1W | Shields Up! | WG UR | oferece UR, WG | 21.8 |
| 70 | -0.5* | teorica | W | 4W | Shuttle Ace | WU WR | pede virar · oferece WR, WU, vida | 33.8 |
| 71 | -0.5* | teorica | R | 4R | Silicate Surveyor | WU WR | oferece WR, WU, teletransporte | 16.6 |
| 72 | -0.5* | teorica | B | 2B | Stray from History | WU+ BG+ UB UR | pede BG, WU · oferece UB, UR | 102.4 |
| 73 | -0.5* | teorica | U | 2U | Suurok-Class Science Vessel | WU WB | oferece WB, WU, virar | 31.8 |
| 74 | -0.5* | teorica | - | 2 | Tea, Earl Grey, Hot | UB | oferece UB, vida | 11.2 |
| 75 | -0.5* | teorica | - | 1 | Tricorder | UR BG | pede fichas · oferece BG, UR, equipamentos | 83.8 |
| 76 | -0.5* | teorica | - | 2 | Warp Core | WU+ RG UG | pede WU · oferece RG, UG | 53.2 |
| 77 | -1.5* | teorica | - |  | Andoria | UG | oferece UG, vida | 16.2 |
| 78 | -1.5* | teorica | - |  | Bajor | UG | oferece UG, vida | 16.2 |
| 79 | -1.5* | teorica | - |  | Cardassia Prime | UG | oferece UG, vida | 16.2 |
| 80 | -1.5* | teorica | G | 4GG | Cold-Blooded Crew | WU RG WG WR UG | oferece RG, UG, WG, WR, WU, teletransporte | 48.2 |
| 81 | -1.5* | teorica | - |  | Earth, Sector 001 | UG | oferece UG, vida | 16.2 |
| 82 | -1.5* | teorica | - |  | Ferenginar | UG | oferece UG, vida | 16.2 |
| 83 | -1.5* | teorica | R | 4RR | Horta | WU RG WR UG | oferece RG, UG, WR, WU | 28.4 |
| 84 | -1.5* | teorica | U | 4UU | Humpback Whales | WU RG WR UG | oferece RG, UG, WR, WU | 27.2 |
| 85 | -1.5* | teorica | - |  | Orion | UG | oferece UG, vida | 16.2 |
| 86 | -1.5* | teorica | - |  | Qo'noS | UG | oferece UG, vida | 16.2 |
| 87 | -1.5* | teorica | - |  | Risa | UG | oferece UG, vida | 16.2 |
| 88 | -1.5* | teorica | B | 4BB | Rogue Artificial Intelligence | WU UB RG WB BG WR UG | oferece BG, RG, UB, UG, WB, WR, WU, teletransporte, vida | 93.5 |
| 89 | -1.5* | teorica | - |  | Romulus | UG | oferece UG, vida | 16.2 |
| 90 | -1.5* | teorica | - |  | Unexplored Territory | RG UG | oferece RG, UG | 23 |
| 91 | -1.5* | teorica | - |  | Vulcan | UG | oferece UG, vida | 16.2 |

## 2. Depois da primeira escolha: os melhores segundos picks

Para cada rara ou mítica, em ordem de poder, as cartas da coleção que o motor mais quer no
P1P2 (nota = poder + parceiros + o pouco de encaixe que o pick 2 já pesa). Para o terceiro
pick em diante: `mtg draft map trk --card "Primeira" --card "Segunda"`, ou o motor ao
vivo (`mtg draft watch`, Oráculo).

**Borg Cube** (M, WB, {5}{W}{B}, +5.0* teorica) · WB+ WU · pede WB · oferece WU, virar
- +3.1 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Borg Cube 1
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.8 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.3 · encaixe +0.1 ↔ Borg Cube 0.5

**Crystalline Entity** (M, -, {8}, +5.0* teorica) · WU WB WR · oferece WB, WR, WU, teletransporte
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Crystalline Entity 0.75
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Crystalline Entity 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Infinite Diversity** (M, R, {7}{R}{R}, +5.0* teorica) · UR+ BG+ · pede BG, UR
- +3.6 Plasma Cascade (?, R) poder +2.0* · parceiros +1.2 · encaixe +0.1 ↔ Infinite Diversity 2
- +3.6 Transporter Malfunction (?, R) poder +2.0* · parceiros +1.2 · encaixe +0.1 ↔ Infinite Diversity 2
- +3.3 Test of Courage (?, G) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Infinite Diversity 2
- +3.3 Energize (?, U) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Infinite Diversity 2
- +3.3 Test of Priorities (?, U) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Infinite Diversity 2
- +3.3 He's Dead, Jim (?, B) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Infinite Diversity 2

**Sela, Tal Shiar Paradox** (R, B, {3}{B}, +5.0* teorica) · BG+ BR WR · pede BG · oferece BR, WR, fichas
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.3 · encaixe +0.1 ↔ Sela, Tal Shiar Paradox 0.5
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Sela, Tal Shiar Paradox 1
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Sela, Tal Shiar Paradox 1
- +3.0 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Sela, Tal Shiar Paradox 1
- +3.0 He's Dead, Jim (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Sela, Tal Shiar Paradox 1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1

**Wesley Crusher, Starfleet Cadet** (R, U, {2}{U}{U}, +5.0* teorica) · UB · oferece UB, oficiais, teletransporte
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Wesley Crusher, Starfleet Cadet 0.75
- +2.9 Energize (?, U) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Wesley Crusher, Starfleet Cadet 0.75
- +2.9 Test of Priorities (?, U) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Wesley Crusher, Starfleet Cadet 0.75
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Captain James T. Kirk** (M, R, {2}{R}, +4.5* teorica) · WR+ UB BR BG · pede WR · oferece BG, BR, UB, fichas, oficiais
- +3.8 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +1.2 · encaixe -0.2 ↔ Captain James T. Kirk 2
- +3.7 Dahar Master (?, R) poder +2.5* · parceiros +0.8 · encaixe +0.1 ↔ Captain James T. Kirk 1.25
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Captain James T. Kirk 1
- +3.1 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Captain James T. Kirk 1
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.8 Captain Benjamin Sisko (?, W) poder +0.5* · parceiros +2.2 · encaixe -0.2 ↔ Captain James T. Kirk 3.75

**Captain Jean-Luc Picard** (M, W, {2}{W}, +4.5* teorica) · WU+ WR+ BR · pede WR, WU, fichas, oficiais · oferece BR, fichas, oficiais, virar
- +3.8 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +1.2 · encaixe -0.2 ↔ Captain Jean-Luc Picard 2
- +3.5 Dahar Master (?, R) poder +2.5* · parceiros +0.9 · encaixe -0.2 ↔ Captain Jean-Luc Picard 1.5
- +3.3 The Destruction of Praxis (?, B) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Captain Jean-Luc Picard 2
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Captain Jean-Luc Picard 1
- +3.1 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Captain Jean-Luc Picard 1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Captain Jean-Luc Picard 0.75

**Captain Kathryn Janeway** (M, G, {3}{G}, +4.5* teorica) · RG WG UG · oferece RG, UG, WG, oficiais
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Captain Kathryn Janeway 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Dr. Beverly Crusher** (M, W, {2}{W}, +4.5* teorica) · WG · pede vida · oferece WG
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Dr. Beverly Crusher 0.75
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Dr. Beverly Crusher 0.75
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 The Measure of a Man (?, W) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Dr. Beverly Crusher 0.75
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Dr. Joseph M'Benga** (M, G, {2}{G}{G}, +4.5* teorica) · WG+ · pede WG
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Encounter the Unknown** (R, R, {1}{R}{R}, +4.5* teorica) · UB UR · oferece UB, UR
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Engineered Explosives** (R, -, {X}, +4.5* teorica)
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Jadzia Dax, Living Legacy** (M, G, {1}{G}, +4.5* teorica) · WG+ BR · pede WG · oferece BR
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Jadzia Dax, Living Legacy 0.25
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Khan, Vengeful Heart** (M, B, {2}{B}{B}, +4.5* teorica) · BR+ WU WR · pede BR · oferece WR, WU, teletransporte
- +3.5 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Khan, Vengeful Heart 1
- +3.5 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Khan, Vengeful Heart 1
- +3.2 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Khan, Vengeful Heart 1
- +3.1 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Khan, Vengeful Heart 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Khan, Vengeful Heart 0.75
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1

**Lieutenant Commander Data** (M, U, {2}{U}, +4.5* teorica) · WG+ UR+ WB · pede UR, WG · oferece WB
- +3.3 Resistance Is Futile (?, B) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Lieutenant Commander Data 2
- +3.1 Energize (?, U) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Lieutenant Commander Data 1
- +3.1 Test of Priorities (?, U) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Lieutenant Commander Data 1
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Lieutenant Commander Data 1
- +2.7 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Lieutenant Commander Data 1

**Lt. Cmdr. Geordi La Forge** (M, U, {2}{U}, +4.5* teorica) · WU+ · pede WU
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Lt. Cmdr. Geordi La Forge 0.25
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Lt. Cmdr. Geordi La Forge 0.25
- +2.7 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Lt. Cmdr. Geordi La Forge 1
- +2.6 Interstellar Effigy (?, U) poder +2.0* · parceiros +0.1 · encaixe +0.1 ↔ Lt. Cmdr. Geordi La Forge 0.25
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Mr. Spock, Science Officer** (M, U, {2}{U}{U}, +4.5* teorica)
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Q, Stacking the Deck** (M, R, {2}{R}{R}, +4.5* teorica) · WU WR · oferece WR, WU, teletransporte
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Q, Stacking the Deck 0.75
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Transporter Malfunction (?, R) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Q, Stacking the Deck 0.75
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Quark, Humble Proprietor** (M, R, {2}{R}, +4.5* teorica) · pede tesouros · oferece tesouros
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Scotty, Miracle Worker** (M, U, {1}{U}{U}, +4.5* teorica) · UR+ BG+ · pede BG, UR, teletransporte
- +3.7 Energize (?, U) poder +2.0* · parceiros +1.2 · encaixe +0.1 ↔ Scotty, Miracle Worker 2
- +3.7 Test of Priorities (?, U) poder +2.0* · parceiros +1.2 · encaixe +0.1 ↔ Scotty, Miracle Worker 2
- +3.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +1.1 · encaixe -0.2 ↔ Scotty, Miracle Worker 1.75
- +3.4 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.5 · encaixe +0.1 ↔ Scotty, Miracle Worker 0.75
- +3.3 Blastoneuron (?, B) poder +2.5* · parceiros +0.8 · encaixe -0.2 ↔ Scotty, Miracle Worker 1.25
- +3.3 Test of Courage (?, G) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Scotty, Miracle Worker 2

**Seven of Nine, Unassimilated** (M, U, {1}{U}, +4.5* teorica) · UG+ BR WB BG · pede UG · oferece BG, BR, WB, oficiais
- +3.3 Resistance Is Futile (?, B) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Seven of Nine, Unassimilated 2
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Seven of Nine, Unassimilated 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Seven of Nine, Unassimilated 1
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Seven of Nine, Unassimilated 0.25
- +2.7 Test of Loyalty (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Seven of Nine, Unassimilated 1

**The Destruction of Praxis** (R, B, {3}{B}{B}, +4.5* teorica) · UG+ BR UR WR · pede UG · oferece BR, UR, WR, fichas, klingons
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Destruction of Praxis 1
- +3.0 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ The Destruction of Praxis 1
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Destruction of Praxis 1

**The Wrath of Khan** (R, R, {2}{R}, +4.5* teorica) · oferece virar
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Kobayashi Maru Scenario** (M, U, {1}{U}{U}, +4.0* teorica) · UB BR WR · oferece BR, UB, WR, fichas, oficiais
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Kobayashi Maru Scenario 1
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Kobayashi Maru Scenario 1
- +2.7 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Kobayashi Maru Scenario 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**U.S.S. Enterprise-A, Free Spirit** (M, W, {3}{W}{W}, +4.0* teorica) · WU BR WB WR · oferece BR, WB, WR, WU, fichas, oficiais, virar
- +3.2 Captain Jean-Luc Picard (?, W) poder +0.5* · parceiros +2.2 · encaixe +0.1 ↔ U.S.S. Enterprise-A, Free Spirit 3.75
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ U.S.S. Enterprise-A, Free Spirit 1
- +3.2 Locutus, the One Who Speaks (?, WB) poder +2.5* · parceiros +1.2 · encaixe -0.1 ↔ U.S.S. Enterprise-A, Free Spirit 2
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ U.S.S. Enterprise-A, Free Spirit 1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ U.S.S. Enterprise-A, Free Spirit 1

**Armus, Skin of Evil** (R, B, {5}{B}{B}, +3.5* teorica) · WU WR · oferece WR, WU
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Antagonist Incorporator** (R, W, {1}{W}, +3.0* teorica) · WB+ BR WR · pede WB · oferece BR, WR, fichas
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Antagonist Incorporator 1
- +3.1 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Antagonist Incorporator 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Locutus, the One Who Speaks (?, WB) poder +2.5* · parceiros +0.9 · encaixe -0.1 ↔ Antagonist Incorporator 1.5
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Antagonist Incorporator 1
- +2.7 Interstellar Effigy (?, U) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Antagonist Incorporator 1

**Captain Benjamin Sisko** (R, W, {1}{W}, +3.0* teorica) · UB+ BR WR · pede UB, fichas, oficiais · oferece BR, WR, fichas, oficiais
- +3.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +1.1 · encaixe -0.2 ↔ Captain Benjamin Sisko 1.75
- +3.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +1.1 · encaixe -0.2 ↔ Captain Benjamin Sisko 1.75
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Captain Benjamin Sisko 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Captain Benjamin Sisko 1
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Captain Benjamin Sisko 1
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Captain Benjamin Sisko 1

**Captain Jonathan Archer** (R, G, {2}{G}, +3.0* teorica) · BR WR · oferece BR, WR, fichas, oficiais, teletransporte
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Captain Jonathan Archer 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Captain Jonathan Archer 0.75
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Captain Jonathan Archer 1
- +2.7 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Captain Jonathan Archer 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Captain Pike, Fullness of Time** (R, G, {1}{G}{G}, +3.0* teorica) · UG+ RG · pede UG · oferece RG, oficiais
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Genesis Effect (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Captain Pike, Fullness of Time 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Collation Trimatrix** (R, B, {B}, +3.0* teorica) · WB+ BR · pede WB, fichas · oferece BR, virar
- +3.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Collation Trimatrix 1
- +3.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Collation Trimatrix 1
- +3.1 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Collation Trimatrix 1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.8 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.3 · encaixe +0.1 ↔ Collation Trimatrix 0.5
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Collation Trimatrix 0.25

**Dathon, His Heart Open** (R, URG, {G}{U}{R}, +3.0* teorica) · UR+ · pede UR · oferece oficiais
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Energize (?, U) poder +2.0* · parceiros +0.1 · encaixe +0.1 ↔ Dathon, His Heart Open 0.25
- +2.6 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.1 · encaixe +0.1 ↔ Dathon, His Heart Open 0.25

**Deanna Troi, Psychic Counsel** (R, W, {1}{W}, +3.0* teorica) · BR WG · oferece BR, WG
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Deanna Troi, Psychic Counsel 0.25
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Death Is Irrelevant** (M, B, {6}{B}{B}, +3.0* teorica) · WB+ · pede WB
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.8 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.3 · encaixe +0.1 ↔ Death Is Irrelevant 0.5
- +2.7 Interstellar Effigy (?, U) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Death Is Irrelevant 1
- +2.7 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Death Is Irrelevant 1

**Deep Space 9** (M, -, {9}, +3.0* teorica) · WR+ WU WB · pede WR · oferece WB, WU, virar
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Deep Space 9 1
- +2.7 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Deep Space 9 0.25
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Deep Space 9 0.25
- +2.7 Locutus, the One Who Speaks (?, WB) poder +2.5* · parceiros +0.9 · encaixe -0.2 ↔ Deep Space 9 1.5
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Deep Space 9 1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Deep Space 9 1

**Dr. Leonard "Bones" McCoy** (R, G, {1}{G}{G}, +3.0* teorica) · BG+ UB · pede BG · oferece UB, teletransporte
- +3.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Dr. Leonard "Bones" McCoy 1
- +3.1 Energize (?, U) poder +2.0* · parceiros +1.1 · encaixe -0.2 ↔ Dr. Leonard "Bones" McCoy 1.75
- +3.1 Transporter Malfunction (?, R) poder +2.0* · parceiros +1.1 · encaixe -0.2 ↔ Dr. Leonard "Bones" McCoy 1.75
- +3.1 Test of Priorities (?, U) poder +2.0* · parceiros +1.1 · encaixe -0.2 ↔ Dr. Leonard "Bones" McCoy 1.75
- +3.1 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Dr. Leonard "Bones" McCoy 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Dr. Leonard "Bones" McCoy 0.75

**Elim Garak, Simple Tailor** (R, B, {2}{B}, +3.0* teorica) · UB+ · pede UB · oferece vida
- +3.5 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Elim Garak, Simple Tailor 1
- +3.2 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Elim Garak, Simple Tailor 1
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Elim Garak, Simple Tailor 1
- +3.1 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Elim Garak, Simple Tailor 1
- +3.1 Test of Loyalty (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Elim Garak, Simple Tailor 1
- +3.1 Impossible Choice (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Elim Garak, Simple Tailor 1

**Excalbian Gamemaster** (M, W, {5}{W}, +3.0* teorica) · BR+ UG+ WU WG WR · pede BR, UG · oferece WG, WR, WU, fichas, oficiais, teletransporte
- +3.4 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe +0.1 ↔ Excalbian Gamemaster 0.75
- +3.4 Captain Jean-Luc Picard (?, W) poder +0.5* · parceiros +2.4 · encaixe +0.1 ↔ Excalbian Gamemaster 4
- +3.2 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Excalbian Gamemaster 1
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Excalbian Gamemaster 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Excalbian Gamemaster 1
- +3.0 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.9 · encaixe -0.2 ↔ Excalbian Gamemaster 1.5

**General Chang, Cold Warrior** (R, B, {B}, +3.0* teorica) · BR+ WG · pede BR, klingons · oferece WG, klingons, oficiais
- +3.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +1.1 · encaixe -0.2 ↔ General Chang, Cold Warrior 1.75
- +3.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ General Chang, Cold Warrior 1
- +3.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ General Chang, Cold Warrior 1
- +3.5 The Destruction of Praxis (?, B) poder +2.0* · parceiros +1.1 · encaixe +0.1 ↔ General Chang, Cold Warrior 1.75
- +3.3 Dahar Master (?, R) poder +2.5* · parceiros +0.8 · encaixe -0.2 ↔ General Chang, Cold Warrior 1.25
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1

**Georgiou, Terran Emperor** (M, B, {4}{B}{B}, +3.0* teorica) · WU BR WR · oferece BR, WR, WU, fichas, oficiais
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Georgiou, Terran Emperor 1
- +3.1 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Georgiou, Terran Emperor 1
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Georgiou, Terran Emperor 1

**Gowron, Eager for Battle** (R, BR, {2}{B}{R}, +3.0* teorica) · BR+ WG · pede BR, klingons · oferece WG, klingons
- +4.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +1.1 · encaixe +0.1 ↔ Gowron, Eager for Battle 1.75
- +3.8 Dahar Master (?, R) poder +2.5* · parceiros +0.8 · encaixe +0.1 ↔ Gowron, Eager for Battle 1.25
- +3.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Gowron, Eager for Battle 1
- +3.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Gowron, Eager for Battle 1
- +3.5 The Destruction of Praxis (?, B) poder +2.0* · parceiros +1.1 · encaixe +0.1 ↔ Gowron, Eager for Battle 1.75
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1

**Grand Nagus Zek** (R, B, {2}{B}, +3.0* teorica) · BR+ · pede BR, tesouros · oferece tesouros
- +3.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Grand Nagus Zek 1
- +3.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Grand Nagus Zek 1
- +3.2 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Grand Nagus Zek 1
- +3.1 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Grand Nagus Zek 1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Dahar Master (?, R) poder +2.5* · parceiros +0.3 · encaixe -0.2 ↔ Grand Nagus Zek 0.5

**Gul Dukat, Colonial Prefect** (M, B, {4}{B}{B}{B}, +3.0* teorica) · WU WR · oferece WR, WU, vida
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Gwyndala, the Progeny** (R, U, {1}{U}, +3.0* teorica) · BR · pede equipamentos, fichas · oferece BR, teletransporte
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Gwyndala, the Progeny 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Gwyndala, the Progeny 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Gwyndala, the Progeny 0.75
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Energize (?, U) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Gwyndala, the Progeny 0.75
- +2.9 Test of Priorities (?, U) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Gwyndala, the Progeny 0.75

**Holo-Engineer** (R, G, {2}{G}{G}, +3.0* teorica) · BR WB WR · pede fichas · oferece BR, WB, WR, fichas, teletransporte
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Holo-Engineer 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Holo-Engineer 1
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Holo-Engineer 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Holo-Engineer 0.75
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Holo-Engineer 1

**Kai Winn, Faithless Leader** (R, B, {1}{B}, +3.0* teorica) · BR · oferece BR
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Kai Winn, Faithless Leader 0.25
- +2.6 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.1 · encaixe +0.1 ↔ Kai Winn, Faithless Leader 0.25
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Kira Nerys, Firebrand** (R, WR, {1}{R}{W}, +3.0* teorica) · WU WR · pede fichas · oferece WR, WU
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Kirk, Commanding Officer (?, WR) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Kira Nerys, Firebrand 1
- +2.8 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Kira Nerys, Firebrand 0.25
- +2.7 Blastoneuron (?, B) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Kira Nerys, Firebrand 0.25

**Lwaxana Troi, Charming Guest** (R, R, {1}{R}, +3.0* teorica) · BR · oferece BR
- +3.1 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe +0.1 ↔ Lwaxana Troi, Charming Guest 0.25
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.1 · encaixe +0.1 ↔ Lwaxana Troi, Charming Guest 0.25
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**MACO Strike Team** (R, G, {G}, +3.0* teorica) · BR WR · oferece BR, WR, fichas, oficiais
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ MACO Strike Team 1
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ MACO Strike Team 1
- +2.7 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ MACO Strike Team 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Miles O'Brien, Transporter Ops** (R, W, {2}{W}, +3.0* teorica) · pede teletransporte · oferece teletransporte
- +3.4 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe +0.1 ↔ Miles O'Brien, Transporter Ops 0.75
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Miles O'Brien, Transporter Ops 0.75
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Miles O'Brien, Transporter Ops 0.75
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Miles O'Brien, Transporter Ops 0.75
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Miles O'Brien, Transporter Ops 0.75
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Miles O'Brien, Transporter Ops 0.75

**Nog, Ambitious Cadet** (R, BG, {B}{G}, +3.0* teorica) · BG+ BR RG UG · pede BG, virar · oferece BR, RG, UG
- +3.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Nog, Ambitious Cadet 1
- +3.3 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.3 · encaixe +0.1 ↔ Nog, Ambitious Cadet 0.5
- +3.3 Blastoneuron (?, B) poder +2.5* · parceiros +0.3 · encaixe +0.1 ↔ Nog, Ambitious Cadet 0.5
- +3.1 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Nog, Ambitious Cadet 1
- +3.1 He's Dead, Jim (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Nog, Ambitious Cadet 1
- +3.1 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Nog, Ambitious Cadet 1

**Nyota Uhura, Communications** (R, U, {2}{U}, +3.0* teorica) · oferece oficiais
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Overflow Submatrix** (R, B, {2}{B}, +3.0* teorica) · WB+ BG+ · pede BG, WB
- +3.3 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.3 · encaixe +0.1 ↔ Overflow Submatrix 0.5
- +3.3 Blastoneuron (?, B) poder +2.5* · parceiros +0.3 · encaixe +0.1 ↔ Overflow Submatrix 0.5
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Overflow Submatrix 1
- +3.1 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Overflow Submatrix 1
- +3.1 He's Dead, Jim (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Overflow Submatrix 1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1

**Primary Unimatrix Adjunct** (R, W, {3}{W}, +3.0* teorica) · WB+ · pede WB
- +3.1 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Primary Unimatrix Adjunct 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Interstellar Effigy (?, U) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Primary Unimatrix Adjunct 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Rok-Tahk, Budding Scientist** (M, G, {4}{G}{G}, +3.0* teorica) · WU BR WR · oferece BR, WR, WU, fichas, teletransporte
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Rok-Tahk, Budding Scientist 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Rok-Tahk, Budding Scientist 0.75
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Rok-Tahk, Budding Scientist 1
- +2.7 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Rok-Tahk, Budding Scientist 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Salt Vampire** (R, B, {1}{B}, +3.0* teorica) · BR · oferece BR, teletransporte, vida
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Salt Vampire 0.75
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Salt Vampire 0.25
- +2.6 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.1 · encaixe +0.1 ↔ Salt Vampire 0.25

**Sarek, Federation Ambassador** (R, WUG, {1}{G}{W}{U}, +3.0* teorica) · WG · oferece WG
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Subcommander T'Pol** (R, U, {2}{U}, +3.0* teorica) · UB · oferece UB, teletransporte
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Subcommander T'Pol 0.75
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Energize (?, U) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Subcommander T'Pol 0.75
- +2.9 Test of Priorities (?, U) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Subcommander T'Pol 0.75
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Sulu, Space Swashbuckler** (R, W, {1}{W}, +3.0* teorica) · BR · pede equipamentos, virar · oferece BR
- +3.1 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Sulu, Space Swashbuckler 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Sulu, Space Swashbuckler 0.25
- +2.7 The Wrath of Khan (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Sulu, Space Swashbuckler 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Tasha Yar, Out of Time** (R, R, {1}{R}, +3.0* teorica) · BG+ BR · pede BG · oferece BR, fichas, oficiais
- +3.6 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ Tasha Yar, Out of Time 1
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Tasha Yar, Out of Time 1
- +3.1 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Tasha Yar, Out of Time 1
- +3.1 Plasma Cascade (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Tasha Yar, Out of Time 1
- +3.1 Transporter Malfunction (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Tasha Yar, Out of Time 1
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1

**Troubling Tribbles** (R, W, {2}{W}, +3.0* teorica) · oferece fichas
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Will Riker, First in the Field** (R, R, {3}{R}, +3.0* teorica) · WU RG WR UG · oferece RG, UG, WR, WU, oficiais
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Will Riker, First in the Field 1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Worf, Intelligence Contractor** (R, R, {2}{R}, +3.0* teorica) · oferece klingons, teletransporte
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe -0.2 ↔ Worf, Intelligence Contractor 0.75
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Transporter Malfunction (?, R) poder +2.0* · parceiros +0.5 · encaixe +0.1 ↔ Worf, Intelligence Contractor 0.75
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**All Good Things...** (R, UG, {3}{G}{U}, +2.5* teorica) · oferece vida
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Brazen Bluff** (R, R, {R}{R}, +2.5* teorica) · UR+ · pede UR
- +3.1 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Brazen Bluff 1
- +3.1 Plasma Cascade (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Brazen Bluff 1
- +3.1 Transporter Malfunction (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Brazen Bluff 1
- +3.1 Encounter the Unknown (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Brazen Bluff 1
- +3.1 Genesis Effect (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Brazen Bluff 1
- +3.1 Perils of the Past (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Brazen Bluff 1

**D-7 Battle Cruiser** (R, R, {1}{R}, +2.5* teorica) · WU BR WB WR · oferece BR, WB, WR, WU, fichas, klingons, virar
- +3.6 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ D-7 Battle Cruiser 1
- +3.1 Planetary Bombardment (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ D-7 Battle Cruiser 1
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ D-7 Battle Cruiser 1
- +2.7 Eject the Warp Core (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ D-7 Battle Cruiser 1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Dominion Infiltration** (R, R, {X}{R}{R}{R}, +2.5* teorica) · UR · oferece UR, fichas
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Federation Resupply** (R, W, {1}{W}, +2.5* teorica) · WU+ UR BG · pede WU, equipamentos, teletransporte · oferece BG, UR
- +3.6 Blastoneuron (?, B) poder +2.5* · parceiros +1.1 · encaixe -0.2 ↔ Federation Resupply 1.75
- +3.4 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.5 · encaixe +0.1 ↔ Federation Resupply 0.75
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Federation Resupply 1
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Federation Resupply 1
- +3.2 Dahar Master (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Federation Resupply 1
- +3.1 U.S.S. Excelsior, Cutting Edge (?, W) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Federation Resupply 1

**Genesis Device** (R, G, {2}{G}, +2.5* teorica) · RG UG · oferece RG, UG
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Genesis Device 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**H.M.S. Bounty, Unlikely Timeship** (R, U, {4}{U}, +2.5* teorica) · WU WB · oferece WB, WU, virar
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ H.M.S. Bounty, Unlikely Timeship 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Hit It!** (R, RG, {1}{R}{G}, +2.5* teorica) · WR · oferece WR
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Mirror Universe Intrusion** (R, UB, {1}{U}{B}, +2.5* teorica) · UR · oferece UR, fichas
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Peace in Our Time** (R, W, {3}{W}, +2.5* teorica)
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Replicator** (R, -, {2}, +2.5* teorica) · pede fichas · oferece vida
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Replicator 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Replicator 1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Replicator 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Romulan Bird-of-Prey** (R, U, {1}{U}, +2.5* teorica) · UR+ WU WB · pede UR · oferece WB, WU, virar
- +3.3 Resistance Is Futile (?, B) poder +2.0* · parceiros +1.2 · encaixe -0.2 ↔ Romulan Bird-of-Prey 2
- +3.1 Energize (?, U) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Romulan Bird-of-Prey 1
- +3.1 Test of Priorities (?, U) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Romulan Bird-of-Prey 1
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Romulan Bird-of-Prey 1
- +2.7 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Romulan Bird-of-Prey 1

**Stable Wormhole** (R, G, {2}{G}, +2.5* teorica) · RG UG · oferece RG, UG
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Stable Wormhole 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**The City on the Edge of Forever** (R, WB, {3}{W}{B}, +2.5* teorica) · BR+ WR · pede BR · oferece WR, fichas, vida
- +3.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ The City on the Edge of Forever 1
- +3.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ The City on the Edge of Forever 1
- +3.1 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ The City on the Edge of Forever 1
- +3.0 Locutus, the One Who Speaks (?, WB) poder +2.5* · parceiros +0.8 · encaixe +0.1 ↔ The City on the Edge of Forever 1.25
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1

**The Inner Light** (R, WG, {3}{G}{W}, +2.5* teorica) · BG+ · pede BG · oferece tesouros, vida
- +3.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ The Inner Light 1
- +3.1 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ The Inner Light 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.8 Amok Time (?, G) poder +2.0* · parceiros +0.3 · encaixe +0.1 ↔ The Inner Light 0.5
- +2.7 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ The Inner Light 0.12
- +2.7 Blastoneuron (?, B) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ The Inner Light 0.12

**The Needs of the Many** (R, W, {1}{W}, +2.5* teorica) · BR+ UR · pede BR · oferece UR
- +3.2 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Needs of the Many 1
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Needs of the Many 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Needs of the Many 1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.9 Dahar Master (?, R) poder +2.5* · parceiros +0.3 · encaixe -0.2 ↔ The Needs of the Many 0.5
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Needs of the Many 1

**U.S.S. Discovery, at Black Alert** (R, G, {3}{G}{G}, +2.5* teorica) · WU WB · oferece WB, WU, virar
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ U.S.S. Discovery, at Black Alert 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**U.S.S. Enterprise-D, Galaxy-Class** (R, -, {3}, +2.5* teorica) · WU WB · oferece WB, WU, virar
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ U.S.S. Enterprise-D, Galaxy-Class 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**U.S.S. Reliant, From Hell's Heart** (R, B, {2}{B}{B}, +2.5* teorica) · BG+ WU WB · pede BG · oferece WB, WU, virar
- +3.4 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.9 · encaixe +0.1 ↔ U.S.S. Reliant, From Hell's Heart 1.5
- +3.3 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.3 · encaixe +0.1 ↔ U.S.S. Reliant, From Hell's Heart 0.5
- +3.3 Blastoneuron (?, B) poder +2.5* · parceiros +0.3 · encaixe +0.1 ↔ U.S.S. Reliant, From Hell's Heart 0.5
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ U.S.S. Reliant, From Hell's Heart 1
- +3.1 He's Dead, Jim (?, B) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ U.S.S. Reliant, From Hell's Heart 1
- +3.0 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe +0.1

**Year of Hell** (R, UR, {1}{U}{R}, +2.5* teorica)
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Branching Timeline** (R, G, {6}{G}{G}, +1.5* teorica) · UG+ UR · pede UG · oferece UR
- +3.0 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Genesis Effect (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Branching Timeline 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Deep Space Scan** (R, U, {4}{U}{U}, +1.5* teorica) · UG+ UR · pede UG · oferece UR
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Genesis Effect (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Deep Space Scan 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Live Long and Prosper** (R, WU, {5}{W}{U}, +1.5* teorica) · UR · oferece UR
- +3.0 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +3.0 Ghost of Illyria (?, W) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.6 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Dahar Master (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Pah-Wraith** (R, R, {5}{R}{R}, +1.5* teorica) · WR+ UG+ WU · pede UG, WR · oferece WU
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Pah-Wraith 1
- +3.1 Dahar Master (?, R) poder +2.5* · parceiros +0.1 · encaixe +0.1 ↔ Pah-Wraith 0.25
- +3.1 Genesis Effect (?, R) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ Pah-Wraith 1
- +3.0 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.9 · encaixe -0.2 ↔ Pah-Wraith 1.5
- +3.0 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe +0.1
- +2.7 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.1 · encaixe -0.2 ↔ Pah-Wraith 0.25

**The Caretaker** (R, U, {5}{U}, +1.5* teorica) · UB+ WU WR · pede UB · oferece WR, WU
- +3.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.6 · encaixe +0.1 ↔ The Caretaker 1
- +3.2 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Caretaker 1
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Caretaker 1
- +3.1 Test of Priorities (?, U) poder +2.0* · parceiros +0.6 · encaixe +0.1 ↔ The Caretaker 1
- +2.7 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Caretaker 1
- +2.7 Command Decision (?, W) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Caretaker 1

**The Holodeck** (R, -, {7}, +1.5* teorica) · BG+ · pede BG
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Holodeck 1
- +2.9 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.3 · encaixe -0.2 ↔ The Holodeck 0.5
- +2.9 Blastoneuron (?, B) poder +2.5* · parceiros +0.3 · encaixe -0.2 ↔ The Holodeck 0.5
- +2.7 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Holodeck 1
- +2.7 Energize (?, U) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Holodeck 1
- +2.7 Plasma Cascade (?, R) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Holodeck 1

**Blood Crypt** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Blood Crypt 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Breeding Pool** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Breeding Pool 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Federation Outpost** (R, -, , -1.5* teorica) · UB BG UG · oferece BG, UB, UG, vida
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Federation Outpost 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Federation Outpost 1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Federation Outpost 1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Federation Outpost 1
- +2.7 Test of Loyalty (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Federation Outpost 1
- +2.7 Amok Time (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Federation Outpost 1

**Godless Shrine** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Godless Shrine 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Hallowed Fountain** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Hallowed Fountain 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Ni'Var Science Academy** (R, -, , -1.5* teorica) · UB BG UG · oferece BG, UB, UG
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Ni'Var Science Academy 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Ni'Var Science Academy 1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Ni'Var Science Academy 1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Ni'Var Science Academy 1
- +2.7 Test of Loyalty (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Ni'Var Science Academy 1
- +2.7 Amok Time (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Ni'Var Science Academy 1

**Overgrown Tomb** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Overgrown Tomb 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Q Continuum** (R, -, , -1.5* teorica) · UB BG UG · oferece BG, UB, UG
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Q Continuum 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Q Continuum 1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Q Continuum 1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Q Continuum 1
- +2.7 Test of Loyalty (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Q Continuum 1
- +2.7 Amok Time (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Q Continuum 1

**Quark's Bar** (R, -, , -1.5* teorica) · UB BG UG · oferece BG, UB, UG
- +3.2 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Quark's Bar 1
- +3.2 Blastoneuron (?, B) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ Quark's Bar 1
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Quark's Bar 1
- +2.7 Resistance Is Futile (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Quark's Bar 1
- +2.7 Test of Loyalty (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Quark's Bar 1
- +2.7 Amok Time (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Quark's Bar 1

**Sacred Foundry** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Sacred Foundry 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Starfleet Academy** (M, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Starfleet Academy 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Steam Vents** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Steam Vents 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Stomping Ground** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Stomping Ground 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**Temple Garden** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Temple Garden 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

**The Unicomplex** (R, -, , -1.5* teorica) · BG+ UB UG · pede BG · oferece UB, UG
- +3.2 Dominion Assault Force (?, G) poder +2.5* · parceiros +0.6 · encaixe -0.2 ↔ The Unicomplex 1
- +2.9 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.3 · encaixe -0.2 ↔ The Unicomplex 0.5
- +2.9 Blastoneuron (?, B) poder +2.5* · parceiros +0.3 · encaixe -0.2 ↔ The Unicomplex 0.5
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Unicomplex 1
- +2.7 Test of Courage (?, G) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Unicomplex 1
- +2.7 Energize (?, U) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ The Unicomplex 1

**Watery Grave** (R, -, , -1.5* teorica) · UG · oferece UG
- +2.7 The Destruction of Praxis (?, B) poder +2.0* · parceiros +0.6 · encaixe -0.2 ↔ Watery Grave 1
- +2.6 Munitions Enthusiast (?, R) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Sela, Tal Shiar Paradox (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Commander Raffi Musiker (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Wesley Crusher, Starfleet Cadet (?, U) poder +2.5* · parceiros +0.0 · encaixe -0.2
- +2.6 Blastoneuron (?, B) poder +2.5* · parceiros +0.0 · encaixe -0.2

## 3. Pares de cartas com mais sinergia direta

9163 pares com elo na coleção; os 40 primeiros (sinergia em unidades de elo;
empate pela soma de poder das duas). Elo entre duas cartas que juntas pedem três cores vale um quarto.

| sin | poder | carta A | carta B | elos |
| --- | --- | --- | --- | --- |
| 4 | +7.5 | Captain Jean-Luc Picard | Excalbian Gamemaster | BR, WR, fichas, oficiais, WU |
| 3.75 | +8.5 | Captain Jean-Luc Picard | U.S.S. Enterprise-A, Free Spirit | WR, WU, fichas, oficiais |
| 3.75 | +7.5 | Captain James T. Kirk | Captain Benjamin Sisko | UB, WR, fichas, oficiais |
| 3.75 | +5.0 | Captain Jean-Luc Picard | U.S.S. Cerritos, Following Up | WR, WU, fichas, oficiais |
| 3 | +7.5 | Captain Jean-Luc Picard | Georgiou, Terran Emperor | WR, fichas, oficiais, WU |
| 3 | +7.0 | Captain Jean-Luc Picard | The City on the Edge of Forever | BR, WR, fichas |
| 3 | +7.0 | Captain Jean-Luc Picard | D-7 Battle Cruiser | WR, WU, fichas |
| 3 | +5.0 | Captain Jean-Luc Picard | In the Pale Moonlight | BR, WR, fichas |
| 3 | +4.0 | Captain Jean-Luc Picard | Photosynthetic Physician | WR, fichas, oficiais, WU |
| 3 | +3.5 | Sarcophagus, Ship of the Dead | Antagonist Incorporator | BR, WB, WR |
| 3 | +1.0 | Sarcophagus, Ship of the Dead | Conquest Mission | BR, WB, WR |
| 2.75 | +8.5 | Captain Jean-Luc Picard | Kobayashi Maru Scenario | WR, fichas, oficiais |
| 2.75 | +7.5 | Captain Jean-Luc Picard | MACO Strike Team | WR, fichas, oficiais |
| 2.75 | +7.5 | Captain Jean-Luc Picard | Captain Jonathan Archer | WR, fichas, oficiais |
| 2.75 | +7.5 | Captain Jean-Luc Picard | Captain Benjamin Sisko | WR, fichas, oficiais |
| 2.75 | +7.0 | Kobayashi Maru Scenario | Captain Benjamin Sisko | UB, fichas, oficiais |
| 2.75 | +6.0 | Excalbian Gamemaster | Captain Benjamin Sisko | BR, fichas, oficiais |
| 2.75 | +5.5 | Captain James T. Kirk | Academy Instructor | WR, fichas, oficiais |
| 2.75 | +5.5 | Captain Jean-Luc Picard | Academy Instructor | WR, fichas, oficiais |
| 2.75 | +4.0 | Academy Instructor | Excalbian Gamemaster | BR, fichas, oficiais |
| 2.75 | +4.0 | Captain Jean-Luc Picard | Make It So | WR, fichas, oficiais |
| 2.75 | +4.0 | Worf, Honor-Bound Warrior | Captain Benjamin Sisko | WR, fichas, oficiais |
| 2.75 | +3.0 | Captain Jean-Luc Picard | Subspace Anomaly | WR, fichas, oficiais |
| 2.75 | +2.5 | Make It So | Captain Benjamin Sisko | UB, fichas, oficiais |
| 2.75 | +2.0 | Worf, Honor-Bound Warrior | Academy Instructor | WR, fichas, oficiais |
| 2.75 | +0.5 | Academy Instructor | Make It So | UR, fichas, oficiais |
| 2.5 | +5.0 | Captain Jean-Luc Picard | Sarcophagus, Ship of the Dead | BR, WU, WR |
| 2.25 | +9.0 | Captain Jean-Luc Picard | Captain James T. Kirk | fichas, oficiais, WR |
| 2.25 | +7.5 | Captain Jean-Luc Picard | Rok-Tahk, Budding Scientist | WR, fichas, WU |
| 2.25 | +7.5 | Captain Jean-Luc Picard | Kira Nerys, Firebrand | WR, fichas, WU |
| 2.25 | +5.5 | Captain Jean-Luc Picard | Worf, Honor-Bound Warrior | fichas, oficiais, WR |
| 2.25 | +5.0 | Captain James T. Kirk | Gabriel Lorca, Mirror Menace | BG, UB, WR |
| 2.25 | +4.0 | Captain Jean-Luc Picard | Cha'DIch Investigator | WR, fichas, WU |
| 2.25 | +4.0 | Worf, Honor-Bound Warrior | Excalbian Gamemaster | WR, fichas, BR |
| 2.25 | +2.5 | Emergency Holographic Crew | Federation Resupply | BG, teletransporte, WU |
| 2.25 | +2.0 | Gray and Adira, Forever Joined | Academy Instructor | fichas, oficiais, UR |
| 2 | +9.5 | Captain Jean-Luc Picard | Sela, Tal Shiar Paradox | WR, fichas |
| 2 | +9.5 | Sela, Tal Shiar Paradox | Captain James T. Kirk | BG, WR |
| 2 | +9.0 | The Destruction of Praxis | Captain Jean-Luc Picard | WR, fichas |
| 2 | +7.5 | Captain James T. Kirk | Excalbian Gamemaster | BR, WR |

## 4. Arquétipos: payoffs e enablers em ordem de poder

### WU Frota Estelar: espaçonaves

Lance espaçonaves e as coloque em operação (Station: vire outra criatura para pôr marcadores de carga). Cartas que compram, crescem ou protegem quando uma espaçonave é conjurada, entra ou recebe carga.

Payoffs (9): Captain Jean-Luc Picard +4.5*, Lt. Cmdr. Geordi La Forge +4.5*, Federation Resupply +2.5*, Rutherford, Upgraded Ensign +1.0*, Hemmer, Fixing What Is Broken +1.0*, Zefram Cochrane, Warp Pioneer +1.0*, Emergency Holographic Crew +0.0*, Warp Core -0.5*, Stray from History -0.5*

Enablers (54): Borg Cube +5.0*, Crystalline Entity +5.0*, Q, Stacking the Deck +4.5*, Khan, Vengeful Heart +4.5*, U.S.S. Enterprise-A, Free Spirit +4.0*, Armus, Skin of Evil +3.5*, Deep Space 9 +3.0*, Georgiou, Terran Emperor +3.0*, Will Riker, First in the Field +3.0*, Rok-Tahk, Budding Scientist +3.0*

### UB Dilemas

Mágicas e habilidades modais ('escolha um') fazem você enfrentar um dilema; as payoffs recompensam cada dilema com cartas, marcadores +1/+1, dreno de vida ou recursão.

Payoffs (9): Elim Garak, Simple Tailor +3.0*, Captain Benjamin Sisko +3.0*, The Caretaker +1.5*, Seven of Nine +1.0*, Jett Reno, Problem Solver +1.0*, Gabriel Lorca, Mirror Menace +0.5*, Tell Me What You See +0.5*, Melkotian Adjudicator +0.0*, Obsidian Order Operative +0.0*

Enablers (39): Wesley Crusher, Starfleet Cadet +5.0*, Captain James T. Kirk +4.5*, Encounter the Unknown +4.5*, Kobayashi Maru Scenario +4.0*, Dr. Leonard "Bones" McCoy +3.0*, Commander Raffi Musiker +3.0*, Subcommander T'Pol +3.0*, Test of Courage +2.5*, Resistance Is Futile +2.5*, Test of Loyalty +2.5*

### BR Klingons: morte com honra

Fichas de Klingon e criaturas baratas alimentam saídas de sacrifício e gatilhos de morte: dano, cartas, Tesouros e marcadores. Sarcophagus e Vengeance Mission contam cada morte.

Payoffs (17): Khan, Vengeful Heart +4.5*, Gowron, Eager for Battle +3.0*, Grand Nagus Zek +3.0*, General Chang, Cold Warrior +3.0*, Excalbian Gamemaster +3.0*, The City on the Edge of Forever +2.5*, The Needs of the Many +2.5*, Dahar Master +2.0*, Planetary Bombardment +1.5*, Eject the Warp Core +1.5*

Enablers (73): Sela, Tal Shiar Paradox +5.0*, The Destruction of Praxis +4.5*, Captain Jean-Luc Picard +4.5*, Captain James T. Kirk +4.5*, Jadzia Dax, Living Legacy +4.5*, Seven of Nine, Unassimilated +4.5*, Kobayashi Maru Scenario +4.0*, U.S.S. Enterprise-A, Free Spirit +4.0*, Munitions Enthusiast +3.0*, MACO Strike Team +3.0*

### RG Landfall: novos planetas

Faça um terreno entrar a cada turno (buscas, fichas de Planeta, terrenos extras, basic landcycling) para disparar landfall: criaturas crescem, Burnham causa dano, Booker cria Vermes e Dal R'El gera mana.

Payoffs (9): Dal R'El, Augment Orphan +1.0*, Captain Michael Burnham +1.0*, Cleveland Booker, Empath +1.0*, Jake Sisko, War Correspondent +1.0*, Syndicate Liquidators +0.5*, Exploratory Mission +0.5*, Saurian Explorer +0.0*, Xindi Surveyors +0.0*, Planetary Patrol +0.0*

Enablers (27): Captain Kathryn Janeway +4.5*, Nog, Ambitious Cadet +3.0*, Captain Pike, Fullness of Time +3.0*, Will Riker, First in the Field +3.0*, Genesis Device +2.5*, Stable Wormhole +2.5*, Genesis Effect +1.5*, David and Carol Marcus, Creators +1.0*, Erica Ortegas, Plucky Pilot +1.0*, The Naked Time +0.5*

### WG Enfermaria: marcadores +1/+1

Coloque marcadores +1/+1 (médicos, Pure Energy, Support Mission, explore) e aproveite quem recompensa criaturas com marcadores: atropelar, hexproof, dobrar marcadores, comprar cartas ao causar dano.

Payoffs (9): Dr. Joseph M'Benga +4.5*, Jadzia Dax, Living Legacy +4.5*, Lieutenant Commander Data +4.5*, Brad Boimler, Eager Ensign +1.0*, Phlox, Unorthodox Doctor +1.0*, Dr. McCoy, Surly Surgeon +1.0*, The Doctor, EMH +0.5*, Federation Field Medic +0.0*, Dominion Supervisor +0.0*

Enablers (31): Dr. Beverly Crusher +4.5*, Captain Kathryn Janeway +4.5*, Gowron, Eager for Battle +3.0*, General Chang, Cold Warrior +3.0*, Sarek, Federation Ambassador +3.0*, Deanna Troi, Psychic Counsel +3.0*, Excalbian Gamemaster +3.0*, Data, New Life +1.0*, Worf, Honor-Bound Warrior +1.0*, Rutherford, Upgraded Ensign +1.0*

### WB Coletivo Borg: criaturas artefato

Criaturas artefato em massa (drones Borg, fichas Borg e Ilusão) com lordes que dão +1/+1, vigilância, ameaçar, golpe duplo, compra de cartas e assimilação. Espaçonaves em operação também são criaturas artefato.

Payoffs (17): Borg Cube +5.0*, Collation Trimatrix +3.0*, Locutus, the One Who Speaks +3.0*, Overflow Submatrix +3.0*, Antagonist Incorporator +3.0*, Death Is Irrelevant +3.0*, Primary Unimatrix Adjunct +3.0*, Resistance Is Futile +2.5*, Rutherford, Upgraded Ensign +1.0*, Command Subadjunct +1.0*

Enablers (43): Crystalline Entity +5.0*, Seven of Nine, Unassimilated +4.5*, Lieutenant Commander Data +4.5*, U.S.S. Enterprise-A, Free Spirit +4.0*, Holo-Engineer +3.0*, Deep Space 9 +3.0*, U.S.S. Discovery, at Black Alert +2.5*, D-7 Battle Cruiser +2.5*, U.S.S. Excelsior, Cutting Edge +2.5*, U.S.S. Enterprise-D, Galaxy-Class +2.5*

### UR Laboratório: mágicas não criatura

Conjure mágicas que não sejam criatura (instantâneas, feitiços, auras, beam me up do cemitério) para disparar fichas de Oficial, marcadores +1/+1, cargas na Bird-of-Prey e cópias de criaturas.

Payoffs (15): Infinite Diversity +5.0*, Scotty, Miracle Worker +4.5*, Lieutenant Commander Data +4.5*, Dathon, His Heart Open +3.0*, Brazen Bluff +2.5*, Romulan Bird-of-Prey +2.5*, Gray and Adira, Forever Joined +1.0*, Academy Instructor +1.0*, Spock, Always Your Friend +1.0*, Anthropological Mission +0.5*

Enablers (58): The Destruction of Praxis +4.5*, Encounter the Unknown +4.5*, Mirror Universe Intrusion +2.5*, Test of Courage +2.5*, Energize +2.5*, Dominion Infiltration +2.5*, Federation Resupply +2.5*, Resistance Is Futile +2.5*, Test of Loyalty +2.5*, Transporter Malfunction +2.5*

### BG Cemitério: vigiar e reciclar

Encha o cemitério com vigiar, moagem e descarte; quem tira cartas dele (beam me up, exílio do cemitério, retorno à mão ou ao campo) dispara Vash, Sela, Blastoneuron e Hologram Stalker.

Payoffs (29): Sela, Tal Shiar Paradox +5.0*, Infinite Diversity +5.0*, Scotty, Miracle Worker +4.5*, Dr. Leonard "Bones" McCoy +3.0*, Tasha Yar, Out of Time +3.0*, Overflow Submatrix +3.0*, Nog, Ambitious Cadet +3.0*, Blastoneuron +3.0*, The Inner Light +2.5*, Resistance Is Futile +2.5*

Enablers (39): Captain James T. Kirk +4.5*, Seven of Nine, Unassimilated +4.5*, Test of Courage +2.5*, Energize +2.5*, Federation Resupply +2.5*, Transporter Malfunction +2.5*, Test of Priorities +2.5*, Dominion Assault Force +2.0*, Plasma Cascade +1.5*, He's Dead, Jim +1.5*

### WR Alerta vermelho: poder total 8

Vá largo com fichas de Oficial e Klingon e anthems (Picard, Sarcophagus, Red Alert!); atacar com poder total 8 ou mais destrava marcadores, cartas, primeiro golpe e bloqueios proibidos.

Payoffs (17): Captain Jean-Luc Picard +4.5*, Captain James T. Kirk +4.5*, Deep Space 9 +3.0*, Locutus, the One Who Speaks +3.0*, Kirk, Commanding Officer +3.0*, Pah-Wraith +1.5*, Worf, Honor-Bound Warrior +1.0*, Hologram Janeway +1.0*, Cleveland Booker, Empath +1.0*, La'An Noonien-Singh, Security +1.0*

Enablers (59): Sela, Tal Shiar Paradox +5.0*, Crystalline Entity +5.0*, The Destruction of Praxis +4.5*, Q, Stacking the Deck +4.5*, Khan, Vengeful Heart +4.5*, Kobayashi Maru Scenario +4.0*, U.S.S. Enterprise-A, Free Spirit +4.0*, Armus, Skin of Evil +3.5*, MACO Strike Team +3.0*, Holo-Engineer +3.0*

### UG Novos mundos: terrenos de nomes diferentes

Terrenos de nomes diferentes (planetas, anomalias, buscas, basic landcycling, terrenos extras) escalam strange new worlds: The Traveler e Pike crescem, Deep Space Scan compra, Suus Mahna e Astute Terraformer ficam baratos.

Payoffs (14): The Destruction of Praxis +4.5*, Seven of Nine, Unassimilated +4.5*, Captain Pike, Fullness of Time +3.0*, Excalbian Gamemaster +3.0*, Deep Space Scan +1.5*, Branching Timeline +1.5*, Pah-Wraith +1.5*, Ensign Pavel Chekov +1.0*, The Traveler +1.0*, Warp Speed +0.5*

Enablers (50): Captain Kathryn Janeway +4.5*, Nog, Ambitious Cadet +3.0*, Will Riker, First in the Field +3.0*, Genesis Device +2.5*, Stable Wormhole +2.5*, Genesis Effect +1.5*, David and Carol Marcus, Creators +1.0*, The Naked Time +0.5*, U.S.S. Voyager, Lone Wanderer +0.5*, Saurian Explorer +0.0*

## 5. Grafo de elos: centralidade e comunidades

As cartas são os nós e os elos diretos, as arestas (9163). **Centralidade** (0 a 100): um passeio
aleatório que segue um elo com chance proporcional ao peso do elo vezes a força da parceira, ou
recomeça em carta aleatória (85% de seguir); a carta central liga muitas parceiras fortes que
ligam outras. É o que a soma Σ não vê: Σ conta elos, a centralidade pesa a qualidade de quem está
do outro lado. Não torna cada elo mais certo (isso só dados de co-ocorrência em partidas fariam);
diz quais cartas são as melhores *portas de entrada* para uma coleção no começo do draft.

| # | centr. | Σ | nota | rar | cor | carta | elos |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 100 | 174.51 | +4.5* | M | W | Captain Jean-Luc Picard | pede WR, WU, fichas, oficiais · oferece BR, fichas, oficiais, virar |
| 2 | 86.4 | 156.42 | +4.5* | M | U | Scotty, Miracle Worker | pede BG, UR, teletransporte |
| 3 | 75.7 | 159.05 | +3.0* | M | W | Excalbian Gamemaster | pede BR, UG · oferece WG, WR, WU, fichas, oficiais, teletransporte |
| 4 | 73.3 | 151 | +3.0* | R | W | Captain Benjamin Sisko | pede UB, fichas, oficiais · oferece BR, WR, fichas, oficiais |
| 5 | 65.4 | 117.37 | +4.5* | R | B | The Destruction of Praxis | pede UG · oferece BR, UR, WR, fichas, klingons |
| 6 | 64.9 | 112.11 | +4.5* | M | U | Lieutenant Commander Data | pede UR, WG · oferece WB |
| 7 | 64.7 | 175.81 | +1.0* | U | R | Academy Instructor | pede UR, fichas, oficiais · oferece BR, WR, fichas, oficiais |
| 8 | 63.7 | 112.35 | +5.0* | M | R | Infinite Diversity | pede BG, UR |
| 9 | 63.6 | 114.18 | +4.5* | M | R | Captain James T. Kirk | pede WR · oferece BG, BR, UB, fichas, oficiais |
| 10 | 57.2 | 103.18 | +4.5* | M | U | Seven of Nine, Unassimilated | pede UG · oferece BG, BR, WB, oficiais |
| 11 | 54.2 | 97.37 | +5.0* | R | B | Sela, Tal Shiar Paradox | pede BG · oferece BR, WR, fichas |
| 12 | 52.6 | 112.82 | +2.5* | R | W | Federation Resupply | pede WU, equipamentos, teletransporte · oferece BG, UR |
| 13 | 52.1 | 123.12 | +2.5* | U | B | Resistance Is Futile | pede BG, WB · oferece UB, UR |
| 14 | 47.6 | 141.76 | +0.5* | U | G | Adversary by Algorithm | pede teletransporte · oferece BG, BR, UR, WB, WR, fichas |
| 15 | 47.4 | 100.25 | +3.0* | R | G | Holo-Engineer | pede fichas · oferece BR, WB, WR, fichas, teletransporte |
| 16 | 47.4 | 99.25 | +3.0* | R | B | Collation Trimatrix | pede WB, fichas · oferece BR, virar |
| 17 | 45.7 | 97.25 | +3.0* | R | W | Antagonist Incorporator | pede WB · oferece BR, WR, fichas |
| 18 | 45.3 | 101.37 | +3.0* | R | B | Overflow Submatrix | pede BG, WB |
| 19 | 45.2 | 83.25 | +4.0* | M | W | U.S.S. Enterprise-A, Free Spirit | oferece BR, WB, WR, WU, fichas, oficiais, virar |
| 20 | 44.6 | 96.37 | +2.5* | R | U | Romulan Bird-of-Prey | pede UR · oferece WB, WU, virar |
| 21 | 43.6 | 95.37 | +3.0* | U | B | Blastoneuron | pede BG · oferece BR, fichas, teletransporte, vida |
| 22 | 42.9 | 125.56 | +0.5* | U | R | Sarcophagus, Ship of the Dead | pede BR, WR · oferece WB, WU, virar |
| 23 | 42.4 | 90.32 | +2.5* | U | U | Test of Priorities | pede teletransporte · oferece BG, UB, UR |
| 24 | 40.5 | 102.86 | +1.5* | R | R | Pah-Wraith | pede UG, WR · oferece WU |
| 25 | 39.8 | 80.75 | +3.0* | M | - | Deep Space 9 | pede WR · oferece WB, WU, virar |

**Comunidades** (propagação de rótulos sobre os pares ligados por mais de um elo, peso 2 ou
mais, limiar escolhido entre 1.5, 2, 2.5 pelo que dá mais grupos;
9 grupos com 3 cartas ou mais, do maior para o menor). Grupo que junta cartas de pares
diferentes é um tema transversal (por exemplo, planeswalkers e quem os pede), que vale como
arquétipo extra ao ler os sinais da mesa. Sobre todos os elos a coleção vira um grupo só.

1. 57 cartas, poder médio +1.5, cores RBW · pares BR 44, WR 42, WB 17 · elos fichas 49, BR 44, WR 42: Sela, Tal Shiar Paradox, The Destruction of Praxis, Captain Jean-Luc Picard, Captain James T. Kirk, Kobayashi Maru Scenario, U.S.S. Enterprise-A, Free Spirit, MACO Strike Team, Holo-Engineer, Tasha Yar, Out of Time, Georgiou, Terran Emperor …
2. 19 cartas, poder médio +1.2, cores URG · pares BG 19, UR 18, UB 4 · elos BG 19, UR 18, teletransporte 11: Infinite Diversity, Scotty, Miracle Worker, Test of Courage, Energize, Federation Resupply, Transporter Malfunction, Test of Priorities, Plasma Cascade, He's Dead, Jim, Those Old Scientists …
3. 16 cartas, poder médio +1.3, cores UWG · pares WU 15, WB 15, BG 2 · elos WB 15, WU 15, virar 13: Deep Space 9, U.S.S. Discovery, at Black Alert, U.S.S. Excelsior, Cutting Edge, U.S.S. Enterprise-D, Galaxy-Class, Romulan Bird-of-Prey, H.M.S. Bounty, Unlikely Timeship, U.S.S. Reliant, From Hell's Heart, Rutherford, Upgraded Ensign, Hemmer, Fixing What Is Broken, Zefram Cochrane, Warp Pioneer …
4. 14 cartas, poder médio +0.5, cores BUG · pares BG 13, UB 12, WB 7 · elos BG 13, UB 12, WB 7: Seven of Nine, Unassimilated, Overflow Submatrix, Resistance Is Futile, Dominion Assault Force, Seven of Nine, Lore, Positronic Provocateur, Gabriel Lorca, Mirror Menace, Tal Shiar Operative, Federation Probe, Q Continuum …
5. 6 cartas, poder médio +0.8, cores WUG · pares WG 6, UR 4, BR 2 · elos WG 6, UR 4, virar 3: Lieutenant Commander Data, Brad Boimler, Eager Ensign, Test of Conviction, Tactical Officer, Shields Up!, I'm a Doctor, Not a . . .
6. 5 cartas, poder médio +0.7, cores BU · pares BG 5, UR 4, UB 3 · elos BG 5, UR 4, UB 3: Test of Loyalty, Anthropological Mission, De-evolve, Tell Me What You See, Stray from History
7. 4 cartas, poder médio +1.0, cores UGW · pares UB 4, WG 3, BG 2 · elos UB 4, WG 3, BG 2: Dr. Leonard "Bones" McCoy, Jett Reno, Problem Solver, Melkotian Adjudicator, Federation Field Medic
8. 3 cartas, poder médio +1.2, cores G · pares UG 3, RG 3, WU 1 · elos UG 3, RG 3, oficiais 1: Captain Pike, Fullness of Time, Warp Speed, Saurian Explorer
9. 3 cartas, poder médio +0.2, cores B · pares WB 3, BG 3, BR 2 · elos WB 3, BG 3, BR 2: Isolinear Processor, Relentless Drednok, Cybernetic Specialist

## Limites

- A nota de poder depende da fonte: só o 17Lands mede partidas com a amostra declarada; o
  Untapped é de outra data e de outros ranks; `*` é leitura teórica.
- Os elos vêm de padrões sobre o texto de regras (`src/mtg_builder/archetypes/<coleção>.json`):
  marcam pertencimento, não qualidade. `mtg draft synergy` mede se a marcação carrega sinal.
- O mapa não vê a mesa: sinais do draft (cores abertas, o que passou) só existem ao vivo.
- Regerar: `mtg draft update trk` e `mtg draft map trk --write`.
