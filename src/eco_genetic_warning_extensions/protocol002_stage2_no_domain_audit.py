"""Trait-loss-only diagnostics for Protocol 002 Stage II no-domain outcomes.

This module does not alter calibration eligibility or ranking. It only describes
why completed candidate cells failed the predeclared seed-block eligibility band.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from .protocol002_calibration import (
    ELIGIBLE_TRAIT_LOSS_RATE_MAX,
    ELIGIBLE_TRAIT_LOSS_RATE_MIN,
    assert_protocol002_blind_calibration_columns,
)


def _band_distance(rate: float) -> float:
    if rate < ELIGIBLE_TRAIT_LOSS_RATE_MIN:
        return ELIGIBLE_TRAIT_LOSS_RATE_MIN - rate
    if rate > ELIGIBLE_TRAIT_LOSS_RATE_MAX:
        return rate - ELIGIBLE_TRAIT_LOSS_RATE_MAX
    return 0.0


def _pattern(rates: tuple[float, ...]) -> str:
    below = sum(rate < ELIGIBLE_TRAIT_LOSS_RATE_MIN for rate in rates)
    inside = sum(ELIGIBLE_TRAIT_LOSS_RATE_MIN <= rate <= ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in rates)
    above = sum(rate > ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in rates)
    if below == len(rates):
        return "all_below_band"
    if above == len(rates):
        return "all_above_band"
    if inside == len(rates):
        return "eligible"
    return "mixed_across_band"


def _candidate_row(batch: dict[str, Any]) -> dict[str, Any] | None:
    seed_blocks = batch.get("seed_blocks", [])
    rates = tuple(block.get("trait_loss_rate") for block in seed_blocks)
    if len(rates) != 5 or any(rate is None for rate in rates):
        return None
    values = tuple(float(rate) for rate in rates)
    cell = batch["cell"]
    pooled = float(batch["pooled_trait_loss_rate"])
    return {
        "batch_index": int(cell["batch_index"]),
        "kappa_mu": float(cell["kappa_mu"]),
        "p_star": float(cell["p_star"]),
        "area_reference": float(cell["area_reference"]),
        "kappa": float(cell["kappa"]),
        "horizon": int(cell["horizon"]),
        "normalised_barrier_increase": float(cell["normalised_barrier_increase"]),
        "seed_block_trait_loss_rates": list(values),
        "pooled_trait_loss_rate": pooled,
        "eligibility_pattern": _pattern(values),
        "total_distance_to_band": sum(_band_distance(rate) for rate in values),
        "maximum_distance_to_band": max(_band_distance(rate) for rate in values),
        "inside_band_seed_count": sum(
            ELIGIBLE_TRAIT_LOSS_RATE_MIN <= rate <= ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in values
        ),
    }


def audit_stage2_no_domain(batch_files: Iterable[str | Path]) -> dict[str, Any]:
    paths = sorted(Path(path) for path in batch_files)
    if len(paths) != 810:
        raise ValueError(f"expected 810 Stage II batch files, found {len(paths)}")

    candidates_by_coordinate: dict[tuple[float, float], list[dict[str, Any]]] = defaultdict(list)
    incomplete_by_coordinate: Counter[tuple[float, float]] = Counter()

    for path in paths:
        batch = json.loads(path.read_text(encoding="utf-8"))
        assert_protocol002_blind_calibration_columns(batch.keys())
        cell = batch["cell"]
        coordinate = (float(cell["kappa_mu"]), float(cell["p_star"]))
        row = _candidate_row(batch)
        if row is None:
            incomplete_by_coordinate[coordinate] += 1
        else:
            candidates_by_coordinate[coordinate].append(row)

    coordinate_results = []
    global_patterns: Counter[str] = Counter()
    for coordinate in sorted(set(candidates_by_coordinate) | set(incomplete_by_coordinate)):
        candidates = candidates_by_coordinate[coordinate]
        pattern_counts = Counter(candidate["eligibility_pattern"] for candidate in candidates)
        global_patterns.update(pattern_counts)
        closest = min(
            candidates,
            key=lambda candidate: (
                candidate["total_distance_to_band"],
                candidate["maximum_distance_to_band"],
                abs(candidate["pooled_trait_loss_rate"] - 0.50),
                candidate["horizon"],
                candidate["normalised_barrier_increase"],
                candidate["area_reference"],
                candidate["kappa"],
                candidate["batch_index"],
            ),
        )
        coordinate_results.append(
            {
                "kappa_mu": coordinate[0],
                "p_star": coordinate[1],
                "complete_candidate_count": len(candidates),
                "incomplete_candidate_count": incomplete_by_coordinate[coordinate],
                "pattern_counts": dict(sorted(pattern_counts.items())),
                "closest_candidate_to_predeclared_band": closest,
            }
        )

    return {
        "stage": "Protocol 002 Stage II no-domain trait-loss-only diagnostic audit",
        "batch_count": len(paths),
        "coordinate_count": len(coordinate_results),
        "eligibility_band": [ELIGIBLE_TRAIT_LOSS_RATE_MIN, ELIGIBLE_TRAIT_LOSS_RATE_MAX],
        "selection_rule_changed": False,
        "warning_fields_inspected": False,
        "diversity_fields_inspected": False,
        "global_pattern_counts": dict(sorted(global_patterns.items())),
        "coordinates": coordinate_results,
    }


def write_stage2_no_domain_audit(batch_root: str | Path, output: str | Path) -> Path:
    root = Path(batch_root)
    files = sorted(root.rglob("batch_*.json"))
    artifact = audit_stage2_no_domain(files)
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
