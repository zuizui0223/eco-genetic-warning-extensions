from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "manuscript" / "publication_lanes.json"
NATURAL_GATE_REGISTRY = ROOT / "manuscript" / "natural_data_gate_registry.json"


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def _flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert registry["schema_version"] == 3

    lanes = registry["active_lanes"]
    assert set(lanes) == {"warning_validity", "state_validity"}
    assert all(lane["status"] == "active" for lane in lanes.values())

    active_paths = [lane["manuscript"] for lane in lanes.values()]
    assert len(active_paths) == len(set(active_paths)) == 2
    for path in active_paths:
        assert (ROOT / path).is_file(), path

    development = registry["independent_development_programs"]
    assert set(development) == {"natural_data_four_gate_program"}
    natural_lane = development["natural_data_four_gate_program"]
    assert natural_lane["status"] == "development_go_primary_ecological_indicators"
    assert natural_lane["publication_structure"] == "one_methodological_empirical_synthesis_without_cross_system_effect_pooling"
    assert natural_lane["primary_target"] == "Ecological Indicators"
    assert len(natural_lane["four_lines"]) == 4
    natural_path = natural_lane["manuscript"]
    assert natural_path not in active_paths
    assert (ROOT / natural_path).is_file()
    for control_path in (
        natural_lane["gate_registry"],
        natural_lane["publication_audit"],
        natural_lane["venue_audit"],
    ):
        assert (ROOT / control_path).is_file(), control_path

    gate_registry = json.loads(NATURAL_GATE_REGISTRY.read_text(encoding="utf-8"))
    assert gate_registry["schema_version"] == 1
    systems = gate_registry["systems"]
    assert len(systems) == 7
    assert {record["line"] for record in systems} == {1, 2, 3, 4}
    assert {record["holdout_unit"] for record in systems} == {
        "site",
        "garden",
        "maternal plant",
        "array",
        "orchard",
        "population",
    }
    assert gate_registry["cross_study"]["locked_outcome"] == "cross_origin_convergence_not_identifiable_from_existing_archives"
    for record in systems:
        assert record["candidate_state"]
        assert record["declared_endpoint"]
        assert record["gate_reached"] in gate_registry["shared_order"]
        assert record["locked_outcome"]
        assert record["claim_ceiling"]

    archive = registry["archive"]
    assert archive["status"] == "integrated_source_archive_not_for_submission"
    assert archive["manuscript"] not in active_paths
    assert archive["manuscript"] != natural_path
    assert (ROOT / archive["manuscript"]).is_file()

    warning = _read(lanes["warning_validity"]["manuscript"])
    warning_flat = _flat(warning)
    for token in (
        "35/35",
        "48/48",
        "33/33",
        "49/49",
        "specificity was 0",
        "binary-marker AUC was 0.5",
        "Event-conditioned temporal precedence can be perfectly reproducible",
    ):
        assert token in warning_flat, token
    assert "does not show that genetic diversity contains no predictive information" in warning_flat
    assert "No endpoint rerun or post-result threshold search is authorised" in warning_flat

    state = _read(lanes["state_validity"]["manuscript"])
    state_flat = _flat(state)
    for token in (
        "0.2543",
        "+4.4 percentage points",
        "-1.2 to +10.0 percentage points",
        "14.8% relative increase",
        "does not establish a signed long-horizon effect",
        "Non-significant tests do not establish equivalence",
        "A scalar connectivity label did not transport across seeds or mechanisms",
        "natural_data_four_gate_program.md",
        "makes no claim that the frozen relative-diversity thresholds are validated predictive warnings",
    ):
        assert token in state_flat, token
    for warning_denominator in ("35/35", "48/48", "33/33", "49/49"):
        assert warning_denominator not in state
    for empirical_token in (
        "1.08774",
        "4932.9195",
        "0.09187",
        "Fallow graound",
        "8.88e-16",
        "-0.10195",
        "cross_origin_convergence_not_identifiable_from_existing_archives",
    ):
        assert empirical_token not in state, f"natural-data result leaked into active state lane: {empirical_token}"

    natural = _read(natural_path)
    natural_flat = _flat(natural)
    for token in (
        "Line 1 — residual context",
        "Line 2 — a process coordinate remains missing",
        "Line 3 — a plausible process proxy fails endpoint-relevant measurement adequacy",
        "Line 4 — preprocessing can erase the mechanistic information",
        "1.08774",
        "4932.9195",
        "0.09187",
        "Fallow graound",
        "8.88e-16",
        "-0.10195",
        "cross_origin_convergence_not_identifiable_from_existing_archives",
    ):
        assert token in natural_flat, token
    for warning_denominator in ("35/35", "48/48", "33/33", "49/49"):
        assert warning_denominator not in natural

    publication_audit = _read(natural_lane["publication_audit"])
    venue_audit = _read(natural_lane["venue_audit"])
    assert "one methodological empirical synthesis" in publication_audit
    assert "Why not four papers" in publication_audit
    assert "Why not a pooled synthesis" in publication_audit
    assert "Primary target — Ecological Indicators" in venue_audit
    assert "Stretch target — Methods in Ecology and Evolution, conditional only" in venue_audit

    integrated = _read(archive["manuscript"])
    assert "INTEGRATED SOURCE ARCHIVE — NOT AN ACTIVE SUBMISSION MANUSCRIPT" in integrated

    ownership = _read("manuscript/PUBLICATION_LANES.md")
    assert "Active lane 1 — warning validity" in ownership
    assert "Active lane 2 — model state validity and process portability" in ownership
    assert "Migrated independent programme — four natural-data gate lines" in ownership
    assert "zuizui0223/egwee" in ownership
    assert "not an active submission manuscript" in ownership

    for router_path in ("README.md", "manuscript/README.md"):
        router = _read(router_path)
        for path in active_paths:
            assert Path(path).name in router, f"{router_path} does not route to {path}"
        assert "publication_lanes.json" in router

    builder = _read("scripts/build_submission_bundle.py")
    for path in (*active_paths, "manuscript/publication_lanes.json", "manuscript/PUBLICATION_LANES.md"):
        assert Path(path).name in builder, f"submission bundle omits {path}"
    assert Path(natural_path).name not in builder, "independent natural-data programme leaked into active EGWE submission bundle"

    print(
        "Publication-lane validation passed: 2 active EGWE manuscripts, "
        "1 migrated natural-data development programme, 1 integrated source archive; "
        "warning, state, and empirical claim ownership are disjoint."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
