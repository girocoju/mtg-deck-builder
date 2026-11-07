# 013 — Perfil do Arena em vários dispositivos

**Status:** 📝 Especificada

## Objetivo

Transformar o que o Oráculo acumula no PC (partidas, win rate por deck, rank, cofre,
baú, coleção aproximada, registros de jogo, rankings de draft) em um **perfil do MTG
Arena** consultável também no celular (Android e iPhone), como o Untapped faz com o seu
aplicativo.

Pedido do usuário em 2026-11-07: "um grande gerenciador de perfil do MTG Arena com o
Oráculo para PC desktop e mobile, Android e iPhone. É possível termos isso em mobile?"

## O que é possível no celular, e o que não é

- **Ler o jogo no celular, não.** O Arena para Android e iOS grava seus arquivos na área
  privada do aplicativo: no Android ela só é acessível com root, e no iOS o sandbox
  impede qualquer outro aplicativo de ler. Por isso o companheiro do Untapped existe só
  para PC e Mac, e o aplicativo de celular deles mostra o que foi sincronizado do PC. O
  mesmo vale aqui: **a captura fica no PC**, pelo Oráculo; partidas jogadas só no celular
  não entram.
- **Consultar o perfil no celular, sim.** O PC publica o que acumulou e o celular lê.

## Opções de entrega (decisão do usuário)

| Opção | Como | Prós | Contras |
| --- | --- | --- | --- |
| A. Página web estática | O Oráculo gera `perfil/index.html` com os dados embutidos; publicada no GitHub Pages do repositório ou como artefato privado | Sem servidor; funciona em qualquer celular; instalável como PWA | Repositório público expõe oponentes e coleção; GitHub Pages em repositório privado exige plano pago; artefato depende de republicar |
| B. Bot de mensagens | Um bot no Telegram ou WhatsApp responde "win rate do Turn 2 Kill?", "quantos Ghalta tenho?" lendo os arquivos do PC (o usuário já constrói automações desse tipo) | Conversa natural; nada publicado na web | O PC precisa estar ligado para responder; exige token do bot e um serviço rodando |
| C. Sincronização para a nuvem | O Oráculo envia `matches.jsonl`, `collection.json` e os registros para um armazenamento (Drive, bucket) e um aplicativo ou página lê de lá | Dados disponíveis com o PC desligado | Mais peças; credenciais na máquina |

## Requisitos (independentes da opção)

1. **Exportador do perfil** (`mtg arena profile`): um JSON único com partidas e win rate
   por deck, rank e saldo da temporada, cofre e baú ao longo do tempo, coleção aproximada
   por coleção, decks salvos com última partida, últimos registros de jogo e, em draft,
   o estado do draft em andamento. Gerado pelo Oráculo a cada partida e sob demanda.
2. **Página do perfil** (opção A como base, usada também pelas outras): HTML sem
   dependências externas, que cabe na tela de celular, com as seções acima e a data da
   última atualização.
3. **Privacidade:** nomes de oponentes e ids de conta só saem da máquina com decisão
   explícita do usuário; a página pode omiti-los.
4. **Honestidade:** a página diz que partidas no celular não são capturadas e que a
   coleção é aproximada.

## Critérios de aceite

- [ ] `mtg arena profile` gera o JSON e a página a partir dos dados existentes, com teste.
- [ ] A página abre no celular do usuário com as partidas de 2026-11-07 e o win rate do
      Turn 2 Kill (registrar como foi publicada).
- [ ] Uma partida jogada no PC aparece no celular sem passo manual além de abrir a página.

## Dependências

Specs 010 e 011 (dados), decisão do usuário sobre a opção de entrega e a privacidade.

## Fora do escopo

- Captura de partidas jogadas no celular (impossível sem root).
- Aplicativo nativo nas lojas (a página instalável cobre o uso).

## Questões em aberto

- Opção A, B ou C? E, na A, repositório público ou outro lugar?
- Mostrar nomes de oponentes fora do PC?
