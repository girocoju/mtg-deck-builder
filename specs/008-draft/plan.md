# 008 — Plano

## Decisões

- **Skill `draft`** (`.claude/skills/draft/SKILL.md`) com três fluxos: guia da coleção,
  recomendação de pick e montagem de deck a partir de um pool.
- **17Lands pelos arquivos JSON das páginas públicas** de Card Ratings e Color Ratings
  (`/card_ratings/data` e `/color_ratings/data`). O site não documenta uma API; o
  `robots.txt` (conferido em 2026-10-05) proíbe `/card_data/details` e
  `/data/card_based_performance`, que não são usados. Uso leve: duas requisições por
  coleção e modo, `User-Agent` identificado e cache de 24 horas.
- **Um snapshot por coleção e modo** em `data/17lands/<coleção>/<modo>.json`, com data,
  número de jogos e win rate médio dos usuários. Os modos nunca são combinados.
- **Amostra mínima:** cartas com menos de 500 jogos em mão ficam fora dos rankings por
  padrão; o número de jogos aparece em toda tabela.
- **O conjunto draftável vem do 17Lands quando há dados** (a lista de cartas dele é a do
  ambiente de draft); sem dados, das impressões de booster da base, ou de todas as cartas
  da coleção.
- **Modo teórico** quando não há dados: `mtg draft set` dá a leitura da coleção pela
  base, e a skill manda declarar a ausência de dados e não inventar rankings.
- **Subestimadas e superestimadas** pela diferença entre a posição no ranking de GIH WR
  e a posição no ranking de ALSA, só para comuns e incomuns.
- **O guia é escrito pelo agente**, a partir das saídas dos comandos; não há gerador
  automático de texto. `drafts/fra.md` serve de modelo.

## Estrutura

```
src/mtg_builder/draft.py   update, ranking, color_pairs, rate, over_under, set_overview
src/mtg_builder/cli.py     mtg draft update | set | cards | colors | rate | gaps
tests/test_draft.py        sem rede (respostas simuladas)
.claude/skills/draft/SKILL.md
drafts/<código>.md         guias
```

## Limitações conhecidas

- Sem ordem de pick dentro do pacote nem dados por arquétipo de três cores.
- A classificação de remoção na leitura da coleção é automática e imprecisa.
- A análise de deck não modela splash nem terrenos condicionais.
- Dados dos primeiros dias de uma coleção têm amostras pequenas; o guia precisa ser refeito.
