from eco_genetic_warning_extensions.dynamic_partner_architecture_phase_t import (
    PHASE_T_ARCHITECTURES,
    PHASE_T_CONSTANT_SUPPORT,
    PHASE_T_DOMINANT_WEIGHTS,
    PHASE_T_EVEN_WEIGHTS,
    PHASE_T_PARTNER_AVAILABILITY,
    PHASE_T_PHASE_N_CONSTANT_BLOCKS,
    PHASE_T_REPLICATES_PER_SEED,
    phase_t_manifest,
    support_from_availability,
)
from eco_genetic_warning_extensions.dynamic_partner_architecture_phase_t_runner import availability_schedule


def test_phase_t_expected_support_is_exactly_matched() -> None:
    assert PHASE_T_REPLICATES_PER_SEED == 100
    assert PHASE_T_PARTNER_AVAILABILITY == 0.75
    assert PHASE_T_CONSTANT_SUPPORT == 0.75
    assert PHASE_T_EVEN_WEIGHTS == (0.25, 0.25, 0.25, 0.25)
    assert PHASE_T_DOMINANT_WEIGHTS == (0.70, 0.10, 0.10, 0.10)
    for architecture in PHASE_T_ARCHITECTURES:
        assert abs(architecture.expected_support - PHASE_T_CONSTANT_SUPPORT) < 1e-12


def test_concentration_changes_theoretical_support_variance_only() -> None:
    even = next(item for item in PHASE_T_ARCHITECTURES if item.name == "even_dynamic")
    dominant = next(item for item in PHASE_T_ARCHITECTURES if item.name == "dominant_dynamic")
    assert abs(even.support_variance - 0.046875) < 1e-12
    assert abs(dominant.support_variance - 0.0975) < 1e-12
    assert dominant.support_variance > even.support_variance > 0.0
    assert dominant.contribution_cv > even.contribution_cv


def test_support_mapping_respects_partner_weights() -> None:
    availability = (True, False, True, False)
    assert support_from_availability(PHASE_T_EVEN_WEIGHTS, availability) == 0.5
    assert abs(support_from_availability(PHASE_T_DOMINANT_WEIGHTS, availability) - 0.8) < 1e-12


def test_common_availability_schedule_is_deterministic() -> None:
    first = availability_schedule(12345, 12)
    second = availability_schedule(12345, 12)
    third = availability_schedule(12346, 12)
    assert first == second
    assert first != third
    assert all(len(row) == 4 for row in first)


def test_phase_n_constant_comparator_is_locked() -> None:
    assert PHASE_T_PHASE_N_CONSTANT_BLOCKS == (
        (51, 86), (45, 90), (45, 86), (46, 91), (53, 88)
    )


def test_manifest_forbids_rewiring_and_outcome_tuning() -> None:
    manifest = phase_t_manifest()
    assert manifest["matched_quantity"] == "expected support = 0.75 for constant, even_dynamic, and dominant_dynamic"
    assert manifest["rewiring"].startswith("not included")
    assert "Do not change availability probability" in manifest["stop_rule"]
    architectures = {row["name"]: row for row in manifest["dynamic_network"]["architectures"]}
    assert architectures["dominant_dynamic"]["support_variance"] > architectures["even_dynamic"]["support_variance"]
