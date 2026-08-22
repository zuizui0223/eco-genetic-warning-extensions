"""Prospective high-precision validation of the historical Phase-D R4-width claim."""
from __future__ import annotations

from .frontier_refinement_manifest import PHASE_D_MASTER_SEEDS, PHASE_D_P_STAR

PHASE_O_REPLICATES_PER_SEED = 100
PHASE_O_PREFIX_REPLICATES = 20
PHASE_O_MIN_BASELINE_ELIGIBLE_PER_SEED = 70

# Locked Phase-D first-20 eligible/loss counts by master seed and p_star.
PHASE_O_PREFIX_COUNTS = {
    20290310: {0.325:(17,9), 0.350:(16,8), 0.375:(17,7)},
    20290311: {0.325:(19,10),0.350:(18,12),0.375:(18,7)},
    20290312: {0.325:(20,16),0.350:(17,11),0.375:(17,9)},
    20290313: {0.325:(18,12),0.350:(17,10),0.375:(18,7)},
    20290314: {0.325:(18,14),0.350:(19,12),0.375:(17,4)},
}


def expected_prefix(master_seed:int,p_star:float)->tuple[int,int]:
    try: return PHASE_O_PREFIX_COUNTS[int(master_seed)][float(p_star)]
    except KeyError as exc: raise ValueError("seed/p_star is not part of locked Phase D") from exc


def phase_o_manifest()->dict[str,object]:
    return {
        "protocol":"warning-blind frontier precision validation Phase O",
        "scientific_scope":"high_precision_phase_d_r4_width_validation",
        "blinding_scope":"source_and_trait_loss_only",
        "master_seeds":list(PHASE_D_MASTER_SEEDS),
        "seed_selection":"all five locked Phase-D master seeds; no replacement seeds and no outcome-based selection",
        "p_star_values":list(PHASE_D_P_STAR),
        "replicates_per_seed":PHASE_O_REPLICATES_PER_SEED,
        "prefix_replicates":PHASE_O_PREFIX_REPLICATES,
        "minimum_baseline_eligible_per_seed":PHASE_O_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_attempts":len(PHASE_D_MASTER_SEEDS)*len(PHASE_D_P_STAR)*PHASE_O_REPLICATES_PER_SEED,
        "historical_r4_rule_unchanged":"all five observed block loss rates inside [0.30,0.70]",
        "source_reconstruction":"independent for each p_star exactly as historical Phase D",
        "prefix_rule":"all 15 seed×p_star first-20 eligible/loss prefixes must reproduce exactly before interpretation",
        "primary_question":"does the historical R3/R4/R3 pattern at p_star=.325/.350/.375 persist at 100-attempt precision?",
        "decision_rule":"retain a narrow-frontier claim only if the central .350 remains R4 and at least one immediate neighbour remains outside R4 with high precision; otherwise revise the frontier claim to the observed high-precision map",
        "stop_rule":"use the five locked seeds once at 100 attempts per p_star; no replacement seeds, p_star refinement, gate changes, or further precision escalation to preserve the old narrow-R4 claim",
    }
