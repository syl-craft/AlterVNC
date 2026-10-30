# Logo AlterVNC

## Idée

Un écran qui en contient un autre : l'écran du PC affiche celui du Mac, et la flèche verte pointe vers lui pour le
piloter. Variante retenue : **c3 · bleu et vert** (concept C « Écran relais »), avec une flèche à la place du trait
d'origine, qui se lisait comme un stylo.

## Fichiers

| Dossier | Contenu |
|---|---|
| `ico/altervnc.ico` | Icône Windows, 14 tailles (16 → 256 px) : dessinée au pixel de 16 à 48 px (`icone-pixel/generer.py`), écran plein `#0B0F14` pour rester net et contrasté sur une barre des tâches claire ou sombre |
| `png/` | Symbole de 16 à 1024 px, lockups clair et sombre pour un écran « À propos » |
| `svg/altervnc-symbol.svg` | Symbole de référence (à partir de 32 px) |
| `svg/altervnc-symbol-small.svg` | Version simplifiée pour 16 à 24 px |
| `svg/*-black.svg`, `*-white.svg` | Versions une couleur |
| `svg/altervnc-logo-*.svg` | Lockups horizontal et vertical, nom en Poppins SemiBold vectorisé |

## Couleurs

| Rôle | HEX | RGB |
|---|---|---|
| Écran et pied | `#9CA3AF` | 156, 163, 175 |
| Écran du Mac | `#4C9AFF` | 76, 154, 255 |
| Flèche de pilotage | `#3FB97A` | 63, 185, 122 |
| Fond de l'appli | `#0B0F14` | 11, 15, 20 |

Le bleu et le vert sont ceux de l'interface : accent et état « connecté ».

## Zone de protection

Laisser autour du symbole un vide égal à la hauteur du pied (20/256 de la largeur), et au moins la hauteur du « A »
autour du lockup.

## À ne pas faire

- Changer les couleurs, ajouter un dégradé ou une ombre.
- Utiliser la version simplifiée au-delà de 24 px, ou le master en dessous de 32 px.
- Déformer, faire pivoter ou recadrer le symbole.
- Remplir l'intérieur de l'écran : c'est un vrai vide, qui prend la couleur du fond.
- Recomposer le nom dans une autre police que Poppins SemiBold.
