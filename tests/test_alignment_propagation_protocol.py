from __future__ import annotations

import json
import math
from pathlib import Path

from eco_genetic_warning_extensions.alignment_propagation_experiment import (
    PROTOCOL_PATH,
    approximate_power,
    barrier_schedule,
    contract_from_protocol,
    paired_risk_interval,
)

ROOT = Path(__file__).resolve().parents[1]


def test_protocol_is_locked_and_nested() -> None:
    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
    assert protocol["status"] == "prospective_locked_before_run"
    contract = contract_from_protocol(protocol)
    assert contract.horizons == (5, 10, 20, 40)
    assert contract.nested_replicates_per_seed == (100, 200, 300)
    assert contract.max_replicates_per_seed == 300
    assert len(contract.master_seeds) == 5
    assert [len(contract.master_seeds) * r for r in contract.nested_replicates_per_seed] == [500, 1000, 1500]
    assert protocol["paired_replication"]["primary_pair_count"] == 1500
    assert protocol["estimands"]["no_significance_search"].startswith("No horizon")


def test_short_horizons_truncate_one_common_forcing_path() -> None:
    schedule = barrier_schedule(40)
    assert len(schedule) == 40
    assert math.isclose(schedule[0], 0.5025, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(schedule[4], 0.5125, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(schedule[9], 0.525, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(schedule[19], 0.55, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(schedule[39], 0.60, rel_tol=0.0, abs_tol=1e-15)
    assert schedule[:5] == barrier_schedule(5)
    assert schedule[:10] == barrier_schedule(10)
    assert schedule[:20] == barrier_schedule(20)


def test_legacy_counts_reproduce_interval_and_planning_discordance() -> None:
    interval = paired_risk_interval(92, 114, 500)
    assert math.isclose(interval["risk_difference_anti_minus_aligned"], 0.044, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(interval["ci95_lower"], -0.012130238951923236, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(interval["ci95_upper"], 0.10013023895192323, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose((114 + 92) / 500, 0.412, rel_tol=0.0, abs_tol=1e-12)


def test_predeclared_power_grid_matches_planning_values() -> None:
    expected = {500: 0.416, 1000: 0.695, 1500: 0.857}
    for n, target in expected.items():
        assert abs(approximate_power(n) - target) < 0.001


def test_protocol_does_not_reopen_phase_v() -> None:
    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
    relation = protocol["relationship_to_phase_v"]
    assert relation["not_a_rerun"] is True
    assert relation["no_change_to_locked_phase_v"] is True
    assert relation["legacy_parent_commit"] == "dd8ee379d0d3518194c767d16402042525bc00dc"
