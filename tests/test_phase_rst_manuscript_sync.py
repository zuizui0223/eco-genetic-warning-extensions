from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _has_decimal(text: str, token: str) -> bool:
    return token in text or token.removeprefix("0") in text


def test_phase_rst_are_in_current_manuscript_sources() -> None:
    main = _read("manuscript/main_text.md")
    claims = _read("manuscript/claim_evidence_map.md")
    artifacts = _read("manuscript/artifact_index.md")
    program = _read("docs/HYPOTHESIS_PROGRAM.md")

    for text in (main, claims, artifacts, program):
        lower = text.lower()
        assert "whole-individual" in lower
        assert "pollen" in lower
        assert "dynamic" in lower

    for token in ("0.606", "0.532", "0.5442", "0.5488", "0.5533"):
        assert _has_decimal(main, token)
        assert _has_decimal(claims, token)

    assert "operator-specific" in main.lower()
    assert "operator-specific" in claims.lower()
    assert "rewiring" in claims.lower() and "gate" in claims.lower()
    assert "rewiring" in program.lower()


def test_old_next_model_boundary_is_removed_from_claim_gate() -> None:
    claims = _read("manuscript/claim_evidence_map.md").lower()
    assert "process-resolved biological movement remain next-model hypotheses" not in claims
    assert "process-resolved movement and dynamic partner availability have now been tested" in claims


def test_phase_rst_do_not_create_new_warning_claims() -> None:
    program = _read("docs/HYPOTHESIS_PROGRAM.md").lower()
    main = _read("manuscript/main_text.md").lower()
    assert "phases r/s/t do not add warning claims" in program
    assert "condition-recovery and r/s/t robustness campaigns withheld warning outcomes" in main
