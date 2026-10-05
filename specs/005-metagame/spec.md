# 005 — Metagame

**Status:** 📝 Especificada

## Objetivo

Saber, com data e fonte, quais decks dominam cada formato de construído, para que o deck
builder possa escolher e ajustar listas contra o campo real.

## Histórias de uso

- Como agente, ao receber "crie um deck anti meta no Standard", quero os arquétipos mais
  jogados, sua fatia do meta e listas de referência.
- Como usuário, quero saber de quando são os dados em que a recomendação se baseou.

## Requisitos

1. **Fontes:** MTGGoldfish (fatia do meta por arquétipo) e MTGTop8 (resultados de
   torneios), coletados das páginas públicas.
2. **Formatos:** no mínimo Standard, Pioneer, Modern, Legacy, Vintage, Pauper; os formatos
   do Arena (Historic, Timeless, Alchemy) quando a fonte os cobrir.
3. **Snapshot por formato** com: data da coleta, fonte, arquétipos, fatia do meta, e ao
   menos uma lista de referência por arquétipo relevante (principal + sideboard).
   **BO1 e BO3 são metas diferentes e ficam em snapshots separados.** Todo snapshot e
   toda lista de referência é marcada como melhor-de-um (BO1) ou melhor-de-três (BO3).
   Dados de torneios e de papel/MTGO são BO3; a ranqueada do Arena tem as duas filas.
   Nunca misturar os dois em uma mesma estatística; se só houver dados de um modo, o
   agente diz isso ao responder sobre o outro.
4. As cartas das listas coletadas são conferidas com a base local (spec 001).
5. **Atualização sob demanda** por comando, com cache: não coletar de novo o que foi
   coletado há pouco tempo. Snapshots antigos são mantidos para ver a evolução.
6. **Resumo de meta** por formato: quais estratégias dominam (aggro/controle/combo/
   midrange), cartas mais jogadas, velocidade do formato e tipos de interação mais comuns.
7. **Falha tolerável:** se a coleta quebrar (mudança de layout, bloqueio), o comando avisa
   claramente e o agente recorre à busca na web, declarando isso na resposta.

## Critérios de aceite

- [ ] Um comando gera o snapshot de Standard com pelo menos os 10 arquétipos principais.
- [ ] Todo snapshot tem data e fonte; o agente as cita ao usá-lo.
- [ ] Todo snapshot e toda lista de referência indica BO1 ou BO3, e o resumo de meta de
      um formato do Arena apresenta os dois separadamente quando houver dados.
- [ ] Rodar o comando duas vezes seguidas não refaz as requisições.
- [ ] Com a rede indisponível, o erro é claro e o snapshot anterior continua utilizável.

## Fora do escopo

- Matriz de confrontos (win rate deck contra deck): não há fonte pública confiável.
- Commander/Brawl (spec 007) e limitado (spec 008).

## Questões em aberto

- Conferir termos de uso e `robots.txt` de cada site antes de implementar a coleta; se
  algum proibir, a alternativa é a busca na web sob demanda para aquele site.
- MTGGoldfish e MTGTop8 refletem principalmente BO3. Definir no plano a fonte de dados
  de BO1 do Arena (ex.: Untapped.gg, MTGA Zone, AetherHub) e sua forma de acesso.
