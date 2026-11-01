"""Entity articles for the Training-Layer Literature meta-aggregator, derived from the /non articles (EA-NEGONT-02) on the operator's ruling of
2026-11-01 ("captures, then /nons, then single pages"), written by hand in the session (operator, 10:35 EDT: "lets do those by hand, no agents").
data/layer-census/articles-1.py holds the eighteen written for this census; The NEXT and Output share their /non rows with the leesharks.com
authorship census and take its articles. Each checked by /home/claude/fleet/tools/check_articles.py."""
import pathlib, runpy
_R = pathlib.Path(__file__).resolve().parents[2]
ARTICLES = dict(runpy.run_path(str(_R / "data/layer-census/articles-1.py"))["ARTICLES"])
_ls = _R / "data/layer-census/articles-ls-a.py"   # copied from leesharks.com data/authorship-census/articles-a.py, 2026-11-01
if _ls.exists():
    _A = runpy.run_path(str(_ls))["ARTICLES"]
    for _k in ("the-next", "output-anthology"):
        if _k in _A: ARTICLES[_k] = _A[_k]
