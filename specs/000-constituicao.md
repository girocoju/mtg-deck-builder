# 000 — Constituição

Princípios que toda spec, plano e resposta do deck builder devem respeitar.

## Visão

Um repositório que transforma o Claude Code em um deck builder especialista de
Magic: The Gathering. O usuário pede em linguagem natural — por exemplo:

- "Crie um deck anti meta no formato Standard"
- "Crie uma estratégia de drafts para a coleção Reality Fracture"
- "Me ajude a montar um deck do formato Brawl com o commander Ivy, Gleeful Spellthief"

— e o agente responde combinando três fontes: a **base de cartas** local, a **teoria**
de deck building e os **dados de metagame**.

## Princípios

1. **Carta citada é carta verificada.** Nenhuma carta entra em uma lista ou recomendação
   sem ter sido consultada na base local. Texto de regras, custo e legalidade vêm da base,
   nunca da memória do modelo.
2. **Lista entregue é lista válida.** Toda decklist final passa pelo validador do formato
   (tamanho, cópias, legalidade, identidade de cor) antes de ser mostrada.
3. **Teoria com fundamento.** Escolhas de construção são justificadas com os conceitos de
   `knowledge/` (papel do deck, curva, base de mana, vantagem de cartas, posicionamento no
   meta), e não com "é bom porque sim".
4. **Meta é dado com data.** Todo dado de metagame carrega fonte e data de coleta. Se o
   snapshot estiver velho ou não existir, o agente avisa e diz que a análise é teórica.
5. **Spec primeiro.** Funcionalidade nova começa por `specs/`. Ver [README](README.md).
6. **Simplicidade.** Python + SQLite, dependências mínimas, tudo reconstruível com um
   comando. Lógica determinística (validar, contar, filtrar) fica em código testado;
   julgamento (escolher, explicar) fica com o agente.
7. **Bom cidadão com as fontes.** Scryfall: bulk data em vez de milhares de requisições,
   `User-Agent` identificado, no máximo uma sincronização por dia. Demais sites: respeitar
   termos de uso e `robots.txt`, cache local, requisições espaçadas.
8. **Direitos autorais.** O PDF do livro não entra no git. A base de conhecimento contém
   conceitos destilados com palavras próprias e referência ao capítulo, nunca cópia do texto.

## Convenções

- **Idioma:** documentação, specs e respostas em português (PT-BR). Nomes de cartas,
  de formatos e o código em inglês.
- **Plataformas:** MTG Arena, Magic Online e papel. Toda lista pode ser exportada para as três.
- **Formatos:** os nomes canônicos são as chaves de legalidade do Scryfall (`standard`,
  `pioneer`, `modern`, `legacy`, `vintage`, `pauper`, `commander`, `brawl`,
  `standardbrawl`, `historic`, `timeless`, `alchemy`, ...). A lista não é fixa no código:
  vem da base a cada sincronização.
