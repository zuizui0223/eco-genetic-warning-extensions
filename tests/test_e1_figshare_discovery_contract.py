from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (ROOT / "scripts" / "fetch_e1_izu_figshare.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "e1-izu-figshare-discovery.yml").read_text(encoding="utf-8")


def test_e1_source_is_exact_public_archive() -> None:
    assert "ARTICLE_ID = 25025000" in SCRIPT
    assert "ARTICLE_VERSION = 1" in SCRIPT
    assert 'RESOURCE_DOI = "10.6084/m9.figshare.25025000.v1"' in SCRIPT
    assert "api.figshare.com/v2/articles" in SCRIPT


def test_discovery_is_schema_audit_not_result_claim() -> None:
    assert "Discovery only. No biological claim is made" in SCRIPT
    assert "structured_candidates" in SCRIPT
    assert "r_hints" in SCRIPT
    assert "tabular" in SCRIPT


def test_external_data_are_not_committed_by_workflow() -> None:
    assert "actions/upload-artifact@v4" in WORKFLOW
    assert "_external/e1_izu_figshare" in WORKFLOW
    assert "git add" not in WORKFLOW
    assert "git commit" not in WORKFLOW
    assert "git push" not in WORKFLOW


def test_workflow_fails_if_archive_is_empty() -> None:
    assert "Figshare item returned no files" in WORKFLOW
    assert "archive inventory is empty" in WORKFLOW
    assert "if-no-files-found: error" in WORKFLOW
