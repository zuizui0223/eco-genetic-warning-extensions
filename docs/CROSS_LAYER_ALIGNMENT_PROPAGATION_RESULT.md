# Cross-layer alignment propagation audit — locked result

## Decision

The preregistered post-review propagation replay passed its historical reproduction gate and returned the joint classification:

- **interaction representation memory:** `attenuating_representation_memory`;
- **cumulative loss horizon family:** `no_detected_horizon_family_loss_incidence_separation`.

The main result is therefore not a directional long-horizon risk effect. It is a target- and horizon-dependent representation result: the initial cross-layer alignment contrast strongly changes near-term interaction dynamics, including a transient amplification at generation 2, then attenuates below half of its generation-1 median by generation 10, while paired functional-loss status remains highly trajectory-sensitive after losses begin even though the marginal loss-incidence difference never clears the preregistered simultaneous horizon-family band.

## Prospective provenance

The propagation question and all primary analysis choices were fixed before intermediate-generation Phase-V outcomes were opened.

- preregistration commit: `8c4745e411fe2107b490dc4f59b2acc966928196`;
- prospective clerical Amendment 001: `9f7e1d3bab2d3ca88509208c0f46e4a2021e186c`;
- historical Phase-V scientific implementation: `260a03220bf09d5f4a4d8cb55ec21062bf120c55`;
- pinned EGC scientific closure: `dd8ee379d0d3518194c767d16402042525bc00dc`;
- result-confirming branch head: `dd5b93ae46ff437e335f6b19b410999406e5f692`;
- successful propagation workflow: `33839614856`;
- uploaded artifact: `9924462968`;
- artifact digest: `sha256:92876a7275b403efe78d232918b3f7554446ed37d46f91d6028bc7109f1dfb44`;
- fixed pair count: 500 aligned/anti-aligned pairs;
- fixed horizon grid: `1, 2, 5, 10, 20, 40, 60` generations;
- bootstrap: 10,000 pair-cluster resamples, RNG seed `20260904`.

The audit is a replay of the historical Phase-V pairs with additional snapshot readout. It is not an independent replication.

## Historical reproduction gate

Every preregistered integrity check passed before the intermediate horizon curves were interpreted:

- baseline coarse marginal signatures reproduced;
- the exact generation-1 certificate reproduced to the declared numerical tolerance;
- all 500 pair keys were present exactly once;
- generation-60 aligned loss count reproduced as **339/500 (`0.678`)**;
- generation-60 anti-aligned loss count reproduced as **361/500 (`0.722`)**;
- the paired terminal table reproduced exactly: **92 aligned-only loss, 114 anti-aligned-only loss, 247 both loss, 47 both no loss**.

The locked generation-1 maximum patchwise interaction-transition difference remained **`0.25433292878878405`**.

## Primary interaction-state propagation

The primary coordinate was the median across the 500 pairs of the maximum absolute patchwise aligned-versus-anti-aligned interaction difference, `D_I_max`.

| horizon | median `D_I_max` | pair-bootstrap 95% interval |
|---:|---:|---:|
| 1 | 0.254333 | [0.254333, 0.254333] |
| 2 | **0.345529** | [0.343803, 0.347266] |
| 5 | 0.161762 | [0.157128, 0.166354] |
| 10 | **0.090313** | [0.084612, 0.095821] |
| 20 | 0.076060 | [0.053551, 0.098580] |
| 40 | 0.086215 | [0.001762, 0.092078] |
| 60 | 0.069601 | [0.000000, 0.073045] |

The preregistered half-retention level was half the generation-1 median:

`0.5 × 0.25433292878878405 = 0.12716646439439203`.

The interaction distance first fell below this level at **generation 10** and remained below it at every later preregistered horizon. The locked classification is therefore **`attenuating_representation_memory` with half-retention horizon 10**.

The curve is not monotone from the initial state. The interaction difference first **amplified** from `0.2543` at generation 1 to `0.3455` at generation 2, then attenuated. This is why no exponential-decay model is fitted or implied.

The required secondary interaction mean-absolute-distance curve showed the same qualitative early amplification and later attenuation:

`0.1497 -> 0.2300 -> 0.0885 -> 0.0388 -> 0.0221 -> 0.0216 -> 0.0174`

at generations `1, 2, 5, 10, 20, 40, 60`.

## Cumulative functional-loss horizon family

The preregistered seven-horizon paired risk-difference family used one simultaneous non-studentized 95% band. Its common half-width was **0.066**. The band included zero at every fixed horizon.

Decision: **`no_detected_horizon_family_loss_incidence_separation`**.

| horizon | aligned loss | anti-aligned loss | aligned−anti risk difference | simultaneous 95% band | discordant pair fraction |
|---:|---:|---:|---:|---:|---:|
| 1 | 0/500 | 0/500 | 0.000 | [-0.066, 0.066] | 0.000 |
| 2 | 0/500 | 0/500 | 0.000 | [-0.066, 0.066] | 0.000 |
| 5 | 0/500 | 0/500 | 0.000 | [-0.066, 0.066] | 0.000 |
| 10 | 8/500 | 10/500 | -0.004 | [-0.070, 0.062] | 0.036 |
| 20 | 169/500 | 196/500 | -0.054 | [-0.120, 0.012] | **0.450** |
| 40 | 334/500 | 356/500 | -0.044 | [-0.110, 0.022] | 0.424 |
| 60 | 339/500 | 361/500 | -0.044 | [-0.110, 0.022] | 0.412 |

The descriptive exact paired McNemar p values were `0.8145`, `0.0828`, `0.1490`, and `0.1432` at generations 10, 20, 40, and 60 respectively. They are retained as descriptive diagnostics only; no intermediate horizon is promoted by an unadjusted p value.

## Trajectory-identity sensitivity without a signed marginal-risk result

The marginal incidence result and the paired trajectory result are different scientific objects.

Once losses became common, aligned and anti-aligned members of the same historical common-seed pair frequently occupied different cumulative-loss states:

- generation 20: **225/500 pairs discordant (`45.0%`)** — 99 aligned-only, 126 anti-aligned-only;
- generation 40: **212/500 discordant (`42.4%`)** — 95 aligned-only, 117 anti-aligned-only;
- generation 60: **206/500 discordant (`41.2%`)** — 92 aligned-only, 114 anti-aligned-only.

This does **not** establish a signed population-level alignment-risk effect. It establishes a narrower paired simulator result: under the identical Phase-V seed map and forcing, changing only the initial cross-layer alignment is associated with substantial sensitivity of which paired trajectories have crossed the realised-loss endpoint by a given horizon, even when the aligned-versus-anti-aligned marginal risk difference is not detected by the horizon-family criterion.

Because stochastic states can consume subsequent random draws differently after their dynamics separate, the discordance is described as **paired trajectory-status sensitivity**, not as a deterministic counterfactual claim about individual biological populations.

## Secondary state coordinates

The propagation profiles were coordinate-specific rather than one-dimensional.

Median mean-absolute patch differences at generations `1,2,5,10,20,40,60` were:

- census population: `3.25, 4.00, 3.25, 2.00, 1.25, 1.00, 1.00`;
- local effective size: `1.95, 2.40, 1.95, 1.20, 0.75, 0.60, 0.60`;
- high-allele frequency: `0.4056, 0.4304, 0.4491, 0.3874, 0.2500, 0.2500, 0.2500`;
- realised high-trait mass: `0.4003, 0.4166, 0.4078, 0.3048, 0.21875, 0.2500, 0.2500`.

Thus the generation-10 interaction half-retention result must not be generalized into a claim that the entire joint state loses memory on a ten-generation timescale. Different coordinates retain different patchwise contrasts.

For `F_ST`, the median absolute paired difference increased through generation 20 among pairs where `F_ST` was finite, but the finite-pair denominator then collapsed from 500/500 at generations 1–5 and 497/500 at generation 10 to **277/500 at generation 20, 55/500 at generation 40, and 47/500 at generation 60**. The late zero median therefore cannot be interpreted as general genetic convergence.

## Scientific interpretation

The propagation audit separates three questions that the previous generation-1 versus generation-60 comparison could not resolve:

1. **Transition representation:** coarse marginal equality is already insufficient at the next interaction transition, and the alignment-induced interaction difference transiently amplifies before attenuating.
2. **Trajectory identity:** once losses occur, the alignment contrast remains associated with substantial paired cumulative-loss-status discordance through generation 60.
3. **Marginal signed risk:** despite that trajectory sensitivity, no aligned-versus-anti-aligned cumulative-loss risk difference is detected anywhere in the preregistered horizon family.

The strongest bounded synthesis is therefore:

> **The predictive relevance of a state representation is relative to both the target and forecast horizon. Cross-layer alignment can strongly alter near-term transitions and the identity of paired trajectories that cross a functional-loss endpoint without yielding a detected portable signed shift in marginal loss incidence.**

This is stronger than the previous endpoint pair `generation 1 differs / generation 60 risk not detected`, because it identifies the intervening propagation structure prospectively rather than inferring it from two endpoints.

## Relation to warning validity

The result does **not** establish that the frozen genetic warning rules failed because cross-layer alignment was omitted.

The warning-validity failure remains a separate denominator/discrimination result: the six frozen diversity thresholds fired in both event and non-event trajectories. The propagation audit neither reruns nor rescues those thresholds.

A higher-level manuscript may now discuss a common principle — that a statistic or representation can be informative for one inferential target and inadequate for another — but must keep the mechanisms distinct:

- event-conditioned temporal precedence is not predictive discrimination;
- one-step transition relevance is not the same as signed long-horizon marginal risk;
- paired trajectory identity is not the same estimand as marginal incidence.

No arrow `warning failure -> missing alignment` is supported.

## Publication consequence

This result materially strengthens the **state-validity** manuscript. It supplies a positive propagation result and a bounded timescale statement rather than only a one-step counterexample plus a terminal null.

It also makes a broader target-/horizon-relative predictability framing scientifically eligible for consideration. It does **not**, by itself, require merging the warning-validity and state-validity manuscripts. The default safe route remains separate claim ownership unless a combined manuscript is deliberately written around the higher-level distinction among inferential targets rather than around an unsupported claim that joint-state representation repairs warning failure.

## Claim ceiling and stop rule

Permitted:

- interaction representation memory transiently amplifies and then attenuates below the preregistered half-retention level by generation 10 in the fixed Phase-V closure;
- no signed cumulative-loss incidence separation is detected across the seven-horizon simultaneous family;
- paired cumulative-loss status remains highly discordant after loss onset;
- state-coordinate propagation is heterogeneous;
- representation adequacy is endpoint- and horizon-relative in this declared finite closure.

Not permitted:

- exponential decay or a continuous half-life estimate;
- a universal ten-generation ecological timescale;
- equivalence of aligned and anti-aligned long-horizon risk;
- a causal explanation of the warning-validity failure by missing alignment;
- a claim that adding alignment validates or rescues the frozen warning thresholds;
- an independent replication claim for this historical-pair replay;
- reopening seeds, horizons, state values, warning endpoints, alignment permutations, or model parameters to obtain a preferred result.
