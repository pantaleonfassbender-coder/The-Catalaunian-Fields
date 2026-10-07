"""Build data/alliance.json, module 2: the alliance, 451.

Sources (public domain), each checked against the page image:
- Jordanes, Getica 176-177, 187-191, 194-195, ed. Th. Mommsen, MGH Auct. ant. V.1 (1882), pp. 104, 107-108
  (text from the Latin Library, which follows Mommsen; archive.org cuaiordanisroman00jord, page = leaf - 73).
- Sidonius Apollinaris, Carmen VII (panegyric on Avitus, 456), vv. 295-311 and 316-353, ed. Chr. Luetjohann,
  MGH Auct. ant. VIII (1887), pp. 210-212 (archive.org bub_gb_W-0JAAAAIAAJ, page = index n - 81);
  transcribed by eye, the OCR being unusable.
- Prosper, Epitoma chronicon 1364 (second sentence), MGH Auct. ant. IX (1892), p. 481;
  Additamenta ad Prosperum Hauniensia, pp. 301-302; Additamenta altera (codex Ovetensis) c. 18, p. 490
  (archive.org chronicaminorasa09momm, page = index n - 15).
English: the site's working translation (CC0).
Run from the repository root:  python tools/build-alliance.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "alliance.json"
jord = json.loads((ROOT / "tools" / "src" / "jordanes_ll.json").read_text(encoding="utf-8"))


def jl(n):
    return re.sub(r"\s+[XLV]+\.\s*$", "", jord[str(n)]).strip()


SID_295 = """Haec post gesta viri (temet, Styx livida, testor)
intemerata mihi praefectus iura regebat:
et caput hoc sibimet solitis defessa ruinis
Gallia suscipiens Getica pallebat ab ira.
nil prece, nil pretio, nil milite fractus agebat
Aetius; capto terrarum damna patebant
Litorio; in Rhodanum proprios producere fines
Theudoridae fixum, nec erat pugnare necesse,
sed migrare Getis. rabidam trux asperat iram
victor; quod sensit Scythicum pro moenibus hostem,
imputat; et nil est gravius, si forsitan umquam
vincere contingat, trepido. postquam undique nullum
praesidium ducibusque tuis nil, Roma, relictum est,
foedus, Avite, novas; saevum tua pagina regem
lecta domat; iussisse sat est te quod rogat orbis.
credent hoc umquam gentes populique futuri?
littera Romani cassat quod, barbare, vincis."""

SID_316 = """Iam praefecturae perfunctus culmine tandem
se dederat ruri (numquam tamen otia, numquam
desidia imbellis: studiumque et cura quieto
armorum semper): subito cum rupta tumultu
barbaries totas in te transfuderat arctos,
Gallia. pugnacem Rugum comitante Gelono
Gepida trux sequitur; Scyrum Burgundio cogit;
Chunus, Bellonotus, Neurus, Bastarna, Toringus,
Bructerus, ulvosa vel quem Nicer alluit unda,
prorumpit Francus; cecidit cito secta bipenni
Hercynia in lintres et Rhenum texuit alno;
et iam terrificis diffuderat Attila turmis
in campos se, Belga, tuos. vix liquerat Alpes
Aetius, tenue et rarum sine milite ducens
robur in auxiliis, Geticum male credulus agmen
incassum propriis praesumens adfore castris."""

SID_332 = """nuntius at postquam ductorem perculit, Hunos
iam prope contemptum propriis in sedibus hostem
expectare Getas, versat vagus omnia secum
consilia et mentem curarum fluctibus urget.
tandem nutanti sedit sententia celsum
exorare virum, collectisque omnibus una
principibus coram supplex sic talibus infit:
"orbis, Avite, salus, cui non nova gloria nunc est,
quod rogat Aetius; voluisti, et non nocet hostis:
vis: prodest. inclusa tenes tot milia nutu,
et populis Geticis sola est tua gratia limes;
infensi semper nobis pacem tibi praestant.
victrices, i, prome aquilas; fac, optime, Chunos,
quorum forte prior fuga nos concusserat olim,
bis victos prodesse mihi." sic fatur, et ille
pollicitus votum fecit spem. protinus inde
avolat et famulas in proelia concitat iras.
ibant pellitae post classica Romula turmae,
ad nomen currente Geta; timet aere vocari
dirutus, opprobrium, non damnum barbarus horrens.
hos ad bella trahit iam tum spes orbis Avitus,
vel iam privatus vel adhuc."""

LAT = {
    "prosper": "sed cum transito Rheno saevissimos eius impetus multae Gallicanae urbes experirentur, cito et nostris et Gothis placuit, ut furori superborum hostium consociatis exercitibus repugnaretur, tantaque patricii Aetii providentia fuit, ut raptim congregatis undique bellatoribus viris adversae multitudini non inpar occurreret.",
    "haun": "[... exercitibus repugnaretur.] Thorismotus tunc regnum Gothorum regebat. [tantaque patricii Aetii providentia fuit, ut] tam Gothos, ut diximus, quam etiam Francos in auxilium, qui tunc vicina Rheno obtinebant, de industria vocaret. non enim tunc reges gens Francorum habebat, sed ducibus contenti erant.",
    "ovet": "Hoc tempore Attila Hunorum rex invadit Gallias. contra hunc commendans se domno Petro apostolo patricius Aetius perrexit dei auxilio pugnaturus.",
}

SECTIONS = [
    ("enemies", "Old enemies", "Old enemies, 436–439",
     "Before 451 the Goths of Toulouse and the Roman army had fought each other, and Aetius' generals had used Hunnic horsemen against them. Jordanes passes quickly over it; Sidonius, praising Avitus, does not.",
     [
         ("jord", 176, "Get. 176 · Mommsen p. 104", "Theoderic, and Aetius",
          "What more? On the death of Vallia, who had been little fortunate for the Gauls (to repeat what we said above), Theoderic succeeded to the kingdom, most prosperous and more fortunate, a man of the greatest self-control, to be prized for strength of mind and body. Against him, in the consulship of Theodosius and Festus, the Romans broke the peace and took up arms in Gaul, with Huns joined to them as auxiliaries; for they had been disturbed by the band of federate Goths who, with count Gaina, had raised a storm at Constantinople. The patrician Aetius was then in command of the soldiers: born of the stock of the bravest Moesians in the city of Durostorum, son of Gaudentius, a man who bore the labours of war, born above all others for the Roman state, who had forced the proud barbarism of the Suevi and the Franks by vast slaughter to serve the Roman empire.",
          "The consulship of Theodosius and Festus is 439. Jordanes' reason is confused: the revolt of Gainas at Constantinople was in 400."),
         ("jord", 177, "Get. 177 · Mommsen p. 104", "Litorius and the Huns",
          "With Huns as auxiliaries, under the leadership of Litorius, the Roman army also marched against the Goths; and when for a long time the lines had stood drawn up on both sides, both brave and neither the weaker, they joined right hands and returned to their former concord. A treaty was confirmed between them, peace was concluded in good faith, and each side withdrew.",
          "Jordanes passes over the end of the campaign: Litorius was defeated and taken before Toulouse in 439, as Sidonius says in the next unit ('capto ... Litorio')."),
         ("sid", "295–311", "Sid. Carm. VII 295–311 · MGH AA VIII pp. 210–211", "Avitus renews the treaty",
          "After these deeds of the hero (I call you to witness, livid Styx), he was governing as prefect laws that were inviolate to me; and Gaul, worn out by her usual ruins, took him as her head while she grew pale at the Gothic wrath. Aetius, broken, could do nothing by prayer, by payment or by soldiers; with Litorius taken, the losses of the lands lay open; Theoderic had resolved to push his borders to the Rhône, and the Goths had no need to fight, only to move. The savage victor sharpens his raging anger; he holds it against us that he felt a Scythian enemy before his walls; and nothing is more grievous than a frightened man, if he ever happens to win. When no defence was left anywhere, and nothing to your generals, Rome, you, Avitus, renew the treaty; your letter, once read, tames the savage king; it is enough that you have ordered what the world entreats. Will the peoples and nations to come ever believe it? A Roman's letter undoes what you, barbarian, win.",
          "Sidonius delivered the panegyric in Rome on 1 January 456, when Avitus, emperor since 455, entered his consulship; Avitus was his father-in-law. The 'Scythian enemy before his walls' are the Hunnic auxiliaries of Litorius at Toulouse. The panegyric gives Avitus alone the credit for the peace with the Goths."),
     ]),
    ("embassy", "Embassy", "The emperor's embassy to Theoderic",
     "Jordanes gives the speeches: Valentinian asks the Goths to join against 'the tyrant of the world', and Theoderic answers that the Romans have made Attila the Goths' enemy too.",
     [
         ("jord", 187, "Get. 187 · Mommsen p. 107", "'The tyrant of the world'",
          "Then the emperor Valentinian sent an embassy to the Visigoths and their king Theoderic with these words: 'It befits your wisdom, bravest of nations, to conspire against the tyrant of the world, who wants to hold the whole world in slavery, who seeks no causes for war but thinks whatever he does is lawful. He measures his ambition by the strength of his arm and sates his pride with licence; scorning right and law, he shows himself an enemy even of nature. He deserves the hatred of all, who proves himself the common enemy of all.",
          "The speeches in Jordanes are his own composition or Cassiodorus', in the manner of ancient historians, not records of what was said."),
         ("jord", 188, "Get. 188 · Mommsen p. 107", "'Remember'",
          "Remember, I pray, what surely cannot be forgotten: that you were driven out by the Huns not in war, where fortune is common to both, but, what grieves more deeply, attacked by treachery. To say nothing of us, can you bear this arrogance unavenged? Strong in arms, take the part of your own griefs and join hands in common. Help also the state of which you hold a member. How much an alliance is to be sought and embraced by us, ask the enemy's own plans.'",
          "'Driven out by the Huns': the flight of the Goths across the Danube in 376, which Jordanes told earlier. 'The state of which you hold a member': the Visigoths were settled in Aquitaine as federates of the Empire."),
         ("jord", 189, "Get. 189 · Mommsen p. 107", "'You have made Attila our enemy too'",
          "With these words and the like the envoys of Valentinian moved King Theoderic. He answered them: 'Romans, you have your wish; you have made Attila our enemy too. We follow him wherever he calls us; and though he is puffed up with victories over different peoples, the Goths know how to fight the proud. I would call no war heavy except one that a bad cause weakens; he fears nothing sad on whom majesty has smiled.'", ""),
         ("jord", 190, "Get. 190 · Mommsen p. 107", "Theoderic's sons",
          "His companions acclaim the leader's answer, and the people follow gladly. All are eager for battle; the Huns are now longed for as enemies. So a countless host of the Visigoths is brought out by King Theoderic. He left four sons at home, Friderich and Eurich, Retemer and Himnerith, and took with him as partners of the labour only the two elder, Thorismud and Theoderic. A happy muster, a safe help, a sweet companionship, to have the comfort of those with whom it is a delight even to face dangers together.",
          "Thorismud succeeds his father on the battlefield (module 4); both Theoderic II and Euric, left at home here, later reign."),
     ]),
    ("coalition", "Coalition", "Gathering the coalition",
     "Who came, and how. Prosper and Jordanes in nearly the same words; a continuation of Prosper on the Franks 'who had no kings'; and Sidonius' version, in which the Goths stay at home until Avitus fetches them.",
     [
         ("lat", "prosper", "Prosper 1364 · MGH AA IX p. 481", "'Our people and the Goths'",
          "But when, after he had crossed the Rhine, many cities of Gaul felt his most savage attacks, our people and the Goths quickly agreed to resist the fury of the proud enemy with their armies joined; and so great was the foresight of the patrician Aetius that, gathering fighting men in haste from every side, he met the opposing multitude on equal terms.",
          "The second sentence of Prosper's entry for 451; the first is in module 1 ('Only against the Goths'), the rest, on the battle, belongs to module 4."),
         ("jord", 191, "Get. 191 · Mommsen pp. 107–108", "The allies",
          "On the Roman side, so great was the foresight of the patrician Aetius, on whom the state of the western region then rested, that, gathering warriors from every side, he met the fierce and boundless multitude on equal terms. For these came as auxiliaries: Franks, Sarmatians, Armoricans, Liticians, Burgundians, Saxons, Riparians, Olibriones, once Roman soldiers but now counted among the auxiliaries, and some other Celtic or German peoples.",
          "The first sentence is Prosper's, almost word for word (previous unit): Jordanes used Prosper's chronicle. Sidonius puts Burgundians and Franks in Attila's army (below): both peoples may have fought on both sides."),
         ("lat", "haun", "Add. ad Prosp. Haun. · MGH AA IX pp. 301–302", "Franks without kings",
          "[...] Thorismud was then ruling the kingdom of the Goths. [And so great was the foresight of the patrician Aetius that] he deliberately called to his help both the Goths, as we have said, and the Franks too, who then held the lands near the Rhine. For at that time the Frankish people had no kings, but were content with dukes.",
          "A later continuation of Prosper, preserved in a Copenhagen manuscript; the words in square brackets are Prosper's, as Mommsen prints them. It is wrong on Thorismud, who succeeded only when his father fell in the battle; its sentence on the Franks has no parallel in the other sources."),
         ("sid", "316–331", "Sid. Carm. VII 316–331 · MGH AA VIII p. 211", "The peoples of the North",
          "His prefecture completed, he had at last given himself to the country (yet never to leisure, never to unwarlike idleness: his zeal and care for arms were always awake in his quiet), when suddenly the barbarian world, bursting out in tumult, had poured the whole North into you, Gaul. The savage Gepid follows the warlike Rugian, with the Gelonian beside him; the Burgundian drives on the Scirian; the Hun, the Bellonotian, the Neurian, the Bastarnian, the Thuringian, the Bructerian, and the Frank whom the Neckar washes with its reedy water, burst out; the Hercynian forest, cut down by the axe, fell quickly into boats and covered the Rhine with alder; and already Attila had spread himself with his terrible squadrons over your fields, Belgian. Aetius had scarcely left the Alps, leading only a thin and scanty strength of auxiliaries without regular troops, and, too trusting, presuming in vain that the Gothic host would join his camp.",
          "A poet's catalogue, partly of classical names (Gelonians and Neurians come from Herodotus' Scythia, the Bastarnians from Hellenistic times), partly of the 450s. It puts Burgundians and Franks among the invaders; Jordanes counts them among Aetius' allies."),
         ("sid", "332–353", "Sid. Carm. VII 332–353 · MGH AA VIII pp. 211–212", "Aetius asks Avitus",
          "But when the news struck the commander that the Goths were waiting in their own homes for the Huns, an enemy they almost despised, he turned over every plan, wavering, and pressed his mind with waves of care. At last, as he wavered, the resolve settled to entreat that lofty man; and with all the chiefs gathered together, in their presence, as a suppliant he began thus: 'Avitus, salvation of the world, for whom it is no new glory that Aetius asks something of you: you willed it, and the enemy does no harm; you will it, and he is of use. By your nod you hold so many thousands shut in, and for the Gothic peoples your favour alone is the frontier; always hostile to us, they keep the peace for you. Go, bring out the victorious eagles; best of men, make the Huns, whose earlier rout once shook us, twice defeated, of use to me.' So he spoke; and Avitus, by promising, turned the prayer into hope. At once he hurries away and stirs the angers of the Goths, now his servants, to battle. The squadrons clad in skins marched after the Roman trumpets, the Goth running at the name; the barbarian fears to be called 'docked of pay' at the sound of the brass, dreading the disgrace, not the loss. These Avitus drew to war, already then the hope of the world, whether already a private man or still in office.",
          "In Sidonius, unlike Jordanes, the Goths had meant to wait for the Huns at home, and only Avitus' credit brought them. 'Docked of pay' (aere dirutus) is a Roman military penalty. The sense of 'whose earlier rout once shook us' is uncertain."),
         ("lat", "ovet", "Add. altera c. 18 · MGH AA IX p. 490", "Commended to Saint Peter",
          "At this time Attila, king of the Huns, invades Gaul. Against him the patrician Aetius set out, commending himself to the lord Peter the apostle, to fight with God's help.",
          "From a short continuation of Prosper in a manuscript of Oviedo. The only source carried here that gives Aetius a religious act."),
     ]),
    ("sangiban", "Sangiban", "Sangiban the Alan",
     "The coalition's weak point in Jordanes: the king of the Alans settled at Orléans, suspected of treason and placed in the middle of the line where he could be watched.",
     [
         ("jord", 194, "Get. 194 · Mommsen p. 108", "Sangiban's offer",
          "But before we tell the order of the battle itself, it seems necessary to set out what happened in the very course of the war, since the battle was as complicated and tangled as it was famous. For Sangiban, king of the Alans, terrified by fear of what was coming, promised to give himself up to Attila and to bring Orléans, the city of Gaul where he was then staying, under his rule.",
          "No other source carried here mentions Sangiban's treason; Jordanes alone, writing for a Gothic audience, tells it."),
         ("jord", 195, "Get. 195 · Mommsen p. 108", "Watched in the middle",
          "When Theoderic and Aetius learned of it, they built great earthworks round that city before Attila came, kept Sangiban under watch as a suspect, and placed him with his own people in the middle of their auxiliaries. Attila, king of the Huns, struck by this turn of events and distrusting his own forces, was afraid to join battle. Turning over in his mind a flight sadder than death itself, he resolved to inquire into the future through soothsayers.",
          "Gregory of Tours tells the relief of Orléans differently, as the work of the bishop Anianus (module 3). The soothsayers' answer follows in Getica 196 (module 4)."),
     ]),
]


def build():
    secs = []
    for sid, zk, titel, blurb, units in SECTIONS:
        out = []
        for i, (kind, key, pg, t, en, note) in enumerate(units, 1):
            orig = jl(key) if kind == "jord" else {"295–311": SID_295, "316–331": SID_316, "332–353": SID_332}[key] if kind == "sid" else LAT[key]
            u = {"n": i, "pg": pg, "titel": t, "orig": orig, "en": en}
            if note:
                u["note"] = note
            out.append(u)
        secs.append({"id": sid, "zk": zk, "titel": titel, "blurb": blurb, "units": out})
    data = {
        "titel": "The alliance, 451",
        "autor": "Jordanes, Getica (about 551); Sidonius Apollinaris, panegyric on Avitus (456); Prosper of Aquitaine and two continuations of his chronicle",
        "jahr": "439–451",
        "orig_sprache": "la",
        "pg_label": "",
        "quelle": "Jordanes, Getica, ed. Th. Mommsen, MGH Auct. ant. V.1 (Berlin 1882), pp. 104, 107–108 (archive.org cuaiordanisroman00jord); Sidonius, Carmina VII, ed. Chr. Luetjohann, MGH Auct. ant. VIII (Berlin 1887), pp. 210–212 (archive.org bub_gb_W-0JAAAAIAAJ); Prosper, Epitoma chronicon, and the Additamenta ad Prosperum Hauniensia and altera, ed. Th. Mommsen, MGH Auct. ant. IX (Berlin 1892), pp. 481, 301–302, 490 (archive.org chronicaminorasa09momm). All public domain.",
        "hinweis": "The Latin follows the printed editions, checked against the page images; Sidonius' verses were transcribed by eye, the machine reading of that volume being unusable. In the Copenhagen continuation, words in square brackets are Prosper's, as Mommsen marks them. The English is the site's working translation, close to the Latin and dedicated to the public domain; for Sidonius' verse it is prose. No public-domain English translation of the panegyric exists.",
        "sections": secs,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in secs)} units in {len(secs)} sections")


if __name__ == "__main__":
    build()
