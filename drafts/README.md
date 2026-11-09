# drafts/ — um documento por coleção

Cada coleção tem uma pasta com dois arquivos:

```
drafts/<código>/<código>.pdf   # o documento da coleção: o que se lê
drafts/<código>/guia.md        # fonte do guia de draft, escrito pelo agente (Markdown)
```

O **PDF é o documento único** da coleção (spec 014), gerado por
`mtg draft map <código> --pdf`: capa com números-chave e sumário; como ler; o guia de draft;
a coleção em números e a leitura; os pares nos dados (quando há); os dez arquétipos (visão
geral, payoffs e enablers em barras, listas completas); a ordem de pick por raridade (barras
e tabela completa); o grafo de elos, comunidades e centralidade; os pares com mais sinergia;
os segundos picks de todas as raras e míticas; limites e fontes.

O **guia em Markdown é só a fonte** da primeira parte: o agente o escreve e atualiza
(processo na skill `draft`, seção A; `drafts/fra/guia.md` é o modelo com dados,
`drafts/trk/guia.md` o modelo teórico) e depois regenera o PDF. Não é para ser lido no
lugar do PDF. Subconjunto de Markdown aceito pelo conversor (`src/mtg_builder/pdf_flow.py`):
títulos `#`, `##` (cada um vira uma página) e `###`, parágrafos, listas com `-` e `1.`,
tabelas `|`, blocos de código, `**negrito**`, `código` e links.

O mapa precisa de `src/mtg_builder/archetypes/<código>.json` (dez pares e ganchos). O
Markdown do mapa, se alguém quiser o texto puro, sai com `--write` em `data/maps/` (fora do
git). Os estados de draft ao vivo ficam em `data/drafts/` (fora do git).

Coleções: `fra/` Reality Fracture (dados do 17Lands e Untapped); `trk/` Star Trek (teórico
até o 17Lands publicar).
