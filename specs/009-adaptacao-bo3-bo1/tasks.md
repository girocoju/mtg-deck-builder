# 009 — Tarefas

- [x] `mtg deck diff` (com teste)
- [x] Skill `adaptar-bo1-bo3`
- [x] Adaptação BO3 → BO1 executada: `decks/standard/boros-tokens-anti-meta-bo1.md`
- [x] Adaptação BO1 → BO3 executada: `decks/standard/mono-red-prowess-bo3.md`
- [ ] Adaptação BO3 → BO1 contra um snapshot BO1 real (depende do CSV do Untapped)
- [ ] Caso de deck que depende do sideboard, para verificar o aviso
- [ ] Teste da skill em sessão nova, acionada só pelo pedido em linguagem natural

## Verificação (2026-10-05)

Suíte completa: 65 testes passando.

**BO3 → BO1 (Boros Tokens):**

- Sem snapshot BO1: adaptação declarada como teórica no arquivo.
- Trocas (`mtg deck diff`): saem 2 Rest in Peace e 1 Mountain; entram 2 Get Lost e
  1 Seam Rip; o sideboard de 15 sai inteiro.
- Lista válida em Standard e no Arena; todas as cartas novas já estavam no sideboard da
  origem e foram consultadas na base.
- Base de mana antes e depois: 22 → 21 terrenos (recomendado 20,9); fontes vermelhas
  17 → 16 e brancas 15 → 15, para exigência de 14; nenhum alerta.

**BO1 → BO3 (Mono-Red Prowess):**

- Snapshot usado: MTGGoldfish, 2026-10-04, BO3.
- Lista principal mantida (a origem não tinha corte de terrenos a repor); sideboard
  refeito contra o campo, com guia para oito matchups e quantidades conferidas.
- Lista válida, 60 + 15.

**Critérios ainda não verificados:** a adaptação contra um snapshot BO1 real e o aviso
para deck dependente de sideboard. Os dois decks de teste são proativos e não dependem
do sideboard, então o aviso do requisito 6 não chegou a ser exercitado.
