from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


LAYER_KEYS = ("O", "D", "I", "T", "F", "C", "R", "G", "A")
PROXIMAL_KEYS = ("D", "I", "T", "F", "C", "R", "G", "A")
FORBIDDEN_RESULT_KEYS = {
    "effect",
    "effect_size",
    "effect_direction",
    "p",
    "p_value",
    "pvalue",
    "estimate",
    "coefficient",
    "significance",
}


def _assert_response_firewall(obj: object) -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if str(key).lower() in FORBIDDEN_RESULT_KEYS:
                raise ValueError(f"outcome-facing registry key is prohibited: {key}")
            _assert_response_firewall(value)
    elif isinstance(obj, list):
        for value in obj:
            _assert_response_firewall(value)


def _layer_counts(systems: list[dict], origin: str, field: str) -> dict[str, dict[str, int]]:
    subset = [system for system in systems if system["origin_family"] == origin]
    result: dict[str, dict[str, int]] = {}
    for layer in LAYER_KEYS:
        counts = Counter(system[field][layer] for system in subset)
        result[layer] = {status: int(counts.get(status, 0)) for status in ("yes", "partial", "no", "unclear")}
    return result


def _both_yes(system: dict, a: str, b: str) -> bool:
    public = system["public_reusable"]
    return public[a] == "yes" and public[b] == "yes"


def summarize(registry: dict) -> dict:
    _assert_response_firewall(registry)
    systems = registry["systems"]
    origins = ("urban", "island")

    by_origin = {}
    for origin in origins:
        subset = [system for system in systems if system["origin_family"] == origin]
        gate_counts = Counter(system["direct_residual_context_gate"] for system in subset)
        by_origin[origin] = {
            "n_systems": len(subset),
            "public_layer_counts": _layer_counts(systems, origin, "public_reusable"),
            "study_measurement_layer_counts": _layer_counts(systems, origin, "study_measurement"),
            "direct_I_and_F_public_yes": sum(_both_yes(system, "I", "F") for system in subset),
            "direct_residual_context_gate": {
                status: int(gate_counts.get(status, 0)) for status in ("yes", "partial", "no")
            },
            "full_proximal_state_public_yes": sum(
                all(system["public_reusable"][layer] == "yes" for layer in PROXIMAL_KEYS)
                for system in subset
            ),
        }

    total = len(systems)
    complete_any = sum(
        all(system["public_reusable"][layer] == "yes" for layer in PROXIMAL_KEYS)
        for system in systems
    )
    c_yes = sum(system["public_reusable"]["C"] == "yes" for system in systems)
    g_yes = sum(system["public_reusable"]["G"] == "yes" for system in systems)

    direct_cross_origin_ready = (
        by_origin["urban"]["direct_residual_context_gate"]["yes"] >= 2
        and by_origin["island"]["direct_residual_context_gate"]["yes"] >= 2
    )

    return {
        "analysis": "N2_response_firewalled_open_data_state_layer_summary",
        "search_cutoff": registry["search_cutoff"],
        "n_systems": total,
        "by_origin": by_origin,
        "full_proximal_state_public_yes_all_systems": complete_any,
        "public_connectivity_C_yes_all_systems": c_yes,
        "public_genetic_G_yes_all_systems": g_yes,
        "direct_cross_origin_residual_context_ready": direct_cross_origin_ready,
        "decision": (
            "direct_cross_origin_residual_context_test_identifiable"
            if direct_cross_origin_ready
            else "N2_measurement_representation_gap_prevents_direct_cross_origin_test"
        ),
        "claim_ceiling": (
            "Bounded candidate-registry statement only: public co-availability of future-relevant layers is incomplete; "
            "missing/repository-undemonstrated layers are measurement/representation boundaries, not ecological absence."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        default="artifacts/empirical/n2_open_data_state_layer_registry.json",
    )
    parser.add_argument(
        "--output",
        default="artifacts/empirical/n2_open_data_state_layer_summary.json",
    )
    args = parser.parse_args()

    registry = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    result = summarize(registry)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
