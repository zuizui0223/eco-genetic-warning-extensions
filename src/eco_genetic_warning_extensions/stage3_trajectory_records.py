"""Flatten immutable Protocol 003 Stage III artifacts to trajectory-endpoint records.

This module is a provenance-preserving data adapter. It does not rerun the
simulation, select domains, change endpoint definitions, or infer new outcomes.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

ENDPOINT_SPECS=(("H_alpha",0.05),("H_alpha",0.10),("H_alpha",0.20),("H_gamma",0.05),("H_gamma",0.10),("H_gamma",0.20))
DOMAIN_METADATA={
    "symmetric_bridge":{"reader_label":"recalibrated_symmetric_domain","artifact_id":8343958766,"artifact_digest":"sha256:c1b42fc9e6ac912a44667ef4cee02090fab37d50fc3a9928c46ae728c0610f58"},
    "transition":{"reader_label":"directional_calibrated_domain","artifact_id":8343922879,"artifact_digest":"sha256:0a994bea874fc9c47544169cd31bbc317c88690dfe1b6fa7548516e35fd7bca8"},
}
FIELDS=("domain","source_domain_label","attempt_index","master_seed","replicate","trajectory_seed","status","kappa_mu","p_star","area_reference","kappa","ramp_generations","hold_generations","horizon","normalised_barrier_increase","source_artifact_id","source_artifact_digest","endpoint","diversity_id","relative_decline_fraction","baseline_eligible","warning_time","trait_loss_time","lead_time_trait_minus_warning","category","valid_pair")


def _endpoint_key(diversity_id:str,fraction:float)->str:
    return f"{diversity_id}_{fraction:.2f}"


def _base_row(attempt:dict[str,Any],index:int,metadata:dict[str,Any])->dict[str,Any]:
    return {"domain":metadata["reader_label"],"source_domain_label":attempt["label"],"attempt_index":index,"master_seed":attempt["master_seed"],"replicate":attempt["replicate"],"trajectory_seed":attempt["trajectory_seed"],"status":attempt["status"],"kappa_mu":attempt["kappa_mu"],"p_star":attempt["p_star"],"area_reference":attempt["area_reference"],"kappa":attempt["kappa"],"ramp_generations":attempt["ramp_generations"],"hold_generations":attempt["hold_generations"],"horizon":attempt["horizon"],"normalised_barrier_increase":attempt["normalised_barrier_increase"],"source_artifact_id":metadata["artifact_id"],"source_artifact_digest":metadata["artifact_digest"]}


def flatten_artifact(payload:dict[str,Any])->list[dict[str,Any]]:
    label=payload["domain"]["label"]
    if label not in DOMAIN_METADATA: raise ValueError(f"unexpected Stage III domain label: {label}")
    metadata=DOMAIN_METADATA[label]; rows=[]; attempts=payload["attempts"]
    if len(attempts)!=100: raise ValueError(f"{label}: expected 100 attempts, found {len(attempts)}")
    for index,attempt in enumerate(attempts):
        base=_base_row(attempt,index,metadata); comparisons=attempt.get("comparisons",[])
        if attempt["status"]!="completed":
            if comparisons: raise ValueError(f"{label} attempt {index}: failed attempt has comparisons")
            for diversity_id,fraction in ENDPOINT_SPECS:
                rows.append({**base,"endpoint":_endpoint_key(diversity_id,fraction),"diversity_id":diversity_id,"relative_decline_fraction":fraction,"baseline_eligible":False,"warning_time":None,"trait_loss_time":None,"lead_time_trait_minus_warning":None,"category":"source_preparation_failed","valid_pair":False})
            continue
        lookup={(item["definition"]["diversity_id"],float(item["definition"]["relative_decline_fraction"])):item for item in comparisons}
        if set(lookup)!=set(ENDPOINT_SPECS): raise ValueError(f"{label} attempt {index}: endpoint coverage mismatch")
        for diversity_id,fraction in ENDPOINT_SPECS:
            item=lookup[(diversity_id,fraction)]
            rows.append({**base,"endpoint":_endpoint_key(diversity_id,fraction),"diversity_id":diversity_id,"relative_decline_fraction":fraction,"baseline_eligible":bool(item["baseline_eligible"]),"warning_time":item["warning_time"],"trait_loss_time":item["trait_loss_time"],"lead_time_trait_minus_warning":item["lead_time_trait_minus_warning"],"category":item["ordering"],"valid_pair":bool(item["valid_pair"])})
    return rows


def build_records(paths:list[str|Path])->list[dict[str,Any]]:
    rows=[]
    for path in paths: rows.extend(flatten_artifact(json.loads(Path(path).read_text(encoding="utf-8"))))
    if len(rows)!=1200: raise ValueError(f"expected 1,200 trajectory-endpoint rows, found {len(rows)}")
    return rows


def write_records(rows:list[dict[str,Any]],output:str|Path)->Path:
    target=Path(output); target.parent.mkdir(parents=True,exist_ok=True)
    with target.open("w",encoding="utf-8",newline="") as handle:
        writer=csv.DictWriter(handle,fieldnames=FIELDS,lineterminator="\n"); writer.writeheader(); writer.writerows(rows)
    return target


def main()->int:
    parser=argparse.ArgumentParser(); parser.add_argument("domain0"); parser.add_argument("domain1"); parser.add_argument("output"); args=parser.parse_args(); write_records(build_records([args.domain0,args.domain1]),args.output); return 0


if __name__=="__main__":
    raise SystemExit(main())
