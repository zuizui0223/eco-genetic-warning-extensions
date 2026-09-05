# Prospective Cirsium natural bridge for the EG flagship

## Status

**Design-only prospective bridge. No outcome may be inspected or model selected using this document after data collection begins.**

This bridge is not required to assemble the current Nature Ecology & Evolution flagship. Its purpose is to provide the single strongest future test of the flagship hierarchy in one natural system if field data collection permits it.

## Central question

> In a natural plant–pollinator system, does a prospectively measured joint ecological/genetic state improve held-out prediction of later reproductive function beyond coarse contextual or marginal summaries, does an early signal add full-denominator predictive information after that state is known, and does origin/history add residual information only after the measured state has earned endpoint relevance?

## Why Cirsium is the preferred bridge candidate

The active Cirsium field programme can, in principle, synchronize several coordinates that are separate in the current EG evidence stack:

- local environmental / fragmentation or island context;
- floral resource and focal-plant density;
- repeated pollinator visitation from field cameras;
- pollinator guild / interaction composition;
- plant floral phenotype and target-relevant trait coordinates;
- spatial neighbourhood / potential mating opportunity;
- plant genetic state from prospectively collected tissue;
- later fruit, viable seed or recruitment outcome on the same focal units.

The bridge therefore tests the hierarchy within one empirical system rather than treating the existing seven natural analyses as external validation of the synthetic model.

## Unit hierarchy

The design should preserve at least three explicit levels:

1. **focal reproductive unit / plant** — repeated interaction measurements and later reproductive outcome;
2. **population / site** — ecological holdout unit and local spatial/genetic context;
3. **origin / island / region** — upstream context tested only after the measured state has earned endpoint relevance.

The primary validation split must be at the population/site level or at a stricter independent validation-cohort level. Observation-level random splitting is forbidden.

## Prospective state map

For each focal plant or population, define a pre-outcome state using only measurements available before the future reproductive endpoint is opened.

### D — upstream context

Candidate coordinates may include island/region identity, habitat configuration, local land-cover context, elevation or other environmental covariates already fixed by the field design.

These variables are contextual predictors, not assumed biological state sufficiency.

### R — local resource / demographic support

- focal floral-unit density;
- local conspecific flowering density;
- neighbourhood floral support if prospectively standardized;
- focal plant size or display size if measured before the outcome window.

### I/T — realised interaction state

From repeated camera or direct observations, prospectively define:

- effort-standardised visitation intensity;
- pollinator guild composition;
- focal visitation diversity or interaction distribution;
- trait-weighted or function-weighted interaction coordinates only if their weighting is defined before outcome inspection.

Raw visitation and any richer effective-interaction representation must remain separately identifiable before preprocessing.

### C/M — connectivity / mating opportunity

Candidate coordinates:

- spatial neighbourhood density and distance-weighted flowering opportunity;
- prospectively defined pollen/mating connectivity proxy;
- where available, parentage or seed-cohort information used only in the role declared before outcome access.

A numeric connectivity value is not assumed comparable across different biological operators.

### G — genetic state

Prospectively selected genetic summaries may include individual/population heterozygosity, allelic richness or ancestry coordinates if the marker panel and preprocessing are fixed before the reproductive endpoint is opened.

No genetic summary is labelled an early warning merely because it is biologically plausible.

### A — cross-layer alignment

Define alignment only after the component layers are fixed. Candidate primary alignment objects should be simple and auditable, for example spatial covariance or rank concordance between interaction support and the focal genetic/trait-support coordinate across plants within a population.

Do not search among multiple alignment metrics after seeing reproductive outcomes.

## Future endpoint

### Primary continuous endpoint

Use a prospectively fixed later reproductive-function measure on the same focal unit, preferably viable seed production or a standardized seed/fruit-set outcome with exposure/display handled according to the field protocol.

The primary analysis should remain continuous where possible to avoid manufacturing an event threshold.

### Secondary binary event for full-denominator warning validation

If a biologically defensible binary event can be locked **before outcome inspection**, evaluate it on every eligible focal unit through one common horizon. A preferred event definition is complete reproductive failure of the declared focal unit (for example, zero viable seed) if biologically meaningful and sufficiently observable.

If event prevalence is too low for the preregistered validation rule, retain `not_estimable`; do not invent a new post-result threshold.

## Candidate early signal

The natural bridge does not need to reuse the six frozen synthetic diversity thresholds. Instead, predeclare one early signal that is available before the reproductive endpoint, such as a low-interaction or low-pollen-receipt state derived from the early observation window.

The signal must be evaluated on the **full eligible denominator**, including later event and non-event units. Temporal precedence among eventual failures is secondary; discrimination and calibration are primary.

No threshold may be optimized on the validation cohort.

## Nested predictive comparison

Fit the same declared model family under ecological holdout for the following nested information sets:

### M0 — context only

`D`

Purpose: establish how much future function is predictable from upstream context alone.

### M1 — coarse biological marginals

`D + R + marginal I/T + marginal G`

Purpose: supply the ordinary layer-wise summaries without cross-layer organization.

### M2 — joint/process state

`M1 + C/M + A`

Purpose: test whether mating/connectivity and cross-layer organization improve future prediction beyond coarse marginals.

### M3 — early signal only

`D + W`

Purpose: evaluate the candidate signal as an actual predictive object rather than a lead-time description.

### M4 — joint state + early signal

`M2 + W`

Purpose: test whether the signal adds information after the measured process state is known.

### M5 — residual origin/history

`M4 + origin/history`

Purpose: test origin/history only after the state and signal have passed their upstream gates.

## Primary estimands

1. held-out predictive performance of M1 vs M2;
2. held-out predictive performance of M2 vs M4;
3. held-out predictive performance of M4 vs M5;
4. for the binary event, sensitivity, specificity, false-positive rate, predictive values and AUC of `W` on the full denominator;
5. stability of the above comparisons across prospectively declared independent populations / validation cohorts.

The exact scoring rule must be matched to the endpoint and frozen before validation outcomes are opened.

## Decision logic

### Bridge-supported state result

Supported only if M2 improves held-out future prediction beyond M1 under the preregistered criterion.

A failure is informative: the measured joint state may be insufficient, the added coordinate may be irrelevant at the sampled scale, or precision may be inadequate. Do not rescue the claim through feature search.

### Bridge-supported warning result

Supported only if `W` shows prospective discrimination on the full denominator and, for the strongest claim, adds held-out information beyond M2 in M4.

Perfect lead ordering among failures alone is not success.

### Residual-context result

Interpret M5 only if the upstream measurement and representation gates are open. A negative M5 comparison does not prove complete state measurement; it means no transferable residual origin/history information was detected under the declared state and design.

## Representation audit before outcome access

Before fitting any endpoint model:

- check whether intended richer predictors are constant rescalings or deterministic transforms of simpler predictors;
- verify that scaling/standardisation does not erase the declared mechanistic weighting;
- record rank and correlation structure among candidate state coordinates;
- lock the exact state representation and any interaction/alignment terms.

If the richer representation collapses onto the coarse one, record the representation failure and do not silently substitute another preprocessing scheme.

## Minimum provenance

The bridge should record:

- field protocol version and date;
- exact focal-unit eligibility rule;
- measurement window and future outcome window;
- camera / observer effort normalization;
- genetic marker panel and filtering contract;
- state-variable construction code;
- held-out population/cohort split;
- frozen scoring rule and success thresholds;
- all STOP conditions;
- immutable source hashes for analysis-ready tables.

## Flagship consequence

A successful bridge would change the flagship from a hierarchy supported by complementary synthetic and natural counterexamples to a partial end-to-end natural validation of the hierarchy. That is the clearest single addition that could move the manuscript from a high-risk Nature Ecology & Evolution attempt toward a substantially stronger one.

A failed or stopped bridge remains scientifically useful if the stop occurs prospectively: it identifies which validation obligation could not be satisfied in the natural system and must not trigger post-result redesign of the current flagship evidence.
