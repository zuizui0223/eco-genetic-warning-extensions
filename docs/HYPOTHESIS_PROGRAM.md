# Condition-first hypothesis program

## Central hypothesis

> **Spatial fragmentation becomes functional fragmentation only under eco-genetic conditions that weaken or destabilise an interaction-supported functional state. Genetic warning is interpretable only after the loss process itself is reproducible.**

The repository follows one rule: if a proposition is not general, recover its **condition or boundary** rather than widening the search until a desired warning result appears.

```text
C0  FUNCTION EXISTS
    interaction-dependent high-function state
        ↓
C1  FUNCTION IS VULNERABLE
    fragmentation / deterioration can disrupt it
        ↓
C2  LOSS REGIME IS CONDITIONED
    recurrent turnover + genetic connectivity + interaction support / partner loss
        ↓
C3  WARNING IS CONDITIONAL
    only inside an independently fixed evaluable loss regime
        ↓
C4  PORTABILITY IS BOUNDED
    warning need not transfer across eco-genetic regimes
```

## C0–C1 — inherited mechanism

The pinned parent repository (`eco-genetic-criticality`, scientific commit `dd8ee379d0d3518194c767d16402042525bc00dc`) supplies the bounded mechanism:

- the declared positive-feedback interaction map can support a high-function state;
- high interaction can support a high-investment trait mode under the declared trait-margin condition;
- projecting the same prepared state into equal isolated fragments lowers interaction, local effective size and realised high-trait mass;
- population persistence, realised function, allele state and genetic diversity remain distinct.

**C0: recovered for the declared model closure.**  
**C1: recovered as bounded parent theory plus finite Type S fragmentation evidence.**

## C2 — conditions generating reproducible functional loss

All C2 campaigns are warning-blind: genetic-diversity decline, warning time, lead/lag ordering and lead time are unavailable during condition selection.

### C2a — recurrent turnover changes source feasibility

Across the original 15 recurrent-transition coordinates, **2,269/3,375** source attempts supported preparation/projection. Coordinate support ranged from **44.89% to 86.67%**.

**Status: supported, finite Type S.**

### C2b — recurrent turnover changes loss regime

Among 648 complete common-grid candidates:

- 322 rapid-loss;
- 242 persistence;
- 84 seed-heterogeneous;
- 0 strict R4 candidates.

The historical 15/15 `no_domain_selected` result remains immutable for that coarse candidate family. Prospective warning-blind refinement later recovered R4 twice at `kappa_mu=0.35, p_star=0.35`; immediate neighbouring `p_star` values remained R3-highrep.

**Conclusion:** R4 exists, but is narrower than pooled loss probability alone implies. Reproducibility across independent stochastic blocks is an additional condition.

**Status: supported, finite Type S.**

### C2c — effective genetic connectivity can change reproducibility

At the independently reproduced R4 anchor, allele-frequency mixing gave:

| migration rate | pooled loss | regime |
|---:|---:|---|
| 0.000 | 0.571 | R4-highrep |
| 0.025 | 0.549 | R4-highrep |
| 0.050 | 0.593 | R4-highrep |
| 0.100 | 0.626 | R3-highrep |
| 0.200 | 0.604 | R3-highrep |

Paired trajectories switched loss status in both directions. Connectivity therefore altered **which stochastic realisations lost function** and whether loss remained reproducible enough for R4; it was not a universal rescue/collapse axis.

`migration_rate` is allele-frequency mixing only, not demographic, pollen, seed, pollinator or recolonisation movement.

**Status: supported at one R4 anchor, finite Type S.**

### C2d — aggregate interaction support does not break R4 across the predeclared tested range

Phase F used only the original Protocol 002 interaction-feedback values `kappa = 3.0, 4.5, 6.0`, at fixed `A_ref=1.0`, `kappa_mu=0.35`, `p_star=0.35`, no allele-frequency migration, horizon 120 and normalized barrier increase 0.30. Each kappa received fresh independent source reconstruction across five seed blocks × 20 attempts. Warning/diversity fields were unavailable.

| interaction kappa | source / baseline eligible | pooled loss among eligible | regime |
|---:|---:|---:|---|
| 3.0 | 77/100 | 0.468 | R4-highrep |
| 4.5 | 94/100 | 0.521 | R4-highrep |
| 6.0 | 87/100 | 0.552 | R4-highrep |

Every seed-block loss rate at every tested kappa remained inside `[0.30,0.70]`. Thus **the recovered R4 event regime was robust to this predeclared three-level aggregate interaction-support axis**. Source/baseline eligibility changed descriptively (0.77, 0.94, 0.87), so source feasibility and post-source event-regime classification need not respond identically.

This does **not** show that interaction support is ecologically irrelevant, nor that all kappa values preserve R4. It shows that `3.0–6.0` did not provide the missing R4 boundary at this anchor. Per the stop rule, no finer or wider kappa search is opened merely to manufacture one.

**Interpretation boundary:** interaction `kappa` is aggregate positive-feedback strength. It is not partner richness, connectance, pollinator diversity or network dimensionality. Phase F therefore tests effective interaction support, not interaction-network simplification itself.

**Status: recovered negative/bounded condition result, finite Type S. Campaign closed.**

Machine-readable result: `artifacts/interaction_support/phase_f_summary.json`; workflow run `32441549848`, artifact `9432854668`.

### C2e — matched one-partner loss can break event-regime reproducibility without raising pooled risk

Phase G introduced a prospective reduced-form partner-contribution closure at the fresh R4 anchor. Four partner contributions summed to one. The intact control retained all four partners. Three loss architectures each removed exactly one of four partners, balanced across replicates, and were constructed to have the same mean retained interaction support (`0.75`) and the same richness change (`4 → 3`), while contribution concentration ranged from even to dominant-partner structure.

The fresh intact control reproduced R4 (`49/90` losses; pooled `0.544`; seed-rate range `0.129`). All three one-partner-loss architectures became R3-highrep:

| partner condition | pooled loss | seed-rate range | regime |
|---|---:|---:|---|
| intact control | 0.544 | 0.129 | R4-highrep |
| even redundant loss | 0.567 | 0.261 | R3-highrep |
| graded-contribution loss | 0.556 | 0.353 | R3-highrep |
| dominant-partner loss | 0.578 | 0.235 | R3-highrep |

Paired loss status switched in both directions relative to intact (38/90, 39/90 and 31/90 trajectories, respectively). A post-hoc paired incidence audit found no evidence that pooled binary loss incidence differed across the four conditions (Cochran's Q = 0.385, df = 3, `p=0.943`). The finite result is therefore a **reproducibility/estimability effect, not a directional increase in mean loss risk**.

The architecture contrast itself was negative at the regime level: even, graded and dominant loss architectures were all R3. Thus this campaign supports sensitivity to the tested partner-loss perturbation but does not show that contribution concentration alone determines the loss regime.

**Interpretation boundary:** Phase G is a reduced-form partner-contribution / functional-redundancy closure. It does not model connectance, adaptive rewiring, partner population dynamics, pollen/seed/pollinator movement or a real ecological network.

**Status: recovered finite partner-loss boundary plus negative architecture contrast. Campaign closed.**

Machine-readable result: `artifacts/partner_redundancy/phase_g_summary.json`; workflow run `32450362310`, artifact `9435520830`.

## C3 — genetic warning only after C2

The inherited symmetric benchmark provides proof of possibility: in one independently calibrated domain, baseline-relative `H_alpha`/`H_gamma` decline preceded 35 observed functional losses at all six tested relative endpoints. Predeclared absolute thresholds produced both leads and lags.

A matched recurrent-transition-direction effect remains unresolved because the refined `p_star` frontier did not recover the adjacent matched R4 interval required by the opening rule. No direction-only warning campaign is opened by further tuning.

**C3: conditional possibility recovered; direction-only causal effect unresolved by design.**

## C4 — warning portability

Historical Protocol 003 recovered two warning-evaluable domains by separate warning-blind calibration. They differ in recurrent-transition, ecological and deterioration parameters. Their fresh-seed warning differences are therefore **bounded portability evidence across calibrated eco-genetic domains**, not an isolated mutation-direction effect.

**C4: bounded non-portability result; causal attribution intentionally limited.**

## Exact theory boundaries

`RECURRENT_TRANSITION_DIVERSITY_THEORY.md` remains authoritative for Type T identities:

- direction has no universal signed effect on heterozygosity;
- transition strength contracts among-patch allele-frequency differences independently of direction under fixed weights;
- stronger local high-state support can coincide with lower heterozygosity;
- allele-frequency homogenisation is not a theorem of functional rescue.

## Urban and island application

Urban and island landscapes are contrasting empirical routes through the same condition space, **not ecological equivalents and not yet demonstrated to converge on one regime**. A field translation should measure separately:

- spatial fragmentation / local habitat support;
- realised interaction support and partner composition;
- functional redundancy and rewiring;
- effective genetic connectivity, separated by biological movement process;
- reproductive assurance / alternative functional routes;
- realised functional performance or loss;
- genetic state through time.

The common next question is:

> **Do different fragmentation mechanisms converge on the same operational functional-fragmentation regime once state feasibility, realised function and loss reproducibility are measured separately?**

Phase G now provides a first reduced-form test of partner loss, but actual connectance, adaptive rewiring, coextinction and biological movement remain empirical or future explicit-network axes. They must not be silently substituted by interaction `kappa` or allele-frequency `migration_rate`.

## Recovery ledger

| condition | status | conclusion |
|---|---|---|
| C0 functional-state existence | recovered | high-function state is possible under the declared interaction closure |
| C1 fragmentation vulnerability | recovered | fragmentation can lower interaction, local effective size and realised function |
| C2a recurrent-turnover source feasibility | supported | source feasibility changes across recurrent-transition coordinates |
| C2b recurrent-turnover loss regime | supported | loss regime changes; R4 exists narrowly despite the immutable coarse-grid no-domain result |
| C2c genetic connectivity | supported at one anchor | connectivity can move R4→R3 without a universal rescue/collapse sign |
| C2d aggregate interaction support | bounded negative result | all predeclared kappa 3.0/4.5/6.0 remain R4; source eligibility varies |
| C2e matched partner loss | supported at one anchor | one-partner loss moved R4→R3 in all three predeclared architectures without a detectable pooled-risk shift; architecture concentration itself did not separate regimes |
| C3 conditional genetic warning | bounded support | relative warning can lead loss in one calibrated benchmark; absolute thresholds are not portable |
| C3 matched direction-only effect | unresolved | no prospectively matched adjacent R4 interval was recovered |
| C4 portability | bounded | warning behaviour differs across non-matched calibrated domains |

## Global stop rules

Do not:

1. inspect warning/diversity fields while selecting C2 event regimes;
2. refine `p_star`, migration, interaction kappa, Phase-G partner weights or the R4 gate merely to obtain a desired result;
3. overwrite the historical 15/15 Protocol 002 no-domain result;
4. call allele-frequency migration demographic/pollinator/seed rescue;
5. call interaction `kappa` network simplification;
6. call Phase G a full network, connectance or rewiring experiment;
7. open a direction-only warning test without prospectively matched evaluable conditions;
8. treat a failed universal hypothesis as unfinished work when its boundary has already been recovered.
