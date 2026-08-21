from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript/main_text.md"


def _words(text: str) -> list[str]:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"^#+\s+.*$", " ", text, flags=re.MULTILINE)
    return re.findall(r"\b[\w]+(?:[’'–-][\w]+)*\b", text, flags=re.UNICODE)


def _section(text: str, start: str, end: str | None = None) -> str:
    assert start in text, f"missing section: {start}"
    tail = text.split(start, 1)[1]
    if end is None or end not in tail:
        return tail
    return tail.split(end, 1)[0]


def test_condition_recovered_manuscript_meets_letter_length_limits() -> None:
    text = MAIN.read_text(encoding="utf-8")
    abstract = _section(text, "## Abstract", "## Introduction")
    main = _section(text, "## Introduction", "## Data and code availability")
    abstract_words = len(_words(abstract))
    main_words = len(_words(main))
    print(f"condition-recovered manuscript words: abstract={abstract_words}, main={main_words}")
    assert abstract_words <= 150
    assert main_words <= 5000


def test_condition_recovered_manuscript_follows_condition_first_science() -> None:
    text = MAIN.read_text(encoding="utf-8")
    required = (
        "Fragmentation disrupted an interaction-supported functional state",
        "Recurrent state turnover changed source feasibility and functional-loss regime",
        "Warning-blind refinement recovered a narrow reproducible event regime",
        "Genetic connectivity changed loss-regime reproducibility without a simple rescue sign",
        "Aggregate interaction support changed source eligibility but not the R4 classification",
        "Genetic erosion could precede functional loss, but not by a universal absolute threshold",
        "Warning behaviour was not fully portable across independently calibrated domains",
    )
    positions = []
    for phrase in required:
        assert phrase in text
        positions.append(text.index(phrase))
    assert positions == sorted(positions)


def test_condition_recovered_manuscript_retains_key_evidence_boundaries() -> None:
    text = MAIN.read_text(encoding="utf-8")
    lower = text.lower()
    # Original no-domain result remains historical/bounded, while later R4 recovery
    # establishes that it was not structural impossibility.
    assert "all 15 coarse coordinates were historically `no_domain_selected`" in text
    assert "the coarse result was a placement boundary rather than structural impossibility" in text
    assert "R4 exists" in text

    # Connectivity and interaction-support axes retain their operator boundaries.
    assert "not demographic migration" in lower
    assert "not partner richness, connectance, pollinator diversity or network dimensionality" in lower
    assert "all three levels were therefore r4-highrep" in lower
    assert "bounded negative condition result" in lower
    assert "the kappa search was closed rather than widened to manufacture a boundary" in lower

    # Warning remains downstream and portability is not a single-factor result.
    assert "not a single-factor effect of transition direction" in text
    assert "does not establish that warning succeeds throughout R4" in text or "does not establish that genetic warning succeeds throughout R4" in text
    assert "universal connectivity threshold" not in lower
    assert "universal interaction-support threshold" not in lower
