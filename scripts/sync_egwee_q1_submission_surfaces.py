from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"{label}: expected one match in {path}, got {n}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def replace_all(path: Path, old: str, new: str, minimum: int, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n < minimum:
        raise AssertionError(f"{label}: expected >= {minimum} matches in {path}, got {n}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def main() -> None:
    article = ROOT / "manuscript/nee_flagship_article.md"
    replace_once(
        article,
        "Natural examples return only in the Discussion as projections of these mechanisms.",
        "Independent natural evidence enters Question 1; operator-level natural analogies remain Discussion-level projections rather than validation of the finite mechanisms.",
        "article roadmap boundary",
    )

    cover = ROOT / "manuscript/nee_flagship_cover_letter.md"
    old_cover = (
        "Published natural systems are used only for ecological interpretation, not validation of the finite closure. *Crepis* motivates limited buffering; Miyake-jima *Camellia–Zosterops* motivates movement-mediated recoupling; *Conospermum* motivates historical memory; and *Spondias* motivates coordinated deterioration. These examples define empirical questions for future synchronized tests of sorting, buffering, recoupling and memory."
    )
    new_cover = (
        "Independent natural evidence now strengthens the first question without being used to validate the finite mechanisms. A covariance-aware EGWEE synthesis of four independent multilayer fragmentation systems rejected general layer exchangeability (Fisher chi-square(8)=27.70, p=5.35e-4), while keeping incompatible Hedges-g and standardized-gradient magnitudes unpooled. By contrast, the first locked natural prospective transfer of the specific strongest-refuge predictor was null (delta NLL M1-M0=-0.0003211, 95% CI -0.0009825 to +0.0003422). Thus the natural corpus supports multidimensional state separation, whereas sorting, buffering, recoupling, density feedback and the AUC 0.9273 last-refuge result remain bounded finite-model findings."
    )
    replace_once(cover, old_cover, new_cover, "cover natural evidence")

    metadata = ROOT / "manuscript/nee_flagship_submission_metadata.md"
    old_projection = (
        "### Ecological projection only\n\n"
        "- *Crepis sancta*\n"
        "- Miyake-jima *Camellia–Zosterops*\n"
        "- *Conospermum undulatum*\n"
        "- *Spondias purpurea*\n"
        "- urban–island comparison\n"
        "- EGWEE natural-data measurement stress tests\n\n"
        "These sources motivate interpretation and future measurement design. They do not validate the finite closure."
    )
    new_projection = (
        "### Independent natural Q1 evidence\n\n"
        "EGWEE contributes four independent covariance-aware multilayer fragmentation clusters / 12 primary effects. Cluster-level synthesis rejects general layer exchangeability (Fisher chi-square(8)=27.70024526, p=0.0005347329) without pooling incompatible effect-size magnitudes. This supports the portability of the state-separation problem, not the finite operators.\n\n"
        "### Natural Q2 portability boundary\n\n"
        "The first locked natural prospective strongest-refuge test did not detect incremental future-occupancy information after contemporaneous marginals: delta NLL M1-M0=-0.0003211, species-bootstrap 95% CI [-0.0009825,+0.0003422]. The secondary persistence-only direction is not promoted."
    )
    replace_once(metadata, old_projection, new_projection, "metadata natural evidence hierarchy")
    replace_all(
        metadata,
        "- natural examples remain Discussion-level projections only.",
        "- natural Q1 state separation is independently supported by EGWEE; natural Q2 strongest-refuge portability is not established.",
        1,
        "metadata claim ceiling",
    )
    replace_once(
        metadata,
        "- natural projection examples excluded from Results;",
        "- natural data enter Results only through the completed EGWEE Question-1 state-separation synthesis;",
        "metadata format contract",
    )

    display = ROOT / "manuscript/nee_flagship_display_plan.md"
    replace_once(
        display,
        "The main figures carry only exact mathematics and locked finite-model evidence. Natural systems remain Introduction/Discussion projections and receive no main-data panel.",
        "The four main figures remain focused on exact mathematics and locked finite-model mechanism. The completed EGWEE state-separation synthesis enters Question 1 as independent numerical evidence in text; it receives no new main-data panel, and the natural strongest-refuge null remains a Discussion portability boundary.",
        "display principle",
    )
    replace_once(
        display,
        "15. Evidence-role map and literature-based ecological projection table: limited buffering, movement recoupling, temporal memory and coordinated deterioration.",
        "15. EGWEE four-cluster state-separation synthesis, evidence-role map and natural-Q2 strongest-refuge null boundary.",
        "display extended data",
    )

    replacements = {
        ROOT / "README.md": [
            ("**empirical multilevel meta-analysis; screening/extraction in progress**", "**empirical multilevel synthesis complete for the four-cluster state-separation result**"),
        ],
        ROOT / "manuscript/README.md": [
            ("**multilevel meta-analysis in `zuizui0223/egwee`; protocol locked, screening/extraction pending**", "**multilevel meta-analysis in `zuizui0223/egwee`; four-cluster state-separation synthesis complete**"),
        ],
        ROOT / "manuscript/PUBLICATION_LANES.md": [
            ("**independent empirical synthesis; protocol locked, screening/extraction pending**", "**independent empirical synthesis; four-cluster state-separation result complete**"),
        ],
        ROOT / "manuscript/EG_SERIES_SUBMISSION_STATUS_2026-09-08.md": [
            ("**protocol locked; screening/extraction pending**", "**four-cluster state-separation synthesis complete**"),
        ],
    }
    for path, pairs in replacements.items():
        for old, new in pairs:
            replace_once(path, old, new, f"router sync {path.name}")


if __name__ == "__main__":
    main()
