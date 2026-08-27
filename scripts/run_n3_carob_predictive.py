from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import urllib.request
import warnings
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.special import gammaln
from statsmodels.discrete.discrete_model import NegativeBinomial

RECORD_ID = 13939480
RECORD_URL = f"https://zenodo.org/api/records/{RECORD_ID}"
TARGET_FILE = "Dataset_CarobTree.xlsx"
CONTRACT_PATH = Path("configs/n3_carob_predictive_contract.json")
BOOTSTRAP_SEED = 20260827
BOOTSTRAP_N = 10000
REPS = {
    "embedded": "I_embedded",
    "joined": "I_joined",
}


def _request(url: str, *, json_only: bool = False) -> urllib.request.Request:
    return urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
            "Accept": "application/json" if json_only else "application/octet-stream,*/*;q=0.8",
        },
    )


def _get_json(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(_request(url, json_only=True), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def acquire_workbook() -> tuple[bytes, dict[str, Any]]:
    record = _get_json(RECORD_URL)
    files = {str(item.get("key")): item for item in record.get("files", [])}
    if TARGET_FILE not in files:
        raise RuntimeError(f"{TARGET_FILE} missing from Zenodo record")
    item = files[TARGET_FILE]
    url = item.get("links", {}).get("content") or item.get("links", {}).get("self")
    if not url:
        raise RuntimeError("Zenodo workbook lacks content URL")
    with urllib.request.urlopen(_request(str(url)), timeout=120) as response:
        payload = response.read()
        transfer = {
            "status": int(response.status),
            "bytes": len(payload),
            "final_url": response.geturl(),
        }
    checksum = str(item.get("checksum", ""))
    md5 = hashlib.md5(payload).hexdigest()
    expected = checksum.split(":", 1)[1] if checksum.startswith("md5:") else None
    if expected is not None and md5 != expected:
        raise RuntimeError(f"Zenodo checksum mismatch: {md5} != {expected}")
    return payload, {
        "record_id": RECORD_ID,
        "doi": record.get("doi"),
        "file": TARGET_FILE,
        "md5": md5,
        "checksum_verified": expected is None or md5 == expected,
        "transfer": transfer,
    }


def _year_string(value: object) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        raise RuntimeError("missing Year")
    try:
        numeric = float(value)
        if numeric.is_integer():
            return str(int(numeric))
    except (TypeError, ValueError):
        pass
    return str(value).strip()


def prepare_orchard_year_frame(payload: bytes) -> tuple[pd.DataFrame, dict[str, Any]]:
    sheets = pd.read_excel(
        io.BytesIO(payload),
        sheet_name=["FruitProduction", "PollinatorAbundance"],
        engine="openpyxl",
    )
    fruit = sheets["FruitProduction"].copy()
    poll = sheets["PollinatorAbundance"].copy()
    required_fruit = {
        "StudyOrchard", "Year", "Tree", "TotalFlowers", "TotalFruits",
        "PolinAbun", "Pnatur1k", "FarmSys", "ratMF",
    }
    required_poll = {"StudyOrchard", "Year", "PolinAbun"}
    miss_fruit = sorted(required_fruit - set(fruit.columns))
    miss_poll = sorted(required_poll - set(poll.columns))
    if miss_fruit or miss_poll:
        raise RuntimeError(f"missing source columns fruit={miss_fruit}, poll={miss_poll}")

    fruit["StudyOrchard"] = fruit["StudyOrchard"].astype(str).str.strip()
    poll["StudyOrchard"] = poll["StudyOrchard"].astype(str).str.strip()
    fruit["Year"] = fruit["Year"].map(_year_string)
    poll["Year"] = poll["Year"].map(_year_string)
    fruit["FarmSys"] = fruit["FarmSys"].astype(str).str.strip()

    numeric_fruit = ["TotalFlowers", "TotalFruits", "PolinAbun", "Pnatur1k", "ratMF"]
    for col in numeric_fruit:
        fruit[col] = pd.to_numeric(fruit[col], errors="raise")
    poll["PolinAbun"] = pd.to_numeric(poll["PolinAbun"], errors="raise")

    if fruit[list(required_fruit)].isna().any().any():
        raise RuntimeError("missing required FruitProduction values despite frozen Stage-A contract")
    if poll[list(required_poll)].isna().any().any():
        raise RuntimeError("missing required PollinatorAbundance values")
    if (fruit["TotalFlowers"] <= 0).any() or (fruit["TotalFruits"] < 0).any():
        raise RuntimeError("invalid fruit count/exposure values")
    if not np.allclose(fruit["TotalFruits"], np.round(fruit["TotalFruits"]), atol=1e-9):
        raise RuntimeError("TotalFruits is not integer-valued; frozen NB count endpoint is invalid")

    key_cols = ["StudyOrchard", "Year"]
    for col in ["PolinAbun", "Pnatur1k", "FarmSys", "ratMF"]:
        max_nunique = int(fruit.groupby(key_cols, sort=False)[col].nunique(dropna=False).max())
        if max_nunique != 1:
            raise RuntimeError(f"{col} is not constant within orchard-year")

    grouped = fruit.groupby(key_cols, as_index=False, sort=True).agg(
        fruit_count=("TotalFruits", "sum"),
        flower_exposure=("TotalFlowers", "sum"),
        I_embedded=("PolinAbun", "first"),
        Pnatur1k=("Pnatur1k", "first"),
        FarmSys=("FarmSys", "first"),
        ratMF=("ratMF", "first"),
        tree_rows=("Tree", "size"),
    )

    poll_dupes = poll.duplicated(key_cols, keep=False)
    if bool(poll_dupes.any()):
        raise RuntimeError("PollinatorAbundance has duplicate orchard-year keys")
    poll_key = poll[key_cols + ["PolinAbun"]].rename(columns={"PolinAbun": "I_joined"})
    frame = grouped.merge(poll_key, on=key_cols, how="left", validate="many_to_one")
    if frame["I_joined"].isna().any():
        raise RuntimeError("at least one production orchard-year lacks joined PolinAbun")

    frame["I_embedded"] = frame["I_embedded"] / 15.0
    frame["I_joined"] = frame["I_joined"] / 15.0
    frame["fruit_count"] = frame["fruit_count"].astype(float)
    frame["flower_exposure"] = frame["flower_exposure"].astype(float)

    audit = {
        "tree_rows": int(len(fruit)),
        "orchard_year_rows": int(len(frame)),
        "orchard_count": int(frame["StudyOrchard"].nunique()),
        "years": sorted(frame["Year"].unique().tolist()),
        "farm_levels": sorted(frame["FarmSys"].astype(str).unique().tolist()),
        "interaction_representations_equal_key_count": int(
            np.isclose(frame["I_embedded"], frame["I_joined"], rtol=0.0, atol=0.0).sum()
        ),
        "interaction_representations_different_key_count": int(
            (~np.isclose(frame["I_embedded"], frame["I_joined"], rtol=0.0, atol=0.0)).sum()
        ),
    }
    if audit["orchard_count"] != 20 or audit["orchard_year_rows"] != 37:
        raise RuntimeError(f"frozen Stage-A dimensions changed: {audit}")
    return frame, audit


def _add_categorical(
    train: pd.DataFrame,
    test: pd.DataFrame,
    column: str,
    train_parts: list[np.ndarray],
    test_parts: list[np.ndarray],
    names: list[str],
) -> tuple[list[str], str]:
    train_values = train[column].astype(str)
    test_values = test[column].astype(str)
    levels = sorted(train_values.unique().tolist())
    unseen = sorted(set(test_values.unique()) - set(levels))
    if unseen:
        raise RuntimeError(f"unseen held-out category for {column}: {unseen}")
    if not levels:
        raise RuntimeError(f"no levels for {column}")
    reference = levels[0]
    encoded = []
    for level in levels[1:]:
        train_col = (train_values.to_numpy() == level).astype(float)
        test_col = (test_values.to_numpy() == level).astype(float)
        train_parts.append(train_col[:, None])
        test_parts.append(test_col[:, None])
        names.append(f"{column}[{level}]")
        encoded.append(level)
    return encoded, reference


def _zscore(train: pd.DataFrame, test: pd.DataFrame, column: str) -> tuple[np.ndarray, np.ndarray]:
    mean = float(train[column].mean())
    sd = float(train[column].std(ddof=0))
    if not math.isfinite(sd) or sd <= 0:
        raise RuntimeError(f"training-fold predictor has zero/nonfinite SD: {column}")
    return (
        (train[column].to_numpy(dtype=float) - mean) / sd,
        (test[column].to_numpy(dtype=float) - mean) / sd,
    )


def design_matrices(
    train: pd.DataFrame,
    test: pd.DataFrame,
    *,
    interaction_column: str,
    kind: str,
) -> tuple[np.ndarray, np.ndarray, list[str]]:
    if kind not in {"baseline", "process", "context"}:
        raise ValueError(kind)
    train_parts = [np.ones((len(train), 1), dtype=float)]
    test_parts = [np.ones((len(test), 1), dtype=float)]
    names = ["intercept"]
    _add_categorical(train, test, "Year", train_parts, test_parts, names)

    if kind in {"process", "context"}:
        zi_train, zi_test = _zscore(train, test, interaction_column)
        train_parts.append(zi_train[:, None])
        test_parts.append(zi_test[:, None])
        names.append("z(I_visit)")

    if kind == "context":
        zp_train, zp_test = _zscore(train, test, "Pnatur1k")
        zr_train, zr_test = _zscore(train, test, "ratMF")
        train_parts.append(zp_train[:, None])
        test_parts.append(zp_test[:, None])
        names.append("z(Pnatur1k)")

        farm_train_parts_before = len(train_parts)
        farm_levels, _ = _add_categorical(train, test, "FarmSys", train_parts, test_parts, names)
        farm_train_cols = train_parts[farm_train_parts_before:]
        farm_test_cols = test_parts[farm_train_parts_before:]

        train_parts.append(zr_train[:, None])
        test_parts.append(zr_test[:, None])
        names.append("z(ratMF)")
        train_parts.append((zr_train ** 2)[:, None])
        test_parts.append((zr_test ** 2)[:, None])
        names.append("z(ratMF)^2")

        for level, f_train, f_test in zip(farm_levels, farm_train_cols, farm_test_cols):
            train_parts.append((zp_train * f_train[:, 0])[:, None])
            test_parts.append((zp_test * f_test[:, 0])[:, None])
            names.append(f"z(Pnatur1k):FarmSys[{level}]")

    return np.hstack(train_parts), np.hstack(test_parts), names


def _nb2_nll(y: np.ndarray, mu: np.ndarray, alpha: float) -> np.ndarray:
    if not math.isfinite(alpha) or alpha <= 0:
        raise RuntimeError(f"invalid NB2 alpha: {alpha}")
    if np.any(mu <= 0) or not np.all(np.isfinite(mu)):
        raise RuntimeError("nonpositive/nonfinite held-out NB2 mean")
    size = 1.0 / alpha
    log_p = -np.log1p(alpha * mu)
    log_one_minus_p = np.log(alpha * mu) - np.log1p(alpha * mu)
    logpmf = (
        gammaln(y + size)
        - gammaln(size)
        - gammaln(y + 1.0)
        + size * log_p
        + y * log_one_minus_p
    )
    if not np.all(np.isfinite(logpmf)):
        raise RuntimeError("nonfinite held-out NB2 log likelihood")
    return -logpmf


def fit_and_score(
    train: pd.DataFrame,
    test: pd.DataFrame,
    *,
    interaction_column: str,
    kind: str,
) -> tuple[np.ndarray, list[str], float]:
    x_train, x_test, names = design_matrices(
        train, test, interaction_column=interaction_column, kind=kind
    )
    y_train = train["fruit_count"].to_numpy(dtype=float)
    y_test = test["fruit_count"].to_numpy(dtype=float)
    offset_train = np.log(train["flower_exposure"].to_numpy(dtype=float))
    offset_test = np.log(test["flower_exposure"].to_numpy(dtype=float))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fit = NegativeBinomial(
            y_train,
            x_train,
            loglike_method="nb2",
            offset=offset_train,
            check_rank=True,
        ).fit(method="bfgs", maxiter=500, disp=0)
    converged = bool(getattr(fit, "mle_retvals", {}).get("converged", False))
    params = np.asarray(fit.params, dtype=float)
    if not converged:
        raise RuntimeError(f"NB2 {kind} model did not converge")
    if len(params) != x_train.shape[1] + 1 or not np.all(np.isfinite(params)):
        raise RuntimeError(f"NB2 {kind} returned invalid parameter vector")
    beta = params[:-1]
    alpha = float(params[-1])
    linear = x_test @ beta + offset_test
    if not np.all(np.isfinite(linear)) or np.any(linear > 700):
        raise RuntimeError("nonfinite/overflow held-out linear predictor")
    mu = np.exp(linear)
    return _nb2_nll(y_test, mu, alpha), names, alpha


def _bootstrap_summary(deltas: np.ndarray) -> tuple[float, list[float]]:
    total = float(deltas.sum())
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    draws = rng.choice(deltas, size=(BOOTSTRAP_N, len(deltas)), replace=True).sum(axis=1)
    low, high = np.quantile(draws, [0.025, 0.975])
    return total, [float(low), float(high)]


def compare_models(
    frame: pd.DataFrame,
    *,
    representation: str,
    restricted_kind: str,
    full_kind: str,
    detected_label: str,
    no_detected_label: str,
) -> dict[str, Any]:
    interaction_column = REPS[representation]
    records = []
    first_columns: dict[str, list[str]] = {}
    try:
        for orchard in sorted(frame["StudyOrchard"].unique().tolist()):
            train = frame[frame["StudyOrchard"] != orchard].copy()
            test = frame[frame["StudyOrchard"] == orchard].copy()
            nll0, cols0, alpha0 = fit_and_score(
                train, test, interaction_column=interaction_column, kind=restricted_kind
            )
            nll1, cols1, alpha1 = fit_and_score(
                train, test, interaction_column=interaction_column, kind=full_kind
            )
            mean0 = float(nll0.mean())
            mean1 = float(nll1.mean())
            records.append(
                {
                    "StudyOrchard": orchard,
                    "orchard_year_rows": int(len(test)),
                    "mean_NLL_restricted": mean0,
                    "mean_NLL_full": mean1,
                    "delta_NLL": mean1 - mean0,
                    "alpha_restricted": float(alpha0),
                    "alpha_full": float(alpha1),
                }
            )
            if not first_columns:
                first_columns = {"restricted": cols0, "full": cols1}
    except Exception as exc:
        return {
            "representation": representation,
            "decision": "primary_model_not_identifiable",
            "error": f"{type(exc).__name__}: {exc}",
            "folds_completed": len(records),
            "orchard_records": records,
        }

    deltas = np.asarray([record["delta_NLL"] for record in records], dtype=float)
    total, ci = _bootstrap_summary(deltas)
    decision = detected_label if total < 0 and ci[1] < 0 else no_detected_label
    return {
        "representation": representation,
        "decision": decision,
        "delta_NLL_total": total,
        "orchard_bootstrap_95ci": ci,
        "bootstrap_seed": BOOTSTRAP_SEED,
        "bootstrap_n": BOOTSTRAP_N,
        "model_columns_first_fold": first_columns,
        "orchard_records": records,
    }


def run_analysis(frame: pd.DataFrame) -> dict[str, Any]:
    process = {
        rep: compare_models(
            frame,
            representation=rep,
            restricted_kind="baseline",
            full_kind="process",
            detected_label="process_information_detected",
            no_detected_label="no_detected_process_information",
        )
        for rep in REPS
    }
    process_decisions = [process[rep]["decision"] for rep in REPS]
    if "primary_model_not_identifiable" in process_decisions:
        return {
            "decision": "process_primary_model_not_identifiable",
            "B1": process,
            "B2_opened": False,
        }
    if all(x == "process_information_detected" for x in process_decisions):
        process_gate = "process_adequacy_supported_across_representations"
    elif all(x == "no_detected_process_information" for x in process_decisions):
        process_gate = "process_measurement_not_supported_for_primary_endpoint"
    else:
        process_gate = "process_representation_sensitive"

    result: dict[str, Any] = {
        "decision": process_gate,
        "B1": process,
        "B1_gate": process_gate,
        "B2_opened": False,
    }
    if process_gate != "process_adequacy_supported_across_representations":
        return result

    context = {
        rep: compare_models(
            frame,
            representation=rep,
            restricted_kind="process",
            full_kind="context",
            detected_label="residual_context_information_detected",
            no_detected_label="no_detected_residual_context_information",
        )
        for rep in REPS
    }
    result["B2_opened"] = True
    result["B2"] = context
    context_decisions = [context[rep]["decision"] for rep in REPS]
    if "primary_model_not_identifiable" in context_decisions:
        final = "context_primary_model_not_identifiable"
    elif all(x == "no_detected_residual_context_information" for x in context_decisions):
        final = "context_predictively_redundant_given_partial_process_state"
    elif all(x == "residual_context_information_detected" for x in context_decisions):
        final = "residual_context_required"
    else:
        final = "residual_context_representation_sensitive"
    result["B2_gate"] = final
    result["decision"] = final
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/empirical/n3_carob_predictive_result.json")
    parser.add_argument("--input-xlsx", default=None)
    args = parser.parse_args()

    contract_bytes = CONTRACT_PATH.read_bytes()
    contract = json.loads(contract_bytes.decode("utf-8"))
    if contract["data"]["expected_md5"] != "9cf7668ae8d825c72edda3346ebf36a6":
        raise RuntimeError("unexpected frozen contract digest")

    result: dict[str, Any] = {
        "analysis": "N3_carob_process_and_residual_context",
        "contract_sha256": hashlib.sha256(contract_bytes).hexdigest(),
        "response_firewall": "Endpoint, holdout unit, model family, two visitation representations, B1/B2 gates, bootstrap rule and no-rescue stop rules were committed before project-computed fitting/scoring of the carob reproductive outcomes.",
    }
    try:
        if args.input_xlsx:
            payload = Path(args.input_xlsx).read_bytes()
            md5 = hashlib.md5(payload).hexdigest()
            acquisition = {
                "source": "provided_local_path",
                "file": str(args.input_xlsx),
                "bytes": len(payload),
                "md5": md5,
                "checksum_verified": md5 == contract["data"]["expected_md5"],
            }
            if not acquisition["checksum_verified"]:
                raise RuntimeError("provided workbook does not match frozen MD5")
        else:
            payload, acquisition = acquire_workbook()
            if acquisition["md5"] != contract["data"]["expected_md5"]:
                raise RuntimeError("downloaded workbook does not match frozen MD5")
        result["acquisition"] = acquisition
        frame, audit = prepare_orchard_year_frame(payload)
        result["data_audit"] = audit
        result.update(run_analysis(frame))
    except Exception as exc:
        result["decision"] = "primary_model_not_identifiable"
        result["error"] = f"{type(exc).__name__}: {exc}"

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "decision": result["decision"],
        "B1_gate": result.get("B1_gate"),
        "B2_opened": result.get("B2_opened"),
        "B2_gate": result.get("B2_gate"),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
