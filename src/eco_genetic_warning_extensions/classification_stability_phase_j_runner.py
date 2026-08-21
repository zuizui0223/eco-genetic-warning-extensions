"""Warning-blind fixed-condition ensemble-stability Phase J runner."""
from __future__ import annotations

import importlib
import json
from collections import Counter
from dataclasses import replace
from pathlib import Path
from statistics import mean, median
from typing import Any

from .classification_stability_phase_j import (
    PHASE_J_AREA_REFERENCE,
    PHASE_J_BARRIER_INCREASE,
    PHASE_J_HOLD_GENERATIONS,
    PHASE_J_INTERACTION_KAPPA,
    PHASE_J_MASTER_SEEDS,
    PHASE_J_MIGRATION_RATE,
    PHASE_J_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_J_RAMP_GENERATIONS,
    PHASE_J_REPLICATES_PER_SEED,
    phase_j_coordinate,
    phase_j_manifest,
    phase_j_panels,
)
from .protocol002_calibration import (
    ELIGIBLE_TRAIT_LOSS_RATE_MAX,
    ELIGIBLE_TRAIT_LOSS_RATE_MIN,
    assert_protocol002_blind_calibration_columns,
)
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


def _named_regime(seed_rates: tuple[float, ...]) -> str:
    base = classify_seed_rates(seed_rates)
    return {
        "warning_evaluable": "R4_highrep",
        "rapid_loss": "R2_highrep",
        "persistence": "R1_highrep",
        "seed_heterogeneous": "R3_highrep",
    }[base]


def run_phase_j(upstream_checkout: str | Path) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = phase_j_coordinate()
    driver_rate = coordinate.kappa_mu / 2.0
    total_generations = PHASE_J_RAMP_GENERATIONS + PHASE_J_HOLD_GENERATIONS
    attempts: list[dict[str, Any]] = []
    source_preparation_count = 0

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        chain = runtime.chain

        deterioration = calibration.RampHoldSchedule(
            PHASE_J_RAMP_GENERATIONS,
            PHASE_J_HOLD_GENERATIONS,
            PHASE_J_BARRIER_INCREASE,
        )

        for master_seed in PHASE_J_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id="classification_stability_phase_j",
                generations=1,
                replicates=PHASE_J_REPLICATES_PER_SEED,
                master_seed=master_seed,
                area_reference_values=(PHASE_J_AREA_REFERENCE,),
                interaction_feedback_values=(PHASE_J_INTERACTION_KAPPA,),
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
                    raise RuntimeError("Phase J must return exactly one H1 cell per master seed")
                cell = cells[0]
                isolated = experiments.scenario_equal_isolated(spec)
                scenario = experiments.LandscapeScenario(
                    scenario_id="equal_fragmented_classification_stability_phase_j",
                    patch_areas=isolated.patch_areas,
                    migration_rate=PHASE_J_MIGRATION_RATE,
                )

                for record in cell.replicates:
                    source_preparation_count += 1
                    base: dict[str, Any] = {
                        "kappa_mu": coordinate.kappa_mu,
                        "p_star": coordinate.p_star,
                        "area_reference": PHASE_J_AREA_REFERENCE,
                        "kappa": PHASE_J_INTERACTION_KAPPA,
                        "migration_rate": PHASE_J_MIGRATION_RATE,
                        "ramp_generations": PHASE_J_RAMP_GENERATIONS,
                        "hold_generations": PHASE_J_HOLD_GENERATIONS,
                        "horizon": total_generations,
                        "normalised_barrier_increase": PHASE_J_BARRIER_INCREASE,
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
                        attempts.append({
                            **base,
                            "status": "source_preparation_failed",
                            "source_prepared": False,
                            "projection_supported": None,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                        continue

                    source, anchor_barrier = prepared
                    interval = cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1] <= interval[0]:
                        raise RuntimeError("prepared Phase-J source requires a positive canonical interval")
                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor_barrier,
                        canonical_interval_width=interval[1] - interval[0],
                        schedule=deterioration,
                    )
                    template = chain.parameters_for_cell(
                        spec,
                        scenario,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)
                    if not invariants.projection_supported:
                        attempts.append({
                            **base,
                            "status": "projection_failed",
                            "source_prepared": True,
                            "projection_supported": False,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                        continue

                    result = mutation.simulate_with_symmetric_allele_mutation(
                        replace(projected, generations=total_generations, random_seed=record.seed),
                        mutation_rate=driver_rate,
                        interaction_barrier_schedule=barriers,
                    )
                    baseline_present = any(
                        item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy
                    )
                    raw_loss_time = dynamics.tau_trait_realised(result)
                    loss_time = None if raw_loss_time is None or raw_loss_time == 0 else raw_loss_time
                    attempts.append({
                        **base,
                        "status": "completed",
                        "source_prepared": True,
                        "projection_supported": True,
                        "baseline_realised_high_trait_present": baseline_present,
                        "eligible_for_trait_loss_denominator": bool(baseline_present),
                        "trait_loss_time_post_baseline": loss_time,
                        "trait_loss_observed_post_baseline": None if not baseline_present else loss_time is not None,
                    })

    artifact = _build_artifact(attempts, source_preparation_count)
    _assert_blind(artifact)
    return artifact


def _build_artifact(attempts: list[dict[str, Any]], source_preparation_count: int) -> dict[str, Any]:
    expected = len(PHASE_J_MASTER_SEEDS) * PHASE_J_REPLICATES_PER_SEED
    if source_preparation_count != expected or len(attempts) != expected:
        raise RuntimeError("Phase J must retain exactly one row per attempted source")

    blocks: list[dict[str, Any]] = []
    rate_by_seed: dict[int, float] = {}
    sufficient = True
    for seed in PHASE_J_MASTER_SEEDS:
        rows = [row for row in attempts if row["master_seed"] == seed]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        if len(eligible) < PHASE_J_MIN_BASELINE_ELIGIBLE_PER_SEED:
            sufficient = False
        rate = None if not eligible else len(losses) / len(eligible)
        if rate is not None:
            rate_by_seed[seed] = rate
        blocks.append({
            "master_seed": seed,
            "attempted_count": len(rows),
            "source_prepared_count": sum(row["source_prepared"] is True for row in rows),
            "projection_supported_count": sum(row["projection_supported"] is True for row in rows),
            "baseline_eligible_count": len(eligible),
            "trait_loss_count": len(losses),
            "trait_loss_rate": rate,
            "inside_R4_band": None if rate is None else ELIGIBLE_TRAIT_LOSS_RATE_MIN <= rate <= ELIGIBLE_TRAIT_LOSS_RATE_MAX,
        })

    panels: list[dict[str, Any]] = []
    for panel_index, panel in enumerate(phase_j_panels(), start=1):
        rates = tuple(rate_by_seed[seed] for seed in panel if seed in rate_by_seed)
        panel_sufficient = len(rates) == len(panel) and all(
            next(block["baseline_eligible_count"] for block in blocks if block["master_seed"] == seed)
            >= PHASE_J_MIN_BASELINE_ELIGIBLE_PER_SEED
            for seed in panel
        )
        regime = "insufficient_highrep_support" if not panel_sufficient else _named_regime(rates)
        panels.append({
            "panel_index": panel_index,
            "master_seeds": list(panel),
            "seed_block_trait_loss_rates": list(rates),
            "regime": regime,
        })

    panel_regimes = [panel["regime"] for panel in panels]
    if not sufficient or any(regime == "insufficient_highrep_support" for regime in panel_regimes):
        stability = "insufficient_support"
    elif len(set(panel_regimes)) == 1:
        stability = f"stable_{panel_regimes[0]}"
    else:
        stability = "ensemble_sensitive"

    rates = list(rate_by_seed.values())
    regime_counts = Counter(panel_regimes)
    return {
        "stage": "warning-blind R4 classification-stability Phase J",
        "calibration_scope": "source_and_trait_loss_only",
        "manifest": phase_j_manifest(),
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "source_preparation_count": source_preparation_count,
        "opening_rule_satisfied": sufficient,
        "stability_classification": stability,
        "seed_blocks": blocks,
        "panels": panels,
        "panel_regime_counts": dict(sorted(regime_counts.items())),
        "twenty_seed_diagnostics": {
            "seed_block_count": len(rates),
            "inside_R4_band_count": sum(ELIGIBLE_TRAIT_LOSS_RATE_MIN <= rate <= ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in rates),
            "below_R4_band_count": sum(rate < ELIGIBLE_TRAIT_LOSS_RATE_MIN for rate in rates),
            "above_R4_band_count": sum(rate > ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in rates),
            "minimum_trait_loss_rate": min(rates) if rates else None,
            "maximum_trait_loss_rate": max(rates) if rates else None,
            "mean_trait_loss_rate": mean(rates) if rates else None,
            "median_trait_loss_rate": median(rates) if rates else None,
        },
        "attempts": attempts,
    }


def write_phase_j(upstream_checkout: str | Path, output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(run_phase_j(upstream_checkout), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
