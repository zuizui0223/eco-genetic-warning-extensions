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
        " Independently, four covariance-aware natural fragmentation systems rejected general exchangeability of biological layer responses (Fisher chi-square(8)=27.70, p=5.35e-4)."
    )
    article = replace_once(article, abstract_old, abstract_new, "abstract natural Q1")

    intro_old = (
        "This distinction matters because contrasting natural outcomes need not imply contradictory fragmentation effects. Local interaction limitation can remain uncompensated; movement can reorganize and restore pollen transfer; current mating processes can deteriorate while adult genetic state retains historical connectivity; and ecological and genetic deterioration can sometimes move together. We use *Crepis sancta*, Miyake-jima *Camellia–Zosterops*, *Conospermum undulatum* and *Spondias purpurea* only to motivate these possibilities. They are not validation data for the finite model."
    )
    intro_new = (
        "Natural fragmentation studies provide an independent test of the premise that biological layers cannot generally be collapsed onto one deterioration coordinate. A covariance-aware synthesis of four independent multilayer systems (*Serapias lingua*, *Brosimum alicastrum*, *Spondias purpurea* and *Eucalyptus wandoo*) rejected exchangeability of within-system fragmentation responses across interaction or movement, reproductive and genetic layers (Fisher chi-square(8)=27.70, p=5.35e-4). The synthesis combines cluster-level evidence rather than pooling incompatible Hedges-g and standardized-gradient magnitudes. We therefore use natural data to test the general state-separation premise, while reserving operator-level causal explanation for the declared finite model."
    )
    article = replace_once(article, intro_old, intro_new, "introduction natural synthesis")

    q2_heading = "### Question 2 — Given state separation, what determines divergent futures and predicts fate?\n"
    natural_q1 = (
        "### Independent natural systems also rejected layer exchangeability\n\n"
        "We then asked whether the state-separation premise was confined to the finite closure. EGWEE retained four independent natural fragmentation clusters with paired within-system dependence: *Serapias lingua* (C/F/G_adult), *Brosimum alicastrum* (C/F), *Spondias purpurea* (C/G_adult/G_offspring) and *Eucalyptus wandoo* (I/F/G_adult). All admitted layer pairs were compared using stored within-cluster covariance, pairwise p-values were Bonferroni-adjusted within cluster, and only the four independent cluster-level p-values were combined across systems. Serapias (p=0.00355) and E. wandoo (p=0.00786) individually rejected exchangeability; Brosimum (p=0.199) and Spondias (p=0.174) did not. Across all four systems, Fisher chi-square(8)=27.700, p=0.000535, rejecting general layer exchangeability. In E. wandoo, the same fragmentation-severity axis increased pollen-tube quantity while reducing seeds per fruit (I-F z=3.009, p=0.00262). These data do not establish a universal ordering; they show that biological fragmentation responses are not generally interchangeable measurements of one scalar deterioration state.\n\n"
    )
    article = replace_once(article, q2_heading, natural_q1 + q2_heading, "Q1 natural result insertion")

    q2_transition = (
        q2_heading
        + "\nThe natural synthesis establishes that state separation is not merely a peculiarity of the finite construction. It does not identify why separated states diverge or which hidden organization predicts fate. Those are mechanistic questions, which we address in the finite closure where state variables and life-cycle operators can be intervened on exactly.\n"
    )
    article = replace_once(article, q2_heading, q2_transition, "Q1-to-Q2 transition")

    discussion_marker = "## Discussion\n\n"
    discussion_insert = (
        "The evidence now separates three levels of inference. First, the portable empirical result is that biological fragmentation responses are not generally exchangeable across layers: four independent covariance-aware natural systems reject the general layer-exchangeability null. Second, the finite closure supplies a mechanistic explanation for how relational state can matter, through cross-layer covariance, q-dependent sorting, recruitment buffering, direct recoupling and density feedback. Third, the first locked natural prospective transfer of the specific strongest-refuge predictor did not detect incremental future-occupancy information after contemporaneous marginals (delta NLL M1-M0=-0.0003211, species-bootstrap 95% CI [-0.0009825,+0.0003422]). We retain that null as a portability boundary rather than promoting the secondary persistence-only direction or treating the finite AUC 0.9273 as naturally validated.\n\n"
    )
    article = replace_once(article, discussion_marker, discussion_marker + discussion_insert, "discussion three-level boundary")
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
    CHECK.write_text(check, encoding="utf-8")


if __name__ == "__main__":
    main()
