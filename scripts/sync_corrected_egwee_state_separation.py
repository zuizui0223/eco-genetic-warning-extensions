from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
EGWEE_COMMIT = "165dad4d3c132e0982b4e5e722fb6405e7cca957"


def replace_required(path: Path, old: str, new: str, minimum: int = 1) -> None:
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n < minimum:
        raise AssertionError(f"{path}: expected >= {minimum} occurrences of {old!r}, got {n}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def main() -> None:
    # Canonical evidence manifest: corrected 3-primary-cluster inference + separate ML015 gradient support.
    manifest_path = ROOT / "manuscript/nee_flagship_source_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    src = manifest["natural_state_separation_source"]
    src.update({
        "commit": EGWEE_COMMIT,
        "n_independent_primary_clusters": 3,
        "n_primary_effects": 9,
        "primary_fisher_statistic": 18.0086,
        "primary_fisher_df": 6,
        "primary_combined_p": 0.00621,
        "decision": "reject_primary_binary_layer_exchangeability_with_separate_gradient_support",
        "gradient_generalisation_cluster": "ML015",
        "gradient_generalisation_cluster_p": 0.00256953,
        "claim_ceiling": "Primary natural inference uses only ML001-ML003 fragmented-versus-reference Hedges-g clusters. ML015 Eucalyptus wandoo is separate Fisher-z gradient generalisation evidence and is not included in the primary Fisher combination; neither effect magnitudes nor p-values are combined across those effect families."
    })
    for stale in ["n_independent_clusters", "fisher_statistic", "fisher_df", "combined_p"]:
        src.pop(stale, None)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    article = ROOT / "manuscript/nee_flagship_article.md"
    replacements = [
        ("Natural evidence rejected exchangeability (Fisher chi-square(8)=27.70, p=5.35e-4).",
         "Three primary natural binary/contrast systems rejected layer exchangeability (Fisher chi-square(6)=18.01, p=0.00621), with separate gradient support."),
        ("A covariance-aware synthesis of four multilayer systems (*Serapias*, *Brosimum*, *Spondias* and *Eucalyptus wandoo*) rejected exchangeability of within-system fragmentation responses (Fisher chi-square(8)=27.70, p=5.35e-4) without pooling incompatible effect-size magnitudes. Natural data therefore test state separation; operator-level causation remains a finite-model question.",
         "A covariance-aware synthesis of three independently admitted fragmented-versus-reference systems (*Serapias*, *Brosimum* and *Spondias*) rejected exchangeability of within-system biological responses (Fisher chi-square(6)=18.01, p=0.00621) on their common Hedges-g family. Separately, *Eucalyptus wandoo* supplied Fisher-z gradient generalisation support (cluster p=0.00257). The gradient evidence is not included in the primary Fisher combination. Natural data therefore test state separation; operator-level causation remains a finite-model question."),
        ("EGWEE retained four independent covariance-aware fragmentation clusters: *Serapias lingua* (C/F/G_adult), *Brosimum alicastrum* (C/F), *Spondias purpurea* (C/G_adult/G_offspring) and *Eucalyptus wandoo* (I/F/G_adult). Cluster-level evidence rejected general layer exchangeability (Fisher chi-square(8)=27.700, p=0.000535). In *E. wandoo*, the same fragmentation-severity axis increased pollen-tube quantity while reducing seeds per fruit (I-F z=3.009, p=0.00262). Thus natural fragmentation responses are not generally interchangeable measurements of one scalar deterioration state; this result does not imply a universal ordering or common effect magnitude.",
         "EGWEE retained three primary covariance-aware fragmented-versus-reference clusters on a common Hedges-g family: *Serapias lingua* (C/F/G_adult), *Brosimum alicastrum* (C/F) and *Spondias purpurea* (C/G_adult/G_juvenile/G_seed). Their independent cluster-level tests rejected primary binary/contrast layer exchangeability (Fisher chi-square(6)=18.009, p=0.00621). Separately, *Eucalyptus wandoo* was analysed only on the frozen Fisher-z gradient scale: fragmentation severity was associated with increased pollen-tube quantity but reduced seeds per fruit, with Bonferroni cluster p=0.00257. The gradient cluster is not included in the primary Fisher combination. Thus natural fragmentation responses are not generally interchangeable measurements of one scalar deterioration state; this result does not imply a universal ordering or common effect magnitude."),
        ("four independent covariance-aware natural systems reject the general layer-exchangeability null",
         "three primary covariance-aware natural systems reject the binary/contrast layer-exchangeability null, with separate gradient generalisation support"),
        ("four independent covariance-aware multilayer fragmentation clusters / 12 primary effects",
         "three independent primary fragmented-versus-reference clusters / 9 primary effects, plus one separate gradient generalisation cluster"),
        ("Fisher chi-square(8)=27.70024526, p=0.0005347329",
         "primary Fisher chi-square(6)=18.0086, p=0.00621; separate ML015 gradient cluster p=0.00256953"),
        ("Fisher chi-square(8)=27.70, p=5.35e-4",
         "primary Fisher chi-square(6)=18.01, p=0.00621; separate gradient cluster p=0.00257"),
        ("Fisher chi-square(8)=27.700, p=0.000535",
         "primary Fisher chi-square(6)=18.009, p=0.00621; separate gradient cluster p=0.00257"),
        ("four-cluster state-separation synthesis complete",
         "three-primary-cluster state-separation synthesis complete; ML015 retained as separate gradient support"),
        ("empirical multilevel synthesis complete for the four-cluster state-separation result",
         "empirical multilevel synthesis complete for the three-primary-cluster result with separate ML015 gradient support"),
    ]
    for old, new in replacements:
        text = article.read_text(encoding="utf-8")
        if old in text:
            article.write_text(text.replace(old, new), encoding="utf-8")

    # Submission surfaces / routers.
    paths = [
        ROOT / "manuscript/nee_flagship_cover_letter.md",
        ROOT / "manuscript/nee_flagship_submission_metadata.md",
        ROOT / "manuscript/nee_flagship_display_plan.md",
        ROOT / "manuscript/NEE_EGWEE_Q1_INTEGRATION_2026-09-13.md",
        ROOT / "README.md",
        ROOT / "manuscript/README.md",
        ROOT / "manuscript/PUBLICATION_LANES.md",
        ROOT / "manuscript/EG_SERIES_SUBMISSION_STATUS_2026-09-08.md",
    ]
    generic = [
        ("four independent multilayer fragmentation systems rejected general layer exchangeability (Fisher chi-square(8)=27.70, p=5.35e-4), while keeping incompatible Hedges-g and standardized-gradient magnitudes unpooled",
         "three independent primary fragmented-versus-reference systems rejected layer exchangeability on the common Hedges-g family (Fisher chi-square(6)=18.01, p=0.00621), while Eucalyptus wandoo separately supported gradient generalisation (cluster p=0.00257)"),
        ("four independent covariance-aware multilayer fragmentation clusters / 12 primary effects", "three independent primary fragmented-versus-reference clusters / 9 primary effects, plus one separate ML015 gradient generalisation cluster"),
        ("four-cluster state-separation synthesis complete", "three-primary-cluster state-separation synthesis complete; ML015 separate gradient support"),
        ("four-cluster state-separation result complete", "three-primary-cluster state-separation result complete; ML015 separate gradient support"),
        ("empirical multilevel synthesis complete for the four-cluster state-separation result", "empirical multilevel synthesis complete for the three-primary-cluster result with separate ML015 gradient support"),
        ("Fisher chi-square(8)=27.70024526, p=0.0005347329", "primary Fisher chi-square(6)=18.0086, p=0.00621; separate ML015 gradient cluster p=0.00256953"),
        ("Fisher chi-square(8)=27.70, p=5.35e-4", "primary Fisher chi-square(6)=18.01, p=0.00621; separate gradient cluster p=0.00257"),
        ("Fisher chi-square(8)=27.700, p=0.000535", "primary Fisher chi-square(6)=18.009, p=0.00621; separate gradient cluster p=0.00257"),
        ("four independent covariance-aware multilayer systems", "three independent primary covariance-aware fragmented-versus-reference systems"),
        ("four independent covariance-aware natural systems", "three independent primary covariance-aware natural systems"),
        ("four independent natural fragmentation clusters", "three independent primary natural fragmentation clusters"),
        ("four-cluster", "three-primary-cluster"),
    ]
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in generic:
            text = text.replace(old, new)
        # Explicitly preserve separate gradient evidence when a surface still lists Eucalyptus as primary.
        text = text.replace("Serapias, Brosimum, Spondias and Eucalyptus wandoo", "Serapias, Brosimum and Spondias, with Eucalyptus wandoo analysed separately on the gradient scale")
        text = text.replace("Serapias / Brosimum / Spondias / Eucalyptus wandoo", "Serapias / Brosimum / Spondias primary; Eucalyptus wandoo separate gradient")
        path.write_text(text, encoding="utf-8")

    # Compliance checker must enforce the corrected family boundary.
    check = ROOT / "scripts/check_nee_flagship_compliance.py"
    text = check.read_text(encoding="utf-8")
    text = text.replace('assert natural_q1["n_independent_clusters"] == 4', 'assert natural_q1["n_independent_primary_clusters"] == 3')
    text = text.replace('assert natural_q1["n_primary_effects"] == 12', 'assert natural_q1["n_primary_effects"] == 9')
    text = text.replace('assert abs(natural_q1["combined_p"] - 0.0005347329) < 1e-12', 'assert abs(natural_q1["primary_combined_p"] - 0.00621) < 1e-12\n    assert abs(natural_q1["gradient_generalisation_cluster_p"] - 0.00256953) < 1e-12')
    text = text.replace('assert natural_q1["decision"] == "reject_general_layer_exchangeability"', 'assert natural_q1["decision"] == "reject_primary_binary_layer_exchangeability_with_separate_gradient_support"')
    text = text.replace('("Fisher chi-square(8)=27.70", "p=5.35e-4", "p=0.000535", "delta NLL M1-M0=-0.0003211")', '("Fisher chi-square(6)=18.01", "p=0.00621", "p=0.00257", "delta NLL M1-M0=-0.0003211")')
    check.write_text(text, encoding="utf-8")

    # NEE workflow pins the corrected EGWEE canonical source and keeps the packet source canonical.
    wf = ROOT / ".github/workflows/nee-math-first-flagship.yml"
    text = wf.read_text(encoding="utf-8")
    text = text.replace("63906a64fab01562dc49ab99907a733b403ea80a", EGWEE_COMMIT)
    wf.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
