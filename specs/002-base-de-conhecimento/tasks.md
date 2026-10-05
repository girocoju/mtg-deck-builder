# 002 — Tarefas

- [x] Extrator de PDF (`scripts/extract_pdf.py`) e extração do livro (433 páginas)
- [x] Destilação do livro por bloco, lendo todas as páginas:
  - [x] p. 6–83 → metodo-quatro-perspectivas, atalhos-de-construcao, preparacao-e-metagame
  - [x] p. 84–177 e 273–320 → jogo-mental-e-mentalidade (resumo único)
  - [x] p. 178–229 → fases-do-jogo, valor-das-cartas, vantagem-de-cartas-e-tempo, mulligan
  - [x] p. 230–272 → sideboard, base-de-mana (princípios), quantidade-de-copias, papel-no-jogo
  - [x] p. 321–354 → arquetipos (com relações entre arquétipos e roteiro anti-meta)
  - [x] p. 29–31 e 355–433 → limitado-e-draft, glossario
- [x] Trechos de construção encontrados nos capítulos de times/mentalidade integrados aos temas
- [x] Artigos de Frank Karsten (7 artigos, 2017–2024) lidos na fonte e registrados
- [x] Fusão em um único `base-de-mana.md` (princípios + números, com regra de precedência)
- [x] Índice (`knowledge/README.md`), registro de fontes (`fontes.md`), processo
      (`COMO-ADICIONAR.md`) e estrutura de lições (`licoes/`)
- [x] Verificador de cópia (`scripts/check_copy.py`)
- [ ] Ingerir uma fonte nova seguindo só o `COMO-ADICIONAR.md` (valida o processo)
- [ ] Registrar a primeira lição a partir de feedback real e usá-la em um pedido posterior

## Verificação (2026-10-04)

- **Cobertura:** todos os capítulos do livro estão mapeados em `knowledge/fontes.md`.
- **Cópia:** `check_copy.py next-level-magic 8` só aponta títulos de capítulos (no mapa de
  `fontes.md`), os nomes das quatro perspectivas e uma frase curta citada em
  `vantagem-de-cartas-e-tempo.md`. Nenhum trecho do livro reproduzido.
- **Links:** nenhuma referência quebrada entre os documentos.
- **"Por que 24 terrenos?":** `knowledge/README.md` → `base-de-mana.md` ("Resposta rápida").
- **Cartas citadas:** conferidas na base com `mtg card` pelos autores de cada documento.

## Ressalvas registradas nos documentos

- A revisão de conteúdo foi por amostragem e por verificações automáticas; os documentos
  não foram relidos um a um contra o livro por uma segunda leitura.
- Números de Karsten: custos fora da tabela-resumo, quatro tabelas em imagem e a fórmula
  de terrenos para 40 cartas estão como "não verificado" ou "calculado".
- O artigo de land drops (2017) foi lido em cópia de terceiros e usa a regra antiga de mulligan.
- Alguns documentos passaram do tamanho planejado (arquetipos, base-de-mana, limitado-e-draft).
- Lacunas: teoria própria de Commander/Brawl, terrenos utilitários, BO1 do Arena.

## Efeito colateral na spec 001

- Faltava índice em `legalities(oracle_id)`: consultas por carta varriam a tabela toda. Criado.
- `mtg card "Savage Lands"` falhava por haver uma carta homônima de layout `front_card`;
  layouts `front_card`, `planar`, `scheme` e `vanguard` saíram das buscas padrão.
