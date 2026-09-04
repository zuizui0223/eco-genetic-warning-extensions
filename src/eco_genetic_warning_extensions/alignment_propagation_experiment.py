"""Post-Phase-V propagation experiment for cross-layer alignment.

This module deliberately does not modify or import the retired Phase-V runner.
It reconstructs the frozen Phase-V state/dynamics contract from the locked
protocol and extends only two design dimensions declared before this run:

- read the same 40-generation trajectories at horizons 5, 10, 20 and 40;
- increase paired replication through nested 500, 1000 and 1500 pair prefixes.

The future forcing is the original 60-generation linear barrier path truncated
at the requested horizon. Shorter horizons therefore do not accelerate the
forcing schedule.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from math import comb
from pathlib import Path
from typing import Any, Iterable

PROTOCOL_PATH = Path(__file__).resolve().parents[2] / "experiments" / "alignment_propagation_protocol.json"


@dataclass(frozen=True)
class PropagationContract:
    master_seeds: tuple[int, ...]
    horizons: tuple[int, ...]
    nested_replicates_per_seed: tuple[int, ...]
    max_replicates_per_seed: int
    max_horizon: int
    barrier_start: float
    barrier_end_60: float
    reference_generations: int


def load_protocol(path: str | Path = PROTOCOL_PATH) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("status") != "prospective_locked_before_run":
        raise RuntimeError("alignment propagation protocol is not locked-before-run")
    return payload


def contract_from_protocol(protocol: dict[str, Any]) -> PropagationContract:
    forcing = protocol["future_forcing"]
    replication = protocol["paired_replication"]
    state = protocol["state_and_dynamics"]
    return PropagationContract(
        master_seeds=tuple(int(x) for x in state["master_seeds"]),
        horizons=tuple(int(x) for x in forcing["report_horizons"]),
        nested_replicates_per_seed=tuple(int(x) for x in replication["nested_replicates_per_seed"]),
        max_replicates_per_seed=int(replication["replicates_per_seed_max"]),
        max_horizon=int(forcing["maximum_simulated_horizon"]),
        barrier_start=float(forcing["barrier_start"]),
        barrier_end_60=float(forcing["barrier_end_at_generation_60"]),
        reference_generations=int(forcing["reference_schedule_generations"]),
    )


def _trajectory_seed(master_seed: int, replicate: int) -> int:
    """Exact Phase-V seed mapping, extended to additional replicate indices."""
    return (master_seed * 1_000_003 + replicate * 101 + 17) % (2**31 - 1)


def condition_bundle_values(condition: str) -> tuple[float, ...]:
    base = (0.20, 0.40, 0.60, 0.80)
    if condition == "aligned":
        return base
    if condition == "anti_aligned":
        return tuple(reversed(base))
    raise ValueError(f"unknown alignment condition: {condition!r}")


def trait_abundance_rows(condition: str, trait_grid_size: int = 31) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    for fraction in condition_bundle_values(condition):
        high = int(round(40 * fraction))
        low = 40 - high
        row = [0] * trait_grid_size
        row[0] = low
        row[-1] = high
        rows.append(tuple(row))
    return tuple(rows)


def barrier_schedule(max_horizon: int = 40, *, reference_generations: int = 60) -> tuple[float, ...]:
    """Truncate the original Phase-V forcing rate rather than rescaling it."""
    if max_horizon < 1 or max_horizon > reference_generations:
        raise ValueError("max_horizon must be within the reference forcing path")
    start = 0.50
    end = 0.65
    span = end - start
    return tuple(start + span * generation / reference_generations for generation in range(1, max_horizon + 1))


def paired_risk_interval(
    aligned_loss_anti_no: int,
    aligned_no_anti_loss: int,
    n_pairs: int,
    *,
    z: float = 1.96,
) -> dict[str, float]:
    """Paired risk difference and large-sample interval from discordant counts."""
    if n_pairs <= 0:
        raise ValueError("n_pairs must be positive")
    b = int(aligned_no_anti_loss)  # anti-only losses
    c = int(aligned_loss_anti_no)  # aligned-only losses
    diff = (b - c) / n_pairs
    variance_d = (b + c) / n_pairs - diff * diff
    variance_d = max(0.0, variance_d)
    se = math.sqrt(variance_d / n_pairs)
    return {
        "risk_difference_anti_minus_aligned": diff,
        "standard_error": se,
        "ci95_lower": diff - z * se,
        "ci95_upper": diff + z * se,
    }


def _two_sided_binomial_p(a: int, b: int) -> float:
    n = a + b
    if n == 0:
        return 1.0
    k = min(a, b)
    tail = sum(comb(n, i) for i in range(k + 1)) / (2**n)
    return min(1.0, 2.0 * tail)


def approximate_power(
    n_pairs: int,
    *,
    absolute_risk_difference: float = 0.05,
    discordance_probability: float = 0.412,
    z_alpha: float = 1.96,
) -> float:
    """Normal-approximation planning power for a paired risk difference."""
    variance_d = discordance_probability - absolute_risk_difference**2
    if variance_d <= 0:
        raise ValueError("planning variance must be positive")
    se = math.sqrt(variance_d / n_pairs)
    noncentral = absolute_risk_difference / se

    def phi(value: float) -> float:
        return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))

    return phi(-z_alpha - noncentral) + (1.0 - phi(z_alpha - noncentral))


def _dynamics_parameters(condition: str, seed: int, generations: int):
    from causal_model.multipatch_criticality_dynamics import DynamicsParameters

    alpha, beta_trait, gamma = (0.6, 0.3, 0.1)
    bundle = condition_bundle_values(condition)
    return DynamicsParameters(
        patch_areas=(1.0, 1.0, 1.0, 1.0),
        generations=generations,
        initial_population=(40, 40, 40, 40),
        initial_interaction=(0.65, 0.75, 0.85, 0.95),
        initial_high_allele_frequency=bundle,
        initial_trait_abundance=trait_abundance_rows(condition),
        density_capacity=40.0,
        area_reference=1.0,
        interaction_feedback=4.5,
        interaction_barrier=0.50,
        trait_grid_size=31,
        trait_occupancy_mode="finite_trait_bin_recruitment",
        genotype_trait_recruitment="two_kernel_recruitment",
        inheritance_weight=0.5,
        q_feedback_alpha=alpha,
        q_feedback_beta_trait=beta_trait,
        q_feedback_gamma_allele=gamma,
        migration_rate=0.0,
        random_seed=seed,
    )


def _run_one(condition: str, master_seed: int, replicate: int, max_horizon: int) -> dict[str, Any]:
    from causal_model.multipatch_criticality_dynamics import tau_trait_realised
    from causal_model.symmetric_allele_mutation_closure import simulate_with_symmetric_allele_mutation

    seed = _trajectory_seed(master_seed, replicate)
    parameters = _dynamics_parameters(condition, seed, max_horizon)
    result = simulate_with_symmetric_allele_mutation(
        parameters,
        mutation_rate=0.0,
        interaction_barrier_schedule=barrier_schedule(max_horizon),
    )
    baseline = result.snapshots[0]
    if not all(item.realised_high_trait_occupied for item in baseline.trait_occupancy):
        raise RuntimeError("propagation experiment baseline lost realised high trait")
    raw_loss = tau_trait_realised(result)
    loss_time = None if raw_loss in {None, 0} else int(raw_loss)
    return {
        "condition": condition,
        "master_seed": int(master_seed),
        "replicate": int(replicate),
        "trajectory_seed": int(seed),
        "trait_loss_time_post_baseline": loss_time,
    }


def simulate_attempts(protocol: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    protocol = load_protocol() if protocol is None else protocol
    contract = contract_from_protocol(protocol)
    rows: list[dict[str, Any]] = []
    for master_seed in contract.master_seeds:
        for replicate in range(contract.max_replicates_per_seed):
            for condition in ("aligned", "anti_aligned"):
                rows.append(_run_one(condition, master_seed, replicate, contract.max_horizon))
    return rows


def _paired_cell(
    attempts: Iterable[dict[str, Any]],
    *,
    horizon: int,
    replicates_per_seed: int,
    master_seeds: tuple[int, ...],
) -> dict[str, Any]:
    selected = [
        row
        for row in attempts
        if int(row["master_seed"]) in master_seeds and int(row["replicate"]) < replicates_per_seed
    ]
    by_key = {
        (str(row["condition"]), int(row["master_seed"]), int(row["replicate"])): row
        for row in selected
    }
    a_only = 0
    b_only = 0
    same_loss = 0
    same_no_loss = 0
    aligned_loss_count = 0
    anti_loss_count = 0
    for seed in master_seeds:
        for replicate in range(replicates_per_seed):
            aligned = by_key[("aligned", seed, replicate)]
            anti = by_key[("anti_aligned", seed, replicate)]
            a_time = aligned["trait_loss_time_post_baseline"]
            b_time = anti["trait_loss_time_post_baseline"]
            a_loss = a_time is not None and int(a_time) <= horizon
            b_loss = b_time is not None and int(b_time) <= horizon
            aligned_loss_count += int(a_loss)
            anti_loss_count += int(b_loss)
            if a_loss and not b_loss:
                a_only += 1
            elif b_loss and not a_loss:
                b_only += 1
            elif a_loss and b_loss:
                same_loss += 1
            else:
                same_no_loss += 1
    n_pairs = len(master_seeds) * replicates_per_seed
    interval = paired_risk_interval(a_only, b_only, n_pairs)
    return {
        "horizon": int(horizon),
        "replicates_per_seed": int(replicates_per_seed),
        "n_pairs": int(n_pairs),
        "aligned_loss_count": int(aligned_loss_count),
        "anti_aligned_loss_count": int(anti_loss_count),
        "aligned_loss_rate": aligned_loss_count / n_pairs,
        "anti_aligned_loss_rate": anti_loss_count / n_pairs,
        "aligned_loss_anti_no_loss": int(a_only),
        "aligned_no_loss_anti_loss": int(b_only),
        "same_loss": int(same_loss),
        "same_no_loss": int(same_no_loss),
        "discordance_rate": (a_only + b_only) / n_pairs,
        "mcnemar_exact_p": _two_sided_binomial_p(a_only, b_only),
        **interval,
    }


def summarise_attempts(
    attempts: list[dict[str, Any]],
    protocol: dict[str, Any] | None = None,
) -> dict[str, Any]:
    protocol = load_protocol() if protocol is None else protocol
    contract = contract_from_protocol(protocol)
    cells = [
        _paired_cell(
            attempts,
            horizon=horizon,
            replicates_per_seed=reps,
            master_seeds=contract.master_seeds,
        )
        for horizon in contract.horizons
        for reps in contract.nested_replicates_per_seed
    ]
    primary_n = len(contract.master_seeds) * contract.max_replicates_per_seed
    primary_cells = [cell for cell in cells if cell["n_pairs"] == primary_n]
    return {
        "experiment_id": protocol["experiment_id"],
        "status": "completed_post_phase_v_propagation_experiment",
        "legacy_phase_v_unchanged": True,
        "horizons": list(contract.horizons),
        "nested_total_pairs": [len(contract.master_seeds) * r for r in contract.nested_replicates_per_seed],
        "primary_pair_count": primary_n,
        "planning_power": {
            str(n): approximate_power(n)
            for n in [len(contract.master_seeds) * r for r in contract.nested_replicates_per_seed]
        },
        "cells": cells,
        "primary_horizon_cells": primary_cells,
        "interpretation_rule": protocol["decision_language"],
    }


def run_experiment(protocol: dict[str, Any] | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    protocol = load_protocol() if protocol is None else protocol
    attempts = simulate_attempts(protocol)
    summary = summarise_attempts(attempts, protocol)
    return summary, attempts


def write_experiment(
    summary_path: str | Path,
    attempts_path: str | Path,
) -> tuple[Path, Path]:
    summary, attempts = run_experiment()
    summary_dest = Path(summary_path)
    attempts_dest = Path(attempts_path)
    summary_dest.parent.mkdir(parents=True, exist_ok=True)
    attempts_dest.parent.mkdir(parents=True, exist_ok=True)
    summary_dest.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    attempts_dest.write_text(json.dumps(attempts, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary_dest, attempts_dest
