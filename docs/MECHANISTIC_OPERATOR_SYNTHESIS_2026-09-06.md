# Mechanistic operator synthesis: why matched marginals reach different fates

Status: synthesis of already locked exact results and prospectively locked intervention evidence. Natural examples are not validation data here.

## 1. Immediate divergence: relational state changes the transition

The aligned/reversed construction holds conventional ecological and genetic marginals fixed while changing cross-layer spatial association. Mean local support remains identical, but support variance changes **49-fold** and the exact next interaction field differs by as much as **0.2543**.

This establishes the first step:

\[
\text{same marginals}\not\Rightarrow\text{same next state}.
\]

The cause is cross-layer covariance, which changes where support is concentrated without changing its mean.

## 2. Route-splitting operator: q-dependent allele sorting

For the high allele,

\[
\operatorname{logit}(p^+)-\operatorname{logit}(p)=\log(0.75+0.4q).
\]

The local switch is exactly `q*=0.625`, equal to the declared high-trait viability threshold. Across patches, one deterministic selection step strictly increases q–allele log-odds covariance whenever q varies spatially.

The focused 6,000-pair deletion resolves the endpoint consequence:

- g40 baseline `RR-AA = +6.65 pp`;
- deleting only local q-dependent allele selection gives `RR-AA = -0.23 pp`;
- preregistered DID **+6.883 pp**, 95% CI **[+5.800,+7.967]**.

This is the resolved **sorting** edge.

## 3. Trait–allele buffering operator: recruitment contracts mismatch

For resident high-trait mass `m`, high-allele frequency `p`, and locked inheritance weight `h=0.5`, two-kernel recruitment gives

\[
r=\frac{m+p}{2}.
\]

Therefore

\[
|r-p|=0.5|m-p|.
\]

Recruitment contracts trait–allele mismatch by exactly **50%** before selection.

The prospectively locked edge deletion gives the endpoint direction:

- g20 deleting recruitment enlarges `RR-AA` from +4.20 to +13.20 pp; DID **-9.00 pp** [−13.29,−4.71];
- g40 enlarges it from +4.40 to +12.73 pp; DID **-8.33 pp** [−12.53,−4.14].

This is the resolved **trait–allele buffering** edge.

## 4. Interaction–bundle recoupling operator: direct eco-genetic feedback

Define the normalized eco-genetic bundle

\[
B=0.75T+0.25G.
\]

The full support signal is

\[
S=0.6q+0.4B.
\]

Hence

\[
|S-B|=0.6|q-B|,
\]

so direct feedback contracts interaction–bundle mismatch by exactly **40% at the support stage**.

Relative to q-only,

\[
\operatorname{logit}(q_F^+)-\operatorname{logit}(q_Q^+)
=0.4\kappa a d(B-q).
\]

Under the locked `kappa=4.5`, `a=1` setting this is `1.8 d(B-q)`. Thus the feedback raises next q where the bundle exceeds q and lowers it where the bundle is below q; it is a directional **recoupling** operator rather than a universal positive-q effect.

Derived paired contrasts from the already locked six-condition intervention show preferential buffering of the reversed arrangement:

- g20: RR benefit **+8.53 pp** [5.21,11.85] versus AA +0.60 pp [−2.71,3.91]; RR-minus-AA buffering-benefit DID **+7.93 pp** [3.29,12.58];
- g40: RR benefit **+7.80 pp** [4.79,10.81] versus AA +1.47 pp [−1.72,4.65]; DID **+6.33 pp** [1.85,10.82].

These are secondary paired contrasts derived from a prospectively locked intervention family, not a separately predeclared primary estimand.

## 5. Collapse-entry operator: density feedback consumes headroom

The q-only interaction update is

\[
q^+=\sigma\{4.5(dq-\theta)\},\qquad d=\min(1,N/K).
\]

Below carrying capacity,

\[
\frac{\partial q^+}{\partial N}>0,
\]

while demographic growth increases with q. Therefore the smooth life cycle contains the positive path

\[
q\downarrow\to N\downarrow\to d\downarrow\to q\downarrow.
\]

To retain `q_next >= 0.625`, the exact boundary is

\[
dq\ge\theta+0.1135168053.
\]

The required `d*q` rises from **0.6160** near the beginning to **0.6635** at g20 and **0.7135** at g40, so forcing progressively consumes demographic headroom.

Deleting density from q in the already locked experiment produces large paired risk reductions:

- g20: AA **38.33 pp** [35.87,40.79], RR **42.53 pp** [40.03,45.04], leaving 0/1,500 losses in both conditions;
- g40: AA **57.47 pp** [54.65,60.28], RR **59.60 pp** [56.73,62.47].

This is the **failure/amplification gate**, not the directional sorting edge.

## 6. Final causal architecture

The finite model now supports the following mechanistic decomposition:

\[
\boxed{
\text{fate}
=
\text{sorting}
\;\text{opposed by}\;
\text{buffering / recoupling}
\;\text{inside a density-feedback collapse gate}
}
\]

More specifically:

1. cross-layer covariance creates transition-relevant spatial heterogeneity;
2. q-dependent allele selection sorts eco-genetic state toward locally favourable interaction states;
3. allele-linked recruitment contracts trait–allele mismatch;
4. direct eco-genetic feedback recouples weak interaction states toward the local trait/genetic bundle;
5. density feedback determines whether demographic erosion is amplified into widespread collapse.

The apparent `AA`, `RR`, collapse or compensation outcomes are therefore not unexplained branches. They are generated by a balance of identifiable life-cycle operators with different signs and targets.

## Claim ceiling

This is a mechanistic decomposition of the declared finite closure. It does not establish that the same algebraic weights, thresholds, generations or operators are universal in natural ecosystems. Natural examples can be used to project candidate sorting, buffering, recoupling and memory mechanisms, but not as validation of this simulator.
