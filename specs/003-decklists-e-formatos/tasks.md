# 003 — Tarefas

- [x] Leitor de listas: Arena (seções, `(SET) número`, companion), MTGO (`SB:`, linha em
      branco), texto simples, Markdown (primeiro bloco de código)
- [x] Resolução de nomes na base, com face da frente, split com `/` e sugestões
- [x] Regras por formato como dados (`formats.RULES`)
- [x] Validação: tamanho, sideboard, cópias e exceções, legalidade,
      restritas, comandante, parceria, identidade de cor, plataforma
- [x] Exportação para Arena, MTGO e texto
- [x] Custo: USD, EUR, tix e wildcards por raridade
- [x] CLI `mtg deck validate | export | cost`
- [x] Convenção de `decks/<formato>/<nome>.md`
- [x] Testes sem rede (20 testes em `tests/test_decks.py`)
- [x] Verificação com a base real

## Verificação (2026-10-04)

- Suíte completa: 30 testes passando.
- **Standard, base real:** lista de 60 válida no deck principal; no sideboard, "Llanowar
  Elfs" gerou sugestão de "Llanowar Elves", e Lightning Bolt e Black Lotus foram
  apontadas como não legais, com o excesso de cópias em linha separada.
- **Brawl, base real:** deck de 100 cartas com Ivy, Gleeful Spellthief validado com
  `--game arena`; a mesma lista em `standardbrawl` foi recusada (tamanho e legalidade).
- **Ida e volta:** a exportação para o Arena foi relida e validada sem diferença.
- **Custo:** valores calculados para a lista de Brawl (USD, EUR, tix e wildcards).
- Tempo de uma validação com a base real: cerca de 0,5 s.

Correção de 2026-10-04: o usuário informou que o sideboard em BO1 no Arena passou a ser de
até 15 cartas; a opção `--bo1` (que limitava a 7) foi removida. Ver a lição em
`knowledge/licoes/`.

Não verificado: importação dentro do cliente do Arena e do MTGO (ver limitações no plano).
