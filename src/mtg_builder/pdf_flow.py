"""Texto corrido e tabelas paginados para os PDFs do projeto (spec 014).

Um subconjunto de Markdown (títulos `#`/`##`/`###`, parágrafos, listas com `-` e `1.`,
tabelas `|`, blocos de código, `**negrito**`, `código` em linha e links) vira blocos;
`Flow.plan()` distribui os blocos em páginas, começando página nova a cada `##` (que vira o
título da página) e quebrando tabelas longas com o cabeçalho repetido; `draw_page()` desenha
uma página planejada numa figura do matplotlib. A medida do texto vem de uma função
`measure(texto, negrito, código, tamanho)` em fração da largura da página: a padrão usa o
renderizador do matplotlib (`matplotlib_measurer`), e os testes passam uma aproximação por
caracteres (`approx_measurer`). Assim o número de páginas é conhecido antes de desenhar, e
a capa pode trazer o sumário com as páginas certas.
"""

import re

PAGE = (11.69, 8.27)                      # A4 paisagem, polegadas
LEFT, WIDTH, TOP, BOTTOM = 0.05, 0.90, 0.885, 0.07
INK, INK2, MUTED, ZEBRA, RULE, CODE_BG = "#0b0b0b", "#52514e", "#898781", "#f3f2ee", "#e1e0d9", "#f0efec"
SIZE = {"body": 8.6, "table": 7.2, "h1": 15, "h2": 12.5, "h3": 10.2, "code": 7.6}
GAP = {"paragraph": 0.6, "heading": 0.9, "table": 0.8, "code": 0.8}   # em linhas do corpo, depois do bloco
BULLET_INDENT, MARKER_WIDTH = 0.012, 0.02
CELL_PAD = 0.004
TABLE_CAP, TABLE_MIN = 0.42, 0.055       # largura máxima e mínima de uma coluna (fração da página)
MERGE_BELOW = 0.35                       # `##` segue na mesma página se ela usou menos que isto da altura


def line_height(size):
    return size * 1.45 / 72 / PAGE[1]


# --- Markdown → blocos --------------------------------------------------------------------------

def inline_runs(text):
    """[(texto, negrito, código)] a partir de `**negrito**`, `código` e `[texto](link)`."""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    runs, bold, code, buffer = [], False, False, []

    def flush():
        if buffer:
            runs.append(("".join(buffer), bold, code))
            buffer.clear()

    i = 0
    while i < len(text):
        if text.startswith("**", i):
            flush()
            bold = not bold
            i += 2
        elif text[i] == "`":
            flush()
            code = not code
            i += 1
        else:
            buffer.append(text[i])
            i += 1
    flush()
    return [r for r in runs if r[0]]


def plain(text):
    return "".join(run[0] for run in inline_runs(text))


def parse_markdown(text):
    """Blocos: {"kind": heading|paragraph|bullet|table|code, ...}. Linhas de continuação de
    um item de lista (indentadas) são coladas ao item; parágrafos juntam linhas seguidas."""
    blocks, paragraph, code, table = [], [], None, None

    def close_paragraph():
        if paragraph:
            blocks.append({"kind": "paragraph", "text": " ".join(s.strip() for s in paragraph)})
            paragraph.clear()

    def close_table():
        nonlocal table
        if table:
            blocks.append(table)
            table = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if code is not None:
            if line.strip().startswith("```"):
                blocks.append({"kind": "code", "lines": code})
                code = None
            else:
                code.append(raw.rstrip("\n"))
            continue
        if line.strip().startswith("```"):
            close_paragraph()
            close_table()
            code = []
            continue
        stripped = line.strip()
        if not stripped:
            close_paragraph()
            close_table()
            continue
        if stripped.startswith("|"):
            close_paragraph()
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if table is None:
                table = {"kind": "table", "headers": cells, "rows": []}
            elif all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c) and any(cells):
                continue
            else:
                table["rows"].append(cells)
            continue
        close_table()
        heading = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if heading:
            close_paragraph()
            blocks.append({"kind": "heading", "level": len(heading.group(1)), "text": heading.group(2).strip()})
            continue
        item = re.match(r"^([-*]|\d+\.)\s+(.*)$", stripped)
        if item and not line.startswith((" ", "\t")):
            close_paragraph()
            marker = item.group(1)
            blocks.append({"kind": "bullet", "marker": "•" if marker in "-*" else marker, "text": item.group(2)})
            continue
        if line.startswith((" ", "\t")) and blocks and blocks[-1]["kind"] == "bullet" and not paragraph:
            blocks[-1]["text"] += " " + stripped          # continuação do item
            continue
        paragraph.append(stripped)
    close_paragraph()
    close_table()
    if code is not None:
        blocks.append({"kind": "code", "lines": code})
    return blocks


# --- medida e quebra de texto -------------------------------------------------------------------

def approx_measurer(text, bold, code, size):
    """Aproximação por caracteres (testes e ausência de renderizador): 0,52 em por caractere,
    0,6 em no código."""
    factor = 0.6 if code else 0.52 * (1.06 if bold else 1.0)
    return len(text) * size * factor / 72 / PAGE[0]


def matplotlib_measurer(fig, mono="DejaVu Sans Mono"):
    """Mede com o renderizador da figura (Agg), direto pela fonte, sem criar artistas; cache
    por (texto, negrito, código, tamanho) e por propriedades de fonte."""
    from matplotlib.font_manager import FontProperties
    renderer = fig.canvas.get_renderer()
    page_width = fig.bbox.width
    cache, fonts = {}, {}

    def measure(text, bold, code, size):
        key = (text, bold, code, size)
        if key not in cache:
            font_key = (bold, code, size)
            if font_key not in fonts:
                fonts[font_key] = FontProperties(family=mono if code else None, weight="semibold" if bold else "normal",
                                                 size=size * (0.92 if code else 1.0))
            width, _height, _descent = renderer.get_text_width_height_descent(text, fonts[font_key], ismath=False)
            cache[key] = width / page_width
        return cache[key]

    return measure


class Typesetter:
    def __init__(self, measure=approx_measurer):
        self.measure = measure

    def width(self, text, bold, code, size):
        return self.measure(text, bold, code, size) if text else 0.0

    def wrap(self, runs, size, width):
        """Linhas de [(x, texto, negrito, código)] que cabem em `width` (fração da página)."""
        lines, line, x = [], [], 0.0
        for text, bold, code in runs:
            for token in re.findall(r"\S+\s*|\s+", text):
                word, trailing = token.rstrip(), token[len(token.rstrip()):]
                w_word = self.width(word, bold, code, size)
                if line and x + w_word > width + 1e-9:
                    lines.append(line)
                    line, x = [], 0.0
                    if not word:
                        continue
                if word or trailing:
                    line.append((x, word + trailing, bold, code))
                    x += w_word + self.width(trailing, bold, code, size)
        if line:
            lines.append(line)
        return lines or [[]]


# --- planejamento em páginas --------------------------------------------------------------------

class Flow:
    """Acumula blocos e os distribui em páginas de altura `TOP - BOTTOM`."""

    def __init__(self, typesetter=None, title="", subtitle=""):
        self.ts = typesetter or Typesetter()
        self.blocks = []
        self.title, self.subtitle = title, subtitle

    def add_markdown(self, text, skip_title=True):
        for block in parse_markdown(text):
            if skip_title and block["kind"] == "heading" and block["level"] == 1:
                self.title = self.title or plain(block["text"])
                continue
            self.blocks.append(block)
        return self

    def heading(self, text, level=2):
        self.blocks.append({"kind": "heading", "level": level, "text": text})
        return self

    def paragraph(self, text):
        self.blocks.append({"kind": "paragraph", "text": text})
        return self

    def bullet(self, text, marker="•"):
        self.blocks.append({"kind": "bullet", "marker": marker, "text": text})
        return self

    def table(self, headers, rows):
        self.blocks.append({"kind": "table", "headers": [str(h) for h in headers], "rows": [[str(c) for c in r] for r in rows]})
        return self

    # --- layout -------------------------------------------------------------------------------

    def _lay_text(self, block):
        size = SIZE["body"]
        indent = BULLET_INDENT + MARKER_WIDTH if block["kind"] == "bullet" else 0.0
        lines = self.ts.wrap(inline_runs(block["text"]), size, WIDTH - indent)
        lh = line_height(size)
        return {"kind": block["kind"], "lines": lines, "size": size, "indent": indent, "marker": block.get("marker", ""),
                "height": len(lines) * lh + GAP["paragraph"] * lh}

    def _lay_heading(self, block):
        size = SIZE[f"h{min(block['level'], 3)}"]
        lines = self.ts.wrap([(plain(block["text"]), True, False)], size, WIDTH)
        lh = line_height(size)
        return {"kind": "heading", "level": block["level"], "lines": lines, "size": size, "indent": 0.0,
                "height": len(lines) * lh + GAP["heading"] * line_height(SIZE["body"])}

    def _lay_code(self, block):
        size = SIZE["code"]
        lh = line_height(size)
        return {"kind": "code", "lines": block["lines"], "size": size,
                "height": (len(block["lines"]) + 0.6) * lh + GAP["code"] * line_height(SIZE["body"])}

    def _table_columns(self, block):
        size = SIZE["table"]
        n = len(block["headers"])
        rows = [block["headers"]] + block["rows"]
        need = []
        for j in range(n):
            widest = max((self.ts.width(plain(r[j]), False, False, size) for r in rows if j < len(r) and r[j]), default=0.0)
            need.append(min(max(widest + 2 * CELL_PAD, TABLE_MIN), TABLE_CAP))
        total = sum(need) or 1.0
        widths = [WIDTH * w / total for w in need]
        xs, x = [], 0.0
        for w in widths:
            xs.append(x)
            x += w
        return xs, widths

    def _lay_row(self, cells, xs, widths, bold=False):
        size = SIZE["table"]
        lines = []
        for j in range(len(xs)):
            if j < len(cells) and cells[j]:
                runs = [(t, True if bold else b, c) for t, b, c in inline_runs(cells[j])]   # negrito antes de medir
                lines.append(self.ts.wrap(runs, size, widths[j] - 2 * CELL_PAD))
            else:
                lines.append([[]])
        height = max(len(cell) for cell in lines) * line_height(size) + 2 * CELL_PAD * PAGE[0] / PAGE[1]
        return {"cells": lines, "height": height}

    def plan(self, top=TOP, bottom=BOTTOM, merge_below=MERGE_BELOW):
        """[{title, subtitle, sections, blocks: [(y, laid)]}]. Cada `##` é uma seção: começa
        página nova e dá o título, a não ser que a página atual tenha usado menos de
        `merge_below` da altura (então a seção segue na mesma página, como título em linha).
        `sections` lista as seções que começam em cada página (para o sumário)."""
        pages, current, y = [], None, top
        title = self.title

        def new_page(page_title, cont=False):
            nonlocal current, y
            current = {"title": page_title + (" (continuação)" if cont else ""), "subtitle": self.subtitle,
                       "sections": [] if cont else [page_title], "blocks": []}
            pages.append(current)
            y = top

        def place(laid):
            nonlocal y
            if current is None:
                new_page(title)
            if y - laid["height"] < bottom and current["blocks"]:
                new_page(current["title"].replace(" (continuação)", ""), cont=True)
            current["blocks"].append((y, laid))
            y -= laid["height"]

        for block in self.blocks:
            if block["kind"] == "heading" and block["level"] <= 2:
                title = plain(block["text"])
                if current is None:
                    new_page(title)
                elif not current["blocks"]:
                    current["title"], current["sections"] = title, [title]
                elif (top - y) < merge_below * (top - bottom):
                    current["sections"].append(title)
                    place(self._lay_heading({"kind": "heading", "level": 2, "text": title}))
                else:
                    new_page(title)
                continue
            if block["kind"] == "heading":
                place(self._lay_heading(block))
            elif block["kind"] in ("paragraph", "bullet"):
                place(self._lay_text(block))
            elif block["kind"] == "code":
                place(self._lay_code(block))
            elif block["kind"] == "table":
                self._place_table(block, place, lambda: y, bottom, top)
        return pages

    def _place_table(self, block, place, current_y, bottom, top):
        xs, widths = self._table_columns(block)
        header = self._lay_row(block["headers"], xs, widths, bold=True)
        rows = [self._lay_row(r, xs, widths) for r in block["rows"]]
        gap = GAP["table"] * line_height(SIZE["body"])
        i = 0
        while i < len(rows) or (i == 0 and not rows):
            available = current_y() - bottom
            if available < header["height"] + (rows[i]["height"] if i < len(rows) else 0) + gap:
                available = top - bottom           # vai para a página seguinte: `place` cuida da quebra
            chunk, used = [], header["height"] + gap
            while i < len(rows) and used + rows[i]["height"] <= available:
                chunk.append(rows[i])
                used += rows[i]["height"]
                i += 1
            if not chunk and i < len(rows):        # linha maior que a página: entra sozinha
                chunk.append(rows[i])
                used += rows[i]["height"]
                i += 1
            place({"kind": "table", "xs": xs, "widths": widths, "header": header, "rows": chunk, "height": used})
            if not rows:
                break


# --- desenho ------------------------------------------------------------------------------------

def _draw_lines(fig, lines, x0, y, size, color=INK2, mono="DejaVu Sans Mono"):
    lh = line_height(size)
    for line in lines:
        for x, text, bold, code in line:
            fig.text(x0 + x, y, text, fontsize=size * (0.92 if code else 1.0), color=INK if bold else color, va="top",
                     fontweight="semibold" if bold else "normal", family=mono if code else None)
        y -= lh
    return y


def draw_page(fig, page):
    """Desenha os blocos planejados de uma página (sem cabeçalho nem rodapé)."""
    from matplotlib.patches import Rectangle
    for y, laid in page["blocks"]:
        kind = laid["kind"]
        if kind == "heading":
            _draw_lines(fig, laid["lines"], LEFT, y, laid["size"], color=INK)
        elif kind in ("paragraph", "bullet"):
            if kind == "bullet":
                fig.text(LEFT + BULLET_INDENT, y, laid["marker"], fontsize=laid["size"], color=INK2, va="top")
            _draw_lines(fig, laid["lines"], LEFT + laid["indent"], y, laid["size"])
        elif kind == "code":
            lh = line_height(laid["size"])
            height = (len(laid["lines"]) + 0.6) * lh
            fig.patches.append(Rectangle((LEFT, y - height), WIDTH, height, transform=fig.transFigure,
                                         facecolor=CODE_BG, edgecolor="none"))
            yy = y - lh * 0.3
            for line in laid["lines"]:
                fig.text(LEFT + 0.006, yy, line, fontsize=laid["size"], color=INK, va="top", family="DejaVu Sans Mono")
                yy -= lh
        elif kind == "table":
            _draw_table(fig, laid, y, Rectangle)


def _draw_table(fig, laid, y, Rectangle):
    size = SIZE["table"]
    pad_y = CELL_PAD * PAGE[0] / PAGE[1]
    header = laid["header"]
    fig.patches.append(Rectangle((LEFT, y - header["height"]), WIDTH, 0.0012, transform=fig.transFigure,
                                 facecolor=MUTED, edgecolor="none"))
    for x, cell in zip(laid["xs"], header["cells"]):
        _draw_lines(fig, cell, LEFT + x + CELL_PAD, y - pad_y, size, color=INK)
    y -= header["height"]
    for i, row in enumerate(laid["rows"]):
        if i % 2 == 1:
            fig.patches.append(Rectangle((LEFT, y - row["height"]), WIDTH, row["height"], transform=fig.transFigure,
                                         facecolor=ZEBRA, edgecolor="none"))
        for x, cell in zip(laid["xs"], row["cells"]):
            _draw_lines(fig, cell, LEFT + x + CELL_PAD, y - pad_y, size)
        y -= row["height"]
    fig.patches.append(Rectangle((LEFT, y), WIDTH, 0.0008, transform=fig.transFigure, facecolor=RULE, edgecolor="none"))
