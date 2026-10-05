---
name: deck-comandante
description: Constrói ou melhora um deck singleton com comandante — Commander (papel/MTGO, 100 cartas), Brawl (Arena, 100 cartas) ou Standard Brawl (Arena, 60 cartas). Use quando o usuário pedir um deck de Commander, EDH ou Brawl, citar um comandante ("me ajude a montar um deck de Brawl com o commander X"), pedir sugestões de comandante para uma estratégia, ou quiser melhorar um deck pré-construído. Não use para formatos de 60 cartas sem comandante nem para draft.
---

# Deck builder de Commander e Brawl

Siga as etapas na ordem. Ferramentas em `.venv\Scripts\mtg` (ver `CLAUDE.md`). Leia antes
`knowledge/commander-e-brawl.md` — ele traz as diferenças entre os formatos, as
proporções por categoria, os Brackets e o método de upgrade — e as lições do formato em
`knowledge/licoes/README.md`.

## 1. Entender o pedido

Extraia: **comandante** (um ou dois), **formato** (`commander`, `brawl`, `standardbrawl`),
**plataforma** e restrições (orçamento, nível de poder, tema).

- Em Brawl, pergunte ou assuma se é fila casual ou ranqueada (`competitivebrawl`).
- Em Commander, proponha o **bracket** alvo (1 a 5) se o usuário não disser; sem
  indicação, mire o bracket 2 ou 3 e diga isso.
- Se o pedido for "que comandantes combinam com X?", busque na base
  (`mtg search --format <formato> --type "legendary creature" --text ... --order edhrec`),
  apresente de 3 a 5 opções com o porquê e espere a escolha.
- Pedido no modo "me ajude a montar": apresente a direção (etapa 3) e confirme com o
  usuário antes de fechar a lista. Pedido direto ("monte"): siga até o fim e entregue.

## 2. Conferir o comandante

`mtg commander "<nome>" [--partner "<nome>"] --format <formato>`

Se for inválido, **pare e explique o motivo** que o comando deu (não é lendária, não é
legal no formato, a dupla não tem partner...). Ofereça alternativas: outro formato em que
a carta é válida, ou comandantes parecidos que sejam legais. Leia o texto com `mtg card`.

## 3. Analisar o comandante e definir o plano

Responda por escrito, antes de escolher cartas:

- o que o comandante faz e que tipo de carta o alimenta;
- como o deck vence **com** ele e o que faz **sem** ele (plano B);
- que categorias ele dispensa ou exige a mais (um comandante que compra cartas dispensa
  parte da compra; um que precisa sobreviver exige proteção).

## 4. Coletar candidatas

- **EDHREC:** `mtg edhrec "<nome>" --format <formato> --game <plataforma>` (sinergia,
  inclusão, papéis; já filtrado pela base) e `--average` para o deck médio, que serve de
  **modelo de partida** em Commander de papel. Cite a fonte e a data da coleta.
  O EDHREC mede Commander de mesa: em Brawl, prefira as cartas baratas e descarte as que
  só rendem com vários oponentes.
- **Busca própria:** `mtg search --format <formato> --identity <cores> --game <plataforma>`
  com `--text` e `--type`, para achar o que o EDHREC não mostra: cartas novas, exclusivas
  do Arena, e tudo o que falta quando o filtro do formato derruba a maior parte das
  sugestões (caso típico de Standard Brawl).
- Se o EDHREC estiver indisponível ou não tiver a página, trabalhe só com a base e diga isso.

## 5. Montar por categorias

Use a tabela de proporções de `knowledge/commander-e-brawl.md` (seção 3), ajustada ao
comandante e ao tamanho do deck. Singleton pede redundância por função
(`knowledge/quantidade-de-copias.md`).

- **Brawl** (um contra um, 25 de vida): curva mais baixa, mais remoção pontual, pouca ou
  nenhuma remoção em massa em decks proativos.
- **Commander:** conte os Game Changers
  (`mtg sql "SELECT name FROM cards WHERE game_changer = 1"`) e confira o bracket alvo:
  nenhum nos brackets 1 e 2, até 3 no bracket 3; veja também turnos extras, combos de
  duas cartas e negação de terrenos.
- Salve em `decks/<formato>/<comandante>.md` (modelo em `decks/README.md`).

## 6. Base de mana e conferência

`mtg deck analyze <arquivo>`:

- terrenos pela fórmula de Karsten (o relatório mostra o recomendado); fontes por cor
  pela carta mais exigente. Custos com dois ou três símbolos da mesma cor são caros em
  100 cartas: troque a carta ou aceite o alerta com justificativa;
- a seção "Proporções de referência" compara as categorias com as metas. Cada item
  "abaixo" ou "acima" precisa ser corrigido ou **justificado na entrega**. A contagem é
  por texto das cartas e não enxerga o comandante: se ele é o motor de compra, diga isso.

## 7. Validar

`mtg deck validate <arquivo> --format <formato> --game <plataforma>` até passar: tamanho
exato, cópia única, identidade de cor, legalidade, disponibilidade na plataforma.

## 8. Entregar

1. lista exportável (`mtg deck export --to arena|mtgo|text`), por categoria no texto;
2. plano de jogo, como o deck vence e o plano B;
3. principais sinergias e combos, explicados;
4. proporções por categoria e os desvios justificados;
5. em Commander: bracket pretendido e Game Changers; em Brawl: fila casual ou ranqueada;
6. fraquezas;
7. custo (`mtg deck cost`);
8. fonte e data dos dados do EDHREC;
9. honestidade: proposta não testada; o que observar nos testes.

Para **melhorar um deck existente**, use o método da seção 5 de
`knowledge/commander-e-brawl.md`: diagnostique com `mtg deck analyze` e com as sete
perguntas antes de sugerir trocas. Registre o retorno do usuário como lição.
