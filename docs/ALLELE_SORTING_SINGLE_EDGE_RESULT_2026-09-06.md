# Focused single-edge proof: q-dependent allele sorting contributes causally to late functional fate

Status: **resolved for the declared finite q-only closure**.

## Prospective design

The operator theorem and focused endpoint protocol were committed before outcomes. The protocol fixed exactly two conditions:

1. the q-only life cycle with local q-dependent high-allele selection;
2. the same life cycle with only the local `q -> allele selection` edge deleted by replacing patch-specific q with the within-condition spatial mean q at that selection step.

All other state values, trait selection, recruitment, inheritance, demography, density feedback, migration, mutation, forcing, horizons and the all-patch realised-high-trait loss endpoint were held fixed. Twelve fresh master seeds x 500 replicates produced **6,000 paired AA/RR keys per condition**. No sequential stopping, seed extension, endpoint search or alternative intervention was permitted after outcomes.

Locked workflow provenance:

- run: `34016797940`
- job: `101441868527`
- artifact: `9984306657`
- digest: `sha256:61a07cc6a8680a59185537b03abdca85d0f172a65d068ee9661dd9f2fb448c2d`
- protocol commit: `2e8d46eb820f88599479321c1e66b309f8c1f16a`
- scientific head: `c6bfada980871c6aaaf883fc00381a2cca6cbcd3`

## Exact operator theorem

For the pinned closure, the deterministic high-allele selection update is

\[
p^+=\frac{p(0.75+0.4q)}{1-p+p(0.75+0.4q)}.
\]

Hence for every interior `0<p<1`,

\[
\frac{\partial p^+}{\partial q}
=\frac{0.4p(1-p)}{[1+p\{(0.75+0.4q)-1\}]^2}>0.
\]

Equivalently,

\[
\operatorname{logit}(p^+)-\operatorname{logit}(p)=\log(0.75+0.4q).
\]

The exact sorting switch is `q*=0.625`: high alleles increase above the switch, are neutral at the switch, and decrease below it. This is the same threshold at which the declared high endpoint trait becomes potentially viable.

A spatial corollary follows. With `u_i=logit(p_i)` and `g(q)=log(0.75+0.4q)`,

\[
\operatorname{Cov}(q,u^+)-\operatorname{Cov}(q,u)=\operatorname{Cov}(q,g(q))
=\frac{1}{2n^2}\sum_{i,j}(q_i-q_j)\{g(q_i)-g(q_j)\}.
\]

Because `g` is strictly increasing, this increment is nonnegative and is strictly positive whenever q varies among patches. Thus one deterministic allele-selection step is itself an exact spatial sorting operator.

## Primary endpoint result

The predeclared primary estimand was

\[
DID_{40}=(RR-AA)_{\rm baseline}-(RR-AA)_{\rm deletion}.
\]

At generation 40:

- baseline local-allele-selection condition:
  - AA loss = **0.68033**
  - RR loss = **0.74683**
  - RR-AA = **+6.65 percentage points**
  - paired 95% CI = **[+5.07,+8.23] pp**
- delete-local-allele-selection condition:
  - AA loss = **0.72300**
  - RR loss = **0.72067**
  - RR-AA = **-0.23 percentage points**
  - paired 95% CI = **[-1.80,+1.34] pp**

Therefore

\[
\boxed{DID_{40}=+6.883\ \mathrm{pp}}
\]

with paired 95% CI

\[
\boxed{[+5.800,+7.967]\ \mathrm{pp}}.
\]

The full interval is positive, so the predeclared rule resolves a **positive endpoint-level sorting contribution** for the single `q -> allele selection` edge.

The secondary generation-20 result independently has the same direction:

\[
DID_{20}=+6.783\ \mathrm{pp},
\]

95% CI `[+5.478,+8.088]` pp.

## Mediator signature

With local allele selection retained, AA relative to RR develops and maintains higher allele-frequency spatial variance and later higher focal-state retention. At generation 40:

- allele-frequency variance AA-RR = **+0.01238**, 95% CI `[+0.00938,+0.01537]`;
- mean high-allele frequency AA-RR = **+0.01823**, `[+0.01397,+0.02248]`;
- maximum high-trait mass AA-RR = **+0.06440**, `[+0.04871,+0.08008]`;
- realised refuge count AA-RR = **+0.08033 patch**, `[+0.06263,+0.09804]`.

When only local allele selection is deleted, all four generation-40 AA-RR contrasts collapse to intervals containing zero:

- allele-frequency variance: `-0.00081`, CI `[-0.00377,+0.00215]`;
- mean allele frequency: `-0.00046`, `[-0.00464,+0.00371]`;
- maximum high-trait mass: `-0.00439`, `[-0.01989,+0.01110]`;
- refuge count: `+0.00133`, `[-0.01596,+0.01863]`.

This mediator collapse is consistent with the exact operator theorem and the endpoint DID: local q-dependent allele selection creates spatial eco-genetic sorting that propagates into late high-trait persistence under this closure.

## Updated causal interpretation

The earlier joint local-selection result is now sharpened. Within the q-only closure:

1. **q-dependent allele selection is an exact spatial sorting operator**;
2. **that single edge contributes causally to the late AA-RR functional-loss contrast**;
3. **allele-linked recruitment acts in the opposite direction as a countervailing buffer**;
4. **density-to-q feedback gates entry into the early system-wide collapse regime**.

Thus the mechanistic core is no longer merely `local ecological selection as a joint block`. It is specifically a competition between **q-dependent allele sorting** and **recruitment / interaction-mediated buffering**, operating under a density-feedback failure gate.

## Claim ceiling

This is a theorem plus prospectively locked causal intervention result for the declared finite q-only closure. It does not establish a universal natural allele-sorting law, does not show that allele sorting is the only possible sorting mechanism in ecological systems, and does not convert the natural examples in the flagship Discussion into validation datasets.
