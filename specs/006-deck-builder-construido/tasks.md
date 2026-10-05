# 006 — Tarefas

- [x] Skill `deck-construido` com o fluxo de oito etapas
- [x] Execução completa do fluxo para "Crie um deck anti meta no formato Standard" (BO3)
- [ ] Execução em Pioneer, Modern e Pauper (inclui a primeira coleta de meta desses formatos)
- [ ] Execução com restrição de orçamento, demonstrando o custo. *Parcial (2026-10-05):*
      `decks/standard/mono-red-prowess-bo1-sem-coringas.md` otimiza uma lista sem gastar
      coringas, mas só com as cartas que o usuário mostrou ter; sem a coleção, não é
      possível demonstrar o custo zero
- [x] Execução em BO1 com snapshot BO1 (2026-10-05): com o meta do Untapped enviado pelo
      usuário, a escolha para Standard BO1 sem coringas foi o melhor deck do campo que ele
      já tem (`decks/standard/mono-white-auras-bo1.md`), e não um deck novo. A lista foi
      reconstruída do resumo do Untapped, não construída carta a carta
- [ ] Teste da skill em sessão nova do Claude Code, acionada só pelo pedido em linguagem natural

## Verificação (2026-10-04)

Pedido executado: "Crie um deck anti meta no formato Standard".
Resultado: `decks/standard/boros-tokens-anti-meta.md`.

- **Meta usado:** MTGGoldfish, 2026-10-04, BO3; dez arquétipos lidos com as listas.
- **Leitura:** campo com 8,8 remoções pontuais e 0,8 em massa por deck, 27% dependente de
  anulações e mágicas em velocidade de instantânea, 34% usando o cemitério.
- **Escolha:** enxame de fichas (Boros Tokens, 1,8% do meta, usado como modelo) com
  Voice of Victory e duas Rest in Peace no principal.
- **Alterações em relação ao modelo:** saíram 2 Seam Rip e 1 Suki, Courageous Rescuer do
  principal; entraram 2 Rest in Peace e a quarta Torch the Tower. Sideboard refeito.
- **Validação:** 60 + 15, todas as cartas legais em Standard e disponíveis no Arena.
- **Análise:** valor de mana médio 1,89; 22 terrenos contra 20,9 da fórmula; 15 fontes
  brancas e 17 vermelhas para exigência de 14; nenhum alerta.
- **Custo:** US$ 238, 43 tix, 48 raras no Arena.
- **Entrega:** todas as seções do requisito 4 estão no arquivo do deck.

Achado durante a execução: a heurística de papéis contava Rest in Peace como remoção em
massa ("exile all graveyards"); corrigido em `analysis.py`.

O fluxo foi executado pelo agente que escreveu a skill, na mesma sessão. Ainda não foi
testado se uma sessão nova, só com o pedido do usuário, aciona a skill e chega ao mesmo
nível de entrega.
