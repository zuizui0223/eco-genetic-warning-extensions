from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import fmean


def loss(record: dict, horizon: int) -> int:
    t = record["last_refuge_loss_time"]
    return int(t is not None and int(t) <= horizon)


def mean_ci(values: list[float]) -> tuple[float, list[float]]:
    mean = fmean(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    se = math.sqrt(variance / len(values))
    return mean, [mean - 1.96 * se, mean + 1.96 * se]


def derive(records: list[dict]) -> dict:
    by = {
        (r["condition"], int(r["master_seed"]), int(r["replicate"])): r
        for r in records
    }
    keys = sorted(
        (int(r["master_seed"]), int(r["replicate"]))
        for r in records
        if r["condition"] == "AA_full"
    )
    if len(keys) != 1500:
        raise RuntimeError(f"expected 1500 paired keys, found {len(keys)}")

    out: dict[str, dict] = {}
    for horizon in (20, 40):
        aa_benefit: list[float] = []
        rr_benefit: list[float] = []
        did: list[float] = []
        for key in keys:
            aa_full = by[("AA_full", *key)]
            rr_full = by[("RR_full", *key)]
            aa_q = by[("AA_q_only", *key)]
            rr_q = by[("RR_q_only", *key)]
            aa = loss(aa_q, horizon) - loss(aa_full, horizon)
            rr = loss(rr_q, horizon) - loss(rr_full, horizon)
            aa_benefit.append(aa)
            rr_benefit.append(rr)
            did.append(rr - aa)

        aa_mean, aa_ci = mean_ci(aa_benefit)
        rr_mean, rr_ci = mean_ci(rr_benefit)
        did_mean, did_ci = mean_ci(did)
        out[str(horizon)] = {
            "AA_qonly_minus_full": aa_mean,
            "AA_ci95": aa_ci,
            "RR_qonly_minus_full": rr_mean,
            "RR_ci95": rr_ci,
            "RR_minus_AA_buffering_benefit_DID": did_mean,
            "DID_ci95": did_ci,
        }
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("records", type=Path)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    records = json.loads(args.records.read_text())
    result = derive(records)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
