# 002 — Plano

## Decisões

- **Markdown puro em `knowledge/`**, um arquivo por tema, lido diretamente pelo agente.
  Sem banco, sem embeddings: o volume (algumas dezenas de páginas) não justifica.
- **Extração de PDF com `pypdf`** (`scripts/extract_pdf.py`), um arquivo de texto por
  página em `data/fontes/<nome>/`, fora do git. Página do arquivo = página citada nas
  referências.
- **Destilação por seção do livro, em paralelo.** O livro (433 páginas) é dividido em
  blocos; cada bloco é lido por inteiro e vira um ou mais documentos temáticos.
- **Base de mana em um único documento**, fundindo os princípios do livro com os números
  dos artigos de Frank Karsten. Quando divergem, prevalecem os números de Karsten (mais
  recentes e baseados em simulação), e o documento diz isso.
- **Números só da fonte.** Tabelas e fórmulas são registradas apenas quando lidas
  diretamente no original; o que não pôde ser conferido fica marcado como não verificado.
- **Atualizações posteriores às fontes** (London mulligan, BO1 no Arena, formatos
  singleton) entram como notas explicitamente marcadas, separadas do que a fonte diz.

## Estrutura

```
knowledge/
  README.md       índice: que documentos ler para cada tipo de pedido
  fontes.md       registro de fontes e mapa capítulo → documento
  COMO-ADICIONAR.md   processo para ingerir uma fonte nova e registrar lições
  <tema>.md       um documento por tema
  licoes/         aprendizado acumulado no uso (uma lição por arquivo)
scripts/extract_pdf.py
data/fontes/      textos brutos (fora do git)
```

## Divisão do livro

| Páginas | Conteúdo | Documentos |
| --- | --- | --- |
| 6–83 | Introdução, atalhos, quatro perspectivas | método, atalhos de construção, preparação e metagame |
| 84–177, 273–320 | Times, mentalidade, jogo mental | resumo único |
| 178–229 | Fases do jogo, valor das cartas, card advantage, tempo, mulligan | quatro documentos |
| 230–272 | Sideboard, base de mana, número de cópias, papel no jogo, combo | quatro documentos |
| 321–359 | Arquétipos | um documento, com roteiro anti-meta |
| 360–433 | Draft, conclusão, glossário | limitado e draft, glossário |

## Riscos

- **Direitos autorais:** revisão final procurando trechos copiados; só conceitos reescritos.
- **Conteúdo datado (2015):** exemplos marcados como históricos; regras que mudaram anotadas.
- **Artigos fora do ar ou bloqueados:** usar hospedagem alternativa ou Web Archive e
  registrar de onde veio cada número.
