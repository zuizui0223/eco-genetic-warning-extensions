from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "manuscript" / "publication_lanes.json"


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def _flat(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert registry["schema_version"] == 1

    lanes = registry["active_lanes"]
    assert set(lanes) == {"warning_validity", "state_validity"}
    assert all(lane["status"] == "active" for lane in lanes.values())

    active_paths = [lane["manuscript"] for lane in lanes.values()]
    assert len(active_paths) == len(set(active_paths)) == 2
    for path in active_paths:
        assert (ROOT / path).is_file(), path

    archive = registry["archive"]
    assert archive["status"] == "integrated_source_archive_not_for_submission"
    assert archive["manuscript"] not in active_paths
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
        "measurement adequacy -> representation/information preservation -> residual origin/history",
        "not a directional long-horizon loss-incidence effect",
        "cross_origin_convergence_not_identifiable_from_existing_archives",
        "No repaired F estimate exists",
        "the residual-context gate was not opened",
        "makes no claim that the frozen relative-diversity thresholds are validated predictive warnings",
    ):
        assert token in state_flat, token
    for warning_denominator in ("35/35", "48/48", "33/33", "49/49"):
        assert warning_denominator not in state

    integrated = _read(archive["manuscript"])
    assert "INTEGRATED SOURCE ARCHIVE — NOT AN ACTIVE SUBMISSION MANUSCRIPT" in integrated

    ownership = _read("manuscript/PUBLICATION_LANES.md")
    assert "Active lane 1 — warning validity" in ownership
    assert "Active lane 2 — state validity and empirical measurement gates" in ownership
    assert "not an active submission manuscript" in ownership

    for router_path in ("README.md", "manuscript/README.md"):
        router = _read(router_path)
        for path in active_paths:
            assert Path(path).name in router, f"{router_path} does not route to {path}"
        assert "publication_lanes.json" in router

    builder = _read("scripts/build_submission_bundle.py")
    for path in (*active_paths, "manuscript/publication_lanes.json", "manuscript/PUBLICATION_LANES.md"):
        assert Path(path).name in builder, f"submission bundle omits {path}"

    print(
        "Publication-lane validation passed: 2 active manuscripts, "
        "1 integrated source archive, warning denominators paired, claim ownership disjoint."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
