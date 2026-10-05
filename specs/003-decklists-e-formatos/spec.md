# 003 — Decklists e formatos

**Status:** ✅ Concluída

## Objetivo

Ler, validar e exportar decklists em qualquer formato do jogo, para que toda lista que o
deck builder entrega seja comprovadamente legal e importável no Arena, no MTGO e utilizável
no papel.

## Histórias de uso

- Como agente, quero validar a lista que montei antes de mostrá-la ao usuário.
- Como usuário, quero colar uma lista exportada do Arena e saber se é legal em Pioneer.
- Como usuário, quero copiar a lista final direto para o importador do Arena ou do MTGO.

## Requisitos

1. **Leitura** de listas em texto: formato do Arena (`4 Nome (SET) 123`), formato simples
   (`4 Nome`), seções de sideboard, comandante e companion.
2. **Regras por formato** descritas como dados, não espalhadas no código:
   - Construído 60 cartas (Standard, Pioneer, Modern, Legacy, Vintage, Pauper, Historic,
     Timeless, Alchemy...): mínimo de 60, sideboard de até 15, até 4 cópias.
   - Singleton com comandante: Commander (100), Brawl (100 no Arena), Standard Brawl (60),
     Pauper Commander, Oathbreaker — cópia única, identidade de cor, comandante válido.
   - Limitado (draft/selado): mínimo de 40, sem limite de cópias.
   - Exceções: terrenos básicos, cartas "qualquer número de cópias", restritas em Vintage,
     melhor-de-um no Arena (sideboard de 7).
3. **Validação** que aponta cada problema: carta inexistente (com sugestão de nome),
   carta ilegal/banida, excesso de cópias, tamanho errado, fora da identidade de cor,
   comandante inválido, carta indisponível na plataforma escolhida.
4. **Exportação** para Arena, MTGO e texto simples, só com quantidade e nome (sem código
   de coleção, que varia entre plataformas). Se a carta existe na plataforma de destino
   é conferido pela validação (requisito 3).
5. **Custo** opcional da lista: preço em USD/EUR (papel), tix (MTGO) e contagem de
   wildcards por raridade (Arena).
6. Listas salvas em `decks/<formato>/<nome>.md`, com a lista e a explicação.

## Critérios de aceite

- [x] Uma lista válida de cada família (60 cartas, singleton com comandante, limitado)
      passa na validação; variações inválidas de cada regra são apontadas individualmente.
- [x] Uma lista exportada para o Arena é reimportada pelo leitor sem diferença.
- [x] Nome com erro de digitação gera sugestão em vez de falha genérica.
- [x] Um deck de Brawl com carta fora da identidade do comandante é rejeitado.


## Fora do escopo

- **Coleção do usuário** (importar a coleção do Arena para priorizar cartas que ele já
  tem). Adiada por decisão do usuário em 2026-10-04: o Arena não exporta a coleção e o
  tracker que ele usa (Untapped.gg) só exporta no plano pago. Retomar como spec própria
  se surgir um caminho gratuito.
- Formatos não cobertos pelas legalidades do Scryfall.
