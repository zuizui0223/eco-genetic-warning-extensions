from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _plain(text: str) -> str:
    return text.lower().replace("**", "")


def test_repository_exposes_one_condition_first_science_spine() -> None:
    root = _read("README.md")
    program = _read("docs/HYPOTHESIS_PROGRAM.md")
    workspace = _read("manuscript/README.md")
    for text in (root, program, workspace):
        assert all(token in text for token in ("C0", "C1", "C2", "C3", "C4"))
    assert "Warning is a downstream conditional outcome" in root
    assert "condition-first" in program.lower()
    assert "protocol chronology" in workspace.lower()


def test_interaction_support_and_connectivity_are_not_mislabeled() -> None:
    root = _plain(_read("README.md"))
    program = _plain(_read("docs/HYPOTHESIS_PROGRAM.md"))
    claims = _plain(_read("manuscript/claim_evidence_map.md"))
    application = _plain(_read("manuscript/urban_island_regime_tests.md"))
    assert "not partner richness" in root
    assert "network simplification" in application
    assert "allele-frequency mixing" in root
    assert "not demographic" in claims
    assert "m=.10` is a reproducible" not in claims
    assert "historical_m010_heterogeneity_not_freshly_replicated" in program


def test_main_text_retains_locked_headline_results_and_phase_u_correction() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    for token in ("2,269", "3,375", "322", "242", "84", "1,037", "0.540", "0.335"):
        assert token in text
    for token in ("0.682", "0.407", "0.273", "0.0205", "0.745", "0.694", "0.499", "0.573", "0.598"):
        assert token in text
    assert "incidence frontier" in lower
    assert "historical r3/r4 labels are retained as protocol facts" in lower
    assert "historical_m010_heterogeneity_not_freshly_replicated" in text
    assert "not supported as an independently reproducible `m=.10` heterogeneity effect" in lower
    assert "not a single-factor effect of transition direction" in lower
    assert "not demographic migration" in lower
    assert "### Stage I" not in text
    assert "### Stage II" not in text
    assert "### Stage III" not in text


def test_superseded_phase_narratives_stay_removed() -> None:
    removed = (
        "manuscript/integrated_story.md", "manuscript/integrated_abstract_and_outline.md",
        "manuscript/integrated_claim_evidence_map.md", "manuscript/hypothesis_condition_phase_map.md",
        "manuscript/main_vs_supplement.md", "manuscript/frontier_refinement_phase_a_results.md",
        "manuscript/frontier_refinement_phase_b_results.md", "manuscript/frontier_reproducibility_phase_c_results.md",
        "manuscript/migration_condition_phase_e_results.md", "manuscript/r4_width_phase_d_results.md",
        "manuscript/protocol002_condition_map_results.md", "manuscript/protocol002_existing_condition_frontier.md",
        "manuscript/el_editorial_pass.md", "manuscript/integrated_introduction.md",
        "manuscript/integrated_discussion.md", "manuscript/gap_novelty_ecological_significance.md",
        "manuscript/results_stage3.md", "manuscript/supervisor_first_draft.md",
        "manuscript/literature_gap_review.md", "docs/CONDITION_RECOVERY_CLOSURE.md",
    )
    for path in removed:
        assert not (ROOT / path).exists(), path
    assert len(removed) == 20
    assert (ROOT / "manuscript/display_allocation.md").exists()
    assert (ROOT / "manuscript/main_text.md").exists()
    assert (ROOT / "manuscript/warning_evaluability_prior_art.md").exists()
    assert (ROOT / "manuscript/core_reference_map.md").exists()


def test_submission_bundle_keeps_provenance_and_condition_evidence() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    captions = _read("manuscript/figure_captions.md")
    assert "claim_evidence_map.md" in builder
    assert "artifact_index.md" in builder
    assert "stage3_trajectory_endpoint_records.csv" in builder
    for number in range(1, 7):
        assert f"## Figure {number}." in captions
    assert "Endpoint rows share trajectories" in captions
    assert "failed fresh-seed replication" in captions


def test_phase_chronology_is_not_a_manuscript_source_of_truth() -> None:
    workspace = _read("manuscript/README.md")
    lower = workspace.lower()
    assert "phase-specific result notes" in lower
    assert "must not compete with the current sources" in lower
    assert "results sections are named by biological result" in lower
