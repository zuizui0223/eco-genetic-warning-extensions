from __future__ import annotations

import json
import math
from pathlib import Path
from statistics import fmean, stdev
from typing import Any

from .operator_balance_route_margin import q_only_route_margin, route_margin

PROTOCOL_PATH = Path(__file__).resolve().parents[2] / "experiments" / "operator_balance_margin_fate_protocol.json"


def load_protocol(path: str | Path = PROTOCOL_PATH) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("status") != "prospective_locked_before_run":
        raise RuntimeError("operator-balance protocol is not prospectively locked")
    return payload


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
    return (master_seed * 1_000_003 + replicate * 103 + 53) % (2**31 - 1)


def barrier_schedule(generations: int) -> tuple[float, ...]:
    return tuple(0.50 + 0.15 * generation / 60.0 for generation in range(1, generations + 1))


def _parameters(condition: dict[str, Any], seed: int, generations: int):
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


def _sign(value: float, tolerance: float = 1e-10) -> int:
    if value > tolerance:
        return 1
    if value < -tolerance:
        return -1
    return 0


def _trajectory_record(
    condition_name: str,
    condition: dict[str, Any],
    master_seed: int,
    replicate: int,
    generations: int,
    marker_generation: int,
) -> dict[str, Any]:
    from causal_model.multipatch_criticality_dynamics import tau_trait_realised
    from causal_model.symmetric_allele_mutation_closure import simulate_with_symmetric_allele_mutation

    seed = _seed(master_seed, replicate)
    params = _parameters(condition, seed, generations)
    barriers = barrier_schedule(generations)
    result = simulate_with_symmetric_allele_mutation(
        params,
        mutation_rate=0.0,
        interaction_barrier_schedule=barriers,
    )
    loss_time = tau_trait_realised(result)
    alpha, beta, gamma = (float(x) for x in condition["q_feedback"])

    positive_refuge_generations = 0
    repair_wedge_patch_generations = 0
    suppression_wedge_patch_generations = 0
    first_all_negative: int | None = None
    marker_all_negative = False
    marker_max_margin = None
    exact_audit_count = 0

    for generation in range(1, generations + 1):
        current = result.snapshots[generation - 1]
        nxt = result.snapshots[generation]
        theta = barriers[generation - 1]
        carrying = tuple(params.density_capacity * area for area in params.patch_areas)
        densities = tuple(min(1.0, n / k) for n, k in zip(current.population, carrying))
        masses = tuple(x.high_trait_mass for x in current.trait_occupancy)
        margins: list[float] = []
        qonly_margins: list[float] = []
        for q, t, g, d, q_next in zip(
            current.interaction,
            masses,
            current.high_allele_frequency,
            densities,
            nxt.interaction,
        ):
            margin = route_margin(
                q,
                t,
                g,
                d,
                theta,
                alpha=alpha,
                beta_trait=beta,
                gamma_allele=gamma,
            )
            q0 = q_only_route_margin(q, d, theta)
            margins.append(margin)
            qonly_margins.append(q0)
            if _sign(margin) != _sign(float(q_next) - 0.625):
                raise RuntimeError(
                    f"exact route-margin audit failed for {condition_name} seed={seed} generation={generation}: "
                    f"margin={margin} q_next={q_next}"
                )
            exact_audit_count += 1
            if beta + gamma > 0.0:
                repair_wedge_patch_generations += q0 < 0.0 <= margin
                suppression_wedge_patch_generations += margin < 0.0 <= q0

        any_positive = any(m >= 0.0 for m in margins)
        all_negative = all(m < 0.0 for m in margins)
        positive_refuge_generations += any_positive
        if all_negative and first_all_negative is None:
            first_all_negative = generation
        if generation == marker_generation:
            marker_all_negative = all_negative
            marker_max_margin = max(margins)

    return {
        "condition": condition_name,
        "master_seed": int(master_seed),
        "replicate": int(replicate),
        "trajectory_seed": int(seed),
        "loss_time": None if loss_time in {None, 0} else int(loss_time),
        "loss_by_endpoint": bool(loss_time is not None and loss_time != 0 and int(loss_time) <= generations),
        "positive_margin_refuge_generations": int(positive_refuge_generations),
        "repair_wedge_patch_generations": int(repair_wedge_patch_generations),
        "suppression_wedge_patch_generations": int(suppression_wedge_patch_generations),
        "first_all_negative_margin_generation": first_all_negative,
        "marker_all_negative": bool(marker_all_negative),
        "marker_max_margin": float(marker_max_margin) if marker_max_margin is not None else None,
        "exact_audit_patch_generations": int(exact_audit_count),
    }


def simulate(protocol: dict[str, Any]) -> list[dict[str, Any]]:
    rep = protocol["replication"]
    generations = int(protocol["forcing"]["generations"])
    marker_generation = int(protocol["forcing"]["primary_marker_generation"])
    records: list[dict[str, Any]] = []
    for master_seed in (int(x) for x in rep["master_seeds"]):
        for replicate in range(int(rep["replicates_per_seed"])):
            for name, condition in protocol["conditions"].items():
                records.append(
                    _trajectory_record(
                        name,
                        condition,
                        master_seed,
                        replicate,
                        generations,
                        marker_generation,
                    )
                )
    return records


def _mean_ci(values: list[float]) -> dict[str, Any]:
    if not values:
        raise ValueError("empty values")
    mean = fmean(values)
    if len(values) == 1:
        return {"mean": mean, "ci95": [mean, mean], "n": 1}
    se = stdev(values) / math.sqrt(len(values))
    return {"mean": mean, "ci95": [mean - 1.96 * se, mean + 1.96 * se], "n": len(values)}


def _by_key(records: list[dict[str, Any]]) -> dict[tuple[str, int, int], dict[str, Any]]:
    return {(r["condition"], int(r["master_seed"]), int(r["replicate"])): r for r in records}


def _keys(records: list[dict[str, Any]]) -> list[tuple[int, int]]:
    return sorted({(int(r["master_seed"]), int(r["replicate"])) for r in records})


def _marker_metrics(records: list[dict[str, Any]], conditions: tuple[str, ...]) -> dict[str, Any]:
    selected = [r for r in records if r["condition"] in conditions]
    tp = fp = tn = fn = 0
    lead_event_count = 0
    event_count = 0
    for r in selected:
        marker = bool(r["marker_all_negative"])
        event = bool(r["loss_by_endpoint"])
        if marker and event:
            tp += 1
        elif marker and not event:
            fp += 1
        elif not marker and event:
            fn += 1
        else:
            tn += 1
        if event:
            event_count += 1
            first = r["first_all_negative_margin_generation"]
            loss_time = r["loss_time"]
            if first is not None and loss_time is not None and int(first) <= int(loss_time):
                lead_event_count += 1

    def ratio(a: int, b: int) -> float | None:
        return None if b == 0 else a / b

    sensitivity = ratio(tp, tp + fn)
    specificity = ratio(tn, tn + fp)
    ppv = ratio(tp, tp + fp)
    npv = ratio(tn, tn + fn)
    fpr = None if specificity is None else 1.0 - specificity
    auc = None if sensitivity is None or specificity is None else (sensitivity + specificity) / 2.0
    return {
        "conditions": list(conditions),
        "n": len(selected),
        "events": event_count,
        "non_events": len(selected) - event_count,
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "sensitivity": sensitivity,
        "specificity": specificity,
        "false_positive_rate": fpr,
        "ppv": ppv,
        "npv": npv,
        "binary_auc": auc,
        "event_side_precedence_fraction": ratio(lead_event_count, event_count),
    }


def summarise(protocol: dict[str, Any], records: list[dict[str, Any]]) -> dict[str, Any]:
    lookup = _by_key(records)
    keys = _keys(records)
    expected_per_condition = int(protocol["replication"]["paired_keys_per_condition"])
    for condition in protocol["conditions"]:
        assert sum(r["condition"] == condition for r in records) == expected_per_condition

    aa_extensions: list[float] = []
    rr_extensions: list[float] = []
    dids: list[float] = []
    repair_rr_minus_aa: list[float] = []
    suppression_rr_minus_aa: list[float] = []
    for master, replicate in keys:
        aa_full = lookup[("AA_full", master, replicate)]
        aa_q = lookup[("AA_q_only", master, replicate)]
        rr_full = lookup[("RR_full", master, replicate)]
        rr_q = lookup[("RR_q_only", master, replicate)]
        aa_ext = float(aa_full["positive_margin_refuge_generations"] - aa_q["positive_margin_refuge_generations"])
        rr_ext = float(rr_full["positive_margin_refuge_generations"] - rr_q["positive_margin_refuge_generations"])
        aa_extensions.append(aa_ext)
        rr_extensions.append(rr_ext)
        dids.append(rr_ext - aa_ext)
        repair_rr_minus_aa.append(
            float(rr_full["repair_wedge_patch_generations"] - aa_full["repair_wedge_patch_generations"])
        )
        suppression_rr_minus_aa.append(
            float(rr_full["suppression_wedge_patch_generations"] - aa_full["suppression_wedge_patch_generations"])
        )

    primary = _mean_ci(dids)
    lo, hi = primary["ci95"]
    if lo > 0.0:
        decision = "resolved_preferential_RR_route_repair"
    elif hi < 0.0:
        decision = "resolved_opposite_direction"
    else:
        decision = "unresolved"

    exact_audits = sum(int(r["exact_audit_patch_generations"]) for r in records)
    expected_audits = len(records) * int(protocol["forcing"]["generations"]) * 4
    if exact_audits != expected_audits:
        raise RuntimeError(f"audit count mismatch {exact_audits} != {expected_audits}")

    marker = {
        "AA_full": _marker_metrics(records, ("AA_full",)),
        "RR_full": _marker_metrics(records, ("RR_full",)),
        "pooled_full": _marker_metrics(records, ("AA_full", "RR_full")),
    }

    return {
        "experiment_id": protocol["experiment_id"],
        "status": "completed_from_locked_protocol",
        "protocol_status": protocol["status"],
        "n_records": len(records),
        "n_paired_keys": len(keys),
        "exact_transition_audit": {
            "patch_generations_checked": exact_audits,
            "mismatches": 0,
        },
        "direct_feedback_extension": {
            "AA_full_minus_qonly": _mean_ci(aa_extensions),
            "RR_full_minus_qonly": _mean_ci(rr_extensions),
            "RR_minus_AA_DID": primary,
            "decision": decision,
        },
        "repair_wedge": {
            "RR_minus_AA_patch_generations": _mean_ci(repair_rr_minus_aa),
            "suppression_RR_minus_AA_patch_generations": _mean_ci(suppression_rr_minus_aa),
        },
        "full_denominator_marker_generation_20_to_loss_generation_40": marker,
        "claim_ceiling": (
            "The route margin is exact for the one-step switch. The finite experiment may support or reject a "
            "long-horizon route-repair interpretation, but the generation-20 marker is not promoted to a warning "
            "without full-denominator specificity/discrimination. Natural systems are not validation data."
        ),
    }


def run(protocol_path: str | Path = PROTOCOL_PATH) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    protocol = load_protocol(protocol_path)
    seeds = tuple(int(x) for x in protocol["replication"]["master_seeds"])
    if len(seeds) != 6 or len(set(seeds)) != 6:
        raise RuntimeError("locked protocol must contain six distinct master seeds")
    if not math.isclose(float(protocol["theorem"]["headroom_constant"]), 0.11351680528133122, abs_tol=1e-15):
        raise RuntimeError("route-margin headroom constant drift")
    records = simulate(protocol)
    return summarise(protocol, records), records


def write(summary_path: str | Path, records_path: str | Path, protocol_path: str | Path = PROTOCOL_PATH) -> None:
    summary, records = run(protocol_path)
    summary_dest = Path(summary_path)
    records_dest = Path(records_path)
    summary_dest.parent.mkdir(parents=True, exist_ok=True)
    records_dest.parent.mkdir(parents=True, exist_ok=True)
    summary_dest.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    records_dest.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
