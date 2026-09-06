# Exact direct eco-genetic feedback recoupling theorem

Status: **operator-level theorem plus derived paired contrast from an already prospectively locked intervention experiment**. No new simulation is opened here.

## 1. Declared support operator

In the full-feedback closure, local interaction support is

\[
S=0.6q+0.3T+0.1G,
\]

where `q` is current interaction state, `T` is realised high-trait mass and `G` is high-allele frequency.

Define the normalized eco-genetic bundle

\[
B=\frac{0.3T+0.1G}{0.4}=0.75T+0.25G.
\]

Then

\[
\boxed{S=0.6q+0.4B}.
\]

Thus the direct eco-genetic feedback stage is a convex recoupling operator between ecological interaction state and the trait/genetic bundle.

## 2. Exact support-stage mismatch contraction

Relative to the bundle,

\[
S-B=0.6(q-B).
\]

Therefore

\[
\boxed{|S-B|=0.6|q-B|}.
\]

The support stage contracts interaction–bundle mismatch by exactly **40%** in absolute distance. More generally, with ecological weight `alpha` and eco-genetic weight `1-alpha`, the contraction factor is exactly `alpha`.

This is not a claim that full feedback always increases q. Instead,

\[
S-q=0.4(B-q),
\]

so the support signal moves upward when the bundle exceeds q and downward when the bundle is below q.

## 3. Exact next-interaction log-odds shift relative to q-only

For local area ratio `a=A/A_ref`, density `d`, feedback strength `kappa` and barrier `theta`, the full-feedback and q-only transitions are

\[
q^+_{F}=\sigma\{\kappa(adS-\theta)\},
\]

\[
q^+_{Q}=\sigma\{\kappa(adq-\theta)\}.
\]

Because `logit(sigmoid(x))=x`,

\[
\boxed{
\operatorname{logit}(q^+_F)-\operatorname{logit}(q^+_Q)
=0.4\kappa ad(B-q)
}.
\]

In the locked mechanism experiment, `kappa=4.5` and `a=1`, giving

\[
\boxed{
\operatorname{logit}(q^+_F)-\operatorname{logit}(q^+_Q)
=1.8d(B-q)
}.
\]

Hence the sign of the direct-feedback change is exact:

- `B>q` -> full feedback raises next q relative to q-only;
- `B=q` -> no direct-feedback change;
- `B<q` -> full feedback lowers next q relative to q-only.

The logistic derivative is at most `1/4`, so the transition-scale displacement obeys

\[
|q^+_F-q^+_Q|\le 0.1\kappa ad|B-q|.
\]

Under the locked `kappa=4.5`, `a=1` setting,

\[
|q^+_F-q^+_Q|\le0.45d|B-q|.
\]

## 4. Why this is recoupling rather than a universal positive feedback

The theorem identifies the direction in which the eco-genetic bundle changes the interaction transition. It is a **recoupling** operator because it reduces the support-stage discrepancy between q and the bundle and shifts next-q log odds according to the sign of that discrepancy.

For the original reversed configuration, the high eco-genetic bundle is placed in weak-interaction patches. Direct feedback can therefore raise the weakest local interaction state even while lowering support elsewhere. This is a redistribution/recoupling mechanism, not a statement that mean support must increase.

## 5. Locked paired intervention evidence

The relational mechanism experiment was prospectively locked before outcomes (workflow `34012983845`, job `101431872354`, artifact `9983093178`, digest `sha256:843a6bdc4a4d4e9de10ce6346cca27a1a863b1780573f000c0f1ab164a81c7ac`). Its protocol used the same trajectory seed across all six conditions within each master-seed/replicate key.

The full-feedback and q-only conditions differ in the direct support weights: `(0.6,0.3,0.1)` versus `(1,0,0)`. We therefore derive paired risk contrasts from the already locked trajectory artifact. These contrasts are **derived from a prospectively locked intervention family but were not a separately predeclared primary estimand**.

### Generation 20

Direct-feedback benefit, defined as `q-only loss - full-feedback loss`:

- AA: **+0.60 pp**, paired 95% CI **[-2.71,+3.91]**;
- RR: **+8.53 pp**, paired 95% CI **[+5.21,+11.85]**.

The paired difference in buffering benefit, `RR benefit - AA benefit`, is

\[
\boxed{+7.93\ \text{pp}}
\]

with 95% CI **[+3.29,+12.58]**.

### Generation 40

- AA benefit: **+1.47 pp**, paired 95% CI **[-1.72,+4.65]**;
- RR benefit: **+7.80 pp**, paired 95% CI **[+4.79,+10.81]**;
- RR-minus-AA buffering-benefit contrast: **+6.33 pp**, paired 95% CI **[+1.85,+10.82]**.

Thus, in this locked ensemble, direct eco-genetic feedback preferentially buffered the reversed arrangement in which the eco-genetic bundle was initially placed against the interaction gradient.

## 6. Mechanistic role alongside the other exact operators

The finite closure now separates three roles:

1. **q-dependent allele sorting**: ecological state sorts allele log odds spatially and contributes causally to late functional fate;
2. **recruitment buffering**: two-kernel recruitment contracts trait–allele mismatch by exactly 50% before selection;
3. **direct feedback recoupling**: the support stage contracts q–bundle mismatch by exactly 40%, and shifts next-q log odds by `0.4*kappa*a*d*(B-q)` relative to q-only.

Density-to-q feedback is separate: it supplies the positive q–N–q collapse gate rather than a directional recoupling operator.

## Claim ceiling

All identities are exact only for the declared finite closure and locked weights. The paired risk contrasts are secondary derived contrasts from the already locked intervention artifact. They do not establish a universal natural recoupling law, and the natural examples remain ecological projections rather than validation data.
