"""Full-denominator audit of the two frozen symmetric warning ensembles.

The audit consumes only compact records extracted from the immutable parent
H2-R validation artifact and the immutable Phase-V fresh-validation artifact.
It never simulates trajectories, changes thresholds, selects endpoints, or
combines the six endpoint rows as independent replicates.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import NormalDist
from typing import Any, Mapping

ENDPOINT_SPECS = (
    ("H_alpha", 0.05),
    ("H_alpha", 0.10),
    ("H_alpha", 0.20),
    ("H_gamma", 0.05),
    ("H_gamma", 0.10),
    ("H_gamma", 0.20),
)
ENSEMBLE_METADATA = {
    "inherited_202611": {
        "source_repository": "zuizui0223/eco-genetic-criticality",
        "workflow_run": 28500796310,
        "artifact_id": 8003007618,
        "artifact_name": "h2r-independent-relative-validation-seeds-20261110-20261114",
        "artifact_digest": "sha256:7d2bbed84ddf57486896c0ca231fd82f2e0915699e391c155d288f5c9db8a6ff",
        "raw_member": "independent_relative_warning_v1.json",
        "raw_member_sha256": "c1552616a94b23ffc1340580231d7d1b16bc7d84c951c3d2606cc437fb15673e",
        "master_seeds": (20261110, 20261111, 20261112, 20261113, 20261114),
    },
    "fresh_202911": {
        "source_repository": "zuizui0223/eco-genetic-warning-extensions",
        "workflow_run": 32636847803,
        "artifact_id": 9492587604,
        "artifact_name": "fresh-warning-replication-phase-v",
        "artifact_digest": "sha256:c1dd951c961999c42255b46327d4650d2298afa98ee4d0a45d04a1e1c5fe6031",
        "raw_member": "phase_v_raw.json",
        "raw_member_sha256": "1674c817b760f5a20320ffdf775181f3c3134d60cc977feffe76c9296c253fb9",
        "master_seeds": (20291110, 20291111, 20291112, 20291113, 20291114),
    },
}
FROZEN_DOMAIN = {
    "mutation_rate": 0.10,
    "area_reference": 0.8,
    "interaction_feedback": 6.0,
    "ramp_generations": 30,
    "hold_generations": 90,
    "horizon": 120,
    "total_normalized_barrier_increase": 0.15,
}
LANDMARKS = (30, 60, 90)
Z_95 = NormalDist().inv_cdf(0.975)


def _endpoint(diversity_id: str, fraction: float) -> str:
    return f"{diversity_id}_{fraction:.2f}"


def _sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_domain(raw: Mapping[str, Any], ensemble: str) -> None:
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
        raise ValueError(f"{ensemble}: validation domain differs from the frozen H2-R domain")


def extract_records(raw_paths: Mapping[str, str | Path]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Extract endpoint first-passage records without opening a new estimand."""
    if set(raw_paths) != set(ENSEMBLE_METADATA):
        raise ValueError("both and only the inherited and fresh frozen ensembles are required")
    output: list[dict[str, Any]] = []
    sources: dict[str, Any] = {}
    for ensemble, metadata in ENSEMBLE_METADATA.items():
        path = Path(raw_paths[ensemble])
        member_digest = _sha256(path)
        if member_digest != metadata["raw_member_sha256"]:
            raise ValueError(f"{ensemble}: raw JSON SHA-256 mismatch")
        raw = json.loads(path.read_text(encoding="utf-8"))
        _validate_domain(raw, ensemble)
        if tuple(raw["master_seeds"]) != metadata["master_seeds"]:
            raise ValueError(f"{ensemble}: master-seed family mismatch")
        records = sorted(
            raw["records"], key=lambda row: (int(row["master_seed"]), int(row["replicate_index"]))
        )
        if len(records) != 100:
            raise ValueError(f"{ensemble}: expected 100 attempted trajectories")
        seen: set[tuple[int, int]] = set()
        available = losses = 0
        for attempt_index, record in enumerate(records):
            key = (int(record["master_seed"]), int(record["replicate_index"]))
            if key in seen:
                raise ValueError(f"{ensemble}: duplicate trajectory key {key}")
            seen.add(key)
            is_available = bool(record["trajectory_available"])
            outcome = record["outcome"] if is_available else None
            if is_available:
                available += 1
                loss_time = outcome["trait_loss_time_post_baseline"]
                losses += loss_time is not None
                lookup = {
                    (
                        comparison["definition"]["diversity_id"],
                        float(comparison["definition"]["relative_decline_fraction"]),
                    ): comparison
                    for comparison in outcome["comparisons"]
                }
                if set(lookup) != set(ENDPOINT_SPECS):
                    raise ValueError(f"{ensemble} attempt {attempt_index}: endpoint mismatch")
            else:
                loss_time = None
                lookup = {}
            for diversity_id, fraction in ENDPOINT_SPECS:
                comparison = lookup.get((diversity_id, fraction))
                output.append(
                    {
                        "ensemble": ensemble,
                        "attempt_index": attempt_index,
                        "master_seed": int(record["master_seed"]),
                        "replicate": int(record["replicate_index"]),
                        "trajectory_seed": (
                            int(record["trajectory_seed"])
                            if record["trajectory_seed"] is not None
                            else None
                        ),
                        "trajectory_available": is_available,
                        "baseline_eligible": bool(comparison["baseline_eligible"]) if comparison else False,
                        "endpoint": _endpoint(diversity_id, fraction),
                        "diversity_id": diversity_id,
                        "relative_decline_fraction": fraction,
                        "warning_time": comparison["warning_time"] if comparison else None,
                        "trait_loss_time": loss_time,
                        "ramp_generations": FROZEN_DOMAIN["ramp_generations"],
                        "hold_generations": FROZEN_DOMAIN["hold_generations"],
                        "horizon": FROZEN_DOMAIN["horizon"],
                    }
                )
        denominators = raw["summary"]["denominators"]
        if available != int(denominators["trajectory_available_count"]):
            raise ValueError(f"{ensemble}: available-trajectory count mismatch")
        if losses != int(denominators["trait_loss_observed_count"]):
            raise ValueError(f"{ensemble}: trait-loss count mismatch")
        sources[ensemble] = {
            key: list(value) if key == "master_seeds" else value
            for key, value in metadata.items()
        }
        sources[ensemble]["raw_member_sha256_verified"] = member_digest
        sources[ensemble]["attempted_trajectories"] = 100
        sources[ensemble]["trajectory_available"] = available
        sources[ensemble]["trait_loss_observed"] = losses
    return output, {
        "analysis_input": "compact extraction from two immutable saved-trajectory artifacts",
        "sources": sources,
        "frozen_domain": FROZEN_DOMAIN,
        "endpoint_family": [
            {"diversity_id": diversity_id, "relative_decline_fraction": fraction}
            for diversity_id, fraction in ENDPOINT_SPECS
        ],
        "scientific_lock": (
            "No threshold, seed, domain, schedule, endpoint, trajectory, or outcome is changed. "
            "Unavailable attempts and right-censored non-events are retained."
        ),
    }


def write_extracted_records(
    rows: list[dict[str, Any]], manifest: dict[str, Any], csv_path: str | Path, manifest_path: str | Path
) -> None:
    target = Path(csv_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    manifest = dict(manifest)
    manifest["record_table"] = {
        "path": target.as_posix(),
        "rows": len(rows),
        "sha256": _sha256(target),
        "grain": "one attempted trajectory x one predeclared endpoint",
    }
    manifest_target = Path(manifest_path)
    manifest_target.parent.mkdir(parents=True, exist_ok=True)
    manifest_target.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _optional_int(value: str) -> int | None:
    return None if value == "" else int(value)


def load_records(path: str | Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with Path(path).open(encoding="utf-8", newline="") as handle:
        for raw in csv.DictReader(handle):
            row: dict[str, Any] = dict(raw)
            for name in (
                "attempt_index",
                "master_seed",
                "replicate",
                "ramp_generations",
                "hold_generations",
                "horizon",
            ):
                row[name] = int(raw[name])
            row["trajectory_seed"] = _optional_int(raw["trajectory_seed"])
            row["relative_decline_fraction"] = float(raw["relative_decline_fraction"])
            row["warning_time"] = _optional_int(raw["warning_time"])
            row["trait_loss_time"] = _optional_int(raw["trait_loss_time"])
            row["trajectory_available"] = raw["trajectory_available"].lower() == "true"
            row["baseline_eligible"] = raw["baseline_eligible"].lower() == "true"
            rows.append(row)
    return rows


def wilson_interval(successes: int, total: int) -> dict[str, float | int | None]:
    if total < 0 or successes < 0 or successes > total:
        raise ValueError("invalid binomial count")
    if total == 0:
        return {"successes": successes, "total": total, "estimate": None, "ci95": None}
    p = successes / total
    denominator = 1 + Z_95**2 / total
    center = (p + Z_95**2 / (2 * total)) / denominator
    half = Z_95 * math.sqrt(p * (1 - p) / total + Z_95**2 / (4 * total**2)) / denominator
    return {
        "successes": successes,
        "total": total,
        "estimate": p,
        "ci95": [max(0.0, center - half), min(1.0, center + half)],
    }


def _classification(rows: list[dict[str, Any]], landmark: int | None) -> dict[str, Any]:
    horizon = int(rows[0]["horizon"])
    if landmark is None:
        risk_set = rows
        marker = lambda row: row["warning_time"] is not None and row["warning_time"] <= horizon
    else:
        risk_set = [
            row
            for row in rows
            if row["trait_loss_time"] is None or row["trait_loss_time"] > landmark
        ]
        marker = lambda row: row["warning_time"] is not None and row["warning_time"] <= landmark
    tp = sum(row["trait_loss_time"] is not None and marker(row) for row in risk_set)
    fn = sum(row["trait_loss_time"] is not None and not marker(row) for row in risk_set)
    fp = sum(row["trait_loss_time"] is None and marker(row) for row in risk_set)
    tn = sum(row["trait_loss_time"] is None and not marker(row) for row in risk_set)
    sensitivity = wilson_interval(tp, tp + fn)
    specificity = wilson_interval(tn, tn + fp)
    ppv = wilson_interval(tp, tp + fp)
    npv = wilson_interval(tn, tn + fn)
    auc = None
    if sensitivity["estimate"] is not None and specificity["estimate"] is not None:
        auc = (float(sensitivity["estimate"]) + float(specificity["estimate"])) / 2
    risk_positive = ppv
    risk_negative = wilson_interval(fn, fn + tn)
    risk_difference = None
    risk_difference_ci95 = None
    if risk_positive["estimate"] is not None and risk_negative["estimate"] is not None:
        risk_difference = float(risk_positive["estimate"]) - float(risk_negative["estimate"])
        positive_ci = risk_positive["ci95"]
        negative_ci = risk_negative["ci95"]
        assert positive_ci is not None and negative_ci is not None
        risk_difference_ci95 = [
            max(-1.0, positive_ci[0] - negative_ci[1]),
            min(1.0, positive_ci[1] - negative_ci[0]),
        ]
    return {
        "landmark": landmark,
        "administrative_horizon": horizon,
        "risk_set": len(risk_set),
        "future_cases": tp + fn,
        "administrative_controls": fp + tn,
        "confusion": {"true_positive": tp, "false_negative": fn, "false_positive": fp, "true_negative": tn},
        "sensitivity": sensitivity,
        "specificity": specificity,
        "positive_predictive_value": ppv,
        "negative_predictive_value": npv,
        "binary_marker_auc": auc,
        "risk_warning_positive": risk_positive,
        "risk_warning_negative": risk_negative,
        "risk_difference_positive_minus_negative": risk_difference,
        "risk_difference_ci95_conservative_newcombe": risk_difference_ci95,
    }


def _endpoint_audit(rows: list[dict[str, Any]]) -> dict[str, Any]:
    events = [row for row in rows if row["trait_loss_time"] is not None]
    non_events = [row for row in rows if row["trait_loss_time"] is None]
    leads = sum(
        row["warning_time"] is not None and row["warning_time"] < row["trait_loss_time"]
        for row in events
    )
    false_alarms = sum(row["warning_time"] is not None for row in non_events)
    return {
        "baseline_eligible_trajectories": len(rows),
        "event_trajectories": len(events),
        "right_censored_non_event_trajectories": len(non_events),
        "lead_sensitivity": wilson_interval(leads, len(events)),
        "non_event_false_positive_rate": wilson_interval(false_alarms, len(non_events)),
        "full_horizon_classification": _classification(rows, None),
        "landmark_dynamic_classification": {
            str(landmark): _classification(rows, landmark) for landmark in LANDMARKS
        },
    }


def _trajectory_groups(rows: list[dict[str, Any]]) -> dict[tuple[str, int], list[dict[str, Any]]]:
    groups: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(row["ensemble"], int(row["attempt_index"]))].append(row)
    for key, cluster in groups.items():
        if len(cluster) != len(ENDPOINT_SPECS):
            raise ValueError(f"{key}: expected six endpoint rows")
        if len({row["trait_loss_time"] for row in cluster}) != 1:
            raise ValueError(f"{key}: trait-loss time differs across endpoint rows")
    return dict(groups)


def audit(rows: list[dict[str, Any]]) -> dict[str, Any]:
    groups = _trajectory_groups(rows)
    expected_groups = len(ENSEMBLE_METADATA) * 100
    if len(groups) != expected_groups:
        raise ValueError(f"expected {expected_groups} attempted trajectories")
    endpoints = tuple(_endpoint(*spec) for spec in ENDPOINT_SPECS)
    output: dict[str, Any] = {}
    for ensemble in ENSEMBLE_METADATA:
        ensemble_rows = [row for row in rows if row["ensemble"] == ensemble]
        baseline = [row for row in ensemble_rows if row["baseline_eligible"]]
        output[ensemble] = {
            "attempted_trajectories": len({row["attempt_index"] for row in ensemble_rows}),
            "available_baseline_eligible_trajectories": len(baseline) // len(ENDPOINT_SPECS),
            "endpoints": {
                endpoint: _endpoint_audit([row for row in baseline if row["endpoint"] == endpoint])
                for endpoint in endpoints
            },
        }
    combined_baseline = [row for row in rows if row["baseline_eligible"]]
    output["combined_descriptive"] = {
        "scope": "trajectory-level descriptive pooling of the two independent ensembles within the identical frozen domain",
        "available_baseline_eligible_trajectories": len(combined_baseline) // len(ENDPOINT_SPECS),
        "endpoints": {
            endpoint: _endpoint_audit([row for row in combined_baseline if row["endpoint"] == endpoint])
            for endpoint in endpoints
        },
    }
    return {
        "analysis": "post-review full-denominator warning-validity audit",
        "population": "all baseline-eligible saved trajectories in each frozen symmetric H2-R ensemble",
        "right_censoring": (
            "All available trajectories share the fixed administrative horizon of 120 generations. "
            "No-loss trajectories remain right-censored for event-time claims and serve as known event-free controls only at that horizon."
        ),
        "endpoint_dependence": (
            "The six endpoint rows from one trajectory are repeated measurements. No endpoint-pooled p-value, "
            "sample size, or confidence interval treats them as independent replicates."
        ),
        "auc_identifiability": (
            "A full continuous time-dependent ROC/AUC was not introduced because the locked endpoint family supplies "
            "six binary first-passage rules, not a preregistered continuous risk score measured at a common time. "
            "The defensible alternative reports binary-marker AUC at the schedule-derived ramp-end landmark (30) "
            "and the fixed half/three-quarter horizon landmarks (60/90), without selecting a favourable landmark."
        ),
        "claim_rule": (
            "Lead sensitivity establishes temporal ordering among event trajectories only. Predictive warning validity "
            "requires non-event specificity or horizon risk separation; it is not inferred from valid pairs alone."
        ),
        "intervals": "two-sided 95% Wilson intervals for binomial rates; no multiplicity-based endpoint aggregation",
        "ensembles": output,
    }


def write_audit_outputs(result: dict[str, Any], json_path: str | Path, csv_path: str | Path) -> None:
    json_target = Path(json_path)
    json_target.parent.mkdir(parents=True, exist_ok=True)
    json_target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    fields = (
        "ensemble",
        "endpoint",
        "baseline_eligible",
        "events",
        "right_censored_non_events",
        "lead_sensitivity",
        "lead_sensitivity_ci_lower",
        "lead_sensitivity_ci_upper",
        "non_event_false_positive_rate",
        "non_event_fpr_ci_lower",
        "non_event_fpr_ci_upper",
        "full_horizon_ppv",
        "full_horizon_npv",
        "full_horizon_specificity",
        "full_horizon_binary_auc",
        "ramp_end_risk_set",
        "ramp_end_future_cases",
        "ramp_end_sensitivity",
        "ramp_end_specificity",
        "ramp_end_ppv",
        "ramp_end_npv",
        "ramp_end_binary_auc",
        "ramp_end_risk_difference",
        "ramp_end_risk_difference_ci_lower",
        "ramp_end_risk_difference_ci_upper",
    )
    table_rows: list[dict[str, Any]] = []
    for ensemble, ensemble_data in result["ensembles"].items():
        for endpoint, endpoint_data in ensemble_data["endpoints"].items():
            lead = endpoint_data["lead_sensitivity"]
            fpr = endpoint_data["non_event_false_positive_rate"]
            full = endpoint_data["full_horizon_classification"]
            ramp = endpoint_data["landmark_dynamic_classification"]["30"]
            lead_ci = lead["ci95"]
            fpr_ci = fpr["ci95"]
            rd_ci = ramp["risk_difference_ci95_conservative_newcombe"]
            table_rows.append(
                {
                    "ensemble": ensemble,
                    "endpoint": endpoint,
                    "baseline_eligible": endpoint_data["baseline_eligible_trajectories"],
                    "events": endpoint_data["event_trajectories"],
                    "right_censored_non_events": endpoint_data["right_censored_non_event_trajectories"],
                    "lead_sensitivity": lead["estimate"],
                    "lead_sensitivity_ci_lower": lead_ci[0] if lead_ci else None,
                    "lead_sensitivity_ci_upper": lead_ci[1] if lead_ci else None,
                    "non_event_false_positive_rate": fpr["estimate"],
                    "non_event_fpr_ci_lower": fpr_ci[0] if fpr_ci else None,
                    "non_event_fpr_ci_upper": fpr_ci[1] if fpr_ci else None,
                    "full_horizon_ppv": full["positive_predictive_value"]["estimate"],
                    "full_horizon_npv": full["negative_predictive_value"]["estimate"],
                    "full_horizon_specificity": full["specificity"]["estimate"],
                    "full_horizon_binary_auc": full["binary_marker_auc"],
                    "ramp_end_risk_set": ramp["risk_set"],
                    "ramp_end_future_cases": ramp["future_cases"],
                    "ramp_end_sensitivity": ramp["sensitivity"]["estimate"],
                    "ramp_end_specificity": ramp["specificity"]["estimate"],
                    "ramp_end_ppv": ramp["positive_predictive_value"]["estimate"],
                    "ramp_end_npv": ramp["negative_predictive_value"]["estimate"],
                    "ramp_end_binary_auc": ramp["binary_marker_auc"],
                    "ramp_end_risk_difference": ramp["risk_difference_positive_minus_negative"],
                    "ramp_end_risk_difference_ci_lower": rd_ci[0] if rd_ci else None,
                    "ramp_end_risk_difference_ci_upper": rd_ci[1] if rd_ci else None,
                }
            )
    csv_target = Path(csv_path)
    csv_target.parent.mkdir(parents=True, exist_ok=True)
    with csv_target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(table_rows)
