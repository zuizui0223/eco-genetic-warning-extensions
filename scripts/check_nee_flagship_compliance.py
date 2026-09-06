from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / "manuscript/nee_flagship_article.md"
DISPLAY = ROOT / "manuscript/nee_flagship_display_plan.md"
REFERENCES = ROOT / "manuscript/nee_flagship_references.md"
MANIFEST = ROOT / "manuscript/nee_flagship_source_manifest.json"
MECHANISM = ROOT / "artifacts/relational_mechanism_decomposition/locked_result.json"
EDGE = ROOT / "artifacts/pathway_edge_decomposition/locked_result.json"
FOCUSED = ROOT / "artifacts/allele_sorting_single_edge/locked_result.json"


def words(text: str) -> list[str]:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return re.findall(r"[A-Za-z0-9_α-ωΑ-Ω]+(?:[-–—'][A-Za-z0-9_α-ωΑ-Ω]+)*", text)


def between(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def main() -> None:
    article = ARTICLE.read_text(encoding="utf-8")
    display = DISPLAY.read_text(encoding="utf-8")
    refs = REFERENCES.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    mechanism = json.loads(MECHANISM.read_text(encoding="utf-8"))
    edge = json.loads(EDGE.read_text(encoding="utf-8"))
    focused = json.loads(FOCUSED.read_text(encoding="utf-8"))

    title = "Eco-genetic sorting and buffering shape functional vulnerability under fragmentation"
    assert article.startswith(f"# {title}\n")
    for heading in ("## Abstract", "## Results", "## Discussion", "## Methods"):
        assert heading in article, heading

    abstract_block = between(article, "## Abstract\n", "## Results\n")
    abstract = abstract_block.strip().split("\n\n", 1)[0]
    abstract_n = len(words(abstract))

    after_abstract = article.index("## Abstract\n") + len("## Abstract\n")
    abstract_end = article.index("\n\n", after_abstract)
    methods_start = article.index("## Methods\n")
    main_text = article[abstract_end + 2:methods_start]
    main_n = len(words(main_text))

    results = between(article, "## Results\n", "## Discussion\n")
    discussion = between(article, "## Discussion\n", "## Methods\n")

    assert abstract_n <= 200, abstract_n
    assert main_n <= 3500, main_n

    figures = re.findall(r"^## Figure (\d+)\s", display, flags=re.M)
    assert figures == ["1", "2", "3", "4"], figures
    assert len(figures) <= 6

    ref_entries = [p for p in refs.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    assert len(ref_entries) <= 50, len(ref_entries)

    required = (
        "K > 4",
        "1,037/1,037",
        "T_I=g\\circ\\phi",
        "0.2543",
        "49-fold difference",
        "+5.33",
        "+5.20",
        "6.23 points",
        "4.70 points",
        "+4.20 points",
        "+4.40 points",
        "+13.20 points",
        "+12.73 points",
        "+7.27 points",
        "selection-mediated spatial sorting",
        "recruitment-mediated buffering",
        "failure gate and amplifier",
        "q*=0.625",
        "6,000 paired AA/RR keys per condition",
        "+6.65 points",
        "-0.23 points",
        "+6.883",
        "+5.800,+7.967",
        "resolved single-edge causal contributor",
        "35 observed losses",
        "48 inherited non-event",
        "33 losses",
        "49 fresh non-events",
        "specificity `0`",
        "binary-marker AUC `0.5`",
    )
    for token in required:
        assert token in article, token

    for token in (
        "Crepis", "Miyake", "Zosterops", "Conospermum", "Spondias",
        "Honshu", "Zurich", "Toronto", "Oenothera", "Eschscholzia",
        "Mallorca", "Campanula americana",
    ):
        assert token not in results, f"natural projection leaked into Results: {token}"

    for token in ("Crepis", "Miyake", "Conospermum", "Spondias", "urban–island"):
        assert token in discussion or token in article[: article.index("## Results")], token

    lower = article.casefold()
    for forbidden in (
        "natural examples validate the model",
        "natural data validate the simulator",
        "alignment caused warning failure",
        "fragmentation caused the anti-aligned",
        "generation 20 is a universal",
        "positive alignment is universally protective",
        "support variance is a universal risk score",
        "matching-dependent recruitment pathway",
        "allele-linked recruitment generates the matching advantage",
        "density feedback causes the matching advantage",
        "q-dependent allele sorting is a universal natural mechanism",
    ):
        assert forbidden not in lower, forbidden

    assert manifest["schema_version"] == 5
    assert len(manifest["load_bearing_sources"]) == 5
    assert len(manifest["projection_sources"]) == 1
    assert len(manifest["claim_firewalls"]) >= 15

    assert mechanism["status"] == "locked_from_successful_prospective_workflow_artifact"
    assert mechanism["source"]["workflow_run"] == 34012983845
    assert mechanism["source"]["artifact_id"] == 9983093178
    assert abs(mechanism["analytic_headline"]["AA_RR_support_variance_ratio"] - 49.0) < 1e-12
    assert mechanism["full_feedback_factorial"]["generation_20"]["mismatched_minus_matched_risk"] > 0

    assert edge["status"] == "locked_from_successful_prospective_workflow_artifact"
    assert edge["source"]["workflow_run"] == 34014537015
    assert edge["source"]["artifact_id"] == 9983623440
    assert edge["fresh_q_only_baseline"]["generation_20"]["RR_minus_AA_risk_difference"] > 0
    assert edge["fresh_q_only_baseline"]["generation_40"]["RR_minus_AA_risk_difference"] > 0
    allele = edge["edge_deletions"]["allele_linked_recruitment"]
    assert allele["decision"] == "resolved_countervailing_buffer"
    assert allele["generation_20"]["baseline_minus_deletion_DID"] < 0
    assert allele["generation_40"]["baseline_minus_deletion_DID"] < 0
    joint = edge["edge_deletions"]["joint_local_allele_and_trait_selection"]
    assert joint["generation_40"]["DID_ci95"][0] > 0
    density = edge["edge_deletions"]["density_to_q_feedback"]
    assert density["generation_20"]["AA_loss_rate"] == 0.0
    assert density["generation_20"]["RR_loss_rate"] == 0.0

    assert focused["status"] == "locked_from_successful_prospective_workflow_artifact"
    assert focused["source"]["workflow_run"] == 34016797940
    assert focused["source"]["job"] == 101441868527
    assert focused["source"]["artifact_id"] == 9984306657
    assert focused["source"]["artifact_digest"] == "sha256:61a07cc6a8680a59185537b03abdca85d0f172a65d068ee9661dd9f2fb448c2d"
    assert abs(focused["operator_certificate"]["q_switch"] - 0.625) < 1e-12
    primary = focused["primary_generation_40_DID"]
    assert primary["decision"] == "resolved_positive_sorting_contribution"
    assert primary["n_paired_keys"] == 6000
    assert primary["paired_ci95"][0] > 0
    assert abs(primary["baseline_minus_deletion_DID"] - 0.06883333333333333) < 1e-12
    baseline40 = focused["risk_pairs"]["baseline_local_allele_selection"]["40"]
    deletion40 = focused["risk_pairs"]["delete_local_allele_selection"]["40"]
    assert baseline40["RR_minus_AA_risk_difference"] > 0
    assert deletion40["paired_ci95"][0] < 0 < deletion40["paired_ci95"][1]

    print(f"NEE abstract words: {abstract_n}")
    print(f"NEE main-text words: {main_n}")
    print(f"Main displays: {len(figures)}")
    print(f"References: {len(ref_entries)}")
    print("Resolved-allele-sorting NEE flagship compliance: PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"Resolved-allele-sorting NEE flagship compliance: FAIL — {exc}", file=sys.stderr)
        raise
