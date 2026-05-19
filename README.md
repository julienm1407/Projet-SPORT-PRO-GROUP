# Projet SPORT PRO GROUP — BEST-SELLER

Proposition stratégique **BEST-SELLER** (EQUIP EPS 2026–2027) — Sport Pro Group.

**Travail réalisé par Julien Mondet.**

## Site en ligne (GitHub Pages)

**https://julienm1407.github.io/Projet-SPORT-PRO-GROUP/**

### Configuration Pages (une seule fois)

1. **Settings** ? **Pages**
2. Source : **Deploy from a branch**
3. Branch : **gh-pages** · dossier **/ (root)**
4. Sauvegarder — le workflow déploie `site/` sur `gh-pages` à chaque push sur `main`

## Prévisualisation locale

```bash
cd site
python3 -m http.server 8765
```

Puis ouvrir http://127.0.0.1:8765

## Structure

- `site/` — site vitrine (HTML, CSS, JS, assets)
- `site/fix_encoding.py` — normalisation UTF-8 après édition
