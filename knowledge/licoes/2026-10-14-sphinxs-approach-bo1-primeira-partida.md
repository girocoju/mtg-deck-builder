# Dimir Sphinx's Approach em BO1: primeira partida perdida para Mono-Green Landfall com pouca remoção na mão

- **Data:** 2026-10-14
- **Origem:** resultado de partida (relato do usuário) e simulação de 100 mãos iniciais
- **Contexto:** Standard, BO1, Arena; `decks/standard/dimir-sphinxs-approach-bo1.md`
  (versão com 12 Approach, 7 cartas de custo 6 ou mais, 5 remoções)
- **Situação:** ativa (hipótese, 1 partida)

## O que aconteceu

Mão inicial de 7 com um terreno (Watery Grave, Paradox Shaper, três Approach, dois Break
Under Pressure), jogando primeiro: mulligan recomendado. A partida foi perdida para
Mono-Green Landfall (5,0% do meta BO1 no snapshot de 2026-10-05) com duas criaturas 7/8 na
mesa do oponente. O usuário relatou que moeu mais de 15 cartas até os turnos 5 e 6, mas
poucas Approach entre elas, e que faltou remoção na mão.

A simulação de 100 mãos feita antes da partida já mostrava: remoção na mão em 49% das
mãos, carta de custo 6 ou mais em 64%, e 27% das mãos com dois terrenos ou menos mais uma
carta cara parada.

## O que aprendemos

- Evidência (1 partida): contra um deck de criaturas grandes, duas remoções de alvo único
  (Break Under Pressure) não bastam; o deck precisa de mais respostas baratas ou de uma
  remoção em massa.
- Sobre a moagem: 12 Approach em 60 são 20% do deck; em 15 cartas moídas o esperado são 3,
  com variância alta. Moer muito não garante a busca; Picklock Prankster, que devolve uma
  Approach moída à mão, é a peça que converte moagem em Approach utilizável.
- Hipótese: a troca de 1 Curator of Destinies e 1 Sphinx of the Final Word por 1 Picklock
  Prankster e 1 Bitter Triumph (aplicada nesta data) corrige parte do problema; se as
  criaturas grandes continuarem passando, o próximo passo é 1 a 2 Singularity Rupture.

## Quando se aplica

Decks de combo ou controle com muitas cartas de 6+ manas em BO1: simular mãos antes de
jogar e manter a contagem de cartas caras em 5 ou menos; contar a remoção na mão como
métrica de construção (meta: acima de 60% das mãos com uma).
