"""Prospectively locked propagation audit for the historical Phase-V alignment contrast.

This module replays the exact historical aligned/anti-aligned Phase-V pairs and
reads already-produced simulator snapshots at a fixed set of horizons.  It does
not alter the biological dynamics and does not evaluate warning thresholds.
"""
from __future__ import annotations

import json
from math import comb, isfinite
from pathlib import Path
from typing import Any, Iterable
import warnings

from .cross_layer_alignment_phase_v import (
    PHASE_V_AREA_REFERENCE,
    PHASE_V_CONDITIONS,
    PHASE_V_DENSITY_CAPACITY,
    PHASE_V_GENERATIONS,
    PHASE_V_INTERACTION_FEEDBACK,
    PHASE_V_MASTER_SEEDS,
    PHASE_V_PATCH_AREAS,
    PHASE_V_POPULATION,
    PHASE_V_Q_FEEDBACK,
    PHASE_V_Q_VALUES,
    PHASE_V_REPLICATES_PER_SEED,
    PHASE_V_TRAIT_GRID_SIZE,
    barrier_schedule,
    condition_bundle_values,
    one_step_state_sufficiency_certificate,
    signatures_match,
    trait_abundance_rows,
)

HISTORICAL_PHASE_V_COMMIT = "260a03220bf09d5f4a4d8cb55ec21062bf120c55"
UPSTREAM_SCIENTIFIC_COMMIT = "dd8ee379d0d3518194c767d16402042525bc00dc"
PROPAGATION_PREREGISTRATION_COMMIT = "8c4745e411fe2107b490dc4f59b2acc966928196"
PROPAGATION_AMENDMENT_001_COMMIT = "9f7e1d3bab2d3ca88509208c0f46e4a2021e186c"
PROPAGATION_HORIZONS = (1, 2, 5, 10, 20, 40, 60)
PROPAGATION_BOOTSTRAP_DRAWS = 10_000
PROPAGATION_BOOTSTRAP_SEED = 20260904
CERTIFICATE_TOLERANCE = 1e-12
LOCKED_SUMMARY_DEFAULT = Path("artifacts/cross_layer_alignment/phase_v_locked_summary.json")

_PATCH_DISTANCE_KEYS = (
    "interaction_mean_abs",
    "population_mean_abs",
    "effective_size_mean_abs",
    "high_allele_frequency_mean_abs",
    "high_trait_mass_mean_abs",
)
_STATE_DISTANCE_KEYS = (
    "interaction_max_abs",
    *_PATCH_DISTANCE_KEYS,
    "h_alpha_abs",
    "h_gamma_abs",
    "fst_abs",
)


def _numpy():
    try:
        import numpy as np
    except ImportError as exc:  # pragma: no cover - exercised by workflow dependency gate
        raise RuntimeError(
            "cross-layer propagation analysis requires the optional 'analysis' dependency (numpy)"
        ) from exc
    return np


def trajectory_seed(master_seed: int, replicate: int) -> int:
    """Historical Phase-V trajectory-seed map; must not change in the replay."""
    return (master_seed * 1_000_003 + replicate * 101 + 17) % (2**31 - 1)


def _parameters(condition: str, seed: int):
    from causal_model.multipatch_criticality_dynamics import DynamicsParameters

    alpha, beta_trait, gamma = PHASE_V_Q_FEEDBACK
    bundle = condition_bundle_values(condition)
    return DynamicsParameters(
        patch_areas=PHASE_V_PATCH_AREAS,
        generations=PHASE_V_GENERATIONS,
        initial_population=PHASE_V_POPULATION,
        initial_interaction=PHASE_V_Q_VALUES,
        initial_high_allele_frequency=bundle,
        initial_trait_abundance=trait_abundance_rows(condition),
        density_capacity=PHASE_V_DENSITY_CAPACITY,
        area_reference=PHASE_V_AREA_REFERENCE,
        interaction_feedback=PHASE_V_INTERACTION_FEEDBACK,
        interaction_barrier=0.50,
        trait_grid_size=PHASE_V_TRAIT_GRID_SIZE,
        trait_occupancy_mode="finite_trait_bin_recruitment",
        genotype_trait_recruitment="two_kernel_recruitment",
        inheritance_weight=0.5,
        q_feedback_alpha=alpha,
        q_feedback_beta_trait=beta_trait,
        q_feedback_gamma_allele=gamma,
        migration_rate=0.0,
        random_seed=seed,
    )


def _mean_abs(left: Iterable[float], right: Iterable[float]) -> float:
    pairs = [(float(a), float(b)) for a, b in zip(left, right)]
    if not pairs:
        raise ValueError("patchwise distance requires at least one coordinate")
    return sum(abs(a - b) for a, b in pairs) / len(pairs)


def _max_abs(left: Iterable[float], right: Iterable[float]) -> float:
    values = [abs(float(a) - float(b)) for a, b in zip(left, right)]
    if not values:
        raise ValueError("patchwise distance requires at least one coordinate")
    return max(values)


def snapshot_distances(aligned: Any, anti_aligned: Any) -> dict[str, float | None]:
    """Return the preregistered paired state distances for one generation."""
    if int(aligned.generation) != int(anti_aligned.generation):
        raise ValueError("paired snapshots must refer to the same generation")

    aligned_high_mass = tuple(item.high_trait_mass for item in aligned.trait_occupancy)
    anti_high_mass = tuple(item.high_trait_mass for item in anti_aligned.trait_occupancy)
    fst_abs: float | None
    if (
        aligned.fst is None
        or anti_aligned.fst is None
        or not isfinite(float(aligned.fst))
        or not isfinite(float(anti_aligned.fst))
    ):
        fst_abs = None
    else:
        fst_abs = abs(float(aligned.fst) - float(anti_aligned.fst))

    return {
        "interaction_max_abs": _max_abs(aligned.interaction, anti_aligned.interaction),
        "interaction_mean_abs": _mean_abs(aligned.interaction, anti_aligned.interaction),
        "population_mean_abs": _mean_abs(aligned.population, anti_aligned.population),
        "effective_size_mean_abs": _mean_abs(aligned.effective_size, anti_aligned.effective_size),
        "high_allele_frequency_mean_abs": _mean_abs(
            aligned.high_allele_frequency, anti_aligned.high_allele_frequency
        ),
        "high_trait_mass_mean_abs": _mean_abs(aligned_high_mass, anti_high_mass),
        "h_alpha_abs": abs(float(aligned.h_alpha) - float(anti_aligned.h_alpha)),
        "h_gamma_abs": abs(float(aligned.h_gamma) - float(anti_aligned.h_gamma)),
        "fst_abs": fst_abs,
    }


def _simulate_condition(condition: str, master_seed: int, replicate: int):
    from causal_model.multipatch_criticality_dynamics import tau_trait_realised
    from causal_model.symmetric_allele_mutation_closure import simulate_with_symmetric_allele_mutation

    seed = trajectory_seed(master_seed, replicate)
    result = simulate_with_symmetric_allele_mutation(
        _parameters(condition, seed),
        mutation_rate=0.0,
        interaction_barrier_schedule=barrier_schedule(),
    )
    if len(result.snapshots) != PHASE_V_GENERATIONS + 1:
        raise RuntimeError("Phase-V replay did not return baseline plus 60 generation snapshots")
    for expected_generation, snapshot in enumerate(result.snapshots):
        if int(snapshot.generation) != expected_generation:
            raise RuntimeError("Phase-V snapshot generation/index contract changed")
    baseline_present = all(item.realised_high_trait_occupied for item in result.snapshots[0].trait_occupancy)
    if not baseline_present:
        raise RuntimeError("Phase-V baseline must retain realised high trait in every patch")
    raw_loss = tau_trait_realised(result)
    loss_time = None if raw_loss in {None, 0} else int(raw_loss)
    return result, loss_time


def run_pair(master_seed: int, replicate: int) -> dict[str, Any]:
    seed = trajectory_seed(master_seed, replicate)
    aligned, aligned_loss_time = _simulate_condition("aligned", master_seed, replicate)
    anti, anti_loss_time = _simulate_condition("anti_aligned", master_seed, replicate)

    horizons: dict[str, Any] = {}
    for horizon in PROPAGATION_HORIZONS:
        distances = snapshot_distances(aligned.snapshots[horizon], anti.snapshots[horizon])
        horizons[str(horizon)] = {
            "distances": distances,
            "aligned_cumulative_loss": aligned_loss_time is not None and aligned_loss_time <= horizon,
            "anti_aligned_cumulative_loss": anti_loss_time is not None and anti_loss_time <= horizon,
        }

    return {
        "master_seed": int(master_seed),
        "replicate": int(replicate),
        "trajectory_seed": int(seed),
        "aligned_trait_loss_time": aligned_loss_time,
        "anti_aligned_trait_loss_time": anti_loss_time,
        "horizons": horizons,
    }


def _two_sided_binomial_p(a: int, b: int) -> float:
    n = a + b
    if n == 0:
        return 1.0
    k = min(a, b)
    tail = sum(comb(n, i) for i in range(k + 1)) / (2**n)
    return min(1.0, 2.0 * tail)


def loss_table(pair_records: list[dict[str, Any]], horizon: int) -> dict[str, Any]:
    aligned_only = 0
    anti_only = 0
    both_loss = 0
    both_no = 0
    for row in pair_records:
        item = row["horizons"][str(horizon)]
        a = bool(item["aligned_cumulative_loss"])
        b = bool(item["anti_aligned_cumulative_loss"])
        if a and b:
            both_loss += 1
        elif a:
            aligned_only += 1
        elif b:
            anti_only += 1
        else:
            both_no += 1
    n = len(pair_records)
    aligned_count = aligned_only + both_loss
    anti_count = anti_only + both_loss
    return {
        "horizon": int(horizon),
        "pairs": n,
        "aligned_loss_count": aligned_count,
        "anti_aligned_loss_count": anti_count,
        "aligned_loss_rate": aligned_count / n,
        "anti_aligned_loss_rate": anti_count / n,
        "paired_risk_difference_aligned_minus_anti": (aligned_count - anti_count) / n,
        "both_no_loss": both_no,
        "aligned_only_loss": aligned_only,
        "anti_aligned_only_loss": anti_only,
        "both_loss": both_loss,
        "identical_status_fraction": (both_no + both_loss) / n,
        "discordant_status_fraction": (aligned_only + anti_only) / n,
        "mcnemar_exact_p_descriptive": _two_sided_binomial_p(aligned_only, anti_only),
    }


def _certificate_matches_locked(current: dict[str, Any], locked: dict[str, Any]) -> bool:
    if bool(current["coarse_marginal_signatures_identical"]) != bool(
        locked["coarse_marginal_signatures_identical"]
    ):
        return False
    if bool(current["coarse_marginals_are_transition_sufficient"]) != bool(
        locked["coarse_marginals_are_transition_sufficient"]
    ):
        return False
    numeric_scalars = (
        "aligned_cross_layer_covariance",
        "anti_aligned_cross_layer_covariance",
        "maximum_patchwise_generation1_difference",
    )
    for key in numeric_scalars:
        if abs(float(current[key]) - float(locked[key])) > CERTIFICATE_TOLERANCE:
            return False
    vector_keys = (
        "aligned_support_signal",
        "anti_aligned_support_signal",
        "aligned_generation1_interaction",
        "anti_aligned_generation1_interaction",
    )
    for key in vector_keys:
        left = tuple(float(value) for value in current[key])
        right = tuple(float(value) for value in locked[key])
        if len(left) != len(right):
            return False
        if any(abs(a - b) > CERTIFICATE_TOLERANCE for a, b in zip(left, right)):
            return False
    return True


def reproduction_gate(
    pair_records: list[dict[str, Any]],
    locked_summary: dict[str, Any],
    certificate: dict[str, Any],
) -> dict[str, Any]:
    keys = [(int(row["master_seed"]), int(row["replicate"])) for row in pair_records]
    expected_keys = [
        (seed, replicate)
        for seed in PHASE_V_MASTER_SEEDS
        for replicate in range(PHASE_V_REPLICATES_PER_SEED)
    ]
    terminal = loss_table(pair_records, 60)
    locked_paired = locked_summary["paired"]
    checks = {
        "baseline_signatures_match": bool(signatures_match()),
        "certificate_matches_locked": _certificate_matches_locked(
            certificate, locked_summary["opening_certificate"]
        ),
        "exact_500_pair_keys": sorted(keys) == sorted(expected_keys) and len(set(keys)) == 500,
        "aligned_terminal_loss_count_matches": terminal["aligned_loss_count"]
        == int(locked_summary["aligned"]["trait_loss_count"]),
        "anti_terminal_loss_count_matches": terminal["anti_aligned_loss_count"]
        == int(locked_summary["anti_aligned"]["trait_loss_count"]),
        "aligned_only_terminal_matches": terminal["aligned_only_loss"]
        == int(locked_paired["aligned_loss_anti_no_loss"]),
        "anti_only_terminal_matches": terminal["anti_aligned_only_loss"]
        == int(locked_paired["aligned_no_loss_anti_loss"]),
        "both_loss_terminal_matches": terminal["both_loss"] == int(locked_paired["same_loss"]),
        "both_no_terminal_matches": terminal["both_no_loss"] == int(locked_paired["same_no_loss"]),
    }
    return {
        "passed": all(checks.values()),
        "decision": "reproduction_gate_passed" if all(checks.values()) else "reproduction_gate_failed",
        "checks": checks,
        "terminal_replay": terminal,
    }


def _metric_matrix(pair_records: list[dict[str, Any]], metric: str):
    np = _numpy()
    values = np.full((len(pair_records), len(PROPAGATION_HORIZONS)), np.nan, dtype=float)
    for row_index, row in enumerate(pair_records):
        for horizon_index, horizon in enumerate(PROPAGATION_HORIZONS):
            value = row["horizons"][str(horizon)]["distances"][metric]
            if value is not None and isfinite(float(value)):
                values[row_index, horizon_index] = float(value)
    return values


def _bootstrap_indices(n_pairs: int, draws: int, seed: int):
    np = _numpy()
    rng = np.random.default_rng(seed)
    return rng.integers(0, n_pairs, size=(draws, n_pairs), dtype=np.int32)


def bootstrap_median_curve(values, indices, *, batch_size: int = 250) -> dict[str, Any]:
    np = _numpy()
    observed = np.nanmedian(values, axis=0)
    boot = np.full((indices.shape[0], values.shape[1]), np.nan, dtype=float)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        for start in range(0, indices.shape[0], batch_size):
            stop = min(start + batch_size, indices.shape[0])
            selected = values[indices[start:stop]]
            boot[start:stop] = np.nanmedian(selected, axis=1)
    lower = np.nanquantile(boot, 0.025, axis=0)
    upper = np.nanquantile(boot, 0.975, axis=0)
    finite_counts = np.sum(np.isfinite(values), axis=0)
    valid_bootstrap_draws = np.sum(np.isfinite(boot), axis=0)
    return {
        "observed_median": observed,
        "lower_95": lower,
        "upper_95": upper,
        "finite_pair_count": finite_counts,
        "valid_bootstrap_draws": valid_bootstrap_draws,
    }


def _loss_difference_matrix(pair_records: list[dict[str, Any]]):
    np = _numpy()
    values = np.zeros((len(pair_records), len(PROPAGATION_HORIZONS)), dtype=float)
    for row_index, row in enumerate(pair_records):
        for horizon_index, horizon in enumerate(PROPAGATION_HORIZONS):
            item = row["horizons"][str(horizon)]
            values[row_index, horizon_index] = float(bool(item["aligned_cumulative_loss"])) - float(
                bool(item["anti_aligned_cumulative_loss"])
            )
    return values


def simultaneous_risk_difference_band(loss_differences, indices, *, batch_size: int = 500) -> dict[str, Any]:
    np = _numpy()
    observed = np.mean(loss_differences, axis=0)
    max_deviations = np.empty(indices.shape[0], dtype=float)
    for start in range(0, indices.shape[0], batch_size):
        stop = min(start + batch_size, indices.shape[0])
        boot_mean = np.mean(loss_differences[indices[start:stop]], axis=1)
        max_deviations[start:stop] = np.max(np.abs(boot_mean - observed), axis=1)
    half_width = float(np.quantile(max_deviations, 0.95))
    lower = observed - half_width
    upper = observed + half_width
    excluded = np.logical_or(lower > 0.0, upper < 0.0)
    return {
        "observed": observed,
        "simultaneous_half_width_95": half_width,
        "lower_95_simultaneous": lower,
        "upper_95_simultaneous": upper,
        "excludes_zero": excluded,
        "classification": (
            "horizon_family_loss_incidence_separation_detected"
            if bool(np.any(excluded))
            else "no_detected_horizon_family_loss_incidence_separation"
        ),
    }


def classify_interaction_memory(medians: dict[int, float]) -> dict[str, Any]:
    first = float(medians[1])
    if not isfinite(first) or first <= 1e-15:
        return {
            "classification": "representation_memory_not_identifiable",
            "half_retention_horizon": None,
            "half_level": None,
        }
    half_level = 0.5 * first
    below = {horizon: float(medians[horizon]) <= half_level for horizon in PROPAGATION_HORIZONS[1:]}
    any_below = any(below.values())
    if any_below:
        first_below = next(horizon for horizon in PROPAGATION_HORIZONS[1:] if below[horizon])
        later = [h for h in PROPAGATION_HORIZONS if h >= first_below]
        retained = all(float(medians[h]) <= half_level for h in later)
        if not retained:
            return {
                "classification": "nonmonotone_representation_memory",
                "half_retention_horizon": None,
                "first_below_half_horizon": first_below,
                "half_level": half_level,
            }
        if first_below <= 5:
            classification = "short_representation_memory"
        else:
            classification = "attenuating_representation_memory"
        return {
            "classification": classification,
            "half_retention_horizon": first_below,
            "half_level": half_level,
        }
    return {
        "classification": "persistent_representation_memory",
        "half_retention_horizon": None,
        "half_level": half_level,
    }


def _json_number(value: Any) -> float | int | bool | None:
    if value is None:
        return None
    if hasattr(value, "item"):
        value = value.item()
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return int(value)
    if isinstance(value, float):
        return None if not isfinite(value) else float(value)
    return value


def _curve_payload(curve: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for index, horizon in enumerate(PROPAGATION_HORIZONS):
        rows.append(
            {
                "horizon": horizon,
                "median": _json_number(curve["observed_median"][index]),
                "lower_95": _json_number(curve["lower_95"][index]),
                "upper_95": _json_number(curve["upper_95"][index]),
                "finite_pair_count": int(curve["finite_pair_count"][index]),
                "valid_bootstrap_draws": int(curve["valid_bootstrap_draws"][index]),
            }
        )
    return rows


def run_propagation_audit(
    *,
    locked_summary_path: str | Path = LOCKED_SUMMARY_DEFAULT,
    bootstrap_draws: int = PROPAGATION_BOOTSTRAP_DRAWS,
    bootstrap_seed: int = PROPAGATION_BOOTSTRAP_SEED,
) -> dict[str, Any]:
    if bootstrap_draws != PROPAGATION_BOOTSTRAP_DRAWS or bootstrap_seed != PROPAGATION_BOOTSTRAP_SEED:
        raise ValueError("scientific propagation run must use the preregistered bootstrap count and seed")

    locked_summary = json.loads(Path(locked_summary_path).read_text(encoding="utf-8"))
    certificate = one_step_state_sufficiency_certificate()
    pair_records = [
        run_pair(seed, replicate)
        for seed in PHASE_V_MASTER_SEEDS
        for replicate in range(PHASE_V_REPLICATES_PER_SEED)
    ]
    gate = reproduction_gate(pair_records, locked_summary, certificate)
    base = {
        "protocol": "post-review cross-layer alignment propagation audit",
        "historical_phase_v_commit": HISTORICAL_PHASE_V_COMMIT,
        "upstream_scientific_commit": UPSTREAM_SCIENTIFIC_COMMIT,
        "preregistration_commit": PROPAGATION_PREREGISTRATION_COMMIT,
        "amendment_001_commit": PROPAGATION_AMENDMENT_001_COMMIT,
        "warning_blind": True,
        "fixed_horizons": list(PROPAGATION_HORIZONS),
        "bootstrap_draws": bootstrap_draws,
        "bootstrap_seed": bootstrap_seed,
        "opening_certificate": certificate,
        "reproduction_gate": gate,
    }
    if not gate["passed"]:
        return {
            **base,
            "decision": "reproduction_gate_failed",
            "interpretation": "Intermediate propagation outcomes are not interpreted because the historical Phase-V replay failed its preregistered reproduction gate.",
        }

    indices = _bootstrap_indices(len(pair_records), bootstrap_draws, bootstrap_seed)
    state_curves: dict[str, Any] = {}
    primary_medians: dict[int, float] = {}
    for metric in _STATE_DISTANCE_KEYS:
        values = _metric_matrix(pair_records, metric)
        curve = bootstrap_median_curve(values, indices)
        payload = _curve_payload(curve)
        state_curves[metric] = payload
        if metric == "interaction_max_abs":
            primary_medians = {
                int(item["horizon"]): float(item["median"])
                for item in payload
                if item["median"] is not None
            }

    memory = classify_interaction_memory(primary_medians)
    loss_tables = [loss_table(pair_records, horizon) for horizon in PROPAGATION_HORIZONS]
    loss_differences = _loss_difference_matrix(pair_records)
    band = simultaneous_risk_difference_band(loss_differences, indices)
    for index, table in enumerate(loss_tables):
        table["risk_difference_lower_95_simultaneous"] = _json_number(
            band["lower_95_simultaneous"][index]
        )
        table["risk_difference_upper_95_simultaneous"] = _json_number(
            band["upper_95_simultaneous"][index]
        )
        table["risk_difference_simultaneous_band_excludes_zero"] = bool(
            band["excludes_zero"][index]
        )

    decision = {
        "interaction_representation_memory": memory["classification"],
        "loss_horizon_family": band["classification"],
    }
    return {
        **base,
        "decision": decision,
        "interaction_memory": memory,
        "state_distance_curves": state_curves,
        "loss_horizon_family": {
            "classification": band["classification"],
            "simultaneous_half_width_95": band["simultaneous_half_width_95"],
            "horizons": loss_tables,
        },
        "pair_records": pair_records,
        "claim_ceiling": (
            "This replay estimates how the locked cross-layer alignment contrast propagates across preregistered forecast horizons. "
            "It does not explain the separate warning-validity failure, does not test whether alignment rescues a warning statistic, and is not an independent replication of Phase V."
        ),
    }


def write_propagation_audit(
    output: str | Path,
    *,
    locked_summary_path: str | Path = LOCKED_SUMMARY_DEFAULT,
) -> Path:
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(
            run_propagation_audit(locked_summary_path=locked_summary_path),
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return destination
