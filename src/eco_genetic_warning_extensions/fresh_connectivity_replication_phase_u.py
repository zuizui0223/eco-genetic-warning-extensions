"""Prospective fresh-seed replication of the Phase-M m=0.10 heterogeneity result.

Phase U introduces no new biological mechanism and no connectivity sweep.  It
asks whether the single surviving high-precision Phase-M block-heterogeneity
observation replicates in one completely fresh five-seed ensemble.
"""
from __future__ import annotations

from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_KAPPA_MU,
    PHASE_E_P_STAR,
    PHASE_E_RAMP_GENERATIONS,
)

PHASE_U_MASTER_SEEDS = (20291010, 20291011, 20291012, 20291013, 20291014)
PHASE_U_REPLICATES_PER_SEED = 100
PHASE_U_MIN_BASELINE_ELIGIBLE_PER_SEED = 70
PHASE_U_MIGRATION_RATES = (0.0, 0.10)
PHASE_U_ALPHA = 0.05


def phase_u_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind fresh connectivity replication Phase U",
        "scientific_scope": "independent_replication_of_phase_m_m010_block_heterogeneity",
        "master_seeds": list(PHASE_U_MASTER_SEEDS),
        "seed_provenance": (
            "prospectively declared fresh master seeds; repository search before declaration found no prior use of 20291010-20291014"
        ),
        "replicates_per_seed": PHASE_U_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_U_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "migration_rates": list(PHASE_U_MIGRATION_RATES),
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
        "paired_design": (
            "Each prepared source and trajectory seed is shared between m=0 and allele-only m=0.10. Source preparation occurs once before either migration condition."
        ),
        "opening_rule": (
            "All five fresh seed blocks must contain at least 70 baseline-eligible trajectories in both conditions, and paired baseline eligibility must be identical. "
            "Neither condition is required to pass the historical R4 screen before interpretation."
        ),
        "primary_estimand": "Pearson equal-rate evidence for between-block heterogeneity at allele-only m=0.10",
        "negative_control_estimand": "Pearson equal-rate evidence for between-block heterogeneity at m=0",
        "secondary_estimands": [
            "pooled functional-loss incidence by condition",
            "paired loss-status switching",
            "exact McNemar marginal-risk contrast m=0.10 versus m=0",
            "historical R1-R4 screen label retained only for descriptive provenance",
        ],
        "decision_rule": {
            "specific_m010_heterogeneity_replicated": "m=0.10 equal-rate p<0.05 AND m=0 equal-rate p>=0.05",
            "fresh_ensemble_heterogeneity_not_specific_to_m010": "m=0.10 equal-rate p<0.05 AND m=0 equal-rate p<0.05",
            "historical_m010_heterogeneity_not_freshly_replicated": "m=0.10 equal-rate p>=0.05",
            "insufficient_fresh_precision": "any block has fewer than 70 paired baseline-eligible trajectories",
        },
        "alpha": PHASE_U_ALPHA,
        "blinding_scope": "source preparation and functional-loss outcomes only; no genetic-warning fields are used",
        "interpretation_boundary": (
            "This is one independent fresh-seed replication at one pre-existing legacy allele-frequency mixing level. It does not estimate a connectivity threshold or establish a universal migration effect."
        ),
        "stop_rule": (
            "Run exactly one fresh five-seed ensemble at m=0 and m=0.10 with 100 attempts per seed. Do not replace seeds, add migration levels, rerun fresh ensembles, "
            "change alpha, alter the historical screen, or increase precision after observing outcomes merely to obtain replication."
        ),
    }
