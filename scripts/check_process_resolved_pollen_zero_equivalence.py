from contextlib import contextmanager
from dataclasses import replace

from causal_model import multipatch_criticality_dynamics as dynamics
from causal_model import multipatch_criticality_experiments as experiments
from causal_model import symmetric_allele_mutation_closure as mutation

from eco_genetic_warning_extensions.mutation_coordinates import MutationCoordinates
from eco_genetic_warning_extensions.process_resolved_pollen import simulate_with_process_resolved_pollen


@contextmanager
def patched_coordinate(coordinate: MutationCoordinates):
    original = mutation.apply_symmetric_allele_mutation

    def transform(frequency: float, _rate: float) -> float:
        return coordinate.apply(frequency)

    mutation.apply_symmetric_allele_mutation = transform
    try:
        yield
    finally:
        mutation.apply_symmetric_allele_mutation = original


def main() -> None:
    coordinate = MutationCoordinates(kappa_mu=0.35, p_star=0.35)
    parameters = replace(
        experiments.standard_profile().base_parameters,
        patch_areas=(0.25, 0.25, 0.25, 0.25),
        generations=8,
        initial_population=(18, 17, 19, 16),
        initial_interaction=(0.72, 0.68, 0.70, 0.66),
        initial_high_allele_frequency=(0.73, 0.62, 0.67, 0.58),
        interaction_feedback=4.5,
        area_reference=1.0,
        migration_rate=0.0,
        random_seed=55103,
    )
    driver_rate = coordinate.kappa_mu / 2.0
    with patched_coordinate(coordinate):
        legacy = mutation.simulate_with_symmetric_allele_mutation(parameters, mutation_rate=driver_rate)
    pollen = simulate_with_process_resolved_pollen(
        dynamics,
        mutation,
        parameters,
        coordinate,
        pollen_immigration_rate=0.0,
        pollen_seed=parameters.random_seed,
    )
    if pollen.diagnostics.total_immigrant_pollen != 0:
        raise SystemExit("zero pollen flow unexpectedly generated immigrants")
    if pollen.simulation.snapshots != legacy.snapshots:
        raise SystemExit("zero-pollen closure does not reproduce pinned finite-bin parent life cycle")
    print("PHASE_S_ZERO_POLLEN_EQUIVALENCE_PASS")


if __name__ == "__main__":
    main()
