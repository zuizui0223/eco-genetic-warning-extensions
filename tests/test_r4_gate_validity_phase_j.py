import pytest

from eco_genetic_warning_extensions.r4_gate_validity_phase_j import (
    PHASE_H_PARTNER_LOSS_BLOCKS,
    PHASE_I_PARTNER_LOSS_BLOCKS,
    accepted_loss_count_bounds,
    audit_observed_blocks,
    block_gate_pass_probability,
    ensemble_gate_pass_probability,
    observed_gate_pass,
    phase_j_audit,
)


def test_gate_count_bounds_match_historical_inclusive_rates() -> None:
    assert accepted_loss_count_bounds(17) == (6, 11)
    assert accepted_loss_count_bounds(18) == (6, 12)
    assert accepted_loss_count_bounds(20) == (6, 14)


def test_phase_h_and_phase_i_historical_gate_labels_are_reproduced() -> None:
    assert observed_gate_pass(PHASE_H_PARTNER_LOSS_BLOCKS) is False
    assert observed_gate_pass(PHASE_I_PARTNER_LOSS_BLOCKS) is True


def test_homogeneous_half_risk_gate_is_finite_sample_sensitive_at_small_n() -> None:
    pass_17 = ensemble_gate_pass_probability((17, 17, 17, 17, 17), 0.5)
    pass_20 = ensemble_gate_pass_probability((20, 20, 20, 20, 20), 0.5)
    pass_100 = ensemble_gate_pass_probability((100, 100, 100, 100, 100), 0.5)
    assert pass_17 < 0.50
    assert pass_20 > pass_17
    assert pass_100 > 0.99


def test_single_block_gate_probability_is_valid() -> None:
    for n in (17, 18, 19, 20, 50, 100):
        for p in (0.3, 0.5, 0.7):
            value = block_gate_pass_probability(n, p)
            assert 0.0 <= value <= 1.0


def test_observed_partner_loss_blocks_do_not_require_excess_seed_heterogeneity() -> None:
    h = audit_observed_blocks("h", PHASE_H_PARTNER_LOSS_BLOCKS, "R3_highrep")
    i = audit_observed_blocks("i", PHASE_I_PARTNER_LOSS_BLOCKS, "R4_highrep")
    assert h.pearson_equal_rate_df == 4
    assert i.pearson_equal_rate_df == 4
    assert h.pearson_equal_rate_p_value > 0.05
    assert i.pearson_equal_rate_p_value > 0.05
    assert h.homogeneous_reference_gate_fail_probability > 0.50
    assert i.homogeneous_reference_gate_fail_probability > 0.30


def test_phase_j_preserves_historical_labels_and_scope() -> None:
    audit = phase_j_audit()
    assert audit["scope"] == "historical_gate_diagnostic_not_reclassification"
    rows = {row["name"]: row for row in audit["observed_audits"]}
    assert rows["phase_h_partner_loss_no_rewiring"]["historical_regime"] == "R3_highrep"
    assert rows["phase_i_partner_loss_no_rescue"]["historical_regime"] == "R4_highrep"
    assert "does not retroactively change" in audit["claim_boundary"]
