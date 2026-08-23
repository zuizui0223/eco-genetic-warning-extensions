"""Extract warning-blind matched p_star brackets from locked Protocol 002 batches."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from .mutation_coordinates import PRIMARY_P_STAR
from .protocol002_condition_map import (
    EXPECTED_BATCH_COUNT,
    EXPECTED_COMPLETE_CANDIDATES,
    candidate_from_batch,
)


def _bracket_type(low_regime: str, high_regime: str) -> str | None:
    if low_regime == "rapid_loss" and high_regime == "seed_heterogeneous":
        return "rapid_to_heterogeneous"
    if low_regime == "rapid_loss" and high_regime == "persistence":
        return "rapid_to_persistence"
    if low_regime == "seed_heterogeneous" and high_regime == "persistence":
        return "heterogeneous_to_persistence"
    return None


def frontier_brackets(batch_files: Iterable[str | Path]) -> dict[str, Any]:
    paths = tuple(sorted(Path(path) for path in batch_files))
    if len(paths) != EXPECTED_BATCH_COUNT:
        raise ValueError(f"expected {EXPECTED_BATCH_COUNT} Stage II batch files, found {len(paths)}")

    rows = []
    for path in paths:
        row = candidate_from_batch(json.loads(path.read_text(encoding="utf-8")))
        if row is not None:
            rows.append(row)
    if len(rows) != EXPECTED_COMPLETE_CANDIDATES:
        raise ValueError(f"expected {EXPECTED_COMPLETE_CANDIDATES} complete candidates, found {len(rows)}")

    grouped: dict[tuple[float, float, float, int, float], dict[float, dict[str, Any]]] = defaultdict(dict)
    for row in rows:
        key = (
            row["kappa_mu"],
            row["area_reference"],
            row["kappa"],
            row["horizon"],
            row["normalised_barrier_increase"],
        )
        grouped[key][row["p_star"]] = row

    adjacent = tuple(zip(PRIMARY_P_STAR, PRIMARY_P_STAR[1:]))
    brackets = []
    for key, by_pstar in grouped.items():
        kappa_mu, area_reference, kappa, horizon, barrier = key
        for low_pstar, high_pstar in adjacent:
            low = by_pstar.get(low_pstar)
            high = by_pstar.get(high_pstar)
            if low is None or high is None:
                continue
            kind = _bracket_type(low["regime"], high["regime"])
            if kind is None:
                continue
            brackets.append(
                {
                    "bracket_type": kind,
                    "kappa_mu": kappa_mu,
                    "area_reference": area_reference,
                    "kappa": kappa,
                    "horizon": horizon,
                    "normalised_barrier_increase": barrier,
                    "low_p_star": low_pstar,
                    "high_p_star": high_pstar,
                    "low_regime": low["regime"],
                    "high_regime": high["regime"],
                    "low_pooled_trait_loss_rate": low["pooled_trait_loss_rate"],
                    "high_pooled_trait_loss_rate": high["pooled_trait_loss_rate"],
                    "delta_pooled_trait_loss_rate": high["pooled_trait_loss_rate"] - low["pooled_trait_loss_rate"],
                    "low_seed_rates": low["seed_block_trait_loss_rates"],
                    "high_seed_rates": high["seed_block_trait_loss_rates"],
                    "low_distance_to_band": low["total_distance_to_band"],
                    "high_distance_to_band": high["total_distance_to_band"],
                    "combined_distance_to_band": low["total_distance_to_band"] + high["total_distance_to_band"],
                    "low_batch_index": low["batch_index"],
                    "high_batch_index": high["batch_index"],
                }
            )

    brackets.sort(
        key=lambda row: (
            row["combined_distance_to_band"],
            abs(row["low_pooled_trait_loss_rate"] - 0.5) + abs(row["high_pooled_trait_loss_rate"] - 0.5),
            row["high_p_star"] - row["low_p_star"],
            row["kappa_mu"],
            row["horizon"],
            row["area_reference"],
            row["kappa"],
            row["normalised_barrier_increase"],
        )
    )

    type_counts: dict[str, int] = defaultdict(int)
    for row in brackets:
        type_counts[row["bracket_type"]] += 1

    return {
        "stage": "Protocol 002 warning-blind matched recurrent-transition frontier brackets",
        "batch_count": len(paths),
        "complete_candidate_count": len(rows),
        "warning_fields_inspected": False,
        "diversity_fields_inspected": False,
        "primary_p_star_levels": list(PRIMARY_P_STAR),
        "bracket_count": len(brackets),
        "bracket_type_counts": dict(sorted(type_counts.items())),
        "brackets": brackets,
        "interpretation_boundary": (
            "Brackets compare adjacent declared p_star levels with kappa_mu, A_ref, interaction kappa, "
            "horizon and barrier increase held identical. They locate finite trait-loss regime frontiers; "
            "they do not estimate warning performance."
        ),
    }


def write_frontier_brackets(batch_root: str | Path, output: str | Path) -> Path:
    root = Path(batch_root)
    artifact = frontier_brackets(root.rglob("batch_*.json"))
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
