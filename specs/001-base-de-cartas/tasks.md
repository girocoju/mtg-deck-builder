# 001 — Tarefas

- [x] Estrutura do projeto (`pyproject.toml`, pacote `mtg_builder`, `.venv`, `.gitignore`)
- [x] Schema SQLite (`cards`, `printings`, `legalities`, `sets`, `rulings`, `meta`, FTS5)
- [x] Download dos bulk files do Scryfall com controle por `updated_at`
- [x] Ingestão de cartas/impressões/legalidades, incluindo cartas multi-face
- [x] Ingestão de rulings e coleções
- [x] Buscas combináveis (`query.py`) e CLI `mtg` (sync, stats, search, card, sets, sql)
- [x] Testes sem rede (10 testes de ingestão e filtros)
- [x] Verificação com dados reais

## Verificação (2026-10-04)

- `mtg sync`: 38.705 cartas, 118.475 impressões, 79.706 rulings, 1.053 coleções,
  23 formatos. Segunda execução: "já atualizado".
- `mtg card "Ivy, Gleeful Spellthief"`: identidade UG, legal em `brawl`.
- `mtg search --format brawl --identity GU --type "legendary creature" --order edhrec`:
  só lendárias dentro de GU.
- `mtg card "Delver of Secrets"`: custo `{U}`, texto das duas faces.
- `mtg sets "Reality Fracture"`: encontra `fra` (461 cartas, lançada em 2026-10-02).
- Nenhuma carta com tipo, valor de mana, texto ou cores nulos.

## Observações para as próximas specs

- A API do Scryfall deixou de oferecer o JSON único: os bulk files agora são `.jsonl.gz`.
- Existe o bulk file `oracle_tags`, útil para a spec 004.
