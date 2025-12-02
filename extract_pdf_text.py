from __future__ import annotations

import sys
from pathlib import Path

import pdfplumber


def extract_pdf_text(input_path: str, output_path: str) -> None:
    in_path = Path(input_path)
    out_path = Path(output_path)

    pages_text: list[str] = []

    with pdfplumber.open(in_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            pages_text.append(f"--- page {i} ---\n{text}\n")

    out_path.write_text("\n".join(pages_text), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) != 2:
        print("Usage: extract_pdf_text.py INPUT.pdf OUTPUT.txt", file=sys.stderr)
        return 1

    input_path, output_path = argv
    extract_pdf_text(input_path, output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

