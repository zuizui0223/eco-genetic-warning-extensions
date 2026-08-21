"""Paired warning-blind pollen-movement Phase I runner."""
from __future__ import annotations

import importlib
import json
from collections import defaultdict
from dataclasses import replace
from math import exp
from pathlib import Path
from random import Random
from typing import Any, Sequence

from .pollen_movement_phase_i import (
    PHASE_I_AREA_REFERENCE,
    PHASE_I_BARRIER_INCREASE,
    PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE,
    PHASE_I_HOLD_GENERATIONS,
    PHASE_I_INTERACTION_KAPPA,
    PHASE_I_MASTER_SEEDS,
    PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_I_POLLEN_POOL_FRACTION,
    PHASE_I_RAMP_GENERATIONS,
    PHASE_I_REPLICATES_PER_SEED,
    phase_i_conditions,
    phase_i_coordinate,
    phase_i_manifest,
    pollen_offspring_frequencies,
)
from .protocol002_calibration import assert_protocol002_blind_calibration_columns
from .protocol002_condition_map import classify_seed_rates
from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS, SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE, UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)


def _assert_blind(value: Any) -> None:
    if isinstance(value, dict):
        assert_protocol002_blind_calibration_columns(value.keys())
        for child in value.values():
            _assert_blind(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            _assert_blind(child)


def simulate_with_pollen_movement(
    mutation_module: Any,
    parameters: Any,
    *,
    mutation_rate: float,
    pollen_pool_fraction: float,
    kernel: str,
    interaction_barrier_schedule: Sequence[float] | None = None,
) -> Any:
    """Run the pinned life cycle with paternal pollen movement replacing legacy mixing."""
    rate = mutation_module.validate_symmetric_allele_mutation_rate(mutation_rate)
    barriers = mutation_module.validate_interaction_barrier_schedule(parameters, interaction_barrier_schedule)
    if parameters.migration_rate != 0.0:
        raise ValueError("pollen-movement closure requires legacy migration_rate=0")

    rng = Random(parameters.random_seed)
    population, interaction, frequency, trait_distribution, trait_abundance = mutation_module._initial_values(parameters)
    snapshots = [
        mutation_module._snapshot(
            0,
            population,
            interaction,
            frequency,
            trait_distribution,
            trait_abundance,
            parameters,
        )
    ]

    for generation in range(1, parameters.generations + 1):
        barrier = parameters.interaction_barrier if barriers is None else barriers[generation - 1]
        current_occupancy = snapshots[-1].trait_occupancy
        current_high_mass = tuple(summary.high_trait_mass for summary in current_occupancy)
        carrying = tuple(parameters.density_capacity * area for area in parameters.patch_areas)
        density = tuple(min(1.0, n / k) for n, k in zip(population, carrying))
        support = tuple(
            mutation_module.interaction_support_signal(q, x_h, p, parameters)
            for q, x_h, p in zip(interaction, current_high_mass, frequency)
        )
        q_next = tuple(
            mutation_module.sigmoid(
                parameters.interaction_feedback
                * ((area / parameters.area_reference) * dens * signal - barrier)
            )
            for area, dens, signal in zip(parameters.patch_areas, density, support)
        )

        selected: list[float] = []
        for q, p in zip(q_next, frequency):
            high_margin = mutation_module.trait_fitness(1.0, q, parameters) - parameters.viability_threshold
            high_fitness = max(1e-12, 1.0 + parameters.selection_strength * high_margin)
            mean_fitness = p * high_fitness + (1.0 - p)
            selected.append(p * high_fitness / mean_fitness)

        weights = tuple(float(n) for n in population)
        offspring = pollen_offspring_frequencies(
            selected,
            weights,
            pollen_pool_fraction=pollen_pool_fraction,
            kernel=kernel,
        )
        mutated = tuple(mutation_module.apply_symmetric_allele_mutation(p, rate) for p in offspring)

        next_population: list[int] = []
        for n, k, q, p in zip(population, carrying, q_next, selected):
            exponent = parameters.baseline_growth + parameters.interaction_growth * q + parameters.high_allele_growth * p - n / k
            next_population.append(max(1, round(n * exp(exponent))))

        if parameters.trait_occupancy_mode == "finite_trait_bin_recruitment":
            next_trait_abundance = tuple(
                mutation_module.update_trait_abundance(abundance, q, p, n_next, parameters, rng)
                for abundance, q, p, n_next in zip(trait_abundance, interaction, frequency, next_population)
            )
            next_trait_distribution = tuple(mutation_module._normalise_distribution(row) for row in next_trait_abundance)
        else:
            next_trait_distribution = tuple(
                mutation_module.update_trait_distribution(mu, q, parameters, p)
                for mu, q, p in zip(trait_distribution, interaction, frequency)
            )
            next_trait_abundance = tuple(
                mutation_module._abundance_from_distribution(distribution, n_next)
                for distribution, n_next in zip(next_trait_distribution, next_population)
            )

        next_frequency: list[float] = []
        for n, q, p in zip(next_population, q_next, mutated):
            n_eff = mutation_module._effective_size(n, q, parameters)
            gene_copies = max(2, round(2.0 * n_eff))
            next_frequency.append(mutation_module._binomial(rng, gene_copies, p) / gene_copies)

        population = tuple(next_population)
        interaction = q_next
        frequency = tuple(next_frequency)
        trait_distribution = next_trait_distribution
        trait_abundance = next_trait_abundance
        snapshots.append(
            mutation_module._snapshot(
                generation,
                population,
                interaction,
                frequency,
                trait_distribution,
                trait_abundance,
                parameters,
            )
        )

    return mutation_module.SimulationResult(parameters, tuple(snapshots))


def _run_condition(
    condition: Any,
    *,
    mutation_module: Any,
    projected_zero: Any,
    projected_legacy: Any,
    total_generations: int,
    driver_rate: float,
    barriers: Sequence[float],
    seed: int,
) -> Any:
    if condition.operator == "legacy_global_mixing":
        return mutation_module.simulate_with_symmetric_allele_mutation(
            replace(projected_legacy, generations=total_generations, random_seed=seed),
            mutation_rate=driver_rate,
            interaction_barrier_schedule=barriers,
        )
    if condition.operator == "none":
        return mutation_module.simulate_with_symmetric_allele_mutation(
            replace(projected_zero, generations=total_generations, random_seed=seed),
            mutation_rate=driver_rate,
            interaction_barrier_schedule=barriers,
        )
    kernel = "regional" if condition.operator == "regional_pollen" else "ring"
    return simulate_with_pollen_movement(
        mutation_module,
        replace(projected_zero, generations=total_generations, random_seed=seed),
        mutation_rate=driver_rate,
        pollen_pool_fraction=condition.pollen_pool_fraction,
        kernel=kernel,
        interaction_barrier_schedule=barriers,
    )


def run_phase_i(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = phase_i_coordinate()
    conditions = phase_i_conditions()
    driver_rate = coordinate.kappa_mu / 2.0
    total_generations = PHASE_I_RAMP_GENERATIONS + PHASE_I_HOLD_GENERATIONS
    attempts: list[dict[str, Any]] = []
    source_preparation_count = 0
    equivalence_pair_count = 0
    equivalence_mismatch_count = 0

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        chain = runtime.chain

        deterioration = calibration.RampHoldSchedule(
            PHASE_I_RAMP_GENERATIONS,
            PHASE_I_HOLD_GENERATIONS,
            PHASE_I_BARRIER_INCREASE,
        )

        for master_seed in PHASE_I_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id="pollen_movement_phase_i",
                generations=1,
                replicates=PHASE_I_REPLICATES_PER_SEED,
                master_seed=master_seed,
                area_reference_values=(PHASE_I_AREA_REFERENCE,),
                interaction_feedback_values=(PHASE_I_INTERACTION_KAPPA,),
                interaction_barrier_values=(0.5,),
            )

            with patched_protocol002_mutation_runner(mutation, coordinate):
                cells = audit.run_finite_h1_boundary_resolution_audit(
                    spec,
                    endpoint_padding_fraction=0.5,
                    stage_generations=SOURCE_STAGE_GENERATIONS,
                    nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,
                    interaction_separation_threshold=0.05,
                    maximum_normalized_bracket_width=0.03,
                )
                if len(cells) != 1:
                    raise RuntimeError("Phase I must return exactly one H1 cell per master seed")
                cell = cells[0]
                isolated = experiments.scenario_equal_isolated(spec)
                scenario_zero = experiments.LandscapeScenario(
                    scenario_id="equal_fragmented_pollen_phase_i_zero",
                    patch_areas=isolated.patch_areas,
                    migration_rate=0.0,
                )
                scenario_legacy = experiments.LandscapeScenario(
                    scenario_id="equal_fragmented_pollen_phase_i_legacy_m010",
                    patch_areas=isolated.patch_areas,
                    migration_rate=PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE,
                )

                for record in cell.replicates:
                    source_preparation_count += 1
                    source_base: dict[str, Any] = {
                        "kappa_mu": coordinate.kappa_mu,
                        "p_star": coordinate.p_star,
                        "area_reference": PHASE_I_AREA_REFERENCE,
                        "kappa": PHASE_I_INTERACTION_KAPPA,
                        "ramp_generations": PHASE_I_RAMP_GENERATIONS,
                        "hold_generations": PHASE_I_HOLD_GENERATIONS,
                        "horizon": total_generations,
                        "normalised_barrier_increase": PHASE_I_BARRIER_INCREASE,
                        "master_seed": master_seed,
                        "replicate": record.replicate_index,
                        "calibration_seed": record.seed,
                        "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                    }
                    prepared = chain._prepare_mutation_high_state(
                        driver_rate,
                        spec,
                        cell,
                        record,
                        endpoint_padding_fraction=0.5,
                        stage_generations=SOURCE_STAGE_GENERATIONS,
                        hold_generations=SOURCE_HOLD_GENERATIONS,
                        interaction_separation_threshold=0.05,
                    )

                    if prepared is None:
                        for condition in conditions:
                            attempts.append({
                                **source_base,
                                **condition.identity(),
                                "status": "source_preparation_failed",
                                "source_prepared": False,
                                "projection_supported": None,
                                "baseline_realised_high_trait_present": None,
                                "eligible_for_trait_loss_denominator": False,
                                "trait_loss_time_post_baseline": None,
                                "trait_loss_observed_post_baseline": None,
                                "regional_legacy_equivalence_exact": None,
                            })
                        continue

                    source, anchor_barrier = prepared
                    interval = cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1] <= interval[0]:
                        raise RuntimeError("prepared Phase-I source requires a positive canonical interval")
                    interval_width = interval[1] - interval[0]
                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor_barrier,
                        canonical_interval_width=interval_width,
                        schedule=deterioration,
                    )
                    template_zero = chain.parameters_for_cell(
                        spec,
                        scenario_zero,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    template_legacy = chain.parameters_for_cell(
                        spec,
                        scenario_legacy,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    projected_zero, inv_zero = chain.project_full_state(source, template_zero)
                    projected_legacy, inv_legacy = chain.project_full_state(source, template_legacy)
                    projection_supported = bool(inv_zero.projection_supported and inv_legacy.projection_supported)

                    if not projection_supported:
                        for condition in conditions:
                            attempts.append({
                                **source_base,
                                **condition.identity(),
                                "status": "projection_failed",
                                "source_prepared": True,
                                "projection_supported": False,
                                "baseline_realised_high_trait_present": None,
                                "eligible_for_trait_loss_denominator": False,
                                "trait_loss_time_post_baseline": None,
                                "trait_loss_observed_post_baseline": None,
                                "regional_legacy_equivalence_exact": None,
                            })
                        continue

                    results = {
                        condition.name: _run_condition(
                            condition,
                            mutation_module=mutation,
                            projected_zero=projected_zero,
                            projected_legacy=projected_legacy,
                            total_generations=total_generations,
                            driver_rate=driver_rate,
                            barriers=barriers,
                            seed=record.seed,
                        )
                        for condition in conditions
                    }
                    regional = results["regional_pollen_pool_g020"]
                    legacy = results["legacy_allele_mixing_m010"]
                    equivalence_pair_count += 1
                    equivalence_exact = regional.snapshots == legacy.snapshots
                    if not equivalence_exact:
                        equivalence_mismatch_count += 1

                    for condition in conditions:
                        result = results[condition.name]
                        baseline_present = any(
                            item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy
                        )
                        raw_loss_time = dynamics.tau_trait_realised(result)
                        loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                        attempts.append({
                            **source_base,
                            **condition.identity(),
                            "status": "completed",
                            "source_prepared": True,
                            "projection_supported": True,
                            "baseline_realised_high_trait_present": baseline_present,
                            "eligible_for_trait_loss_denominator": bool(baseline_present),
                            "trait_loss_time_post_baseline": loss_time,
                            "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                            "regional_legacy_equivalence_exact": equivalence_exact
                            if condition.name in {"regional_pollen_pool_g020", "legacy_allele_mixing_m010"}
                            else None,
                        })

    artifact = _build_artifact(
        attempts,
        source_preparation_count,
        equivalence_pair_count=equivalence_pair_count,
        equivalence_mismatch_count=equivalence_mismatch_count,
    )
    _assert_blind(artifact)
    return artifact


def _regime_for_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], float | None, bool, str]:
    seed_blocks: list[dict[str, Any]] = []
    rates: list[float] = []
    sufficient = True
    for seed in PHASE_I_MASTER_SEEDS:
        seed_rows = [row for row in rows if row["master_seed"] == seed and row["eligible_for_trait_loss_denominator"]]
        seed_losses = [row for row in seed_rows if row["trait_loss_observed_post_baseline"] is True]
        if len(seed_rows) < PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED:
            sufficient = False
        rate = None if not seed_rows else len(seed_losses) / len(seed_rows)
        seed_blocks.append({
            "master_seed": seed,
            "baseline_eligible_count": len(seed_rows),
            "trait_loss_count": len(seed_losses),
            "trait_loss_rate": rate,
        })
        if rate is not None:
            rates.append(rate)
    eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
    losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
    pooled = None if not eligible else len(losses) / len(eligible)
    if not sufficient or len(rates) != len(PHASE_I_MASTER_SEEDS):
        regime = "insufficient_highrep_support"
    else:
        base_regime = classify_seed_rates(tuple(rates))
        regime = {
            "warning_evaluable": "R4_highrep",
            "rapid_loss": "R2_highrep",
            "persistence": "R1_highrep",
            "seed_heterogeneous": "R3_highrep",
        }[base_regime]
    return seed_blocks, pooled, sufficient, regime


def _paired_switches(reference_rows: list[dict[str, Any]], comparison_rows: list[dict[str, Any]], reference: str, comparison: str) -> dict[str, Any]:
    indexed = {(row["master_seed"], row["replicate"]): row for row in reference_rows}
    counts = {"comparable_pair_count": 0, "loss_to_no_loss": 0, "no_loss_to_loss": 0, "same_loss": 0, "same_no_loss": 0}
    for row in comparison_rows:
        ref = indexed[(row["master_seed"], row["replicate"])]
        if not (row["eligible_for_trait_loss_denominator"] and ref["eligible_for_trait_loss_denominator"]):
            continue
        counts["comparable_pair_count"] += 1
        ref_loss = ref["trait_loss_observed_post_baseline"] is True
        new_loss = row["trait_loss_observed_post_baseline"] is True
        if ref_loss and not new_loss:
            counts["loss_to_no_loss"] += 1
        elif not ref_loss and new_loss:
            counts["no_loss_to_loss"] += 1
        elif ref_loss and new_loss:
            counts["same_loss"] += 1
        else:
            counts["same_no_loss"] += 1
    return {"reference": reference, "comparison": comparison, **counts}


def _build_artifact(
    attempts: list[dict[str, Any]],
    source_preparation_count: int,
    *,
    equivalence_pair_count: int,
    equivalence_mismatch_count: int,
) -> dict[str, Any]:
    expected_sources = len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED
    expected_rows = expected_sources * len(phase_i_conditions())
    if source_preparation_count != expected_sources:
        raise RuntimeError(f"Phase I must attempt {expected_sources} source preparations")
    if len(attempts) != expected_rows:
        raise RuntimeError(f"Phase I must retain {expected_rows} movement-condition rows")

    by_condition: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in attempts:
        by_condition[str(row["name"])].append(row)

    summaries: list[dict[str, Any]] = []
    for condition in phase_i_conditions():
        rows = by_condition[condition.name]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        seed_blocks, pooled, sufficient, regime = _regime_for_rows(rows)
        summaries.append({
            "movement_condition": condition.name,
            "operator": condition.operator,
            "pollen_pool_fraction": condition.pollen_pool_fraction,
            "legacy_migration_rate": condition.legacy_migration_rate,
            "status_counts": {
                "attempted": len(rows),
                "source_prepared": sum(row["source_prepared"] is True for row in rows),
                "projection_supported": sum(row["projection_supported"] is True for row in rows),
                "baseline_eligible": len(eligible),
                "trait_loss": len(losses),
            },
            "seed_blocks": seed_blocks,
            "pooled_trait_loss_rate": pooled,
            "highrep_support_sufficient": sufficient,
            "regime": regime,
        })

    summary_by_name = {row["movement_condition"]: row for row in summaries}
    no_pollen = summary_by_name["no_pollen_control"]
    regional = summary_by_name["regional_pollen_pool_g020"]
    ring = summary_by_name["ring_pollen_pool_g020"]
    equivalence_exact = equivalence_pair_count > 0 and equivalence_mismatch_count == 0
    opening_rule_satisfied = bool(
        no_pollen["highrep_support_sufficient"]
        and no_pollen["regime"] == "R4_highrep"
        and equivalence_exact
    )
    if not opening_rule_satisfied:
        kernel_comparison = "not_opened"
    elif regional["regime"] == ring["regime"]:
        kernel_comparison = "kernel_same_regime"
    else:
        kernel_comparison = "kernel_changed_regime"

    paired = [
        _paired_switches(
            by_condition["no_pollen_control"],
            by_condition["regional_pollen_pool_g020"],
            "no_pollen_control",
            "regional_pollen_pool_g020",
        ),
        _paired_switches(
            by_condition["regional_pollen_pool_g020"],
            by_condition["ring_pollen_pool_g020"],
            "regional_pollen_pool_g020",
            "ring_pollen_pool_g020",
        ),
    ]

    return {
        "stage": "warning-blind pollen-movement Phase I",
        "calibration_scope": "source_movement_and_trait_loss_only",
        "manifest": phase_i_manifest(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "source_preparation_count": source_preparation_count,
        "regional_legacy_equivalence": {
            "pair_count": equivalence_pair_count,
            "mismatch_count": equivalence_mismatch_count,
            "trajectory_exact": equivalence_exact,
            "pollen_pool_fraction": PHASE_I_POLLEN_POOL_FRACTION,
            "equivalent_legacy_migration_rate": PHASE_I_EQUIVALENT_GLOBAL_MIGRATION_RATE,
        },
        "opening_rule_satisfied": opening_rule_satisfied,
        "kernel_comparison": kernel_comparison,
        "movement_condition_summaries": summaries,
        "paired_loss_status": paired,
        "attempts": attempts,
    }


def write_phase_i(upstream_checkout: str | Path, output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(run_phase_i(upstream_checkout), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
