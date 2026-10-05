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

**Importação no Arena confirmada pelo usuário em 2026-10-05:** as listas exportadas foram
coladas no cliente mais de uma vez, sem problemas, inclusive as cartas de duas faces
exportadas só com o nome da frente.

**Listas do Arena em português (2026-10-05):** o cliente em português exporta os nomes
traduzidos, que não existem na base. O leitor passou a resolver a carta pela coleção e
pelo número de colecionador da linha (`2 Beladona Tûk (HOB) 4`), com teste. A lista de
60 cartas do usuário foi lida e validada assim.

**Falha de importação relatada em 2026-10-05:** uma sessão nova gravou no arquivo do deck
`Tithing Blade // Consuming Sepulcher` (carta de duas faces com os dois nomes) e o Arena
recusou com "título de card desconhecido". O exportador já gerava o nome certo, mas a
lista tinha sido escrita à mão. Correções: `mtg deck validate` passou a avisar quando a
lista tem nomes assim; as quatro skills, o `CLAUDE.md` e o `decks/README.md` mandam
entregar sempre a saída de `mtg deck export --to arena`.

Não verificado: importação no MTGO; cartas split (`Fire // Ice`) no Arena, que o
exportador mantém com os dois nomes.
