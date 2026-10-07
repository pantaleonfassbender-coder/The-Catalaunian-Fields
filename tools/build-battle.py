"""Build data/battle.json, module 4: the battle and the withdrawal, 451.

Sources (public domain), each checked against the page image:
- Jordanes, Getica 192-193, 196-218, ed. Th. Mommsen, MGH Auct. ant. V.1 (1882), pp. 108-114
  (text from the Latin Library, which follows Mommsen, checked word by word against the OCR of
  archive.org cuaiordanisroman00jord; readings such as rubor 198 and notibus 200 are Mommsen's).
- Prosper, Epitoma chronicon 1364 (third sentence), MGH AA IX (1892) pp. 481-482; Additamenta ad Prosperum
  Hauniensia p. 302; Continuatio codicis Reichenaviensis c. 19 p. 490; Chronica Gallica a. 511 c. 615 p. 663
  (archive.org chronicaminorasa09momm, page = index n - 15).
- Hydatius c. 150. 152. 153, MGH AA XI (1894) p. 26 (archive.org chronicaminorasa11momm, page = index n - 11);
  Cassiodorus, Chronica 1253, p. 157; Isidore, Historia Gothorum 25 (longer recension), pp. 277-278
  (same scan, page = index n - 15 in that part of the volume).
- Gregory of Tours, Historiae II.7 (from 'His diebus'), ed. W. Arndt, MGH SRM I.1 (1884) pp. 69-71
  (archive.org monumentagerman01hann); English: O. M. Dalton (1927), vol. II pp. 47-48.
English of Jordanes and the chronicles: the site's working translation (CC0).
Run from the repository root:  python tools/build-battle.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "battle.json"
jord = json.loads((ROOT / "tools" / "src" / "jordanes_ll.json").read_text(encoding="utf-8"))


def jl(*ns):
    return " ".join(re.sub(r"\s+[XLV]+\.\s*$", "", jord[str(n)]).strip() for n in ns)


LAT = {
    "prosper": "in quo conflictu quamvis neutris cedentibus inaestimabiles strages commorientium factae sint, Chunos tamen eo constat victos fuisse, quod amissa proeliandi fiducia qui superfuerant ad propria reverterunt.",
    "cass": "His conss. Romani Aetio duce Gothis auxiliaribus contra Attilam in campo Catalaunico pugnaverunt. qui virtute Gothorum superatus abscessit.",
    "reich": "Pugna facta in Galliis inter Aetium et Attilanum regem Hunorum cum utriusque populi caede. Attila fugatur in Gallias superiores.",
    "hyd": "[150] gens Hunorum pace rupta depraedatur provincias Galliarum. plurimae civitates effractae: in campis Catalaunicis haud longe de civitate, quam effregerant, Mettis, Aetio duci et regi Theodori, quibus erat in pace societas, aperto Marte confligens divino caesa superatur auxilio: bellum nox intempesta diremit. rex illic Theodorus prostratus occubuit: CCC ferme milia hominum in eo certamine cecidisse memorantur. [152] Occiso Theodore Thurismo filius eius succedit in regno. [153] Huni cum rege suo Attila relictis Galliis post certamen Italiam petunt.",
    "isid": "Pace deinde Theuderidus cum Romanis inita denuo adversus Hunos Galliarum provincias saeva depopulatione vastantes atque urbes plurimas evertentes in campis Catalaunicis auxiliante Aetio duce Romano aperto Marte conflixit ibique proeliando victor occubuit. Gothi autem dimicante Thurismundo Theuderedi regis filio adeo fortiter congressi sunt, ut inter primum proelium et postremum trecenta ferme milia hominum prostrarentur.",
    "gall": "Aetius patricius cum Theoderico rege Gothorum contra Attilam regem Hugnorum Tricassis pugnat loco Mauriacos, ubi Theodericus a quo occisus incertum est et Laudaricus cognatus Attilae: cadavera vero innumera.",
    "haun": "sicque [raptim congregatis undique bellatoribus viris adversae multitudini] nostrae partis [non impar occurreret] pugnatumque est in quinto miliario de Trecas loco nuncupato Maurica in Campania. [in quo conflictu ... Chunos constat eo victos fuisse, quod ... ad propria reverterunt.] mortuusque est in eo proelio Theodor rex Gothorum, in cuius locum Thorismotus filius eius maior natu sufficitur. sicque astu Aetii actum, ut, dum Francos hortatur ad propria remeare, ne vacuam virorum robore sedem Attila occuparet Thorismotumque hortatur, ut sumpti honoris gloriam in sedibus regni remeans firmaret, ne a fratribus praeventus dignitate careret, solus cum suorum robore militum remanens cuncta praeda et hostium spoliis proprium ditat exercitum.",
    "g7c": "His diebus Romam sonus adiit, Aetium in maximo discrimine inter falangas hostium laborare. Quo auditu uxor eius anxia atque maesta, assidua basilicas sanctorum apostolorum adibat atque, ut virum suum de hac via reciperet sospitem, praecabatur. Quae cum die noctuque haec agerit, quadam nocte homo pauperculus, crapulatus a vino, in angulo basilicae beati Petri apostoli obdormivit. Clausis autem ex more usteis a custodibus, non est nanctus. De nocte vero consurgens, relucentibus per tota aedis spatia lychinis, pavore territus, aditum, per quem foris evaderit, quaerit. Verum ubi primi atque alterius ustei claustra pulsat et obserata cuncta cognoscit, solo decubuit, trepidus praestolans locum, ut, convenientibus ad matutinis hymnis populis, hic liber abscederit. Interea vidit duas personas se invicem venerabiliter salutantes sollicitusque de suis esse prosperitatibus. Tunc qui erat senior ita exorsus est: 'Uxoris Aeti lacrimas diucius sustenire non patior. Petit enim assiduae, ut virum suum de Galliis reducam incolomem, cum aliud exinde fuisset apud divinum iuditium praefinitum, sed tamen obtenui inmensam pietatem pro vita illius. Et ecce nunc illum propero viventem exinde reducturus! Verumtamen obtestor, ut qui haec audierit sileat arcanumque Dei vulgare non audeat, ne pereat velociter a terra'. Ille autem haec audiens, silire non potuit; sed mox inluciscente caelo omnia quae audierat matri familiae pandit, expletisque sermonibus, lumen caruit oculorum.",
    "g7d": "Igitur Aetius cum Gothis Francisque coniunctus adversus Attilanem confligit. At ille ad internitionem vastari suum cernens exercitum, fuga delabitur. Theodor vero Gothorum rex huic certamine subcubuit. Nam nullus ambigat, Chunorum exercitum obtentu memorati antestites fuisse fugatum. Verum Aetius patritius cum Thorismodo victuriam obtinuit hostesque delivit. Expletoque bello, ait Aetius Thorismodo: 'Festina velociter redire in patriam, ne insistente germano a patris regno priveris'. Haec ille audiens, cum velocitate discessit, quasi antecipaturus fratrem et prior patris cathedram adepturus. Simili et Francorum regem dolo fugavit. Illis autem recedentibus, Aetius, spoliato campo, victor in patriam cum grande est reversus spolia. Attila vero cum paucis reversus est.",
}

# (orig: tuple of Getica sections or LAT key, page label, title, English, note)
SECTIONS = [
    ("field", "Field", "The field and the omens",
     "Jordanes names the field and then stops to ask what could justify such a slaughter. Sangiban's suspected treason, which he tells next (Get. 194–195), is in module 2. Then Attila consults his soothsayers.",
     [
         ((192,), "Get. 192 · Mommsen p. 108", "The Catalaunian fields, 'also called Mauriacan'",
          "So they came together on the Catalaunian fields, which are also called Mauriacan, a hundred leagues long, as the Gauls call them, and seventy wide. A Gallic league measures fifteen hundred paces. That stretch of earth became the arena of countless peoples. The two strongest battle lines engage; nothing is done by stealth, the fight is in open battle.",
          "A hundred by seventy leagues is some 220 by 155 kilometres: a region, roughly Champagne, not a battlefield. Jordanes alone joins the two names that the other sources keep apart: the Catalaunian fields (Hydatius, Cassiodorus, Isidore) and Mauriacus (the Gallic chronicles and Gregory). See the comparison 'Where was the field?'."),
         ((193,), "Get. 193 · Mommsen p. 108", "'Mankind lives for kings'",
          "What cause could be found worthy of the movement of so many? Or what hatred drove them all to take up arms against each other? It is proved that mankind lives for kings, when at the mad impulse of one mind a slaughter of nations is made, and at the will of a proud king what nature brought forth over so many ages perishes in a moment.",
          ""),
         ((196,), "Get. 196 · Mommsen pp. 108–109", "The soothsayers",
          "In their usual way they looked now at the entrails of cattle, now at certain veins in scraped bones, and announced ill fortune for the Huns; yet this little comfort they foretold, that the highest commander of the enemy on the other side would fall, and by his death would stain the victory that remained and the triumph. And since Attila held the death of Aetius, who stood in the way of his plans, worth seeking even at the cost of his own ruin, he was troubled by such an omen; and being a deviser of plans in matters of war, he joined battle in fear about the ninth hour of the day, so that if things went otherwise, the coming night would help him.",
          "The ninth hour is mid-afternoon. The 'highest commander' who falls will be Theoderic, not Aetius (Get. 209): Jordanes, writing from the Gothic side, makes the Gothic king's death the price of the victory."),
     ]),
    ("lines", "Lines", "The battle lines",
     "Who stood where. Jordanes is the only source for the order of battle, and his geometry of a hill with two slopes and two wings is not easy to draw.",
     [
         ((197,), "Get. 197 · Mommsen p. 109", "The hill",
          "The parties met, as we have said, on the Catalaunian fields. The ground there rose in a slope to the height of a hill. Both armies wanted to hold it, since the advantage of a place confers no small benefit: the Huns with their men took the right side of it, the Romans and Visigoths with their auxiliaries the left, and leaving the ridge at its summit between them they joined battle. Theoderic with the Visigoths held the right wing, Aetius with the Romans the left; in the middle they placed Sangiban, who, as we said above, commanded the Alans, with military caution, so that a crowd of loyal men should enclose the man of whose mind they were less sure. For he readily takes on the necessity of fighting on whom the difficulty of fleeing is imposed.",
          "The sense of 'leaving the ridge at its summit' (relictoque de cacumine eius iugo) is uncertain. On Sangiban see module 2."),
         ((198,), "Get. 198 · Mommsen p. 109", "Attila in the centre",
          "On the other side the battle line of the Huns was so ordered that Attila was placed in the middle with his bravest men, the king in this arrangement providing rather for himself, so that, set amid the strength of his own people, he would be kept out of the danger that threatened. His wings were surrounded by the many peoples and various nations he had brought under his rule.",
          "Mommsen prints rubor with the best manuscripts; 'strength' translates robur, the reading of others, which the sense requires."),
         ((199, 200), "Get. 199–200 · Mommsen pp. 109–110", "Goths against Goths",
          "Among them the army of the Ostrogoths stood out, led by the brothers Valamir, Theodemir and Videmir, nobler even than the king whom they then served, for the power of the Amal family made them illustrious; and with the countless host of the Gepids was that most famous king Ardaric, who for his great loyalty to Attila took part in his counsels. For Attila, weighing them with his shrewdness, loved him and Valamir, king of the Ostrogoths, above the other petty kings. Valamir was close in keeping a secret, smooth in speech, skilled in wiles; Ardaric, as we have said, famous for loyalty and counsel. Attila had good reason to trust them to fight against the Visigoths, their kin. The rest of the crowd of kings, if one may say so, and the leaders of various nations waited on Attila's nods like guardsmen, and where he gave a sign with his eye, each stood by without a murmur, in fear and trembling, or carried out at once what he had been ordered.",
          "Theodemir was the father of Theoderic the Great, whose Amal house Cassiodorus and Jordanes served; their ancestors fought for Attila here, against the Visigoths. Ardaric's Gepids broke the Hunnic empire after Attila's death (module 5)."),
         ((201,), "Get. 201 · Mommsen p. 110", "The fight for the height",
          "Attila alone, king of all the kings, was over all and anxious for all. So the battle began over the advantage of the place we have described. Attila directs his men to seize the summit of the hill, but he is forestalled by Thorismud and Aetius, who struggled up to climb the heights of the hill, got above, and with the help of the height easily threw the Huns into confusion as they came.",
          ""),
     ]),
    ("speech", "Speech", "Attila's speech",
     "A set speech in the manner of ancient historians, written by Jordanes or by Cassiodorus before him. It is the only place where Attila speaks at length, and it is a Roman author's Attila.",
     [
         ((202, 203, 204), "Get. 202–204 · Mommsen p. 110", "'A sign of fear'",
          "Then Attila, seeing his army thrown into confusion by what had happened, thought it should be steadied with an address on the spot: 'After victories over so many nations, after the world subdued, if you stand firm, I had judged it foolish to whet you with words as though you did not know the business. Let a new leader seek that, or an untried army. It is not right for me to say anything commonplace, nor for you to hear it. For what else are you used to but war? Or what is sweeter for a brave man than to seek revenge with his own hand? It is a great gift of nature to sate the soul with vengeance. Let us then attack the enemy eagerly: those who bring war are always the bolder. Despise these gathered nations that do not agree: it is a sign of fear to defend oneself by alliance. See, before our onset they are already carried off by terror: they seek the heights, they take the mounds, and with late repentance they cry out for fortifications in the plain. You know how light the arms of the Romans are: they are weighed down, I do not say by the first wound, but by the very dust, while they close up in order and link their lines and their shield-roofs.'",
          "'It is a sign of fear to defend oneself by alliance': the speech turns the coalition of module 2 into its weakness."),
         ((205, 206), "Get. 205–206 · Mommsen pp. 110–111", "'This is the field'",
          "'Fight on with steadfast minds, as you are used to, and, despising their line, attack the Alans, fall on the Visigoths. We should seek quick victory where the war holds together. Once the sinews are cut, the limbs soon fall away, and a body cannot stand when you have taken out its bones. Let your spirits rise, let your usual fury swell. Now, Huns, bring out your counsel, now your arms: let the wounded man demand the death of his opponent, and the unhurt take his fill of the enemy's slaughter. No weapons reach those who are to live; those who are to die, fate hurls down even at rest. Lastly, why would fortune have made the Huns victors over so many nations, unless she had prepared them for the joys of this battle? Who opened to our ancestors the way across the Maeotic marsh, closed and secret for so many ages? Who made armed men give way to men still unarmed? A gathered multitude could not bear the face of the Huns. I am not deceived in the outcome: this is the field which so many successes have promised us. I shall be the first to hurl my weapons at the enemy. If anyone can stay at rest while Attila fights, he is a dead man.' Fired by these words, all rush into the fight.",
          "The way across the Maeotic marsh (the Sea of Azov) is the story of the hind that led Hunnic hunters across it, told by Jordanes in Get. 123–124."),
     ]),
    ("fight", "Fight", "The fight",
     "'Bellum atrox multiplex immane pertinax': the sentence that names the companion game. A brook running with blood, Theoderic's death told two ways, Attila in his wagon fort, Thorismud and Aetius lost in the dark.",
     [
         ((207,), "Get. 207 · Mommsen p. 111", "'Bellum atrox'",
          "And although the situation itself held terror, the king's presence took hesitation away from the downcast. They come together hand to hand; a war savage, manifold, monstrous, stubborn, the like of which no antiquity anywhere tells, where such deeds are reported that a man who was denied the sight of this wonder could have seen nothing remarkable in all his life.",
          ""),
         ((208,), "Get. 208 · Mommsen p. 111", "The brook",
          "For if one may believe the elders, a brook of that field, flowing past between low banks, swelled with the much blood from the wounds of the slain; not increased by rains, as it used to be, but stirred by an unaccustomed liquid, it became a torrent through the increase of gore. And those whom the wounds they had received drove there in parching thirst drew in streams mixed with slaughter: so, constrained by a wretched lot, they drank, wounded men, the blood they had shed.",
          "'If one may believe the elders': Jordanes, a century later, cites oral tradition. The Latin putantes ('thinking') is hard to construe; 'drinking' (potantes) is the likely sense."),
         ((209,), "Get. 209 · Mommsen p. 111", "Theoderic's death",
          "Here King Theoderic, while he rode about encouraging his army, was thrown from his horse and trampled under the feet of his own men, and so ended a life of ripe old age. Others say that he was killed by a spear of Andagis, from the side of the Ostrogoths, who then followed Attila's rule. This was what the soothsayers had foretold to Attila, although he had thought of Aetius.",
          "Two versions side by side. Andagis was the father of Gunthigis Baza, the general whom Jordanes served as secretary (Get. 266): the man who may have killed the Visigothic king was the father of the author's own patron. The Gallic chronicle of 511 says that who killed him 'is uncertain'."),
         ((210,), "Get. 210 · Mommsen pp. 111–112", "The wagon fort",
          "Then the Visigoths, separating from the Alans, fall upon the band of the Huns and would nearly have killed Attila, had he not prudently fled first and shut himself and his men at once within the enclosure of the camp, which he had fortified with wagons; a frail defence, yet there men sought protection for their lives whom a little before no earthen wall could withstand.",
          ""),
         ((211,), "Get. 211 · Mommsen p. 112", "Thorismud in the dark",
          "Thorismud, son of King Theoderic, who with Aetius had seized the hill first and driven the enemy down from the higher ground, believing he was coming back to his own lines, ran unawares in the blind night into the enemy's wagons. As he fought bravely, someone wounded him in the head and threw him from his horse; rescued by the foresight of his men, he gave up his intention of fighting.",
          ""),
         ((212,), "Get. 212 · Mommsen p. 112", "The lion in its den",
          "Aetius likewise, separated in the confusion of the night, wandered in the midst of the enemy, anxious lest some misfortune had befallen the Goths, and searched for them; at last reaching the allied camp, he spent the rest of the night under the protection of shields. When day broke on the morrow and they saw the fields heaped with corpses and that the Huns did not dare to break out, they thought the victory theirs, knowing that Attila would not flee from battle unless struck by a great disaster. Yet he did nothing like a man laid low and cast down, but clashing his arms, he sounded the trumpets and threatened an attack: like a lion pressed by hunting spears, pacing the mouth of his den, who neither dares to spring out nor ceases to terrify the neighbourhood with his roaring, so the most warlike king, shut in, troubled his victors.",
          "Hydatius too says that night broke off the battle."),
     ]),
    ("fort", "Parting", "The siege of the camp and the parting",
     "The allies decide to starve Attila out, and then do not. Jordanes' explanation is Aetius' fear of the Goths; the casualty figure follows, and Thorismud's return to Toulouse.",
     [
         ((213,), "Get. 213 · Mommsen p. 112", "The pyre of saddles",
          "So the Goths and the Romans meet and deliberate what to do with the overcome Attila. They decide to wear him out by siege, since he had no supply of food, while his own archers, posted within the enclosure of the camp, kept off any approach with their frequent shots. It is said that the king, still high-minded in this extremity, built a pyre of horses' saddles and meant to throw himself into the flames if the enemy broke in, so that no one might rejoice at his wounding and the lord of so many nations might not come into the power of his enemies.",
          "'It is said': again a report, not a statement."),
         ((214, 215), "Get. 214–215 · Mommsen pp. 112–113", "The king found among the dead",
          "But during these delays of the siege the Visigoths look for their king, the sons for their father, wondering at his absence, since good fortune had followed. When after long search, as is the way of brave men, they found him among the thickest heaps of the dead, they honoured him with songs and carried him off under the eyes of the enemy. You might have seen bands of Goths, harsh with discordant voices, paying the dead his rites while the battle still raged. Tears were shed, but such as are given to brave men. For it was death, but glorious, with the Hun as witness, so that the enemy's pride might be thought humbled when they saw the body of so great a king carried out with its insignia. And the Goths, still paying the last rites to Theoderic, bear the royal majesty away with clashing arms, and the most valiant Thorismud, as befitted a son, followed his dearest father's glorious shade in the funeral. When this was done, moved by the grief of his loss and by the drive of the courage in which he was strong, he sought to avenge his father's death on the rest of the Huns, and consulted the patrician Aetius, as the elder and ripe in wisdom, on what he should do at this moment.",
          ""),
         ((216,), "Get. 216 · Mommsen p. 113", "Aetius' advice",
          "Aetius, fearing that if the Huns were utterly destroyed the Roman empire would be overwhelmed by the Goths, gives this counsel: that he should return to his own seat and take the kingdom his father had left, lest his brothers seize their father's treasure and invade the kingdom of the Visigoths, and he should then have to fight hard against his own and, what is worse, wretchedly. This answer was received, not as ambiguous, which is how it was given, but rather as given for his own advantage; and leaving the Huns, he returned to Gaul.",
          "One of three explanations of the parting: Jordanes gives Aetius a political motive, the Copenhagen continuation and Gregory a motive of booty, and Gregory adds that the Frankish king was sent away by the same trick (see the comparison 'Why did the allies part?')."),
         ((217,), "Get. 217 · Mommsen p. 113", "165,000 dead",
          "So human frailty, while it runs to meet suspicions, often lets slip a great occasion for action. In this most famous war of the bravest nations, one hundred and sixty-five thousand are reported slain on both sides, not counting fifteen thousand Gepids and Franks, who, meeting each other by night before the general engagement, fell by mutual wounds, the Franks fighting on the Roman side, the Gepids on the side of the Huns.",
          "Hydatius and, after him, Isidore give about 300,000; Prosper speaks only of 'inestimable slaughter', the Gallic chronicle of 'countless corpses'. No figure can be checked, and all are far beyond what the armies of the 450s could field."),
         ((218,), "Get. 218 · Mommsen pp. 113–114", "Thorismud at Toulouse",
          "So Attila, learning of the Goths' departure, thought it rather a trick of the enemy, as is usually concluded from the unexpected, and kept himself within the camp for a long time. But when long silences followed the enemy's absence, his mind rises to victory, joys are anticipated, and the mighty king's spirit returns to its old fortune. Thorismud, then, raised to royal majesty immediately on his father's death on the Catalaunian fields, where he had also fought, enters Toulouse. There, though the crowd of his brothers and strong men rejoiced, he so tempered his beginnings that he met no contest over the succession.",
          "Thorismud reigned only two years: Gregory and the Gallic sources say his brothers killed him in 453 (module 5)."),
     ]),
    ("chron", "Chronicles", "Chronicles in Italy and Spain",
     "The short notices. Prosper, in Rome, wrote within four years of the battle; Cassiodorus compiled his chronicle in 519 for a Gothic prince; Hydatius wrote at the far end of the West, in Galicia; Isidore of Seville copied Hydatius about 624. None of them agrees with Jordanes on everything.",
     [
         ("prosper", "Prosper 1364 · MGH AA IX pp. 481–482", "'Neither side gave way'",
          "In that conflict, although neither side gave way and inestimable slaughters of men dying together were made, it is agreed that the Huns were beaten in this: those who survived lost confidence in fighting and went back home.",
          "The end of Prosper's entry for 451, whose first two sentences are in modules 1 and 2. Prosper's chronicle was completed in 455: this is the nearest account in time. It names no place and no Theoderic, and defines victory by who went home."),
         ("cass", "Cassiodorus, Chronica 1253 · MGH AA XI p. 157", "'By the valour of the Goths'",
          "In this consulship the Romans, under the leadership of Aetius, with the Goths as auxiliaries, fought against Attila on the Catalaunian field. He, overcome by the valour of the Goths, withdrew.",
          "Cassiodorus wrote his chronicle in 519 for Eutharic, the son-in-law of Theoderic the Great, and gives the victory to the Goths. His lost Gothic History was Jordanes' main source."),
         ("reich", "Contin. cod. Reichenav. c. 19 · MGH AA IX p. 490", "'With slaughter on both sides'",
          "A battle was fought in Gaul between Aetius and Attila, king of the Huns, with slaughter of both peoples. Attila is put to flight into upper Gaul.",
          "A short continuation of Prosper in a Reichenau manuscript. 'Upper Gaul' is not explained."),
         ("hyd", "Hydatius c. 150. 152. 153 · MGH AA XI p. 26", "'Not far from Metz'",
          "[150] The people of the Huns, breaking the peace, plunders the provinces of Gaul. Very many cities were broken into. On the Catalaunian fields, not far from the city of Metz, which they had broken into, fighting in open battle against the general Aetius and King Theoderic, who were allied in peace, they are cut down and overcome with God's help. The dead of night broke off the battle. King Theoderic fell there, laid low. About 300,000 men are said to have fallen in that battle. [152] Theoderic being killed, his son Thurismo succeeds to the kingdom. [153] The Huns with their king Attila leave Gaul after the battle and head for Italy.",
          "Hydatius wrote in Galicia, in north-west Spain, in the 460s, and knew Gaul by report; Metz lies well over a hundred kilometres east of Châlons and Troyes. He files these entries under Valentinian's twenty-eighth year (452) and surrounds them with omens: an eclipse, a comet, a red sky in the north (c. 149, 151). Mommsen's brackets marking the manuscripts are left out here."),
         ("isid", "Isidore, Hist. Goth. 25 · MGH AA XI pp. 277–278", "'Between the first battle and the last'",
          "Then Theoderic, having made peace with the Romans, again fought in open battle on the Catalaunian fields, with Aetius the Roman general helping, against the Huns, who were laying waste the provinces of Gaul with savage devastation and overthrowing very many cities; and there, fighting, he fell as victor. And the Goths, with Thurismund, son of King Theoderic, fighting, engaged so bravely that between the first battle and the last nearly three hundred thousand men were laid low.",
          "The longer recension of Isidore's History of the Goths, about 624; Mommsen marks the borrowing from Hydatius. The shorter recension says instead that Attila, beaten, 'was never seen again, for fear of the pursuing army'. 'Between the first battle and the last' suggests more than one engagement."),
     ]),
    ("gaul", "Gaul", "Gaul remembers",
     "The sources written in Gaul place the battle near Troyes, at a place called Mauriacus, five miles out; they name a dead kinsman of Attila; and they tell of a trick by which Aetius kept the spoils. Gregory of Tours adds a vision in Rome.",
     [
         ("gall", "Chron. Gall. a. 511 c. 615 · MGH AA IX p. 663", "'By whom killed, uncertain'",
          "The patrician Aetius with Theoderic, king of the Goths, fights against Attila, king of the Huns, at Troyes, at the place Mauriacus, where Theoderic was killed, by whom is uncertain, and Laudaric, Attila's kinsman; and the corpses were countless.",
          "A Gallic chronicle running to 511. Laudaric appears nowhere else."),
         ("haun", "Add. ad Prosp. Haun. · MGH AA IX p. 302", "'At the fifth milestone from Troyes'",
          "And so [gathering fighting men in haste from every side, he met the opposing multitude] on our side [on equal terms], and the battle was fought at the fifth milestone from Troyes, at a place called Maurica, in Champagne. [In that conflict ... it is agreed that the Huns were beaten in this, that ... they went back home.] And Theodor, king of the Goths, died in that battle; in his place Thorismot, his elder son, was put. And so it was done by Aetius' cunning that, urging the Franks to return home lest Attila occupy their seat while it was empty of its strength of men, and urging Thorismot to return to the seat of his kingdom and make firm the glory of the honour he had received, lest he be forestalled by his brothers and lose the dignity, he alone, remaining with the strength of his own soldiers, enriched his own army with all the booty and the spoils of the enemy.",
          "The Copenhagen continuation of Prosper (module 2); words in square brackets are Prosper's, as Mommsen marks them. The fifth Roman milestone is about seven and a half kilometres. The most precise place-name in any source, and the plainest statement of the trick."),
         ("g7c", "Greg. Hist. II.7 · MGH SRM I pp. 69–70", "Aetius' wife and the drunkard in Saint Peter's",
          "In these days a rumour reached Rome that Aëtius was hard pressed and in grievous danger among the hordes of the enemy. At these tidings his wife in her sadness and anxiety frequented without ceasing the churches of the holy apostles, and prayed that she might receive back her lord safe from this campaign. She continued in prayer night and day, and one night a poor man who was drunken fell asleep in a corner of the church of the blessed apostle Peter. The doors were shut as usual, but he was not discovered by the guardians. During the night he got up, to find a brilliance of lamps flashing light through the whole building, and searched in terror for the entry, that he might find a way out. He tried the bolts, first of one door and then of another, but found them all fast; so he lay down on the ground anxiously watching the door, that he might escape as soon as the people assembled for the morning hymns. But now he perceived two persons who saluted each other with reverence, and asked each other how they did. The elder thus began: 'I may no longer endure the tears of the wife of Aëtius. She prayeth without ceasing that I may bring back her husband safe and sound from Gaul, when the divine judgement hath otherwise determined. Nevertheless I have obtained this immeasurable grace for his life. And behold I hasten thither now to bring him thence alive. But I adjure him who hath heard these things to hold his peace, nor dare to divulge the secret, or forthwith he shall perish from the earth.' Nevertheless the man could not be silent, but as soon as light appeared in the heaven, he revealed all that he had heard to the wife of Aëtius; and as soon as he had spoken, the light of his eyes failed.",
          "English: Dalton (1927), his II.6 (7). The two persons are Peter and Paul, the elder Peter. Fredegar repeats the story, as Dalton notes. Compare Aetius commending himself to Saint Peter in the Oviedo continuation (module 2)."),
         ("g7d", "Greg. Hist. II.7 · MGH SRM I pp. 70–71", "The battle and the trick",
          "Now Aëtius, in alliance with the Goths and Franks, fought with Attila, who seeing his army being worn down even to destruction, left the field in flight. Theodoric, king of the Goths, succumbed in this battle. No man may doubt that the army of the Huns was routed by the intercession of the bishop whom I have named. But the patrician Aëtius won the victory with Thorismund, and utterly destroyed the enemy. And when the war was ended, Aëtius said to Thorismund: 'Make haste to return with all speed to thy country, lest by the action of thy brother thou be despoiled of thy father's kingdom.' At these words Thorismund departed in haste to forestall his brother and take first possession of his father's throne. With like craft he sent off the king of the Franks. And as soon as they were gone he collected the spoil from the field and returned home with great booty. But Attila retired with a small number of men.",
          "English: Dalton (1927). Arndt's text has 'Theodor', as in the Copenhagen continuation. For Gregory the victory belongs to Anianus' prayers (module 3) as much as to Aetius; the Frankish king is not named. The rest of the chapter, on Aquileia and Thorismund's death, belongs to module 5."),
     ]),
]


def build():
    secs = []
    for sid, zk, titel, blurb, units in SECTIONS:
        out = []
        for i, (src, pg, t, en, note) in enumerate(units, 1):
            orig = jl(*src) if isinstance(src, tuple) else LAT[src]
            u = {"n": i, "pg": pg, "titel": t, "orig": orig, "en": en}
            if note:
                u["note"] = note
            out.append(u)
        secs.append({"id": sid, "zk": zk, "titel": titel, "blurb": blurb, "units": out})
    data = {
        "titel": "The battle and the withdrawal, 451",
        "autor": "Jordanes, Getica (about 551); the chronicles of Prosper, Hydatius, Cassiodorus and Isidore, the Gallic chronicle of 511 and two continuations of Prosper; Gregory of Tours",
        "jahr": "451",
        "orig_sprache": "la",
        "pg_label": "",
        "quelle": "Jordanes, Getica, ed. Th. Mommsen, MGH Auct. ant. V.1 (Berlin 1882), pp. 108–114 (archive.org cuaiordanisroman00jord); Prosper, Epitoma chronicon, the Additamenta ad Prosperum Hauniensia, the Continuatio codicis Reichenaviensis and the Chronica Gallica a. 511, ed. Th. Mommsen, MGH Auct. ant. IX (Berlin 1892), pp. 302, 481–482, 490, 663 (archive.org chronicaminorasa09momm); Hydatius, Cassiodorus' Chronica and Isidore's Historia Gothorum, ed. Th. Mommsen, MGH Auct. ant. XI (Berlin 1894), pp. 26, 157, 277–278 (archive.org chronicaminorasa11momm); Gregory of Tours, Historiae II.7, ed. W. Arndt, MGH SRM I.1 (Hanover 1884), pp. 69–71, English by O. M. Dalton (Oxford 1927), vol. II pp. 47–48. All public domain.",
        "hinweis": "The Latin follows the printed editions, checked against the page images; Jordanes' text, from the Latin Library, was compared word by word with Mommsen's and keeps his readings. In the Copenhagen continuation, words in square brackets are Prosper's, as Mommsen marks them. Gregory is in Dalton's English (public domain); Jordanes and the chronicles are in the site's working translation, close to the Latin and dedicated to the public domain. Mierow's English Jordanes is not used (see 'Not carried').",
        "sections": secs,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in secs)} units in {len(secs)} sections")


if __name__ == "__main__":
    build()
