"""Precision audit for selected high-replication bounded-negative results."""
from __future__ import annotations

import json
import math
from pathlib import Path
from statistics import NormalDist
from typing import Any

Z_95 = NormalDist().inv_cdf(0.975)


def wilson_interval(events: int, eligible: int) -> dict[str, Any]:
    if eligible <= 0 or events < 0 or events > eligible:
        raise ValueError("invalid event denominator")
    p = events / eligible
    denominator = 1 + Z_95**2 / eligible
    center = (p + Z_95**2 / (2 * eligible)) / denominator
    half = Z_95 * math.sqrt(
        p * (1 - p) / eligible + Z_95**2 / (4 * eligible**2)
    ) / denominator
    return {
        "events": events,
        "eligible": eligible,
        "risk": p,
        "wilson_95_ci": [max(0.0, center - half), min(1.0, center + half)],
    }


def paired_risk_difference_interval(
    comparable: int, loss_to_no_loss: int, no_loss_to_loss: int
) -> dict[str, Any]:
    """Normal CI for the mean paired binary difference.

    Each trajectory contributes -1, 0, or +1 for comparison-minus-reference.
    The interval therefore uses the paired trajectory as the unit and does not
    mistake the two condition totals for independent binomial samples.
    """
    if comparable <= 1:
        raise ValueError("paired comparison requires at least two trajectories")
    if min(loss_to_no_loss, no_loss_to_loss) < 0:
        raise ValueError("discordant counts must be non-negative")
    if loss_to_no_loss + no_loss_to_loss > comparable:
        raise ValueError("discordant counts exceed comparable trajectories")
    difference = (no_loss_to_loss - loss_to_no_loss) / comparable
    sum_squares = loss_to_no_loss + no_loss_to_loss
    sample_variance = (sum_squares - comparable * difference**2) / (comparable - 1)
    standard_error = math.sqrt(sample_variance / comparable)
    return {
        "comparable_trajectories": comparable,
        "loss_to_no_loss": loss_to_no_loss,
        "no_loss_to_loss": no_loss_to_loss,
        "risk_difference_comparison_minus_reference": difference,
        "paired_normal_95_ci": [
            max(-1.0, difference - Z_95 * standard_error),
            min(1.0, difference + Z_95 * standard_error),
        ],
        "standard_error": standard_error,
    }


def audit(source: dict[str, Any]) -> dict[str, Any]:
    phases: dict[str, Any] = {}
    for phase, phase_data in source["phases"].items():
        conditions = {
            name: wilson_interval(int(values["events"]), int(values["eligible"]))
            for name, values in phase_data["conditions"].items()
        }
        comparisons: dict[str, Any] = {}
        for name, values in phase_data["paired_comparisons"].items():
            paired = paired_risk_difference_interval(
                int(values["comparable"]),
                int(values["loss_to_no_loss"]),
                int(values["no_loss_to_loss"]),
            )
            paired.update(
                {
                    "reference": values["reference"],
                    "comparison": values["comparison"],
                    "exact_mcnemar_p": values["exact_mcnemar_p"],
                }
            )
            comparisons[name] = paired
        phases[phase] = {
            "scope": phase_data["scope"],
            "provenance": phase_data["provenance"],
            "condition_risk_95_ci": conditions,
            "paired_effect_95_ci": comparisons,
        }
    return {
        "analysis": "precision bounds for selected bounded-negative results",
        "claim_class": "precision-bounded null; not equivalence",
        "methods": {
            "condition_risk": "two-sided 95% Wilson interval on the observed eligible trajectory denominator",
            "paired_effect": (
                "comparison-minus-reference paired risk difference with a two-sided 95% normal interval "
                "from whole-trajectory {-1,0,+1} differences"
            ),
            "interpretation": (
                "Failure to detect a difference does not establish equivalence. The confidence interval states "
                "which paired marginal-risk differences remain compatible with the fixed trials."
            ),
        },
        "phases": phases,
    }


def write_output(result: dict[str, Any], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
