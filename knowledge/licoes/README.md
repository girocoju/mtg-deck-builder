# Lições

Aprendizado acumulado no uso do deck builder: o que o feedback do usuário, os resultados
de partidas e os erros do agente ensinaram. Antes de atender um pedido, o agente lê as
lições do formato ou tema envolvido. Processo em [COMO-ADICIONAR.md](../COMO-ADICIONAR.md).

## Índice

| Data | Lição | Formato / tema | Situação |
| --- | --- | --- | --- |
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
