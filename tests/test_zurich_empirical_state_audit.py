import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_e2_zurich_audit.md").read_text(encoding="utf-8")
ARTIFACT = json.loads((ROOT / "artifacts" / "empirical" / "zurich_partial_state_audit.json").read_text(encoding="utf-8"))


def test_zurich_audit_is_secondary_not_raw_refit() -> None:
    assert "secondary audit" in DOC.lower()
    assert "not a new refit" in DOC.lower()
    assert ARTIFACT["status"] == "secondary_audit_of_open_source_model_outputs_not_raw_data_refit"


def test_urban_scalar_is_not_promoted_to_universal_state() -> None:
    effects = ARTIFACT["urban_500_function_effects"]
    assert len(effects) == 6
    assert ARTIFACT["clear_negative_urban_500_count"] == 3
    assert any(row["classification"] == "interval_includes_zero" for row in effects)
    assert "does not define a single functional-fragmentation response" in DOC


def test_interaction_state_remains_function_specific() -> None:
    selected = ARTIFACT["selected_interaction_effects"]
    carrot = [row for row in selected if row["function"] == "carrot_seed_set"]
    assert any(row["guild"] == "hoverflies_abundance" and row["mean"] > 0 for row in carrot)
    assert any(row["guild"] == "honeybees_abundance" and row["mean"] < 0 for row in carrot)
    assert "not total pollinator abundance or richness" in DOC


def test_joint_state_sufficiency_is_not_claimed_without_joint_model() -> None:
    assert "not sufficient to test the strict state-sufficiency criterion" in DOC
    assert "does **not** claim that interaction state statistically mediates the urban effect" in DOC
    assert "joint state-sufficiency model" in ARTIFACT["identification_boundary"]
    assert "held-out predictive" in ARTIFACT["next_model"]


def test_missing_full_state_axes_are_explicit() -> None:
    mapping = ARTIFACT["state_mapping"]
    assert "not available" in mapping["natural_plant_genetic_state"]
    assert "not available" in mapping["process_specific_pollen_seed_connectivity"]
    assert "not resolved" in mapping["ecological_memory"]
