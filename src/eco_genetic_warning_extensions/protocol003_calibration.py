"""Protocol 003 independent trait-loss-only calibration.

This module reuses the validated Protocol 003 trajectory runner with a separately
locked candidate grid and seed family. It does not calculate warning endpoints.
"""
from __future__ import annotations

from contextlib import ExitStack
from pathlib import Path
from typing import Any
from unittest.mock import patch

from .mutation_coordinates import MutationCoordinates
from . import protocol003_bracket_pilot as bracket

CALIBRATION_MASTER_SEEDS = (20270610, 20270611, 20270612, 20270613, 20270614)
CALIBRATION_REPLICATES_PER_SEED = 5


def protocol003_calibration_cells() -> tuple[bracket.Protocol003BracketCell, ...]:
    definitions = (
        ("symmetric_bridge", MutationCoordinates(0.20, 0.50), 0.8, 6.0, 210, 0.20),
        ("symmetric_bridge", MutationCoordinates(0.20, 0.50), 0.8, 6.0, 300, 0.30),
        ("transition", MutationCoordinates(0.05, 0.90), 1.0, 4.5, 90, 0.10),
        ("transition", MutationCoordinates(0.05, 0.90), 1.0, 4.5, 90, 0.15),
    )
    return tuple(
        bracket.Protocol003BracketCell(
            cell_index=index,
            label=label,
            coordinate=coordinate,
            area_reference=area_reference,
            kappa=kappa,
            hold_generations=hold,
            normalised_barrier_increase=increase,
        )
        for index, (label, coordinate, area_reference, kappa, hold, increase) in enumerate(definitions)
    )


def run_protocol003_calibration_cell(upstream_checkout: str | Path, cell_index: int) -> dict[str, Any]:
    cells = protocol003_calibration_cells()
    with ExitStack() as stack:
        stack.enter_context(patch.object(bracket, "BRACKET_MASTER_SEEDS", CALIBRATION_MASTER_SEEDS))
        stack.enter_context(patch.object(bracket, "BRACKET_REPLICATES_PER_CELL", CALIBRATION_REPLICATES_PER_SEED))
        stack.enter_context(patch.object(bracket, "protocol003_bracket_cells", lambda: cells))
        artifact = bracket.run_protocol003_bracket_cell(upstream_checkout, cell_index)

    attempts = artifact["attempts"]
    seed_blocks = []
    for seed in CALIBRATION_MASTER_SEEDS:
        eligible = [row for row in attempts if row["master_seed"] == seed and row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        seed_blocks.append({
            "master_seed": seed,
            "baseline_eligible_count": len(eligible),
            "trait_loss_count": len(losses),
            "trait_loss_rate": None if not eligible else len(losses) / len(eligible),
        })

    pooled = artifact["pooled_trait_loss_rate"]
    complete_blocks = all(block["baseline_eligible_count"] >= 3 for block in seed_blocks)
    acceptable_blocks = sum(
        block["trait_loss_rate"] is not None and 0.20 <= block["trait_loss_rate"] <= 0.80
        for block in seed_blocks
    )
    eligible = bool(
        pooled is not None
        and 0.30 <= float(pooled) <= 0.70
        and complete_blocks
        and acceptable_blocks >= 4
    )

    artifact["stage"] = "Protocol 003 independent trait-loss-only calibration cell"
    artifact["design"] = {
        "master_seeds": list(CALIBRATION_MASTER_SEEDS),
        "replicates_per_seed": CALIBRATION_REPLICATES_PER_SEED,
        "endpoint_contract": "trait_loss_only",
        "candidate_count": len(cells),
    }
    artifact["seed_blocks"] = seed_blocks
    artifact["calibration_eligible"] = eligible
    artifact["domain_selected"] = False
    artifact["type_s_result_claimed"] = False
    return artifact
