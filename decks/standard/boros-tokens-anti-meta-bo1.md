# Boros Tokens — Standard (BO1), adaptado do BO3

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-10-05
- **Origem:** [boros-tokens-anti-meta.md](boros-tokens-anti-meta.md), construído para BO3.
- **Meta de referência:** **não há snapshot BO1.** A adaptação foi feita por princípios
  (robustez e flexibilidade), não contra um campo medido. O meta BO3 do MTGGoldfish de
  2026-10-04 serviu só como indício do que existe no formato.

```
Deck
4 Belladonna Took
4 Voice of Victory
4 Stadium Headliner
4 Frontline Rush
4 The Last Ronin's Technique
4 Song of Totentanz
4 Warleader's Call
4 Political Triumph
4 Torch the Tower
2 Get Lost
1 Seam Rip
4 Sacred Foundry
4 Inspiring Vantage
4 Sunbillow Verge
2 Dalkovan Encampment
2 Fountainport
4 Mountain
1 Plains
```

## O que mudou

| Saiu | Entrou | Por quê |
| --- | --- | --- |
| 2 Rest in Peace | 2 Get Lost | Rest in Peace é ódio estreito: forte contra os decks de cemitério, morta contra o resto. Em BO3 dá para tirá-la no jogo 2; em BO1 uma carta morta fica morta. Get Lost responde a criatura, encantamento ou planeswalker de qualquer deck |
| 1 Mountain | 1 Seam Rip | Deck agressivo de curva baixa (valor de mana médio 1,9; a fórmula de Karsten dá cerca de 21 terrenos). Em BO1 a suavização de mão reduz as mãos de 0 ou 1 terreno, e a regra do projeto permite 1 ou 2 terrenos a menos para aggro. Seam Rip é interação de uma mana contra o início rápido dos decks agressivos, que tendem a ser mais comuns em BO1 |
| Sideboard de 15 | Sem sideboard | Em BO1 não há troca entre jogos, e o deck não tem efeitos que buscam cartas de fora do jogo |

## O que o deck ganha e perde

- **Ganha:** nenhuma carta morta no jogo 1; mais uma resposta barata; mãos iniciais mais
  regulares (com 21 terrenos, a chance de 2 a 4 terrenos na mão inicial sobe de 74% no
  sorteio puro para até 88% com a suavização de BO1).
- **Perde:** as respostas dedicadas do sideboard. Pioram em relação ao BO3:
  - **Izzet Spellementals** — sem Rest in Peace nem Bilbo's Gambit, o deck depende só de
    velocidade e de Voice of Victory contra Sunderflock;
  - **controles com remoção em massa** — sem Bilbo's Gambit e Sunspine Lynx;
  - **Lifegain** — sem Sunspine Lynx.
- **Não muda:** a tese (enxame contra remoção pontual) e a base de mana de duas cores.

## Dependência do sideboard

O plano principal não depende do sideboard: o deck não é transformacional e continua
proativo em BO1. O que se perde são respostas a cartas específicas, listadas acima.

## Conferência (2026-10-05)

- `mtg deck validate --format standard --game arena`: lista válida, 60 cartas.
- `mtg deck analyze`: 21 terrenos para 20,9 recomendados; 15 fontes brancas e 16
  vermelhas para exigência de 14 em cada cor; nenhum alerta.
- `mtg deck diff` contra a lista BO3: saem 2 Rest in Peace e 1 Mountain do principal,
  entram 2 Get Lost e 1 Seam Rip; o sideboard inteiro sai.

## Honestidade

Adaptação teórica, não testada. Sem meta BO1, a suposição de que há mais aggro na
ranqueada BO1 é conhecimento geral, não dado. Quando houver snapshot BO1 (importação do
Untapped), refazer: as duas vagas de Get Lost e a de Seam Rip são as primeiras a rever.
Ao voltar para BO3, repor o 22º terreno.
