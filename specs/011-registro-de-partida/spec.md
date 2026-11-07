# 011 — Registro de partida e conselhos ao vivo

**Status:** 📝 Especificada

## Objetivo

Fazer o Oráculo (spec 010) enxergar a partida inteira, não só vida e turnos: mão, campo
de batalha, cemitério, exílio e pilha dos dois lados, fases e passos, ataques, bloqueios
e dano, cartas compradas, jogadas e resolvidas. Com isso: (1) mostrar o estado do jogo na
janela, (2) gravar cada partida em arquivo para a análise posterior e as lições
(`knowledge/licoes/`), e (3) dar conselhos ao vivo que possam ser calculados com certeza
(letal disponível, mana aberta do oponente, cartas vistas do deck dele).

Pedido do usuário em 2026-11-07, depois do primeiro teste ao vivo: "o Oráculo pegou
apenas os pontos de vida"; "registro de mão e cemitério também é importante"; "bem como
exílio".

## O que o log do Arena contém (conferido na partida de 2026-11-07)

Cada partida gera centenas de `GameStateMessage` (uma `Full` no início e `Diff` a cada
mudança) com:

- **zonas** com identificador, tipo (Hand, Library, Graveyard, Exile, Battlefield, Stack,
  Limbo, Revealed, Command, Sideboard) e dono, e a lista de instâncias em cada uma;
- **objetos** (cartas, fichas, habilidades): instância, `grpId` (a carta, resolvida pela
  base do Arena), zona, dono, controlador, tipos, poder e resistência, virada ou não,
  dano marcado, estado de ataque e de bloqueio, enjoo de invocação;
- **anotações**: transferência de zona com categoria (CastSpell, Resolve, Draw, PlayLand,
  Sacrifice, SBA_Damage...), dano causado, vida modificada, turno novo, fase ou passo,
  virar e desvirar, marcadores, fichas criadas, mudança de identificador de instância;
- **turnInfo** (turno, fase, passo, jogador ativo, quem decide) e **players** (vida).

A mão do oponente chega só como contagem (as cartas dele ficam ocultas até serem
jogadas ou reveladas); a nossa chega completa. A biblioteca chega como contagem.

## Histórias de uso

- "Durante a partida, quero ver minha mão, os dois campos, cemitérios e exílio na janela,
  com o que aconteceu nos últimos lances."
- "Acabou a partida: guarde o registro para eu te pedir uma análise depois."
- "Me avise quando eu tiver letal na mesa" (poder das criaturas que podem atacar contra
  a vida do oponente).
- "Mostre o que o oponente já jogou e quanta mana ele tem aberta."
- (Fase posterior, questão em aberto) "Me diga a melhor jogada agora."

## Requisitos

1. **Rastreador de estado** (`arena_game.py`): aplica cada `GameStateMessage` e mantém
   zonas, objetos, vida, turno, fase e passo; traduz anotações em eventos legíveis em
   PT-BR ("você conjura Ghalta the Unstoppable", "oponente joga Forest", "Ghalta ataca",
   "15 de dano em Mister_Jedi", "vida 20 → 4"); segue a mudança de identificador de
   instância para não perder a carta quando ela troca de zona.
2. **Visão da partida na janela do Oráculo:** turno, fase, jogador ativo, vida; sua mão;
   os dois campos com poder, resistência, virada ou não, enjoo; cemitérios; exílio;
   pilha; contagem da mão e da biblioteca do oponente; mana aberta de cada lado
   (terrenos desvirados); últimos eventos. Deve caber na janela (cerca de 40 linhas).
3. **Registro da partida** em `data/games/<data>-<evento>-<oponente>.json` (eventos com
   turno e fase, estado final, deck enviado, resultado) e um resumo em Markdown
   (`.md`) legível pelo agente para a análise e para as lições.
4. **Conselhos calculáveis**, mostrados na janela quando valem: letal disponível (soma do
   poder das criaturas que podem atacar, contando ímpeto e enjoo, contra a vida do
   oponente, com o aviso de que bloqueadores não são descontados); mana aberta do
   oponente no seu turno (sinal de resposta); cartas do oponente já vistas, agrupadas.
   Nada que dependa de julgamento é apresentado como certeza.
5. **`mtg arena watch`** passa a mostrar os eventos do rastreador; `--file` reproduz uma
   partida gravada e grava o registro.
6. **Skill:** o agente lê o registro de uma partida quando o usuário pede análise ("o que
   fiz de errado?") e registra lições pelo processo de `knowledge/COMO-ADICIONAR.md`.
7. **Histórico e win rate** (pedido de 2026-11-07): o Arena só guarda as duas últimas
   sessões em disco, então o projeto acumula cada partida vista em `data/matches.jsonl`
   (id, hora, evento, deck, oponente, resultado, turnos) e `mtg arena history` resume
   vitórias e derrotas por deck, o rank e o saldo da temporada construída que o cliente
   informa no login, e o cofre (ouro, gemas, curingas, fichas). Partidas anteriores à
   instalação não existem na máquina: ficam só em serviços como o Untapped, que o usuário
   já usa.
8. **Coleção aproximada** (`data/collection.json`, `mtg arena collection`): por `grpId`,
   com a quantidade máxima vista em cada fonte: as listas dos decks salvos, que vêm na
   resposta de abertura do cliente (155 decks, 2.953 cartas distintas em 2026-11-07), e
   os boosters abertos com o Oráculo ligado (soma). É aproximação por baixo e é dita
   como tal; `--find` responde quantas cópias de uma carta são conhecidas, para os
   pedidos "sem gastar coringas".

## Critérios de aceite

- [ ] Reproduzindo o log da partida de 2026-11-07 (Ladder, vitória no turno 10),
      o rastreador mostra a mão do usuário em cada turno, os terrenos e criaturas nos dois
      campos, os cemitérios, o exílio, os ataques e os 15 de dano do turno final, sem erro
      de instância (teste com trecho anonimizado em `tests/fixtures/`).
- [ ] O registro em JSON e o resumo em Markdown são gravados ao fim da partida e o
      agente consegue descrever a partida só a partir deles.
- [ ] O aviso de letal aparece no turno em que o usuário tinha letal e não aparece nos
      outros (verificado nessa mesma partida).
- [ ] A janela do Oráculo mostra a visão da partida em tempo real em uma ranqueada,
      cabendo na tela (registro em `tasks.md` com a data).
- [ ] Testes sem rede com mensagens sintéticas para cada tipo de anotação usado.

## Dependências

Spec 010 (leitor de log, base de cartas do Arena, Oráculo), 001 (base de cartas).

## Fora do escopo

- Ver a mão do oponente (o log não traz).
- Decidir jogadas por julgamento (ver questão em aberto).
- Replays gráficos; estatísticas agregadas de muitas partidas (pode virar spec depois).

## Questões em aberto

- **Conselho por julgamento ao vivo.** Dá para mandar o estado da partida a um modelo (API
  do Claude) e mostrar a resposta na janela, mas custa chamadas por lance, tem latência de
  segundos e exige uma chave de API na máquina; a constituição deixa o julgamento com o
  agente, que hoje não está na partida. Proposta: primeiro os conselhos calculáveis do
  requisito 4 e o registro para análise posterior; decidir sobre a API depois de ver o
  valor desses dois.
- Semântica exata dos códigos numéricos de `DamageDealt.type` e `UserActionTaken.actionType`
  (não documentados); tratar como opacos até haver evidência.
- **Coleção.** O cliente não grava a coleção no log, nem com a aba Coleção aberta
  (testado em 2026-11-07). Requisito 8 abaixo: aproximação por baixo pelos decks salvos
  e por importação de CSV. **Boosters também não:** o usuário abriu três boosters em
  2026-11-07 com o log acompanhado e o cliente gravou só a troca de tela
  (`Client.SceneChange` para `BoosterChamber`) e linhas "Index Reveal complete", sem
  nenhuma carta nem atualização do cofre. O que entra na conta vindo de boosters, hoje,
  é só o baú e os curingas na próxima abertura do Arena (`StartHook`). Fonte restante
  de ganhos de cartas no log: a resposta final do draft em modo bot (`DTO_InventoryInfo`,
  segundo o guia do log de 2026), a conferir no primeiro draft.
