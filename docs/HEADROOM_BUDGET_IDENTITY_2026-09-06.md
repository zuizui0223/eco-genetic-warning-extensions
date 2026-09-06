# Exact discrete headroom budget identity

Status: **exact accounting identity** for changes in route headroom under the declared support coordinates. It converts the route mechanism into a generation-by-generation balance sheet without introducing a new model or fitted parameter.

## 1. Headroom state

For one patch with fixed area ratio `a`, define

\[
H_t=a d_t S_t-\theta_t-c_0,
\]

where

\[
S_t=0.6q_t+0.3T_t+0.1G_t
\]

and `c_0=logit(0.625)/4.5` for the shared route switch.

The constant cancels from changes, so

\[
\Delta H=a(d_{t+1}S_{t+1}-d_tS_t)-\Delta\theta.
\]

## 2. Exact symmetric discrete product rule

For any two values `d_0,S_0` and `d_1,S_1`,

\[
d_1S_1-d_0S_0
=\bar d\,\Delta S+\bar S\,\Delta d,
\]

with

\[
\bar d=(d_1+d_0)/2,
\qquad
\bar S=(S_1+S_0)/2.
\]

Since

\[
\Delta S=0.6\Delta q+0.3\Delta T+0.1\Delta G,
\]

we obtain the exact budget

\[
\boxed{
\Delta H
=a\bar d(0.6\Delta q+0.3\Delta T+0.1\Delta G)
+a\bar S\Delta d
-\Delta\theta.
}
\]

Equivalently, define five terms:

\[
C_q=0.6a\bar d\Delta q,
\quad
C_T=0.3a\bar d\Delta T,
\quad
C_G=0.1a\bar d\Delta G,
\quad
C_d=a\bar S\Delta d,
\quad
C_\theta=-\Delta\theta.
\]

Then

\[
\boxed{
\Delta H=C_q+C_T+C_G+C_d+C_\theta
}
\]

with no residual term.

## 3. Interpretation of the five terms

- `C_q`: interaction-state change changes route reserve directly;
- `C_T`: realised trait-state change changes local support;
- `C_G`: allele-frequency change changes local support;
- `C_d`: demographic density changes the amount of support that is effectively transmitted into the interaction update;
- `C_theta`: external forcing consumes headroom deterministically when the barrier rises.

The already resolved operators map naturally onto this ledger:

- q-dependent allele sorting drives a directional component of future `Delta G`;
- allele-linked recruitment buffers mismatch and therefore changes future `Delta T`;
- direct eco-genetic recoupling acts on `Delta q` through the support-to-interaction transition;
- density feedback acts strongly on `Delta d` and then back on q;
- the imposed deterioration schedule enters only through `-Delta theta`.

Thus the four biological operators and the external forcing can be compared on a common currency: **how much route headroom they add or remove per generation**.

## 4. Why the midpoint form matters

A naive expansion

\[
d_1S_1-d_0S_0=d_0\Delta S+S_0\Delta d+\Delta d\Delta S
\]

contains an interaction residual whose allocation depends on update order. The midpoint identity is symmetric in the before and after states and assigns the product change exactly between support change and density change without a leftover cross-term.

This does not make the biological causal graph simultaneous; the simulator still has an explicit life-cycle order. The midpoint form is an accounting convention for observed state changes, not a replacement for the prospective edge-deletion experiments that identify causal pathways.

## 5. Multi-generation closure

Summing over generations telescopes:

\[
H_T-H_0
=\sum_{t=0}^{T-1}
(C_{q,t}+C_{T,t}+C_{G,t}+C_{d,t}+C_{\theta,t}).
\]

Therefore a complete trajectory can, in principle, be accompanied by an exact headroom balance sheet showing whether interaction change, trait change, allele change, density change or external forcing accounted for its movement toward or away from the route boundary.

## Claim ceiling

The identity is exact algebra, but the labels are accounting contributions rather than independent causal effects. Causal claims about specific operators still come from the prospectively locked interventions and exact operator theorems. The budget does not make headroom alone Markov-sufficient for the full multi-generation eco-genetic trajectory, and it is not a universal natural-system decomposition without system-specific transition weights.
