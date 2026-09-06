# Exact eco-genetic coherence switch at the route-headroom boundary

Status: **exact local life-cycle theorem** for the declared finite closure. It shows that the route-headroom boundary does not only separate next interaction states: the same boundary simultaneously separates high-trait potential viability and the deterministic direction of high-allele selection.

## 1. Headroom representation

For target `c=0.625`, define local route headroom `H` so that

\[
q^+=\sigma\{\operatorname{logit}(0.625)+\kappa H\},
\qquad \kappa=4.5.
\]

Because the logistic function is strictly increasing,

\[
H\gtreqless0
\iff
q^+\gtreqless0.625.
\]

## 2. The same q*=0.625 is the high-trait viability switch

For the pinned parent trait surface,

\[
W(z;q)=1.1-0.8z^2+(0.2+0.8q)\exp[-((z-1)/0.15)^2].
\]

At the focal high trait `z=1`,

\[
W(1;q)=0.5+0.8q.
\]

With viability threshold one,

\[
W(1;q)-1=0.8(q-0.625).
\]

Hence

\[
q^+\gtreqless0.625
\iff
W(1;q^+)\gtreqless1.
\]

So positive route headroom means that the next interaction state is also on the potentially viable side for the declared high trait.

## 3. The same q*=0.625 is the high-allele selection switch

The deterministic high-allele selection step uses the newly updated interaction state `q^+`. With selection strength `s=0.5`, its relative high-allele fitness is

\[
w(q^+)=1+s[W(1;q^+)-1]
=0.75+0.4q^+.
\]

Thus

\[
w(q^+)\gtreqless1
\iff
q^+\gtreqless0.625.
\]

For any interior allele frequency `0<p<1`,

\[
p_s=\frac{p w}{1-p+pw},
\]

and therefore

\[
p_s-p
=\frac{p(1-p)(w-1)}{1-p+pw}.
\]

The denominator is positive, so

\[
\boxed{
H\gtreqless0
\iff
q^+\gtreqless0.625
\iff
W(1;q^+)\gtreqless1
\iff
p_s\gtreqless p.
}
\]

Equality holds throughout at `H=0`.

This is the exact **eco-genetic coherence switch**. Crossing one local route surface simultaneously changes:

1. which side of the interaction threshold the patch enters;
2. whether the declared high trait is potentially viable at the next interaction state;
3. whether deterministic selection increases or decreases the high allele.

## 4. Quantitative sensitivity at the switch

Because

\[
q^+(H)=\sigma[\operatorname{logit}(0.625)+4.5H],
\]

at `H=0`,

\[
\boxed{
\frac{dq^+}{dH}=4.5(0.625)(0.375)=1.0546875.
}
\]

The high-trait viability margin has slope

\[
\boxed{
\frac{d[W(1;q^+)-1]}{dH}=0.8(1.0546875)=0.84375.
}
\]

The relative high-allele fitness has slope

\[
\boxed{
\frac{dw}{dH}=0.4(1.0546875)=0.421875.
}
\]

At the boundary `w=1`, so the selection-induced log-odds increment `log w` also has derivative `0.421875` with respect to H.

Thus H is not merely a sign label. Near the switch it has a quantified local effect on ecological interaction state, trait viability margin and allele-selection pressure.

## 5. Mechanistic consequence

The shared threshold creates a locally coherent reinforcement structure. Once the route margin is positive, the next interaction state both supports the high trait and selects the high allele upward. Once the margin is negative, the next interaction state lies below high-trait potential viability and selects the high allele downward.

This does not mean the system becomes irreversibly bistable at H=0. Recruitment, direct recoupling, density feedback, future forcing and finite drift can move later headroom back across the surface. The theorem instead identifies why crossing the route boundary changes several eco-genetic tendencies in the same direction within the declared life cycle.

## Claim ceiling

The triple equivalence is exact for the pinned trait-performance surface, selection rule and interaction update. It is not asserted as a universal ecological threshold, an evolutionary stable state, or an irreversible natural tipping point. Realised high-trait occupancy can lag potential viability, and later stochastic or feedback processes can reverse the subsequent trajectory.
