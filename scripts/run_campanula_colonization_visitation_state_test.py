from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RECORD_ID = 10814705
RNG_SEED = 20260825
N_BOOT = 10_000
USER_AGENT = "eco-genetic-warning-extensions/1.0"
FILES = {
    "seed": {
        "filename": "PLdataindividual.csv",
        "md5": "b84fa5c83513dbe75c0bf7840d1c74aa",
    },
    "pollinator": {
        "filename": "pollinator.csv",
        "md5": "81e0deaa78a6a97e1211484cb9d0d3b3",
    },
}

SEED_REQUIRED = {
    "source.population",
    "autonomy",
    "individual",
    "experimental.population",
    "site",
    "size",
    "dayfromstartofexperiment",
    "treatment",
    "seednumber",
}
POLL_REQUIRED = {
    "experimental.population",
    "site",
    "source population",
    "autonomy",
    "size",
    "visits.per.flower",
}


def _download(filename: str, expected_md5: str) -> tuple[str, bytes, str]:
    url = f"https://zenodo.org/records/{RECORD_ID}/files/{filename}?download=1"
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/csv,*/*"})
    with urlopen(req, timeout=180) as response:
        payload = response.read()
    observed = hashlib.md5(payload).hexdigest()
    if observed != expected_md5:
        raise RuntimeError(f"MD5 mismatch for {filename}: expected={expected_md5}, observed={observed}")
    return url, payload, hashlib.sha256(payload).hexdigest()


def _source_lock() -> tuple[dict[str, dict[str, str]], dict[str, pd.DataFrame]]:
    provenance: dict[str, dict[str, str]] = {}
    frames: dict[str, pd.DataFrame] = {}
    for role, spec in FILES.items():
        url, payload, sha256 = _download(spec["filename"], spec["md5"])
        provenance[role] = {
            "filename": spec["filename"],
            "md5": spec["md5"],
            "sha256": sha256,
            "download_url": url,
        }
        frames[role] = pd.read_csv(io.BytesIO(payload))
    return provenance, frames


def _clean_text(series: pd.Series) -> pd.Series:
    return series.astype("string").str.strip()


def _not_identifiable(source_lock: dict, reason: str, details: dict | None = None) -> dict:
    return {
        "stage": "Campanula experimental-colonization realised-visitation state test",
        "decision": "not_identifiable_for_primary_endpoint",
        "reason": reason,
        "details": details or {},
        "source_lock": source_lock,
        "bootstrap": {"replicates": N_BOOT, "rng_seed": RNG_SEED, "held_out_unit": "experimental.population"},
        "claim_boundary": (
            "No post-hoc treatment remapping, context spelling repair, alternate visitation metric, endpoint transformation, "
            "or validation scheme is opened after a preregistered identifiability gate fails."
        ),
    }


def _prepare(source_lock: dict, seed: pd.DataFrame, poll: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict] | dict:
    missing_seed = sorted(SEED_REQUIRED - set(seed.columns))
    missing_poll = sorted(POLL_REQUIRED - set(poll.columns))
    if missing_seed or missing_poll:
        return _not_identifiable(
            source_lock,
            "required_columns_missing",
            {"seed_missing": missing_seed, "pollinator_missing": missing_poll},
        )

    seed = seed.copy()
    poll = poll.copy()
    for col in ["experimental.population", "site", "source.population", "autonomy", "size", "individual", "treatment"]:
        seed[col] = _clean_text(seed[col])
    for col in ["experimental.population", "site", "source population", "autonomy", "size"]:
        poll[col] = _clean_text(poll[col])

    if poll["experimental.population"].isna().any() or poll["experimental.population"].duplicated().any():
        duplicates = sorted(poll.loc[poll["experimental.population"].duplicated(keep=False), "experimental.population"].dropna().unique().tolist())
        return _not_identifiable(source_lock, "pollinator_population_not_unique", {"duplicate_populations": duplicates})

    # Population-level context must be internally constant in the seed table.
    for col in ["site", "source.population", "autonomy", "size"]:
        counts = seed.groupby("experimental.population", dropna=False)[col].nunique(dropna=False)
        bad = counts[counts != 1]
        if not bad.empty:
            return _not_identifiable(
                source_lock,
                "seed_population_context_not_constant",
                {"column": col, "populations": [str(x) for x in bad.index.tolist()]},
            )

    seed_context = (
        seed.groupby("experimental.population", as_index=False)
        .agg({"site": "first", "source.population": "first", "autonomy": "first", "size": "first"})
    )
    poll_context = poll[["experimental.population", "site", "source population", "autonomy", "size"]].copy()
    merged_context = seed_context.merge(poll_context, on="experimental.population", how="outer", suffixes=("_seed", "_poll"), indicator=True)
    if not (merged_context["_merge"] == "both").all():
        bad = merged_context.loc[merged_context["_merge"] != "both", ["experimental.population", "_merge"]]
        return _not_identifiable(source_lock, "population_key_mismatch_between_sources", {"rows": bad.astype(str).to_dict("records")})

    comparisons = [
        ("site_seed", "site_poll", "site"),
        ("source.population", "source population", "source.population"),
        ("autonomy_seed", "autonomy_poll", "autonomy"),
        ("size_seed", "size_poll", "size"),
    ]
    for left, right, label in comparisons:
        mismatch = merged_context[left].astype("string") != merged_context[right].astype("string")
        mismatch = mismatch.fillna(True)
        if mismatch.any():
            bad = merged_context.loc[mismatch, ["experimental.population", left, right]]
            return _not_identifiable(
                source_lock,
                "population_context_mismatch_between_sources",
                {"column": label, "rows": bad.astype(str).to_dict("records")},
            )

    seed["dayfromstartofexperiment"] = pd.to_numeric(seed["dayfromstartofexperiment"], errors="coerce")
    seed["seednumber"] = pd.to_numeric(seed["seednumber"], errors="coerce")
    poll["visits.per.flower"] = pd.to_numeric(poll["visits.per.flower"], errors="coerce")

    if poll["visits.per.flower"].isna().any() or (~np.isfinite(poll["visits.per.flower"].to_numpy(dtype=float))).any():
        bad = poll.loc[poll["visits.per.flower"].isna() | ~np.isfinite(poll["visits.per.flower"].to_numpy(dtype=float)), "experimental.population"].astype(str).tolist()
        return _not_identifiable(source_lock, "nonfinite_visits_per_flower", {"populations": bad})

    # Fixed treatment classification.
    lower = seed["treatment"].str.lower()
    seed["treatment_class"] = np.where(
        lower.str.contains("control", na=False),
        "control",
        np.where(lower.str.contains("supp", na=False), "supplemented", pd.NA),
    )

    # Individuals with nonconstant timing across treatment rows are excluded only from paired endpoints.
    timing_counts = seed.groupby(["experimental.population", "individual"], dropna=False)["dayfromstartofexperiment"].nunique(dropna=False)
    bad_timing_keys = set(timing_counts[timing_counts != 1].index.tolist())
    seed["timing_valid"] = [
        (pop, ind) not in bad_timing_keys and pd.notna(day)
        for pop, ind, day in zip(seed["experimental.population"], seed["individual"], seed["dayfromstartofexperiment"], strict=True)
    ]

    classified = seed[seed["treatment_class"].notna() & seed["seednumber"].notna() & seed["timing_valid"]].copy()
    if classified.empty:
        return _not_identifiable(source_lock, "no_valid_control_or_supplemented_rows")

    aggregated = (
        classified.groupby(
            ["experimental.population", "individual", "site", "source.population", "autonomy", "size", "dayfromstartofexperiment", "treatment_class"],
            as_index=False,
            dropna=False,
        )["seednumber"]
        .mean()
    )
    wide = aggregated.pivot_table(
        index=["experimental.population", "individual", "site", "source.population", "autonomy", "size", "dayfromstartofexperiment"],
        columns="treatment_class",
        values="seednumber",
        aggfunc="first",
    ).reset_index()
    if "control" not in wide.columns or "supplemented" not in wide.columns:
        return _not_identifiable(source_lock, "paired_treatment_classes_absent", {"columns": [str(x) for x in wide.columns]})

    paired = wide[wide["control"].notna() & wide["supplemented"].notna()].copy()
    paired["PL_abs"] = paired["supplemented"] - paired["control"]
    paired["F_control"] = paired["control"]
    paired = paired.merge(
        poll[["experimental.population", "visits.per.flower"]], on="experimental.population", how="left", validate="many_to_one"
    )

    valid_populations = sorted(paired["experimental.population"].dropna().unique().tolist())
    if len(valid_populations) < 8 or len(paired) < 20:
        return _not_identifiable(
            source_lock,
            "insufficient_paired_primary_sample",
            {"n_populations": len(valid_populations), "n_individuals": len(paired)},
        )

    diagnostics = {
        "n_seed_rows": int(len(seed)),
        "n_pollinator_rows": int(len(poll)),
        "n_paired_individuals": int(len(paired)),
        "n_valid_populations": int(len(valid_populations)),
        "excluded_nonconstant_timing_individuals": int(len(bad_timing_keys)),
    }
    return paired, poll, diagnostics


STATE_FEATURES = {
    "S0": ["site", "source.population", "dayfromstartofexperiment"],
    "S1": ["site", "source.population", "dayfromstartofexperiment", "visits.per.flower"],
    "S2": ["site", "source.population", "dayfromstartofexperiment", "visits.per.flower", "size"],
    "S3": ["site", "source.population", "dayfromstartofexperiment", "visits.per.flower", "size", "autonomy"],
}
CATEGORICAL = {"site", "source.population", "size", "autonomy"}
NUMERIC = {"dayfromstartofexperiment", "visits.per.flower"}


def _pipeline(features: list[str]) -> Pipeline:
    cats = [f for f in features if f in CATEGORICAL]
    nums = [f for f in features if f in NUMERIC]
    transformers = []
    if cats:
        transformers.append(("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cats))
    if nums:
        transformers.append(("num", StandardScaler(), nums))
    pre = ColumnTransformer(transformers=transformers, remainder="drop")
    return Pipeline([("pre", pre), ("model", Ridge(alpha=1.0))])


def _lopo(data: pd.DataFrame, response: str) -> dict:
    populations = sorted(data["experimental.population"].unique().tolist())
    per_state: dict[str, dict[str, float]] = {state: {} for state in STATE_FEATURES}
    row_predictions: dict[str, list[dict]] = {state: [] for state in STATE_FEATURES}
    for held in populations:
        train = data[data["experimental.population"] != held].copy()
        test = data[data["experimental.population"] == held].copy()
        for state, features in STATE_FEATURES.items():
            model = _pipeline(features)
            model.fit(train[features], train[response].astype(float))
            pred = model.predict(test[features])
            obs = test[response].to_numpy(dtype=float)
            mse = float(np.mean((obs - pred) ** 2))
            per_state[state][str(held)] = mse
            for idx, observed, predicted in zip(test.index, obs, pred, strict=True):
                row_predictions[state].append(
                    {
                        "index": int(idx),
                        "experimental_population": str(held),
                        "observed": float(observed),
                        "predicted": float(predicted),
                    }
                )
    return {
        "population_mse": per_state,
        "mean_mse": {state: float(np.mean(list(scores.values()))) for state, scores in per_state.items()},
        "n_populations": len(populations),
        "n_individuals": int(len(data)),
        "predictions": row_predictions,
    }


def _bootstrap_gain(scores_a: dict[str, float], scores_b: dict[str, float]) -> dict:
    keys = sorted(set(scores_a) & set(scores_b))
    gains = np.array([float(scores_a[k]) - float(scores_b[k]) for k in keys], dtype=float)
    rng = np.random.default_rng(RNG_SEED)
    boot = np.empty(N_BOOT, dtype=float)
    n = len(gains)
    for i in range(N_BOOT):
        idx = rng.integers(0, n, size=n)
        boot[i] = float(np.mean(gains[idx]))
    lo, hi = np.quantile(boot, [0.025, 0.975])
    return {
        "mean_gain": float(np.mean(gains)),
        "ci95": [float(lo), float(hi)],
        "n_populations": n,
        "bootstrap_replicates": N_BOOT,
        "rng_seed": RNG_SEED,
        "supported_positive_gain": bool(lo > 0),
    }


def _endpoint_result(data: pd.DataFrame, response: str) -> dict:
    fitted = _lopo(data, response)
    p = fitted["population_mse"]
    comparisons = {
        "S0_to_S1": _bootstrap_gain(p["S0"], p["S1"]),
        "S1_to_S2": _bootstrap_gain(p["S1"], p["S2"]),
        "S2_to_S3": _bootstrap_gain(p["S2"], p["S3"]),
    }
    return {
        "response": response,
        "mean_mse": fitted["mean_mse"],
        "n_populations": fitted["n_populations"],
        "n_individuals": fitted["n_individuals"],
        "comparisons": comparisons,
    }


def _primary_decision(endpoint: dict) -> str:
    c = endpoint["comparisons"]
    process = bool(c["S0_to_S1"]["supported_positive_gain"])
    size = bool(c["S1_to_S2"]["supported_positive_gain"])
    autonomy = bool(c["S2_to_S3"]["supported_positive_gain"])
    if autonomy:
        return "residual_compensation_after_context"
    if size:
        return "residual_colonization_size_after_visitation"
    if process:
        return "realised_visitation_informative_context_redundant"
    return "realised_visitation_not_predictively_supported"


def run() -> dict:
    source_lock, frames = _source_lock()
    prepared = _prepare(source_lock, frames["seed"], frames["pollinator"])
    if isinstance(prepared, dict):
        return prepared
    paired, _poll, diagnostics = prepared

    primary = _endpoint_result(paired, "PL_abs")
    secondary = _endpoint_result(paired, "F_control")
    decision = _primary_decision(primary)
    return {
        "stage": "Campanula experimental-colonization realised-visitation state test",
        "decision": decision,
        "source_lock": source_lock,
        "diagnostics": diagnostics,
        "state_sequence": {
            "S0": "site + source.population + z(dayfromstartofexperiment)",
            "S1": "S0 + z(visits.per.flower)",
            "S2": "S1 + size",
            "S3": "S2 + autonomy",
        },
        "bootstrap": {"replicates": N_BOOT, "rng_seed": RNG_SEED, "held_out_unit": "experimental.population"},
        "PL_abs": primary,
        "F_control": secondary,
        "claim_boundary": (
            "Population-level realised visitation is tested as a predictor, not assumed sufficient. The dataset does not measure "
            "stigma pollen receipt, pollen quality, donor identity or genetics."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/campanula_colonization_visitation_result.json")
    args = parser.parse_args()
    result = run()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "decision": result.get("decision"),
                "reason": result.get("reason"),
                "PL_process": result.get("PL_abs", {}).get("comparisons", {}).get("S0_to_S1"),
                "PL_size": result.get("PL_abs", {}).get("comparisons", {}).get("S1_to_S2"),
                "PL_autonomy": result.get("PL_abs", {}).get("comparisons", {}).get("S2_to_S3"),
                "F_process": result.get("F_control", {}).get("comparisons", {}).get("S0_to_S1"),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
