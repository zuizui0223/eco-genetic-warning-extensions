# Stage-A mapping — Mallorca carob island residual-context candidate

## Scope

This document freezes the measurement mapping for `I3_MALLORCA_CAROB_2025` before any project-level fitted outcome analysis. It does not use the source paper's reported effect directions to select predictors or endpoints.

Source study: Gómez-Martínez et al. 2025, 20 carob orchards on Mallorca Island, Spain. Data availability points to Zenodo `10.5281/zenodo.13939479`. Public PLOS/Digital.CSIC supplements independently expose the orchard context table and orchard-year pollinator-visitation table.

## Ecological unit

- independent holdout unit: **study orchard** (`n = 20`);
- repeated observation layer: **year** (2019, 2020);
- tree observations are nested within orchards and are not independent landscapes;
- the two study years are not treated as two independent island systems.

Any later validation must hold out the entire orchard across both years.

## Upstream context `O`

The source design defines, before any production outcome is used:

- `% natural habitat` within a 1-km radius landscape buffer;
- farming system: conventional versus ecological;
- male-to-female tree ratio;
- tree density as a source-defined control/support coordinate;
- sampling year as a repeated temporal coordinate.

Public representation:

- PLOS S1 Table / Digital.CSIC handle `10261/396616`: landscape and local characteristics of the 20 study orchards.

Status: `O = yes` at Stage A.

## Direct interaction state `I`

The source protocol sampled each orchard on five days in each flowering season. On each sampling day, three observers each conducted one hour of observation while walking orchard tree lines. Observation effort is therefore fixed at:

`5 days × 3 observers × 1 h = 15 observer-hours per orchard-year`.

The source recorded direct contacts of floral visitors with reproductive flower parts and retained functional groups.

Primary direct interaction intensity, if the public table matches the protocol:

`I_visit = total recorded pollinator visits / 15 observer-hours`

for each orchard-year.

The partner-resolved visit vector is retained in provenance but is not substituted for `I_visit` after outcome access.

Public representation:

- PLOS S3 Table / Digital.CSIC handle `10261/396621`: pollinator visits by group in the 20 study orchards for each sampling year.

Status: `I = yes` at Stage A.

## Local support `D`

The source study retains tree density at orchard level and directly measured flower numbers on marked female-tree branches for reproduction. Because the public supplementary context table is confirmed but the raw production table is not yet verified, Stage A retains:

- orchard tree density: reusable support/control candidate;
- flower-count denominator: source-measured but raw alignment with the production file still pending.

Status: `D = partial` until the raw realised-function table is verified.

## Realised function `F`

The source defines three non-interchangeable realised-function responses:

1. fruit production per female tree = developed fruits per 1000 flowers;
2. seed production per female tree = seeds per 1000 flowers;
3. seed weight = grams per developed seed.

These definitions are retained exactly. They are not collapsed to a generic z-score.

The paper and its methods establish that these responses were measured in both study years, but the project has not yet verified the exact Zenodo file/column schema containing the raw production observations.

Status: `F = partial` at Stage A.

## Alignment key `A`

The context and visitation supplements are explicitly orchard / orchard-year based. The source production design is tree-within-orchard by year. A valid later analysis requires the raw production file to expose an orchard identity that can be joined without reconstructing values from published figures or coefficients.

Until that raw key is verified:

`A = partial`.

Do not infer alignment merely because all data appear in one publication.

## Current Stage-A decision

`mallorca_carob_context_and_visitation_verified_function_join_pending`

The system is **not yet admitted to fitted B1/B2 analysis**.

What has been earned:

- 20 independent orchard holdouts;
- source-defined upstream context;
- direct effort-standardised visitation;
- source-defined realised function semantics;
- public reusable O and I representations.

What remains:

- exact raw F file identity;
- F column names and units;
- orchard/year/tree join key;
- missingness and eligible orchard count after the join.

## Stop rules

Do not:

1. reconstruct raw F values from figures, model coefficients, means, ranges or error bars;
2. choose one of the three F endpoints because its published relationship is favourable;
3. treat orchard-year rows as independent orchards;
4. add a pollinator-composition score, CCA axis or guild weight to the primary state merely because the source paper reports an association;
5. drop orchards based on outcome direction;
6. fit a residual-context model until the raw F/A schema is verified;
7. interpret the source paper's published inference as a new held-out replication by this project.

## Next gate

Acquire the exact Zenodo raw data through a legitimate route, inspect only file names/column names/types/keys first, and verify F/A. If that gate passes, a separate preregistration will freeze the B1/B2 held-out model before project-level outcome modelling.