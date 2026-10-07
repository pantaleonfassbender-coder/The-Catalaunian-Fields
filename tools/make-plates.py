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
    ("leo", "Raphael - The Meeting of Leo the Great and Attila.jpg",
     "Leo the Great and Attila", "church",
     "Raphael, fresco in the Stanza di Eliodoro, Vatican (1514). Pope Leo meets Attila on the Mincio in 452; Peter and Paul appear in the sky with swords. The meeting is in Prosper's chronicle; the apostles are Raphael's."),
    ("lupus", "H. Grobet - Saint Loup arrête Attila devant Troyes (451).jpg",
     "Saint Lupus stops Attila before Troyes", "church",
     "Colour lithograph by E. Crété after H. Grobet (1902). The Life of Lupus, which the editor Bruno Krusch judged a late invention, made the bishop of Troyes the man who faced Attila."),
]


def api(params):
    q = urllib.parse.urlencode({**params, "format": "json"})
    req = urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + q, headers=UA)
    return json.load(urllib.request.urlopen(req))


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
