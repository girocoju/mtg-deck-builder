# 005 — Plano

## Decisões

- **MTGGoldfish por leitura de HTML**, com a biblioteca padrão (`urllib` + expressões
  regulares): a página `/metagame/<formato>/full` lista os arquétipos com a fatia do
  meta, e a página de cada arquétipo traz a lista de referência em um campo do
  formulário. O `robots.txt` do site foi conferido em 2026-10-04: essas páginas são
  permitidas; os caminhos `/deck/download*` são proibidos e não são usados.
- **Comportamento de bom cidadão:** `User-Agent` identificado com o endereço do projeto,
  2 segundos entre requisições, só as 12 listas principais por padrão, e no máximo uma
  coleta por formato a cada 24 horas (a não ser com `--force`).
- **Untapped.gg sem coleta automática.** Verificado em 2026-10-04: a página do meta não
  traz os dados no HTML (vêm de uma API interna, sem documentação pública), o acesso
  automatizado simples recebe 403, o `robots.txt` restringe as páginas de decks e parte
  dos dados é exclusiva do plano pago. Usar a API interna seria contornar essas
  restrições. O caminho adotado é a **importação manual de CSV**.
- **BO1 e BO3 em pastas separadas** (`data/meta/<formato>/bo1|bo3/`). O MTGGoldfish só
  alimenta BO3. `mtg meta show` mostra os dois e diz explicitamente quando um não existe.
- **Snapshots imutáveis por dia e fonte** (`<data>-<fonte>.json`), em `data/` (fora do
  git): o histórico fica para comparar a evolução do meta.
- **Listas conferidas com a base:** cada lista de referência passa por
  `decklist.resolve`; cartas não encontradas ficam registradas no snapshot. A análise da
  spec 004 anexa valor de mana médio, terrenos, criaturas e papéis a cada arquétipo.
- **Macroarquétipo por heurística:** pelo nome quando ele diz (control, midrange, aggro,
  landfall...), senão pelo número de criaturas e pela curva. É aproximação declarada; a
  classificação fina é julgamento do agente com `knowledge/arquetipos.md`.
- **Aviso de validade:** snapshot com mais de 14 dias sai marcado no relatório.

## Estrutura

```
src/mtg_builder/meta.py   coleta, importação, resumo, relatório
src/mtg_builder/cli.py    mtg meta update | show | import
tests/test_meta.py        sem rede (página e site simulados)
data/meta/<formato>/<modo>/<data>-<fonte>.json
```

## Formato do CSV de importação

```csv
archetype,share,winrate,games
Mono-Red Aggro,12.5%,55.1,18400
Dimir Midrange,9.8%,53.0,14200
```

`winrate` e `games` são opcionais. Com `--decks <pasta>`, um arquivo
`<nome do arquétipo>.txt` na pasta vira a lista de referência daquele arquétipo.

## Riscos

- **Mudança de layout do MTGGoldfish:** a coleta falha com mensagem clara ("o layout da
  página pode ter mudado") e o snapshot anterior continua valendo.
- **Uma lista por arquétipo** não representa as variações; o resumo de cartas mais
  jogadas é aproximado e cobre só os arquétipos com lista (cerca de 75% do meta com 12).
- **Fatia do meta não é win rate:** o MTGGoldfish mede presença em resultados, não taxa
  de vitória. Matriz de confrontos continua fora do escopo.
