"""Finite-sample validity audit for the historical R4 all-block gate.

The historical warning-evaluability screen labels a five-block candidate R4 only
when every observed block loss rate lies in [0.30, 0.70].  At finite block
sizes this rule can fail even when all blocks share the same latent Bernoulli
loss probability.  This module quantifies that sampling-only failure probability
and audits the Phase-H / Phase-I partner-loss blocks for evidence of excess
between-block heterogeneity.

This is a diagnostic of the operational gate.  It does not overwrite historical
R1-R4 labels and does not assume the simulator is literally a homogeneous
Bernoulli process.  The homogeneous-binomial model is a reference null used to
ask whether R3 by itself identifies biological seed heterogeneity.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil, comb, exp, factorial, floor
from typing import Iterable

R4_LOWER = 0.30
R4_UPPER = 0.70
PHASE_J_P_GRID = tuple(index / 100.0 for index in range(30, 71, 5))
PHASE_J_BLOCK_SIZES = (17, 18, 19, 20, 50, 100)

# Locked observed blocks from the prospectively run Phase H and Phase I
# partner-loss/no-rescue conditions.  Each tuple is (losses, eligible).
PHASE_H_PARTNER_LOSS_BLOCKS = ((9, 18), (8, 17), (9, 17), (6, 17), (5, 17))
PHASE_I_PARTNER_LOSS_BLOCKS = ((7, 17), (8, 18), (11, 19), (9, 18), (9, 18))


@dataclass(frozen=True)
class GateAudit:
    name: str
    blocks: tuple[tuple[int, int], ...]
    pooled_loss_rate: float
    observed_gate_pass: bool
    historical_regime: str
    homogeneous_reference_gate_pass_probability: float
    homogeneous_reference_gate_fail_probability: float
    pearson_equal_rate_statistic: float
    pearson_equal_rate_df: int
    pearson_equal_rate_p_value: float

    def as_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "blocks": [
                {"losses": losses, "eligible": eligible, "rate": losses / eligible}
                for losses, eligible in self.blocks
            ],
            "pooled_loss_rate": self.pooled_loss_rate,
            "observed_gate_pass": self.observed_gate_pass,
            "historical_regime": self.historical_regime,
            "homogeneous_reference_gate_pass_probability": self.homogeneous_reference_gate_pass_probability,
            "homogeneous_reference_gate_fail_probability": self.homogeneous_reference_gate_fail_probability,
            "pearson_equal_rate_statistic": self.pearson_equal_rate_statistic,
            "pearson_equal_rate_df": self.pearson_equal_rate_df,
            "pearson_equal_rate_p_value": self.pearson_equal_rate_p_value,
        }


def accepted_loss_count_bounds(n: int) -> tuple[int, int]:
    if n < 1:
        raise ValueError("block size must be positive")
    return ceil(R4_LOWER * n - 1e-12), floor(R4_UPPER * n + 1e-12)


def block_gate_pass_probability(n: int, p: float) -> float:
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must lie in [0, 1]")
    low, high = accepted_loss_count_bounds(n)
    return sum(
        comb(n, k) * (p**k) * ((1.0 - p) ** (n - k))
        for k in range(low, high + 1)
    )


def ensemble_gate_pass_probability(block_sizes: Iterable[int], p: float) -> float:
    probability = 1.0
    count = 0
    for n in block_sizes:
        probability *= block_gate_pass_probability(int(n), p)
        count += 1
    if count == 0:
        raise ValueError("at least one block is required")
    return probability


def observed_gate_pass(blocks: Iterable[tuple[int, int]]) -> bool:
    rows = tuple(blocks)
    if not rows:
        raise ValueError("at least one block is required")
    for losses, eligible in rows:
        if eligible < 1 or losses < 0 or losses > eligible:
            raise ValueError("invalid loss/eligible count")
        rate = losses / eligible
        if rate < R4_LOWER or rate > R4_UPPER:
            return False
    return True


def pooled_rate(blocks: Iterable[tuple[int, int]]) -> float:
    rows = tuple(blocks)
    losses = sum(row[0] for row in rows)
    eligible = sum(row[1] for row in rows)
    if eligible < 1:
        raise ValueError("pooled eligible count must be positive")
    return losses / eligible


def _chi_square_sf_even_df(statistic: float, df: int) -> float:
    """Exact chi-square survival function for positive even degrees of freedom."""
    if statistic < 0.0:
        raise ValueError("chi-square statistic must be nonnegative")
    if df < 2 or df % 2:
        raise ValueError("this closed-form helper requires positive even df")
    x = statistic / 2.0
    terms = df // 2
    return exp(-x) * sum((x**j) / factorial(j) for j in range(terms))


def pearson_equal_rate_test(blocks: Iterable[tuple[int, int]]) -> tuple[float, int, float]:
    """Pearson test of equal loss probability across independent blocks.

    Expected loss/non-loss counts are computed from the pooled rate.  The Phase-H
    and Phase-I audits each have five blocks, hence df=4 and the exact even-df
    chi-square survival form above applies.
    """
    rows = tuple(blocks)
    if len(rows) < 2:
        raise ValueError("at least two blocks are required")
    p = pooled_rate(rows)
    if p <= 0.0 or p >= 1.0:
        raise ValueError("pooled rate must lie strictly inside (0,1)")
    statistic = 0.0
    for losses, eligible in rows:
        nonlosses = eligible - losses
        expected_loss = eligible * p
        expected_nonloss = eligible * (1.0 - p)
        statistic += ((losses - expected_loss) ** 2) / expected_loss
        statistic += ((nonlosses - expected_nonloss) ** 2) / expected_nonloss
    df = len(rows) - 1
    p_value = _chi_square_sf_even_df(statistic, df)
    return statistic, df, p_value


def audit_observed_blocks(name: str, blocks: tuple[tuple[int, int], ...], historical_regime: str) -> GateAudit:
    p = pooled_rate(blocks)
    sizes = tuple(eligible for _, eligible in blocks)
    gate_pass_probability = ensemble_gate_pass_probability(sizes, p)
    statistic, df, p_value = pearson_equal_rate_test(blocks)
    return GateAudit(
        name=name,
        blocks=blocks,
        pooled_loss_rate=p,
        observed_gate_pass=observed_gate_pass(blocks),
        historical_regime=historical_regime,
        homogeneous_reference_gate_pass_probability=gate_pass_probability,
        homogeneous_reference_gate_fail_probability=1.0 - gate_pass_probability,
        pearson_equal_rate_statistic=statistic,
        pearson_equal_rate_df=df,
        pearson_equal_rate_p_value=p_value,
    )


def phase_j_audit() -> dict[str, object]:
    phase_h = audit_observed_blocks("phase_h_partner_loss_no_rewiring", PHASE_H_PARTNER_LOSS_BLOCKS, "R3_highrep")
    phase_i = audit_observed_blocks("phase_i_partner_loss_no_rescue", PHASE_I_PARTNER_LOSS_BLOCKS, "R4_highrep")
    calibration = []
    for n in PHASE_J_BLOCK_SIZES:
        for p in PHASE_J_P_GRID:
            pass_probability = block_gate_pass_probability(n, p) ** 5
            calibration.append({
                "eligible_per_block": n,
                "latent_homogeneous_loss_probability": p,
                "five_block_gate_pass_probability": pass_probability,
                "five_block_gate_fail_probability": 1.0 - pass_probability,
            })
    return {
        "stage": "R4 finite-sample gate validity Phase J",
        "scope": "historical_gate_diagnostic_not_reclassification",
        "historical_r4_rule": {
            "block_count": 5,
            "lower": R4_LOWER,
            "upper": R4_UPPER,
            "rule": "all observed block loss rates must lie inside [0.30,0.70]",
        },
        "observed_audits": [phase_h.as_dict(), phase_i.as_dict()],
        "sampling_calibration": calibration,
        "interpretation_rule": (
            "An R3 gate failure does not by itself identify biological seed heterogeneity if the same outcome is plausible under "
            "a homogeneous-binomial reference at the observed finite block sizes. Historical R1-R4 labels remain immutable protocol facts."
        ),
        "claim_boundary": (
            "Phase J audits the finite-sample behaviour of the R4 classifier. It does not prove simulator trajectories are iid Bernoulli, "
            "does not retroactively change the R4 band, and does not use genetic-warning outcomes."
        ),
    }
