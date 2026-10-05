# Decks

Decks produzidos pelo deck builder, um arquivo por deck em `decks/<formato>/<nome>.md`
(formato = chave do Scryfall: `standard`, `brawl`, `commander`...; para melhor-de-um,
use o sufixo `-bo1` no nome).

Cada arquivo traz a lista em um **bloco de código** — é esse bloco que as ferramentas
leem — seguida da explicação:

````markdown
# Nome do deck

- **Formato:** standard (BO3) · **Plataforma:** Arena · **Data:** AAAA-MM-DD
- **Meta de referência:** fonte e data do snapshot usado

```
Deck
4 Nome da Carta
...

Sideboard
2 Nome da Carta
```

## Plano de jogo
## Papel das cartas
## Guia de sideboard
## Pontos fracos
````

Comandos:

```
.venv\Scripts\mtg deck validate decks\standard\meu-deck.md --format standard
.venv\Scripts\mtg deck export decks\standard\meu-deck.md --to arena
.venv\Scripts\mtg deck cost decks\standard\meu-deck.md
```
