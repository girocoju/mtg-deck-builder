# Sideboard em BO1 no Arena é de até 15 cartas

- **Data:** 2026-10-04
- **Origem:** feedback do usuário (correção de regra)
- **Contexto:** MTG Arena, melhor-de-um, formatos de 60 cartas
- **Situação:** ativa

## O que aconteceu

O validador foi escrito com a regra antiga, em que o sideboard de melhor-de-um no Arena
era limitado a 7 cartas, e a spec 009 repetia o mesmo número. O usuário, que joga no
Arena, corrigiu: o limite em BO1 passou a ser de até 15, igual ao de BO3.

## O que aprendemos

- O limite de sideboard é 15 em BO1 e em BO3. O que continua diferente em BO1 é o uso:
  não há troca entre jogos, então o sideboard só serve a efeitos que buscam cartas de
  fora do jogo.
- A regra veio da memória do modelo, não de uma fonte conferida. Regras de cliente (Arena)
  mudam e não estão na base de cartas: tratá-las como dado datado e conferir com o
  usuário ou com fonte oficial antes de codificá-las.

## Quando se aplica

Ao validar ou montar qualquer lista BO1 para o Arena, e na adaptação entre BO3 e BO1
(spec 009). Não generalizar para MTGO ou papel, que não têm fila BO1 com regra própria.
