from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_integrated_story_contains_locked_headline_results() -> None:
    text = _read("manuscript/integrated_story.md").lower()
    required = (
        "2,269", "3,375", "20,250", "322", "242", "84",
        "0.35", "r4", "0.540", "0.335", "323", "12 lags",
    )
    for token in required:
        assert token in text


def test_integrated_claims_preserve_parent_extension_boundary() -> None:
    text = _read("manuscript/integrated_claim_evidence_map.md").lower()
    assert "prohibited claims" in text
    assert "no_domain_selected" in text
    assert "do not pool their trajectories" in text
    assert "separately declared" in text


def test_main_supplement_allocation_keeps_debug_history_out() -> None:
    text = _read("manuscript/main_vs_supplement.md")
    assert "implementation debugging" in text
    assert "temporary GitHub Actions outages" in text
    assert "out of the scientific manuscript" in text


def test_main_text_follows_condition_recovered_four_question_story() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    assert text.splitlines()[0] == "# Eco-genetic regimes govern when genetic early warning can be validated"
    assert "conditions of estimability" in lower
    assert "r4 exists" in lower
    assert "warning estimability is therefore conditional not only on recurrent state turnover but also on effective genetic connectivity" in lower
    assert "non-portability across calibrated eco-genetic domains" in lower
    assert "### Stage I" not in text
    assert "### Stage II" not in text
    assert "### Stage III" not in text

    fragmentation = text.index("### Fragmentation disrupted an interaction-supported functional state")
    benchmark = text.index("### Genetic erosion could precede functional loss")
    source_regime = text.index("### Recurrent state turnover changed both source feasibility and the way function was lost")
    r4 = text.index("### Warning-blind refinement recovered a narrow reproducible R4 event regime")
    connectivity = text.index("### Effective genetic connectivity moved the same R4 anchor into a heterogeneous event regime")
    portability = text.index("### Warning behaviour was not fully portable across independently calibrated domains")
    assert fragmentation < benchmark < source_regime < r4 < connectivity < portability

    for number in range(1, 7):
        assert f"Figure {number}" in text


def test_stage3_portability_claim_retains_direct_uncertainty_and_selection_boundary() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    assert "conditional positive lead-time medians" in lower
    assert "lead-time medians condition on observing both events and a leading warning" in lower
    assert "full-denominator event incidence and warning availability are treated as more primary" in lower
    assert "0.540" in text
    assert "0.335" in text
    assert "all six direct timing-difference intervals included zero" in lower
    assert "not an isolated effect of recurrent-transition direction" in lower
    assert "(Figure 6)" in text


def test_stage3_per_trajectory_records_are_committed_for_external_audit() -> None:
    path = ROOT / "manuscript/tables/stage3_trajectory_endpoint_records.csv"
    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1201
    header = lines[0]
    for token in ("trajectory_seed", "warning_time", "trait_loss_time", "lead_time_trait_minus_warning", "category"):
        assert token in header


def test_workspace_does_not_present_mutation_direction_as_sole_novelty() -> None:
    text = _read("manuscript/README.md")
    assert "Genetic-warning reliability is not a portable property" in text
    assert "one mechanism that reshapes this closure" in text
    assert "Mutation direction governs genetic early-warning reliability" not in text
    assert "Stage III does not identify the isolated causal effect" in text


def test_submission_figure_one_is_closure_first() -> None:
    text = _read("scripts/build_submission_bundle.py")
    assert "Genetic warning emerges from eco-genetic closure" in text
    assert "figure1_eco_genetic_closure.svg" in text
    assert "figure1_mutation_coordinates.svg" not in text
    assert "Stage II candidate-regime composition" not in text


def test_submission_bundle_includes_biological_figure_captions() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    captions = _read("manuscript/figure_captions.md")
    assert "figure_captions.md" in builder
    for number in range(1, 7):
        assert f"## Figure {number}." in captions
    assert "all 15 were retained as `no_domain_selected`" in captions
    assert "Endpoint rows share trajectories" in captions
    assert "Interpret this diagnostic together with full-denominator Figures 4–5" in captions


def test_main_text_contains_load_bearing_citation_roles() -> None:
    text = _read("manuscript/main_text.md")
    required = (
        "Scheffer et al. 2009", "Schwartz et al. 2007", "Soulé et al. 2005",
        "Legrand et al. 2017", "Govaert et al. 2019", "Hastings & Wysham 2010",
        "Boettiger & Hastings 2012, 2013", "Gsell et al. 2016", "Hughes et al. 2008",
        "Whitlock 2014", "Miles et al. 2019", "Youngsteadt & Keighron 2023",
        "Schrader et al. 2021",
    )
    for token in required:
        assert token in text


def test_verified_reference_list_covers_every_citation_family() -> None:
    references = _read("manuscript/references.md")
    required = (
        "doi:10.1038/nature08227", "doi:10.1890/05-0386", "doi:10.1016/j.tree.2006.08.009",
        "doi:10.1111/ecog.02537", "doi:10.1111/1365-2435.13241", "doi:10.1073/pnas.1608242113",
        "doi:10.1111/j.1461-0248.2008.01179.x", "doi:10.1111/1365-2745.12240",
        "doi:10.1111/mec.15221", "doi:10.1146/annurev-ecolsys-102221-044616",
        "doi:10.1111/brv.12782",
    )
    for token in required:
        assert token in references


def test_table_captions_lock_statistical_units_and_numbering() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    captions = _read("manuscript/table_captions.md")
    assert "references.md" in builder
    assert "table_captions.md" in builder
    for label in ("Table S1.", "Table S2.", "Table S3.", "Table S4.", "Table S5.", "Table S6."):
        assert label in captions
    assert "Table 1." not in captions
    assert "Table 2." not in captions
    assert "whole-trajectory bootstrap intervals" in captions
    assert "directional-minus-symmetric median differences" in captions
    assert "not a test of warning performance" in captions
