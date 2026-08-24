#!/usr/bin/env python3
"""Run the preregistered E2 Zurich ecological partial-state audit.

The script expects a checkout of BetterBlooms at the pinned source commit and an
extracted copy of EnviDat 10.16904/envidat.676.  It does not search predictors
or endpoints.  Function-specific pollinator guild sets are copied from the
source reproductive-success abundance scripts; the residual context is fixed
to PlantS + Urban_500 + PlantS:Urban_500 from the source habitat scripts.

Validation holds out whole gardens.  This is a predictive state audit, not a
reproduction of every nested random-effect estimate in the source article.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.special import gammaln

SOURCE_REPOSITORY = "mrejichacko/BetterBlooms"
SOURCE_COMMIT = "d6361f6874398e797322afe07a8fea85a3c7e927"
SOURCE_DATA_DOI = "10.16904/envidat.676"
SOURCE_EXCLUDED_GARDEN = 39
BOOTSTRAP_SEED = 20260824
BOOTSTRAP_REPLICATES = 10_000


@dataclass(frozen=True)
class Endpoint:
    name: str
    filename: str
    plant: str
    family: str
    interaction_counts: tuple[str, ...]
    response_success: str
    response_failure: str | None = None
    sainfoin_filter: bool = False


ENDPOINTS = (
    Endpoint(
        "daucus_seed_set",
        "daucus_carota_seed_set.csv",
        "Carrot",
        "poisson",
        (
            "A_Apis_Carrot",
            "A_socialBees_Carrot",
            "A_solitaryBees_Carrot",
            "A_otherAculeata_Carrot",
            "A_Syrphidae_Carrot",
            "A_Coleoptera_Carrot",
        ),
        "n_seeds",
    ),
    Endpoint(
        "raphanus_fruit_set",
        "raphanus_sativus_fruit_set.csv",
        "Radish",
        "binomial",
        (
            "A_Apis_Radish",
            "A_socialBees_Radish",
            "A_solitaryBees_Radish",
            "A_Syrphidae_Radish",
        ),
        "n_flowers_with_fruits",
        "n_flowers_without_fruits",
    ),
    Endpoint(
        "raphanus_seed_set",
        "raphanus_sativus_seed_set.csv",
        "Radish",
        "poisson",
        (
            "A_Apis_Radish",
            "A_socialBees_Radish",
            "A_solitaryBees_Radish",
            "A_Syrphidae_Radish",
        ),
        "n_seeds",
    ),
    Endpoint(
        "onobrychis_fruit_set",
        "onobrychis_viciifolia_fruit_set.csv",
        "Sainfoin",
        "binomial",
        (
            "A_Apis_Sainfoin",
            "A_Bombus_Sainfoin",
            "A_solitaryBees_Sainfoin",
        ),
        "n_flowers_with_fruits",
        "n_flowers_without_fruits",
        sainfoin_filter=True,
    ),
    Endpoint(
        "symphytum_fruit_set",
        "symphytum_officinale_fruit_set.csv",
        "Comfrey",
        "binomial",
        ("A_Bombus_Comfrey",),
        "n_flowers_with_seeds",
        "n_flowers_without_seeds",
    ),
    Endpoint(
        "symphytum_seed_set",
        "symphytum_officinale_seed_set.csv",
        "Comfrey",
        "binomial",
        ("A_Bombus_Comfrey",),
        "n_seeds",
        "n_unfertilized_ovules",
    ),
)


def _read_semicolon(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, sep=";")


def _require(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise KeyError(f"{label} missing required columns: {missing}")


def _find_pollination_dir(root: Path) -> Path:
    direct = root / "07_pollination_success"
    if direct.is_dir():
        return direct
    candidates = [path for path in root.rglob("07_pollination_success") if path.is_dir()]
    if len(candidates) != 1:
        raise RuntimeError(f"expected one 07_pollination_success directory, found {len(candidates)}")
    return candidates[0]


def build_predictors(source: Path) -> pd.DataFrame:
    floristic = _read_semicolon(source / "raw_data" / "plant_floristic_data.txt")
    landscape = _read_semicolon(source / "raw_data" / "explanatory_variables.txt")
    abundance = _read_semicolon(source / "cleaned_data" / "pollinator_abundance_aggregated_garden_phytometer.txt")
    effort = _read_semicolon(source / "cleaned_data" / "sampling_effort_gardens_plants_aggregated.txt")

    plant_s = "SR_all_insect_pollinated_May_August"
    _require(floristic, ["Id", plant_s], "plant floristic data")
    _require(landscape, ["Id", "Urban_500", "X_KOORDINATE", "Y_KOORDINATE"], "landscape data")
    _require(abundance, ["Id"] + sorted({c for endpoint in ENDPOINTS for c in endpoint.interaction_counts}), "abundance data")
    _require(
        effort,
        [
            "Id",
            "sampling_effort_min_carrot",
            "sampling_effort_min_radish",
            "sampling_effort_min_sainfoin",
            "sampling_effort_min_comfrey",
        ],
        "sampling effort data",
    )

    frame = floristic[["Id", plant_s]].rename(columns={plant_s: "PlantS"})
    frame = frame.merge(landscape[["Id", "Urban_500", "X_KOORDINATE", "Y_KOORDINATE"]], on="Id", how="inner")
    frame = frame.merge(abundance, on="Id", how="inner")
    frame = frame.merge(effort, on="Id", how="inner")
    frame["Id"] = frame["Id"].astype(int)

    for endpoint in ENDPOINTS:
        effort_column = f"sampling_effort_min_{endpoint.plant.lower()}"
        days = frame[effort_column].astype(float) / 60.0 / 9.0
        if (days <= 0).any():
            raise ValueError(f"non-positive sampling effort for {endpoint.plant}")
        for count_column in endpoint.interaction_counts:
            rate_column = f"{count_column}__daily"
            if rate_column not in frame:
                frame[rate_column] = frame[count_column].astype(float) / days
    return frame


def _response_frame(endpoint: Endpoint, pollination_dir: Path, predictors: pd.DataFrame) -> pd.DataFrame:
    path = pollination_dir / endpoint.filename
    if not path.exists():
        raise FileNotFoundError(path)
    response = pd.read_csv(path)
    required = ["Id", endpoint.response_success]
    if endpoint.response_failure is not None:
        required.append(endpoint.response_failure)
    if endpoint.sainfoin_filter:
        required.append("n_inflorescences_assessed")
    _require(response, required, endpoint.filename)
    response["Id"] = response["Id"].astype(int)
    frame = response.merge(predictors, on="Id", how="inner")
    frame = frame.loc[frame["Id"] != SOURCE_EXCLUDED_GARDEN].copy()
    if endpoint.sainfoin_filter:
        frame = frame.loc[
            (frame["n_inflorescences_assessed"] != 0)
            & (~frame["Id"].isin([19, 28, 52]))
        ].copy()
    return frame


def _feature_names(endpoint: Endpoint, model: str) -> list[str]:
    interaction = [f"{column}__daily" for column in endpoint.interaction_counts]
    if model == "S0":
        return ["PlantS", "Urban_500", "PlantS_x_Urban_500"]
    if model == "S1":
        return interaction
    if model == "S2":
        return interaction + ["PlantS", "Urban_500", "PlantS_x_Urban_500"]
    raise ValueError(model)


def _standardized_design(
    train: pd.DataFrame,
    test: pd.DataFrame,
    endpoint: Endpoint,
    model: str,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, dict[str, float]]]:
    base_columns = [f"{column}__daily" for column in endpoint.interaction_counts]
    if model in {"S0", "S2"}:
        base_columns += ["PlantS", "Urban_500"]
    # unique while retaining order
    seen: set[str] = set()
    base_columns = [c for c in base_columns if not (c in seen or seen.add(c))]

    train_z = pd.DataFrame(index=train.index)
    test_z = pd.DataFrame(index=test.index)
    scaling: dict[str, dict[str, float]] = {}
    for column in base_columns:
        values = train[column].astype(float)
        mean = float(values.mean())
        sd = float(values.std(ddof=0))
        if not np.isfinite(sd) or sd <= 1e-12:
            raise RuntimeError(f"training fold has zero/invalid variation in {column}")
        train_z[column] = (train[column].astype(float) - mean) / sd
        test_z[column] = (test[column].astype(float) - mean) / sd
        scaling[column] = {"mean": mean, "sd": sd}

    if model in {"S0", "S2"}:
        train_z["PlantS_x_Urban_500"] = train_z["PlantS"] * train_z["Urban_500"]
        test_z["PlantS_x_Urban_500"] = test_z["PlantS"] * test_z["Urban_500"]

    names = _feature_names(endpoint, model)
    x_train = sm.add_constant(train_z[names], has_constant="add")
    x_test = sm.add_constant(test_z[names], has_constant="add")
    return x_train, x_test, scaling


def _fit_predict(
    train: pd.DataFrame,
    test: pd.DataFrame,
    endpoint: Endpoint,
    model: str,
) -> tuple[np.ndarray, dict[str, Any]]:
    x_train, x_test, scaling = _standardized_design(train, test, endpoint, model)
    if endpoint.family == "poisson":
        y = train[endpoint.response_success].astype(float).to_numpy()
        fit = sm.GLM(y, x_train, family=sm.families.Poisson()).fit(maxiter=200, disp=0)
    else:
        assert endpoint.response_failure is not None
        success = train[endpoint.response_success].astype(float).to_numpy()
        failure = train[endpoint.response_failure].astype(float).to_numpy()
        total = success + failure
        if np.any(total <= 0):
            raise RuntimeError("binomial response contains non-positive trial count")
        proportion = success / total
        fit = sm.GLM(
            proportion,
            x_train,
            family=sm.families.Binomial(),
            freq_weights=total,
        ).fit(maxiter=200, disp=0)
    prediction = np.asarray(fit.predict(x_test), dtype=float)
    return prediction, {
        "converged": bool(getattr(fit, "converged", True)),
        "coefficients": {str(key): float(value) for key, value in fit.params.items()},
        "scaling": scaling,
    }


def _score(test: pd.DataFrame, prediction: np.ndarray, endpoint: Endpoint) -> tuple[float, float]:
    if endpoint.family == "poisson":
        y = test[endpoint.response_success].astype(float).to_numpy()
        mu = np.clip(prediction, 1e-12, None)
        nll = mu - y * np.log(mu) + gammaln(y + 1.0)
        mae = np.abs(y - mu)
        return float(np.mean(nll)), float(np.mean(mae))

    assert endpoint.response_failure is not None
    success = test[endpoint.response_success].astype(float).to_numpy()
    failure = test[endpoint.response_failure].astype(float).to_numpy()
    total = success + failure
    p = np.clip(prediction, 1e-12, 1.0 - 1e-12)
    nll = -(success * np.log(p) + failure * np.log(1.0 - p)) / total
    observed = success / total
    mae = np.abs(observed - p)
    return float(np.mean(nll)), float(np.mean(mae))


def _bootstrap_interval(values: np.ndarray) -> tuple[float, float]:
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    n = len(values)
    draws = rng.choice(values, size=(BOOTSTRAP_REPLICATES, n), replace=True)
    means = draws.mean(axis=1)
    low, high = np.quantile(means, [0.025, 0.975])
    return float(low), float(high)


def audit_endpoint(endpoint: Endpoint, frame: pd.DataFrame) -> dict[str, Any]:
    gardens = sorted(int(value) for value in frame["Id"].dropna().unique())
    if len(gardens) < 5:
        return {
            "endpoint": endpoint.name,
            "decision": "not_identifiable_from_archive",
            "reason": f"only {len(gardens)} gardens after source-compatible exclusions",
        }

    folds: list[dict[str, Any]] = []
    for garden in gardens:
        train = frame.loc[frame["Id"] != garden].copy()
        test = frame.loc[frame["Id"] == garden].copy()
        if test.empty:
            continue
        record: dict[str, Any] = {"held_out_garden": garden, "test_rows": len(test), "models": {}}
        try:
            for model in ("S0", "S1", "S2"):
                prediction, fit_info = _fit_predict(train, test, endpoint, model)
                nll, mae = _score(test, prediction, endpoint)
                record["models"][model] = {"nll": nll, "mae": mae, "fit": fit_info}
            record["delta_nll_s1_minus_s2"] = (
                record["models"]["S1"]["nll"] - record["models"]["S2"]["nll"]
            )
            record["delta_nll_s0_minus_s1"] = (
                record["models"]["S0"]["nll"] - record["models"]["S1"]["nll"]
            )
        except Exception as exc:
            record["error"] = f"{type(exc).__name__}: {exc}"
        folds.append(record)

    valid = [fold for fold in folds if "delta_nll_s1_minus_s2" in fold]
    if len(valid) != len(gardens):
        return {
            "endpoint": endpoint.name,
            "family": endpoint.family,
            "garden_count": len(gardens),
            "valid_fold_count": len(valid),
            "decision": "not_identifiable_from_archive",
            "reason": "one or more leave-one-garden-out folds could not fit the locked model sequence",
            "folds": folds,
        }

    deltas = np.array([fold["delta_nll_s1_minus_s2"] for fold in valid], dtype=float)
    low, high = _bootstrap_interval(deltas)
    mean = float(deltas.mean())
    median = float(np.median(deltas))
    positive_fraction = float(np.mean(deltas > 0.0))
    decision = (
        "ecological_partial_state_incomplete"
        if mean > 0.0 and low > 0.0
        else "no_detected_residual_urban_information"
    )
    return {
        "endpoint": endpoint.name,
        "family": endpoint.family,
        "garden_count": len(gardens),
        "observation_count": len(frame),
        "interaction_counts": list(endpoint.interaction_counts),
        "mean_delta_nll_s1_minus_s2": mean,
        "median_delta_nll_s1_minus_s2": median,
        "positive_fold_fraction": positive_fraction,
        "bootstrap_95_interval_mean_delta": [low, high],
        "decision": decision,
        "folds": folds,
    }


def run(source: Path, envidat_root: Path) -> dict[str, Any]:
    predictors = build_predictors(source)
    pollination_dir = _find_pollination_dir(envidat_root)
    endpoint_results = []
    for endpoint in ENDPOINTS:
        try:
            frame = _response_frame(endpoint, pollination_dir, predictors)
            endpoint_results.append(audit_endpoint(endpoint, frame))
        except Exception as exc:
            endpoint_results.append(
                {
                    "endpoint": endpoint.name,
                    "decision": "not_identifiable_from_archive",
                    "reason": f"{type(exc).__name__}: {exc}",
                }
            )

    decisions: dict[str, int] = {}
    for result in endpoint_results:
        decisions[result["decision"]] = decisions.get(result["decision"], 0) + 1

    return {
        "status": "e2_zurich_residual_context_audit_complete",
        "source_repository": SOURCE_REPOSITORY,
        "source_commit": SOURCE_COMMIT,
        "source_data_doi": SOURCE_DATA_DOI,
        "source_excluded_garden": SOURCE_EXCLUDED_GARDEN,
        "validation": "leave_one_garden_out",
        "bootstrap_seed": BOOTSTRAP_SEED,
        "bootstrap_replicates": BOOTSTRAP_REPLICATES,
        "primary_comparison": "S2_interaction_plus_context_vs_S1_interaction_only",
        "decision_rule": {
            "ecological_partial_state_incomplete": "mean Delta_g > 0 and garden-bootstrap 95% interval wholly above zero",
            "no_detected_residual_urban_information": "otherwise; not proof of equivalence",
            "not_identifiable_from_archive": "locked response/predictor/fold structure cannot be executed without changing the declaration",
        },
        "decision_counts": decisions,
        "endpoint_results": endpoint_results,
        "interpretation_boundary": (
            "Ecological partial-state test in standardized phytometer plants only. No natural plant genetic, pollen/seed connectivity, "
            "mating-system, cohort-lag or full urban-island convergence claim is permitted."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--betterblooms", type=Path, required=True)
    parser.add_argument("--envidat-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("artifacts/empirical/e2_zurich_residual_context.json"))
    args = parser.parse_args()
    result = run(args.betterblooms, args.envidat_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "decision_counts": result["decision_counts"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
