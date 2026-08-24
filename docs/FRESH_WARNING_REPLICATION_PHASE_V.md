# Phase V — fresh fixed-domain genetic-warning replication

## Question

Does the parent H2-R result that baseline-relative genetic erosion precedes realised functional-trait loss replicate in one independent fresh-seed ensemble when the calibrated domain and all six warning endpoints are frozen?

This is a C3 replication. It does not reopen C2 calibration and does not search for a more favourable domain.

## Frozen domain

The parent scientific commit remains `dd8ee379d0d3518194c767d16402042525bc00dc` and the selected H2-R validation domain is unchanged:

- symmetric allele-state transition rate `0.10`;
- `A_ref=0.8`;
- interaction feedback `kappa=6.0`;
- 30-generation ramp + 90-generation hold;
- normalized barrier increase `0.15`;
- standard finite-bin profile;
- 20 attempted replicates per master seed.

No calibration cell, schedule, or warning endpoint is reselected.

## Fresh seeds

`20291110–20291114`, five master seeds ×20 attempts = 100 attempted trajectories.

Before declaration, a repository search across both parent and extension repositories returned no match for these five seed values. No replacement or outcome-based seed selection is permitted.

## Frozen endpoint family

For both `H_alpha` and `H_gamma`, first post-baseline decline by:

- 5%;
- 10%;
- 20%.

The functional endpoint remains realised high-trait loss. Records without both warning and loss are retained as censored rather than discarded from attempted denominators.

## Primary decision

Each of the six endpoints must first have at least **20 valid same-trajectory warning/loss pairs**.

### Strict replication

All six endpoints have at least 20 valid pairs and every valid pair is a warning lead: zero ties and zero lags.

### Directional replication only

Strict replication fails, but every endpoint has at least 20 valid pairs, lead fraction is greater than 0.5, and a one-sided exact binomial test against lead probability 0.5 gives `p<0.05`, counting ties and lags as non-leads.

### Insufficient precision

At least one endpoint has fewer than 20 valid pairs.

### Not replicated

Precision is sufficient, but at least one endpoint fails the directional replication rule.

The decision order is `insufficient_precision → strict_replication → directional_replication_only → not_replicated`.

## Secondary reporting

Report attempted/source-prepared/projection-supported/trajectory-available/loss-observed denominators, warning availability, lead/tie/lag counts, lead fractions and seed-block counts for every endpoint. These do not alter the primary decision.

## Boundaries

A positive Phase-V result would replicate warning behaviour only in the already frozen symmetric H2-R domain. It would not establish:

- a universal genetic-warning threshold;
- portability to other eco-genetic domains;
- an isolated recurrent-transition-direction effect;
- warning validity under every fragmentation or movement closure.

## Stop rule

Run this one five-seed ensemble once. Do not replace seeds, add thresholds, recalibrate the domain, increase precision or add endpoint families after observing the outcome merely to obtain replication.
