# Star Trek (TRK) — guia de draft preliminar e teórico

- **Situação em 2026-10-05:** a coleção sai em 2026-11-13. **O 17Lands não tem dados**
  (`mtg draft update trk` confirma), e a base local tem só as **86 cartas já reveladas**.
- **Este guia é teórico e parcial.** Nada aqui vem de partidas: é a leitura das cartas
  conhecidas pela base (`mtg draft set trk`) mais os princípios de
  `knowledge/limitado-e-draft.md`. Deve ser refeito quando a coleção estiver completa e,
  de novo, quando houver cerca de duas semanas de dados.

## O que já dá para ver

Cartas reveladas por cor (comuns e incomuns, que decidem um draft):

| Cor | Reveladas | Comuns | Incomuns | Criaturas C+U | Classificadas como remoção |
| --- | --- | --- | --- | --- | --- |
| Branco | 15 | 10 | 4 | 9 | Command Decision; Malfunctioning Holodeck; 70,000 Light-Years from Home |
| Azul | 11 | 7 | 4 | 6 | nenhuma |
| Preto | 17 | 9 | 6 | 9 | Resistance Is Futile; Eject the Warp Core; He's Dead, Jim |
| Vermelho | 13 | 8 | 4 | 7 | Munitions Enthusiast; Plasma Cascade; Perils of the Past |
| Verde | 15 | 10 | 4 | 8 | Amok Time |
| Multicoloridas | 2 | 0 | 1 | 1 | — |
| Incolores | 13 | 1 | 0 | 1 | — |

A coluna de remoção é uma classificação automática pelo texto das cartas e pode errar
para os dois lados; confira o texto com `mtg card` antes de usar em uma decisão.

Palavras-chave mais frequentes entre as reveladas: ciclos de cycling de terreno
(landcycling, basic landcycling, typecycling: 5 cartas cada), flying (5), landfall (4),
surveil (4).

## Leitura provisória

- **Cycling de terreno em comuns** costuma indicar um formato com curva um pouco mais
  alta e mãos mais regulares: cartas caras deixam de ser um risco na mão inicial.
- **Azul sem remoção revelada** e com poucas criaturas: se a coleção completa confirmar,
  azul dependerá de evasão e de truques de tempo, e a segunda cor terá de trazer a remoção.
- **Preto, branco e vermelho** têm três cartas de remoção cada entre as reveladas; verde, uma.
- Só duas cartas multicoloridas foram reveladas: **ainda não é possível descrever os dez
  arquétipos** nem as cartas sinalizadoras de cada par.

## O que este guia ainda não pode dizer

- Ranking de comuns e incomuns: sem dados, e com a coleção incompleta, qualquer ordem
  seria palpite.
- Velocidade do formato, melhores pares de cores, bombas, cartas superestimadas.
- Mecânicas próprias da coleção: as palavras-chave acima são as que a base registra; as
  mecânicas novas podem não estar marcadas.

## Como usar até lá

Avalie cada carta pelo método do livro (`knowledge/limitado-e-draft.md`): remoção e
evasão primeiro, curva de criaturas em seguida, truques por último; 17 terrenos em 40
cartas; duas cores. Ao abrir a coleção, comece o draft sem cores fixas e leia os sinais.

## Refazer

```
.venv\Scripts\mtg sync                 # traz as cartas novas
.venv\Scripts\mtg draft set trk        # leitura da coleção
.venv\Scripts\mtg draft update trk --mode all   # quando houver dados
```
