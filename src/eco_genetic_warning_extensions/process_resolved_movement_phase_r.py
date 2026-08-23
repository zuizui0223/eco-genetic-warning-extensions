"""Prospective Phase R: process-resolved individual dispersal versus allele-only mixing.

The experiment asks whether the one high-precision Phase-M heterogeneity result at
legacy allele-frequency mixing m=0.10 is reproduced when connectivity is instead
implemented as post-recruitment movement of whole individuals.

No movement-rate search is permitted.  The single process-resolved rate d=0.10
was declared because 0.10 is the already-identified legacy comparator; it is a
nominal stress-test match, not a claim of quantitatively equivalent gene flow.
"""
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

PHASE_R_REPLICATES_PER_SEED = 100
PHASE_R_MIN_BASELINE_ELIGIBLE_PER_SEED = 70
PHASE_R_LEGACY_MIGRATION_RATE = 0.10
PHASE_R_INDIVIDUAL_DISPERSAL_RATE = 0.10
PHASE_R_CONDITIONS = (
    "no_connectivity",
    "allele_only_m010",
    "individual_dispersal_d010",
)

# Exact high-precision Phase-M block counts, ordered by PHASE_E_MASTER_SEEDS.
# Entries are (losses, eligible).  Both legacy conditions must reproduce these
# before the new process-resolved condition can be interpreted.
PHASE_R_PHASE_M_BLOCKS = {
    "no_connectivity": ((47, 88), (48, 89), (58, 93), (46, 86), (51, 91)),
    "allele_only_m010": ((45, 88), (48, 89), (66, 93), (42, 86), (48, 91)),
}

# Exact original first-20 Phase-E prefixes, entries (eligible, losses).
PHASE_R_PREFIX_COUNTS = {
    20290410: {"no_connectivity": (15, 7), "allele_only_m010": (15, 10)},
    20290411: {"no_connectivity": (18, 11), "allele_only_m010": (18, 13)},
    20290412: {"no_connectivity": (20, 11), "allele_only_m010": (20, 12)},
    20290413: {"no_connectivity": (18, 12), "allele_only_m010": (18, 10)},
    20290414: {"no_connectivity": (20, 11), "allele_only_m010": (20, 12)},
}


def phase_r_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind process-resolved movement validation Phase R",
        "scientific_scope": "operator_portability_of_connectivity_effect",
        "master_seeds": list(PHASE_E_MASTER_SEEDS),
        "replicates_per_seed": PHASE_R_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_R_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "conditions": list(PHASE_R_CONDITIONS),
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
            "operator": "allele_frequency_mixing",
            "migration_rate": PHASE_R_LEGACY_MIGRATION_RATE,
            "reason": "Phase M detected high-precision between-block heterogeneity only at this tested legacy level",
        },
        "process_resolved_condition": {
            "operator": "post_recruitment_whole_individual_dispersal",
            "individual_dispersal_rate": PHASE_R_INDIVIDUAL_DISPERSAL_RATE,
            "destination_rule": "uniform among other patches",
            "census_and_trait_bins_move": True,
            "genetic_contribution": "source post-selection allele frequency weighted by realised integer migrant flux",
            "legacy_migration_rate": 0.0,
            "timing": "after local recruitment; before recurrent allele-state transition and finite drift",
            "nominal_rate_equivalence_claimed": False,
        },
        "opening_rule": (
            "The no-connectivity and allele-only m=0.10 conditions must exactly reproduce both the original first-20 Phase-E prefixes "
            "and the five locked 100-attempt Phase-M block counts. Process-resolved baseline eligibility must equal the paired no-connectivity condition."
        ),
        "primary_question": (
            "Does d=0.10 whole-individual dispersal show detectable high-precision between-block heterogeneity under the same source/seed ensemble?"
        ),
        "secondary_questions": (
            "Does process-resolved dispersal change marginal functional-loss probability versus no connectivity, and does it differ from allele-only m=0.10?"
        ),
        "interpretation_boundary": (
            "d=0.10 is a per-individual emigration probability and is not calibrated as equivalent to legacy m=0.10. The parent state lacks joint genotype-trait identities, "
            "so migrant trait bins are moved exactly while genetic contribution follows source post-selection allele frequency without genotype-trait covariance."
        ),
        "stop_rule": (
            "Run only the three declared conditions at the five locked Phase-E master seeds and 100 attempts per seed. Do not add movement rates, destination kernels, "
            "replacement seeds, or tune the operator after outcomes merely to reproduce or remove the Phase-M m=0.10 heterogeneity result."
        ),
    }
