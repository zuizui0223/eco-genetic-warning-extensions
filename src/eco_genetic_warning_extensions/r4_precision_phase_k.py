"""Prospective high-precision validation of the historical R4/R3 discrepancy.

Phase J showed that the five-block all-in-band gate is finite-sample sensitive at
17-20 eligible trajectories per block.  Phase K therefore precision-expands all
master seeds that generated the Phase-H / Phase-I discrepancy.  No replacement
seeds are selected.

Each historical master seed is rerun with 100 attempted replicates.  The first
20 replicate prefix must reproduce its locked historical count before the full
100-replicate block is interpreted.  Only intact and partner-loss/no-rescue
conditions are run; genetic-warning outcomes remain unavailable.
"""
from __future__ import annotations

from .explicit_rewiring_phase_h import PHASE_H_MASTER_SEEDS
from .support_timing_phase_i import PHASE_I_MASTER_SEEDS

PHASE_K_REPLICATES_PER_SEED = 100
PHASE_K_MIN_BASELINE_ELIGIBLE_PER_SEED = 70
PHASE_K_PREFIX_REPLICATES = 20

# (eligible, losses) for the first 20 attempted replicates of each locked campaign.
PHASE_H_PREFIX_INTACT = {
    20290710: (18, 9),
    20290711: (17, 8),
    20290712: (17, 7),
    20290713: (17, 6),
    20290714: (17, 7),
}
PHASE_H_PREFIX_LOSS = {
    20290710: (18, 9),
    20290711: (17, 8),
    20290712: (17, 9),
    20290713: (17, 6),
    20290714: (17, 5),
}
PHASE_I_PREFIX_INTACT = {
    20290810: (17, 9),
    20290811: (18, 10),
    20290812: (19, 10),
    20290813: (18, 8),
    20290814: (18, 9),
}
PHASE_I_PREFIX_LOSS = {
    20290810: (17, 7),
    20290811: (18, 8),
    20290812: (19, 11),
    20290813: (18, 9),
    20290814: (18, 9),
}


def phase_k_seed_families() -> dict[str, tuple[int, ...]]:
    return {
        "phase_h_seed_family": tuple(PHASE_H_MASTER_SEEDS),
        "phase_i_seed_family": tuple(PHASE_I_MASTER_SEEDS),
    }


def expected_prefix(master_seed: int, condition: str) -> tuple[int, int]:
    if condition not in {"intact_control", "partner_loss_no_rescue"}:
        raise ValueError("unknown Phase-K condition")
    if master_seed in PHASE_H_PREFIX_INTACT:
        table = PHASE_H_PREFIX_INTACT if condition == "intact_control" else PHASE_H_PREFIX_LOSS
        return table[master_seed]
    if master_seed in PHASE_I_PREFIX_INTACT:
        table = PHASE_I_PREFIX_INTACT if condition == "intact_control" else PHASE_I_PREFIX_LOSS
        return table[master_seed]
    raise ValueError("master seed is not part of the locked Phase-H / Phase-I families")


def phase_k_manifest() -> dict[str, object]:
    families = phase_k_seed_families()
    all_seeds = tuple(seed for values in families.values() for seed in values)
    return {
        "protocol": "warning-blind R4 precision validation Phase K",
        "scientific_scope": "within_block_precision_of_fixed_partner_loss_regime",
        "calibration_scope": "source_network_and_trait_loss_only",
        "blinding_scope": "source_network_and_trait_loss_only",
        "historical_r4_rule_unchanged": "all five observed block loss rates inside [0.30,0.70]",
        "seed_families": {name: list(values) for name, values in families.items()},
        "seed_selection": "all five Phase-H and all five Phase-I master seeds; no replacement or outcome-based selection",
        "replicates_per_seed": PHASE_K_REPLICATES_PER_SEED,
        "prefix_replicates": PHASE_K_PREFIX_REPLICATES,
        "minimum_baseline_eligible_per_seed": PHASE_K_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "conditions": ["intact_control", "partner_loss_no_rescue"],
        "prepared_source_count": len(all_seeds) * PHASE_K_REPLICATES_PER_SEED,
        "trajectory_count": len(all_seeds) * PHASE_K_REPLICATES_PER_SEED * 2,
        "paired_conditions": True,
        "prefix_rule": (
            "For every master seed and both conditions, the first 20 attempted replicates must exactly reproduce the locked "
            "historical eligible/loss counts. Any mismatch is an implementation/provenance failure and blocks interpretation."
        ),
        "precision_rule": (
            "Each full 100-attempt block must retain at least 70 baseline-eligible trajectories. Historical R4 classification is then "
            "applied unchanged to the five full blocks in each seed family."
        ),
        "decision_rule": (
            "If both historical seed families converge to the same full-precision partner-loss regime, record precision_convergence. "
            "If they retain different R4/R3 classifications, record between_ensemble_instability_persists. No seed replacement or "
            "R4-band modification is allowed."
        ),
        "interpretation_boundary": (
            "Phase K distinguishes finite within-block sampling instability from persistent between-master-seed-family differences. "
            "It does not revise historical labels and does not test genetic-warning performance."
        ),
        "stop_rule": (
            "Run the ten locked master seeds once at 100 attempts per block. Do not add replacement seeds, alter the 0.30-0.70 band, "
            "or increase replicates again merely to obtain agreement."
        ),
    }
