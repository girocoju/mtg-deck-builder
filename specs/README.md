# Specs — desenvolvimento guiado por especificação

Este diretório é a fonte da verdade sobre **o que** o projeto faz e **em que ponto está**.
Nenhuma funcionalidade é implementada sem uma spec aprovada.

## Roadmap

| #   | Spec                                                        | Entrega                                                        | Status          |
| --- | ----------------------------------------------------------- | -------------------------------------------------------------- | --------------- |
| 000 | [Constituição](000-constituicao.md)                         | Princípios que valem para todas as specs                       | Vigente         |
| 001 | [Base de cartas](001-base-de-cartas/spec.md)                | Base local completa (Scryfall) + CLI `mtg` de consulta         | ✅ Concluída    |
| 002 | [Base de conhecimento](002-base-de-conhecimento/spec.md)    | Teoria de deck building (Chapin, Karsten) em `knowledge/`       | 🚧 Em andamento |
| 003 | [Decklists e formatos](003-decklists-e-formatos/spec.md)    | Ler, validar e exportar listas (Arena, MTGO, papel)            | ✅ Concluída    |
| 004 | [Análise de deck](004-analise-de-deck/spec.md)              | Curva, base de mana, papéis das cartas, diagnóstico            | ✅ Concluída    |
| 005 | [Metagame](005-metagame/spec.md)                            | Snapshots do meta (MTGGoldfish; BO1 por importação)            | ✅ Concluída    |
| 006 | [Deck builder construído](006-deck-builder-construido/spec.md) | "Crie um deck anti meta no formato Standard"                | 🚧 Em andamento |
| 007 | [Commander e Brawl](007-commander-e-brawl/spec.md)          | "Monte um deck de Brawl com o commander X" (EDHREC)            | ✅ Concluída    |
| 008 | [Draft](008-draft/spec.md)                                  | "Crie uma estratégia de draft para a coleção X" (17Lands)      | 📝 Especificada |
| 009 | [Adaptação BO3 ↔ BO1](009-adaptacao-bo3-bo1/spec.md)        | "Adapte o deck em questão BO3 para BO1"                        | 📝 Especificada |

Status possíveis: 📝 Especificada → 📐 Planejada → 🚧 Em andamento → ✅ Concluída.

Dependências: 003 e 004 dependem de 001; 006, 007 e 008 dependem de 002–004;
006 depende de 005; 009 depende de 003–006. A ordem numérica é a ordem sugerida de execução.

## Processo

Cada spec vive em uma pasta `NNN-nome/` com até três arquivos, criados nesta ordem:

1. **`spec.md` — o quê e por quê.** Objetivo, histórias de uso, requisitos, critérios de
   aceite verificáveis e o que fica fora do escopo. Não fala de implementação.
   Dúvidas ficam em "Questões em aberto" e precisam ser resolvidas antes do plano.
2. **`plan.md` — como.** Decisões técnicas, estrutura de arquivos, modelo de dados, riscos.
   Escrito só quando a spec é a próxima a ser executada (evita plano desatualizado).
3. **`tasks.md` — passos.** Checklist pequeno e ordenado; cada item marcado ao ser concluído.

Uma spec só vira ✅ quando todos os critérios de aceite foram verificados de verdade
(teste automatizado ou execução real registrada no `tasks.md`), e a tabela acima é atualizada.

Mudou de ideia sobre um requisito? Altere primeiro o `spec.md`, depois o código.
