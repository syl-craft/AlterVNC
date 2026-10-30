# Images pour le README

| Fichier | Usage |
|---|---|
| `altervnc-banniere-clair.png`, `altervnc-banniere-sombre.png` | Bannière 1280 × 400 en tête du README |
| `altervnc-logo-clair.png`, `altervnc-logo-sombre.png` | Logo horizontal |
| `altervnc-logo-vertical-*.png` | Logo vertical |
| `altervnc-apercu-social.png` | Aperçu social GitHub 1280 × 640 (Settings › Social preview) |
| `altervnc-logo-anime.webp` | Logo animé |

Bannière qui suit le thème de GitHub :

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/altervnc-banniere-sombre.png">
  <img alt="AlterVNC — Pilotez votre Mac depuis Windows" src="docs/images/altervnc-banniere-clair.png">
</picture>
```

Toutes les images font moins de 50 Ko.
