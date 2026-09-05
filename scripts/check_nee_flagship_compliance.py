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
    # Count prose tokens conservatively; markdown punctuation is ignored.
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"https?://\S+", " URL ", text)
    return re.findall(r"[A-Za-z0-9_α-ωΑ-Ω]+(?:[-–—'][A-Za-z0-9_α-ωΑ-Ω]+)*", text)


def section(text: str, heading: str, next_heading: str | None = None) -> str:
    start_marker = f"## {heading}\n"
    if start_marker not in text:
        raise AssertionError(f"missing section: {heading}")
    start = text.index(start_marker) + len(start_marker)
    if next_heading is None:
        return text[start:]
    end_marker = f"## {next_heading}\n"
    if end_marker not in text[start:]:
        raise AssertionError(f"missing next section: {next_heading}")
    end = text.index(end_marker, start)
    return text[start:end]


def main() -> None:
    article = ARTICLE.read_text(encoding="utf-8")
    display = DISPLAY.read_text(encoding="utf-8")
    refs = REFERENCES.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert article.startswith("# Ecological prediction requires validated state, signal and measurement\n")
    assert "## Introduction" not in article, "NEE Article introduction should be unheaded"
    for h in ("## Abstract", "## Results", "## Discussion", "## Methods"):
        assert h in article, h

    abstract = section(article, "Abstract", "Results")
    # The unheaded introduction lies between the abstract and Results, so remove it
    # from the abstract span by splitting at the first paragraph after the abstract.
    # The abstract is the first paragraph after its heading.
    abstract = abstract.strip().split("\n\n", 1)[0]
    abstract_n = len(words(abstract))
    assert abstract_n <= 200, f"abstract={abstract_n} words"

    results_start = article.index("## Results\n")
    methods_start = article.index("## Methods\n")
    # Main text includes the unheaded introduction plus Results and Discussion,
    # but excludes title, abstract, Methods and reference list.
    after_abstract_heading = article.index("## Abstract\n") + len("## Abstract\n")
    first_double = article.index("\n\n", after_abstract_heading)
    intro_start = first_double + 2
    main_text = article[intro_start:methods_start]
    main_n = len(words(main_text))
    assert main_n <= 3500, f"main_text={main_n} words"

    figures = re.findall(r"^## Figure (\d+)\s", display, flags=re.M)
    assert figures == ["1", "2", "3", "4", "5"], figures
    assert len(figures) <= 6

    # NEE Articles normally recommend no more than ~50 references.
    ref_entries = [p for p in refs.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    assert len(ref_entries) <= 50, len(ref_entries)

    assert manifest["schema_version"] == 1
    assert len(manifest["sources"]) == 3
    repos = {x["repository"] for x in manifest["sources"]}
    assert repos == {
        "zuizui0223/eco-genetic-criticality",
        "zuizui0223/eco-genetic-warning-extensions",
        "zuizui0223/egwee",
    }
    assert len(manifest["claim_firewalls"]) >= 6

    # Load-bearing headline values must be present once in the integrated draft.
    for token in ("1,037/1,037", "0.2543", "+5.33", "35/35", "48/48", "specificity 0", "8.88e-16"):
        assert token in article, token

    # Forbidden causal shortcuts.
    forbidden = (
        "fragmentation caused the anti-aligned",
        "alignment caused warning failure",
        "natural data validate the simulator",
        "generation 20 is a universal",
    )
    lower = article.casefold()
    for token in forbidden:
        assert token.casefold() not in lower, token

    print(f"NEE abstract words: {abstract_n}")
    print(f"NEE main-text words: {main_n}")
    print(f"Main displays: {len(figures)}")
    print(f"Core references: {len(ref_entries)}")
    print("NEE flagship compliance: PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"NEE flagship compliance: FAIL — {exc}", file=sys.stderr)
        raise
