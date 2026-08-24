from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = (ROOT / "manuscript" / "empirical_miconia_joint_state_access_result.md").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "miconia-joint-state-discovery.yml").read_text(encoding="utf-8")


def test_miconia_closes_as_access_nonidentifiability_not_ecological_null() -> None:
    assert "`not_identifiable_from_archive`" in RESULT
    assert "access/non-identifiability result" in RESULT
    assert "not an ecological null" in RESULT
    assert "did **not** inspect workbook schema or any outcome values" in RESULT


def test_three_access_attempts_and_failures_are_retained() -> None:
    for run in ("32732304033", "32733136599", "32733622959"):
        assert run in RESULT
    assert "HTTP 403" in RESULT
    assert "HTTP 401" in RESULT
    assert "4,324" in RESULT
    assert "13,042" in RESULT
    assert "before schema inspection" in RESULT


def test_locked_source_identifiers_are_unchanged() -> None:
    assert "10.5061/dryad.1cm80" in RESULT
    for file_id in (30526, 30527, 30528, 30529):
        assert str(file_id) in RESULT


def test_workflow_is_manual_only_after_stop_rule() -> None:
    assert "workflow_dispatch:" in WORKFLOW
    assert "pull_request:" not in WORKFLOW
    assert "No fourth download-route modification is allowed" in RESULT


def test_no_project_generated_miconia_result_is_claimed() -> None:
    assert "Do not report" in RESULT
    assert "any project-generated Miconia model result" in RESULT
    assert "Published ecological findings may still be cited as literature" in RESULT
