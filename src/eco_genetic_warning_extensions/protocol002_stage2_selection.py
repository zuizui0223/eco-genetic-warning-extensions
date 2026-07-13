"""Aggregate Protocol 002 Stage II batch artifacts and select calibration domains."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .mutation_coordinates import MutationCoordinates, primary_phase_grid
from .protocol002_calibration import (
    Protocol002CalibrationCandidate,
    select_protocol002_calibration_domain,
)

EXPECTED_STAGE2_BATCH_COUNT = 810
EXPECTED_STAGE2_ATTEMPT_COUNT = 20_250


def load_stage2_batch_artifacts(paths: Iterable[str | Path]) -> tuple[dict, ...]:
    artifacts = tuple(json.loads(Path(path).read_text(encoding="utf-8")) for path in paths)
    batch_indices = [int(item["campaign"]["batch_index"]) for item in artifacts]
    if len(artifacts) != EXPECTED_STAGE2_BATCH_COUNT:
        raise ValueError(f"expected {EXPECTED_STAGE2_BATCH_COUNT} Stage II batch artifacts, found {len(artifacts)}")
    if sorted(batch_indices) != list(range(EXPECTED_STAGE2_BATCH_COUNT)):
        raise ValueError("Stage II batch indices are incomplete or duplicated")
    if sum(int(item["status_counts"]["attempted"]) for item in artifacts) != EXPECTED_STAGE2_ATTEMPT_COUNT:
        raise ValueError("Stage II attempted-count total does not equal 20,250")
    return artifacts


def candidate_from_batch_artifact(artifact: dict) -> Protocol002CalibrationCandidate | None:
    rates = tuple(block["trait_loss_rate"] for block in artifact["seed_blocks"])
    if len(rates) != 5 or any(rate is None for rate in rates):
        return None
    cell = artifact["cell"]
    return Protocol002CalibrationCandidate(
        coordinate=MutationCoordinates(kappa_mu=float(cell["kappa_mu"]), p_star=float(cell["p_star"])),
        area_reference=float(cell["area_reference"]),
        kappa=float(cell["kappa"]),
        ramp_generations=int(cell["ramp_generations"]),
        hold_generations=int(cell["hold_generations"]),
        normalised_barrier_increase=float(cell["normalised_barrier_increase"]),
        seed_block_trait_loss_rates=tuple(float(rate) for rate in rates),
    )


def _candidate_row(candidate: Protocol002CalibrationCandidate) -> dict:
    return {
        "kappa_mu": candidate.coordinate.kappa_mu,
        "p_star": candidate.coordinate.p_star,
        "area_reference": candidate.area_reference,
        "kappa": candidate.kappa,
        "ramp_generations": candidate.ramp_generations,
        "hold_generations": candidate.hold_generations,
        "horizon": candidate.horizon,
        "normalised_barrier_increase": candidate.normalised_barrier_increase,
        "seed_block_trait_loss_rates": list(candidate.seed_block_trait_loss_rates),
        "pooled_trait_loss_rate": candidate.pooled_trait_loss_rate,
        "rank_key": list(candidate.rank_key()),
    }


def stage2_selection_artifact(batch_artifacts: Iterable[dict]) -> dict:
    artifacts = tuple(batch_artifacts)
    candidates = tuple(
        candidate
        for candidate in (candidate_from_batch_artifact(artifact) for artifact in artifacts)
        if candidate is not None
    )
    selected_rows = []
    no_domain_rows = []
    for coordinate in primary_phase_grid():
        selected = select_protocol002_calibration_domain(candidates, coordinate=coordinate)
        coordinate_row = {"kappa_mu": coordinate.kappa_mu, "p_star": coordinate.p_star}
        if selected is None:
            no_domain_rows.append({**coordinate_row, "status": "no_domain_selected"})
        else:
            selected_rows.append({**coordinate_row, "status": "selected", "domain": _candidate_row(selected)})

    return {
        "stage": "Protocol 002 Stage II calibration domain selection",
        "batch_count": len(artifacts),
        "attempt_count": sum(int(item["status_counts"]["attempted"]) for item in artifacts),
        "candidate_count_with_complete_seed_blocks": len(candidates),
        "eligible_candidate_count": sum(candidate.is_eligible() for candidate in candidates),
        "selected_domain_count": len(selected_rows),
        "no_domain_selected_count": len(no_domain_rows),
        "selected_domains": selected_rows,
        "no_domain_selected": no_domain_rows,
        "selection_rule": "min(|pooled_rate-0.50|, horizon, barrier_increase, A_ref, kappa) among candidates with every seed-block rate in [0.30, 0.70]",
        "warning_fields_inspected": False,
        "diversity_fields_inspected": False,
    }


def write_stage2_selection(batch_root: str | Path, output: str | Path) -> Path:
    root = Path(batch_root)
    paths = sorted(root.rglob("batch_*.json"))
    artifacts = load_stage2_batch_artifacts(paths)
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(stage2_selection_artifact(artifacts), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target
