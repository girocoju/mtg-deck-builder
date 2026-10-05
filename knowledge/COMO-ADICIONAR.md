# Como adicionar conhecimento

Dois caminhos: ingerir uma **fonte** nova (livro, artigo, vídeo transcrito) ou registrar
uma **lição** aprendida no uso do deck builder.

## Ingerir uma fonte

Pedido típico: "adicione este artigo à base de conhecimento: <URL>" ou "ingira este PDF".

1. **Obter o texto.**
   - PDF: `.venv\Scripts\python scripts\extract_pdf.py <arquivo.pdf> <nome-da-fonte>`
     (requer `pip install -e ".[knowledge]"`). O texto vai para
     `data/fontes/<nome-da-fonte>/`, um arquivo por página, fora do git.
   - URL: ler a página. Se ela não carregar, baixar o HTML (`curl -L -o pagina.html <URL>`)
     e extrair com `.venv\Scripts\python scripts\extract_html.py pagina.html <nome-da-fonte>`;
     em último caso, outra hospedagem do mesmo texto ou o Web Archive. Anotar de onde veio.
   - Texto colado: salvar em `data/fontes/<nome-da-fonte>/`.
2. **Ler a fonte inteira** antes de escrever. Fontes longas são divididas em blocos.
3. **Avaliar a fonte.** Fonte oficial, estudo com dados, artigo de jogador reconhecido ou
   guia de divulgação? Dizer isso no documento. Regras, banidas e legalidade citadas por
   fontes não oficiais são conferidas na base local antes de entrar.
4. **Destilar por tema.** Para cada ideia útil à construção de decks, localizar o
   documento do tema em [README.md](README.md) e acrescentar ali: o que é, quando se
   aplica, como usar na construção, exemplo. Só criar documento novo se nenhum tema
   existente servir (e então incluí-lo no índice).
5. **Regras de redação.**
   - Palavras próprias. Nada de copiar ou traduzir trechos; no máximo uma frase curta
     entre aspas por documento. Números, fórmulas e tabelas são fatos e podem ser
     registrados com atribuição.
   - Números só se lidos na fonte. O que não foi conferido fica como "não verificado";
     contas próprias ficam como "calculado".
   - Nomes de cartas, formatos e termos consagrados em inglês; cartas citadas devem
     existir na base (`mtg card "Nome"`).
   - Exemplos datados são marcados como "Exemplo histórico".
6. **Tratar conflitos.** Se a fonte nova contradiz o que já está no documento, manter as
   duas posições, dizer qual prevalece e por quê (em geral a mais recente ou a apoiada
   em dados).
7. **Referenciar.** Acrescentar a fonte na seção de referências de cada documento tocado
   (capítulo/páginas ou URL e data de acesso).
8. **Registrar em [fontes.md](fontes.md):** autor, tipo, data, onde está o original, o
   que foi aproveitado e em quais documentos. Mapear cada capítulo ou seção como
   "coberto em X" ou "fora do escopo".
9. **Conferir cópia** (fontes em PDF/texto local):
   `.venv\Scripts\python scripts\check_copy.py <nome-da-fonte>` não deve apontar trechos
   além de frases curtas citadas.

## Registrar uma lição

Uma lição nasce quando o uso mostra algo que a teoria não previu: feedback do usuário
sobre um deck gerado, resultado de partidas, erro do agente, descoberta sobre um formato.

1. Criar `licoes/AAAA-MM-DD-assunto-curto.md` seguindo o modelo em
   [licoes/README.md](licoes/README.md).
2. Acrescentar uma linha no índice de `licoes/README.md`.
3. Se a mesma lição aparecer pela segunda vez, ou valer para qualquer formato,
   **promovê-la**: incorporar ao documento do tema (citando as lições como referência) e
   marcar as lições originais como promovidas.

O agente deve registrar a lição no mesmo atendimento em que ela surge, e dizer ao usuário
que registrou.
