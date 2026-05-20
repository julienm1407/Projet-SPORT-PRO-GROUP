#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(__file__).parent / "index.html"
t = p.read_text(encoding="utf-8")

# Fix encoding glitches from generator
fixes = [
    ("o� ", "o� "),
    (" � créer", " � créer"),
    (" exp�rience � il", " exp�rience � il"),
    ("�cosyst�me", "�cosyst�me"),
    ("YouTube � chaque", "YouTube � chaque"),
    ("handball � le", "handball � le"),
    ("� premi�re", "� premi�re"),
    ("r�le", "r�le"),
    ("� Sport Pro Group", "� Sport Pro Group"),
    ("�tablissements", "�tablissements"),  # only in kpi span - careful
    ("Sport Pro Group � elle", "Sport Pro Group � elle"),
    ("�cosyst�me coh�rent", "�cosyst�me coh�rent"),
    ("Marseille � aboutissement", "Marseille � aboutissement"),
    ("partenaire � organisation", "partenaire � organisation"),
    ("paysage � Sport", "paysage � Sport"),
    ("emailing � cliquer", "emailing � cliquer"),
    ("2026�2027 � Les", "2026�2027 � Les"),
    ("Preuve sociale sociale", "Preuve sociale"),
    ("sont l�", "sont l�"),
    ("</cite>", ""),  # remove stray if broken
]
for a, b in fixes:
    t = t.replace(a, b)
# fix kpi - we may have broken �tablissements in middle of words - revert if needed
t = t.replace("plus de 10&nbsp;600 �tablissements scolaires", "plus de 10&nbsp;600 �tablissements scolaires")
t = t.replace("<span>�tablissements</span>", "<span>�tablissements</span>")

HEADER = """  <header class="site-header">
    <div class="header-inner">
      <a href="#accueil" class="logo">
        <span>Sport Pro Group</span>
        <strong>BEST-<em>SELLER</em></strong>
      </a>
      <div class="header-nav-zone">
        <p class="header-nav-hint">
          <span class="hint-icon" aria-hidden="true">&#8595;</span>
          Faites d�filer pour d�couvrir la proposition
        </p>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu</button>
        <nav class="main-nav" id="main-nav" aria-label="Sections de la proposition">
          <a href="#introduction">Introduction</a>
          <a href="#concept">Concept</a>
          <a href="#produits">Produits</a>
          <a href="#xavier">Xavier</a>
          <a href="#video">Vid�o</a>
          <a href="#email">Email</a>
          <a href="#reseaux">R�seaux</a>
          <a href="#unss">UNSS</a>
          <a href="#mediatheque">M�diath�que</a>
          <a href="#conclusion">Conclusion</a>
        </nav>
      </div>
    </div>
  </header>

  <a href="#introduction" class="scroll-cue" id="scroll-cue" aria-label="Faire d�filer vers le contenu">
    <span class="scroll-cue-text">D�filer pour explorer</span>
    <span class="scroll-cue-arrow" aria-hidden="true"></span>
  </a>"""

HEADER = HEADER.replace("div", "div")

old_header = t[t.find("<header class=\"site-header\">"):t.find("<main>")]
t = t.replace(old_header, HEADER + "\n\n  ")

# Hero extra paragraph
t = t.replace(
    """        <p class="hero-desc">
          Prolonger l'exp�rience du catalogue EQUIP EPS au-del� du papier. Faire sortir les �quipements
          vers le terrain, raconter leur r�alit� d'usage et créer un �cosyst�me digital complet pour
          plus de 10&nbsp;600 �tablissements scolaires.
        </p>""",
    """        <p class="hero-desc">
          Le lancement du catalogue EQUIP EPS 2026 repr�sente un temps fort pour Sport Pro Group.
          Plus de 10&nbsp;600 �tablissements ont d�j� re�u leur catalogue � mais recevoir un catalogue
          ne suffit plus toujours � créer une v�ritable exp�rience.
        </p>
        <p class="hero-desc">
          Notre ambition : prolonger cette exp�rience au-del� du papier, replacer les �quipements dans
          leur environnement naturel et construire un �cosyst�me de marque coh�rent, du digital jusqu'au terrain.
        </p>""",
)

# Flow details after flow-track
flow_insert = """        </div>
        <div class="flow-details">"""
flow_insert = flow_insert.replace("div", "div")
t = t.replace(
    """          <span class="flow-step">Terrain</span>
        </div>
      </div>
    </section>

    <section id="introduction">""",
    """          <span class="flow-step">Terrain</span>
        </div>
        <div class="flow-details">
          <article class="flow-detail-card"><h3>Catalogue &amp; email</h3><p>Le catalogue devient une porte d'entr�e. L'email annonce la suite : � Vous avez re�u le catalogue. Voici maintenant la suite. �</p></article>
          <article class="flow-detail-card"><h3>Histoire &amp; Xavier</h3><p>Xavier introduit une r�alit� terrain avant toute mise en avant produit. Il cr�dibilise Sport Pro Group et ses usages.</p></article>
          <article class="flow-detail-card"><h3>Produits &amp; ambassadeurs</h3><p>Un professeur et deux �l�ves incarnent les BEST-SELLER en situation r�elle, dans le gymnase.</p></article>
          <article class="flow-detail-card"><h3>Contenus &amp; r�seaux</h3><p>Le court m�trage et les r�seaux prolongent l'immersion � chaque plateforme avec un r�le distinct.</p></article>
          <article class="flow-detail-card"><h3>Terrain &amp; UNSS</h3><p>Le tournoi handball cl�ture le parcours : le terrain devient le v�ritable m�dia de la campagne.</p></article>
        </div>
      </div>
    </section>

    <section id="introduction">""".replace("div", "div"),
)
t = t.replace("div", "div")

# Introduction enrichment
t = t.replace(
    """        <p class="section-intro">
          Le lancement du catalogue EQUIP EPS 2026 repr�sente un temps fort pour Sport Pro Group.
          Recevoir un catalogue ne suffit plus toujours � créer une v�ritable exp�rience � il pr�sente
          des r�f�rences, mais raconte rarement leur r�alit� sur le terrain.
        </p>
        <blockquote class="quote-block">""",
    """        <div class="prose">
          <p>Le catalogue EQUIP EPS regroupe les �quipements des �coles, coll�ges et lyc�es. Il pr�sente des r�f�rences
          et des caract�ristiques techniques, mais raconte rarement la r�alit� sur le terrain : des s�ances qui
          s'encha�nent, des professeurs passionn�s, des �l�ves qui pratiquent et des �quipements qui deviennent
          des rep�res du quotidien.</p>
        </div>
        <blockquote class="quote-block">""",
)

t = t.replace(
    """        </blockquote>
        <div class="cards">""".replace("div", "div"),
    """        </blockquote>
        <p class="section-intro">Pour y r�pondre, la campagne <strong>BEST-SELLER</strong> s'appuie sur un �cosyst�me o� chaque support est compl�mentaire :</p>
        <ul class="content-list">
          <li>Une histoire racont�e par <strong>Xavier</strong>, professeur d'EPS</li>
          <li>Des <strong>ambassadeurs</strong> (1 professeur, 2 �l�ves) qui incarnent les usages</li>
          <li>Un <strong>court m�trage</strong> immersif et un <strong>dispositif emailing</strong> central</li>
          <li>Une <strong>strat�gie digitale</strong> par plateforme et une <strong>activation UNSS</strong> finale</li>
        </ul>
        <div class="cards">""",
)
t = t.replace("div", "div")

# Expand cards text
t = t.replace("<p>10&nbsp;600+ �tablissements �quip�s. Point de d�part, non finalit�.</p>",
    "<p>10&nbsp;600+ �tablissements �quip�s. Support d�j� re�u : point de d�part de la narration, non finalit�.</p>")
t = t.replace("<p>Court m�trage cin�matographique, interview Xavier, capsules produits.</p>",
    "<p>Teaser, interview, court m�trage et capsules � contenus premium r�utilisables sur tout le dispositif.</p>")
t = t.replace("<p>Facebook, Instagram, LinkedIn, YouTube � chaque plateforme, un r�le.</p>",
    "<p>Facebook, Instagram, LinkedIn, YouTube : chaque r�seau raconte une partie diff�rente de la m�me histoire.</p>")
t = t.replace("<p>Tournoi handball � le produit quitte le papier pour le terrain r�el.</p>",
    "<p>Tournoi handball UNSS � le ballon MAX quitte le catalogue pour le terrain r�el.</p>")

t = t.replace(
    """        </div>
      </div>
    </section>

    <section id="concept">""",
    """        </div>
        <p class="prose-note">Au-delà de la promotion produit, Sport Pro Group crée des contenus, des échanges et une proximité durable avec sa communauté EPS.</p>
      </div>
    </section>

    <section id="concept">""",
)

# Concept - add commercial + DA blocks
t = t.replace(
    """            <p style="margin-top:1rem;color:var(--gray)">
              La direction artistique s'inspire des magazines EQUIP EPS, des revues sportives et
              techniques : annotations, cartouches produits, titres imposants, compositions magazine.
              L'objectif : faire dispara�tre la fronti�re entre catalogue et r�alit�.
            </p>
          </div>""",
    """            <h3 class="prose-heading">Dimension commerciale</h3>
            <p style="color:var(--gray)">Des offres BEST-SELLER peuvent accompagner la campagne : packs terrain, avantages limit�s, op�rations sur les temps forts. Valoriser ce qui est r�ellement utilis� � pas ce qui reste au second plan.</p>
            <h3 class="prose-heading">Direction artistique</h3>
            <p style="margin-top:0.75rem;color:var(--gray)">
              Magazines EQUIP EPS, revues sportives et techniques, contenus immersifs : annotations,
              cartouches produits, focus mati�re, titres imposants. M�me sur les r�seaux, l'ADN catalogue
              reste pr�sent � la fronti�re entre papier et r�alit� s'estompe.
            </p>
          </div>""",
)

# Products - insight box and descriptions
t = t.replace(
    """        <p class="section-intro">
          Un professeur d'EPS n'ach�te pas uniquement un produit : il recherche du temps gagn�,
          de la fiabilit�, de la durabilit� et un mat�riel capable de suivre la r�alit� de son �tablissement.
        </p>
        <div class="products-grid">""",
    """        <div class="prose">
          <p>L'analyse des ventes de la saison pr�c�dente montre que les BEST-SELLER ne sont pas seulement les produits qui vendent le plus : ce sont ceux valid�s par le terrain, au quotidien, par les enseignants et les �tablissements.</p>
        </div>
        <div class="insight-box">
          <h3>Insight terrain</h3>
          <p>Un professeur d'EPS recherche du temps gagn�, de la fiabilit�, de la durabilit� et un mat�riel adapt� � des centaines d'�l�ves, des usages multiples et du mat�riel partag�.</p>
        </div>
        <div class="products-grid">""",
)

t = t.replace(
    """            <span>REF: HB0008 � Multi-disciplines, durabilit�</span>
          </div>
          <div class="product-item">
            <strong>Sifflet FOX 40</strong>
            <span>REF: ME0008 � R�sistant, cordon fourni</span>
          </div>
          <div class="product-item">
            <strong>Chasuble r�versible</strong>
            <span>REF: ME1507 � Grip alv�ol�, 100% polyester</span>
          </div>
          <div class="product-item">
            <strong>Raquette JOOLA Carbon Control</strong>
            <span>REF: TT0074 � Carbone control, bois certifi� ITTF</span>
          </div>
        </div>
        <div class="kpi-row">""".replace("div", "div"),
    """            <span class="product-ref">REF: HB0008</span>
            <p class="product-desc">Multi-disciplines, forte durabilit�. Produit central du tournoi UNSS handball.</p>
          </div>
          <div class="product-item">
            <strong>Sifflet FOX 40</strong>
            <span class="product-ref">REF: ME0008</span>
            <p class="product-desc">Indispensable du quotidien enseignant � r�sistant, cordon fourni.</p>
          </div>
          <div class="product-item">
            <strong>Chasuble r�versible</strong>
            <span class="product-ref">REF: ME1507</span>
            <p class="product-desc">Grip alv�ol�, 100&nbsp;% polyester � partag�e entre de nombreuses s�ances.</p>
          </div>
          <div class="product-item">
            <strong>Raquette JOOLA Carbon Control</strong>
            <span class="product-ref">REF: TT0074</span>
            <p class="product-desc">Carbone control, bois certifi� ITTF � performance en EPS raquettes.</p>
          </div>
        </div>
        <p class="prose-note">Constantes : commandes fr�quentes, renouvellement r�current, adaptation scolaire, simplicit� d'utilisation.</p>
        <div class="kpi-row">""",
)
t = t.replace("div", "div")

# Xavier - expand
t = t.replace(
    """            <p style="color:var(--gray)">
              <strong>&laquo; L'aventure continue &raquo;</strong> � Xavier ne revient pas raconter une commande,
              il revient raconter une relation. Il devient une preuve terrain avant m�me d'introduire
              les produits BEST-SELLER.
            </p>
          </div>""",
    """            <p style="color:var(--gray)">� travers son interview, il �voque le mat�riel utilis� intensivement, les besoins qui �voluent et le renouvellement des �quipements � tout en validant l'accompagnement, la proximité et la relation durable avec Sport Pro Group.</p>
            <p style="margin-top:1rem;color:var(--gray)">
              <strong>&laquo; L'aventure continue &raquo;</strong> � Xavier ne revient pas raconter une commande,
              il revient raconter une relation. Il devient une <strong>preuve terrain</strong> avant l'introduction des produits BEST-SELLER.
            </p>
          </div>""",
)

# Video - ambassadeurs
t = t.replace(
    """            <h3 style="margin-bottom:0.75rem">Objectifs du format vid�o</h3>
            <ul style="color:var(--gray);padding-left:1.25rem">
              <li>Moderniser la prise de parole de la marque</li>
              <li>Créer une immersion émotionnelle forte</li>
              <li>Alimenter l'ensemble de l'�cosyst�me �ditorial</li>
              <li>Produire un contenu de marque r�utilisable</li>
            </ul>""",
    """            <h3 class="prose-heading">Ambassadeurs</h3>
            <p style="color:var(--gray)">Un professeur et deux �l�ves ne pr�sentent pas les produits : ils les vivent, int�gr�s � une s�ance r�elle du quotidien scolaire.</p>
            <h3 class="prose-heading" style="margin-top:1rem">Objectifs vid�o</h3>
            <ul class="content-list compact">
              <li>Moderniser la prise de parole et renforcer l'image premium</li>
              <li>Créer une immersion émotionnelle (Reels, stories, YouTube)</li>
              <li>Produire un contenu r�utilisable : teaser, capsules, extraits, making-of</li>
            </ul>""",
)

# Email
t = t.replace(
    """        <p class="section-intro">
          L'email constitue notre seul lien direct avec les �tablissements. Message implicite :
          &laquo; Vous avez re�u le catalogue. Voici maintenant la suite. &raquo;
        </p>""",
    """        <div class="prose">
          <p>L'email est le <strong>seul lien direct</strong> avec les �tablissements � ma�tris� et personnalis�, contrairement aux r�seaux soumis aux algorithmes. Message : &laquo; Vous avez re�u le catalogue. Voici maintenant la suite. &raquo;</p>
          <p>Construction progressive : accueil post-rentr�e, rappel catalogue, d�couverte BEST-SELLER, produits, Xavier, puis renvoi vers contenus et site.</p>
        </div>""",
)

# Platform copy - insert before each panel's dl
t = t.replace(
    """        <div id="panel-facebook" class="platform-panel active">
          <dl class="platform-info">""".replace("div", "div"),
    """        <div id="panel-facebook" class="platform-panel active">
          <p class="platform-copy"><strong>Facebook</strong> � proximité et dimension humaine. Ton accessible, t�moignages et partages entre coll�gues. Mardi / jeudi, 18h�20h.</p>
          <dl class="platform-info">""",
)
t = t.replace(
    """        <div id="panel-instagram" class="platform-panel">
          <dl class="platform-info">""",
    """        <div id="panel-instagram" class="platform-panel">
          <p class="platform-copy"><strong>Instagram</strong> � immersion et visibilit�. Reels, stories, capsules et coulisses. Touche aussi le bouche-�-oreille scolaire. 12h ou 18h.</p>
          <dl class="platform-info">""",
)
t = t.replace(
    """        <div id="panel-linkedin" class="platform-panel">
          <dl class="platform-info">""",
    """        <div id="panel-linkedin" class="platform-panel">
          <p class="platform-copy"><strong>LinkedIn</strong> � expertise et cr�dibilit� B2B. Interview vid�o et carrousel r�sum�. Mardi / jeudi, 8h�9h.</p>
          <dl class="platform-info">""",
)
t = t.replace(
    """        <div id="panel-stories" class="platform-panel">
          <dl class="platform-info">""",
    """        <div id="panel-stories" class="platform-panel">
          <p class="platform-copy"><strong>Stories</strong> � pr�sence quotidienne, formats verticaux 9:16, codes revue technique. Relais des posts, focus produits, trafic vers le site.</p>
          <dl class="platform-info">""",
)
t = t.replace("div", "div")

# UNSS
t = t.replace(
    """        <p class="section-intro">
          Handball � Aix-en-Provence et Marseille � aboutissement naturel du parcours.
          Le ballon Handball MAX, BEST-SELLER mis en avant, quitte d�finitivement le catalogue.
        </p>""",
    """        <div class="prose">
          <p>Tournoi local UNSS handball (Aix-en-Provence, Marseille et alentours) : aboutissement du parcours catalogue &rarr; digital &rarr; terrain. L'UNSS est notre c�ur de cible ; le ballon Handball MAX EQUIP EPS, BEST-SELLER de la campagne, est utilis� en situation r�elle.</p>
          <p>Implantation � La Ciotat et partenariat Acad�mie : organisation, mobilisation et l�gitimit� territoriale facilit�es. L'�v�nement g�n�re interviews, photos, stories et capsules pour prolonger la campagne.</p>
        </div>""",
)

# Conclusion cards
t = t.replace("<p>�cosyst�me coh�rent, preuve sociale terrain, contenus premium r�utilisables.</p>",
    "<p>�cosyst�me coh�rent, narration humaine (Xavier, ambassadeurs), preuve sociale terrain et contenus premium r�utilisables.</p>")
t = t.replace("<p>Investissement production vid�o, validations UNSS, KPI � confirmer en d�ploiement.</p>",
    "<p>Production vid�o (tournage, montage, logistique), validations UNSS et calendrier scolaire. KPI email et social = estimations � confirmer.</p>")
t = t.replace("<p>Nouveaux ambassadeurs, sports d�clin�s, rendez-vous �v�nementiels annuels.</p>",
    "<p>Nouveaux ambassadeurs, contenus enseignants, sports d�clin�s, partenariats r�guliers � BEST-SELLER comme territoire durable.</p>")


p.write_text(t, encoding="utf-8")
print("Patched", p, "->", p.stat().st_size, "bytes")
