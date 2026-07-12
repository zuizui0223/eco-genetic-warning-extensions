from eco_genetic_warning_extensions.protocol002_stage1_projection_pilot import _artifact


def test_projection_pilot_artifact_counts_statuses() -> None:
    attempts = [
        {"source_support": True, "source_prepared": True, "projection_status": "projection_supported"},
        {"source_support": True, "source_prepared": True, "projection_status": "projection_failed"},
        {"source_support": False, "source_prepared": False, "projection_status": "not_run"},
    ]
    artifact = _artifact(attempts)
    assert artifact["status_counts"] == {
        "source_supported": 2,
        "source_prepared": 2,
        "projection_supported": 1,
        "projection_failed": 1,
        "projection_not_run": 1,
    }
    assert artifact["projection_run_present"] is True
    assert artifact["h2_h3_horizon_run_present"] is False
    assert artifact["type_s_result_claimed"] is False
