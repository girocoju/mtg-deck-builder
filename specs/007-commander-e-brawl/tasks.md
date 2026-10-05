# 007 — Tarefas

- [x] Conferir acesso e `robots.txt` do EDHREC
- [x] `edhrec.py`: página do comandante e deck médio, com cache e filtro pela base
- [x] `mtg commander`: validade do comandante com motivo da recusa
- [x] `mtg edhrec`: sinergias e deck médio filtrados por formato e plataforma
- [x] Proporções por categoria em `mtg deck analyze`
- [x] Skill `deck-comandante`
- [x] Testes sem rede (7 testes em `tests/test_edhrec.py`)
- [x] Três decks de verificação com dados reais
- [ ] Teste da skill em sessão nova, acionada só pelo pedido em linguagem natural
- [ ] Exercitar uma dupla de comandantes (partner) com dados reais do EDHREC

## Verificação (2026-10-04)

Suíte completa: 57 testes passando.

**Comandante inválido:** `mtg commander "Ivy, Gleeful Spellthief" --format standardbrawl`
responde que a carta não é legal no formato; `mtg commander "Lightning Bolt" --format
commander` responde que é Instant e o formato exige criatura lendária.

| Deck | Formato | Validação | Origem |
| --- | --- | --- | --- |
| `decks/brawl/ivy-gleeful-spellthief.md` | brawl, Arena | 100 cartas, identidade GU, todas no Arena; válido também em `competitivebrawl` | Lista anterior revista com as sinergias do EDHREC (125 cartas utilizáveis de 205) |
| `decks/commander/tatyova-benthic-druid.md` | commander, papel | 100 cartas válidas | Deck médio do EDHREC, com uma troca indicada pela análise de mana |
| `decks/standardbrawl/tatyova-benthic-druid.md` | standardbrawl, Arena | 60 cartas válidas, todas no Arena | 83 sinergias que sobreviveram ao filtro (221 excluídas) |

**O que a análise pegou:**

- Ivy: Lion Umbra ({G}{G}) pedia 30 fontes verdes contra 22; trocada por Slippery Bogle.
- Tatyova (Commander): Counterspell ({U}{U}) pedia 30 fontes azuis contra 24; trocada.
- Tatyova (Standard Brawl): Archdruid's Charm ({G}{G}{G}) pedia 23 fontes verdes contra
  21; trocada por Embrace the Paradox.
- Os desvios das proporções de cada deck estão tabelados e justificados no arquivo do deck.
- Tatyova (Commander) tem 2 Game Changers: declarada como bracket 3.

Os decks não foram testados em jogo. O fluxo foi executado pelo agente que escreveu a
skill, na mesma sessão.
