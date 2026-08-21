"""Exact diagnostics for the legacy all-block R4 calibration gate.

The historical R4 rule labels a panel warning-evaluable only when every seed
block's observed trait-loss rate lies in the fixed interval [0.30, 0.70].  This
module records the design consequence of that rule separately from biological
parameter effects.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import sqrt
from typing import Iterable

from .protocol002_condition_map import classify_seed_rates


def all_block_gate_pass_probability(block_pass_probability: float, panel_size: int) -> float:
    """Return q**B for B independent blocks each passing with probability q."""
    q = float(block_pass_probability)
    if not 0.0 <= q <= 1.0:
        raise ValueError("block_pass_probability must lie in [0, 1]")
    if panel_size < 1:
        raise ValueError("panel_size must be positive")
    return q ** panel_size


def wilson_interval(successes: int, total: int, *, z: float = 1.959963984540054) -> tuple[float, float]:
    """Return the two-sided Wilson interval for a binomial pass fraction."""
    if total < 1 or not 0 <= successes <= total:
        raise ValueError("require 0 <= successes <= total with total positive")
    p = successes / total
    z2 = z * z
    denominator = 1.0 + z2 / total
    centre = (p + z2 / (2.0 * total)) / denominator
    half = z * sqrt(p * (1.0 - p) / total + z2 / (4.0 * total * total)) / denominator
    return max(0.0, centre - half), min(1.0, centre + half)


def enumerate_panel_regimes(seed_rates: Iterable[float], *, panel_size: int = 5) -> dict[str, object]:
    """Enumerate every unordered fixed-size panel under the unchanged classifier."""
    rates = tuple(float(rate) for rate in seed_rates)
    if panel_size < 1 or panel_size > len(rates):
        raise ValueError("panel_size must lie between one and the number of seed rates")
    if any(rate < 0.0 or rate > 1.0 for rate in rates):
        raise ValueError("seed rates must lie in [0, 1]")

    counts: Counter[str] = Counter()
    total = 0
    for panel in combinations(rates, panel_size):
        counts[classify_seed_rates(panel)] += 1
        total += 1
    return {
        "seed_block_count": len(rates),
        "panel_size": panel_size,
        "panel_count": total,
        "regime_counts": dict(sorted(counts.items())),
        "regime_fractions": {
            key: value / total for key, value in sorted(counts.items())
        },
    }


def legacy_gate_design_statement() -> str:
    return (
        "For independent seed blocks with single-block pass probability q, the historical all-block R4 gate passes a "
        "B-block panel with probability q**B. Unless q is exactly 0 or 1, the categorical pass probability therefore "
        "depends mechanically on panel size and cannot by itself define a sample-size-invariant biological state."
    )
