from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_integrated_story_contains_locked_headline_results() -> None:
    text = _read("manuscript/integrated_story.md").lower()
    required = ("2,269", "3,375", "20,250", "322", "242", "84", "323", "12 lags", "0.540", "0.335")
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


def test_main_text_centres_event_regime_feasibility() -> None:
    text = _read("manuscript/main_text.md")
    lower = text.lower()
    assert text.splitlines()[0] == "# Eco-genetic regimes govern when genetic early warning can be validated"
    assert "strict calibration selected no common validation domain" in lower
    assert "genetic warning therefore depends first on event-regime feasibility" in lower
    assert "warning portability across calibrated eco-genetic domains" in lower
    assert "### Stage I" not in text
    assert "### Stage II" not in text
    assert "### Stage III" not in text
    source = text.index("### Recurrent-transition direction changed whether a high-trait source could be established")
    regimes = text.index("### The common deterioration family separated into rapid-loss, persistence and heterogeneous regimes")
    fragmentation = text.index("### Fragmentation produced large, consistent reductions")
    benchmark = text.index("### Relative genetic erosion preceded functional-trait loss")
    assert source < regimes < fragmentation < benchmark


def test_stage3_timing_claim_uses_direct_difference_uncertainty_and_selection_boundary() -> None:
    text = _read("manuscript/main_text.md")
    assert "conditional estimand" in text.lower()
    assert "`−97.0` to `−3.5` generations" in text
    assert "`−97.0` to `−4.5`" in text
    assert "all six directional-minus-symmetric 95% difference intervals included zero" in text
    assert "Figure 4 therefore provides the primary Stage III timing evidence" in text
    assert "Figure 6 is retained as a conditional diagnostic" in text
    assert "event-regime feasibility precedes warning comparison" in text


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
        "Gomulkiewicz & Holt 1995", "Legrand et al. 2017", "Field & Welsh 2007",
        "Andersen et al. 2012", "Frankham 2005", "Lipsitch et al. 2010",
    )
    for token in required:
        assert token in text


def test_verified_reference_list_covers_every_citation_family() -> None:
    references = _read("manuscript/references.md")
    required = (
        "doi:10.1038/nature08227", "doi:10.1890/05-0386", "doi:10.1016/j.tree.2006.08.009",
        "doi:10.1111/ecog.02537", "doi:10.1111/1365-2435.13241", "doi:10.1098/rstb.2018.0238",
        "doi:10.1146/annurev-ecolsys-110316-023011", "doi:10.1111/j.1467-9868.2007.00593.x",
        "doi:10.1093/ije/dyr213", "doi:10.1016/j.biocon.2005.05.002",
        "doi:10.1097/EDE.0b013e3181d61eeb",
    )
    for token in required:
        assert token in references


def test_table_captions_lock_statistical_units_and_numbering() -> None:
    builder = _read("scripts/build_submission_bundle.py")
    captions = _read("manuscript/table_captions.md")
    assert "references.md" in builder
    assert "table_captions.md" in builder
    for label in ("Table S1.", "Table S2.", "Table S3.", "Table S4.", "Table S5."):
        assert label in captions
    assert "Table 1." not in captions
    assert "Table 2." not in captions
    assert "whole-trajectory bootstrap intervals" in captions
    assert "directional-minus-symmetric median differences" in captions
    assert "not a test of warning performance" in captions
