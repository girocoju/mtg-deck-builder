# 011 — Tarefas

- [x] `arena_game.py`: rastreador (zonas, objetos, troca de instância, vida, turno), eventos
      em PT-BR, visão da partida, dicas calculáveis, registro JSON e Markdown
- [x] `arena_match.py`: mensagens inteiras no evento `game_state`; sessão com rastreador,
      `board()`, gravação em `data/games/`
- [x] Oráculo mostra a visão da partida; `mtg arena watch --file` imprime a mesa final
- [x] Fixture anonimizada da partida de 2026-11-07 e teste de reprodução de ponta a ponta
- [x] Testes sintéticos por tipo de anotação
- [x] Teste ao vivo: ranqueada em 2026-11-07 (spec 010) e, em 2026-11-09, as quatro partidas
      do primeiro Premier Draft mais as de Ladder da mesma noite, todas com a visão na janela
      e gravadas em `data/games/`; o que faltou está em "Verificação (2026-11-09)"
- [ ] Skill: análise de partida a partir do registro e lição em `knowledge/licoes/` (a primeira
      análise foi feita à mão em 2026-11-09, lição
      `knowledge/licoes/2026-11-09-draft-fra-ug-primeiro-draft-1-3.md`; a skill ainda não existe)
- [ ] Decidir a questão em aberto (conselho por julgamento via API) depois do uso

## Verificação (2026-11-09)

Quatro partidas do Premier Draft de FRA (1–3: take2 WB, dsnipex RG, GeextaH RG, Sasiki
BG+U) gravadas ao vivo pelo Oráculo; o usuário pediu "o primeiro foi horroroso, consegue
ver os logs?", e a análise saiu dos registros (lances turno a turno, mão e campos nos
`snapshots` do JSON, texto das cartas pela base). Lição registrada em
`knowledge/licoes/2026-11-09-draft-fra-ug-primeiro-draft-1-3.md`.

Dois defeitos nos registros, corrigidos:

- **Deck de outro evento.** Os quatro registros saíram "com Turn 2 Kill", o deck de Ladder
  enviado às 17h. O `EventSetDeckV3` do deck de Limitado chegou ao log às 19:55 e 19:58
  ("Deck Draft Oráculo v1", 40 cartas), mas o classificador de draft chama de "unknown"
  toda linha que cite um evento de draft, e `companion.classify_all` parava nele; o lado da
  partida nunca viu o deck. Agora "unknown" não impede o classificador de partida, e
  `MatchSession.match_deck()` só usa o deck cujo `EventName` é o da sala (a linha
  "partida em ..." diz qual deck, ou avisa que o deck deste evento não apareceu no log).
- **Fichas com nome de carta.** O Beast 4/4 de Bestial Incursion saía como "Generous
  Revival", o Jace como "Enlightened Confidant" e o Heartwood como "Guiding Hydra": na
  base do Arena as fichas de FRA têm `ExpansionCode` FRA e números 1 a 15 (Beast #8, Jace
  #5, Heartwood #11), e a resolução pela impressão (coleção + número) as confundia com as
  cartas reais de mesmo número. Ficha agora fica com o próprio nome (`token: true`), sem a
  queda para a impressão.

Reprodução do `Player.log` inteiro com o código corrigido (`arena_match.classify_match`,
806 eventos): oito partidas reconhecidas (Yxma, take2, dsnipex, GeextaH, Sasiki, CeeK,
EndersShadow501, Mastropasqua), decks "Turn 2 Kill", "Deck Draft Oráculo v1" e "Orzhov
Infinite Turns" nos eventos certos; os quatro registros do draft foram substituídos pelos
regenerados (mesmos nomes de arquivo). Testes novos: deck de outro evento fora do
registro, ficha com número colidente, classificador combinado deixando o deck de Limitado
passar. Suíte: 130 testes. O Oráculo aberto desde 17:29 ainda roda o código antigo; a
troca pede `mtg arena companion --stop` e `--start` entre partidas.

Observado nos registros e ainda não tratado: uma mágica iniciada e cancelada no cliente
aparece como "você conjura X" seguido de "você compra X" no turno seguinte (Fulminous
Forte, turno 11 da partida contra take2); um cancelamento deveria aparecer como tal.

## Verificação (2026-11-07)

Reprodução da partida real (Ladder, "Turn 2 Kill" contra Mister_Jedi) com
`mtg arena watch --file`: 456 eventos reconhecidos; o rastreador narrou do primeiro
terreno ao fim: compras (as suas com o nome, as do oponente como "uma carta"), terrenos
jogados, conjurações e resoluções, ficha criada, marcador, as duas lutas de The Last
Agni Kai (15 de dano em cada bloqueador e as mortes), o ataque com Llanowar Elves e
Ghalta, Primal Hunger 15/12, os 16 de dano, Burn Together com mais 15 (vida −11),
o sacrifício e a vitória. Mesa final com mão, campos (terrenos agrupados, virados),
cemitérios, exílio, contagens e cartas vistas do oponente. Registro gravado em
`data/games/2026-11-07-0056-Ladder-Mister_Jedi-g1.{json,md}`.

Limites vistos: criaturas com ímpeto recém-chegadas não entram na conta de letal (o log
não traz palavras-chave), e a conta não prevê truques nem arremessos: no turno 10 ela
diria "sem letal" (16 de poder contra 20 de vida) e o jogo acabou com Wild Ride, duas
lutas e Burn Together. A dica some na segunda fase principal e no fim do combate, de
propósito. O Oráculo foi reiniciado com o rastreador às 00:58; falta ver a visão da
partida ao vivo numa ranqueada.
