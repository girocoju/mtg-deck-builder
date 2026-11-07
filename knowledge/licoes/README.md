# Lições

Aprendizado acumulado no uso do deck builder: o que o feedback do usuário, os resultados
de partidas e os erros do agente ensinaram. Antes de atender um pedido, o agente lê as
lições do formato ou tema envolvido. Processo em [COMO-ADICIONAR.md](../COMO-ADICIONAR.md).

## Índice

| Data | Lição | Formato / tema | Situação |
| --- | --- | --- | --- |
| 2026-10-14 | [Sphinx's Approach v7: 1 vitória, 1 derrota; Deadly Cover-Up é o contra absoluto](2026-10-14-sphinxs-approach-bo1-v7-cover-up.md) | Standard, BO1, Arena | ativa (combo puro 4–1) |
| 2026-10-14 | [Sphinx's Approach v6: fichas de Black Mage venceram na primeira partida](2026-10-14-sphinxs-approach-bo1-vitoria-black-mages.md) | Standard, BO1, Arena | ativa (3 vitórias seguidas) |
| 2026-10-14 | [Sphinx's Approach: a vitória pelo Fblthp ignora o total de vida do oponente](2026-10-14-sphinxs-approach-bo1-vitoria-fblthp.md) | Standard, BO1, Arena | ativa (2 vitórias seguidas) |
| 2026-10-14 | [Sphinx's Approach: primeira vitória veio com o combo puro](2026-10-14-sphinxs-approach-bo1-primeira-vitoria.md) | Standard, BO1, Arena | ativa (1 vitória) |
| 2026-10-14 | [Sphinx's Approach em BO1: três derrotas em três; deck de turno 6 em formato de turno 5](2026-10-14-sphinxs-approach-bo1-tres-derrotas.md) | Standard, BO1, Arena | ativa (3 partidas, 0 vitórias) |
| 2026-10-14 | [Sphinx's Approach: moer o próprio cemitério alimenta o Reanimator](2026-10-14-sphinxs-approach-bo1-reanimator.md) | Standard, BO1, Arena | ativa (hipótese, 1 partida) |
| 2026-10-14 | [Sphinx's Approach em BO1: derrota para Mono-Green Landfall, pouca remoção na mão](2026-10-14-sphinxs-approach-bo1-primeira-partida.md) | Standard, BO1, Arena | ativa (hipótese, 1 partida) |
| 2026-10-13 | [Abzan Ral Combo em BO1: versão otimizada montou o motor completo no primeiro teste](2026-10-13-abzan-ral-combo-bo1-primeiro-teste.md) | Standard, BO1, Arena | ativa (hipótese, 1 partida documentada) |
| 2026-10-05 | [Boros Tokens em BO1: 1–3 no primeiro teste, duas derrotas para decks brancos](2026-10-05-boros-tokens-bo1-primeiro-teste.md) | Standard, BO1, Arena | ativa (hipótese, 4 partidas) |
| 2026-10-04 | [Sideboard em BO1 no Arena é de até 15 cartas](2026-10-04-sideboard-bo1-arena.md) | Arena, BO1, todos os formatos de 60 | ativa |

## Modelo

Arquivo `AAAA-MM-DD-assunto-curto.md`:

```markdown
# <a lição em uma frase>

- **Data:** AAAA-MM-DD
- **Origem:** feedback do usuário | resultado de partidas | erro do agente | observação
- **Contexto:** formato, modo (BO1/BO3, tipo de draft), deck ou coleção, arquivo do deck se houver
- **Situação:** ativa | promovida para <documento> | superada

## O que aconteceu
O fato, com os dados disponíveis (quantas partidas, contra o quê).

## O que aprendemos
A conclusão, separando o que é evidência do que é hipótese.

## Quando se aplica
Em que pedidos futuros o agente deve lembrar disso, e quando NÃO generalizar.
```

Uma lição apoiada em poucas partidas é uma hipótese: registre o tamanho da amostra.
