# 014 — Mapa de picks da coleção

**Status:** 🚧 Em andamento — código, testes e mapa de FRA gerados em 2026-11-08; falta calibrar com o primeiro draft real

## Objetivo

Antes do primeiro draft de uma coleção, ter pronto **o peso de cada carta e a relação entre
elas**, intrínsecos à coleção e aos dados de partidas, sem depender do draft em curso: a
ordem de pick geral e por raridade (o que se compara no P1P1), os melhores picks seguintes
dada qualquer sequência de escolhas (a árvore de escolhas, que começa quase sempre por uma
rara ou mítica), os elos diretos entre cartas (quem pede o que a outra oferece) e o grafo
que eles formam (quais cartas são hubs, que comunidades cruzam os dez pares).

Pedido do usuário em 2026-11-08, depois de testar o motor da spec 010 com um pacote: "para
cada coleção, [...] a gente tenha um peso para cada escolha de todas as cartas da coleção.
[...] construir uma árvore com todas as cartas da coleção para ver qual o melhor peso, qual
a melhor sinergia entre as escolhas para construir um bom deck de draft. [...] Isso tem que
estar pronto antes de eu iniciar o primeiro draft [...] tem que estar intrínseco na
coleção." E, na sequência: "Fazer uma análise de grafo seria uma das saídas? Assim a
correlação entre as cartas da coleção ficam mais acuradas?"

## Histórias de uso

- "Antes do draft de FRA, me dê o peso de cada carta da coleção, por raridade."
- "Peguei Ajani Unrelenting no P1P1. Qual a melhor segunda escolha entre todas as cartas
  da coleção? E neste pacote?"
- "Quais cartas da coleção mais combinam entre si? Que cartas são o centro de uma
  estratégia?"
- "Quais são as sinergias que não aparecem nos dez arquétipos oficiais?"
- (Agente, ao recomendar um pick) "Esta carta tem elo direto com duas das suas escolhas."

## Requisitos

1. **Peso por carta.** Para toda carta draftável da coleção: poder pelas fontes da spec 010
   (17Lands → Untapped → Draftsim → teórica, com a fonte declarada), arquétipos que serve,
   elos que pede e oferece, e a soma das sinergias diretas com o resto da coleção. Ordem de
   pick geral e por raridade. Raridade não entra na nota: entra porque cada pacote tem uma
   rara ou mítica, cerca de três incomuns e dez comuns, e por isso a comparação do P1P1 é
   "a rara do pacote contra a melhor incomum e a melhor comum", e a do P1P2 em diante,
   quase sempre, entre incomuns e comuns.
2. **Elos diretos.** Cada arquétipo da spec 010 é um elo em que a payoff pede e a enabler
   oferece; o arquivo de arquétipos pode declarar ganchos fora dos dez pares (fichas de
   criatura e quem as aproveita, planeswalkers e quem os pede, descarte). A sinergia entre
   duas cartas soma os elos em que uma pede o que a outra oferece, cada elo contado uma
   vez; duas payoffs do mesmo arquétipo dividem o plano e valem metade; enabler marcado só
   por estatística (qualquer criatura barata) vale um quarto; se as duas cartas juntas
   pedem três cores, só com splash, e o elo vale um quarto.
3. **Componente `parceiros` no motor.** `mtg draft pick` ganha um componente, visível na
   tabela, com a soma dos elos diretos entre a carta e cada carta já escolhida, com peso
   fixo e teto: um elo desempata cartas próximas e não transforma carta fraca em bomba.
   A linha diz com quais picks a carta tem elo.
4. **Árvore de escolhas.** Para qualquer sequência de picks, o ranking da coleção inteira
   como próximo pick, pelo motor (poder + parceiros + o que mais o pick já pesa). O mapa
   traz, para cada rara e mítica, os melhores segundos picks; os seguintes saem sob demanda
   (`--card A --card B ...`) ou ao vivo pelo Oráculo.
5. **Grafo de elos.** Cartas são nós, elos são arestas com peso. Centralidade (passeio
   aleatório que prefere parceiras fortes): quais cartas são as melhores portas de entrada
   para a coleção. Comunidades (propagação de rótulos sobre os elos plenos): agrupamentos
   que podem cruzar os dez pares oficiais. O mapa diz o que o grafo acrescenta e o que não:
   melhora o peso de cada carta (quem está do outro lado do elo), não a certeza de cada elo,
   que viria só de dados de co-ocorrência em partidas, que o 17Lands não publica.
6. **Documento e comando.** `mtg draft map <coleção>` com `--rarity`, `--card`, `--pairs`,
   `--graph`, `--top`, `--write` e `--json`; `--write` grava `drafts/<coleção>-mapa.md`
   completo (como ler, ordem por raridade, segundos picks, pares, arquétipos, grafo,
   limites), regenerável quando os dados mudarem.

## Critérios de aceite

- [x] Testes sem rede: elos (payoff pede, enabler oferece, gancho, genérico, splash, elo
      contado uma vez), componente `parceiros` com teto, ordem do mapa, pares, parceiros,
      próximos picks, centralidade, comunidades, documento.
- [x] `mtg draft map fra --write` gera o mapa com todas as cartas draftáveis e fonte por
      carta; o pacote de teste do usuário (P1P1 Ajani Unrelenting) mostra elos diretos com
      Compel Brutality, Warrior's Blades e Awaken the Inferno (registro em `tasks.md`).
- [ ] Depois do primeiro draft real: conferir se os elos indicados fizeram sentido no deck
      montado e ajustar pesos ou ganchos (registro em `tasks.md`).

## Dependências

Spec 010 (motor, arquétipos, fontes), 008 (dados do 17Lands), 001 (base).

## Fora do escopo

- Aprender os elos a partir de partidas (co-ocorrência): não há dado público.
- Simular a árvore inteira (14 × 3 picks sobre 280 cartas): a árvore é dada sob demanda,
  um nível por vez, pelo motor.
- Ajustar os pesos por otimização automática: os pesos ficam na tabela única da spec 010 e
  mudam por evidência registrada.

## Questões em aberto

- **Cobertura do 17Lands.** Em 2026-11-08 o 17Lands publica GIH WR só para 79 das 290
  cartas de FRA (nenhuma rara ou mítica), mesmo com intervalo de datas na consulta; o resto
  vem do Untapped (coleta de 2026-10-12, ranks bronze a platina) e da Draftsim. A fonte
  aparece em cada linha; o mapa deve ser regenerado quando o 17Lands voltar a publicar.
- **Calibração.** Os pesos de `parceiros` (0,6 por elo, teto 3,0), enabler genérico (0,25)
  e splash (0,25) são escolhas iniciais: decidir depois do primeiro draft real se um elo
  está pesando demais ou de menos.
