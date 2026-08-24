"""Execute the preregistered warning-blind Phase-V alignment contrast."""
from __future__ import annotations

import json
from dataclasses import replace
from math import comb
from pathlib import Path
from typing import Any

from .cross_layer_alignment_phase_v import (
    PHASE_V_ALPHA,
    PHASE_V_AREA_REFERENCE,
    PHASE_V_CONDITIONS,
    PHASE_V_DENSITY_CAPACITY,
    PHASE_V_GENERATIONS,
    PHASE_V_INTERACTION_FEEDBACK,
    PHASE_V_MASTER_SEEDS,
    PHASE_V_PATCH_AREAS,
    PHASE_V_POPULATION,
    PHASE_V_Q_FEEDBACK,
    PHASE_V_Q_VALUES,
    PHASE_V_REPLICATES_PER_SEED,
    PHASE_V_TRAIT_GRID_SIZE,
    barrier_schedule,
    baseline_signature,
    condition_bundle_values,
    one_step_state_sufficiency_certificate,
    phase_v_manifest,
    signatures_match,
    trait_abundance_rows,
)

UPSTREAM_SCIENTIFIC_COMMIT = "dd8ee379d0d3518194c767d16402042525bc00dc"


def _trajectory_seed(master_seed: int, replicate: int) -> int:
    return (master_seed * 1_000_003 + replicate * 101 + 17) % (2**31 - 1)


def _two_sided_binomial_p(a: int, b: int) -> float:
    n = a + b
    if n == 0:
        return 1.0
    k = min(a, b)
    tail = sum(comb(n, i) for i in range(k + 1)) / (2**n)
    return min(1.0, 2.0 * tail)


def _parameters(condition: str, seed: int):
    from causal_model.multipatch_criticality_dynamics import DynamicsParameters

    alpha, beta_trait, gamma = PHASE_V_Q_FEEDBACK
    bundle = condition_bundle_values(condition)
    return DynamicsParameters(
        patch_areas=PHASE_V_PATCH_AREAS,
        generations=PHASE_V_GENERATIONS,
        initial_population=PHASE_V_POPULATION,
        initial_interaction=PHASE_V_Q_VALUES,
        initial_high_allele_frequency=bundle,
        initial_trait_abundance=trait_abundance_rows(condition),
        density_capacity=PHASE_V_DENSITY_CAPACITY,
        area_reference=PHASE_V_AREA_REFERENCE,
        interaction_feedback=PHASE_V_INTERACTION_FEEDBACK,
        interaction_barrier=0.50,
        trait_grid_size=PHASE_V_TRAIT_GRID_SIZE,
        trait_occupancy_mode="finite_trait_bin_recruitment",
        genotype_trait_recruitment="two_kernel_recruitment",
        inheritance_weight=0.5,
        q_feedback_alpha=alpha,
        q_feedback_beta_trait=beta_trait,
        q_feedback_gamma_allele=gamma,
        migration_rate=0.0,
        random_seed=seed,
    )


def _run_one(condition: str, master_seed: int, replicate: int) -> dict[str, Any]:
    from causal_model.multipatch_criticality_dynamics import tau_trait_realised
    from causal_model.symmetric_allele_mutation_closure import simulate_with_symmetric_allele_mutation

    seed = _trajectory_seed(master_seed, replicate)
    parameters = _parameters(condition, seed)
    result = simulate_with_symmetric_allele_mutation(
        parameters,
        mutation_rate=0.0,
        interaction_barrier_schedule=barrier_schedule(),
    )
    baseline = result.snapshots[0]
    baseline_present = all(item.realised_high_trait_occupied for item in baseline.trait_occupancy)
    raw_loss = tau_trait_realised(result)
    loss_time = None if raw_loss in {None, 0} else int(raw_loss)
    final = result.snapshots[-1]
    return {
        "condition": condition,
        "master_seed": master_seed,
        "replicate": replicate,
        "trajectory_seed": seed,
        "baseline_all_patches_realised_high_trait_present": baseline_present,
        "baseline_h_alpha": baseline.h_alpha,
        "baseline_h_gamma": baseline.h_gamma,
        "baseline_fst": baseline.fst,
        "trait_loss_time_post_baseline": loss_time,
        "trait_loss_observed_post_baseline": loss_time is not None,
        "restricted_loss_time": PHASE_V_GENERATIONS + 1 if loss_time is None else loss_time,
        "final_mean_interaction": sum(final.interaction) / len(final.interaction),
        "final_total_population": sum(final.population),
        "final_realised_high_trait_patch_count": sum(
            item.realised_high_trait_occupied for item in final.trait_occupancy
        ),
    }


def _summarise_condition(rows: list[dict[str, Any]], condition: str) -> dict[str, Any]:
    subset = [row for row in rows if row["condition"] == condition]
    losses = sum(row["trait_loss_observed_post_baseline"] for row in subset)
    blocks = []
    for seed in PHASE_V_MASTER_SEEDS:
        by_seed = [row for row in subset if row["master_seed"] == seed]
        block_losses = sum(row["trait_loss_observed_post_baseline"] for row in by_seed)
        blocks.append({
            "master_seed": seed,
            "attempted": len(by_seed),
            "trait_loss_count": block_losses,
            "trait_loss_rate": block_losses / len(by_seed),
            "mean_restricted_loss_time": sum(row["restricted_loss_time"] for row in by_seed) / len(by_seed),
        })
    restricted = sorted(int(row["restricted_loss_time"]) for row in subset)
    mid = len(restricted) // 2
    median = (restricted[mid - 1] + restricted[mid]) / 2 if len(restricted) % 2 == 0 else restricted[mid]
    return {
        "condition": condition,
        "attempted": len(subset),
        "trait_loss_count": losses,
        "pooled_trait_loss_rate": losses / len(subset),
        "mean_restricted_loss_time": sum(restricted) / len(restricted),
        "median_restricted_loss_time": median,
        "seed_blocks": blocks,
    }


def _paired_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_key = {
        (row["condition"], row["master_seed"], row["replicate"]): row
        for row in rows
    }
    aligned_loss_anti_no = 0
    aligned_no_anti_loss = 0
    same_loss = 0
    same_no_loss = 0
    aligned_earlier = 0
    anti_earlier = 0
    ties = 0
    restricted_differences = []
    for seed in PHASE_V_MASTER_SEEDS:
        for replicate in range(PHASE_V_REPLICATES_PER_SEED):
            aligned = by_key[("aligned", seed, replicate)]
            anti = by_key[("anti_aligned", seed, replicate)]
            a_loss = bool(aligned["trait_loss_observed_post_baseline"])
            b_loss = bool(anti["trait_loss_observed_post_baseline"])
            if a_loss and not b_loss:
                aligned_loss_anti_no += 1
            elif not a_loss and b_loss:
                aligned_no_anti_loss += 1
            elif a_loss and b_loss:
                same_loss += 1
            else:
                same_no_loss += 1
            a_time = int(aligned["restricted_loss_time"])
            b_time = int(anti["restricted_loss_time"])
            restricted_differences.append(a_time - b_time)
            if a_time < b_time:
                aligned_earlier += 1
            elif b_time < a_time:
                anti_earlier += 1
            else:
                ties += 1
    return {
        "comparable_pairs": len(restricted_differences),
        "aligned_loss_anti_no_loss": aligned_loss_anti_no,
        "aligned_no_loss_anti_loss": aligned_no_anti_loss,
        "same_loss": same_loss,
        "same_no_loss": same_no_loss,
        "mcnemar_exact_p": _two_sided_binomial_p(aligned_loss_anti_no, aligned_no_anti_loss),
        "aligned_earlier_restricted_time": aligned_earlier,
        "anti_aligned_earlier_restricted_time": anti_earlier,
        "restricted_time_ties": ties,
        "mean_aligned_minus_anti_restricted_loss_time": sum(restricted_differences) / len(restricted_differences),
    }


def run_phase_v() -> dict[str, Any]:
    certificate = one_step_state_sufficiency_certificate()
    if not signatures_match():
        raise RuntimeError("Phase V opening failed: coarse baseline signatures differ")
    if certificate["coarse_marginals_are_transition_sufficient"] is True:
        raise RuntimeError("Phase V opening failed: declared alignment contrast does not change generation-1 transition")

    rows: list[dict[str, Any]] = []
    for seed in PHASE_V_MASTER_SEEDS:
        for replicate in range(PHASE_V_REPLICATES_PER_SEED):
            for condition in PHASE_V_CONDITIONS:
                row = _run_one(condition, seed, replicate)
                if row["baseline_all_patches_realised_high_trait_present"] is not True:
                    raise RuntimeError("Phase V baseline must retain realised high trait in every patch")
                rows.append(row)

    summaries = [_summarise_condition(rows, condition) for condition in PHASE_V_CONDITIONS]
    paired = _paired_summary(rows)
    if paired["mcnemar_exact_p"] < PHASE_V_ALPHA:
        decision = "cross_layer_alignment_changes_functional_loss_incidence"
    else:
        decision = "coarse_marginals_not_transition_sufficient_but_no_detected_loss_incidence_effect"
    return {
        "phase": "V",
        "decision": decision,
        "upstream_scientific_commit": UPSTREAM_SCIENTIFIC_COMMIT,
        "manifest": phase_v_manifest(),
        "baseline_signatures": {
            condition: baseline_signature(condition) for condition in PHASE_V_CONDITIONS
        },
        "mechanistic_certificate": certificate,
        "condition_summaries": summaries,
        "paired_summary": paired,
        "attempts": rows,
        "interpretation": (
            "Phase V tests whether layer-wise coarse marginals suffice to define an operational functional-fragmentation regime. "
            "A deterministic generation-1 difference falsifies transition sufficiency of those marginals. The paired finite-loss contrast separately tests whether that hidden alignment propagates to the declared functional-loss endpoint under the fixed deterioration schedule."
        ),
    }


def write_phase_v(output: str | Path) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(run_phase_v(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
