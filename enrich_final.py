#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from pathlib import Path

p = Path(__file__).parent / "index.html"

HEADER = r"""  <header class="site-header">
    <div class="header-inner">
      <a href="#accueil" class="logo">
        <span>Sport Pro Group</span>
        <strong>BEST-<em>SELLER</em></strong>
      </a>
      <div class="header-nav-zone">
        <p class="header-nav-hint">
          <span class="hint-icon" aria-hidden="true">&#8595;</span>
          Faites défiler pour découvrir la proposition
        </p>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu</button>
        <nav class="main-nav" id="main-nav" aria-label="Sections de la proposition">
          <a href="#introduction">Introduction</a>
          <a href="#concept">Concept</a>
          <a href="#produits">Produits</a>
          <a href="#xavier">Xavier</a>
          <a href="#video">Vidéo</a>
          <a href="#email">Email</a>
          <a href="#reseaux">Réseaux</a>
          <a href="#unss">UNSS</a>
          <a href="#mediatheque">Médiathèque</a>
          <a href="#conclusion">Conclusion</a>
        </nav>
      </div>
    </div>
  </header>

  <a href="#introduction" class="scroll-cue" id="scroll-cue" aria-label="Faire défiler vers le contenu">
    <span class="scroll-cue-text">Défiler pour explorer</span>
    <span class="scroll-cue-arrow" aria-hidden="true"></span>
  </a>"""

FLOW = r"""
        <motion.div class="flow-details">
          <article class="flow-detail-card"><h3>Catalogue &amp; email</h3><p>Le catalogue devient une porte d'entrée. L'email, seul lien direct avec les établissements, annonce la suite.</p></article>
          <article class="flow-detail-card"><h3>Histoire &amp; Xavier</h3><p>Réalité terrain et besoins identifiés avant toute mise en avant produit.</p></article>
          <article class="flow-detail-card"><h3>Produits &amp; ambassadeurs</h3><p>Un professeur et deux élèves font vivre les BEST-SELLER en situation réelle.</p></article>
          <article class="flow-detail-card"><h3>Contenus &amp; réseaux</h3><p>Le court métrage et les réseaux prolongent l'immersion — chaque plateforme a un rôle.</p></article>
          <article class="flow-detail-card"><h3>Terrain &amp; UNSS</h3><p>Le tournoi handball clôture le parcours : le terrain devient le média de la campagne.</p></article>
        </div>""".replace("motion.div", "div")

INTRO = r"""
        <div class="prose"><p>Le catalogue EQUIP EPS présente des références techniques, mais raconte rarement la réalité sur le terrain : séances qui s'enchaînent, passion des enseignants et équipements devenus repères du quotidien.</p></div>
        <p class="section-intro">Le lancement du catalogue EQUIP EPS 2026 représente un temps fort pour Sport Pro Group. Recevoir un catalogue ne suffit plus toujours à créer une véritable expérience — il présente des références, mais raconte rarement leur réalité sur le terrain.</p>
        <blockquote class="quote-block">
          &laquo; Comment prolonger l'expérience du catalogue au-delà du papier et créer un véritable
          lien entre les produits présentés et leur réalité d'usage ? &raquo;
        </blockquote>
        <p class="section-intro">Pour y répondre, la campagne <strong>BEST-SELLER</strong> s'appuie sur un écosystème complémentaire :</p>
        <ul class="content-list">
          <li>Une histoire racontée par <strong>Xavier</strong>, professeur d'EPS</li>
          <li>Des <strong>ambassadeurs</strong> (1 professeur, 2 élèves) et un <strong>court métrage</strong></li>
          <li>Un <strong>emailing</strong> direct et une <strong>stratégie réseaux</strong> par plateforme</li>
          <li>Une activation <strong>UNSS</strong> en clôture sur le terrain</li>
        </ul>"""


def main():
    t = p.read_text(encoding="utf-8")
    i0, i1 = t.find("<header"), t.find("<main>")
    t = t[:i0] + HEADER + "\n\n  " + t[i1:]

    t = re.sub(
        r"<p class=\"hero-desc\">.*?</p>\s*<div class=\"hero-actions\">",
        """<p class="hero-desc">
          Le lancement du catalogue EQUIP EPS 2026 représente un temps fort pour Sport Pro Group.
          Plus de 10&nbsp;600 établissements ont déjà reçu leur catalogue — mais recevoir un catalogue
          ne suffit plus toujours à créer une véritable expérience.
        </p>
        <p class="hero-desc">
          Notre ambition : prolonger cette expérience au-delà du papier, replacer les équipements dans
          leur environnement naturel et construire un écosystème de marque cohérent, du digital jusqu'au terrain.
        </p>
        <div class="hero-actions">""",
        t, count=1, flags=re.DOTALL,
    )

    t = re.sub(r"<div class=\"flow-details\">.*?</motion.div>\s*</div>", FLOW.strip(), t, flags=re.DOTALL)
    t = re.sub(r"<div class=\"flow-details\">.*?</div>\s*(?=</div>\s*</section>\s*<section id=\"introduction\">)", FLOW.strip(), t, flags=re.DOTALL)
    if t.count("flow-detail-card") < 5:
        t = t.replace(
            '<span class="flow-step">Terrain</span>\n        </div>',
            '<span class="flow-step">Terrain</span>\n        </div>' + FLOW,
        )

    t = re.sub(
        r"<section id=\"introduction\">.*?<blockquote class=\"quote-block\">.*?</blockquote>",
        "<section id=\"introduction\">\n      <div class=\"section-inner\">\n        <p class=\"section-label\">Contexte</p>\n        <h2 class=\"section-title\">Introduction</h2>\n" + INTRO,
        t, count=1, flags=re.DOTALL,
    )

    t = t.replace(
        'La direction artistique s\'inspire des magazines EQUIP EPS, des revues sportives et\n              techniques : annotations, cartouches produits, titres imposants, compositions magazine.\n              L\'objectif : faire disparaître la frontière entre catalogue et réalité.',
        'Dimension commerciale : offres BEST-SELLER (packs terrain, avantages campagne). Direction artistique : magazines EQUIP EPS, revues sportives, annotations, cartouches produits — l\'ADN catalogue reste visible sur tous les supports.',
    )

    if "insight-box" not in t:
        t = t.replace(
            '<h2 class="section-title">Les références BEST-SELLER</h2>',
            '<h2 class="section-title">Les références BEST-SELLER</h2>\n        <motion.div class="prose"><p>L\'analyse des ventes montre que les BEST-SELLER sont validés par le terrain : utilisation quotidienne, enseignants et établissements.</p></motion.div>\n        <div class="insight-box"><h3>Insight terrain</h3><p>Le professeur d\'EPS recherche du temps gagné, de la fiabilité, de la durabilité et un matériel adapté à des centaines d\'élèves.</p></div>'.replace("motion.div", "div"),
        )

    t = t.replace(
        "L'email constitue notre seul lien direct avec les établissements. Message implicite :\n          &laquo; Vous avez reçu le catalogue. Voici maintenant la suite. &raquo;",
        "L'email est le seul lien direct avec les établissements. Progression : accueil, rappel catalogue, découverte BEST-SELLER, produits, Xavier, renvoi site. Message : &laquo; Vous avez reçu le catalogue. Voici maintenant la suite. &raquo;",
    )

    t = t.replace(
        "Handball — Aix-en-Provence et Marseille — aboutissement naturel du parcours.\n          Le ballon Handball MAX, BEST-SELLER mis en avant, quitte définitivement le catalogue.",
        "Tournoi UNSS handball (Aix-en-Provence, Marseille) : aboutissement catalogue ? digital ? terrain. Le ballon Handball MAX quitte le catalogue pour le terrain. Proximité La Ciotat et partenariat Académie facilitent l'organisation.",
    )

    for a, b in [
        ("Point de départ, non finalité.", "Point de départ de la narration, non finalité."),
        ("Court métrage cinématographique, interview Xavier, capsules produits.", "Teaser, interview, court métrage et capsules — réutilisables sur tout le dispositif."),
        ("Facebook, Instagram, LinkedIn, YouTube — chaque plateforme, un rôle.", "Chaque réseau raconte une partie différente de la même histoire."),
        ("Écosystème cohérent, preuve sociale terrain, contenus premium réutilisables.", "Écosystème cohérent, narration humaine, preuve sociale terrain, contenus premium."),
    ]:
        t = t.replace(a, b)

    if "prose-note" not in t[:t.find('id="concept"')]:
        t = t.replace(
            '</div>\n      </div>\n    </section>\n\n    <section id="concept">',
            '</div>\n        <p class="prose-note">Au-delà de la promotion produit, Sport Pro Group crée des contenus, des échanges et une proximité durable avec sa communauté EPS.</p>\n      </div>\n    </section>\n\n    <section id="concept">',
            1,
        )

    plat = {
        "facebook": "Facebook — proximité et dimension humaine. Témoignages, partages entre collègues. Mardi/jeudi 18h–20h.",
        "instagram": "Instagram — immersion et visibilité. Reels, stories, capsules. 12h ou 18h.",
        "linkedin": "LinkedIn — expertise et crédibilité B2B. Interview vidéo et carrousel. 8h–9h.",
        "stories": "Stories — présence quotidienne, format 9:16, focus produits et trafic vers le site.",
    }
    for name, text in plat.items():
        t = re.sub(
            rf'(<div id="panel-{name}" class="platform-panel[^"]*">)\s*(?:<p class="platform-copy">.*?</p>\s*)?',
            rf'\1\n          <p class="platform-copy"><strong>{text.split(" — ")[0]}</strong> — {text.split(" — ", 1)[1]}</p>\n          ',
            t, count=1, flags=re.DOTALL,
        )

    p.write_text(t, encoding="utf-8")
    print("Written", p.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
