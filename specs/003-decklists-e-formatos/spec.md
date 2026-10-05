# 003 — Decklists e formatos

**Status:** 📝 Especificada

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
4. **Exportação** para Arena, MTGO e texto simples, escolhendo impressões que existem na
   plataforma de destino.
5. **Custo** opcional da lista: preço em USD/EUR (papel), tix (MTGO) e contagem de
   wildcards por raridade (Arena).
6. Listas salvas em `decks/<formato>/<nome>.md`, com a lista e a explicação.
7. **Coleção do usuário (Arena):**
   - O Arena não tem exportação oficial da coleção. A importação é feita a partir do
     arquivo CSV/texto exportado por um tracker (ex.: Untapped.gg, MTGA Assistant,
     AetherHub), que o usuário salva em `data/colecao/`. Fica fora do git.
   - O importador aceita os formatos dos trackers mais comuns e casa as cartas com a base
     por `arena_id` ou por nome + coleção; o que não casar é listado, não descartado.
   - Também é possível informar os wildcards disponíveis por raridade.
   - Com a coleção carregada, a validação informa, por lista: cartas que o usuário já
     tem, cartas que faltam e wildcards necessários por raridade.
   - Os deck builders (specs 006–008) podem receber "priorize minha coleção" ou "use só
     o que eu tenho" como restrição.

## Critérios de aceite

- [ ] Uma lista válida de cada família (60 cartas, singleton com comandante, limitado)
      passa na validação; variações inválidas de cada regra são apontadas individualmente.
- [ ] Uma lista exportada para o Arena é reimportada pelo leitor sem diferença.
- [ ] Nome com erro de digitação gera sugestão em vez de falha genérica.
- [ ] Um deck de Brawl com carta fora da identidade do comandante é rejeitado.

- [ ] Um arquivo de coleção exportado de um tracker é importado e, para uma lista de
      Standard, o relatório mostra cartas faltantes e wildcards por raridade.

## Fora do escopo

- Ler a coleção direto do cliente do Arena (memória ou logs do jogo).
- Coleção de papel e de MTGO (pode entrar depois pelo mesmo importador).
- Formatos não cobertos pelas legalidades do Scryfall.

## Questões em aberto

- Qual tracker o usuário usa (ou prefere instalar)? O primeiro formato de arquivo
  suportado será o dele.
