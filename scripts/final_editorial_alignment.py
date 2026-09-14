from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_TITLE = "Eco-genetic sorting and buffering shape functional vulnerability under fragmentation"
NEW_TITLE = "Fragmentation separates biological states and local coupling shapes functional fate"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"{label}: expected one match, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    article_path = ROOT / "manuscript/nee_flagship_article.md"
    article = article_path.read_text(encoding="utf-8")
    article = replace_once(article, f"# {OLD_TITLE}", f"# {NEW_TITLE}", "article title")
    article = replace_once(
        article,
        "Fragmentation can leave ecological components present while altering the processes that keep them functionally coupled. We combine exact results with prospectively locked finite experiments to explain why systems with the same marginal ecological and genetic quantities reach different futures.",
        "Fragmentation can separate biological states while altering the processes that keep ecological and genetic components coupled. We combine exact results with prospectively locked finite experiments to explain why matched ecological and genetic marginals can reach different futures.",
        "abstract opening",
    )
    article = replace_once(
        article,
        "Functional vulnerability therefore reflects both operator balance and the reserve of the strongest remaining local functional refuge.",
        "Functional vulnerability therefore reflects operator balance and the reserve of the strongest remaining local functional refuge.",
        "abstract close",
    )
    article_path.write_text(article, encoding="utf-8")

    cover_path = ROOT / "manuscript/nee_flagship_cover_letter.md"
    cover = cover_path.read_text(encoding="utf-8").replace(OLD_TITLE, NEW_TITLE)
    cover_path.write_text(cover, encoding="utf-8")

    meta_path = ROOT / "manuscript/nee_flagship_submission_metadata.md"
    meta = meta_path.read_text(encoding="utf-8").replace(OLD_TITLE, NEW_TITLE)
    meta_path.write_text(meta, encoding="utf-8")

    checker_path = ROOT / "scripts/check_nee_flagship_compliance.py"
    checker = checker_path.read_text(encoding="utf-8").replace(OLD_TITLE, NEW_TITLE)
    checker_path.write_text(checker, encoding="utf-8")

    fig_path = ROOT / "scripts/build_nee_sorting_buffering_figures.py"
    fig = fig_path.read_text(encoding="utf-8")
    fig = replace_once(fig, '"Sorting and buffering mechanism",', '"State separation and operator balance under fragmentation",', "fig1 svg title")
    fig = replace_once(fig, '"State separation, q-dependent allele sorting, buffering and warning discrimination.",', '"State separation, hidden cross-layer organization, operator balance and fate discrimination.",', "fig1 svg description")
    fig = replace_once(
        fig,
        't(750, 665, "Natural systems enter only as ecological projections of limited buffering, recoupling or memory.", 13),',
        't(750, 665, "Natural systems test state separation; operator-level causation remains finite-model evidence.", 13),',
        "fig1 natural evidence boundary",
    )
    fig_path.write_text(fig, encoding="utf-8")

    helper_path = ROOT / "scripts/_apply_nee_two_question_generalization_reframe.py"
    if helper_path.exists():
        helper = helper_path.read_text(encoding="utf-8").replace(OLD_TITLE, NEW_TITLE)
        helper_path.write_text(helper, encoding="utf-8")


if __name__ == "__main__":
    main()
