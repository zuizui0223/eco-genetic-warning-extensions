from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_repository_exposes_one_condition_first_science_spine() -> None:
    root = _read("README.md")
    program = _read("docs/HYPOTHESIS_PROGRAM.md")
    workspace = _read("manuscript/README.md")
    for text in (root, program, workspace):
        assert "C0" in text and "C1" in text and "C2" in text and "C3" in text and "C4" in text
    assert "Warning is therefore a downstream conditional outcome" in root
    assert "condition-first" in program.lower()
    assert "protocol chronology" in workspace.lower()


def test_interaction_support_is_not_mislabeled_as_network_simplification() -> None:
    root = _read("README.md")
    program = _read("docs/HYPOTHESIS_PROGRAM.md")
    assert "not partner richness" in root
    assert "not partner richness" in program
    assert "network dimensionality" in program
    assert "Phase F" in program
    assert "3.0, 4.5, 6.0" in program


def test_main_text_retains_locked_headline_results_and_boundaries() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    for token in ("2,269", "3,375", "322", "242", "84", "r4 exists", "0.571", "0.540", "0.335", "1,037"):
        assert token in text.lower() if token == "r4 exists" else token in text
    assert "not an isolated effect of recurrent-transition direction" in lower
    assert "not demographic migration" in lower or "not demographic" in lower
    assert "### Stage I" not in text
    assert "### Stage II" not in text
    assert "### Stage III" not in text


def test_submission_bundle_keeps_provenance_and_statistical_units() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    captions = _read("manuscript/figure_captions.md")
    assert "claim_evidence_map.md" in builder
    assert "artifact_index.md" in builder
    assert "stage3_trajectory_endpoint_records.csv" in builder
    for number in range(1, 7):
        assert f"## Figure {number}." in captions
    assert "Endpoint rows share trajectories" in captions


def test_verified_reference_list_covers_load_bearing_families() -> None:
    references = _read("manuscript/references.md")
    required = (
        "doi:10.1038/nature08227",
        "doi:10.1890/05-0386",
        "doi:10.1111/ecog.02537",
        "doi:10.1111/j.1461-0248.2008.01179.x",
        "doi:10.1111/mec.15221",
        "doi:10.1146/annurev-ecolsys-102221-044616",
    )
    for token in required:
        assert token in references


def test_phase_chronology_is_not_a_manuscript_source_of_truth() -> None:
    workspace = _read("manuscript/README.md")
    assert "Phase-specific historical documents are provenance only" not in workspace  # old wording removed
    assert "phase-specific result notes" in workspace.lower()
    assert "must not override" in workspace.lower()
