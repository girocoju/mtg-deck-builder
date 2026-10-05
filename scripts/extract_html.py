"""Extrai o texto de um artigo em HTML salvo localmente para data/fontes/<nome>/artigo.txt.

Uso: python scripts/extract_html.py <arquivo.html> <nome>
Pega o maior bloco <article> (ou a página toda, se não houver) e remove marcação.
O texto extraído é material bruto para destilação (spec 002) e fica fora do git.
"""

import html
import re
import sys
from pathlib import Path

from mtg_builder.db import DATA_DIR


def main():
    raw = Path(sys.argv[1]).read_text("utf-8", errors="replace")
    articles = re.findall(r"<article\b.*?</article>", raw, flags=re.S)
    body = max(articles, key=len) if articles else raw
    body = re.sub(r"<(script|style|svg|noscript|template)\b.*?</\1>", " ", body, flags=re.S)
    body = re.sub(r"<h[1-6][^>]*>", "\n\n## ", body)
    body = re.sub(r"<li[^>]*>", "\n- ", body)
    body = re.sub(r"</t[dh]>", " | ", body)
    body = re.sub(r"<(p|tr|br|div)\b[^>]*>", "\n", body)
    text = html.unescape(re.sub(r"<[^>]+>", "", body))
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
    out = DATA_DIR / "fontes" / sys.argv[2]
    out.mkdir(parents=True, exist_ok=True)
    (out / "artigo.txt").write_text(text, encoding="utf-8")
    print(f"{len(text)} caracteres em {out / 'artigo.txt'}")


if __name__ == "__main__":
    main()
