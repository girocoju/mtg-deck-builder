# 010 — Assistente e simulador de draft

**Status:** 🚧 Em andamento — código, testes e reprodução offline prontos (2026-11-07); falta o primeiro draft real

## Objetivo

Atender pedidos como **"Estou draftando Reality Fracture agora: a cada pacote, me diga o
melhor pick considerando o que já peguei"**, no instante em que o pacote aparece e sem
depender de captura de tela: ler o pacote direto do log que o MTG Arena grava em disco,
pontuar cada carta com a conta aberta, e permitir treinar fora do jogo com um simulador de
draft contra bots. É a continuação da seção "Recomendar um pick" da spec 008, que hoje
depende de o usuário digitar o pacote e de o agente ponderar sem guardar o estado do draft.

## Histórias de uso

- "Vou draftar FRA agora no Arena. Acompanhe meus picks e me diga o que pegar a cada
  pacote." (ao vivo, pelo log do cliente)
- "P1P1: Denzilore Fatehold, Liliana the Faultless e Identity Echo. Qual pego?" (digitado)
- "Peguei Liliana. No segundo pacote vieram Jace, Reality Sculptor; Garruk, Veiled Butcher
  e Sanctum Lurker. E agora?" (o pick depende do que já foi escolhido)
- "Se eu pegar a Liliana, o que posso esperar do próximo pacote?" (probabilidades)
- "Simule um draft de FRA para eu treinar." / "Rode cem drafts e me diga que cores os bots
  deixam abertas."
- "Acabou o draft: monte o deck de 40 com o que peguei." (spec 008, seção C, agora com o
  pool capturado automaticamente)

## Como o Untapped faz e o que dá para fazer aqui

O Arena não tem API de plugins. O Draftsmith do Untapped e o cliente do 17Lands leem o
arquivo **`Player.log`**, que o cliente grava em disco quando a opção *Detailed Logs
(Plugin Support)* está ligada. Na máquina do usuário, conferido em 2026-11-06: opção
ligada, arquivo em `%USERPROFILE%\AppData\LocalLow\Wizards Of The Coast\MTGA\Player.log`.
O log registra cada pacote mostrado (identificadores das cartas, número do pacote e do
pick) e cada pick feito, em Premier, Traditional e Quick Draft. Os identificadores são
resolvidos pela base de cartas do próprio Arena, um SQLite em
`MTGA_Data\Downloads\Raw\Raw_CardDatabase_*.mtga`, com coleção, número de colecionador,
raridade e nomes em inglês e português, que se junta à base do projeto por (coleção,
número).

Consequência: não há overlay dentro do jogo nesta spec. O assistente roda em uma janela
ao lado (terminal, segundo monitor) e atualiza sozinho a cada pacote. Overlay desenhado
sobre a janela do jogo é uma fase posterior possível, listada em "Fora do escopo".

## Requisitos

1. **Motor de pontuação de pick** (`mtg draft pick`). Entrada: coleção, modo, número do
   pacote e do pick, cartas do pacote e cartas já escolhidas (do estado do draft ou de um
   arquivo). Saída: ranking do pacote com a nota total e os componentes, cada um visível:
   - **poder:** GIH WR do 17Lands no modo pedido, contra a média dos usuários; Untapped
     como segunda fonte quando o 17Lands não tem amostra; sem dado algum, avaliação
     teórica pela leitura da carta (raridade, remoção, custo), marcada como teórica;
   - **encaixe nas cores:** peso do compromisso cresce com o pick (picks 1 a 4 quase só
     poder; de meados do segundo pacote em diante, o deck manda), conforme
     `knowledge/limitado-e-draft.md`, seções 3 e 6;
   - **força do par de cores** (color ratings do 17Lands);
   - **necessidade do deck:** modelo do "deck perfeito" (criaturas na curva, remoção,
     truques): a carta que preenche uma função vazia sobe;
   - **sinal:** ALSA da carta contra o pick atual (carta que costuma sair cedo e chega
     tarde indica cor aberta), e o que já foi passado neste draft;
   - **flexibilidade:** carta de uma cor vale mais que carta de duas no começo;
   - **sinergia** (pedido do usuário em 2026-11-07, a partir das descrições oficiais dos
     dez arquétipos na tela do evento do Arena): payoff ou enabler do arquétipo do par
     escolhido, por padrões sobre o texto de regras (`archetypes/<coleção>.json`), com
     `mtg draft synergy` medindo nos dados se a marcação carrega sinal.
   O motor é determinístico e testado; os pesos ficam em uma tabela única e documentada.
   O julgamento final e a explicação continuam com o agente, que cita os componentes.
2. **Estado do draft.** Cada draft tem um arquivo com pacotes vistos, picks feitos, cores
   inferidas e cartas passadas (para os sinais). Permite retomar, auditar e, ao final,
   exportar o pool para a montagem do deck de 40.
3. **Acompanhamento ao vivo** (`mtg draft watch`). Lê o `Player.log` incrementalmente,
   reconhece pacote e pick de Premier, Traditional e Quick Draft, resolve os
   identificadores pela base do Arena, atualiza o estado e imprime o ranking no instante
   em que o pacote aparece; registra o pick quando ele é feito; ao final, grava o pool.
   Exige a opção *Detailed Logs* ligada e avisa quando ela estiver desligada ou o log não
   for encontrado. Só lê o arquivo: nada é enviado a serviço nenhum.
4. **Simulador** (`mtg draft sim`). Gera três pacotes de 14 cartas pela composição
   declarada da coleção (arquivo de colação por coleção, com fonte e data), põe sete bots
   escolhendo com o motor do requisito 1 (com ruído e preferências de cor, para a mesa
   variar) e conduz o draft no terminal, pick a pick, ou de forma automática
   (`--auto N`) para medir o que os bots deixam aberto. Produz o pool e segue para a
   montagem do deck.
5. **Probabilidades mostradas ao usuário.** Chance de a carta dar a volta no pacote,
   estimada pelo ALSA; o que esperar do próximo pacote (raridades por posição, chance de
   ao menos uma rara ou mítica de um par de cores), calculado pela colação e pela lista
   de cartas draftáveis; tudo apresentado como estimativa, com a fonte.
6. **Snapshots datados** do 17Lands e do Untapped, como a spec 005 faz com o meta: um
   arquivo por coleção, modo e data, nunca sobrescrito; toda saída diz a data e o tamanho
   da amostra. Motivação: em 2026-11-06 a coleta do 17Lands para FRA veio com 73 das 290
   cartas com win rate e nenhuma rara, sobrescrevendo o snapshot de 2026-10-12 que
   sustenta `drafts/fra/guia.md`.
7. **Skill `draft` atualizada:** a seção B passa a usar o motor; nova seção "Acompanhar
   um draft ao vivo" com o passo a passo (ligar a opção no Arena, abrir o watch, ler o
   ranking, montar o deck no final).
8. **Honestidade.** Notas são estimativas; raras e míticas costumam estar sem amostra;
   bots do simulador não são humanos nem os bots do Quick Draft do Arena; o log pode
   atrasar ou mudar de formato a cada atualização do cliente, e o assistente diz quando
   deixa de entender uma linha.
9. **Teste do leitor sem gastar fichas** (pedido do usuário em 2026-11-07, fichas e
   recursos escassos): um leitor de partidas (`mtg arena watch`) mostra deck enviado,
   oponente, turnos, vida e resultado de um jogo comum, provando que o log está sendo
   gravado e lido ao vivo e que os identificadores viram nomes; e uma reprodução de log
   sintético (`mtg draft watch --file`) percorre os 42 picks antes do draft real.
10. **Janela flutuante** (`--window`): janela comum do Windows sempre no topo e
    semitransparente, visível com o Arena em modo janela ou tela cheia sem bordas; não
    desenha sobre o jogo.
11. **Decisão explícita e deck no fim** (pedidos do usuário durante o primeiro draft real,
    2026-11-09): cada pacote abre com a linha `► PEGUE: carta (nota; por quê) · 2º · 3º`,
    com aviso de empate técnico quando a diferença é menor que meio ponto, porque "o
    Oráculo só mostra métrica, não fala a escolha". Ao fim do draft (último pick ou evento
    de encerramento) o Oráculo monta o deck de 40 pelo método da skill `draft` (par pelas
    jogáveis, splash de até três cartas de um símbolo, doze corpos, quatro de interação,
    dezessete terrenos), mostra a lista pronta para o Arena na janela e grava o arquivo em
    `decks/limited/`; `mtg draft build` repete a montagem na linha de comando. Do pick 9 de
    cada pacote em diante, rara ou mítica que falta na coleção conhecida ganha um bônus
    pequeno, porque "não teve UMA pick de rara" num draft em que as raras dos pacotes eram
    fracas: no Arena, rara em pick de sobra é coringa.

## Critérios de aceite

- [x] Dados um pacote e os picks anteriores (teste sem rede, snapshot simulado),
      `mtg draft pick` devolve o ranking com os componentes de cada carta, e cartas sem
      dado aparecem marcadas como avaliação teórica. *(tests/test_draft_pick.py)*
- [x] Com um trecho de `Player.log`, `mtg draft watch --file` reproduz os 42 pacotes e
      picks, resolve todas as cartas pela base do Arena e grava o pool com as 42 cartas
      escolhidas. *(2026-11-07, log sintético com GrpIds reais de FRA:
      `tests/fixtures/player-log-premier-fra-sintetico.txt`; 2026-11-09, trecho real do
      primeiro draft: `tests/fixtures/player-log-premier-fra-2026-11-09.txt`, 42/42, deck
      montado no fim)*
- [x] Em um draft real no Arena, o ranking aparece na janela antes de o usuário escolher,
      em cada um dos 42 picks, sem captura de tela. *(2026-11-09, Premier Draft de FRA com o
      Oráculo: o P1P1 apareceu, 42 pacotes e 42 picks; a numeração saiu errada e foi
      corrigida; registro em `tasks.md`)*
- [x] `mtg draft sim fra --auto 10` gera 80 pools de 42 cartas com distribuição de
      raridades compatível com a colação declarada. *(2026-11-07: 3,8 raras ou míticas
      por pool de 42, ou 1,26 por pacote, igual ao esperado da colação; teste de mesa
      completa em tests/test_draft_sim.py)*
- [x] Toda saída numérica traz fonte, data, modo e amostra; snapshots novos não apagam os
      anteriores e o guia continua apontando para o seu. *(snapshots datados com
      `latest.json`; `--snapshot AAAA-MM-DD` escolhe outro)*
- [x] O leitor de partidas reproduz um log real com deck, oponente, turnos, vida e
      resultado corretos. *(2026-11-07: quatro partidas de Brawl do log do usuário, deck
      de 99 cartas com todos os nomes resolvidos; falta o teste ao vivo em ranqueada)*
- [x] Um deck de 40 montado a partir de um pool capturado ao vivo passa no validador
      (spec 008, seção C). *(2026-11-09: `decks/limited/fra-draft-2026-11-09-ug-splash-r.md`,
      `mtg deck validate --format limited` válido; a montagem automática do Oráculo sobre o
      mesmo pool dá o mesmo par e splash)*

## Dependências

Spec 001 (base de cartas: junção por coleção e número de colecionador), 008 (dados do
17Lands, skill `draft`, montagem do deck de 40) e 003 (validação e exportação).

## Fora do escopo

- Overlay desenhado sobre a janela do jogo; captura de tela ou OCR.
- Enviar dados a serviços externos; qualquer interação com a conta do Arena.
- Sealed ao vivo (o log também registra a abertura dos pacotes; pode entrar depois, a
  montagem já é coberta pela 008).
- Análise das partidas além do leitor de teste do requisito 9 (mão, jogadas, decisões).

## Questões em aberto

- **Win rate por par de cores no 17Lands:** o endpoint público ignorou os parâmetros
  `colors` e `deck_colors` em 2026-11-06. Sem ele, o encaixe vem do GIH WR geral mais a
  força do par; conferir na página do site se existe outro parâmetro antes do plano final.
- **Encolhimento dos dados do 17Lands** em 2026-11-06 (causa desconhecida). Se persistir,
  o Untapped passa a fonte principal para raras e míticas, e o guia diz isso.
- **Primeiro pick do primeiro pacote:** há relato no fórum da Wizards de que o evento do
  pacote não é gravado para o P1P1 em algumas versões; o cliente do 17Lands trata uma
  mensagem combinada para esse caso. Confirmar no primeiro draft real e registrar.
- **Colação do Arena para FRA:** o mtg.wtf só publica a do booster de papel (com posições
  de par de planeswalkers e uma posição "third_not"); o pacote do Arena tem 14 cartas.
  Usar a de papel sem a carta de token, declarar a aproximação e confrontar com os
  pacotes capturados no log.
