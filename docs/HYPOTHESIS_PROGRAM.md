# Independent hypothesis program

## Current scientific question

`eco-genetic-warning-extensions` does **not** reopen the completed H1/H3 evidence ledger in `eco-genetic-criticality`. It changes the recurrent state-transition closure and asks, in order:

```text
H-MD-1  Can the high-function source state be established?
   ↓
H-MD-2  What realised functional-loss regime is generated?
   ↓
H-MD-3a Does a matched warning-validation domain exist?
   ↓
H-MD-3b If it exists, does transition direction itself change warning performance?
```

H-MD-1/2/3 were present in the pre-campaign Paper 001 design. The split of H-MD-3 into **3a/3b is post hoc logical decomposition**, used only to state clearly which part of the completed evidence is resolved. It is not retroactive preregistration.

## Inherited parent result, not extension evidence

The parent finite program established its own bounded chain:

```text
interaction feedback can support distinct functional states
→ fragmentation can disrupt the high-function state and reduce local effective size
→ relative genetic erosion can precede realised functional-trait loss in one calibrated symmetric domain
```

Those parent trajectories are never pooled with extension trajectories. The canonical parent scientific state remains `dd8ee379d0d3518194c767d16402042525bc00dc`.

## H-MD-1 — source feasibility

**Proposition.** At fixed recurrent-transition relaxation strength `kappa_mu`, changing directional equilibrium `p_star` changes the finite region in which a prepared high-function source can be established.

For

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p,
\]

a local post-transition requirement \(M(p)\ge p_c\) requires, for \(\kappa_\mu<1\),

\[
p\ge\theta(p_c)=\frac{p_c-\kappa_\mu p_\mu^*}{1-\kappa_\mu}.
\]

Increasing `p_star` lowers this required pre-transition frequency.

**Test.** Protocol 002 Stage I, common `3 kappa_mu × 5 p_star` grid with independent source reconstruction.

**Result.** 2,269 of 3,375 attempts supported source preparation/projection; coordinate support ranged from 44.89% to 86.67% and generally increased with `p_star` within fixed-`kappa_mu` rows.

**Status: supported, finite Type S.**

## H-MD-2 — functional-loss regime

**Proposition.** Under the same deterioration candidate family, recurrent-transition coordinates change the realised high-trait-loss regime.

**Test.** Protocol 002 Stage II used the same warning-blind deterioration family across all 15 coordinates. Diversity and warning fields were unavailable to calibration.

**Result.** Among 648 complete five-seed candidates:

- 322 rapid-loss-side;
- 242 persistence-side;
- 84 seed-heterogeneous.

**Status: supported, finite Type S.**

This is an upstream result: recurrent-transition dynamics changed how functional loss was generated before genetic warning was evaluated.

## H-MD-3a — matched-domain evaluability

For coordinate \(\theta\), define the strict Protocol 002 eligible set

\[
E_\theta=\{c:0.30\le r_{c,b}\le0.70\text{ for every one of five seed blocks }b\}.
\]

The locked selector can choose a warning-validation domain **if and only if** \(E_\theta\neq\varnothing\).

**Result.** Across the completed Stage II evidence:

- eligible candidate count = 0;
- selected domain count = 0;
- `no_domain_selected` = 15/15 coordinates.

Thus \(E_\theta=\varnothing\) for every tested coordinate in the declared common candidate family.

**Status: negative result, recovered for the declared finite grid/family.**

This is a finite **no-domain/evaluability certificate**, not evidence that genetic warning itself failed. Warning values were not inspected during this selection.

## H-MD-3b — direction-only warning effect

**Proposition.** Conditional on matched evaluable domains existing under a common deterioration family, recurrent-transition direction changes warning availability, lead/lag ordering, or lead time.

### Finite empirical status

**Bounded unresolved / not identified.** Protocol 002 never instantiated the matched domains required for this contrast. Therefore the current finite evidence cannot assign a direction-only warning effect or null effect.

### Type T boundary 1 — no universal direction-to-diversity sign

For \(H(p)=2p(1-p)\), write \(k=\kappa_\mu\), \(s=p_\mu^*\), and \(M(p)=p+k(s-p)\). Then

\[
H(M(p))-H(p)=2k(s-p)[1-2p-k(s-p)],
\]

and

\[
\frac{\partial H(M(p))}{\partial s}=2k[1-2M(p)].
\]

So increasing `p_star` can increase or decrease heterozygosity depending on the current allele-frequency state; the sign changes at \(M(p)=1/2\).

### Type T boundary 2 — direction and among-patch contraction are separable

With fixed patch weights,

\[
H_\gamma-H_\alpha=2\operatorname{Var}_w(p_j),
\]

and a common affine transition gives

\[
H_\gamma'-H_\alpha'=(1-k)^2(H_\gamma-H_\alpha).
\]

This contraction depends on `kappa_mu` but not on `p_star`. Direction shifts the weighted mean allele state; transition strength contracts among-patch deviations.

### Type T boundary 3 — local function-support and diversity can oppose each other

For local high-associated allele support margin

\[
S=M(p)-p_c,
\]

\[
\frac{\partial S}{\partial s}=k>0.
\]

Thus increasing `p_star` always strengthens this local post-transition high-state support condition. But diversity follows the derivative above. Therefore:

- \(M(p)<1/2\): support and heterozygosity increase together;
- \(M(p)=1/2\): support increases while heterozygosity is stationary to first order;
- \(M(p)>1/2\): support increases while heterozygosity **decreases**.

So genetic diversity is **not a monotone proxy for local functional support** under this recurrent-transition operator. Full realised ecological function still depends on the complete stochastic life cycle; this is a local Type T support boundary, not a warning theorem.

The exact derivations and executable tests are in [`RECURRENT_TRANSITION_DIVERSITY_THEORY.md`](RECURRENT_TRANSITION_DIVERSITY_THEORY.md) and `src/eco_genetic_warning_extensions/mutation_coordinates.py`.

## Protocol 003 — portability, not H-MD-3b recovery

Protocol 003 was declared only after Protocol 002 closed. Warning-blind recalibration recovered two evaluable domains, but they differ in recurrent-transition parameters **and** `A_ref`, interaction-feedback `kappa`, deterioration strength, and horizon.

Observed Stage III:

- recalibrated symmetric: 323 lead / 1 tie / 0 lag, valid-pair availability 0.540;
- directional calibrated: 184 lead / 5 tie / 12 lag, availability 0.335;
- directional `H_gamma` 20%: warning 41/81 versus realised functional loss 52/81;
- all six full-horizon-normalized direct timing-difference intervals include zero.

**Status: separate portability/boundary result.** Warning behaviour is not invariant across the two recalibrated domains, but the contrast does not identify recurrent-transition direction alone.

## Historical H2-R-AS

H2-R-AS was the original Protocol 001 special-case warning formulation. It remains part of protocol history, not the final organising hypothesis. The completed campaigns showed that source feasibility, functional-loss regime, and matched-domain evaluability must be resolved before a direction-only warning comparison is meaningful.

## Final recovery ledger

| item | status | current conclusion |
|---|---|---|
| **H-MD-1** | **supported** | recurrent-transition coordinates change high-function source feasibility |
| **H-MD-2** | **supported** | recurrent-transition coordinates change functional-loss regime |
| **H-MD-3a** | **negative / recovered** | no eligible matched common-family warning domain exists in the tested 15-coordinate design |
| **H-MD-3b finite effect** | **bounded unresolved** | matched direction-only warning effect was not instantiated |
| **H-MD-3b theory** | **Type T boundaries recovered** | direction has no universal diversity sign; diversity and local high-state support can move in opposite directions |
| **Protocol 003** | **portability result** | warning availability/ordering differ across two non-matched recalibrated domains; cause is not isolated to direction |

## Stop rule before any new protocol

Do not open a new finite campaign merely by widening schedules or relaxing the Protocol 002 gate. A future H-MD-3b campaign is scientifically justified only after it predeclares:

1. a matched deterioration family with non-direction parameters fixed across compared coordinates;
2. a warning-blind evaluability rule;
3. a specified allele-frequency state/path region;
4. a directional prediction derived from the Type T identities above;
5. fresh calibration and validation seeds.

Until then, H-MD-3b is **scientifically bounded rather than unfinished**.

## Protocol map

- **Protocol 001:** historical bridge/pilot; H2-R-AS provenance.
- **Protocol 002 Stage I:** H-MD-1.
- **Protocol 002 Stage II:** H-MD-2 + H-MD-3a.
- **Protocol 003:** separately declared evaluability recovery + non-matched portability validation.
- **Secondary review audit:** locked-record uncertainty/timing/censoring analysis; no simulation rerun.

## Current interpretation boundary

Permitted:

- source feasibility and functional-loss regime change across recurrent-transition coordinates;
- the strict common candidate family contains no eligible warning-validation domain at all 15 tested coordinates;
- direction alone has no universal signed one-step effect on diversity;
- stronger local high-state allele support can coincide with lower genetic diversity;
- warning portability differs across the two separately recalibrated domains.

Not permitted:

- H-MD-3b is false merely because no Protocol 002 domain was selected;
- Protocol 003 identifies a direction-only causal warning effect;
- lower genetic diversity necessarily means poorer ecological function;
- the local transition theorem determines full warning first-passage ordering;
- `p_star` is an empirical biological mutation-rate estimate;
- extension evidence replaces the parent H1/H3 ledger.
