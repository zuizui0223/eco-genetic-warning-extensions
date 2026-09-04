from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TITLE = "Matching eco-genetic summaries can hide different ecological futures"


def test_state_manuscript_cover_and_metadata_are_synchronized() -> None:
    manuscript = (ROOT / "manuscript/state_validity_and_empirical_measurement_gates.md").read_text(encoding="utf-8")
    cover = (ROOT / "manuscript/cover_letter.md").read_text(encoding="utf-8")
    metadata = (ROOT / "manuscript/submission_metadata.md").read_text(encoding="utf-8")
    readiness = (ROOT / "RELEASE_READINESS.md").read_text(encoding="utf-8")
    assert manuscript.startswith(f"# {TITLE}\n")
    assert TITLE in cover
    assert TITLE in metadata
    assert TITLE in readiness
    assert "35/35" not in cover
    assert "48/48" not in cover
    assert "Campanula" not in cover
    assert "natural-data extension" not in cover.casefold()


def test_state_display_contract_is_two_figure_and_warning_free() -> None:
    display = (ROOT / "manuscript/state_validity_display_allocation.md").read_text(encoding="utf-8")
    assert "exactly two figures" in display
    assert "Figure 1 — matching marginals can hide different next transitions" in display
    assert "Figure 2 — the hidden state difference propagates on a forecast horizon" in display
    assert "0.2543" in display
    assert "+5.33" in display
    assert "35/35" in display  # appears only in explicit exclusions
    assert "Do not include" in display


def test_locked_primary_propagation_values_match_submission_claims() -> None:
    payload = json.loads((ROOT / "artifacts/alignment_propagation/locked_summary.json").read_text(encoding="utf-8"))
    primary = {int(row["horizon"]): row for row in payload["result"]["primary_horizon_cells"]}
    assert primary[5]["risk_difference_anti_minus_aligned"] == 0.0
    assert primary[10]["risk_difference_anti_minus_aligned"] == 0.0033333333333333335
    assert primary[20]["risk_difference_anti_minus_aligned"] == 0.05333333333333334
    assert primary[40]["risk_difference_anti_minus_aligned"] == 0.052
    assert primary[20]["ci95_lower"] == 0.020439227320699846
    assert primary[20]["ci95_upper"] == 0.08622743934596683
    assert primary[40]["ci95_lower"] == 0.019623552659379068
    assert primary[40]["ci95_upper"] == 0.08437644734062093


def test_state_only_bundle_builds_without_non_state_evidence(tmp_path: Path) -> None:
    out = tmp_path / "state_submission"
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/build_state_validity_submission_bundle.py"),
            "--repo-root",
            str(ROOT),
            "--output",
            str(out),
        ],
        cwd=ROOT,
        check=True,
    )
    expected = {
        "manuscript/main_text.md",
        "manuscript/references.md",
        "manuscript/cover_letter.md",
        "manuscript/submission_metadata.md",
        "manuscript/display_allocation.md",
        "figures/figure1_state_counterexample.svg",
        "figures/figure2_horizon_propagation.svg",
        "tables/propagation_complete_grid.csv",
        "provenance/phase_v_locked_summary.json",
        "provenance/alignment_propagation_protocol.json",
        "provenance/alignment_propagation_locked_summary.json",
        "supplement/phase_u_fresh_connectivity.json",
        "supplement/phase_r_whole_individual_movement.json",
        "supplement/phase_s_pollen_only_movement.json",
        "supplement/phase_t_partner_architecture.json",
        "MANIFEST.sha256",
    }
    observed = {p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file()}
    assert expected <= observed
    assert not any("warning_validity" in path for path in observed)
    assert not any("natural_data" in path for path in observed)
    assert not any("empirical_" in path for path in observed)
    assert not any("stage3_" in path for path in observed)

    fig1 = (out / "figures/figure1_state_counterexample.svg").read_text(encoding="utf-8")
    fig2 = (out / "figures/figure2_horizon_propagation.svg").read_text(encoding="utf-8")
    assert "0.2543" in fig1
    assert "+5.33" in fig2
    assert "+5.20" in fig2
    assert "precision diagnostics" in fig2
