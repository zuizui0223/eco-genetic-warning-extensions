from random import Random

from eco_genetic_warning_extensions.process_resolved_movement import (
    mix_frequency_by_realised_flux,
    move_trait_abundance,
    uniform_other_patch_flux,
    validate_individual_dispersal_rate,
)
from eco_genetic_warning_extensions.process_resolved_movement_phase_r import (
    PHASE_R_CONDITIONS,
    PHASE_R_INDIVIDUAL_DISPERSAL_RATE,
    PHASE_R_LEGACY_MIGRATION_RATE,
    PHASE_R_PHASE_M_BLOCKS,
    PHASE_R_REPLICATES_PER_SEED,
    phase_r_manifest,
)


def test_rate_and_manifest_are_predeclared_once() -> None:
    assert validate_individual_dispersal_rate(0.10) == 0.10
    assert PHASE_R_INDIVIDUAL_DISPERSAL_RATE == 0.10
    assert PHASE_R_LEGACY_MIGRATION_RATE == 0.10
    assert PHASE_R_REPLICATES_PER_SEED == 100
    assert PHASE_R_CONDITIONS == (
        "no_connectivity",
        "allele_only_m010",
        "individual_dispersal_d010",
    )
    manifest = phase_r_manifest()
    assert manifest["process_resolved_condition"]["legacy_migration_rate"] == 0.0
    assert manifest["process_resolved_condition"]["nominal_rate_equivalence_claimed"] is False
    assert "Do not add movement rates" in manifest["stop_rule"]


def test_locked_phase_m_comparators_are_exact() -> None:
    assert PHASE_R_PHASE_M_BLOCKS["no_connectivity"] == (
        (47, 88), (48, 89), (58, 93), (46, 86), (51, 91)
    )
    assert PHASE_R_PHASE_M_BLOCKS["allele_only_m010"] == (
        (45, 88), (48, 89), (66, 93), (42, 86), (48, 91)
    )


def test_zero_rate_has_zero_flux() -> None:
    flux = uniform_other_patch_flux((20, 30, 40, 50), 0.0, Random(1))
    assert flux == ((0, 0, 0, 0),) * 4


def test_flux_retains_one_individual_and_has_zero_diagonal() -> None:
    population = (12, 9, 15, 10)
    flux = uniform_other_patch_flux(population, 1.0, Random(5))
    for source, size in enumerate(population):
        assert flux[source][source] == 0
        assert sum(flux[source]) == size - 1


def test_trait_movement_conserves_metapopulation_and_follows_flux() -> None:
    abundance = (
        (8, 2, 0),
        (0, 6, 4),
        (3, 3, 4),
    )
    flux = (
        (0, 2, 1),
        (1, 0, 2),
        (2, 1, 0),
    )
    moved, population = move_trait_abundance(abundance, flux, Random(17))
    assert sum(population) == sum(sum(row) for row in abundance)
    assert tuple(sum(row) for row in moved) == population
    expected = []
    for destination in range(3):
        outbound = sum(flux[destination][other] for other in range(3) if other != destination)
        incoming = sum(flux[source][destination] for source in range(3) if source != destination)
        expected.append(sum(abundance[destination]) - outbound + incoming)
    assert population == tuple(expected)


def test_genetic_mixing_uses_realised_integer_flux() -> None:
    frequencies = (0.2, 0.8)
    population = (10, 10)
    flux = ((0, 2), (1, 0))
    mixed = mix_frequency_by_realised_flux(frequencies, population, flux)
    assert abs(mixed[0] - ((8 * 0.2 + 1 * 0.8) / 9)) < 1e-12
    assert abs(mixed[1] - ((9 * 0.8 + 2 * 0.2) / 11)) < 1e-12
