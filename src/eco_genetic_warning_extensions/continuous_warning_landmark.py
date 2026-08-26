"""One-time exploratory continuous landmark audit of two frozen ensembles."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Any, Mapping, Sequence

from .warning_validity_audit import ENSEMBLE_METADATA, FROZEN_DOMAIN, LANDMARKS

DIVERSITY_COORDINATES = ("H_alpha", "H_gamma")
SERIES_FIELDS = {"H_alpha": "h_alpha_series", "H_gamma": "h_gamma_series"}
BOOTSTRAP_REPLICATES = 10_000
BOOTSTRAP_BASE_SEED = 20_260_826


def _sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_raw(raw: Mapping[str, Any], ensemble: str) -> None:
    metadata = ENSEMBLE_METADATA[ensemble]
    if tuple(raw["master_seeds"]) != metadata["master_seeds"]:
        raise ValueError(f"{ensemble}: master-seed family mismatch")
    domain = raw["validation_domain"]
    schedule = domain["schedule"]
    observed = {
        "mutation_rate": float(domain["mutation_rate"]),
        "area_reference": float(domain["area_reference"]),
        "interaction_feedback": float(domain["interaction_feedback"]),
        "ramp_generations": int(schedule["ramp_generations"]),
        "hold_generations": int(schedule["hold_generations"]),
        "horizon": int(schedule["total_generations"]),
        "total_normalized_barrier_increase": float(
            schedule["total_normalized_barrier_increase"]
        ),
    }
    if observed != FROZEN_DOMAIN:
        raise ValueError(f"{ensemble}: frozen validation domain mismatch")


def extract_trajectory_series(
    raw_paths: Mapping[str, str | Path],
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    """Verify immutable artifacts and extract one record per eligible trajectory."""
    if set(raw_paths) != set(ENSEMBLE_METADATA):
        raise ValueError("both and only the inherited and fresh frozen ensembles are required")
    output: dict[str, list[dict[str, Any]]] = {}
    source_manifest: dict[str, Any] = {}
    horizon = int(FROZEN_DOMAIN["horizon"])
    for ensemble, metadata in ENSEMBLE_METADATA.items():
        path = Path(raw_paths[ensemble])
        observed_sha = _sha256(path)
        if observed_sha != metadata["raw_member_sha256"]:
            raise ValueError(f"{ensemble}: raw JSON SHA-256 mismatch")
        raw = json.loads(path.read_text(encoding="utf-8"))
        _validate_raw(raw, ensemble)
        records = sorted(
            raw["records"],
            key=lambda row: (int(row["master_seed"]), int(row["replicate_index"])),
        )
        if len(records) != 100:
            raise ValueError(f"{ensemble}: expected 100 attempted trajectories")
        eligible: list[dict[str, Any]] = []
        available = losses = 0
        for attempt_index, record in enumerate(records):
            if not bool(record["trajectory_available"]):
                continue
            available += 1
            outcome = record["outcome"]
            comparisons = outcome["comparisons"]
            if len(comparisons) != 6:
                raise ValueError(f"{ensemble} attempt {attempt_index}: endpoint count mismatch")
            eligibility = {bool(item["baseline_eligible"]) for item in comparisons}
            if len(eligibility) != 1:
                raise ValueError(
                    f"{ensemble} attempt {attempt_index}: baseline eligibility differs by endpoint"
                )
            loss_time = outcome["trait_loss_time_post_baseline"]
            if loss_time is not None:
                loss_time = int(loss_time)
                if not 0 < loss_time <= horizon:
                    raise ValueError(f"{ensemble} attempt {attempt_index}: invalid loss time")
                losses += 1
            series: dict[str, list[float]] = {}
            for diversity_id, field in SERIES_FIELDS.items():
                values = [float(value) for value in outcome[field]]
                if len(values) != horizon + 1:
                    raise ValueError(
                        f"{ensemble} attempt {attempt_index}: {field} must contain 0..{horizon}"
                    )
                if not all(math.isfinite(value) for value in values) or values[0] <= 0:
                    raise ValueError(
                        f"{ensemble} attempt {attempt_index}: invalid {diversity_id} series"
                    )
                series[diversity_id] = values
            if eligibility == {True}:
                eligible.append(
                    {
                        "attempt_index": attempt_index,
                        "master_seed": int(record["master_seed"]),
                        "replicate": int(record["replicate_index"]),
                        "trajectory_seed": int(record["trajectory_seed"]),
                        "trait_loss_time": loss_time,
                        "series": series,
                    }
                )
        denominators = raw["summary"]["denominators"]
        if available != int(denominators["trajectory_available_count"]):
            raise ValueError(f"{ensemble}: available count mismatch")
        if losses != int(denominators["trait_loss_observed_count"]):
            raise ValueError(f"{ensemble}: loss count mismatch")
        output[ensemble] = eligible
        source_manifest[ensemble] = {
            "source_repository": metadata["source_repository"],
            "workflow_run": metadata["workflow_run"],
            "artifact_id": metadata["artifact_id"],
            "artifact_name": metadata["artifact_name"],
            "artifact_digest": metadata["artifact_digest"],
            "raw_member": metadata["raw_member"],
            "raw_member_sha256_verified": observed_sha,
            "attempted_trajectories": 100,
            "available_trajectories": available,
            "baseline_eligible_trajectories": len(eligible),
        }
    return output, source_manifest


def concordance_auc(cases: Sequence[float], controls: Sequence[float]) -> float:
    if not cases or not controls:
        raise ValueError("AUC requires at least one case and one control")
    concordance = 0.0
    for case in cases:
        for control in controls:
            concordance += float(case > control) + 0.5 * float(case == control)
    return concordance / (len(cases) * len(controls))


def _percentile(values: Sequence[float], probability: float) -> float:
    if not values or not 0 <= probability <= 1:
        raise ValueError("invalid percentile request")
    ordered = sorted(values)
    position = probability * (len(ordered) - 1)
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def stratified_bootstrap_auc(
    cases: Sequence[float],
    controls: Sequence[float],
    *,
    seed: int,
    replicates: int = BOOTSTRAP_REPLICATES,
) -> list[float]:
    if replicates <= 0:
        raise ValueError("bootstrap replicates must be positive")
    rng = random.Random(seed)
    estimates = []
    for _ in range(replicates):
        sampled_cases = [cases[rng.randrange(len(cases))] for _ in cases]
        sampled_controls = [controls[rng.randrange(len(controls))] for _ in controls]
        estimates.append(concordance_auc(sampled_cases, sampled_controls))
    return [_percentile(estimates, 0.025), _percentile(estimates, 0.975)]


def _cell_seed(ensemble_index: int, diversity_index: int, landmark_index: int) -> int:
    return BOOTSTRAP_BASE_SEED + ensemble_index * 100 + diversity_index * 10 + landmark_index


def landmark_cell(
    trajectories: Sequence[Mapping[str, Any]],
    diversity_id: str,
    landmark: int,
    *,
    bootstrap_seed: int,
    bootstrap_replicates: int = BOOTSTRAP_REPLICATES,
) -> dict[str, Any]:
    cases: list[float] = []
    controls: list[float] = []
    excluded_prior_losses = 0
    for trajectory in trajectories:
        loss_time = trajectory["trait_loss_time"]
        if loss_time is not None and int(loss_time) <= landmark:
            excluded_prior_losses += 1
            continue
        series = trajectory["series"][diversity_id]
        score = 1.0 - float(series[landmark]) / float(series[0])
        if loss_time is None:
            controls.append(score)
        else:
            cases.append(score)
    auc = concordance_auc(cases, controls)
    ci95 = stratified_bootstrap_auc(
        cases,
        controls,
        seed=bootstrap_seed,
        replicates=bootstrap_replicates,
    )
    return {
        "diversity_id": diversity_id,
        "landmark": landmark,
        "administrative_horizon": FROZEN_DOMAIN["horizon"],
        "score": f"1 - {diversity_id}(t) / {diversity_id}(0)",
        "risk_set": len(cases) + len(controls),
        "future_cases": len(cases),
        "dynamic_controls": len(controls),
        "excluded_losses_at_or_before_landmark": excluded_prior_losses,
        "auc": auc,
        "auc_ci95_percentile": ci95,
        "bootstrap_replicates": bootstrap_replicates,
        "bootstrap_seed": bootstrap_seed,
    }


def exploratory_audit(
    trajectories: Mapping[str, Sequence[Mapping[str, Any]]],
    source_manifest: Mapping[str, Any],
    *,
    protocol_commit: str,
    bootstrap_replicates: int = BOOTSTRAP_REPLICATES,
) -> dict[str, Any]:
    if len(protocol_commit) != 40 or any(ch not in "0123456789abcdef" for ch in protocol_commit):
        raise ValueError("protocol_commit must be a lowercase 40-character Git SHA")
    ensembles: dict[str, Any] = {}
    for ensemble_index, ensemble in enumerate(ENSEMBLE_METADATA):
        cells = []
        for diversity_index, diversity_id in enumerate(DIVERSITY_COORDINATES):
            for landmark_index, landmark in enumerate(LANDMARKS):
                cells.append(
                    landmark_cell(
                        trajectories[ensemble],
                        diversity_id,
                        landmark,
                        bootstrap_seed=_cell_seed(
                            ensemble_index, diversity_index, landmark_index
                        ),
                        bootstrap_replicates=bootstrap_replicates,
                    )
                )
        ensembles[ensemble] = {
            "baseline_eligible_trajectories": len(trajectories[ensemble]),
            "cells": cells,
            "auc_range": [min(cell["auc"] for cell in cells), max(cell["auc"] for cell in cells)],
        }
    return {
        "analysis": "postreview_exploratory_continuous_landmark_auc",
        "prospective_protocol_commit": protocol_commit,
        "preregistration": "manuscript/warning_continuous_landmark_exploratory_preregistration.md",
        "frozen_domain": FROZEN_DOMAIN,
        "source_manifest": source_manifest,
        "estimand": "landmark cumulative/dynamic concordance AUC through generation 120",
        "score_direction": "greater baseline-relative erosion predicts greater future-loss risk",
        "uncertainty": (
            "95% percentile interval from stratified trajectory-level bootstrap; "
            "cases and dynamic controls resampled separately"
        ),
        "endpoint_dependence": (
            "Six cells reuse each ensemble's trajectories and are not independent replicates; "
            "no pooled endpoint p-value is calculated."
        ),
        "claim_boundary": (
            "Exploratory fixed-score evidence only. It cannot restore the frozen binary rules as "
            "validated predictive warning or characterize genetic diversity in general."
        ),
        "ensembles": ensembles,
    }


def write_outputs(result: Mapping[str, Any], json_path: str | Path, csv_path: str | Path) -> None:
    json_target = Path(json_path)
    json_target.parent.mkdir(parents=True, exist_ok=True)
    json_target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    fields = (
        "ensemble",
        "diversity_id",
        "landmark",
        "risk_set",
        "future_cases",
        "dynamic_controls",
        "excluded_losses_at_or_before_landmark",
        "auc",
        "auc_ci95_lower",
        "auc_ci95_upper",
        "bootstrap_replicates",
        "bootstrap_seed",
    )
    rows = []
    for ensemble, ensemble_result in result["ensembles"].items():
        for cell in ensemble_result["cells"]:
            rows.append(
                {
                    "ensemble": ensemble,
                    "diversity_id": cell["diversity_id"],
                    "landmark": cell["landmark"],
                    "risk_set": cell["risk_set"],
                    "future_cases": cell["future_cases"],
                    "dynamic_controls": cell["dynamic_controls"],
                    "excluded_losses_at_or_before_landmark": cell[
                        "excluded_losses_at_or_before_landmark"
                    ],
                    "auc": cell["auc"],
                    "auc_ci95_lower": cell["auc_ci95_percentile"][0],
                    "auc_ci95_upper": cell["auc_ci95_percentile"][1],
                    "bootstrap_replicates": cell["bootstrap_replicates"],
                    "bootstrap_seed": cell["bootstrap_seed"],
                }
            )
    csv_target = Path(csv_path)
    csv_target.parent.mkdir(parents=True, exist_ok=True)
    with csv_target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
