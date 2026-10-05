# 009 — Plano

## Decisões

- **Skill `adaptar-bo1-bo3`** (`.claude/skills/adaptar-bo1-bo3/SKILL.md`), com seis
  etapas e um ramo para cada sentido. Reaproveita validação (003), análise (004), meta
  por modo (005) e os documentos de sideboard, papel no jogo e base de mana.
- **Um comando novo, `mtg deck diff`,** para a tabela "saiu / entrou": compara duas
  listas por seção. O "por quê" é escrito pelo agente.
- **A regra de terrenos em BO1** vem de `knowledge/base-de-mana.md`, seção 1.4: aggro de
  curva baixa pode cortar 1 ou 2; os demais não cortam; ao voltar para BO3, repor.
- **Sem snapshot do modo de destino, a adaptação é teórica** e declarada como tal. É a
  situação de todo BO1 enquanto não houver importação do Untapped.
- **O arquivo adaptado fica ao lado do original**, com sufixo `-bo1` ou `-bo3`, e aponta
  para a origem.

## Riscos

- Sem meta BO1, as escolhas de "o que é flexível" são julgamento geral.
- O guia de sideboard em BO3 parte de uma lista de referência por arquétipo.
- A suavização de mão do Arena é modelada como limite superior; o corte de terrenos em
  BO1 é hipótese a validar em jogo.
