"""Prospective Phase S: pollen-only gene flow versus allele-only mixing."""
from __future__ import annotations

from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_KAPPA_MU,
    PHASE_E_MASTER_SEEDS,
    PHASE_E_P_STAR,
    PHASE_E_RAMP_GENERATIONS,
)
from .process_resolved_movement_phase_r import PHASE_R_PHASE_M_BLOCKS, PHASE_R_PREFIX_COUNTS

PHASE_S_REPLICATES_PER_SEED = 100
PHASE_S_MIN_BASELINE_ELIGIBLE_PER_SEED = 70
PHASE_S_LEGACY_MIGRATION_RATE = 0.10
PHASE_S_POLLEN_IMMIGRATION_RATE = 0.20
PHASE_S_CONDITIONS = (
    "no_connectivity",
    "allele_only_m010",
    "pollen_only_g020",
)

# Phase S uses the exact same legacy comparator locks as Phase R/M.
PHASE_S_PHASE_M_BLOCKS = PHASE_R_PHASE_M_BLOCKS
PHASE_S_PREFIX_COUNTS = PHASE_R_PREFIX_COUNTS


def phase_s_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind pollen-only gene-flow validation Phase S",
        "scientific_scope": "operator_portability_of_allele_mixing_to_pollen_gene_flow",
        "master_seeds": list(PHASE_E_MASTER_SEEDS),
        "replicates_per_seed": PHASE_S_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_S_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "conditions": list(PHASE_S_CONDITIONS),
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
        "legacy_comparator": {
            "operator": "direct_post_selection_allele_frequency_mixing",
            "migration_rate": PHASE_S_LEGACY_MIGRATION_RATE,
        },
        "pollen_condition": {
            "operator": "pollen_only_paternal_gametic_gene_flow",
            "pollen_immigration_rate": PHASE_S_POLLEN_IMMIGRATION_RATE,
            "legacy_migration_rate": 0.0,
            "maternal_gene_pool": "local_post_selection",
            "paternal_slots": "one_per_local_recruit",
            "external_pollen_fraction": PHASE_S_POLLEN_IMMIGRATION_RATE,
            "donor_weight": "source_local_recruited_census_excluding_destination",
            "census_moves": False,
            "trait_bins_move": False,
            "timing": "after local recruitment; before recurrent allele-state transition and finite drift",
            "separate_pollen_rng": True,
        },
        "nominal_match_rationale": (
            "In the declared biparental closure, paternal gametes contribute one half of the zygotic allele pool. "
            "An external-pollen fraction g=0.20 therefore contributes at most about 0.10 of expected zygotic genomic ancestry before donor weighting. "
            "This is a mechanistic nominal comparison to legacy m=0.10, not calibrated equivalence."
        ),
        "opening_rule": (
            "Zero pollen flow must reproduce the pinned finite-bin parent life cycle. The no-connectivity and allele-only m=0.10 comparators must exactly reproduce "
            "all original first-20 Phase-E prefixes and all five locked 100-attempt Phase-M block counts. Pollen flow must not change paired baseline eligibility."
        ),
        "primary_question": (
            "Does pollen-only g=0.20 show detectable high-precision between-block heterogeneity under the exact Phase-M source/seed ensemble?"
        ),
        "secondary_questions": (
            "Does pollen-only gene flow change marginal functional-loss probability versus no connectivity or allele-only m=0.10?"
        ),
        "interpretation_boundary": (
            "The parent does not model explicit flowers, mating pairs, pollen limitation, selfing, incompatibility or genotype-by-trait identities. "
            "Phase S is a finite paternal-gamete-origin closure, not a full plant mating system or pollinator movement model."
        ),
        "stop_rule": (
            "Run only no connectivity, legacy m=0.10 and pollen g=0.20 at the five locked Phase-E seeds and 100 attempts per seed. "
            "Do not tune pollen fractions, donor kernels, selfing, replacement seeds or precision after outcomes to reproduce or remove legacy heterogeneity."
        ),
    }
