"""Aggregate Protocol 003 blind bracket pilot artifacts.

The aggregation remains trait-loss-only. It ranks schedules within each sentinel by
absolute distance of the pooled trait-loss rate from 0.5, then horizon and barrier
increase. It does not select a warning-validation domain.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

EXPECTED_CELL_COUNT = 16
EXPECTED_SENTINELS = ("rapid_loss", "symmetric_bridge", "transition", "persistence")


def load_bracket_artifacts(root: str | Path) -> list[dict[str, Any]]:
    paths = sorted(Path(root).rglob("*.json"))
    artifacts = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    artifacts = [item for item in artifacts if item.get("stage") == "Protocol 003 blind sentinel bracket pilot"]
    if len(artifacts) != EXPECTED_CELL_COUNT:
        raise RuntimeError(f"expected {EXPECTED_CELL_COUNT} bracket artifacts, found {len(artifacts)}")
    indices = sorted(int(item["cell"]["cell_index"]) for item in artifacts)
    if indices != list(range(EXPECTED_CELL_COUNT)):
        raise RuntimeError("bracket artifact cell indices are incomplete or duplicated")
    return sorted(artifacts, key=lambda item: int(item["cell"]["cell_index"]))


def _rank_key(artifact: dict[str, Any]) -> tuple[float, int, float, int]:
    rate = artifact.get("pooled_trait_loss_rate")
    distance = float("inf") if rate is None else abs(float(rate) - 0.5)
    cell = artifact["cell"]
    return (
        distance,
        int(cell["horizon"]),
        float(cell["normalised_barrier_increase"]),
        int(cell["cell_index"]),
    )


def aggregate_bracket_artifacts(artifacts: Iterable[dict[str, Any]]) -> dict[str, Any]:
    rows = list(artifacts)
    by_label: dict[str, list[dict[str, Any]]] = {label: [] for label in EXPECTED_SENTINELS}
    for artifact in rows:
        label = str(artifact["cell"]["label"])
        if label not in by_label:
            raise RuntimeError(f"unexpected sentinel label: {label}")
        by_label[label].append(artifact)

    sentinels = []
    for label in EXPECTED_SENTINELS:
        candidates = sorted(by_label[label], key=lambda item: int(item["cell"]["cell_index"]))
        if len(candidates) != 4:
            raise RuntimeError(f"sentinel {label} must have four schedules")
        candidate_rows = []
        for item in candidates:
            candidate_rows.append({
                **item["cell"],
                "attempted": int(item["status_counts"]["attempted"]),
                "baseline_eligible": int(item["status_counts"]["baseline_eligible"]),
                "trait_loss": int(item["status_counts"]["trait_loss"]),
                "pooled_trait_loss_rate": item.get("pooled_trait_loss_rate"),
            })
        selected = min(candidates, key=_rank_key)
        selected_rate = selected.get("pooled_trait_loss_rate")
        rates = [item.get("pooled_trait_loss_rate") for item in candidates]
        numeric_rates = [float(rate) for rate in rates if rate is not None]
        bracket_crosses_half = bool(numeric_rates) and min(numeric_rates) <= 0.5 <= max(numeric_rates)
        sentinels.append({
            "label": label,
            "coordinate": {
                "kappa_mu": selected["cell"]["kappa_mu"],
                "p_star": selected["cell"]["p_star"],
            },
            "candidate_schedules": candidate_rows,
            "closest_schedule": {
                **selected["cell"],
                "pooled_trait_loss_rate": selected_rate,
                "distance_from_half": None if selected_rate is None else abs(float(selected_rate) - 0.5),
            },
            "bracket_crosses_half": bracket_crosses_half,
            "ready_for_independent_calibration": selected_rate is not None and abs(float(selected_rate) - 0.5) <= 0.25,
        })

    return {
        "stage": "Protocol 003 blind bracket pilot aggregation",
        "source_workflow_run_id": 29399936075,
        "cell_count": len(rows),
        "trajectory_attempt_count": sum(int(item["status_counts"]["attempted"]) for item in rows),
        "endpoint_contract": "trait_loss_only",
        "domain_selected": False,
        "sentinels": sentinels,
    }


def write_bracket_aggregation(input_root: str | Path, output: str | Path) -> Path:
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = aggregate_bracket_artifacts(load_bracket_artifacts(input_root))
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target
