"""Extrai o texto de um PDF para data/fontes/<nome>/, um arquivo por página.

Uso: python scripts/extract_pdf.py <arquivo.pdf> [nome]
Requer: pip install -e ".[knowledge]"
O texto extraído é material bruto para destilação (spec 002) e fica fora do git.
"""

import sys
from pathlib import Path

from pypdf import PdfReader

from mtg_builder.db import DATA_DIR


def main():
    pdf = Path(sys.argv[1])
    name = sys.argv[2] if len(sys.argv) > 2 else pdf.stem
    out = DATA_DIR / "fontes" / name
    out.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(pdf)
    for number, page in enumerate(reader.pages, start=1):
        (out / f"p{number:03d}.txt").write_text(page.extract_text() or "", encoding="utf-8")
    print(f"{len(reader.pages)} páginas em {out}")


if __name__ == "__main__":
    main()
