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
- [ ] Depois do primeiro draft real: conferir os elos indicados contra o deck montado e
      registrar aqui se algum peso (parceiros, enabler genérico, splash) precisa mudar
- [ ] Quando o 17Lands voltar a publicar GIH WR das raras e míticas: `mtg draft update fra` e
      `mtg draft map fra --write`; anotar o que mudou na ordem

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
