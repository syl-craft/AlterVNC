"""Icône AlterVNC calée sur la grille des pixels, une variante par taille (16 à 48 px).

Pourquoi : à 24 px (barre des tâches à 100 %), le symbole réduit depuis 256 px tombe entre deux pixels et
devient flou. Ici chaque bord est sur un pixel entier, et l'écran est plein (#0B0F14) pour rester lisible
sur une barre des tâches claire comme sombre.
"""
import sys

GRIS, ECRAN, BLEU, VERT = "#9CA3AF", "#0B0F14", "#4C9AFF", "#3FB97A"


def icone(s: int) -> str:
    t = max(2, round(s * 0.09))            # épaisseur du cadre
    m = max(1, round(s * 0.04))            # marge latérale
    x0, x1 = m, s - m
    y0, y1 = round(s * 0.10), round(s * 0.74)
    r = max(1, round(s * 0.10))
    xi0, yi0, xi1, yi1 = x0 + t, y0 + t, x1 - t, y1 - t
    p = max(1, round(s * 0.045))           # retrait de l'écran du Mac
    iw, ih = xi1 - xi0, yi1 - yi0
    # Écran du Mac aux proportions du logo : plus large que haut, centré verticalement.
    bx0, bx1 = xi0 + round(iw * 0.36), xi1 - max(1, round(iw * 0.08))
    by0, by1 = yi0 + max(1, round(ih * 0.20)), yi1 - max(1, round(ih * 0.20))
    pied_l = round(s * 0.40)
    pied_h = max(2, round(s * 0.08))
    pied_y = min(s - pied_h, y1 + max(1, round(s * 0.07)))
    # Flèche : pointe vers le haut à droite, dans le coin bas gauche de l'écran.
    ax0, ay1 = xi0 + p, yi1 - p
    ax1, ay0 = bx0 - p, yi0 + p + round((yi1 - yi0) * 0.25)
    w = ax1 - ax0
    h = ay1 - ay0
    tete = max(2, round(min(w, h) * 0.62))
    tige = max(1, round(min(w, h) * 0.30))
    pointe = f"{ax1},{ay0} {ax1},{ay0 + tete} {ax1 - tete},{ay0}"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{s}" height="{s}">
  <rect id="cadre" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="{r}" fill="{GRIS}"/>
  <rect id="ecran" x="{xi0}" y="{yi0}" width="{xi1 - xi0}" height="{yi1 - yi0}" fill="{ECRAN}" shape-rendering="crispEdges"/>
  <rect id="ecran-distant" x="{bx0}" y="{by0}" width="{bx1 - bx0}" height="{by1 - by0}" fill="{BLEU}" shape-rendering="crispEdges"/>
  <line id="fleche-tige" x1="{ax0 + tige / 2}" y1="{ay1 - tige / 2}" x2="{ax1 - tete / 2}" y2="{ay0 + tete / 2}" stroke="{VERT}" stroke-width="{tige}" stroke-linecap="square"/>
  <polygon id="fleche" points="{pointe}" fill="{VERT}"/>
  <rect id="pied" x="{(s - pied_l) // 2}" y="{pied_y}" width="{pied_l}" height="{pied_h}" rx="{max(0, pied_h // 2 - 1)}" fill="{GRIS}"/>
</svg>
"""


for taille in map(int, sys.argv[1:]):
    with open(f"altervnc-{taille}.svg", "w", encoding="utf-8") as f:
        f.write(icone(taille))
