from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.request import Request, urlopen

import numpy as np

RECORD_ID = 4942351
FILE_NAME = "multiplePaternity.csv"
FILE_MD5 = "600f6f370ffa8ad205d0ccb6bc92ab65"
DOWNLOAD_URL = f"https://zenodo.org/records/{RECORD_ID}/files/{FILE_NAME}?download=1"
RNG_SEED = 20260824
N_PERMUTATIONS = 10_000
REQUIRED = ("plantID", "treatment", "isolation20", "correlatedPaternity")


def _download() -> bytes:
    req = Request(
        DOWNLOAD_URL,
        headers={
            "User-Agent": "eco-genetic-warning-extensions/1.0",
            "Accept": "text/csv,*/*",
        },
    )
    with urlopen(req, timeout=120) as response:
        payload = response.read()
    digest = hashlib.md5(payload).hexdigest()  # source archive publishes MD5
    if digest != FILE_MD5:
        raise RuntimeError(f"source MD5 mismatch: expected={FILE_MD5}, observed={digest}")
    return payload


def _load(payload: bytes) -> list[dict[str, object]]:
    text = payload.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames is None:
        raise RuntimeError("source CSV has no header")
    missing_columns = [name for name in REQUIRED if name not in reader.fieldnames]
    if missing_columns:
        raise RuntimeError(f"required source columns absent: {missing_columns}; fields={reader.fieldnames}")

    rows: list[dict[str, object]] = []
    for row_id, raw in enumerate(reader):
        plant_id = str(raw["plantID"]).strip()
        treatment = str(raw["treatment"]).strip().lower()
        if not plant_id or not treatment:
            raise RuntimeError(f"blank plantID/treatment in row {raw!r}")
        try:
            isolation = float(str(raw["isolation20"]).strip())
            paternity = float(str(raw["correlatedPaternity"]).strip())
        except ValueError as exc:
            raise RuntimeError(f"non-numeric primary value in row {raw!r}") from exc
        if not np.isfinite(isolation) or not np.isfinite(paternity):
            raise RuntimeError(f"non-finite primary value in row {raw!r}")
        rows.append(
            {
                "row_id": row_id,
                "plantID": plant_id,
                "treatment": treatment,
                "isolation20": isolation,
                "correlatedPaternity": paternity,
            }
        )

    if len(rows) < 12:
        raise RuntimeError(f"too few seed-family rows for declared test: n={len(rows)}")

    # Each row is one fruit/seed-family sample; multiple treatments may occur on
    # one maternal plant. Spatial isolation, however, is an individual property
    # and must agree across every row sharing plantID.
    for plant_id in sorted({str(row["plantID"]) for row in rows}):
        group = [row for row in rows if str(row["plantID"]) == plant_id]
        isolations = {float(row["isolation20"]) for row in group}
        if len(isolations) != 1:
            raise RuntimeError(
                f"repeated plantID disagrees on isolation20: plantID={plant_id}, "
                f"isolation20={sorted(isolations)}"
            )

    if len({str(row["plantID"]) for row in rows}) < 10:
        raise RuntimeError("too few unique maternal plants for grouped validation")
    return rows


def _design(
    rows: list[dict[str, object]],
    *,
    include_isolation: bool,
    treatment_levels: list[str],
    isolation_mean: float | None = None,
    isolation_sd: float | None = None,
) -> tuple[np.ndarray, float | None, float | None, list[str]]:
    n = len(rows)
    blocks = [np.ones((n, 1), dtype=float)]
    names = ["intercept"]
    for level in treatment_levels[1:]:
        blocks.append(np.array([[float(str(row["treatment"]) == level)] for row in rows]))
        names.append(f"treatment={level}")
    if include_isolation:
        values = np.array([float(row["isolation20"]) for row in rows], dtype=float)
        if isolation_mean is None:
            isolation_mean = float(values.mean())
        if isolation_sd is None:
            isolation_sd = float(values.std(ddof=0))
        if isolation_sd <= 0:
            raise RuntimeError("isolation20 has zero variance")
        blocks.append(((values - isolation_mean) / isolation_sd)[:, None])
        names.append("z_isolation20")
    return np.concatenate(blocks, axis=1), isolation_mean, isolation_sd, names


def _fit_predict(
    train: list[dict[str, object]],
    test: list[dict[str, object]],
    *,
    include_isolation: bool,
    treatment_levels: list[str],
) -> tuple[np.ndarray, np.ndarray]:
    x_train, mean, sd, _ = _design(
        train,
        include_isolation=include_isolation,
        treatment_levels=treatment_levels,
    )
    x_test, _, _, _ = _design(
        test,
        include_isolation=include_isolation,
        treatment_levels=treatment_levels,
        isolation_mean=mean,
        isolation_sd=sd,
    )
    y_train = np.array([float(row["correlatedPaternity"]) for row in train])
    y_test = np.array([float(row["correlatedPaternity"]) for row in test])
    beta, *_ = np.linalg.lstsq(x_train, y_train, rcond=None)
    return y_test, x_test @ beta


def _grouped_loo(
    rows: list[dict[str, object]], include_isolation: bool, treatment_levels: list[str]
) -> dict[str, object]:
    observed: list[float] = []
    predicted: list[float] = []
    residual_rows: list[dict[str, object]] = []
    plant_ids = sorted({str(row["plantID"]) for row in rows})

    for held_out_plant in plant_ids:
        train = [row for row in rows if str(row["plantID"]) != held_out_plant]
        test = [row for row in rows if str(row["plantID"]) == held_out_plant]
        y, pred = _fit_predict(
            train,
            test,
            include_isolation=include_isolation,
            treatment_levels=treatment_levels,
        )
        for held, o_raw, p_raw in zip(test, y, pred, strict=True):
            o = float(o_raw)
            p = float(p_raw)
            observed.append(o)
            predicted.append(p)
            residual_rows.append(
                {
                    "row_id": held["row_id"],
                    "plantID": held["plantID"],
                    "treatment": held["treatment"],
                    "isolation20": held["isolation20"],
                    "observed": o,
                    "predicted": p,
                    "residual": o - p,
                }
            )

    obs = np.array(observed)
    pred = np.array(predicted)
    residual = obs - pred
    return {
        "mse": float(np.mean(residual**2)),
        "mae": float(np.mean(np.abs(residual))),
        "fold_count": len(plant_ids),
        "predictions": residual_rows,
    }


def _rss_and_beta(
    rows: list[dict[str, object]], include_isolation: bool, treatment_levels: list[str]
) -> tuple[float, np.ndarray, list[str]]:
    x, _, _, names = _design(
        rows,
        include_isolation=include_isolation,
        treatment_levels=treatment_levels,
    )
    y = np.array([float(row["correlatedPaternity"]) for row in rows])
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    residual = y - x @ beta
    return float(np.sum(residual**2)), beta, names


def _plant_level_table(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    plants: list[dict[str, object]] = []
    for plant_id in sorted({str(row["plantID"]) for row in rows}):
        group = [row for row in rows if str(row["plantID"]) == plant_id]
        profile = tuple(sorted(str(row["treatment"]) for row in group))
        plants.append(
            {
                "plantID": plant_id,
                "treatment_profile": profile,
                "isolation20": float(group[0]["isolation20"]),
                "row_count": len(group),
            }
        )
    return plants


def _permute_isolation_within_profile(
    rows: list[dict[str, object]], rng: np.random.Generator
) -> list[dict[str, object]]:
    copied = [dict(row) for row in rows]
    plants = _plant_level_table(rows)
    replacement: dict[str, float] = {}
    profiles = sorted({tuple(plant["treatment_profile"]) for plant in plants})
    for profile in profiles:
        group = [plant for plant in plants if tuple(plant["treatment_profile"]) == profile]
        plant_ids = [str(plant["plantID"]) for plant in group]
        values = np.array([float(plant["isolation20"]) for plant in group], dtype=float)
        shuffled = rng.permutation(values) if len(group) > 1 else values
        replacement.update({plant_id: float(value) for plant_id, value in zip(plant_ids, shuffled, strict=True)})
    for row in copied:
        row["isolation20"] = replacement[str(row["plantID"])]
    return copied


def run() -> dict[str, object]:
    payload = _download()
    rows = _load(payload)
    treatment_levels = sorted({str(row["treatment"]) for row in rows})
    if len(treatment_levels) < 2:
        raise RuntimeError(f"expected >=2 treatments, got {treatment_levels}")

    m0_loo = _grouped_loo(rows, False, treatment_levels)
    m1_loo = _grouped_loo(rows, True, treatment_levels)
    rss0, beta0, names0 = _rss_and_beta(rows, False, treatment_levels)
    rss1, beta1, names1 = _rss_and_beta(rows, True, treatment_levels)
    isolation_idx = names1.index("z_isolation20")
    isolation_beta = float(beta1[isolation_idx])
    observed_gain = float(rss0 - rss1)

    rng = np.random.default_rng(RNG_SEED)
    extreme = 0
    gains: list[float] = []
    for _ in range(N_PERMUTATIONS):
        permuted = _permute_isolation_within_profile(rows, rng)
        perm_rss1, _, _ = _rss_and_beta(permuted, True, treatment_levels)
        gain = float(rss0 - perm_rss1)
        gains.append(gain)
        if gain >= observed_gain - 1e-15:
            extreme += 1
    permutation_p = float((1 + extreme) / (N_PERMUTATIONS + 1))

    predictive = float(m1_loo["mse"]) < float(m0_loo["mse"])
    model_support = isolation_beta > 0 and permutation_p < 0.05
    if predictive and model_support:
        decision = "residual_isolation_detected"
    elif predictive:
        decision = "predictive_residual_isolation_only"
    elif model_support:
        decision = "model_residual_isolation_only"
    else:
        decision = "no_detected_residual_isolation"

    treatment_summary = {}
    for level in treatment_levels:
        group = [row for row in rows if str(row["treatment"]) == level]
        treatment_summary[level] = {
            "n_rows": len(group),
            "n_maternal_plants": len({str(row["plantID"]) for row in group}),
            "mean_correlated_paternity": float(np.mean([float(row["correlatedPaternity"]) for row in group])),
            "mean_isolation20": float(np.mean([float(row["isolation20"]) for row in group])),
        }

    plants = _plant_level_table(rows)
    profile_summary: dict[str, int] = {}
    for plant in plants:
        key = "/".join(str(value) for value in plant["treatment_profile"])
        profile_summary[key] = profile_summary.get(key, 0) + 1

    unique_plants = len(plants)
    return {
        "stage": "Oenothera harringtonii mating-state residual-isolation test",
        "decision": decision,
        "source_lock": {
            "publication_doi": "10.1111/mec.14115",
            "dataset_doi": "10.5061/dryad.p24q3",
            "zenodo_record": RECORD_ID,
            "file": FILE_NAME,
            "published_md5": FILE_MD5,
            "observed_md5": hashlib.md5(payload).hexdigest(),
            "download_url": DOWNLOAD_URL,
        },
        "schema": {
            "n_seed_family_rows": len(rows),
            "n_maternal_plants": unique_plants,
            "repeated_plant_rows": len(rows) - unique_plants,
            "treatment_levels": treatment_levels,
            "treatment_profile_counts": profile_summary,
            "response": "correlatedPaternity",
            "residual_state_coordinate": "isolation20",
            "validation_unit": "maternal plant; all repeated fruit/seed-family rows held out together",
            "permutation_unit": "maternal-plant isolation values permuted within identical treatment-profile strata",
        },
        "treatment_summary": treatment_summary,
        "models": {
            "M0": {
                "formula": "correlatedPaternity ~ treatment",
                "loo_mse": m0_loo["mse"],
                "loo_mae": m0_loo["mae"],
                "fold_count": m0_loo["fold_count"],
                "rss": rss0,
                "design_columns": names0,
                "beta": [float(v) for v in beta0],
            },
            "M1": {
                "formula": "correlatedPaternity ~ treatment + z(isolation20)",
                "loo_mse": m1_loo["mse"],
                "loo_mae": m1_loo["mae"],
                "fold_count": m1_loo["fold_count"],
                "rss": rss1,
                "design_columns": names1,
                "beta": [float(v) for v in beta1],
                "isolation_beta": isolation_beta,
            },
        },
        "incremental_isolation": {
            "loo_mse_change_M1_minus_M0": float(m1_loo["mse"] - m0_loo["mse"]),
            "loo_mse_percent_change": float(100.0 * (m1_loo["mse"] - m0_loo["mse"]) / m0_loo["mse"]),
            "rss_gain_M0_minus_M1": observed_gain,
            "treatment_profile_stratified_plant_permutation_p": permutation_p,
            "permutations": N_PERMUTATIONS,
            "rng_seed": RNG_SEED,
            "permuted_gain_95pct": [float(np.quantile(gains, 0.025)), float(np.quantile(gains, 0.975))],
        },
        "claim_boundary": (
            "This is a contemporary mating-state (G_mating/C_pollen) test. It does not use a direct ecological-function "
            "endpoint and does not establish a universal fragmentation or isolation threshold."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/oenothera_mating_state_result.json")
    args = parser.parse_args()
    result = run()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], **result["incremental_isolation"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
