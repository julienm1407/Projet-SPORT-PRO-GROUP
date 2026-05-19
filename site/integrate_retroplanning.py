#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert retroplanning section, fix nav/steps, restore truncated tail."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
INDEX = ROOT / "index.html"
FRAGMENT = ROOT / "_retroplanning_fragment.html"
TAIL_FILE = ROOT / "_site_tail.html"

NAV = (
    '      <nav class="nav-quick" aria-label="Navigation rapide">\n'
    '        <a href="#accueil">01 Accueil</a>\n'
    '        <a href="#parcours">02 Parcours</a>\n'
    '        <a href="#introduction">03 Intro</a>\n'
    '        <a href="#concept">04 Concept</a>\n'
    '        <a href="#produits">05 Produits</a>\n'
    '        <a href="#xavier">06 Xavier</a>\n'
    '        <a href="#video">07 Vid\u00e9o</a>\n'
    '        <a href="#email">08 Email</a>\n'
    '        <a href="#reseaux">09 R\u00e9seaux</a>\n'
    '        <a href="#retroplanning">10 Planning</a>\n'
    '        <a href="#unss">11 UNSS</a>\n'
    '        <a href="#mediatheque">12 M\u00e9diath\u00e8que</a>\n'
    '        <a href="#conclusion">13 Synth\u00e8se</a>\n'
    "      </nav>"
)

STEP_08 = "<p class=\"section-phase\">\u00c9tape 08 \u00b7 Email</p>"
STEP_09 = "<p class=\"section-phase\">\u00c9tape 09 \u00b7 R\u00e9seaux</p>"
STEP_10 = "<p class=\"section-phase\">\u00c9tape 10 \u00b7 R\u00e9troplanning</p>"
STEP_11 = "<p class=\"section-phase\">\u00c9tape 11 \u00b7 UNSS</p>"
FLOW_CARD = (
    '          <article class="flow-detail-card"><h3>R\u00e9troplanning</h3>'
    "<p>Calendrier V3 (ao\u00fbt\u2013octobre) : sept phases, cr\u00e9neaux et objectifs par plateforme.</p></article>\n"
)


def load_index() -> str:
    raw = INDEX.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def strip_motion(html: str) -> str:
    return html.replace("motion.div", "div")


def retro_section() -> str:
    frag = strip_motion(FRAGMENT.read_text(encoding="utf-8"))
    frag = re.sub(
        r"<p class=\"section-phase\">.*?</p>",
        STEP_10,
        frag,
        count=1,
    )
    return frag.strip() + "\n\n"


def patch_nav(text: str) -> str:
    return re.sub(
        r"<nav class=\"nav-quick\"[^>]*>.*?</nav>",
        NAV,
        text,
        count=1,
        flags=re.DOTALL,
    )


def insert_retro(text: str) -> str:
    if 'id="retroplanning"' in text:
        return text
    marker = '    <section id="unss">'
    if marker not in text:
        raise SystemExit("unss section not found")
    return text.replace(marker, retro_section() + marker, 1)


def renumber_steps(text: str) -> str:
    if 'id="email"' in text and "\u00c9tape 08" not in text:
        text = re.sub(
            r'(<section id="email">\s*<div class="section-inner">)\s*<p class="section-label">',
            r"\1\n        " + STEP_08 + "\n        <p class=\"section-label\">",
            text,
            count=1,
        )
    if 'id="reseaux"' in text and "\u00c9tape 09" not in text:
        text = re.sub(
            r'(<section id="reseaux"[^>]*>\s*<div class="section-inner">)\s*<p class="section-label">',
            r"\1\n        " + STEP_09 + "\n        <p class=\"section-label\">",
            text,
            count=1,
        )
    text = re.sub(
        r'<p class="section-phase">[^<]*UNSS</p>',
        STEP_11,
        text,
        count=1,
    )
    return text


def add_flow_retro(text: str) -> str:
    if "R\u00e9troplanning</h3>" in text and "flow-detail-card" in text:
        return text
    return text.replace(
        '<article class="flow-detail-card"><h3>Terrain &amp; UNSS</h3>',
        FLOW_CARD + '          <article class="flow-detail-card"><h3>Terrain &amp; UNSS</h3>',
        1,
    )


def restore_tail(text: str) -> str:
    if 'id="mediatheque"' in text and "</html>" in text:
        return text
    raw = TAIL_FILE.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            tail = strip_motion(raw.decode(enc))
            break
        except UnicodeDecodeError:
            continue
    else:
        tail = strip_motion(raw.decode("utf-8", errors="replace"))
    idx = text.rfind("</section>")
    if idx == -1:
        raise SystemExit("could not find closing section tag")
    return text[: idx + len("</section>")] + "\n\n" + tail


def main() -> None:
    text = load_index()
    text = patch_nav(text)
    text = insert_retro(text)
    text = renumber_steps(text)
    text = add_flow_retro(text)
    text = restore_tail(text)
    INDEX.write_text(text, encoding="utf-8")

    fix = ROOT / "fix_encoding.py"
    if fix.is_file():
        subprocess.run([sys.executable, str(fix)], check=True)

    print("OK: retroplanning integrated (UTF-8 normalized)")


if __name__ == "__main__":
    main()
