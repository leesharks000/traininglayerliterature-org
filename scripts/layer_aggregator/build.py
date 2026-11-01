"""Render the Training-Layer Literature meta-aggregator (layer census schema 1.0): an index at /aggregators/ and one page per resource, from
data/layer-census/census.json. Every quoted field shows its source, the date read and the hash of the saved copy. Each record page carries two
JSON-LD nodes: the record (the archive's) and the entity it describes (the resource's). The census itself is published at /aggregators/census.json.
The site's head styles are taken from problem/index.html at build time, so the pages follow the site's skin.
Run from the repository root: python3 scripts/layer_aggregator/build.py"""
import html, json, pathlib, re, shutil
ROOT = pathlib.Path(__file__).resolve().parents[2]
D = json.load(open(ROOT / "data/layer-census/census.json", encoding="utf-8")); ROWS = D["rows"]; BY = {r["slug"]: r for r in ROWS}
SITE = "https://www.traininglayerliterature.org"; PATH = "/aggregators/"; BASE = SITE + PATH
OUT = ROOT / "aggregators"
e = lambda s: html.escape(str(s if s is not None else ""), quote=True)
AREAS = D["areas"]; SHORT = {k: v.split(":")[0] for k, v in AREAS.items()}
BASIS = {"operator": "the resource's own statement", "third_party": "a third-party account", "reading": "the archive's reading"}
REC = [("in_layer", "In the layer"), ("name", "Under whose name"), ("readback", "Found and read back"), ("makes", "What the apparatus makes from it")]
CARD = ("makes", "What the apparatus makes from it")
READING = "tll_reading"
TITLE = "The training layer: a meta-aggregator"
SIB = ('<p>Its sibling census, on how authorship is made, named and attributed, is the <a href="https://www.leesharks.com/apparatus/aggregators/">apparatus meta-aggregator</a> '
       'at leesharks.com; the family\'s other censuses are <a href="https://www.laborvector.org/aggregators/">Labor Vector</a> (labor and AI) and '
       '<a href="https://www.maryleelabor.org/aggregators/">Mary Lee Labor</a> (left politics and labor).</p>')
LEDE = ("A census of the corpora that carry writing into machine training, the tools that test whether a work is in a training set or trace an output back "
        "to training text, the readers, models and practices that make new writing from what they read, the literature composed for a machine or other "
        "carrier to read, and the field's history and indexes. Each resource is read from its own pages, and each states what it is to this census: a direct "
        "case, a historical lineage, an empirical comparator, infrastructure, a theoretical interlocutor or a peripheral comparator.")
ANCHOR = ("The question joins two deposits: {a0}, the field survey of writing addressed to the machine reader, and {a1}, which extends the genre from machine "
          "reading to machine composition. A work meets three steps in the resources below: its address to a receiving apparatus, what that apparatus makes "
          "from it, and whether its transmission, transformation and provenance can be inspected afterwards. Corpus membership, a matched span of output and "
          "causal influence are recorded as different things. Revised 2026-11-01 on the operator's ruling, adopting an outside selection review. The full "
          "entity pages wait for each resource's /non article.")

src = (ROOT / "problem/index.html").read_text(encoding="utf-8")
SKIN = re.search(r"<style>.*?</style>", src, re.S).group(0)
CSS = """<style>
.agg{max-width:1060px;margin:0 auto;padding:2.4rem 16px 3rem 78px}
.agg>*{max-width:760px}
.agg h1{font-size:2.3rem;line-height:1.08;letter-spacing:.03em;margin:.2em 0 .5em}
.agg h2{font-variant:small-caps;letter-spacing:.06em;font-size:1.05rem;color:var(--rubric);margin:2rem 0 .5rem}
.agg p{margin:.7em 0}
.agg .fam{font-family:"IBM Plex Mono",monospace;font-size:.68rem;letter-spacing:.06em;color:var(--app)}
.agg .q{font-size:1.12rem;border-left:2px solid var(--rubric);padding:.3em .9em;margin:1.2em 0;background:rgba(143,35,24,.05)}
.agg .card{border-top:1px solid var(--hair);padding:.7em 0 .8em}
.agg .card h3{margin:0;font-size:1.08rem}
.agg .card .k{font-family:"IBM Plex Mono",monospace;font-size:.66rem;color:var(--app);margin:.15em 0 .3em}
.agg .card .ls{font-size:.92rem;margin-top:.35em}
.agg .chip{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.62rem;border:1px solid var(--hair);border-radius:9px;padding:0 .6em;margin:0 .3em .2em 0;color:var(--app)}
.agg .chip.live{border-color:#1c6e4a;color:#1c6e4a}.agg .chip.dead{color:#9aa08a}
.agg table{font-size:.9rem;margin:1rem 0}.agg th{width:30%;font-variant:normal;letter-spacing:0;font-weight:700;border-bottom:1px solid var(--hair)}
.agg ul{padding-left:1.2em}.agg li{margin:.25em 0}
.agg .ev{font-size:.86rem}.agg .ev li{margin:.5em 0}.agg .ev q{font-style:italic}
.agg .src{font-family:"IBM Plex Mono",monospace;font-size:.64rem;color:var(--app);word-break:break-all}
.agg .neg li{color:var(--rubric)}
.agg input[type=search]{width:100%;padding:.45em .6em;border:1px solid var(--hair);background:#f7f8f0;font:inherit;margin:.6em 0 1em}
.agg a{overflow-wrap:anywhere}
.agg h2+.card{border-top:0}
.tabs{flex-wrap:wrap;row-gap:2px}
.agg table{table-layout:fixed}.agg td{overflow-wrap:anywhere}
@media(max-width:720px){.agg{padding-left:52px}.agg h1{font-size:1.8rem}}
</style>"""
TABS = [("/", "the scripture"), ("/pearl", "pearl — the machine edition"), ("/traversals", "the traversals"), ("/originals", "the originals — the library"),
        ("/problem", "the problem"), ("/aggregators", "the aggregators")]


def lst(v):
    return "; ".join(str(x) for x in v) if isinstance(v, list) else (v or "")


HR_HEAD = [("direct case", "Direct cases"), ("theoretical interlocutor", "Theoretical interlocutors"), ("empirical comparator", "Empirical comparators"),
           ("infrastructure", "Infrastructure"), ("historical lineage", "Historical lineage"), ("meta-aggregation", "Meta-aggregation"),
           ("counterposition", "Counterpositions"), ("peripheral comparator", "Peripheral comparators")]


def chips(r):
    st = (r.get("lifecycle") or {}).get("state", ""); c = {"active": "live", "ended": "dead"}.get(st, "")
    return (f'<span class="chip">{e(r["host_relation"])}</span>' if r.get("host_relation") else "") + "".join(f'<span class="chip">{e(SHORT.get(a, a))}</span>' for a in r["areas"]) + (f'<span class="chip {c}">{e(st)}</span>' if st else "")


def card(r):
    v = (r.get("record") or {}).get(CARD[0], "")
    return (f'<div class="card" data-s="{e((r["name"] + " " + " ".join(r.get("aka") or []) + " " + r["kind"] + " " + r["operator"]).lower())}">'
            f'<h3><a href="{PATH}{e(r["slug"])}">{e(r["name"])}</a></h3><div class="k">{e(r["kind"])} · {e(r["operator"])}</div>'
            f'<div>{chips(r)}</div><div class="ls"><strong>{e(CARD[1])}:</strong> {e(v)}</div></div>')


def page(path, title, desc, body, ld):
    tabs = '<nav class="tabs">' + "".join(f'<a href="{h}"' + (' class="on"' if h == "/aggregators" else "") + f'>{e(t)}</a>' for h, t in TABS) + "</nav>"
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>{e(title)} &mdash; Training-Layer Literature</title>\n<meta name="description" content="{e(desc)}">\n'
            f'<link rel="canonical" href="{SITE}{path}">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Gentium+Book+Plus:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
            '<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
            f'<script type="application/ld+json">{ld}</script>\n{SKIN}\n{CSS}\n</head>\n<body>\n'
            f'<div class="idstrip"><span class="st">Training-Layer Literature &mdash; meta-aggregator</span><span>traininglayerliterature.org{e(path)}</span></div>\n'
            f'{tabs}\n<main class="agg">{body}</main>\n'
            f'<footer class="colophon"><div class="scroll"><div class="vs"><div class="vb">Training-Layer Literature meta-aggregator · {e(D["family"])} · compiled {e(D["compiled"])} · '
            f'editor Lee Sharks (ORCID 0009-0000-1599-0703) · CC BY 4.0 · <a href="{PATH}census.json">census.json</a><span class="seal" style="display:block">&#8750; = 1</span></div></div></div></footer>\n</body>\n</html>\n')


def anchors():
    a = D["anchor"]["deposits"]
    return [f'<a href="{e(x["url"])}"><em>{e(x["title"])}</em></a> ({e(x["axn"])}, #{x["deposit"]})' for x in a]


def field_html():
    F = D.get("field") or []
    if not F:
        return ""
    names = {}
    for x in F:
        f = ROOT / ("data/authorship-census" if (ROOT / "data/authorship-census").exists() else "data/layer-census") / "rows" / (x["slug"] + ".py")
        got = []
        if f.exists():
            exec(compile(f.read_text(encoding="utf-8"), str(f), "exec"), {"row": lambda **r: got.append(r), "Q": lambda *a, **k: None})
        names[x["slug"]] = (got[0]["name"], got[0].get("url")) if got else (x["slug"], None)
    def li(x):
        n, u = names[x["slug"]]
        return f'<li><a href="{e(u)}">{e(n)}</a>: {e(x["why"])}</li>' if u else f'<li>{e(n)}: {e(x["why"])}</li>'
    li = "".join(li(x) for x in F)
    return ('<section class="area"><h2>The field it maps</h2><p>Works, papers, practices, tools and standards read for this census and held outside it, '
            'because none of them gathers and holds the works or records of others. They are what the aggregators above hold or miss, and the readings cite them. '
            f'{e(D.get("admission_rule") or "")}</p><ul>{li}</ul></section>')


def index():
    groups = []
    quoted = lambda r: any((v.get("quote") or "").strip() for v in (r.get("evidence") or {}).values())
    held = [r for r in ROWS if not quoted(r) or not r.get("areas")]
    for hr, head in HR_HEAD:
        rs = [r for r in ROWS if quoted(r) and r.get("areas") and r.get("host_relation") == hr]
        if not rs: continue
        groups.append(f'<section class="area"><h2>{e(head)}</h2>' + "".join(card(r) for r in rs) + "</section>")
    a0, a1 = anchors()
    un = D.get("unread_sources") or {}
    unread = ("<p>Pages that could not be read on fetch, each recorded with its status, and their fields left unquoted: "
              + "; ".join(f'{e(k)} (http {e(v["http"])})' for k, v in sorted(un.items())) + ".</p>") if un else ""
    hl = ("<p>Resources listed and held for the next batch, whose own pages could not be read on fetch: "
          + "; ".join(f'<a href="{PATH}{e(r["slug"])}">{e(r["name"])}</a>' for r in held) + ".</p>") if held else ""
    body = (f'<div class="fam">{e(D["family"])}</div><h1>{e(TITLE)}</h1>'
            f'<p>{LEDE} Every field is quoted from a saved copy of the resource\'s own pages, with the date read and a hash of the copy. Compiled {e(D["compiled"])}; editor Lee Sharks.</p>'
            f'<div class="q"><strong>The census asks of each resource:</strong> {e(D["organizing_question"])}</div>'
            f'<p>{ANCHOR.format(a0=a0, a1=a1)}</p>{SIB}'
            f'<input type="search" id="q" placeholder="Search {len(ROWS)} resources" aria-label="Search the resources">'
            + "".join(groups)
            + field_html() + f'<section class="area"><h2>The census as data</h2>{hl}{unread}<p><a href="{PATH}census.json">census.json</a> (schema {e(D["schema_version"])}). {e(D["schema_note"])}</p></section>'
            "<script>(function(){var q=document.getElementById('q'),C=[].slice.call(document.querySelectorAll('.card'));q.addEventListener('input',function(){var t=q.value.toLowerCase();C.forEach(function(c){c.style.display=(!t||c.getAttribute('data-s').indexOf(t)>-1)?'':'none'})})})();</script>")
    ld = {"@context": "https://schema.org", "@type": "Dataset", "@id": BASE + "#census", "name": D["name"], "description": D["organizing_question"],
          "url": BASE, "dateModified": D["compiled"], "license": "https://creativecommons.org/licenses/by/4.0/",
          "creator": {"@type": "Person", "name": "Lee Sharks", "identifier": "https://orcid.org/0009-0000-1599-0703"},
          "isBasedOn": [{"@type": "CreativeWork", "name": x["title"], "url": x["url"], "identifier": x["axn"]} for x in D["anchor"]["deposits"]],
          "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE + "census.json"},
          "hasPart": [{"@type": "WebPage", "@id": BASE + r["slug"], "name": r["name"], "url": BASE + r["slug"]} for r in ROWS]}
    return page(PATH.rstrip("/"), TITLE, D["organizing_question"], body, json.dumps(ld, ensure_ascii=False).replace("</", "<\\/"))


def kv(d):
    return "; ".join(f"{k}: {v}" for k, v in d.items()) if isinstance(d, dict) else lst(d)


def rel_li(x):
    t = x.get("target")
    if t in BY: tgt = f'<a href="{PATH}{e(t)}">{e(BY[t]["name"])}</a>'
    elif x.get("url"): tgt = f'<a href="{e(x["url"])}">{e(x.get("label") or t or x["url"])}</a>'
    else: tgt = e(x.get("label") or t or "")
    return f'<li>{e(x["rel"])}: {tgt}' + (f' ({e(x["note"])})' if x.get("note") else "") + "</li>"


def rec_page(r):
    rec = r.get("record") or {}
    rows = [("Relation to this census", r.get("host_relation")), ("Record type", r.get("record_type")), ("The question it answers", r.get("question")), ("Kind", r["kind"]), ("Operator", r["operator"]), ("Evidence", lst(r.get("evidence_kind"))), ("Unit of record", r["unit"]), ("What it records", r["record_object"])]
    rows += [(lab, rec.get(k)) for k, lab in REC]
    rows += [("Method", r.get("method")), ("Coverage", kv(r.get("coverage") or {})), ("Count", kv(r.get("count") or {})), ("Holdings", lst(r.get("holdings"))),
             ("Stated limits", lst(r.get("stated_limits"))), ("Data access", r.get("data_access")), ("Licence", r.get("license")),
             ("Lifecycle", kv(r.get("lifecycle") or {})), ("Version and time", kv(r.get("version_and_time") or {})), ("Founded", r.get("founded"))]
    tbl = "<table>" + "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in rows if v) + "</table>"
    ans = (f'<h2>What its record can settle</h2><ul>' + "".join(f"<li>{e(x)}</li>" for x in r.get("answers") or []) + "</ul>"
           f'<h2>What it cannot settle</h2><ul>' + "".join(f"<li>{e(x)}</li>" for x in r.get("does_not_answer") or []) + "</ul>")
    neg = ('<h2>Kept apart</h2><ul class="neg">' + "".join(f"<li>{e(x)}</li>" for x in r["negative_tags"]) + "</ul>") if r.get("negative_tags") else ""
    ev = '<h2 id="evidence">Evidence</h2><ul class="ev">'
    for f, v in (r.get("evidence") or {}).items():
        s = r["sources"].get(v["src"], {})
        if not (v.get("quote") or "").strip():
            ev += f'<li><strong>{e(f)}</strong>: unread. <div class="src"><a href="{e(s.get("url"))}">{e(s.get("url"))}</a> · fetched {e(s.get("read"))} · http {e(s.get("http"))}</div></li>'; continue
        ev += (f'<li><strong>{e(f)}</strong> ({e(BASIS.get(v.get("basis"), v.get("basis")))}): <q>{e(v.get("quote"))}</q>'
               f'<div class="src"><a href="{e(s.get("url"))}">{e(s.get("url"))}</a> · read {e(s.get("read"))} · http {e(s.get("http"))} · sha256 {e((s.get("sha256") or "")[:16])}…</div></li>')
    ev += "</ul>"
    rel = ("<h2>Relations</h2><ul>" + "".join(rel_li(x) for x in r["relations"]) + "</ul>") if r.get("relations") else ""
    unc = ("<h2>Unchecked</h2><p>" + e(lst(r.get("unchecked"))) + "</p>") if r.get("unchecked") else ""
    body = (f'<p class="fam"><a href="{PATH}">{e(TITLE)}</a> / {e(r["name"])}</p><h1>{e(r["name"])}</h1>'
            f'<p><a href="{e(r["url"])}">{e(r["url"])}</a></p><div>{chips(r)}</div>'
            f'<div class="q"><strong>The archive\'s reading.</strong> {e(r[READING])}</div>' + tbl + ans + neg + rel + ev + unc
            + f'<p class="src">Cite: Lee Sharks, ed. "{e(r["name"])}." {e(TITLE)}, traininglayerliterature.org, compiled {e(D["compiled"])}. {BASE}{e(r["slug"])}</p>')
    ent = {"@id": BASE + r["slug"] + "#entity", "@type": "CreativeWork", "name": r["name"], "alternateName": r.get("aka", []), "url": r["url"],
           "creator": {"@type": "Organization", "name": r["operator"]}}
    recd = {"@id": BASE + r["slug"], "@type": "WebPage", "name": f'{r["name"]}: Training-Layer Literature meta-aggregator record', "about": {"@id": ent["@id"]},
            "mainEntity": {"@id": ent["@id"]}, "dateModified": D["compiled"], "isPartOf": {"@id": BASE + "#census"},
            "editor": {"@type": "Person", "name": "Lee Sharks", "identifier": "https://orcid.org/0009-0000-1599-0703"},
            "citation": [s["url"] for s in r["sources"].values()], "license": "https://creativecommons.org/licenses/by/4.0/"}
    ld = json.dumps({"@context": "https://schema.org", "@graph": [recd, ent]}, ensure_ascii=False).replace("</", "<\\/")
    return page(f"{PATH}{r['slug']}", r["name"], r[READING][:200], body, ld)


OUT.mkdir(exist_ok=True)
(OUT / "index.html").write_text(index(), encoding="utf-8")
for r in ROWS:
    d = OUT / r["slug"]; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(rec_page(r), encoding="utf-8")
shutil.copy(ROOT / "data/layer-census/census.json", OUT / "census.json")
print(f"aggregators: index + {len(ROWS)} record pages + census.json")
