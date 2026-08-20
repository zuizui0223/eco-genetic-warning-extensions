"""Warning-blind condition mapping for locked Protocol 002 Stage II batches.

This module reuses only trait-loss calibration fields. It never inspects genetic
diversity, warning timing, lead/lag, or event-pair outcomes. Its purpose is to
map which declared ecological/transition conditions produced rapid loss,
persistence, seed heterogeneity, or an eligible intermediate-risk event regime.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median
from typing import Any, Iterable

from .protocol002_calibration import (
    ELIGIBLE_TRAIT_LOSS_RATE_MAX,
    ELIGIBLE_TRAIT_LOSS_RATE_MIN,
    assert_protocol002_blind_calibration_columns,
)

EXPECTED_BATCH_COUNT = 810
EXPECTED_COMPLETE_CANDIDATES = 648

FACTOR_ORDER = (
    "kappa_mu",
    "p_star",
    "area_reference",
    "kappa",
    "horizon",
    "normalised_barrier_increase",
)


def _band_distance(rate: float) -> float:
    if rate < ELIGIBLE_TRAIT_LOSS_RATE_MIN:
        return ELIGIBLE_TRAIT_LOSS_RATE_MIN - rate
    if rate > ELIGIBLE_TRAIT_LOSS_RATE_MAX:
        return rate - ELIGIBLE_TRAIT_LOSS_RATE_MAX
    return 0.0


def classify_seed_rates(rates: tuple[float, ...]) -> str:
    """Classify one complete five-seed candidate using the locked Protocol 002 band."""
    if all(ELIGIBLE_TRAIT_LOSS_RATE_MIN <= rate <= ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in rates):
        return "warning_evaluable"
    if all(rate > ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in rates):
        return "rapid_loss"
    if all(rate < ELIGIBLE_TRAIT_LOSS_RATE_MIN for rate in rates):
        return "persistence"
    return "seed_heterogeneous"


def candidate_from_batch(batch: dict[str, Any]) -> dict[str, Any] | None:
    """Extract one warning-blind complete-candidate record from a Stage II batch."""
    assert_protocol002_blind_calibration_columns(batch.keys())
    seed_blocks = batch.get("seed_blocks", [])
    rates_raw = tuple(block.get("trait_loss_rate") for block in seed_blocks)
    if len(rates_raw) != 5 or any(rate is None for rate in rates_raw):
        return None
    rates = tuple(float(rate) for rate in rates_raw)
    cell = batch["cell"]
    pooled = float(batch.get("pooled_trait_loss_rate", sum(rates) / len(rates)))
    row = {
        "batch_index": int(cell["batch_index"]),
        "kappa_mu": float(cell["kappa_mu"]),
        "p_star": float(cell["p_star"]),
        "area_reference": float(cell["area_reference"]),
        "kappa": float(cell["kappa"]),
        "horizon": int(cell["horizon"]),
        "normalised_barrier_increase": float(cell["normalised_barrier_increase"]),
        "seed_block_trait_loss_rates": list(rates),
        "pooled_trait_loss_rate": pooled,
        "seed_range": max(rates) - min(rates),
        "regime": classify_seed_rates(rates),
        "inside_band_seed_count": sum(
            ELIGIBLE_TRAIT_LOSS_RATE_MIN <= rate <= ELIGIBLE_TRAIT_LOSS_RATE_MAX for rate in rates
        ),
        "total_distance_to_band": sum(_band_distance(rate) for rate in rates),
        "maximum_distance_to_band": max(_band_distance(rate) for rate in rates),
        "pooled_distance_to_half": abs(pooled - 0.5),
    }
    return row


def _factor_summary(rows: tuple[dict[str, Any], ...], factor: str) -> list[dict[str, Any]]:
    grouped: dict[float | int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row[factor]].append(row)
    output: list[dict[str, Any]] = []
    for value in sorted(grouped):
        subset = grouped[value]
        regimes = Counter(row["regime"] for row in subset)
        output.append(
            {
                "value": value,
                "candidate_count": len(subset),
                "mean_pooled_trait_loss_rate": sum(row["pooled_trait_loss_rate"] for row in subset) / len(subset),
                "median_pooled_trait_loss_rate": median(row["pooled_trait_loss_rate"] for row in subset),
                "mean_seed_range": sum(row["seed_range"] for row in subset) / len(subset),
                "mean_total_distance_to_band": sum(row["total_distance_to_band"] for row in subset) / len(subset),
                "regime_counts": dict(sorted(regimes.items())),
            }
        )
    return output


def _adjacent_effects(rows: tuple[dict[str, Any], ...], factor: str) -> list[dict[str, Any]]:
    """Return matched adjacent-level pooled-loss contrasts for one factor."""
    levels = sorted({row[factor] for row in rows})
    other_factors = tuple(name for name in FACTOR_ORDER if name != factor)
    indexed = {
        tuple(row[name] for name in FACTOR_ORDER): row
        for row in rows
    }
    output: list[dict[str, Any]] = []
    for low, high in zip(levels, levels[1:]):
        deltas: list[float] = []
        for row in rows:
            if row[factor] != low:
                continue
            key_values = {name: row[name] for name in FACTOR_ORDER}
            key_values[factor] = high
            key = tuple(key_values[name] for name in FACTOR_ORDER)
            partner = indexed.get(key)
            if partner is None:
                continue
            deltas.append(partner["pooled_trait_loss_rate"] - row["pooled_trait_loss_rate"])
        output.append(
            {
                "low": low,
                "high": high,
                "matched_pair_count": len(deltas),
                "median_delta_pooled_trait_loss_rate": median(deltas) if deltas else None,
                "mean_delta_pooled_trait_loss_rate": (sum(deltas) / len(deltas)) if deltas else None,
                "positive_count": sum(delta > 0 for delta in deltas),
                "negative_count": sum(delta < 0 for delta in deltas),
                "zero_count": sum(delta == 0 for delta in deltas),
            }
        )
    return output


def _coordinate_summary(rows: tuple[dict[str, Any], ...]) -> list[dict[str, Any]]:
    grouped: dict[tuple[float, float], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(row["kappa_mu"], row["p_star"])].append(row)
    output: list[dict[str, Any]] = []
    for (kappa_mu, p_star), subset in sorted(grouped.items()):
        regimes = Counter(row["regime"] for row in subset)
        closest = min(
            subset,
            key=lambda row: (
                row["total_distance_to_band"],
                row["maximum_distance_to_band"],
                row["seed_range"],
                row["pooled_distance_to_half"],
                row["horizon"],
                row["normalised_barrier_increase"],
                row["area_reference"],
                row["kappa"],
                row["batch_index"],
            ),
        )
        output.append(
            {
                "kappa_mu": kappa_mu,
                "p_star": p_star,
                "candidate_count": len(subset),
                "mean_pooled_trait_loss_rate": sum(row["pooled_trait_loss_rate"] for row in subset) / len(subset),
                "mean_seed_range": sum(row["seed_range"] for row in subset) / len(subset),
                "regime_counts": dict(sorted(regimes.items())),
                "closest_candidate_to_evaluable_band": closest,
            }
        )
    return output


def condition_map(batch_files: Iterable[str | Path]) -> dict[str, Any]:
    paths = tuple(sorted(Path(path) for path in batch_files))
    if len(paths) != EXPECTED_BATCH_COUNT:
        raise ValueError(f"expected {EXPECTED_BATCH_COUNT} Stage II batch files, found {len(paths)}")

    complete_rows: list[dict[str, Any]] = []
    incomplete_count = 0
    for path in paths:
        batch = json.loads(path.read_text(encoding="utf-8"))
        row = candidate_from_batch(batch)
        if row is None:
            incomplete_count += 1
        else:
            complete_rows.append(row)

    rows = tuple(complete_rows)
    if len(rows) != EXPECTED_COMPLETE_CANDIDATES:
        raise ValueError(
            f"expected {EXPECTED_COMPLETE_CANDIDATES} complete five-seed candidates, found {len(rows)}"
        )

    regimes = Counter(row["regime"] for row in rows)
    closest_global = sorted(
        rows,
        key=lambda row: (
            row["total_distance_to_band"],
            row["maximum_distance_to_band"],
            row["seed_range"],
            row["pooled_distance_to_half"],
            row["horizon"],
            row["normalised_barrier_increase"],
            row["area_reference"],
            row["kappa"],
            row["kappa_mu"],
            row["p_star"],
            row["batch_index"],
        ),
    )[:20]

    return {
        "stage": "Protocol 002 warning-blind condition map from locked Stage II batches",
        "batch_count": len(paths),
        "complete_candidate_count": len(rows),
        "incomplete_candidate_count": incomplete_count,
        "eligibility_band": [ELIGIBLE_TRAIT_LOSS_RATE_MIN, ELIGIBLE_TRAIT_LOSS_RATE_MAX],
        "warning_fields_inspected": False,
        "diversity_fields_inspected": False,
        "selection_rule_changed": False,
        "global_regime_counts": dict(sorted(regimes.items())),
        "coordinate_summaries": _coordinate_summary(rows),
        "factor_summaries": {factor: _factor_summary(rows, factor) for factor in FACTOR_ORDER},
        "adjacent_factor_effects": {factor: _adjacent_effects(rows, factor) for factor in FACTOR_ORDER},
        "closest_candidates_to_evaluable_band": closest_global,
        "interpretation_boundary": (
            "This artifact diagnoses condition structure inside the already completed Protocol 002 grid. "
            "It does not select a warning domain, inspect warning/diversity outcomes, or establish that an "
            "evaluable regime exists outside the tested candidate family."
        ),
    }


def write_condition_map(batch_root: str | Path, output: str | Path) -> Path:
    root = Path(batch_root)
    files = sorted(root.rglob("batch_*.json"))
    artifact = condition_map(files)
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
