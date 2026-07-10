import json

import pytest

from eco_genetic_warning_extensions.mutation_coordinates import MutationCoordinates
from eco_genetic_warning_extensions.protocol002_stage0 import (
    LIFECYCLE_MUTATION_POSITION,
    UPSTREAM_COMMIT,
    coordinate_certificate,
    stage0_certificate,
    write_stage0_certificate,
)


def test_coordinate_certificate_records_operator_and_flux_invariants() -> None:
    record = coordinate_certificate(MutationCoordinates(kappa_mu=0.20, p_star=0.75))
    assert record["rate_sum"] == pytest.approx(0.20)
    assert record["contraction_factor"] == pytest.approx(0.80)
    assert record["mutation_only_equilibrium"] == pytest.approx(0.75)
    assert record["expected_flux_at_p0"] == pytest.approx(0.15)
    assert record["expected_flux_at_p05"] == pytest.approx(0.10)
    assert record["expected_flux_at_p1"] == pytest.approx(0.05)
    assert all(record[key] for key in ("maps_zero_into_unit_interval", "maps_half_into_unit_interval", "maps_one_into_unit_interval"))


def test_primary_certificate_is_phase_complete_and_pins_upstream() -> None:
    certificate = stage0_certificate()
    assert certificate["coordinate_count"] == 15
    assert certificate["upstream"]["commit"] == UPSTREAM_COMMIT
    assert certificate["upstream"]["mutation_position"] == LIFECYCLE_MUTATION_POSITION
    assert certificate["interpretation"]["simulation_result_present"] is False


def test_stage0_certificate_can_be_written_without_running_simulation(tmp_path) -> None:
    path = write_stage0_certificate(tmp_path / "stage0.json", [MutationCoordinates(0.20, 0.50)])
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["coordinate_count"] == 1
    assert payload["coordinates"][0]["symmetric"] is True
    assert payload["interpretation"]["simulation_result_present"] is False
