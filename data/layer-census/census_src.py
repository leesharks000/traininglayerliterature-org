"""The training-layer census of traininglayerliterature.org, first batch (2026-11-01). Writes census.json.

Operator, 2026-11-01: "tll is a separate question... it probably needs a meta-aggregator too, and that is a useful way to distinguish and
individuate the purposes"; "yes, lets build both". Training-layer literature is writing addressed to the machine reader and carried into
training. Organizing question: is the work in the layer, under whose name, and can it be found there and read back? Anchors: Who Is Writing
for the Machines? Training-Layer Literature: A Field Survey (#186, AXN:032C), and Generative Uptake: Training-Layer Literature Extended from
Machine Reading to Machine Composition (#1543, AXN:0642).

Each row is written in rows/<slug>.py from the saved sources only (sources/, dated and hashed in sources/manifest.json). Every quoted value is
checked verbatim (whitespace-normalised) against the saved text of its source. A resource's own terms are kept as its own; where it meets the
census's question is stated separately, in tll_reading, as the archive's reading.
"""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
MAN = json.load(open(HERE / "sources/manifest.json"))

AREAS = {'corpora': 'The corpora: collections, crawls and datasets whose texts enter machine training', 'finding': 'Finding a work in the layer: tools and methods that test whether a work is in a training set or in a model', 'machine-reader': 'Writing for the machine reader: electronic literature, data poetics, generative and computational writing', 'meta-aggregation': 'Meta-aggregation: a resource that itself gathers and reads other resources'}
EVIDENCE_KINDS = ['web crawl', 'digital library', 'dataset', 'dataset documentation', 'search tool', 'opt-out registry', 'detection method', 'research paper', 'anthology', 'knowledge base', 'journal', 'event archive', 'census of resources']


def Q(src, quote, basis="operator"):
    return {"src": src, "basis": basis, "quote": quote}


ROWS = []
def row(**r): ROWS.append(r)


ORDER = ['common-crawl', 'project-gutenberg', 'internet-archive', 'hathitrust', 'htrc', 'the-pile', 'dolma', 'spawning-hibt', 'books3-search', 'min-k-prob', 'speak-memory', 'elc', 'elmcip', 'cell', 'ebr', 'taper', 'nanogenmo']
for slug in ORDER:
    p = HERE / "rows" / f"{slug}.py"
    if p.exists():
        exec(compile(p.read_text(encoding="utf-8"), str(p), "exec"), {"row": row, "Q": Q})

def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
problems = []
REQ = ["slug", "name", "url", "operator", "areas", "evidence_kind", "kind", "unit", "record_object", "record", "method",
       "holdings", "stated_limits", "answers", "does_not_answer", "tll_reading", "lifecycle", "version_and_time", "negative_tags", "evidence"]
for r in ROWS:
    miss = [k for k in REQ if k not in r]
    if miss: problems.append((r.get("slug"), "missing fields", miss))
    for i in r.get("areas") or []:
        if i not in AREAS: problems.append((r["slug"], "unknown area", i))
    for k in r.get("evidence_kind") or []:
        if k not in EVIDENCE_KINDS: problems.append((r["slug"], "unknown evidence kind", k))
    rec = r.get("record") or {}
    for k in ('in_layer', 'name', 'readback'):
        if k not in rec: problems.append((r.get("slug"), "record missing", k))
    srcs = {}
    for f, ev in (r.get("evidence") or {}).items():
        sid = ev["src"]
        if sid not in MAN:
            problems.append((r["slug"], f, "source not saved", sid)); continue
        srcs[sid] = {"url": MAN[sid]["url"], "read": MAN[sid]["fetched"][:10], "sha256": MAN[sid]["sha256"], "http": MAN[sid]["http"]}
        if ev.get("quote"):
            txt = norm((HERE / "sources" / f"{sid}.txt").read_text(encoding="utf-8"))
            if norm(ev["quote"]) not in txt:
                problems.append((r["slug"], f, sid, ev["quote"][:80]))
    r["sources"] = srcs
    r.setdefault("observed", {"on": "2026-11-01", "fetch": "read"})
unread = {k: {"url": v["url"], "http": v["http"], "fetched": v["fetched"]} for k, v in MAN.items() if v["http"] != "200" or v["text_chars"] < 100}
out = {"name": 'Training-Layer Literature meta-aggregator census: the layer', "compiled": "2026-11-01", "schema_version": "1.0", "editor": "Lee Sharks",
       "family": "Meta-Aggregators of the Crimson Hexagon",
       "schema_note": "The MMRS, provenance, Labor Vector and left-census core (slug, name, aka, url, operator, kind, unit, count, lifecycle, version_and_time, negative_tags, evidence, relations, unchecked, sources) extended for the training layer: areas (one or more of four), evidence_kind, record_object (what it records), record (in_layer: whose works it holds or carries into training, or how it bears on that; name: whether a work keeps its author's name and attribution there, as the resource itself shows, or 'not recorded'; readback: whether and how a work can be found there and read back: search, membership test, provenance, or 'not recorded'), method, coverage, holdings, stated_limits, answers and does_not_answer, and tll_reading (where it meets the question of #186 and #1543: the archive's reading, kept apart from the resource's own terms). Every quote is verbatim from a saved source.",
       "organizing_question": 'Is the work in the layer, under whose name, and can it be found there and read back?',
       "anchor": {'deposits': [{'deposit': 186, 'axn': 'AXN:032C', 'title': 'Who Is Writing for the Machines? Training-Layer Literature: A Field Survey', 'url': 'https://www.alexanarch.org/s/records/186/'}, {'deposit': 1543, 'axn': 'AXN:0642', 'title': 'Generative Uptake: Training-Layer Literature Extended from Machine Reading to Machine Composition (EA-TLL-COMPOSITION-01)', 'url': 'https://www.alexanarch.org/s/records/1543/'}]},
       "areas": AREAS, "evidence_kinds": EVIDENCE_KINDS, "unread_sources": unread, "pending": [], "rows": ROWS}
json.dump(out, open(HERE / "census.json", "w"), ensure_ascii=False, indent=1)
print(len(ROWS), "rows;", sum(len(r.get("evidence") or {}) for r in ROWS), "evidence items;", len(problems), "problems")
for p in problems: print("  ", p)
