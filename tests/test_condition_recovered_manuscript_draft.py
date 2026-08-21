from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "manuscript/main_text_condition_recovered_draft.md"


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


def test_condition_recovered_draft_meets_letter_length_limits() -> None:
    text = DRAFT.read_text(encoding="utf-8")
    abstract = _section(text, "## Abstract", "## Introduction")
    main = _section(text, "## Introduction", "## Data and code availability")
    abstract_words = len(_words(abstract))
    main_words = len(_words(main))
    print(f"condition-recovered draft words: abstract={abstract_words}, main={main_words}")
    assert abstract_words <= 150
    assert main_words <= 5000


def test_condition_recovered_draft_follows_four_question_science() -> None:
    text = DRAFT.read_text(encoding="utf-8")
    required = (
        "Fragmentation disrupted an interaction-supported functional state",
        "Genetic erosion could precede functional loss",
        "Warning-blind refinement recovered a narrow reproducible R4 event regime",
        "Effective genetic connectivity moved the same R4 anchor into a heterogeneous event regime",
        "Warning behaviour was not fully portable across independently calibrated domains",
    )
    for phrase in required:
        assert phrase in text


def test_condition_recovered_draft_retains_key_evidence_boundaries() -> None:
    text = DRAFT.read_text(encoding="utf-8")
    assert "not structural impossibility" in text
    assert "R4 exists" in text
    assert "It is not demographic migration, pollinator movement, seed dispersal, recolonisation or trait-bin dispersal" in text
    assert "not a single-factor effect of transition direction" in text
    assert "does not establish that genetic warning succeeds throughout R4" in text
    assert "universal connectivity threshold" not in text
