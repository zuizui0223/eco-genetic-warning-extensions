# E3 preregistration — Southern Norway fragmented-landscape residual-context test

## Status and source lock

This is a **prospective declaration written before inspecting the downloaded Dryad workbook**. The source is fixed to Lázaro et al. (2020), *Ecological Applications* 30:e02099, Dryad DOI `10.5061/dryad.d51c59zzj`.

The published design contains 24 habitat fragments in an agricultural landscape and four focal wild-plant species. It jointly measured fragmentation/context variables, floral and pollinator-community state, visitation rates, and direct seed-production endpoints.

This analysis is deliberately a **falsification complement** to E1 Honshu–Izu and E2 Zurich. It asks whether a proximal measured interaction state is sufficient to make landscape fragmentation context predictively redundant. A positive residual-context result is scientifically acceptable and would indicate that the measured state is incomplete.

## Question

> After conditioning on the measured floral/pollinator/visitation state, do patch geometry and surrounding landscape still improve held-out prediction of direct seed production?

The target is not a significant fragmentation coefficient in isolation. The target is transferable residual information after the process state is supplied.

## Fixed endpoint family

All four focal plant species in the locked dataset are retained. No species is selected or dropped because its result is convenient.

Primary direct-function endpoint: the archived **seed-set / seed-production** measure used by the source study for each focal species.

Secondary endpoint: seed weight, if it is present in the same synchronized fragment/species table.

If a species lacks enough independent fragments to support leave-one-fragment-out prediction after complete-case synchronization, it is labelled `not_identifiable_for_species`; it is not replaced by another species.

## Candidate process state

The primary measured ecological state is fixed semantically before schema inspection:

- focal-species visitation rate / visits per flower;
- pollinator abundance or total visits where synchronized;
- pollinator functional-group richness and/or evenness where synchronized;
- local flower abundance and flower richness where synchronized;
- focal-species identity is handled by analysing species separately rather than pooling species into one coefficient.

No new network or diversity metric is opened after seeing the residual-context result.

## Upstream landscape/context block

The residual-context block is limited to the fragmentation variables declared in the source study:

- patch size;
- patch isolation;
- patch complexity;
- percentage forest in the surrounding landscape.

A variable is used only if it is directly present in the locked workbook or uniquely reconstructable from a source table without imputation. No alternative buffer radius or transformed landscape metric is searched after outcomes.

## Model sequence

For each of the four focal species, on an identical complete-case row set:

### E3-S0 — coarse local state

`F ~ local flower abundance + local flower richness`

Use only fields that are directly synchronized at the focal fragment/species level.

### E3-S1 — proximal process state

`F ~ local floral state + visitation + pollinator abundance/richness/evenness`

The exact archived column names are mapped after discovery; unavailable components are omitted for synchronization reasons and the omission is recorded.

### E3-S2 — residual landscape-context model

`E3-S1 + patch size + isolation + complexity + surrounding forest`

No S1×landscape interactions are opened unless an equivalent interaction is explicitly part of the archived source analysis code/table and can be declared before fitting the residual-context comparison.

## Validation unit

Primary validation is **leave-one-fragment-out** prediction. Every observation from the held-out fragment is excluded from fitting in that fold.

Random row splits are prohibited.

For each species and model retain:

- held-out squared error / MSE;
- held-out absolute error / MAE;
- fold-wise difference `S2 - S1`;
- the number of fragments in which S2 improves on S1.

## Decision rule

The conclusion is endpoint-specific; the four species are not pooled into one universal fragmentation effect.

For a species with `n` identifiable fragment folds, let `W` be the number of folds with lower squared error under S2 than S1. Compute the exact one-sided sign-test probability under `W ~ Binomial(n, 0.5)`.

Because four focal species are predeclared, use `alpha = 0.0125` for the species-level residual-context call.

- **residual_context_detected**: S2 has lower aggregate held-out MSE than S1 **and** the one-sided sign test for fold-wise improvement has `p < 0.0125`.
- **no_detected_residual_context**: S2 does not lower aggregate held-out MSE and the improvement sign test does not pass `0.0125`.
- **mixed_predictive_evidence**: all other identifiable outcomes.
- **not_identifiable_for_species**: fewer than 12 independent usable fragment folds or no synchronized direct-function/process/context join.

This rule is fixed before the workbook schema is inspected. No effect-size threshold is tuned after the result.

## Interpretation

A `residual_context_detected` result means the measured ecological process state is incomplete at the tested resolution. It does **not** mean patch complexity, isolation, or forest cover is itself a universal biological regime variable.

A `no_detected_residual_context` result supports only partial-state convergence for that focal species and observation scale. It does not establish full eco-genetic convergence because `G/C/R/M/A` are not synchronously measured.

## Stop rules

Do not:

1. select only species that support convergence or only species that support residual context;
2. search alternate buffer radii, landscape indices, pollinator metrics, or outcome definitions after seeing results;
3. impute missing process or context values from other fragments;
4. randomly split rows from the same fragment across training and test sets;
5. interpret a null visitation coefficient as evidence that interactions are irrelevant;
6. convert any one natural-system numerical threshold into a universal fragmentation cutoff.
