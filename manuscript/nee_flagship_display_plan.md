# NEE flagship display architecture

## Rule

The main paper uses **five display items**. Every item answers one layer of the predictive-validity hierarchy. No figure is allowed to read as a standalone component-paper recap.

## Figure 1 — What must be valid before an ecological forecast is valid?

**Purpose:** define the paper before any dataset is shown.

```text
biological process / disturbance
            |
            v
      biological state X_t
            |  Gate 1: distinguish target-relevant biological objects
            v
 analytical representation phi(X_t)
            |  Gate 2: preserve future-relevant structure
            v
 candidate signal g(phi(X_0:t))
            |  Gate 3: full-denominator predictive validation
            v
      future target Y_(t+h)

natural measurement M_t --------> estimated state
                 Gate 4: endpoint relevance + representation + identifiability
```

Four red `not implied` labels:

1. common disturbance != one biological state;
2. matching marginals != matching futures;
3. perfect precedence != predictive discrimination;
4. plausible proxy != validated empirical state.

**Caption ceiling:** this is an inferential hierarchy, not a demonstrated causal mediation chain among the four empirical results.

## Figure 2 — One disturbance separates biological states

**Source:** EGC locked fragmentation gradient.

**Panel A:** potential high-trait viability vs realised occupancy.
- one patch: viability 1,037/1,037;
- every subdivision: viability 0/1,037;
- realised occupancy at generation 30 remains approximately 99.6–100%.

**Panel B:** retained interaction, local effective size and realised high-trait mass across patch counts 1,2,3,4,6,8,12,16.

Emphasize different curve shapes rather than a single fragmentation severity axis.

**Take-home label:** `same structural change != same biological state response`.

## Figure 3 — Matching summaries can hide different futures

**Panel A:** aligned vs anti-aligned constructive state pair.
- identical census and declared ecological/genetic marginals;
- covariance +0.025 vs -0.025;
- max exact next-interaction difference 0.2543.

**Panel B:** primary 1,500-pair risk-difference curve.
- g5: 0.0 pp;
- g10: +0.33 pp [-0.44,+1.11];
- g20: +5.33 pp [+2.04,+8.62];
- g40: +5.20 pp [+1.96,+8.44].

**Panel C, compact inset:** 500/1000/1500 nested precision at g20/g40 to show interval narrowing without qualitative effect reversal.

**Take-home label:** `matching marginals != dynamic equivalence`.

## Figure 4 — Perfect lead time can have chance discrimination

**Panel A:** inherited full denominator.
- events: 35/35 marker-positive before loss;
- non-events: 48/48 marker-positive by horizon.

**Panel B:** fresh full denominator.
- events: 33/33 marker-positive before loss;
- non-events: 49/49 marker-positive by horizon.

Use confusion-matrix blocks rather than six repeated threshold panels; note that all six frozen rules have the same binary validity endpoint.

**Panel C:** theorem graphic:

`sensitivity = 1`

`specificity free in [0,1] under event-only precedence`

`binary AUC = (1 + specificity)/2`

Observed specificity = 0 -> AUC = 0.5.

**Take-home label:** `temporal order != prediction`.

## Figure 5 — Natural measurements stop at different validation gates

**Source:** EGWEE seven-system gate registry.

Rows:
- Honshu–Izu
- Zurich
- Toronto
- Oenothera
- Eschscholzia
- Mallorca carob
- Campanula americana

Columns / progression:
- measurement adequacy
- representation preservation
- residual context
- cross-study identifiability

Outcome markers:
- no detected transferable residual gain;
- missing coordinate detected;
- measurement adequacy not earned / endpoint not identifiable;
- representation collapse.

Footer: cross-origin synthesis `not_identifiable / STOP`.

No pooled effect-size axis and no severity ranking.

**Take-home label:** `plausible proxy != validated state`.

## Extended Data

- ED1: exact interaction-map theorem and evidence taxonomy.
- ED2: full fragmentation-gradient paired summaries.
- ED3: complete aligned/anti-aligned matched-summary certificate.
- ED4: 500/1000/1500 propagation precision grid.
- ED5: all six warning endpoints and full metrics.
- ED6: exact precedence-discrimination proof schematic.
- ED7: natural gate registry with endpoint and holdout unit.
- ED8: six-system downstream-inference boundary table.
- ED9: Campanula representation-collapse diagnostic.
- ED10: provenance map pinning all source commits and locked artifacts.

## Main-text compression rule

If the Article exceeds the Nature Ecology & Evolution 3,500-word main-text ceiling, cut technical explanation from component Results first and move it to Methods/Extended Data. Do not cut the four non-implications or the claim-boundary paragraph that prevents causal over-reading.
