"""Ré-encode des PNG opaques en RGB 8 bits, filtre adaptatif par ligne et zlib niveau 9.

Le canvas du navigateur écrit des PNG RGBA peu compressés ; ce script les ramène sous la limite de 50 Ko du kit.
Usage : python optimiser-png.py fichier.png [...]
"""
import struct
import sys
import zlib


def lire(chemin):
    data = open(chemin, "rb").read()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "pas un PNG"
    pos, idat, ihdr = 8, b"", None
    while pos < len(data):
        longueur, = struct.unpack(">I", data[pos:pos + 4])
        type_ = data[pos + 4:pos + 8]
        contenu = data[pos + 8:pos + 8 + longueur]
        if type_ == b"IHDR":
            ihdr = struct.unpack(">IIBBBBB", contenu)
        elif type_ == b"IDAT":
            idat += contenu
        pos += 12 + longueur
    largeur, hauteur, profondeur, couleur, _, _, entrelace = ihdr
    assert profondeur == 8 and couleur in (2, 6) and entrelace == 0, ihdr
    canaux = 3 if couleur == 2 else 4
    brut = zlib.decompress(idat)
    pas = largeur * canaux
    lignes, precedente, i = [], bytearray(pas), 0
    for _ in range(hauteur):
        filtre = brut[i]
        ligne = bytearray(brut[i + 1:i + 1 + pas])
        i += 1 + pas
        for x in range(pas):
            a = ligne[x - canaux] if x >= canaux else 0
            b = precedente[x]
            c = precedente[x - canaux] if x >= canaux else 0
            if filtre == 1:
                ligne[x] = (ligne[x] + a) & 255
            elif filtre == 2:
                ligne[x] = (ligne[x] + b) & 255
            elif filtre == 3:
                ligne[x] = (ligne[x] + (a + b) // 2) & 255
            elif filtre == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                ligne[x] = (ligne[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        lignes.append(ligne)
        precedente = ligne
    if canaux == 4:
        lignes = [bytearray(b for k in range(0, pas, 4) for b in l[k:k + 3]) for l in lignes]
    return largeur, hauteur, lignes


def filtrer(ligne, precedente, canaux=3):
    candidats = []
    for filtre in range(5):
        sortie = bytearray(len(ligne))
        for x in range(len(ligne)):
            a = ligne[x - canaux] if x >= canaux else 0
            b = precedente[x]
            c = precedente[x - canaux] if x >= canaux else 0
            if filtre == 0:
                v = ligne[x]
            elif filtre == 1:
                v = ligne[x] - a
            elif filtre == 2:
                v = ligne[x] - b
            elif filtre == 3:
                v = ligne[x] - (a + b) // 2
            else:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                v = ligne[x] - (a if pa <= pb and pa <= pc else b if pb <= pc else c)
            sortie[x] = v & 255
        cout = sum(v if v < 128 else 256 - v for v in sortie)
        candidats.append((cout, filtre, sortie))
    _, filtre, sortie = min(candidats)
    return bytes([filtre]) + bytes(sortie)


def ecrire(chemin, largeur, hauteur, lignes):
    precedente = bytearray(largeur * 3)
    flux = b""
    for ligne in lignes:
        flux += filtrer(ligne, precedente)
        precedente = ligne

    def bloc(type_, contenu):
        return struct.pack(">I", len(contenu)) + type_ + contenu + struct.pack(">I", zlib.crc32(type_ + contenu) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n" + bloc(b"IHDR", struct.pack(">IIBBBBB", largeur, hauteur, 8, 2, 0, 0, 0))
    png += bloc(b"IDAT", zlib.compress(flux, 9)) + bloc(b"IEND", b"")
    open(chemin, "wb").write(png)
    return len(png)


for chemin in sys.argv[1:]:
    largeur, hauteur, lignes = lire(chemin)
    print(chemin, ecrire(chemin, largeur, hauteur, lignes), "octets")
