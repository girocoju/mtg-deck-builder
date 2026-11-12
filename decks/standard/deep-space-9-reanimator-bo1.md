# Deep Space 9 Reanimator (ajuste v2)

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-11-12
- **Meta de referência:** Untapped.gg, Standard BO1, coletado em 2026-10-05 (38 dias, anterior a TRK: indício, não medida)

```
Deck
4 Deep Space 9
4 Tune Up
2 Daretti, Rocketeer Engineer
4 Fear of Missing Out
4 Melded Moxite
4 Hit It!
2 Collector's Vault
4 Gene Pollinator
4 Sentinel of the Nameless City
4 Chainsaw
2 Craterclaw Colossus
4 Stomping Ground
4 Sacred Foundry
4 Thornspire Verge
4 Hushwood Verge
4 Starting Town
1 Forest
1 Mountain
```

Validação: `mtg deck validate --format standard --game arena` acusa só Deep Space 9 e
Hit It! como "não legal em standard". A base (Scryfall de 2026-11-08) ainda marca TRK como
`future`; o Arena aceitou as duas na Ladder em 2026-11-12. As outras 52 cartas passam.

## O que mudou em relação à lista jogada em 2026-11-12 (1–3)

| Sai | Entra | Por quê |
| --- | --- | --- |
| 2 Craftwork Crusher | 2 Chainsaw | custo 7 que nunca foi conjurado; na mão é carta morta |
| 2 Collector's Vault | 2 Chainsaw | o motor de descarte mais lento (2 + 2 de mana); a lista ainda tem 8 descartes e Hit It! |
| 1 Craterclaw Colossus | 1 Tune Up | de 5 para 6 cartas que devolvem Deep Space 9 (65,1% → 72,1% de ter uma até o turno 4, na compra) |

## Plano de jogo

Pôr Deep Space 9 no cemitério (Fear of Missing Out, Melded Moxite, Collector's Vault,
Hit It!) e devolvê-lo com Tune Up no turno 4, ou no 3 com Gene Pollinator; Daretti faz o
mesmo no turno 5 sacrificando um Treasure, um Map ou o Moxite. Cada manutenção exila
quatro cartas e põe as permanentes em campo; Hit It! dá ímpeto ao que chegar.

## Papel das cartas

- **Chainsaw** é a única interação: 3 de dano ao entrar, é artefato (conta para Craterclaw
  Colossus, serve de sacrifício para Daretti) e é permanente, então Deep Space 9 a põe em
  jogo com o gatilho.
- **Sentinel of the Nameless City** é o bloqueador que segura o chão até o turno 4.

## Pontos fracos

- Anulação e devolução à mão (Countersculpt, Into the Flood Maw, Aetherize): o deck não
  tem como forçar Tune Up.
- Exílio de cemitério incidental (Veteran Survivor) e exílio de artefato barato
  (Seam Rip, Sheltered by Ghosts) atingem os motores de descarte.
- Proposta não testada: 4 partidas com a lista anterior; ver
  `knowledge/licoes/2026-11-12-deep-space-9-reanimator-bo1-primeiro-teste.md`.
