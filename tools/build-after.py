"""Build data/after.json, module 5: afterwards and afterlife, 452-1918.

Sources (public domain), each checked against the page image or a scan:
- Jordanes, Getica 219-223, 225-228, 254-263, ed. Th. Mommsen, MGH Auct. ant. V.1 (1882), pp. 114-116, 123-126
  (Latin Library text, compared word by word with the OCR of archive.org cuaiordanisroman00jord).
- Prosper 1367, 1370, 1371, 1373, MGH AA IX (1892) pp. 482-483; Chronica Gallica a. 511 c. 621-622, p. 663
  (archive.org chronicaminorasa09momm).
- Hydatius c. 154, 156, 160, MGH AA XI (1894) pp. 26-27; Marcellinus Comes a. 454-455, p. 86;
  Cassiodorus, Chronica 1255-1256, 1258, 1260, p. 157 (archive.org chronicaminorasa11momm).
- Sidonius, Carmen VII 357-362, ed. Luetjohann, MGH AA VIII (1887) p. 212 (archive.org bub_gb_W-0JAAAAIAAJ).
- Gregory of Tours, Historiae II.7 (end), ed. Arndt, MGH SRM I.1 p. 71; English: Dalton (1927) vol. II p. 48.
- Gibbon, Decline and Fall, ch. 35 (text: Project Gutenberg #733; compared with the octavo of 1788,
  vol. VI pp. 116-121, archive.org 10433040bsb).
- Creasy, The Fifteen Decisive Battles of the World (New York: Harper 1851) pp. 153-155
  (archive.org cu31924027750763), transcribed from the page images.
- Wilhelm II, speech at Bremerhaven, 27 July 1900, official text in J. Penzler, Die Reden Kaiser Wilhelms II.,
  vol. 2 (Leipzig: Reclam [1904]) pp. 209-211 (archive.org dieredenkaiserwi02wilhuoft).
- Kipling, 'For All We Have and Are' (1914), The Years Between (London 1919) pp. 21-22
  (archive.org yearsbetween00kipluoft).
English of the Latin and German: the site's working translation (CC0), except Gregory (Dalton).
Run from the repository root:  python tools/build-after.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "after.json"
jord = json.loads((ROOT / "tools" / "src" / "jord5.json").read_text(encoding="utf-8"))


def jl(*ns):
    return " ".join(jord[str(n)].replace("Vna tamen", "Una tamen") for n in ns)


LAT = {
    "prosp1367": "Attila redintegratis viribus, quas in Gallia amiserat, Italiam ingredi per Pannonias intendit, nihil duce nostro Aetio secundum prioris belli opera prospiciente, ita ut ne clusuris quidem Alpium, quibus hostes prohiberi poterant, uteretur, hoc solum spebus suis superesse existimans, si ab omni Italia cum imperatore discederet. sed cum hoc plenum dedecoris et periculi videretur, continuit verecundia metum, et tot nobilium provinciarum latissima eversione credita est saevitia et cupiditas hostilis explenda, nihilque inter omnia consilia principis ac senatus populique Romani salubrius visum est, quam ut per legatos pax truculentissimi regis expeteretur. suscepit hoc negotium cum viro consulari Avieno et viro praefectorio Trygetio beatissimus papa Leo auxilio dei fretus, quem sciret numquam piorum laboribus defuisse. nec aliud secutum est quam praesumpserat fides. nam tota legatione dignanter accepta ita summi sacerdotis praesentia rex gavisus est, ut et bello abstinere praeciperet et ultra Danuvium promissa pace discederet.",
    "hyd154": "Secundo regni anno principis Marciani Huni, qui Italiam praedabantur, aliquantis etiam civitatibus inruptis, divinitus partim fame, partim morbo quodam plagis caelestibus feriuntur: missis etiam per Marcianum principem Aetio duce caeduntur auxiliis pariterque in sedibus suis et caelestibus plagis et per Marciani subiguntur exercitum et ita subacti pace facta cum Romanis proprias universi repetunt sedes, ad quas rex eorum Attila mox reversus interiit.",
    "cass1255": "[1255] His conss. Attila redintegratis viribus Aquileiam magna vi dimicans introivit. [1256] Cum quo a Valentiniano imp. papa Leo directus pacem fecit.",
    "prosp1371": "Apud Gothos intra Gallias consistentes inter filios Theodoris regis, quorum Thorismodus maximus natu patri successerat, orta dissensio est, et cum rex ea moliretur, quae et Romanae paci et Gothicae adversarentur quieti, a germanis suis, quia noxiis dispositionibus inrevocabiliter instaret, occisus est.",
    "hyd156": "Thurismo rex Gothorum spirans hostilia a Theoderico et Frederico fratribus iugulatur: cui Theodericus succedit in regno.",
    "gall621": "[621] Thurismundus rex Gothorum Arelatem circumspectat, qui a fratribus suis occisus. [622] Attila occiditur.",
    "greg7e": "nec multo post Aquileia a Chunis capta, incensa atque deruta, Italia pervagata atque subversa est. Thorismodus, cui supra meminimus, Alanos bello edomuit, ipsi deinceps post multas lites et bella a fratribus oppraessus ac iugulatus interiit.",
    "marc454a": "Attila rex Hunnorum Europae orbator provinciae noctu mulieris manu cultroque confoditur. quidam vero sanguinis reiectione necatum perhibent.",
    "prosp1370": "Attila in sedibus suis mortuo magna primum inter filios ipsius certamina de optinendo regno exorta sunt, deinde aliquot gentium, quae Chunis parebant, defectus secuti causas et occasiones bellis dederunt, quibus ferocissimi populi mutuis incursibus contererentur.",
    "cass1258": "His conss. Attila in sedibus suis moritur.",
    "prosp1373": "Inter Valentinianum Augustum et Aetium patricium post promissae invicem fidei sacramenta, post pactum de coniunctione filiorum, dirae inimicitiae convaluerunt, et unde fuit gratia caritatis augenda, inde exarsit fomes odiorum, incentore, ut creditum est, Heraclio spadone, qui ita sibi imperatoris animum insincero famulatu obstrinxerat, ut eum facile in quae vellet impelleret. cum ergo Heraclius sinistra omnia imperatori de Aetio persuaderet, hoc unum creditum est saluti principis profuturum, si inimici molitionem suo opere praeoccupavisset. unde Aetius imperatoris manu et circumstantium gladiis intra palatii penetralia crudeliter confectus est, Boetio praetorii praefecto simul perempto, qui eidem multa amicitia copulabatur.",
    "hyd160": "Aetius dux et patricius fraudulenter singularis accitus intra palatium manu ipsius Valentiniani imperatoris occiditur et cum ipso per spatharium eius aliqui singulariter intromissi iugulantur honorati.",
    "marc454b": "[454] Aetius magna Occidentalis rei publicae salus et regi Attilae terror a Valentiniano imperatore cum Boethio amico in palatio trucidatur, atque cum ipso Hesperium cecidit regnum nec hactenus valuit relevari. [455] Valentinianus princeps dolo Maximi patricii, cuius etiam fraude Aetius perierat, in campo Martio per Optilam et Thraustilam Aetii satellites iam percusso Heraclio spadone truncatus est.",
    "cass1260": "His conss. Aetius patricius in Palatio manu Valentiniani imp. extinctus est, Boetius vero praefectus praetorio amicus eius circumstantium gladiis interemptus.",
    "sid357": "Iam prope fata tui bis senas vulturis alas\ncomplebant (scis namque tuos, scis, Roma, labores):\nAetium Placidus mactavit semivir amens.\nvixque tuo impositum capiti diadema, Petroni:\nilico barbaries, nec non sibi capta videri\nRoma Getis tellusque suo cessura furori.",
    "kaiser": "Eine große Aufgabe harrt eurer: ihr sollt das schwere Unrecht, das geschehen ist, sühnen. Die Chinesen haben das Völkerrecht umgeworfen, sie haben in einer in der Weltgeschichte nicht erhörten Weise der Heiligkeit des Gesandten, den Pflichten des Gastrechts Hohn gesprochen. Es ist das um so empörender, als dies Verbrechen begangen worden ist von einer Nation, die auf ihre uralte Kultur stolz ist. Bewährt die alte preußische Tüchtigkeit, zeigt euch als Christen im freudigen Ertragen von Leiden, möge Ehre und Ruhm euren Fahnen und Waffen folgen, gebt an Manneszucht und Disziplin aller Welt ein Beispiel.\n\nIhr wißt es wohl, ihr sollt fechten gegen einen verschlagenen, tapferen, gut bewaffneten, grausamen Feind. Kommt ihr an ihn, so wißt: Pardon wird (euch) nicht gegeben, Gefangene werden nicht gemacht. Führt eure Waffen so, daß auf tausend Jahre hinaus kein Chinese mehr es wagt, einen Deutschen scheel anzusehen. Wahrt Manneszucht.",
}

GIBBON_1 = "The discipline and tactics of the Greeks and Romans form an interesting part of their national manners. The attentive study of the military operations of Xenophon, or Caesar, or Frederic, when they are described by the same genius which conceived and executed them, may tend to improve (if such improvement can be wished) the art of destroying the human species. But the battle of Chalons can only excite our curiosity by the magnitude of the object; since it was decided by the blind impetuosity of Barbarians, and has been related by partial writers, whose civil or ecclesiastical profession secluded them from the knowledge of military affairs. Cassiodorus, however, had familiarly conversed with many Gothic warriors, who served in that memorable engagement; “a conflict,” as they informed him, “fierce, various, obstinate, and bloody; such as could not be paralleled either in the present or in past ages.” The number of the slain amounted to one hundred and sixty-two thousand, or, according to another account, three hundred thousand persons; and these incredible exaggerations suppose a real and effective loss sufficient to justify the historian’s remark, that whole generations may be swept away by the madness of kings, in the space of a single hour."
GIBBON_2 = "It was determined, in a general council of war, to besiege the king of the Huns in his camp, to intercept his provisions, and to reduce him to the alternative of a disgraceful treaty or an unequal combat. But the impatience of the Barbarians soon disdained these cautious and dilatory measures; and the mature policy of Ætius was apprehensive that, after the extirpation of the Huns, the republic would be oppressed by the pride and power of the Gothic nation. The patrician exerted the superior ascendant of authority and reason to calm the passions, which the son of Theodoric considered as a duty; represented, with seeming affection and real truth, the dangers of absence and delay and persuaded Torismond to disappoint, by his speedy return, the ambitious designs of his brothers, who might occupy the throne and treasures of Thoulouse. After the departure of the Goths, and the separation of the allied army, Attila was surprised at the vast silence that reigned over the plains of Chalons: the suspicion of some hostile stratagem detained him several days within the circle of his wagons, and his retreat beyond the Rhine confessed the last victory which was achieved in the name of the Western empire."
CREASY_1 = "A broad expanse of plains, the Campi Catalaunici of the ancients, spreads far and wide around the city of Châlons, in the northeast of France. The long rows of poplars, through which the River Marne winds its way, and a few thinly-scattered villages, are almost the only objects that vary the monotonous aspect of the greater part of this region. But about five miles from Châlons, near the little hamlets of Chape and Cuperly, the ground is indented and heaped up in ranges of grassy mounds and trenches, which attest the work of man’s hands in ages past, and which, to the practiced eye, demonstrate that this quiet spot has once been the fortified position of a huge military host. Local tradition gives to these ancient earth-works the name of Attila’s Camp. Nor is there any reason to question the correctness of the title, or to doubt that behind these very ramparts it was that 1400 years ago the most powerful heathen king that ever ruled in Europe mustered the remnants of his vast army, which had striven on these plains against the Christian soldiery of Thoulouse and Rome. Here it was that Attila prepared to resist to the death his victors in the field; and here he heaped up the treasures of his camp in one vast pile, which was to be his funeral pyre should his camp be stormed. It was here that the Gothic and Italian forces watched, but dared not assail their enemy in his despair, after that great and terrible day of battle."
CREASY_2 = "The victory which the Roman general, Aëtius, with his Gothic allies, had then gained over the Huns, was the last victory of imperial Rome. But among the long Fasti of her triumphs, few can be found that, for their importance and ultimate benefit to mankind, are comparable with this expiring effort of her arms. It did not, indeed, open to her any new career of conquest—it did not consolidate the relics of her power—it did not turn the rapid ebb of her fortunes. The mission of imperial Rome was, in truth, already accomplished. [...] But it was all-important to mankind what nations should divide among them Rome’s rich inheritance of empire. Whether the Germanic and Gothic warriors should form states and kingdoms out of the fragments of her dominions, and become the free members of the commonwealth of Christian Europe; or whether pagan savages, from the wilds of Central Asia, should crush the relics of classic civilization and the early institutions of the Christianized Germans in one hopeless chaos of barbaric conquest. The Christian Visigoths of King Theodoric fought and triumphed at Châlons, side by side with the legions of Aëtius. Their joint victory over the Hunnish host not only rescued for a time from destruction the old age of Rome, but preserved for centuries of power and glory the Germanic element in the civilization of modern Europe."
CREASY_3 = "In order to estimate the full importance to mankind of the battle of Châlons, we must keep steadily in mind who and what the Germans were, and the important distinctions between them and the numerous other races that assailed the Roman empire; and it is to be understood that the Gothic and Scandinavian nations are included in the German race."
KIPLING = "For all we have and are,\nFor all our children’s fate,\nStand up and take the war,\nThe Hun is at the gate!\nOur world has passed away,\nIn wantonness o’erthrown.\nThere is nothing left to-day\nBut steel and fire and stone!\n    Though all we knew depart,\n    The old Commandments stand:—\n    ‘In courage keep your heart,\n    In strength lift up your hand.’\n\nOnce more we hear the word\nThat sickened earth of old:—\n‘No law except the Sword\nUnsheathed and uncontrolled.’\nOnce more it knits mankind,\nOnce more the nations go\nTo meet and break and bind\nA crazed and driven foe."

SECTIONS = [
    ("italy", "Italy", "Italy and Pope Leo, 452",
     "A year after the battle Attila crossed the Julian Alps. Aquileia fell; Milan and Pavia were sacked; and on the Mincio a Roman embassy led by Pope Leo met him, and he turned back. Jordanes tells it with an omen of storks; Prosper, who lived in Leo's Rome, blames Aetius; Hydatius gives the credit to famine, disease and an army from the East.",
     [
         ((219,), "Get. 219 · Mommsen p. 114", "Aquileia",
          "Attila, seizing the occasion of the Visigoths' withdrawal, and seeing, as he had often wished, his enemies broken up into parts, soon moved his army, now secure, to crush the Romans, and in his first attack besieged the city of Aquileia, the metropolis of the Venetians, set on a point or tongue of the Adriatic gulf, whose wall on the east is washed by the river Natissa, flowing from Mount Piccis.",
          "'Secure' after the Visigoths' departure: Jordanes ties the invasion of Italy to Aetius' advice to Thorismud (module 4)."),
         ((220, 221), "Get. 220–221 · Mommsen p. 114", "The storks",
          "There, besieging it long and hard and prevailing not at all, since the bravest Roman soldiers resisted from within, with his army already murmuring and wanting to leave, Attila walked round the walls, deliberating whether to break camp or stay longer, and noticed the white birds, that is the storks, which nest on the gables of houses, carrying their young out of the city and, against their custom, bearing them out into the countryside. And being a most shrewd inquirer, he understood, and said to his men: 'Look at the birds that foresee things to come: they are leaving the city that is to perish and deserting the citadels that are to fall, as danger threatens. Let this not be thought empty or uncertain; fear of what is coming changes the habits of creatures that know beforehand.' In short, he fired his men's spirits again for the assault on Aquileia. They built siege engines and brought every kind of artillery to bear, and without delay they broke into the city, plundered it, divided it and laid it waste so cruelly that they left scarcely a trace of it to be seen.",
          ""),
         ((222,), "Get. 222 · Mommsen pp. 114–115", "Milan, Pavia, and Alaric's example",
          "From then on, bolder and not yet sated with Roman blood, the Huns rage through the other cities of the Venetians. Milan too, the metropolis of Liguria and once a royal city, they lay waste in the same way, and Ticinum they cast down with a like fate; raging, they strike the neighbouring places and demolish almost all Italy. And when his mind had turned to going on to Rome, his men, as the historian Priscus relates, drew him away, not out of care for the city, to which they were enemies, but holding up the example of Alaric, once king of the Visigoths: they feared for their own king's fortune, because Alaric did not long survive the sack of Rome but soon departed from human affairs.",
          "Ticinum is Pavia. Jordanes cites Priscus: the reason for sparing Rome is the Huns' superstition, not the Pope."),
         ((223,), "Get. 223 · Mommsen p. 115", "Leo on the Mincio",
          "So while his mind wavered between going and not going, and he delayed, deliberating with himself, a peaceful embassy came to him from Rome. For Pope Leo came to him in person in the Ambuleian field of the Venetians, where the river Mincio is crossed by many travellers. He soon laid aside his army's fury and, returning the way he had come, departed beyond the Danube with peace promised, declaring above all, and decreeing with threats, that he would bring worse things on Italy unless they sent him Honoria, the sister of the emperor Valentinian and daughter of Placidia Augusta, with the share of the royal wealth owed to her.",
          "Honoria's offer of marriage is in module 1 (Get. 224). Raphael's fresco (plate 'Leo the Great and Attila') adds Peter and Paul with swords in the sky."),
         ("prosp1367", "Prosper 1367 · MGH AA IX p. 482", "'Our general Aetius provided nothing'",
          "Attila, having restored the strength he had lost in Gaul, set out to enter Italy through Pannonia; and our general Aetius provided nothing in keeping with what he had done in the earlier war, so that he did not even use the barriers of the Alps, by which the enemy could have been kept out, thinking that the only thing left to his hopes was to leave all Italy together with the emperor. But since this seemed full of disgrace and danger, shame held back fear; and it was believed that the enemy's savagery and greed could be sated by the widest ruin of so many noble provinces; and among all the counsels of the emperor, the senate and the Roman people nothing seemed more salutary than to seek peace from the most savage king through envoys. The most blessed Pope Leo took on this task, with the consular Avienus and the former prefect Trygetius, trusting in the help of God, whom he knew never to have failed the labours of the pious. Nor did anything follow other than what faith had presumed. For the whole embassy was received with honour, and the king was so pleased by the presence of the highest priest that he ordered a halt to the war and, having promised peace, went away beyond the Danube.",
          "Prosper, writing in Rome close to Leo, blames Aetius for leaving the Alpine passes open, a year after praising his foresight (module 2). Leo goes with two senators; the king is 'pleased' by him, but no miracle is told."),
         ("hyd154", "Hydatius c. 154 · MGH AA XI pp. 26–27", "Famine, disease, and an army from the East",
          "In the second year of the emperor Marcian, the Huns who were plundering Italy, having broken into several cities as well, are struck by blows from heaven, partly famine, partly some disease; they are also cut down by auxiliaries sent by the emperor Marcian under the general Aetius, and they are subdued both in their own seats by plagues from heaven and by Marcian's army; and so, beaten, they made peace with the Romans and all went back to their own seats, where their king Attila died soon after his return.",
          "Hydatius knows nothing of Leo. Whether this Aetius is the western patrician or an eastern general of the same name is disputed. Marcian's army fought the Huns 'in their own seats', north of the Danube."),
         ("cass1255", "Cassiodorus, Chronica 1255–1256 · MGH AA XI p. 157", "'Sent by the emperor'",
          "[1255] In this consulship Attila, his strength restored, entered Aquileia, fighting with great force. [1256] With him Pope Leo, sent by the emperor Valentinian, made peace.",
          "Cassiodorus makes Leo the emperor's envoy."),
     ]),
    ("thorismud", "Thorismud", "A second war in Gaul? Thorismud's end",
     "Jordanes alone tells of a second Hunnic invasion of Gaul, against the Alans on the Loire, beaten back by Thorismud 'in almost the same manner as on the Catalaunian fields'. Gregory has a single line on Thorismud defeating the Alans. On Thorismud's death the sources agree: his brothers killed him.",
     [
         ((225, 226), "Get. 225–226 · Mommsen pp. 115–116", "Attila turns on the Alans",
          "So Attila went back to his seats, and as if regretting his idleness and finding it hard to cease from war, he sent envoys to Marcian, emperor of the East, threatening to lay waste the provinces because what the emperor Theodosius had once promised him was not being paid, and showing himself more inhuman than usual to his enemies. While doing this, crafty and cunning as he was, he threatened in one direction and moved his arms in another, and, what remained for his anger, turned his face against the Visigoths. But he did not have the success he had had against the Romans. For returning by roads different from before, he resolved to bring under his rule the part of the Alans settled across the river Loire, so that, the face of the war changed through them, he might threaten more terribly. So, setting out from the provinces of Dacia and Pannonia, where the Huns then lived with various subject nations, Attila moved his army against the Alans.",
          ""),
         ((227,), "Get. 227 · Mommsen p. 116", "'Twice beaten'",
          "But Thorismud, king of the Visigoths, foreseeing Attila's deceit with no less subtlety, came first to the Alans with all speed, and there, prepared, met Attila's movements as he arrived; and when battle was joined, in almost the same manner as before on the Catalaunian fields, he drove him from the hope of victory and, sending him back routed from his parts without a triumph, forced him to flee to his own seats. So Attila, famous and master of many victories, while he sought to cast off the reputation of a loser and to wipe out what he had suffered from the Visigoths before, suffered it twice and withdrew without glory.",
          "No other source tells of this campaign, and many historians doubt it, or take it for a doublet of 451. Gregory's line that Thorismund 'overcame the Alans in battle' (below) may be its kernel."),
         ((228,), "Get. 228 · Mommsen p. 116", "The footstool",
          "Thorismud, having driven the bands of Huns from the Alans without any harm to his own men, went to Toulouse and settled his people in quiet peace; and in the third year of his reign, when he was ill and was having blood let from a vein, he was killed, Ascalc his client telling his enemies that his weapons had been taken away. Yet with the one hand he had free, holding a footstool, he became the avenger of his own blood, killing several of those who plotted against him.",
          "Jordanes does not name the brothers; the chronicles below do."),
         ("prosp1371", "Prosper 1371 · MGH AA IX p. 483", "'Contrary to Roman peace'",
          "Among the Goths settled within Gaul a quarrel arose between the sons of King Theoderic, of whom Thorismod, the eldest, had succeeded his father; and since the king was planning things contrary both to Roman peace and to Gothic quiet, he was killed by his brothers, because he pressed on irrevocably with harmful designs.",
          "In Prosper Thorismod is a danger to Rome, which is what Jordanes' Aetius feared (module 4)."),
         ("hyd156", "Hydatius c. 156 · MGH AA XI p. 27", "Theoderic and Frederic",
          "Thurismo, king of the Goths, breathing hostility, is slain by his brothers Theoderic and Frederic; Theoderic succeeds him in the kingdom.",
          "Theoderic II, left at home in 451 (Get. 190, module 2), reigned until 466."),
         ("gall621", "Chron. Gall. a. 511 c. 621–622 · MGH AA IX p. 663", "'Attila is killed'",
          "[621] Thurismund, king of the Goths, eyes Arles; he was killed by his brothers. [622] Attila is killed.",
          "'Eyes Arles' (Arelatem circumspectat): threatens the Roman seat of government in Gaul. 'Attila occiditur', killed, not 'dies': compare Marcellinus below."),
         ("greg7e", "Greg. Hist. II.7 · MGH SRM I p. 71", "Gregory's last lines",
          "And soon afterwards Aquileia was taken, burned, and laid in ruins by the Huns, who roamed over all Italy and laid the land waste. The above-named Thorismund overcame the Alans in battle; but at last, after many disputes and wars, he perished, strangled by his brothers.",
          "English: Dalton (1927), vol. II p. 48, the end of his II.6 (7); the chapter's beginning is in modules 3 and 4."),
     ]),
    ("death", "Death", "Attila's death, 453",
     "Jordanes, after Priscus: a wedding night, a nosebleed, a girl weeping under her veil; the mourning with cut hair and wounded faces, the funeral song, the strava, three coffins and the killing of the gravediggers. Against it, a sixth-century chronicle: stabbed by a woman.",
     [
         ((254,), "Get. 254 · Mommsen pp. 123–124", "Ildico",
          "As the historian Priscus relates, at the time of his death, after countless wives, as was the custom of that people, he took in marriage a very beautiful girl named Ildico; and at his wedding, relaxed by excessive merriment and heavy with wine and sleep, he lay on his back, and the blood which usually flowed from his nose, being stopped in its usual passages, ran down by a deadly road into his throat and killed him. So drunkenness gave a shameful end to a king glorious in war. On the next day, when a great part of the day had passed, the royal attendants, suspecting something sad, broke down the doors after great shouting and found Attila dead without any wound, his death brought about by a flow of blood, and the girl weeping with downcast face under her veil.",
          "Priscus' own account is lost; this is the fullest version of it."),
         ((255,), "Get. 255 · Mommsen p. 124", "The broken bow",
          "Then, as is the custom of that people, they cut off part of their hair and disfigured their faces, made hideous with deep wounds, so that the great warrior should be mourned not with women's laments and tears but with the blood of men. And this marvel was added concerning him: to Marcian, emperor of the East, anxious about so fierce an enemy, the deity appeared in his sleep and showed him, that same night, the bow of Attila broken, as if to say that this people relied greatly on that weapon. The historian Priscus says that he proves this by true testimony. For Attila was held so terrible by great empires that the powers above announced his death to rulers as a gift.",
          ""),
         ((256, 257), "Get. 256–257 · Mommsen p. 124", "The funeral song",
          "Of the honours with which his shade was honoured by his people, let us not fail to tell a little out of much. His body was laid out in the middle of the plain within silken tents, and a spectacle to wonder at is solemnly performed. The choicest horsemen of the whole people of the Huns rode round the place where he lay, in the manner of the circus races, and told his deeds in a funeral song in this order: 'The chief king of the Huns, Attila, born of his father Mundzucus, lord of the bravest nations, who with a power unheard of before him alone possessed the Scythian and Germanic kingdoms, and terrified both empires of the Roman world by taking their cities, and, appeased by their prayers, accepted a yearly tribute so that the rest should not be given up to plunder; and when he had done all this with good fortune, he fell, not by an enemy's wound, not by the treachery of his own, but with his people unharmed, happy amid joys, without feeling pain. Who then would think this a death, which no one thinks calls for vengeance?'",
          "The song in Latin prose is Jordanes' or Priscus' rendering; whether it reflects a real Hunnic lament cannot be known. 'Not by the treachery of his own' answers, as it were in advance, the story of murder below."),
         ((258,), "Get. 258 · Mommsen pp. 124–125", "Three coffins",
          "After he had been mourned with such laments, they celebrate over his tomb, with a huge feast, what they themselves call a strava, and joining opposites to one another they expressed funeral grief mixed with joy; and at night, in secret, they buried the body in the earth and enclosed it in coffins, the first of gold, the second of silver, the third of strong iron, signifying by this that all things befitted the mightiest king: iron because he subdued the nations, gold and silver because he received the ornaments of both empires. They add arms of enemies won in slaughter, trappings precious with the varied glitter of gems, and insignia of every kind with which the splendour of a court is adorned. And so that human curiosity might be kept from such riches, they slew those assigned to the work, a hateful reward; and sudden death came upon the buriers together with the buried.",
          "'Strava' is the one word Jordanes gives as the Huns' own; its origin is disputed. No grave of Attila has ever been found."),
         ("marc454a", "Marcellinus Comes a. 454 · MGH AA XI p. 86", "'By the hand and knife of a woman'",
          "Attila, king of the Huns, the despoiler of the province of Europa, is stabbed at night by the hand and knife of a woman. Some, however, say that he was killed by a vomiting of blood.",
          "Marcellinus wrote in Constantinople in the sixth century and files the death under 454. Europa was a Roman province in Thrace. The murder version lived on in Germanic legend, where Atli, Attila, dies by his wife's hand."),
         ("prosp1370", "Prosper 1370 · MGH AA IX pp. 482–483", "The sons' quarrels",
          "When Attila had died in his own seats, first great struggles over gaining the kingdom arose among his sons; then the defections of some of the peoples which obeyed the Huns gave causes and occasions for wars, in which the fiercest peoples wore each other down by mutual attacks.",
          ""),
         ("cass1258", "Cassiodorus, Chronica 1258 · MGH AA XI p. 157", "'Dies in his seats'",
          "In this consulship Attila dies in his own seats.",
          "The consulship of Opilio and Vincomalus: 453."),
     ]),
    ("nedao", "Nedao", "The empire breaks: the Nedao",
     "Attila's sons divide the peoples like slaves; Ardaric the Gepid, who stood by Attila on the Catalaunian fields (module 4), leads the revolt. A battle of all against all on an unidentified river in Pannonia, usually dated 454.",
     [
         ((259, 260), "Get. 259–260 · Mommsen p. 125", "Ardaric rises",
          "When this was done, as young men's minds are stirred by the ambition of power, a contest over the kingdom arose among Attila's successors, and while all of them, ill-advised, wanted to rule, all together lost the empire. So an abundance of successors often weighs on kingdoms more than a lack. For Attila's sons, of whom through the licence of his lust there was almost a people, demanded that the nations be divided among them in equal lots, so that warlike kings with their peoples should be drawn by lot like a household's slaves. When Ardaric, king of the Gepids, learned this, angry that so many nations should be treated like the meanest slaves, he was the first to rise against Attila's sons, and the success that followed wiped out the shame of servitude laid on him; and by his breaking away he freed not only his own people but the others equally oppressed, since all readily seek what is attempted for the good of all. So they arm for mutual destruction, and battle is joined in Pannonia by the river called Nedao.",
          ""),
         ((261, 262), "Get. 261–262 · Mommsen p. 125", "'The Goth with lances, the Gepid with the sword'",
          "There was a clash of the various peoples whom Attila had held under his rule. Kingdoms are divided with their peoples, and out of one body come different limbs, not such as would share the suffering of one, but such as, the head cut off, would rage against each other: the bravest nations, which had never found their equals against them unless they tore each other apart with mutual wounds. For there, I think, was a spectacle to wonder at, where one could see the Goth fighting with lances, the Gepid raging with the sword, the Rugian breaking off the spears in his own wounds, the Suevian relying on his foot, the Hun on the arrow, the Alan drawing up his line in heavy, the Herul in light armour. After many hard struggles, unexpected victory favoured the Gepids. For nearly thirty thousand, Huns as well as men of the other peoples bringing aid to the Huns, were destroyed by the sword and the conspiracy of Ardaric. In that battle Attila's eldest son, named Ellac, is killed, whom his father was said to have loved so far above the others that he preferred him to all his various children for the kingdom; but fortune did not agree with the father's wishes. For after much slaughter of the enemy, it is agreed, he was killed so manfully that his father, had he lived, would have wished for so glorious a death.",
          "The river Nedao has not been identified with certainty."),
         ((263,), "Get. 263 · Mommsen pp. 125–126", "'The Huns gave way'",
          "His other brothers, after his death, are put to flight along the shore of the Pontic sea, where we described the Goths as having lived before. So the Huns gave way, to whom the whole world was thought to give way. So ruinous a thing is division, that those who terrified when their strength was united fell when divided. This cause of Ardaric, king of the Gepids, was a happy one for the various nations which served the rule of the Huns unwillingly, and it raised their long most sorrowful minds to the longed-for joy of freedom; and many came through their envoys to Roman soil and, received most gladly by Marcian, then emperor, accepted the seats distributed to them to live in.",
          ""),
     ]),
    ("aetius", "Aetius", "Aetius and Valentinian, 454–455",
     "Three years after the battle, the emperor Valentinian III killed Aetius with his own hand in the palace; six months later Aetius' guardsmen killed the emperor. For Marcellinus, writing in Constantinople, the Western realm fell with Aetius; for Sidonius, praising Avitus in 456, Rome's twelve centuries were running out.",
     [
         ("prosp1373", "Prosper 1373 · MGH AA IX p. 483", "The eunuch Heraclius",
          "Between the emperor Valentinian and the patrician Aetius, after oaths of mutual faith had been sworn and an agreement made on the marriage of their children, dire enmities grew strong, and where the grace of love should have grown, from there flared the tinder of hatred, the instigator being, as was believed, the eunuch Heraclius, who had so bound the emperor's mind to himself by insincere service that he could easily drive him wherever he wished. So, since Heraclius persuaded the emperor of every evil about Aetius, this one thing was believed to serve the emperor's safety, that he should forestall his enemy's plotting by his own act. So Aetius was cruelly done to death within the inner rooms of the palace by the emperor's hand and the swords of those standing round, and Boethius, the praetorian prefect, who was joined to him by great friendship, was killed with him.",
          "Other manuscripts give a different reason: 'while Aetius pressed the agreement more insistently and pursued his son's cause too vehemently'. The marriage was to join Aetius' son Gaudentius with the emperor's daughter Placidia. One manuscript dates the murder at Rome to 21 September (a. d. XI Kal. Oct.)."),
         ("hyd160", "Hydatius c. 160 · MGH AA XI p. 27", "Summoned alone",
          "Aetius, general and patrician, treacherously summoned alone into the palace, is killed by the hand of the emperor Valentinian himself, and with him some dignitaries, let in one by one by the emperor's sword-bearer, are slaughtered.",
          ""),
         ("marc454b", "Marcellinus Comes a. 454–455 · MGH AA XI p. 86", "'With him fell the Western realm'",
          "[454] Aetius, the great salvation of the Western state and the terror of King Attila, is slaughtered in the palace by the emperor Valentinian together with his friend Boethius; and with him fell the Hesperian realm, and it has not been able to rise again until now. [455] The emperor Valentinian, by the treachery of the patrician Maximus, through whose deceit Aetius too had perished, was cut down on the Campus Martius by Optila and Thraustila, Aetius' guardsmen, the eunuch Heraclius having been struck down first.",
          "Written in Constantinople under Justinian; 'until now' is the 520s or 530s. The judgement that the West fell with Aetius begins here, not with the moderns."),
         ("cass1260", "Cassiodorus, Chronica 1260 · MGH AA XI p. 157", "In the palace",
          "In this consulship the patrician Aetius was killed in the palace by the hand of the emperor Valentinian; and Boethius, the praetorian prefect, his friend, was slain by the swords of those standing round.",
          ""),
         ("sid357", "Sid. Carm. VII 357–362 · MGH AA VIII p. 212", "'The frantic half-man'",
          "Already the fates were almost filling out the twelve wings of your vulture (you know your labours, Rome, you know them): the frantic half-man Placidus slaughtered Aetius. And scarcely was the diadem set on your head, Petronius, when at once the barbarian world rose, and Rome seemed to the Goths taken for themselves, and the land about to yield to their fury.",
          "The panegyric on Avitus of 1 January 456 (module 2). The twelve vultures of Romulus' augury were read as twelve centuries of Rome; Placidus is Valentinian III (Placidus Valentinianus), 'half-man' an insult; Petronius Maximus followed him for a few weeks. English: the site's prose translation."),
     ]),
    ("afterlife", "Afterlife", "Afterlife: from 'last victory' to 'the Hun'",
     "How an undecided battle became one of the turning points of the world, and the Huns a name for Germans. Gibbon in the 1780s, Creasy in 1851, the Kaiser at Bremerhaven in 1900, Kipling in 1914. The paintings and prints of the same story are on the Plates page.",
     [
         ("gibbon1", "Gibbon, Decline and Fall, ch. 35 · 1788 ed. vol. VI pp. 116–117", "'The madness of kings'",
          GIBBON_1,
          "Gibbon puts Jordanes' 'bellum atrox' into the mouths of Gothic veterans talking to Cassiodorus, and gives 162,000 dead where Mommsen's Jordanes has 165,000, beside Hydatius' 300,000. 'The historian's remark' is Get. 193 (module 4). Text after the Project Gutenberg edition, compared with the octavo of 1788."),
         ("gibbon2", "Gibbon, Decline and Fall, ch. 35 · 1788 ed. vol. VI pp. 120–121", "'The last victory … of the Western empire'",
          GIBBON_2,
          "Gibbon follows Jordanes on Aetius' motive (Get. 216) and calls it 'mature policy'. The phrase 'the last victory which was achieved in the name of the Western empire' is the root of Creasy's 'last victory of imperial Rome'. The 1788 edition spells 'waggons' and 'atchieved'."),
         ("creasy1", "Creasy, Fifteen Decisive Battles (1851), ch. VI · p. 153", "'Attila's Camp'",
          CREASY_1,
          "Edward Creasy's book went through dozens of editions. 'Attila's Camp' at La Cheppe near Châlons is an earthwork far older than the Huns; Creasy's confidence that it was Attila's is his own. The quoted verse from Herbert's 'Attila' (1838) that follows here is left out."),
         ("creasy2", "Creasy, Fifteen Decisive Battles (1851), ch. VI · pp. 154–155", "'The Germanic element'",
          CREASY_2,
          "The bracket marks a passage left out on Rome's civilizing mission. The battle saves not Rome but the 'Christianized Germans': the Huns become 'pagan savages from the wilds of Central Asia'."),
         ("creasy3", "Creasy, Fifteen Decisive Battles (1851), ch. VI · p. 155", "'The German race'",
          CREASY_3,
          "Creasy goes on to praise the Germans' 'personal freedom' and the chastity of their women, quoting the ethnologist Prichard, and then Thomas Arnold on the spread of 'the German element': the nineteenth-century racial reading of 451, which the next unit turns upside down."),
         ("kaiser", "Wilhelm II, Bremerhaven, 27 July 1900 · Penzler II pp. 210–211", "'Pardon wird nicht gegeben'",
          "A great task awaits you: you are to atone for the grave wrong that has been done. The Chinese have overturned the law of nations; in a manner unheard of in the history of the world they have mocked the sanctity of the envoy and the duties of hospitality. It is all the more outrageous because this crime was committed by a nation proud of its ancient culture. Prove the old Prussian efficiency, show yourselves Christians in the joyful bearing of suffering, may honour and glory follow your flags and arms, give the whole world an example of manly discipline and order.\n\nYou know well that you are to fight against a cunning, brave, well-armed, cruel enemy. When you come upon him, know this: quarter will not be given (you), prisoners will not be taken. Wield your weapons so that for a thousand years to come no Chinese will dare to look askance at a German. Keep discipline.",
          "The speech to the troops leaving for the Boxer war, in the official text printed by the Reichsanzeiger and by Penzler. It has no Huns. The version taken down by journalists and printed in the press on 28 July 1900 compared the troops to 'the Huns under their king Etzel' who had made themselves a name for a thousand years; that version gave the speech its name, and the British 'Hun' of 1914 its echo. It is not carried here, because no scan of the newspaper text could be checked (see 'Not carried'). Penzler adds the Wolff agency's different report of the same day."),
         ("kipling", "Kipling, 'For All We Have and Are' (1914) · The Years Between (1919) pp. 21–22", "'The Hun is at the gate!'",
          KIPLING,
          "Published in The Times on 2 September 1914, a month into the war. The poem's first two stanzas; the rest of the poem is in the same volume. Attila's Huns, by way of the Kaiser's speech, became the name for the Germans in Britain, France and America."),
     ]),
]


def build():
    secs = []
    for sid, zk, titel, blurb, units in SECTIONS:
        out = []
        for i, (src, pg, t, en, note) in enumerate(units, 1):
            if isinstance(src, tuple):
                orig = jl(*src)
            elif src in LAT:
                orig = LAT[src]
            else:
                orig = ""
            if src in ("gibbon1", "gibbon2", "creasy1", "creasy2", "creasy3", "kipling"):
                u = {"n": i, "pg": pg, "titel": t, "en": en}
            else:
                u = {"n": i, "pg": pg, "titel": t, "orig": orig, "en": en}
            if note:
                u["note"] = note
            out.append(u)
        sec = {"id": sid, "zk": zk, "titel": titel, "blurb": blurb, "units": out}
        if sid == "afterlife":
            sec["sprache"] = "de"
        secs.append(sec)
    data = {
        "titel": "Afterwards and afterlife, 452–1918",
        "autor": "Jordanes; the chronicles of Prosper, Hydatius, Cassiodorus, Marcellinus and the Gallic chronicle of 511; Sidonius; Gregory of Tours; Gibbon (1788), Creasy (1851), Wilhelm II (1900), Kipling (1914)",
        "jahr": "452–1918",
        "orig_sprache": "la",
        "pg_label": "",
        "quelle": "Jordanes, Getica, ed. Th. Mommsen, MGH Auct. ant. V.1 (Berlin 1882), pp. 114–116, 123–126 (archive.org cuaiordanisroman00jord); Prosper and the Chronica Gallica a. 511, MGH Auct. ant. IX (Berlin 1892), pp. 482–483, 663 (archive.org chronicaminorasa09momm); Hydatius, Marcellinus Comes, Cassiodorus, MGH Auct. ant. XI (Berlin 1894), pp. 26–27, 86, 157 (archive.org chronicaminorasa11momm); Sidonius, Carmina VII, MGH Auct. ant. VIII (Berlin 1887), p. 212; Gregory of Tours, Historiae II.7, ed. W. Arndt, MGH SRM I.1 (1884), p. 71, English by O. M. Dalton (1927); E. Gibbon, The History of the Decline and Fall of the Roman Empire, ch. 35 (octavo ed., London 1788, vol. VI; archive.org 10433040bsb); E. S. Creasy, The Fifteen Decisive Battles of the World (New York: Harper 1851), pp. 153–155 (archive.org cu31924027750763); J. Penzler (ed.), Die Reden Kaiser Wilhelms II., vol. 2 (Leipzig: Reclam [1904]), pp. 209–211 (archive.org dieredenkaiserwi02wilhuoft); R. Kipling, The Years Between (London 1919), pp. 21–22 (archive.org yearsbetween00kipluoft). All public domain.",
        "hinweis": "The Latin follows the printed editions, checked against the page images; Jordanes' text, from the Latin Library, was compared word by word with Mommsen's. Gibbon, Creasy and Kipling wrote in English and are given as printed (Gibbon after the Project Gutenberg text, compared with the octavo of 1788); the Kaiser's speech is in German with the site's translation. The other English is the site's working translation, dedicated to the public domain, except Gregory (Dalton).",
        "sections": secs,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in secs)} units in {len(secs)} sections")


if __name__ == "__main__":
    build()
