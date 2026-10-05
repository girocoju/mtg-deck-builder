# 004 — Tarefas

- [x] Hipergeométrica e `mtg odds`
- [x] Curva por valor de mana (criaturas e outras) e valor de mana médio
- [x] Contagem de terrenos (com MDFCs fracionadas) e recomendação pela fórmula
- [x] Exigência por cor (tabela de Karsten) e contagem de fontes
- [x] Papéis por heurística de texto
- [x] Alertas e relatório em texto e JSON (`mtg deck analyze`)
- [x] Parâmetros para 40, 60, 80 e 99 cartas
- [x] Testes sem rede (10 testes em `tests/test_analysis.py`)
- [x] Verificação com a base real
- [ ] Melhoria futura: papéis a partir do bulk `oracle_tags` do Scryfall

## Verificação (2026-10-04)

- Suíte completa: 40 testes passando.
- **Referência de probabilidade:** 4 cópias em 60 até o turno 4 = 52,8%, e duas ou mais
  = 12,6%, iguais aos valores publicados por Karsten.
- **Contagem manual:** curva, média e fórmula conferidas em lista de teste com números
  calculados à mão.
- **Alerta de cor:** deck de duas cores com 6 fontes azuis para um custo `1UU` gera o
  alerta "18 fontes recomendadas".
- **Base real, deck de Brawl (Ivy):** a análise apontou 35 terrenos contra 32
  recomendados e 23 fontes azuis para Counterspell, que pede 30 em 99 cartas. A lista foi
  corrigida a partir desses alertas.
- **Base real, Standard mono-red:** 22 terrenos contra 21,5 recomendados; sem alertas.
