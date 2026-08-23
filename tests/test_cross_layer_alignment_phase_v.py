from eco_genetic_warning_extensions.cross_layer_alignment_phase_v import (
    PHASE_V_CONDITIONS,
    PHASE_V_MASTER_SEEDS,
    PHASE_V_REPLICATES_PER_SEED,
    barrier_schedule,
    baseline_signature,
    cross_layer_covariance,
    one_step_state_sufficiency_certificate,
    phase_v_manifest,
    signatures_match,
    trait_abundance_rows,
)


def test_phase_v_is_exactly_one_alignment_contrast() -> None:
    manifest = phase_v_manifest()
    assert PHASE_V_CONDITIONS == ("aligned", "anti_aligned")
    assert PHASE_V_MASTER_SEEDS == (20300110, 20300111, 20300112, 20300113, 20300114)
    assert PHASE_V_REPLICATES_PER_SEED == 100
    assert manifest["warning_blind"] is True
    assert "Do not change state values" in manifest["stop_rule"]
    assert "city-versus-island" in manifest["urban_island_scope"]


def test_coarse_baseline_marginals_are_mathematically_identical() -> None:
    assert signatures_match()
    left = baseline_signature("aligned")
    right = baseline_signature("anti_aligned")
    exact_keys = (
        "patch_areas_sorted", "population_sorted", "q_sorted", "p_sorted",
        "high_trait_mass_sorted", "trait_bin_totals", "total_population",
    )
    for key in exact_keys:
        assert left[key] == right[key]
    for key in ("mean_q", "mean_p", "mean_high_trait_mass", "h_alpha", "h_gamma", "fst"):
        assert abs(float(left[key]) - float(right[key])) <= 1e-15
    assert left["total_population"] == 160
    assert abs(float(left["mean_q"]) - 0.8) < 1e-15
    assert abs(float(left["mean_p"]) - 0.5) < 1e-15
    assert abs(float(left["mean_high_trait_mass"]) - 0.5) < 1e-15
    assert abs(float(left["h_alpha"]) - 0.4) < 1e-15
    assert abs(float(left["h_gamma"]) - 0.5) < 1e-15
    assert abs(float(left["fst"]) - 0.2) < 1e-15


def test_trait_bin_totals_are_preserved_by_permutation() -> None:
    aligned = trait_abundance_rows("aligned")
    anti = trait_abundance_rows("anti_aligned")
    assert sorted(aligned) == sorted(anti)
    assert all(sum(row) == 40 for row in aligned + anti)


def test_alignment_is_the_only_cross_layer_direction_change() -> None:
    assert cross_layer_covariance("aligned") > 0
    assert cross_layer_covariance("anti_aligned") < 0
    assert abs(cross_layer_covariance("aligned") + cross_layer_covariance("anti_aligned")) < 1e-15


def test_identical_marginals_do_not_define_identical_next_transition() -> None:
    certificate = one_step_state_sufficiency_certificate()
    assert certificate["coarse_marginal_signatures_identical"] is True
    assert certificate["coarse_marginals_are_transition_sufficient"] is False
    assert float(certificate["maximum_patchwise_generation1_difference"]) > 0.05


def test_barrier_schedule_is_fixed_and_monotone() -> None:
    values = barrier_schedule()
    assert len(values) == 60
    assert values[0] > 0.50
    assert abs(values[-1] - 0.65) < 1e-15
    assert all(right > left for left, right in zip(values, values[1:]))
