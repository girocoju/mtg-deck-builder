# Specs — desenvolvimento guiado por especificação

Este diretório é a fonte da verdade sobre **o que** o projeto faz e **em que ponto está**.
Nenhuma funcionalidade é implementada sem uma spec aprovada.

## Roadmap

| #   | Spec                                                        | Entrega                                                        | Status          |
| --- | ----------------------------------------------------------- | -------------------------------------------------------------- | --------------- |
| 000 | [Constituição](000-constituicao.md)                         | Princípios que valem para todas as specs                       | Vigente         |
| 001 | [Base de cartas](001-base-de-cartas/spec.md)                | Base local completa (Scryfall) + CLI `mtg` de consulta         | ✅ Concluída    |
| 002 | [Base de conhecimento](002-base-de-conhecimento/spec.md)    | Teoria de deck building (Chapin, Karsten) em `knowledge/`       | ✅ Concluída    |
| 003 | [Decklists e formatos](003-decklists-e-formatos/spec.md)    | Ler, validar e exportar listas (Arena, MTGO, papel)            | ✅ Concluída    |
| 004 | [Análise de deck](004-analise-de-deck/spec.md)              | Curva, base de mana, papéis das cartas, diagnóstico            | ✅ Concluída    |
| 005 | [Metagame](005-metagame/spec.md)                            | Snapshots do meta (MTGGoldfish; BO1 por importação)            | ✅ Concluída    |
| 006 | [Deck builder construído](006-deck-builder-construido/spec.md) | "Crie um deck anti meta no formato Standard"                | 🚧 Em andamento |
| 007 | [Commander e Brawl](007-commander-e-brawl/spec.md)          | "Monte um deck de Brawl com o commander X" (EDHREC)            | ✅ Concluída    |
| 008 | [Draft](008-draft/spec.md)                                  | "Crie uma estratégia de draft para a coleção X" (17Lands)      | ✅ Concluída    |
| 009 | [Adaptação BO3 ↔ BO1](009-adaptacao-bo3-bo1/spec.md)        | "Adapte o deck em questão BO3 para BO1"                        | 🚧 Em andamento |
| 010 | [Assistente e simulador de draft](010-assistente-de-draft/spec.md) | Pick a pick pelo log do Arena, simulador com bots, snapshots datados | 🚧 Em andamento |
| 011 | [Registro de partida](011-registro-de-partida/spec.md)      | Mão, campo, cemitério, exílio, ataques e dano na janela; registro da partida; conselhos calculáveis | 🚧 Em andamento |
| 012 | [Conselheiro local](012-conselheiro-local/spec.md)         | Opinião de jogada ao vivo por modelo local (Ollama), com contexto montado pelo rastreador | ⏸️ Adiada |
| 013 | [Perfil em vários dispositivos](013-perfil-em-varios-dispositivos/spec.md) | Perfil do Arena (partidas, coleção, baú) consultável no celular; captura fica no PC | 📝 Especificada |
| 014 | [Mapa de picks da coleção](014-mapa-de-picks/spec.md) | Peso de cada carta antes do draft: ordem por raridade, segundos picks, elos diretos, grafo de sinergias; leitura da coleção e PDF ilustrado (FRA, TRK) | 🚧 Em andamento |

Status possíveis: 📝 Especificada → 📐 Planejada → 🚧 Em andamento → ✅ Concluída.

Dependências: 003 e 004 dependem de 001; 006, 007 e 008 dependem de 002–004;
006 depende de 005; 009 depende de 003–006; 010 depende de 001, 003 e 008; 014 depende de
008 e 010. A ordem numérica é a ordem sugerida de execução.

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
