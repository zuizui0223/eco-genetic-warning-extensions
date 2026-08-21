import json
from pathlib import Path

import pytest

from eco_genetic_warning_extensions.classification_gate_theory import (
    all_block_gate_pass_probability,
    enumerate_panel_regimes,
    legacy_gate_design_statement,
    wilson_interval,
)

ROOT = Path(__file__).resolve().parents[1]


def test_all_block_gate_pass_probability_depends_on_panel_size() -> None:
    q = 0.95
    assert all_block_gate_pass_probability(q, 1) == pytest.approx(0.95)
    assert all_block_gate_pass_probability(q, 5) == pytest.approx(0.95**5)
    assert all_block_gate_pass_probability(q, 10) < all_block_gate_pass_probability(q, 5)
    assert all_block_gate_pass_probability(1.0, 100) == 1.0
    assert all_block_gate_pass_probability(0.0, 1) == 0.0


def test_phase_j_all_five_block_panels_are_exactly_75_percent_R4() -> None:
    summary = json.loads(
        (ROOT / "artifacts/classification_stability/phase_j_summary.json").read_text(encoding="utf-8")
    )
    rates = [row["trait_loss_rate"] for row in summary["seed_blocks"]]
    audit = enumerate_panel_regimes(rates, panel_size=5)
    assert audit["panel_count"] == 15504
    assert audit["regime_counts"] == {"seed_heterogeneous": 3876, "warning_evaluable": 11628}
    assert audit["regime_fractions"]["warning_evaluable"] == pytest.approx(0.75)
    assert audit["regime_fractions"]["seed_heterogeneous"] == pytest.approx(0.25)


def test_phase_j_block_pass_fraction_and_wilson_interval_are_locked() -> None:
    summary = json.loads(
        (ROOT / "artifacts/classification_stability/phase_j_summary.json").read_text(encoding="utf-8")
    )
    successes = summary["twenty_seed_diagnostics"]["inside_R4_band_count"]
    total = summary["twenty_seed_diagnostics"]["seed_block_count"]
    assert successes == 19 and total == 20
    lower, upper = wilson_interval(successes, total)
    assert lower == pytest.approx(0.763868806553258, abs=1e-12)
    assert upper == pytest.approx(0.9911185511992047, abs=1e-12)


def test_design_statement_explicitly_limits_biological_interpretation() -> None:
    statement = legacy_gate_design_statement().lower()
    assert "q**b" in statement
    assert "panel size" in statement
    assert "sample-size-invariant biological state" in statement
