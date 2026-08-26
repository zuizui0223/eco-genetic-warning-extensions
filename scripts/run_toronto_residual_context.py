from __future__ import annotations

import argparse
import json
import math
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.special import gammaln

DOI = "10.5061/dryad.b8gtht7r4"
EXPECTED_FILE = "data.csv"
REQUIRED_COLUMNS = {
    "site_id",
    "urban_cover",
    "ugs_edge_density",
    "floral_richness_1",
    "floral_richness_2",
    "floral_richness_3",
    "species_phytometer",
    "floral_units_array",
    "number_of_visits",
    "survey_effort",
    "number_seed",
    "fruit_sample_size",
}
SPECIES_RICHNESS = {
    "PEHI": "floral_richness_1",
    "DECA": "floral_richness_2",
    "LOSI": "floral_richness_2",
    "SYNO": "floral_richness_3",
}
BOOTSTRAP_SEED = 20260827
BOOTSTRAP_N = 10000


def _request(url: str, *, json_only: bool = False) -> urllib.request.Request:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    headers["Accept"] = "application/json" if json_only else "text/csv,application/octet-stream,*/*;q=0.8"
    return urllib.request.Request(url, headers=headers)


def _get_json(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(_request(url, json_only=True), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def dryad_manifest() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    encoded = urllib.parse.quote(f"doi:{DOI}", safe="")
    versions_url = f"https://datadryad.org/api/v2/datasets/{encoded}/versions"
    versions = _get_json(versions_url).get("_embedded", {}).get("stash:versions", [])
    if not versions:
        raise RuntimeError("Dryad returned no dataset versions")
    latest = versions[-1]
    files_href = latest.get("_links", {}).get("stash:files", {}).get("href")
    if not files_href:
        raise RuntimeError("Dryad latest version lacks a files link")
    files_url = "https://datadryad.org" + files_href if str(files_href).startswith("/") else str(files_href)
    files = _get_json(files_url).get("_embedded", {}).get("stash:files", [])
    manifest: list[dict[str, Any]] = []
    for item in files:
        self_href = str(item.get("_links", {}).get("self", {}).get("href", ""))
        match = re.search(r"/files/(\d+)$", self_href)
        manifest.append(
            {
                "path": item.get("path"),
                "file_id": int(match.group(1)) if match else None,
                "size": item.get("size"),
                "mime_type": item.get("mimeType"),
                "digest": item.get("digest"),
                "digest_type": item.get("digestType"),
                "links": item.get("_links", {}),
            }
        )
    return latest, manifest


def _looks_like_challenge(data: bytes, content_type: str | None) -> bool:
    head = data[:4096].lower()
    return (
        b"validating" in head
        or b"cloudflare" in head
        or b"just a moment" in head
        or (content_type is not None and "text/html" in content_type.lower())
    )


def download_locked_csv(destination: Path) -> dict[str, Any]:
    latest, manifest = dryad_manifest()
    matches = [item for item in manifest if item["path"] == EXPECTED_FILE]
    if len(matches) != 1 or matches[0]["file_id"] is None:
        raise RuntimeError(f"expected exactly one {EXPECTED_FILE!r} in Dryad manifest")
    item = matches[0]
    file_id = int(item["file_id"])
    attempts: list[dict[str, Any]] = []
    urls = [
        f"https://datadryad.org/stash/downloads/file_stream/{file_id}",
        f"https://datadryad.org/downloads/file_stream/{file_id}",
        f"https://datadryad.org/stash/downloads/file_stream/{file_id}?download=1",
        f"https://datadryad.org/downloads/file_stream/{file_id}?download=1",
    ]
    for url in urls:
        record: dict[str, Any] = {"url": url}
        try:
            with urllib.request.urlopen(_request(url), timeout=120) as response:
                data = response.read()
                content_type = response.headers.get("Content-Type")
                record.update(
                    {
                        "status": int(response.status),
                        "content_type": content_type,
                        "bytes": len(data),
                    }
                )
                if _looks_like_challenge(data, content_type):
                    record["accepted"] = False
                    record["reason"] = "html_or_antibot_challenge"
                elif item.get("size") is not None and len(data) != int(item["size"]):
                    record["accepted"] = False
                    record["reason"] = "byte_size_mismatch"
                else:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(data)
                    record["accepted"] = True
                    attempts.append(record)
                    return {
                        "download_status": "success",
                        "dataset_version": latest,
                        "locked_file": item,
                        "attempts": attempts,
                    }
        except urllib.error.HTTPError as exc:
            record.update({"status": int(exc.code), "accepted": False, "reason": f"HTTPError: {exc.reason}"})
        except Exception as exc:  # pragma: no cover - network dependent
            record.update({"accepted": False, "reason": f"{type(exc).__name__}: {exc}"})
        attempts.append(record)
    return {
        "download_status": "failed",
        "dataset_version": latest,
        "locked_file": item,
        "attempts": attempts,
    }


def prepare_frame(path: Path) -> tuple[pd.DataFrame, dict[str, Any]]:
    raw = pd.read_csv(path)
    missing_columns = sorted(REQUIRED_COLUMNS - set(raw.columns))
    if missing_columns:
        raise RuntimeError(f"missing preregistered columns: {missing_columns}")

    species = set(raw["species_phytometer"].dropna().astype(str))
    unknown_species = sorted(species - set(SPECIES_RICHNESS))
    if unknown_species:
        raise RuntimeError(f"unexpected phytometer codes: {unknown_species}")

    frame = raw.copy()
    frame["I_visit"] = frame["number_of_visits"] / frame["survey_effort"]
    frame["garden_richness_matched"] = np.nan
    for species_code, richness_column in SPECIES_RICHNESS.items():
        mask = frame["species_phytometer"].astype(str) == species_code
        frame.loc[mask, "garden_richness_matched"] = frame.loc[mask, richness_column]

    required_values = [
        "site_id",
        "species_phytometer",
        "urban_cover",
        "ugs_edge_density",
        "floral_units_array",
        "I_visit",
        "garden_richness_matched",
        "number_seed",
        "fruit_sample_size",
    ]
    before = len(frame)
    frame = frame.dropna(subset=required_values).copy()
    frame = frame[frame["survey_effort"] > 0].copy()
    frame = frame[frame["fruit_sample_size"] > 0].copy()
    frame = frame[np.isfinite(frame["I_visit"])].copy()

    audit = {
        "raw_rows": before,
        "eligible_rows": len(frame),
        "site_count": int(frame["site_id"].nunique()),
        "species_counts": {str(k): int(v) for k, v in frame["species_phytometer"].value_counts().sort_index().items()},
        "excluded_rows": int(before - len(frame)),
    }
    if audit["site_count"] < 5:
        raise RuntimeError("fewer than five independent gardens remain eligible")
    return frame, audit


def _design_matrices(train: pd.DataFrame, test: pd.DataFrame, include_context: bool) -> tuple[np.ndarray, np.ndarray, list[str]]:
    species_levels = sorted(train["species_phytometer"].astype(str).unique())
    reference = species_levels[0]
    columns: list[str] = ["intercept"]
    train_parts = [np.ones((len(train), 1), dtype=float)]
    test_parts = [np.ones((len(test), 1), dtype=float)]

    for level in species_levels:
        if level == reference:
            continue
        columns.append(f"species[{level}]")
        train_parts.append((train["species_phytometer"].astype(str).to_numpy() == level).astype(float)[:, None])
        test_parts.append((test["species_phytometer"].astype(str).to_numpy() == level).astype(float)[:, None])

    continuous = ["I_visit", "floral_units_array", "garden_richness_matched"]
    if include_context:
        continuous += ["urban_cover", "ugs_edge_density"]

    for name in continuous:
        mean = float(train[name].mean())
        sd = float(train[name].std(ddof=0))
        if not math.isfinite(sd) or sd <= 0:
            raise RuntimeError(f"training-fold predictor has zero/nonfinite SD: {name}")
        columns.append(name)
        train_parts.append(((train[name].to_numpy(dtype=float) - mean) / sd)[:, None])
        test_parts.append(((test[name].to_numpy(dtype=float) - mean) / sd)[:, None])

    return np.hstack(train_parts), np.hstack(test_parts), columns


def _poisson_nll(y: np.ndarray, mu: np.ndarray) -> np.ndarray:
    if np.any(mu <= 0) or not np.all(np.isfinite(mu)):
        raise RuntimeError("nonpositive/nonfinite Poisson prediction")
    return mu - y * np.log(mu) + gammaln(y + 1.0)


def _fit_score(train: pd.DataFrame, test: pd.DataFrame, include_context: bool) -> tuple[np.ndarray, list[str]]:
    x_train, x_test, columns = _design_matrices(train, test, include_context=include_context)
    y_train = train["number_seed"].to_numpy(dtype=float)
    y_test = test["number_seed"].to_numpy(dtype=float)
    offset_train = np.log(train["fruit_sample_size"].to_numpy(dtype=float))
    offset_test = np.log(test["fruit_sample_size"].to_numpy(dtype=float))
    model = sm.GLM(y_train, x_train, family=sm.families.Poisson(), offset=offset_train)
    fit = model.fit(maxiter=200, disp=0)
    if not bool(fit.converged):
        raise RuntimeError("Poisson GLM did not converge")
    mu = np.asarray(fit.predict(x_test, offset=offset_test), dtype=float)
    return _poisson_nll(y_test, mu), columns


def run_logo(frame: pd.DataFrame) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    try:
        for site in sorted(frame["site_id"].astype(str).unique()):
            test = frame[frame["site_id"].astype(str) == site].copy()
            train = frame[frame["site_id"].astype(str) != site].copy()
            nll0, columns0 = _fit_score(train, test, include_context=False)
            nll1, columns1 = _fit_score(train, test, include_context=True)
            delta = float(nll1.sum() - nll0.sum())
            records.append(
                {
                    "site_id": site,
                    "n_rows": int(len(test)),
                    "nll_M0": float(nll0.sum()),
                    "nll_M1": float(nll1.sum()),
                    "delta_NLL": delta,
                }
            )
    except Exception as exc:
        return {
            "decision": "primary_model_not_identifiable",
            "error": f"{type(exc).__name__}: {exc}",
            "folds_completed": len(records),
            "garden_records": records,
        }

    deltas = np.array([record["delta_NLL"] for record in records], dtype=float)
    total_delta = float(deltas.sum())
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    draws = rng.choice(deltas, size=(BOOTSTRAP_N, len(deltas)), replace=True).sum(axis=1)
    ci_low, ci_high = np.quantile(draws, [0.025, 0.975])
    decision = (
        "residual_urban_context_information_detected"
        if total_delta < 0 and float(ci_high) < 0
        else "no_detected_residual_urban_context_information"
    )
    return {
        "decision": decision,
        "delta_NLL_total": total_delta,
        "garden_bootstrap_95ci": [float(ci_low), float(ci_high)],
        "bootstrap_seed": BOOTSTRAP_SEED,
        "bootstrap_n": BOOTSTRAP_N,
        "garden_records": records,
        "M0_columns": columns0,
        "M1_columns": columns1,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=".tmp/toronto/data.csv")
    parser.add_argument("--output", default="artifacts/empirical/toronto_residual_context_result.json")
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    result: dict[str, Any] = {
        "analysis": "prospectively_frozen_toronto_residual_urban_context_replication",
        "doi": DOI,
        "response_firewall": "Model, endpoint, mapping and holdout unit were committed before project-level access to Toronto reproductive outcome values.",
    }

    if args.download:
        acquisition = download_locked_csv(input_path)
        result["acquisition"] = acquisition
        if acquisition["download_status"] != "success":
            result["decision"] = "locked_archive_bytes_not_acquired"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
            print(json.dumps({"decision": result["decision"]}))
            return 0

    if not input_path.exists():
        result["decision"] = "locked_archive_bytes_not_acquired"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
        print(json.dumps({"decision": result["decision"]}))
        return 0

    try:
        frame, audit = prepare_frame(input_path)
        result["schema_audit"] = audit
        result.update(run_logo(frame))
    except Exception as exc:
        result["decision"] = "primary_model_not_identifiable"
        result["error"] = f"{type(exc).__name__}: {exc}"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "delta_NLL_total": result.get("delta_NLL_total")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
