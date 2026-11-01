# Brief: write training-layer census rows from saved sources (traininglayerliterature.org meta-aggregator, 2026-11-01)

Repository /home/claude/fleet/traininglayerliterature-org. Do not run git. Do not fetch anything: every source has already been fetched once and saved verbatim. Write only your rows, as new files data/layer-census/rows/<slug>.py, one per entity you are given.

## Read first
1. data/layer-census/census_src.py: the driver. It defines row(), Q(), the areas and the evidence kinds, the required fields, and the verbatim check. Read its docstring: the organizing question comes from Who Is Writing for the Machines? Training-Layer Literature: A Field Survey (#186), text at /home/claude/alexanarch/data/texts/AXN-032C-text.md, and Generative Uptake (#1543), text at /home/claude/alexanarch/data/texts/AXN-0642-text.md; read #186 whole (it is the archive's own survey of this field) and #1543's statement of machine composition before writing.
2. The exemplar census this follows: /home/claude/fleet/laborvector/data/labor-census/ (census_src.py and rows/). Read three rows whole (turkopticon, data-workers-inquiry, fairwork-cloudwork) Also read the left census for its fields: /home/claude/fleet/maryleelabor-org/data/left-census/rows/marxists-internet-archive.py. for register: short field values, quotes carried in evidence, untested or unrecorded things said plainly, negative tags that keep the resource apart from what it is mistaken for.
3. Your entities' saved sources: data/layer-census/sources/<slug>--<id>.txt (the text) with sources/manifest.json (url, http, sha256). source-list.json says which ids belong to which entity. A source with http 403 or almost no text is unread; say so in unchecked, and never quote it.

## Each row (a single row(...) call in rows/<slug>.py)
- slug (given), name (the resource's own name), aka, url (its own canonical page), operator (who runs it, as its sources say), kind (what it is in its own words: archive, library, digital edition, database, tracker, publication, organisation...).
- areas: one or more keys of AREAS, primary first, only where its sources make it bear on that area.
- evidence_kind: one or more of EVIDENCE_KINDS, for the kind of record it actually holds.
- unit: its own unit of record (a work, a recording, an author page, a case, a dataset document...).
- record_object: what it records, as its sources say (whose works, which forms, which period).
- record: {"in_layer": whose works it holds or carries into training, or how it bears on that, "name": whether a work keeps its author's name and attribution there, AS ITS OWN SOURCES SHOW (metadata fields kept or stripped, attribution rules, authorship of generated text), or "not recorded", "readback": whether and how a work can be found there and read back (search, membership test, documentation, provenance), or "not recorded"}. This is the census's organizing question; do not supply what the sources do not show.
- method (how it gathers: volunteer transcription, scholarly edition, deposit of papers, news-derived event coding, survey microdata...), coverage {"geography", "period"}, count {"value", "as_of"} where stated.
- holdings: its holdings or headline content as it states them, short, each figure backed by an evidence item. stated_limits: its own stated limits (quote them).
- answers / does_not_answer: two short lists of questions its record can and cannot settle, exact to its method.
- tll_reading: one or two sentences, the archive's reading, on where the resource meets the question of #186 and #1543 (writing addressed to the machine reader; a work carried into training and whether it can be read back under its name), or "none stated". Keep the resource's own terms intact.
- data_access, license (as stated), lifecycle {"state": active | historical | paused | ended, "detail"}, founded where stated, version_and_time {"...": date, "read": "2026-10-31"}.
- negative_tags: "NOT ..." lines that keep it apart from what it is mistaken for or a stronger claim than it makes.
- evidence: {field_key: Q("<slug>--<id>", "<verbatim quote>")}. Every figure, date, limit and self-description is backed here; quotes verbatim from the saved .txt. basis "third_party" for a source not the resource's own.
- relations: [{"rel": "neighbour" | "part_of" | "has_part" | "uses" | "used_by", "target": "<another slug in ORDER>", "note"}] only where the sources support it .
- unchecked: what you could not read.

## Prose
Plain declarative English. Do not write "not X but Y", "X, not Y", "rather than" or "instead of" outside quotations; state the thing directly. No gendered generics. No hard line breaks inside values.

## Check
Run `cd data/layer-census && python3.12 census_src.py`. It prints problems for every row present; fix yours (missing fields, unknown keys, a quote not found) until your rows show none. Other readers' rows may appear; ignore their problems.

Wikipedia pages in sources are third-party: quote them with basis "third_party". Final message: your rows, each with its intersections, evidence kinds and lifecycle; sources you could not use; anything a row could not record; and any resource whose sources make it look misplaced in this census.
