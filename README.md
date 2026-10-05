# MTG Deck Builder

Deck builder de Magic: The Gathering operado por comandos em linguagem natural dentro do
[Claude Code](https://claude.com/claude-code):

> "Crie um deck anti meta no formato Standard"
> "Crie uma estratégia de drafts para a coleção Reality Fracture"
> "Me ajude a montar um deck do formato Brawl com o commander Ivy, Gleeful Spellthief"

Ele combina três bases:

1. **Cartas** — todas as cartas, impressões, coleções, legalidades e rulings, via [Scryfall](https://scryfall.com/docs/api).
2. **Teoria** — conceitos de deck building destilados de *Next Level Magic*, de Patrick Chapin.
3. **Metagame** — MTGGoldfish/MTGTop8 (construído), EDHREC (Commander/Brawl) e 17Lands (draft).

O desenvolvimento é guiado por especificações: o andamento está em [specs/README.md](specs/README.md).

## Instalação

Requer Python 3.11+.

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[dev]"
.\.venv\Scripts\mtg sync      # baixa ~85 MB do Scryfall e monta data/mtg.sqlite
```

## Uso da base de cartas

```powershell
.\.venv\Scripts\mtg card "Ivy, Gleeful Spellthief"
.\.venv\Scripts\mtg search --format brawl --identity GU --type "legendary creature" --order edhrec
.\.venv\Scripts\mtg sets "Reality Fracture"
.\.venv\Scripts\mtg --json search --set dmu --rarity common --booster
```

Rode `mtg sync` de novo quando sair coleção nova ou mudar a lista de banidas (no máximo
uma vez por dia, a pedido do Scryfall).

## Aviso

Projeto de fã, não oficial, sem vínculo com a Wizards of the Coast. Dados de cartas
fornecidos pelo Scryfall. O livro *Next Level Magic* não é distribuído neste repositório.
