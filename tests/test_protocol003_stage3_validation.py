from eco_genetic_warning_extensions.protocol003_stage3_validation import (
    RELATIVE_DECLINE_FRACTIONS,
    VALIDATION_MASTER_SEEDS,
    VALIDATION_REPLICATES_PER_SEED,
    protocol003_validation_domains,
)


def test_protocol003_stage3_design_is_locked() -> None:
    domains = protocol003_validation_domains()
    assert len(domains) == 2
    assert VALIDATION_MASTER_SEEDS == (20270710, 20270711, 20270712, 20270713, 20270714)
    assert VALIDATION_REPLICATES_PER_SEED == 20
    assert RELATIVE_DECLINE_FRACTIONS == (0.05, 0.10, 0.20)
    assert len(domains) * len(VALIDATION_MASTER_SEEDS) * VALIDATION_REPLICATES_PER_SEED == 200


def test_protocol003_stage3_domains_match_confirmation() -> None:
    domains = protocol003_validation_domains()
    assert domains[0].label == "symmetric_bridge"
    assert domains[0].hold_generations == 210
    assert domains[0].normalised_barrier_increase == 0.20
    assert domains[1].label == "transition"
    assert domains[1].hold_generations == 90
    assert domains[1].normalised_barrier_increase == 0.10
