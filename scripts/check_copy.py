"""Procura trechos copiados de uma fonte nos documentos de knowledge/.

Uso: python scripts/check_copy.py <nome-da-fonte-em-data/fontes> [palavras]
Compara sequências de N palavras (padrão 8) de cada documento com o texto bruto da
fonte e lista as coincidências. Serve para garantir que a base contém conceitos
destilados, não reprodução do original (spec 002).
"""

import re
import sys
from pathlib import Path

from mtg_builder.db import DATA_DIR

ROOT = Path(__file__).resolve().parents[1]


def words(text):
    return re.findall(r"[a-zà-ÿ0-9']+", text.lower())


def main():
    source = DATA_DIR / "fontes" / sys.argv[1]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    source_words = words(" ".join(p.read_text("utf-8") for p in sorted(source.glob("*.txt"))))
    shingles = {tuple(source_words[i:i + size]) for i in range(len(source_words) - size + 1)}

    total = 0
    for doc in sorted((ROOT / "knowledge").rglob("*.md")):
        # As seções de referências citam títulos de capítulos, o que é esperado.
        text = re.sub(r"(?ms)^#+ Referências.*?(?=^#+ |\Z)", "", doc.read_text("utf-8"))
        doc_words = words(text)
        hits = [" ".join(doc_words[i:i + size]) for i in range(len(doc_words) - size + 1)
                if tuple(doc_words[i:i + size]) in shingles]
        total += len(hits)
        for hit in hits:
            print(f"{doc.name}: {hit}")
    print(f"{total} coincidências de {size} palavras")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
