# 008 — Tarefas

- [x] Conferir `robots.txt` e acesso do 17Lands
- [x] `draft.py`: coleta por coleção e modo, com cache; rankings; pares de cores;
      avaliação de pacote/pool; subestimadas e superestimadas; leitura da coleção
- [x] CLI `mtg draft update | set | cards | colors | rate | gaps`
- [x] Skill `draft` (guia, pick, pool)
- [x] Testes sem rede (7 testes em `tests/test_draft.py`)
- [x] Guia com dados: `drafts/fra.md`
- [x] Guia teórico: `drafts/trk.md`
- [x] Deck de 40 a partir de um pool de 45: `decks/limited/fra-pool-exemplo.md`
- [ ] Teste da skill em sessão nova, acionada só pelo pedido em linguagem natural
- [ ] Recomendação de pick exercitada com um pacote real informado pelo usuário
- [ ] Regenerar `drafts/fra.md` com cerca de duas semanas de dados

## Verificação (2026-10-05)

Suíte completa: 64 testes passando.

- **Coleta real de Reality Fracture:** Premier Draft (220.847 jogos), Traditional Draft
  (23.030), Sealed (44.089) e Pick Two (30.417) têm dados; Quick Draft e Traditional
  Sealed não. Cada modo ficou em arquivo próprio.
- **Guia com dados:** `drafts/fra.md` traz os dez pares com win rate, rankings de comuns
  e incomuns por cor, bombas, prioridades, armadilhas e a comparação entre modos, com
  data, modo e aviso de amostra.
- **Sem dados:** `mtg draft cards fra --mode quick` e `mtg draft update trk` respondem
  que não há dados e mandam usar o modo teórico; `drafts/trk.md` se declara teórico e
  parcial (86 cartas reveladas).
- **Cartas da coleção:** as cartas do deck de exemplo foram conferidas contra a lista do
  17Lands (nenhuma fora). No guia, os nomes vêm das saídas dos comandos.
- **Pool de 45:** deck de 40 validado em `limited`; a análise confirmou 10 fontes azuis
  e 9 vermelhas para exigência de 9, e gerou o alerta esperado para o splash de uma carta.
- **Avaliação de pacote:** `mtg draft rate` devolve as estatísticas das cartas citadas e
  lista à parte as que não têm dados.

Observações:

- A coleção tinha seis dias de dados: só 220 das 290 cartas passam da amostra mínima.
- 31 cartas da lista do 17Lands não casaram com a coleção `fra` da base (básicos e folha
  bônus) e ficam fora da leitura por cor.
- O pool de teste foi sorteado, não draftado: tinha só 21 cartas conjuráveis nas duas
  melhores cores, o que forçou 18 terrenos e um splash.
