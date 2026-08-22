"""Prospective high-precision validation of the historical Phase-C .35/.40 contrast."""
from __future__ import annotations

from .frontier_refinement_manifest import PHASE_C_MASTER_SEEDS, PHASE_C_P_STAR

PHASE_P_REPLICATES_PER_SEED = 100
PHASE_P_PREFIX_REPLICATES = 20
PHASE_P_MIN_BASELINE_ELIGIBLE_PER_SEED = 70

# Locked Phase-C first-20 eligible/loss counts, keyed by the actual
# historical Phase-C master seeds declared in frontier_refinement_manifest.
PHASE_P_PREFIX_COUNTS = {
    20290210:{0.35:(19,11),0.40:(20,6)},
    20290211:{0.35:(17,9),0.40:(15,6)},
    20290212:{0.35:(19,9),0.40:(18,7)},
    20290213:{0.35:(17,10),0.40:(20,4)},
    20290214:{0.35:(19,7),0.40:(19,5)},
}


def expected_prefix(master_seed:int,p_star:float)->tuple[int,int]:
    try:return PHASE_P_PREFIX_COUNTS[int(master_seed)][float(p_star)]
    except KeyError as exc: raise ValueError("seed/p_star is not part of locked Phase C") from exc


def phase_p_manifest()->dict[str,object]:
    return {
        "protocol":"warning-blind outer frontier precision validation Phase P",
        "scientific_scope":"high_precision_phase_c_pstar_035_040_validation",
        "blinding_scope":"source_and_trait_loss_only",
        "master_seeds":list(PHASE_C_MASTER_SEEDS),
        "seed_selection":"all five locked Phase-C master seeds; no replacement seeds and no outcome-based selection",
        "p_star_values":list(PHASE_C_P_STAR),
        "replicates_per_seed":PHASE_P_REPLICATES_PER_SEED,
        "prefix_replicates":PHASE_P_PREFIX_REPLICATES,
        "minimum_baseline_eligible_per_seed":PHASE_P_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_attempts":len(PHASE_C_MASTER_SEEDS)*len(PHASE_C_P_STAR)*PHASE_P_REPLICATES_PER_SEED,
        "historical_r4_rule_unchanged":"all five observed block loss rates inside [0.30,0.70]",
        "source_reconstruction":"independent for each p_star exactly as historical Phase C",
        "prefix_rule":"all ten seed×p_star first-20 eligible/loss prefixes must reproduce exactly before interpretation",
        "primary_question":"does the historical p_star=.40 R3 classification persist at 100-attempt precision relative to the .35 R4 anchor?",
        "stop_rule":"use the five locked seeds once at 100 attempts per p_star; no replacement seeds, new p_star values, gate changes, or further precision escalation merely to preserve the historical .40 R3 label",
    }
