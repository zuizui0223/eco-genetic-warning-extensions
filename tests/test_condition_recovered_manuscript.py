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
        "Recurrent turnover changed source feasibility and loss incidence",
        "The historical `m=.10` connectivity heterogeneity did not replicate in fresh seeds",
        "Process-resolved movement also did not establish a portable connectivity effect",
        "Aggregate feedback and partner dynamics were bounded negative results",
        "Relative diversity thresholds ordered observed losses but did not discriminate events",
        "Warning behaviour was not fully portable across calibrated domains",
    )
    positions = [text.index(phrase) for phrase in required]
    assert positions == sorted(positions)


def test_condition_recovered_manuscript_retains_evidence_and_phase_u_boundary() -> None:
    text = MAIN.read_text(encoding="utf-8")
    lower = text.lower()
    assert "all 15 coarse coordinates remain historically `no_domain_selected`" in text
    assert "placement boundary rather than structural impossibility" in lower
    assert ".0205" in text
    assert ".745" in text
    assert "historical_m010_heterogeneity_not_freshly_replicated" in text
    assert "not supported as an independently reproducible `m=.10` heterogeneity effect" in lower
    assert "no robust, portable connectivity heterogeneity effect was established" in lower
    assert "seed-family contingent" in lower
    assert "not demographic migration" in lower
    assert "adaptive-rewiring gate remained closed" in lower
    assert "not a single-factor effect of transition direction" in lower
    assert "phase u is one preregistered independent replication" in lower
    assert "r4 itself means genetic warning succeeds" not in lower
    assert "the defensible conclusion is therefore not that `m=.10` is a reproducible heterogeneity threshold" in lower
