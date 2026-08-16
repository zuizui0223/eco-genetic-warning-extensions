from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def update_main() -> None:
    path = ROOT / "manuscript/main_text.md"
    text = path.read_text(encoding="utf-8")

    methods_anchor = (
        "The first-phase fragmentation experiment compared the same H1-prepared full state after conservation-preserving projection into one-large and equal-isolated landscapes. Twelve predeclared primary cells, each with 100 attempted seed-replicates, were evaluated. Manuscript-facing effect sizes were calculated after the campaign from the already locked paired outcomes: final interaction was the mean of `final_q_by_patch`, local effective size was the mean of `final_effective_size_by_patch`, and realised high-trait mass used the stored metapopulation summary. No simulation was rerun for this descriptive summary."
    )
    methods_new = methods_anchor + (
        "\n\nAfter review, a separately declared supplementary sensitivity replayed the same finite closure with fresh master seeds `20260820`–`20260824` and projected each prepared source across 1, 2, 3, 4, 6, 8, 12, and 16 equal isolated patches at fixed total area. Patch-count outcomes from one source were paired repeated measures; no warning endpoint was evaluated (Supplementary Methods)."
    )
    text = replace_once(text, methods_anchor, methods_new, "main methods gradient insertion")

    result_anchor = (
        "Pooled descriptively across those paired replicates, mean final interaction was `0.9977` in one large patch and `0.0048` after equal isolation; the median paired reduction was 99.86%. Mean local effective size fell from `72.83` to `8.18`, with a median paired reduction of 88.73%. Mean realised high-trait mass fell from `0.575` to `0.177`, with a median paired reduction of 68.87% (Supplementary Table S1). These finite results provide the demographic and functional bridge between the analytical interaction threshold and later genetic-warning analyses."
    )
    result_new = result_anchor + (
        "\n\nA fresh-seed fragmentation gradient showed that the four-patch contrast was not endpoint-specific. Of 1,200 attempted sources, 1,037 were prepared and projected across all eight patch counts. At the first split to two isolated patches, paired medians fell by 99.83% for interaction, 77.87% for local effective size, and 71.71% for realised high-trait mass, with all three lower in 1,037/1,037 sources. Interaction and local effective size then declined further, whereas realised high-trait mass partially recovered; fresh four-patch reductions closely reproduced the historical endpoint (Supplementary Fig. S1)."
    )
    text = replace_once(text, result_anchor, result_new, "main results gradient insertion")

    # Recover word budget by removing repetition now carried by the Supplement and figure.
    old = (
        "The first-phase fragmentation result was quantitatively strong. Across 12 primary cells, 1,055 of 1,200 attempted replicates satisfied the H1 full-state hold criterion. Every one of those 1,055 qualified replicates satisfied the predeclared H3 fragmentation pattern: mean final interaction, mean local effective size, and realised high-trait mass were all lower after equal isolation than in the matched one-large projection."
    )
    new = (
        "Across 12 primary cells, 1,055 of 1,200 attempted replicates satisfied the H1 full-state hold criterion, and every qualified replicate had lower final interaction, local effective size, and realised high-trait mass after equal isolation than in its matched one-large projection."
    )
    text = replace_once(text, old, new, "compress historical fragmentation paragraph")

    path.write_text(text, encoding="utf-8")
    (ROOT / "manuscript/supervisor_first_draft.md").write_text(text, encoding="utf-8")


def update_supplement() -> None:
    path = ROOT / "manuscript/supplementary_methods.md"
    text = path.read_text(encoding="utf-8")
    old = (
        "The locked parent artifact contains the predeclared `one_large`, `equal_isolated`, and `equal_migrating` scenarios, but not an intermediate gradient in the number of isolated fragments. Consequently, an additional fragmentation-gradient figure would require a new finite-model campaign rather than replotting an existing locked result."
    )
    new = """### S2.1 Post-review fixed-area fragmentation-gradient sensitivity

The locked historical artifact contained no intermediate patch-count gradient. We therefore declared a new supplementary campaign before inspecting any new gradient outcome. It retained the frozen 12 mutation-H1 primary cells, the same H1 boundary-resolution and high-state replay, the 30-generation full-state hold, the same symmetric recurrent-mutation closure, total area `4.0`, and zero migration. Fresh master seeds `20260820`–`20260824` supplied 20 source replicates per seed and cell. Each prepared source was projected as a repeated measure into 1, 2, 3, 4, 6, 8, 12, and 16 equal isolated patches. No warning endpoint was selected, tuned, or evaluated.

The authoritative campaign is parent workflow run `31937210601`, artifact `9261157020`, digest `sha256:424031d0f6bcdf75c13e03deb35324f0d3f6fd46f58ff7b34961bbd00556537c`. Of 1,200 attempted sources, 1,037 completed H1 preparation and projection at every patch count, yielding 9,600 repeated-measures rows. The first attempted execution is not evidence: it stopped before a complete gradient because an existing private helper still used a former positional API. That call was changed to the exactly equivalent keyword-only interface before any gradient outcome was inspected; no scientific parameter, seed, landscape, or outcome definition changed.

At two isolated patches, pooled paired medians retained `0.001744` of one-patch interaction, `0.221311` of local effective size, and `0.282918` of realised high-trait mass, corresponding to reductions of 99.83%, 77.87%, and 71.71%. All three metrics were below their paired one-patch value in 1,037/1,037 supported sources. The fresh four-patch reductions were 99.86%, 88.73%, and 69.82%, closely reproducing the historical 99.86%, 88.73%, and 68.87% endpoint estimates.

The gradient was not a single smooth dose-response. Cell-specific median interaction and local effective size declined monotonically in all 12 cells after the sharp one-to-two-patch transition, but realised high-trait mass partially recovered after its initial drop: the pooled retained median rose from `0.2829` at two patches to `0.3939` at 16. Potential high-trait viability was present in 1,037/1,037 one-patch outcomes and 0/1,037 outcomes at every tested patch count from 2 to 16, while realised high-trait occupancy still persisted in approximately 99.6–100% of supported trajectories at generation 30. This finite lag reinforces the distinction between potential viability and realised occupancy.

For the canonical one-state interaction map, the coordinate `K_fragment = kappa A_patch / A_ref` was recorded as an analytical reference. The finite response did not occur at `K=4`: at two patches all 12 primary cells still had `K_fragment > 4` (range 7.5–15.0), although interaction and potential high-trait viability had already collapsed. `K=4` therefore remains a theorem-layer geometry boundary, not a fitted finite fragmentation threshold.

**Supplementary Figure S1. Fixed-area fragmentation gradient from paired H1-prepared sources.** Grey lines show the 12 frozen primary-cell median retained fractions relative to the paired one-patch projection; the black line shows the pooled paired median. Panels report final interaction, local effective size, and realised high-trait mass across 1, 2, 3, 4, 6, 8, 12, and 16 isolated equal patches. The figure is new finite Type S sensitivity evidence and does not replace the historical H1/H3 ledger."""
    text = replace_once(text, old, new, "supplement gradient replacement")
    path.write_text(text, encoding="utf-8")


def update_claim_map() -> None:
    path = ROOT / "manuscript/claim_evidence_map.md"
    text = path.read_text(encoding="utf-8")
    anchor = (
        "| P3 | Fixed absolute thresholds `H_alpha <= 0.20` and `H_gamma <= 0.20` are not robust warning rules in that same benchmark. | Stored-trajectory H2-A audit: 14/0/6 and 8/0/8 lead/tie/lag. | negative robustness result |"
    )
    addition = anchor + (
        "\n| P4 | A fresh fixed-area fragmentation sensitivity shows that the historical four-patch contrast was already present after the first split to two isolated patches; interaction and local effective size then declined further, whereas realised high-trait mass was non-monotonic. | Parent run `31937210601`, artifact `9261157020`; 1,037 prepared sources projected across eight patch counts. | new supplementary finite Type S sensitivity |"
    )
    text = replace_once(text, anchor, addition, "claim P4")

    numeric_anchor = "| median paired realised high-trait-mass reduction | 68.87% |"
    numeric_add = numeric_anchor + "\n| fresh fragmentation-gradient attempted / prepared sources | 1,200 / 1,037 |\n| fresh n=2 paired reductions: interaction / local effective size / realised high-trait mass | 99.83% / 77.87% / 71.71% |\n| fresh n=4 paired reductions: interaction / local effective size / realised high-trait mass | 99.86% / 88.73% / 69.82% |\n| potential high-trait viability: n=1 / every n>=2 | 1,037/1,037 / 0/1,037 |"
    text = replace_once(text, numeric_anchor, numeric_add, "claim gradient numeric facts")

    prohibited_anchor = "- Two calibrated domains constitute a complete phase diagram of warning performance."
    prohibited_add = prohibited_anchor + "\n- The fragmentation sensitivity is a universal monotone dose-response.\n- `K=4` is the observed finite fragmentation threshold.\n- The post-review fragmentation sensitivity replaces the historical H1/H3 evidence ledger."
    text = replace_once(text, prohibited_anchor, prohibited_add, "claim gradient prohibitions")

    map_anchor = "| Figure 6 | corrected absolute and horizon-normalized positive lead time with trajectory-bootstrap intervals | S7 |"
    map_add = map_anchor + "\n| Supplementary Figure S1 | fresh fixed-area paired fragmentation gradient | P4 |"
    text = replace_once(text, map_anchor, map_add, "claim Figure S1")
    path.write_text(text, encoding="utf-8")


def update_artifact_index() -> None:
    path = ROOT / "manuscript/artifact_index.md"
    text = path.read_text(encoding="utf-8")
    anchor = (
        "| Inherited H1/H3 finite chain | paired one-large versus equal-isolated outcomes used for the fragmentation effect-size audit | parent run `28456092898`, artifact `7987193632`, digest `sha256:b74b604f3233fa6086e2afa39cd780fa375aac4b1abd8c63e6f5ed8b3a467d2c` |"
    )
    addition = anchor + (
        "\n| Post-review H3 fragmentation gradient | fresh fixed-area paired projections at 1, 2, 3, 4, 6, 8, 12, and 16 isolated patches; 1,200 attempted / 1,037 prepared sources | parent run `31937210601`, artifact `9261157020`, digest `sha256:424031d0f6bcdf75c13e03deb35324f0d3f6fd46f58ff7b34961bbd00556537c` |"
    )
    text = replace_once(text, anchor, addition, "artifact gradient row")

    machine_anchor = "- `manuscript/tables/inherited_h3_effect_summary.csv` — paired first-phase H3 descriptive effects from the locked parent artifact."
    machine_add = machine_anchor + "\n- `h3_fragmentation_gradient_records.csv` in the checksummed submission bundle — 9,600 post-review repeated-measures rows from 1,200 attempted fresh sources across eight patch counts.\n- `h3_fragmentation_gradient_cell_summary.csv` and `h3_fragmentation_gradient_pooled_summary.csv` — cell-level and pooled paired gradient summaries underlying Supplementary Figure S1."
    text = replace_once(text, machine_anchor, machine_add, "artifact gradient tables")

    main_fig_anchor = "6. **Absolute and horizon-normalized positive warning lead time.** Conventional medians and whole-trajectory bootstrap intervals are shown; the direct between-domain audit demonstrates endpoint-dependent absolute contrasts and no separated full-horizon-normalized contrast."
    main_fig_add = main_fig_anchor + "\n\n### Supplementary figure\n\nS1. **Fixed-area fragmentation gradient from paired H1-prepared sources.** Fresh-seed repeated-measures sensitivity across 1, 2, 3, 4, 6, 8, 12, and 16 isolated equal patches; interaction and local effective size decline after the first split, while realised high-trait mass is non-monotonic."
    text = replace_once(text, main_fig_anchor, main_fig_add, "artifact Supplementary Figure S1")
    path.write_text(text, encoding="utf-8")


def update_allocation() -> None:
    path = ROOT / "manuscript/main_vs_supplement.md"
    text = path.read_text(encoding="utf-8")
    old = (
        "### Figure 6 — absolute and horizon-normalized positive lead time\nReports conventional medians and whole-trajectory bootstrap 95% intervals in generations and as fractions of each calibrated horizon. The latter prevents the different Stage III schedules from being mistaken for a single-factor timing contrast."
    )
    new = (
        "### Figure 6 — absolute and horizon-normalized positive lead time\nSecondary conditional diagnostic among observed leading pairs. Conventional medians and whole-trajectory bootstrap intervals are shown in generations and as fractions of each calibrated horizon; the text explicitly conditions interpretation on Figure 4 event incidence and Figure 5 availability."
    )
    text = replace_once(text, old, new, "allocation Figure 6")
    supp_anchor = (
        "Supplement includes full mathematical results and proofs, life-cycle specification, migration bounds, source/projection invariants, complete Stage I–III parameter and seed bookkeeping, Protocol 002 and Protocol 003 calibration rules and amendments, inherited H3 effect-size audit, the post-review Stage III timing/uncertainty audit, full endpoint/censoring tables, and provenance hashes."
    )
    supp_new = supp_anchor + "\n\n### Supplementary Figure S1 — fixed-area fragmentation gradient\nNew post-review Type S sensitivity using fresh seeds and the same mutation-primary H1/H3 closure. It shows the paired response across 1, 2, 3, 4, 6, 8, 12, and 16 isolated equal patches and retains the non-monotonic realised high-trait-mass response."
    text = replace_once(text, supp_anchor, supp_new, "allocation Supplementary Figure S1")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    update_main()
    update_supplement()
    update_claim_map()
    update_artifact_index()
    update_allocation()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
