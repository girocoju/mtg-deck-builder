# 007 — Plano

## Decisões

- **Skill `deck-comandante`** (`.claude/skills/deck-comandante/SKILL.md`) com oito
  etapas, apoiada em três peças de código novas e nas specs 001 a 004.
- **EDHREC pelos arquivos JSON das páginas públicas** (`json.edhrec.com/pages/...`): a
  página do comandante (sinergia e inclusão por carta) e o deck médio. O site não tem API
  oficial; o `robots.txt` de `edhrec.com` (conferido em 2026-10-04) não restringe as
  páginas de comandantes. Uso leve: uma requisição por página, `User-Agent` identificado
  e cache de 7 dias em `data/edhrec/`.
- **Toda carta do EDHREC passa pela base** antes de ser sugerida: identidade de cor,
  legalidade no formato e existência na plataforma. O motivo de cada exclusão é mantido.
- **Deck médio como modelo** em Commander de papel (templating); em Brawl e Standard
  Brawl o filtro derruba muitas cartas e a lista é montada a partir das sinergias
  restantes mais a busca própria na base.
- **Comando `mtg commander`** responde "pode ser comandante neste formato?" com o motivo
  da recusa, antes de qualquer construção.
- **Proporções por categoria dentro de `mtg deck analyze`**: para decks com comandante, o
  relatório compara terrenos, aceleração, compra, interação pontual e remoção em massa
  com as metas de `knowledge/commander-e-brawl.md`, escaladas pelo tamanho do deck. São
  informativas (guia, não regra): desvios são justificados na entrega, não bloqueiam.
- **Bracket é estimativa explicada:** a base marca os Game Changers; os demais critérios
  (turnos extras, combos, negação de terrenos) são lidos pelo agente.

## Estrutura

```
src/mtg_builder/edhrec.py     load (cache), recommendations, average_deck, commander_report
src/mtg_builder/analysis.py   COMMANDER_TARGETS e seção de proporções
src/mtg_builder/cli.py        mtg commander | mtg edhrec
tests/test_edhrec.py          sem rede (páginas simuladas)
.claude/skills/deck-comandante/SKILL.md
```

## Limitações conhecidas

- O EDHREC mede Commander de mesa (multiplayer, 40 de vida). Em Brawl, um contra um e com
  25 de vida, as sinergias valem como candidatas, não como ranking.
- As metas de proporção para 60 cartas (Standard Brawl) são as de 100 cartas escaladas,
  sem fonte própria.
- A contagem de categorias é por texto das cartas e não enxerga o comandante.
- Comandantes com dupla (partner) usam a página combinada do EDHREC, não exercitada com
  dados reais.
