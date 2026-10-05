# 004 — Análise de deck

**Status:** ✅ Concluída

## Objetivo

Dar ao agente números objetivos sobre uma lista — curva, cores, base de mana, composição —
para que ajustes e diagnósticos partam de medidas, não de impressão.

## Histórias de uso

- Como agente, depois de montar uma lista, quero conferir se a base de mana sustenta os
  custos coloridos antes de entregá-la.
- Como usuário, quero colar meu deck e receber um diagnóstico: pontos fracos e trocas sugeridas.

## Requisitos

1. **Curva de mana:** distribuição por valor de mana, separada por criaturas e não-criaturas.
2. **Cores:** símbolos de mana por cor nos custos versus fontes de cada cor nos terrenos
   e demais produtores de mana.
3. **Base de mana:** número de terrenos recomendado para a curva e fontes necessárias por
   cor para conjurar as mágicas no turno esperado, com a referência usada (ver spec 002).
4. **Composição por papel:** contagem de ameaças, remoções, compra/vantagem de cartas,
   aceleração, interação, proteção e condições de vitória. A classificação é heurística
   (por tipo e texto) e pode ser corrigida pelo agente.
5. **Probabilidades:** chance de ter N cópias/terrenos até o turno T (hipergeométrica).
6. **Relatório** em texto e JSON, com alertas (ex.: "18 fontes brancas recomendadas, a
   lista tem 13").
7. Parâmetros por formato: deck de 40, 60 ou 100 cartas mudam as recomendações.

## Critérios de aceite

- [x] Para uma lista conhecida, os números batem com a contagem manual.
- [x] Um deck de duas cores com fontes insuficientes de uma delas gera alerta.
- [x] As probabilidades batem com valores de referência da distribuição hipergeométrica.
- [x] Cartas dupla-face, split e de custo X são contadas de forma documentada.

## Fora do escopo

- Simulação de partidas ou goldfishing.
- Avaliação de qualidade individual das cartas (isso é julgamento do agente + dados de meta).
