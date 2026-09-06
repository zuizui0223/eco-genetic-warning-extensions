from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import fmean


def loss(record: dict, horizon: int) -> int:
    t = record["last_refuge_loss_time"]
    return int(t is not None and int(t) <= int(horizon))


def mean_ci(values: list[float]) -> tuple[float, list[float]]:
    mean = fmean(values)
    if len(values) < 2:
        return mean, [mean, mean]
    var = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    se = math.sqrt(var / len(values))
    return mean, [mean - 1.96 * se, mean + 1.96 * se]


def derive(records: list[dict]) -> dict:
    by = {
        (r["intervention"], r["condition"], int(r["master_seed"]), int(r["replicate"])): r
        for r in records
    }
    keys = sorted(
        (int(r["master_seed"]), int(r["replicate"]))
        for r in records
        if r["intervention"] == "baseline_indirect" and r["condition"] == "AA"
    )
    if len(keys) != 1500:
        raise RuntimeError(f"expected 1500 locked paired keys, got {len(keys)}")

    out = {}
    for horizon in (20, 40):
        h = {}
        for condition in ("AA", "RR"):
            baseline = [
                loss(by[("baseline_indirect", condition, *key)], horizon)
                for key in keys
            ]
            deletion = [
                loss(by[("delete_density_to_q", condition, *key)], horizon)
                for key in keys
            ]
            paired = [b - d for b, d in zip(baseline, deletion)]
            effect, ci = mean_ci(paired)
            h[condition] = {
                "n_paired_keys": len(keys),
                "baseline_loss_rate": fmean(baseline),
                "delete_density_loss_rate": fmean(deletion),
                "baseline_minus_deletion_risk": effect,
                "paired_ci95": ci,
            }
        out[f"generation_{horizon}"] = h
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--records", required=True, help="records.json from locked pathway-edge-decomposition artifact")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    records = json.loads(Path(args.records).read_text(encoding="utf-8"))
    result = derive(records)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
