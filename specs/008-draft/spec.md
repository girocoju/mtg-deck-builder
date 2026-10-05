# 008 — Draft

**Status:** ✅ Concluída

## Objetivo

Atender pedidos como **"Crie uma estratégia de drafts para a coleção Reality Fracture"**:
um guia de draft por coleção, combinando leitura das cartas, teoria de limitado e, quando
existirem, dados reais de desempenho.

## Histórias de uso

- "Crie uma estratégia de drafts para a coleção Reality Fracture."
- "Quais são as melhores comuns de cada cor em [coleção]?"
- "Estou no pick 1 do pacote 2 com estas cartas; qual pego?" (dado o que já peguei)
- "Draftei estas 45 cartas; monte o melhor deck de 40."

## Requisitos

1. **Comando/skill** dedicado, que recebe a coleção por nome ou código.
2. **Leitura da coleção** a partir da base (spec 001): todas as cartas da coleção (uma
   por carta, ignorando variantes de arte), por cor e raridade, sem distinguir em que
   tipo de booster cada uma sai; mecânicas e palavras-chave; curva de criaturas, remoções e truques de
   combate disponíveis por cor nas comuns e incomuns.
3. **Dados do 17Lands** quando disponíveis para a coleção: win rate por carta (GIH WR),
   ordem média de pick e desempenho por par de cores — com data de coleta e cache local.
   Todos os modos de limitado que o 17Lands cobre são elegíveis e ficam separados:
   Premier Draft, Quick Draft, Traditional Draft (BO3), Sealed e Traditional Sealed, além
   de modos especiais quando existirem. O usuário pode pedir um modo específico; sem
   indicação, o guia usa o modo com mais dados e aponta onde os outros divergem (ex.:
   bots do Quick Draft valorizam cartas de forma diferente de jogadores humanos).
4. **Modo teórico** para coleções sem dados (recém-lançadas ou só de papel): avaliação
   pelas regras de limitado da base de conhecimento, declarada como teórica.
5. **Guia da coleção** com:
   - visão geral: velocidade do formato, mecânicas, o que importa;
   - os 10 arquétipos (pares de cores): plano, cartas-chave, incomuns sinalizadoras;
   - ranking de comuns e incomuns por cor; bombas e remoções por raridade;
   - ordem de prioridade de picks e como ler sinais;
   - armadilhas: cartas superestimadas e subestimadas (dados vs. impressão);
   - recomendações de construção: terrenos, curva, número de criaturas.
6. **Assistente de pick e de montagem:** dado um pacote e as cartas já escolhidas,
   recomenda o pick com justificativa; dado um pool, monta o deck de 40 e valida (spec 003).
7. Guias salvos em `drafts/<código-da-coleção>.md`, regeneráveis quando os dados mudam.

## Critérios de aceite

- [x] Para uma coleção com dados no 17Lands, o guia traz os 10 arquétipos com win rate e
      rankings baseados em dados, com a data da coleta.
- [x] Os dados de cada modo (Premier, Quick, Traditional, Sealed) ficam separados e o
      guia diz de qual modo vem cada número.
- [x] Para uma coleção sem dados, o guia é gerado e se declara teórico.
- [x] Toda carta citada pertence à coleção (ou à sua folha bônus) na base local.
- [x] Dado um pool de 45 cartas, o deck montado tem 40 cartas válidas e base de mana conferida.

## Fora do escopo

- Overlay/integração em tempo real com o cliente do Arena.
- Cube.

## Questões em aberto

- Vale baixar os datasets públicos de partidas do 17Lands para análises que as páginas
  não dão (ordem de pick, arquétipos de três cores)? Seria o caso de reavaliar o
  armazenamento (ver plano da spec 001).
