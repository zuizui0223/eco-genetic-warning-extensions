"""Prospective high-precision validation of historical Phase-G partner-loss claims."""
from __future__ import annotations

from .partner_redundancy_phase_g import PHASE_G_MASTER_SEEDS, phase_g_conditions

PHASE_N_REPLICATES_PER_SEED = 100
PHASE_N_PREFIX_REPLICATES = 20
PHASE_N_MIN_BASELINE_ELIGIBLE_PER_SEED = 70

# Locked Phase-G first-20 eligible/loss counts by seed and architecture.
PHASE_N_PREFIX_COUNTS = {
    20290610: {"intact_control":(18,9),"even_redundant":(18,10),"graded_contributions":(18,9),"dominant_partner":(18,9)},
    20290611: {"intact_control":(17,8),"even_redundant":(17,8),"graded_contributions":(17,7),"dominant_partner":(17,8)},
    20290612: {"intact_control":(18,10),"even_redundant":(18,8),"graded_contributions":(18,10),"dominant_partner":(18,12)},
    20290613: {"intact_control":(20,12),"even_redundant":(20,13),"graded_contributions":(20,11),"dominant_partner":(20,11)},
    20290614: {"intact_control":(17,10),"even_redundant":(17,12),"graded_contributions":(17,13),"dominant_partner":(17,12)},
}


def expected_prefix(master_seed: int, architecture: str) -> tuple[int,int]:
    try:
        return PHASE_N_PREFIX_COUNTS[int(master_seed)][architecture]
    except KeyError as exc:
        raise ValueError("seed/architecture is not part of locked Phase G") from exc


def phase_n_manifest() -> dict[str,object]:
    conditions = phase_g_conditions()
    return {
        "protocol":"warning-blind partner-architecture precision validation Phase N",
        "scientific_scope":"high_precision_partner_loss_architecture_condition_map",
        "blinding_scope":"source_and_trait_loss_only",
        "master_seeds":list(PHASE_G_MASTER_SEEDS),
        "seed_selection":"all five locked Phase-G master seeds; no replacement or outcome-based selection",
        "architectures":[condition.name for condition in conditions],
        "replicates_per_seed":PHASE_N_REPLICATES_PER_SEED,
        "prefix_replicates":PHASE_N_PREFIX_REPLICATES,
        "minimum_baseline_eligible_per_seed":PHASE_N_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_count":len(PHASE_G_MASTER_SEEDS)*PHASE_N_REPLICATES_PER_SEED,
        "trajectory_count":len(PHASE_G_MASTER_SEEDS)*PHASE_N_REPLICATES_PER_SEED*len(conditions),
        "paired_across_architectures":True,
        "historical_r4_rule_unchanged":"all five observed block loss rates inside [0.30,0.70]",
        "prefix_rule":"all 20-replicate historical eligible/loss prefixes must reproduce exactly before interpretation",
        "primary_question":"do the three historical partner-loss R3 labels persist at 100-attempt precision?",
        "paired_effect_question":"quantify exact paired loss-status changes versus intact independently of gate class",
        "stop_rule":"use the five locked seeds once at 100 attempts; no replacement seeds, architecture tuning, gate changes, or further precision escalation to preserve old R3 labels",
    }
