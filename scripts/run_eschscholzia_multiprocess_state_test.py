from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, Ridge

DATA_ROOT = "https://data-package.ceh.ac.uk/data"
USER_AGENT = "eco-genetic-warning-extensions/1.0"
RNG_SEED = 20260825
N_BOOT = 10_000

SOURCES = {
    "pollinator": {
        "uuid": "01906784-6742-44bf-b244-a4b63bed8d82",
        "doi": "10.5285/01906784-6742-44bf-b244-a4b63bed8d82",
        "package_sha256": "66b0b9eec2ffcf6df8bc19f4677c159e5f574a4a23aa452221cc2b552b01f0c5",
        "member": "data/Pantrap_catches_from_Buckinghamshire_UK.csv",
        "csv_sha256": "db063840850fb4f358db7e99271feb9b9a92f6701b889d1b59a1348ffada89ef",
    },
    "f_seed": {
        "uuid": "8caf2d8a-564d-4f2e-a797-174165a83796",
        "doi": "10.5285/8caf2d8a-564d-4f2e-a797-174165a83796",
        "package_sha256": "b541f46ecee09ba7c5dbbcbe06f30f343e2620e3942289c5839f98382d089859",
        "member": "data/The_seed_set_of_supplemented_and_pollinator_exposed_Ecalifornica_flowers.csv",
        "csv_sha256": "83ab56cc8b3e4b2ae2b7141e55683b1cff2734006d4fa4f6735605d3a2be379f",
    },
    "r_seed": {
        "uuid": "5b400b69-b828-45e8-b04e-7ccbfdb0987f",
        "doi": "10.5285/5b400b69-b828-45e8-b04e-7ccbfdb0987f",
        "package_sha256": "6781fed48c9c7b8a293e713434a02769a2490d68c6f2e218167f623af1c60ec1",
        "member": "data/Eschscholzia_californica_seed_set.csv",
        "csv_sha256": "ad52e8b52885cde66a0ed5476bffb0e9894b4d0429e42d927ea72b388b3ea27b",
    },
    "g_paternity": {
        "uuid": "7b721c07-bc38-4815-8669-4675867663d0",
        "doi": "10.5285/7b721c07-bc38-4815-8669-4675867663d0",
        "package_sha256": "e785a2aad2ba43ef5a5a6b90122badc2b70b1682a4ada5719e8a2ed25cddf033",
        "member": "data/Paternity_analysis_of_introduced_Eschscholzia_californica_plants.csv",
        "csv_sha256": "6805ceb4164fefa373ba758a0fcf0a58fe67624b432d3aea6d344d690efd71f2",
    },
}


class NotIdentifiable(RuntimeError):
    pass


@dataclass
class EndpointResult:
    decision: str
    model_scores: dict[str, float]
    per_array_scores: dict[str, dict[str, float]]
    comparisons: dict[str, dict[str, object]]
    n_rows: int
    n_arrays: int
    notes: dict[str, object]


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _download_source(spec: dict[str, str]) -> tuple[bytes, bytes, str]:
    url = f"{DATA_ROOT}/{spec['uuid']}.zip"
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/zip,*/*"})
    with urlopen(req, timeout=180) as response:
        package = response.read()
    observed_package = _sha256(package)
    if observed_package != spec["package_sha256"]:
        raise RuntimeError(
            f"package SHA mismatch for {spec['doi']}: expected={spec['package_sha256']} observed={observed_package}"
        )
    with zipfile.ZipFile(io.BytesIO(package)) as archive:
        try:
            raw = archive.read(spec["member"])
        except KeyError as exc:
            raise RuntimeError(f"locked CSV member absent: {spec['member']}") from exc
    observed_csv = _sha256(raw)
    if observed_csv != spec["csv_sha256"]:
        raise RuntimeError(
            f"CSV SHA mismatch for {spec['doi']}: expected={spec['csv_sha256']} observed={observed_csv}"
        )
    return package, raw, url


def _read_csv(raw: bytes) -> pd.DataFrame:
    # dtype=str prevents numeric key coercion (e.g. 1 -> 1.0) across source products.
    return pd.read_csv(io.BytesIO(raw), dtype=str, keep_default_na=False, encoding="utf-8-sig")


def _clean(value: object) -> str:
    return str(value).strip()


def _numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.replace("", np.nan), errors="coerce")


def _array_key(block: object, array: object) -> str:
    b = _clean(block)
    a = _clean(array)
    if not b or not a:
        raise NotIdentifiable("blank Block/Experimental array key")
    return f"{b}||{a}"


def _plant_key(block: object, array: object, plant: object) -> str:
    p = _clean(plant)
    if not p:
        raise NotIdentifiable("blank Plant identification number")
    return f"{_array_key(block, array)}||{p}"


def _unique_nonblank(values: pd.Series, *, label: str) -> str:
    cleaned = sorted({_clean(v) for v in values if _clean(v)})
    if len(cleaned) != 1:
        raise NotIdentifiable(f"{label} is not internally unique: {cleaned}")
    return cleaned[0]


def _prepare_pollinator(df: pd.DataFrame) -> pd.DataFrame:
    required = [
        "Block",
        "Experimental array",
        "Habitat",
        "Pollinator species",
        "Intertegular span (mm)",
    ]
    missing = [x for x in required if x not in df.columns]
    if missing:
        raise NotIdentifiable(f"pollinator columns missing: {missing}")

    work = df.copy()
    work["array_key"] = [
        _array_key(b, a) for b, a in zip(work["Block"], work["Experimental array"], strict=True)
    ]
    work["species_clean"] = work["Pollinator species"].map(_clean)
    work["itd"] = _numeric(work["Intertegular span (mm)"])

    rows = []
    for key, group in work.groupby("array_key", sort=True):
        block = _unique_nonblank(group["Block"], label=f"pollinator Block {key}")
        habitat = _unique_nonblank(group["Habitat"], label=f"pollinator Habitat {key}")
        count = int((group["species_clean"] != "").sum())
        itd = group.loc[np.isfinite(group["itd"]) & (group["itd"] > 0), "itd"].astype(float)
        if len(itd) == 0:
            raise NotIdentifiable(f"no valid positive ITD for array {key}")
        rows.append(
            {
                "array_key": key,
                "block": block,
                "habitat": habitat,
                "I_log_count": float(np.log1p(count)),
                "I_count": count,
                "T_mean_ITD": float(itd.mean()),
                "n_valid_ITD": int(len(itd)),
            }
        )
    state = pd.DataFrame(rows)
    if len(state) != 16:
        raise NotIdentifiable(f"expected 16 pollinator arrays, observed {len(state)}")
    return state


def _check_join_metadata(
    df: pd.DataFrame,
    pstate: pd.DataFrame,
    *,
    block_col: str,
    array_col: str,
    habitat_col: str,
    label: str,
) -> pd.DataFrame:
    work = df.copy()
    work["array_key"] = [
        _array_key(b, a) for b, a in zip(work[block_col], work[array_col], strict=True)
    ]
    pmap = pstate.set_index("array_key")
    for key, group in work.groupby("array_key", sort=True):
        if key not in pmap.index:
            raise NotIdentifiable(f"{label}: array not found in pollinator state: {key}")
        b = _unique_nonblank(group[block_col], label=f"{label} Block {key}")
        h = _unique_nonblank(group[habitat_col], label=f"{label} Habitat {key}")
        if b != str(pmap.loc[key, "block"]):
            raise NotIdentifiable(f"{label}: Block mismatch for {key}: {b} vs {pmap.loc[key, 'block']}")
        if h != str(pmap.loc[key, "habitat"]):
            raise NotIdentifiable(f"{label}: Habitat mismatch for {key}: {h} vs {pmap.loc[key, 'habitat']}")
    work = work.merge(
        pstate[["array_key", "block", "habitat", "I_log_count", "T_mean_ITD"]],
        on="array_key",
        how="left",
        validate="many_to_one",
    )
    return work


def _prepare_f(df: pd.DataFrame, pstate: pd.DataFrame) -> pd.DataFrame:
    required = [
        "Block",
        "Experimental_array",
        "Plant_identification_number",
        "Habitat",
        "Mean_number_of_seeds_from_field_exposed_flowers",
        "Number_of_seeds_from_supplemented_flowers",
    ]
    missing = [x for x in required if x not in df.columns]
    if missing:
        raise NotIdentifiable(f"F columns missing: {missing}")
    work = _check_join_metadata(
        df,
        pstate,
        block_col="Block",
        array_col="Experimental_array",
        habitat_col="Habitat",
        label="F",
    )
    work["plant_key"] = [
        _plant_key(b, a, p)
        for b, a, p in zip(
            work["Block"], work["Experimental_array"], work["Plant_identification_number"], strict=True
        )
    ]
    if work["plant_key"].duplicated().any():
        dup = work.loc[work["plant_key"].duplicated(), "plant_key"].iloc[0]
        raise NotIdentifiable(f"F duplicate plant row: {dup}")
    f = _numeric(work["Mean_number_of_seeds_from_field_exposed_flowers"])
    d = _numeric(work["Number_of_seeds_from_supplemented_flowers"])
    if (~np.isfinite(f) | (f < 0)).any():
        raise NotIdentifiable("F primary response has missing/non-finite/negative value")
    work["y_F"] = np.log1p(f.astype(float))
    work["D_capacity"] = np.where(np.isfinite(d) & (d >= 0), np.log1p(d.astype(float)), np.nan)
    if work["array_key"].nunique() < 12:
        raise NotIdentifiable("F spans fewer than 12 arrays")
    return work


def _sample_type(value: object) -> str | None:
    text = _clean(value).casefold()
    if "exclud" in text:
        return "excluded"
    if "expos" in text:
        return "exposed"
    return None


def _prepare_r(df: pd.DataFrame, pstate: pd.DataFrame) -> pd.DataFrame:
    required = [
        "Block",
        "Experimental array",
        "Plant identification number",
        "Sample type",
        "Habitat",
        "Number of seeds",
    ]
    missing = [x for x in required if x not in df.columns]
    if missing:
        raise NotIdentifiable(f"R columns missing: {missing}")
    work = _check_join_metadata(
        df,
        pstate,
        block_col="Block",
        array_col="Experimental array",
        habitat_col="Habitat",
        label="R",
    )
    work["plant_key"] = [
        _plant_key(b, a, p)
        for b, a, p in zip(
            work["Block"], work["Experimental array"], work["Plant identification number"], strict=True
        )
    ]
    work["sample_class"] = work["Sample type"].map(_sample_type)
    work["seed_n"] = _numeric(work["Number of seeds"])
    valid = work[(work["sample_class"] == "excluded") & np.isfinite(work["seed_n"]) & (work["seed_n"] >= 0)].copy()
    if valid.empty:
        raise NotIdentifiable("R has no recognized pollinator-excluded seed rows")
    agg = (
        valid.groupby(["plant_key", "array_key"], as_index=False)["seed_n"].mean().rename(columns={"seed_n": "mean_excluded_seed"})
    )
    agg["R_auto"] = np.log1p(agg["mean_excluded_seed"].astype(float))
    return agg[["plant_key", "array_key", "R_auto"]]


def _parentage(value: object) -> int | None:
    text = _clean(value).casefold()
    if "outcross" in text:
        return 1
    if "self" in text:
        return 0
    return None


def _prepare_g(df: pd.DataFrame, pstate: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, int]]:
    required = [
        "Block",
        "Experimental_array",
        "Plant_identification_number",
        "Habitat",
        "Parentage",
        "Distance_of_pollen_movement",
    ]
    missing = [x for x in required if x not in df.columns]
    if missing:
        raise NotIdentifiable(f"G columns missing: {missing}")
    work = _check_join_metadata(
        df,
        pstate,
        block_col="Block",
        array_col="Experimental_array",
        habitat_col="Habitat",
        label="G",
    )
    work["plant_key"] = [
        _plant_key(b, a, p)
        for b, a, p in zip(
            work["Block"], work["Experimental_array"], work["Plant_identification_number"], strict=True
        )
    ]
    work["G_outcross"] = work["Parentage"].map(_parentage)
    unrecognized = int(work["G_outcross"].isna().sum())
    g = work[work["G_outcross"].notna()].copy()
    if g.empty or set(g["G_outcross"].astype(int).unique()) != {0, 1}:
        raise NotIdentifiable("G Parentage does not expose both recognized self and outcross classes")
    if g["array_key"].nunique() < 12:
        raise NotIdentifiable("G recognized parentage spans fewer than 12 arrays")
    g["G_outcross"] = g["G_outcross"].astype(int)

    dist = _numeric(g["Distance_of_pollen_movement"])
    c = g[(g["G_outcross"] == 1) & np.isfinite(dist) & (dist >= 0)].copy()
    if not c.empty:
        c["y_C"] = np.log1p(_numeric(c["Distance_of_pollen_movement"]).astype(float))
    counts = {"total_paternity_rows": int(len(work)), "recognized_G_rows": int(len(g)), "unrecognized_parentage_rows": unrecognized}
    return g, c, counts


def _array_weights(df: pd.DataFrame) -> np.ndarray:
    counts = df.groupby("array_key")["array_key"].transform("count").astype(float)
    return (1.0 / counts).to_numpy(dtype=float)


def _z_from_unique_arrays(train: pd.DataFrame, test: pd.DataFrame, column: str) -> tuple[np.ndarray, np.ndarray]:
    unique = train[["array_key", column]].drop_duplicates("array_key")
    if unique["array_key"].duplicated().any():
        raise NotIdentifiable(f"array-level state {column} differs within array")
    values = unique[column].to_numpy(dtype=float)
    mean = float(np.mean(values))
    sd = float(np.std(values, ddof=0))
    if not np.isfinite(sd) or sd <= 0:
        raise NotIdentifiable(f"zero/nonfinite training variance for array state {column}")
    return (train[column].to_numpy(dtype=float) - mean) / sd, (test[column].to_numpy(dtype=float) - mean) / sd


def _z_from_unique_plants(train: pd.DataFrame, test: pd.DataFrame, column: str) -> tuple[np.ndarray, np.ndarray]:
    unique = train[["plant_key", column]].drop_duplicates("plant_key")
    if unique["plant_key"].duplicated().any():
        raise NotIdentifiable(f"plant-level state {column} differs within plant")
    values = unique[column].to_numpy(dtype=float)
    mean = float(np.mean(values))
    sd = float(np.std(values, ddof=0))
    if not np.isfinite(sd) or sd <= 0:
        raise NotIdentifiable(f"zero/nonfinite training variance for plant state {column}")
    return (train[column].to_numpy(dtype=float) - mean) / sd, (test[column].to_numpy(dtype=float) - mean) / sd


def _categorical_columns(train: pd.DataFrame, test: pd.DataFrame, column: str) -> tuple[list[np.ndarray], list[np.ndarray], list[str]]:
    levels = sorted({_clean(v) for v in train[column] if _clean(v)})
    if not levels:
        raise NotIdentifiable(f"no levels for categorical {column}")
    test_levels = {_clean(v) for v in test[column] if _clean(v)}
    unseen = test_levels - set(levels)
    if unseen:
        raise NotIdentifiable(f"held-out unseen {column} levels: {sorted(unseen)}")
    tr_cols: list[np.ndarray] = []
    te_cols: list[np.ndarray] = []
    names: list[str] = []
    for level in levels[1:]:
        tr_cols.append(np.array([float(_clean(v) == level) for v in train[column]], dtype=float))
        te_cols.append(np.array([float(_clean(v) == level) for v in test[column]], dtype=float))
        names.append(f"{column}={level}")
    return tr_cols, te_cols, names


def _design(train: pd.DataFrame, test: pd.DataFrame, state: str, secondary: str | None = None) -> tuple[np.ndarray, np.ndarray, list[str]]:
    tr_parts: list[np.ndarray] = []
    te_parts: list[np.ndarray] = []
    names: list[str] = []

    tr_block, te_block, block_names = _categorical_columns(train, test, "block")
    tr_parts.extend(tr_block)
    te_parts.extend(te_block)
    names.extend(block_names)

    if state in {"S1", "S2", "S3"}:
        for col, name in (("I_log_count", "z_log1p_I_count"), ("T_mean_ITD", "z_T_mean_ITD")):
            tr_z, te_z = _z_from_unique_arrays(train, test, col)
            tr_parts.append(tr_z)
            te_parts.append(te_z)
            names.append(name)

    if state in {"S2", "S3"}:
        tr_h, te_h, h_names = _categorical_columns(train, test, "habitat")
        tr_parts.extend(tr_h)
        te_parts.extend(te_h)
        names.extend(h_names)

    if state == "S3":
        if secondary is None:
            raise ValueError("S3 requires secondary state coordinate")
        tr_z, te_z = _z_from_unique_plants(train, test, secondary)
        tr_parts.append(tr_z)
        te_parts.append(te_z)
        names.append(f"z_{secondary}")

    if tr_parts:
        x_train = np.column_stack(tr_parts)
        x_test = np.column_stack(te_parts)
    else:
        x_train = np.zeros((len(train), 0), dtype=float)
        x_test = np.zeros((len(test), 0), dtype=float)
    return x_train, x_test, names


def _fit_score_continuous(train: pd.DataFrame, test: pd.DataFrame, response: str, state: str, secondary: str | None = None) -> float:
    x_train, x_test, _ = _design(train, test, state, secondary)
    y_train = train[response].to_numpy(dtype=float)
    y_test = test[response].to_numpy(dtype=float)
    model = Ridge(alpha=1.0, fit_intercept=True)
    model.fit(x_train, y_train, sample_weight=_array_weights(train))
    pred = model.predict(x_test)
    return float(np.mean((y_test - pred) ** 2))


def _fit_score_binary(train: pd.DataFrame, test: pd.DataFrame, response: str, state: str, secondary: str | None = None) -> float:
    x_train, x_test, _ = _design(train, test, state, secondary)
    y_train = train[response].to_numpy(dtype=int)
    y_test = test[response].to_numpy(dtype=int)
    if set(np.unique(y_train)) != {0, 1}:
        raise NotIdentifiable("binary training fold lacks both classes")
    model = LogisticRegression(
        penalty="l2",
        C=1.0,
        solver="lbfgs",
        max_iter=10_000,
        fit_intercept=True,
        random_state=0,
    )
    model.fit(x_train, y_train, sample_weight=_array_weights(train))
    prob = np.clip(model.predict_proba(x_test)[:, 1], 1e-8, 1 - 1e-8)
    nll = -(y_test * np.log(prob) + (1 - y_test) * np.log(1 - prob))
    return float(np.mean(nll))


def _loao(df: pd.DataFrame, response: str, kind: str, *, secondary: str | None = None) -> dict[str, dict[str, float]]:
    arrays = sorted(df["array_key"].unique())
    if len(arrays) < 2:
        raise NotIdentifiable("too few arrays for LOAO")
    states = ["S0", "S1", "S2"] + (["S3"] if secondary is not None else [])
    per_state: dict[str, dict[str, float]] = {state: {} for state in states}
    for held in arrays:
        train = df[df["array_key"] != held].copy()
        test = df[df["array_key"] == held].copy()
        if test.empty:
            continue
        for state in states:
            sec = secondary if state == "S3" else None
            if kind == "continuous":
                score = _fit_score_continuous(train, test, response, state, sec)
            elif kind == "binary":
                score = _fit_score_binary(train, test, response, state, sec)
            else:
                raise ValueError(kind)
            per_state[state][str(held)] = score
    return per_state


def _mean_scores(per_state: dict[str, dict[str, float]]) -> dict[str, float]:
    return {state: float(np.mean(list(scores.values()))) for state, scores in per_state.items()}


def _bootstrap_gain(base: dict[str, float], aug: dict[str, float]) -> dict[str, object]:
    arrays = sorted(set(base) & set(aug))
    gains = np.array([base[a] - aug[a] for a in arrays], dtype=float)
    if len(gains) == 0:
        raise NotIdentifiable("no common arrays for score comparison")
    rng = np.random.default_rng(RNG_SEED)
    means = np.empty(N_BOOT, dtype=float)
    for i in range(N_BOOT):
        sample = rng.choice(gains, size=len(gains), replace=True)
        means[i] = float(np.mean(sample))
    observed = float(np.mean(gains))
    lo, hi = [float(x) for x in np.quantile(means, [0.025, 0.975])]
    return {
        "n_arrays": int(len(gains)),
        "mean_gain": observed,
        "ci95": [lo, hi],
        "supported_positive_gain": bool(observed > 0 and lo > 0),
        "permutations": N_BOOT,
        "rng_seed": RNG_SEED,
    }


def _endpoint_decision(comparisons: dict[str, dict[str, object]]) -> str:
    process = bool(comparisons["S0_to_S1"]["supported_positive_gain"])
    habitat = bool(comparisons["S1_to_S2"]["supported_positive_gain"])
    if habitat:
        return "residual_context_detected_after_process_state"
    if process:
        return "process_state_informative_no_detected_residual_context"
    return "process_state_not_predictively_supported"


def _run_primary_endpoint(df: pd.DataFrame, response: str, kind: str) -> EndpointResult:
    per = _loao(df, response, kind)
    comparisons = {
        "S0_to_S1": _bootstrap_gain(per["S0"], per["S1"]),
        "S1_to_S2": _bootstrap_gain(per["S1"], per["S2"]),
    }
    return EndpointResult(
        decision=_endpoint_decision(comparisons),
        model_scores=_mean_scores(per),
        per_array_scores=per,
        comparisons=comparisons,
        n_rows=int(len(df)),
        n_arrays=int(df["array_key"].nunique()),
        notes={},
    )


def _secondary_extension(df: pd.DataFrame, response: str, kind: str, secondary: str) -> dict[str, object]:
    if df[secondary].isna().any():
        return {"decision": "not_identifiable_secondary", "reason": f"missing {secondary} on comparison rows"}
    per = _loao(df, response, kind, secondary=secondary)
    gain = _bootstrap_gain(per["S2"], per["S3"])
    return {
        "decision": "supported_positive_gain" if gain["supported_positive_gain"] else "no_detected_positive_gain",
        "scores": _mean_scores({"S2": per["S2"], "S3": per["S3"]}),
        "comparison": gain,
        "n_rows": int(len(df)),
        "n_arrays": int(df["array_key"].nunique()),
    }


def _endpoint_to_dict(result: EndpointResult) -> dict[str, object]:
    return {
        "decision": result.decision,
        "model_scores_equal_array_weight": result.model_scores,
        "per_array_scores": result.per_array_scores,
        "comparisons": result.comparisons,
        "n_rows": result.n_rows,
        "n_arrays": result.n_arrays,
        "notes": result.notes,
    }


def run() -> dict[str, object]:
    source_info: dict[str, object] = {}
    frames: dict[str, pd.DataFrame] = {}
    for role, spec in SOURCES.items():
        package, raw, url = _download_source(spec)
        frames[role] = _read_csv(raw)
        source_info[role] = {
            "doi": spec["doi"],
            "url": url,
            "package_sha256": _sha256(package),
            "csv_member": spec["member"],
            "csv_sha256": _sha256(raw),
        }

    result: dict[str, object] = {
        "stage": "Eschscholzia californica multi-process natural state-sufficiency test",
        "source_lock": source_info,
        "preregistration": "manuscript/empirical_eschscholzia_multiprocess_test_preregistration.md",
        "bootstrap": {"replicates": N_BOOT, "rng_seed": RNG_SEED, "held_out_unit": "Experimental array"},
        "claim_boundary": (
            "Pan traps are array-level pollinator availability/community proxies, not direct focal-plant visitation. "
            "This is a partial natural-state predictive test, not a universal fragmentation threshold or causal habitat decomposition."
        ),
    }

    try:
        pstate = _prepare_pollinator(frames["pollinator"])
    except NotIdentifiable as exc:
        result["decision"] = "multi_endpoint_not_identifiable"
        result["reason"] = f"pollinator_state: {exc}"
        return result

    result["schema_counts"] = {
        "pollinator_rows": int(len(frames["pollinator"])),
        "pollinator_arrays": int(len(pstate)),
    }

    # F primary and capacity extension.
    f_result: dict[str, object]
    try:
        f = _prepare_f(frames["f_seed"], pstate)
        f_primary = _run_primary_endpoint(f, "y_F", "continuous")
        f_result = _endpoint_to_dict(f_primary)
        f_result["capacity_extension"] = _secondary_extension(f, "y_F", "continuous", "D_capacity")
        f_result["capacity_extension"]["semantic_decision"] = (
            "capacity_adds_function_information"
            if f_result["capacity_extension"].get("decision") == "supported_positive_gain"
            else "no_detected_capacity_gain"
            if f_result["capacity_extension"].get("decision") == "no_detected_positive_gain"
            else "capacity_not_identifiable"
        )
    except NotIdentifiable as exc:
        f_result = {"decision": "not_identifiable_for_endpoint", "reason": str(exc)}
    result["F_seed"] = f_result

    # R state preparation is independent of G primary.
    try:
        r = _prepare_r(frames["r_seed"], pstate)
        result["R_state"] = {"decision": "R_state_identified", "n_plants": int(r["plant_key"].nunique()), "n_arrays": int(r["array_key"].nunique())}
    except NotIdentifiable as exc:
        r = pd.DataFrame(columns=["plant_key", "array_key", "R_auto"])
        result["R_state"] = {"decision": "R_state_not_identifiable", "reason": str(exc)}

    # G primary, C secondary, and R extension.
    g_result: dict[str, object]
    c_result: dict[str, object]
    try:
        g, c, g_counts = _prepare_g(frames["g_paternity"], pstate)
        result["schema_counts"].update(g_counts)
        g_primary = _run_primary_endpoint(g, "G_outcross", "binary")
        g_result = _endpoint_to_dict(g_primary)

        if not r.empty:
            g_r = g.merge(r[["plant_key", "R_auto"]], on="plant_key", how="inner", validate="many_to_one")
            if g_r["array_key"].nunique() >= 2 and not g_r.empty:
                ext = _secondary_extension(g_r, "G_outcross", "binary", "R_auto")
                ext["semantic_decision"] = (
                    "R_adds_mating_state_information"
                    if ext.get("decision") == "supported_positive_gain"
                    else "no_detected_R_gain"
                    if ext.get("decision") == "no_detected_positive_gain"
                    else "R_gain_not_identifiable"
                )
                g_result["R_extension"] = ext
            else:
                g_result["R_extension"] = {"decision": "not_identifiable_secondary", "reason": "R-complete G subset too small"}
        else:
            g_result["R_extension"] = {"decision": "not_identifiable_secondary", "reason": "R state unavailable"}

        if c["array_key"].nunique() >= 8:
            c_primary = _run_primary_endpoint(c, "y_C", "continuous")
            c_result = _endpoint_to_dict(c_primary)
        else:
            c_result = {"decision": "C_not_identifiable", "n_rows": int(len(c)), "n_arrays": int(c["array_key"].nunique())}
    except NotIdentifiable as exc:
        g_result = {"decision": "not_identifiable_for_endpoint", "reason": str(exc)}
        c_result = {"decision": "C_not_identifiable", "reason": "G source preparation failed"}
    result["G_mating"] = g_result
    result["C_pollen"] = c_result

    f_dec = str(f_result.get("decision"))
    g_dec = str(g_result.get("decision"))
    if "not_identifiable" in f_dec or "not_identifiable" in g_dec:
        overall = "multi_endpoint_not_identifiable"
    elif "residual_context_detected_after_process_state" in {f_dec, g_dec}:
        overall = "multi_endpoint_state_insufficiency_detected"
    elif f_dec == g_dec == "process_state_informative_no_detected_residual_context":
        overall = "multi_endpoint_partial_state_convergence_supported"
    else:
        overall = "multi_endpoint_convergence_not_established"
    result["decision"] = overall
    result["primary_endpoint_decisions"] = {"F_seed": f_dec, "G_mating": g_dec}
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/eschscholzia_multiprocess_state_result.json")
    args = parser.parse_args()
    result = run()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "decision": result.get("decision"),
        "primary_endpoint_decisions": result.get("primary_endpoint_decisions"),
        "F_process": result.get("F_seed", {}).get("comparisons", {}).get("S0_to_S1"),
        "F_habitat": result.get("F_seed", {}).get("comparisons", {}).get("S1_to_S2"),
        "G_process": result.get("G_mating", {}).get("comparisons", {}).get("S0_to_S1"),
        "G_habitat": result.get("G_mating", {}).get("comparisons", {}).get("S1_to_S2"),
    }
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
