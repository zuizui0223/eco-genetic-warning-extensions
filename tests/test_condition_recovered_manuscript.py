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
    assert len(_words(abstract)) <= 150
    assert len(_words(main)) <= 5000


def test_condition_recovered_manuscript_follows_current_condition_first_science() -> None:
    text = MAIN.read_text(encoding="utf-8")
    required = (
        "Fragmentation disrupted an interaction-supported functional state",
        "Recurrent turnover changed source feasibility and historical loss-screen placement",
        "High-precision recurrent-turnover replays recovered an incidence frontier",
        "Allele-frequency connectivity produced non-monotone block heterogeneity, not a marginal-risk gradient",
        "The connectivity heterogeneity did not port to whole-individual or pollen-only movement",
        "Aggregate feedback, partner loss and temporal partner variability were bounded negative condition results",
        "Genetic erosion could precede functional loss, but not by a universal absolute threshold",
        "Warning behaviour was not fully portable across independently calibrated domains",
    )
    positions = [text.index(phrase) for phrase in required]
    assert positions == sorted(positions)


def test_condition_recovered_manuscript_retains_evidence_and_new_interpretation_boundaries() -> None:
    text = MAIN.read_text(encoding="utf-8")
    lower = text.lower()
    assert "all 15 coarse coordinates remain historically `no_domain_selected`" in text
    assert "the coarse result was a placement boundary rather than structural impossibility" in lower
    assert "historical r3 is described as a mixed-block screen failure" in lower
    assert "not demographic migration" in lower
    assert "not partner richness, connectance, pollinator diversity or network dimensionality" in lower
    assert "bounded negative condition result" in lower
    assert "the kappa search was closed rather than widened to manufacture a boundary" in lower
    assert "operator-specific within the tested connectivity closures" in lower
    assert "adaptive-rewiring gate therefore remains **closed**" in lower
    assert "not a single-factor effect of transition direction" in lower
    assert "r4 itself means genetic warning succeeds" not in lower
    assert "universal connectivity threshold" not in lower
