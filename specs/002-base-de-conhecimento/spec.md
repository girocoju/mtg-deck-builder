# 002 — Base de conhecimento

**Status:** 📝 Especificada

## Objetivo

Manter uma base de conhecimento de deck building que o agente consulta ao construir e
justificar decks, e que **cresce com o tempo**: começa com o livro *Next Level Magic*
(Patrick Chapin, edição 2015, 433 páginas), recebe outras fontes (artigos, livros,
vídeos transcritos) e acumula o que for aprendido no uso do próprio deck builder.

## Histórias de uso

- Como agente, ao montar um deck, quero consultar rapidamente "como dimensionar a base de
  mana" ou "como se posicionar contra um meta agressivo" sem reler as fontes.
- Como usuário, quero que as explicações do deck builder citem o conceito usado e de onde
  ele veio.
- Como usuário, quero entregar um link, PDF ou texto e pedir "adicione isso à base de
  conhecimento".
- Como usuário, quero que correções e descobertas ("esse deck perdeu para X porque...",
  "essa recomendação estava errada") fiquem registradas e melhorem as próximas respostas.

## Requisitos

1. **Organização por tema, não por fonte.** `knowledge/` tem um documento por tema (base
   de mana, curva, arquétipos e papéis, vantagem de cartas e tempo, sideboard,
   metagame, ajuste de listas, limitado/draft, Commander/Brawl...). Cada fonte nova
   enriquece os documentos existentes em vez de criar um resumo isolado.
2. **Formato de cada documento:** conceito, quando se aplica, como usar na construção,
   exemplo e referências (fonte + capítulo/seção/URL). Em português, com palavras próprias.
3. **Registro de fontes** (`knowledge/fontes.md`): cada fonte com autor, data, tipo,
   onde está o original, o que foi aproveitado e em quais documentos.
4. **Fontes iniciais:**
   - *Next Level Magic* (Chapin) — a teoria geral;
   - artigos de Frank Karsten sobre base de mana (número de terrenos e de fontes por
     cor) — a referência numérica usada pela spec 004.
5. **Processo de ingestão repetível** para qualquer fonte nova (PDF, URL ou texto):
   extrair, destilar, integrar aos temas, registrar em `fontes.md`. Textos brutos ficam
   em `data/`, fora do git.
6. **Conflitos e data:** quando fontes divergem, o documento registra as duas posições e
   qual prevalece (em geral a mais recente ou a apoiada em dados). Conceitos que dependem
   de cartas, regras ou formatos de uma época são generalizados; exemplos datados ficam
   marcados como históricos.
7. **Aprendizado acumulado** (`knowledge/licoes/`): lições vindas do uso — feedback do
   usuário sobre decks gerados, resultados de partidas relatados, erros do agente.
   Cada lição tem data, contexto (formato, deck), o que foi aprendido e quando se aplica.
   Lições que se repetem são promovidas para o documento do tema.
8. **Índice** (`knowledge/README.md`) dizendo, para cada tipo de pedido (construído,
   anti-meta, Commander/Brawl, draft), quais documentos e lições ler.
9. Do livro, os temas de jogo técnico e mentalidade, que não afetam construção, entram
   como um resumo único, não em detalhe.

## Critérios de aceite

- [ ] Todo capítulo do livro está mapeado em `fontes.md` como "coberto em X" ou "fora do escopo".
- [ ] Os artigos de base de mana estão integrados ao tema, com tabelas de referência
      (terrenos por curva, fontes por custo colorido) para decks de 40, 60 e 100 cartas.
- [ ] Nenhum documento contém trechos longos copiados das fontes.
- [ ] Dado o pedido "por que 24 terrenos neste deck?", o agente encontra a resposta em
      `knowledge/` lendo no máximo dois arquivos.
- [ ] Uma fonte nova (um artigo por URL) é adicionada seguindo só o processo documentado.
- [ ] Um feedback do usuário sobre um deck vira uma lição registrada e é citado em um
      pedido posterior semelhante.

## Fora do escopo

- Busca semântica/embeddings (o índice em Markdown basta para este volume; reavaliar se
  a base crescer muito).
- Tradução ou reprodução integral de qualquer fonte.
