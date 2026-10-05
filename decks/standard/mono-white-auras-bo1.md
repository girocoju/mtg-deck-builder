# Mono-White Auras — Standard (BO1)

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-10-05
- **Meta de referência:** Untapped.gg, Standard BO1, capturas enviadas pelo usuário em
  2026-10-05 (`mtg meta show standard --mode bo1`). Fatias: 11/08 a 05/10, Bronze a Mythic,
  2,9 milhões de partidas. Win rates e cartas: 29/09 a 05/10, Bronze a Platinum, 390 mil.
- **Origem da lista:** **reconstruída** a partir da lista mais jogada do arquétipo no
  Untapped (57,9% de vitórias em 13 mil partidas): o resumo mostra 16 criaturas, 24
  encantamentos e 20 terrenos, todos em 4 cópias, e as dez cartas mais usadas do
  arquétipo são exatamente 4 criaturas e 6 encantamentos. Não li a lista carta a carta:
  **confira com o "Copy to MTGA"** antes de jogar.
- **Coringas:** nenhum. O Untapped marca a lista como "All cards owned" na sua conta.

```
Deck
4 Optimistic Scavenger
4 Veteran Survivor
4 Spellbook Vendor
4 Skyward Spider
4 Ethereal Armor
4 Shardmage's Rescue
4 Sheltered by Ghosts
4 Feather of Flight
4 Origin of Spider-Man
4 Seam Rip
20 Plains
```

## Por que este deck

O pedido era vencer no BO1 sem gastar coringas. Pelo roteiro de
`knowledge/preparacao-e-metagame.md`, a primeira pergunta é se vale jogar o melhor deck
ou tentar batê-lo. Aqui os dados respondem:

| Arquétipo | Fatia do campo | Win rate | Partidas | Você tem? |
| --- | --- | --- | --- | --- |
| **Mono-White Auras** | **13,0%** | **57,7%** | 36.000 | Sim |
| 4-Color Reanimator | 5,5% | 58,5% | 13.000 | Não (7 raras) |
| Jeskai Artifacts | 4,1% | 57,6% | 11.000 | Não (7 raras, 1 mítica) |
| Mono-White Lifegain | 6,0% | 54,4% | 17.000 | Sim |
| Mono-Green Landfall | 5,0% | 54,4% | 14.000 | Sim |
| Orzhov Lifegain | 5,7% | 53,7% | 14.000 | Não |
| Azorius Control | 4,3% | 53,7% | 10.000 | Não |
| Boros Superfriends | 3,9% | 50,5% | 9.900 | Sim |

Entre os decks que você já tem, Auras é o de maior win rate por mais de 3 pontos, com a
maior amostra do formato. Os dois decks que rendem o mesmo ou mais custam coringas. E os
decks com remoção em massa, que em teoria punem Auras (Azorius Control e Boros
Superfriends, ambos com Day of Judgment em quase 90% das listas), estão **abaixo** dele:
no campo real, a resposta a Auras não está compensando.

## Como o deck funciona

- **Criaturas de 1 e 2 manas (16)** que crescem sozinhas: Optimistic Scavenger ganha um
  contador a cada encantamento que entra; Veteran Survivor vira 5/4 com hexproof; Skyward
  Spider tem ward {2} e voa quando encantada; Spellbook Vendor cria uma Role por turno.
- **Auras de 1 e 2 manas (16):** Ethereal Armor dá +1/+1 por encantamento e first strike;
  Sheltered by Ghosts dá lifelink e ward {2} e **exila uma permanente do oponente**;
  Feather of Flight dá voo e compra uma carta; Shardmage's Rescue tem flash e dá hexproof
  no turno em que entra — é a resposta à remoção.
- **Origin of Spider-Man** cria um corpo, cresce uma criatura e dá double strike no
  terceiro capítulo: é o turno de finalização.
- **Seam Rip** exila uma permanente de custo 2 ou menos.
- Papel: beatdown em todos os confrontos. Partidas duram 4,6 minutos em média.

## Por que ele bateu o Boros Tokens

A lição `knowledge/licoes/2026-10-05-boros-tokens-bo1-primeiro-teste.md` registra duas
derrotas rápidas para este deck. Lendo as cartas, o motivo é estrutural: ward {2} e o
hexproof de Shardmage's Rescue anulam Torch the Tower e Get Lost; lifelink desfaz o dano
espalhado de Warleader's Call; Sheltered by Ghosts exila o próprio Warleader's Call; e
uma criatura voadora com first strike ignora um chão cheio de fichas 1/1.

## Pontos fracos

- **Remoção em massa** (Day of Judgment): o deck põe várias cartas em uma criatura.
- **Efeitos de sacrifício:** Bringer of the Last Gift, do 4-Color Reanimator, ignora
  ward e hexproof. É o provável pior confronto, e o Reanimator tem o maior win rate do campo.
- **Remoção barata nos dois primeiros turnos,** antes de a criatura receber ward ou de
  haver mana para Shardmage's Rescue.
- **Mãos sem criatura:** são só 16; uma mão de Auras sem corpo não faz nada.
- **Espelho:** 13% do campo é o mesmo deck; quem joga primeiro tende a levar.

## Ajustes

A lista de 13 mil partidas é o resultado de muita gente afinando o mesmo deck; não tenho
dados que justifiquem mexer nela. Dois pontos para observar:

- **Terrenos:** a fórmula de Karsten dá 21 para esta curva; a lista usa 20, e uma lista
  de jogador Mythic em destaque no Untapped usa 18 com duas mágicas a mais. É coerente
  com a regra de BO1 para aggro de curva baixa. Fique em 20 até ter resultado próprio.
- **Mulligan:** mão sem criatura é mulligan, mesmo custando uma carta: Auras sem corpo
  não fazem nada.

## Conferência (2026-10-05)

- `mtg deck validate --format standard --game arena`: lista válida, 60 cartas.
- `mtg deck analyze`: valor de mana médio 1,5; 20 terrenos para 20,6 recomendados; 20
  fontes brancas desviradas para exigência de 14; chance de 2 a 4 terrenos na mão
  inicial de 72% no sorteio puro e até 87% com a suavização de BO1; nenhum alerta.

## Honestidade

Não é um deck que eu construí: é o melhor deck do campo, que você já tem, identificado
pelos dados. Lista reconstruída, a conferir. O que observar ao jogar: resultado no
espelho, contra Reanimator e contra decks com Day of Judgment, e quantas vezes a mão
inicial veio sem criatura.
