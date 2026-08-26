from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = json.loads(
    (ROOT / "artifacts/prepublication_review/precision_bounded_null_audit.json").read_text(
        encoding="utf-8"
    )
)


def test_nulls_are_precision_bounded_not_equivalence_claims() -> None:
    assert RESULT["claim_class"] == "precision-bounded null; not equivalence"
    assert "does not establish equivalence" in RESULT["methods"]["interpretation"]


def test_phase_u_paired_effect_interval_is_trajectory_based() -> None:
    comparison = RESULT["phases"]["phase_u_fresh_connectivity"]["paired_effect_95_ci"][
        "m_0.10_minus_m_0"
    ]
    assert comparison["comparable_trajectories"] == 452
    assert comparison["risk_difference_comparison_minus_reference"] == 5 / 452
    lower, upper = comparison["paired_normal_95_ci"]
    assert lower < 0 < upper
    assert -0.04 < lower < -0.03
    assert 0.05 < upper < 0.06


def test_partner_effect_intervals_preserve_detectable_width() -> None:
    phase_n = RESULT["phases"]["phase_n_partner_loss"]["paired_effect_95_ci"]
    phase_t = RESULT["phases"]["phase_t_dynamic_partner"]["paired_effect_95_ci"]
    for comparison in (*phase_n.values(), *phase_t.values()):
        lower, upper = comparison["paired_normal_95_ci"]
        assert lower < 0 < upper
    even = phase_t["even_minus_constant"]
    assert even["risk_difference_comparison_minus_reference"] == 2 / 441
    assert even["paired_normal_95_ci"][1] > 0.03
