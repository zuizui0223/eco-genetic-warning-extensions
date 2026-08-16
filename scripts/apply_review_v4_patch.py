from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f"expected text not found: {old[:90]!r}")
    return text.replace(old, new, 1)


def reorder_results(text: str) -> str:
    start = text.index("## Results\n")
    end = text.index("## Discussion\n")
    block = text[start + len("## Results\n"):end]
    matches = list(re.finditer(r"(?m)^### .+$", block))
    sections = {}
    for i, m in enumerate(matches):
        s = m.start()
        e = matches[i + 1].start() if i + 1 < len(matches) else len(block)
        heading = m.group(0)
        sections[heading] = block[s:e].strip() + "\n\n"
    keys = {
        "source": next(k for k in sections if "high-trait source" in k),
        "regime": next(k for k in sections if "common deterioration family" in k),
        "fragment": next(k for k in sections if "Fragmentation produced" in k),
        "benchmark": next(k for k in sections if "Relative genetic erosion" in k),
        "stage3": next(k for k in sections if "Warning availability" in k),
    }
    ordered = "".join(sections[keys[name]] for name in ("source", "regime", "fragment", "benchmark", "stage3"))
    return text[:start] + "## Results\n\n" + ordered + text[end:]


def add_reference(text: str, anchor: str, entry: str) -> str:
    if entry.split(".")[0] in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"reference anchor missing: {anchor}")
    return text.replace(anchor, entry + "\n\n" + anchor, 1)


def main() -> None:
    main_path = ROOT / "manuscript/main_text.md"
    text = main_path.read_text(encoding="utf-8")

    # Methods: make the conditional timing estimand explicit and put full-denominator incidence first.
    old = "The six endpoint records within one trajectory are correlated. We therefore calculated descriptive 95% percentile intervals by resampling whole attempted trajectories, retaining all six endpoint rows within each sampled trajectory. We used 20,000 trajectory-cluster bootstrap replicates with fixed seed `20260814`. The aggregate quantities were lead fraction among valid pairs, lag fraction among valid pairs, and valid-pair availability among all attempted endpoint opportunities. Endpoint-specific positive lead-time medians were bootstrapped in the same way. Because the two validation domains use independent trajectories, we additionally resampled 100 whole trajectories independently within each domain and calculated the directional-minus-symmetric difference in median lead time for every endpoint and bootstrap replicate. This directly quantifies uncertainty in the between-domain contrast rather than inferring it from overlap of marginal intervals."
    new = "The six endpoint records within one trajectory are correlated. We therefore calculated descriptive 95% percentile intervals by resampling whole attempted trajectories, retaining all six endpoint rows within each sampled trajectory (Field & Welsh 2007). We used 20,000 trajectory-cluster bootstrap replicates with fixed seed `20260814`. The aggregate quantities were lead fraction among valid pairs, lag fraction among valid pairs, and valid-pair availability among all attempted endpoint opportunities. Endpoint-specific positive lead-time medians were bootstrapped in the same way. Because the two validation domains use independent trajectories, we additionally resampled 100 whole trajectories independently within each domain and calculated the directional-minus-symmetric difference in median lead time for every endpoint and bootstrap replicate. This directly quantifies uncertainty in the between-domain contrast rather than inferring it from overlap of marginal intervals.\n\nThe positive-lead median is a **conditional estimand**: a trajectory contributes only if both warning and trait loss are observed in that domain and the warning leads. The contributing sets therefore differ systematically across domains, and administrative censoring can preferentially exclude later losses and their potentially longer lead times. Horizon normalization does not remove this selection. We therefore treat full-denominator cumulative event incidence and availability as the primary Stage III timing evidence; conditional lead-time medians are a secondary diagnostic that must be interpreted together with Figures 4 and 5."
    text = replace_once(text, old, new)

    old = "Finally, warning and trait loss are not classical competing risks because both can occur in the same trajectory. We therefore report cumulative observed incidence of each event rather than forcing them into a competing-risk estimand. Cumulative curves retain all baseline-eligible completed trajectories through their full administratively censored horizon."
    new = "Finally, warning and trait loss are not classical competing risks because both can occur in the same trajectory; competing-risk cumulative incidence is defined for mutually exclusive event types (Andersen et al. 2012). We therefore report paired cumulative observed incidence of each event rather than forcing them into a competing-risk estimand. Cumulative curves retain all baseline-eligible completed trajectories through their full administratively censored horizon."
    text = replace_once(text, old, new)

    # Results order follows the title/Abstract: common-grid identification first.
    text = reorder_results(text)

    old = "Positive lead-time point estimates were lower in the directional calibrated domain: conventional medians were `106–109` generations across endpoints in the recalibrated symmetric domain and `72.5–77.5` generations in the directional calibrated domain. Direct trajectory-bootstrap contrasts, however, showed that this absolute difference was separated from zero only for the `H_alpha` 5% and 10% endpoints; the other four endpoint intervals included zero. The calibrated horizons were 240 and 120 generations, respectively. After dividing lead time by the full horizon, point estimates reversed (`0.442–0.454` versus `0.604–0.646`), but **all six** directional-minus-symmetric 95% difference intervals included zero (Figure 6; Supplementary Table S5). The point-estimate reversal is therefore descriptive evidence of schedule dependence, not evidence for a separated normalized domain effect."
    new = "Conditional on observing a leading warning-loss pair, positive lead-time point estimates were lower in the directional calibrated domain: conventional medians were `106–109` generations across endpoints in the recalibrated symmetric domain and `72.5–77.5` generations in the directional calibrated domain. The direct absolute difference interval excluded zero at only two of six endpoints, `H_alpha` 5% (`−97.0` to `−3.5` generations) and 10% (`−97.0` to `−4.5`), and both exclusions were close to zero at the upper bound; the other four intervals included zero. After full-horizon normalization, all six directional-minus-symmetric 95% difference intervals included zero. These medians are calculated on domain-specific selected subsets (54 leading pairs per symmetric endpoint versus 24–35 in the directional domain) and are additionally shaped by administrative censoring, so they are not a marginal domain-wide timing effect. Figure 4 therefore provides the primary Stage III timing evidence on the full baseline-eligible denominator; Figure 6 is retained as a conditional diagnostic to show why apparent lead time is schedule- and selection-dependent (Supplementary Table S5)."
    text = replace_once(text, old, new)

    old = "The timing audit makes that limitation concrete. Absolute median lead times were lower in the directional calibrated domain, whereas horizon-normalized point estimates reversed the ordering. Direct between-domain bootstrap intervals show that the absolute contrast is endpoint-dependent and that every horizon-normalized contrast includes zero. A claim that direction either shortened or lengthened intervention time would therefore be unsupported. Instead, the result shows why warning time must be interpreted as a property of the whole calibrated system, including the schedule used to make functional loss observable."
    new = "The timing audit makes that limitation concrete but is deliberately secondary to the full-denominator incidence curves. Absolute conditional medians were lower in the directional calibrated domain, whereas horizon-normalized point estimates reversed the ordering; direct difference intervals were endpoint-dependent and every normalized interval included zero. More importantly, the median conditions on the domain-specific subset in which both events are observed and the warning leads, so different availability and administrative censoring change which trajectories contribute. A claim that direction either shortened or lengthened intervention time would therefore be unsupported. Warning timing must be interpreted jointly with event incidence and availability, not from the selected lead-time distribution alone."
    text = replace_once(text, old, new)

    # Genetic-drift and negative-control literature.
    text = text.replace("Genetic monitoring requires biological calibration", "Genetic monitoring requires biological calibration", 1)
    text = replace_once(text,
        "Relative diversity erosion was highly informative in the inherited symmetric benchmark, but fixed thresholds were unreliable and relative warnings became less available in a separately calibrated domain.",
        "Relative diversity erosion was highly informative in the inherited symmetric benchmark, but fixed thresholds were unreliable and relative warnings became less available in a separately calibrated domain. This calibration problem sits alongside the established sensitivity of small populations to drift, diversity loss and inbreeding (Frankham 2005).")
    text = replace_once(text,
        "The next empirical and model-based test should therefore compare genetic warning with control variables outside the proposed eco-genetic pathway or with deliberately perturbed baseline windows.",
        "The next empirical and model-based test should therefore compare genetic warning with control variables outside the proposed eco-genetic pathway or with deliberately perturbed baseline windows, using negative controls to expose generic deterioration or analytic artefacts rather than assuming specificity (Lipsitch et al. 2010).")

    # Add verified references to the integrated reference list.
    text = add_reference(text, "Bell, G. (2017). Evolutionary rescue.", "Andersen, P.K., Geskus, R.B., de Witte, T. & Putter, H. (2012). Competing risks in epidemiology: possibilities and pitfalls. *International Journal of Epidemiology*, **41**, 861–870. doi:10.1093/ije/dyr213")
    text = add_reference(text, "Gomulkiewicz, R. & Holt, R.D. (1995).", "Field, C.A. & Welsh, A.H. (2007). Bootstrapping clustered data. *Journal of the Royal Statistical Society: Series B*, **69**, 369–390. doi:10.1111/j.1467-9868.2007.00593.x")
    text = add_reference(text, "Gomulkiewicz, R. & Holt, R.D. (1995).", "Frankham, R. (2005). Genetics and extinction. *Biological Conservation*, **126**, 131–140. doi:10.1016/j.biocon.2005.05.002")
    text = add_reference(text, "McConkey, K.R. & Drake, D.R. (2006).", "Lipsitch, M., Tchetgen Tchetgen, E. & Cohen, T. (2010). Negative controls: a tool for detecting confounding and bias in observational studies. *Epidemiology*, **21**, 383–388. doi:10.1097/EDE.0b013e3181d61eeb")
    main_path.write_text(text, encoding="utf-8")
    (ROOT / "manuscript/supervisor_first_draft.md").write_text(text, encoding="utf-8")

    # Figure 6 explicitly labels selection-conditioning; avoid minus-sign glyph dependence.
    cap_path = ROOT / "manuscript/figure_captions.md"
    caps = cap_path.read_text(encoding="utf-8")
    old_cap = "Conventional median positive lead time with trajectory-bootstrap 95% intervals and contributing lead counts. **A**, generations. **B**, fraction of the full calibrated horizon. Absolute point estimates were lower in the directional calibrated domain, whereas normalized point estimates reversed. Direct directional-minus-symmetric bootstrap intervals were endpoint-dependent for absolute time and included zero at all six normalized endpoints; Stage III does not identify a single-factor timing effect."
    new_cap = "Conditional median positive lead time among trajectories in which both events were observed and warning led, with whole-trajectory bootstrap 95% intervals and contributing lead counts. **A**, generations. **B**, fraction of the full calibrated horizon. The contributing set differs by domain and endpoint, and administrative censoring can remove later losses; normalization does not remove this selection. Direct directional-minus-symmetric intervals were endpoint-dependent for absolute time and included zero at all six normalized endpoints. Interpret this diagnostic together with full-denominator Figures 4–5."
    caps = replace_once(caps, old_cap, new_cap)
    cap_path.write_text(caps, encoding="utf-8")

    # Methodological bibliography source of truth.
    refs_path = ROOT / "manuscript/references.md"
    refs = refs_path.read_text(encoding="utf-8")
    refs = add_reference(refs, "Bell, G. (2017). Evolutionary rescue.", "Andersen, P.K., Geskus, R.B., de Witte, T. & Putter, H. (2012). Competing risks in epidemiology: possibilities and pitfalls. *International Journal of Epidemiology*, **41**, 861–870. doi:10.1093/ije/dyr213")
    refs = add_reference(refs, "Gomulkiewicz, R. & Holt, R.D. (1995).", "Field, C.A. & Welsh, A.H. (2007). Bootstrapping clustered data. *Journal of the Royal Statistical Society: Series B*, **69**, 369–390. doi:10.1111/j.1467-9868.2007.00593.x")
    refs = add_reference(refs, "Gomulkiewicz, R. & Holt, R.D. (1995).", "Frankham, R. (2005). Genetics and extinction. *Biological Conservation*, **126**, 131–140. doi:10.1016/j.biocon.2005.05.002")
    refs = add_reference(refs, "McConkey, K.R. & Drake, D.R. (2006).", "Lipsitch, M., Tchetgen Tchetgen, E. & Cohen, T. (2010). Negative controls: a tool for detecting confounding and bias in observational studies. *Epidemiology*, **21**, 383–388. doi:10.1097/EDE.0b013e3181d61eeb")
    refs_path.write_text(refs, encoding="utf-8")

    fig_src = ROOT / "src/eco_genetic_warning_extensions/publication_figures.py"
    src = fig_src.read_text(encoding="utf-8")
    src = src.replace("Direct D−S bootstrap:", "Direct directional-minus-symmetric bootstrap:")
    fig_src.write_text(src, encoding="utf-8")


if __name__ == "__main__":
    main()
