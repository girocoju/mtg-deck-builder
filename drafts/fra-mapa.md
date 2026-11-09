# Reality Fracture (FRA) — mapa de picks

Gerado por `mtg draft map fra --write` em 2026-11-09. Dados: 17Lands 2026-11-08 (PremierDraft, 885596 jogos, média 54.4%) · Untapped 2026-10-12 (média 53.8%) · Draftsim (notas teóricas).
Fonte do poder, por carta: untapped 194, 17lands 79, draftsim* 7. Cartas draftáveis: 280 (29 míticas, 61 raras, 109 incomuns, 81 comuns).

**Como ler.** A nota é em pontos percentuais de win rate acima da média da fonte da carta
(17Lands: GIH WR − média dos usuários; Untapped: idem com a média dele; `draftsim*` e
`teorica*` são notas sem amostra de partidas). Raridade não entra na conta: ela só aparece
porque raras e míticas costumam ter mais poder, e porque cada pacote tem uma rara ou mítica,
cerca de três incomuns e dez comuns. No P1P1 compare a rara do pacote com a melhor incomum e a
melhor comum (seção 1); do P1P2 em diante, a rara quase sempre já saiu e a escolha é entre
incomuns e comuns (seção 2). Arquétipos: pares que a carta serve (`+` = payoff). Elos: o que a
carta *pede* e *oferece* (os dez pares e os ganchos fichas, planeswalker, descarte); Σ é a soma das sinergias diretas com
toda a coleção (quantas parceiras ela tem e quão fortes são os elos).

**Como o motor combina.** `mtg draft pick` soma: poder + encaixe nas cores (peso cresce do P1P1 até
o pick 21) + par + necessidade + sinal + flexibilidade + sinergia do par + **parceiros**
(0.6 ponto por unidade de elo com cada carta já escolhida, teto 3). Por isso um elo
direto desempata cartas próximas e não vira uma carta fraca em bomba. Teoria:
`knowledge/limitado-e-draft.md`, seções 3 (prioridades), 4 (arquétipos e deck perfeito) e 6
(compromisso).

## 0. Leitura da coleção e dos arquétipos

- **Composição.** 280 cartas draftáveis (29 míticas, 61 raras, 109 incomuns, 81 comuns). Por cor: branco 39, azul 39, preto 39, vermelho 40, verde 37, multicoloridas 54, incolores 32. As 25 multicoloridas incomuns são as sinalizadoras dos pares (teoria: `limitado-e-draft.md` §4, arquétipos).
- **Criaturas de comum e incomum.** 109 no total; verde tem mais (18) e branco menos (16). 63% custam até 3 (curva média; §2 custo e curva, §8 parâmetros do formato). Curva por cor, custo 1 a 6+: W 0 4 6 3 2 1; U 1 6 3 3 2 1; B 1 3 7 2 2 1; R 1 4 4 3 3 1; G 1 5 5 2 2 3.
- **Remoção de comum e incomum** (classificação automática pelo texto; confira com `mtg card`): branco 5: Surgical Precision, Your Fate Ends Here, Refute Destiny, Prophesied End, Memory Trap; azul 3: Icy Reception, Unsummon, Yuriko, Hope from the Shadows; preto 5: Terminal Criticism, Silence the Echo, Extended Absence, Proft, Sinister Mastermind, Last Gasp; vermelho 7: Way of the Warlord, Fulminous Forte, Tether Technician, Wrath of the Bloodmane, No Admittance, Awaken the Inferno, Violent Echoes; verde 3: Sureshot Sower, Budding Insurgent, Yoshimaru, Scrappy Stray; multicoloridas 8: Mind Meanderer, Twisted Fates, Konstrari Charm, Vigorbloom Charm, Stingerquill Charm, Theorix Charm, Craftwork Crusher, Warrior's Blades; incolores 2: Archive Arbiter, Afterthought Sentry. Remoção é a prioridade de pick depois das bombas (§2 removal, §3 prioridades); a cor com menos remoção depende da segunda cor.
- **Mecânicas e palavras-chave** (ocorrências e grupos de cor): Surveil 43 (U 13, W 9, B 6); Empower Jace 35 (U 9, B 7, W 6); Flying 28 (multi 8, U 8, W 6); Prepared 24 (multi 10, U 4, R 3); Trample 10 (R 3, multi 3, incolor 2); Flash 9 (U 4, multi 2, G 1); Prowess 9 (R 4, U 4, multi 1); Mill 8 (multi 4, B 3, G 1); Vigilance 8 (G 3, multi 2, U 2); Haste 6 (R 4, multi 1, B 1).
- **Correção de mana.** 20 terrenos não básicos draftáveis, 5 cartas com landcycling e 5 fontes de mana de qualquer cor: Kwia Vigorbloom, Murmuring Volume, Vraska, the Cutting Glare, Gideon's Memorial, Vraska, Soul of Stone. Quanto mais correção, mais compensa o splash de uma bomba ou remoção (§2 card advantage e correção de mana; §7 construção).
- **Pares nos dados** (17Lands 2026-11-08 (PremierDraft, 885596 jogos, média 54.4%); win rate do par e diferença para a média 54.4%): WU 56.2% (+1.8), UB 55.3% (+0.9), UR 55.1% (+0.7), RG 55.1% (+0.7), BG 54.8% (+0.4), BR 53.9% (-0.5), WG 53.8% (-0.6), WB 53.6% (-0.8), WR 53.2% (-1.3), UG 52.3% (-2.1). Entre o melhor e o pior par há 3.9 pontos.
- **Arquétipos** (profundo = 6 ou mais payoffs em comum e incomum; raso = 3 ou menos, depende de abrir a rara; §4 arquétipos e deck perfeito): WU Agressivo com Vigiar de Futurforte: 8 payoffs (5 C/U) e 84 enablers (62 C/U), médio; melhor payoff Denzilore Fatehold +6.1; sinalizadoras Denzilore Fatehold, Fatehold Chronologist // Peer Review, Fatehold Charm, Prudent Fateseer // Peer Review, Desperate Futurescribe, Proctor of Potential · UB Matemática do Cemitério de Theorix: 12 payoffs (9 C/U) e 66 enablers (49 C/U), profundo; melhor payoff Null Summoner +6.3; sinalizadoras Uldaros Theorix, Paradox Shaper // Omit Variables, Null Summoner, Theorix Metamage // Omit Variables, Recursive Recruitment, Theorix Charm · BR Dano Direto de Aculeopena: 5 payoffs (4 C/U) e 17 enablers (12 C/U), médio; melhor payoff Grim Repriser -2.1; sinalizadoras Stinging Vitriol, Stingerquill Charm, Ingris Stingerquill, Whiplash Wordsmith // Vicious Verse, Grim Repriser, Stingerquill Voxmancer // Vicious Verse · RG Aceleração de Mana de Konstrari: 8 payoffs (2 C/U) e 58 enablers (40 C/U), raso; melhor payoff Garruk, Curse Breaker +9.6; sinalizadoras Aerid Konstrari, Konstrari Charm, Tenured Tethermage, Konstrari Improviser // Soul Tether, Craftwork Crusher, Woodwork Prodigy // Soul Tether · WG Ganho de Vida de Vigorflor: 9 payoffs (4 C/U) e 26 enablers (23 C/U), médio; melhor payoff Kwia Vigorbloom +7.0; sinalizadoras Kwia Vigorbloom, Emergency Phytomedic // Seed Suture, Vigorbloom Charm, Solarium Sentry, Bloombrute, Vigorbloom Vanguard // Seed Suture · WB Desgaste de Liliana: 5 payoffs (4 C/U) e 88 enablers (56 C/U), médio; melhor payoff Generous Revival +1.1; sinalizadoras Twisted Fates, Edgar, Ancient Bloodlord, Vindictive Triumph, Blessed Ghoul · UR Destreza de Chandra: 16 payoffs (11 C/U) e 55 enablers (47 C/U), profundo; melhor payoff Geist of Saint Thalia +6.4; sinalizadoras Clash of Elements, Saheeli, Jewel of Avishkar, Frostbite Pyromental, Twinned Vision · BG Bestiário de Garruk: 13 payoffs (10 C/U) e 37 enablers (22 C/U), profundo; melhor payoff Garruk, Veiled Butcher +11.0; sinalizadoras Vraska, the Cutting Glare, Hapatra, the Desert Fang, Ferocity of the Hunt, Primal Witchstalker · WR Exército de Ajani: 8 payoffs (7 C/U) e 41 enablers (32 C/U), profundo; melhor payoff Ajani Unrelenting +17.0; sinalizadoras Solitary Cell, Charge the Sanctum, Mabel, Valley Hero, Warrior's Blades · UG Maestria de Jace: 47 payoffs (32 C/U) e 2 enablers (1 C/U), profundo; melhor payoff Ajani Unrelenting +17.0; sinalizadoras Avatar of Burgeoning Echoes, Mind Meanderer, Tam's Resistance, Entrust the Spark, Tam, the Possibility, Kiora of Salt and Sand.
- **Ganchos fora dos dez pares** (quem pede / quem oferece): fichas 29/28, planeswalker 50/8, descarte 1/17.
- **Grafo.** Cartas mais centrais (portas de entrada para a coleção): Ajani Unrelenting 100, Garruk, Curse Breaker 65, The Theorist, Jace Beleren 49.9, Garruk, Veiled Butcher 43.3, Way of the Healer 24.2. 4 comunidades com 3 cartas ou mais (elos de peso ≥ 1.5): 82 cartas (WUB; elos planeswalker, UG); 14 cartas (RBU; elos WU, WB); 4 cartas (WG; elos WG, WR); 3 cartas (UR; elos UR, fichas).

## 1. Ordem de pick da coleção inteira

Nota (fonte), cor, custo, arquétipos, elos e Σ sinergia. Ordem dentro da raridade.

### Míticas (29)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +17.0 | untapped | R | 4RR | Ajani Unrelenting | WR+ UG+ WB | pede UG, WR, fichas, planeswalker · oferece WB, descarte, fichas, planeswalker | 158.5 |
| 2 | +13.2 | untapped | UB | 3UBB | Uldaros Theorix | UB RG BG | oferece BG, RG, UB | 12.7 |
| 3 | +12.1 | untapped | U | 2UU | The Theorist, Jace Beleren | WB WR | pede fichas · oferece WB, WR, fichas, planeswalker | 105.8 |
| 4 | +11.0 | untapped | B | 3BB | Garruk, Veiled Butcher | BG+ WB | pede BG · oferece WB, fichas, planeswalker | 97.9 |
| 5 | +10.0 | untapped | B | 4BB | Overwrite the Multiverse | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 47.7 |
| 6 | +9.6 | untapped | G | 3GG | Garruk, Curse Breaker | RG+ BG+ WB | pede BG, RG · oferece WB, fichas, planeswalker | 144.4 |
| 7 | +7.7 | untapped | RG | 1RGG | Aerid Konstrari | RG+ BG | pede RG · oferece BG | 39.6 |
| 8 | +7.0 | untapped | WG | 3GWW | Kwia Vigorbloom | WG+ RG BG | pede WG · oferece BG, RG | 25.1 |
| 9 | +6.1 | untapped | WU | 1WUU | Denzilore Fatehold | WU+ WR | pede WU, fichas · oferece WR | 55.2 |
| 10 | +5.8 | untapped | R | 2RR | Chandra, Torch of Defiance | BR RG | oferece BR, RG, planeswalker | 57.8 |
| 11 | +3.4 | untapped | UG | GU | Avatar of Burgeoning Echoes | UG+ WU UB WB WR | pede UG, planeswalker · oferece UB, WB, WR, WU | 30.6 |
| 12 | +3.2 | untapped | U | 1UU | Seasoned Cryomancer | UB | oferece UB, descarte | 12 |
| 13 | +2.6 | untapped | U | 1UU | Chandra, Chill of Compliance | WU UB RG | oferece RG, UB, WU, planeswalker | 73.5 |
| 14 | +2.3 | untapped | BR | BRR | Ingris Stingerquill | BR WB | oferece BR, WB, fichas | 24 |
| 15 | +1.5 | untapped | - | 2 | The Echoverse Fulcrum |  | oferece descarte | 0.8 |
| 16 | +1.5 | untapped | W | 1W | Enlightened Confidant | WG+ WU UB WB | pede WG · oferece UB, WB, WU | 48.2 |
| 17 | +1.1 | untapped | R | 1R | Stingcaster Mage | UB+ WU WB | pede UB · oferece WB, WU | 65 |
| 18 | +0.9 | untapped | R | 4RRR | Craterclaw Colossus | RG+ BG+ | pede BG, RG | 63.6 |
| 19 | -0.2 | untapped | G | 1G | Tarmogoyf | WU WB | oferece WB, WU | 2.5 |
| 20 | -1.6 | untapped | G | GGGG | Hexhaven Invigorator | BG | oferece BG | 3.2 |
| 21 | -2.0 | untapped | B | 3B | Darklight Phoenix | UB | oferece UB | 12 |
| 22 | -3.0* | draftsim | W | W | Loyal Tutor | UR | pede planeswalker · oferece UR | 21.8 |
| 23 | -3.1 | untapped | - | 10 | Emrakul, the Exigent Doom | RG BG | oferece BG, RG | 20.2 |
| 24 | -3.1 | untapped | W | 1W | Ajani Resolute | WG+ UG+ WB WR | pede UG, WG, fichas, planeswalker · oferece WB, WR, fichas, planeswalker | 161.8 |
| 25 | -3.2* | draftsim | G | 5GGG | Omnipresence |  | pede fichas | 22.8 |
| 26 | -3.6 | untapped | B | 1B // B | Bloodline Recollector // Ancestral Craving | WU WB UR | oferece UR, WB, WU | 17 |
| 27 | -4.5 | untapped | W | 7WW | Return to the Light Realms | UB | oferece UB | 9 |
| 28 | -10.9 | untapped | - | 3 | Codie, Ravenous Codex | UR | pede fichas · oferece UR | 42.5 |
| 29 | -20.4 | untapped | G | 1GG | Gardenize | WB+ RG | pede WB · oferece RG | 49.1 |

### Raras (61)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +9.2 | untapped | U | 2UU | Sphinx of False Conclusions | WB BG | oferece BG, WB, descarte | 8.4 |
| 2 | +7.6 | untapped | B | B | Lich's Relic |  | pede fichas | 23.5 |
| 3 | +6.6 | untapped | B | 2B | Sanctum Lurker | UG+ BR WG | pede UG, planeswalker · oferece BR, WG | 43.2 |
| 4 | +6.4 | untapped | W | 5WW | Kindred Judgment |  |  |  |
| 5 | +6.3 | untapped | UB | 2UB | Null Summoner | UB+ BG | pede UB · oferece BG | 44.7 |
| 6 | +6.1 | untapped | BG | BBG | Vraska, the Cutting Glare | RG BG | oferece BG, RG | 12.8 |
| 7 | +6.0 | untapped | G | 3GG | Hungering Puppetbeast | RG BG WR | oferece BG, RG, WR | 17.8 |
| 8 | +4.6 | untapped | U | 1UU | Lyra, Tolarian Archangel | WB | oferece WB, fichas | 30.2 |
| 9 | +3.8 | untapped | WU | WU | Proctor of Potential | WU+ UB WB | pede WU · oferece UB, WB | 40.7 |
| 10 | +3.6 | untapped | W | XW | Guiding Hydra | WU WB WR | oferece WB, WR, WU | 11.2 |
| 11 | +3.4 | untapped | U | U // 1U | Diviner of Victory // Unwind History | WU+ UB WB UR | pede WU · oferece UB, UR, WB | 79.2 |
| 12 | +3.4 | untapped | B | 2B | Gideon the Oathless | UG+ BR | pede UG, planeswalker · oferece BR, descarte | 36.5 |
| 13 | +3.4 | untapped | G | 1GG | Simulacrum Shaper | WB | oferece WB | 5 |
| 14 | +3.3 | untapped | W | 2W | Lyra, Archangel of Dawn | WG+ WR | pede WG · oferece WR | 38 |
| 15 | +3.1 | untapped | G | 4GGG | Verdant Kraken | RG WB BG | oferece BG, RG, WB, fichas | 39.2 |
| 16 | +3.0 | untapped | G | 1G // G | Carnivorous Cultivator // Enroot | WU UB WB UR BG | oferece BG, UB, UR, WB, WU | 39 |
| 17 | +3.0 | untapped | W | 1W | Repurposed Enforcer | UG+ WU UB WB | pede UG, fichas, planeswalker · oferece UB, WB, WU | 72.5 |
| 18 | +2.6 | untapped | W | W | Liliana the Faultless | UG+ WU WG WB | pede UG, planeswalker · oferece WB, WG, WU, descarte | 44.5 |
| 19 | +2.1 | untapped | RG | 1RG | Tenured Tethermage | RG+ WR | pede RG · oferece WR | 41.9 |
| 20 | +1.9 | untapped | U | 2U | Jace's Machinations | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 51.9 |
| 21 | +1.8* | draftsim | U | 2U | Cruel Calculations |  |  |  |
| 22 | +1.8 | untapped | - |  | Theorist's Sanctum | RG UG | oferece RG, UG | 54.2 |
| 23 | +1.4 | untapped | U | 2U // 2U | Variable Chaser // Arc of Fortune | UR+ | pede UR | 54.2 |
| 24 | +1.4 | untapped | U | 3UU | Jace, Reality Sculptor | UG+ | pede UG, planeswalker · oferece planeswalker | 77.9 |
| 25 | +1.2 | untapped | B | B | Dark Matter Manipulator | UB+ WU WB | pede UB · oferece WB, WU | 69.5 |
| 26 | +1.0 | untapped | R | 2RR | Curse-Marred Demon | BG | oferece BG, descarte | 12.2 |
| 27 | +0.6 | untapped | - |  | Shipwreck Marsh | RG | oferece RG | 7.2 |
| 28 | +0.5 | untapped | B | 1B | Liliana the Repentant | UG+ WU UB WB WR | pede UG, planeswalker · oferece UB, WB, WR, WU | 52.5 |
| 29 | +0.3 | untapped | U | 1U | Theorist's Proxy | UG+ WU UB WB | pede UG, planeswalker · oferece UB, WB, WU | 53.1 |
| 30 | +0.2 | untapped | B | 4B | Rise of the Deathbringer |  |  |  |
| 31 | -0.1 | untapped | R | XR | Ajani's Anguish |  |  |  |
| 32 | -0.1 | untapped | R | 1R | Samut, Hazoret's Champion | WU WB | oferece WB, WU | 2.5 |
| 33 | -0.4 | untapped | WG | GW | Solarium Sentry | WU WG WB | oferece WB, WG, WU | 10.4 |
| 34 | -0.4 | untapped | WUR | URW | Vraska, Soul of Stone | UR+ WB | pede UR · oferece WB, fichas | 24.1 |
| 35 | -0.7 | untapped | R | 3RR | Draconic Visitor | RG BG | oferece BG, RG | 4.7 |
| 36 | -0.9 | untapped | - |  | Deserted Beach | RG | oferece RG | 7.2 |
| 37 | -1.2 | untapped | B | BB | Vraska's Final Mercy | UG+ WU UB UR | pede UG, planeswalker · oferece UB, UR, WU | 62.2 |
| 38 | -1.2 | untapped | R | 5RR | Face Yourself |  |  |  |
| 39 | -1.9 | untapped | WB | WBB | Vindictive Triumph |  |  |  |
| 40 | -2.0 | untapped | - |  | Haunted Ridge | RG | oferece RG | 7.2 |
| 41 | -2.1 | untapped | R | 1R | Master of Barbs | BR+ WU WB | pede BR, fichas · oferece WB, WU | 45.7 |
| 42 | -2.1 | untapped | - |  | Overgrown Farmland | RG | oferece RG | 7.2 |
| 43 | -2.2* | draftsim | UG | 1GU | Tam, the Possibility | UG+ | pede UG, planeswalker | 18.6 |
| 44 | -2.4 | untapped | - |  | Rockfall Vale | RG | oferece RG | 7.2 |
| 45 | -2.6 | untapped | R | R // R | Pompous Battlemage // Improvised Act | UR+ WU WB | pede UR · oferece WB, WU, descarte | 57.9 |
| 46 | -2.9 | untapped | - |  | Hall of Echoes | RG | oferece RG | 7.2 |
| 47 | -3.0* | draftsim | UG | 3GU | Entrust the Spark |  | pede planeswalker | 5 |
| 48 | -3.0 | untapped | BR | BR | Stinging Vitriol | BR UR | oferece BR, UR, descarte | 15 |
| 49 | -3.2* | draftsim | R | 2R | Identity Echo | UG+ | pede UG, planeswalker | 30.4 |
| 50 | -4.0 | untapped | R | 1RR // R | Pyre Rhymer // Molten Tide | UR+ | pede UR | 54.6 |
| 51 | -4.2 | untapped | UR | URR | Frostbite Pyromental | BG | oferece BG | 4.8 |
| 52 | -4.3 | untapped | G | 1G | Puppet Crafting | UB | oferece UB | 9.8 |
| 53 | -4.5 | untapped | WR | RW | Solitary Cell | RG+ | pede RG | 30.7 |
| 54 | -5.6 | untapped | W | 1W | Gideon's Memorial |  |  |  |
| 55 | -5.7 | untapped | WUBRG | 2/W2/U2/B2/R2/G | Karn, Gilded Guardian | RG+ BG | pede RG · oferece BG | 13.9 |
| 56 | -6.1 | untapped | - |  | Roiling Canopy | RG | oferece RG | 7.2 |
| 57 | -7.5 | untapped | - | 2 | Karn, Argent Defender | WU WB | oferece WB, WU | 3.2 |
| 58 | -7.6 | untapped | U | 1U | Samut, Tyrant of Naktamun | UR+ WU WB | pede UR · oferece WB, WU | 57.5 |
| 59 | -9.0 | untapped | W | 3W | Flickering Hound |  |  |  |
| 60 | -10.0 | untapped | B | 1B | Extrapolate the Impossible | UR | oferece UR | 14.5 |
| 61 | -10.1 | untapped | W | 2W | Germinate Recruits | WG+ WB | pede WG · oferece WB, fichas | 63.2 |

### Incomuns (109)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +9.0 | 17lands | RG | 3RRGG | Craftwork Crusher | RG WB BG | oferece BG, RG, WB, fichas | 25.9 |
| 2 | +7.0 | 17lands | R | 4RR | Kiora of Fire and Ashes | RG WB | oferece RG, WB, fichas | 31.3 |
| 3 | +6.4 | 17lands | U | 1U | Geist of Saint Thalia | UR+ WU WB | pede UR · oferece WB, WU | 57.5 |
| 4 | +6.1 | 17lands | W | 2W | Your Fate Ends Here | RG+ WU UB | pede RG · oferece UB, WU | 54.9 |
| 5 | +5.8 | 17lands | U | 3U | Plan for All Outcomes | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 51.9 |
| 6 | +5.1 | 17lands | B | 1B | Multiply by Zero | UR | oferece UR | 14.5 |
| 7 | +5.0 | 17lands | BG | 2BBG | Hapatra, the Desert Fang | UB+ RG | pede UB · oferece RG | 37.3 |
| 8 | +5.0 | 17lands | U | 1U | Fblthp, Impossibly Lost | WU WB | oferece WB, WU | 3.2 |
| 9 | +4.9 | 17lands | W | 3W | Way of the Healer | UG+ WU UB WB | pede UG, planeswalker · oferece UB, WB, WU, fichas | 81.7 |
| 10 | +4.8 | 17lands | R | 2RR | Violent Echoes | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 44.3 |
| 11 | +4.7 | 17lands | UR | 1UR | Clash of Elements |  |  |  |
| 12 | +4.4 | 17lands | U | 1U | Proft, Consulting Detective | WU+ WB WR | pede WU · oferece WB, WR | 60.7 |
| 13 | +4.3 | 17lands | - | 6 | Archive Arbiter | RG WG BG | oferece BG, RG, WG | 14.1 |
| 14 | +3.7 | 17lands | B | 2B | Break Under Pressure | WG | oferece WG | 7.5 |
| 15 | +3.5 | 17lands | UB | 2UB | Recursive Recruitment | UB+ WB WR | pede UB · oferece WB, WR, fichas | 62.5 |
| 16 | +3.4 | 17lands | UB | UB | Theorix Charm | UB UR | oferece UB, UR | 19.8 |
| 17 | +3.1 | 17lands | U | UU | Countersculpt | UG+ WU UB UR | pede UG, planeswalker · oferece UB, UR, WU | 66.4 |
| 18 | +2.9 | 17lands | U | 4U | Way of the Mind Sculptor | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 51.9 |
| 19 | +2.8 | untapped | UG | 3GUU | Mind Meanderer | RG BG | oferece BG, RG | 2.4 |
| 20 | +2.7 | 17lands | R | 2R | Fulminous Forte |  |  |  |
| 21 | +2.1 | 17lands | B | 3B | Rewrite Regrets | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 47.7 |
| 22 | +2.1 | 17lands | UR | 2UR | Saheeli, Jewel of Avishkar | UR+ WB | pede UR · oferece WB, fichas | 47 |
| 23 | +2.0 | 17lands | BG | 1BG | Primal Witchstalker | UB | oferece UB | 8.2 |
| 24 | +1.4 | 17lands | WU | 1W/UW/U // 2W/U | Prudent Fateseer // Peer Review | WU+ UB WB UR | pede WU, fichas · oferece UB, UR, WB, fichas | 76.9 |
| 25 | +1.3 | untapped | WB | 2WWB | Twisted Fates | WR | oferece WR | 5 |
| 26 | +1.1 | 17lands | UB | 1U/B // U/B | Paradox Shaper // Omit Variables | WU UB WB UR | oferece UB, UR, WB, WU | 21.7 |
| 27 | +1.1 | 17lands | G | XGG | Fblthp, Knows the Way | WU WB | oferece WB, WU | 2.5 |
| 28 | +1.1 | untapped | W | 2W | Generous Revival | WB+ UB WR | pede WB · oferece UB, WR | 61.1 |
| 29 | +0.9 | untapped | WU | WU | Fatehold Charm | UR UG | pede fichas · oferece UG, UR | 50.5 |
| 30 | +0.9 | untapped | WG | 2GW | Bloombrute | WG+ BG+ | pede BG, WG | 36.4 |
| 31 | +0.8 | untapped | WG | 1G/W // G/W | Vigorbloom Vanguard // Seed Suture | WR+ WU WG WB UR | pede WR, fichas · oferece UR, WB, WG, WU | 54.6 |
| 32 | +0.5 | untapped | U | 4UU | Ruric Thar, Biomagus | UR+ RG BG | pede UR · oferece BG, RG | 58.2 |
| 33 | +0.4 | untapped | W | 1W | Teyo, Lightshield Expert | UG+ WU WB WR | pede UG, planeswalker · oferece WB, WR, WU | 42.7 |
| 34 | -0.0 | untapped | B | 1B | Gallia, Tragic Host | WB+ WU UB WR | pede WB · oferece UB, WR, WU | 65.1 |
| 35 | -0.1 | untapped | R | 2R | Pia, Determined Rebuilder | RG+ WB | pede RG · oferece WB, fichas | 70.4 |
| 36 | -0.2* | draftsim | U | 1U | Precise Redaction | UR | oferece UR | 14.5 |
| 37 | -0.2 | untapped | G | 2G | Way of the Paradox | UG+ WU UB WG | pede UG, planeswalker · oferece UB, WG, WU | 55.6 |
| 38 | -0.2 | untapped | G | 5GG | Ruric Thar, Magecrusher | RG BG | oferece BG, RG | 14.6 |
| 39 | -0.3 | untapped | U | 3U | Traxos, Academy Guardian | UR+ | pede UR | 54.2 |
| 40 | -0.3 | untapped | G | G // 2R/G | Heartwood Crafter // Soul Tether | WU RG WB UR | oferece RG, UR, WB, WU | 22.7 |
| 41 | -0.4 | untapped | W | 3WW | Saheeli, Consul of Oversight | WU+ RG WB BG | pede WU · oferece BG, RG, WB, fichas | 89 |
| 42 | -0.4 | untapped | WG | GW | Vigorbloom Charm | WG UR WR | oferece UR, WG, WR | 19.5 |
| 43 | -0.4 | untapped | BR | BR | Stingerquill Charm | BR WB UR | oferece BR, UR, WB, fichas | 33.2 |
| 44 | -0.5 | untapped | G | 8G | Ghalta the Unstoppable | RG BG | oferece BG, RG | 14.6 |
| 45 | -0.5 | untapped | WR | 2RW | Warrior's Blades | BR WG WR | pede fichas · oferece BR, WG, WR | 30.5 |
| 46 | -0.5 | untapped | W | 1W | Prophesied End | UR | oferece UR | 13.8 |
| 47 | -0.6 | untapped | R | R | Marwyn, the Clearcutter | WU WB | oferece WB, WU | 2.5 |
| 48 | -0.6 | 17lands | WU | 2WU | Desperate Futurescribe | WU+ WR | pede WU · oferece WR | 40.7 |
| 49 | -0.6 | untapped | B | 2B | Tinybones, Pocket Nuisance | BR | oferece BR | 5 |
| 50 | -0.6 | untapped | RG | RG | Konstrari Charm | BG+ RG UR WR | pede BG · oferece RG, UR, WR | 36.1 |
| 51 | -0.6 | untapped | U | 1U | Tetsuko Umezawa, Fugitive | BG+ WU WB | pede BG · oferece WB, WU | 25.2 |
| 52 | -0.8 | untapped | W | 3W | Thalia, the Survivor | WG | oferece WG | 9 |
| 53 | -0.9 | untapped | G | 4G | Way of the Wildspeaker | BG+ UG+ WU UB WB | pede BG, UG, planeswalker · oferece UB, WB, WU, fichas | 100 |
| 54 | -0.9 | untapped | G | 3G | Jiang Yanggu, Never Alone |  |  |  |
| 55 | -0.9 | untapped | G | 2G | Restore with Empathy | UB WG | oferece UB, WG | 18.8 |
| 56 | -1.1 | untapped | BR | B/R // B/R | Stingerquill Voxmancer // Vicious Verse | WU BR WB UR | oferece BR, UR, WB, WU | 15.6 |
| 57 | -1.2 | untapped | U | 2U | Arni, Humble Scribe |  | oferece descarte | 0.8 |
| 58 | -1.4 | untapped | UG | 1GU | Kiora of Salt and Sand | UG+ | pede UG, planeswalker · oferece fichas | 31.9 |
| 59 | -1.4 | untapped | G | 1G | Yoshimaru, Scrappy Stray | WU WB WR | oferece WB, WR, WU | 10.5 |
| 60 | -1.6 | untapped | U | 3U | Hapatra, the Desert Frost | BG | oferece BG | 2.7 |
| 61 | -1.7 | untapped | W | 2W | Koth of the Homestead | WG WR | oferece WG, WR | 17 |
| 62 | -1.8 | untapped | W | 3W | Yuriko, Blade of the Mighty |  |  |  |
| 63 | -1.8 | untapped | B | 2B | Proft, Sinister Mastermind | UB+ BG | pede UB · oferece BG | 69.9 |
| 64 | -1.8 | untapped | G | 1G | Marwyn, the Preserver | WU UB WB | oferece UB, WB, WU | 12.2 |
| 65 | -1.8 | untapped | W | 1W | Tomik, Orzhov Lawmage | WR+ UG+ WU WB | pede UG, WR, planeswalker · oferece WB, WU | 75.5 |
| 66 | -2.1 | untapped | BR | BR | Grim Repriser | BR+ UR+ WU UB WB | pede BR, UR · oferece UB, WB, WU | 60.7 |
| 67 | -2.1 | untapped | R | 2R | Way of the Warlord | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 44.3 |
| 68 | -2.1 | untapped | U | U | Yuriko, Hope from the Shadows | UB+ WU WB | pede UB · oferece WB, WU | 78.1 |
| 69 | -2.2 | untapped | B | 2B | Winter, Tormented Loner | UB+ WB | pede UB, fichas, planeswalker · oferece WB | 103.5 |
| 70 | -2.2 | untapped | G | 3G | Titanbones, Towering Heart | WG+ BG WR | pede WG · oferece BG, WR | 39 |
| 71 | -2.3 | untapped | B | B | Mabel, Bitter Recluse | WU WB BG | oferece BG, WB, WU | 14 |
| 72 | -2.4 | untapped | R | 4R | Jiang Yanggu, Alone | RG BG WR | pede descarte · oferece BG, RG, WR, descarte | 23.9 |
| 73 | -2.5 | untapped | R | 3R | Tetsuko Umezawa, Pursuer | UR+ | pede UR | 54.6 |
| 74 | -2.7 | untapped | WB | WB | Edgar, Ancient Bloodlord | UG+ WU WG WB WR | pede UG, fichas, planeswalker · oferece WB, WG, WR, WU | 47.6 |
| 75 | -2.7 | untapped | G | G | Hunter's Axe |  | pede fichas | 22.8 |
| 76 | -2.8 | untapped | W | 8W | Ghalta the Immovable | RG | pede fichas · oferece RG | 24.2 |
| 77 | -2.9 | untapped | G | 2G | Loot, the Nexus |  |  |  |
| 78 | -3.0 | untapped | - | 4 | Traxos, Scourge Eternal | BG | oferece BG | 13 |
| 79 | -3.0 | untapped | W | 1W | Refute Destiny | WU UB UR | oferece UB, UR, WU | 30.8 |
| 80 | -3.2 | untapped | B | 2B | Way of the Deathbringer | BG+ UG+ WU UB WB | pede BG, UG, fichas, planeswalker · oferece UB, WB, WU, fichas | 117.7 |
| 81 | -3.3 | untapped | RG | 2R/G // 2R/G | Woodwork Prodigy // Soul Tether | RG UR | oferece RG, UR | 14.2 |
| 82 | -3.3 | untapped | U | 2U | Way of the Cryomancer | UR+ UG+ WU UB | pede UG, UR, planeswalker · oferece UB, WU | 106.1 |
| 83 | -3.4 | untapped | R | 2R | Koth, the Geomancer | BR RG | oferece BR, RG | 12.2 |
| 84 | -3.4 | untapped | U | U | Perfected Theory | UR | oferece UR | 14.5 |
| 85 | -3.4 | untapped | W | 2W | Rescue Girl, First Responder |  |  |  |
| 86 | -3.5 | untapped | B | 3B | Teyo, Diamondblade Mage | BG+ UG+ WR | pede BG, UG, planeswalker · oferece WR | 60.1 |
| 87 | -3.6 | untapped | B | 4B | Massacre Girl, Most Wanted | BR+ UG+ RG WG BG WR | pede BR, UG, planeswalker · oferece BG, RG, WG, WR | 67.8 |
| 88 | -3.7 | untapped | W | 2W | Danitha, Sword of Hope |  |  |  |
| 89 | -3.8 | untapped | B | 1B | Terminal Criticism | WG UR | oferece UR, WG | 22 |
| 90 | -4.0 | untapped | R | 2R | Command the Stage | BR+ UB WB WR | pede BR · oferece UB, WB, WR, fichas | 64.8 |
| 91 | -4.0 | untapped | R | 1R | Gallia, the Merrymaker | WR+ WU WB | pede WR · oferece WB, WU | 39.9 |
| 92 | -4.1 | untapped | W | 2W | Yoshimaru, Beloved Companion | WR+ | pede WR | 40.8 |
| 93 | -4.2 | untapped | WR | 1RW | Mabel, Valley Hero | WR | oferece WR | 6.5 |
| 94 | -4.3 | untapped | B | 2B | Danitha, Spear of Agony | WR | oferece WR | 7.2 |
| 95 | -4.3 | untapped | G | 3GG | Edgar, Moonlit Sovereign | WR+ RG BG | pede WR, fichas · oferece BG, RG | 66.1 |
| 96 | -4.6 | untapped | R | 1R | Way of the Pyromancer | UG+ WU UB RG | pede UG, planeswalker · oferece RG, UB, WU | 51.6 |
| 97 | -4.9 | untapped | R | 1R | Tomik, Izzet Sparkmage | UR+ WU WB | pede UR · oferece WB, WU | 57.1 |
| 98 | -5.6 | untapped | W | 2W | Way of the Mentor | WG+ UG+ WU UB | pede UG, WG, planeswalker · oferece UB, WU | 78.5 |
| 99 | -5.8 | untapped | G | G | Flourishing Grapple | UR | oferece UR | 13.8 |
| 100 | -6.1 | untapped | - |  | Hexhaven Dueling Arena | RG UR | oferece RG, UR | 22.5 |
| 101 | -6.2 | untapped | - | 1 | Eye of Jace | UB+ WU BR WG | pede UB · oferece BR, WG, WU | 93.5 |
| 102 | -6.4 | untapped | R | 4R | Winter, Team Player | UR+ RG | pede UR, fichas · oferece RG | 80.7 |
| 103 | -6.5 | untapped | R | 3R | Arni, Renowned Champion | BG | pede fichas · oferece BG | 35.8 |
| 104 | -7.1 | untapped | B | 2B | Loot, the Anomaly | UB+ WB | pede UB, fichas · oferece WB | 95.5 |
| 105 | -7.2 | untapped | G | 2G | Pia, Aether Ascetic |  | oferece descarte | 0.8 |
| 106 | -9.0 | untapped | R | 1R | Essence Burn | UR | oferece UR | 15.2 |
| 107 | -9.3 | untapped | U | 4U | Yargle, Goliath of Otaria | RG | oferece RG | 1.2 |
| 108 | -11.5 | untapped | B | 4B | Yargle, Glutton of Urborg | RG BG | oferece BG, RG | 4.1 |
| 109 | -12.3 | untapped | B | 1B | Way of the Necromancer | WB+ UG+ WU UB | pede UG, WB, planeswalker · oferece UB, WU | 92.4 |

### Comuns (81)

| # | nota | fonte | cor | custo | carta | arquétipos | elos | Σ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | +5.2 | 17lands | G | 1G | Something Worth Saving | UB WG UR | oferece UB, UR, WG | 32.5 |
| 2 | +4.8 | 17lands | U | 2U | Mindseeker Oculus | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 51.9 |
| 3 | +4.8 | 17lands | U | 1U | Icy Reception | UR | oferece UR | 14.5 |
| 4 | +4.5 | 17lands | U | 3U | Protege's Awakening | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 51.9 |
| 5 | +4.5 | 17lands | B | 3B | Extended Absence | BR WG | oferece BR, WG | 12.5 |
| 6 | +4.2 | 17lands | W | 1W | Unflinching Hortimancer | WG+ WU WB WR | pede WG · oferece WB, WR, WU | 41.2 |
| 7 | +4.0 | 17lands | B | 1B | Last Gasp | UR | oferece UR | 14.5 |
| 8 | +3.6 | 17lands | B | 1B // U/B | Void Extrapolator // Omit Variables | UB+ WU WB UR | pede UB · oferece UR, WB, WU | 84 |
| 9 | +3.5 | 17lands | U | U | Unsummon | UR | oferece UR | 14.5 |
| 10 | +3.4 | 17lands | U | 4U | Undulating Witness | RG | oferece RG | 1.2 |
| 11 | +3.1 | 17lands | WU | 1W/U // 2W/U | Fatehold Chronologist // Peer Review | WU UB WB UR | oferece UB, UR, WB, WU, fichas | 39.2 |
| 12 | +3.1 | 17lands | R | 1R | No Admittance | UG+ WU UB BR UR | pede UG, planeswalker · oferece BR, UB, UR, WU | 64.6 |
| 13 | +3.1 | 17lands | R | 2R | Wrath of the Bloodmane |  |  |  |
| 14 | +3.0 | 17lands | WG | G/W // G/W | Emergency Phytomedic // Seed Suture | WU WG WB UR WR | oferece UR, WB, WG, WR, WU | 20.8 |
| 15 | +3.0 | 17lands | G | 1G | Compel Brutality | UG+ UR | pede UG, planeswalker · oferece UR | 45.6 |
| 16 | +2.3 | 17lands | W | 1W | Surgical Precision | WG UR | oferece UR, WG | 22.8 |
| 17 | +2.2 | 17lands | W | 4WW | Hexhaven Battalion | UG+ WU UB WB | pede UG, planeswalker · oferece UB, WB, WU, fichas | 81.7 |
| 18 | +2.0 | 17lands | U | 1U | Surveillance Phantasm | WU+ UB WB | pede WU · oferece UB, WB | 64.7 |
| 19 | +1.9 | 17lands | UG | 1G/U | Tam's Resistance | UG+ WU UB UR WR | pede UG, planeswalker · oferece UB, UR, WR, WU | 39.4 |
| 20 | +1.9 | 17lands | G | 1G | Arcane Amphisbaena | UG+ WU UB WB BG | pede UG, planeswalker · oferece BG, UB, WB, WU | 60.9 |
| 21 | +1.8 | 17lands | W | 2W | Memory Trap |  |  |  |
| 22 | +1.8 | 17lands | - |  | Transformative Commons | RG | oferece RG | 7.2 |
| 23 | +1.5 | 17lands | G | 4GG | Vinelasher Adept | RG WR | oferece RG, WR | 9.6 |
| 24 | +1.5 | 17lands | - |  | Formidable Commons | RG | oferece RG | 7.2 |
| 25 | +1.0 | 17lands | R | 4R | Awaken the Inferno | WR | oferece WR | 7.2 |
| 26 | +1.0 | 17lands | U | 1U | Cryotheory Adept | UR+ WU UB WB | pede UR · oferece UB, WB, WU | 68.7 |
| 27 | +0.8 | 17lands | - | 2 | Medic's Kitesail | WG | pede fichas · oferece WG | 36.2 |
| 28 | +0.8 | 17lands | - | 3 | Keeper of the Quiet Hour | UG+ WU UB | pede UG, planeswalker · oferece UB, WU | 53 |
| 29 | +0.7 | 17lands | - |  | Fatehold Annex | RG | oferece RG | 7.2 |
| 30 | +0.7 | 17lands | W | 3W // G/W | Blossom-Blessed Angel // Seed Suture | WG UR WR | oferece UR, WG, WR | 30.8 |
| 31 | +0.6 | 17lands | U | 3U // 2W/U | Semester Foreseer // Peer Review | WU UB WB UR | oferece UB, UR, WB, WU, fichas | 64 |
| 32 | +0.5 | 17lands | U | 2U | Divining Duelist |  | oferece descarte | 0.8 |
| 33 | +0.5 | 17lands | - |  | Room of Refuge | WR | oferece WR | 8 |
| 34 | +0.4 | 17lands | WB | W/B | Blessed Ghoul | WU UB WG WB | oferece UB, WB, WG, WU | 16 |
| 35 | +0.4 | 17lands | U | 2U | Infinite Coursework | UR | pede fichas · oferece UR | 39.5 |
| 36 | +0.3 | 17lands | R | 1R | Skilled Battlecarver | WU WB | oferece WB, WU | 2.5 |
| 37 | +0.3 | 17lands | UB | 2U/B // U/B | Theorix Metamage // Omit Variables | UB+ UR | pede UB · oferece UR | 52.2 |
| 38 | +0.2 | 17lands | G | 2G | Greenhouse Propagator | RG WG | pede fichas · oferece RG, WG | 38.2 |
| 39 | +0.1 | untapped | G | 4G | Wrecking Gecko | BG+ RG | pede BG · oferece RG | 25.5 |
| 40 | +0.0 | 17lands | B | 4BB | Apex Witchstalker | RG WG BG | oferece BG, RG, WG | 11.6 |
| 41 | -0.1 | 17lands | B | 1B | Rank Rat | WU WB | oferece WB, WU | 2.5 |
| 42 | -0.1 | 17lands | - | 3 | Murmuring Volume |  | oferece descarte | 0.8 |
| 43 | -0.1 | 17lands | W | 1W | Campus Crier | UG+ WU UB WB | pede UG, planeswalker · oferece UB, WB, WU | 49.7 |
| 44 | -0.2 | 17lands | B | 1B | Silence the Echo | WB UR | pede fichas · oferece UR, WB | 43 |
| 45 | -0.3 | 17lands | UR | 1U/R | Twinned Vision | UB UR | oferece UB, UR, descarte | 20.5 |
| 46 | -0.5 | untapped | - |  | Innovative Commons | RG | oferece RG | 7.2 |
| 47 | -0.5 | 17lands | - |  | Meticulous Commons | RG | oferece RG | 7.2 |
| 48 | -0.7 | 17lands | B | 2B | Screeching Soulbreaker | BR WG | oferece BR, WG | 12.5 |
| 49 | -0.7 | 17lands | RG | 1R/G // 2R/G | Konstrari Improviser // Soul Tether | WU RG WB UR | oferece RG, UR, WB, WU | 15.2 |
| 50 | -0.8 | 17lands | - |  | Theorix Annex | RG | oferece RG | 7.2 |
| 51 | -0.8 | 17lands | B | 2B | Theoretical Necromancer | WB+ UB BG | pede WB · oferece BG, UB | 59.5 |
| 52 | -0.9 | 17lands | U | 1UU | Sphinx's Approach | UB | oferece UB | 11.2 |
| 53 | -1.3 | 17lands | - |  | Stingerquill Annex | RG | oferece RG | 7.2 |
| 54 | -1.3 | 17lands | R | 3R | Heartstring Puller | WB BG | oferece BG, WB, fichas | 41 |
| 55 | -1.3 | 17lands | G | 3G | Bestial Incursion | BG+ UB WB | pede BG · oferece UB, WB, fichas | 63.1 |
| 56 | -1.5 | untapped | W | 2W | Shatterwing Pegasus | WR+ | pede WR, fichas | 63.5 |
| 57 | -1.6 | untapped | G | 1G | Sureshot Sower | WU WB | oferece WB, WU | 2.5 |
| 58 | -2.2 | untapped | R | 4R | Tether Technician | BR RG BG | oferece BG, BR, RG, descarte | 10.4 |
| 59 | -2.4 | untapped | - |  | Vigorbloom Annex | RG | oferece RG | 7.2 |
| 60 | -2.4 | untapped | - |  | Konstrari Annex | RG | oferece RG | 7.2 |
| 61 | -2.5 | untapped | - | 2 | Afterthought Sentry | WU WB | oferece WB, WU | 3.2 |
| 62 | -2.6 | untapped | B | 2B | Cast Away Doubt | BR | oferece BR | 5 |
| 63 | -2.6 | untapped | R | 1R | Blazing Crescendo | UR | oferece UR | 15.2 |
| 64 | -2.6 | untapped | BG | 1B/G | Ferocity of the Hunt | BG+ | pede BG, fichas | 28.9 |
| 65 | -3.0 | untapped | W | 1W | Academic Ascent | UG+ WU UB UR | pede UG, planeswalker · oferece UB, UR, WU | 62.2 |
| 66 | -3.0 | untapped | - |  | Dedicated Commons | RG | oferece RG | 7.2 |
| 67 | -3.1 | untapped | W | 4W | Fateshaper Aspirant | UB RG WR | oferece RG, UB, WR | 18.4 |
| 68 | -3.2 | untapped | R | 2R // B/R | Hallway Heckler // Vicious Verse | BR UR | oferece BR, UR, descarte | 21 |
| 69 | -3.3 | untapped | B | 1B | Solve for Disappointment | UG+ WU UB UR | pede UG, planeswalker · oferece UB, UR, WU | 62.2 |
| 70 | -3.4 | untapped | W | 2W | Graft Surgeon | WR+ WB | pede WR · oferece WB | 45.8 |
| 71 | -3.5 | untapped | R | 1R | Eardrum Rattler | WU WB | oferece WB, WU | 2.5 |
| 72 | -3.5 | untapped | G | 2G | Inspired Tethermage | UG+ WU UB WR | pede UG, planeswalker · oferece UB, WR, WU | 54.6 |
| 73 | -3.5 | untapped | R | 2R | Chandra's Emberling | UR+ WR | pede UR · oferece WR | 61.9 |
| 74 | -3.8 | untapped | WR | 2R/W | Charge the Sanctum | WR | pede fichas · oferece WR | 21 |
| 75 | -3.9 | untapped | - | 2 | Living Library | WU WB | oferece WB, WU | 3.2 |
| 76 | -4.3 | untapped | G | 2G | Budding Insurgent |  |  |  |
| 77 | -5.1 | untapped | B | 3B | Rampart Hunter | BG+ | pede BG | 22.2 |
| 78 | -5.2 | untapped | BR | 3B/R // B/R | Whiplash Wordsmith // Vicious Verse | BR+ UR | pede BR · oferece UR | 27.5 |
| 79 | -5.4 | untapped | G | G | Tethermage's Advantage | UR | oferece UR | 13.8 |
| 80 | -6.3 | untapped | W | 1W | Predictive Preparations | UB UR WR | oferece UB, UR, WR | 30.8 |
| 81 | -7.5 | untapped | R | R | Artifist Acumen | UR | oferece UR | 15.2 |

## 2. Depois da primeira escolha: os melhores segundos picks

Para cada rara ou mítica, em ordem de poder, as cartas da coleção que o motor mais quer no
P1P2 (nota = poder + parceiros + o pouco de encaixe que o pick 2 já pesa). Para o terceiro
pick em diante: `mtg draft map fra --card "Primeira" --card "Segunda"`, ou o motor ao
vivo (`mtg draft watch`, Oráculo).

**Ajani Unrelenting** (M, R, {4}{R}{R}, +17.0 untapped) · WR+ UG+ WB · pede UG, WR, fichas, planeswalker · oferece WB, descarte, fichas, planeswalker
- +14.0 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +1.8 · encaixe -0.2 ↔ Ajani Unrelenting 3
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.3 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +1.2 · encaixe -0.2 ↔ Ajani Unrelenting 2
- +11.0 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.9 · encaixe -0.2 ↔ Ajani Unrelenting 1.5
- +10.9 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +1.2 · encaixe -0.2 ↔ Ajani Unrelenting 2
- +9.3 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe -0.2

**Uldaros Theorix** (M, UB, {3}{U}{B}{B}, +13.2 untapped) · UB RG BG · oferece BG, RG, UB
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.6 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe +0.1 ↔ Uldaros Theorix 0.25
- +10.5 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.8 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.1 · encaixe -0.2 ↔ Uldaros Theorix 0.12
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**The Theorist, Jace Beleren** (M, U, {2}{U}{U}, +12.1 untapped) · WB WR · pede fichas · oferece WB, WR, fichas, planeswalker
- +18.9 Ajani Unrelenting (M, R) poder +17.0 · parceiros +1.8 · encaixe -0.2 ↔ The Theorist, Jace Beleren 3
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ The Theorist, Jace Beleren 1
- +10.7 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe -0.2 ↔ The Theorist, Jace Beleren 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ The Theorist, Jace Beleren 1
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Garruk, Veiled Butcher** (M, B, {3}{B}{B}, +11.0 untapped) · BG+ WB · pede BG · oferece WB, fichas, planeswalker
- +18.3 Ajani Unrelenting (M, R) poder +17.0 · parceiros +1.2 · encaixe -0.2 ↔ Garruk, Veiled Butcher 2
- +12.8 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.1 · encaixe -0.1 ↔ Garruk, Veiled Butcher 0.25
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Garruk, Veiled Butcher 1
- +11.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe +0.1 ↔ Garruk, Veiled Butcher 1
- +10.0 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.3 · encaixe -0.2 ↔ Garruk, Veiled Butcher 0.5
- +9.5 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.1 · encaixe -0.2 ↔ Garruk, Veiled Butcher 0.25

**Overwrite the Multiverse** (M, B, {4}{B}{B}, +10.0 untapped) · UG+ WU UB · pede UG, planeswalker · oferece UB, WU
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Overwrite the Multiverse 1.5
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Overwrite the Multiverse 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.0 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe +0.1 ↔ Overwrite the Multiverse 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Overwrite the Multiverse 1
- +9.3 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe -0.2

**Garruk, Curse Breaker** (M, G, {3}{G}{G}, +9.6 untapped) · RG+ BG+ WB · pede BG, RG · oferece WB, fichas, planeswalker
- +18.3 Ajani Unrelenting (M, R) poder +17.0 · parceiros +1.2 · encaixe -0.2 ↔ Garruk, Curse Breaker 2
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Garruk, Curse Breaker 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.1 · encaixe -0.2 ↔ Garruk, Curse Breaker 0.12
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.3 · encaixe -0.2 ↔ Garruk, Curse Breaker 0.5
- +10.7 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe -0.2 ↔ Garruk, Curse Breaker 1
- +9.5 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.1 · encaixe -0.2 ↔ Garruk, Curse Breaker 0.25

**Sphinx of False Conclusions** (R, U, {2}{U}{U}, +9.2 untapped) · WB BG · oferece BG, WB, descarte
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Sphinx of False Conclusions 0.25
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.8 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.1 · encaixe -0.2 ↔ Sphinx of False Conclusions 0.25

**Aerid Konstrari** (M, RG, {1}{R}{G}{G}, +7.7 untapped) · RG+ BG · pede RG · oferece BG
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2 ↔ Aerid Konstrari 0.06
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2 ↔ Aerid Konstrari 0.06
- +10.5 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.5 · encaixe +0.1 ↔ Aerid Konstrari 0.75
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Lich's Relic** (R, B, {B}, +7.6 untapped) · pede fichas
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Lich's Relic 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Lich's Relic 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.0 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe +0.1 ↔ Lich's Relic 1
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Lich's Relic 1

**Kwia Vigorbloom** (M, WG, {3}{G}{W}{W}, +7.0 untapped) · WG+ RG BG · pede WG · oferece BG, RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2 ↔ Kwia Vigorbloom 0.06
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.3 · encaixe +0.1 ↔ Kwia Vigorbloom 0.5
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Sanctum Lurker** (R, B, {2}{B}, +6.6 untapped) · UG+ BR WG · pede UG, planeswalker · oferece BR, WG
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Sanctum Lurker 1.5
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Sanctum Lurker 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.0 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe +0.1 ↔ Sanctum Lurker 1
- +10.8 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe +0.1 ↔ Sanctum Lurker 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Sanctum Lurker 1

**Kindred Judgment** (R, W, {5}{W}{W}, +6.4 untapped)
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Null Summoner** (R, UB, {2}{U}{B}, +6.3 untapped) · UB+ BG · pede UB · oferece BG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +13.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.6 · encaixe +0.1 ↔ Null Summoner 1
- +12.6 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.6 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe +0.1 ↔ Null Summoner 0.25
- +11.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe +0.1 ↔ Null Summoner 1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2 ↔ Null Summoner 0.06

**Vraska, the Cutting Glare** (R, BG, {B}{B}{G}, +6.1 untapped) · RG BG · oferece BG, RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +12.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe +0.1 ↔ Vraska, the Cutting Glare 1
- +11.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +1.2 · encaixe +0.1 ↔ Vraska, the Cutting Glare 2
- +10.5 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1

**Denzilore Fatehold** (M, WU, {1}{W}{U}{U}, +6.1 untapped) · WU+ WR · pede WU, fichas · oferece WR
- +17.4 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.3 · encaixe -0.2 ↔ Denzilore Fatehold 0.5
- +13.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Denzilore Fatehold 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Denzilore Fatehold 0.25
- +10.3 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.1 · encaixe -0.2 ↔ Denzilore Fatehold 0.25
- +9.8 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.1 · encaixe -0.2 ↔ Denzilore Fatehold 0.25

**Hungering Puppetbeast** (R, G, {3}{G}{G}, +6.0 untapped) · RG BG WR · oferece BG, RG, WR
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Hungering Puppetbeast 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Hungering Puppetbeast 0.25
- +10.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.8 · encaixe +0.1 ↔ Hungering Puppetbeast 1.25
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Chandra, Torch of Defiance** (M, R, {2}{R}{R}, +5.8 untapped) · BR RG · oferece BR, RG, planeswalker
- +18.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe +0.1 ↔ Chandra, Torch of Defiance 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.7 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe -0.2 ↔ Chandra, Torch of Defiance 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Chandra, Torch of Defiance 1

**Lyra, Tolarian Archangel** (R, U, {1}{U}{U}, +4.6 untapped) · WB · oferece WB, fichas
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Lyra, Tolarian Archangel 1
- +13.1 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Lyra, Tolarian Archangel 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Proctor of Potential** (R, WU, {W}{U}, +3.8 untapped) · WU+ UB WB · pede WU · oferece UB, WB
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.6 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.1 · encaixe -0.2 ↔ Proctor of Potential 0.25
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Guiding Hydra** (R, W, {X}{W}, +3.6 untapped) · WU WB WR · oferece WB, WR, WU
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Guiding Hydra 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Diviner of Victory // Unwind History** (R, U, {U} // {1}{U}, +3.4 untapped) · WU+ UB WB UR · pede WU · oferece UB, UR, WB
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.7 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe -0.2 ↔ Diviner of Victory // Unwind History 1
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Avatar of Burgeoning Echoes** (M, UG, {G}{U}, +3.4 untapped) · UG+ WU UB WB WR · pede UG, planeswalker · oferece UB, WB, WR, WU
- +17.6 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.4 · encaixe -0.2 ↔ Avatar of Burgeoning Echoes 0.62
- +13.1 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Avatar of Burgeoning Echoes 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Avatar of Burgeoning Echoes 0.25
- +10.5 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe +0.1 ↔ Avatar of Burgeoning Echoes 1
- +10.2 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.1 · encaixe -0.2 ↔ Avatar of Burgeoning Echoes 0.12

**Gideon the Oathless** (R, B, {2}{B}, +3.4 untapped) · UG+ BR · pede UG, planeswalker · oferece BR, descarte
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Gideon the Oathless 1.5
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Gideon the Oathless 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.0 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe +0.1 ↔ Gideon the Oathless 1
- +10.8 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe +0.1 ↔ Gideon the Oathless 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Gideon the Oathless 1

**Simulacrum Shaper** (R, G, {1}{G}{G}, +3.4 untapped) · WB · oferece WB
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +10.0 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe +0.1

**Lyra, Archangel of Dawn** (R, W, {2}{W}, +3.3 untapped) · WG+ WR · pede WG · oferece WR
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Lyra, Archangel of Dawn 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Seasoned Cryomancer** (M, U, {1}{U}{U}, +3.2 untapped) · UB · oferece UB, descarte
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Verdant Kraken** (R, G, {4}{G}{G}{G}, +3.1 untapped) · RG WB BG · oferece BG, RG, WB, fichas
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Verdant Kraken 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Verdant Kraken 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Verdant Kraken 0.25
- +10.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.8 · encaixe +0.1 ↔ Verdant Kraken 1.25
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Carnivorous Cultivator // Enroot** (R, G, {1}{G} // {G}, +3.0 untapped) · WU UB WB UR BG · oferece BG, UB, UR, WB, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Carnivorous Cultivator // Enroot 1
- +10.6 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe +0.1 ↔ Carnivorous Cultivator // Enroot 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Repurposed Enforcer** (R, W, {1}{W}, +3.0 untapped) · UG+ WU UB WB · pede UG, fichas, planeswalker · oferece UB, WB, WU
- +18.6 Ajani Unrelenting (M, R) poder +17.0 · parceiros +1.5 · encaixe -0.2 ↔ Repurposed Enforcer 2.5
- +13.4 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +1.2 · encaixe -0.2 ↔ Repurposed Enforcer 2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.3 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +1.2 · encaixe -0.2 ↔ Repurposed Enforcer 2
- +10.9 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +1.2 · encaixe -0.2 ↔ Repurposed Enforcer 2
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe -0.2 ↔ Repurposed Enforcer 0.5

**Chandra, Chill of Compliance** (M, U, {1}{U}{U}, +2.6 untapped) · WU UB RG · oferece RG, UB, WU, planeswalker
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Chandra, Chill of Compliance 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.7 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe -0.2 ↔ Chandra, Chill of Compliance 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Chandra, Chill of Compliance 1

**Liliana the Faultless** (R, W, {W}, +2.6 untapped) · UG+ WU WG WB · pede UG, planeswalker · oferece WB, WG, WU, descarte
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Liliana the Faultless 1.5
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Liliana the Faultless 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Liliana the Faultless 1
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe -0.2 ↔ Liliana the Faultless 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Liliana the Faultless 1

**Ingris Stingerquill** (M, BR, {B}{R}{R}, +2.3 untapped) · BR WB · oferece BR, WB, fichas
- +18.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe +0.1 ↔ Ingris Stingerquill 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.4 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.1 · encaixe -0.2 ↔ Ingris Stingerquill 0.25
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +10.5 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Tenured Tethermage** (R, RG, {1}{R}{G}, +2.1 untapped) · RG+ WR · pede RG · oferece WR
- +18.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe +0.1 ↔ Tenured Tethermage 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2 ↔ Tenured Tethermage 0.06
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.4 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.3 · encaixe +0.1 ↔ Tenured Tethermage 0.5
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Jace's Machinations** (R, U, {2}{U}, +1.9 untapped) · UG+ WU UB · pede UG, planeswalker · oferece UB, WU
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Jace's Machinations 1.5
- +13.1 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Jace's Machinations 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Jace's Machinations 1
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe -0.2 ↔ Jace's Machinations 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Jace's Machinations 1

**Cruel Calculations** (R, U, {2}{U}, +1.8* draftsim)
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Theorist's Sanctum** (R, -, , +1.8 untapped) · RG UG · oferece RG, UG
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Theorist's Sanctum 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.7 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe -0.2 ↔ Theorist's Sanctum 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Theorist's Sanctum 1

**The Echoverse Fulcrum** (M, -, {2}, +1.5 untapped) · oferece descarte
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Enlightened Confidant** (M, W, {1}{W}, +1.5 untapped) · WG+ WU UB WB · pede WG · oferece UB, WB, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Variable Chaser // Arc of Fortune** (R, U, {2}{U} // {2}{U}, +1.4 untapped) · UR+ · pede UR
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Jace, Reality Sculptor** (R, U, {3}{U}{U}, +1.4 untapped) · UG+ · pede UG, planeswalker · oferece planeswalker
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Jace, Reality Sculptor 1.5
- +13.1 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Jace, Reality Sculptor 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Jace, Reality Sculptor 1
- +11.0 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.9 · encaixe -0.2 ↔ Jace, Reality Sculptor 1.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Jace, Reality Sculptor 1

**Dark Matter Manipulator** (R, B, {B}, +1.2 untapped) · UB+ WU WB · pede UB · oferece WB, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +13.3 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.6 · encaixe -0.1 ↔ Dark Matter Manipulator 1
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +11.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe +0.1 ↔ Dark Matter Manipulator 1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Stingcaster Mage** (M, R, {1}{R}, +1.1 untapped) · UB+ WU WB · pede UB · oferece WB, WU
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.1 · encaixe -0.2 ↔ Stingcaster Mage 0.25
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.7 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.6 · encaixe -0.2 ↔ Stingcaster Mage 1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Curse-Marred Demon** (R, R, {2}{R}{R}, +1.0 untapped) · BG · oferece BG, descarte
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Curse-Marred Demon 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Curse-Marred Demon 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Craterclaw Colossus** (M, R, {4}{R}{R}{R}, +0.9 untapped) · RG+ BG+ · pede BG, RG
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.1 · encaixe -0.2 ↔ Craterclaw Colossus 0.12
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.3 · encaixe -0.2 ↔ Craterclaw Colossus 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Craterclaw Colossus 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Shipwreck Marsh** (R, -, , +0.6 untapped) · RG · oferece RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Shipwreck Marsh 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Liliana the Repentant** (R, B, {1}{B}, +0.5 untapped) · UG+ WU UB WB WR · pede UG, planeswalker · oferece UB, WB, WR, WU
- +18.6 Ajani Unrelenting (M, R) poder +17.0 · parceiros +1.5 · encaixe -0.2 ↔ Liliana the Repentant 2.5
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Liliana the Repentant 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.0 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe +0.1 ↔ Liliana the Repentant 1
- +10.8 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe +0.1 ↔ Liliana the Repentant 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Liliana the Repentant 1

**Theorist's Proxy** (R, U, {1}{U}, +0.3 untapped) · UG+ WU UB WB · pede UG, planeswalker · oferece UB, WB, WU
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Theorist's Proxy 1.5
- +13.1 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Theorist's Proxy 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Theorist's Proxy 1
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe -0.2 ↔ Theorist's Proxy 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Theorist's Proxy 1

**Rise of the Deathbringer** (R, B, {4}{B}, +0.2 untapped)
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Ajani's Anguish** (R, R, {X}{R}, -0.1 untapped)
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Samut, Hazoret's Champion** (R, R, {1}{R}, -0.1 untapped) · WU WB · oferece WB, WU
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Tarmogoyf** (M, G, {1}{G}, -0.2 untapped) · WU WB · oferece WB, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +10.0 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe +0.1

**Solarium Sentry** (R, WG, {G}{W}, -0.4 untapped) · WU WG WB · oferece WB, WG, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +10.0 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe +0.1

**Vraska, Soul of Stone** (R, WUR, {U}{R}{W}, -0.4 untapped) · UR+ WB · pede UR · oferece WB, fichas
- +17.6 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.1 · encaixe +0.1 ↔ Vraska, Soul of Stone 0.25
- +12.7 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.1 · encaixe +0.1 ↔ Vraska, Soul of Stone 0.25
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.8 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Draconic Visitor** (R, R, {3}{R}{R}, -0.7 untapped) · RG BG · oferece BG, RG
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Draconic Visitor 0.25
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +10.0 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.3 · encaixe -0.2 ↔ Draconic Visitor 0.5

**Deserted Beach** (R, -, , -0.9 untapped) · RG · oferece RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Deserted Beach 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Vraska's Final Mercy** (R, B, {B}{B}, -1.2 untapped) · UG+ WU UB UR · pede UG, planeswalker · oferece UB, UR, WU
- +18.0 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe -0.2 ↔ Vraska's Final Mercy 1.5
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Vraska's Final Mercy 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.0 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe +0.1 ↔ Vraska's Final Mercy 1
- +10.8 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe +0.1 ↔ Vraska's Final Mercy 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Vraska's Final Mercy 1

**Face Yourself** (R, R, {5}{R}{R}, -1.2 untapped)
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Hexhaven Invigorator** (M, G, {G}{G}{G}{G}, -1.6 untapped) · BG · oferece BG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Hexhaven Invigorator 0.25
- +10.1 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.1 · encaixe +0.1 ↔ Hexhaven Invigorator 0.25
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Vindictive Triumph** (R, WB, {W}{B}{B}, -1.9 untapped)
- +17.2 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.3 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Darklight Phoenix** (M, B, {3}{B}, -2.0 untapped) · UB · oferece UB
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +10.5 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Haunted Ridge** (R, -, , -2.0 untapped) · RG · oferece RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Haunted Ridge 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Master of Barbs** (R, R, {1}{R}, -2.1 untapped) · BR+ WU WB · pede BR, fichas · oferece WB, WU
- +18.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe +0.1 ↔ Master of Barbs 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Master of Barbs 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Master of Barbs 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Master of Barbs 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Overgrown Farmland** (R, -, , -2.1 untapped) · RG · oferece RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Overgrown Farmland 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Tam, the Possibility** (R, UG, {1}{G}{U}, -2.2* draftsim) · UG+ · pede UG, planeswalker
- +17.4 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.2 · encaixe -0.2 ↔ Tam, the Possibility 0.38
- +13.1 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Tam, the Possibility 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Tam, the Possibility 0.25
- +10.5 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe +0.1 ↔ Tam, the Possibility 1
- +10.2 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.1 · encaixe -0.2 ↔ Tam, the Possibility 0.12

**Rockfall Vale** (R, -, , -2.4 untapped) · RG · oferece RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Rockfall Vale 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Pompous Battlemage // Improvised Act** (R, R, {R} // {R}, -2.6 untapped) · UR+ WU WB · pede UR · oferece WB, WU, descarte
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Hall of Echoes** (R, -, , -2.9 untapped) · RG · oferece RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Hall of Echoes 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Entrust the Spark** (R, UG, {3}{G}{U}, -3.0* draftsim) · pede planeswalker
- +17.4 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.1 · encaixe -0.2 ↔ Entrust the Spark 0.25
- +13.1 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe +0.1 ↔ Entrust the Spark 1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Entrust the Spark 0.25
- +10.5 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe +0.1 ↔ Entrust the Spark 1
- +10.2 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Loyal Tutor** (M, W, {W}, -3.0* draftsim) · UR · pede planeswalker · oferece UR
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Loyal Tutor 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Loyal Tutor 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Loyal Tutor 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Loyal Tutor 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Stinging Vitriol** (R, BR, {B}{R}, -3.0 untapped) · BR UR · oferece BR, UR, descarte
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +10.5 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Emrakul, the Exigent Doom** (M, -, {10}, -3.1 untapped) · RG BG · oferece BG, RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Emrakul, the Exigent Doom 1
- +10.9 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +1.2 · encaixe -0.2 ↔ Emrakul, the Exigent Doom 2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Ajani Resolute** (M, W, {1}{W}, -3.1 untapped) · WG+ UG+ WB WR · pede UG, WG, fichas, planeswalker · oferece WB, WR, fichas, planeswalker
- +19.2 Ajani Unrelenting (M, R) poder +17.0 · parceiros +2.1 · encaixe -0.2 ↔ Ajani Resolute 3.5
- +13.4 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +1.2 · encaixe -0.2 ↔ Ajani Resolute 2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.3 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +1.2 · encaixe -0.2 ↔ Ajani Resolute 2
- +11.0 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.9 · encaixe -0.2 ↔ Ajani Resolute 1.5
- +10.9 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +1.2 · encaixe -0.2 ↔ Ajani Resolute 2

**Identity Echo** (R, R, {2}{R}, -3.2* draftsim) · UG+ · pede UG, planeswalker
- +18.4 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.9 · encaixe +0.1 ↔ Identity Echo 1.5
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Identity Echo 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Identity Echo 1
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.3 · encaixe -0.2 ↔ Identity Echo 0.5
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Identity Echo 1

**Omnipresence** (M, G, {5}{G}{G}{G}, -3.2* draftsim) · pede fichas
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Omnipresence 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Omnipresence 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Omnipresence 1
- +10.6 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe +0.1 ↔ Omnipresence 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Bloodline Recollector // Ancestral Craving** (M, B, {1}{B} // {B}, -3.6 untapped) · WU WB UR · oferece UR, WB, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +10.5 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Pyre Rhymer // Molten Tide** (R, R, {1}{R}{R} // {R}, -4.0 untapped) · UR+ · pede UR
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Frostbite Pyromental** (R, UR, {U}{R}{R}, -4.2 untapped) · BG · oferece BG
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.2 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe -0.2 ↔ Frostbite Pyromental 0.25
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.8 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.1 · encaixe -0.2 ↔ Frostbite Pyromental 0.25

**Puppet Crafting** (R, G, {1}{G}, -4.3 untapped) · UB · oferece UB
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +10.0 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe +0.1

**Solitary Cell** (R, WR, {R}{W}, -4.5 untapped) · RG+ · pede RG
- +17.5 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2 ↔ Solitary Cell 0.06
- +12.3 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.8 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.1 · encaixe -0.2 ↔ Solitary Cell 0.12

**Return to the Light Realms** (M, W, {7}{W}{W}, -4.5 untapped) · UB · oferece UB
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Gideon's Memorial** (R, W, {1}{W}, -5.6 untapped)
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Karn, Gilded Guardian** (R, WUBRG, {2/W}{2/U}{2/B}{2/R}{2/G}, -5.7 untapped) · RG+ BG · pede RG · oferece BG
- +17.4 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe +0.1
- +12.9 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe +0.1 ↔ Karn, Gilded Guardian 0.06
- +12.6 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.5 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.1 · encaixe +0.1 ↔ Karn, Gilded Guardian 0.25
- +10.4 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +10.2 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.2 · encaixe +0.1 ↔ Karn, Gilded Guardian 0.38

**Roiling Canopy** (R, -, , -6.1 untapped) · RG · oferece RG
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Roiling Canopy 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Karn, Argent Defender** (R, -, {2}, -7.5 untapped) · WU WB · oferece WB, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Samut, Tyrant of Naktamun** (R, U, {1}{U}, -7.6 untapped) · UR+ WU WB · pede UR · oferece WB, WU
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.5 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe +0.1
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Sphinx of False Conclusions (R, U) poder +9.2 · parceiros +0.0 · encaixe +0.1

**Flickering Hound** (R, W, {3}{W}, -9.0 untapped)
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Extrapolate the Impossible** (R, B, {1}{B}, -10.0 untapped) · UR · oferece UR
- +17.1 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.0 · encaixe -0.2
- +12.7 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.1
- +12.2 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.0 · encaixe -0.2
- +11.4 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe +0.1
- +10.5 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe +0.1
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Germinate Recruits** (R, W, {2}{W}, -10.1 untapped) · WG+ WB · pede WG · oferece WB, fichas
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Germinate Recruits 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Germinate Recruits 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.1 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.0 · encaixe -0.2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2
- +9.7 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.0 · encaixe -0.2

**Codie, Ravenous Codex** (M, -, {3}, -10.9 untapped) · UR · pede fichas · oferece UR
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Codie, Ravenous Codex 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Codie, Ravenous Codex 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Codie, Ravenous Codex 1
- +10.3 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +0.6 · encaixe -0.2 ↔ Codie, Ravenous Codex 1
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

**Gardenize** (M, G, {1}{G}{G}, -20.4 untapped) · WB+ RG · pede WB · oferece RG
- +17.7 Ajani Unrelenting (M, R) poder +17.0 · parceiros +0.6 · encaixe -0.2 ↔ Gardenize 1
- +12.8 The Theorist, Jace Beleren (M, U) poder +12.1 · parceiros +0.6 · encaixe -0.2 ↔ Gardenize 1
- +12.6 Uldaros Theorix (M, UB) poder +13.2 · parceiros +0.0 · encaixe -0.2
- +11.7 Garruk, Veiled Butcher (M, B) poder +11.0 · parceiros +0.6 · encaixe -0.2 ↔ Gardenize 1
- +11.2 Garruk, Curse Breaker (M, G) poder +9.6 · parceiros +1.2 · encaixe +0.1 ↔ Gardenize 2
- +10.1 Overwrite the Multiverse (M, B) poder +10.0 · parceiros +0.0 · encaixe -0.2

## 3. Pares de cartas com mais sinergia direta

6559 pares com elo na coleção; os 40 primeiros (sinergia em unidades de elo;
empate pela soma de poder das duas). Elo entre duas cartas que juntas pedem três cores vale um quarto.

| sin | poder | carta A | carta B | elos |
| --- | --- | --- | --- | --- |
| 3.5 | +13.9 | Ajani Resolute | Ajani Unrelenting | WR, fichas, planeswalker, UG |
| 3.5 | -5.8 | Ajani Resolute | Edgar, Ancient Bloodlord | WG, fichas, planeswalker, UG |
| 3 | +29.2 | Ajani Unrelenting | The Theorist, Jace Beleren | WR, fichas, planeswalker |
| 3 | -2.3 | Ajani Resolute | Vigorbloom Vanguard // Seed Suture | WG, WR, fichas |
| 2.5 | +21.9 | Ajani Unrelenting | Way of the Healer | fichas, planeswalker, UG |
| 2.5 | +20.0 | Ajani Unrelenting | Repurposed Enforcer | fichas, planeswalker, UG |
| 2.5 | +19.3 | Hexhaven Battalion | Ajani Unrelenting | fichas, planeswalker, UG |
| 2.5 | +17.6 | Liliana the Repentant | Ajani Unrelenting | WR, planeswalker, UG |
| 2.5 | +17.5 | Ajani Unrelenting | Teyo, Lightshield Expert | WR, planeswalker, UG |
| 2.5 | +16.1 | Way of the Wildspeaker | Ajani Unrelenting | fichas, planeswalker, UG |
| 2.5 | +13.9 | Way of the Deathbringer | Ajani Unrelenting | fichas, planeswalker, UG |
| 2.5 | +13.6 | Ajani Unrelenting | Teyo, Diamondblade Mage | WR, planeswalker, UG |
| 2.5 | +13.5 | Ajani Unrelenting | Inspired Tethermage | WR, planeswalker, UG |
| 2.5 | +13.4 | Ajani Unrelenting | Massacre Girl, Most Wanted | WR, planeswalker, UG |
| 2.5 | +7.8 | Garruk, Veiled Butcher | Way of the Deathbringer | fichas, planeswalker, BG |
| 2.5 | +6.4 | Garruk, Curse Breaker | Way of the Deathbringer | fichas, planeswalker, BG |
| 2.5 | +4.7 | Ajani Unrelenting | Way of the Necromancer | WB, planeswalker, UG |
| 2.5 | +3.5 | Ajani Resolute | Sanctum Lurker | WG, planeswalker, UG |
| 2.5 | +1.7 | Ajani Resolute | Way of the Healer | fichas, planeswalker, UG |
| 2.5 | -0.2 | Ajani Resolute | Repurposed Enforcer | fichas, planeswalker, UG |
| 2.5 | -0.6 | Ajani Resolute | Liliana the Faultless | WG, planeswalker, UG |
| 2.5 | -0.9 | Ajani Resolute | Hexhaven Battalion | fichas, planeswalker, UG |
| 2.5 | -3.3 | Ajani Resolute | Way of the Paradox | WG, planeswalker, UG |
| 2.5 | -4.0 | Ajani Resolute | Way of the Wildspeaker | fichas, planeswalker, UG |
| 2.5 | -5.0 | Ajani Resolute | Tomik, Orzhov Lawmage | WR, planeswalker, UG |
| 2.5 | -6.3 | Ajani Resolute | Way of the Deathbringer | fichas, planeswalker, UG |
| 2.5 | -6.8 | Ajani Resolute | Massacre Girl, Most Wanted | WG, planeswalker, UG |
| 2.5 | -15.4 | Ajani Resolute | Way of the Necromancer | WB, planeswalker, UG |
| 2.25 | -3.5 | Way of the Deathbringer | Saheeli, Consul of Oversight | WU, fichas, BG |
| 2 | +28.0 | Garruk, Veiled Butcher | Ajani Unrelenting | fichas, planeswalker |
| 2 | +26.6 | Garruk, Curse Breaker | Ajani Unrelenting | fichas, planeswalker |
| 2 | +18.1 | Ajani Unrelenting | Generous Revival | WB, WR |
| 2 | +17.0 | Gallia, Tragic Host | Ajani Unrelenting | WB, WR |
| 2 | +17.0 | The Theorist, Jace Beleren | Way of the Healer | fichas, planeswalker |
| 2 | +16.5 | Ajani Unrelenting | Warrior's Blades | WR, fichas |
| 2 | +15.8 | Garruk, Curse Breaker | Vraska, the Cutting Glare | BG, RG |
| 2 | +15.2 | Ajani Unrelenting | Tomik, Orzhov Lawmage | planeswalker, UG, WR |
| 2 | +15.1 | The Theorist, Jace Beleren | Repurposed Enforcer | fichas, planeswalker |
| 2 | +14.9 | Ajani Unrelenting | Winter, Tormented Loner | fichas, planeswalker |
| 2 | +14.4 | Hexhaven Battalion | The Theorist, Jace Beleren | fichas, planeswalker |

## 4. Arquétipos: payoffs e enablers em ordem de poder

### WU Agressivo com Vigiar de Futurforte · par 56.2%

Use vigiar e anteveja o futuro do seu grimório para construir ameaças e pressionar seus oponentes.

Payoffs (8): Denzilore Fatehold +6.1, Proft, Consulting Detective +4.4, Proctor of Potential +3.8, Diviner of Victory // Unwind History +3.4, Surveillance Phantasm +2.0, Prudent Fateseer // Peer Review +1.4, Saheeli, Consul of Oversight -0.4, Desperate Futurescribe -0.6

Enablers (84): Overwrite the Multiverse +10.0, Geist of Saint Thalia +6.4, Your Fate Ends Here +6.1, Plan for All Outcomes +5.8, Fblthp, Impossibly Lost +5.0, Way of the Healer +4.9, Mindseeker Oculus +4.8, Violent Echoes +4.8, Protege's Awakening +4.5, Unflinching Hortimancer +4.2

### UB Matemática do Cemitério de Theorix · par 55.3%

Triture a si mesmo para atingir o limiar e transformar o cemitério em uma fonte de poder confiável.

Payoffs (12): Null Summoner +6.3, Hapatra, the Desert Fang +5.0, Void Extrapolator // Omit Variables +3.6, Recursive Recruitment +3.5, Dark Matter Manipulator +1.2, Stingcaster Mage +1.1, Theorix Metamage // Omit Variables +0.3, Proft, Sinister Mastermind -1.8, Yuriko, Hope from the Shadows -2.1, Winter, Tormented Loner -2.2

Enablers (66): Uldaros Theorix +13.2, Overwrite the Multiverse +10.0, Your Fate Ends Here +6.1, Plan for All Outcomes +5.8, Something Worth Saving +5.2, Way of the Healer +4.9, Mindseeker Oculus +4.8, Violent Echoes +4.8, Protege's Awakening +4.5, Proctor of Potential +3.8

### BR Dano Direto de Aculeopena · par 53.9%

Jogue sal na ferida usando cards que causam dano diretamente ao seu oponente, o que por sua vez permite fortalecer seus cards e manter a pressão.

Payoffs (5): Grim Repriser -2.1, Master of Barbs -2.1, Massacre Girl, Most Wanted -3.6, Command the Stage -4.0, Whiplash Wordsmith // Vicious Verse -5.2

Enablers (17): Sanctum Lurker +6.6, Chandra, Torch of Defiance +5.8, Extended Absence +4.5, Gideon the Oathless +3.4, No Admittance +3.1, Ingris Stingerquill +2.3, Stingerquill Charm -0.4, Warrior's Blades -0.5, Tinybones, Pocket Nuisance -0.6, Screeching Soulbreaker -0.7

### RG Aceleração de Mana de Konstrari · par 55.1%

Crie fichas de Xilocardio (Heartwood) para obter muito mana e mostrar ao oponente a arte de construir coisas grandes!

Payoffs (8): Garruk, Curse Breaker +9.6, Aerid Konstrari +7.7, Your Fate Ends Here +6.1, Tenured Tethermage +2.1, Craterclaw Colossus +0.9, Pia, Determined Rebuilder -0.1, Solitary Cell -4.5, Karn, Gilded Guardian -5.7

Enablers (58): Uldaros Theorix +13.2, Craftwork Crusher +9.0, Kiora of Fire and Ashes +7.0, Kwia Vigorbloom +7.0, Vraska, the Cutting Glare +6.1, Hungering Puppetbeast +6.0, Chandra, Torch of Defiance +5.8, Hapatra, the Desert Fang +5.0, Archive Arbiter +4.3, Undulating Witness +3.4

### WG Ganho de Vida de Vigorflor · par 53.8%

Faça suas criaturas crescerem de várias maneiras enquanto aumenta a vida para dominar o campo de batalha com remédios amargos.

Payoffs (9): Kwia Vigorbloom +7.0, Unflinching Hortimancer +4.2, Lyra, Archangel of Dawn +3.3, Enlightened Confidant +1.5, Bloombrute +0.9, Titanbones, Towering Heart -2.2, Ajani Resolute -3.1, Way of the Mentor -5.6, Germinate Recruits -10.1

Enablers (26): Sanctum Lurker +6.6, Something Worth Saving +5.2, Extended Absence +4.5, Archive Arbiter +4.3, Break Under Pressure +3.7, Emergency Phytomedic // Seed Suture +3.0, Liliana the Faultless +2.6, Surgical Precision +2.3, Vigorbloom Vanguard // Seed Suture +0.8, Medic's Kitesail +0.8

### WB Desgaste de Liliana · par 53.6%

Recorra ao cemitério para obter efeitos que permitem continuar colocando criaturas pequenas no campo de batalha até enterrar seus inimigos.

Payoffs (5): Generous Revival +1.1, Gallia, Tragic Host -0.0, Theoretical Necromancer -0.8, Way of the Necromancer -12.3, Gardenize -20.4

Enablers (88): Ajani Unrelenting +17.0, The Theorist, Jace Beleren +12.1, Garruk, Veiled Butcher +11.0, Garruk, Curse Breaker +9.6, Sphinx of False Conclusions +9.2, Craftwork Crusher +9.0, Kiora of Fire and Ashes +7.0, Geist of Saint Thalia +6.4, Fblthp, Impossibly Lost +5.0, Way of the Healer +4.9

### UR Destreza de Chandra · par 55.1%

Conjure mágicas que não sejam de criatura para desencadear habilidades e manter a pressão sobre seus oponentes.

Payoffs (16): Geist of Saint Thalia +6.4, Saheeli, Jewel of Avishkar +2.1, Variable Chaser // Arc of Fortune +1.4, Cryotheory Adept +1.0, Ruric Thar, Biomagus +0.5, Traxos, Academy Guardian -0.3, Vraska, Soul of Stone -0.4, Grim Repriser -2.1, Tetsuko Umezawa, Pursuer -2.5, Pompous Battlemage // Improvised Act -2.6

Enablers (55): Something Worth Saving +5.2, Multiply by Zero +5.1, Icy Reception +4.8, Last Gasp +4.0, Void Extrapolator // Omit Variables +3.6, Unsummon +3.5, Diviner of Victory // Unwind History +3.4, Theorix Charm +3.4, Fatehold Chronologist // Peer Review +3.1, No Admittance +3.1

### BG Bestiário de Garruk · par 54.8%

Coloque criaturas assustadoras em jogo para caçar seus inimigos. Combine toque mortífero e atropelar para esmagar qualquer defesa!

Payoffs (13): Garruk, Veiled Butcher +11.0, Garruk, Curse Breaker +9.6, Craterclaw Colossus +0.9, Bloombrute +0.9, Wrecking Gecko +0.1, Konstrari Charm -0.6, Tetsuko Umezawa, Fugitive -0.6, Way of the Wildspeaker -0.9, Bestial Incursion -1.3, Ferocity of the Hunt -2.6

Enablers (37): Uldaros Theorix +13.2, Sphinx of False Conclusions +9.2, Craftwork Crusher +9.0, Aerid Konstrari +7.7, Kwia Vigorbloom +7.0, Null Summoner +6.3, Vraska, the Cutting Glare +6.1, Hungering Puppetbeast +6.0, Archive Arbiter +4.3, Verdant Kraken +3.1

### WR Exército de Ajani · par 53.2%

Fortaleça suas criaturas com marcadores +1/+1 para partir para a agressão à vontade!

Payoffs (8): Ajani Unrelenting +17.0, Vigorbloom Vanguard // Seed Suture +0.8, Shatterwing Pegasus -1.5, Tomik, Orzhov Lawmage -1.8, Graft Surgeon -3.4, Gallia, the Merrymaker -4.0, Yoshimaru, Beloved Companion -4.1, Edgar, Moonlit Sovereign -4.3

Enablers (41): The Theorist, Jace Beleren +12.1, Denzilore Fatehold +6.1, Hungering Puppetbeast +6.0, Proft, Consulting Detective +4.4, Unflinching Hortimancer +4.2, Guiding Hydra +3.6, Recursive Recruitment +3.5, Avatar of Burgeoning Echoes +3.4, Lyra, Archangel of Dawn +3.3, Emergency Phytomedic // Seed Suture +3.0

### UG Maestria de Jace · par 52.3%

Continue empoderando Jace para manter um fluxo constante de cards ou escolha seu caminho para a vitória com cards que concedem habilidades aos seus planeswalkers!

Payoffs (47): Ajani Unrelenting +17.0, Overwrite the Multiverse +10.0, Sanctum Lurker +6.6, Plan for All Outcomes +5.8, Way of the Healer +4.9, Mindseeker Oculus +4.8, Violent Echoes +4.8, Protege's Awakening +4.5, Avatar of Burgeoning Echoes +3.4, Gideon the Oathless +3.4

Enablers (2): Theorist's Sanctum +1.8, Fatehold Charm +0.9

## 5. Grafo de elos: centralidade e comunidades

As cartas são os nós e os elos diretos, as arestas (6559). **Centralidade** (0 a 100): um passeio
aleatório que segue um elo com chance proporcional ao peso do elo vezes a força da parceira, ou
recomeça em carta aleatória (85% de seguir); a carta central liga muitas parceiras fortes que
ligam outras. É o que a soma Σ não vê: Σ conta elos, a centralidade pesa a qualidade de quem está
do outro lado. Não torna cada elo mais certo (isso só dados de co-ocorrência em partidas fariam);
diz quais cartas são as melhores *portas de entrada* para uma coleção no começo do draft.

| # | centr. | Σ | nota | rar | cor | carta | elos |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 100 | 158.5 | +17.0 | M | R | Ajani Unrelenting | pede UG, WR, fichas, planeswalker · oferece WB, descarte, fichas, planeswalker |
| 2 | 65 | 144.43 | +9.6 | M | G | Garruk, Curse Breaker | pede BG, RG · oferece WB, fichas, planeswalker |
| 3 | 49.9 | 105.75 | +12.1 | M | U | The Theorist, Jace Beleren | pede fichas · oferece WB, WR, fichas, planeswalker |
| 4 | 43.3 | 97.92 | +11.0 | M | B | Garruk, Veiled Butcher | pede BG · oferece WB, fichas, planeswalker |
| 5 | 24.2 | 81.73 | +4.9 | U | W | Way of the Healer | pede UG, planeswalker · oferece UB, WB, WU, fichas |
| 6 | 24.1 | 47.73 | +10.0 | M | B | Overwrite the Multiverse | pede UG, planeswalker · oferece UB, WU |
| 7 | 22 | 83.99 | +3.6 | C | B | Void Extrapolator // Omit Variables | pede UB · oferece UR, WB, WU |
| 8 | 21.5 | 57.49 | +6.4 | U | U | Geist of Saint Thalia | pede UR · oferece WB, WU |
| 9 | 21.4 | 54.85 | +6.1 | U | W | Your Fate Ends Here | pede RG · oferece UB, WU |
| 10 | 20.4 | 72.49 | +3.0 | R | W | Repurposed Enforcer | pede UG, fichas, planeswalker · oferece UB, WB, WU |
| 11 | 20.3 | 79.23 | +3.4 | R | U | Diviner of Victory // Unwind History | pede WU · oferece UB, UR, WB |
| 12 | 20.1 | 55.17 | +6.1 | M | WU | Denzilore Fatehold | pede WU, fichas · oferece WR |
| 13 | 19.1 | 51.87 | +5.8 | U | U | Plan for All Outcomes | pede UG, planeswalker · oferece UB, WU |
| 14 | 18.7 | 57.75 | +5.8 | M | R | Chandra, Torch of Defiance | oferece BR, RG, planeswalker |
| 15 | 18.5 | 39.56 | +7.7 | M | RG | Aerid Konstrari | pede RG · oferece BG |
| 16 | 18.2 | 60.73 | +4.4 | U | U | Proft, Consulting Detective | pede WU · oferece WB, WR |
| 17 | 18.1 | 81.73 | +2.2 | C | W | Hexhaven Battalion | pede UG, planeswalker · oferece UB, WB, WU, fichas |
| 18 | 17.5 | 51.87 | +4.8 | C | U | Mindseeker Oculus | pede UG, planeswalker · oferece UB, WU |
| 19 | 17.5 | 66.37 | +3.1 | U | U | Countersculpt | pede UG, planeswalker · oferece UB, UR, WU |
| 20 | 17.2 | 73.5 | +2.6 | M | U | Chandra, Chill of Compliance | oferece RG, UB, WU, planeswalker |
| 21 | 16.9 | 51.87 | +4.5 | C | U | Protege's Awakening | pede UG, planeswalker · oferece UB, WU |
| 22 | 16.7 | 44.72 | +6.3 | R | UB | Null Summoner | pede UB · oferece BG |
| 23 | 16.5 | 62.49 | +3.5 | U | UB | Recursive Recruitment | pede UB · oferece WB, WR, fichas |
| 24 | 16.2 | 43.23 | +6.6 | R | B | Sanctum Lurker | pede UG, planeswalker · oferece BR, WG |
| 25 | 16.2 | 64.6 | +3.1 | C | R | No Admittance | pede UG, planeswalker · oferece BR, UB, UR, WU |

**Comunidades** (propagação de rótulos sobre os pares ligados por mais de um elo, peso 1.5 ou
mais, limiar escolhido entre 1.5, 2, 2.5 pelo que dá mais grupos;
4 grupos com 3 cartas ou mais, do maior para o menor). Grupo que junta cartas de pares
diferentes é um tema transversal (por exemplo, planeswalkers e quem os pede), que vale como
arquétipo extra ao ler os sinais da mesa. Sobre todos os elos a coleção vira um grupo só.

1. 82 cartas, poder médio +0.3, cores WUB · pares UG 48, UB 44, WU 43 · elos planeswalker 56, UG 48, UB 44: Ajani Unrelenting, The Theorist, Jace Beleren, Garruk, Veiled Butcher, Overwrite the Multiverse, Garruk, Curse Breaker, Sanctum Lurker, Vraska, the Cutting Glare, Denzilore Fatehold, Plan for All Outcomes, Chandra, Torch of Defiance …
2. 14 cartas, poder médio -1.1, cores RBU · pares WU 9, WB 9, UR 9 · elos WU 9, WB 9, UR 9: Proctor of Potential, Void Extrapolator // Omit Variables, Diviner of Victory // Unwind History, Surveillance Phantasm, Enlightened Confidant, Stingerquill Charm, Stingerquill Voxmancer // Vicious Verse, Grim Repriser, Yuriko, Hope from the Shadows, Stinging Vitriol …
3. 4 cartas, poder médio +1.5, cores WG · pares WG 4, WR 4, WU 2 · elos WG 4, WR 4, WB 2: Unflinching Hortimancer, Lyra, Archangel of Dawn, Vigorbloom Vanguard // Seed Suture, Titanbones, Towering Heart
4. 3 cartas, poder médio -2.8, cores UR · pares UR 3, WB 1 · elos UR 3, fichas 3, WB 1: Saheeli, Jewel of Avishkar, Infinite Coursework, Codie, Ravenous Codex

## Limites

- A nota de poder depende da fonte: só o 17Lands mede partidas com a amostra declarada; o
  Untapped é de outra data e de outros ranks; `*` é leitura teórica.
- Os elos vêm de padrões sobre o texto de regras (`src/mtg_builder/archetypes/<coleção>.json`):
  marcam pertencimento, não qualidade. `mtg draft synergy` mede se a marcação carrega sinal.
- O mapa não vê a mesa: sinais do draft (cores abertas, o que passou) só existem ao vivo.
- Regerar: `mtg draft update fra` e `mtg draft map fra --write`.
