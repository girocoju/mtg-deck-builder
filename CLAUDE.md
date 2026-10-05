# MTG Deck Builder

Repositório que faz do Claude Code um deck builder de Magic: The Gathering: base local de
cartas (Scryfall), teoria de deck building e dados de metagame, usados para responder
pedidos como "crie um deck anti meta no Standard" ou "estratégia de draft para a coleção X".

## Regras do projeto

- **Spec-driven:** antes de implementar qualquer coisa, leia `specs/README.md` (roadmap e
  processo) e `specs/000-constituicao.md` (princípios). Trabalhe na spec ativa; ao
  concluir tarefas, marque-as em `tasks.md` e atualize o status no roadmap.
- **Nunca cite carta de memória.** Texto, custo e legalidade vêm sempre de `mtg card` /
  `mtg search`. Se a carta não está na base, ela não entra na lista.
- **Idioma:** respostas, specs e docs em PT-BR; nomes de cartas, formatos e código em inglês.
- `NextLevelMagic2015.pdf` é material protegido: não vai para o git e não deve ser
  reproduzido; só conceitos destilados com palavras próprias (spec 002).

## Ferramentas

Ambiente: `.venv` com o pacote instalado em modo editável (`pip install -e ".[dev]"`).

```
.venv\Scripts\mtg sync                    # atualiza a base a partir do Scryfall
.venv\Scripts\mtg stats                   # contagens, formatos e data da sincronização
.venv\Scripts\mtg card "Nome"  [--rulings]
.venv\Scripts\mtg search --format brawl --identity GU --type "legendary creature" --order edhrec
.venv\Scripts\mtg search --set <código> --rarity common --booster --text "flying"
.venv\Scripts\mtg sets "<nome ou código>"
.venv\Scripts\mtg sql "SELECT ..."        # somente leitura; schema em src/mtg_builder/db.py
.venv\Scripts\python -m pytest -q
```

`--json` (antes do subcomando) devolve saída estruturada. `--text` usa sintaxe FTS5
(`"draw a card"`, `flying AND haste`). `--identity` é "identidade contida em" (regra de
Commander/Brawl); `--colors` é "tem todas estas cores".

Formatos usam as chaves do Scryfall: `standard`, `pioneer`, `modern`, `legacy`, `vintage`,
`pauper`, `commander`, `brawl` (100 cartas, Arena), `standardbrawl`, `historic`,
`timeless`, `alchemy` etc. — a lista atual sai em `mtg stats`.

## Estrutura

- `specs/` — especificações e roadmap (fonte da verdade do andamento)
- `src/mtg_builder/` — código; `tests/` — testes sem rede
- `data/` — base SQLite e downloads (fora do git, reconstruível)
- `knowledge/`, `decks/`, `drafts/` — criados pelas specs 002, 003/006/007 e 008
