import pytest

from mtg_builder import pdf_flow

GUIDE = """# Coleção Teste (TST) — guia

- **Dados:** fonte de `teste`, coletados em 2026-01-01. Linha de continuação do item
  que deve ser colada ao item anterior.
- Segundo item com [um link](arquivo.md) no meio.

## Visão geral

Parágrafo com **negrito** e `código`. Segunda linha do mesmo
parágrafo.

| Cor | Comuns | Observação |
| --- | --- | --- |
| Azul | 10 | **melhor** cor |
| Verde | 9 | fraca |

### Subseção

1. Primeiro passo
2. Segundo passo

```
mtg draft update tst
```

## Limites

Texto final.
"""


def test_inline_runs_and_plain():
    runs = pdf_flow.inline_runs("a **b** `c` [d](x.md)")
    assert runs == [("a ", False, False), ("b", True, False), (" ", False, False), ("c", False, True), (" d", False, False)]
    assert pdf_flow.plain("**x** `y`") == "x y"


def test_parse_markdown_blocks():
    blocks = pdf_flow.parse_markdown(GUIDE)
    kinds = [b["kind"] for b in blocks]
    assert kinds == ["heading", "bullet", "bullet", "heading", "paragraph", "table", "heading", "bullet", "bullet", "code",
                     "heading", "paragraph"]
    assert blocks[0]["level"] == 1 and blocks[3]["level"] == 2 and blocks[6]["level"] == 3
    assert blocks[1]["text"].endswith("colada ao item anterior.") and blocks[1]["marker"] == "•"
    assert blocks[4]["text"] == "Parágrafo com **negrito** e `código`. Segunda linha do mesmo parágrafo."
    assert blocks[5]["headers"] == ["Cor", "Comuns", "Observação"] and blocks[5]["rows"] == [["Azul", "10", "**melhor** cor"], ["Verde", "9", "fraca"]]
    assert blocks[7]["marker"] == "1." and blocks[8]["marker"] == "2." and blocks[9]["lines"] == ["mtg draft update tst"]


def test_wrap_and_plan_pages():
    ts = pdf_flow.Typesetter(pdf_flow.approx_measurer)
    lines = ts.wrap([("palavra " * 40, False, False)], 8.6, 0.2)
    assert len(lines) > 1 and all(x <= 0.2 for line in lines for x, _t, _b, _c in line)
    flow = pdf_flow.Flow(ts).add_markdown(GUIDE)
    assert flow.title == "Coleção Teste (TST) — guia"
    pages = flow.plan()
    sections = [s for p in pages for s in p["sections"]]
    assert sections == ["Coleção Teste (TST) — guia", "Visão geral", "Limites"]                 # toda seção aparece uma vez
    assert pages[0]["title"] == "Coleção Teste (TST) — guia" and "Visão geral" in pages[0]["sections"]   # página pouco usada: segue nela
    kinds = [laid["kind"] for _y, laid in pages[0]["blocks"]]
    assert kinds[:9] == ["bullet", "bullet", "heading", "paragraph", "table", "heading", "bullet", "bullet", "code"]
    table = next(laid for _y, laid in pages[0]["blocks"] if laid["kind"] == "table")
    assert len(table["rows"]) == 2 and len(table["xs"]) == 3 and abs(sum(table["widths"]) - pdf_flow.WIDTH) < 1e-9
    assert all(y >= pdf_flow.BOTTOM - 1e-9 for p in pages for y, _laid in p["blocks"])
    strict = pdf_flow.Flow(ts).add_markdown(GUIDE).plan(merge_below=0.0)
    assert [p["title"] for p in strict] == ["Coleção Teste (TST) — guia", "Visão geral", "Limites"]   # sem fusão: página por ##
    header = pdf_flow.Flow(ts)._lay_row(["Win rate", "x"], [0.0, 0.3], [0.3, 0.3], bold=True)
    assert all(bold for line in header["cells"][0] for _x, _t, bold, _c in line)                  # negrito medido como negrito


def test_long_table_splits_with_header_repeated():
    ts = pdf_flow.Typesetter(pdf_flow.approx_measurer)
    flow = pdf_flow.Flow(ts, title="Tabela")
    flow.heading("Tabela longa", 2)
    flow.table(["#", "carta"], [[i, f"Carta {i}"] for i in range(120)])
    pages = flow.plan()
    assert len(pages) >= 3 and pages[1]["title"] == "Tabela longa (continuação)"
    chunks = [laid for p in pages for _y, laid in p["blocks"] if laid["kind"] == "table"]
    assert sum(len(c["rows"]) for c in chunks) == 120 and all(c["header"]["cells"] for c in chunks)


def test_draw_page_with_matplotlib(tmp_path):
    pytest.importorskip("matplotlib")
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib import pyplot as plt
    fig = plt.figure(figsize=pdf_flow.PAGE)
    ts = pdf_flow.Typesetter(pdf_flow.matplotlib_measurer(fig))
    assert 0 < ts.width("palavra", False, False, 8.6) < 0.1 and ts.width("palavra", True, False, 8.6) > 0
    pages = pdf_flow.Flow(ts).add_markdown(GUIDE).plan()
    pdf_flow.draw_page(fig, pages[0])
    out = tmp_path / "pagina.pdf"
    fig.savefig(out)
    plt.close(fig)
    assert out.stat().st_size > 1000
