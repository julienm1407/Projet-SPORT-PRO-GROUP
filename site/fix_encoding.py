#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Normalize site files to UTF-8.

HTML/CSS were often saved as Windows-1252 while pages declare charset=UTF-8.
Run after any edit to index.html:  python3 fix_encoding.py
"""
from __future__ import annotations

from pathlib import Path

SITE = Path(__file__).parent
TARGETS = (
    SITE / "index.html",
    SITE / "css" / "styles.css",
)

CONTROL_CHAR = "\u009d"
ETAPE_01 = "\u00c9tape 01"

REPLACEMENTS: list[tuple[str, str]] = [
    (CONTROL_CHAR + " premi\u00e8re vue", "\u00c0 premi\u00e8re vue"),
    (CONTROL_CHAR + " premi\u00e8re", "\u00c0 premi\u00e8re"),
    ("\u00e9 premi\u00e8re vue", "\u00c0 premi\u00e8re vue"),
    ("\u00e9 premi\u00e8re", "\u00c0 premi\u00e8re"),
    ("A premi\u00e8re vue", "\u00c0 premi\u00e8re vue"),
    ("a premi\u00e8re vue", "\u00c0 premi\u00e8re vue"),
    ("\u00e9 travers", "\u00e0 travers"),
    ("toujours \u00e9 cr\u00e9er", "toujours \u00e0 cr\u00e9er"),
    ("exp\u00e9rience \u00e9 il", "exp\u00e9rience \u2014 il"),
    ("YouTube \u00e9 chaque", "YouTube \u2014 chaque"),
    ("handball \u00e9 le", "handball \u2014 le"),
    ("Marseille \u00e9 aboutissement", "Marseille \u2014 aboutissement"),
    ("partenaire \u00e9 organisation", "partenaire \u2014 organisation"),
    ("\u00e9quipements \u00e9 elle", "\u00e9quipements \u2014 elle"),
    ("Sport Pro Group \u00e9 <a", "Sport Pro Group \u2014 <a"),
    ("Sport Pro Group \u00e9 elle", "Sport Pro Group \u2014 elle"),
    ("paysage \u00e9 Sport", "paysage \u2014 Sport"),
    ("emailing \u00e9 cliquer", "emailing \u2014 cliquer"),
    ("&raquo; \u00e9 Xavier", "&raquo; \u2014 Xavier"),
    ("</strong> \u00e9 Xavier", "</strong> \u2014 Xavier"),
    ("au-del\u00e9", "au-del\u00e0"),
    ("M\u00e9diath\u00e9que", "M\u00e9diath\u00e8que"),
    ("\u00e9cosyst\u00e9me", "\u00e9cosyst\u00e8me"),
    ("\u00e9QUIPEPS", "\u00c9QUIPEPS"),
    ("<h3>\u00e9cosyst\u00e8me", "<h3>\u00c9cosyst\u00e8me"),
    ("<p>\u00e9cosyst\u00e8me", "<p>\u00c9cosyst\u00e8me"),
    ("<span>\u00e9tablissements</span>", "<span>\u00c9tablissements</span>"),
    ("r\u00e9le", "r\u00f4le"),
    ("o\u00e9 ", "o\u00f9 "),
    ("o\u00e9 le", "o\u00f9 le"),
    (" \u2014  Sport", " \u2014 Sport"),
    ("il il revient", "il revient"),
    ("Preuve sociale sociale", "Preuve sociale"),
    ("sont l\u00e9", "sont l\u00e0"),
    ("premi\u00e9re", "premi\u00e8re"),
    ("motion.div", "div"),
]


def load_text(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    try:
        return data.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        for enc in ("cp1252", "latin-1"):
            try:
                return data.decode(enc), enc
            except UnicodeDecodeError:
                continue
        return data.decode("utf-8", errors="replace"), "replace"


def fix_text(text: str) -> tuple[str, int]:
    count = 0
    for old, new in REPLACEMENTS:
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            count += n
    if CONTROL_CHAR in text:
        n = text.count(CONTROL_CHAR)
        text = text.replace(CONTROL_CHAR, "\u2014")
        count += n
    return text, count


def normalize_file(path: Path) -> None:
    if not path.is_file():
        return
    text, source_enc = load_text(path)
    text, n_fix = fix_text(text)
    path.write_text(text, encoding="utf-8")
    path.read_bytes().decode("utf-8")
    print(f"{path.name}: {source_enc} -> utf-8 ({n_fix} replacement(s))")


def main() -> None:
    for path in TARGETS:
        normalize_file(path)

    html = (SITE / "index.html").read_text(encoding="utf-8")
    warnings = []
    for needle in ("\u00e9 premi\u00e8re", CONTROL_CHAR, "\ufffd", "\u00e9cosyst\u00e9me", "o\u00e9 ", "au-del\u00e9"):
        if needle in html:
            warnings.append(repr(needle))
    if warnings:
        print("WARNING: still contains:", ", ".join(warnings))
        return
    if ETAPE_01 not in html:
        print("WARNING: step labels missing")
        return
    print("Verification OK.")


if __name__ == "__main__":
    main()
