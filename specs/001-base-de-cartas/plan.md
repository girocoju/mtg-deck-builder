# 001 — Plano

## Decisões

- **Scryfall, não a API da Wizards.** A Wizards não tem API pública oficial de cartas; o
  Scryfall é a referência da comunidade, tem bulk data diário e inclui legalidades,
  dados de Arena/MTGO, preços e rulings.
- **Um único bulk file de cartas (`default_cards`, ~80 MB compactado).** Ele traz uma
  linha por impressão; as cartas "oracle" são derivadas dele (primeira impressão vista de
  cada `oracle_id`). Evita baixar e reconciliar `oracle_cards` separadamente.
- **Formato `.jsonl.gz`** (o único que a API oferece hoje, em `jsonl_download_uri`): lido
  linha a linha com `gzip` + `json` da biblioteca padrão, sem dependências externas.
- **SQLite + FTS5** (biblioteca padrão do Python): um arquivo, zero servidor. BigQuery foi
  considerado e descartado por ora: a base tem ~40 mil cartas (~150 MB), cabe em disco,
  responde em milissegundos, funciona offline e não tem custo nem credenciais. Vale
  reavaliar se um dia guardarmos os datasets brutos de partidas do 17Lands (spec 008).
- **Recarga total a cada sincronização**, dentro de uma transação: simples, idempotente,
  e a base nunca fica pela metade se o processo cair.
- **`updated_at` do bulk file guardado em `meta`** para pular downloads desnecessários.
- **Legalidades em tabela própria**, só com status diferente de `not_legal`. Formatos
  novos aparecem sozinhos, sem mudança de código.

## Estrutura

```
src/mtg_builder/
  db.py        conexão, schema, função SQL subset() para identidade de cor
  scryfall.py  download dos bulk files e ingestão
  query.py     buscas
  cli.py       comando `mtg` (sync, stats, search, card, sets, sql)
tests/
  fixtures/default_cards.json   amostra de cartas no formato do Scryfall
  test_cards_db.py
data/          mtg.sqlite (fora do git, reconstruível)
```

## Modelo de dados

- `cards` — uma linha por carta oracle. Cores e identidade como texto em ordem WUBRG (`"GU"`).
- `printings` — uma linha por impressão, com raridade, plataformas, booster e preços.
- `legalities` — (`format`, `oracle_id`, `status`).
- `sets`, `rulings`, `meta`.
- `cards_fts` — índice full-text de nome, tipo e texto.

## Riscos

- Cartas sem `oracle_id` no topo (layout `reversible_card`) e cartas dupla-face sem
  custo/cores no topo: os campos são lidos da primeira face.
- Mudança de formato do bulk file: a ingestão usa `.get()` para tudo que é opcional.
