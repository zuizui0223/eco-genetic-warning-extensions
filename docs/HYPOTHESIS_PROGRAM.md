# Independent hypothesis program

## Current scientific question

`eco-genetic-warning-extensions` does **not** reopen the completed H1/H3 evidence ledger in `eco-genetic-criticality`. It extends that mechanism by asking, in order:

```text
H-MD-1  Can the high-function source state be established?
   ↓
H-MD-2  What realised functional-loss regime is generated?
   ↓
H-MD-3a Does a reproducible, nondegenerate event regime exist in which warning is estimable?
   ↓
H-MD-3b Only if a matched evaluable region exists: does transition direction change warning performance?
```

The split of historical H-MD-3 into **3a/3b is a post hoc logical decomposition**. It is used to state what is and is not resolved; it is not retroactive preregistration.

## Inherited parent mechanism

The parent repository established the bounded mechanistic chain:

```text
interaction feedback can support distinct functional states
→ fragmentation can disrupt the prepared high-function state
→ interaction, local effective size and realised high-trait mass can fall
→ relative genetic erosion can precede realised functional-trait loss in one calibrated symmetric domain
```

Parent trajectories are never pooled with extension trajectories. The canonical parent scientific state remains `dd8ee379d0d3518194c767d16402042525bc00dc`.

## H-MD-1 — source feasibility

**Proposition.** At fixed recurrent-transition strength `kappa_mu`, changing directional equilibrium `p_star` changes the finite region in which a prepared high-function source can be established.

For

\[
M(p)=\kappa_\mu p_\mu^*+(1-\kappa_\mu)p,
\]

a local post-transition requirement \(M(p)\ge p_c\) requires, for \(\kappa_\mu<1\),

\[
p\ge\theta(p_c)=\frac{p_c-\kappa_\mu p_\mu^*}{1-\kappa_\mu}.
\]

Increasing `p_star` lowers this required pre-transition frequency.

**Finite result.** Protocol 002 Stage I produced 2,269 supported source preparations/projections from 3,375 attempts. Coordinate support ranged from 44.89% to 86.67% and generally increased with `p_star` within fixed-`kappa_mu` rows.

**Status: supported, finite Type S.**

## H-MD-2 — functional-loss regime

**Proposition.** Under a common deterioration family, recurrent-transition coordinates alter the realised high-trait-loss regime.

**Locked Protocol 002 result.** Among 648 complete five-seed candidates:

- 322 rapid-loss;
- 242 persistence;
- 84 seed-heterogeneous;
- 0 strict warning-evaluable candidates on the original common grid.

A later warning-blind reaggregation of the same 810 Stage II batches showed that, among matched complete candidates, increasing `p_star` or `kappa_mu` never increased pooled trait-loss rate in the tested adjacent contrasts. Horizon extension could reveal additional losses, while barrier magnitude, `A_ref` and interaction `kappa` had weaker or mixed pooled-loss effects conditional on candidate completeness.

Prospective frontier work then resolved the rapid-to-persistence transition more finely:

- **Phase A (`kappa_mu=0.05`)**: 10 interior cells / 250 attempts; 0 R4, 6 R3, 4 R2.
- **Phase B (`kappa_mu=0.35`)**: at one fixed ecological/deterioration anchor, pooled loss declined smoothly across `p_star=0.30,0.35,0.40,0.45` (`0.739→0.476→0.304→0.095`), but all four low-rep cells were seed-heterogeneous.
- **Phase C high-rep**: `p_star=0.35` became R4-highrep; `0.40` remained R3-highrep.
- **Phase D independent high-rep replay**: `0.35` again became R4-highrep; neighboring `0.325` and `0.375` were R3-highrep.

**Status: supported, finite Type S, with a resolved narrow transition frontier.**

## H-MD-3a — event-regime evaluability

Define a warning-evaluable event regime independently of any genetic warning. A high-rep candidate is R4 when every independent seed block has realised functional-loss frequency in `[0.30,0.70]` and the predeclared baseline-eligibility floor is met.

### Original common-grid result

The strict Protocol 002 selector found:

- eligible candidate count = 0;
- selected domain count = 0;
- `no_domain_selected` = 15/15 coordinates.

This remains an immutable result for the **declared coarse common grid/family**. It was never evidence that the warning itself failed.

### Refined condition recovery

Warning-blind Phases B–D show that the coarse-grid result was **not structural impossibility**.

At fixed:

- `A_ref=1.0`;
- interaction `kappa=4.5`;
- `kappa_mu=0.35`;
- ramp 30 + hold 90 (horizon 120);
- normalized barrier increase `0.30`;
- equal-isolated projection;

`p_star=0.35` recovered R4 independently twice.

**Phase C:**

- seed loss rates `0.579, 0.529, 0.474, 0.588, 0.368`;
- pooled loss `0.505`;
- all five blocks in `[0.30,0.70]`.

**Phase D independent replay:**

- seed loss rates `0.500, 0.667, 0.647, 0.588, 0.632`;
- pooled loss `0.609`;
- all five blocks in `[0.30,0.70]`.

Neighbors were not R4:

- `p_star=0.325`: pooled `0.663`, but two seed blocks exceeded 0.70;
- `p_star=0.375`: pooled `0.391`, but one seed block fell below 0.30;
- `p_star=0.40` in Phase C: pooled `0.304`, but two seed blocks fell below 0.30.

### Recovered conclusion

**H-MD-3a is now positively recovered in a narrow finite region.**

The important distinction is:

> intermediate pooled loss probability is not sufficient for warning evaluability; reproducibility across independent stochastic blocks is an additional condition.

The original 15/15 no-domain result therefore means that the predeclared coarse common grid missed the narrow R4 region, not that R4 cannot exist.

The `p_star` search stops here. Phase D did not find a contiguous neighboring R4 cell at ±0.025, and no finer tuning is permitted merely to widen the warning domain.

## H-MD-3b — direction-only warning effect

**Proposition.** Conditional on at least two matched evaluable domains under identical non-direction conditions, recurrent-transition direction changes warning availability, ordering or lead time.

### Current finite status

**Still not tested in the refined frontier program.** Phases A–D withheld all diversity and warning fields.

A reproducible R4 point now exists, but the predeclared condition for opening a new direction-only warning experiment was a contiguous matched R4 interval. Phase D found no adjacent R4 at ±0.025. Therefore no new H-MD-3b warning validation is opened from this frontier.

Protocol 003 remains a separate portability comparison across two independently recalibrated, non-matched eco-genetic domains.

## Exact recurrent-transition boundaries

The local affine operator provides several Type T constraints on interpretation.

### T1 — no universal signed direction-to-diversity effect

For \(H(p)=2p(1-p)\), \(k=\kappa_\mu\), \(s=p_\mu^*\),

\[
\frac{\partial H(M(p))}{\partial s}=2k[1-2M(p)].
\]

The sign changes at `M(p)=0.5`. Increasing `p_star` can therefore increase or decrease heterozygosity depending on state.

### T2 — transition strength and direction have separable spatial effects

With fixed patch weights,

\[
H_\gamma'-H_\alpha'=(1-k)^2(H_\gamma-H_\alpha).
\]

Thus the one-step contraction of among-patch allele-frequency heterogeneity depends on `kappa_mu`, not `p_star`.

### T3 — local high-state support and diversity can oppose

For support margin \(S=M(p)-p_c\),

\[
\frac{\partial S}{\partial s}=k>0.
\]

When `M(p)>0.5`, increasing `p_star` strengthens the local high-associated allele condition while decreasing heterozygosity. Genetic diversity is therefore not a monotone proxy for local functional support.

### T4 — recurrent-transition support frontier

For a pre-state below a local high-state threshold, stronger `kappa_mu` lowers the `p_star` required to reach the same post-transition support boundary. This gives the correct direction for the finite frontier shift without claiming a theorem for the full stochastic loss regime.

## Protocol 003 — portability, not direction-only recovery

Protocol 003 was declared after the original Protocol 002 no-domain result. Warning-blind recalibration recovered two evaluable domains, but they differ in recurrent-transition parameters, `A_ref`, interaction `kappa`, deterioration strength and horizon.

Observed Stage III:

- recalibrated symmetric: 323 lead / 1 tie / 0 lag, valid-pair availability 0.540;
- directional calibrated: 184 lead / 5 tie / 12 lag, availability 0.335;
- directional `H_gamma` 20%: warning 41/81 versus realised functional loss 52/81;
- all six full-horizon-normalized direct timing-difference intervals include zero.

**Status: bounded portability result, not an isolated direction effect.**

## Current recovery ledger

| item | status | current conclusion |
|---|---|---|
| **parent H1/H3** | **mechanistic core recovered** | interaction-dependent function can be prepared and fragmentation can disrupt it under the declared parent closure |
| **H2 relative benchmark** | **conditionally supported** | relative genetic erosion can precede realised functional loss in one calibrated symmetric domain |
| **H-MD-1** | **supported** | recurrent-transition coordinates change high-function source feasibility |
| **H-MD-2** | **supported** | recurrent-transition coordinates reorganise functional-loss regimes |
| **H-MD-3a coarse grid** | **negative, immutable** | 15/15 original coordinates selected no domain under the strict common-family gate |
| **H-MD-3a refined condition** | **positive, independently reproduced** | R4 exists at the fixed B1 condition with `kappa_mu=0.35, p_star=0.35`, but is narrow along `p_star` |
| **H-MD-3b finite effect** | **not opened** | no contiguous matched R4 interval was recovered at the predeclared ±0.025 resolution |
| **H-MD-3b theory** | **Type T boundaries recovered** | diversity sign, spatial contraction and local functional support are not interchangeable |
| **Protocol 003** | **portability result** | warning availability/ordering differ across non-matched recalibrated domains; cause is not isolated to direction |

## Next condition axis — migration / effective genetic connectivity

The recurrent-transition direction search is closed. The next biologically motivated condition question is whether **allele-frequency migration among fragmented patches** shifts the event-regime class of the independently reproduced R4 anchor.

This is directly connected to the remaining H3 boundary and to urban/island applications, but the simulator scope must remain explicit:

- `migration_rate` in the current life cycle mixes allele frequencies toward the population-weighted mean;
- it is **not** demographic migration, pollinator movement, seed dispersal, or trait-bin dispersal;
- parent Type T results already show that migration can homogenize patch frequencies and can coexist with separately certified rescue conditions;
- therefore the finite sign of migration on realised functional-loss regime is not assumed in advance.

The next campaign must remain trait-loss/source-only. Genetic diversity and warning outcomes stay locked until the connectivity condition map is fixed.

## Stop rules

Do not:

1. refine `p_star` further merely to manufacture a wider R4 region;
2. tune migration using warning/diversity outcomes;
3. call any migration effect demographic or pollinator rescue without an explicit life-cycle extension;
4. open H-MD-3b unless the required matched evaluable conditions are prospectively satisfied;
5. overwrite the historical Protocol 002 15/15 no-domain result.
