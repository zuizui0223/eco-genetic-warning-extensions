"""Prospective high-precision validation of historical Phase-E connectivity claims.

Phase L showed that the historical R3 labels at migration rates 0.10 and 0.20
cannot by themselves identify biological between-block heterogeneity at the
original 15-20 eligible trajectories per block. Phase M precision-expands the
same five historical Phase-E master seeds to 100 attempted replicates per seed
and replays all five migration rates without replacement seeds or gate changes.
"""
from __future__ import annotations

from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_KAPPA_MU,
    PHASE_E_MASTER_SEEDS,
    PHASE_E_MIGRATION_RATES,
    PHASE_E_P_STAR,
    PHASE_E_RAMP_GENERATIONS,
)

PHASE_M_REPLICATES_PER_SEED = 100
PHASE_M_PREFIX_REPLICATES = 20
PHASE_M_MIN_BASELINE_ELIGIBLE_PER_SEED = 70

# Locked Phase-E first-20 (eligible, losses) counts by master seed and migration rate.
PHASE_M_PREFIX_COUNTS = {
    20290410: {
        0.0: (15, 7), 0.025: (15, 8), 0.05: (15, 8), 0.10: (15, 10), 0.20: (15, 9),
    },
    20290411: {
        0.0: (18, 11), 0.025: (18, 10), 0.05: (18, 12), 0.10: (18, 13), 0.20: (18, 13),
    },
    20290412: {
        0.0: (20, 11), 0.025: (20, 9), 0.05: (20, 10), 0.10: (20, 12), 0.20: (20, 9),
    },
    20290413: {
        0.0: (18, 12), 0.025: (18, 11), 0.05: (18, 12), 0.10: (18, 10), 0.20: (18, 12),
    },
    20290414: {
        0.0: (20, 11), 0.025: (20, 12), 0.05: (20, 12), 0.10: (20, 12), 0.20: (20, 12),
    },
}


def expected_prefix(master_seed: int, migration_rate: float) -> tuple[int, int]:
    try:
        return PHASE_M_PREFIX_COUNTS[int(master_seed)][float(migration_rate)]
    except KeyError as exc:
        raise ValueError("seed/rate is not part of locked Phase E") from exc


def phase_m_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind connectivity precision validation Phase M",
        "scientific_scope": "high_precision_allele_frequency_mixing_condition_map",
        "calibration_scope": "source_and_trait_loss_only",
        "blinding_scope": "source_and_trait_loss_only",
        "master_seeds": list(PHASE_E_MASTER_SEEDS),
        "seed_selection": "all five locked Phase-E master seeds; no replacement or outcome-based selection",
        "migration_rates": list(PHASE_E_MIGRATION_RATES),
        "replicates_per_seed": PHASE_M_REPLICATES_PER_SEED,
        "prefix_replicates": PHASE_M_PREFIX_REPLICATES,
        "minimum_baseline_eligible_per_seed": PHASE_M_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "coordinate": {"kappa_mu": PHASE_E_KAPPA_MU, "p_star": PHASE_E_P_STAR},
        "fixed_conditions": {
            "area_reference": PHASE_E_AREA_REFERENCE,
            "interaction_kappa": PHASE_E_INTERACTION_KAPPA,
            "ramp_generations": PHASE_E_RAMP_GENERATIONS,
            "hold_generations": PHASE_E_HOLD_GENERATIONS,
            "horizon": PHASE_E_RAMP_GENERATIONS + PHASE_E_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_E_BARRIER_INCREASE,
            "fragmentation_geometry": "four_equal_patches_fixed_total_area",
        },
        "prepared_source_count": len(PHASE_E_MASTER_SEEDS) * PHASE_M_REPLICATES_PER_SEED,
        "trajectory_count": len(PHASE_E_MASTER_SEEDS) * PHASE_M_REPLICATES_PER_SEED * len(PHASE_E_MIGRATION_RATES),
        "paired_across_migration_rates": True,
        "historical_r4_rule_unchanged": "all five observed block loss rates inside [0.30,0.70]",
        "prefix_rule": (
            "For every historical master seed and all five migration rates, the first 20 attempted replicates must exactly reproduce "
            "the locked Phase-E eligible/loss counts. Any mismatch blocks scientific interpretation."
        ),
        "primary_question": (
            "At 100-attempt precision, do m=0.10 and m=0.20 remain outside R4, or do the historical R3 labels disappear?"
        ),
        "paired_effect_question": (
            "Regardless of gate class, quantify paired loss-status switches versus m=0 and exact McNemar evidence for a directional "
            "change in marginal functional-loss probability."
        ),
        "interpretation_boundary": (
            "migration_rate is allele-frequency mixing only; it is not demographic, pollen, seed, pollinator, recolonisation, or trait-bin movement."
        ),
        "stop_rule": (
            "Run the five locked master seeds once at 100 attempts per seed and all five historical migration rates. Do not add replacement "
            "seeds, alter migration levels, change the historical R4 band, or increase precision again merely to preserve the old R3 claim."
        ),
    }
