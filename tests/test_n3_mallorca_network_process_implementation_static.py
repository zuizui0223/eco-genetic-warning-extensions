from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (ROOT / "scripts/run_n3_mallorca_network_process_adequacy.py").read_text(encoding="utf-8")
CONTRACT = json.loads((ROOT / "protocols/n3_mallorca_network_process_adequacy_contract.json").read_text())


def test_implementation_tracks_locked_source_and_units() -> None:
    assert 'DOI = "10.5061/dryad.hqbzkh1bm"' in SCRIPT
    assert 'SEM_SHEET = "Sheet 3_SEMvariables"' in SCRIPT
    assert '"SeedsFlowerRounded"' in SCRIPT
    assert '"DPD"' in SCRIPT and '"FloralUnitSize"' in SCRIPT
    assert '"I_visit"' in SCRIPT
    assert "sum(weights)" in SCRIPT
    assert "sm.families.Poisson()" in SCRIPT


def test_implementation_preserves_loso_and_species_bootstrap() -> None:
    assert 'frame["SpeciesNorm"] == species' in SCRIPT
    assert 'frame["SpeciesNorm"] != species' in SCRIPT
    assert 'BOOTSTRAP_SEED = 20260828' in SCRIPT
    assert 'BOOTSTRAP_N = 10000' in SCRIPT
    assert 'rng.choice(deltas' in SCRIPT
    assert '"process_information_detected" if total < 0 and float(hi) < 0' in SCRIPT


def test_implementation_does_not_add_forbidden_rescues() -> None:
    assert "WeightPerSeed" not in SCRIPT
    assert "WeightedClosenessCentrality" not in SCRIPT
    assert "Act_Rate" not in SCRIPT
    assert "Targ_Rate" not in SCRIPT
    assert "FlowerAbundance" not in SCRIPT
    assert CONTRACT["holdout_unit"] == "plant_species"
    assert CONTRACT["response"]["name"] == "SeedsFlowerRounded"
