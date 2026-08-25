# Prospective Campanula effective-interaction state discovery

## Purpose

The preceding empirical programme separated two failure modes:

1. a measured pollinator proxy can exist but fail to earn endpoint-relevant held-out predictive status (*Eschscholzia californica*); and
2. a conceptually stronger realised-visitation variable can be schema-joinable yet absent on every response-bearing unit (experimental-colonization *Campanula*).

The next independent test therefore asks a stricter measurement question:

> **Can realised pollinator visitation be calibrated by independently measured per-visit functional efficiency, without using population pollen-limitation outcomes to define the interaction state?**

The source is Koski et al. (2018), *Linking pollinator efficiency to patterns of pollen limitation: small bees exploit the plant–pollinator mutualism*, with data archived at Dryad doi:`10.5061/dryad.5nj81nf` and mirrored at Zenodo record `4969330`.

The source study reports 23 natural populations of *Campanula americana* and separates population-level pollen limitation / visitation from single-visit measurements used to quantify pollen deposition, seed-set and pollen-removal efficiency by pollinator group. This separation makes the archive a candidate for a non-circular **effective-interaction state**.

## Source lock before workbook inspection

Fixed source:

- Zenodo record: `4969330`;
- file: `Koski et al. 2018_Data_ProcRoySoc.xlsx`;
- published MD5: `2d26307743e8a22384781854b8f2f33b`;
- underlying Dryad DOI: `10.5061/dryad.5nj81nf`.

No alternate version, supplementary workbook, publication table or manually reconstructed dataset may replace this file after inspection begins.

## Schema-only boundary

This first stage may inspect only workbook structure needed to decide whether a prospectively defined effective-interaction analysis is possible.

Allowed outputs:

- file byte size, MD5 and SHA-256;
- workbook sheet names;
- sheet dimensions;
- cell **types** in the first 10 rows;
- string labels/text in the first 10 rows of each sheet;
- string-only text from a sheet whose title explicitly contains `metadata`, limited to the first 100 rows;
- candidate identifier/header tokens derived only from those string labels.

Not allowed:

- numeric data-cell values;
- population pollen-limitation values;
- visitation frequencies;
- efficiency measurements;
- means, variances, correlations or group contrasts;
- fitted models, coefficients, p-values or effect directions;
- selecting pollinator groups or efficiency definitions from observed outcomes.

The discovery artifact must contain no numeric outcome or predictor values from the study.

## Fixed conceptual mapping target

From schema labels only, determine whether the workbook contains defensible, separable representations of:

### Population endpoint layer

- population identity (`P`);
- population-level pollen limitation or enough source-defined fields to construct it (`F_PL`);
- realised visitation frequency by pollinator group (`I_visit`).

### Independent calibration layer

At least one single-visit calibration family that is **not defined using population pollen limitation**:

- pollen deposited on stigmas per visit (`E_deposition`);
- seed-set consequence per visit (`E_seed`);
- pollen removal per visit (`E_removal`).

The calibration layer must contain a pollinator-group identity that can be mapped prospectively to the group labels in the population-visitation layer without using numerical outcome patterns.

## Prospective effective-interaction state

If schema permits it, a later analysis may compare raw visitation with an independently calibrated interaction representation such as:

`I_effective = Σ_g visitation_g × efficiency_g`

where every `efficiency_g` weight is estimated **only from the independent single-visit calibration layer**. Population pollen limitation may never be used to choose or estimate those weights.

The exact efficiency family, aggregation rule, model sequence, validation unit and decision rule are **not opened in this discovery PR**. They must be fixed in a second preregistration after schema-only inspection and before any numeric data row is read.

## Required discovery decision

The schema-only stage must end in exactly one of:

- **`effective_interaction_state_identifiable`** — population identity, pollen-limitation endpoint, group-specific realised visitation and at least one independently measured single-visit efficiency family are present, and pollinator-group labels can be mapped between population and calibration layers from schema/text alone;
- **`partial_effective_interaction_state_identifiable`** — population PL and group visitation are present and calibration data exist, but one required key/group mapping or calibration family cannot be linked without numeric inspection; a bounded preregistered test may still be possible;
- **`not_identifiable_from_archive`** — the required endpoint, visitation, independent calibration or label mapping cannot be established without outcome-informed reconstruction.

All three outcomes are acceptable.

## Claim ceiling

A successful discovery does not establish that large or small bees are beneficial, harmful, efficient or inefficient. It establishes only that the archive can support an outcome-independent calibration test.

The eventual scientific claim, if the second stage succeeds, is about **measurement adequacy of an effective interaction state**, not a universal pollinator-size rule.

## Stop rule

Do not inspect numeric rows to choose a pollinator grouping, efficiency family, population subset, transformation or interaction score. Do not derive efficiency weights from population pollen limitation. If schema labels are insufficient, retain the corresponding partial/not-identifiable decision rather than repairing the archive from the publication results.