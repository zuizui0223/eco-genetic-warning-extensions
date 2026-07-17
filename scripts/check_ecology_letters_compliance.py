from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript/main_text.md"
COMPLIANCE = ROOT / "manuscript/ecology_letters_compliance.md"
ALLOCATION = ROOT / "manuscript/main_vs_supplement.md"
CAPTIONS = ROOT / "manuscript/table_captions.md"


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


def main() -> int:
    manuscript = MAIN.read_text(encoding="utf-8")
    compliance = COMPLIANCE.read_text(encoding="utf-8")
    allocation = ALLOCATION.read_text(encoding="utf-8")
    captions = CAPTIONS.read_text(encoding="utf-8")

    abstract = _section(manuscript, "## Abstract", "## Introduction")
    main_text = _section(manuscript, "## Introduction", "## Data and code availability")
    abstract_words = len(_words(abstract))
    main_words = len(_words(main_text))

    assert abstract_words <= 150, f"abstract exceeds 150 words: {abstract_words}"
    assert main_words <= 5000, f"main text exceeds 5000 words: {main_words}"

    running_title_match = re.search(r"Running title:\s*\*\*(.+?)\*\*", compliance)
    assert running_title_match, "running title is not declared"
    running_title = running_title_match.group(1).strip()
    assert len(running_title) < 45, f"running title is {len(running_title)} characters"

    keywords_match = re.search(r"Keywords:\s*\*\*(.+?)\*\*", compliance)
    assert keywords_match, "keywords are not declared"
    keywords = [item.strip() for item in keywords_match.group(1).split(";") if item.strip()]
    assert len(keywords) <= 10, f"keyword count exceeds 10: {len(keywords)}"

    assert "Main display items: **Figures 1–6 only**" in compliance
    assert "Main tables: **none**" in compliance
    assert "Text boxes: **none**" in compliance
    assert "## Main-text tables" not in allocation
    for number in range(1, 7):
        assert f"### Figure {number}" in allocation
    for number in range(1, 6):
        assert f"## Table S{number}." in captions
    assert "## Table 1." not in captions
    assert "## Table 2." not in captions

    print(
        f"Ecology Letters compliance passed: abstract={abstract_words}, "
        f"estimated_main_text={main_words}, displays=6, keywords={len(keywords)}, "
        f"running_title_chars={len(running_title)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
