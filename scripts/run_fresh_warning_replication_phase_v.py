from __future__ import annotations

import argparse
import json
from dataclasses import replace
from pathlib import Path

from eco_genetic_warning_extensions.fresh_warning_replication_phase_v import (
    PHASE_V_MASTER_SEEDS,
    PHASE_V_REPLICATES_PER_SEED,
    evaluate_parent_summary,
    phase_v_manifest,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="artifacts/fresh_warning_replication")
    args = parser.parse_args()

    from causal_model.h2r_independent_relative_validation import run_h2r_independent_relative_validation
    from causal_model.h2r_validation_domain import SELECTED_VALIDATION_DOMAIN
    from causal_model.multipatch_criticality_experiments import standard_profile

    manifest = phase_v_manifest()
    domain = SELECTED_VALIDATION_DOMAIN
    expected = manifest["frozen_domain"]
    actual = {
        "mutation_rate": domain.mutation_rate,
        "area_reference": domain.area_reference,
        "interaction_feedback": domain.interaction_feedback,
        "ramp_generations": domain.schedule.ramp_generations,
        "hold_generations": domain.schedule.hold_generations,
        "total_generations": domain.schedule.total_generations,
        "total_normalized_barrier_increase": domain.schedule.total_normalized_barrier_increase,
        "profile": "standard",
    }
    if actual != expected:
        raise RuntimeError(f"frozen H2-R domain drifted: expected={expected!r}, actual={actual!r}")

    spec = replace(standard_profile(), replicates=PHASE_V_REPLICATES_PER_SEED)
    result = run_h2r_independent_relative_validation(spec, master_seeds=PHASE_V_MASTER_SEEDS)
    summary = evaluate_parent_summary(result.summary)

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "phase_v_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (out / "phase_v_raw.json").write_text(json.dumps(result.as_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (out / "phase_v_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PHASE_V_SUMMARY_BEGIN")
    print(json.dumps(summary, sort_keys=True))
    print("PHASE_V_SUMMARY_END")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
