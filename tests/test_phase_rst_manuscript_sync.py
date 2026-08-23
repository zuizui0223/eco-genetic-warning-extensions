from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _has_decimal(text: str, token: str) -> bool:
    return token in text or token.removeprefix("0") in text


def test_phase_rstu_are_in_current_manuscript_sources() -> None:
    main = _read("manuscript/main_text.md")
    claims = _read("manuscript/claim_evidence_map.md")
    artifacts = _read("manuscript/artifact_index.md")
    program = _read("docs/HYPOTHESIS_PROGRAM.md")

    for text in (main, claims, artifacts, program):
        lower = text.lower()
        assert "whole-individual" in lower
        assert "pollen" in lower
        assert "dynamic" in lower
        assert "phase u" in lower

    for token in ("0.606", "0.532", "0.5442", "0.5488", "0.5533", "0.745", "0.694"):
        assert _has_decimal(main, token)
        assert _has_decimal(claims, token)

    assert "seed-family contingent" in main.lower()
    assert "fresh non-replication" in claims.lower() or "did not reproduce" in claims.lower()
    assert "rewiring" in claims.lower() and "gate" in claims.lower()
    assert "rewiring" in program.lower()


def test_old_next_model_and_replicated_connectivity_boundaries_are_removed() -> None:
    claims = _read("manuscript/claim_evidence_map.md").lower()
    assert "process-resolved biological movement remain next-model hypotheses" not in claims
    assert "## prohibited claims" in claims
    assert "`m=.10` is a reproducible or established connectivity heterogeneity threshold" in claims
    assert "no robust portable connectivity heterogeneity effect is established" in claims
    assert "one independent fresh-seed ensemble" in claims
    assert "one non-replication" in claims


def test_phase_rstu_do_not_create_new_warning_claims() -> None:
    program = _read("docs/HYPOTHESIS_PROGRAM.md").lower()
    main = _read("manuscript/main_text.md").lower()
    assert "phases r/s/t/u add no warning claims" in program
    assert "fresh-replication campaigns withheld warning outcomes" in main
