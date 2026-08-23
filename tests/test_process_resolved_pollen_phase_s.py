from random import Random

from eco_genetic_warning_extensions.process_resolved_pollen import (
    external_pollen_flux,
    validate_pollen_immigration_rate,
    zygotic_frequency_from_pollen_flux,
)
from eco_genetic_warning_extensions.process_resolved_pollen_phase_s import (
    PHASE_S_CONDITIONS,
    PHASE_S_POLLEN_IMMIGRATION_RATE,
    PHASE_S_REPLICATES_PER_SEED,
    phase_s_manifest,
)


def test_phase_s_design_is_fixed() -> None:
    assert PHASE_S_REPLICATES_PER_SEED == 100
    assert PHASE_S_POLLEN_IMMIGRATION_RATE == 0.20
    assert PHASE_S_CONDITIONS == ("no_connectivity", "allele_only_m010", "pollen_only_g020")
    manifest = phase_s_manifest()
    assert manifest["pollen_condition"]["census_moves"] is False
    assert manifest["pollen_condition"]["trait_bins_move"] is False
    assert "paternal gametes contribute one half" in manifest["nominal_match_rationale"]
    assert "Do not tune pollen fractions" in manifest["stop_rule"]


def test_zero_pollen_has_zero_flux_and_local_zygotic_frequency() -> None:
    population = (10, 12, 9, 11)
    frequency = (0.2, 0.4, 0.6, 0.8)
    flux = external_pollen_flux(population, 0.0, Random(1))
    assert flux == ((0, 0, 0, 0),) * 4
    assert zygotic_frequency_from_pollen_flux(frequency, population, flux) == frequency


def test_external_pollen_flux_has_zero_diagonal_and_respects_slots() -> None:
    population = (10, 12, 9, 11)
    flux = external_pollen_flux(population, 1.0, Random(7))
    for destination, slots in enumerate(population):
        assert flux[destination][destination] == 0
        assert sum(flux[source][destination] for source in range(4)) == slots


def test_pollen_zygotic_frequency_uses_local_maternal_half() -> None:
    frequency = (0.2, 0.8)
    population = (10, 10)
    flux = ((0, 10), (10, 0))
    zygotic = zygotic_frequency_from_pollen_flux(frequency, population, flux)
    assert abs(zygotic[0] - 0.5) < 1e-12
    assert abs(zygotic[1] - 0.5) < 1e-12


def test_rate_validation() -> None:
    assert validate_pollen_immigration_rate(0.2) == 0.2
