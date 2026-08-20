import eco_genetic_warning_extensions as package


def test_top_level_api_exposes_current_scientific_primitives_only() -> None:
    assert set(package.__all__) == {
        "AsymmetricMutation",
        "MutationCoordinates",
        "alpha_gamma_diversity",
        "heterozygosity",
        "mutate_frequency",
        "primary_phase_grid",
    }


def test_historical_development_helpers_are_not_top_level_exports() -> None:
    historical_names = {
        "CalibrationCandidate",
        "MinimalLifeCycleFixture",
        "MutationSlotFixture",
        "example_source_skeleton_artifact",
        "select_protocol_001_domain",
        "symmetric_minimal_life_cycle_differences",
        "symmetric_slot_bridge_differences",
    }
    assert historical_names.isdisjoint(package.__all__)
