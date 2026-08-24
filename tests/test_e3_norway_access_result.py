from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "manuscript" / "empirical_e3_norway_access_result.md").read_text(encoding="utf-8")


def test_e3_is_access_nonidentifiability_not_ecological_null() -> None:
    assert "not_identifiable_from_public_download_in_current_execution" in TEXT
    assert "access/execution result" in TEXT
    assert "not a null ecological result" in TEXT
    assert "was **not run**" in TEXT


def test_locked_public_file_is_recorded() -> None:
    assert "Visitation&Seedsetdata_Dryad.xlsx" in TEXT
    assert "241700" in TEXT
    assert "135,774 bytes" in TEXT
    assert "1f242b448e05582da21fb8fef9443535e515864052a641ac33c853683a091198" in TEXT


def test_three_fetch_attempts_and_stop_rule_are_explicit() -> None:
    for run in ("32715861222", "32716610143", "32718007962"):
        assert run in TEXT
    assert "Do not retry a fourth download adapter" in TEXT


def test_published_counterexample_is_separated_from_project_reanalysis() -> None:
    assert "external falsification example" in TEXT
    assert "must **not** be represented as a new held-out result" in TEXT
    assert "landscape context can directly predict seed production even when visitation does not" in TEXT
