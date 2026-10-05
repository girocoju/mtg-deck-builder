# 006 — Plano

## Decisões

- **O deck builder é uma skill do Claude Code**, não código novo:
  `.claude/skills/deck-construido/SKILL.md` descreve o fluxo em oito etapas, e o agente o
  executa usando as ferramentas das specs 001 a 005 e os documentos de `knowledge/`.
  A descrição da skill faz com que pedidos em linguagem natural a acionem.
- **Julgamento com o agente, verificação com as ferramentas:** escolher o arquétipo e as
  cartas é raciocínio do agente; existência, legalidade, base de mana e custo são sempre
  conferidos por comando.
- **Modelo antes de invenção:** quando o snapshot tem um arquétipo próximo do plano, a
  lista dele é o ponto de partida, e cada alteração é registrada com o motivo. Isso segue
  o princípio de templating do livro e reduz o risco de uma lista inviável.
- **BO1 sem dados é declarado:** enquanto não houver snapshot BO1, a skill manda dizer
  isso e não usar o meta BO3 como se fosse BO1.
- **O arquivo do deck é a entrega durável:** `decks/<formato>/<nome>.md`, com a lista em
  bloco de código e todas as seções exigidas pela spec.

## Etapas da skill

1. Entender o pedido · 2. Ler o meta e a teoria · 3. Definir o plano · 4. Selecionar as
cartas · 5. Base de mana · 6. Sideboard · 7. Validar · 8. Entregar.

## Riscos

- **Qualidade real desconhecida:** não há simulação nem dados de win rate; a lista é uma
  proposta fundamentada. O retorno dos testes do usuário, registrado como lição, é o
  mecanismo de correção.
- **Uma lista de referência por arquétipo** pode não refletir as variações do meta.
- **A heurística de papéis** erra em cartas de redação incomum; os números de "remoção"
  do resumo de meta são aproximados.
