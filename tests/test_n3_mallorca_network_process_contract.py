from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_stage_a_is_locked_and_fit_ready() -> None:
    x = json.loads((ROOT / "artifacts/empirical/n3_mallorca_network_stage_a_locked.json").read_text())
    assert x["decision"] == "fit_ready_for_prospective_B1_preregistration"
    assert x["eligible_species_year_pair_count"] == 41
    assert x["eligible_distinct_species_count"] == 22
    assert x["eligible_pair_counts_by_year"] == {"2016": 21, "2017": 20}
    assert x["fitness_or_baseline_missingness_exclusions"] == 0
    assert x["workflow_run"] == 33135325313


def test_process_contract_freezes_source_defined_direct_visitation() -> None:
    x = json.loads((ROOT / "protocols/n3_mallorca_network_process_adequacy_contract.json").read_text())
    assert x["source_doi"] == "10.5061/dryad.hqbzkh1bm"
    assert x["holdout_unit"] == "plant_species"
    assert x["eligible_species_year_pairs"] == 41
    assert x["response"] == {"name": "SeedsFlowerRounded", "family": "Poisson", "link": "log"}
    assert x["baseline_predictors"] == ["Year", "DPD", "FloralUnitSize"]
    assert x["process"]["unit"] == "visits_per_flower_per_5_min"
    assert "WeightedClosenessCentrality" in x["process"]["forbidden_substitutes"]
    assert "Act_Rate" in x["process"]["forbidden_substitutes"]
    assert x["bootstrap"] == {"unit": "plant_species", "draws": 10000, "seed": 20260828, "ci": [0.025, 0.975]}
    assert x["claim_ceiling"] == "within_one_Mallorca_community_process_adequacy_only_not_cross_origin_convergence"


def test_preregistration_preserves_no_rescue_and_claim_ceiling() -> None:
    text = (ROOT / "manuscript/n3_mallorca_network_process_adequacy_preregistration.md").read_text()
    assert "leave-one-species-out" in text
    assert "SeedsFlowerRounded" in text
    assert "sum across all pollinator columns" in text
    assert "No seed-weight endpoint" in text
    assert "Neither result is an independent island system replication" in text
    assert "infer island–urban equivalence or difference" in text
