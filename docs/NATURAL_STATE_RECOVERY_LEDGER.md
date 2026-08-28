# Natural-state recovery ledger

This ledger separates successive empirical questions. They must not be collapsed into one urban-versus-island claim.

## N1 — can the existing Honshu–Izu and Zurich archives directly identify urban–island convergence?

Hypothesis:

`F_future ⟂ origin | S_measured`.

Decision:

`cross_origin_convergence_not_identifiable_from_existing_archives`.

Reason:

- Honshu–Izu and Zurich do not use the same biological state coordinates;
- their realised-function responses are not prospectively interchangeable;
- `origin == study/protocol identity`, so an origin coefficient would also be a study/taxon/method coefficient;
- generic z-scoring is not a biological harmonisation method.

This does not show that urban and island systems differ. It shows that the direct equality is not identified by those two archives.

## N2 — is the missing matched state merely a feature of those two archives?

N2 prospectively locked five urban and five island pollination studies and scored whether state layers were both measured and retained in reusable public representations.

Decision:

`N2_measurement_representation_gap_prevents_direct_cross_origin_test`.

Locked bounded-registry facts:

- direct reusable `I + F` both scored `yes`: urban 3/5, island 0/5;
- reusable process-specific connectivity `C`: 0/10;
- reusable contemporary mating/genetic state `G`: 0/10;
- full intended proximal-state stack: 0/10.

Interpretation boundary:

The island 0/5 result is **not** an estimate that island studies lack pollination-function information. Several source papers measured reproduction even when their public archive description did not demonstrate a joinable response layer. N2 therefore identifies information loss between biological measurement and reusable representation in that bounded registry.

### Independent urban residual-context replication: Toronto

A separate prospectively frozen Toronto community-garden analysis reached the residual-context stage. Whole gardens were held out. `M0` contained phytometer identity, effort-standardised direct visitation, focal floral units and source-matched garden floral richness; `M1` added urban cover and green-space edge density.

After the response-firewalled case-only normalization of the four already-preregistered phytometer codes, 28 eligible rows from 10 gardens remained. The locked result was:

- `Delta NLL = NLL(M1)-NLL(M0) = +4932.9195`;
- garden-bootstrap 95% CI `[+603.9654,+10953.6611]`;
- decision **`no_detected_residual_urban_context_information`**.

This is an independent urban replication of the narrower residual-context pattern already seen in Zurich: under the declared partial state and held-out design, adding the upstream urban context did not improve transfer. It is not evidence that urban context is biologically irrelevant, that the measured state is complete, or that urban systems as a class behave one way.

## N3 — is N2's island 0/5 pattern general to island open-data systems?

N3 was opened only after the N2 decision was fixed. It is not a candidate replacement or rescue of N2.

The first-pass island registry prospectively contains four systems:

1. Mallorca carob orchards — landscape/local management + pollinator visitation + fruit/seed production;
2. Balearic `Cneorum tricoccon`–`Podarcis lilfordi` — pollination census + fruits/seeds in one Dryad archive;
3. Mallorca community network–fitness study — visitation/network data + seeds per flower/seed weight;
4. Terceira apple orchards — orchard/landscape context + visitation + fruit/seed/apple function.

N3 first established that `island 0/5 in N2` does not imply that island process-function archives do not exist. All four N3 studies measured direct visitation and realised reproduction at study level, and raw schema work recovered reusable process/function material in multiple systems.

### Mallorca carob became the first N3 fit-capable island system

The deposited carob workbook retained 20 orchards, 37 orchard-year rows and 568 tree rows with fruit production, direct pollinator abundance, natural-habitat context, farming system and male:female ratio. Stage A also found two non-identical source-deposited `PolinAbun` representations, so both were frozen as mandatory rather than selecting one after outcomes.

Before project-computed reproductive-outcome fitting, the contract fixed:

- primary endpoint: `TotalFruits` with `log(TotalFlowers)` exposure;
- holdout: whole orchard;
- model family: NB2;
- B1: year-only versus year + direct pollinator abundance;
- B2: residual context opens only if **both** pollinator-abundance representations pass B1;
- orchard bootstrap seed/count and no-rescue stop rules.

The one-shot result was:

- embedded `FruitProduction.PolinAbun`: `Delta NLL = -0.10195`, 95% CI `[-3.12202,+3.61919]`;
- joined `PollinatorAbundance.PolinAbun`: `Delta NLL = -0.09919`, 95% CI `[-3.14415,+3.66453]`;
- both decisions: `no_detected_process_information`;
- final decision: **`process_measurement_not_supported_for_primary_endpoint`**;
- B2 residual-context test: **not opened**.

This is a measurement-adequacy boundary. It does not show that pollinators do not affect carob reproduction and does not test whether landscape/management context is redundant, because the process coordinate did not first earn held-out predictive adequacy for the locked fruit-production endpoint.

### Other N3 island systems remain representation/alignment candidates

- The `Cneorum` archive co-deposits pollination censuses and fruit/seed data, but the observational pollinator-census and lizard-exclusion reproductive experiment are distinct source-design components; same-archive status alone does not establish a valid row/unit join.
- The Mallorca network–fitness archive contains direct visitation-network and fitness material. A later same-data representation exposed incomplete species-by-year overlap (2016: 21/23; 2017: 20/23), so it is not treated as a complete direct-visitation join merely because both files exist.
- The Azores study measured context, visitation and reproduction, but the currently verified public supplement still does not demonstrate a reusable orchard-level reproductive table sufficient for the preregistered fit gate.

Current N3 decision:

`island_process_function_archives_recovered_and_first_fit_capable_system_failed_process_adequacy_gate`.

Therefore N3 rejects the over-generalised interpretation of N2, but it does **not** supply an island residual-context comparison to pair with Toronto/Zurich. The first fit-capable island case stopped one gate earlier.

## Current empirical rule

The natural-data programme now directly supports this order:

`biological measurement`
`-> reusable representation`
`-> endpoint-relevant predictive adequacy`
`-> residual origin/context test`
`-> cross-system transfer`
`-> only then cross-origin convergence`.

Toronto reached the residual-context gate and found no transferable gain from its added urban coordinates. Mallorca carob stopped at endpoint-relevant predictive adequacy. The contrast is itself informative: **context redundancy is not a meaningful question until the candidate process state has first earned predictive state status for the endpoint.**

This is the empirical counterpart of the constructive state-sufficiency result: information can exist in the biological system or source study while being lost, misaligned or non-predictive in the representation used for forecasting.

## What remains open

The strongest cross-origin hypothesis remains open:

`P(F_future | S, island) = P(F_future | S, urban)`.

A decisive test requires at least two independent systems per origin with:

- matched biological state semantics;
- matched direct function semantics;
- verified cross-layer join/alignment;
- the candidate process state first showing endpoint-relevant predictive adequacy;
- origin replicated independently of study identity;
- whole-system/landscape held-out validation.

N1–N3 progressively identify why this test has not yet been earned. Toronto strengthens the urban residual-context evidence, while carob shows that a nominally direct island process measurement can fail the earlier predictive-adequacy gate. Neither is evidence for ecological equivalence or difference between urban and island systems.
