"""Prospective warning-blind support/timing decomposition Phase I.

Phase H recovered network structure and match-weighted support without recovering
R4. Phase I asks why. Under the current explicit-network closure, network topology
enters the eco-genetic life cycle only through the network-derived support
multiplier. Therefore topology-only manipulations are representation-null controls,
not evidence for an independent topological channel.

The causal experiment separates partial support recovery, full support recovery on
the same 10-generation schedule, and immediate full support after the same partner
loss. Fresh sources and seeds are paired across all conditions. No Phase-I outcome
is available when the conditions below are declared.
"""
from __future__ import annotations

from dataclasses import dataclass

from .explicit_rewiring_phase_h import (
    PHASE_H_AREA_REFERENCE,
    PHASE_H_BARRIER_INCREASE,
    PHASE_H_EDGE_CAPACITIES,
    PHASE_H_HOLD_GENERATIONS,
    PHASE_H_INITIAL_EDGE_STRENGTHS,
    PHASE_H_INTERACTION_KAPPA,
    PHASE_H_KAPPA_MU,
    PHASE_H_MIGRATION_RATE,
    PHASE_H_PARTNER_POOL_SIZE,
    PHASE_H_P_STAR,
    PHASE_H_PRIMARY_PARTNER_COUNT,
    PHASE_H_RAMP_GENERATIONS,
    PHASE_H_REWIRING_WINDOW_GENERATIONS,
    PHASE_H_TRAIT_MATCH_SCORES,
    intact_edges,
    network_edges_at_generation,
    phase_h_conditions,
    post_loss_edges,
    support_multiplier,
)
from .mutation_coordinates import MutationCoordinates

PHASE_I_MASTER_SEEDS = (20290810, 20290811, 20290812, 20290813, 20290814)
PHASE_I_REPLICATES_PER_SEED = 20
PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED = 10


@dataclass(frozen=True)
class SupportTimingCondition:
    name: str
    topology_rule: str
    effective_support_rule: str

    def __post_init__(self) -> None:
        if self.topology_rule not in {"intact", "loss", "rewired"}:
            raise ValueError("unknown Phase-I topology rule")
        if self.effective_support_rule not in {"topology", "loss", "rewired", "full_delayed", "full_immediate"}:
            raise ValueError("unknown Phase-I effective-support rule")

    def identity(self) -> dict[str, str]:
        return {
            "name": self.name,
            "topology_rule": self.topology_rule,
            "effective_support_rule": self.effective_support_rule,
        }


PHASE_I_CONDITIONS = (
    SupportTimingCondition("intact_control", "intact", "topology"),
    SupportTimingCondition("partner_loss_no_rescue", "loss", "topology"),
    SupportTimingCondition("topology_only_null", "rewired", "loss"),
    SupportTimingCondition("partial_support_only", "loss", "rewired"),
    SupportTimingCondition("coupled_rewiring_replay", "rewired", "topology"),
    SupportTimingCondition("full_support_delayed", "loss", "full_delayed"),
    SupportTimingCondition("full_support_immediate", "loss", "full_immediate"),
)


def phase_i_coordinate() -> MutationCoordinates:
    return MutationCoordinates(kappa_mu=PHASE_H_KAPPA_MU, p_star=PHASE_H_P_STAR)


def phase_i_conditions() -> tuple[SupportTimingCondition, ...]:
    return PHASE_I_CONDITIONS


def _phase_h_rewiring_condition():
    return phase_h_conditions()[-1]


def topology_edges_at_generation(
    condition: SupportTimingCondition,
    replicate_index: int,
    generation: int,
) -> tuple[float, ...]:
    if condition.topology_rule == "intact":
        return intact_edges()
    if condition.topology_rule == "loss":
        return post_loss_edges(replicate_index)
    return network_edges_at_generation(_phase_h_rewiring_condition(), replicate_index, generation)


def _rewired_support(replicate_index: int, generation: int) -> float:
    edges = network_edges_at_generation(_phase_h_rewiring_condition(), replicate_index, generation)
    return support_multiplier(edges)


def _loss_support(replicate_index: int) -> float:
    return support_multiplier(post_loss_edges(replicate_index))


def _full_delayed_support(replicate_index: int, generation: int) -> float:
    start = _loss_support(replicate_index)
    window = PHASE_H_REWIRING_WINDOW_GENERATIONS
    if window <= 1 or generation >= window:
        return 1.0
    if generation <= 1:
        return start
    progress = (generation - 1) / (window - 1)
    return start + progress * (1.0 - start)


def effective_support_at_generation(
    condition: SupportTimingCondition,
    replicate_index: int,
    generation: int,
) -> float:
    if generation < 1:
        raise ValueError("generation must start at one")
    if condition.effective_support_rule == "topology":
        return support_multiplier(topology_edges_at_generation(condition, replicate_index, generation))
    if condition.effective_support_rule == "loss":
        return _loss_support(replicate_index)
    if condition.effective_support_rule == "rewired":
        return _rewired_support(replicate_index, generation)
    if condition.effective_support_rule == "full_delayed":
        return _full_delayed_support(replicate_index, generation)
    return 1.0


def phase_i_schedule(
    condition: SupportTimingCondition,
    replicate_index: int,
    generations: int,
) -> tuple[dict[str, object], ...]:
    if generations < 1:
        raise ValueError("generations must be positive")
    rows = []
    for generation in range(1, generations + 1):
        edges = topology_edges_at_generation(condition, replicate_index, generation)
        raw_support = support_multiplier(edges)
        effective_support = effective_support_at_generation(condition, replicate_index, generation)
        active = sum(edge > 1e-12 for edge in edges)
        rows.append({
            "generation": generation,
            "edge_strengths": list(edges),
            "active_edge_count": active,
            "realised_connectance": active / PHASE_H_PARTNER_POOL_SIZE,
            "raw_topology_support_multiplier": raw_support,
            "effective_support_multiplier": effective_support,
        })
    return tuple(rows)


def phase_i_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind support/timing decomposition Phase I",
        "scientific_scope": "support_magnitude_and_recovery_timing_after_partner_loss",
        "calibration_scope": "source_network_and_trait_loss_only",
        "blinding_scope": "source_network_and_trait_loss_only",
        "coordinate": {"kappa_mu": PHASE_H_KAPPA_MU, "p_star": PHASE_H_P_STAR},
        "fixed_conditions": {
            "area_reference": PHASE_H_AREA_REFERENCE,
            "interaction_kappa": PHASE_H_INTERACTION_KAPPA,
            "ramp_generations": PHASE_H_RAMP_GENERATIONS,
            "hold_generations": PHASE_H_HOLD_GENERATIONS,
            "horizon": PHASE_H_RAMP_GENERATIONS + PHASE_H_HOLD_GENERATIONS,
            "normalised_barrier_increase": PHASE_H_BARRIER_INCREASE,
            "fragmentation_geometry": "four_equal_patches_fixed_total_area",
            "migration_rate": PHASE_H_MIGRATION_RATE,
        },
        "network": {
            "candidate_partner_count": PHASE_H_PARTNER_POOL_SIZE,
            "initial_active_partner_count": PHASE_H_PRIMARY_PARTNER_COUNT,
            "initial_edge_strengths": list(PHASE_H_INITIAL_EDGE_STRENGTHS),
            "trait_match_scores": list(PHASE_H_TRAIT_MATCH_SCORES),
            "edge_capacities": list(PHASE_H_EDGE_CAPACITIES),
            "rewiring_window_generations": PHASE_H_REWIRING_WINDOW_GENERATIONS,
            "phase_h_partial_recovery_rule": "same fixed trait_capacity rewiring rule as Phase H",
        },
        "conditions": [condition.identity() for condition in PHASE_I_CONDITIONS],
        "master_seeds": list(PHASE_I_MASTER_SEEDS),
        "replicates_per_seed": PHASE_I_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_I_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_count": len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED,
        "trajectory_count": len(PHASE_I_CONDITIONS) * len(PHASE_I_MASTER_SEEDS) * PHASE_I_REPLICATES_PER_SEED,
        "paired_across_conditions": True,
        "opening_rule": (
            "Interpret the decomposition only if fresh intact_control is R4_highrep and fresh partner_loss_no_rescue "
            "is R3_highrep; otherwise record not_opened without changing seeds, support schedules, network rules, or thresholds."
        ),
        "representation_nulls": (
            "topology_only_null must have the same effective-support schedule and biological outcomes as partner_loss_no_rescue; "
            "partial_support_only must have the same effective-support schedule and biological outcomes as coupled_rewiring_replay. "
            "These are model-representation audits, not independent topology-effect tests."
        ),
        "causal_readout": (
            "If partial support is R4, the Phase-H support recovery was sufficient on fresh seeds. If partial remains R3 but "
            "full_support_delayed is R4, recovery magnitude was limiting. If full_support_delayed remains R3 but "
            "full_support_immediate is R4, recovery timing/path dependence is implicated. Immediate full support is a positive "
            "representation control and must match intact biological outcomes under this closure."
        ),
        "stop_rule": (
            "Classify these conditions once. Do not tune support levels, recovery window, partner-loss identity, seeds, or R4 thresholds "
            "after observing Phase-I outcomes."
        ),
        "interpretation_boundary": (
            "The current closure has no topology-to-life-cycle channel independent of match-weighted support. Phase I therefore tests "
            "support magnitude and recovery timing/history, while topology-only comparisons audit the representation."
        ),
    }
