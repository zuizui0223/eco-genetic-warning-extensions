from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://zenodo.org/records/10814705/files/pollinator.csv?download=1"
EXPECTED_MD5 = "81e0deaa78a6a97e1211484cb9d0d3b3"
USER_AGENT = "eco-genetic-warning-extensions/1.0"


def _download() -> bytes:
    req = Request(URL, headers={"User-Agent": USER_AGENT, "Accept": "text/csv,*/*"})
    with urlopen(req, timeout=120) as response:
        payload = response.read()
    observed = hashlib.md5(payload).hexdigest()
    if observed != EXPECTED_MD5:
        raise RuntimeError(f"pollinator.csv MD5 mismatch: expected={EXPECTED_MD5}, observed={observed}")
    return payload


def _parse_float(value: str | None) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    return number


def diagnose(payload: bytes) -> dict[str, object]:
    text = payload.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames is None:
        raise RuntimeError("pollinator.csv has no header")
    fields = [str(x) for x in reader.fieldnames]
    if "experimental.population" not in fields or "visits.per.flower" not in fields:
        raise RuntimeError(f"locked diagnostic columns absent: {fields}")

    flower_fields = [
        name
        for name in fields
        if "flower" in name.lower() and "day" in name.lower() and name != "visits.per.flower"
    ]
    total_visit_field = "total.poll.visits" if "total.poll.visits" in fields else None

    nonfinite_rows: list[dict[str, object]] = []
    row_count = 0
    for row in reader:
        row_count += 1
        raw = str(row.get("visits.per.flower", "")).strip()
        value = _parse_float(raw)
        nonfinite = value is None or not math.isfinite(value)
        if not nonfinite:
            continue

        flower_values = {name: row.get(name) for name in flower_fields}
        flower_numeric = [
            number
            for number in (_parse_float(row.get(name)) for name in flower_fields)
            if number is not None and math.isfinite(number)
        ]
        if value is None:
            kind = "missing_or_non_numeric"
        elif math.isnan(value):
            kind = "nan"
        elif math.isinf(value):
            kind = "positive_infinity" if value > 0 else "negative_infinity"
        else:
            kind = "other_nonfinite"

        nonfinite_rows.append(
            {
                "experimental.population": str(row.get("experimental.population", "")).strip(),
                "raw_visits_per_flower": raw,
                "nonfinite_kind": kind,
                "total_poll_visits": row.get(total_visit_field) if total_visit_field else None,
                "flower_count_columns": flower_values,
                "finite_flower_count_values": flower_numeric,
                "all_finite_flower_counts_zero": bool(flower_numeric) and all(v == 0 for v in flower_numeric),
            }
        )

    return {
        "source": {
            "url": URL,
            "md5": EXPECTED_MD5,
            "sha256": hashlib.sha256(payload).hexdigest(),
        },
        "diagnostic_scope": (
            "Predictor-only diagnostic after the preregistered primary endpoint closed. "
            "No seed outcome, treatment contrast, model, alternate visitation metric, imputation, or repaired value is used."
        ),
        "rows_in_pollinator_file": row_count,
        "flower_count_columns_detected": flower_fields,
        "nonfinite_visits_per_flower_count": len(nonfinite_rows),
        "nonfinite_rows": nonfinite_rows,
        "decision_effect": "none; the locked decision remains not_identifiable_for_primary_endpoint",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/empirical/campanula_nonfinite_visitation_diagnostic.json",
    )
    args = parser.parse_args()
    result = diagnose(_download())
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "nonfinite_count": result["nonfinite_visits_per_flower_count"],
        "populations": [row["experimental.population"] for row in result["nonfinite_rows"]],
        "kinds": [row["nonfinite_kind"] for row in result["nonfinite_rows"]],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
