#!/usr/bin/env python3
"""Inject retroplanning section into index.html (UTF-8 safe)."""
from pathlib import Path

ROOT = Path(__file__).parent
INDEX = ROOT / "index.html"

NAV_INSERT = """              <a href="#retroplanning" class="nav-link-card">
                <span class="nav-num">10</span>
                <span class="nav-text"><strong>Rùtroplanning</strong><small>Calendrier &amp; phases</small></span>
              </a>
"""

SECTION = """
    <section id="retroplanning" class="retro-section">
      <div class="section-inner">
        <p class="section-phase">ùtape 10 ù Rùtroplanning</p>
        <p class="section-label">Calendrier opùrationnel</p>
        <h2 class="section-title">Rùtroplanning BEST-SELLER</h2>
        <p class="section-intro">
          Planning de diffusion V3 (aoùtùoctobre 2026) : sept phases narratives ù de l'humanisation
          (Xavier) ù la clùture terrain (tournoi UNSS). Chaque publication est calùe sur une
          plateforme, un crùneau horaire et un objectif de campagne.
        </p>

        <p class="retro-actions">
          <a class="btn btn-primary" href="assets/Retroplanning-BEST-SELLER.pdf" download>
            Tùlùcharger le PDF calendrier
          </a>
          <a class="btn btn-outline" href="assets/Retroplanning-BEST-SELLER.pdf" target="_blank" rel="noopener">
            Ouvrir dans un nouvel onglet
          </a>
        </p>

        <motion.div class="retro-overview" aria-label="Vue d'ensemble des phases">
          <article class="retro-phase-card" data-phase="Humaniser">
            <span class="retro-phase-name">Humaniser</span>
            <span class="retro-phase-dates">24ù25 aoùt</span>
            <p>Point d'appui humain ù interview Xavier</p>
          </article>
          <article class="retro-phase-card" data-phase="Intriguer">
            <span class="retro-phase-name">Intriguer</span>
            <span class="retro-phase-dates">31 aoùt ù 3 sept.</span>
            <p>Teaser, email A/B, vision campagne</p>
          </article>
          <article class="retro-phase-card" data-phase="Rùvùler">
            <span class="retro-phase-name">Rùvùler</span>
            <span class="retro-phase-dates">7ù8 sept.</span>
            <p>Lancement officiel BEST-SELLER</p>
          </article>
          <article class="retro-phase-card" data-phase="Conversion">
            <span class="retro-phase-name">Conversion</span>
            <span class="retro-phase-dates">14ù18 sept.</span>
            <p>Stories produits &amp; extraits court mùtrage</p>
          </article>
          <article class="retro-phase-card" data-phase="Premium">
            <span class="retro-phase-name">Premium</span>
            <span class="retro-phase-dates">21ù25 sept.</span>
            <p>Court mùtrage complet &amp; dùclinaisons</p>
          </article>
          <article class="retro-phase-card" data-phase="UNSS">
            <span class="retro-phase-name">UNSS</span>
            <span class="retro-phase-dates">28 sept. ù 3 oct.</span>
            <p>Annonce &amp; teaser tournoi</p>
          </article>
          <article class="retro-phase-card" data-phase="Clùture">
            <span class="retro-phase-name">Clùture</span>
            <span class="retro-phase-dates">10ù11 oct.</span>
            <p>Tournoi terrain &amp; fin de narration</p>
          </article>
        </motion.div>

        <motion.div class="retro-filters" role="group" aria-label="Filtrer par phase">
          <button type="button" class="retro-filter active" data-filter="all">Toutes les phases</button>
          <button type="button" class="retro-filter" data-filter="Humaniser">Humaniser</button>
          <button type="button" class="retro-filter" data-filter="Intriguer">Intriguer</button>
          <button type="button" class="retro-filter" data-filter="Rùvùler">Rùvùler</button>
          <button type="button" class="retro-filter" data-filter="Conversion">Conversion</button>
          <button type="button" class="retro-filter" data-filter="Premium">Premium</button>
          <button type="button" class="retro-filter" data-filter="UNSS">UNSS</button>
          <button type="button" class="retro-filter" data-filter="Clùture">Clùture</button>
        </motion.div>

        <motion.div class="retro-table-wrap">
          <table class="retro-table">
            <thead>
              <tr>
                <th scope="col">Phase</th>
                <th scope="col">Date</th>
                <th scope="col">Jour</th>
                <th scope="col">Heure</th>
                <th scope="col">Plateforme</th>
                <th scope="col">Contenu</th>
              </tr>
            </thead>
            <tbody>
              <tr data-phase="Humaniser"><td><span class="retro-badge retro-badge--humaniser">Humaniser</span></td><td>24/08/2026</td><td>Lundi</td><td>18:30</td><td>Facebook</td><td>Interview Xavier</td></tr>
              <tr data-phase="Humaniser"><td><span class="retro-badge retro-badge--humaniser">Humaniser</span></td><td>24/08/2026</td><td>Lundi</td><td>19:00</td><td>Instagram Reels</td><td>Interview Xavier</td></tr>
              <tr data-phase="Humaniser"><td><span class="retro-badge retro-badge--humaniser">Humaniser</span></td><td>24/08/2026</td><td>Lundi</td><td>20:00</td><td>Instagram Story</td><td>Partage Reels Xavier</td></tr>
              <tr data-phase="Humaniser"><td><span class="retro-badge retro-badge--humaniser">Humaniser</span></td><td>25/08/2026</td><td>Mardi</td><td>08:30</td><td>LinkedIn</td><td>Carrousel Xavier</td></tr>
              <tr data-phase="Intriguer"><td><span class="retro-badge retro-badge--intriguer">Intriguer</span></td><td>31/08/2026</td><td>Lundi</td><td>08:30</td><td>Email</td><td>Email A/B BEST-SELLER</td></tr>
              <tr data-phase="Intriguer"><td><span class="retro-badge retro-badge--intriguer">Intriguer</span></td><td>31/08/2026</td><td>Lundi</td><td>18:30</td><td>Facebook</td><td>Teaser BEST-SELLER</td></tr>
              <tr data-phase="Intriguer"><td><span class="retro-badge retro-badge--intriguer">Intriguer</span></td><td>31/08/2026</td><td>Lundi</td><td>19:00</td><td>Instagram Reels</td><td>Teaser vidùo</td></tr>
              <tr data-phase="Intriguer"><td><span class="retro-badge retro-badge--intriguer">Intriguer</span></td><td>03/09/2026</td><td>Jeudi</td><td>08:30</td><td>LinkedIn</td><td>Vision campagne</td></tr>
              <tr data-phase="Rùvùler"><td><span class="retro-badge retro-badge--reveler">Rùvùler</span></td><td>07/09/2026</td><td>Lundi</td><td>18:30</td><td>Instagram</td><td>Post principal BEST-SELLER</td></tr>
              <tr data-phase="Rùvùler"><td><span class="retro-badge retro-badge--reveler">Rùvùler</span></td><td>07/09/2026</td><td>Lundi</td><td>19:00</td><td>Facebook</td><td>Post BEST-SELLER</td></tr>
              <tr data-phase="Rùvùler"><td><span class="retro-badge retro-badge--reveler">Rùvùler</span></td><td>08/09/2026</td><td>Mardi</td><td>08:00</td><td>LinkedIn</td><td>BEST-SELLER + rùflexion</td></tr>
              <tr data-phase="Conversion"><td><span class="retro-badge retro-badge--conversion">Conversion</span></td><td>14/09/2026</td><td>Lundi</td><td>12:00</td><td>Instagram Story</td><td>Story campagne</td></tr>
              <tr data-phase="Conversion"><td><span class="retro-badge retro-badge--conversion">Conversion</span></td><td>15/09/2026</td><td>Mardi</td><td>12:00</td><td>Instagram Story</td><td>Story Ballon</td></tr>
              <tr data-phase="Conversion"><td><span class="retro-badge retro-badge--conversion">Conversion</span></td><td>16/09/2026</td><td>Mercredi</td><td>12:00</td><td>Instagram Story</td><td>Story Sifflet</td></tr>
              <tr data-phase="Conversion"><td><span class="retro-badge retro-badge--conversion">Conversion</span></td><td>16/09/2026</td><td>Mercredi</td><td>18:00</td><td>Instagram Reels</td><td>Extrait court mùtrage #1</td></tr>
              <tr data-phase="Conversion"><td><span class="retro-badge retro-badge--conversion">Conversion</span></td><td>17/09/2026</td><td>Jeudi</td><td>12:00</td><td>Instagram Story</td><td>Story Chasuble</td></tr>
              <tr data-phase="Conversion"><td><span class="retro-badge retro-badge--conversion">Conversion</span></td><td>18/09/2026</td><td>Vendredi</td><td>12:00</td><td>Instagram Story</td><td>Story Raquette</td></tr>
              <tr data-phase="Conversion"><td><span class="retro-badge retro-badge--conversion">Conversion</span></td><td>18/09/2026</td><td>Vendredi</td><td>18:00</td><td>Instagram Reels</td><td>Extrait court mùtrage #2</td></tr>
              <tr data-phase="Premium"><td><span class="retro-badge retro-badge--premium">Premium</span></td><td>21/09/2026</td><td>Lundi</td><td>19:00</td><td>YouTube</td><td>Court mùtrage complet</td></tr>
              <tr data-phase="Premium"><td><span class="retro-badge retro-badge--premium">Premium</span></td><td>22/09/2026</td><td>Mardi</td><td>18:30</td><td>Facebook</td><td>Extrait vidùo</td></tr>
              <tr data-phase="Premium"><td><span class="retro-badge retro-badge--premium">Premium</span></td><td>24/09/2026</td><td>Jeudi</td><td>08:00</td><td>LinkedIn</td><td>Interview vidùo Xavier</td></tr>
              <tr data-phase="Premium"><td><span class="retro-badge retro-badge--premium">Premium</span></td><td>25/09/2026</td><td>Vendredi</td><td>18:00</td><td>Instagram Reels</td><td>Extrait court mùtrage #3</td></tr>
              <tr data-phase="UNSS"><td><span class="retro-badge retro-badge--unss">UNSS</span></td><td>28/09/2026</td><td>Lundi</td><td>18:30</td><td>Facebook</td><td>Annonce tournoi UNSS</td></tr>
              <tr data-phase="UNSS"><td><span class="retro-badge retro-badge--unss">UNSS</span></td><td>29/09/2026</td><td>Mardi</td><td>12:00</td><td>Instagram Story</td><td>Compte ù rebours tournoi</td></tr>
              <tr data-phase="UNSS"><td><span class="retro-badge retro-badge--unss">UNSS</span></td><td>01/10/2026</td><td>Jeudi</td><td>08:00</td><td>LinkedIn</td><td>Sport Pro Group acteur terrain</td></tr>
              <tr data-phase="UNSS"><td><span class="retro-badge retro-badge--unss">UNSS</span></td><td>03/10/2026</td><td>Samedi</td><td>18:00</td><td>Instagram Reels</td><td>Teaser tournoi</td></tr>
              <tr data-phase="Clùture"><td><span class="retro-badge retro-badge--cloture">Clùture</span></td><td>10/10/2026</td><td>Samedi</td><td>10hù17h</td><td>Terrain</td><td>Tournoi UNSS</td></tr>
              <tr data-phase="Clùture"><td><span class="retro-badge retro-badge--cloture">Clùture</span></td><td>11/10/2026</td><td>Dimanche</td><td>18:00</td><td>Tous rùseaux</td><td>L'aventure continue</td></tr>
            </tbody>
          </table>
        </motion.div>

        <motion.div class="retro-objectives">
          <h3 class="retro-objectives-title">Objectifs par phase</h3>
          <motion.div class="cards retro-objective-cards">
            <article class="card" data-phase="Humaniser">
              <h3>Humaniser</h3>
              <ul>
                <li>Crùer un point d'appui humain</li>
                <li>Version immersive ù story partage 20h</li>
                <li>Rappel service &amp; crùdibilitù</li>
              </ul>
            </article>
            <article class="card" data-phase="Intriguer">
              <h3>Intriguer</h3>
              <ul>
                <li>Crùer l'attente &amp; la curiositù</li>
                <li>Story partage 20h</li>
                <li>Renforcer image de marque</li>
              </ul>
            </article>
            <article class="card" data-phase="Rùvùler">
              <h3>Rùvùler</h3>
              <ul>
                <li>Lancement officiel</li>
                <li>Catalogue ? terrain (story 20h)</li>
                <li>Vision professionnelle</li>
              </ul>
            </article>
            <article class="card" data-phase="Conversion">
              <h3>Conversion</h3>
              <ul>
                <li>Moment achat ù trafic site + Xavier</li>
                <li>Dùcouverte produit (ballon, sifflet, chasuble, raquetteù)</li>
                <li>Produit en action ù stories &amp; reels</li>
              </ul>
            </article>
            <article class="card" data-phase="Premium">
              <h3>Premium</h3>
              <ul>
                <li>Contenu premium &amp; transmission</li>
                <li>Immersion ù story partage</li>
                <li>Accompagnement &amp; dùcouverte</li>
              </ul>
            </article>
            <article class="card" data-phase="UNSS">
              <h3>UNSS</h3>
              <ul>
                <li>Crùer anticipation &amp; engagement</li>
                <li>Image marque terrain</li>
                <li>Crùer l'attente avant l'ùvùnement</li>
              </ul>
            </article>
            <article class="card" data-phase="Clùture">
              <h3>Clùture</h3>
              <ul>
                <li>Expùrience rùelle ù stories live &amp; interviews</li>
                <li>Fin de narration ù ù L'aventure continue ù</li>
              </ul>
            </article>
          </motion.div>
        </motion.div>
      </motion.div>
    </section>

"""

def main():
    text = INDEX.read_text(encoding="utf-8")
    text = text.replace("motion.div", "motion.div")  # noop placeholder
    text = SECTION.replace("motion.div", "div")

    if "id=\"retroplanning\"" in text:
        print("retroplanning already present")
        return

    anchor = '              <a href="#reseaux" class="nav-link-card">'
    if anchor not in text:
        raise SystemExit("nav anchor not found")
    # Insert nav after reseaux block closing </a>
    reseaux_end = text.index('              <a href="#reseaux" class="nav-link-card">')
    reseaux_close = text.index("</a>", reseaux_end) + len("</a>")
    text = text[:reseaux_close] + "\n" + NAV_INSERT + text[reseaux_close:]

    # Renumber nav items
    text = text.replace(
        '<span class="nav-num">10</span>\n                <span class="nav-text"><strong>Tournoi UNSS</strong>',
        '<span class="nav-num">11</span>\n                <span class="nav-text"><strong>Tournoi UNSS</strong>',
    )
    text = text.replace(
        '<span class="nav-num">11</span>\n                <span class="nav-text"><strong>Conclusion</strong>',
        '<span class="nav-num">12</span>\n                <span class="nav-text"><strong>Conclusion</strong>',
    )
    text = text.replace(
        '<span class="nav-num">12</span>\n                <span class="nav-text"><strong>Mùdiathùque</strong>',
        '<span class="nav-num">13</span>\n                <span class="nav-text"><strong>Mùdiathùque</strong>',
    )

    unss_marker = '    <section id="unss">'
    if unss_marker not in text:
        raise SystemExit("unss section not found")
    text = text.replace(unss_marker, SECTION + "\n" + unss_marker, 1)

    text = text.replace("ùtape 10 ù UNSS", "ùtape 11 ù UNSS")
    text = text.replace("ùtape 12 ù Mùdiathùque", "ùtape 13 ù Mùdiathùque")
    # conclusion step if exists
    if "ùtape 11 ù Conclusion" not in text and "id=\"conclusion\"" in text:
        text = text.replace(
            '<section id="conclusion">',
            '<section id="conclusion">',
        )
        # find conclusion phase label
        import re
        text = re.sub(
            r'(<section id="conclusion">[\s\S]*?<p class="section-phase">)ùtape \d+ ù',
            r"\1ùtape 12 ù",
            text,
            count=1,
        )

    INDEX.write_text(text, encoding="utf-8")
    print("patched index.html")


if __name__ == "__main__":
    main()
