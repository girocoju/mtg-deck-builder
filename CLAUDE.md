# MTG Deck Builder

Repositório que faz do Claude Code um deck builder de Magic: The Gathering: base local de
cartas (Scryfall), teoria de deck building e dados de metagame, usados para responder
pedidos como "crie um deck anti meta no Standard" ou "estratégia de draft para a coleção X".

## Regras do projeto

- **Spec-driven:** antes de implementar qualquer coisa, leia `specs/README.md` (roadmap e
  processo) e `specs/000-constituicao.md` (princípios). Trabalhe na spec ativa; ao
  concluir tarefas, marque-as em `tasks.md` e atualize o status no roadmap.
- **Use a teoria.** Ao construir, ajustar ou explicar um deck, leia os documentos de
  `knowledge/` indicados no índice e cite o conceito usado.
- **Nunca cite carta de memória.** Texto, custo e legalidade vêm sempre de `mtg card` /
  `mtg search`. Se a carta não está na base, ela não entra na lista.
- **Lista entregue é lista validada.** Antes de mostrar uma decklist, rode
  `mtg deck validate` no formato pedido e corrija até passar; rode `mtg deck analyze`
  e resolva ou justifique cada alerta. Decks ficam em
  `decks/<formato>/<nome>.md` (convenção em `decks/README.md`).
- **Meta é dado com data.** Ao usar `mtg meta show`, cite fonte, data e modo (BO1/BO3).
  Sem snapshot do modo pedido, diga isso e trate a análise como teórica; nunca use o
  meta BO3 como se fosse BO1.
- **Idioma:** respostas, specs e docs em PT-BR; nomes de cartas, formatos e código em inglês.
- `NextLevelMagic2015.pdf` é material protegido: não vai para o git e não deve ser
  reproduzido; só conceitos destilados com palavras próprias (spec 002).

## Skills

- `deck-construido` (`.claude/skills/deck-construido/SKILL.md`): pedidos de deck de 60
  cartas em formatos de construído, inclusive anti-meta. Siga as etapas dela.
- `deck-comandante` (`.claude/skills/deck-comandante/SKILL.md`): Commander, Brawl e
  Standard Brawl, a partir de um comandante.
- `draft` (`.claude/skills/draft/SKILL.md`): guia de draft de uma coleção, ajuda com
  picks e montagem de deck de 40 a partir de um pool.
- `adaptar-bo1-bo3` (`.claude/skills/adaptar-bo1-bo3/SKILL.md`): adapta uma lista de 60
  cartas entre BO3 e BO1, nos dois sentidos.

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
.venv\Scripts\mtg deck validate <arquivo> --format brawl [--game arena]
.venv\Scripts\mtg deck export <arquivo> --to arena|mtgo|text
.venv\Scripts\mtg deck cost <arquivo>
.venv\Scripts\mtg deck diff <antes> <depois>      # o que saiu e o que entrou
.venv\Scripts\mtg deck analyze <arquivo>          # curva, terrenos, fontes por cor, papéis, alertas
.venv\Scripts\mtg odds --copies 4 --turn 4 [--deck 60] [--min 1] [--draw]
.venv\Scripts\mtg commander "Nome" [--partner "Nome"] --format brawl   # pode ser comandante?
.venv\Scripts\mtg edhrec "Nome" --format brawl --game arena [--average]  # sinergias filtradas pela base
.venv\Scripts\mtg draft update fra --mode all      # 17Lands: premier, quick, trad, sealed, tradsealed, picktwo
.venv\Scripts\mtg draft set|colors|gaps fra        # leitura da coleção, pares de cores, sub/superestimadas
.venv\Scripts\mtg draft cards fra --color U --rarity common [--mode trad]
.venv\Scripts\mtg draft rate fra "Carta A" "Carta B" [--file pool.txt]
.venv\Scripts\mtg meta update standard          # coleta do MTGGoldfish (BO3), no máximo 1x por dia
.venv\Scripts\mtg meta show standard [--mode bo1|bo3]   # arquétipos, resumo, cartas mais jogadas
.venv\Scripts\mtg meta import meta.csv --format standard --mode bo1 --source untapped
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
- `knowledge/` — teoria de deck building por tema; comece por `knowledge/README.md`, que diz
  o que ler para cada tipo de pedido. Para acrescentar fonte ou lição: `knowledge/COMO-ADICIONAR.md`
- `scripts/` — extração de PDF e verificação de cópia para a base de conhecimento
- `decks/` — decks gerados (lista em bloco de código + explicação)
- `drafts/` — guias de draft por coleção (`drafts/fra.md` é o modelo)
