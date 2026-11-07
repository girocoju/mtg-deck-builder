# 011 — Plano

## Decisões

- **Rastreador em `arena_game.py` (`GameTracker`)**, alimentado pelas `GameStateMessage`
  que `arena_match.classify_match` passa a entregar inteiras (`messages`). Ordem de
  aplicação de cada mensagem: zonas (lista de instâncias; chave ausente = zona vazia),
  `ObjectIdChanged` (a instância antiga vira a nova, para a carta não se perder ao trocar
  de zona), objetos (substituição completa: campo ausente = valor padrão, ex.: desvirada),
  instâncias apagadas, `turnInfo`, `players`, `gameInfo`; só então as anotações viram
  eventos. Tudo que não é reconhecido fica guardado no objeto e não gera texto.
- **Eventos em PT-BR** a partir das anotações vistas no log: ZoneTransfer por categoria
  (CastSpell "conjura", PlayLand "joga", Draw "compra", Resolve "entra em campo" ou
  "resolve", Sacrifice, SBA_* "morre", Destroy, Countered, Exile; categoria desconhecida:
  "X: zona → zona (categoria)"), DamageDealt, ModifiedLife, CounterAdded, TokenCreated,
  ataque pelos objetos com `attackState = Declared` (uma vez por criatura e turno), turno
  novo pelo `turnInfo`, e "fim do jogo" por `gameInfo.stage`. Os códigos numéricos de
  `DamageDealt.type` e `UserActionTaken` ficam opacos.
- **Quem é "você":** `authenticateResponse.clientId` casado com `reservedPlayers` da
  sala; os nomes dos lugares vêm da sala. Sem sala (reprodução parcial), rótulos
  "jogador N".
- **Visão da partida (`board_text`)** em cerca de 15 linhas mais os últimos lances:
  cabeçalho (jogo, turno, fase, passo, ativo, vida), sua mão, seu campo (terrenos
  agrupados com virados, criaturas com P/R e estado, outras permanentes), campo do
  oponente, cemitérios, exílio, pilha, contagens de mão e biblioteca do oponente e mana
  aberta dos dois, cartas vistas do oponente (máximo simultâneo por carta), dicas.
- **Dicas calculáveis (`hints`)**: letal na mesa (soma do poder das suas criaturas
  desviradas sem enjoo contra a vida do oponente, com o número de bloqueadores desvirados
  dele, só no seu turno antes do dano de combate; ímpeto não é lido, então criaturas com
  ímpeto recém-chegadas não contam) e mana aberta do oponente. Nada de julgamento.
- **Registro** por jogo em `data/games/<data-hora>-<evento>-<oponente>-g<n>.json` (deck
  enviado, jogadores, resultado, vida, eventos com turno, fase e passo, cartas vistas,
  mesa final) e `.md` (lances agrupados por turno, mesa final), gravados quando o jogo
  acaba (`GameStage_GameOver`) ou a sala completa; uma vez por jogo; novo rastreador a
  cada `gameNumber`.
- **Oráculo:** em partida a janela mostra as últimas quatro linhas de sala (deck,
  oponente) e a visão da partida; em draft, o ranking (o mais recente ganha).
- **Fixture real:** a partida de 2026-11-07 anonimizada (nomes, ids de conta, sessões e
  ids de partida trocados) em `tests/fixtures/player-log-ladder-2026-11-07.txt.gz`, lida
  sem a base de cartas (nomes `#grpId`), para o teste de ponta a ponta.

## Estrutura

```
src/mtg_builder/arena_game.py       GameTracker: apply, describe, board_text, hints, record, markdown
src/mtg_builder/arena_match.py      classify_match entrega as mensagens; MatchSession usa o rastreador e grava
src/mtg_builder/companion.py        compose mostra a visão da partida
tests/test_arena_game.py            mensagens sintéticas por anotação; reprodução da partida real
tests/fixtures/player-log-ladder-2026-11-07.txt.gz
data/games/                         registros (fora do git)
```

## Riscos

- Categorias de `ZoneTransfer` e campos de objeto fora dos vistos nesta partida (ex.:
  bloqueios, cartas de duas faces, cópias) aparecem com texto genérico; o registro guarda
  o bruto para corrigir depois.
- O Arena pode mudar os nomes dos campos em atualizações; os testes com a partida real
  acusam.
- A visão pode não caber na janela em mesas cheias; a fonte é ajustável e os terrenos
  já saem agrupados.
