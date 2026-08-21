"""Prospective warning-blind explicit rewiring Phase H manifest.

Phase H asks whether one fixed, biologically constrained rewiring rule can recover
loss-regime reproducibility after the matched single-partner loss used to motivate
the next step from Phase G.  Every condition starts from the same focal interaction
network: four active primary partners inside a six-partner candidate pool.  The
same primary partner is removed in the two loss conditions.  Only the rewiring
rule differs.

This is an explicit one-focal-node interaction-network closure.  Edge strengths,
partner availability, latent candidate edges, trait-match scores and edge
capacities are represented directly.  It is not a full multispecies network and
does not model partner demography, coextinction, pollen movement or pollinator
movement.
"""
from __future__ import annotations

from dataclasses import dataclass

from .mutation_coordinates import MutationCoordinates

PHASE_H_MASTER_SEEDS = (20290710, 20290711, 20290712, 20290713, 20290714)
PHASE_H_REPLICATES_PER_SEED = 20
PHASE_H_MIN_BASELINE_ELIGIBLE_PER_SEED = 10
PHASE_H_RAMP_GENERATIONS = 30
PHASE_H_HOLD_GENERATIONS = 90
PHASE_H_AREA_REFERENCE = 1.0
PHASE_H_INTERACTION_KAPPA = 4.5
PHASE_H_KAPPA_MU = 0.35
PHASE_H_P_STAR = 0.35
PHASE_H_BARRIER_INCREASE = 0.30
PHASE_H_MIGRATION_RATE = 0.0

PHASE_H_PARTNER_POOL_SIZE = 6
PHASE_H_PRIMARY_PARTNER_COUNT = 4
PHASE_H_INITIAL_EDGE_STRENGTHS = (0.25, 0.25, 0.25, 0.25, 0.0, 0.0)
PHASE_H_TRAIT_MATCH_SCORES = (1.0, 0.9, 0.8, 0.7, 0.6, 0.5)
PHASE_H_EDGE_CAPACITIES = (0.30, 0.30, 0.30, 0.30, 0.30, 0.30)
PHASE_H_REWIRING_FRACTION = 0.50
PHASE_H_REWIRING_WINDOW_GENERATIONS = 10


@dataclass(frozen=True)
class RewiringCondition:
    name: str
    remove_primary_partner: bool
    rewiring_rule: str

    def __post_init__(self) -> None:
        if self.rewiring_rule not in {"none", "trait_capacity"}:
            raise ValueError("unknown Phase-H rewiring rule")
        if not self.remove_primary_partner and self.rewiring_rule != "none":
            raise ValueError("intact Phase-H condition cannot rewire without partner loss")

    def identity(self) -> dict[str, object]:
        return {
            "name": self.name,
            "remove_primary_partner": self.remove_primary_partner,
            "rewiring_rule": self.rewiring_rule,
        }


PHASE_H_CONDITIONS = (
    RewiringCondition("intact_control", False, "none"),
    RewiringCondition("partner_loss_no_rewiring", True, "none"),
    RewiringCondition("partner_loss_trait_capacity_rewiring", True, "trait_capacity"),
)


def phase_h_coordinate() -> MutationCoordinates:
    return MutationCoordinates(kappa_mu=PHASE_H_KAPPA_MU, p_star=PHASE_H_P_STAR)


def phase_h_conditions() -> tuple[RewiringCondition, ...]:
    return PHASE_H_CONDITIONS


def lost_primary_partner_index(replicate_index: int) -> int:
    if replicate_index < 0:
        raise ValueError("replicate_index must be nonnegative")
    return replicate_index % PHASE_H_PRIMARY_PARTNER_COUNT


def _validate_edges(edges: tuple[float, ...]) -> tuple[float, ...]:
    if len(edges) != PHASE_H_PARTNER_POOL_SIZE:
        raise ValueError("Phase-H edge vector must match candidate partner pool")
    for edge, capacity in zip(edges, PHASE_H_EDGE_CAPACITIES):
        if edge < -1e-12 or edge > capacity + 1e-12:
            raise ValueError("Phase-H edge strength lies outside [0, capacity]")
    return tuple(max(0.0, float(edge)) for edge in edges)


def intact_edges() -> tuple[float, ...]:
    return _validate_edges(PHASE_H_INITIAL_EDGE_STRENGTHS)


def post_loss_edges(replicate_index: int) -> tuple[float, ...]:
    index = lost_primary_partner_index(replicate_index)
    values = list(intact_edges())
    values[index] = 0.0
    return _validate_edges(tuple(values))


def _capacity_constrained_allocation(
    base_edges: tuple[float, ...],
    lost_index: int,
    effort_to_reallocate: float,
) -> tuple[float, ...]:
    """Allocate rewired interaction effort by trait match and spare edge capacity."""
    if effort_to_reallocate < 0.0:
        raise ValueError("effort_to_reallocate must be nonnegative")
    allocation = [0.0] * PHASE_H_PARTNER_POOL_SIZE
    remaining = float(effort_to_reallocate)
    for _ in range(PHASE_H_PARTNER_POOL_SIZE + 2):
        if remaining <= 1e-12:
            break
        eligible = [
            index
            for index in range(PHASE_H_PARTNER_POOL_SIZE)
            if index != lost_index
            and PHASE_H_EDGE_CAPACITIES[index] - base_edges[index] - allocation[index] > 1e-12
            and PHASE_H_TRAIT_MATCH_SCORES[index] > 0.0
        ]
        if not eligible:
            break
        spare = {
            index: PHASE_H_EDGE_CAPACITIES[index] - base_edges[index] - allocation[index]
            for index in eligible
        }
        weights = {
            index: PHASE_H_TRAIT_MATCH_SCORES[index] * spare[index]
            for index in eligible
        }
        total_weight = sum(weights.values())
        if total_weight <= 0.0:
            break
        proposals = {
            index: remaining * weights[index] / total_weight
            for index in eligible
        }
        used = 0.0
        for index in eligible:
            take = min(spare[index], proposals[index])
            allocation[index] += take
            used += take
        if used <= 1e-12:
            break
        remaining -= used
    return tuple(allocation)


def rewired_target_edges(replicate_index: int) -> tuple[float, ...]:
    lost_index = lost_primary_partner_index(replicate_index)
    base = post_loss_edges(replicate_index)
    lost_effort = PHASE_H_INITIAL_EDGE_STRENGTHS[lost_index]
    allocation = _capacity_constrained_allocation(
        base,
        lost_index,
        PHASE_H_REWIRING_FRACTION * lost_effort,
    )
    target = tuple(edge + extra for edge, extra in zip(base, allocation))
    if abs(sum(allocation) - PHASE_H_REWIRING_FRACTION * lost_effort) > 1e-9:
        raise RuntimeError("Phase-H declared rewiring effort could not be allocated under capacities")
    if target[lost_index] != 0.0:
        raise RuntimeError("lost Phase-H partner cannot receive rewired edge strength")
    return _validate_edges(target)


def _rewiring_progress(generation: int) -> float:
    if generation < 1:
        raise ValueError("network schedule generation must start at one")
    if PHASE_H_REWIRING_WINDOW_GENERATIONS <= 1:
        return 1.0
    if generation <= 1:
        return 0.0
    if generation >= PHASE_H_REWIRING_WINDOW_GENERATIONS:
        return 1.0
    return (generation - 1) / (PHASE_H_REWIRING_WINDOW_GENERATIONS - 1)


def network_edges_at_generation(
    condition: RewiringCondition,
    replicate_index: int,
    generation: int,
) -> tuple[float, ...]:
    if not condition.remove_primary_partner:
        return intact_edges()
    base = post_loss_edges(replicate_index)
    if condition.rewiring_rule == "none":
        return base
    target = rewired_target_edges(replicate_index)
    progress = _rewiring_progress(generation)
    edges = tuple(base_edge + progress * (target_edge - base_edge) for base_edge, target_edge in zip(base, target))
    return _validate_edges(edges)


def functional_support(edges: tuple[float, ...]) -> float:
    _validate_edges(edges)
    return sum(edge * match for edge, match in zip(edges, PHASE_H_TRAIT_MATCH_SCORES))


def intact_functional_support() -> float:
    return functional_support(intact_edges())


def support_multiplier(edges: tuple[float, ...]) -> float:
    baseline = intact_functional_support()
    if baseline <= 0.0:
        raise RuntimeError("Phase-H intact functional support must be positive")
    return min(1.0, functional_support(edges) / baseline)


def active_edge_count(edges: tuple[float, ...]) -> int:
    return sum(edge > 1e-12 for edge in edges)


def network_schedule(
    condition: RewiringCondition,
    replicate_index: int,
    generations: int,
) -> tuple[dict[str, object], ...]:
    if generations < 1:
        raise ValueError("generations must be positive")
    rows = []
    for generation in range(1, generations + 1):
        edges = network_edges_at_generation(condition, replicate_index, generation)
        rows.append({
            "generation": generation,
            "edge_strengths": list(edges),
            "active_edge_count": active_edge_count(edges),
            "candidate_partner_count": PHASE_H_PARTNER_POOL_SIZE,
            "realised_connectance": active_edge_count(edges) / PHASE_H_PARTNER_POOL_SIZE,
            "functional_support": functional_support(edges),
            "support_multiplier": support_multiplier(edges),
        })
    return tuple(rows)


def phase_h_manifest() -> dict[str, object]:
    return {
        "protocol": "warning-blind explicit rewiring Phase H",
        "scientific_scope": "trait_and_capacity_constrained_interaction_rewiring_after_matched_partner_loss",
        "calibration_scope": "source_and_trait_loss_only",
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
            "focal_node_count": 1,
            "candidate_partner_count": PHASE_H_PARTNER_POOL_SIZE,
            "initial_active_partner_count": PHASE_H_PRIMARY_PARTNER_COUNT,
            "initial_edge_strengths": list(PHASE_H_INITIAL_EDGE_STRENGTHS),
            "trait_match_scores": list(PHASE_H_TRAIT_MATCH_SCORES),
            "edge_capacities": list(PHASE_H_EDGE_CAPACITIES),
            "loss_assignment": "lost_primary_partner_index = replicate_index mod 4",
            "rewiring_fraction_of_lost_effort": PHASE_H_REWIRING_FRACTION,
            "rewiring_window_generations": PHASE_H_REWIRING_WINDOW_GENERATIONS,
            "rewiring_allocation_rule": "trait_match_score * spare_edge_capacity with deterministic capacity redistribution",
            "functional_mapping": "sum(edge_strength * trait_match_score), normalized to intact and capped at 1",
        },
        "conditions": [condition.identity() for condition in PHASE_H_CONDITIONS],
        "master_seeds": list(PHASE_H_MASTER_SEEDS),
        "replicates_per_seed": PHASE_H_REPLICATES_PER_SEED,
        "minimum_baseline_eligible_per_seed": PHASE_H_MIN_BASELINE_ELIGIBLE_PER_SEED,
        "prepared_source_count": len(PHASE_H_MASTER_SEEDS) * PHASE_H_REPLICATES_PER_SEED,
        "trajectory_count": len(PHASE_H_CONDITIONS) * len(PHASE_H_MASTER_SEEDS) * PHASE_H_REPLICATES_PER_SEED,
        "paired_across_rewiring_conditions": True,
        "output_scope": "source_projection_network_diagnostics_and_trait_loss_only",
        "blinding_scope": "source_network_and_trait_loss_only",
        "opening_rule": (
            "Interpret rewiring as a rescue test only if the fresh intact control is R4_highrep and the fresh matched "
            "partner-loss/no-rewiring condition is R3_highrep; otherwise record the failed opening without changing "
            "seeds, network scores, capacities, rewiring fraction, rewiring window, or thresholds."
        ),
        "rescue_rule": (
            "If the opening rule is satisfied, classify the predeclared rewiring condition once: R4_highrep is a bounded "
            "rescue of warning estimability; any other regime is not a rescue."
        ),
        "stop_rule": (
            "Do not tune trait-match scores, edge capacities, candidate partners, rewiring fraction, rewiring window, "
            "loss identity, seeds, or R4 thresholds after observing the Phase-H result."
        ),
        "interpretation_boundary": (
            "Phase H is an explicit one-focal-node interaction-network closure with fixed partner availability. It does "
            "not model partner population dynamics, coextinction, pollen/seed movement, demographic movement, or "
            "pollinator movement and must not be interpreted as a universal ecological-network rescue theorem."
        ),
    }
