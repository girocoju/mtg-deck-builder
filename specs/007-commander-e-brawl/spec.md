# 007 — Commander e Brawl

**Status:** ✅ Concluída

## Objetivo

Atender pedidos como **"Me ajude a montar um deck do formato Brawl com o commander Ivy,
Gleeful Spellthief"**: construir decks singleton em torno de um comandante, para
Commander (papel/MTGO) e Brawl / Standard Brawl (Arena).

## Histórias de uso

- "Me ajude a montar um deck de Brawl com o commander Ivy, Gleeful Spellthief."
- "Monte um Commander de até US$ 100 com [comandante]."
- "Que comandantes combinam com uma estratégia de tokens em Standard Brawl?"

## Requisitos

1. **Comando/skill** dedicado; aceita o comandante, o formato e restrições opcionais
   (orçamento, nível de poder, plataforma).
2. **Análise do comandante:** o que ele faz, que estratégias habilita, de que tipo de
   carta precisa (ex.: Ivy quer mágicas baratas que dão alvo em uma única criatura).
3. **Dados de sinergia do EDHREC** para o comandante (cartas mais usadas e de maior
   sinergia), com data de coleta e cache local. Como o EDHREC reflete Commander de papel,
   toda sugestão é filtrada pela legalidade e disponibilidade no formato pedido.
4. **Busca própria na base** por sinergias que o EDHREC não mostra (cartas novas, cartas
   exclusivas do Arena), usando texto e tipo.
5. **Estrutura do deck por categorias** com quantidades-alvo ajustadas ao comandante e ao
   tamanho do deck: terrenos, aceleração, compra de cartas, remoção pontual, remoção em
   massa, proteção, peças de sinergia e condições de vitória.
6. **Regras do formato** via validador (spec 003): identidade de cor, cópia única,
   tamanho (100 em Commander e Brawl, 60 em Standard Brawl), banidas de cada formato.
7. **Entrega:** lista por categoria, exportável; plano de jogo; principais combos e
   sinergias explicados; como o deck vence; fraquezas; custo.
8. **Modo colaborativo** ("me ajude a montar"): o agente propõe a direção e confirma as
   escolhas principais com o usuário antes de fechar a lista.

## Critérios de aceite

- [x] O pedido com Ivy, Gleeful Spellthief em Brawl produz 100 cartas válidas, todas com
      identidade dentro de GU e disponíveis no Arena.
- [x] O deck tem, de forma verificável, as categorias do requisito 5 dentro das metas,
      ou com cada desvio apontado pela ferramenta e justificado na entrega.
- [x] Um comandante inválido para o formato é recusado com explicação.
- [x] O mesmo fluxo gera um deck de Commander (papel) e um de Standard Brawl.

## Fora do escopo

- cEDH e análise de meta competitivo de Commander.
- Cálculo oficial de "bracket"/nível de poder além de uma estimativa explicada.

## Questões em aberto

- Existe fonte de dados específica de Brawl do Arena (um contra um) que valha integrar?
  Hoje as sinergias vêm de Commander de mesa.
