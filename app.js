/* The Catalaunian Fields, 451 — a documentary apparatus. Vanilla JS, hash routes. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { rome: "Rome and Gaul", goths: "The Visigoths", huns: "The Huns", church: "Bishops and saints", reception: "Reception" };
const LANGS = { la: "Latin", grc: "Greek", fr: "French", de: "German" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("catalaunian_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  const pl = plateOf("hunnenschlacht");
  const planned = D.mods.planned || [];
  view.innerHTML = `
  <div class="hero">
    <div>
      <span class="tag">440–454 · Attila · Aetius · Theoderic · the bishops of Gaul</span>
      <h1>A battle no one can place</h1>
      <p class="lede">In 451 Attila crossed the Rhine with the peoples of his empire. Metz burned, Orléans was saved at the last moment, and somewhere in the plains of Champagne, on the Catalaunian fields or at Mauriacus near Troyes, an army of Romans, Visigoths, Alans, Franks and Burgundians under the patrician Aetius met him. The Visigothic king fell; Attila withdrew into his wagon fort and then out of Gaul; and Aetius let him go.</p>
      <p class="readable">This apparatus follows the campaign through the documents that tell it, and through the documents that contradict each other about it: one long narrative written a century later from the Gothic side, a handful of chronicle notices, a bishop's history, saints' lives, and a poet's panegyric. Every text is public domain and carried in whole sections, with the Latin or Greek beside the English.</p>
      <p class="quote">"bellum atrox multiplex immane pertinax": a war savage, manifold, monstrous, stubborn.
      <br><span class="fine">Jordanes, Getica 207, written about 551</span></p>
    </div>
    <figure><img src="assets/plates/${pl.id}.jpg" alt="${esc(pl.titel)}">
      <figcaption>${esc(pl.caption)} <a href="#/plates">All plates →</a></figcaption></figure>
  </div>

  ${D.mods.shipped.length ? `<h2>What the apparatus carries</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
  ${planned.length ? `<h2>Planned modules</h2><div class="grid g2">${planned.map(plannedCard).join("")}</div>` : ""}

  <h2>The questions it asks</h2>
  <div class="grid g2">
    <div class="panel"><h3>Where was the field?</h3>
      <p>Jordanes says the Catalaunian fields, "which are also called Mauriacan", a hundred leagues long and seventy wide. The chronicler Hydatius puts the battle not far from Metz, the Gallic sources at Mauriacus near Troyes. Nineteenth-century scholars argued for Châlons, Méry-sur-Seine and Troyes. The apparatus keeps the question open.</p></div>
    <div class="panel"><h3>Why did Aetius let Attila go?</h3>
      <p>Jordanes: so that the Goths would not become too strong once the Huns were destroyed. Gregory of Tours: by a ruse, to keep the spoils. A continuation of Prosper's chronicle tells of a trick played on the Franks and on Thorismund. Three motives for one decision.</p></div>
    <div class="panel"><h3>Who tells it?</h3>
      <p>A Gothic historian in Constantinople a century later, working from Cassiodorus and Priscus; chroniclers in Rome, in Gaul and in Spanish Galicia; a bishop of Tours a century and a half later; the authors of saints' lives, some of which their modern editor judged invented; a poet praising the man who won the Goths for the alliance. The Huns speak only through the East Roman envoy Priscus.</p></div>
    <div class="panel"><h3>How did it become 'the saving of the West'?</h3>
      <p>Through Gibbon and Creasy, Kaulbach's Battle of the Huns and Liszt's music, the Hungarian chronicles that made Attila an ancestor, and the "Huns" of 1900 and of 1914–1918. The last module follows the afterlife as its own subject.</p></div>
    <div class="panel"><h3>Can the story be played?</h3>
      <p>The companion game <em>Bellum atrox</em> is in preparation: as Aetius you hold together a coalition of former enemies, and every card will link back to its passage here.</p></div>
  </div>`;
}
function plannedCard(m) {
  return `<div class="card planned"><div>${side(m.side)} <span class="fine">in preparation</span></div><h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texts</span><h1>The corpus</h1>
    <p class="lede">${(D.mods.planned || []).length ? `Stage 1 of the collection is in progress: ${["no", "one", "two", "three", "four", "five"][D.mods.shipped.length]} of five modules are carried, the others are planned.` : "Stage 1 of the collection is complete: all five modules are carried."} What is not carried, and why, is listed below.</p>
    ${D.mods.shipped.length ? `<h2>Carried</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>Planned</h2><div class="grid g2">${D.mods.planned.map(plannedCard).join("")}</div>` : ""}
    <h2 id="missing">Not carried</h2><div class="grid g2">${(D.mods.missing || []).map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">not carried</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Loading…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const lang = bilingual ? langPref : "en";
  const origLang = sec.sprache || t.orig_sprache;
  const origName = LANGS[origLang] || "Original";
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← All texts</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · cited as ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + English`], ["orig", origName], ["en", "English"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Source and editorial note</span>
      <p><b>Source.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Cite as ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg" title="${esc(t.pg_label || "")} page.line">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="origcol"><div class="orig" lang="${esc(origLang)}"${t.rtl ? ' dir="rtl"' : ""}>${esc(u.orig)}</div>${u.tr ? `<div class="translit">${esc(u.tr)}</div>` : ""}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("catalaunian_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Compare</span><h1>Two sides of one moment</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← All comparisons</a></p><p class="fine">Loading…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(sec.titel)}</b><br><span class="fine">${esc(t.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}${u.pg ? `<br>${esc(u.pg)}` : ""}</div>
        <div class="text">${esc(u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← All comparisons</a></p>
    <span class="tag">Compare</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Timeline</span><h1>439–1918</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Plates</span><h1>The emperor, the seal, and the legend</h1>
    <p class="lede">No picture of the battle was made by anyone who saw it. What survives from the time is a seal; what the later Middle Ages made of the scene is Fortune's wheel.</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Sources, method, limits</span><h1>How this apparatus is made</h1>
    <div class="readable">
    <p><b>Public domain only.</b> Every text is carried from a printing that is out of copyright in the United States and in Germany, and its source is named on its page. Modern editions and translations in copyright are not used; nor is Mierow's English Jordanes, whose translator died in 1961.</p>
    <p><b>Read against the page.</b> The Latin comes from the Monumenta Germaniae Historica (Mommsen's Jordanes of 1882 and his Chronica minora of 1892–94, Krusch's saints' lives, Arndt and Krusch's Gregory of Tours, Luetjohann's Sidonius), the Greek of Priscus from Müller and Dindorf; every passage is checked against the page image of the printing.</p>
    <p><b>Working translations.</b> Where no public-domain English exists, the site gives its own working translation, close to the original and dedicated to the public domain (CC0). Where a public-domain English exists (Bury and Hodgkin for Priscus, Hodgkin's extract of Jordanes, Dalton's Gregory of Tours and Sidonius' letters), it is named and used.</p>
    <p><b>Voices and distances.</b> Jordanes wrote about 551 in Constantinople, a Goth working from Cassiodorus' lost Gothic history and from Priscus; his account is the only long one. Prosper wrote in Rome within a few years, Hydatius in Galicia, the Gallic chroniclers in southern Gaul. Gregory of Tours wrote about 590. The saints' lives are later still, some much later; their editor's judgments are given beside them.</p>
    <p><b>Dates.</b> The text is followed; the timeline gives the dates of modern accounts for what the text does not date, and says so.</p>
    </div>
    <h2>Sources carried</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>
    <h2>Plates</h2><p class="fine readable">${esc(D.plates.credit)}</p>`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Could not load the apparatus: ${esc(e.message)}</p>`; });
