from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "artifacts" / "empirical" / "n3_island_process_function_registry.json"
OUTPUT = ROOT / "artifacts" / "empirical" / "n3_island_process_function_summary.json"


def summarize(registry: dict) -> dict:
    systems = registry["systems"]
    both_study = sum(
        s["study_measurement"]["I"] == "yes" and s["study_measurement"]["F"] == "yes"
        for s in systems
    )
    both_public_yes = sum(
        s["public_reusable"]["I"] == "yes" and s["public_reusable"]["F"] == "yes"
        for s in systems
    )
    process_ready_yes = sum(s["process_function_gate"] == "yes" for s in systems)
    process_partial = sum(s["process_function_gate"] == "partial" for s in systems)
    residual_yes = sum(s["residual_context_gate"] == "yes" for s in systems)
    residual_partial = sum(s["residual_context_gate"] == "partial" for s in systems)
    explicit_process_function_file_set = [
        s["id"] for s in systems
        if s["public_reusable"]["I"] == "yes" and s["public_reusable"]["F"] == "yes"
    ]
    return {
        "analysis": "N3_island_process_function_stage_A_summary",
        "n_systems": len(systems),
        "study_level_direct_I_and_F_yes": both_study,
        "public_reusable_direct_I_and_F_both_yes": both_public_yes,
        "public_reusable_direct_I_and_F_both_yes_systems": explicit_process_function_file_set,
        "process_function_gate_yes": process_ready_yes,
        "process_function_gate_partial": process_partial,
        "residual_context_gate_yes": residual_yes,
        "residual_context_gate_partial": residual_partial,
        "decision": "island_process_function_archives_recovered_but_schema_alignment_still_required",
        "interpretation": (
            "The earlier N2 island 0/5 result is a bounded-registry measurement/representation result, "
            "not a general absence of island process-function archives. N3 prospectively recovers island "
            "studies measuring direct visitation and realised reproduction. Public reusable direct I and F "
            "are now explicit for two of four N3 systems, but no N3 system is promoted to a fitted "
            "process-function or residual-context analysis until the preregistered join/schema gate passes."
        ),
        "claim_ceiling": (
            "N3 establishes archive candidates and narrows the remaining obstacle to schema-level alignment; "
            "it does not establish an ecological island effect or urban-island convergence."
        ),
    }


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    summary = summarize(registry)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
