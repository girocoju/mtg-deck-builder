# 014 — Plano

## Decisões

- **Elos saem dos arquétipos já marcados** (`src/mtg_builder/archetypes/<coleção>.json`),
  sem um segundo vocabulário: payoff de um par *pede* o par, enabler *oferece*. Ganchos
  (`hooks`) no mesmo arquivo cobrem o que cruza os pares: `fichas` (quem cria fichas de
  criatura ↔ quem quer muitas criaturas, equipamentos, auras, sacrifício), `planeswalker`
  (planeswalkers de verdade ↔ quem pede um em jogo; a ficha de Jace já é o elo UG) e
  `descarte`. Cada gancho tem `needs`, `provides` e `weight`.
- **Pesos dos elos** (`archetypes.py`): quem pede pesa 1 (payoff) ou o peso do gancho; quem
  oferece pesa 1, ou `GENERIC_ENABLER` = 0,25 quando só um padrão `stat:` a marca (criatura
  de custo 2, criatura grande: qualquer corpo serve, não é sinergia). `link_scores(a, b)`
  conta cada elo uma vez (máximo entre as duas direções); `SHARED_PAYOFF` = 0,5 para duas
  payoffs do mesmo par; `synergy()` soma e aplica `SPLASH_FACTOR` = 0,25 quando a união das
  cores passa de duas. Antes desse ajuste, Ajani Unrelenting somava 164 unidades de elo e
  as comunidades viravam um grupo só de 262 cartas.
- **Componente `parceiros`** (`draft_pick.py`): `WEIGHTS["parceiro"]` = 0,6 ponto por
  unidade de elo com cada pick feito, teto `parceiros_max` = 3,0, sem escalar pelo
  compromisso (um elo é informação concreta desde o pick 2). A linha guarda `elos`
  (até três picks com elo e o valor), mostrados como `↔ Carta 1.5`.
- **Mapa** (`draft_map.py`): `SetMap` monta uma entrada por carta draftável (lista do
  17Lands quando há snapshot, senão impressões de booster, senão todas; sem básicos), a
  matriz de pares (uma vez, ~6.500 pares em FRA, 2,5 s para o documento inteiro),
  `pick_order`, `partners`, `follow_ups` (o motor da spec 010 sobre a coleção inteira, com
  os picks dados no estado), `tree` (raras e míticas → melhores segundos picks),
  `archetype_tables`, `centrality` e `communities`.
- **Centralidade:** PageRank com pesos sobre o grafo não dirigido, amortecimento 0,85, em
  que o passeio escolhe a parceira com chance proporcional ao peso do elo vezes a força da
  parceira (poder + 5, mínimo 0,5). Escala 0–100. Carta sem elo fica no mínimo
  (1 − d)/N. Escolhido no lugar de autovetor puro porque este zera tudo fora da componente
  densa.
- **Comunidades:** propagação de rótulos assíncrona e determinística (ordem alfabética,
  desempate a favor do rótulo atual e depois alfabético), só sobre arestas de peso ≥ 1
  (elos plenos), até 30 iterações; grupos com 3 cartas ou mais, com cores, pares oficiais
  e elos dominantes. Sobre todos os elos o grafo é denso demais e vira um grupo só.
- **Documento** `drafts/<coleção>-mapa.md`: cabeçalho (geração, dados, cobertura por fonte,
  como ler, como o motor combina), 1 ordem por raridade, 2 segundos picks por rara e
  mítica (6 cada), 3 pares (40), 4 arquétipos (payoffs e enablers por poder), 5 grafo
  (25 mais centrais e comunidades), limites. ~1.200 linhas; o agente lê por seção.

## Arquivos

- `src/mtg_builder/archetypes.py`: `links`, `link_scores`, `synergy`, `links_between`,
  `label_links`; constantes `SHARED_PAYOFF`, `SPLASH_FACTOR`, `GENERIC_ENABLER`.
- `src/mtg_builder/archetypes/fra.json`: bloco `hooks`.
- `src/mtg_builder/draft_pick.py`: pesos `parceiro` e `parceiros_max`, componente na
  `rank`, coluna `parc` na tabela, cache de `functions` por nome.
- `src/mtg_builder/draft_map.py`: módulo novo.
- `src/mtg_builder/cli.py`: `mtg draft map`.
- `tests/test_draft_map.py`.
- `drafts/fra-mapa.md` (gerado).

## Riscos

- Os padrões de texto marcam pertencimento, não qualidade: um elo entre duas cartas fracas
  continua fraco (o poder manda; o teto do componente garante).
- A fonte de poder de raras e míticas em FRA é o Untapped de 2026-10-12, não o 17Lands:
  notas podem estar infladas (Ajani Unrelenting 70,8% no Untapped). O mapa declara a fonte
  por linha.
- Grafo denso: a centralidade favorece quem pede e oferece muitos elos (planeswalkers que
  criam fichas). É o comportamento esperado, e o documento explica o que a medida diz.
