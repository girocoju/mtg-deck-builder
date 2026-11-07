# 010 — Plano

## Decisões

- **Fonte do draft ao vivo é o `Player.log` do Arena**, lido só em leitura, do mesmo
  jeito que o cliente aberto do 17Lands (`rconroy293/mtga-log-client`, consultado em
  2026-11-06) e o parser `manasight-parser` fazem. Caminho padrão no Windows:
  `%USERPROFILE%\AppData\LocalLow\Wizards Of The Coast\MTGA\Player.log` (o cliente
  recria o arquivo a cada abertura e guarda o anterior em `Player-prev.log`). A opção
  *Detailed Logs (Plugin Support)* precisa estar ligada; o arquivo diz `DETAILED LOGS:
  ENABLED` no começo, e o comando confere isso.
- **Formato das linhas:** cada mensagem começa com `[UnityCrossThreadLogger]` (ou
  `[Client GRE]`), seguido do nome do evento; o JSON começa no primeiro `[` ou `{` e pode
  continuar nas linhas seguintes. O leitor acumula linhas até o JSON fechar. Marcadores
  usados, com o campo que confirma cada um (nomes dos clientes citados acima; os do
  Arena mudam sem aviso, por isso ficam numa tabela única no código):

  | Modo | Pacote mostrado | Pick feito |
  | --- | --- | --- |
  | Premier / Traditional | `Draft.Notify` com `draftId`, `SelfPack`, `SelfPick`, `PackCards` (string "id,id,id" ou lista); ou `LogBusinessEvents` com `CardsInPack`, `PackNumber`, `PickNumber`, `PickGrpId` (mensagem combinada, cobre o P1P1) | `EventPlayerDraftMakePick` com `GrpIds`, `Pack`, `Pick`, `DraftId` |
  | Quick Draft | JSON com `DraftStatus == "PickNext"`, `DraftPack` (lista de ids), `PackNumber`, `PickNumber`, `EventName` | `BotDraft_DraftPick` com `PickInfo.CardIds`, `PackNumber`, `PickNumber` |
  | Qualquer | `Event_Join` com `EventName` (entrou no evento); `Draft_CompleteDraft` com `DraftId` (acabou) | |

  Pacote e pick vêm indexados a partir de zero; a saída mostra de 1 a 3 e de 1 a 14.
- **Identificadores resolvidos pela base do Arena:** `MTGA_Data\Downloads\Raw\
  Raw_CardDatabase_<hash>.mtga` (SQLite; o hash muda a cada atualização, o comando pega
  o mais recente da pasta). Tabela `Cards` (`GrpId`, `ExpansionCode`, `CollectorNumber`,
  `Rarity`, `TitleId`, `DraftContent`, `IsToken`) e `Localizations_enUS` /
  `Localizations_ptBR` (`LocId`, `Loc`) para nomes; os nomes trazem marcação HTML
  (`<nobr>`), removida na leitura. A junção com a base do projeto é primeiro pelo nome em
  inglês (é o que o Arena guarda) e, se o nome não existir na base, pela impressão
  `(ExpansionCode, CollectorNumber)` em `printings`. Conferido em 2026-11-06: 447 linhas FRA,
  305 cartas primárias, 301 com `DraftContent = 1`. O Scryfall não traz `arena_id` para
  FRA, por isso a base do Arena é a fonte primária do mapeamento, e `arena_id` o apoio.
  Caminho da instalação configurável (`--arena-dir`); padrão
  `C:\Program Files\Wizards of the Coast\MTGA`.
- **Motor de pick determinístico, com pesos em uma tabela.** Nota em pontos percentuais
  de win rate, para ser comparável ao GIH WR:
  - `poder` = GIH WR − média dos usuários (17Lands, modo pedido, mínimo 500 jogos em
    mão); sem amostra, Untapped (`data/fontes/...`, escalado pela média do Untapped);
    sem nada, nota teórica pela raridade e pela classificação de remoção da spec 008,
    marcada `teorica`;
  - `encaixe` = w(pick) × (bônus se a carta cabe nas cores inferidas; penalidade se não
    cabe; metade para carta de duas cores com uma delas), com w crescendo de 0 no P1P1 a
    1 no P2P7 e constante depois (seções 3 e 6 de `knowledge/limitado-e-draft.md`);
  - `par` = win rate do par (color ratings) − média, aplicado quando a carta cabe no par
    mais provável;
  - `necessidade` = bônus para função vazia no modelo do deck perfeito (criaturas de
    custo 2, 3 e 4, remoção, truques; contagens-alvo na tabela);
  - `sinal` = bônus quando ALSA da carta < pick atual (carta que costuma sair cedo
    chegou tarde), proporcional à diferença; cores que já passaram cartas boas neste
    draft somam;
  - `flexibilidade` = pequeno bônus para carta mono no primeiro pacote;
  - `sinergia` = w(pick) × 1,5 × (1,0 payoff | 0,5 enabler) do arquétipo do par mais
    provável, pelos padrões de `archetypes/<coleção>.json` (`archetypes.py`: `re:` texto,
    `kw:` palavra-chave, `type:`, `stat:`, `creature`, `&`). Em FRA (2026-11-07, 17Lands
    + Untapped, cerca de 80 cartas com dados por par), as cartas marcadas rendem de +0,2
    a +0,9 pp acima das não marcadas nas mesmas cores em 8 dos 10 pares (UG neutro; UR
    negativo em −1,7 pp mesmo depois de estreitar os enablers a custo 2 ou menos: as
    cartas de prowess e as mágicas baratas de FRA são, em média, mais fracas, e a
    marcação diz "pertence ao arquétipo", não "é boa"). É sinal pequeno: a sinergia
    desempata, não decide, e o peso máximo de 1,5 ponto reflete isso; o poder domina.
  Cores inferidas: soma do `poder` das cartas escolhidas por cor; o par mais provável é o
  melhor entre os pares com as duas cores mais fortes. A saída lista cada componente e o
  motivo em uma frase, e o agente faz a explicação final.
- **Estado do draft** em `data/drafts/<data>-<coleção>-<modo>-<id>.json`: evento, coleção,
  modo, lista de pacotes (número, pick, cartas vistas, carta escolhida, ranking calculado,
  hora) e pool final. `mtg draft pick` sem `--state` trabalha com o que foi passado na
  linha de comando; com `--state`, acumula.
- **`mtg draft watch`:** lê o arquivo de 0,5 em 0,5 s a partir do fim (ou do começo, com
  `--from-start`), detecta rotação (tamanho menor que a posição lida), e a cada pacote
  imprime cabeçalho (coleção, modo, pacote, pick, cores inferidas) e o ranking. `--file`
  lê um log gravado de ponta a ponta, sem esperar (base dos testes e das reproduções);
  `--check` só confere log, opção de logs detalhados, base do Arena e dados. A coleção
  vem do nome do evento (`PremierDraft_FRA_...`) ou, se o watch começou no meio, da
  coleção mais frequente entre as cartas do pacote. Nada sai da máquina.
- **Janela flutuante (`--window`, `overlay.py`):** tkinter da biblioteca padrão, janela
  *topmost* com transparência, fonte monoespaçada; Esc fecha, + e − mudam a fonte, F
  troca de canto. Em tela cheia exclusiva o jogo a cobre: usar modo janela ou tela cheia
  sem bordas. O terminal continua sendo o modo padrão. No venv deste projeto o tkinter
  só encontra o Tcl se `TCL_LIBRARY`/`TK_LIBRARY` apontarem para `<Python base>/tcl`
  (o módulo faz isso); sem Tcl/Tk, cai para uma janela WinForms aberta pelo PowerShell
  (`overlay.ps1`), que lê um arquivo temporário com o texto e um sinal de vida e se
  fecha sozinha quando o Python para.
- **Oráculo (`companion.py`, `mtg arena companion`):** laço que consulta `tasklist` a
  cada 3 s até ver `MTGA.exe`, abre a janela com um leitor de log de classificador
  combinado (draft e partida), fecha a janela quando o Arena some (verificado a cada 3 s
  dentro do `poll`) e, se o usuário fechou com Esc, só reabre no próximo início do Arena.
  Instalação: tarefa do Agendador do Windows (`Register-ScheduledTask -AtLogOn`, sem
  elevação; `schtasks /SC ONLOGON` exigiria administrador), nome "Oraculo - MTG Deck
  Builder", apontando para o `pythonw.exe` da instalação base do Python com
  `scripts/oraculo.pyw` (que põe `src/` no caminho): o `pythonw.exe` do venv é um
  lançador que abre um `python.exe` de console, e o Windows Terminal mostrava uma aba
  vazia para ele (2026-11-07). Registro em `data/companion.log`; `--start`, `--stop`,
  `--status`, `--uninstall`. A primeira versão usava um atalho na pasta Inicializar e um
  processo filho do terminal: o Windows Terminal e o VS Code matam a árvore de processos
  ao fechar a aba, e o Oráculo morreu junto (2026-11-07); a tarefa agendada nasce fora de
  qualquer terminal e sobrevive a ele.
- **Leitor de partidas (`arena_match.py`, `mtg arena watch`):** mesmo leitor de log com
  outro classificador: `authenticateResponse` (quem é o usuário), `EventSetDeckV3`
  (deck enviado, resolvido carta a carta), `matchGameRoomStateChangedEvent` (oponente,
  resultado) e `greToClientEvent.gameStateMessage` (turno, jogador ativo, vida). É o
  teste do leitor sem fichas; conferido em 2026-11-07 contra quatro partidas do log real.
- **Colação por coleção** em `src/mtg_builder/boosters/<coleção>.json` (vai para o git,
  é feito à mão): posições do pacote, raridade ou folha de cada posição, taxa por carta
  quando conhecida, fonte e data. Para FRA, a folha do Play Booster de papel do mtg.wtf
  (`/pack/fra-play`, 2026-11-06) sem a carta de token, 14 cartas; a lista de cartas
  draftáveis vem de `DraftContent = 1` na base do Arena quando disponível, senão das
  impressões `booster` da base. Aproximação declarada na saída do simulador.
- **Simulador:** mesa de 8, três pacotes passados esquerda, direita, esquerda; bots
  escolhem pelo motor com ruído gaussiano na nota e uma preferência de cor sorteada por
  bot; `--auto N` roda N mesas e resume cores abertas, pools e raridades. O modo
  interativo mostra o pacote numerado e lê o pick no terminal; os bots usam dados do modo
  pedido (Quick Draft com dados de Quick Draft).
- **Snapshots datados:** `data/17lands/<coleção>/<modo>/<data>.json` mais `latest.json`
  (cópia); `cached()` passa a devolver o mais recente, `--date` escolhe outro; os
  arquivos antigos no formato `<modo>.json` são migrados na primeira execução. Mesmo
  esquema para o Untapped quando houver importação.
- **Skill `draft`:** seção B chama `mtg draft pick` e cita os componentes; seção nova
  "D. Acompanhar um draft ao vivo" (ligar a opção no Arena, `mtg draft watch`, ler o
  ranking, `mtg draft pool` no final e seguir para a seção C).

## Estrutura

```
src/mtg_builder/draft.py            snapshots datados (update, cached, snapshots), Untapped e Draftsim
src/mtg_builder/draft_pick.py       motor de pontuação, inferência de cores, estado do draft, tabela
src/mtg_builder/arena_log.py        leitura do Player.log, marcadores, base de cartas do Arena
src/mtg_builder/arena_match.py      classificador de partidas e sessão (teste do log sem fichas)
src/mtg_builder/draft_sim.py        colação, geração de pacotes, bots, mesa
src/mtg_builder/overlay.py          janela flutuante (tkinter)
src/mtg_builder/boosters/fra.json   colação declarada (fonte e data); default.json genérica
src/mtg_builder/cli.py              mtg draft pick | watch | pool | sim; mtg arena watch
tests/test_draft_pick.py            motor com snapshot simulado, fontes secundárias, snapshots datados
tests/test_arena_log.py             mensagens de draft e de partida, leitor incremental, base do Arena
tests/test_draft_sim.py             colação, pacotes, mesa completa
tests/fixtures/player-log-premier-fra-sintetico.txt   draft de 42 picks com GrpIds reais
.claude/skills/draft/SKILL.md       seções B e D
data/drafts/<...>.json              estados (fora do git)
```

## Modelo de dados

Estado do draft:

```json
{"event": "PremierDraft_FRA_20261106", "set": "fra", "mode": "premier",
 "snapshot": "2026-11-06", "started_at": "...",
 "packs": [{"pack": 1, "pick": 1, "seen": ["Denzilore Fatehold", "..."],
            "picked": "Liliana the Faultless", "ranking": [{"name": "...", "total": 4.2,
            "poder": 3.1, "encaixe": 0.0, "par": 0.0, "necessidade": 0.6, "sinal": 0.0,
            "flexibilidade": 0.5, "fonte": "17lands|untapped|teorica"}]}],
 "colors": {"W": 7.5, "U": 2.1}, "pool": ["..."]}
```

Colação:

```json
{"set": "fra", "source": "https://mtg.wtf/pack/fra-play", "collected_at": "2026-11-06",
 "cards": 14, "note": "Play Booster de papel sem a carta de token",
 "slots": [{"rarity": "common", "count": 6}, {"rarity": "uncommon", "count": 1},
           {"sheet": "common_uncommon", "count": 1}, ...,
           {"sheet": "rare_mythic", "count": 1, "rates": {"rare": 0.875, "mythic": 0.125}}]}
```

## Riscos

- **O formato do log muda** com atualizações do Arena. Mitigação: marcadores em uma
  tabela, teste com trecho real, e o watch avisa "linha de draft não reconhecida" em vez
  de calar.
- **P1P1 sem `Draft.Notify`** (relato no fórum da Wizards). Mitigação: tratar a mensagem
  combinada de `LogBusinessEvents` e, na falta das duas, aceitar o pacote digitado.
- **Base do Arena em `Program Files`**: leitura simples, mas o hash do arquivo muda;
  escolher o mais recente e expor `--arena-dir`.
- **Dados do 17Lands encolhidos** (2026-11-06): sem rara com amostra, o motor cai no
  Untapped ou na nota teórica; a saída sempre diz a fonte de cada nota.
- **Bots não são humanos:** o simulador serve para treino e para medir a mesa, não para
  prever o Arena; a saída diz isso.
- **Colação aproximada:** confrontar a distribuição de raridades dos pacotes capturados
  no log com a declarada e ajustar o arquivo.
