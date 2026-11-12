// Remplace le slogan des bannières du README et de l'aperçu social, sans toucher au symbole ni au nom.
// La zone du slogan est effacée à la couleur du fond, puis le nouveau texte est écrit en Poppins Regular,
// à la taille et sur la ligne de base de l'ancien slogan (mesurées sur « Pilotez votre Mac depuis Windows »).
// Usage : node slogan.cjs <dossier contenant node_modules/@playwright/test> "<nouveau slogan>"
// Les PNG de départ sont ceux du commit 92384de (kit d'origine) : git show 92384de:readme/<fichier> > <fichier>
const { chromium } = require(process.argv[2] + "/node_modules/@playwright/test");
const fs = require("fs");
const path = require("path");
const slogan = process.argv[3];
const ancien = "Pilotez votre Mac depuis Windows";

// Boîte de l'ancien slogan (pixels non-fond), mesurée sur les PNG d'origine.
const images = [
  { file: "altervnc-banniere-clair.png", bg: "#ffffff", color: "#5f5f5f", box: [439, 253, 1106, 294], align: "left" },
  { file: "altervnc-banniere-sombre.png", bg: "#161616", color: "#b4b4b4", box: [439, 253, 1106, 294], align: "left" },
  { file: "altervnc-apercu-social.png", bg: "#161616", color: "#b4b4b4", box: [273, 556, 1007, 601], align: "center" },
];

(async () => {
  const b = await chromium.launch({ channel: "chrome" });
  const p = await b.newPage();
  await p.setContent(`<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400&display=block">`);
  await p.evaluate(() => document.fonts.load("400 40px Poppins"));
  for (const im of images) {
    const file = path.join(__dirname, im.file);
    const uri = "data:image/png;base64," + fs.readFileSync(file).toString("base64");
    const out = await p.evaluate(async ({ uri, im, slogan, ancien }) => {
      const img = new Image(); img.src = uri; await img.decode();
      const c = document.createElement("canvas"); c.width = img.width; c.height = img.height;
      const g = c.getContext("2d"); g.drawImage(img, 0, 0);
      const [x0, y0, x1, y1] = im.box;
      // Taille : celle qui donne à l'ancien slogan la largeur mesurée.
      g.font = "400 100px Poppins";
      const ref = g.measureText(ancien);
      const refW = ref.actualBoundingBoxLeft + ref.actualBoundingBoxRight;
      let size = 100 * (x1 - x0 + 1) / refW;
      g.font = `400 ${size}px Poppins`;
      const baseline = y0 + g.measureText(ancien).actualBoundingBoxAscent;
      // Le nouveau slogan garde la taille d'origine s'il tient, sinon il réduit jusqu'à la marge.
      const maxW = im.align === "center" ? c.width - 2 * 64 : c.width - x0 - 130;
      let m = g.measureText(slogan);
      if (m.actualBoundingBoxLeft + m.actualBoundingBoxRight > maxW) {
        size *= maxW / (m.actualBoundingBoxLeft + m.actualBoundingBoxRight);
        g.font = `400 ${size}px Poppins`; m = g.measureText(slogan);
      }
      g.fillStyle = im.bg; g.fillRect(im.align === "center" ? 0 : x0 - 8, y0 - 8, im.align === "center" ? c.width : c.width - x0 + 8, y1 - y0 + 16);
      g.fillStyle = im.color; g.textBaseline = "alphabetic";
      const w = m.actualBoundingBoxLeft + m.actualBoundingBoxRight;
      const x = im.align === "center" ? (c.width - w) / 2 + m.actualBoundingBoxLeft : x0 + m.actualBoundingBoxLeft;
      g.fillText(slogan, x, baseline);
      return { png: c.toDataURL("image/png").split(",")[1], size: Math.round(size * 10) / 10 };
    }, { uri, im, slogan, ancien });
    fs.writeFileSync(file, Buffer.from(out.png, "base64"));
    console.log(im.file, "taille", out.size);
  }
  await b.close();
})();
