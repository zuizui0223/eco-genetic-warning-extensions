"""Per-seed runner and aggregator for pollen-only gene-flow Phase S."""
from __future__ import annotations

import importlib
import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterable

from .migration_condition_phase_e import (
    PHASE_E_AREA_REFERENCE,
    PHASE_E_BARRIER_INCREASE,
    PHASE_E_HOLD_GENERATIONS,
    PHASE_E_INTERACTION_KAPPA,
    PHASE_E_KAPPA_MU,
    PHASE_E_MASTER_SEEDS,
    PHASE_E_P_STAR,
    PHASE_E_RAMP_GENERATIONS,
)
from .mutation_coordinates import MutationCoordinates
from .process_resolved_movement_phase_r_runner import (
    _exact_mcnemar_two_sided,
    _outcome_row,
    _pooled_rate,
    _regime,
    pearson_equal_rate_test,
)
from .process_resolved_pollen import simulate_with_process_resolved_pollen
from .process_resolved_pollen_phase_s import (
    PHASE_S_CONDITIONS,
    PHASE_S_LEGACY_MIGRATION_RATE,
    PHASE_S_MIN_BASELINE_ELIGIBLE_PER_SEED,
    PHASE_S_PHASE_M_BLOCKS,
    PHASE_S_POLLEN_IMMIGRATION_RATE,
    PHASE_S_PREFIX_COUNTS,
    PHASE_S_REPLICATES_PER_SEED,
    phase_s_manifest,
)
from .protocol002_source_grid import SOURCE_HOLD_GENERATIONS, SOURCE_NESTED_BARRIER_GRIDS, SOURCE_STAGE_GENERATIONS
from .protocol002_stage1_projection_pilot import UPSTREAM_CHAIN_RUNTIME_MODULE
from .protocol002_stage2_smoke import UPSTREAM_CALIBRATION_MODULE, UPSTREAM_DYNAMICS_MODULE
from .protocol002_upstream_h1_asym_smoke import (
    UPSTREAM_EXPERIMENT_MODULE,
    UPSTREAM_H1_MODULE,
    UPSTREAM_MUTATION_MODULE,
    _upstream_import_path,
    patched_protocol002_mutation_runner,
)


def run_phase_s_seed(upstream_checkout: str | Path, master_seed: int) -> dict[str, Any]:
    if master_seed not in PHASE_E_MASTER_SEEDS:
        raise ValueError("master seed is not one of the locked Phase-E seeds")
    checkout = Path(upstream_checkout)
    if not checkout.exists():
        raise FileNotFoundError(f"upstream checkout does not exist: {checkout}")

    coordinate = MutationCoordinates(kappa_mu=PHASE_E_KAPPA_MU, p_star=PHASE_E_P_STAR)
    driver_rate = coordinate.kappa_mu / 2.0
    total_generations = PHASE_E_RAMP_GENERATIONS + PHASE_E_HOLD_GENERATIONS
    attempts: list[dict[str, Any]] = []

    with _upstream_import_path(checkout):
        audit = importlib.import_module(UPSTREAM_H1_MODULE)
        experiments = importlib.import_module(UPSTREAM_EXPERIMENT_MODULE)
        mutation = importlib.import_module(UPSTREAM_MUTATION_MODULE)
        runtime = importlib.import_module(UPSTREAM_CHAIN_RUNTIME_MODULE)
        calibration = importlib.import_module(UPSTREAM_CALIBRATION_MODULE)
        dynamics = importlib.import_module(UPSTREAM_DYNAMICS_MODULE)
        chain = runtime.chain

        schedule = calibration.RampHoldSchedule(
            PHASE_E_RAMP_GENERATIONS,
            PHASE_E_HOLD_GENERATIONS,
            PHASE_E_BARRIER_INCREASE,
        )
        spec = replace(
            experiments.standard_profile(),
            experiment_id="process_resolved_pollen_phase_s",
            generations=1,
            replicates=PHASE_S_REPLICATES_PER_SEED,
            master_seed=master_seed,
            area_reference_values=(PHASE_E_AREA_REFERENCE,),
            interaction_feedback_values=(PHASE_E_INTERACTION_KAPPA,),
            interaction_barrier_values=(0.5,),
        )

        with patched_protocol002_mutation_runner(mutation, coordinate):
            cells = audit.run_finite_h1_boundary_resolution_audit(
                spec,
                endpoint_padding_fraction=0.5,
                stage_generations=SOURCE_STAGE_GENERATIONS,
                nested_barrier_points=SOURCE_NESTED_BARRIER_GRIDS,
                interaction_separation_threshold=0.05,
                maximum_normalized_bracket_width=0.03,
            )
            if len(cells) != 1:
                raise RuntimeError("Phase S requires exactly one H1 cell per master seed")
            cell = cells[0]
            isolated = experiments.scenario_equal_isolated(spec)

            for record in cell.replicates:
                base = {
                    "master_seed": master_seed,
                    "replicate": record.replicate_index,
                    "calibration_seed": record.seed,
                    "source_support": record.resolution_stable_h1_loop_mechanism_supported,
                }
                prepared = chain._prepare_mutation_high_state(
                    driver_rate,
                    spec,
                    cell,
                    record,
                    endpoint_padding_fraction=0.5,
                    stage_generations=SOURCE_STAGE_GENERATIONS,
                    hold_generations=SOURCE_HOLD_GENERATIONS,
                    interaction_separation_threshold=0.05,
                )
                if prepared is None:
                    for condition in PHASE_S_CONDITIONS:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "source_prepared": False,
                            "projection_supported": None,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                    continue

                source, anchor_barrier = prepared
                interval = cell.canonical_bistable_barrier_interval
                if interval is None or interval[1] <= interval[0]:
                    raise RuntimeError("Phase-S source requires a positive canonical interval")
                barriers = calibration.ramp_and_hold_barrier_schedule(
                    anchor_barrier=anchor_barrier,
                    canonical_interval_width=interval[1] - interval[0],
                    schedule=schedule,
                )

                scenarios = {
                    "no_connectivity": experiments.LandscapeScenario(
                        scenario_id="phase_s_no_connectivity",
                        patch_areas=isolated.patch_areas,
                        migration_rate=0.0,
                    ),
                    "allele_only_m010": experiments.LandscapeScenario(
                        scenario_id="phase_s_allele_only_m010",
                        patch_areas=isolated.patch_areas,
                        migration_rate=PHASE_S_LEGACY_MIGRATION_RATE,
                    ),
                }
                projected_by_condition: dict[str, Any] = {}
                projection_ok = True
                for condition, scenario in scenarios.items():
                    template = chain.parameters_for_cell(
                        spec,
                        scenario,
                        replace(cell.parameters, interaction_barrier=anchor_barrier),
                        seed=record.seed,
                    )
                    projected, invariants = chain.project_full_state(source, template)
                    projection_ok = projection_ok and bool(invariants.projection_supported)
                    projected_by_condition[condition] = projected

                if not projection_ok:
                    for condition in PHASE_S_CONDITIONS:
                        attempts.append({
                            **base,
                            "condition": condition,
                            "source_prepared": True,
                            "projection_supported": False,
                            "baseline_realised_high_trait_present": None,
                            "eligible_for_trait_loss_denominator": False,
                            "trait_loss_time_post_baseline": None,
                            "trait_loss_observed_post_baseline": None,
                        })
                    continue

                no_parameters = replace(
                    projected_by_condition["no_connectivity"],
                    generations=total_generations,
                    random_seed=record.seed,
                )
                legacy_parameters = replace(
                    projected_by_condition["allele_only_m010"],
                    generations=total_generations,
                    random_seed=record.seed,
                )
                no_result = mutation.simulate_with_symmetric_allele_mutation(
                    no_parameters,
                    mutation_rate=driver_rate,
                    interaction_barrier_schedule=barriers,
                )
                legacy_result = mutation.simulate_with_symmetric_allele_mutation(
                    legacy_parameters,
                    mutation_rate=driver_rate,
                    interaction_barrier_schedule=barriers,
                )
                pollen = simulate_with_process_resolved_pollen(
                    dynamics,
                    mutation,
                    no_parameters,
                    coordinate,
                    pollen_immigration_rate=PHASE_S_POLLEN_IMMIGRATION_RATE,
                    interaction_barrier_schedule=barriers,
                    pollen_seed=record.seed,
                )

                attempts.append(_outcome_row(base, "no_connectivity", no_result, dynamics))
                attempts.append(_outcome_row(base, "allele_only_m010", legacy_result, dynamics))
                attempts.append(_outcome_row(
                    base,
                    "pollen_only_g020",
                    pollen.simulation,
                    dynamics,
                    total_immigrant_pollen=pollen.diagnostics.total_immigrant_pollen,
                    realised_pollen_immigration_fraction=pollen.diagnostics.realised_pollen_immigration_fraction,
                ))

    prefix_ok = True
    baseline_pairing_ok = True
    condition_summaries = []
    by_key = {(row["replicate"], row["condition"]): row for row in attempts}
    for replicate in range(PHASE_S_REPLICATES_PER_SEED):
        no = by_key[(replicate, "no_connectivity")]
        pollen = by_key[(replicate, "pollen_only_g020")]
        if no["eligible_for_trait_loss_denominator"] != pollen["eligible_for_trait_loss_denominator"]:
            baseline_pairing_ok = False

    for condition in PHASE_S_CONDITIONS:
        rows = [row for row in attempts if row["condition"] == condition]
        eligible = [row for row in rows if row["eligible_for_trait_loss_denominator"]]
        losses = [row for row in eligible if row["trait_loss_observed_post_baseline"] is True]
        summary = {
            "condition": condition,
            "attempted": len(rows),
            "baseline_eligible": len(eligible),
            "trait_loss": len(losses),
            "trait_loss_rate": None if not eligible else len(losses) / len(eligible),
            "precision_sufficient": len(eligible) >= PHASE_S_MIN_BASELINE_ELIGIBLE_PER_SEED,
        }
        if condition in PHASE_S_PREFIX_COUNTS[master_seed]:
            prefix = [row for row in rows if row["replicate"] < 20]
            pe = [row for row in prefix if row["eligible_for_trait_loss_denominator"]]
            pl = [row for row in pe if row["trait_loss_observed_post_baseline"] is True]
            expected_eligible, expected_losses = PHASE_S_PREFIX_COUNTS[master_seed][condition]
            match = len(pe) == expected_eligible and len(pl) == expected_losses
            prefix_ok = prefix_ok and match
            summary["prefix"] = {
                "observed_eligible": len(pe),
                "observed_losses": len(pl),
                "expected_eligible": expected_eligible,
                "expected_losses": expected_losses,
                "matches_historical": match,
            }
        if condition == "pollen_only_g020":
            pollen_rows = [row for row in rows if row.get("total_immigrant_pollen") is not None]
            summary["pollen"] = {
                "mean_total_immigrant_pollen": None if not pollen_rows else sum(row["total_immigrant_pollen"] for row in pollen_rows) / len(pollen_rows),
                "mean_realised_pollen_immigration_fraction": None if not pollen_rows else sum(row["realised_pollen_immigration_fraction"] for row in pollen_rows) / len(pollen_rows),
            }
        condition_summaries.append(summary)

    return {
        "stage": "process-resolved pollen validation Phase S",
        "master_seed": master_seed,
        "prefix_audit_passed": prefix_ok,
        "pollen_baseline_pairing_passed": baseline_pairing_ok,
        "condition_summaries": condition_summaries,
        "attempts": attempts,
    }


def _paired_counts(payloads: tuple[dict[str, Any], ...], reference: str, comparison: str) -> dict[str, Any]:
    rows = {
        (row["master_seed"], row["replicate"], row["condition"]): row
        for payload in payloads
        for row in payload["attempts"]
    }
    counts = {"comparable_pair_count": 0, "loss_to_no_loss": 0, "no_loss_to_loss": 0, "same_loss": 0, "same_no_loss": 0}
    for seed in PHASE_E_MASTER_SEEDS:
        for replicate in range(PHASE_S_REPLICATES_PER_SEED):
            ref = rows[(seed, replicate, reference)]
            alt = rows[(seed, replicate, comparison)]
            if not (ref["eligible_for_trait_loss_denominator"] and alt["eligible_for_trait_loss_denominator"]):
                continue
            counts["comparable_pair_count"] += 1
            ref_loss = ref["trait_loss_observed_post_baseline"] is True
            alt_loss = alt["trait_loss_observed_post_baseline"] is True
            if ref_loss and not alt_loss:
                counts["loss_to_no_loss"] += 1
            elif not ref_loss and alt_loss:
                counts["no_loss_to_loss"] += 1
            elif ref_loss:
                counts["same_loss"] += 1
            else:
                counts["same_no_loss"] += 1
    return {
        "reference": reference,
        "comparison": comparison,
        **counts,
        "exact_mcnemar_two_sided_p": _exact_mcnemar_two_sided(counts["loss_to_no_loss"], counts["no_loss_to_loss"]),
    }


def aggregate_phase_s(seed_payloads: Iterable[dict[str, Any]]) -> dict[str, Any]:
    payloads = tuple(seed_payloads)
    if sorted(payload["master_seed"] for payload in payloads) != sorted(PHASE_E_MASTER_SEEDS):
        raise RuntimeError("Phase S requires exactly the five locked Phase-E master seeds")

    prefix_ok = all(payload["prefix_audit_passed"] for payload in payloads)
    baseline_pairing_ok = all(payload["pollen_baseline_pairing_passed"] for payload in payloads)
    summaries = []
    regime_by_condition = {}
    blocks_by_condition: dict[str, tuple[tuple[int, int], ...]] = {}

    for condition in PHASE_S_CONDITIONS:
        blocks = []
        pollen_rows = []
        for payload in sorted(payloads, key=lambda item: item["master_seed"]):
            row = next(item for item in payload["condition_summaries"] if item["condition"] == condition)
            blocks.append((int(row["trait_loss"]), int(row["baseline_eligible"])))
            if "pollen" in row:
                pollen_rows.append(row["pollen"])
        block_tuple = tuple(blocks)
        blocks_by_condition[condition] = block_tuple
        sufficient = all(eligible >= PHASE_S_MIN_BASELINE_ELIGIBLE_PER_SEED for _, eligible in block_tuple)
        rates = tuple(losses / eligible for losses, eligible in block_tuple)
        regime = "insufficient_precision" if not sufficient else _regime(rates)
        statistic, df, p_value = pearson_equal_rate_test(block_tuple)
        summary = {
            "condition": condition,
            "blocks": [
                {"master_seed": seed, "losses": losses, "eligible": eligible, "rate": losses / eligible}
                for seed, (losses, eligible) in zip(PHASE_E_MASTER_SEEDS, block_tuple, strict=True)
            ],
            "pooled_loss_rate": _pooled_rate(block_tuple),
            "historical_screen_at_full_precision": regime,
            "pearson_equal_rate_statistic": statistic,
            "pearson_equal_rate_df": df,
            "pearson_equal_rate_p_value": p_value,
            "precision_sufficient": sufficient,
        }
        if pollen_rows:
            summary["pollen"] = {
                "mean_total_immigrant_pollen_across_seed_blocks": sum(row["mean_total_immigrant_pollen"] for row in pollen_rows) / len(pollen_rows),
                "mean_realised_pollen_immigration_fraction_across_seed_blocks": sum(row["mean_realised_pollen_immigration_fraction"] for row in pollen_rows) / len(pollen_rows),
            }
        summaries.append(summary)
        regime_by_condition[condition] = regime

    legacy_full_replay_ok = (
        blocks_by_condition["no_connectivity"] == PHASE_S_PHASE_M_BLOCKS["no_connectivity"]
        and blocks_by_condition["allele_only_m010"] == PHASE_S_PHASE_M_BLOCKS["allele_only_m010"]
    )
    opening_passed = prefix_ok and baseline_pairing_ok and legacy_full_replay_ok
    pollen_summary = next(row for row in summaries if row["condition"] == "pollen_only_g020")
    paired_vs_no = _paired_counts(payloads, "no_connectivity", "pollen_only_g020")
    paired_vs_legacy = _paired_counts(payloads, "allele_only_m010", "pollen_only_g020")

    if not opening_passed:
        decision = "opening_replay_failed"
    elif pollen_summary["pearson_equal_rate_p_value"] < 0.05:
        decision = "pollen_gene_flow_shows_between_block_heterogeneity"
    else:
        decision = "legacy_m010_heterogeneity_not_reproduced_by_pollen_gene_flow"

    return {
        "stage": "process-resolved pollen validation Phase S",
        "manifest": phase_s_manifest(),
        "opening": {
            "prefix_audit_passed": prefix_ok,
            "pollen_baseline_pairing_passed": baseline_pairing_ok,
            "legacy_full_phase_m_replay_passed": legacy_full_replay_ok,
            "opening_passed": opening_passed,
        },
        "decision": decision,
        "condition_summaries": summaries,
        "regime_by_condition": regime_by_condition,
        "paired_pollen_vs_no_connectivity": paired_vs_no,
        "paired_pollen_vs_allele_only_m010": paired_vs_legacy,
        "interpretation": {
            "pollen_marginal_effect_detected": paired_vs_no["exact_mcnemar_two_sided_p"] < 0.05,
            "pollen_differs_from_allele_only_m010": paired_vs_legacy["exact_mcnemar_two_sided_p"] < 0.05,
            "pollen_between_block_heterogeneity_detected": pollen_summary["pearson_equal_rate_p_value"] < 0.05,
        },
        "per_seed_payloads": list(payloads),
    }


def load_and_aggregate_phase_s(paths: Iterable[str | Path]) -> dict[str, Any]:
    return aggregate_phase_s([json.loads(Path(path).read_text(encoding="utf-8")) for path in paths])
