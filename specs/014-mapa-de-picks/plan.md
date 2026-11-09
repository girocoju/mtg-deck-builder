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
  desempate a favor do rótulo atual e depois alfabético), só sobre arestas com mais de um
  elo, até 30 iterações; grupos com 3 cartas ou mais, com cores, pares oficiais e elos
  dominantes. Sobre todos os elos o grafo é denso demais e vira um grupo só. O limiar é
  escolhido por `communities_auto` entre 1,5, 2,0 e 2,5: fica o que dá mais grupos (empate:
  o menor). Em FRA fica 1,5 (quatro grupos); em TRK, com oito ganchos, 1,5 dá um grupo de
  135 cartas e 2,0 dá nove.
- **Leitura da coleção** (`SetMap.overview`, `archetype_summary`, `hook_summary`,
  `analysis_lines`): mesma leitura de `draft.set_overview`, mas sobre o conjunto do mapa;
  frases em PT-BR com a seção da teoria citada; profundidade de arquétipo por payoffs em
  comum e incomum (`DEPTH_DEEP` = 6, `DEPTH_SHALLOW` = 3); indício de velocidade pela
  parcela das criaturas de comum e incomum até custo 3 (`CURVE_SPLIT` = 65% / 50%). Entra
  como seção 0 do Markdown e como páginas 2 e 3 do PDF.
- **PDF** (`draft_map_pdf.py`, matplotlib em modo Agg, dependência opcional `viz`): A4
  paisagem, Segoe UI com DejaVu Sans de reserva, fontes TrueType incorporadas. Paleta
  (skill dataviz, validador rodado): W `#eda100`, U `#2a78d6`, B `#7b3fa0`, R `#e34948`,
  G `#008300`, incolor cinza neutro; multicolorida é barra ou nó dividido, sem "dourado"
  (o dourado colide com amarelo e vermelho no validador). Pior par verde↔vermelho fica na
  faixa que exige codificação secundária, por isso todo rótulo traz a letra da cor.
  Raridade usa uma rampa ordinal de uma matiz; comunidades usam a paleta categórica de oito
  cores. Grafo: Fruchterman-Reingold com pesos em numpy (atração cresce com o quadrado do
  peso acima de 0,75, para que um elo só puxe pouco), só arestas de peso ≥ 1 desenhadas,
  rótulos nas mais centrais sem sobreposição. Duas colunas de 20 barras por página na
  ordem de pick; duas arquétipos por página; 19 a 20 páginas, 20 a 25 s.
- **Documento único por coleção** (pedido do usuário em 2026-11-09: "os arquivos em .md
  ficaram horríveis para leitura. Incorpore nos mapas em .pdf de cada coleção [...]
  centralizar tudo num mesmo doc de coleção [...] organizar por pastas"): a pasta
  `drafts/<coleção>/` tem `guia.md` (fonte do guia, Markdown escrito pelo agente) e
  `<coleção>.pdf` (o que se lê). O Markdown do mapa (`markdown()`) passa a uso interno em
  `data/maps/`, fora do git, e os `*-mapa.md` saíram do repositório.
- **Conversor de Markdown** (`pdf_flow.py`): títulos (`##` vira página, `###` em linha),
  parágrafos, listas, tabelas que quebram entre páginas repetindo o cabeçalho, blocos de
  código, negrito e código em linha com medida real do texto (renderizador do matplotlib,
  com cache) para a quebra de linha; as páginas são planejadas antes de desenhar, por isso a
  capa traz o sumário com números de página. Colunas de tabela recebem largura proporcional
  ao conteúdo, entre 5,5% e 42% da página. Testes com uma medida aproximada por caracteres.
- **Estrutura do PDF:** capa (números-chave e sumário em duas colunas), como ler, guia (uma
  seção por página), coleção em números, leitura, pares nos dados, arquétipos (visão geral,
  barras duas a duas, listas completas), ordem de pick (barras das 40 melhores e tabela
  completa por raridade), grafo, comunidades, centralidade, 40 pares, segundos picks de
  todas as raras e míticas, limites. FRA: 63 páginas, 108 s (a medida de texto do guia é a
  parte lenta).

## Arquivos

- `src/mtg_builder/archetypes.py`: `links`, `link_scores`, `synergy`, `links_between`,
  `label_links`; constantes `SHARED_PAYOFF`, `SPLASH_FACTOR`, `GENERIC_ENABLER`.
- `src/mtg_builder/archetypes/fra.json`: bloco `hooks`.
- `src/mtg_builder/draft_pick.py`: pesos `parceiro` e `parceiros_max`, componente na
  `rank`, coluna `parc` na tabela, cache de `functions` por nome.
- `src/mtg_builder/draft_map.py`: módulo novo; `overview`, `archetype_summary`,
  `hook_summary`, `communities_auto`, `analysis_lines`.
- `src/mtg_builder/draft_map_pdf.py`: PDF.
- `src/mtg_builder/archetypes/trk.json`: dez pares e oito ganchos de Star Trek.
- `src/mtg_builder/cli.py`: `mtg draft map` (`--pdf`).
- `pyproject.toml`: extra `viz` (matplotlib).
- `tests/test_draft_map.py`, `tests/test_archetypes.py` (arquivos reais compilam).
- `src/mtg_builder/pdf_flow.py`: Markdown → páginas (texto corrido e tabelas).
- `drafts/README.md`; `drafts/fra/guia.md` e `drafts/fra/fra.pdf`; `drafts/trk/guia.md` e
  `drafts/trk/trk.pdf` (PDFs gerados; `.gitignore` libera `drafts/*/*.pdf`).
- `tests/test_pdf_flow.py`.

## Riscos

- Os padrões de texto marcam pertencimento, não qualidade: um elo entre duas cartas fracas
  continua fraco (o poder manda; o teto do componente garante).
- A fonte de poder de raras e míticas em FRA é o Untapped de 2026-10-12, não o 17Lands:
  notas podem estar infladas (Ajani Unrelenting 70,8% no Untapped). O mapa declara a fonte
  por linha.
- Grafo denso: a centralidade favorece quem pede e oferece muitos elos (planeswalkers que
  criam fichas). É o comportamento esperado, e o documento explica o que a medida diz.
