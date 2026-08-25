from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

RECORD_ID = 4969330
DRYAD_DOI = "10.5061/dryad.5nj81nf"
FILE_NAME = "Koski et al. 2018_Data_ProcRoySoc.xlsx"
EXPECTED_MD5 = "2d26307743e8a22384781854b8f2f33b"
EXPECTED_SHA256 = "b81b77248b75330049e1ddd8ae026db127f838e979620a0415a5addb9a7e8f27"
SHEET = "PopVis Rates_ PL_Depletion"
RNG_SEED = 20260825
N_BOOT = 10_000
USER_AGENT = "eco-genetic-warning-extensions/1.0"

POPULATION_COLUMN = "Population"
RESPONSE_COLUMN = "Pollen Limitation 2016"

RAW_COLUMNS = [
    "Bumblebee Rate",
    "Megachile Rate",
    "Small Rate",
]
PHASE_COLUMNS = [
    "Bumble Female Rate",
    "Megachile Female Rate",
    "Small Female Rate",
    "Bumble Male Rate",
    "Megachile Male Rate",
    "Small Male Rate",
]
EFFECTIVE_COLUMNS = [
    "Bumble Grains Dep Per Hour",
    "Mega Grains Dep Per Hour",
    "Small Grains Dep Per Hour",
    "Bumble Grains Rem Per Hour",
    "Mega Grains Rem Per Hour",
    "Small Grains Rem Per Hour",
]
ALL_NUMERIC = [RESPONSE_COLUMN, *RAW_COLUMNS, *PHASE_COLUMNS, *EFFECTIVE_COLUMNS]


def _download() -> tuple[str, bytes]:
    encoded = quote(FILE_NAME)
    url = f"https://zenodo.org/records/{RECORD_ID}/files/{encoded}?download=1"
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream,*/*",
        },
    )
    with urlopen(req, timeout=180) as response:
        payload = response.read()
    md5 = hashlib.md5(payload).hexdigest()
    sha256 = hashlib.sha256(payload).hexdigest()
    if md5 != EXPECTED_MD5:
        raise RuntimeError(f"source MD5 mismatch: expected={EXPECTED_MD5}, observed={md5}")
    if sha256 != EXPECTED_SHA256:
        raise RuntimeError(f"source SHA256 mismatch: expected={EXPECTED_SHA256}, observed={sha256}")
    return url, payload


def _load_population_sheet(payload: bytes) -> pd.DataFrame:
    frame = pd.read_excel(io.BytesIO(payload), sheet_name=SHEET, engine="openpyxl")
    if len(frame) != 23:
        raise RuntimeError(f"expected exactly 23 population rows, observed={len(frame)}")

    required = {POPULATION_COLUMN, *ALL_NUMERIC}
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise RuntimeError(f"locked columns absent: {missing}; columns={list(frame.columns)}")

    population = frame[POPULATION_COLUMN].astype("string").str.strip()
    if population.isna().any() or (population == "").any():
        raise RuntimeError("blank population identifier")
    if population.duplicated().any():
        duplicates = population[population.duplicated(keep=False)].tolist()
        raise RuntimeError(f"duplicate population identifiers: {duplicates}")
    frame = frame.copy()
    frame[POPULATION_COLUMN] = population.astype(str)

    for column in ALL_NUMERIC:
        numeric = pd.to_numeric(frame[column], errors="coerce")
        if numeric.isna().any() or not np.isfinite(numeric.to_numpy(dtype=float)).all():
            raise RuntimeError(f"non-finite locked value in column {column!r}")
        frame[column] = numeric.astype(float)

    if len(frame) < 20:
        raise RuntimeError(f"fewer than 20 populations remain: n={len(frame)}")
    return frame


def _ridge() -> Pipeline:
    return Pipeline(
        [
            ("scale", StandardScaler()),
            ("ridge", Ridge(alpha=1.0)),
        ]
    )


def _lopo(frame: pd.DataFrame) -> dict[str, object]:
    y = frame[RESPONSE_COLUMN].to_numpy(dtype=float)
    feature_sets = {
        "M_raw": RAW_COLUMNS,
        "M_phase": PHASE_COLUMNS,
        "M_effective": EFFECTIVE_COLUMNS,
    }
    squared_errors: dict[str, list[float]] = {
        "M0": [],
        "M_raw": [],
        "M_phase": [],
        "M_effective": [],
    }

    n = len(frame)
    for held in range(n):
        train_idx = np.array([i for i in range(n) if i != held], dtype=int)
        test_idx = np.array([held], dtype=int)
        y_train = y[train_idx]
        y_test = float(y[test_idx][0])

        mean_prediction = float(np.mean(y_train))
        squared_errors["M0"].append(float((y_test - mean_prediction) ** 2))

        for label, columns in feature_sets.items():
            x = frame[columns].to_numpy(dtype=float)
            model = _ridge()
            model.fit(x[train_idx], y_train)
            prediction = float(model.predict(x[test_idx])[0])
            squared_errors[label].append(float((y_test - prediction) ** 2))

    mse = {label: float(np.mean(values)) for label, values in squared_errors.items()}
    return {"mse": mse, "squared_errors": squared_errors}


def _bootstrap_gain(gains: np.ndarray) -> dict[str, object]:
    n = gains.size
    # The preregistration fixes the same seed for every contrast. Reinitializing
    # here also applies the same bootstrap population-index draws to every paired
    # contrast, which preserves comparability across representations.
    rng = np.random.default_rng(RNG_SEED)
    samples = rng.integers(0, n, size=(N_BOOT, n))
    boot = gains[samples].mean(axis=1)
    ci_low, ci_high = np.quantile(boot, [0.025, 0.975])
    mean_gain = float(np.mean(gains))
    return {
        "mean_gain": mean_gain,
        "ci95": [float(ci_low), float(ci_high)],
        "supported_positive_gain": bool(ci_low > 0),
        "n_populations": int(n),
        "bootstrap_replicates": N_BOOT,
        "rng_seed": RNG_SEED,
    }


def _comparisons(squared_errors: dict[str, list[float]]) -> dict[str, object]:
    arrays = {key: np.asarray(value, dtype=float) for key, value in squared_errors.items()}
    contrast_defs = {
        "raw_adequacy": ("M0", "M_raw"),
        "phase_adequacy": ("M0", "M_phase"),
        "effective_adequacy": ("M0", "M_effective"),
        "phase_gain_over_raw": ("M_raw", "M_phase"),
        "effective_gain_over_raw": ("M_raw", "M_effective"),
        "effective_gain_over_phase": ("M_phase", "M_effective"),
    }
    result: dict[str, object] = {}
    for name, (smaller, larger) in contrast_defs.items():
        gains = arrays[smaller] - arrays[larger]
        result[name] = _bootstrap_gain(gains)
    return result


def _decision(comparisons: dict[str, object]) -> tuple[str, dict[str, bool]]:
    flags = {
        "raw_supported": bool(comparisons["raw_adequacy"]["supported_positive_gain"]),
        "phase_supported": bool(comparisons["phase_adequacy"]["supported_positive_gain"]),
        "effective_supported": bool(comparisons["effective_adequacy"]["supported_positive_gain"]),
        "effective_over_raw": bool(comparisons["effective_gain_over_raw"]["supported_positive_gain"]),
    }
    if flags["effective_supported"] and flags["effective_over_raw"]:
        label = "effective_interaction_supported_over_raw"
    elif flags["effective_supported"]:
        label = "effective_interaction_supported_no_gain_over_raw"
    elif flags["phase_supported"]:
        label = "phase_matched_visitation_supported_no_effective_support"
    elif flags["raw_supported"]:
        label = "raw_visitation_supported_no_effective_support"
    else:
        label = "no_interaction_representation_supported"
    return label, flags


def run() -> dict[str, object]:
    url, payload = _download()
    frame = _load_population_sheet(payload)
    lopo = _lopo(frame)
    comparisons = _comparisons(lopo["squared_errors"])
    decision, flags = _decision(comparisons)

    return {
        "stage": "Campanula americana effective-interaction predictive adequacy",
        "decision": decision,
        "flags": flags,
        "source_lock": {
            "dryad_doi": DRYAD_DOI,
            "zenodo_record": RECORD_ID,
            "filename": FILE_NAME,
            "download_url": url,
            "md5": hashlib.md5(payload).hexdigest(),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "sheet": SHEET,
        },
        "sample": {
            "n_populations": len(frame),
            "population_column": POPULATION_COLUMN,
            "response": RESPONSE_COLUMN,
        },
        "representations": {
            "M0": {"columns": [], "model": "training response mean"},
            "M_raw": {"columns": RAW_COLUMNS, "model": "StandardScaler + Ridge(alpha=1.0)"},
            "M_phase": {"columns": PHASE_COLUMNS, "model": "StandardScaler + Ridge(alpha=1.0)"},
            "M_effective": {"columns": EFFECTIVE_COLUMNS, "model": "StandardScaler + Ridge(alpha=1.0)"},
        },
        "lopo_mse": lopo["mse"],
        "comparisons": comparisons,
        "bootstrap": {
            "held_out_unit": "Population",
            "replicates": N_BOOT,
            "rng_seed": RNG_SEED,
            "note": "each contrast reinitializes the same fixed seed and therefore uses identical bootstrap population-index draws",
        },
        "claim_boundary": (
            "This test evaluates predictive adequacy of source-defined raw, phase-matched, and independently "
            "efficiency-calibrated pollinator representations for population pollen limitation. It does not identify "
            "a universal pollinator-size rule, universal threshold, or complete eco-genetic state."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/empirical/campanula_effective_interaction_result.json",
    )
    args = parser.parse_args()
    try:
        result = run()
    except Exception as exc:
        result = {
            "stage": "Campanula americana effective-interaction predictive adequacy",
            "decision": "not_identifiable_for_primary_endpoint",
            "reason": f"{type(exc).__name__}: {exc}",
            "bootstrap": {
                "held_out_unit": "Population",
                "replicates": N_BOOT,
                "rng_seed": RNG_SEED,
            },
        }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "decision": result.get("decision"),
        "reason": result.get("reason"),
        "mse": result.get("lopo_mse"),
        "comparisons": result.get("comparisons"),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
