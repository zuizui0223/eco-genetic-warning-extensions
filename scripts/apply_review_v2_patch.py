from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NEW_TITLE = "Eco-genetic regimes govern when genetic early warning can be validated"
NEW_ABSTRACT = (
    "Ecological early-warning studies usually ask whether a signal precedes loss, but that question assumes the system generates a comparable loss regime. "
    "We used a finite eco-genetic model with warning-blind calibration, frozen endpoints and fresh validation seeds. Across a common 15-coordinate recurrent-transition grid, source support ranged from 44.89% to 86.67%, while 20,250 calibration attempts separated into rapid-loss, persistence and seed-heterogeneous regimes; strict calibration selected no common validation domain. "
    "Thus recurrent-transition direction changed whether warning could be evaluated before warning values were inspected. A separately declared recalibration recovered two non-matched eco-genetic domains. Warning availability fell from 0.540 to 0.335 and lags appeared, but direct trajectory-bootstrap differences showed endpoint-dependent absolute timing and no separated horizon-normalized timing contrast. "
    "Genetic warning therefore depends first on event-regime feasibility and only second on conditional ordering within a calibrated domain."
)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def patch_manuscript(text: str) -> str:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise RuntimeError("missing manuscript title")
    lines[0] = f"# {NEW_TITLE}"
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    text, n = re.subn(
        r"## Abstract\n\n.*?\n\n## Introduction",
        f"## Abstract\n\n{NEW_ABSTRACT}\n\n## Introduction",
        text,
        count=1,
        flags=re.S,
    )
    if n != 1:
        raise RuntimeError(f"abstract: expected one replacement, found {n}")

    text = replace_once(
        text,
        "The original Stage III summary calculated the reported “median” as the upper middle order statistic for even sample sizes. The audit instead uses the conventional median, averaging the two middle values when `n` is even. Absolute positive lead times are also divided by the full calibrated deterioration horizon (ramp + hold). A hold-only normalization is retained in the Supplementary Material as a sensitivity description.\n\nThe six endpoint records within one trajectory are correlated. We therefore calculated descriptive 95% percentile intervals by resampling whole attempted trajectories, retaining all six endpoint rows within each sampled trajectory. We used 20,000 trajectory-cluster bootstrap replicates with fixed seed `20260814`. The aggregate quantities were lead fraction among valid pairs, lag fraction among valid pairs, and valid-pair availability among all attempted endpoint opportunities. Endpoint-specific positive lead-time medians were bootstrapped in the same way.",
        "The historical Stage III artifact generator calculated its timing “median” as the upper middle order statistic for even sample sizes. The audit instead uses the conventional median, averaging the two middle values when `n` is even. Repository-wide inspection found this definition only in the historical Stage III timing-summary path; the fragmentation effect-size audit and other manuscript-facing medians were calculated separately from locked values using the conventional median. Absolute positive lead times are also divided by the full calibrated deterioration horizon (ramp + hold); a hold-only normalization is retained as a sensitivity description.\n\nThe six endpoint records within one trajectory are correlated. We therefore calculated descriptive 95% percentile intervals by resampling whole attempted trajectories, retaining all six endpoint rows within each sampled trajectory. We used 20,000 trajectory-cluster bootstrap replicates with fixed seed `20260814`. The aggregate quantities were lead fraction among valid pairs, lag fraction among valid pairs, and valid-pair availability among all attempted endpoint opportunities. Endpoint-specific positive lead-time medians were bootstrapped in the same way. Because the two validation domains use independent trajectories, we additionally resampled 100 whole trajectories independently within each domain and calculated the directional-minus-symmetric difference in median lead time for every endpoint and bootstrap replicate. This directly quantifies uncertainty in the between-domain contrast rather than inferring it from overlap of marginal intervals.",
        "secondary audit methods",
    )

    text = replace_once(
        text,
        "The absolute timing contrast did not identify a direction effect. Using the conventional median, positive lead times were `106–109` generations across endpoints in the recalibrated symmetric domain and `72.5–77.5` generations in the directional calibrated domain. However, the calibrated horizons were 240 and 120 generations, respectively. After dividing lead time by the full calibrated horizon, median lead fractions were `0.442–0.454` in the recalibrated symmetric domain but `0.604–0.646` in the directional calibrated domain (Figure 6). Thus the directional calibrated domain had a shorter **absolute** warning-to-loss interval but a larger interval relative to its calibrated horizon. The Stage III timing difference therefore cannot be attributed to recurrent-transition direction alone.",
        "Positive lead-time point estimates were lower in the directional calibrated domain: conventional medians were `106–109` generations across endpoints in the recalibrated symmetric domain and `72.5–77.5` generations in the directional calibrated domain. Direct trajectory-bootstrap contrasts, however, showed that this absolute difference was separated from zero only for the `H_alpha` 5% and 10% endpoints; the other four endpoint intervals included zero. The calibrated horizons were 240 and 120 generations, respectively. After dividing lead time by the full horizon, point estimates reversed (`0.442–0.454` versus `0.604–0.646`), but **all six** directional-minus-symmetric 95% difference intervals included zero (Figure 6; Supplementary Table S5). The point-estimate reversal is therefore descriptive evidence of schedule dependence, not evidence for a separated normalized domain effect.",
        "timing results",
    )

    text = replace_once(
        text,
        "The final Stage III comparison answers a different question. The two validation domains differ not only in `p_star` and `kappa_mu`, but also in `A_ref`, interaction-feedback `kappa`, barrier increase, and deterioration horizon. The comparison therefore asks whether a relative-diversity warning is portable across two independently calibrated eco-genetic settings. It cannot identify the isolated causal contribution of transition direction to warning ordering or lead time.\n\nThe horizon-normalized timing result makes that limitation concrete. Absolute lead times were shorter in the directional calibrated domain, but they occupied a larger fraction of that domain's shorter calibrated horizon. A claim that direction itself “shortened intervention time” would therefore be unsupported. Instead, the result strengthens the broader conclusion: warning time is a property of the whole calibrated system, including the deterioration schedule used to make functional loss observable.",
        "The final Stage III comparison answers a different question. The two validation domains differ not only in `p_star` and `kappa_mu`, but also in `A_ref`, interaction-feedback `kappa`, barrier increase, and deterioration horizon. The comparison therefore asks whether a relative-diversity warning is portable across two independently calibrated eco-genetic settings. It cannot identify the isolated causal contribution of transition direction to warning ordering or lead time.\n\nA matched-schedule Stage III comparison would seem to solve this problem, but the strict common-family experiment explains why it was not the primary validation design. Under the same predeclared deterioration family, all 15 transition coordinates failed the common event-risk gate because candidates collapsed into rapid-loss, persistence, or seed-heterogeneous regimes. Holding the schedule fixed therefore did not yield comparable warning-validation domains to contrast. Recovering intermediate event risk required coordinate-specific recalibration, which restored evaluability at the cost of single-factor identification. That trade-off is itself the biological result: **event-regime feasibility precedes warning comparison**.\n\nThe timing audit makes that limitation concrete. Absolute median lead times were lower in the directional calibrated domain, whereas horizon-normalized point estimates reversed the ordering. Direct between-domain bootstrap intervals show that the absolute contrast is endpoint-dependent and that every horizon-normalized contrast includes zero. A claim that direction either shortened or lengthened intervention time would therefore be unsupported. Instead, the result shows why warning time must be interpreted as a property of the whole calibrated system, including the schedule used to make functional loss observable.",
        "discussion identification",
    )

    text = replace_once(
        text,
        "The cumulative event-incidence curves make the same point without discarding non-events. Warning and trait loss are not mutually exclusive competing risks, so we followed both over the complete horizon rather than forcing a competing-risk model. In the recalibrated symmetric domain, relative-warning incidence rapidly approached one while trait loss accumulated later. In the directional calibrated domain, warning incidence often plateaued below one and approached or fell below trait-loss incidence by the end of follow-up. Warning availability is therefore part of the ecological result, not a nuisance denominator.",
        "The cumulative event-incidence curves make the same point without discarding non-events. Warning and trait loss are not mutually exclusive competing risks, so we followed both over the complete horizon rather than forcing a competing-risk model. In the recalibrated symmetric domain, relative-warning incidence rapidly approached one while trait loss accumulated later. In the directional calibrated domain, warning incidence often plateaued below one. Most strikingly, for the 20% `H_gamma` endpoint, warning was observed in 41 of 81 baseline-eligible completed trajectories (`0.506`) whereas functional-trait loss occurred in 52 of 81 (`0.642`) by the end of follow-up (Figure 4). Warning availability is therefore part of the ecological result, not a nuisance denominator.",
        "cumulative incidence result",
    )

    text = replace_once(
        text,
        "A separately declared warning-blind protocol recovered two validation domains only after changing the candidate family and event-risk gate. Those domains differed in ecological parameters and deterioration schedules as well as recurrent-transition parameters. Their validation showed lower warning availability and nonzero lag in the directional calibrated domain, but the apparent reduction in absolute lead time reversed after normalization by the calibrated horizon. The defensible conclusion is therefore not that transition direction alone weakens or accelerates genetic warning. Genetic warning is an emergent, calibration-dependent property of the eco-genetic system that generates functional persistence, genetic change, censoring, and the opportunity to observe both warning and loss.",
        "The strongest extension result occurred before warning values were examined: recurrent-transition coordinates reorganised source feasibility and partitioned a common deterioration family into rapid-loss, persistence and seed-heterogeneous regimes, leaving no strict common validation domain. A separately declared warning-blind protocol later recovered two non-matched domains for a portability test. Warning availability was lower and lags appeared in the directional calibrated domain, but direct timing contrasts remained endpoint- and schedule-dependent. The defensible conclusion is therefore not that transition direction alone weakens or accelerates genetic warning. **Whether warning can be meaningfully evaluated is itself an eco-genetic property, and conditional warning performance comes only after that feasibility question is satisfied.**",
        "conclusion",
    )
    return text


def patch_captions(_: str) -> str:
    return """# Main figure captions

## Figure 1. Eco-genetic closure links fragmentation to genetic warning

Fragmentation alters interaction state, high-trait state, local effective size and genetic diversity. Recurrent-transition direction, deterioration and observation rules modify this closure. Arrows summarize the tested causal organization; they do not assert a universal theorem.

## Figure 2. High-trait source feasibility depends on recurrent-transition coordinates

Projection-supported source fractions across 15 recurrent-transition coordinates, with 225 attempts per coordinate. Values are printed directly. Within fixed relaxation-strength rows, support generally increased towards high-trait-directed equilibria.

## Figure 3. A common deterioration family separates into three event regimes

**A**, dominant rapid-loss, seed-heterogeneous or persistence regime across the 15-coordinate map. **B**, composition of 648 complete warning-blind candidates: 322 rapid-loss-side, 84 seed-heterogeneous and 242 persistence-side. No coordinate satisfied the strict all-seed gate; all 15 were retained as `no_domain_selected`.

## Figure 4. Cumulative warning and functional-loss incidence

Cumulative observed warning and realised trait-loss incidence among baseline-eligible completed validation trajectories, retained through each domain's administrative horizon. Warning and loss can both occur in one trajectory, so the curves are paired event incidences rather than competing-risk estimates. For directional-domain `H_gamma` at 20%, final warning incidence was 41/81 versus 52/81 for trait loss.

## Figure 5. Warning availability, censoring and ordering

Each bar retains the full 100 attempted trajectories for one preregistered endpoint: source failure (SF), baseline ineligibility (BI), both censored (BC), warning censored (WC), trait loss censored (TC), lead, tie and lag. Endpoint rows share trajectories; uncertainty is therefore resampled by whole trajectory.

## Figure 6. Absolute and schedule-normalized positive warning lead time

Conventional median positive lead time with trajectory-bootstrap 95% intervals and contributing lead counts. **A**, generations. **B**, fraction of the full calibrated horizon. Absolute point estimates were lower in the directional calibrated domain, whereas normalized point estimates reversed. Direct directional-minus-symmetric bootstrap intervals were endpoint-dependent for absolute time and included zero at all six normalized endpoints; Stage III does not identify a single-factor timing effect.

## Caption rules retained for submission

- Keep the inherited symmetric benchmark, recalibrated symmetric domain and directional calibrated domain terminologically distinct.
- State when endpoint counts share trajectories.
- Describe `p_star` as an effective recurrent-transition equilibrium, not an empirical mutation-rate estimate.
- Keep the strict Protocol 002 no-domain outcome separate from the separately declared Protocol 003 recalibration.
- Never describe the Stage III timing contrast as the isolated effect of transition direction.
"""


def patch_table_captions(text: str) -> str:
    return replace_once(
        text,
        "For each Stage III endpoint and calibrated domain: full attempted denominator, source failure, baseline ineligibility, censoring categories, valid-pair counts, lead/tie/lag ordering, conventional median positive lead time, horizon-normalized lead time, and trajectory-bootstrap 95% intervals. Endpoint rows within trajectories are correlated; the bootstrap resamples trajectories rather than treating the six endpoint summaries as independent observations.",
        "For each Stage III endpoint and calibrated domain: full attempted denominator, censoring categories, lead/tie/lag ordering, conventional median positive lead time and horizon-normalized lead time with whole-trajectory bootstrap intervals. The companion between-domain table reports directional-minus-symmetric median differences for absolute, horizon-normalized and hold-normalized timing, with intervals calculated by independently resampling whole trajectories within each domain.",
        "Table S5 caption",
    )


def main() -> int:
    manuscript_paths = [
        ROOT / "manuscript/main_text.md",
        ROOT / "manuscript/supervisor_first_draft.md",
    ]
    for path in manuscript_paths:
        path.write_text(patch_manuscript(path.read_text(encoding="utf-8")), encoding="utf-8")
    captions = ROOT / "manuscript/figure_captions.md"
    captions.write_text(patch_captions(captions.read_text(encoding="utf-8")), encoding="utf-8")
    table_captions = ROOT / "manuscript/table_captions.md"
    table_captions.write_text(
        patch_table_captions(table_captions.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
