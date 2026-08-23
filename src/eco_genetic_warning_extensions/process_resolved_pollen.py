"""Process-resolved pollen-only gene flow for the pinned finite life cycle.

The operator moves paternal gametic contribution among patches without moving
census abundance or realised trait-bin abundance.  It is intentionally separate
from both the parent's direct allele-frequency mixing scalar and Phase-R whole-
individual dispersal.

A destination's recruited cohort supplies one paternal slot per recruit.  A
fixed fraction of those paternal slots is assigned to external pollen donors;
donor patches are sampled proportional to their locally recruited census.  The
maternal contribution remains local.  Because paternal alleles comprise one
half of a biparental zygote, pollen immigration g=0.20 has an expected maximum
external genomic contribution of about 0.10 before source weighting.  This is a
mechanistic nominal comparison to legacy m=0.10, not calibrated equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import exp
from random import Random
from typing import Any, Sequence


POLLEN_SEED_OFFSET = 1_711_303


@dataclass(frozen=True)
class PollenDiagnostics:
    immigrant_pollen_by_generation: tuple[int, ...]
    total_immigrant_pollen: int
    total_paternal_slots: int

    @property
    def realised_pollen_immigration_fraction(self) -> float:
        if self.total_paternal_slots <= 0:
            return 0.0
        return self.total_immigrant_pollen / self.total_paternal_slots


@dataclass(frozen=True)
class ProcessResolvedPollenResult:
    simulation: Any
    diagnostics: PollenDiagnostics


def validate_pollen_immigration_rate(rate: float) -> float:
    value = float(rate)
    if not 0.0 <= value <= 1.0:
        raise ValueError("pollen_immigration_rate must lie in [0, 1]")
    return value


def _binomial(rng: Random, trials: int, probability: float) -> int:
    if trials < 0:
        raise ValueError("trials must be nonnegative")
    p = min(1.0, max(0.0, float(probability)))
    return sum(rng.random() < p for _ in range(trials))


def _multinomial(rng: Random, trials: int, weights: Sequence[float]) -> tuple[int, ...]:
    values = tuple(float(value) for value in weights)
    if trials < 0 or any(value < 0.0 for value in values):
        raise ValueError("invalid multinomial arguments")
    total = sum(values)
    if total <= 0.0:
        if trials == 0:
            return tuple(0 for _ in values)
        raise ValueError("donor weights must have positive mass")
    probabilities = tuple(value / total for value in values)
    cumulative = []
    running = 0.0
    for value in probabilities:
        running += value
        cumulative.append(running)
    cumulative[-1] = 1.0
    counts = [0 for _ in probabilities]
    for _ in range(trials):
        draw = rng.random()
        for index, boundary in enumerate(cumulative):
            if draw <= boundary:
                counts[index] += 1
                break
    return tuple(counts)


def external_pollen_flux(
    recruited_population: Sequence[int],
    pollen_immigration_rate: float,
    rng: Random,
) -> tuple[tuple[int, ...], ...]:
    """Draw source→destination counts of external paternal contributions."""
    rate = validate_pollen_immigration_rate(pollen_immigration_rate)
    population = tuple(int(value) for value in recruited_population)
    if not population or any(value < 1 for value in population):
        raise ValueError("recruited_population must contain positive counts")
    patch_count = len(population)
    if patch_count == 1:
        if rate > 0.0:
            raise ValueError("positive external pollen flow requires at least two patches")
        return ((0,),)

    matrix = [[0 for _ in population] for _ in population]
    if rate == 0.0:
        return tuple(tuple(row) for row in matrix)

    for destination, paternal_slots in enumerate(population):
        immigrants = _binomial(rng, paternal_slots, rate)
        sources = [index for index in range(patch_count) if index != destination]
        allocation = _multinomial(rng, immigrants, tuple(population[index] for index in sources))
        for source, count in zip(sources, allocation):
            matrix[source][destination] = count
    return tuple(tuple(row) for row in matrix)


def zygotic_frequency_from_pollen_flux(
    post_selection_frequency: Sequence[float],
    recruited_population: Sequence[int],
    flux: Sequence[Sequence[int]],
) -> tuple[float, ...]:
    """Combine local maternal and realised paternal pollen gene pools."""
    frequencies = tuple(float(value) for value in post_selection_frequency)
    population = tuple(int(value) for value in recruited_population)
    patch_count = len(population)
    if len(frequencies) != patch_count or len(flux) != patch_count or any(len(row) != patch_count for row in flux):
        raise ValueError("frequency, population and pollen flux dimensions must match")
    if any(not 0.0 <= value <= 1.0 for value in frequencies):
        raise ValueError("frequencies must lie in [0, 1]")

    zygotic = []
    for destination, paternal_slots in enumerate(population):
        external = sum(int(flux[source][destination]) for source in range(patch_count) if source != destination)
        if external < 0 or external > paternal_slots:
            raise ValueError("external pollen count must fit paternal slots")
        local_slots = paternal_slots - external
        paternal_numerator = local_slots * frequencies[destination]
        paternal_numerator += sum(
            int(flux[source][destination]) * frequencies[source]
            for source in range(patch_count)
            if source != destination
        )
        paternal_frequency = paternal_numerator / paternal_slots
        maternal_frequency = frequencies[destination]
        zygotic.append(0.5 * (maternal_frequency + paternal_frequency))
    return tuple(zygotic)


def simulate_with_process_resolved_pollen(
    dynamics: Any,
    mutation_module: Any,
    parameters: Any,
    coordinate: Any,
    *,
    pollen_immigration_rate: float,
    interaction_barrier_schedule: Sequence[float] | None = None,
    pollen_seed: int | None = None,
) -> ProcessResolvedPollenResult:
    """Run the finite-bin life cycle with pollen-only paternal gene flow."""
    rate = validate_pollen_immigration_rate(pollen_immigration_rate)
    if float(parameters.migration_rate) != 0.0:
        raise ValueError("process-resolved pollen requires legacy migration_rate=0")
    barriers = mutation_module.validate_interaction_barrier_schedule(parameters, interaction_barrier_schedule)

    rng = Random(parameters.random_seed)
    pollen_rng = Random(int(parameters.random_seed if pollen_seed is None else pollen_seed) + POLLEN_SEED_OFFSET)
    population, interaction, frequency, trait_distribution, trait_abundance = dynamics._initial_values(parameters)
    snapshots = [dynamics._snapshot(0, population, interaction, frequency, trait_distribution, trait_abundance, parameters)]
    immigrants_by_generation: list[int] = []
    paternal_slots_total = 0

    for generation in range(1, parameters.generations + 1):
        barrier = parameters.interaction_barrier if barriers is None else barriers[generation - 1]
        current_occupancy = snapshots[-1].trait_occupancy
        current_high_mass = tuple(summary.high_trait_mass for summary in current_occupancy)
        carrying = tuple(parameters.density_capacity * area for area in parameters.patch_areas)
        density = tuple(min(1.0, n / k) for n, k in zip(population, carrying))
        support = tuple(
            dynamics.interaction_support_signal(q, x_h, p, parameters)
            for q, x_h, p in zip(interaction, current_high_mass, frequency)
        )
        q_next = tuple(
            dynamics.sigmoid(
                parameters.interaction_feedback
                * ((area / parameters.area_reference) * dens * signal - barrier)
            )
            for area, dens, signal in zip(parameters.patch_areas, density, support)
        )

        selected = []
        for q, p in zip(q_next, frequency):
            high_margin = dynamics.trait_fitness(1.0, q, parameters) - parameters.viability_threshold
            high_fitness = max(1e-12, 1.0 + parameters.selection_strength * high_margin)
            mean_fitness = p * high_fitness + (1.0 - p)
            selected.append(p * high_fitness / mean_fitness)
        selected = tuple(selected)

        next_population = []
        for n, k, q, p in zip(population, carrying, q_next, selected):
            exponent = parameters.baseline_growth + parameters.interaction_growth * q + parameters.high_allele_growth * p - n / k
            next_population.append(max(1, round(n * exp(exponent))))
        next_population = tuple(next_population)

        if parameters.trait_occupancy_mode == "finite_trait_bin_recruitment":
            next_trait_abundance = tuple(
                dynamics.update_trait_abundance(abundance, q, p, n_next, parameters, rng)
                for abundance, q, p, n_next in zip(trait_abundance, interaction, frequency, next_population)
            )
            next_trait_distribution = tuple(dynamics._normalise_distribution(row) for row in next_trait_abundance)
        else:
            next_trait_distribution = tuple(
                dynamics.update_trait_distribution(mu, q, parameters, p)
                for mu, q, p in zip(trait_distribution, interaction, frequency)
            )
            next_trait_abundance = tuple(
                dynamics._abundance_from_distribution(distribution, n_next)
                for distribution, n_next in zip(next_trait_distribution, next_population)
            )

        flux = external_pollen_flux(next_population, rate, pollen_rng)
        immigrants = sum(sum(row) for row in flux)
        immigrants_by_generation.append(immigrants)
        paternal_slots_total += sum(next_population)
        zygotic = zygotic_frequency_from_pollen_flux(selected, next_population, flux)
        transitioned = tuple(coordinate.apply(value) for value in zygotic)

        next_frequency = []
        for n, q, p in zip(next_population, q_next, transitioned):
            n_eff = dynamics._effective_size(n, q, parameters)
            gene_copies = max(2, round(2.0 * n_eff))
            next_frequency.append(dynamics._binomial(rng, gene_copies, p) / gene_copies)

        population = next_population
        interaction = q_next
        frequency = tuple(next_frequency)
        trait_distribution = next_trait_distribution
        trait_abundance = next_trait_abundance
        snapshots.append(
            dynamics._snapshot(generation, population, interaction, frequency, trait_distribution, trait_abundance, parameters)
        )

    simulation = dynamics.SimulationResult(parameters, tuple(snapshots))
    diagnostics = PollenDiagnostics(
        immigrant_pollen_by_generation=tuple(immigrants_by_generation),
        total_immigrant_pollen=sum(immigrants_by_generation),
        total_paternal_slots=paternal_slots_total,
    )
    return ProcessResolvedPollenResult(simulation=simulation, diagnostics=diagnostics)
