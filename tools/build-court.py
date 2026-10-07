"""Build data/court.json, module 1: Attila's court and the road to Gaul, 440–450.

Sources (public domain):
- Priscus, fr. 8, in J. B. Bury's free English translation, History of the Later Roman Empire I
  (London: Macmillan, 1923), pp. 279–288; text from the LacusCurtius transcription
  (tools/src/bury9.html, parsed into tools/src/bury_paras.json), Thayer's typo marks removed.
- Jordanes, Getica 178–186 and 224, ed. Th. Mommsen, MGH Auct. ant. V.1 (Berlin 1882), pp. 104–106
  and 115; text from the Latin Library, which follows Mommsen, diffed against the OCR of
  archive.org cuaiordanisroman00jord and checked at the page image (printed page = leaf - 73).
- Prosper, Epitoma chronicon 1364 (first sentence), and Chronica Gallica a. 452 c. 139,
  ed. Mommsen, MGH Auct. ant. IX (1892), pp. 481 and 662 (archive.org chronicaminorasa09momm).
English of Jordanes, Prosper and the Gallic chronicle: the site's working translation (CC0).
Run from the repository root:  python tools/build-court.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "src"
OUT = ROOT / "data" / "court.json"

bury = json.loads((SRC / "bury_paras.json").read_text(encoding="utf-8"))
# paragraph 10 ("The next day I entered the enclosure...") runs on into 11 across a page break
bury[10]["text"] += " " + bury[11]["text"]; bury[10]["pg2"] = bury[11]["pg2"]
jord = json.loads((SRC / "jordanes_ll.json").read_text(encoding="utf-8"))


def bt(i):
    t = re.sub(r"[º•]", "", bury[i]["text"])
    t = re.sub(r"\s+", " ", t).strip()
    p1, p2 = bury[i]["pg1"], bury[i]["pg2"]
    return t, (f"Bury p. {p1}" if p1 == p2 else f"Bury pp. {p1}–{p2}")


def jl(n):
    t = re.sub(r"\s+[XLV]+\.\s*$", "", jord[str(n)]).strip()
    return t


PRISCUS = [
    (0, "A man and a god", "The embassy of 448–449 dines with Attila's envoys Edecon and Orestes at Sardica; the comparison of Attila with the emperor nearly ends the dinner."),
    (1, "Naissus, the Danube, and Attila's tent", "Naissus still deserted after its sack; the crossing of the Danube; the first audience in Attila's tent and his anger at the interpreter Bigilas. Bury leaves out the passages marked with dots."),
    (4, "The wooden palace", "The village where Attila's house was 'more splendid than his residences in other places': the enclosure of polished boards, and the bath of Onegesius built by a captive from Sirmium."),
    (5, "Attila enters the village", "Girls in rows singing Scythian songs; the wife of Onegesius brings out meat and wine, and Attila eats sitting on his horse; then a Greek in Scythian dress, a former merchant of Viminacium, who greets Priscus."),
    (6, "Why a Greek preferred the Huns", "The renegade's case: among the Scythians a man lives free after war; among the Romans taxes, unjust judges and the law's delays ruin him."),
    (7, "Priscus answers", "Priscus defends the Roman laws, the courts and the care of the state for its subjects; the Greek weeps and agrees that the laws are good but the governors bad."),
    (10, "Kreka, and Attila as judge", "The enclosure of Attila's wife Kreka and her women at their embroidery; Attila comes out with Onegesius and judges disputes at the door."),
    (13, "War unless", "Onegesius on what Attila wants: a consular of the highest rank as envoy, or war."),
    (14, "The banquet", "The banquet of the evening: the order of seats, the toasts, Attila's wooden cup and plain meat against the silver dishes of his guests, the songs of his victories, a madman, the Moor Zerkon, and Attila's tenderness only toward his youngest son."),
]

GETICA = [
    (178, "Attila, and Priscus' road to his village", "Mommsen p. 104",
     "In this peace there was Attila, lord of all the Huns and almost the only ruler in the world over the peoples of all Scythia, a man marvellous for his fame among all nations. The historian Priscus, who was sent to him on an embassy by Theodosius the Younger, says among other things: 'Crossing great rivers, the Tisia, the Tibisia and the Dricca, we came to the place where long ago Vidigoia, the bravest of the Goths, fell by the treachery of the Sarmatians; and from there, not far on, we reached the village where King Attila was staying, a village, I say, like a very large city, in which we found wooden walls made of shining planks, so closely joined that they counterfeited solid wall, and one could hardly make out the joints of the planks even by looking closely.'",
     "Jordanes quotes Priscus in Latin; the passage corresponds to Bury's 'The wooden palace' in this module. Tisia: the Tisza."),
    (179, "Halls and porticoes", "Mommsen p. 104",
     "You could see dining halls of great extent and colonnades laid out with every ornament. The space of the court was enclosed by a vast circuit, so that its very size showed it to be a royal palace. This was the seat of King Attila, who held the whole barbarian world; he preferred these dwellings to the cities he had taken.", ""),
    (180, "Mundzucus' son, and Bleda", "Mommsen p. 105",
     "This Attila was the son of Mundzucus, whose brothers Octar and Roas are said to have held the kingship before Attila, though not over all the peoples he ruled. After their death he succeeded to the kingdom of the Huns together with his brother Bleda; and to be equal to the expedition he was preparing, he sought an increase of strength by murder, making his way to the ruin of all by the slaughter of his own.",
     "Roas is the king the Greek sources call Rua or Rugila."),
    (181, "The brother killed", "Mommsen p. 105",
     "But, as justice weighed it, growing by a detestable means, he found a hideous end for his cruelty. For when his brother Bleda, who ruled a great part of the Huns, had been killed by treachery, he united the whole people under himself; and gathering together the great number of the other peoples he then held under his rule, he chose above all to subdue the first nations of the world, the Romans and the Visigoths.", ""),
    (182, "The man who shook the nations", "Mommsen p. 105",
     "His army was said to number five hundred thousand men. He was a man born into the world to shake the nations, the terror of all lands, who somehow frightened everyone by the dreadful rumour spread about him. He was haughty in his walk, rolling his eyes this way and that, so that the power of the proud man showed even in the movement of his body; a lover of war, yet restrained in his own hand; very strong in counsel, open to the entreaties of suppliants, and gracious to those he had once taken under his protection. He was short, with a broad chest and a large head, small eyes, a thin beard flecked with grey, a flat nose and a dark complexion, showing the marks of his origin.",
     "The figure of five hundred thousand is a rumour, as Jordanes says (ferebatur); no number in the sources for 451 can be taken as a count."),
    (183, "The sword of Mars", "Mommsen pp. 105–106",
     "Though he was by nature always confident in great things, his confidence was increased by the finding of the sword of Mars, always held sacred among the kings of the Scythians, which the historian Priscus says was discovered in this way. 'A shepherd,' he says, 'saw that a heifer of his herd was limping and could find no cause for so great a wound. Anxiously he followed the trail of blood and at last came to a sword which it had trodden on unawares while grazing; he dug it up and took it straight to Attila. Attila rejoiced at the gift and, being of great spirit, believed that he had been made prince of the whole world, and that through the sword of Mars the power of wars had been granted to him.'", ""),
]

CAUSES = [
    ("jord", 184, "Gaiseric's gifts", "Mommsen p. 106",
     "Learning, then, that his mind was set on laying waste the world, Gaiseric, king of the Vandals, whom we mentioned a little earlier, drove him with many gifts to make war on the Visigoths, fearing that Theoderic, king of the Visigoths, would avenge the wrong done to his daughter. She had been married to Huneric, Gaiseric's son, and at first was happy in so great a match; but afterwards, since he was cruel even to his own children, on the mere suspicion that she had prepared poison for him he cut off her nose and mutilated her ears, and, robbing her of her natural beauty, sent her back to her father in Gaul, so that the wretched woman might always present a shameful sight, and the cruelty, by which even strangers would be moved, might win the father's vengeance the more surely.",
     "The first reason for the war in Jordanes: a Vandal king's bribe. No other source carried here gives it."),
    ("jord", 185, "Letters to Valentinian", "Mommsen p. 106",
     "Attila, therefore, long pregnant with a war already conceived and now brought to birth by Gaiseric's bribe, sent envoys to Italy to the emperor Valentinian, sowing discord between Goths and Romans, so that those he could not shake in battle he might crush by hatred among themselves. He declared that he was in no way breaking his friendship with the Empire, but that his quarrel was with Theoderic, king of the Visigoths. Wishing to be received gladly, he filled the rest of the letter with the usual flatteries of greeting, striving to give credit to a lie.",
     "The second reason, in Attila's own claim: a war only against the Goths. Prosper reports the same claim (next unit but one)."),
    ("jord", 186, "Letters to Theoderic", "Mommsen p. 106",
     "In the same way he sent a letter to Theoderic, king of the Visigoths, urging him to leave his alliance with the Romans and to remember the battles that had lately been stirred up against him. Under his great ferocity he was a subtle man, and fought with craft before he made war.",
     "The battles 'lately stirred up' against Theoderic are the wars of the 430s, in which Aetius had used Hunnic auxiliaries against the Goths (Getica 177)."),
    ("prosper", 1364, "Only against the Goths", "MGH AA IX p. 481",
     "Attila, after the murder of his brother, grown stronger by the dead man's resources, forced many thousands of the neighbouring peoples into a war which he declared he was bringing only upon the Goths, as a guardian of the Roman friendship.",
     "Prosper wrote in Rome within a few years of the events. Only the first sentence of the entry is given here; the battle it goes on to describe belongs to module 4."),
    ("gall", 139, "A wife owed by right", "MGH AA IX p. 662",
     "Attila, entering Gaul, demands a wife as though she were owed to him by right; there, having inflicted and suffered a heavy defeat, he withdraws to his own lands.",
     "The third reason, in the Gallic chronicle of 452: Honoria, the emperor's sister. The chronicler ends the campaign of 451 in one sentence."),
    ("jord", 224, "Honoria's eunuch", "Mommsen p. 115",
     "For it was said that this Honoria, kept shut up at her brother's command for the dignity of the court and to keep her chaste, secretly sent a eunuch to invite Attila, so that she might use his protection against her brother's power: a thoroughly shameful deed, to buy licence for her lust at the cost of public ruin.",
     "Jordanes tells the story only when Attila turns to Italy in 452, and as hearsay (ferebatur). Priscus' fragments on Honoria and her ring (Müller, FHG IV p. 98) are not yet carried."),
]
LATIN = {
    ("prosper", 1364): "Attila post necem fratris auctus opibus interempti multa vicinarum sibi gentium milia cogit in bellum, quod Gothis tantum se inferre tamquam custos Romanae amicitiae denuntiabat.",
    ("gall", 139): "Attila Gallias ingressus quasi iure debitam poscit uxorem: ubi gravi clade inflicta et accepta ad propria concedit.",
}


def build():
    sec1 = [{"n": i + 1, "pg": bt(p)[1], "titel": t, "en": bt(p)[0], "note": note} for i, (p, t, note) in enumerate(PRISCUS)]
    sec2 = [{"n": i + 1, "pg": f"Get. {n} · {pg}", "titel": t, "orig": jl(n), "en": en, **({"note": note} if note else {})}
            for i, (n, t, pg, en, note) in enumerate(GETICA)]
    sec3 = []
    for i, (kind, n, t, pg, en, note) in enumerate(CAUSES):
        orig = jl(n) if kind == "jord" else LATIN[(kind, n)]
        label = {"jord": f"Get. {n}", "prosper": f"Prosper {n}", "gall": f"Chron. Gall. 452 c. {n}"}[kind]
        sec3.append({"n": i + 1, "pg": f"{label} · {pg}", "titel": t, "orig": orig, "en": en, "note": note})
    data = {
        "titel": "Attila's court and the road to Gaul, 440–450",
        "autor": "Priscus of Panium (embassy of 448–449, in Bury's English); Jordanes, Getica (about 551); Prosper of Aquitaine (Rome, about 455); the Gallic chronicle of 452",
        "jahr": "448–451",
        "orig_sprache": "la",
        "pg_label": "",
        "quelle": "Priscus fr. 8 in J. B. Bury, History of the Later Roman Empire I (London 1923), pp. 279–288 (LacusCurtius transcription); Jordanes, Getica, ed. Th. Mommsen, MGH Auct. ant. V.1 (Berlin 1882), pp. 104–106, 115 (archive.org cuaiordanisroman00jord); Prosper, Epitoma chronicon, and Chronica Gallica a. 452, ed. Th. Mommsen, MGH Auct. ant. IX (Berlin 1892), pp. 481, 662 (archive.org chronicaminorasa09momm). All public domain.",
        "hinweis": "Priscus is given in Bury's free English of 1923 (Bury died in 1927), whole paragraphs; Bury's own omissions are marked with dots, and Hodgkin's Italy and her Invaders II (1892), pp. 54–97, renders the parts he leaves out. The Greek of Priscus (Müller, FHG IV pp. 77–95; Dindorf, HGM I pp. 289–323) is not yet carried. Jordanes' Latin follows Mommsen, checked against the page; Prosper and the Gallic chronicle likewise. Their English is the site's working translation. Mierow's English Jordanes is not used (Mierow died in 1961).",
        "sections": [
            {"id": "embassy", "zk": "Priscus", "titel": "Priscus at Attila's court, 448–449",
             "blurb": "The only eyewitness of Attila: an East Roman envoy's account of the journey, the wooden palace, a Greek who preferred the Huns, the judge at the door and the banquet.", "units": sec1},
            {"id": "attila", "zk": "Get. Attila", "titel": "Jordanes on Attila",
             "blurb": "The Gothic historian's portrait, written a century later from Priscus and Cassiodorus: the village like a city, the murdered brother, the man born to shake the nations, the sword of Mars.", "units": sec2},
            {"id": "causes", "zk": "Causes", "titel": "Three reasons for war",
             "blurb": "Why Gaul in 451? A Vandal king's bribe, a war 'only against the Goths', and the emperor's sister claimed as a wife: three reasons in the sources, none of which excludes the others.", "units": sec3},
        ],
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in data['sections'])} units in {len(data['sections'])} sections")


if __name__ == "__main__":
    build()
