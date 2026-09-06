# Pathway edge decomposition — result

Status: **completed and locked from the prospectively declared run**.

## Question

Which life-cycle links transmit the AA-versus-RR functional-loss difference after direct trait/allele feedback into `q` has already been removed?

The protocol was committed before outcomes (`76ff259df512a8afda521226ae5d24c0339a4033`). The scientific run used exactly eight declared interventions, five fresh master seeds, 300 replicates per seed and the original 40-generation forcing/endpoint contract.

## Fresh baseline

The indirect q-only relational effect reproduced independently:

- generation 20: AA `.3833`, RR `.4253`, RR-AA **`+4.20 pp`** (`95% CI +0.86,+7.54`);
- generation 40: AA `.6873`, RR `.7313`, RR-AA **`+4.40 pp`** (`+1.18,+7.62`).

The previous ~7-point q-only effect is therefore not a one-off, although its magnitude is not fixed.

## 1. Allele-linked recruitment is a buffer, not the source of the matching advantage

Deleting `G -> recruit trait distribution` increased absolute loss sharply and enlarged the RR disadvantage:

- generation 20 deletion: AA `.7667`, RR `.8987`, RR-AA **`+13.20 pp`**;
- generation 40 deletion: AA `.7780`, RR `.9053`, RR-AA **`+12.73 pp`**.

The preregistered difference-in-differences was

- g20: **`-9.00 pp`** (`-13.29,-4.71`);
- g40: **`-8.33 pp`** (`-12.53,-4.14`).

By the locked decision rule this is a resolved **countervailing / compensatory pathway**. Allele-linked recruitment replenishes high-trait state in both arrangements and disproportionately rescues the reversed arrangement. The earlier wording that allele-linked recruitment itself generated the matching advantage is therefore rejected.

## 2. Local ecological selection as a block creates the late matching advantage

Deleting both local spatial selection links — `q -> allele selection` and `q -> trait selection` — changed the RR-AA contrast to:

- g20: `+0.60 pp`; DID `+3.60 pp` (`-1.18,+8.38`), unresolved;
- g40: `-2.87 pp`; DID **`+7.27 pp`** (`+2.67,+11.87`), resolved.

Thus local ecological selection as a **joint block** is required for the late AA advantage.

The single-edge tests refine but do not fully resolve that block:

- deleting local `q -> trait selection`: essentially no attenuation at g20 or g40;
- deleting local `q -> allele selection`: RR-AA falls to `+2.47 pp` at g20 and `+0.33 pp` at g40, but the preregistered DID intervals still include zero.

Secondary mediators point toward the allele-selection branch. Under the baseline at g20/g40, AA has more high-trait mass, more allele-state differentiation and later more realised refugia. After deleting local allele selection, those AA-RR mediator contrasts shrink to values whose paired intervals include zero. This makes **q-dependent allele sorting the leading single-edge candidate**, but it does not satisfy the locked risk-level resolution rule and must remain labelled unresolved individually.

## 3. Resident trait memory, local trait selection alone and state-dependent growth are not individually required

The preregistered DIDs remained unresolved when deleting:

- resident trait inheritance;
- local q-dependent trait selection alone;
- q/high-allele contributions to demographic growth.

These results rule out a simple chain in which any one of those links alone explains the q-only AA advantage.

## 4. Density-to-q feedback is a failure gate, not a clean matching-specific mediator

Deleting the density multiplier from the q update produced **zero losses in either condition by generation 20**. At generation 40, loss was delayed to `.1127` in AA and `.1353` in RR.

Thus `N -> q` feedback is required for the declared forcing trajectory to enter early system-wide functional loss. The g20 DID is formally positive because the endpoint disappears entirely, but that degeneracy prevents a clean matching-specific mediation interpretation. At g40 the attenuation of the AA-RR contrast is unresolved.

The correct interpretation is therefore **failure gate / amplification**, not “density feedback causes the matching advantage.”

## 5. The trajectory reveals concentration before persistence

Fresh baseline mediator trajectories show a temporal crossover.

At generation 5, AA has substantially greater maximum high-trait mass (`+0.0744`, CI `+0.0626,+0.0862`) while occupying **fewer** high-trait refugia (`-0.1813 patch`, `-0.2188,-0.1439`). The same pattern remains weaker at generation 10.

By generation 20 the sign of refuge number reverses: AA retains `+0.0767` more realised refugia (`+0.0285,+0.1248`) while keeping the upper-tail high-trait-mass advantage. At generation 40 the corresponding differences are `+0.0533` refugia and `+0.0426` maximum high-trait mass.

This is a **concentration-to-persistence signature**: the aligned state initially concentrates focal functional state more strongly into fewer patches, then retains more patches later. It is descriptive of the mechanism trajectory and is not used as a separate causal certificate.

## Updated mechanism

The q-only indirect mechanism is now best summarized as:

```text
local ecological selection
        |
        v
selection-mediated spatial sorting
        |
        +----> persistent compatible local cores ----> lower late loss
        |
        ^
        |
allele-linked recruitment
(recruitment-mediated buffering of mismatch)

N -> q density feedback = failure/amplification gate
```

The key correction is that **allele-linked recruitment belongs on the buffering side**, not the sorting side. The late sorting contribution is resolved only for the joint local-selection block; q-dependent allele selection is the leading single-edge candidate but remains individually unresolved under the locked risk criterion.

## Ecological interpretation

This sharpens the flagship’s “competing pathways” claim. Relational state affects fate because a life cycle can do two opposite things with spatial mismatch:

1. **sort** compatible ecological and genetic states into persistent local cores; and
2. **buffer** mismatch by replenishing focal phenotype where local compatibility is weak.

Direct trait/allele feedback to interaction state, recovered in the prior mechanism experiment, is a second buffering/recoupling route. Functional fate is therefore not controlled by alignment as a scalar; it is the outcome of **sorting versus buffering under feedback-amplified deterioration**.

## Provenance

- prospective workflow run: `34014537015`
- job: `101435935218`
- artifact ID: `9983623440`
- artifact digest: `sha256:45b38de7514dac8df356579156d994fbc5728e8924308299b2b73571b3595842`
- scientific head: `1502e9c9c82ce45755593f0acdfe2da1a4d34b95`
- protocol commit: `76ff259df512a8afda521226ae5d24c0339a4033`
- compact locked result: `artifacts/pathway_edge_decomposition/locked_result.json`

## Claim boundary

These assignments apply to the declared finite q-only closure. Do not promote local allele selection to a resolved single-edge causal claim; do not interpret the generation-20 density deletion as clean matching-specific mediation; and do not generalize the observed sorting, buffering or timescales as universal natural laws.
