# The Catalaunian Fields, 451

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23218775.svg)](https://doi.org/10.5281/zenodo.23218775)

A documentary apparatus for Attila's invasion of Gaul in 451, the battle on the Catalaunian fields, and its afterlife from 452 to 1918: public-domain sources with the Latin beside the English, comparisons setting the sources side by side, a timeline linked into the texts, and plates.

Its subject is the disagreement of the sources: where the field was (the Catalaunian fields, "not far from Metz", or Mauriacus five miles from Troyes), how many fell, how King Theoderic died, why Aetius let Attila go, whether Orléans was saved before or after the Huns broke in, and how an undecided battle became "the saving of the West".

Live: https://the-catalaunian-fields.netlify.app/

**Stage 1 is closed (October 2026).** It carries five modules with 121 passages:

- **Attila's court and the road to Gaul, 440–450** — Priscus' embassy of 448–449 in Bury's English (1923); Jordanes, *Getica* 178–186 and 224 (Mommsen 1882); Prosper and the Gallic chronicle of 452 on the causes of the war.
- **The alliance, 451** — Jordanes, *Getica* 176–177, 187–195; Prosper and the Copenhagen and Oviedo continuations (MGH AA IX); Sidonius' panegyric on Avitus (Luetjohann 1887), transcribed by eye.
- **The cities and their bishops, 451** — Gregory of Tours, *Histories* II.5–7 (Arndt 1884; Dalton's English 1927); the Lives of Anianus, Lupus and Genovefa (Krusch 1896) beside Krusch's verdicts; Sidonius' letters VII.12 and VIII.15 (Dalton's English 1915).
- **The battle and the withdrawal, 451** — Jordanes, *Getica* 192–218, with a new English translation; Prosper, Cassiodorus, Hydatius, Isidore, the Gallic chronicle of 511, the Copenhagen and Reichenau continuations; the rest of Gregory II.7.
- **Afterwards and afterlife, 452–1918** — Italy and Pope Leo, Thorismud's death, Attila's death, the Nedao, the murder of Aetius (Jordanes, Prosper, Hydatius, Cassiodorus, Marcellinus, Sidonius, Gregory); Gibbon (octavo 1788), Creasy (1851), Wilhelm II's Bremerhaven speech of 1900 in its official text (Penzler 1904), Kipling (1919).

A **Compare** page sets the sources side by side on nine questions (where the field was, how many fell, how Theoderic died, why the allies parted, who won, Orléans, why Attila left Italy, how he died, when the West fell).

What is **not carried**, and why, is listed on the Texts page (`data/modules.json`, key `missing`): Mierow's English Jordanes (not yet public domain in Germany), the Greek of Priscus and the fragments Bury does not translate, and the press version of the "Hun speech", for which no scan of a newspaper of 1900 could be checked.

The companion game, *Bellum atrox* (prototype 0): https://bellum-atrox.netlify.app/

## Files

- `data/modules.json`: the modules carried, and what is not carried and why.
- `data/<module>.json`: the texts (`court`, `alliance`, `cities`, `battle`, `after`).
- `data/timeline.json`, `data/compare.json`, `data/plates.json`.
- `tools/build-*.py`: build the module files. The Latin and German texts are in the scripts, except Jordanes and Priscus, which are read from `tools/src/jordanes_ll.json`, `tools/src/jord5.json` (Mommsen's text as given by the Latin Library, compared word by word with Mommsen's printing) and `tools/src/bury_paras.json` (Bury's Priscus as given by LacusCurtius).
- `tools/make-plates.py`: fetches the plates from Wikimedia Commons after checking that each file page carries a public-domain or CC0 licence.

## Building the data

```
python tools/build-court.py
python tools/build-alliance.py
python tools/build-cities.py
python tools/build-battle.py
python tools/build-after.py
python tools/make-plates.py
```

## Running locally

Any static server, e.g. `python -m http.server 8950`.

## Citation

Fassbender, Pantaleon. *The Catalaunian Fields, 451: A Documentary Apparatus.* 2026. https://doi.org/10.5281/zenodo.23218775 (all versions; version 1.0.0: https://doi.org/10.5281/zenodo.23218776). Please also cite the printed source of any passage you quote. Metadata: `CITATION.cff`, `.zenodo.json`.

Code: MIT. Editions and working translations: CC0. Editorial matter: CC BY 4.0. See `LICENSES.md`.
