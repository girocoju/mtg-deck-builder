# 010 — Tarefas

- [x] Snapshots datados do 17Lands (`data/17lands/<coleção>/<modo>/<data>.json` +
      `latest.json`, migração dos arquivos antigos, `--snapshot`), com teste
- [x] `arena_log.py`: localizar `Player.log`, conferir *Detailed Logs*, ler mensagens
      (marcadores da tabela do plano), ler a base de cartas do Arena e juntar com a base
      do projeto; testes com trechos sintéticos
- [x] `draft_pick.py`: motor de pontuação (tabela de pesos, componentes, fontes), inferência
      de cores, estado do draft; testes com snapshot simulado, inclusive carta sem dado
- [x] `mtg draft pick` (pacote na linha de comando ou `--state`), saída em tabela e `--json`
- [x] `mtg draft watch` (`--file`, `--from-start`, `--arena-dir`, `--check`, `--window`),
      `mtg draft pool`
- [x] Colação `boosters/fra.json` (mtg.wtf, 2026-11-06) e `draft_sim.py` (pacotes, bots,
      mesa, `--auto N`); teste de distribuição de raridades
- [x] `mtg draft sim` interativo e automático
- [x] Leitor de partidas `mtg arena watch` (pedido do usuário: testar o log numa ranqueada
      antes de gastar fichas); conferido contra o log real
- [x] Skill `draft`: seção B pelo motor; seção D "Acompanhar um draft ao vivo"
- [x] `CLAUDE.md`: comandos novos na lista de ferramentas
- [x] Oráculo (`companion.py`, `mtg arena companion`): espera o `MTGA.exe`, abre a janela com
      draft e partida, fecha quando o Arena fecha; instalado como tarefa agendada do
      Windows em 2026-11-07 (a versão por atalho e processo filho morreu junto com o
      terminal do usuário; a tarefa nasce do serviço do Agendador e sobrevive)
- [x] Sinergia por arquétipo (`archetypes/fra.json`, componente `sinergia`, `mtg draft synergy`)
      a partir das descrições oficiais dos dez pares; sinal medido nos dados (plano)
- [x] Teste ao vivo sem fichas: com o Oráculo aberto, uma partida de ranqueada (deck,
      oponente, turnos e resultado aparecendo em tempo real). *(2026-11-07, 00:39–00:44,
      Ladder de Standard contra Mister_Jedi: deck "Turn 2 Kill" de 60 cartas, todas
      resolvidas; dez turnos com vida; vitória registrada no instante; captura de tela do
      usuário. O usuário notou que só vida, turnos e resultado aparecem: fases, ataques,
      dano e cartas jogadas ficam para uma spec própria.)*
- [x] Primeiro draft real acompanhado pelo Oráculo (2026-11-09, Premier Draft de FRA, ver
      "Verificação (2026-11-09)"): trecho anonimizado em
      `tests/fixtures/player-log-premier-fra-2026-11-09.txt`, teste de 42 pacotes e 42 picks
- [x] Deck de 40 montado a partir do pool capturado e validado
      (`decks/limited/fra-draft-2026-11-09-ug-splash-r.md`, montado à mão durante a sessão;
      a montagem automática do Oráculo reproduz o mesmo par e o mesmo splash)
- [x] Correções do primeiro draft real: numeração de pacote e pick (base 1 em `Draft.Notify`
      e `EventPlayerDraftMakePick`), evento de encerramento sem `DraftId`, linha de
      recomendação `► PEGUE:` na janela, bônus de sobra para rara ou mítica que falta na
      coleção (`col`), montagem automática do deck ao fim do draft (`draft_deck.py`,
      `mtg draft build`)
- [ ] Confrontar a distribuição de raridades dos pacotes capturados com a colação declarada
- [ ] Verificar os critérios de aceite restantes e atualizar o status no roadmap

## Verificação (2026-11-09): primeiro draft real

- Premier Draft de FRA (`PremierDraft_FRA_20260929`), 19:29–19:50, com o Oráculo aberto e o
  agente acompanhando o estado em `data/drafts/` por um monitor. **O P1P1 apareceu** no log
  antes do pick (`Draft.Notify` com 14 cartas); 42 pacotes e 42 picks reconhecidos, 0 linhas
  não decodificadas; o encerramento veio como `DraftCompleteDraft` com `EventName` e sem
  `DraftId`.
- **Numeração errada:** a janela mostrou o primeiro pacote como "P2 pick 2". O log real traz
  `SelfPack`/`SelfPick` e `Pack`/`Pick` a partir de 1; o leitor somava 1 (suposição do
  sintético). Efeito: o compromisso de cor começava em 75% e o ranking favorecia a cor do
  primeiro pick; o agente recalculou cada pacote com `mtg draft pick --pack --pick` durante
  o draft. Corrigido; o sintético foi rebaseado para base 1; `LogBusinessEvents`,
  `DraftStatus` e `BotDraft_DraftPick` seguem como base 0, ainda sem log real para conferir.
- **Pedidos do usuário durante o draft:** "O Oráculo só mostra métrica? Não fala a escolha
  que tenho que fazer?" → linha `► PEGUE: carta (nota; por quê) · 2º · 3º`, com aviso de
  empate técnico abaixo de 0,5 ponto. "Insira a montagem do deck no Oráculo também" →
  `draft_deck.py` e `mtg draft build`; ao fim do draft a janela mostra a lista para o Arena
  e grava `decks/limited/<coleção>-<evento>-<data>-<cores>.md`. "Não teve UMA pick de rara e
  mítica" → do pick 9 em diante, rara (+1,5) ou mítica (+2,5) que falta na coleção ganha o
  componente `col`; nas 42 picks reais, teria mudado só sobras (Identity Echo, Loot, Karn).
- Reprodução do trecho real (`mtg draft watch --file ... --set fra --offline`): 42/42, deck
  proposto UG com splash R (Clash of Elements e dois Fulminous Forte), 23 mágicas, 17
  terrenos, o mesmo par e splash da montagem à mão; diferenças só nas últimas vagas
  (a automática prefere Something Worth Saving ×3 a Icy Reception e Infinite Coursework,
  por poder), por isso a proposta passa pela revisão da seção C da skill.
- Dado novo: o snapshot do 17Lands colhido às 19:29 (895 mil jogos) mudou notas de comuns
  em até 4 pontos em relação ao de 2026-11-08 (Hexhaven Battalion 56,7% → 61,3%): a fonte
  pública está instável; a recomendação cita a data e a fonte em cada linha.

## Verificação (2026-11-07)

- Suíte: 91 testes passando (`python -m pytest -q`).
- `mtg arena watch --file` sobre o `Player.log` real: deck de Brawl de 99 cartas resolvido
  por nome (todas), quatro partidas com oponente, turnos, vida e resultado corretos.
- `mtg draft watch --file tests/fixtures/player-log-premier-fra-sintetico.txt`: 42 pacotes,
  42 picks (o primeiro só pela mensagem combinada), 0 entradas não decodificadas, pool de
  42 cartas gravado em `data/drafts/`.
- `mtg draft pick fra ...` com os exemplos do usuário: Multiply by Zero (17Lands 63,2%)
  à frente de Denzilore Fatehold (Untapped 59,9%, sem amostra no 17Lands) no P1P1; no
  P2P1 com W/U escolhidas, Garruk, Veiled Butcher (64,8%) ainda vence a penalidade de cor.
- `mtg draft sim fra --auto 10 --seed 5`: 1,26 raras ou míticas por pacote (colação
  declarada: 1,28); pares mais escolhidos pelos bots UB, WU, UR.
- Bugs achados pelos testes e corrigidos: par de cores sem dados virava penalidade de −27
  pontos; terrenos raros saíam na posição de terreno comum do pacote; índice fora do
  intervalo no decodificador do Untapped; nomes da base do Arena com marcação `<nobr>`.
- Janela flutuante: o tkinter do venv não achava o Tcl (`init.tcl`); corrigido apontando
  `TCL_LIBRARY` para o Python base, e acrescentada a janela em PowerShell/WinForms como
  reserva. As duas abriram e fecharam nos testes de fumaça (`mtg draft watch --window`
  por 6 s; janela PowerShell por 3 s, encerrada pelo Python).
- Perfil de colação `fra-paper.json` a partir de 13 Play Boosters de papel enviados pelo
  usuário (5,3 incomuns e 7,6 comuns por pacote); `mtg draft sim fra --booster paper
  --auto 5` reproduz a amostra (5,4 incomuns por pacote, 1,03 raras ou míticas).
