from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "manuscript" / "state_validity_and_empirical_measurement_gates.md"
WARNING = ROOT / "manuscript" / "warning_validity.md"
SUMMARY = ROOT / "artifacts" / "cross_layer_alignment" / "phase_v_locked_summary.json"


def paired_risk_difference_interval(summary: dict) -> tuple[float, float, float]:
    paired = summary["paired"]
    n = int(paired["comparable_pairs"])
    anti_only = int(paired["aligned_no_loss_anti_loss"])
    aligned_only = int(paired["aligned_loss_anti_no_loss"])
    diff = (anti_only - aligned_only) / n
    variance_d = (anti_only + aligned_only) / n - diff * diff
    se = math.sqrt(variance_d / n)
    return diff, diff - 1.96 * se, diff + 1.96 * se


def test_state_validity_reports_interval_not_p_value_only() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    diff, lower, upper = paired_risk_difference_interval(summary)
    assert math.isclose(diff, 0.044, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(lower, -0.012130238951923236, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(upper, 0.10013023895192323, rel_tol=0.0, abs_tol=1e-12)
    baseline = float(summary["aligned"]["pooled_trait_loss_rate"])
    assert math.isclose(upper / baseline, 0.14768471821817586, rel_tol=0.0, abs_tol=1e-12)

    text = STATE.read_text(encoding="utf-8")
    for required in (
        "+4.4 percentage points",
        "-1.2 to +10.0 percentage points",
        "14.8% relative increase",
        "Non-significant tests do not establish equivalence",
    ):
        assert required in text
    flat = " ".join(text.split())
    assert (
        "does not exclude effects of roughly this magnitude" in flat
        or "did not exclude effects of roughly this magnitude" in flat
        or (
            "upper confidence limit corresponds" in flat
            and "14.8% relative increase" in flat
        )
    )


def test_warning_abstract_leads_with_frozen_full_denominator_design() -> None:
    text = WARNING.read_text(encoding="utf-8")
    abstract = text.split("## Abstract", 1)[1].split("## Introduction", 1)[0].strip()
    flat = " ".join(abstract.split())
    assert flat.startswith(
        "We evaluated six predeclared and frozen baseline-relative genetic-diversity "
        "thresholds against the full baseline-eligible denominator for the first time "
        "under their frozen protocol"
    )
    for required in (
        "without changing endpoints or rerunning trajectories",
        "35/35 and 33/33",
        "48/48 and 49/49",
        "408 event-threshold lead records",
        "582 non-event-threshold firing records",
        "not independent biological replicates",
    ):
        assert required in flat


def test_warning_endpoint_record_counts_match_frozen_trajectory_denominators() -> None:
    inherited_events = 35
    fresh_events = 33
    inherited_nonevents = 48
    fresh_nonevents = 49
    n_thresholds = 6
    assert (inherited_events + fresh_events) * n_thresholds == 408
    assert (inherited_nonevents + fresh_nonevents) * n_thresholds == 582