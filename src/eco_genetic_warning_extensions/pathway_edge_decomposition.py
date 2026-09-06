from __future__ import annotations

import json
import math
from dataclasses import replace
from math import exp
from pathlib import Path
from random import Random
from statistics import fmean
from typing import Any, Iterable

PROTOCOL_PATH = Path(__file__).resolve().parents[2] / "experiments" / "pathway_edge_decomposition_protocol.json"


def load_protocol(path: str | Path = PROTOCOL_PATH) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("status") != "prospective_locked_before_run":
        raise RuntimeError("pathway edge-decomposition protocol is not prospectively locked")
    if len(payload.get("interventions", {})) != 8:
        raise RuntimeError("expected exactly eight locked interventions")
    return payload


def _variance(values: Iterable[float]) -> float:
    values = tuple(float(x) for x in values)
    mean = fmean(values)
    return fmean((x - mean) ** 2 for x in values)


def _seed(master_seed: int, replicate: int, intervention_index: int) -> int:
    # Same AA/RR seed within intervention. Intervention offset keeps streams
    # independent across edge deletions while preserving paired keys.
    return (master_seed * 1_000_003 + replicate * 101 + intervention_index * 10_007 + 29) % (2**31 - 1)


def barrier_schedule(generations: int) -> tuple[float, ...]:
    return tuple(0.50 + 0.15 * generation / 60.0 for generation in range(1, generations + 1))


def _trait_abundance(fractions: tuple[float, ...], grid_size: int = 31) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    for fraction in fractions:
        high = int(round(40 * fraction))
        row = [0] * grid_size
        row[0] = 40 - high
        row[-1] = high
        rows.append(tuple(row))
    return tuple(rows)


def _condition_values(protocol: dict[str, Any], condition: str) -> tuple[tuple[float, ...], tuple[float, ...]]:
    fixed = protocol["fixed_state"]
    if condition == "AA":
        return tuple(float(x) for x in fixed["AA_trait_assignment"]), tuple(float(x) for x in fixed["AA_allele_assignment"])
    if condition == "RR":
        return tuple(float(x) for x in fixed["RR_trait_assignment"]), tuple(float(x) for x in fixed["RR_allele_assignment"])
    raise ValueError(condition)


def _parameters(protocol: dict[str, Any], intervention: dict[str, Any], condition: str, seed: int, generations: int):
    from causal_model.multipatch_criticality_dynamics import DynamicsParameters

    trait_values, allele_values = _condition_values(protocol, condition)
    allele_linked = bool(intervention["allele_linked_recruitment"])
    inheritance_weight = float(intervention["resident_inheritance_weight"])
    state_dep_demo = bool(intervention["state_dependent_demography"])
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
        genotype_trait_recruitment="two_kernel_recruitment" if allele_linked else "resident_trait_only",
        inheritance_weight=inheritance_weight,
        q_feedback_alpha=1.0,
        q_feedback_beta_trait=0.0,
        q_feedback_gamma_allele=0.0,
        interaction_growth=0.4 if state_dep_demo else 0.0,
        high_allele_growth=0.1 if state_dep_demo else 0.0,
        migration_rate=0.0,
        random_seed=seed,
    )


def _trait_update(
    abundance,
    selection_q: float,
    high_allele_frequency: float,
    next_population: int,
    params,
    rng: Random,
):
    from causal_model.multipatch_criticality_dynamics import (
        _multinomial,
        _normalise_distribution,
        recruit_trait_distribution,
        trait_fitness,
        trait_grid,
    )

    resident = _normalise_distribution(abundance)
    recruit = recruit_trait_distribution(resident, high_allele_frequency, params)
    grid = trait_grid(params)
    selected = _normalise_distribution(
        mass * max(params.trait_selection_floor, trait_fitness(z, selection_q, params))
        for z, mass in zip(grid, recruit)
    )
    return _multinomial(rng, next_population, selected)


def _simulate_one(protocol: dict[str, Any], intervention_name: str, intervention: dict[str, Any], condition: str, master_seed: int, replicate: int, intervention_index: int) -> dict[str, Any]:
    from causal_model.multipatch_criticality_dynamics import (
        SimulationResult,
        _binomial,
        _effective_size,
        _initial_values,
        _normalise_distribution,
        _snapshot,
        sigmoid,
        tau_trait_realised,
        trait_fitness,
    )

    generations = int(protocol["forcing"]["generations"])
    horizons = tuple(int(x) for x in protocol["forcing"]["report_horizons"])
    barriers = barrier_schedule(generations)
    seed = _seed(master_seed, replicate, intervention_index)
    params = _parameters(protocol, intervention, condition, seed, generations)
    rng = Random(seed)
    population, interaction, frequency, trait_distribution, trait_abundance = _initial_values(params)
    snapshots = [_snapshot(0, population, interaction, frequency, trait_distribution, trait_abundance, params)]

    for generation in range(1, generations + 1):
        barrier = barriers[generation - 1]
        carrying = tuple(params.density_capacity * area for area in params.patch_areas)
        if bool(intervention["density_in_q_update"]):
            density = tuple(min(1.0, n / k) for n, k in zip(population, carrying))
        else:
            density = tuple(1.0 for _ in population)

        # Direct T/G -> q was removed in the parent q-only intervention and
        # remains removed in every edge-deletion condition here.
        q_next = tuple(
            sigmoid(params.interaction_feedback * ((area / params.area_reference) * dens * q - barrier))
            for area, dens, q in zip(params.patch_areas, density, interaction)
        )

        q_for_allele = q_next
        if str(intervention["allele_selection_mode"]) == "spatial_mean_q":
            mean_q = fmean(q_next)
            q_for_allele = tuple(mean_q for _ in q_next)

        selected_allele: list[float] = []
        for q_sel, p in zip(q_for_allele, frequency):
            high_margin = trait_fitness(1.0, q_sel, params) - params.viability_threshold
            high_fitness = max(1e-12, 1.0 + params.selection_strength * high_margin)
            mean_fitness = p * high_fitness + (1.0 - p)
            selected_allele.append(p * high_fitness / mean_fitness)

        next_population: list[int] = []
        for n, k, q, p_selected in zip(population, carrying, q_next, selected_allele):
            exponent = params.baseline_growth + params.interaction_growth * q + params.high_allele_growth * p_selected - n / k
            next_population.append(max(1, round(n * exp(exponent))))

        q_for_trait = interaction
        if str(intervention["trait_selection_mode"]) == "spatial_mean_q":
            mean_q_trait = fmean(interaction)
            q_for_trait = tuple(mean_q_trait for _ in interaction)

        next_trait_abundance = tuple(
            _trait_update(abundance, q_sel, p, n_next, params, rng)
            for abundance, q_sel, p, n_next in zip(trait_abundance, q_for_trait, frequency, next_population)
        )
        next_trait_distribution = tuple(_normalise_distribution(row) for row in next_trait_abundance)

        next_frequency: list[float] = []
        for n, q, p in zip(next_population, q_next, selected_allele):
            n_eff = _effective_size(n, q, params)
            gene_copies = max(2, round(2.0 * n_eff))
            next_frequency.append(_binomial(rng, gene_copies, p) / gene_copies)

        population = tuple(next_population)
        interaction = tuple(q_next)
        frequency = tuple(next_frequency)
        trait_distribution = next_trait_distribution
        trait_abundance = next_trait_abundance
        snapshots.append(_snapshot(generation, population, interaction, frequency, trait_distribution, trait_abundance, params))

    result = SimulationResult(params, tuple(snapshots))
    loss_time = tau_trait_realised(result)
    states: dict[str, Any] = {}
    for horizon in horizons:
        snap = result.snapshots[horizon]
        high_mass = tuple(float(x.high_trait_mass) for x in snap.trait_occupancy)
        states[str(horizon)] = {
            "mean_high_trait_mass": fmean(high_mass),
            "max_high_trait_mass": max(high_mass),
            "realised_refugia_count": sum(bool(x.realised_high_trait_occupied) for x in snap.trait_occupancy),
            "mean_q": fmean(snap.interaction),
            "max_q": max(snap.interaction),
            "mean_population": fmean(snap.population),
            "population_variance": _variance(snap.population),
            "mean_allele_frequency": fmean(snap.high_allele_frequency),
            "allele_frequency_variance": _variance(snap.high_allele_frequency),
        }
    return {
        "intervention": intervention_name,
        "condition": condition,
        "master_seed": int(master_seed),
        "replicate": int(replicate),
        "trajectory_seed": int(seed),
        "last_refuge_loss_time": None if loss_time in {None, 0} else int(loss_time),
        "states": states,
    }


def simulate(protocol: dict[str, Any]) -> list[dict[str, Any]]:
    rep = protocol["replication"]
    records: list[dict[str, Any]] = []
    interventions = list(protocol["interventions"].items())
    for intervention_index, (intervention_name, intervention) in enumerate(interventions):
        for master_seed in (int(x) for x in rep["master_seeds"]):
            for replicate in range(int(rep["replicates_per_seed"])):
                for condition in ("AA", "RR"):
                    records.append(
                        _simulate_one(
                            protocol,
                            intervention_name,
                            intervention,
                            condition,
                            master_seed,
                            replicate,
                            intervention_index,
                        )
                    )
    return records


def _loss_indicator(record: dict[str, Any], horizon: int) -> int:
    t = record["last_refuge_loss_time"]
    return int(t is not None and int(t) <= horizon)


def _paired_d(records: list[dict[str, Any]], intervention: str, horizon: int) -> dict[tuple[int, int], int]:
    selected = {
        (r["condition"], int(r["master_seed"]), int(r["replicate"])): r
        for r in records
        if r["intervention"] == intervention
    }
    keys = sorted((m, r) for c, m, r in selected if c == "AA")
    return {
        key: _loss_indicator(selected[("RR", *key)], horizon) - _loss_indicator(selected[("AA", *key)], horizon)
        for key in keys
    }


def _mean_ci(values: Iterable[float]) -> tuple[float, list[float]]:
    values = tuple(float(x) for x in values)
    mean = fmean(values)
    if len(values) < 2:
        return mean, [mean, mean]
    var = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    se = math.sqrt(var / len(values))
    return mean, [mean - 1.96 * se, mean + 1.96 * se]


def _risk_pair_summary(records: list[dict[str, Any]], intervention: str, horizon: int) -> dict[str, Any]:
    d = _paired_d(records, intervention, horizon)
    effect, ci = _mean_ci(d.values())
    aa = [r for r in records if r["intervention"] == intervention and r["condition"] == "AA"]
    rr = [r for r in records if r["intervention"] == intervention and r["condition"] == "RR"]
    return {
        "intervention": intervention,
        "horizon": horizon,
        "n_pairs": len(d),
        "AA_loss_rate": fmean(_loss_indicator(r, horizon) for r in aa),
        "RR_loss_rate": fmean(_loss_indicator(r, horizon) for r in rr),
        "RR_minus_AA_risk_difference": effect,
        "paired_ci95": ci,
    }


def _did_summary(records: list[dict[str, Any]], intervention: str, horizon: int) -> dict[str, Any]:
    baseline = _paired_d(records, "baseline_indirect", horizon)
    deletion = _paired_d(records, intervention, horizon)
    if baseline.keys() != deletion.keys():
        raise RuntimeError("paired keys differ across interventions")
    attenuation_values = [baseline[key] - deletion[key] for key in baseline]
    attenuation, ci = _mean_ci(attenuation_values)
    if ci[0] > 0:
        decision = "supports_matching_pathway"
    elif ci[1] < 0:
        decision = "countervailing_or_compensatory_pathway"
    else:
        decision = "unresolved"
    return {
        "intervention": intervention,
        "horizon": horizon,
        "n_paired_keys": len(attenuation_values),
        "baseline_minus_deletion_difference_in_risk_differences": attenuation,
        "paired_ci95": ci,
        "decision": decision,
    }


def _metric_difference(records: list[dict[str, Any]], intervention: str, horizon: int, metric: str) -> dict[str, Any]:
    by = {
        (r["condition"], int(r["master_seed"]), int(r["replicate"])): r
        for r in records
        if r["intervention"] == intervention
    }
    keys = sorted((m, rep) for c, m, rep in by if c == "AA")
    # AA - RR, so positive high-trait/refuge values indicate AA retention.
    values = [
        float(by[("AA", *key)]["states"][str(horizon)][metric])
        - float(by[("RR", *key)]["states"][str(horizon)][metric])
        for key in keys
    ]
    mean, ci = _mean_ci(values)
    return {"AA_minus_RR": mean, "paired_ci95": ci}


def summarise(protocol: dict[str, Any], records: list[dict[str, Any]]) -> dict[str, Any]:
    interventions = tuple(protocol["interventions"])
    primary_horizons = tuple(int(x) for x in protocol["primary_endpoint"]["primary_horizons"])
    all_horizons = tuple(int(x) for x in protocol["forcing"]["report_horizons"])
    risk = {
        intervention: {str(h): _risk_pair_summary(records, intervention, h) for h in primary_horizons}
        for intervention in interventions
    }
    did = {
        intervention: {str(h): _did_summary(records, intervention, h) for h in primary_horizons}
        for intervention in interventions
        if intervention != "baseline_indirect"
    }
    metrics = (
        "mean_high_trait_mass",
        "max_high_trait_mass",
        "realised_refugia_count",
        "mean_q",
        "max_q",
        "mean_population",
        "population_variance",
        "mean_allele_frequency",
        "allele_frequency_variance",
    )
    mediators = {
        intervention: {
            str(h): {metric: _metric_difference(records, intervention, h, metric) for metric in metrics}
            for h in all_horizons
        }
        for intervention in interventions
    }
    return {
        "schema_version": 1,
        "experiment_id": protocol["experiment_id"],
        "status": "completed_from_locked_protocol",
        "risk_pairs": risk,
        "edge_deletion_difference_in_differences": did,
        "mediator_differences_AA_minus_RR": mediators,
        "claim_boundary": protocol["claim_boundary"],
    }


def run(protocol_path: str | Path = PROTOCOL_PATH) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    protocol = load_protocol(protocol_path)
    records = simulate(protocol)
    return summarise(protocol, records), records


def write(summary_path: str | Path, records_path: str | Path, protocol_path: str | Path = PROTOCOL_PATH) -> None:
    summary, records = run(protocol_path)
    summary_path, records_path = Path(summary_path), Path(records_path)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    records_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    records_path.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
