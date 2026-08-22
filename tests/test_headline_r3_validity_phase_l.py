from eco_genetic_warning_extensions.headline_r3_validity_phase_l import phase_l_audit


def test_all_load_bearing_historical_r3_cases_are_audited() -> None:
    audit = phase_l_audit()
    assert audit["case_count"] == 10
    ids = {row["name"] for row in audit["headline_r3_cases"]}
    assert ids == {
        "C_pstar_040", "D_pstar_0325", "D_pstar_0375",
        "E_m010", "E_m020",
        "G_even", "G_graded", "G_dominant",
        "H_no_rewiring", "H_rewiring",
    }


def test_no_headline_r3_case_identifies_excess_block_heterogeneity_at_small_n() -> None:
    audit = phase_l_audit()
    assert audit["r3_cases_with_detectable_excess_block_heterogeneity"] == 0
    for row in audit["headline_r3_cases"]:
        assert row["historical_regime"] == "R3_highrep"
        assert row["pearson_equal_rate_p_value"] > 0.05
        assert row["inferential_status"] == "r3_does_not_identify_excess_block_heterogeneity"


def test_gate_sampling_failure_is_substantial_for_every_load_bearing_r3_case() -> None:
    audit = phase_l_audit()
    for row in audit["headline_r3_cases"]:
        assert row["sampling_reference_gate_failure_substantial"] is True
        assert row["homogeneous_reference_gate_fail_probability"] >= 0.10


def test_historical_r4_controls_remain_controls_not_reclassified() -> None:
    audit = phase_l_audit()
    assert audit["control_count"] == 4
    for row in audit["historical_r4_controls"]:
        assert row["historical_regime"] == "R4_highrep"
        assert row["inferential_status"] == "historical_r4_control"


def test_phase_l_requires_precision_followup_without_changing_old_labels() -> None:
    audit = phase_l_audit()
    assert audit["all_headline_r3_cases_require_mechanistic_reaudit"] is True
    follow = audit["required_follow_up"]
    assert "precision-validate" in follow["Phase C/D"]
    assert "precision-validate" in follow["Phase E"]
    assert "precision-validate" in follow["Phase G"]
    assert "Do not modify historical R3/R4 labels" in audit["stop_rule"]
