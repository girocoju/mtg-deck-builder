# 003 — Plano

## Decisões

- **Regras como dados** em `formats.py` (`RULES`): cada formato é um dicionário com
  tamanho mínimo ou exato, limite de sideboard, limite de cópias e se exige comandante.
  As chaves são os nomes de formato do Scryfall, mais `limited`. Regras que o validador
  não confere ficam declaradas em `notes` e saem como aviso.
- **Legalidade vem da base**, nunca de listas no código: banidas e restritas mudam a
  cada sincronização.
- **Um leitor tolerante** para os três formatos de texto (Arena com seções e
  `(SET) número`, MTGO `.txt`, lista simples). Arquivos `.md` são lidos pelo primeiro
  bloco de código, o que permite guardar lista e explicação no mesmo arquivo em `decks/`.
- **Resolução de nomes em memória:** um índice nome → carta montado por execução
  (cerca de 0,5 s com a base real), aceitando a face da frente de cartas de duas faces e
  `Fire/Ice` para split. Erros de digitação geram sugestões por similaridade (`difflib`).
- **Exportação só com nomes**, sem código de coleção: os códigos do Arena nem sempre
  coincidem com os do Scryfall, e os importadores aceitam nomes. No Arena, cartas de duas
  faces saem com o nome da frente; cartas split mantêm os dois.
- **Custo pelo menor preço** entre as impressões (papel: USD/EUR; MTGO: tix) e, no
  Arena, pela menor raridade disponível lá. Terrenos básicos não entram.
- **Erros e avisos em português**, um por problema, para o agente repassar ou corrigir.

## Estrutura

```
src/mtg_builder/
  decklist.py   parse, resolve, merged, export, cost
  formats.py    RULES, validate, regras de comandante e de cópias
  cli.py        mtg deck validate | export | cost
tests/test_decks.py
decks/README.md   convenção dos arquivos de deck
```

## Regras cobertas

| Família | Formatos | Regras |
| --- | --- | --- |
| Construído de 60 | standard, pioneer, modern, legacy, vintage, pauper, historic, timeless, alchemy, explorer, future, premodern, oldschool, penny | ≥ 60, sideboard ≤ 15 (em BO1 e BO3), ≤ 4 cópias, restritas = 1 |
| Singleton com comandante | commander, duel, predh, paupercommander, brawl, competitivebrawl, standardbrawl (60), oathbreaker (60) | tamanho exato, cópia única, comandante válido, parceria válida, identidade de cor |
| Singleton sem comandante | gladiator | 100 exatas, cópia única |
| Limitado | limited | ≥ 40, sem limite de cópias, sem checagem de legalidade |

Exceções de cópias: terrenos básicos, "A deck can have any number of cards named" e
"up to N cards named". Comandantes: criatura lendária; veículo ou espaçonave lendários
com poder; texto "can be your commander"; planeswalker lendário nos formatos de Brawl.
Dois comandantes: partner, partner with, friends forever, background, Doctor's companion.

## Limitações conhecidas

- Não conferidos: condição de construção do companion; raridade do comandante em Pauper
  Commander; oathbreaker e signature spell.
- A importação no cliente do Arena e no MTGO não foi testada dentro dos jogos; o
  formato do `.txt` do MTGO para comandante (no bloco do sideboard) é suposição.
- Preços e raridades são os da última sincronização com o Scryfall.
