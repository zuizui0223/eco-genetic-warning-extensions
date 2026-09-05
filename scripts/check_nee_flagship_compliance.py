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
    abstract = abstract.strip().split("\n\n", 1)[0]
    abstract_n = len(words(abstract))

    methods_start = article.index("## Methods\n")
    after_abstract_heading = article.index("## Abstract\n") + len("## Abstract\n")
    first_double = article.index("\n\n", after_abstract_heading)
    intro_start = first_double + 2
    main_text = article[intro_start:methods_start]
    main_n = len(words(main_text))

    figures = re.findall(r"^## Figure (\d+)\s", display, flags=re.M)
    ref_entries = [p for p in refs.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]

    # Print counts before any subsequent claim-contract assertion so CI logs remain diagnostic.
    print(f"NEE abstract words: {abstract_n}")
    print(f"NEE main-text words: {main_n}")
    print(f"Main displays: {len(figures)}")
    print(f"Core references: {len(ref_entries)}")

    assert abstract_n <= 200, f"abstract={abstract_n} words"
    assert main_n <= 3500, f"main_text={main_n} words"
    assert figures == ["1", "2", "3", "4", "5"], figures
    assert len(figures) <= 6
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

    # Load-bearing scientific content: allow reader-facing prose rather than one exact notation.
    required_patterns = {
        "EGC denominator": r"1,037/1,037",
        "state certificate": r"0\.2543",
        "propagation": r"\+5\.33",
        "event leads": r"35/35",
        "inherited non-events": r"all 48 inherited non-event trajectories|48/48",
        "fresh non-events": r"all 49 fresh non-event trajectories|49/49",
        "warning specificity": r"specificity 0|specificity zero",
        "representation collapse": r"8\.88e-16",
    }
    for label, pattern in required_patterns.items():
        assert re.search(pattern, article, flags=re.I), label

    forbidden = (
        "fragmentation caused the anti-aligned",
        "alignment caused warning failure",
        "natural data validate the simulator",
        "generation 20 is a universal",
    )
    lower = article.casefold()
    for token in forbidden:
        assert token.casefold() not in lower, token

    print("NEE flagship compliance: PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"NEE flagship compliance: FAIL — {exc}", file=sys.stderr)
        raise
