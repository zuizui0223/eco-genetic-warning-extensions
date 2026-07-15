"""Fresh-seed Protocol 003 Stage III relative-warning validation."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any

from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS, SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage0 import UPSTREAM_COMMIT, UPSTREAM_REPOSITORY
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE, UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE, UPSTREAM_H1_MODULE, UPSTREAM_MUTATION_MODULE,
    _upstream_import_path, patched_protocol002_mutation_runner,
)
from .protocol003_confirmation_calibration import protocol003_confirmation_cells

VALIDATION_MASTER_SEEDS = (20270710, 20270711, 20270712, 20270713, 20270714)
VALIDATION_REPLICATES_PER_SEED = 20
RELATIVE_DECLINE_FRACTIONS = (0.05, 0.10, 0.20)
UPSTREAM_WARNING_MODULE = "causal_model.h2_relative_warning_contract"


def protocol003_validation_domains():
    return protocol003_confirmation_cells()


def _classification(comparison: Any) -> str:
    if not comparison.baseline_eligible:
        return "baseline_ineligible"
    if comparison.warning_time is None and comparison.trait_loss_time is None:
        return "both_censored"
    if comparison.warning_time is None:
        return "warning_censored"
    if comparison.trait_loss_time is None:
        return "trait_loss_censored"
    delta = comparison.trait_loss_time - comparison.warning_time
    return "lead" if delta > 0 else "tie" if delta == 0 else "lag"


def run_protocol003_validation_domain(upstream_checkout: str | Path, domain_index: int) -> dict[str, Any]:
    checkout = Path(upstream_checkout)
    domains = protocol003_validation_domains()
    if not 0 <= int(domain_index) < len(domains):
        raise ValueError(f"domain_index must lie in [0, {len(domains)-1}]")
    domain = domains[int(domain_index)]
    coordinate = domain.coordinate
    driver_rate = coordinate.kappa_mu / 2.0
    attempts: list[dict[str, Any]] = []

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        warning = importlib.import_module(UPSTREAM_WARNING_MODULE)
        chain = runtime.chain
        schedule = calibration.RampHoldSchedule(30, domain.hold_generations, domain.normalised_barrier_increase)

        for master_seed in VALIDATION_MASTER_SEEDS:
            spec = replace(
                experiments.standard_profile(),
                experiment_id=f"protocol003_validation_{domain.cell_index:02d}",
                generations=1,
                replicates=VALIDATION_REPLICATES_PER_SEED,
                master_seed=master_seed,
                area_reference_values=(domain.area_reference,),
                interaction_feedback_values=(domain.kappa,),
                interaction_barrier_values=(0.5,),
            )
            with patched_protocol002_mutation_runner(mutation, coordinate):
                h1_cells = audit.run_finite_h1_boundary_resolution_audit(
                    spec, endpoint_padding_fraction=0.5,
                    stage_generations=SOURCE_STAGE_GENERATIONS,
                    nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,
                    interaction_separation_threshold=0.05,
                    maximum_normalized_bracket_width=0.03,
                )
                h1_cell = h1_cells[0]
                isolated = chain._scenario_map(spec)[experiments.SCENARIO_EQUAL_ISOLATED]
                for record in h1_cell.replicates:
                    row: dict[str, Any] = {
                        **domain.identity(), "master_seed": master_seed,
                        "replicate": record.replicate_index, "trajectory_seed": record.seed,
                        "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                    }
                    prepared = chain._prepare_mutation_high_state(
                        driver_rate, spec, h1_cell, record,
                        endpoint_padding_fraction=0.5,
                        stage_generations=SOURCE_STAGE_GENERATIONS,
                        hold_generations=SOURCE_HOLD_GENERATIONS,
                        interaction_separation_threshold=0.05,
                    )
                    if prepared is None:
                        row.update(status="source_preparation_failed", comparisons=[])
                        attempts.append(row); continue
                    source, anchor = prepared
                    interval = h1_cell.canonical_bistable_barrier_interval
                    if interval is None or interval[1] <= interval[0]:
                        raise RuntimeError("positive canonical interval required")
                    template = chain.parameters_for_cell(spec, isolated, replace(h1_cell.parameters, interaction_barrier=anchor), seed=record.seed)
                    projected, invariants = chain.project_full_state(source, template)
                    if not invariants.projection_supported:
                        row.update(status="projection_failed", comparisons=[])
                        attempts.append(row); continue
                    barriers = calibration.ramp_and_hold_barrier_schedule(
                        anchor_barrier=anchor,
                        canonical_interval_width=interval[1]-interval[0],
                        schedule=schedule,
                    )
                    result = mutation.simulate_with_symmetric_allele_mutation(
                        replace(projected, generations=schedule.total_generations, random_seed=record.seed),
                        mutation_rate=driver_rate,
                        interaction_barrier_schedule=barriers,
                    )
                    baseline_present = any(x.realised_high_trait_occupied for x in result.snapshots[0].trait_occupancy)
                    raw_loss = dynamics.tau_trait_realised(result)
                    loss_time = None if raw_loss in (None, 0) else raw_loss
                    comparisons = []
                    for diversity_id, values in (
                        ("H_alpha", [s.h_alpha for s in result.snapshots]),
                        ("H_gamma", [s.h_gamma for s in result.snapshots]),
                    ):
                        for fraction in RELATIVE_DECLINE_FRACTIONS:
                            definition = warning.RelativeWarningDefinition(diversity_id, fraction)
                            comparison = warning.compare_relative_warning(values, trait_loss_time=loss_time, definition=definition)
                            item = comparison.as_dict()
                            item["ordering"] = _classification(comparison)
                            comparisons.append(item)
                    row.update(
                        status="completed",
                        baseline_realised_high_trait_present=baseline_present,
                        trait_loss_time_post_baseline=loss_time,
                        trait_loss_observed_post_baseline=(None if not baseline_present else loss_time is not None),
                        comparisons=comparisons,
                    )
                    attempts.append(row)

    completed = [r for r in attempts if r["status"] == "completed"]
    summary: dict[str, Any] = {}
    for diversity_id in ("H_alpha", "H_gamma"):
        for fraction in RELATIVE_DECLINE_FRACTIONS:
            key = f"{diversity_id}_{fraction:.2f}"
            items = [c for r in completed for c in r["comparisons"] if c["definition"]["diversity_id"] == diversity_id and c["definition"]["relative_decline_fraction"] == fraction]
            counts = {name: sum(c["ordering"] == name for c in items) for name in ("lead","tie","lag","warning_censored","trait_loss_censored","both_censored","baseline_ineligible")}
            lead_times = [c["lead_time_trait_minus_warning"] for c in items if c["ordering"] == "lead"]
            summary[key] = {"counts": counts, "valid_pairs": counts["lead"]+counts["tie"]+counts["lag"], "median_positive_lead_time": None if not lead_times else sorted(lead_times)[len(lead_times)//2]}
    return {
        "stage": "Protocol 003 Stage III fresh-seed warning validation",
        "upstream": {"repository": UPSTREAM_REPOSITORY, "commit": UPSTREAM_COMMIT},
        "domain": domain.identity(),
        "design": {"master_seeds": list(VALIDATION_MASTER_SEEDS), "replicates_per_seed": VALIDATION_REPLICATES_PER_SEED, "relative_decline_fractions": list(RELATIVE_DECLINE_FRACTIONS), "endpoint_family": ["H_alpha","H_gamma"]},
        "status_counts": {"attempted": len(attempts), "completed": len(completed)},
        "endpoint_summary": summary,
        "attempts": attempts,
        "type_s_result_claimed": True,
    }


def write_protocol003_validation_domain(upstream_checkout: str | Path, domain_index: int, output: str | Path) -> Path:
    target = Path(output); target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(run_protocol003_validation_domain(upstream_checkout, domain_index), indent=2, sort_keys=True)+"\n", encoding="utf-8")
    return target
