# EG-series publication roadmap — 2026-09-04

## Decision

The EG programme is developed as **four publication claims that answer four different inferential questions**, not as one omnibus manuscript and not as four arbitrary slices of one result.

The shared programme principle is:

> **Information for one inferential target does not guarantee adequacy for another.**

The logical progression is:

```text
EGC: what biological states separate under fragmentation?
  -> EGWE state: what representation preserves future-relevant distinctions?
  -> EGWE warning: when is a temporally early signal actually predictive?
  -> EGWEE: when does an empirical measurement earn state/proxy status before residual context is interpreted?
```

Publication order need not match logical order. Scientific claim ownership does.

---

## Paper I — EGC: mechanism and biological-state separation

**Repository:** `zuizui0223/eco-genetic-criticality`

**Working manuscript:** `manuscript/main_text.md`

**Working title:**

> *Interaction thresholds and state separation under fragmentation: a theorem-guided finite-model framework*

### Owned question

When fragmentation acts on an interaction-dependent finite eco-genetic system, do potential viability, realised occupancy, interaction support, demographic/effective-size state and genetic summaries behave as one latent deterioration axis?

### Headline answer

No. Under the declared theorem/closure hierarchy, these biological objects are distinct. The preregistered fragmentation gradient supplies the constructive finite example: potential high-trait viability is lost at the first subdivision while realised occupancy persists over the finite endpoint, interaction and local effective size continue to decline, and realised high-trait mass follows a different non-monotone shape.

### Claim firewall

EGC owns **state separation and mechanism**, not forecasting sufficiency. Phrases such as `which state is sufficient` should be replaced during the literature pass by `which biological state is relevant to the declared question` or equivalent state-separation language.

EGC does not own full-denominator warning validity, cross-layer representation sufficiency, or natural-data residual-context inference.

### Current bottleneck

No new simulation is required for the active claim. The bottleneck is the dedicated literature/novelty pass and final citation placement around fragmentation, ecological-function loss, genetic diversity, eco-evolutionary feedback and theorem-to-closure discipline.

---

## Paper II — EGWE state validity: representation and propagation

**Repository:** `zuizui0223/eco-genetic-warning-extensions`

**Working manuscript:** `manuscript/state_validity_and_empirical_measurement_gates.md`

### Owned question

If two present states match the usual ecological/genetic marginal summaries, can their future dynamics still differ because the cross-layer spatial arrangement has been erased? If so, over what declared forecast horizons does that distinction propagate to realised functional-loss risk?

### Headline answer

Yes.

1. The constructive aligned/anti-aligned states match census, interaction, allele-frequency and realised-trait marginals, `H_alpha`, `H_gamma` and `F_ST`, yet their exact next interaction transition differs by as much as **0.2543**.
2. The original frozen Phase-V 500-pair generation-60 contrast was **+4.4 percentage points anti-aligned minus aligned**, with paired 95% CI approximately **-1.2 to +10.0 points**; it was correctly treated as imprecise rather than equivalent.
3. A **separately prospectively locked post-Phase-V propagation experiment** retained one common forcing path, fixed horizons `5, 10, 20, 40`, nested paired prefixes `500, 1000, 1500`, and a primary 1,500-pair estimand.
4. In the primary 1,500-pair curve, anti-aligned minus aligned loss-risk difference was:
   - generation 5: **0.0 pp**;
   - generation 10: **+0.33 pp**, 95% CI **-0.44 to +1.11**;
   - generation 20: **+5.33 pp**, 95% CI **+2.04 to +8.62**;
   - generation 40: **+5.20 pp**, 95% CI **+1.96 to +8.44**.
5. The nested prefixes show that the main change from 500 to 1,500 pairs was interval width rather than a qualitative reversal of the generation-20/40 effect-size estimate.

The supported positive statement is therefore:

> **A cross-layer state distinction erased by standard marginal summaries can alter the next transition and can propagate to a measurable, horizon-dependent functional-loss risk contrast under a declared deterioration path.**

### Claim ceiling

The experiment does not establish generation 20 as a universal cutoff, a natural-system timescale, complete state sufficiency, or a universal risk effect. It is a finite closure-specific propagation result.

### Warning firewall

This result does **not** explain why the frozen diversity thresholds fail predictive discrimination. No warning threshold was rerun with alignment information. The causal implication `warning failure -> missing cross-layer alignment` remains forbidden.

### Publication role

This is now the **conceptual flagship** of the series. The post-Phase-V 1,500-pair experiment removes the former dependence on a one-step positive result paired only with an unresolved 60-generation contrast. The manuscript has its own positive forecast-horizon result and should remain separate from the warning-validity paper.

### Superseded audit

PR #143 contained an alternative 500-pair propagation audit. It was closed without merge after the separately locked 1,500-pair experiment became the authoritative `main` result. The old PR remains provenance only and must not create a competing source of truth.

---

## Paper III — EGWE warning validity: temporal precedence versus prediction

**Repository:** `zuizui0223/eco-genetic-warning-extensions`

**Working manuscript:** `manuscript/warning_validity.md`

**Working title:**

> *Event-conditioned temporal precedence is not predictive warning validity*

### Owned question

Does repeated observation that a frozen marker precedes every observed event establish prospective warning validity?

### Headline answer

No. For the six frozen relative-diversity rules:

- inherited event trajectories: **35/35** leads;
- fresh event trajectories: **33/33** leads;
- inherited horizon non-events: **48/48** also fired;
- fresh horizon non-events: **49/49** also fired.

Thus every frozen binary marker has horizon sensitivity 1, specificity 0 and binary-marker AUC 0.5 in both frozen ensembles.

The denominator theorem explains the inferential failure: perfect event-conditioned precedence constrains the event side of the confusion matrix but does not identify non-event firing and therefore cannot identify predictive discrimination.

### Claim firewall

The warning paper does not own joint-state sufficiency or propagation. It does not claim that alignment, connectivity or any other omitted state coordinate would rescue the frozen thresholds. It invalidates these six rules as predictive warnings in the tested state; it does not establish that genetic diversity generally contains no predictive information.

### Publication role

Keep this paper separate. Its novelty is an **evaluation/denominator problem**, whereas the state paper is a **representation/forecast-horizon problem**. Combining them would invite the unsupported causal reading that the warning failed because cross-layer alignment was omitted.

---

## Paper IV — EGWEE: empirical measurement and representation gates

**Repository:** `zuizui0223/egwee`

**Working manuscript:** `manuscript/natural_data_ecological_indicators_spine.md`

**Working title:**

> *Test the state before interpreting the residual: four empirical gates for ecological state indicators*

### Owned question

Before geography, habitat, origin or history is interpreted as residual biological information, has the proposed state/proxy first earned endpoint-relevant predictive status and has its analytical representation preserved the information it claims to contain?

### Four-gate sequence

```text
measurement adequacy
  -> representation preservation
  -> residual-context testing
  -> cross-study identifiability
```

### Empirical branches

- **Residual context adds no detected transferable gain after the locked partial state:** Honshu-Izu, Zurich, Toronto.
- **A contemporary coordinate remains missing:** *Oenothera harringtonii*.
- **A plausible process proxy fails endpoint-relevant adequacy:** *Eschscholzia californica*, Mallorca carob.
- **Preprocessing erases the intended mechanistic distinction:** *Campanula americana*.
- **Cross-origin synthesis remains non-identifiable:** STOP, not an ecological null.

### Claim firewall

These heterogeneous systems are not pooled into a common ecological effect and do not validate the EGC/EGWE simulator or genetic-warning rules. Their common contribution is the ordered empirical inference gate.

### Publication role

Primary target remains **Ecological Indicators** in the present form. A Methods in Ecology and Evolution route is conditional on separately developing reusable gate code and truth-known simulation benchmarks; prose reframing alone is insufficient.

---

## Series-level story

The papers should be cross-referenced by **question progression**, not marketed as four parts of one required reading sequence.

### One-sentence programme story

> **Eco-genetic prediction can fail at several distinct layers: biological states can separate under the same structural change, analytical summaries can erase future-relevant state structure, temporally early markers can lack event discrimination, and empirical proxies can fail before residual context is interpretable.**

### Four questions for readers

1. **What breaks?** — EGC.
2. **What information must be retained to forecast it?** — EGWE state.
3. **When is an early signal actually predictive?** — EGWE warning.
4. **Can the required biological state be measured and represented in natural data?** — EGWEE.

---

## Submission priority

### Priority 1 — EGWE state validity

Finish first. The authoritative positive result is now the constructive next-transition counterexample plus the separately locked 1,500-pair horizon-dependent propagation curve. Manuscript revision should foreground these two linked results and demote operator-portability negatives to a supporting generalisation/boundary section.

### Priority 2 — EGC

The numerical/theorem programme is closed enough for the active claim. Complete literature/novelty placement, remove sufficiency-language overlap with EGWE and finalise the standalone state-separation paper.

### Priority 3 — EGWE warning validity

Keep the compact denominator theorem + frozen full-denominator audit. Do not reopen thresholds, endpoints or continuous-score searches merely to enlarge the paper.

### Priority 4 — EGWEE natural-data four-gate paper

Continue as the independent empirical methodological synthesis. Do not reopen pooled cross-origin modelling or use natural anchors as external validation of the synthetic model.

---

## Global no-go rules

- Do not merge the state and warning papers by implying that missing alignment caused warning failure.
- Do not use EGC fragmentation-gradient state separation as a proof of EGWE forecast sufficiency.
- Do not use the post-Phase-V propagation experiment as if it were part of original Phase V.
- Do not interpret the generation-20 readout as a universal biological threshold.
- Do not use natural datasets as validation of the finite synthetic closure.
- Do not pool heterogeneous natural systems merely to obtain one cross-system effect.
- Do not reopen frozen warning thresholds, endpoints, seeds or schedules after the negative full-denominator result.

## Current authoritative homes

- EGC mechanism/state separation: `zuizui0223/eco-genetic-criticality`
- EGWE state + warning: `zuizui0223/eco-genetic-warning-extensions`
- EGWEE natural-data four-gate manuscript: `zuizui0223/egwee`
