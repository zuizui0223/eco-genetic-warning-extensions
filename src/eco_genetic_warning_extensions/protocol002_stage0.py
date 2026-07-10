"""Stage 0 algebraic certificate for Protocol 002.

This module deliberately contains no ecological simulation. It creates a
machine-readable record that every predeclared mutation coordinate satisfies the
operator invariants required before a source-reconstruction run is permitted.
"""
from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .mutation_coordinates import MutationCoordinates, primary_phase_grid

UPSTREAM_REPOSITORY = "zuizui0223/eco-genetic-criticality"
UPSTREAM_COMMIT = "dd8ee379d0d3518194c767d16402042525bc00dc"
UPSTREAM_MODULE = "causal_model/symmetric_allele_mutation_closure.py"
LIFECYCLE_MUTATION_POSITION = "after_selection_and_migration__before_finite_drift"


def coordinate_certificate(coordinate: MutationCoordinates) -> dict[str, float | bool]:
    """Return auditable invariants for one directional-mutation coordinate."""
    equilibrium = coordinate.mutation().mutation_only_equilibrium
    if equilibrium is None:  # MutationCoordinates excludes the identity operator.
        raise RuntimeError("non-identity mutation coordinates must have an equilibrium")
    flux_at_zero = coordinate.expected_flux(0.0)
    flux_at_half = coordinate.expected_flux(0.5)
    flux_at_one = coordinate.expected_flux(1.0)
    return {
        "kappa_mu": coordinate.kappa_mu,
        "p_star": coordinate.p_star,
        "u_low_to_high": coordinate.low_to_high,
        "u_high_to_low": coordinate.high_to_low,
        "rate_sum": coordinate.low_to_high + coordinate.high_to_low,
        "contraction_factor": coordinate.contraction_factor,
        "mutation_only_equilibrium": equilibrium,
        "symmetric": coordinate.is_symmetric,
        "maps_zero_into_unit_interval": 0.0 <= coordinate.apply(0.0) <= 1.0,
        "maps_half_into_unit_interval": 0.0 <= coordinate.apply(0.5) <= 1.0,
        "maps_one_into_unit_interval": 0.0 <= coordinate.apply(1.0) <= 1.0,
        "expected_flux_at_p0": flux_at_zero,
        "expected_flux_at_p05": flux_at_half,
        "expected_flux_at_p1": flux_at_one,
    }


def stage0_certificate(
    coordinates: Iterable[MutationCoordinates] | None = None,
) -> dict[str, Any]:
    """Build the immutable-content payload for a Protocol 002 Stage 0 artifact."""
    points = tuple(primary_phase_grid() if coordinates is None else coordinates)
    if not points:
        raise ValueError("Stage 0 requires at least one mutation coordinate")
    entries = [coordinate_certificate(point) for point in points]
    return {
        "protocol": "Protocol 002 — mutation-direction phase diagram",
        "stage": "Stage 0 — algebraic and implementation certificate",
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "commit": UPSTREAM_COMMIT,
            "module": UPSTREAM_MODULE,
            "mutation_position": LIFECYCLE_MUTATION_POSITION,
        },
        "coordinate_count": len(entries),
        "coordinates": entries,
        "interpretation": {
            "fixed_across_equal_kappa": "mutation-map contraction factor",
            "not_fixed_across_equal_kappa": "frequency-dependent expected mutation flux",
            "simulation_result_present": False,
        },
    }


def write_stage0_certificate(path: str | Path, coordinates: Iterable[MutationCoordinates] | None = None) -> Path:
    """Write a deterministic, formatted Stage 0 certificate JSON artifact."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = stage0_certificate(coordinates)
    destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return destination
