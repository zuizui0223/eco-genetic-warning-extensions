"""Secondary audit of Protocol 003 warning timing and uncertainty.

This module operates only on the locked Stage III trajectory-endpoint table. It
does not select domains, alter calibration, rerun simulations, or inspect any
new warning-validation trajectories.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any

ENDPOINTS = (
    "H_alpha_0.05",
    "H_alpha_0.10",
    "H_alpha_0.20",
    "H_gamma_0.05",
    "H_gamma_0.10",
    "H_gamma_0.20",
)
DOMAINS = ("recalibrated_symmetric_domain", "directional_calibrated_domain")
BOOTSTRAP_SEED = 20260814
DEFAULT_BOOTSTRAP_REPLICATES = 20_000


def _as_int(value: str) -> int | None:
    return None if value == "" else int(value)


def load_records(path: str | Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with Path(path).open(encoding="utf-8", newline="") as handle:
        for raw in csv.DictReader(handle):
            row: dict[str, Any] = dict(raw)
            for name in (
                "attempt_index",
                "master_seed",
                "replicate",
                "trajectory_seed",
                "ramp_generations",
                "hold_generations",
                "horizon",
            ):
                row[name] = int(raw[name])
            for name in (
                "kappa_mu",
                "p_star",
                "area_reference",
                "kappa",
                "normalised_barrier_increase",
                "relative_decline_fraction",
            ):
                row[name] = float(raw[name])
            for name in ("warning_time", "trait_loss_time", "lead_time_trait_minus_warning"):
                row[name] = _as_int(raw[name])
            row["baseline_eligible"] = raw["baseline_eligible"].lower() == "true"
            row["valid_pair"] = raw["valid_pair"].lower() == "true"
            records.append(row)
    return records


def _percentile(values: list[float], probability: float) -> float:
    if not values:
        return math.nan
    ordered = sorted(values)
    if len(ordered) == 1:
        return float(ordered[0])
    position = probability * (len(ordered) - 1)
    lo = math.floor(position)
    hi = math.ceil(position)
    if lo == hi:
        return float(ordered[lo])
    weight = position - lo
    return float(ordered[lo] * (1 - weight) + ordered[hi] * weight)


def _ci(values: list[float]) -> dict[str, float]:
    return {
        "lower": _percentile(values, 0.025),
        "median": _percentile(values, 0.5),
        "upper": _percentile(values, 0.975),
    }


def _trajectory_groups(
    records: list[dict[str, Any]], domain: str
) -> dict[int, list[dict[str, Any]]]:
    groups: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in records:
        if row["domain"] == domain:
            groups[int(row["attempt_index"])].append(row)
    if sorted(groups) != list(range(100)):
        raise ValueError(f"{domain}: expected attempt_index 0..99")
    for index, rows in groups.items():
        if len(rows) != 6:
            raise ValueError(f"{domain} attempt {index}: expected six endpoints")
    return dict(groups)


def _point_summary(groups: dict[int, list[dict[str, Any]]]) -> dict[str, Any]:
    rows = [row for cluster in groups.values() for row in cluster]
    valid = [row for row in rows if row["valid_pair"]]
    lead = [row for row in valid if row["category"] == "lead"]
    lag = [row for row in valid if row["category"] == "lag"]
    tie = [row for row in valid if row["category"] == "tie"]
    return {
        "valid_pairs": len(valid),
        "lead": len(lead),
        "tie": len(tie),
        "lag": len(lag),
        "lead_fraction_among_valid_pairs": len(lead) / len(valid) if valid else None,
        "lag_fraction_among_valid_pairs": len(lag) / len(valid) if valid else None,
        "valid_pair_availability_per_attempted_endpoint": len(valid) / len(rows),
    }


def _endpoint_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    categories = (
        "source_preparation_failed",
        "baseline_ineligible",
        "both_censored",
        "warning_censored",
        "trait_loss_censored",
        "lead",
        "tie",
        "lag",
    )
    for endpoint in ENDPOINTS:
        endpoint_rows = [row for row in rows if row["endpoint"] == endpoint]
        counts = {
            category: sum(row["category"] == category for row in endpoint_rows)
            for category in categories
        }
        positive = [
            float(row["lead_time_trait_minus_warning"])
            for row in endpoint_rows
            if row["category"] == "lead"
        ]
        horizon = int(endpoint_rows[0]["horizon"])
        hold = int(endpoint_rows[0]["hold_generations"])
        output[endpoint] = {
            "counts": counts,
            "attempted": len(endpoint_rows),
            "valid_pairs": counts["lead"] + counts["tie"] + counts["lag"],
            "positive_leads": len(positive),
            "median_positive_lead_time": statistics.median(positive) if positive else None,
            "median_positive_lead_fraction_of_horizon": (
                statistics.median([v / horizon for v in positive]) if positive else None
            ),
            "median_positive_lead_fraction_of_hold": (
                statistics.median([v / hold for v in positive]) if positive else None
            ),
        }
    return output


def _bootstrap(
    groups: dict[int, list[dict[str, Any]]],
    replicates: int,
    rng: random.Random,
) -> dict[str, Any]:
    indices = sorted(groups)
    aggregate = {
        "lead_fraction_among_valid_pairs": [],
        "lag_fraction_among_valid_pairs": [],
        "valid_pair_availability_per_attempted_endpoint": [],
    }
    endpoint_values = {
        endpoint: {
            "median_positive_lead_time": [],
            "median_positive_lead_fraction_of_horizon": [],
        }
        for endpoint in ENDPOINTS
    }
    for _ in range(replicates):
        sampled = [rng.choice(indices) for _ in indices]
        rows = [row for index in sampled for row in groups[index]]
        valid = [row for row in rows if row["valid_pair"]]
        if valid:
            aggregate["lead_fraction_among_valid_pairs"].append(
                sum(row["category"] == "lead" for row in valid) / len(valid)
            )
            aggregate["lag_fraction_among_valid_pairs"].append(
                sum(row["category"] == "lag" for row in valid) / len(valid)
            )
        aggregate["valid_pair_availability_per_attempted_endpoint"].append(
            len(valid) / len(rows)
        )
        for endpoint in ENDPOINTS:
            endpoint_rows = [
                row
                for row in rows
                if row["endpoint"] == endpoint and row["category"] == "lead"
            ]
            if endpoint_rows:
                values = [
                    float(row["lead_time_trait_minus_warning"]) for row in endpoint_rows
                ]
                horizon = float(endpoint_rows[0]["horizon"])
                endpoint_values[endpoint]["median_positive_lead_time"].append(
                    float(statistics.median(values))
                )
                endpoint_values[endpoint][
                    "median_positive_lead_fraction_of_horizon"
                ].append(
                    float(statistics.median([value / horizon for value in values]))
                )
    return {
        "aggregate_cluster_bootstrap_95_ci": {
            key: _ci(values) for key, values in aggregate.items()
        },
        "endpoint_bootstrap_95_ci": {
            endpoint: {key: _ci(values) for key, values in metrics.items()}
            for endpoint, metrics in endpoint_values.items()
        },
    }


def _lead_values(
    groups: dict[int, list[dict[str, Any]]], endpoint: str, metric: str
) -> list[float]:
    rows = [
        row
        for cluster in groups.values()
        for row in cluster
        if row["endpoint"] == endpoint and row["category"] == "lead"
    ]
    if metric == "absolute_generations":
        return [float(row["lead_time_trait_minus_warning"]) for row in rows]
    if metric == "horizon_fraction":
        return [
            float(row["lead_time_trait_minus_warning"]) / float(row["horizon"])
            for row in rows
        ]
    if metric == "hold_fraction":
        return [
            float(row["lead_time_trait_minus_warning"])
            / float(row["hold_generations"])
            for row in rows
        ]
    raise ValueError(f"unknown lead-time metric: {metric}")


def _sampled_lead_values(
    groups: dict[int, list[dict[str, Any]]],
    sampled_indices: list[int],
    endpoint: str,
    metric: str,
) -> list[float]:
    rows = [
        row
        for index in sampled_indices
        for row in groups[index]
        if row["endpoint"] == endpoint and row["category"] == "lead"
    ]
    if metric == "absolute_generations":
        return [float(row["lead_time_trait_minus_warning"]) for row in rows]
    if metric == "horizon_fraction":
        return [
            float(row["lead_time_trait_minus_warning"]) / float(row["horizon"])
            for row in rows
        ]
    if metric == "hold_fraction":
        return [
            float(row["lead_time_trait_minus_warning"])
            / float(row["hold_generations"])
            for row in rows
        ]
    raise ValueError(f"unknown lead-time metric: {metric}")


def _between_domain_difference_bootstrap(
    domain_groups: dict[str, dict[int, list[dict[str, Any]]]], replicates: int
) -> dict[str, Any]:
    """Bootstrap directional-minus-symmetric median differences.

    The two validation domains contain independent attempted trajectories. Each
    replicate resamples 100 whole attempted trajectories independently within
    each domain and preserves the six endpoint rows of every sampled trajectory.
    """
    symmetric = domain_groups[DOMAINS[0]]
    directional = domain_groups[DOMAINS[1]]
    symmetric_indices = sorted(symmetric)
    directional_indices = sorted(directional)
    rng = random.Random(BOOTSTRAP_SEED)
    metrics = ("absolute_generations", "horizon_fraction", "hold_fraction")
    bootstrap_values = {
        endpoint: {metric: [] for metric in metrics} for endpoint in ENDPOINTS
    }

    for _ in range(replicates):
        sampled_symmetric = [
            rng.choice(symmetric_indices) for _ in symmetric_indices
        ]
        sampled_directional = [
            rng.choice(directional_indices) for _ in directional_indices
        ]
        for endpoint in ENDPOINTS:
            for metric in metrics:
                symmetric_values = _sampled_lead_values(
                    symmetric, sampled_symmetric, endpoint, metric
                )
                directional_values = _sampled_lead_values(
                    directional, sampled_directional, endpoint, metric
                )
                if not symmetric_values or not directional_values:
                    continue
                bootstrap_values[endpoint][metric].append(
                    float(statistics.median(directional_values))
                    - float(statistics.median(symmetric_values))
                )

    output: dict[str, Any] = {}
    for endpoint in ENDPOINTS:
        output[endpoint] = {}
        for metric in metrics:
            point = float(
                statistics.median(_lead_values(directional, endpoint, metric))
            ) - float(statistics.median(_lead_values(symmetric, endpoint, metric)))
            interval = _ci(bootstrap_values[endpoint][metric])
            output[endpoint][metric] = {
                "directional_minus_symmetric": point,
                "bootstrap_95_ci": interval,
                "ci_includes_zero": interval["lower"] <= 0.0 <= interval["upper"],
            }
    return output


def _cumulative_event_incidence(rows: list[dict[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for endpoint in ENDPOINTS:
        endpoint_rows = [
            row
            for row in rows
            if row["endpoint"] == endpoint
            and row["category"]
            not in ("source_preparation_failed", "baseline_ineligible")
        ]
        horizon = int(endpoint_rows[0]["horizon"])
        n = len(endpoint_rows)
        series = []
        for generation in range(horizon + 1):
            warning_count = sum(
                row["warning_time"] is not None
                and int(row["warning_time"]) <= generation
                for row in endpoint_rows
            )
            loss_count = sum(
                row["trait_loss_time"] is not None
                and int(row["trait_loss_time"]) <= generation
                for row in endpoint_rows
            )
            series.append(
                {
                    "generation": generation,
                    "warning_incidence": warning_count / n,
                    "trait_loss_incidence": loss_count / n,
                }
            )
        output[endpoint] = {
            "baseline_eligible_completed": n,
            "horizon": horizon,
            "series": series,
        }
    return output


def audit(
    records: list[dict[str, Any]],
    bootstrap_replicates: int = DEFAULT_BOOTSTRAP_REPLICATES,
) -> dict[str, Any]:
    rng = random.Random(BOOTSTRAP_SEED)
    domains: dict[str, Any] = {}
    groups_by_domain: dict[str, dict[int, list[dict[str, Any]]]] = {}
    for domain in DOMAINS:
        groups = _trajectory_groups(records, domain)
        groups_by_domain[domain] = groups
        rows = [row for cluster in groups.values() for row in cluster]
        first = rows[0]
        domain_summary = {
            "schedule": {
                key: first[key]
                for key in (
                    "kappa_mu",
                    "p_star",
                    "area_reference",
                    "kappa",
                    "ramp_generations",
                    "hold_generations",
                    "horizon",
                    "normalised_barrier_increase",
                )
            },
            "aggregate": _point_summary(groups),
            "endpoints": _endpoint_summary(rows),
            "cumulative_event_incidence": _cumulative_event_incidence(rows),
        }
        domain_summary.update(_bootstrap(groups, bootstrap_replicates, rng))
        domains[domain] = domain_summary

    return {
        "analysis": "Protocol 003 locked-validation secondary timing and uncertainty audit",
        "evidence_boundary": (
            "Post hoc secondary analysis of locked Stage III validation records only; "
            "no domain selection, calibration, simulation, endpoint definition, or "
            "trajectory is changed."
        ),
        "bootstrap": {
            "unit": "whole attempted trajectory",
            "replicates": bootstrap_replicates,
            "seed": BOOTSTRAP_SEED,
            "interval": "percentile 95%",
        },
        "median_correction": (
            "The historical Stage III artifact generator used "
            "sorted(values)[len(values)//2], the upper middle order statistic for "
            "even n. This audit reports the conventional median. Repository-wide "
            "inspection found this historical definition only in the Stage III timing "
            "summary path; the inherited H3 paired reductions were computed separately "
            "from locked paired outcomes and are not affected by this correction."
        ),
        "domains": domains,
        "between_domain_median_differences": _between_domain_difference_bootstrap(
            groups_by_domain, bootstrap_replicates
        ),
    }


def _write_difference_csv(audit_result: dict[str, Any], path: str | Path) -> None:
    fields = [
        "endpoint",
        "absolute_generations_difference_directional_minus_symmetric",
        "absolute_generations_ci_lower",
        "absolute_generations_ci_upper",
        "absolute_generations_ci_includes_zero",
        "horizon_fraction_difference_directional_minus_symmetric",
        "horizon_fraction_ci_lower",
        "horizon_fraction_ci_upper",
        "horizon_fraction_ci_includes_zero",
        "hold_fraction_difference_directional_minus_symmetric",
        "hold_fraction_ci_lower",
        "hold_fraction_ci_upper",
        "hold_fraction_ci_includes_zero",
    ]
    rows: list[dict[str, Any]] = []
    for endpoint in ENDPOINTS:
        difference = audit_result["between_domain_median_differences"][endpoint]
        row: dict[str, Any] = {"endpoint": endpoint}
        for metric in ("absolute_generations", "horizon_fraction", "hold_fraction"):
            values = difference[metric]
            interval = values["bootstrap_95_ci"]
            row[f"{metric}_difference_directional_minus_symmetric"] = values[
                "directional_minus_symmetric"
            ]
            row[f"{metric}_ci_lower"] = interval["lower"]
            row[f"{metric}_ci_upper"] = interval["upper"]
            row[f"{metric}_ci_includes_zero"] = values["ci_includes_zero"]
        rows.append(row)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(
    audit_result: dict[str, Any],
    json_path: str | Path,
    csv_path: str | Path,
    difference_csv_path: str | Path | None = None,
) -> None:
    json_target = Path(json_path)
    json_target.parent.mkdir(parents=True, exist_ok=True)
    json_target.write_text(
        json.dumps(audit_result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    fields = [
        "domain",
        "endpoint",
        "attempted",
        "positive_leads",
        "valid_pairs",
        "lead",
        "tie",
        "lag",
        "source_preparation_failed",
        "baseline_ineligible",
        "both_censored",
        "warning_censored",
        "trait_loss_censored",
        "median_positive_lead_time",
        "median_positive_lead_time_ci_lower",
        "median_positive_lead_time_ci_upper",
        "median_positive_lead_fraction_of_horizon",
        "median_positive_lead_fraction_of_horizon_ci_lower",
        "median_positive_lead_fraction_of_horizon_ci_upper",
    ]
    rows: list[dict[str, Any]] = []
    for domain, domain_data in audit_result["domains"].items():
        for endpoint, endpoint_data in domain_data["endpoints"].items():
            interval = domain_data["endpoint_bootstrap_95_ci"][endpoint]
            counts = endpoint_data["counts"]
            rows.append(
                {
                    "domain": domain,
                    "endpoint": endpoint,
                    "attempted": endpoint_data["attempted"],
                    "positive_leads": endpoint_data["positive_leads"],
                    "valid_pairs": endpoint_data["valid_pairs"],
                    "lead": counts["lead"],
                    "tie": counts["tie"],
                    "lag": counts["lag"],
                    "source_preparation_failed": counts["source_preparation_failed"],
                    "baseline_ineligible": counts["baseline_ineligible"],
                    "both_censored": counts["both_censored"],
                    "warning_censored": counts["warning_censored"],
                    "trait_loss_censored": counts["trait_loss_censored"],
                    "median_positive_lead_time": endpoint_data[
                        "median_positive_lead_time"
                    ],
                    "median_positive_lead_time_ci_lower": interval[
                        "median_positive_lead_time"
                    ]["lower"],
                    "median_positive_lead_time_ci_upper": interval[
                        "median_positive_lead_time"
                    ]["upper"],
                    "median_positive_lead_fraction_of_horizon": endpoint_data[
                        "median_positive_lead_fraction_of_horizon"
                    ],
                    "median_positive_lead_fraction_of_horizon_ci_lower": interval[
                        "median_positive_lead_fraction_of_horizon"
                    ]["lower"],
                    "median_positive_lead_fraction_of_horizon_ci_upper": interval[
                        "median_positive_lead_fraction_of_horizon"
                    ]["upper"],
                }
            )
    csv_target = Path(csv_path)
    csv_target.parent.mkdir(parents=True, exist_ok=True)
    with csv_target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    if difference_csv_path is not None:
        _write_difference_csv(audit_result, difference_csv_path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("records")
    parser.add_argument("json_output")
    parser.add_argument("csv_output")
    parser.add_argument("--difference-csv")
    parser.add_argument(
        "--bootstrap-replicates", type=int, default=DEFAULT_BOOTSTRAP_REPLICATES
    )
    args = parser.parse_args()
    write_outputs(
        audit(load_records(args.records), args.bootstrap_replicates),
        args.json_output,
        args.csv_output,
        args.difference_csv,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
