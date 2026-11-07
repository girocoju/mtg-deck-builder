# 011 — Tarefas

- [x] `arena_game.py`: rastreador (zonas, objetos, troca de instância, vida, turno), eventos
      em PT-BR, visão da partida, dicas calculáveis, registro JSON e Markdown
- [x] `arena_match.py`: mensagens inteiras no evento `game_state`; sessão com rastreador,
      `board()`, gravação em `data/games/`
- [x] Oráculo mostra a visão da partida; `mtg arena watch --file` imprime a mesa final
- [x] Fixture anonimizada da partida de 2026-11-07 e teste de reprodução de ponta a ponta
- [x] Testes sintéticos por tipo de anotação
- [ ] Teste ao vivo: uma ranqueada com a visão na janela (registrar data e o que faltou)
- [ ] Skill: análise de partida a partir do registro e lição em `knowledge/licoes/`
- [ ] Decidir a questão em aberto (conselho por julgamento via API) depois do uso

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
