# 014 — Tarefas

- [x] `archetypes.py`: elos por carta (`links`), sinergia entre duas cartas (`link_scores`,
      `synergy`, `links_between`), ganchos no arquivo (`hooks`), pesos de enabler genérico,
      payoff compartilhada e splash; ganchos de FRA (fichas, planeswalker, descarte)
- [x] `draft_pick.py`: componente `parceiros` (peso 0,6 por elo, teto 3,0), coluna `parc` e
      `↔ parceiros` na tabela, cache de funções por nome
- [x] `draft_map.py`: cartas draftáveis, ordem por raridade, pares, parceiros, próximos picks
      (motor sobre a coleção inteira), árvore (raras e míticas → segundos picks), tabelas por
      arquétipo, centralidade (PageRank com pesos), comunidades (propagação de rótulos sobre
      pares com peso ≥ 1,5), documento Markdown
- [x] `mtg draft map` (`--rarity`, `--card`, `--pack/--pick`, `--pairs`, `--graph`, `--top`,
      `--write`, `--json`)
- [x] Testes (`tests/test_draft_map.py`): elos, sinergia, componente, mapa, grafo, documento
- [x] `drafts/fra-mapa.md` gerado; `CLAUDE.md` (regra e comando), skill `draft` (seções A e B),
      roadmap
- [x] Leitura da coleção em `draft_map.py` (`overview`, `archetype_summary`, `hook_summary`,
      `analysis_lines`, seção 0 do Markdown) e `communities_auto` (limiar 1,5 / 2,0 / 2,5)
- [x] `draft_map_pdf.py` (matplotlib, extra `viz`) e `mtg draft map --pdf`: capa, coleção em
      números, leitura, pares nos dados, arquétipos (visão geral e duas por página), ordem por
      raridade, grafo, comunidades, centralidade, pares, segundos picks, limites
- [x] `archetypes/trk.json`: dez pares (WU espaçonaves, UB dilemas, BR Klingons e sacrifício,
      RG landfall, WG marcadores +1/+1, WB criaturas artefato Borg, UR mágicas não criatura,
      BG cemitério e vigiar, WR poder total 8, UG terrenos de nomes diferentes) e oito ganchos
      (fichas, virar, oficiais, vida, tesouros, klingons, equipamentos, teletransporte)
- [x] Testes: leitura, resumo, comunidades automáticas, PDF (pula sem matplotlib), arquivos
      reais de arquétipos compilam; `drafts/trk-mapa.md`, `trk-mapa.pdf`, `fra-mapa.pdf`
      gerados; `CLAUDE.md`, skill `draft`, `drafts/trk.md`, roadmap
- [ ] Depois do primeiro draft real: conferir os elos indicados contra o deck montado e
      registrar aqui se algum peso (parceiros, enabler genérico, splash) precisa mudar
- [ ] Quando o 17Lands voltar a publicar GIH WR das raras e míticas: `mtg draft update fra` e
      `mtg draft map fra --write --pdf`; anotar o que mudou na ordem
- [ ] Quando TRK tiver dados (e a tela do evento no Arena): nomes oficiais dos arquétipos em
      `trk.json`, `mtg draft update trk` e `mtg draft map trk --write --pdf`; comparar a ordem
      teórica com a medida

## Verificação (2026-11-09)

- Suíte: 116 testes passando, 2 novos (leitura + PDF; arquivos de arquétipos).
- Base sincronizada em 2026-11-09: TRK passou de 91 para 311 cartas (306 draftáveis: 26
  míticas, 79 raras, 110 incomuns, 91 comuns); 17Lands sem a coleção em todos os modos.
- Marcação de TRK conferida carta a carta na saída do script de checagem: 5 cartas sem elo
  (Malfunctioning Holodeck, Year of Hell, Mr. Spock, Dominion Saboteur, Peace in Our Time);
  padrão de payoff WU apertado para não pegar Engineered Explosives e Sarcophagus por
  "charge counter". Ganchos: fichas 16/39 (pedem/oferecem), virar 8/26, oficiais 3/44, vida
  3/39, tesouros 2/5, klingons 3/16, equipamentos 3/4, teletransporte 14/57.
- `mtg draft map trk --write --pdf`: 306 cartas, 9.163 pares, 19 páginas, 22 s. Mais
  centrais: Captain Jean-Luc Picard 100, Scotty 86, Excalbian Gamemaster 76, Captain Sisko
  73, The Destruction of Praxis 65. Comunidades com limiar 2,0 (1,5 dava um grupo de 135):
  nove grupos, os maiores com 57 (BR/WR/WB, fichas), 19 (BG/UR, teletransporte), 16 (WU/WB,
  virar: espaçonaves), 14 (BG/UB).
- `mtg draft map fra --write --pdf`: 280 cartas, 6.559 pares, 20 páginas (tem a página dos
  pares nos dados). Comunidades ficam em 1,5 (quatro grupos, como em 2026-11-08).
- Paleta (validador da skill dataviz, `--pairs all`, superfície clara): W `#eda100`,
  U `#2a78d6`, B `#7b3fa0`, R `#e34948`, G `#008300` passam o piso de visão normal (pior par
  17,1); pior par sob protanopia verde↔vermelho 7,2 (faixa 6–8: exige rótulo, que toda barra
  e nó rotulado têm); amarelo abaixo de 3:1 de contraste (relevo: rótulos e tabela no
  Markdown). Dourado para multicoloridas reprovou (colide com amarelo e vermelho): nó e
  barra divididos.
- Páginas conferidas em PNG (110 dpi): capa, números, leitura, arquétipos, ordem, grafo,
  comunidades, centralidade, pares, segundos picks, limites; corrigidos no caminho a
  sobreposição dos pequenos múltiplos, o texto das sinalizadoras fora da página, o subtítulo
  longo dos segundos picks, o asterisco indevido em centralidade e Σ, e o grafo em bola
  (atração passou a crescer com o quadrado do peso; rótulos sem sobreposição).

## Verificação (2026-11-08)

- Suíte: 114 testes passando (`python -X utf8 -m pytest -q`), 3 novos no mapa.
- Fontes em FRA: 17Lands 2026-11-08 publica GIH WR para 79 de 290 cartas (53 comuns, 26
  incomuns, nenhuma rara ou mítica), mesmo com `start_date`/`end_date` na consulta; o
  Untapped (2026-10-12) cobre 194 das restantes com 500 jogos ou mais; 7 ficam com a
  Draftsim. O mapa declara a fonte em cada linha.
- `mtg draft map fra --write`: 280 cartas draftáveis (29 míticas, 61 raras, 109 incomuns,
  81 comuns), 6.559 pares com elo, documento de 1.235 linhas em 2,5 s.
- Pacote de teste do usuário (gerador de boosters, P1P1 Ajani Unrelenting, P1P2 com 13
  cartas): Multiply by Zero +5,2 (17Lands 59,6%) continua à frente; Compel Brutality sobe
  para +4,0 com elo 1,5 com Ajani (planeswalker em jogo causa dano igual à lealdade; os
  dois são payoff de UG); Awaken the Inferno +2,1 (elo WR: marcador +1/+1); Warrior's
  Blades passa de −1,0 para +0,2 (elo 2: equipamento para as fichas de Ajani e marcador
  +1/+1); Entrust the Spark fica em 0,25 porque UG com R pede três cores.
- Sobre a coleção inteira, depois de Ajani: The Theorist, Jace Beleren +14,0 (elo 3:
  fichas, planeswalker, WR), à frente de Uldaros Theorix (+12,6, poder maior, sem elo).
- Antes de contar cada elo uma vez e pesar o enabler genérico em 0,25, Ajani somava 164
  unidades de elo e a propagação de rótulos devolvia um grupo só de 262 cartas; com peso
  mínimo 1,5 por aresta saem quatro grupos legíveis (planeswalkers e quem os pede, 82;
  vigiar e cemitério WU/UB/BR, 14; ganho de vida e contadores WG/WR, 4; mágicas UR, 3).
- Centralidade: Ajani Unrelenting 100, Garruk, Curse Breaker 65, The Theorist 50, Garruk,
  Veiled Butcher 43; depois Way of the Healer (incomum) 24, a primeira não mítica.
