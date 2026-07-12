# Protocol 002 Stage II calibration schema

## Purpose

Stage II selects at most one deterioration schedule per mutation coordinate using
trait-loss outcomes only. Warning, diversity, lead/lag, and event-pair fields are
forbidden during calibration.

## Candidate family

```text
ramp generations:              30
hold generations:              90, 210
normalised barrier increase:   0.15, 0.30, 0.45
master seeds:                  20270310–20270314
replicates per source cell:    5
```

## Eligibility

A candidate is eligible only when every independent seed-block trait-loss rate
lies in:

```text
[0.30, 0.70]
```

The pooled rate is used for ranking only; it cannot rescue an ineligible seed
block.

## Deterministic selection

Eligible candidates are ranked by:

```text
(|pooled trait-loss rate - 0.50|,
 horizon,
 normalised barrier increase,
 area_reference,
 kappa)
```

At most one candidate is selected per `(kappa_mu, p_star)` coordinate. If no
candidate is eligible, the retained result is `no_domain_selected`.

## Blind-calibration guard

Calibration inputs reject columns containing warning/diversity information,
including:

```text
h_alpha
h_gamma
warning
lead
lag
lead_time
diversity
heterozygosity
event_pair
```

This module defines schema and selection only. It does not run the Stage II
calibration campaign.