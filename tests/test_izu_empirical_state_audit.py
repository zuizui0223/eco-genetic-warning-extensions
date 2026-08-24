import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "empirical_e1_izu_audit.md").read_text(encoding="utf-8")
ARTIFACT = json.loads((ROOT / "artifacts" / "empirical" / "izu_partial_state_audit.json").read_text(encoding="utf-8"))


def test_izu_audit_uses_measured_functional_state() -> None:
    assert ARTIFACT["design"] == {
        "network_count": 40,
        "site_count": 8,
        "season_count": 5,
        "system": "Japanese coastal continental and oceanic island plant-pollinator networks",
    }
    state = ARTIFACT["candidate_ecological_state"]
    assert "pollinator_functional_composition_FD_Q_FEve" in state
    assert "flower_pollinator_trait_matching" in state
    assert "direct_pollination_function" in state


def test_species_richness_is_not_promoted_to_the_regime() -> None:
    result = ARTIFACT["published_state_results"]
    assert "rather than pollinator species diversity" in result["community_trait_matching_best_model"]
    assert "functional diversity" in ARTIFACT["headline"]
    assert "pollinator richness" not in ARTIFACT["candidate_ecological_state"]


def test_island_geography_is_upstream_not_assumed_sufficient() -> None:
    assert "island geography is a real upstream filter" in DOC
    assert "does not identify which downstream coordinate is functionally decisive" in DOC
    assert "do not by themselves prove" in ARTIFACT["identification_boundary"]


def test_residual_origin_prediction_is_the_next_test() -> None:
    assert "Does `E1-M2` improve held-out prediction/calibration" in DOC
    assert "holding out whole sites or site-seasons" in ARTIFACT["next_model"]
    assert "No new significance threshold" in DOC


def test_missing_genetic_connectivity_axes_are_explicit() -> None:
    missing = ARTIFACT["missing_full_state_axes"]
    assert "matched_focal_plant_genetics" in missing
    assert "parentage_based_pollen_connectivity" in missing
    assert "reproductive_assurance" in missing
