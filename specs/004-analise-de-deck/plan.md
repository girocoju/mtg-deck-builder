# 004 — Plano

## Decisões

- **Tudo em `analysis.py`**, sem dependências: recebe um deck já resolvido
  (`decklist.resolve`) e devolve um dicionário serializável; `report()` gera o texto.
- **Números de Karsten como dados no código**, copiados de `knowledge/base-de-mana.md`
  (Parte 2): fórmulas de terrenos para 60, 80 e 99 cartas e a tabela de fontes por custo
  para 40/60/80/99. Para 40 cartas não há fórmula publicada: o padrão é 17 (16 a 18).
- **Tamanho de referência pelo total de cartas:** até 45 → 40; até 70 → 60; até 90 → 80;
  acima → 99.
- **Exigência de cor = carta mais exigente** de cada cor (não a soma), como manda a
  tabela. Cartas de ouro somam 1 ao requisito. Custos fora da tabela usam o vizinho mais
  exigente e saem marcados como aproximados.
- **Papéis por heurística de texto** (expressões regulares sobre o texto oracle). É
  simples, funciona offline e é testável; erra em cartas de redação incomum, por isso o
  relatório lista as cartas de cada papel no JSON para o agente corrigir. O bulk file
  `oracle_tags` do Scryfall (tags da comunidade) fica como melhoria futura: exigiria
  nova tabela e sincronização, e a heurística basta para os alertas desta spec.
- **Probabilidades pela hipergeométrica exata** (`math.comb`), mão de 7 sem mulligan.
  Simular mulligans fica fora: os valores são um piso conservador.

## Como cada caso é contado

| Caso | Regra |
| --- | --- |
| Comandante | Fora da curva e da média (não é comprado); entra na exigência de cor |
| Sideboard | Fora da análise |
| Carta de duas faces | Custo e tipo da face da frente |
| Split | Cada metade gera sua própria exigência de cor; valor de mana somado na curva |
| Custo X | X vale zero |
| Híbrido e Phyrexian | Contam como mana genérica (não exigem a cor) |
| MDFC mágica/terreno | Mágica na curva; 0,38 terreno se entra virado, 0,74 se não; 0,8 fonte da cor |
| Terreno que busca básico | Fonte das cores dos tipos citados, ou de todas as cores do deck |
| Terreno "entra virado" | Conta como fonte, mas não como fonte desvirada (turno 1) |
| Criatura de mana de custo ≤ 2 | 1/2 fonte; pedra de mana de custo ≤ 2: 3/4. Só para mágicas de custo ≥ 3 |
| Mágica barata de compra/ramp | Não-terreno de custo ≤ 2 que compra ou gera mana (reduz 0,28 terreno cada) |

## Alertas

- Terrenos fora da fórmula por mais de 2 (ou fora de 16–18 em 40 cartas).
- Fontes de uma cor abaixo da exigência da carta mais exigente.
- Quatro ou mais mágicas de 1 mana de uma cor com menos fontes desviradas que o exigido
  para custo `C`.
- Terrenos virados acima de um limite por tamanho (9 em 60 cartas).

## Limitações conhecidas

- Tesouros, ramp de custo 3 ou mais e cantrips não entram como fração de fonte.
- Terrenos condicionais ("entra virado a menos que...") são contados como desvirados.
- A classificação de papéis não distingue qualidade; "ameaça" é toda criatura ou planeswalker.
