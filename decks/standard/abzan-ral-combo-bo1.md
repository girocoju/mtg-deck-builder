# Abzan Ral Combo (otimizado para consistência)

- **Formato:** standard (BO1) · **Plataforma:** Arena · **Data:** 2026-10-13
- **Origem:** lista do usuário (24 terrenos, já vencedora em partidas), ajustada em duas
  rodadas a pedido: primeiro dois terrenos a menos e duas cartas de consistência; depois
  as trocas propostas na análise, com o critério de consistência do próprio deck, não do meta
- **Meta de referência:** não usado nesta versão. Para a leitura do campo, há um snapshot
  de Standard BO1 (Untapped.gg, 2026-10-05; `mtg meta show standard --mode bo1`)

```
Deck
4 Ajani Resolute
2 Ajani, Outland Chaperone
4 Amalia Benavides Aguirre
2 Bleachbone Verge
3 Erode
4 Godless Shrine
4 Hinterland Sanctifier
3 Liliana the Faultless
4 Lunar Convocation
4 Overgrown Tomb
1 Plains
2 Professor Dellian Fel
4 Ral Zarek, Guest Lecturer
2 Shattered Sanctum
4 Starting Town
1 Swamp
4 Temple Garden
4 Way of the Mentor
4 Way of the Paradox
```

## O que mudou em relação à lista original e por quê

| Saiu | Entrou | Motivo |
| --- | --- | --- |
| 2 Overgrown Farmland | 1 Lunar Convocation (4ª) | Farmland entra virado até haver dois outros terrenos, nos turnos em que o deck quer jogar Sanctifier, Liliana e Ajani Resolute; e verde-branco era o par menos necessário (Way of the Paradox pede 12 fontes verdes; havia 16). Lunar Convocation é o único motor de compra repetível e não é lendária: a 4ª cópia sobe a chance de ter uma até o turno 4 de 42,7% para 52,8% (`mtg odds`) e cópias extras drenam mais 1 por turno |
| | 1 Ajani Resolute (4ª) | A peça de 2 manas que converte cada ganho de vida em lealdade e, com Paradox, gera vida de graça todo turno (0: ganhe 1 vida → Paradox: +1 vida pela ativação → Mentor: +2 de lealdade em cada walker). Quanto antes cai, mais cedo Ral chega a 7 |
| 2 Hushwood Verge | 2 Bleachbone Verge | Ral ({1}{B}{B}) pedia 18 fontes pretas e havia 15 (alerta do `mtg deck analyze`). Bleachbone dá preto sempre e branco com qualquer Plains ou Swamp em jogo, o que inclui Godless Shrine, Temple Garden e Overgrown Tomb. Fontes passam a W 17, B 17, G 12; o verde fica no mínimo exato de Paradox, única carta verde |
| 2 Essence Channeler | 1 Ral Zarek, Guest Lecturer (4º) | Channeler é só um corpo que cresce; não acha peças nem acelera Ral. Ral é a condição de vitória e também seleção (+1: surveil 2); com 4 cópias, a chance de ter um até o turno 6 vai de 49,5% para 60,1%. Como o −7 zera a lealdade quando Ral está em 7, uma segunda cópia não é carta morta: repõe o walker para o turno seguinte |
| | 1 Amalia Benavides Aguirre (4ª) | A carta que mais suaviza o deck: a cada ganho de vida explora, e terreno revelado vai para a mão. Em um deck com 22 terrenos e 10 jogadas de custo 1, é o que garante o quarto terreno; quando não é terreno, cresce rumo aos 20 de poder. Ward (3 vidas) protege o motor; Ral −2 devolve uma cópia morta |

**Terrenos.** A fórmula de Karsten para esta lista dá 22,6 (`knowledge/base-de-mana.md`,
"Resposta rápida"). Com 22, o deck fica um pouco abaixo, o que sustentam a suavização de
mão inicial do Arena em BO1 (seção 1.4: abrir com 2 a 4 terrenos sobe de 75% para cerca de
94%), a filtragem embutida (4 Amalia explorando, 4 Ral e a ficha de Jace com surveil, 4
Lunar Convocation comprando) e a curva que para no 4 com só duas cartas. Não cortar mais:
3 terrenos no turno 3 já está em 72% jogando primeiro, sem contar a suavização.

**Básicos mantidos** (1 Plains, 1 Swamp), como pedido: são os alvos da busca quando o
oponente usa Erode em uma permanente sua.

**Fontes por cor** (`mtg deck analyze`): W 17 (Ajani, Outland Chaperone {1}{W}{W} pede 18;
são 2 cópias que não precisam cair no turno 3), B 17 (Ral pede 18; 4 Starting Town pagam
1 vida por cor, que o deck recupera), G 12 (Paradox pede 12).

## Plano de jogo

Combo de ganho de vida e lealdade, montado só com o texto das cartas (`mtg card`):

1. **Turnos 1 e 2:** Hinterland Sanctifier e Liliana the Faultless (ganham 1 vida sempre
   que outra criatura ou, no caso de Liliana, outro planeswalker seu entra), Ajani
   Resolute (ganha lealdade a cada ganho de vida; 0: ganhe 1 vida), Amalia (explora a cada
   ganho de vida) e Lunar Convocation (drena 1 por turno em que você ganhou vida; {1}{B},
   pague 2 vidas: compre).
2. **Turno 3:** Way of the Mentor ou Way of the Paradox. As duas criam ou carregam uma
   ficha de Jace (empower 5), que compra (−3) ou filtra (−1). Mentor: cada ganho de vida
   põe 1 lealdade em **cada** planeswalker seu. Paradox: cada ativação de lealdade ganha 1
   vida e libera um terreno extra no turno. Com as duas, toda ativação vira vida, que vira
   lealdade em todos os walkers, inclusive na ficha de Jace. A segunda cópia de cada Way
   não é morta: entra, dá empower 5 e só então a regra de lendas a remove.
3. **Ral Zarek, Guest Lecturer** entra com 3 e sobe com cada ganho de vida. Com 7: −7,
   cinco moedas, o oponente pula X turnos (X = caras). A esperança é de 2,5 turnos; sair
   zero tem probabilidade de 1/32 (3,1%, calculado). Enquanto acumula, +1 (surveil 2)
   procura peças, −1 descarta e −2 devolve Amalia, Liliana ou Sanctifier do cemitério.
   Ajani, Outland Chaperone +1 cria uma ficha todo turno, e cada ficha dispara Sanctifier e
   Liliana: é um gerador de vida repetível, não só um walker de apoio.
4. **Fechamento:** Lunar Convocation drena todo turno; Professor Dellian Fel (+2: 3 vidas;
   −6: emblema que faz o oponente perder a vida que você ganha) converte o motor em dano;
   Amalia com poder exatamente 20 limpa a mesa; Ajani, Outland Chaperone −8 coloca em jogo
   permanentes de custo até 3 do topo, proporcionais ao total de vida.

Papel por matchup (`knowledge/papel-no-jogo.md`): controle contra aggro (ganha vida mais
rápido do que leva dano e Erode mata a ameaça) e combo contra midrange e controle (vence
pelo turno em que Ral ulta, não por dano).

## Papel das cartas

| Grupo | Cartas | Função |
| --- | --- | --- |
| Ganho de vida repetível | Hinterland Sanctifier 4, Liliana the Faultless 3, Ajani Resolute 4, Ajani, Outland Chaperone 2 (+1 gera ficha), Professor Dellian Fel 2, Way of the Paradox 4 | Combustível do motor; Paradox transforma ativações em vida |
| Conversores | Way of the Mentor 4, Ajani Resolute 4, Amalia 4, Lunar Convocation 4 | Vida vira lealdade, cartas, contadores ou dano |
| Condição de vitória | Ral Zarek 4, Professor Dellian Fel 2, Lunar Convocation 4, Amalia 4 | Turnos pulados, dreno, emblema, limpeza de mesa |
| Interação | Erode 3, Ajani, Outland Chaperone (−2: 4 de dano em criatura virada), Dellian Fel (−3) | Remoção barata; Erode dá um básico ao oponente |
| Compra e seleção | Lunar Convocation 4, Amalia 4 (explorar), Ral 4 (+1), ficha de Jace | Achar as Ways e Ral; a ficha de Jace também ativa Paradox |
| Proteção | Liliana ({1}, {T}, descarte: hexproof para outra criatura ou planeswalker), Amalia (ward 3 vidas) | Protege Ral; as Ways ficam expostas |

## Guia de sideboard

Em BO1 não há troca entre jogos e o deck não tem efeitos que busquem cartas de fora, então
a lista não leva sideboard (`knowledge/licoes/2026-10-04-sideboard-bo1-arena.md`).

## Pontos fracos

- **Ways são encantamentos lendários expostos:** remoção de encantamento (Get Lost, por
  exemplo) desmonta o motor. Liliana não as protege.
- **Dez lendas de custo 1 a 3 em quatro cópias** (Ajani Resolute, Amalia, Ral, as Ways):
  a segunda cópia na mão é pior que a primeira. O deck compensa com Ral −2, com o empower
  da segunda Way e com o fato de Ral morrer ao ultar.
- **Ral −7 depende de moedas:** 3,1% de pular zero turnos; a esperança é 2,5.
- **Erode dá terreno ao oponente:** acelera decks de ramp.
- **Verde no limite:** 12 fontes para Way of the Paradox, 4 delas Starting Town (1 vida).
- Lista não testada nesta configuração; a versão original venceu partidas.

## O que observar nos testes

- Quantas vezes faltou o quarto terreno no turno 4: 54% com 22 terrenos contra 63% com 24,
  jogando primeiro e sem contar a suavização de mão do BO1 nem as explorações de Amalia. Se
  Dellian Fel ficar preso na mão com frequência, é o sinal de voltar a 23.
- Se sobrarem cópias lendárias na mão (segundo Ral, segunda Amalia) sem uso: voltar um Ral
  a 3 e repor com Essence Channeler ou quarto Erode.
- Se faltou verde para Paradox no turno 3: trocar um Bleachbone Verge por Hushwood Verge.
