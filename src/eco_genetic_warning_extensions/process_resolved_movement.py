"""Process-resolved whole-individual dispersal for the pinned finite life cycle.

This extension leaves the pinned parent simulator unchanged.  It copies the
published life-cycle ordering and inserts one explicit movement step after local
recruitment and before recurrent allele-state transition / finite drift.

Moved individuals carry census mass and realised trait-bin abundance exactly.
Their genetic contribution is the source patch's post-selection high-allele
frequency, so migrant gene pools are mixed by realised integer movement fluxes
rather than by the parent's direct allele-frequency convex combination.

The parent model does not track joint genotype-by-trait identities.  Therefore
this closure preserves trait-bin individuals and source genetic composition but
does not claim genotype-trait covariance at the migrant level.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import exp
from random import Random
from typing import Any, Sequence


MOVEMENT_SEED_OFFSET = 907_211


@dataclass(frozen=True)
class MovementDiagnostics:
    per_generation_movers: tuple[int, ...]
    total_movers: int
    total_local_recruits_exposed: int

    @property
    def realised_movement_fraction(self) -> float:
        if self.total_local_recruits_exposed <= 0:
            return 0.0
        return self.total_movers / self.total_local_recruits_exposed


@dataclass(frozen=True)
class ProcessResolvedMovementResult:
    simulation: Any
    diagnostics: MovementDiagnostics


def validate_individual_dispersal_rate(rate: float) -> float:
    value = float(rate)
    if not 0.0 <= value <= 1.0:
        raise ValueError("individual_dispersal_rate must lie in [0, 1]")
    return value


def _binomial(rng: Random, trials: int, probability: float) -> int:
    if trials < 0:
        raise ValueError("trials must be nonnegative")
    p = min(1.0, max(0.0, float(probability)))
    return sum(rng.random() < p for _ in range(trials))


def _multinomial(rng: Random, trials: int, probabilities: Sequence[float]) -> tuple[int, ...]:
    if trials < 0:
        raise ValueError("trials must be nonnegative")
    weights = tuple(float(value) for value in probabilities)
    total = sum(weights)
    if total <= 0.0:
        if trials == 0:
            return tuple(0 for _ in weights)
        raise ValueError("probabilities must have positive mass")
    probs = tuple(value / total for value in weights)
    counts = [0 for _ in probs]
    cumulative = []
    running = 0.0
    for value in probs:
        running += value
        cumulative.append(running)
    cumulative[-1] = 1.0
    for _ in range(trials):
        draw = rng.random()
        for index, boundary in enumerate(cumulative):
            if draw <= boundary:
                counts[index] += 1
                break
    return tuple(counts)


def uniform_other_patch_flux(
    population: Sequence[int],
    dispersal_rate: float,
    rng: Random,
) -> tuple[tuple[int, ...], ...]:
    """Draw an integer source→destination movement matrix.

    Each recruited individual independently emigrates with the declared rate,
    subject to the parent's positive-population convention: at least one local
    recruit is retained in every source patch.  Emigrants choose uniformly among
    the *other* patches.  The diagonal is always zero.
    """
    rate = validate_individual_dispersal_rate(dispersal_rate)
    sizes = tuple(int(value) for value in population)
    if not sizes or any(value < 1 for value in sizes):
        raise ValueError("population must contain positive patch counts")
    patch_count = len(sizes)
    if patch_count == 1:
        if rate > 0.0:
            raise ValueError("positive dispersal requires at least two patches")
        return ((0,),)

    matrix = [[0 for _ in sizes] for _ in sizes]
    if rate == 0.0:
        return tuple(tuple(row) for row in matrix)

    for source, size in enumerate(sizes):
        movers = _binomial(rng, max(0, size - 1), rate)
        destinations = [index for index in range(patch_count) if index != source]
        allocation = _multinomial(rng, movers, (1.0 for _ in destinations))
        for destination, count in zip(destinations, allocation):
            matrix[source][destination] = count
    return tuple(tuple(row) for row in matrix)


def _draw_without_replacement_counts(
    rng: Random,
    counts: Sequence[int],
    draws: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return (drawn, remaining) category counts without replacement."""
    remaining = [int(value) for value in counts]
    if any(value < 0 for value in remaining):
        raise ValueError("counts must be nonnegative")
    total = sum(remaining)
    if not 0 <= draws <= total:
        raise ValueError("draws must lie between zero and total abundance")
    drawn = [0 for _ in remaining]
    for _ in range(draws):
        ticket = rng.randrange(sum(remaining))
        running = 0
        for index, value in enumerate(remaining):
            running += value
            if ticket < running:
                remaining[index] -= 1
                drawn[index] += 1
                break
    return tuple(drawn), tuple(remaining)


def move_trait_abundance(
    trait_abundance: Sequence[Sequence[int]],
    flux: Sequence[Sequence[int]],
    rng: Random,
) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
    """Move realised trait-bin individuals according to a fixed flux matrix."""
    source_rows = tuple(tuple(int(value) for value in row) for row in trait_abundance)
    patch_count = len(source_rows)
    if patch_count == 0 or len(flux) != patch_count:
        raise ValueError("trait_abundance and flux must have matching nonzero patch count")
    bin_count = len(source_rows[0])
    if bin_count == 0 or any(len(row) != bin_count for row in source_rows):
        raise ValueError("all trait-abundance rows must share a nonzero bin count")
    if any(len(row) != patch_count for row in flux):
        raise ValueError("flux must be square")

    residents = [list(row) for row in source_rows]
    incoming = [[0 for _ in range(bin_count)] for _ in range(patch_count)]

    for source in range(patch_count):
        source_total = sum(source_rows[source])
        outbound = sum(int(flux[source][destination]) for destination in range(patch_count) if destination != source)
        if outbound > source_total - 1:
            raise ValueError("flux must retain at least one individual in each source patch")
        remaining = tuple(residents[source])
        for destination in range(patch_count):
            if destination == source:
                if int(flux[source][destination]) != 0:
                    raise ValueError("flux diagonal must be zero")
                continue
            count = int(flux[source][destination])
            if count < 0:
                raise ValueError("flux counts must be nonnegative")
            moved, remaining = _draw_without_replacement_counts(rng, remaining, count)
            for trait_bin, value in enumerate(moved):
                incoming[destination][trait_bin] += value
        residents[source] = list(remaining)

    moved_rows = []
    populations = []
    for patch in range(patch_count):
        row = tuple(residents[patch][trait_bin] + incoming[patch][trait_bin] for trait_bin in range(bin_count))
        if sum(row) < 1:
            raise RuntimeError("process-resolved movement produced an empty patch")
        moved_rows.append(row)
        populations.append(sum(row))

    if sum(populations) != sum(sum(row) for row in source_rows):
        raise RuntimeError("trait movement must conserve metapopulation census")
    return tuple(moved_rows), tuple(populations)


def mix_frequency_by_realised_flux(
    source_frequency: Sequence[float],
    local_population: Sequence[int],
    flux: Sequence[Sequence[int]],
) -> tuple[float, ...]:
    """Mix source post-selection allele frequencies by realised migrant counts."""
    frequencies = tuple(float(value) for value in source_frequency)
    sizes = tuple(int(value) for value in local_population)
    patch_count = len(sizes)
    if len(frequencies) != patch_count or len(flux) != patch_count or any(len(row) != patch_count for row in flux):
        raise ValueError("frequency, population and flux dimensions must match")
    if any(not 0.0 <= value <= 1.0 for value in frequencies):
        raise ValueError("source frequencies must lie in [0, 1]")

    results = []
    for destination in range(patch_count):
        outbound_here = sum(int(flux[destination][other]) for other in range(patch_count) if other != destination)
        resident = sizes[destination] - outbound_here
        incoming = sum(int(flux[source][destination]) for source in range(patch_count) if source != destination)
        denominator = resident + incoming
        if denominator < 1:
            raise RuntimeError("movement produced empty destination gene pool")
        numerator = resident * frequencies[destination]
        numerator += sum(
            int(flux[source][destination]) * frequencies[source]
            for source in range(patch_count)
            if source != destination
        )
        results.append(numerator / denominator)
    return tuple(results)


def simulate_with_process_resolved_dispersal(
    dynamics: Any,
    mutation_module: Any,
    parameters: Any,
    coordinate: Any,
    *,
    dispersal_rate: float,
    interaction_barrier_schedule: Sequence[float] | None = None,
    movement_seed: int | None = None,
) -> ProcessResolvedMovementResult:
    """Run the pinned life cycle with post-recruitment individual dispersal.

    The legacy ``parameters.migration_rate`` must be zero.  This prevents double
    counting allele-only mixing and process-resolved movement.  Recurrent-state
    transition ``coordinate.apply`` occurs after movement-derived genetic mixing
    and before the parent's finite drift draw.
    """
    rate = validate_individual_dispersal_rate(dispersal_rate)
    if float(parameters.migration_rate) != 0.0:
        raise ValueError("process-resolved dispersal requires legacy migration_rate=0")
    barriers = mutation_module.validate_interaction_barrier_schedule(parameters, interaction_barrier_schedule)

    rng = Random(parameters.random_seed)
    mover_seed = int(parameters.random_seed if movement_seed is None else movement_seed) + MOVEMENT_SEED_OFFSET
    movement_rng = Random(mover_seed)
    population, interaction, frequency, trait_distribution, trait_abundance = dynamics._initial_values(parameters)
    snapshots = [dynamics._snapshot(0, population, interaction, frequency, trait_distribution, trait_abundance, parameters)]
    movers_by_generation: list[int] = []
    exposed = 0

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

        local_next_population = []
        for n, k, q, p in zip(population, carrying, q_next, selected):
            exponent = parameters.baseline_growth + parameters.interaction_growth * q + parameters.high_allele_growth * p - n / k
            local_next_population.append(max(1, round(n * exp(exponent))))

        if parameters.trait_occupancy_mode == "finite_trait_bin_recruitment":
            local_trait_abundance = tuple(
                dynamics.update_trait_abundance(abundance, q, p, n_next, parameters, rng)
                for abundance, q, p, n_next in zip(trait_abundance, interaction, frequency, local_next_population)
            )
        else:
            local_trait_distribution = tuple(
                dynamics.update_trait_distribution(mu, q, parameters, p)
                for mu, q, p in zip(trait_distribution, interaction, frequency)
            )
            local_trait_abundance = tuple(
                dynamics._abundance_from_distribution(distribution, n_next)
                for distribution, n_next in zip(local_trait_distribution, local_next_population)
            )

        exposed += sum(local_next_population)
        flux = uniform_other_patch_flux(local_next_population, rate, movement_rng)
        movers = sum(sum(row) for row in flux)
        movers_by_generation.append(movers)
        moved_trait_abundance, moved_population = move_trait_abundance(local_trait_abundance, flux, movement_rng)
        moved_trait_distribution = tuple(dynamics._normalise_distribution(row) for row in moved_trait_abundance)
        movement_mixed = mix_frequency_by_realised_flux(selected, local_next_population, flux)
        transitioned = tuple(coordinate.apply(value) for value in movement_mixed)

        next_frequency = []
        for n, q, p in zip(moved_population, q_next, transitioned):
            n_eff = dynamics._effective_size(n, q, parameters)
            gene_copies = max(2, round(2.0 * n_eff))
            next_frequency.append(dynamics._binomial(rng, gene_copies, p) / gene_copies)

        population = tuple(moved_population)
        interaction = q_next
        frequency = tuple(next_frequency)
        trait_abundance = moved_trait_abundance
        trait_distribution = moved_trait_distribution
        snapshots.append(
            dynamics._snapshot(generation, population, interaction, frequency, trait_distribution, trait_abundance, parameters)
        )

    simulation = dynamics.SimulationResult(parameters, tuple(snapshots))
    diagnostics = MovementDiagnostics(tuple(movers_by_generation), sum(movers_by_generation), exposed)
    return ProcessResolvedMovementResult(simulation=simulation, diagnostics=diagnostics)
