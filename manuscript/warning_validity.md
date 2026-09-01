# Event-conditioned temporal precedence is not predictive warning validity

**Publication status:** active warning-validity manuscript.  This manuscript is
the sole active publication lane for the full-denominator warning result.  It
does not make a joint-state or cross-system convergence claim.

## Abstract

Early-warning rules are often evaluated only among trajectories that later
experience the target event.  We audited six frozen baseline-relative genetic-
diversity thresholds in two independently seeded finite-model ensembles without
changing endpoints or rerunning trajectories.  Every threshold preceded every
observed functional-trait loss in the inherited and fresh ensembles (35/35 and
33/33), but every threshold also fired in every non-event trajectory by the
common horizon (48/48 and 49/49).  Full-horizon sensitivity and false-positive
rate were therefore 1, specificity was 0, and binary-marker AUC was 0.5 in both
ensembles.  Event-conditioned temporal precedence can thus reproduce perfectly
while providing no horizon-level discrimination.  The result invalidates these
six rules as predictive warnings in the tested state; it does not show that
genetic diversity contains no predictive information or that no alternative
warning statistic could succeed.

## Introduction

A precursor may occur before every observed failure and still be useless for
predicting which units will fail.  The distinction is a denominator problem.
Event-conditioned ordering estimates whether a threshold precedes an event
among trajectories in which both threshold and event are observed.  Predictive
warning validity additionally requires the rule not to fire indiscriminately in
trajectories that remain event-free through the same administrative horizon.

The distinction matters for genetic early-warning studies because diversity
decline is biologically plausible under deterioration and can therefore look
compelling in event-only sequences.  A perfect lead count is not, by itself,
evidence of specificity, risk separation, or prospective discrimination.  We
test that boundary using two frozen ensembles in which the loss process was
defined before warning values were opened and all baseline-eligible non-events
were retained.

Our question is deliberately narrow: do six already frozen relative-diversity
rules distinguish trajectories with realised functional-trait loss from those
without loss by a common horizon?  No threshold, seed, schedule, eligibility
rule, or endpoint was changed for this audit.

## Methods

### Provenance and separation of ensembles

The inherited ensemble comes from the pinned scientific parent repository at
commit `dd8ee379d0d3518194c767d16402042525bc00dc` and its frozen validation run
`28500796310`.  The fresh ensemble comes from the independently seeded Phase-V
run `32636847803`.  Parent and extension trajectories were audited separately
and were never pooled.

The inherited ensemble attempted 100 trajectories and retained 83 that were
baseline-eligible under the frozen rule.  Thirty-five reached realised
functional-trait loss and 48 remained event-free through the common horizon.
The fresh ensemble attempted 100 trajectories, retained 82 baseline-eligible
trajectories, observed 33 losses, and retained 49 horizon non-events.

### Frozen warning rules

The six endpoints were the first post-baseline generations at which either
`H_alpha` or `H_gamma` declined by 5%, 10%, or 20% from its own baseline.  The
fresh ensemble used the same endpoints without recalibration.  The historical
`strict_replication` decision required sufficient valid warning/loss pairs and
all valid pairs to be leads; it was a rule about ordering among valid event
pairs, not a predictive-validity classification.

### Full-denominator audit

For every endpoint and ensemble, the audit restored all baseline-eligible
trajectories.  It recorded whether the threshold fired by the administrative
horizon and whether realised functional-trait loss occurred by that horizon.
It then reported sensitivity, false-positive rate, specificity, positive and
negative predictive value, and AUC for the binary horizon marker.

Non-events remain right-censored for event-time inference but are known
event-free controls at the shared horizon.  Endpoints within a trajectory are
repeated measurements, not independent biological replicates.  Continuous AUC
was not introduced because the locked rules do not supply a common-time
continuous score.  Fixed ramp-end summaries are retained only as secondary
descriptions.

## Results

### Event-conditioned ordering reproduced

For each of the six endpoints, the inherited rule crossed before all 35
observed losses.  The independently seeded fresh ensemble reproduced the same
valid-pair ordering for all 33 observed losses.  The corresponding counts were
therefore 35/35 and 33/33, with zero ties or lags in the frozen valid-pair
classification.

This preserves the historical `strict_replication` decision as a protocol fact:
conditional on observing both a threshold crossing and a loss, the crossing
preceded the loss in both ensembles.

### The same rules fired in every non-event trajectory

Every one of the six endpoints also crossed by the horizon in all 48 inherited
non-event trajectories and all 49 fresh non-event trajectories.  Consequently,
for every endpoint in both ensembles, sensitivity was 1.0, false-positive rate
was 1.0, specificity was 0, and binary-marker AUC was 0.5.  Positive predictive
value equalled event prevalence, 0.422 in the inherited ensemble and 0.402 in
the fresh ensemble; negative predictive value was undefined because no
trajectory remained marker-negative.

Fixed ramp-end AUC ranged from `0.500` to `0.538` in the inherited ensemble and
from `0.500` to `0.510` in the fresh ensemble.  These secondary fixed-time
summaries do not rescue the frozen horizon rules.

## Discussion

### Temporal precedence is not warning validity

The two ensembles show the strongest possible separation between an
event-conditioned ordering claim and a predictive claim.  The ordering result
reproduced without exception, yet the full-denominator classifier performed at
chance because every event and every non-event crossed the same rules.  The
correct conclusion is therefore:

> Event-conditioned temporal precedence can be perfectly reproducible while
> full-denominator predictive warning validity is absent.

Loss-process calibration remains necessary: a warning cannot be interpreted
without a declared target event, eligibility rule, and horizon.  Calibration is
not sufficient, however, because selecting only trajectories with both warning
and loss removes the observations needed to estimate false-positive behaviour.

### Claim boundary

This audit rejects predictive validity for the six frozen 5%, 10%, and 20%
`H_alpha`/`H_gamma` rules in these two symmetric finite-model ensembles.  It
does not establish a universal genetic threshold, show that diversity contains
no predictive information generally, test every continuous score, or imply
that an independently specified multivariate warning could not discriminate.
No endpoint rerun or post-result threshold search is authorised by this negative
result.

The separately calibrated Protocol-003 domains remain bounded portability
evidence.  They do not identify a single-factor direction effect and are not a
substitute for the full-denominator result presented here.

## Data and code availability

The compact 1,200-row trajectory-endpoint table is stored at
`artifacts/warning_validity/trajectory_endpoint_records.csv` and is fixed by
`artifacts/warning_validity/source_manifest.json` with SHA-256
`65295c612042557abb46115a2c408b883f0b516c8d5af974423b895f54a7c7ab`.
The derived JSON and publication table are
`artifacts/prepublication_review/warning_validity_audit.json` and
`manuscript/tables/warning_validity_audit.csv`.  The audit implementation and
tests are version controlled.  Frozen trajectories and results were not
modified for this manuscript split.
