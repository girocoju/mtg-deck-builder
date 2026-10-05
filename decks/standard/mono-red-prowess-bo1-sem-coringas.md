# Mono-Red — Standard (BO1), versão sem gastar coringas

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-10-05
- **Origem:** [mono-red-prowess-bo1.md](mono-red-prowess-bo1.md). O usuário não tem
  4 Stingcaster Mage, 4 Emeritus of Conflict e 2 das 4 Pompous Battlemage, e não quer
  gastar coringas.
- **Meta de referência:** Untapped.gg, Standard BO1, de 29/09 a 05/10/2026, ranks Bronze a
  Platinum, 390 mil partidas — recorte parcial (7 das 14 listas com mais de mil partidas,
  lidas de uma captura de tela enviada pelo usuário).

```
Deck
4 Slickshot Show-Off
4 Emberheart Challenger
2 Pompous Battlemage
4 Stadium Headliner
4 Boltwave
4 Burst Lightning
4 Shock
4 Lightning Strike
4 Torch the Tower
1 Abrade
2 Sure Strike
2 Chandra, Torch of Defiance
19 Mountain
2 Soulstone Sanctuary
```

## Restrição: só cartas que você já mostrou ter

Não tenho a sua coleção. Usei apenas cartas que aparecem nos seus dois decks montados no
Arena: o restante do Prowess (principal e reserva) e o Boros Tokens que você testou.
**Confirme que as cópias são suas**, principalmente as 4 Stadium Headliner e as 4 Torch
the Tower (vieram do Boros Tokens).

## O que mudou

| Saiu | Entrou | Por quê |
| --- | --- | --- |
| 4 Stingcaster Mage | 4 Stadium Headliner | Você não tem a carta. Headliner é a única criatura vermelha barata que você mostrou ter: custa 1, ataca com uma ficha a cada turno e, sacrificada, vira remoção |
| 4 Emeritus of Conflict | 4 Torch the Tower | Você não tem a carta. O campo BO1 que você mandou é liderado por decks brancos de criaturas (Auras e Lifegain); Torch the Tower custa 1 e **exila**, respondendo à criatura antes que as Auras a tirem do alcance |
| 2 Pompous Battlemage | 2 Chandra, Torch of Defiance | Você tem só 2 das 4. Chandra estava na sua reserva: é a fonte de vantagem de cartas e de dano repetido que o deck perde com menos criaturas |
| 1 Mountain | 1 Abrade | Curva baixa em BO1 permite 1 terreno a menos (suavização de mão). Abrade estava na reserva e serve contra criaturas e contra Jeskai Artifacts |
| Reserva de 15 | Sem reserva | Em BO1 a reserva não é usada; ela veio junto porque a lista original foi escrita com uma |

## O que a otimização consegue e o que não consegue

- **Consegue:** um deck completo, válido e coerente sem nenhum coringa; curva e base de
  mana conferidas; remoção ajustada ao campo BO1 que você mandou.
- **Não consegue:** manter a força do original. Saem 10 das 20 criaturas, justamente as
  que davam nome ao deck (prowess). Com 14 criaturas e 21 mágicas de dano e remoção, o
  deck passa de **prowess** para **burn com criaturas**: menos explosivo, mais dependente
  de queimar o oponente.
- **Posição no campo:** queimar o oponente é ruim contra ganho de vida, e o segundo deck
  mais forte do recorte é Mono-White Lifegain (58,4%). O Untapped lista um Mono-Red Burn
  com 56,9% de vitórias, mas a lista dele é outra e não a tenho.

A lição `knowledge/licoes/2026-10-05-boros-tokens-bo1-primeiro-teste.md` aponta na mesma
direção: no seu teste do Boros Tokens, duas das três derrotas foram para decks brancos.

## Alternativa que não gasta coringas e é mais forte

Na captura do Untapped, três listas aparecem como **"All cards owned"** (você já tem todas
as cartas): Mono-White Auras (57,9% em 13 mil partidas — a mais jogada e testada do
recorte), Mono-White Lifegain (58,4%) e Mono-Black Skeletons (56,7%). Pelo critério "não
gastar coringas e vencer mais", qualquer uma delas é melhor escolha que este mono-red
remendado. Se você colar uma delas ("Copy to MTGA"), eu analiso e ajusto.

## Conferência (2026-10-05)

- `mtg deck validate --format standard --game arena`: lista válida, 60 cartas.
- `mtg deck analyze`: 21 terrenos para 22,0 recomendados (um a menos de propósito, pela
  regra de BO1 para aggro de curva baixa); valor de mana médio 1,54; 19 fontes vermelhas
  desviradas para exigência de 16 (Chandra, {2}{R}{R}); nenhum alerta.
- `mtg deck diff` contra a lista original: ver a tabela acima.

## Honestidade

Não testado. A escolha das substitutas foi limitada ao que vi nos seus decks, não ao que
seria melhor no formato; com a coleção completa haveria outras opções.
