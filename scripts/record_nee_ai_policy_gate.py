from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"{label}: expected one match, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    meta_path = ROOT / "manuscript/nee_flagship_submission_metadata.md"
    meta = meta_path.read_text(encoding="utf-8")
    meta = replace_once(
        meta,
        "- AI/automated-tool disclosure: [pending author review]",
        "- AI/automated-tool disclosure: [submission hard stop — journal-specific policy clarification required; see `NEE_AI_POLICY_AUDIT_2026-09-15.md`]",
        "metadata AI gate",
    )
    marker = "## Publication governance — flagship-first\n"
    insert = (
        "## Journal-policy eligibility gate\n\n"
        "The scientific and reproducibility package is mechanically complete, but NEE portal submission remains blocked pending resolution of the journal-specific generative-AI policy ambiguity recorded in `manuscript/NEE_AI_POLICY_AUDIT_2026-09-15.md`. Do not treat disclosure drafting alone as proof of policy compliance.\n\n"
    )
    meta = replace_once(meta, marker, insert + marker, "metadata policy section")
    meta_path.write_text(meta, encoding="utf-8")

    checklist_path = ROOT / "manuscript/submission_checklist.md"
    checklist = checklist_path.read_text(encoding="utf-8")
    checklist = replace_once(
        checklist,
        "- [ ] AI/automated-tool disclosure reviewed and approved.\n",
        "- [ ] AI/automated-tool disclosure reviewed and approved.\n- [ ] NEE journal-specific AI-policy eligibility clarified; current ambiguity is a submission hard stop (`NEE_AI_POLICY_AUDIT_2026-09-15.md`).\n",
        "checklist policy gate",
    )
    checklist_path.write_text(checklist, encoding="utf-8")


if __name__ == "__main__":
    main()
