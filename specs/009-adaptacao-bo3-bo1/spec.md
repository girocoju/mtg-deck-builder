# 009 — Adaptação de deck entre BO3 e BO1

**Status:** 🚧 Em andamento — skill pronta e exercitada nos dois sentidos; faltam os critérios marcados abaixo

## Objetivo

Atender pedidos como **"Adapte o deck em questão BO3 para BO1"**: receber uma lista
pensada para melhor-de-três (60 + sideboard de 15) e devolver a versão para
melhor-de-um, explicando cada troca. O caminho inverso (BO1 → BO3) também é atendido.

## Histórias de uso

- "Adapte o deck em questão BO3 para BO1." (deck da conversa, arquivo em `decks/` ou
  lista colada)
- "Peguei esta lista de um torneio; quero jogar na ranqueada BO1 do Arena."
- "Subi de rank com este deck em BO1; monte o sideboard e o guia para jogar BO3."

## Por que não é só "tirar o sideboard"

Em BO3 a lista principal pode ser especializada, porque os jogos 2 e 3 são corrigidos
pelo sideboard. Em BO1 não há jogos pós-sideboard, o campo é outro (mais aggro e decks
lineares, menos decks que dependem de sideboard) e, no Arena, a mão inicial passa por um
algoritmo de suavização. O sideboard em BO1 também tem até 15 cartas, mas só é usado
por efeitos que buscam cartas de fora do jogo.

## Requisitos

1. **Comando/skill** que aceita o deck de origem (da conversa, de arquivo ou colado), o
   formato e a direção da adaptação (padrão: BO3 → BO1).
2. **Diagnóstico da lista de origem:** plano de jogo, papel de cada grupo de cartas, e
   para que matchups serve cada carta do sideboard.
3. **BO3 → BO1:**
   - usar o snapshot de meta **BO1** do formato (spec 005) para decidir contra o que a
     lista principal precisa estar preparada;
   - promover para a lista principal as cartas de sideboard que valem contra a maior
     fatia do campo BO1, e cortar as cartas principais mais estreitas ou mais fracas
     nesse campo;
   - preferir respostas flexíveis a respostas estreitas, já que não há como trocá-las;
   - reavaliar cartas cujo valor depende do sideboard (ex.: efeitos que buscam cartas de
     fora do jogo) e montar o sideboard (até 15 cartas) em função delas, se o deck as usa;
   - reconferir curva e base de mana após as trocas (spec 004).
4. **BO1 → BO3:** usar o snapshot de meta **BO3**; decidir o que sai da lista principal
   para o sideboard; construir o sideboard de 15 e o guia de trocas por matchup.
5. **Entrega:** lista adaptada e validada (spec 003), exportável; tabela "saiu / entrou /
   por quê"; o que o deck ganha e o que perde com a adaptação; matchups que pioram sem
   sideboard; data e modo do snapshot de meta usado.
6. **Honestidade:** se o deck depende estruturalmente do sideboard (ex.: plano
   transformacional) ou é mal posicionado no campo BO1, o agente diz isso e sugere
   alternativa, em vez de entregar uma adaptação ruim sem aviso.
7. **Sem dados de meta do modo de destino:** a adaptação é feita por princípios
   (robustez, flexibilidade), declarada como teórica.

## Critérios de aceite

- [ ] Dada uma lista BO3 de Standard com sideboard, o resultado BO1 passa no validador,
      traz a tabela de trocas justificadas e cita o snapshot de meta BO1 usado.
      *(Parcial: validado e com a tabela, mas sem snapshot BO1 — feito em modo teórico.)*
- [x] Nenhuma carta nova entra sem ter sido consultada na base e ser legal no formato.
- [x] A base de mana da lista adaptada é reconferida e o relatório mostra o antes e o depois.
- [x] O caminho BO1 → BO3 produz sideboard de 15 com guia por matchup.
- [ ] Para um deck que depende do sideboard, a resposta contém o aviso do requisito 6.

## Dependências

Specs 002 (teoria: `knowledge/sideboard.md`, `papel-no-jogo.md`), 003 (validação),
004 (análise), 005 (meta separado por modo) e 006 (fluxo de construção, do qual esta
spec reaproveita as etapas).

## Fora do escopo

- Conversão entre formatos diferentes (ex.: Standard → Pioneer).
- Commander/Brawl, que não têm sideboard.

## Questões em aberto

- Nenhuma no momento. A regra de terrenos em BO1 está em `knowledge/base-de-mana.md`
  (seção 1.4): aggro de curva baixa pode cortar 1 a 2 terrenos; os demais não cortam;
  ao voltar para BO3, repor.
