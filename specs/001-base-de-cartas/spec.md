# 001 — Base de cartas

**Status:** ✅ Concluída

## Objetivo

Ter, localmente, a base completa de cartas de Magic — todas as cartas, impressões,
coleções, legalidades por formato e rulings — consultável offline e rápida o bastante
para o agente fazer dezenas de buscas por pedido.

## Histórias de uso

- Como agente, quero buscar "criaturas lendárias legais em Brawl com identidade GU" para
  propor cartas reais a um deck.
- Como agente, quero o texto oracle, o custo e a legalidade exatos de uma carta pelo nome.
- Como agente, quero listar as cartas de uma coleção por raridade para avaliar um draft.
- Como usuário, quero atualizar a base com um único comando quando sair coleção nova.

## Requisitos

1. **Fonte:** bulk data do Scryfall (`default_cards` e `rulings`) e o endpoint `/sets`.
2. **Sincronização** com um comando (`mtg sync`), que não baixa nada se a base já está
   em dia com o Scryfall, e que pode ser repetida sem duplicar dados.
3. **Conteúdo por carta:** nome, custo, valor de mana, tipo, texto oracle, cores,
   identidade de cor, palavras-chave, P/R, lealdade, faces (cartas dupla-face, split,
   adventure), rank EDHREC e legalidade em todos os formatos que o Scryfall informa.
4. **Conteúdo por impressão:** coleção, número, raridade, data, onde existe (papel,
   Arena, MTGO), se sai em booster e preços (USD, EUR, tix).
5. **Consulta** por: nome, texto (full-text), tipo, cores, identidade de cor, formato,
   coleção, raridade, plataforma e valor de mana — combináveis entre si.
6. Tokens, emblemas e cartas de arte ficam na base, mas fora das buscas por padrão.
7. Saída legível para humanos e em JSON para ferramentas; consulta SQL somente leitura
   como válvula de escape.

## Critérios de aceite

- [x] `mtg sync` em uma máquina limpa cria a base; uma segunda execução informa "já atualizado".
- [x] `mtg card "Ivy, Gleeful Spellthief"` mostra texto, identidade GU e legalidade em `brawl`.
- [x] `mtg search --format brawl --identity GU --type "legendary creature"` retorna só
      cartas que atendem aos três filtros.
- [x] `mtg sets "<nome ou código>"` encontra a coleção e mostra a contagem por raridade.
- [x] Cartas dupla-face têm custo, cores e texto preenchidos.
- [x] Testes automatizados cobrem ingestão e filtros sem acessar a rede.

## Fora do escopo

- Imagens das cartas (só guardamos a URL).
- Cartas em outros idiomas além da impressão padrão do Scryfall.
- Histórico de preços.
