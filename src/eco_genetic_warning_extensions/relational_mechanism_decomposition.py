from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from statistics import fmean
from typing import Any

PROTOCOL_PATH = Path(__file__).resolve().parents[2] / "experiments" / "relational_mechanism_decomposition_protocol.json"


def load_protocol(path: str | Path = PROTOCOL_PATH) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("status") != "prospective_locked_before_run":
        raise RuntimeError("mechanism protocol is not locked before run")
    return payload


def _variance(values: tuple[float, ...]) -> float:
    mean = fmean(values)
    return fmean((value - mean) ** 2 for value in values)


def _covariance(x: tuple[float, ...], y: tuple[float, ...]) -> float:
    mx, my = fmean(x), fmean(y)
    return fmean((a - mx) * (b - my) for a, b in zip(x, y))


def _assignment(kind: str) -> tuple[float, ...]:
    base = (0.20, 0.40, 0.60, 0.80)
    if kind == "ascending":
        return base
    if kind == "descending":
        return tuple(reversed(base))
    raise ValueError(kind)


def _trait_abundance(values: tuple[float, ...], grid_size: int = 31) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    for fraction in values:
        high = int(round(40 * fraction))
        row = [0] * grid_size
        row[0] = 40 - high
        row[-1] = high
        rows.append(tuple(row))
    return tuple(rows)


def _seed(master_seed: int, replicate: int) -> int:
    return (master_seed * 1_000_003 + replicate * 101 + 17) % (2**31 - 1)


def barrier_schedule(generations: int) -> tuple[float, ...]:
    return tuple(0.50 + 0.15 * generation / 60.0 for generation in range(1, generations + 1))


def _parameters(condition_name: str, condition: dict[str, Any], seed: int, generations: int):
    from causal_model.multipatch_criticality_dynamics import DynamicsParameters

    trait_values = _assignment(str(condition["trait_assignment"]))
    allele_values = _assignment(str(condition["allele_assignment"]))
    alpha, beta, gamma = (float(x) for x in condition["q_feedback"])
    return DynamicsParameters(
        patch_areas=(1.0, 1.0, 1.0, 1.0),
        generations=generations,
        initial_population=(40, 40, 40, 40),
        initial_interaction=(0.65, 0.75, 0.85, 0.95),
        initial_high_allele_frequency=allele_values,
        initial_trait_abundance=_trait_abundance(trait_values),
        density_capacity=40.0,
        area_reference=1.0,
        interaction_feedback=4.5,
        interaction_barrier=0.50,
        trait_grid_size=31,
        trait_occupancy_mode="finite_trait_bin_recruitment",
        genotype_trait_recruitment="two_kernel_recruitment",
        inheritance_weight=0.5,
        q_feedback_alpha=alpha,
        q_feedback_beta_trait=beta,
        q_feedback_gamma_allele=gamma,
        migration_rate=0.0,
        random_seed=seed,
    )


def _support(snapshot, params) -> tuple[float, ...]:
    from causal_model.multipatch_criticality_dynamics import interaction_support_signal

    return tuple(
        interaction_support_signal(q, occupancy.high_trait_mass, allele, params)
        for q, occupancy, allele in zip(
            snapshot.interaction,
            snapshot.trait_occupancy,
            snapshot.high_allele_frequency,
        )
    )


def analytic_baseline(protocol: dict[str, Any]) -> dict[str, Any]:
    q = tuple(float(x) for x in protocol["locked_parent_state"]["initial_interaction"])
    out: dict[str, Any] = {}
    for name, condition in protocol["conditions"].items():
        trait = _assignment(str(condition["trait_assignment"]))
        allele = _assignment(str(condition["allele_assignment"]))
        alpha, beta, gamma = (float(x) for x in condition["q_feedback"])
        support = tuple(alpha * x + beta * t + gamma * g for x, t, g in zip(q, trait, allele))
        predicted_variance = (
            alpha**2 * _variance(q)
            + beta**2 * _variance(trait)
            + gamma**2 * _variance(allele)
            + 2.0 * alpha * beta * _covariance(q, trait)
            + 2.0 * alpha * gamma * _covariance(q, allele)
            + 2.0 * beta * gamma * _covariance(trait, allele)
        )
        out[name] = {
            "trait": trait,
            "allele": allele,
            "support": support,
            "support_mean": fmean(support),
            "support_variance": _variance(support),
            "support_variance_from_covariance_identity": predicted_variance,
            "cov_q_trait": _covariance(q, trait),
            "cov_q_allele": _covariance(q, allele),
            "cov_trait_allele": _covariance(trait, allele),
            "max_support": max(support),
            "min_support": min(support),
        }
    return out


def _trajectory_record(condition_name: str, condition: dict[str, Any], master_seed: int, replicate: int, generations: int, horizons: tuple[int, ...]) -> dict[str, Any]:
    from causal_model.multipatch_criticality_dynamics import tau_trait_realised
    from causal_model.symmetric_allele_mutation_closure import simulate_with_symmetric_allele_mutation

    seed = _seed(master_seed, replicate)
    params = _parameters(condition_name, condition, seed, generations)
    result = simulate_with_symmetric_allele_mutation(
        params,
        mutation_rate=0.0,
        interaction_barrier_schedule=barrier_schedule(generations),
    )
    loss_time = tau_trait_realised(result)
    states: dict[str, Any] = {}
    q_threshold = 0.625
    for horizon in horizons:
        snap = result.snapshots[horizon]
        support = _support(snap, params)
        occupied = tuple(bool(x.realised_high_trait_occupied) for x in snap.trait_occupancy)
        states[str(horizon)] = {
            "support_mean": fmean(support),
            "support_variance": _variance(support),
            "max_support": max(support),
            "min_support": min(support),
            "max_q": max(snap.interaction),
            "mean_q": fmean(snap.interaction),
            "q_variance": _variance(tuple(float(x) for x in snap.interaction)),
            "q_refugia_count": sum(float(q) >= q_threshold for q in snap.interaction),
            "realised_refugia_count": sum(occupied),
            "max_high_trait_mass": max(x.high_trait_mass for x in snap.trait_occupancy),
        }
    return {
        "condition": condition_name,
        "master_seed": int(master_seed),
        "replicate": int(replicate),
        "trajectory_seed": int(seed),
        "last_refuge_loss_time": None if loss_time in {None, 0} else int(loss_time),
        "states": states,
    }


def simulate(protocol: dict[str, Any]) -> list[dict[str, Any]]:
    rep = protocol["replication"]
    horizons = tuple(int(x) for x in protocol["forcing"]["report_horizons"])
    generations = int(protocol["forcing"]["generations"])
    records: list[dict[str, Any]] = []
    for master_seed in (int(x) for x in rep["master_seeds"]):
        for replicate in range(int(rep["replicates_per_seed"])):
            for condition_name, condition in protocol["conditions"].items():
                records.append(
                    _trajectory_record(
                        condition_name,
                        condition,
                        master_seed,
                        replicate,
                        generations,
                        horizons,
                    )
                )
    return records


def _mean_metric(records: list[dict[str, Any]], condition: str, horizon: int, metric: str) -> float:
    values = [float(r["states"][str(horizon)][metric]) for r in records if r["condition"] == condition]
    return fmean(values)


def _loss_rate(records: list[dict[str, Any]], condition: str, horizon: int) -> float:
    selected = [r for r in records if r["condition"] == condition]
    return fmean(
        r["last_refuge_loss_time"] is not None and int(r["last_refuge_loss_time"]) <= horizon
        for r in selected
    )


def _paired_binary_difference(records: list[dict[str, Any]], a: str, b: str, horizon: int) -> dict[str, Any]:
    selected = {(r["condition"], r["master_seed"], r["replicate"]): r for r in records if r["condition"] in {a, b}}
    keys = sorted({(r["master_seed"], r["replicate"]) for r in records if r["condition"] == a})
    a_only = b_only = same_loss = same_no = 0
    for master, replicate in keys:
        ar = selected[(a, master, replicate)]
        br = selected[(b, master, replicate)]
        al = ar["last_refuge_loss_time"] is not None and int(ar["last_refuge_loss_time"]) <= horizon
        bl = br["last_refuge_loss_time"] is not None and int(br["last_refuge_loss_time"]) <= horizon
        if al and not bl:
            a_only += 1
        elif bl and not al:
            b_only += 1
        elif al and bl:
            same_loss += 1
        else:
            same_no += 1
    n = len(keys)
    diff = (b_only - a_only) / n
    discordance = (a_only + b_only) / n
    se = math.sqrt(max(0.0, discordance - diff * diff) / n)
    return {
        "a": a,
        "b": b,
        "horizon": horizon,
        "n_pairs": n,
        "risk_difference_b_minus_a": diff,
        "ci95": [diff - 1.96 * se, diff + 1.96 * se],
        "a_only_loss": a_only,
        "b_only_loss": b_only,
        "same_loss": same_loss,
        "same_no_loss": same_no,
    }


def summarise(protocol: dict[str, Any], records: list[dict[str, Any]]) -> dict[str, Any]:
    horizons = tuple(int(x) for x in protocol["forcing"]["report_horizons"])
    conditions = tuple(protocol["conditions"])
    metrics = (
        "support_mean",
        "support_variance",
        "max_support",
        "max_q",
        "mean_q",
        "q_variance",
        "q_refugia_count",
        "realised_refugia_count",
        "max_high_trait_mass",
    )
    cells: dict[str, Any] = {}
    for condition in conditions:
        cells[condition] = {}
        for horizon in horizons:
            cells[condition][str(horizon)] = {
                **{metric: _mean_metric(records, condition, horizon, metric) for metric in metrics},
                "loss_rate": _loss_rate(records, condition, horizon),
            }

    paired = []
    for horizon in (20, 40):
        paired.append(_paired_binary_difference(records, "AA_full", "RR_full", horizon))
        paired.append(_paired_binary_difference(records, "AA_q_only", "RR_q_only", horizon))

    # Factorial risk effects: positive = reversed assignment raises loss risk.
    factorial: dict[str, Any] = {}
    for horizon in (20, 40):
        risks = {c: _loss_rate(records, c, horizon) for c in ("AA_full", "AR_full", "RA_full", "RR_full")}
        trait_reversal = ((risks["RA_full"] + risks["RR_full"]) - (risks["AA_full"] + risks["AR_full"])) / 2.0
        allele_reversal = ((risks["AR_full"] + risks["RR_full"]) - (risks["AA_full"] + risks["RA_full"])) / 2.0
        interaction = risks["RR_full"] - risks["RA_full"] - risks["AR_full"] + risks["AA_full"]
        factorial[str(horizon)] = {
            "risks": risks,
            "trait_reversal_main_effect": trait_reversal,
            "allele_reversal_main_effect": allele_reversal,
            "trait_by_allele_interaction": interaction,
        }

    analytic = analytic_baseline(protocol)
    aa, rr = analytic["AA_full"], analytic["RR_full"]
    return {
        "experiment_id": protocol["experiment_id"],
        "status": "completed_from_locked_protocol",
        "analytic_baseline": analytic,
        "analytic_headline": {
            "AA_RR_support_mean_difference": aa["support_mean"] - rr["support_mean"],
            "AA_RR_support_variance_ratio": aa["support_variance"] / rr["support_variance"],
            "AA_RR_support_variance_difference": aa["support_variance"] - rr["support_variance"],
        },
        "trajectory_cells": cells,
        "paired_primary": paired,
        "factorial_loss_decomposition": factorial,
        "claim_boundary": protocol["mechanistic_hypothesis"]["claim_boundary"],
    }


def run(protocol_path: str | Path = PROTOCOL_PATH) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    protocol = load_protocol(protocol_path)
    # Exact pre-run contract check for z=1 high-trait viability threshold.
    from causal_model.multipatch_criticality_dynamics import DynamicsParameters, trait_fitness

    check = DynamicsParameters(patch_areas=(1.0,))
    q_star = (check.viability_threshold - (check.low_base - check.low_cost) - check.high_base) / check.high_interaction_benefit
    expected = float(protocol["locked_parent_state"]["high_trait_viability_q_threshold_at_z1"])
    if not math.isclose(q_star, expected, rel_tol=0.0, abs_tol=1e-12):
        raise RuntimeError(f"q viability threshold drift: {q_star} != {expected}")
    records = simulate(protocol)
    return summarise(protocol, records), records


def write(summary_path: str | Path, records_path: str | Path, protocol_path: str | Path = PROTOCOL_PATH) -> None:
    summary, records = run(protocol_path)
    summary_dest, records_dest = Path(summary_path), Path(records_path)
    summary_dest.parent.mkdir(parents=True, exist_ok=True)
    records_dest.parent.mkdir(parents=True, exist_ok=True)
    summary_dest.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    records_dest.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
