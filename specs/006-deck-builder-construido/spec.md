# 006 — Deck builder de construído

**Status:** 📝 Especificada

## Objetivo

Atender pedidos como **"Crie um deck anti meta no formato Standard"**: o agente entrega
uma lista de 60 cartas + sideboard, válida, exportável e com a estratégia explicada.

## Histórias de uso

- "Crie um deck anti meta no formato Standard."
- "Monte um deck aggro mono-red barato para Pioneer."
- "Quero jogar com [carta X] no Modern; construa um deck em volta dela."
- "Aqui está minha lista; ajuste-a para o meta atual."

## Requisitos

1. **Comando/skill do Claude Code** que conduz o processo; pedidos em linguagem natural
   no repositório disparam o mesmo fluxo.
2. **Fluxo de construção** (cada etapa usa as specs anteriores):
   1. Entender o pedido: formato, plataforma, BO1 ou BO3, restrições (cores, orçamento,
      cartas obrigatórias, usar a coleção do usuário). Perguntar só o que for
      indispensável. BO1 e BO3 geram decks diferentes: meta próprio (spec 005), sideboard
      de 15 com guia em BO3, e em BO1 lista principal mais robusta sem depender de sideboard.
   2. Ler o meta do formato (spec 005) e a teoria aplicável (spec 002).
   3. Definir o plano de jogo: arquétipo, papel contra os principais decks, condições de vitória.
   4. Selecionar cartas na base (spec 001), somente legais no formato e na plataforma.
   5. Montar a base de mana e conferir com a análise (spec 004).
   6. Montar o sideboard com plano contra os principais arquétipos.
   7. Validar (spec 003) e corrigir até passar.
3. **Modo anti-meta:** identificar os decks mais jogados, suas fraquezas comuns, e
   escolher estratégia e cartas que as explorem — explicando o raciocínio deck a deck.
4. **Entrega:** lista exportável para a plataforma pedida; plano de jogo; papel de cada
   grupo de cartas; guia de sideboard contra os principais decks; pontos fracos do deck;
   data do snapshot de meta usado; custo (wildcards, USD ou tix).
5. O deck é salvo em `decks/<formato>/`.
6. **Honestidade:** o agente deixa claro que a lista é uma proposta fundamentada, não
   testada em jogo, e sugere o que observar ao testá-la.

## Critérios de aceite

- [ ] O pedido "Crie um deck anti meta no formato Standard" produz uma lista que passa no
      validador, com sideboard de 15 e todos os itens de entrega do requisito 4.
- [ ] O mesmo pedido em BO1 e em BO3 usa o snapshot de meta do modo certo e a resposta
      declara para qual modo o deck foi construído.
- [ ] A explicação cita os arquétipos do snapshot e a data dele.
- [ ] Toda carta da lista existe na base e é legal no formato na data da sincronização.
- [ ] O mesmo fluxo funciona para pelo menos Standard, Pioneer, Modern e Pauper.
- [ ] Restrição de orçamento informada pelo usuário é respeitada e demonstrada.

## Fora do escopo

- Simulação de partidas para medir win rate.
- Formatos com comandante (spec 007) e limitado (spec 008).
