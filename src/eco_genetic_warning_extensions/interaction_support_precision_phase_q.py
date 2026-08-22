"""Prospective high-precision validation of historical Phase-F interaction-support results."""
from __future__ import annotations
from .interaction_support_phase_f import PHASE_F_INTERACTION_KAPPAS, PHASE_F_MASTER_SEEDS

PHASE_Q_REPLICATES_PER_SEED=100
PHASE_Q_PREFIX_REPLICATES=20
PHASE_Q_MIN_BASELINE_ELIGIBLE_PER_SEED=70
PHASE_Q_PREFIX_COUNTS={
20290510:{3.0:(14,9),4.5:(19,13),6.0:(18,9)},
20290511:{3.0:(17,7),4.5:(19,8),6.0:(16,11)},
20290512:{3.0:(12,4),4.5:(19,10),6.0:(17,10)},
20290513:{3.0:(17,9),4.5:(18,9),6.0:(18,8)},
20290514:{3.0:(17,7),4.5:(19,9),6.0:(18,10)},}

def expected_prefix(seed:int,kappa:float)->tuple[int,int]:
    try:return PHASE_Q_PREFIX_COUNTS[int(seed)][float(kappa)]
    except KeyError as exc:raise ValueError("seed/kappa not in locked Phase F") from exc

def phase_q_manifest()->dict[str,object]:
    return {"protocol":"interaction-support precision validation Phase Q","blinding_scope":"source_and_trait_loss_only","master_seeds":list(PHASE_F_MASTER_SEEDS),"seed_selection":"all five locked Phase-F master seeds; no replacement seeds and no outcome-based selection","interaction_kappas":list(PHASE_F_INTERACTION_KAPPAS),"replicates_per_seed":PHASE_Q_REPLICATES_PER_SEED,"prefix_replicates":20,"minimum_baseline_eligible_per_seed":70,"historical_r4_rule_unchanged":"all five observed block loss rates inside [0.30,0.70]","source_reconstruction":"independent for each kappa exactly as Phase F","primary_question":"do all three historical kappa levels remain R4 at 100-attempt precision?","stop_rule":"no replacement seeds, new kappa values, gate changes, or further precision escalation merely to preserve the old all-R4 result"}
