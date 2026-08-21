import json
from pathlib import Path

from eco_genetic_warning_extensions.interaction_support_phase_f import (
    PHASE_F_AREA_REFERENCE,
    PHASE_F_INTERACTION_KAPPAS,
    PHASE_F_KAPPA_MU,
    PHASE_F_MIGRATION_RATE,
    PHASE_F_P_STAR,
    PHASE_F_REPLICATES_PER_SEED,
    phase_f_manifest,
)


ROOT = Path(__file__).resolve().parents[1]


def test_phase_f_reuses_original_protocol002_kappa_levels() -> None:
    assert PHASE_F_INTERACTION_KAPPAS == (3.0, 4.5, 6.0)
    assert PHASE_F_AREA_REFERENCE == 1.0
    assert PHASE_F_KAPPA_MU == 0.35
    assert PHASE_F_P_STAR == 0.35
    assert PHASE_F_MIGRATION_RATE == 0.0
    assert PHASE_F_REPLICATES_PER_SEED == 20


def test_phase_f_manifest_is_blinded_and_bounded() -> None:
    manifest = phase_f_manifest()
    assert manifest["calibration_scope"] == "source_and_trait_loss_only"
    assert manifest["blinding_scope"] == "source_and_trait_loss_only"
    assert "warning_blind" not in manifest
    assert manifest["interaction_kappa_provenance"] == "original_protocol002_source_grid_values"
    assert manifest["condition_count"] == 3
    assert "do not refine kappa" in manifest["stop_rule"]


def test_phase_f_does_not_claim_network_simplification() -> None:
    boundary = phase_f_manifest()["interpretation_boundary"]
    assert "not partner richness" in boundary
    assert "network dimensionality" in boundary
    assert "pollinator diversity" in boundary


def test_phase_f_committed_result_closes_predeclared_axis() -> None:
    path = ROOT / "artifacts/interaction_support/phase_f_summary.json"
    artifact = json.loads(path.read_text(encoding="utf-8"))
    rows = artifact["interaction_support_summaries"]

    assert [row["interaction_kappa"] for row in rows] == [3.0, 4.5, 6.0]
    assert [row["status_counts"]["attempted"] for row in rows] == [100, 100, 100]
    assert [row["status_counts"]["baseline_eligible"] for row in rows] == [77, 94, 87]
    assert [row["status_counts"]["trait_loss"] for row in rows] == [36, 49, 48]
    assert [row["regime"] for row in rows] == ["R4_highrep", "R4_highrep", "R4_highrep"]
    assert [row["pooled_trait_loss_rate"] for row in rows] == [
        36 / 77,
        49 / 94,
        48 / 87,
    ]
    assert all(0.30 <= block["trait_loss_rate"] <= 0.70 for row in rows for block in row["seed_blocks"])

    provenance = artifact["run_provenance"]
    assert provenance["workflow_run_id"] == 32441549848
    assert provenance["artifact_id"] == 9432854668
    assert provenance["artifact_digest"] == "sha256:bb221af16a9b6557280610e90807fdfe058dccbafd7d0183e38d4525ecef2c16"
