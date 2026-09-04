from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript/state_validity_and_empirical_measurement_gates.md"
COMPLIANCE = ROOT / "manuscript/ecology_letters_compliance.md"
ALLOCATION = ROOT / "manuscript/state_validity_display_allocation.md"
COVER = ROOT / "manuscript/cover_letter.md"


def _words(text: str) -> list[str]:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"^#+\s+.*$", " ", text, flags=re.MULTILINE)
    return re.findall(r"\b[\w]+(?:[’'–-][\w]+)*\b", text, flags=re.UNICODE)


def _section(text: str, start: str, end: str) -> str:
    try:
        return text.split(start, 1)[1].split(end, 1)[0]
    except IndexError as exc:
        raise AssertionError(f"missing section boundary: {start!r} -> {end!r}") from exc


def _first_prose_paragraph(section: str) -> str:
    for block in re.split(r"\n\s*\n", section.strip()):
        stripped = block.strip()
        if not stripped or stripped.startswith("#"):
            continue
        return stripped
    raise AssertionError("Introduction has no prose paragraph")


def main() -> int:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    compliance = COMPLIANCE.read_text(encoding="utf-8")
    allocation = ALLOCATION.read_text(encoding="utf-8")
    cover = COVER.read_text(encoding="utf-8")

    abstract = _section(manuscript, "## Abstract", "## Introduction")
    introduction = _section(manuscript, "## Introduction", "## Methods")
    main_text = _section(manuscript, "## Introduction", "## Data and code availability")
    conclusion = _section(manuscript, "## Conclusion", "## Data and code availability")

    abstract_words = len(_words(abstract))
    main_words = len(_words(main_text))
    problem_words = len(_words(_first_prose_paragraph(introduction)))
    conclusion_words = len(_words(conclusion))

    assert abstract_words <= 150, f"state abstract exceeds 150 words: {abstract_words}"
    assert main_words <= 5000, f"state main text exceeds 5000 words: {main_words}"
    assert problem_words < 100, f"opening problem statement is not under 100 words: {problem_words}"
    assert conclusion_words < 200, f"conclusion is not under 200 words: {conclusion_words}"

    running_title_match = re.search(r"Running title:\s*\*\*(.+?)\*\*", compliance)
    assert running_title_match, "state running title is not declared"
    running_title = running_title_match.group(1).strip()
    assert len(running_title) < 45, f"running title is {len(running_title)} characters"

    keywords_match = re.search(r"Keywords:\s*\*\*(.+?)\*\*", compliance)
    assert keywords_match, "state keywords are not declared"
    keywords = [item.strip() for item in keywords_match.group(1).split(";") if item.strip()]
    assert len(keywords) <= 10, f"keyword count exceeds 10: {len(keywords)}"

    assert "Main display items: **2 figures**" in compliance
    assert "Main tables: **none**" in compliance
    assert "Text boxes: **none**" in compliance
    assert "exactly two figures" in allocation
    assert "### Figure 1" in allocation
    assert "### Figure 2" in allocation
    assert "### Figure 3" not in allocation

    title = manuscript.splitlines()[0].removeprefix("# ").strip()
    assert title == "Matching eco-genetic summaries can hide different ecological futures"
    assert title in cover
    for forbidden in ("35/35", "48/48", "33/33", "49/49", "Honshu", "Oenothera", "Eschscholzia"):
        assert forbidden not in cover, f"non-state claim leaked into cover letter: {forbidden}"

    print(
        "State Ecology Letters compliance passed: "
        f"abstract={abstract_words}, main_text={main_words}, "
        f"problem_statement={problem_words}, conclusion={conclusion_words}, "
        f"displays=2, keywords={len(keywords)}, running_title_chars={len(running_title)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
