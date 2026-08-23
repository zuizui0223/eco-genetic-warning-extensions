"""Preregistered fresh-seed replication of the frozen H2-R relative-warning benchmark."""
from __future__ import annotations

from math import comb
from typing import Any, Mapping

PHASE_V_MASTER_SEEDS = (20291110, 20291111, 20291112, 20291113, 20291114)
PHASE_V_REPLICATES_PER_SEED = 20
PHASE_V_MIN_VALID_PAIRS_PER_ENDPOINT = 20
PHASE_V_RELATIVE_DECLINES = (0.05, 0.10, 0.20)
PHASE_V_DIVERSITY_IDS = ("H_alpha", "H_gamma")
PHASE_V_ALPHA = 0.05
PHASE_V_UPSTREAM_COMMIT = "dd8ee379d0d3518194c767d16402042525bc00dc"

PHASE_V_FROZEN_DOMAIN = {
    "mutation_rate": 0.10,
    "area_reference": 0.8,
    "interaction_feedback": 6.0,
    "ramp_generations": 30,
    "hold_generations": 90,
    "total_generations": 120,
    "total_normalized_barrier_increase": 0.15,
    "profile": "standard",
}


def one_sided_binomial_lead_p_value(leads: int, valid_pairs: int) -> float:
    """Exact P[X >= leads] under X~Binomial(valid_pairs, 0.5)."""
    if valid_pairs < 0 or leads < 0 or leads > valid_pairs:
        raise ValueError("invalid lead/valid-pair counts")
    if valid_pairs == 0:
        return 1.0
    return sum(comb(valid_pairs, k) for k in range(leads, valid_pairs + 1)) / (2**valid_pairs)


def phase_v_manifest() -> dict[str, Any]:
    return {
        "protocol": "fresh fixed-domain genetic-warning replication Phase V",
        "scientific_scope": "independent_replication_of_baseline_relative_H_alpha_H_gamma_warning",
        "upstream_commit": PHASE_V_UPSTREAM_COMMIT,
        "master_seeds": list(PHASE_V_MASTER_SEEDS),
        "seed_selection": (
            "all five seeds were checked against both repositories before declaration; no matches were found; "
            "no replacement or outcome-based seed selection is allowed"
        ),
        "replicates_per_seed": PHASE_V_REPLICATES_PER_SEED,
        "attempted_trajectories": len(PHASE_V_MASTER_SEEDS) * PHASE_V_REPLICATES_PER_SEED,
        "frozen_domain": dict(PHASE_V_FROZEN_DOMAIN),
        "endpoint_family": [
            {"diversity_id": diversity_id, "relative_decline_fraction": decline}
            for diversity_id in PHASE_V_DIVERSITY_IDS
            for decline in PHASE_V_RELATIVE_DECLINES
        ],
        "minimum_valid_pairs_per_endpoint": PHASE_V_MIN_VALID_PAIRS_PER_ENDPOINT,
        "directional_replication_rule": (
            "all six endpoints must have at least 20 valid same-trajectory warning/loss pairs, lead fraction > 0.5, "
            "and one-sided exact binomial p<0.05 when ties and lags are counted as non-leads"
        ),
        "strict_replication_rule": (
            "all six endpoints must have at least 20 valid same-trajectory pairs and every valid pair must be a lead "
            "with zero ties and zero lags"
        ),
        "decision_order": [
            "insufficient_precision",
            "strict_replication",
            "directional_replication_only",
            "not_replicated",
        ],
        "opening_boundary": (
            "the validation domain, endpoint family and deterioration schedule are frozen from the parent H2-R programme; "
            "there is no recalibration, endpoint selection or warning-informed domain search"
        ),
        "stop_rule": (
            "run this one five-seed ensemble once; do not replace seeds, change relative thresholds, recalibrate the domain, "
            "increase precision, or add endpoint families after seeing the result merely to obtain replication"
        ),
    }


def evaluate_parent_summary(summary: Mapping[str, Any]) -> dict[str, Any]:
    """Apply the preregistered Phase-V replication decision to parent H2-R summary output."""
    rows = []
    for endpoint in summary["endpoint_summaries"]:
        definition = dict(endpoint["definition"])
        valid = int(endpoint["valid_pair_count"])
        leads = int(endpoint["warning_lead_count"])
        ties = int(endpoint["warning_tie_count"])
        lags = int(endpoint["warning_lag_count"])
        p_value = one_sided_binomial_lead_p_value(leads, valid)
        sufficient = valid >= PHASE_V_MIN_VALID_PAIRS_PER_ENDPOINT
        strict = sufficient and leads == valid and ties == 0 and lags == 0
        directional = sufficient and leads > valid / 2 and p_value < PHASE_V_ALPHA
        rows.append({
            "definition": definition,
            "trajectory_available_count": int(endpoint["trajectory_available_count"]),
            "warning_observed_count": int(endpoint["warning_observed_count"]),
            "trait_loss_observed_count": int(endpoint["trait_loss_observed_count"]),
            "valid_pair_count": valid,
            "warning_lead_count": leads,
            "warning_tie_count": ties,
            "warning_lag_count": lags,
            "warning_lead_fraction": None if valid == 0 else leads / valid,
            "one_sided_binomial_p_vs_half": p_value,
            "precision_sufficient": sufficient,
            "strict_endpoint_replication": strict,
            "directional_endpoint_replication": directional,
            "seed_blocks": endpoint.get("seed_blocks", []),
        })

    if any(not row["precision_sufficient"] for row in rows):
        decision = "insufficient_precision"
    elif all(row["strict_endpoint_replication"] for row in rows):
        decision = "strict_replication"
    elif all(row["directional_endpoint_replication"] for row in rows):
        decision = "directional_replication_only"
    else:
        decision = "not_replicated"

    return {
        "stage": "fresh fixed-domain genetic-warning replication Phase V",
        "manifest": phase_v_manifest(),
        "decision": decision,
        "denominators": dict(summary["denominators"]),
        "endpoint_summaries": rows,
        "claim_boundary": (
            "Phase V tests replication only in the already frozen symmetric H2-R domain. It does not establish a universal "
            "genetic-warning threshold, portability across domains, or a direction-only recurrent-transition effect."
        ),
    }
