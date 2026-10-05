# 005 — Tarefas

- [x] Conferir `robots.txt` e acesso do MTGGoldfish e do Untapped.gg
- [x] Leitura da página de metagame e das listas de referência do MTGGoldfish
- [x] Snapshot datado, com fonte, modo e histórico; cache de 24 h
- [x] Conferência das listas com a base e estatísticas por arquétipo (spec 004)
- [x] Importação manual por CSV (BO1 do Arena e outras fontes)
- [x] Resumo do meta: macroarquétipos, velocidade, interação, cartas mais jogadas
- [x] Falhas claras de rede e de layout, preservando o snapshot anterior
- [x] CLI `mtg meta update | show | import`
- [x] Testes sem rede (8 testes em `tests/test_meta.py`)
- [x] Verificação com coleta real
- [x] Primeiro snapshot BO1 real (2026-10-05): **parcial**, lido de uma captura de tela do
      Untapped enviada pelo usuário — 7 das 14 listas com mais de mil partidas, com win
      rate e número de partidas, sem decklists nem fatia por arquétipo
- [x] Snapshot BO1 com fatia por arquétipo (2026-10-05): aba Meta do Untapped, lida de
      captura do usuário — 8 arquétipos mais jogados e 8 maiores win rates
- [ ] Decklists de referência dos arquétipos BO1 (modo "Text" da página Decks)

## Verificação (2026-10-04)

- Suíte completa: 49 testes passando.
- **Coleta real de Standard:** 60 arquétipos e as 12 listas principais (75% do meta),
  com data e fonte. Líderes: Izzet Spellementals 14,9%, Mono-Green Landfall 11,1%, Dimir
  Midrange 8,2%, Jund Sacrifice 8,2%.
- **Cache:** a segunda execução respondeu "ainda é recente; nada a fazer", sem requisições.
- **BO1 separado:** `mtg meta show standard` informa que não há snapshot BO1 e que ele
  vem por importação; o teste de importação confirma que BO1 e BO3 não se misturam.
- **Conferência com a base:** a primeira coleta apontou três cartas "fora da base" que
  eram nomes sem acento (Mjolnir, Dain, Kili). A resolução de nomes passou a ignorar
  acentos e a segunda coleta não apontou nenhuma.

Só o Standard foi coletado de verdade; os demais formatos usam o mesmo código e não
foram exercitados.
