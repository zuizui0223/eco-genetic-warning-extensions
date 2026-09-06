from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / "manuscript/nee_flagship_article.md"
DISPLAY = ROOT / "manuscript/nee_flagship_display_plan.md"
REFERENCES = ROOT / "manuscript/nee_flagship_references.md"
MANIFEST = ROOT / "manuscript/nee_flagship_source_manifest.json"


def words(text: str) -> list[str]:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return re.findall(r"[A-Za-z0-9_α-ωΑ-Ω]+(?:[-–—'][A-Za-z0-9_α-ωΑ-Ω]+)*", text)


def between(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def main() -> None:
    article = ARTICLE.read_text(encoding="utf-8")
    display = DISPLAY.read_text(encoding="utf-8")
    refs = REFERENCES.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    title = "Relational eco-genetic state governs functional vulnerability under fragmentation"
    assert article.startswith(f"# {title}\n")
    for heading in ("## Abstract", "## Results", "## Discussion", "## Methods"):
        assert heading in article, heading

    abstract_block = between(article, "## Abstract\n", "## Results\n")
    abstract = abstract_block.strip().split("\n\n", 1)[0]
    abstract_n = len(words(abstract))

    after_abstract = article.index("## Abstract\n") + len("## Abstract\n")
    abstract_end = article.index("\n\n", after_abstract)
    methods_start = article.index("## Methods\n")
    main_text = article[abstract_end + 2:methods_start]
    main_n = len(words(main_text))

    results = between(article, "## Results\n", "## Discussion\n")
    discussion = between(article, "## Discussion\n", "## Methods\n")

    assert abstract_n <= 200, abstract_n
    assert main_n <= 3500, main_n

    figures = re.findall(r"^## Figure (\d+)\s", display, flags=re.M)
    assert figures == ["1", "2", "3", "4"], figures
    assert len(figures) <= 6

    ref_entries = [p for p in refs.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    assert len(ref_entries) <= 50, len(ref_entries)

    required = (
        "K > 4",
        "1,037/1,037",
        "T_I=g\\circ\\phi",
        "0.2543",
        "+5.33",
        "+5.20",
        "35 observed losses",
        "48 inherited non-event",
        "33 observed losses",
        "49 fresh non-event",
        "specificity 0",
        "binary-marker AUC 0.5",
    )
    for token in required:
        assert token in article, token

    # Natural examples and natural-data programmes must stay outside load-bearing Results.
    for token in (
        "Crepis",
        "Miyake",
        "Zosterops",
        "Conospermum",
        "Spondias",
        "Honshu",
        "Zurich",
        "Toronto",
        "Oenothera",
        "Eschscholzia",
        "Mallorca",
        "Campanula americana",
    ):
        assert token not in results, f"natural projection leaked into Results: {token}"

    for token in ("Crepis", "Miyake", "Conospermum", "Spondias", "urban–island"):
        assert token in discussion or token in article[: article.index("## Results")], token

    lower = article.casefold()
    for forbidden in (
        "natural examples validate the model",
        "natural data validate the simulator",
        "alignment caused warning failure",
        "fragmentation caused the anti-aligned",
        "generation 20 is a universal",
    ):
        assert forbidden not in lower, forbidden

    assert manifest["schema_version"] == 2
    assert len(manifest["load_bearing_sources"]) == 2
    assert len(manifest["projection_sources"]) == 1
    assert len(manifest["claim_firewalls"]) >= 8

    print(f"NEE abstract words: {abstract_n}")
    print(f"NEE main-text words: {main_n}")
    print(f"Main displays: {len(figures)}")
    print(f"References: {len(ref_entries)}")
    print("Math-first NEE flagship compliance: PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"Math-first NEE flagship compliance: FAIL — {exc}", file=sys.stderr)
        raise
