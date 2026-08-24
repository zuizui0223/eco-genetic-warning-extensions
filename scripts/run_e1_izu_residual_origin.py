from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

PRIMARY_NUMERIC = {
    "C0": ("richness",),
    "C1": ("TM_z", "FDQ", "FEve"),
    "C2": ("TM_z", "FDQ", "FEve", "dist"),
}
CATEGORICAL = ("season", "plant")
RESPONSE = "pollen_z"
EXPECTED_SITES = 8
EXPECTED_POLLEN_ROWS = 572


def _close(a: float, b: float, tol: float = 1e-10) -> bool:
    return bool(abs(float(a) - float(b)) <= tol)


def _infer_site_alias_mapping(
    main: pd.DataFrame,
    pollen: pd.DataFrame,
    species_plant: pd.DataFrame,
) -> dict[str, str]:
    """Map pollen-table site aliases to data_main site names without using the outcome."""
    # First map numeric siteid -> pollen alias using the shared species-level trait-matching values.
    siteid_to_alias: dict[int, str] = {}
    sp_unique = species_plant[["siteid", "season", "plant", "TM_sp"]].drop_duplicates()
    pollen_unique = pollen.dropna(subset=["TM_sp"])[["site", "season", "plant", "TM_sp"]].drop_duplicates()
    for siteid, group in sp_unique.groupby("siteid"):
        candidates: list[tuple[str, int]] = []
        for alias, candidate in pollen_unique.groupby("site"):
            joined = group.merge(candidate, on=["season", "plant"], suffixes=("_sp", "_pollen"))
            if joined.empty:
                continue
            exact = sum(
                _close(left, right)
                for left, right in zip(joined["TM_sp_sp"], joined["TM_sp_pollen"], strict=True)
            )
            if exact == len(joined):
                candidates.append((str(alias), int(exact)))
        if not candidates:
            raise RuntimeError(f"no pollen alias matches siteid={siteid}")
        candidates.sort(key=lambda item: item[1], reverse=True)
        if len(candidates) > 1 and candidates[0][1] == candidates[1][1]:
            raise RuntimeError(f"ambiguous pollen alias for siteid={siteid}: {candidates}")
        siteid_to_alias[int(siteid)] = candidates[0][0]

    # Then map siteid -> data_main site using FDQ and FEve, which are shared exactly by site-season.
    state_unique = (
        species_plant.groupby(["siteid", "season"], as_index=False)[["FDQ", "FEve"]]
        .first()
    )
    siteid_to_main: dict[int, str] = {}
    for siteid, group in state_unique.groupby("siteid"):
        matches: list[str] = []
        for site_name, candidate in main.groupby("site"):
            joined = group.merge(candidate[["season", "FDQ", "FEve"]], on="season", suffixes=("_sp", "_main"))
            if len(joined) != 5:
                continue
            if all(
                _close(fdq_sp, fdq_main) and _close(feve_sp, feve_main)
                for fdq_sp, fdq_main, feve_sp, feve_main in zip(
                    joined["FDQ_sp"],
                    joined["FDQ_main"],
                    joined["FEve_sp"],
                    joined["FEve_main"],
                    strict=True,
                )
            ):
                matches.append(str(site_name))
        if len(matches) != 1:
            raise RuntimeError(f"siteid={siteid} has non-unique main-site mapping: {matches}")
        siteid_to_main[int(siteid)] = matches[0]

    mapping = {siteid_to_alias[sid]: siteid_to_main[sid] for sid in siteid_to_alias}
    if len(mapping) != EXPECTED_SITES or len(set(mapping.values())) != EXPECTED_SITES:
        raise RuntimeError(f"expected a one-to-one 8-site mapping, got {mapping}")
    return mapping


def _prepare(data_root: Path) -> tuple[pd.DataFrame, dict[str, str]]:
    main = pd.read_csv(data_root / "data_main.csv")
    pollen = pd.read_csv(data_root / "data_pollen.csv")
    species_plant = pd.read_csv(data_root / "data_sp_plant.csv")

    if len(main) != 40 or main["site"].nunique() != EXPECTED_SITES:
        raise RuntimeError("data_main must contain 40 rows from 8 sites")
    if len(pollen) != EXPECTED_POLLEN_ROWS:
        raise RuntimeError(f"expected {EXPECTED_POLLEN_ROWS} pollen rows, got {len(pollen)}")

    mapping = _infer_site_alias_mapping(main, pollen, species_plant)
    pollen = pollen.copy()
    pollen["main_site"] = pollen["site"].map(mapping)
    if pollen["main_site"].isna().any():
        raise RuntimeError("not every pollen site was mapped to data_main")

    main_state = main[["site", "season", "FDQ", "FEve", "dist", "area", "richness", "D"]].rename(
        columns={"site": "main_site"}
    )
    merged = pollen.merge(main_state, on=["main_site", "season"], how="left", validate="many_to_one")

    required = [RESPONSE, "TM_z", "FDQ", "FEve", "dist", "richness", *CATEGORICAL]
    missing = merged[required].isna().sum().to_dict()
    if any(int(value) != 0 for value in missing.values()):
        raise RuntimeError(f"primary E1 variables contain missing values after synchronized join: {missing}")
    if merged["main_site"].nunique() != EXPECTED_SITES:
        raise RuntimeError("merged pollen table does not retain all 8 sites")
    if any(group["dist"].nunique() != 1 for _, group in merged.groupby("main_site")):
        raise RuntimeError("distance must be constant within site")
    return merged, mapping


def _design_fit(train: pd.DataFrame, test: pd.DataFrame, numeric: tuple[str, ...]) -> tuple[np.ndarray, list[str]]:
    blocks_train: list[np.ndarray] = [np.ones((len(train), 1), dtype=float)]
    blocks_test: list[np.ndarray] = [np.ones((len(test), 1), dtype=float)]
    names = ["intercept"]

    for column in numeric:
        mean = float(train[column].mean())
        std = float(train[column].std(ddof=0))
        if std <= 0:
            std = 1.0
        blocks_train.append(((train[[column]].to_numpy(dtype=float) - mean) / std))
        blocks_test.append(((test[[column]].to_numpy(dtype=float) - mean) / std))
        names.append(column)

    for column in CATEGORICAL:
        levels = sorted(str(value) for value in train[column].dropna().unique())
        # Drop the first level because an intercept is present. Unseen held-out levels map to all zero.
        for level in levels[1:]:
            blocks_train.append((train[column].astype(str).to_numpy() == level).astype(float)[:, None])
            blocks_test.append((test[column].astype(str).to_numpy() == level).astype(float)[:, None])
            names.append(f"{column}={level}")

    x_train = np.concatenate(blocks_train, axis=1)
    x_test = np.concatenate(blocks_test, axis=1)
    beta, *_ = np.linalg.lstsq(x_train, train[RESPONSE].to_numpy(dtype=float), rcond=None)
    return x_test @ beta, names


def _metrics(y: np.ndarray, pred: np.ndarray) -> dict[str, float | None]:
    residual = y - pred
    mse = float(np.mean(residual**2))
    mae = float(np.mean(np.abs(residual)))
    corr: float | None
    if len(y) > 1 and float(np.std(y)) > 0 and float(np.std(pred)) > 0:
        corr = float(np.corrcoef(y, pred)[0, 1])
    else:
        corr = None
    return {"mse": mse, "mae": mae, "correlation": corr}


def _rank(values: np.ndarray) -> np.ndarray:
    # pandas' average rank handles ties deterministically and avoids a scipy dependency.
    return pd.Series(values).rank(method="average").to_numpy(dtype=float)


def _spearman(x: np.ndarray, y: np.ndarray) -> float | None:
    rx, ry = _rank(x), _rank(y)
    if float(np.std(rx)) <= 0 or float(np.std(ry)) <= 0:
        return None
    return float(np.corrcoef(rx, ry)[0, 1])


def run(data_root: Path) -> dict[str, object]:
    data, mapping = _prepare(data_root)
    sites = sorted(str(value) for value in data["main_site"].unique())
    folds: list[dict[str, object]] = []
    prediction_rows: list[dict[str, object]] = []

    for held_out in sites:
        train = data[data["main_site"] != held_out].copy()
        test = data[data["main_site"] == held_out].copy()
        fold: dict[str, object] = {
            "held_out_site": held_out,
            "n": int(len(test)),
            "distance_from_mainland": float(test["dist"].iloc[0]),
            "models": {},
        }
        for model_id, numeric in PRIMARY_NUMERIC.items():
            pred, design_names = _design_fit(train, test, numeric)
            y = test[RESPONSE].to_numpy(dtype=float)
            metrics = _metrics(y, pred)
            fold["models"][model_id] = {**metrics, "numeric_predictors": list(numeric), "design_columns": design_names}
            for row_index, observed, predicted in zip(test.index, y, pred, strict=True):
                prediction_rows.append({
                    "model": model_id,
                    "held_out_site": held_out,
                    "source_row": int(row_index),
                    "distance_from_mainland": float(test.loc[row_index, "dist"]),
                    "observed": float(observed),
                    "predicted": float(predicted),
                    "residual": float(observed - predicted),
                })
        folds.append(fold)

    def aggregate(model_id: str) -> dict[str, float]:
        mse = np.array([float(fold["models"][model_id]["mse"]) for fold in folds])
        mae = np.array([float(fold["models"][model_id]["mae"]) for fold in folds])
        n = np.array([int(fold["n"]) for fold in folds], dtype=float)
        return {
            "mean_site_mse": float(mse.mean()),
            "mean_site_mae": float(mae.mean()),
            "row_weighted_mse": float(np.average(mse, weights=n)),
            "row_weighted_mae": float(np.average(mae, weights=n)),
        }

    aggregates = {model_id: aggregate(model_id) for model_id in PRIMARY_NUMERIC}
    c2_mse_better = sum(
        float(fold["models"]["C2"]["mse"]) < float(fold["models"]["C1"]["mse"])
        for fold in folds
    )
    c1_mse_better = sum(
        float(fold["models"]["C1"]["mse"]) < float(fold["models"]["C0"]["mse"])
        for fold in folds
    )

    residual_by_site: dict[str, dict[str, float]] = {}
    for model_id in ("C1", "C2"):
        rows = [row for row in prediction_rows if row["model"] == model_id]
        grouped: dict[str, list[float]] = {}
        distances: dict[str, float] = {}
        for row in rows:
            grouped.setdefault(str(row["held_out_site"]), []).append(float(row["residual"]))
            distances[str(row["held_out_site"])] = float(row["distance_from_mainland"])
        site_rows = [
            {
                "site": site,
                "distance_from_mainland": distances[site],
                "mean_residual": float(np.mean(values)),
            }
            for site, values in sorted(grouped.items())
        ]
        rho = _spearman(
            np.array([row["distance_from_mainland"] for row in site_rows], dtype=float),
            np.array([row["mean_residual"] for row in site_rows], dtype=float),
        )
        residual_by_site[model_id] = {"spearman_residual_vs_distance": rho, "sites": site_rows}

    c1 = aggregates["C1"]["row_weighted_mse"]
    c2 = aggregates["C2"]["row_weighted_mse"]
    return {
        "stage": "E1 Honshu-Izu ecological partial-state residual-origin test",
        "source_lock": {
            "doi": "10.6084/m9.figshare.25025000.v1",
            "article_id": 25025000,
            "version": 1,
        },
        "schema_mapping": {
            "site_alias_to_main_site": mapping,
            "response": RESPONSE,
            "models": {key: list(value) for key, value in PRIMARY_NUMERIC.items()},
            "categorical_structure": list(CATEGORICAL),
            "join_key": ["site", "season"],
            "row_count": int(len(data)),
            "site_count": int(data["main_site"].nunique()),
        },
        "validation": "leave-one-site-out; all rows from one of 8 sites held out per fold",
        "folds": folds,
        "aggregates": aggregates,
        "c1_vs_c0": {
            "C1_lower_mse_fold_count": int(c1_mse_better),
            "row_weighted_mse_change_C1_minus_C0": float(
                aggregates["C1"]["row_weighted_mse"] - aggregates["C0"]["row_weighted_mse"]
            ),
        },
        "c2_vs_c1": {
            "C2_lower_mse_fold_count": int(c2_mse_better),
            "row_weighted_mse_change_C2_minus_C1": float(c2 - c1),
            "row_weighted_mse_percent_change": float(100.0 * (c2 - c1) / c1),
            "mean_site_mse_change_C2_minus_C1": float(
                aggregates["C2"]["mean_site_mse"] - aggregates["C1"]["mean_site_mse"]
            ),
        },
        "held_out_residuals": residual_by_site,
        "interpretation_boundary": (
            "This is an ecological partial-state test only. It evaluates whether distance adds transferable predictive information "
            "after the preregistered I/T state; it cannot establish full eco-genetic convergence because G/C/R/M are not synchronized. "
            "The candidate state itself must not be called sufficient merely because geography fails to improve prediction."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", default="_external/e1_izu_figshare/downloads")
    parser.add_argument("--output", default="artifacts/empirical/e1_residual_origin_result.json")
    args = parser.parse_args()

    result = run(Path(args.data_root))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["c2_vs_c1"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
