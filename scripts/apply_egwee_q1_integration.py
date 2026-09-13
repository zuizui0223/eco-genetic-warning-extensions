from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / "manuscript/nee_flagship_article.md"
CHECK = ROOT / "scripts/check_nee_flagship_compliance.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"{label}: expected one match, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    article = ARTICLE.read_text(encoding="utf-8")

    abstract_old = (
        "Fixed-area fragmentation separates potential viability from realised occupancy, while matched marginals can still conceal a 49-fold difference in support variance and a 0.2543 difference in exact next interaction state."
    )
    abstract_new = abstract_old + (
        " Natural evidence rejected exchangeability (Fisher chi-square(8)=27.70, p=5.35e-4)."
    )
    article = replace_once(article, abstract_old, abstract_new, "abstract natural Q1")

    intro_old = (
        "This distinction matters because contrasting natural outcomes need not imply contradictory fragmentation effects. Local interaction limitation can remain uncompensated; movement can reorganize and restore pollen transfer; current mating processes can deteriorate while adult genetic state retains historical connectivity; and ecological and genetic deterioration can sometimes move together. We use *Crepis sancta*, Miyake-jima *Camellia–Zosterops*, *Conospermum undulatum* and *Spondias purpurea* only to motivate these possibilities. They are not validation data for the finite model."
    )
    intro_new = (
        "Natural fragmentation provides an independent test of the same premise. A covariance-aware synthesis of four multilayer systems (*Serapias*, *Brosimum*, *Spondias* and *Eucalyptus wandoo*) rejected exchangeability of within-system fragmentation responses (Fisher chi-square(8)=27.70, p=5.35e-4) without pooling incompatible effect-size magnitudes. Natural data therefore test state separation; operator-level causation remains a finite-model question."
    )
    article = replace_once(article, intro_old, intro_new, "introduction natural synthesis")

    q2_heading = "### Question 2 — Given state separation, what determines divergent futures and predicts fate?\n"
    natural_q1 = (
        "### Independent natural systems also rejected layer exchangeability\n\n"
        "EGWEE retained four independent covariance-aware fragmentation clusters: *Serapias lingua* (C/F/G_adult), *Brosimum alicastrum* (C/F), *Spondias purpurea* (C/G_adult/G_offspring) and *Eucalyptus wandoo* (I/F/G_adult). Cluster-level evidence rejected general layer exchangeability (Fisher chi-square(8)=27.700, p=0.000535). In *E. wandoo*, the same fragmentation-severity axis increased pollen-tube quantity while reducing seeds per fruit (I-F z=3.009, p=0.00262). Thus natural fragmentation responses are not generally interchangeable measurements of one scalar deterioration state; this result does not imply a universal ordering or common effect magnitude.\n\n"
    )
    article = replace_once(article, q2_heading, natural_q1 + q2_heading, "Q1 natural result insertion")

    q2_transition = (
        q2_heading
        + "\nNatural data establish that state separation is not peculiar to the finite construction; the finite closure is then used to identify why separated states diverge.\n"
    )
    article = replace_once(article, q2_heading, q2_transition, "Q1-to-Q2 transition")

    old_natural_discussion = (
        "This framework gives a sharper interpretation to contrasting natural systems without treating them as validation data. In *Crepis sancta*, low local flowering density is associated with reduced pollinator activity and reproduction despite broader movement, consistent with insufficient buffering. On Miyake-jima, reduced floral resources are accompanied by broader *Zosterops* movement and pollen mixing, a plausible real-world analogue of recoupling in which movement repairs local functional mismatch. In *Conospermum undulatum*, current pollen connectivity and reproduction can deteriorate while adult neutral genetics retain a historical signal, adding a memory axis that the current finite closure does not model explicitly. *Spondias purpurea* illustrates more coordinated decline across visitation, pollen flow, reproductive function and younger-cohort genetics. These systems motivate measurements of sorting, buffering, recoupling and memory; they do not replicate the simulator.\n\n"
        "The same logic revises the earlier urban–island comparison. `Urban`, `island`, forest fragment and volcanic disturbance are upstream histories, not mechanistic states. Different histories can generate similar or different balances of local selection, recruitment, movement, mating opportunity and demographic feedback. Existing Honshu–Izu and Zurich archives cannot establish a universal urban–island convergence law because study identity, taxa, state coordinates and endpoints are not harmonized. A prospective comparison should instead ask which operator is active and whether buffering and recoupling keep pace with local sorting and demographic headroom loss."
    )
    new_natural_discussion = (
        "The natural and finite results therefore carry different inferential loads. EGWEE supplies the portable empirical result that fragmentation responses are not generally exchangeable across biological layers; it does not validate the model's sorting, buffering, recoupling or density operators. Conversely, the first locked natural prospective transfer of the specific strongest-refuge predictor was null after contemporaneous marginals (delta NLL M1-M0=-0.0003211, species-bootstrap 95% CI [-0.0009825,+0.0003422]). We retain that result as a portability boundary rather than promoting its secondary persistence-only direction or treating the finite AUC 0.9273 as naturally validated."
    )
    article = replace_once(article, old_natural_discussion, new_natural_discussion, "discussion natural synthesis replacement")

    methods_old = (
        "Published natural systems and the separate natural-data measurement programme are Discussion-level projections only."
    )
    methods_new = (
        "EGWEE supplies independent natural evidence for Question 1 only; the natural strongest-refuge test remains a null portability boundary, and all operator-level causal claims remain finite-closure results."
    )
    article = replace_once(article, methods_old, methods_new, "methods evidence architecture")
    ARTICLE.write_text(article, encoding="utf-8")

    check = CHECK.read_text(encoding="utf-8")
    check = replace_once(check, 'assert manifest["schema_version"] == 7', 'assert manifest["schema_version"] == 8', "manifest schema")
    check = replace_once(
        check,
        '    for token in (\n        "Crepis", "Miyake", "Zosterops", "Conospermum", "Spondias",\n        "Honshu", "Zurich", "Toronto", "Oenothera", "Eschscholzia",\n        "Mallorca", "Campanula americana",\n    ):\n        assert token not in results, f"natural projection leaked into Results: {token}"\n',
        '    # Natural data may now enter Results only through the completed EGWEE Q1 synthesis.\n    for token in (\n        "Crepis", "Miyake", "Zosterops", "Conospermum",\n        "Honshu", "Zurich", "Toronto", "Oenothera", "Eschscholzia",\n        "Mallorca", "Campanula americana",\n    ):\n        assert token not in results, f"non-Q1 natural projection leaked into Results: {token}"\n    for token in ("Serapias", "Brosimum", "Spondias", "Eucalyptus wandoo", "p=0.000535"):\n        assert token in results, f"natural Q1 synthesis missing from Results: {token}"\n',
        "natural result firewall",
    )
    check = replace_once(
        check,
        '    assert len(manifest["projection_sources"]) == 1\n    assert len(manifest["claim_firewalls"]) >= 18\n',
        '    natural_q1 = manifest["natural_state_separation_source"]\n    assert natural_q1["decision"] == "reject_general_layer_exchangeability"\n    assert natural_q1["n_independent_clusters"] == 4\n    assert natural_q1["n_primary_effects"] == 12\n    assert abs(natural_q1["combined_p"] - 0.0005347329) < 1e-12\n    natural_q2 = manifest["natural_q2_boundary"]\n    assert natural_q2["status"] == "no_detected_incremental_strongest_refuge_information"\n    assert natural_q2["species_bootstrap_95_ci"][0] < 0 < natural_q2["species_bootstrap_95_ci"][1]\n    assert len(manifest["claim_firewalls"]) >= 12\n',
        "manifest natural evidence contract",
    )
    anchor = '    for token in required:\n        assert token in article, token\n'
    addition = anchor + '\n    for token in ("Fisher chi-square(8)=27.70", "p=5.35e-4", "p=0.000535", "delta NLL M1-M0=-0.0003211"):\n        assert token in article, token\n'
    check = replace_once(check, anchor, addition, "article natural evidence requirements")
    check = replace_once(
        check,
        '    for token in ("Crepis", "Miyake", "Conospermum", "Spondias", "urban–island"):\n        assert token in discussion or token in article[: article.index("## Results")], token\n',
        '    # Qualitative natural anchors are superseded in the flagship by the formal EGWEE Q1 synthesis.\n    for token in ("Serapias", "Brosimum", "Spondias", "Eucalyptus wandoo"):\n        assert token in results or token in article[: article.index("## Results")], token\n',
        "natural projection presence contract",
    )
    CHECK.write_text(check, encoding="utf-8")


if __name__ == "__main__":
    main()
