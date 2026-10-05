# Mono-Red Prowess — Standard (BO3), adaptado do BO1

- **Formato:** standard (BO3) · **Plataforma:** Arena, MTGO e papel · **Data:** 2026-10-05
- **Origem:** [mono-red-prowess-bo1.md](mono-red-prowess-bo1.md), lista de BO1.
- **Meta de referência:** MTGGoldfish, coletado em 2026-10-04 (torneios de MTGO e papel, BO3).

```
Deck
4 Pompous Battlemage
4 Slickshot Show-Off
4 Emberheart Challenger
4 Stingcaster Mage
4 Emeritus of Conflict
4 Boltwave
4 Burst Lightning
4 Shock
4 Lightning Strike
2 Sure Strike
20 Mountain
2 Soulstone Sanctuary

Sideboard
4 Magebane Lizard
3 Scorching Shot
2 Abrade
2 Pyroclasm
2 Soul-Guide Lantern
2 Chandra, Torch of Defiance
```

## O que mudou

| Saiu | Entrou | Por quê |
| --- | --- | --- |
| — | — | **Lista principal mantida.** A versão BO1 já usava 22 terrenos (não havia corte a repor) e não tinha cartas escolhidas só por serem flexíveis em BO1 |
| 3 Twin Bolt (sideboard) | 1 Magebane Lizard, 2 Soul-Guide Lantern | Twin Bolt era genérica. O campo BO3 tem 37% de decks de muitas mágicas (Izzet Spellementals, Dimir Midrange, 4c Control, Azorius Control, Dimir Excruciator) e 34% que usam o cemitério |
| 1 Abrade (sideboard) | 1 Scorching Shot | Mais alvos de resistência 5 no campo (Sunderflock e Eddymurk Crab são 5/5; dragões do Boros Dragons) do que artefatos |

## Guia de sideboard

| Contra (fatia do meta) | Entram | Saem |
| --- | --- | --- |
| Izzet Spellementals (14,9%) | 4 Magebane Lizard, 2 Soul-Guide Lantern, 3 Scorching Shot | 4 Shock, 2 Sure Strike, 3 Burst Lightning |
| Mono-Green Landfall (11,1%) | 3 Scorching Shot, 2 Soul-Guide Lantern | 4 Shock, 1 Sure Strike |
| Dimir Midrange (8,2%) | 4 Magebane Lizard, 2 Chandra, Torch of Defiance | 4 Boltwave, 2 Sure Strike |
| Jund Sacrifice (8,2%) | 2 Pyroclasm, 2 Soul-Guide Lantern | 2 Sure Strike, 2 Boltwave |
| Boros Dragons (6,8%) | 3 Scorching Shot | 2 Sure Strike, 1 Shock |
| 4c Control / Azorius Control (9,7%) | 4 Magebane Lizard, 2 Chandra, Torch of Defiance | 4 Shock, 2 Sure Strike |
| Boros Dwarves (4,6%) | 2 Abrade, 2 Pyroclasm | 4 Boltwave |
| Lifegain (3,1%) | 2 Pyroclasm, 3 Scorching Shot | 4 Boltwave, 1 Sure Strike |

## O que o deck ganha e perde

- **Ganha:** respostas dedicadas nos jogos 2 e 3, principalmente contra os decks de
  mágicas (Magebane Lizard pune cada mágica não-criatura) e de cemitério.
- **Perde:** o efeito surpresa do BO1 e a vantagem de enfrentar listas sem resposta: nos
  jogos 2 e 3 os oponentes trazem remoção em massa barata e ganho de vida.
- **Confrontos que seguem difíceis:** Lifegain e os controles com Day of Judgment.

## Conferência (2026-10-05)

- `mtg deck validate --format standard --game arena`: lista válida, 60 + 15.
- `mtg deck analyze`: igual à versão BO1 (22 terrenos para 21,5 recomendados; sem alertas).
- `mtg deck diff` contra a lista BO1: principal idêntico; no sideboard saem 3 Twin Bolt e
  1 Abrade, entram 1 Magebane Lizard, 2 Soul-Guide Lantern e 1 Scorching Shot.

## Honestidade

Adaptação não testada. As trocas do guia são raciocínio sobre as listas de referência do
snapshot, uma por arquétipo; variações dessas listas podem pedir outros planos.
