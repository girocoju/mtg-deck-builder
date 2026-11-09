"""Documento da coleção em PDF (spec 014): guia de draft + leitura da coleção + mapa completo.

`render()` monta `drafts/<coleção>/<coleção>.pdf`, A4 paisagem, a partir de um `SetMap` e do
guia escrito pelo agente em `drafts/<coleção>/guia.md` (Markdown, convertido por
`pdf_flow`). Partes: capa com números-chave e sumário; como ler; o guia (uma seção por
página, com continuação); a coleção em números e a leitura; os pares nos dados (quando
há); os dez arquétipos (visão geral, payoffs e enablers em barras, listas completas);
ordem de pick por raridade (barras com as 40 melhores e tabela completa); grafo de elos
(nó = carta, cor = cor da carta, tamanho = centralidade), comunidades e centralidade;
pares com mais sinergia; segundos picks de todas as raras e míticas; limites. As páginas
são planejadas antes de desenhar, por isso o sumário traz os números de página.

Cores: W amarelo, U azul, B roxo, R vermelho, G verde, incolor cinza; multicolorida =
barra ou nó dividido. Paleta validada para visão de cores (skill dataviz: pior par
verde↔vermelho ΔE 7,2 sob protanopia, faixa que exige rótulos; toda barra e todo nó
rotulado trazem a letra da cor). Precisa de matplotlib (`pip install -e ".[viz]"`).
"""

import math
import textwrap
from datetime import datetime
from pathlib import Path

from . import pdf_flow
from .draft_map import COLOR_GROUPS, COLOR_PT, DRAFTS_DIR, RARITY_ORDER, RARITY_PT, _links, _mark, analysis_lines

PAGE = (11.69, 8.27)                      # A4 paisagem, polegadas
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
COLOR_HEX = {"W": "#eda100", "U": "#2a78d6", "B": "#7b3fa0", "R": "#e34948", "G": "#008300"}
COLORLESS = "#898781"
CATEGORICAL = ("#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948")
ORDINAL = {"common": "#9ec5f4", "uncommon": "#5598e7", "rare": "#256abf", "mythic": "#104281"}   # uma matiz, claro → escuro
RARITY_LETTER = {"mythic": "M", "rare": "R", "uncommon": "U", "common": "C"}
SOURCE_PT = {"17lands": "17Lands", "untapped": "Untapped", "draftsim*": "Draftsim*", "teorica*": "teórica*"}
EDGE_MIN = 1.0            # arestas desenhadas no grafo (o enabler genérico, 0,25, e um elo fraco, 0,5, ficam de fora)
STRONG_EDGE = 1.5         # arestas com mais de um elo: mais escuras e com mais peso no posicionamento
GRAPH_LABELS = 30         # cartas rotuladas no grafo (as mais centrais, sem rótulos sobrepostos)
TOP_ORDER = 40            # cartas por página de barras na ordem de pick (a tabela completa vem depois)
TOP_PAIRS = 40            # pares na tabela de sinergia direta


def _setup():
    try:
        import matplotlib
        matplotlib.use("Agg")
        from matplotlib import pyplot as plt
        import numpy as np
    except ImportError as error:        # dependência opcional
        raise RuntimeError('o PDF do mapa precisa de matplotlib: .venv\\Scripts\\pip install -e ".[viz]"') from error
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans"],
                         "pdf.fonttype": 42, "text.color": INK, "axes.labelcolor": INK2, "xtick.color": MUTED,
                         "ytick.color": INK2, "axes.edgecolor": AXIS, "axes.facecolor": SURFACE,
                         "figure.facecolor": SURFACE, "savefig.facecolor": SURFACE})
    return plt, np


def _hex(card_colors):
    """Cores (hex) de uma carta, uma por cor; cinza para incolor."""
    colors = [COLOR_HEX[c] for c in (card_colors or "") if c in COLOR_HEX]
    return colors or [COLORLESS]


def _source(name):
    return SOURCE_PT.get(name, name)


def _clean(text):
    return text.replace("**", "").replace("`", "")


def _cut(text, width):
    return text if len(text) <= width else text[:width - 1].rstrip() + "…"


def _label(entry, width=34):
    """`Nome · WU R` para eixos e tabelas: a letra da cor acompanha a cor da barra."""
    tail = f" · {entry.get('cor', '-')} {RARITY_LETTER.get(entry.get('raridade', ''), '')}".rstrip()
    return _cut(entry["name"], width) + tail


def _cost(entry):
    return (entry.get("custo") or "").replace("{", "").replace("}", "")


def _rect(fig, x, y, color, w=0.009, h=0.009):
    from matplotlib.patches import Rectangle
    return Rectangle((x, y), w, h * PAGE[0] / PAGE[1], transform=fig.transFigure, facecolor=color, edgecolor="none")


class Doc:
    """Páginas com cabeçalho e rodapé numerado; blocos de texto; tabelas; legendas."""

    def __init__(self, plt, pdf, code, set_name):
        self.plt, self.pdf, self.code, self.set_name = plt, pdf, code, set_name
        self.n = 0
        self.today = datetime.now().strftime("%Y-%m-%d")

    def page(self, title, subtitle=""):
        fig = self.plt.figure(figsize=PAGE)
        fig.text(0.04, 0.955, title, fontsize=16, fontweight="semibold", color=INK, va="top")
        for i, part in enumerate(textwrap.wrap(subtitle, 190)[:2]):
            fig.text(0.04, 0.912 - i * 0.019, part, fontsize=8.5, color=INK2, va="top")
        return fig

    def close(self, fig, note=""):
        self.n += 1
        fig.text(0.04, 0.025, f"{self.set_name} ({self.code}) · documento da coleção · {self.today}"
                 + (f" · {note}" if note else ""), fontsize=7, color=MUTED)
        fig.text(0.96, 0.025, str(self.n), fontsize=7, color=MUTED, ha="right")
        self.pdf.savefig(fig)
        self.plt.close(fig)

    @staticmethod
    def paragraphs(fig, x, y, width, lines, size=8.5):
        """Parágrafos com cabeça em negrito (o trecho inicial entre `**`); `width` em fração da
        página. Devolve o y em que parou."""
        chars = max(24, int(width * PAGE[0] * 72 / (size * 0.5)))
        line_h = size * 1.5 / 72 / PAGE[1]
        for line in lines:
            head, text = "", _clean(line)
            if line.startswith("**") and "**" in line[2:]:
                end = line.index("**", 2)
                head, text = line[2:end], _clean(line[end + 2:]).strip()
            if head:
                fig.text(x, y, head, fontsize=size, fontweight="semibold", color=INK, va="top")
                y -= line_h
            for part in textwrap.wrap(text, chars) or [""]:
                fig.text(x, y, part, fontsize=size, color=INK2, va="top")
                y -= line_h
            y -= line_h * 0.5
        return y

    @staticmethod
    def table(fig, x, y, columns, rows, size=7.5, head=True):
        """Tabela curta por texto: `columns` = [(título, deslocamento x em fração)]."""
        row_h = size * 1.65 / 72 / PAGE[1]
        if head:
            for title, dx in columns:
                fig.text(x + dx, y, title, fontsize=size, fontweight="semibold", color=INK, va="top")
            y -= row_h * 1.25
        for row in rows:
            for (title, dx), cell in zip(columns, row):
                fig.text(x + dx, y, str(cell), fontsize=size, color=INK2, va="top")
            y -= row_h
        return y

    @staticmethod
    def color_legend(fig, x, y, size=7.5, theoretical=False):
        items = [(COLOR_HEX[c], COLOR_PT[c]) for c in "WUBRG"] + [(COLORLESS, "incolor")]
        for color, name in items:
            fig.patches.append(_rect(fig, x, y, color))
            fig.text(x + 0.012, y + 0.004, name, fontsize=size, color=INK2, va="center")
            x += 0.012 + 0.0062 * len(name) + 0.012
        fig.text(x, y + 0.004, "multicolorida = dividida" + (" · * e barra clara = nota teórica" if theoretical else ""),
                 fontsize=size, color=MUTED, va="center")


# --- gráficos de barras ---------------------------------------------------------------------

def _style(ax, grid_axis="x"):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(length=0, labelsize=7.5)
    if grid_axis:
        ax.grid(axis=grid_axis, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def _hbars(ax, rows, value_key="poder", label=None, fmt="{:+.1f}", size=7.5, faded=None, color=None, mark=True):
    """Barras horizontais finas, uma por carta, na ordem dada; cor da carta (dividida nas
    multicoloridas) ou uma cor fixa; valor na ponta, asterisco na nota teórica (`mark`)."""
    n = len(rows)
    ys = list(range(n))[::-1]
    for y, row in zip(ys, rows):
        value = row[value_key]
        colors = [color] if color else _hex(row.get("cor"))
        alpha = 0.5 if (faded and faded(row)) else 1.0
        h = 0.64 / len(colors)
        for i, hex_color in enumerate(colors):
            ax.barh(y + 0.32 - h * (i + 0.5), value, height=h * 0.9, color=hex_color, alpha=alpha, linewidth=0)
        star = "*" if mark and row.get("teorica") else ""
        ax.text(value, y, " " + fmt.format(value) + star if value >= 0 else fmt.format(value) + star + " ",
                fontsize=size - 0.5, color=MUTED, va="center", ha="left" if value >= 0 else "right")
    ax.set_yticks(ys)
    ax.set_yticklabels([label(r) if label else r["name"] for r in rows], fontsize=size)
    ax.set_ylim(-0.7, max(n, 1) - 0.3)
    ax.axvline(0, color=AXIS, linewidth=0.8)
    _style(ax)
    values = [r[value_key] for r in rows] + [0.0]
    lo, hi = min(values), max(values)
    pad = (hi - lo) * 0.18 or 1.0
    ax.set_xlim(lo - (pad if lo < 0 else 0), hi + pad)


# --- grafo -----------------------------------------------------------------------------------

def _layout(np, names, edges, seed=7, iterations=250):
    """Fruchterman-Reingold com pesos (numpy): repulsão entre todos os nós, atração ao longo
    das arestas crescendo com o peso (um elo só puxa pouco; dois ou mais, muito), leve
    gravidade ao centro, temperatura decrescente."""
    n = len(names)
    if n == 0:
        return {}
    index = {name: i for i, name in enumerate(names)}
    rng = np.random.default_rng(seed)
    pos = rng.uniform(-1.0, 1.0, (n, 2))
    k = math.sqrt(4.0 / n)
    ei = np.array([(index[a], index[b]) for a, b, _w in edges], dtype=int).reshape(-1, 2)
    ew = np.array([(w - 0.75) ** 2 for _a, _b, w in edges], dtype=float)
    temperature = 0.12
    cooling = temperature / (iterations + 1)
    for _ in range(iterations):
        delta = pos[:, None, :] - pos[None, :, :]
        dist = np.linalg.norm(delta, axis=2)
        np.fill_diagonal(dist, 1.0)
        dist = np.maximum(dist, 0.02)
        disp = (delta / dist[..., None] * (k * k / dist)[..., None]).sum(axis=1)
        if len(ei):
            d = pos[ei[:, 0]] - pos[ei[:, 1]]
            dl = np.maximum(np.linalg.norm(d, axis=1), 0.02)
            pull = d / dl[:, None] * (dl * dl / k * ew)[:, None]
            np.add.at(disp, ei[:, 0], -pull)
            np.add.at(disp, ei[:, 1], pull)
        disp -= pos * 0.04
        length = np.maximum(np.linalg.norm(disp, axis=1), 1e-6)
        pos += disp / length[:, None] * np.minimum(length, temperature)[:, None]
        temperature -= cooling
    pos -= pos.mean(axis=0)
    scale = np.abs(pos).max() or 1.0
    pos /= scale
    return {name: (float(pos[i, 0]), float(pos[i, 1])) for name, i in index.items()}


def _node(ax, x, y, radius, colors, alpha=1.0):
    from matplotlib.patches import Circle, Wedge
    ax.add_patch(Circle((x, y), radius + 0.005, facecolor=SURFACE, edgecolor="none", zorder=3))   # anel de superfície
    if len(colors) == 1:
        ax.add_patch(Circle((x, y), radius, facecolor=colors[0], edgecolor="none", alpha=alpha, zorder=4))
        return
    step = 360.0 / len(colors)
    for i, color in enumerate(colors):
        ax.add_patch(Wedge((x, y), radius, 90 + i * step, 90 + (i + 1) * step, facecolor=color, edgecolor="none",
                           alpha=alpha, zorder=4))


def _place_labels(candidates, pos, sizes, limit, dx=0.26, dy=0.05):
    """Rótulos das cartas mais centrais, pulando os que cairiam sobre um rótulo já posto."""
    placed, out = [], []
    for name in candidates:
        x, y = pos[name]
        y += sizes[name] + 0.012
        if any(abs(x - px) < dx and abs(y - py) < dy for px, py in placed):
            continue
        placed.append((x, y))
        out.append(name)
        if len(out) >= limit:
            break
    return out


def _draw_graph(ax, names, pairs, pos, sizes, colors_of, labels, alpha_of=None):
    """Arestas (mais escuras com mais de um elo), nós com tamanho e cores dados, rótulos."""
    from matplotlib.collections import LineCollection
    import matplotlib.patheffects as pe
    weak = [(pos[p["a"]], pos[p["b"]]) for p in pairs if p["sinergia"] < STRONG_EDGE]
    strong = [(pos[p["a"]], pos[p["b"]]) for p in pairs if p["sinergia"] >= STRONG_EDGE]
    if weak:
        ax.add_collection(LineCollection(weak, colors=AXIS, linewidths=0.2, alpha=0.22, zorder=1))
    if strong:
        ax.add_collection(LineCollection(strong, colors=INK2, linewidths=0.55, alpha=0.32, zorder=2))
    for name in names:
        x, y = pos[name]
        _node(ax, x, y, sizes[name], colors_of(name), alpha_of(name) if alpha_of else 1.0)
    for name in labels:
        x, y = pos[name]
        ax.text(x, y + sizes[name] + 0.012, _cut(name, 28), fontsize=6.5, color=INK, ha="center", va="bottom", zorder=6,
                path_effects=[pe.withStroke(linewidth=2.2, foreground=SURFACE)])
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.1, 1.14)
    ax.set_aspect("equal")
    ax.axis("off")


# --- páginas de capa e leitura -------------------------------------------------------------

def _cover(doc, setmap, sources, ctx, toc):
    code = setmap.set_code
    fig = doc.page(f"{doc.set_name} ({code.upper()}) — documento da coleção",
                   f"Guia de draft, leitura da coleção e mapa de picks · gerado em {doc.today} por mtg draft map {code} --pdf · "
                   f"{sources or 'sem dados: avaliação teórica'}")
    pairs = setmap.pairs()
    coverage = setmap.coverage()
    main_source = next(iter(coverage)) if coverage else "-"
    tiles = [
        ("cartas draftáveis", str(len(setmap.cards)),
         ", ".join(f"{ctx['overview']['raridades'][r]} {RARITY_PT[r]}" for r in RARITY_ORDER)),
        ("pares com elo direto", str(len(pairs)), f"{sum(1 for p in pairs if p['sinergia'] >= STRONG_EDGE)} com mais de um elo"),
        ("fonte do poder", _source(main_source).rstrip("*"), ", ".join(f"{_source(k)} {v}" for k, v in coverage.items())),
        ("arquétipos e ganchos", f"{len(setmap.tagger.archetypes)} + {len(setmap.tagger.hooks)}",
         ", ".join(setmap.tagger.hooks) or "sem ganchos"),
        ("comunidades", str(len(ctx["communities"])),
         f"grupos de 3 cartas ou mais sobre elos de peso ≥ {ctx['community_weight']:g}"),
    ]
    x = 0.04
    for label, value, note in tiles:
        fig.text(x, 0.855, label, fontsize=8, color=INK2, va="top")
        fig.text(x, 0.825, value, fontsize=26, fontweight="semibold", color=INK, va="top")
        for i, part in enumerate(textwrap.wrap(note, 30)[:3]):
            fig.text(x, 0.755 - i * 0.02, part, fontsize=7, color=MUTED, va="top")
        x += 0.185
    fig.text(0.04, 0.675, "Sumário", fontsize=11, fontweight="semibold", color=INK, va="top")
    lines = []
    for part, entries in toc:
        lines.append((part, entries[0][1], True))
        lines += [(f"    {title}", page, False) for title, page in entries[1:]] if len(entries) > 1 else []
    half = math.ceil(len(lines) / 2)
    line_h = 0.0195
    for column, chunk in enumerate((lines[:half], lines[half:])):
        x0 = 0.04 + column * 0.47
        y = 0.645
        for text, page, bold in chunk:
            fig.text(x0, y, _cut(text, 78), fontsize=7.8, color=INK if bold else INK2, va="top",
                     fontweight="semibold" if bold else "normal")
            fig.text(x0 + 0.43, y, str(page), fontsize=7.8, color=MUTED, va="top", ha="right")
            y -= line_h
    doc.close(fig)


def _how_to_read(doc, setmap):
    code = setmap.set_code
    fig = doc.page("Como ler este documento", "Convenções usadas em todas as partes: nota, fonte, elos, grafo e cores.")
    how = [
        "**Partes.** O guia de draft (escrito pelo agente a partir dos dados e da teoria, fonte em drafts/" + code
        + "/guia.md) vem primeiro; depois a leitura da coleção em números, os dez arquétipos, a ordem de pick por "
        "raridade com a tabela completa, o grafo de elos com comunidades e centralidade, os pares com mais sinergia, os "
        "segundos picks de todas as raras e míticas e os limites. Tudo é regenerado por mtg draft map " + code + " --pdf.",
        "**Como ler a nota.** Pontos percentuais de win rate acima da média da fonte da carta (17Lands: GIH WR menos a média "
        "dos usuários; Untapped: idem com a média dele). Asterisco e barra mais clara: nota teórica (Draftsim ou a regra "
        "raridade, remoção e custo), sem amostra de partidas. Raridade não entra na conta: raras e míticas aparecem no alto "
        "porque costumam ter mais poder, e cada pacote traz uma rara ou mítica, cerca de três incomuns e dez comuns. No P1P1 "
        "compare a rara do pacote com a melhor incomum e a melhor comum; do P1P2 em diante a escolha é quase sempre entre "
        "incomuns e comuns.",
        "**Elos e sinergia.** Cada arquétipo e cada gancho é um elo: a payoff pede, o enabler oferece. Duas cartas têm "
        "sinergia direta quando uma pede o que a outra oferece (1 por elo; 0,25 se o enabler é só uma estatística, como "
        "'criatura de custo 2'; 0,5 entre duas payoffs do mesmo par; um quarto se as duas juntas pedem três cores). "
        "Σ é a soma das sinergias de uma carta com toda a coleção. No motor de picks (mtg draft pick), cada unidade "
        "de elo com uma carta já escolhida vale 0,6 ponto, até 3: um elo desempata cartas próximas, não vira carta fraca em bomba.",
        "**Grafo.** Nós são cartas, arestas são elos (só os de peso 1 ou mais). Tamanho do nó = centralidade (passeio "
        "aleatório que prefere parceiras fortes): a carta central é porta de entrada para a coleção. Comunidades são "
        "grupos ligados por mais de um elo e mostram temas que cruzam os dez pares.",
        "**Cores.** Barra e nó levam a cor da carta (multicolorida dividida; incolor cinza) e o rótulo repete a letra da cor "
        "e a raridade (M, R, U, C). Nas tabelas, a coluna 'elos' diz o que a carta pede e oferece.",
    ]
    doc.paragraphs(fig, 0.04, 0.86, 0.92, how, size=9)
    doc.color_legend(fig, 0.04, 0.09, theoretical=True)
    doc.close(fig)


def _numbers(doc, setmap, ctx):
    groups = ctx["overview"]["grupos"]
    fig = doc.page("A coleção em números",
                   "Cartas draftáveis por cor e raridade; criaturas de comum e incomum por custo; remoção de comum e incomum "
                   "(classificação automática pelo texto); palavras-chave mais frequentes.")
    ax = fig.add_axes([0.07, 0.56, 0.40, 0.30])            # cores × raridade (rampa ordinal, uma matiz)
    order = [g for g in COLOR_GROUPS if groups[g]["total"]]
    ys = list(range(len(order)))[::-1]
    left = [0.0] * len(order)
    for rarity in ("common", "uncommon", "rare", "mythic"):
        values = [groups[g][rarity] for g in order]
        ax.barh(ys, values, left=left, height=0.62, color=ORDINAL[rarity], linewidth=0, label=RARITY_PT[rarity])
        for y, v, l in zip(ys, values, left):
            if v >= 4:
                ax.text(l + v / 2, y, str(v), fontsize=6.5, color="#ffffff" if rarity in ("rare", "mythic") else INK,
                        ha="center", va="center")
        left = [l + v for l, v in zip(left, values)]
    ax.set_yticks(ys)
    ax.set_yticklabels([COLOR_PT[g] for g in order], fontsize=8)
    for y, total in zip(ys, left):
        ax.text(total + 0.6, y, f"{int(total)}", fontsize=7, color=MUTED, va="center")
    _style(ax)
    ax.set_xlim(0, max(left) * 1.12)
    ax.legend(loc="lower right", fontsize=7, frameon=False, ncol=4, bbox_to_anchor=(1.0, 1.0))
    ax.set_title("Cartas por cor e raridade", fontsize=9, color=INK, loc="left")
    ax = fig.add_axes([0.60, 0.56, 0.34, 0.30])            # palavras-chave
    rows = [{"name": w, "poder": n, "cor": "-"} for w, n, _top in ctx["overview"]["palavras"][:12]]
    if rows:
        _hbars(ax, rows, fmt="{:.0f}", color=CATEGORICAL[0], size=7.5)
    ax.set_title("Palavras-chave (ocorrências na coleção)", fontsize=9, color=INK, loc="left")
    fig.text(0.07, 0.475, "Criaturas de comum e incomum por custo (1 a 6+)", fontsize=9, color=INK, va="top")
    peak = max([groups[c]["curva_cu"][str(i)] for c in "WUBRG" for i in range(1, 7)] + [1])
    for j, c in enumerate("WUBRG"):                        # curva por cor (pequenos múltiplos)
        ax = fig.add_axes([0.07 + j * 0.082, 0.29, 0.068, 0.125])
        values = [groups[c]["curva_cu"][str(i)] for i in range(1, 7)]
        ax.bar(range(1, 7), values, width=0.7, color=COLOR_HEX[c], linewidth=0)
        for i, v in enumerate(values, 1):
            if v:
                ax.text(i, v + peak * 0.03, str(v), fontsize=6, color=MUTED, ha="center", va="bottom")
        ax.set_ylim(0, peak * 1.3)
        ax.set_xticks(range(1, 7))
        ax.set_xticklabels(["1", "2", "3", "4", "5", "6+"], fontsize=6)
        ax.set_yticks([])
        _style(ax, grid_axis=None)
        ax.set_title(f"{COLOR_PT[c]} · {groups[c]['criaturas_cu']}", fontsize=7.5, color=INK2, loc="left")
    ax = fig.add_axes([0.60, 0.27, 0.34, 0.19])            # remoção C+U por cor
    rows = [{"name": COLOR_PT[g], "poder": len(groups[g]["remocao_cu"]), "cor": g if g in COLOR_HEX else "-"}
            for g in COLOR_GROUPS if groups[g]["total"]]
    _hbars(ax, rows, fmt="{:.0f}", size=7.5)
    ax.set_title("Remoção de comum e incomum por cor", fontsize=9, color=INK, loc="left")
    removal = [f"{COLOR_PT[g]}: {', '.join(groups[g]['remocao_cu'])}" for g in COLOR_GROUPS if groups[g]["remocao_cu"]]
    y = 0.215
    for part in textwrap.wrap(" · ".join(removal), 170)[:4]:
        fig.text(0.07, y, part, fontsize=7, color=MUTED, va="top")
        y -= 0.018
    doc.color_legend(fig, 0.07, 0.10)
    doc.close(fig)


def _reading(doc, setmap, ctx):
    lines = ctx["analysis"]
    fig = doc.page("Leitura da coleção",
                   "O que os números dizem, com a seção da teoria (knowledge/limitado-e-draft.md) que sustenta cada leitura.")
    first = [l for l in lines if not l.startswith(("**Arquétipos", "**Ganchos", "**Grafo"))]
    y = doc.paragraphs(fig, 0.04, 0.87, 0.92, first, size=8.5)
    rest = [l for l in lines if l.startswith(("**Ganchos", "**Grafo"))]
    if y > 0.25:
        doc.paragraphs(fig, 0.04, y, 0.92, rest, size=8.5)
    doc.close(fig)


def _pairs_data(doc, setmap, ctx):
    ratings = setmap.ratings
    base = ratings.baseline
    ranked = sorted(ratings.pairs.items(), key=lambda kv: -kv[1])
    games = {c["short"]: c.get("games") for c in (ratings.snapshot or {}).get("colors", [])}
    fig = doc.page("Os dez pares nos dados",
                   f"{ratings.describe().split(' · ')[0]} · win rate do par menos a média dos usuários ({base:.1%}); "
                   "azul acima da média, vermelho abaixo. Jogos por par à direita.")
    ax = fig.add_axes([0.16, 0.14, 0.56, 0.72])
    names = {s["pair"]: s["name"] for s in ctx["summary"]}
    ys = list(range(len(ranked)))[::-1]
    for y, (pair, wr) in zip(ys, ranked):
        delta = (wr - base) * 100
        ax.barh(y, delta, height=0.6, color=CATEGORICAL[0] if delta >= 0 else CATEGORICAL[7], linewidth=0)
        ax.text(delta + (0.06 if delta >= 0 else -0.06), y, f"{wr:.1%} ({delta:+.1f})", fontsize=7.5, color=MUTED,
                va="center", ha="left" if delta >= 0 else "right")
    ax.set_yticks(ys)
    ax.set_yticklabels([f"{pair} · {_cut(names.get(pair, ''), 36)}" for pair, _wr in ranked], fontsize=8)
    ax.axvline(0, color=AXIS, linewidth=0.8)
    _style(ax)
    span = max(abs((wr - base) * 100) for _p, wr in ranked) * 1.6 or 1
    ax.set_xlim(-span, span)
    ax.set_xlabel("pontos percentuais acima (+) ou abaixo (−) da média", fontsize=7.5, color=INK2)
    fig.text(0.75, 0.86, "jogos", fontsize=8, fontweight="semibold", color=INK, va="top")
    for y, (pair, _wr) in zip(ys, ranked):
        n = games.get(pair)
        fig.text(0.75, 0.14 + (y + 0.5) / len(ranked) * 0.72 - 0.01, f"{n:,}".replace(",", ".") if n else "-",
                 fontsize=8, color=INK2, va="center")
    fig.text(0.83, 0.86, "\n".join(textwrap.wrap(
        "Leitura: o win rate do par mede o deck inteiro (qualidade das comuns, remoção, curva), não a sinergia marcada. "
        f"A diferença entre o melhor e o pior par é de {(ranked[0][1] - ranked[-1][1]) * 100:.1f} pontos. Compare com a "
        "profundidade de cada arquétipo nas páginas seguintes: par forte e raso vence pelas cartas; par fraco e profundo "
        "precisa que a mesa deixe o tema aberto.", 30)), fontsize=7.5, color=INK2, va="top")
    doc.close(fig)


# --- arquétipos ----------------------------------------------------------------------------

def _pips(fig, x, y, pair, size=0.012):
    for i, c in enumerate(pair):
        fig.patches.append(_rect(fig, x + i * (size + 0.003), y, COLOR_HEX.get(c, COLORLESS), w=size, h=size))


def _archetypes_overview(doc, setmap, ctx):
    summary = ctx["summary"]
    fig = doc.page("Os dez arquétipos", "Nome, plano, profundidade (payoffs em comum e incomum), contagens e sinalizadoras. "
                   "Profundo = 6 ou mais payoffs C/U; raso = 3 ou menos, depende de abrir a rara.")
    cols = 5
    w, h = 0.184, 0.40
    for i, s in enumerate(summary[:10]):
        cx = 0.04 + (i % cols) * w
        cy = 0.86 - (i // cols) * (h + 0.02)
        fig.patches.append(_rect(fig, cx, cy - h, "#f3f2ee", w=w - 0.012, h=h * PAGE[1] / PAGE[0]))
        _pips(fig, cx + 0.008, cy - 0.03, s["pair"])
        fig.text(cx + 0.045, cy - 0.012, s["pair"], fontsize=11, fontweight="semibold", color=INK, va="top")
        if s["win_rate"]:
            fig.text(cx + 0.075, cy - 0.014, f"{s['win_rate']:.1%}", fontsize=9, color=INK2, va="top")
        y = cy - 0.05
        for part in textwrap.wrap(s["name"], 26)[:2]:
            fig.text(cx + 0.008, y, part, fontsize=8.5, fontweight="semibold", color=INK, va="top")
            y -= 0.02
        y -= 0.004
        for part in textwrap.wrap(_clean(s["plan"]), 34)[:7]:
            fig.text(cx + 0.008, y, part, fontsize=6.8, color=INK2, va="top")
            y -= 0.0165
        y -= 0.006
        depth = {"profundo": CATEGORICAL[0], "médio": MUTED, "raso": CATEGORICAL[7]}[s["profundidade"]]
        fig.patches.append(_rect(fig, cx + 0.008, y - 0.006, depth, w=0.006, h=0.006))
        fig.text(cx + 0.018, y, f"{s['profundidade']} · {s['payoffs']} payoffs ({s['payoffs_cu']} C/U) · "
                 f"{s['enablers']} enablers", fontsize=6.8, color=INK, va="top")
        y -= 0.02
        if s["top_payoff"]:
            fig.text(cx + 0.008, y, f"melhor payoff: {_cut(s['top_payoff']['name'], 26)} "
                     f"{s['top_payoff']['poder']:+.1f}{_mark(s['top_payoff'])}", fontsize=6.8, color=INK2, va="top")
            y -= 0.017
        if s["sinalizadoras"]:
            for part in textwrap.wrap("sinalizadoras: " + ", ".join(s["sinalizadoras"]), 36)[:3]:
                fig.text(cx + 0.008, y, part, fontsize=6.5, color=MUTED, va="top")
                y -= 0.0155
    doc.close(fig)


def _archetype_page(doc, setmap, ctx, pair_tables):
    by_pair = {s["pair"]: s for s in ctx["summary"]}
    title = " · ".join(f"{t['pair']} {t['name']}" for t in pair_tables)
    fig = doc.page(_cut(title, 95), "Payoffs (pedem o elo) e enablers (oferecem) em ordem de poder, os oito melhores de cada; "
                   "cor da barra = cor da carta; * nota teórica. Listas completas no fim desta parte.")
    for j, table in enumerate(pair_tables):
        s = by_pair[table["pair"]]
        x0 = 0.04 + j * 0.48
        _pips(fig, x0, 0.855, table["pair"])
        wr = f" · par {table['win_rate']:.1%} nos dados" if table["win_rate"] else ""
        fig.text(x0 + 0.04, 0.868, f"{table['pair']} · {table['name']}{wr}", fontsize=10.5, fontweight="semibold",
                 color=INK, va="top")
        y = 0.835
        for part in textwrap.wrap(_clean(table["plan"]), 100)[:3]:
            fig.text(x0, y, part, fontsize=7.5, color=INK2, va="top")
            y -= 0.017
        counts = (f"{s['profundidade']} · {table['total_payoffs']} payoffs ({s['payoffs_cu']} C/U) · "
                  f"{table['total_enablers']} enablers ({s['enablers_cu']} C/U)"
                  + (f" · sinalizadoras: {', '.join(s['sinalizadoras'])}" if s["sinalizadoras"] else ""))
        y -= 0.004
        for part in textwrap.wrap(counts, 108)[:2]:
            fig.text(x0, y, part, fontsize=7, color=MUTED, va="top")
            y -= 0.015
        ax = fig.add_axes([x0 + 0.17, 0.42, 0.26, 0.29])
        if table["payoffs"]:
            _hbars(ax, table["payoffs"], label=lambda e: _label(e, 26), faded=lambda e: e["teorica"])
        ax.set_title(f"Payoffs ({table['total_payoffs']})", fontsize=8.5, color=INK, loc="left")
        ax = fig.add_axes([x0 + 0.17, 0.08, 0.26, 0.29])
        if table["enablers"]:
            _hbars(ax, table["enablers"], label=lambda e: _label(e, 26), faded=lambda e: e["teorica"])
        ax.set_title(f"Enablers ({table['total_enablers']})", fontsize=8.5, color=INK, loc="left")
    doc.close(fig)


def _archetype_lists_flow(ts, setmap):
    """Listas completas de payoffs e enablers por par, em texto corrido."""
    flow = pdf_flow.Flow(ts, title="Arquétipos: listas completas",
                         subtitle="Toda carta marcada em cada par, em ordem de poder (nota e * teórica); C/U = comuns e incomuns.")
    flow.heading("Arquétipos: listas completas", 2)
    for table in setmap.archetype_tables(top=None):
        wr = f" · par {table['win_rate']:.1%} nos dados" if table["win_rate"] else ""
        flow.heading(f"{table['pair']} · {table['name']}{wr}", 3)
        flow.paragraph(table["plan"])

        def names(entries):
            return ", ".join(f"{e['name']} {e['poder']:+.1f}{_mark(e)} ({e['cor']} {RARITY_LETTER.get(e['raridade'], '')})"
                             for e in entries) or "nenhuma"
        flow.paragraph(f"**Payoffs ({table['total_payoffs']}):** {names(table['payoffs'])}")
        flow.paragraph(f"**Enablers ({table['total_enablers']}):** {names(table['enablers'])}")
    return flow


# --- ordem de pick --------------------------------------------------------------------------

def _pick_order_page(doc, setmap, rarity, top=TOP_ORDER):
    rows = setmap.pick_order(rarity)
    shown = rows[:top]
    fig = doc.page(f"Ordem de pick: {RARITY_PT[rarity]} ({len(shown)} de {len(rows)})",
                   "Nota em pontos de win rate acima da média da fonte; cor da barra = cor da carta (dividida nas "
                   "multicoloridas); * e barra clara = nota teórica. Rótulo: posição, carta · cor · raridade; Σ = soma "
                   "das sinergias na coleção. Tabela completa nas páginas seguintes.")
    half = (len(shown) + 1) // 2
    for j, chunk in enumerate((shown[:half], shown[half:])):
        if not chunk:
            continue
        ax = fig.add_axes([0.20 + j * 0.49, 0.10, 0.26, 0.76])
        _hbars(ax, chunk, label=lambda e: f"{e['posicao']:>2}. {_label(e, 30)}" + (f"  Σ{e['elos']:g}" if e["elos"] else ""),
               faded=lambda e: e["teorica"], size=7)
    doc.color_legend(fig, 0.20, 0.06, theoretical=True)
    doc.close(fig)


def _order_tables_flow(ts, setmap):
    """Tabela completa da ordem de pick, uma seção por raridade."""
    flow = pdf_flow.Flow(ts, title="Ordem de pick: tabela completa",
                         subtitle="Nota (fonte), cor, custo, arquétipos (+ = payoff), elos (pede · oferece) e Σ sinergia; * nota teórica.")
    for rarity in RARITY_ORDER:
        rows = setmap.pick_order(rarity)
        if not rows:
            continue
        flow.heading(f"Tabela completa: {RARITY_PT[rarity]} ({len(rows)})", 2)
        flow.table(["#", "nota", "fonte", "cor", "custo", "carta", "arquétipos", "elos", "Σ"],
                   [[r["posicao"], f"{r['poder']:+.1f}{_mark(r)}", _source(r["fonte"]).rstrip("*"), r["cor"], _cost(r),
                     r["name"], r["arquetipos"], _links(r), f"{r['elos']:g}" if r["elos"] else ""] for r in rows])
    return flow


# --- grafo ----------------------------------------------------------------------------------

def _graph_page(doc, setmap, ctx):
    names, pairs, pos, central, sizes, labels, ranked_names = ctx["graph"]
    fig = doc.page("Grafo de elos", f"{len(names)} cartas com pelo menos um elo de peso ≥ {EDGE_MIN:g} e {len(pairs)} arestas "
                   f"(escuras: mais de um elo, peso ≥ {STRONG_EDGE:g}). Tamanho do nó = centralidade; cor = cor da carta; "
                   f"rótulos nas mais centrais sem sobreposição. Sem elo desenhado: {len(setmap.cards) - len(names)} cartas.")
    ax = fig.add_axes([0.02, 0.05, 0.74, 0.84])
    _draw_graph(ax, names, pairs, pos, sizes, lambda n: _hex(setmap.cards[n]["cor"]), labels)
    ranked = [(n, central.get(n, 0)) for n in ranked_names[:18]]
    rows = [(f"{v:g}", _label(setmap.cards[n], 28)) for n, v in ranked]
    doc.table(fig, 0.78, 0.86, [("centr.", 0.0), ("carta", 0.05)], rows, size=7)
    doc.color_legend(fig, 0.04, 0.06)
    doc.close(fig)


def _communities_page(doc, setmap, ctx):
    names, pairs, pos, _central, sizes, _labels, ranked_names = ctx["graph"]
    groups, weight = ctx["communities"], ctx["community_weight"]
    member = {}
    for i, g in enumerate(groups):
        for n in g["cartas"]:
            member[n] = i
    fig = doc.page("Comunidades", f"Propagação de rótulos sobre os pares com peso ≥ {weight:g} (mais de um elo; limiar escolhido "
                   f"entre 1,5, 2 e 2,5 pelo que dá mais grupos); {len(groups)} grupos com 3 cartas ou mais. Mesma posição da "
                   "página anterior; cinza = fora de qualquer grupo.")
    ax = fig.add_axes([0.02, 0.05, 0.66, 0.84])

    def color_of(n):
        i = member.get(n)
        return [CATEGORICAL[i]] if i is not None and i < len(CATEGORICAL) else ["#c3c2b7"]

    _draw_graph(ax, names, pairs, pos, {n: (sizes[n] if n in member else 0.008) for n in names}, color_of,
                _place_labels([n for n in ranked_names if n in member], pos, sizes, 22),
                alpha_of=lambda n: 1.0 if n in member else 0.6)
    y = 0.87
    for i, g in enumerate(groups[:len(CATEGORICAL)]):
        fig.patches.append(_rect(fig, 0.70, y - 0.008, CATEGORICAL[i]))
        colors = "".join(c for c, _n in g["cores"]) or "-"
        fig.text(0.715, y, f"{i + 1} · {g['tamanho']} cartas · cores {colors} · poder médio {g['poder']:+.1f}",
                 fontsize=7.5, fontweight="semibold", color=INK, va="top")
        y -= 0.017
        detail = ("pares " + ", ".join(f"{p} {n}" for p, n in g["pares"]) + " · elos "
                  + ", ".join(f"{l} {n}" for l, n in g["elos"]) + ": " + ", ".join(g["cartas"][:6])
                  + (" …" if g["tamanho"] > 6 else ""))
        for part in textwrap.wrap(detail, 52)[:4]:
            fig.text(0.715, y, part, fontsize=6.8, color=INK2, va="top")
            y -= 0.0145
        y -= 0.01
    if len(groups) > len(CATEGORICAL):
        fig.text(0.715, y, f"+ {len(groups) - len(CATEGORICAL)} grupos menores em cinza", fontsize=7, color=MUTED, va="top")
    doc.close(fig)


def _centrality_page(doc, setmap, ctx):
    central = ctx["graph"][3]
    totals = setmap.partner_totals()
    fig = doc.page("Centralidade e soma das sinergias", "À esquerda, as 25 cartas mais centrais (0 a 100; PageRank com pesos: "
                   "liga parceiras fortes que ligam outras). À direita, as 25 com maior Σ (soma das sinergias diretas na coleção).")
    ax = fig.add_axes([0.21, 0.10, 0.25, 0.76])
    rows = [{**setmap.cards[n], "centr": v} for n, v in sorted(central.items(), key=lambda kv: -kv[1])[:25]]
    _hbars(ax, rows, value_key="centr", label=lambda e: _label(e, 30), fmt="{:.0f}", size=7, mark=False)
    ax.set_title("Centralidade", fontsize=9, color=INK, loc="left")
    ax = fig.add_axes([0.70, 0.10, 0.25, 0.76])
    rows = [{**setmap.cards[n], "soma": v} for n, v in sorted(totals.items(), key=lambda kv: -kv[1])[:25]]
    _hbars(ax, rows, value_key="soma", label=lambda e: _label(e, 30), fmt="{:.0f}", size=7, mark=False)
    ax.set_title("Σ sinergia", fontsize=9, color=INK, loc="left")
    doc.color_legend(fig, 0.21, 0.06)
    doc.close(fig)


# --- pares e segundos picks -----------------------------------------------------------------

def _pairs_flow(ts, setmap, top=TOP_PAIRS):
    pairs = setmap.pairs()
    flow = pdf_flow.Flow(ts, title="Pares de cartas com mais sinergia direta",
                         subtitle=f"{len(pairs)} pares com elo na coleção; os {min(top, len(pairs))} primeiros (sinergia em "
                         "unidades de elo; empate pela soma de poder). Elo entre cartas que juntas pedem três cores vale um quarto.")
    flow.heading("Pares de cartas com mais sinergia direta", 2)
    flow.table(["sinergia", "poder", "carta A", "carta B", "elos"],
               [[f"{p['sinergia']:g}", f"{p['poder']:+.1f}", _label(setmap.cards[p["a"]], 60), _label(setmap.cards[p["b"]], 60),
                 ", ".join(p["elos"])] for p in pairs[:top]])
    return flow


def _follow_ups_flow(ts, setmap, top=6):
    tree = setmap.tree(top=top)
    flow = pdf_flow.Flow(ts, title="Segundos picks de todas as raras e míticas",
                         subtitle="Para cada rara ou mítica, em ordem de poder, as cartas da coleção que o motor mais quer no P1P2 "
                         "(nota = poder + parceiros + o pouco de encaixe do pick 2); ↔ = elo com a primeira.")
    flow.heading("Segundos picks de todas as raras e míticas", 2)
    flow.paragraph(f"Do terceiro pick em diante: `mtg draft map {setmap.set_code} --card \"Primeira\" --card \"Segunda\"`, "
                   "ou o motor ao vivo (`mtg draft watch`, Oráculo).")
    rows = []
    for entry in tree:
        first = entry["primeiro"]
        links = _links(first)
        head = (f"**{first['name']}** · {first['cor']} {RARITY_LETTER.get(first['raridade'], '')} · "
                f"{first['poder']:+.1f}{_mark(first)} {_source(first['fonte']).rstrip('*')}"
                + (f" · {first['arquetipos']}" if first["arquetipos"] else "") + (f" · {links}" if links else ""))
        parts = []
        for row in entry["seguintes"]:
            elo = f" ↔{row['elos'][0][1]:g}" if row.get("elos") else ""
            parts.append(f"{row['total']:+.1f} {row['name']} ({row['cor']}{elo})")
        rows.append([head, " · ".join(parts)])
    flow.table(["primeira escolha", "melhores segundos picks (nota · carta · cor · elo)"], rows)
    return flow


def _limits_page(doc, setmap, sources):
    code = setmap.set_code
    lines = [
        "**Fonte do poder.** " + ", ".join(f"{_source(k)} {v}" for k, v in setmap.coverage().items()) + ". Só o 17Lands mede "
        "partidas com a amostra declarada; o Untapped é de outra data e de outros ranks; a Draftsim e a nota teórica não têm "
        f"amostra. Dados: {sources or 'nenhum (modo teórico)'}.",
        "**Elos.** Vêm de padrões sobre o texto de regras (src/mtg_builder/archetypes/" + code + ".json): marcam pertencimento, "
        "não qualidade. Um elo não transforma carta fraca em bomba; no motor, desempata cartas próximas. mtg draft synergy "
        "mede se a marcação carrega sinal nos dados, quando há dados.",
        "**O que o mapa não vê.** A mesa: cores abertas, o que passou, o que o vizinho pegou. Isso só existe ao vivo "
        "(mtg draft watch, Oráculo). O mapa é a preparação: o que cada carta vale antes do primeiro pacote.",
        "**Remoção e curva.** A classificação de remoção é automática pelo texto e inclui algumas criaturas com efeito de "
        "remoção; confira com mtg card. A leitura de velocidade pela curva é indício, não medida: prevalece o que as "
        "partidas mostrarem.",
        "**Guia.** A primeira parte é o guia escrito pelo agente (drafts/" + code + "/guia.md) na data que ele declara; as partes "
        "seguintes são calculadas a cada geração e podem ter dados mais novos que o guia. Em divergência, vale a data mais recente.",
        f"**Regerar.** mtg draft update {code} e mtg draft map {code} --pdf. Depois de editar o guia, gere de novo: o PDF é o "
        "documento da coleção; o guia em Markdown é só a fonte.",
        "**Teoria.** knowledge/limitado-e-draft.md: §2 avaliação de cartas, §3 prioridades de pick, §4 arquétipos e deck "
        "perfeito, §6 compromisso com cores, §7 construção do deck de 40, §8 parâmetros do formato.",
    ]
    fig = doc.page("Limites e fontes")
    doc.paragraphs(fig, 0.04, 0.87, 0.92, lines, size=9)
    doc.close(fig)


# --- documento -----------------------------------------------------------------------------

def _flow_entries(part, flow):
    """Uma entrada do plano por página planejada; vão ao sumário as seções que começam na página."""
    entries = []
    for page in flow.plan():
        def draw(doc, page=page, subtitle=flow.subtitle):
            fig = doc.page(page["title"], subtitle)
            pdf_flow.draw_page(fig, page)
            doc.close(fig)
        entries.append({"part": part, "titles": list(page["sections"]), "draw": draw})
    return entries


def _entry(part, title, draw):
    return {"part": part, "titles": [title], "draw": draw}


def guide_path(set_code):
    return DRAFTS_DIR / set_code.lower() / "guia.md"


def render(setmap, set_name="", sources="", path=None, guide=None, seed=7):
    """Monta o documento da coleção; devolve (caminho, páginas). `guide` é o Markdown do guia
    (padrão: drafts/<coleção>/guia.md, se existir)."""
    plt, np = _setup()
    from matplotlib.backends.backend_pdf import PdfPages
    code = setmap.set_code
    path = Path(path or DRAFTS_DIR / code / f"{code}.pdf")
    path.parent.mkdir(parents=True, exist_ok=True)
    guide_file = Path(guide) if guide else guide_path(code)
    guide_text = guide_file.read_text("utf-8") if guide_file.exists() else ""
    central = setmap.centrality()
    pairs = [p for p in setmap.pairs() if p["sinergia"] >= EDGE_MIN]
    names = sorted({p["a"] for p in pairs} | {p["b"] for p in pairs})
    pos = _layout(np, names, [(p["a"], p["b"], p["sinergia"]) for p in pairs], seed=seed)
    sizes = {n: 0.010 + 0.036 * math.sqrt(central.get(n, 0) / 100.0) for n in names}
    ranked_names = [n for n, _v in sorted(central.items(), key=lambda kv: -kv[1]) if n in pos]
    labels = _place_labels(ranked_names, pos, sizes, GRAPH_LABELS)
    groups, weight = setmap.communities_auto()
    ctx = {"overview": setmap.overview(), "summary": setmap.archetype_summary(), "communities": groups,
           "community_weight": weight, "analysis": analysis_lines(setmap),
           "graph": (names, pairs, pos, central, sizes, labels, ranked_names)}
    scratch = plt.figure(figsize=PAGE)
    ts = pdf_flow.Typesetter(pdf_flow.matplotlib_measurer(scratch))

    plan = [_entry("Como ler este documento", "Como ler este documento", lambda doc: _how_to_read(doc, setmap))]
    if guide_text:
        guide = pdf_flow.Flow(ts, title="Guia de draft", subtitle=f"Parte 1 · guia escrito pelo agente (fonte: drafts/{code}/guia.md)")
        guide.add_markdown(guide_text)
        plan += _flow_entries("Guia de draft", guide)
    part = "A coleção em números"
    plan.append(_entry(part, "A coleção em números", lambda doc: _numbers(doc, setmap, ctx)))
    plan.append(_entry(part, "Leitura da coleção", lambda doc: _reading(doc, setmap, ctx)))
    if setmap.ratings.pairs and setmap.ratings.baseline:
        plan.append(_entry(part, "Os dez pares nos dados", lambda doc: _pairs_data(doc, setmap, ctx)))
    part = "Os dez arquétipos"
    plan.append(_entry(part, "Visão geral", lambda doc: _archetypes_overview(doc, setmap, ctx)))
    tables = setmap.archetype_tables(top=8)
    for i in range(0, len(tables), 2):
        pair_tables = tables[i:i + 2]
        plan.append(_entry(part, " · ".join(t["pair"] for t in pair_tables),
                           lambda doc, pt=pair_tables: _archetype_page(doc, setmap, ctx, pt)))
    plan += _flow_entries(part, _archetype_lists_flow(ts, setmap))
    part = "Ordem de pick"
    for rarity in RARITY_ORDER:
        if setmap.pick_order(rarity):
            plan.append(_entry(part, f"Barras: {RARITY_PT[rarity]}", lambda doc, r=rarity: _pick_order_page(doc, setmap, r)))
    plan += _flow_entries(part, _order_tables_flow(ts, setmap))
    if names:
        part = "Grafo de elos"
        plan.append(_entry(part, "Grafo de elos", lambda doc: _graph_page(doc, setmap, ctx)))
        plan.append(_entry(part, "Comunidades", lambda doc: _communities_page(doc, setmap, ctx)))
        plan.append(_entry(part, "Centralidade e Σ sinergia", lambda doc: _centrality_page(doc, setmap, ctx)))
    part = "Pares e segundos picks"
    plan += _flow_entries(part, _pairs_flow(ts, setmap))
    plan += _flow_entries(part, _follow_ups_flow(ts, setmap))
    plan.append(_entry("Limites e fontes", "Limites e fontes", lambda doc: _limits_page(doc, setmap, sources)))
    plt.close(scratch)

    toc = []
    for i, entry in enumerate(plan, start=2):
        for title in entry["titles"]:
            if toc and toc[-1][0] == entry["part"]:
                toc[-1][1].append((title, i))
            else:
                toc.append((entry["part"], [(title, i)]))
    with PdfPages(path) as pdf:
        doc = Doc(plt, pdf, code, set_name or code.upper())
        _cover(doc, setmap, sources, ctx, toc)
        for entry in plan:
            entry["draw"](doc)
        info = pdf.infodict()
        info["Title"] = f"{doc.set_name} ({code.upper()}) — documento da coleção"
        info["Subject"] = "MTG Deck Builder · spec 014 · mtg draft map --pdf"
        pages = doc.n
    return path, pages
