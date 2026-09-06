# Exact density-feedback failure-gate theorem for the q-only closure

Status: **operator-level theorem plus locked finite intervention evidence** for the declared q-only closure. This document explains why density-to-interaction feedback can gate entry into the loss regime; it does not assert a universal natural collapse threshold.

## 1. Interaction update with density feedback

In the locked q-only pathway experiment, one patch updates interaction state by

\[
q^+=\sigma\{\kappa(dq-\theta)\},
\]

with

\[
\kappa=4.5,
\qquad
d=\min(1,N/K),
\]

where `N` is population size and `K` is local carrying capacity. For the locked four-patch state, `K=40` in every patch.

For `q>0` and `0<d<1`,

\[
\frac{\partial q^+}{\partial d}
=\kappa q\,q^+(1-q^+)>0.
\]

When `N<K`, `d=N/K`, so

\[
\boxed{
\frac{\partial q^+}{\partial N}
=\frac{\kappa q}{K}q^+(1-q^+)>0
}
\]

for every positive q. Thus reducing local population strictly lowers the next interaction state on the unsaturated-density branch. When `N>=K`, density is capped at one and this edge saturates rather than reversing.

## 2. Exact demographic headroom boundary for q*=0.625

The allele-sorting theorem and the declared high-trait viability condition share the switch

\[
q^*=0.625.
\]

To keep the next interaction state at or above a target `c`,

\[
q^+\ge c
\]

is equivalent to

\[
\kappa(dq-\theta)\ge \operatorname{logit}(c).
\]

Hence the exact required density is

\[
\boxed{
d\ge d_{\min}(q,\theta;c)
=\frac{\theta+\operatorname{logit}(c)/\kappa}{q}
}
\]

whenever q is positive.

For `c=0.625` and `kappa=4.5`,

\[
\frac{\operatorname{logit}(0.625)}{4.5}
=0.1135168053.
\]

Therefore the exact condition for the next q to remain above the shared high-trait/high-allele switch is

\[
\boxed{dq\ge\theta+0.1135168053}.
\]

The locked barrier path is

\[
\theta_g=0.50+0.15\frac{g}{60}=0.50+0.0025g.
\]

Thus the required density–interaction product rises over the experiment:

| generation | theta | required `d*q` for `q_next >= .625` |
|---:|---:|---:|
| 1 | 0.5025 | **0.6160168** |
| 20 | 0.5500 | **0.6635168** |
| 40 | 0.6000 | **0.7135168** |

For example, if current `q=0.8`, required density rises from `0.7700` at generation 1 to `0.8294` at generation 20 and `0.8919` at generation 40. If the right-hand side divided by q exceeds one, even full density cannot keep the next q above the switch.

This gives a precise meaning to **demographic headroom**: rising forcing continuously reduces the population-density margin within which the high-trait/high-allele interaction regime can be maintained.

## 3. Positive two-step q -> N -> q feedback

Before integer rounding, the declared demographic update is

\[
N^+=N\exp\left(r_0+a q^+ + b p_s-\frac{N}{K}\right),
\]

with `a=0.4` and `b=0.1`, where `p_s` is selected high-allele frequency.

Holding `p_s` fixed,

\[
\boxed{
\frac{\partial N^+}{\partial q^+}=aN^+>0
}.
\]

The implemented rounding and lower bound are nondecreasing transformations, so they can flatten this response locally but cannot reverse its sign.

At the following interaction update, when `N^+<K`,

\[
\frac{\partial q^{++}}{\partial N^+}
=\frac{\kappa q^+}{K}q^{++}(1-q^{++})>0.
\]

The direct smooth two-step loop gain is therefore

\[
\boxed{
G=\frac{\kappa a}{K}
q^+N^+q^{++}(1-q^{++})>0
}
\]

on the unsaturated-density branch.

Hence the model contains a genuine positive feedback path

\[
q\downarrow\Rightarrow N\downarrow\Rightarrow d\downarrow\Rightarrow q\downarrow.
\]

The q-dependent allele-selection edge adds another nonnegative contribution to the q-to-demography derivative in the baseline closure, so the direct demographic loop above is a sufficient positive path rather than the only one.

## 4. Prospectively locked edge-deletion evidence

The pathway edge-decomposition protocol was fixed before outcomes (workflow `34014537015`, artifact `9983623440`). The density-edge intervention removed only `N -> q` by setting the density multiplier in the q update to one, while demographic dynamics, q-dependent selection, trait recruitment, forcing and the functional-loss endpoint remained active.

### Generation 20

Baseline q-only cumulative loss:

- AA: **38.33%**;
- RR: **42.53%**.

With `N -> q` deleted:

- AA: **0/1,500 losses**;
- RR: **0/1,500 losses**.

Using the locked paired keys, deletion reduced cumulative risk by:

- AA: **38.33 pp**, paired 95% CI **[35.87,40.79]**;
- RR: **42.53 pp**, paired 95% CI **[40.03,45.04]**.

Thus this edge was necessary for every generation-20 functional-loss event observed in that locked ensemble.

### Generation 40

Baseline cumulative loss:

- AA: **68.73%**;
- RR: **73.13%**.

With `N -> q` deleted:

- AA: **11.27%**;
- RR: **13.53%**.

Paired risk reductions were:

- AA: **57.47 pp**, paired 95% CI **[54.65,60.28]**;
- RR: **59.60 pp**, paired 95% CI **[56.73,62.47]**.

The edge therefore remains a large system-level amplifier at generation 40, although it is not the unique cause of all later losses.

## 5. Why this is a failure gate rather than the sorting edge

Deleting `N -> q` collapses the total event rate, but the generation-40 attenuation of the **RR-minus-AA differential** remained unresolved in the original preregistered matching-specific DID. It is therefore incorrect to call density feedback the source of the sorting advantage.

The evidence instead separates roles:

1. **q-dependent allele sorting** determines a directional eco-genetic sorting advantage;
2. **allele-linked recruitment** contracts trait–allele mismatch and buffers that advantage;
3. **density-to-q feedback** controls whether declining demography feeds back strongly enough to push the system into widespread functional loss.

The exact headroom boundary shows why the third process becomes more consequential as forcing increases: the required `d*q` product for staying above the shared `q*=0.625` switch rises from `0.6160` near the beginning to `0.7135` by generation 40.

## Claim ceiling

The derivative, headroom boundary and positive loop gain are exact for the declared q-only closure (with the loop derivative referring to its smooth pre-rounding demographic backbone). The paired risk reductions are derived from the already locked prospective trajectory artifact. None of these quantities is asserted as a universal natural density threshold, natural generation timescale or universal Allee effect.
