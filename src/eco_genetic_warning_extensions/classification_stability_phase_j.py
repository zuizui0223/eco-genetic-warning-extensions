"""Prospective warning-blind R4 classification-stability Phase J manifest.

Phase E and Phase I independently classified the same nominal m=0.10 condition
differently (R3 versus R4) under different fresh seed/source ensembles.  Phase J
does not vary a biological parameter.  It fixes that condition and asks whether
the five-seed R1/R2/R3/R4 gate is stable across four prospectively fixed,
independent fresh panels.
"""
from __future__ import annotations

from .mutation_coordinates import MutationCoordinates

PHASE_J_MASTER_SEEDS = tuple(range(20290910, 20290930))
PHASE_J_REPLICATES_PER_SEED = 20
PHASE_J_MIN_BASELINE_ELIGIBLE_PER_SEED = 10
PHASE_J_PANEL_SIZE = 5
PHASE_J_AREA_REFERENCE = 1.0
PHASE_J_INTERACTION_KAPPA = 4.5
PHASE_J_KAPPA_MU = 0.35
PHASE_J_P_STAR = 0.35
PHASE_J_MIGRATION_RATE = 0.10
PHASE_J_RAMP_GENERATIONS = 30
PHASE_J_HOLD_GENERATIONS = 90
PHASE_J_BARRIER_INCREASE = 0.30


def phase_j_coordinate() -> MutationCoordinates:
    return MutationCoordinates(kappa_mu=PHASE_J_KAPPA_MU, p_star=PHASE_J_P_STAR)


def phase_j_panels() -> tuple[tuple[int, ...], ...]:
    seeds = PHASE_J_MASTER_SEEDS
    return tuple(
        tuple(seeds[start : start + PHASE_J_PANEL_SIZE])
        for start in range(0, len(seeds), PHASE_J_PANEL_SIZE)
    )


def phase_j_manifest() -> dict[str, object]:
    panels = phase_j_panels()
    return {
        "protocol": "warning-blind R4 classification-stability Phase J",
        "scientific_scope": "independent_seed_ensemble_stability_of_fixed_R4_gate",
        "calibration_scope": "source_and_trait_loss_only",
        "blinding_scope": "source_and_trait_loss_only",
        "fixed_condition": {
            "area_reference": PHASE_J_AREA_REFERENCE,
            "interaction_kappa": PHASE_J_INTERACTION_KAPPA,
            "kappa_mu": PHASE_J_KAPPA_MU,
            "p_star": PHASE_J_P_STAR,
            "migration_rate": PHASE_J_MIGRATION_RATE,
            "ramp_generations": PHASE_J_RAMP_GENERATIONS,
            "hold_generations": PHASE_J_HOLD_GENERATIONS,
            "horizon": PHASE_J_RAMP_GENERATIONS + PHASE_J_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_J_BARRIER_INCREASE,
            "fragmentation_geometry": "four_equal_patches_fixed_total_area",
        },
        "motivation_only_not_selection_data": {
            "phase_e_m010_regime": "R3_highrep",
            "phase_i_m010_regime": "R4_highrep",
            "rule": "historical labels motivate the audit but do not alter the fixed condition, seed panels or classifier",
        },
        "master_seeds": list(PHASE_J_MASTER_SEEDS),
        "replicates_per_seed": PHASE_J_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_J_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "panel_size": PHASE_J_PANEL_SIZE,
        "panels": [list(panel) for panel in panels],
        "panel_count": len(panels),
        "prepared_source_count": len(PHASE_J_MASTER_SEEDS) * PHASE_J_REPLICATES_PER_SEED,
        "trajectory_count": len(PHASE_J_MASTER_SEEDS) * PHASE_J_REPLICATES_PER_SEED,
        "classification_rule": (
            "Each master seed yields one trait-loss rate. Each prospectively fixed five-seed panel is classified by the "
            "unchanged Protocol-002 R1/R2/R3/R4 all-seed rule."
        ),
        "stability_rule": (
            "If all four sufficient panels receive the same regime, record stable_<regime>; if sufficient panels differ, "
            "record ensemble_sensitive. Any insufficient panel yields insufficient_support."
        ),
        "opening_rule": (
            "All 20 fresh seed blocks must contain at least the predeclared minimum baseline-eligible trajectories. "
            "Otherwise record insufficient_support without replacing seeds."
        ),
        "stop_rule": (
            "Run exactly these 20 master seeds and four fixed five-seed panels once. Do not add seeds, regroup panels, "
            "change m=0.10, or change the R4 thresholds after observing the result."
        ),
        "interpretation_boundary": (
            "Phase J tests finite ensemble stability of the categorical event-regime gate at one fixed condition. It does "
            "not estimate a universal probability that a condition is R4 and does not invalidate any locked earlier finite campaign."
        ),
    }
