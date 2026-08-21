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
- **Phase E migration condition**: the independently reproduced R4 anchor remained R4-highrep at allele-frequency migration `m=0,0.025,0.05` and became R3-highrep at `m=0.10,0.20`.

**Status: supported, finite Type S, with a resolved narrow transition frontier and one mapped connectivity boundary.**

## H-MD-3a — event-regime evaluability

Define a warning-evaluable event regime independently of any genetic warning. A high-rep candidate is R4 when every independent seed block has realised functional-loss frequency in `[0.30,0.70]` and the predeclared baseline-eligibility floor is met.

### Original common-grid result

The strict Protocol 002 selector found:

- eligible candidate count = 0;
- selected domain count = 0;
- `no_domain_selected` = 15/15 coordinates.

This remains an immutable result for the **declared coarse common grid/family**. It was never evidence that the warning itself failed.

### Refined recurrent-transition recovery

At fixed:

- `A_ref=1.0`;
- interaction `kappa=4.5`;
- `kappa_mu=0.35`;
- ramp 30 + hold 90 (horizon 120);
- normalized barrier increase `0.30`;
- equal-isolated projection;

`p_star=0.35` recovered R4 independently twice.

**Phase C:** seed loss rates `0.579, 0.529, 0.474, 0.588, 0.368`; pooled loss `0.505`.

**Phase D independent replay:** `0.500, 0.667, 0.647, 0.588, 0.632`; pooled loss `0.609`.

Neighbors were not R4:

- `p_star=0.325`: pooled `0.663`, but two seed blocks >0.70;
- `p_star=0.375`: pooled `0.391`, but one seed block <0.30;
- `p_star=0.40` in Phase C: pooled `0.304`, but two seed blocks <0.30.

Thus the coarse-grid 15/15 no-domain result was **not structural impossibility**. R4 exists, but it is narrow along the tested recurrent-transition frontier.

### Phase E — effective genetic connectivity

Phase E fixed the independently reproduced R4 anchor and varied only the simulator's allele-frequency migration toward the population-weighted selected mean. One hundred prepared sources were paired across five rates, producing 500 migration-level trajectories.

| `migration_rate` | pooled trait-loss rate | regime |
|---:|---:|---|
| 0.000 | 0.571 | **R4-highrep** |
| 0.025 | 0.549 | **R4-highrep** |
| 0.050 | 0.593 | **R4-highrep** |
| 0.100 | 0.626 | **R3-highrep** |
| 0.200 | 0.604 | **R3-highrep** |

Relative to isolation, paired loss-status switches increased with mixing: 8/91, 12/91, 21/91 and 25/91 trajectories at the four nonzero rates, and both `loss→no loss` and `no loss→loss` occurred at every rate.

### Recovered H-MD-3a conclusion

**H-MD-3a is positively recovered in a bounded finite region, and evaluability itself is connectivity-dependent.**

The important distinction is now stronger than a pooled-risk statement:

> intermediate pooled functional-loss probability is not sufficient for warning evaluability; reproducibility across independent stochastic blocks is an additional condition, and effective genetic connectivity can change that reproducibility without a simple monotone rescue/collapse shift in pooled loss.

The `p_star` and migration searches are closed under their predeclared stop rules. No finer tuning is permitted merely to widen R4.

## H-MD-3b — direction-only warning effect

**Proposition.** Conditional on at least two matched evaluable domains under identical non-direction conditions, recurrent-transition direction changes warning availability, ordering or lead time.

### Current finite status

**Still not tested in the refined frontier program.** Phases A–E withheld all diversity and warning fields.

A reproducible R4 point exists, and several matched migration conditions retain R4, but H-MD-3b is specifically a recurrent-transition-direction contrast. The predeclared opening condition required an adjacent confirmed R4 interval along `p_star`; Phase D found no such adjacent R4 at ±0.025. Therefore no new direction-only warning validation is opened.

Protocol 003 remains a separate portability comparison across two independently recalibrated, non-matched eco-genetic domains.

## Exact recurrent-transition and migration boundaries

### T1 — no universal signed direction-to-diversity effect

For \(H(p)=2p(1-p)\), \(k=\kappa_\mu\), \(s=p_\mu^*\),

\[
\frac{\partial H(M(p))}{\partial s}=2k[1-2M(p)].
\]

The sign changes at `M(p)=0.5`.

### T2 — transition strength and direction have separable spatial effects

With fixed patch weights,

\[
H_\gamma'-H_\alpha'=(1-k)^2(H_\gamma-H_\alpha).
\]

Thus one-step contraction of among-patch allele-frequency heterogeneity depends on `kappa_mu`, not `p_star`.

### T3 — local high-state support and diversity can oppose

For support margin \(S=M(p)-p_c\),

\[
\frac{\partial S}{\partial s}=k>0.
\]

When `M(p)>0.5`, increasing `p_star` strengthens the local high-associated allele condition while decreasing heterozygosity.

### T4 — recurrent-transition support frontier

For a pre-state below a local high-state threshold, stronger `kappa_mu` lowers the `p_star` required to reach the same post-transition support boundary.

### T5 — migration homogenisation is not a functional-loss sign theorem

In the parent migration layer, allele-frequency mixing contracts deviations from a common mean and can coexist with a separately certified rescue condition. Phase E shows in the full finite closure that migration can change which trajectories lose realised function in both directions. Therefore neither the exact homogenisation result nor nonzero connectivity carries a universal beneficial/harmful sign for realised functional loss.

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
| **H-MD-3a refined recurrent condition** | **positive, independently reproduced** | R4 exists at `kappa_mu=0.35, p_star=0.35`, but is narrow along `p_star` |
| **H-MD-3a connectivity condition** | **supported at one R4 anchor** | R4 persisted at `m<=0.05` and shifted to R3 at `m=0.10,0.20`; pooled risk alone did not explain evaluability |
| **H-MD-3b finite effect** | **not opened** | no contiguous matched R4 interval was recovered along recurrent-transition direction |
| **H-MD-3b theory** | **Type T boundaries recovered** | diversity sign, spatial contraction and local functional support are not interchangeable |
| **Protocol 003** | **portability result** | warning availability/ordering differ across non-matched recalibrated domains; cause is not isolated to direction |

## Next condition decision

Do **not** refine `p_star` or migration further. The next ecological uncertainty is whether local interaction/habitat support changes the recovered R4/connectivity structure. This is directly relevant to urban pollinator support and island mutualist/reproductive-assurance gradients.

However, another simulation campaign should be opened only if that empirical analogue can be represented cleanly by an existing model parameter. If not, condition recovery should stop here and the manuscript should be rewritten around the recovered hierarchy rather than adding an abstract parameter sweep.

## Stop rules

Do not:

1. refine `p_star` further merely to manufacture a wider R4 region;
2. tune migration further merely to preserve or create R4;
3. tune any condition using warning/diversity outcomes;
4. call the current migration effect demographic, pollinator or seed rescue;
5. open H-MD-3b unless the required matched evaluable recurrent-transition conditions are prospectively satisfied;
6. overwrite the historical Protocol 002 15/15 no-domain result.
