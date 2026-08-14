from __future__ import annotations

import json
from pathlib import Path

from eco_genetic_warning_extensions.stage3_trajectory_records import build_records, write_records


def _payload(label: str) -> dict:
    domain = {
        "label": label,
        "kappa_mu": 0.2 if label == "symmetric_bridge" else 0.05,
        "p_star": 0.5 if label == "symmetric_bridge" else 0.9,
        "area_reference": 0.8 if label == "symmetric_bridge" else 1.0,
        "kappa": 6.0 if label == "symmetric_bridge" else 4.5,
        "ramp_generations": 30,
        "hold_generations": 210 if label == "symmetric_bridge" else 90,
        "horizon": 240 if label == "symmetric_bridge" else 120,
        "normalised_barrier_increase": 0.2 if label == "symmetric_bridge" else 0.1,
    }
    attempts=[]
    for i in range(100):
        attempts.append({**domain, "master_seed": 100+i//20, "replicate": i%20, "trajectory_seed": 1000+i, "status": "source_preparation_failed", "comparisons": []})
    return {"domain": domain, "attempts": attempts}


def test_raw_stage3_adapter_retains_full_attempted_denominator(tmp_path: Path) -> None:
    paths=[]
    for i,label in enumerate(("symmetric_bridge","transition")):
        path=tmp_path/f"domain{i}.json"
        path.write_text(json.dumps(_payload(label)), encoding="utf-8")
        paths.append(path)
    rows=build_records(paths)
    assert len(rows)==1200
    assert sum(r["category"] == "source_preparation_failed" for r in rows)==1200
    output=write_records(rows,tmp_path/"records.csv")
    assert output.exists()
    assert len(output.read_text(encoding="utf-8").splitlines())==1201
