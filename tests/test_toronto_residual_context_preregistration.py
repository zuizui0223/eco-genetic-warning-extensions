from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREREG = ROOT / "manuscript" / "empirical_toronto_residual_context_preregistration.md"
SCRIPT = ROOT / "scripts" / "run_toronto_residual_context.py"


def test_toronto_preregistration_locks_primary_endpoint_and_holdout_unit() -> None:
    text = PREREG.read_text(encoding="utf-8")
    assert "Primary realised-function endpoint" in text
    assert "`number_seed`" in text
    assert "`fruit_sample_size` is the exposure/denominator" in text
    assert "leave-one-garden-out (LOGO)" in text
    assert "Species rows sharing a garden are never counted as independent systems" in text


def test_toronto_preregistration_locks_process_and_context_order() -> None:
    text = PREREG.read_text(encoding="utf-8")
    assert "`I_visit = number_of_visits / survey_effort`" in text
    assert "`urban_cover`" in text
    assert "`ugs_edge_density`" in text
    assert "tested only after the partial process state is fixed" in text
    assert "No `urban_cover × species` or `edge_density × species` interaction is opened" in text


def test_toronto_script_implements_locked_species_richness_mapping() -> None:
    text = SCRIPT.read_text(encoding="utf-8")
    assert '"PEHI": "floral_richness_1"' in text
    assert '"DECA": "floral_richness_2"' in text
    assert '"LOSI": "floral_richness_2"' in text
    assert '"SYNO": "floral_richness_3"' in text
    assert "BOOTSTRAP_SEED = 20260827" in text


def test_toronto_script_keeps_context_out_of_m0_and_uses_garden_bootstrap() -> None:
    text = SCRIPT.read_text(encoding="utf-8")
    assert 'continuous = ["I_visit", "floral_units_array", "garden_richness_matched"]' in text
    assert 'continuous += ["urban_cover", "ugs_edge_density"]' in text
    assert 'for site in sorted(frame["site_id"].astype(str).unique())' in text
    assert 'rng.choice(deltas, size=(BOOTSTRAP_N, len(deltas)), replace=True)' in text
