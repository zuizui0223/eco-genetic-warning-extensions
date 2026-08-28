# N3 Mallorca network process-adequacy preregistration

## Status

This protocol is frozen **after** response-firewalled Stage A and **before** project-computed use of the focal reproductive outcome values or any visitation–fitness association.

Stage A recovered 41 eligible species×year rows from 22 plant species (2016: 21; 2017: 20) in Dryad `10.5061/dryad.hqbzkh1bm`. The five excluded species×year rows are excluded solely because that plant has no row in the corresponding year's direct-visitation network. No row was excluded because of the value of `SeedsFlowerRounded`, `DPD`, or `FloralUnitSize`.

## Question

Does source-defined direct flower visitation earn held-out predictive information for seed production across plant species in this Mallorca island community?

This is an N3 **B1 process-adequacy** test. It is not an island–urban comparison, does not estimate an island effect, and does not open any residual-context B2 test because no comparable upstream context coordinate is preregistered for this system.

## Frozen ecological unit and holdout

- analysis row: plant species × study year;
- independent held-out unit: **plant species**;
- leave-one-species-out (LOSO): all available years for one species are held out together;
- species×year rows from one species are never treated as independent holdouts.

## Frozen process coordinate

For each eligible species×year row, `I_visit` is the **sum across all pollinator columns of that plant's row in the corresponding quantitative network matrix**.

The source defines every matrix link weight as the average number of visits per flower in an observation period of 5 min. Therefore the row sum retains the same source unit: total observed flower-visitation rate per flower per 5 min across pollinator taxa.

No network centrality, d', linkage level, acting/target indirect-effect index, pollinator richness, or later-representation proxy may substitute for `I_visit` after outcomes are opened.

## Frozen response and baseline coordinates

Primary response:

- `SeedsFlowerRounded` from `Sheet 3_SEMvariables`.
- This is the source's rounded seeds-per-flower response used with a Poisson log-link component model.

Baseline state terms:

- study year;
- `DPD` (source-defined degree of pollinator dependence);
- `FloralUnitSize`.

The source paper explicitly treats pollinator dependence and flower size as direct predictors that may affect seed production independently of network position. They are therefore fixed baseline terms rather than selected after seeing this project's result.

No seed-weight endpoint, network metric, flower-abundance term, interaction with year, polynomial term, or alternate response family is permitted as a same-outcome rescue.

## Frozen models

Within each LOSO fold, continuous predictors are standardized using **training-fold mean and SD only**.

Restricted model:

`M0: SeedsFlowerRounded ~ Year + z(DPD) + z(FloralUnitSize)`

Process model:

`M1: SeedsFlowerRounded ~ Year + z(DPD) + z(FloralUnitSize) + z(I_visit)`

Both use a Poisson GLM with log link, matching the source response family. No species random intercept is included because prediction is explicitly to a held-out species unseen in training.

## Frozen score and decision

For each held-out species, sum row-wise Poisson negative log likelihood over all of its available study years.

Define

`DeltaNLL_species = NLL(M1) - NLL(M0)`.

Aggregate by summing `DeltaNLL_species` over held-out species.

Uncertainty is a 10,000-draw nonparametric bootstrap of **species-level** delta values with seed `20260828`.

Decision:

- `process_information_detected` only if total `DeltaNLL < 0` **and** the species-bootstrap 95% CI upper bound is `< 0`;
- otherwise `no_detected_process_information`;
- if the frozen Poisson models cannot be fit or validly scored in the declared LOSO folds, `primary_model_not_identifiable`.

## Claim ceiling

A positive result would mean that direct source-defined visitation adds transferable predictive information for the source's seeds-per-flower endpoint across held-out plant species in this one Mallorca community.

A null result would mean only that this declared direct-visitation coordinate did not earn that predictive information under the frozen LOSO design. It would not show that pollinators are biologically irrelevant.

Neither result is an independent island system replication at the level of landscapes, and neither licenses island–urban convergence.

## Stop rules

After this protocol is committed, do not:

1. replace `I_visit` with centrality, linkage, d', pollinator richness, `Act_Rate`, `Targ_Rate`, or another network summary;
2. switch from `SeedsFlowerRounded` to seed weight or another fitness endpoint;
3. add/remove baseline predictors after seeing outcome scores;
4. add year interactions or nonlinear process terms after seeing the result;
5. drop held-out species because their delta is unfavorable;
6. use the 41 species×year rows as 41 independent bootstrap units;
7. tune thresholds, bootstrap seed, model family, or eligibility after fitting;
8. infer island–urban equivalence or difference from this one island community.
