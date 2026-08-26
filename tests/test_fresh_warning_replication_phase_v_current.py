import json
from pathlib import Path

from eco_genetic_warning_extensions.fresh_warning_replication_phase_v import (
    PHASE_V_FROZEN_DOMAIN,
    PHASE_V_MASTER_SEEDS,
    one_sided_binomial_lead_p_value,
    phase_v_manifest,
)

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = json.loads((ROOT / "artifacts" / "fresh_warning_replication" / "phase_v_locked_summary.json").read_text(encoding="utf-8"))
RESULT = (ROOT / "docs" / "FRESH_WARNING_REPLICATION_PHASE_V_RESULT.md").read_text(encoding="utf-8")


def test_phase_v_manifest_remains_frozen() -> None:
    manifest = phase_v_manifest()
    assert tuple(manifest["master_seeds"]) == PHASE_V_MASTER_SEEDS
    assert manifest["frozen_domain"] == PHASE_V_FROZEN_DOMAIN
    assert manifest["attempted_trajectories"] == 100
    assert len(manifest["endpoint_family"]) == 6


def test_exact_binomial_reference() -> None:
    assert one_sided_binomial_lead_p_value(33, 33) == 1.1641532182693481e-10


def test_locked_phase_v_result_is_strict_replication() -> None:
    assert SUMMARY["decision"] == "strict_replication"
    assert SUMMARY["denominators"]["trait_loss_observed_count"] == 33
    assert len(SUMMARY["endpoint_family"]) == 6
    for row in SUMMARY["endpoint_family"]:
        assert row["valid_pairs"] == 33
        assert row["leads"] == 33
        assert row["ties"] == 0
        assert row["lags"] == 0


def test_phase_v_protocol_fact_is_retained_but_predictive_claim_is_corrected() -> None:
    assert "within the frozen symmetric H2-R domain" in RESULT
    assert "strictly replicated" in RESULT
    assert "all 49 non-event trajectories" in RESULT
    assert "specificity was therefore zero" in RESULT
    assert "not validated predictive early warning" in RESULT
    assert "which measured ecological state defines the domain" in RESULT
    assert "universal absolute or relative genetic-warning threshold" in RESULT


def test_phase_v_provenance_is_immutable() -> None:
    p = SUMMARY["provenance"]
    assert p["workflow_run"] == 32636847803
    assert p["aggregate_artifact"] == 9492587604
    assert p["artifact_digest"] == "sha256:c1dd951c961999c42255b46327d4650d2298afa98ee4d0a45d04a1e1c5fe6031"
