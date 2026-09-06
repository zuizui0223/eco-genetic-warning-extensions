# Moving branching-headroom theorem for the declared finite closure

Status: **exact operator-level theorem**. This theorem unifies the already resolved sorting, recoupling and density-gate mechanisms into one moving local boundary. It does not add a new endpoint simulation and does not claim a universal natural threshold.

## 1. Definition

Under the locked full-feedback weights,

\[
S=0.6q+0.3T+0.1G=0.6q+0.4B,
\qquad B=0.75T+0.25G.
\]

The interaction update is

\[
q^+=\sigma\{\kappa(dS-\theta)\},
\qquad \kappa=4.5,
\]

with density `d=min(1,N/K)`. The high-trait viability threshold and the high-allele selection switch are both

\[
q^*=0.625.
\]

Let

\[
c^*=\frac{\operatorname{logit}(q^*)}{\kappa}
=0.1135168052813313.
\]

Define **branching headroom**

\[
\boxed{
H=dS-\theta-c^*
=d(0.6q+0.4B)-\theta-0.1135168052813313.
}
\]

## 2. Exact route-switch equivalence

Because sigmoid is strictly increasing,

\[
q^+\ge q^*
\iff
\kappa(dS-\theta)\ge \operatorname{logit}(q^*)
\iff
H\ge0.
\]

Thus `H=0` is the exact moving surface on which the next interaction state equals the shared switch `q*=0.625`.

The local high-allele selection operator is

\[
\operatorname{logit}(p^+)-\operatorname{logit}(p)
=\log(0.75+0.4q^+).
\]

Since `0.75+0.4(0.625)=1`,

\[
\boxed{
H>0
\iff q^+>0.625
\iff \Delta\operatorname{logit}(p)>0,
}
\]

with all inequalities reversed when `H<0` and equality throughout when `H=0`.

Therefore the sign of one exact local quantity simultaneously determines:

1. whether the next interaction state lies above or below the declared high-trait viability switch; and
2. whether deterministic high-allele selection increases or decreases high-allele log odds before drift.

This is the closest model-level analogue of a route flag: it is not an arbitrary classifier but an algebraic consequence of the declared life cycle.

## 3. How the resolved operators move headroom

For interior density and positive support,

\[
\frac{\partial H}{\partial B}=0.4d>0,
\qquad
\frac{\partial H}{\partial q}=0.6d>0,
\qquad
\frac{\partial H}{\partial d}=S>0,
\qquad
\frac{\partial H}{\partial\theta}=-1.
\]

Hence stronger local interaction and a stronger eco-genetic bundle raise headroom; demographic loss lowers headroom through density; and rising forcing lowers headroom one-for-one.

Relative to q-only support, direct eco-genetic recoupling changes headroom by

\[
\boxed{H_F-H_Q=0.4d(B-q).}
\]

Thus recoupling moves a patch toward the positive-headroom side exactly when `B>q`, and toward the negative side when `B<q`.

A density decrease from `d_1` to `d_2<d_1` changes headroom by

\[
H(d_2)-H(d_1)=-(d_1-d_2)S<0,
\]

which is the local geometric form of the resolved density failure gate.

Allele-linked recruitment acts one stage upstream by contracting trait–allele mismatch. With locked inheritance weight `h=0.5`, recruit high-trait mass is `r=(m+p)/2`.

## 4. Exact branch-amplification corollary

The selected high-allele frequency can be written

\[
p_s=\frac{p(0.75+0.4q^+)}{1-p+p(0.75+0.4q^+)}.
\]

Subtracting the pre-selection frequency gives

\[
\boxed{
p_s-p=
\frac{0.4p(1-p)(q^+-0.625)}
{1+0.4p(q^+-0.625)}.
}
\]

For every interior `0<p<1`, the denominator is positive. Hence

\[
\operatorname{sign}(p_s-p)
=\operatorname{sign}(q^+-0.625)
=\operatorname{sign}(H).
\]

The smooth demographic exponent contains the terms `0.4 q^+ + 0.1 p_s`. Relative to the route-surface reference `0.4 q^* + 0.1 p`, define

\[
\Delta r_{branch}=0.4(q^+-q^*)+0.1(p_s-p).
\]

Both summands have the sign of `H`, so

\[
\boxed{
\operatorname{sign}(\Delta r_{branch})=\operatorname{sign}(H)
}
\]

for nonzero headroom. Thus crossing the route surface does not only change ecological viability and allele-selection direction; it shifts the ecological and genetic contributions to smooth demographic growth in the **same direction**. Integer rounding can flatten a small demographic response locally but cannot reverse the sign of the underlying smooth contribution.

Below carrying capacity, higher population increases future density and therefore future headroom. The already proven positive q–N–q loop consequently supplies a downstream amplification path. This does not make `H` a sufficient predictor of final loss because recruitment and direct recoupling can repair subsequent state; it proves that the declared life cycle contains a coherent local reinforcement mechanism on either side of the moving surface.

## 5. Opening-state AA/RR geometry

The locked matched-marginal construction has `q=(0.65,0.75,0.85,0.95)`, AA bundle `B=(0.20,0.40,0.60,0.80)`, RR bundle `B=(0.80,0.60,0.40,0.20)`, and density one at opening. Therefore

\[
S_{AA}=(0.47,0.61,0.75,0.89),
\qquad
S_{RR}=(0.71,0.69,0.67,0.65).
\]

At generation 1, `theta_1=0.5025`, so the exact support boundary is `0.6160168053`. Opening headrooms are

\[
H_{AA}=(-0.1460168,-0.0060168,+0.1339832,+0.2739832),
\]

\[
H_{RR}=(+0.0939832,+0.0739832,+0.0539832,+0.0339832).
\]

The corresponding next interaction states are

\[
q^+_{AA}=(0.4635,0.6186,0.7528,0.8512),
\]

\[
q^+_{RR}=(0.7178,0.6993,0.6800,0.6601).
\]

The deterministic high-allele log-odds increments are approximately

\[
(-0.0668,-0.0026,+0.0499,+0.0866)
\]

for AA and

\[
(+0.0365,+0.0293,+0.0218,+0.0139)
\]

for RR.

AA therefore begins with **two patches below the route surface but two strong positive-headroom cores**. RR begins with **all four patches above the surface, but only shallow headroom**. This is the exact opening form of the earlier equalization-versus-refuge contrast: RR has broader short-term positive routing, whereas AA concentrates deeper positive routing in fewer cores.

## 6. Frozen-support crossing times under the locked forcing slope

The locked barrier schedule is `theta_g=0.50+0.0025g`. If density and local support were held fixed only for diagnostic purposes, the route surface reaches a patch at

\[
g^*=\frac{dS-0.6135168053}{0.0025}.
\]

For opening support at density one:

- AA: `S=.47` and `.61` are already below the surface at generation 1; `.75` crosses at `g*=54.59`; `.89` at `110.59`.
- RR: `.71` crosses at `38.59`; `.69` at `30.59`; `.67` at `22.59`; `.65` at `14.59`.

This is **not** the simulated trajectory because q, B and density evolve. It is an exact opening-state diagnostic. It explains why equalized RR support can look safer early while lacking the deep headroom of the strongest AA cores under a rising boundary.

## 7. Relation to the resolved causal evidence

The theorem organizes, rather than replaces, the prospective interventions:

1. q-dependent allele sorting: sign(`H`) determines the sign of the deterministic allele-selection increment through `q+`;
2. recruitment buffering: reduces trait–allele disagreement before the next bundle is formed;
3. direct recoupling: shifts headroom by exactly `0.4d(B-q)` and preferentially buffered RR in the locked paired ensemble;
4. density failure gate: demographic erosion moves headroom downward by reducing `d`, while q also supports demography, creating the positive q–N–q loop.

The resolved endpoint evidence remains unchanged: focused 6,000-pair allele-selection deletion `DID_40=+6.883 pp [5.800,7.967]`; recruitment-deletion DIDs `-9.00` and `-8.33 pp`; direct-feedback buffering-benefit DIDs `+7.93` and `+6.33 pp`; density deletion removed all generation-20 losses and reduced generation-40 cumulative risk by about 57–60 pp.

## Claim ceiling

`H` is an exact coordinate only for the declared finite closure, weights, interaction map and shared `q*=0.625` switch. Frozen-support crossing times are opening-state diagnostics, not forecasts of natural generations. `H` is not claimed to be a sufficient final-loss predictor because repair operators can change later state. No universal ecological headroom threshold is claimed.