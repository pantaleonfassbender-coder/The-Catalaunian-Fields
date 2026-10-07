"""Fetch the plates from Wikimedia Commons into assets/plates/ (<id>.jpg, max 1600 px, and <id>_t.jpg),
after checking that the file page carries a public-domain or CC0 licence template, and write
data/plates.json. Run from the repository root:  python tools/make-plates.py
"""
import io
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
UA = {"User-Agent": "CatalaunianFields/0.1 (educational; pantaleon fassbender)"}
OK = re.compile(r"\{\{\s*(PD-|Licensed-PD|cc-zero|CC-zero|CC-0|Cc-zero|PD\b|Public domain)", re.I)
BAD = re.compile(r"cc-by|GFDL|Licence Ouverte", re.I)

CREDIT = ("Plates: public-domain or CC0 images from Wikimedia Commons, each named in its caption with the "
          "original; the licence was checked on the file page. Resized for this site.")

# id, Commons file, title, side, caption
PLATES = [
    ("hunnenschlacht", "Die Hunnenschlacht Raab nach Wilhelm von Kaulbach.jpg",
     "The Battle of the Huns", "reception",
     "Steel engraving by J. L. Raab (1869) after Wilhelm von Kaulbach's Hunnenschlacht: the dead of a battle against Attila fight on in the air, after a story told by the philosopher Damascius. Kaulbach's picture (1834–37) and Liszt's symphonic poem made the battle a scene of nineteenth-century art."),
    ("map450", "C. 450 Roman and Hun Empires.jpg",
     "The Roman and Hunnic empires about 450", "rome",
     "William R. Shepherd, Historical Atlas (1911). A modern map of the empires on the eve of Attila's march into Gaul."),
    ("gaul450", "C. 450 Germanic invasions of Gaul.jpg",
     "Gaul about 450", "rome",
     "William R. Shepherd, Historical Atlas (1911): the Germanic kingdoms in Gaul, among them the Visigoths of Toulouse and the Burgundians, whose warriors fought in 451."),
    ("thuroczy", "Thuróczy krónika - Attila király csatája a catalaunumi síkon.jpg",
     "King Attila's battle on the Catalaunian plain", "reception",
     "Woodcut from the Chronicle of János Thuróczy (Augsburg 1488), where Attila is the first king of the Hungarians: the battle as Hungarian history told it."),
    ("feast", "Than Mór - Attila lakomája (1870).jpg",
     "Attila's feast", "huns",
     "Mór Than, Attila lakomája (1870), Hungarian National Gallery: the banquet Priscus describes, painted for a Hungarian public for whom Attila was an ancestral king. Attila sits with his wooden cup among guests served from silver."),
    ("aetius", "Flavius Aetius.jpg",
     "An imagined Aetius", "rome",
     "Engraving after Giovanni Strozza (18th century). No likeness of Aetius survives that can be shown here: this portrait is an invention of the early modern print trade, as are most images of him."),
    ("leo", "Raphael - The Meeting of Leo the Great and Attila.jpg",
     "Leo the Great and Attila", "church",
     "Raphael, fresco in the Stanza di Eliodoro, Vatican (1514). Pope Leo meets Attila on the Mincio in 452; Peter and Paul appear in the sky with swords. The meeting is in Prosper's chronicle; the apostles are Raphael's."),
    ("lupus", "H. Grobet - Saint Loup arrête Attila devant Troyes (451).jpg",
     "Saint Lupus stops Attila before Troyes", "church",
     "Colour lithograph by E. Crété after H. Grobet (1902). The Life of Lupus, which the editor Bruno Krusch judged a late invention, made the bishop of Troyes the man who faced Attila."),
    ("genevieve", "Puvis de Chavannes - Sainte Geneviève veillant sur Paris.jpg",
     "Genovefa keeps watch over Paris", "church",
     "Pierre Puvis de Chavannes, Sainte Geneviève veillant sur Paris, a version of his last panel for the Panthéon (1898), Musée du Grand Siècle. The old Genovefa watches over the sleeping city by night; the Life of Genovefa itself has her keep the Parisians from fleeing in 451."),
    ("meaux", "Meaux Vitrail 1869 4 Ste Geneviève et Attila.jpg",
     "Genovefa before Attila", "church",
     "Stained glass, cathedral of Meaux (1869): Genovefa kneels before a crowned Attila on horseback. The meeting is the window's: in the Life of Genovefa she never sees him, and her quarrel is with the citizens of Paris."),
    ("neuville", "De Neuville - The Huns at the Battle of Chalons.jpg",
     "The Huns at Châlons", "huns",
     "Engraving after Alphonse de Neuville, from Guizot's illustrated history of France (1870s): the Huns as the nineteenth century imagined them, half-naked horsemen in a storm of battle. Nothing in the sources describes the battle like this."),
    ("maerlant", "Battle of the Catalaunian plains.jpg",
     "The battle in a Dutch chronicle", "reception",
     "Miniature from Jacob van Maerlant's Spieghel Historiael (about 1325–1335), National Library of the Netherlands: the battle of Attila, Aetius, Merovech and Theoderic as a clash of fourteenth-century knights. Merovech, the Frankish king named here, appears in none of the sources of the fifth and sixth centuries."),
    ("paczka", "Paczka Ferenc - Attila halála - 1884.jpg",
     "Attila's death", "huns",
     "Ferenc Paczka, Attila halála (Attila's death), 1884: Ildico stands over the dead king. In Jordanes she weeps 'with downcast face under her veil'; the salon painter unveils her, and the murder legend hangs in the air."),
    ("delacroix", "Eugene Ferdinand Victor Delacroix Attila fragment.jpg",
     "Attila tramples Italy and the Arts", "reception",
     "Eugène Delacroix, detail of his Attila for the library of the Palais Bourbon, Paris (1843–1847): Attila, followed by his barbarian hordes, tramples Italy and the Arts. The nineteenth century's Attila as the enemy of civilization."),
]


def api(params):
    q = urllib.parse.urlencode({**params, "format": "json"})
    req = urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + q, headers=UA)
    for wait in (0, 20, 60, 120):
        time.sleep(wait)
        try:
            return json.load(urllib.request.urlopen(req))
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
    raise RuntimeError("Commons API still rate-limited")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    plates = []
    for pid, fname, title, side, caption in PLATES:
        page = next(iter(api({"action": "query", "titles": "File:" + fname, "prop": "revisions|imageinfo",
                              "rvprop": "content", "rvslots": "main", "iiprop": "url|size",
                              "iiurlwidth": 1600})["query"]["pages"].values()))
        text = page["revisions"][0]["slots"]["main"]["*"]
        lic = text[text.lower().find("license"):][:600] if "license" in text.lower() else text
        assert OK.search(text) and not BAD.search(lic), f"licence not PD/CC0: {fname}"
        ii = page["imageinfo"][0]
        dest = OUT / f"{pid}.jpg"
        if not dest.exists():
            raw = urllib.request.urlopen(urllib.request.Request(ii.get("thumburl") or ii["url"], headers=UA)).read()
            im = Image.open(io.BytesIO(raw)).convert("RGB")
            if im.width > 1600:
                im = im.resize((1600, round(im.height * 1600 / im.width)))
            im.save(dest, "JPEG", quality=84, optimize=True)
            t = im.copy(); t.thumbnail((480, 480)); t.save(OUT / f"{pid}_t.jpg", "JPEG", quality=80)
            time.sleep(2)
        plates.append({"id": pid, "titel": title, "side": side, "caption": caption,
                       "source": f"Wikimedia Commons, File:{fname} ({ii['descriptionurl']})"})
        print(pid, dest.stat().st_size // 1024, "KB")
    (ROOT / "data" / "plates.json").write_text(json.dumps({"credit": CREDIT, "plates": plates}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
