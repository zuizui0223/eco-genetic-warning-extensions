# Perfect precedence versus predictive discrimination theorem

Status: exact finite-denominator theorem for the binary horizon marker used by the warning-validity paper.

## Question

The empirical result is striking but the general principle can sound obvious:

> a marker can occur before an event and still have false positives.

The stronger question is exact:

> **If a binary warning rule precedes every observed event, what full-denominator predictive quantities are mathematically forced, and which remain completely free?**

## Setup

Fix a common administrative horizon. Let

- `Y=1` denote the target event by the horizon;
- `M=1` denote that the frozen marker fired by the horizon.

Assume there is at least one event and one non-event. Perfect event-conditioned precedence means every event trajectory has a marker time strictly before its event time. Therefore every event is marker-positive by the horizon.

Let `n1` be the number of event trajectories, `n0` the number of non-events, and `f` the number of non-events in which the marker also fires.

## Theorem P1 — perfect precedence forces sensitivity, but not specificity

Under perfect event-conditioned precedence,

\[
\boxed{\mathrm{sensitivity}=1.}
\]

But for fixed `n0`, every specificity value on the finite grid

\[
\boxed{\left\{0,\frac1{n_0},\ldots,1\right\}}
\]

is compatible with exactly the same perfect event-conditioned precedence statement.

### Proof

Because every event has `M=1`, all `n1` events are true positives and none are false negatives. Hence sensitivity is 1.

Precedence is conditioned on event trajectories and imposes no condition on marker status among the `n0` non-events. Choose any integer `f` from 0 to `n0` and let exactly `f` non-events be marker-positive. Then

\[
\mathrm{specificity}=\frac{n_0-f}{n_0}.
\]

As `f` ranges from `0` to `n0`, specificity ranges over the stated grid while the event trajectories—and therefore the perfect precedence statement—are unchanged. ∎

## Theorem P2 — exact binary-marker AUC under perfect precedence

For a binary score, AUC is

\[
\boxed{\mathrm{AUC}=\frac{\mathrm{sensitivity}+\mathrm{specificity}}2.}
\]

Therefore under perfect precedence,

\[
\boxed{\mathrm{AUC}=\frac{1+\mathrm{specificity}}2
=1-\frac{f}{2n_0}.}
\]

Thus the same perfect event-conditioned precedence is compatible with binary-marker AUC values from `0.5` to `1` on the corresponding finite grid.

### Proof of the binary-score identity

The ROC curve for a binary score has the points

\[
(0,0),\quad(\mathrm{FPR},\mathrm{TPR}),\quad(1,1).
\]

Its trapezoidal area is

\[
\frac12\mathrm{FPR}\,\mathrm{TPR}
+\frac12(1-\mathrm{FPR})(1+\mathrm{TPR})
=\frac12(1+\mathrm{TPR}-\mathrm{FPR}).
\]

Since `TPR=sensitivity` and `1-FPR=specificity`, this becomes

\[
\frac12(\mathrm{sensitivity}+\mathrm{specificity}).
\]

Substituting sensitivity 1 from Theorem P1 gives the result. ∎

## Corollary P2a — chance discrimination is a sharp endpoint, not a contradiction

When all non-events are marker-positive, `f=n0`, so

\[
\mathrm{specificity}=0,
\qquad
\mathrm{AUC}=0.5.
\]

The marker still precedes every event. Therefore

\[
\boxed{\text{perfect precedence and chance binary discrimination are jointly attainable}.}
\]

The EGWE result realizes this sharp endpoint in both audited ensembles.

## Corollary P3 — positive predictive value is also not fixed by precedence

Under perfect precedence,

\[
\mathrm{PPV}=\frac{n_1}{n_1+f}.
\]

Hence PPV depends on both non-event firing and event prevalence. Perfect event-conditioned ordering alone does not determine it.

When `f=n0`,

\[
\mathrm{PPV}=\frac{n_1}{n_1+n_0},
\]

which is exactly event prevalence: the binary marker supplies no horizon-level enrichment over knowing prevalence alone.

## Locked EGWE data attain the worst-discrimination endpoint

### Inherited ensemble

- events: `n1=35`;
- non-events: `n0=48`;
- all 35 events have marker before loss;
- all 48 non-events are marker-positive by the common horizon.

Theorems P1–P3 therefore give

\[
\mathrm{sensitivity}=1,
\quad
\mathrm{specificity}=0,
\quad
\mathrm{AUC}=0.5,
\quad
\mathrm{PPV}=35/83\approx0.422.
\]

### Fresh ensemble

- events: `n1=33`;
- non-events: `n0=49`;
- all 33 events have marker before loss;
- all 49 non-events are marker-positive.

Thus

\[
\mathrm{sensitivity}=1,
\quad
\mathrm{specificity}=0,
\quad
\mathrm{AUC}=0.5,
\quad
\mathrm{PPV}=33/82\approx0.402.
\]

The empirical audit is therefore not merely an example with some false positives. It lands at the **sharp minimum-discrimination endpoint compatible with perfect sensitivity for a binary marker**.

## What this theorem changes

The safe general result is not just

> “precedence does not imply prediction.”

It is:

> **perfect event-conditioned precedence identifies sensitivity but leaves non-event specificity unconstrained; for a binary horizon marker, discrimination can therefore range from chance to perfect without changing the event-conditioned lead result.**

This is a denominator theorem. It shows exactly which information is deleted by conditioning only on event trajectories.

## Claim ceiling

The theorem concerns:

- binary horizon markers;
- a shared administrative horizon;
- event-conditioned perfect precedence;
- standard binary-score ROC/AUC.

It does not characterize continuous time-dependent scores, competing-risk ROC curves, censoring estimators beyond the fixed horizon, or every possible early-warning statistic. Those require separately declared prediction objects.

## Executable obligations

`tests/test_precedence_discrimination_theorem.py` must verify:

1. every finite specificity grid point is compatible with perfect event sensitivity;
2. binary AUC matches an independent pairwise-ranking oracle;
3. AUC ranges from 0.5 to 1 while precedence is fixed;
4. `f=n0` gives specificity 0, AUC 0.5 and PPV equal prevalence;
5. the inherited 35/48 and fresh 33/49 locked denominators reproduce the manuscript metrics exactly.
