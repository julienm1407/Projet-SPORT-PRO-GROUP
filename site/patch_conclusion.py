#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace conclusion section with enriched version (UTF-8 safe)."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
INDEX = ROOT / "index.html"

CONCLUSION = """
    <section id="conclusion" class="conclusion-section">
      <div class="section-inner">
        <p class="section-phase">\u00c9tape 13 \u00b7 Synth\u00e8se</p>
        <p class="section-label">Synth\u00e8se</p>
        <h2 class="section-title">Conclusion &amp; perspectives</h2>
        <p class="section-intro">
          La campagne <strong>BEST-SELLER</strong> r\u00e9pond \u00e0 une double ambition : donner une suite au catalogue
          EQUIP EPS 2026 et installer Sport Pro Group comme partenaire de terrain, pas seulement comme fournisseur.
          Du papier au tournoi UNSS, chaque support a jou\u00e9 un r\u00f4le pr\u00e9cis dans une m\u00eame histoire.
        </p>

        <blockquote class="quote-block conclusion-quote">
          &laquo; Recevoir un catalogue ne suffit plus. Il faut une exp\u00e9rience qui continue &mdash;
          sur les r\u00e9seaux, par l'email, dans la vid\u00e9o, et sur le terrain. &raquo;
        </blockquote>

        <div class="conclusion-recap">
          <p class="prose-heading">Ce que le dispositif d\u00e9montre</p>
          <div class="kpi-row conclusion-kpi">
            <div class="kpi"><strong>13</strong><span>\u00e9tapes strat\u00e9giques</span></div>
            <div class="kpi"><strong>7</strong><span>phases r\u00e9troplanning</span></div>
            <div class="kpi"><strong>10&nbsp;600+</strong><span>\u00e9tablissements cibl\u00e9s</span></div>
            <div class="kpi"><strong>5</strong><span>plateformes activ\u00e9es</span></div>
          </div>
          <ul class="content-list conclusion-checklist">
            <li>Un <strong>parcours narratif</strong> lisible : catalogue &rarr; humanisation &rarr; lancement &rarr; conversion &rarr; premium &rarr; terrain</li>
            <li>Des <strong>contenus diff\u00e9renci\u00e9s</strong> par r\u00e9seau (proximit\u00e9, immersion, expertise, stories quotidiennes)</li>
            <li>Un <strong>email direct</strong> avec test A/B pour optimiser l'ouverture et le trafic site</li>
            <li>Une <strong>cl\u00f4ture UNSS</strong> qui mat\u00e9rialise le BEST-SELLER phare (Handball MAX) en situation r\u00e9elle</li>
          </ul>
        </div>

        <div class="cards conclusion-cards">
          <article class="card">
            <h3>Forces</h3>
            <ul>
              <li>\u00c9cosyst\u00e8me coh\u00e9rent du digital au terrain</li>
              <li>Preuve sociale et cr\u00e9dibilit\u00e9 via Xavier</li>
              <li>Contenus premium r\u00e9utilisables (teaser, court m\u00e9trage, d\u00e9clinaisons)</li>
              <li>Calendrier op\u00e9rationnel structur\u00e9 et pilotable</li>
              <li>Image de marque renforc\u00e9e aupr\u00e8s des enseignants EPS</li>
            </ul>
          </article>
          <article class="card">
            <h3>Limites &amp; vigilance</h3>
            <ul>
              <li>Investissement de production vid\u00e9o \u00e0 anticiper</li>
              <li>Coordination UNSS et partenaires acad\u00e9miques</li>
              <li>KPI email et r\u00e9seaux \u00e0 valider en conditions r\u00e9elles</li>
              <li>Charge \u00e9ditoriale sur la dur\u00e9e du r\u00e9troplanning</li>
            </ul>
          </article>
          <article class="card">
            <h3>Perspectives</h3>
            <ul>
              <li>Nouveaux ambassadeurs et sports d\u00e9clin\u00e9s (autres BEST-SELLER)</li>
              <li>\u00c9ditions annuelles du tournoi et rendez-vous territoriaux</li>
              <li>Extension du r\u00e9troplanning et formats courts r\u00e9currents</li>
              <li>Capitalisation des contenus terrain en preuve continue</li>
            </ul>
          </article>
        </div>

        <div class="insight-box conclusion-outro">
          <h3>En r\u00e9sum\u00e9</h3>
          <p>
            BEST-SELLER transforme une s\u00e9lection de r\u00e9f\u00e9rences en <strong>exp\u00e9rience de marque</strong>.
            Sport Pro Group ne se contente plus de pr\u00e9senter des \u00e9quipements : elle raconte, accompagne
            et investit le terrain scolaire. La proposition est pr\u00eate \u00e0 \u00eatre d\u00e9ploy\u00e9e sur la fen\u00eatre
            ao\u00fbt&ndash;octobre 2026, avec des livrables concrets et une logique de campagne claire pour EQUIP EPS.
          </p>
        </div>

        <p class="conclusion-actions">
          <a class="btn btn-primary" href="assets/Proposition-BEST-SELLER.pdf" target="_blank" rel="noopener">
            T\u00e9l\u00e9charger la proposition compl\u00e8te (PDF)
          </a>
          <a class="btn btn-secondary" href="#mediatheque">Revoir la m\u00e9diath\u00e8que</a>
        </p>
      </div>
    </section>
""".strip()


def main() -> None:
    frag = CONCLUSION

    text = INDEX.read_text(encoding="utf-8")
    pattern = r'    <section id="conclusion"[^>]*>.*?</section>\s*(?=</main>)'
    if not re.search(pattern, text, flags=re.DOTALL):
        raise SystemExit("conclusion section not found")
    text = re.sub(pattern, frag + "\n", text, count=1, flags=re.DOTALL)
    INDEX.write_text(text, encoding="utf-8")

    fix = ROOT / "fix_encoding.py"
    if fix.is_file():
        subprocess.run([sys.executable, str(fix)], check=True)
    print("OK: conclusion enriched")


if __name__ == "__main__":
    main()
