#!/usr/bin/env python3
"""Fail if any internal link in docs/ points at a missing file."""

import os
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
PATTERN = re.compile(r'(?:href|src)="([^"#]+)(?:#[^"]*)?"')


def main():
    broken = []
    pages = 0
    for page in DOCS.rglob("*.html"):
        pages += 1
        text = page.read_text(encoding="utf-8")
        for href in PATTERN.findall(text):
            if not href or href.startswith(("http://", "https://", "//", "mailto:", "data:", "/")):
                continue
            target = os.path.normpath(os.path.join(page.parent, href))
            if not os.path.exists(target):
                broken.append(f"{page.relative_to(DOCS.parent)} -> {href}")
    for line in broken:
        print(line)
    print(f"checked {pages} pages, {len(broken)} broken internal links")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
