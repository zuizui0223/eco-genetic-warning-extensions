# Relational mechanism decomposition — locked result (2026-09-06)

Status: **completed from prospectively locked protocol**.

## Question

The flagship already established that matched marginal eco-genetic summaries can encode different exact transitions and, in one locked propagation ensemble, different later functional-loss risks. This experiment asked the next question prospectively:

> **Why can relationally different states reach different ecological outcomes?**

The predeclared causal candidate was

`cross-layer covariance -> support variance -> nonlinear q transition -> functional refugia -> last-refuge loss`.

The experiment also predeclared a 2 x 2 trait/allele assignment decomposition and an intervention that removed direct trait and allele contributions to the interaction-support signal.

## 1. The immediate transition mechanism is exact

In the declared closure,

\[
S_j=\alpha q_j+\beta T_j+\gamma G_j,
\]

with `(alpha,beta,gamma)=(0.6,0.3,0.1)`. For the original aligned and fully reversed states, the mean support is identical (`0.68`), but support population variance is

- aligned: `0.0245`;
- fully reversed: `0.0005`;
- ratio: **49 x**.

This follows exactly from the covariance terms in `Var(S)` with all layer-wise marginals held fixed. Therefore the previously observed `0.2543` next-interaction difference has a mechanistic origin: relational covariance changes the **spatial distribution of local support**, not its mean.

This part of the original mechanism is supported.

## 2. A simple directional refuge mechanism does not explain long-horizon fate

In the new independently seeded 1,500-pair full-feedback comparison, aligned versus fully reversed states did **not** show a stable directional difference in all-patch functional loss:

- generation 20: reversed minus aligned = **-0.8 percentage points**, 95% CI `[-4.16,+2.56]`;
- generation 40: reversed minus aligned = **+0.6 percentage points**, 95% CI `[-2.69,+3.89]`.

Thus the earlier locked `+5.33` and `+5.20` percentage-point propagation contrasts remain results of their prospectively locked ensemble, but they are **not** evidence for a universal rule that positive alignment monotonically protects against long-horizon functional loss.

The predeclared simple chain `support variance -> persistent refuge -> directional long-horizon protection` is therefore insufficient as the full mechanism.

## 3. Trait and allele organization are strongly non-additive

The full-feedback 2 x 2 factorial used:

- `AA`: trait aligned, allele aligned;
- `AR`: trait aligned, allele reversed;
- `RA`: trait reversed, allele aligned;
- `RR`: trait reversed, allele reversed.

Loss rates were:

| horizon | AA | AR | RA | RR |
|---|---:|---:|---:|---:|
| g20 | 0.3733 | 0.4520 | 0.4113 | 0.3653 |
| g40 | 0.6720 | 0.7407 | 0.7033 | 0.6780 |

The predeclared trait-by-allele interaction contrast was:

- g20: **-12.47 pp**, paired 95% CI `[-16.30,-8.63]`;
- g40: **-9.40 pp**, paired 95% CI `[-13.01,-5.79]`.

Equivalently, the average risk of the trait-allele **mismatched** cells (`AR`,`RA`) exceeded the matched cells (`AA`,`RR`) by:

- g20: **+6.23 pp**, paired 95% CI `[+4.32,+8.15]`;
- g40: **+4.70 pp**, paired 95% CI `[+2.90,+6.50]`.

The main effects of reversing either layer alone were much smaller and not consistently directional. The dominant result is therefore **relational coherence between trait and allele layers**, not a single orientation score relative to interaction state.

## 4. Direct eco-genetic feedback into q is not necessary

The preregistered `q-only` intervention set the interaction-support weights to `(1,0,0)`, removing direct trait and allele contributions to `q`. Consequently the aligned and fully reversed conditions had exactly the same generation-1 interaction field and the same initial q-support signal.

Nevertheless, later loss diverged strongly:

- g20: reversed minus aligned = **+7.13 pp**, paired 95% CI `[+3.91,+10.36]`;
- g40: reversed minus aligned = **+6.93 pp**, paired 95% CI `[+3.79,+10.08]`.

At g20, aligned also retained more upper-tail high-trait mass (`+0.0730`, paired 95% CI `[+0.0455,+0.1005]`) and more realised high-trait refugia (`+0.0847` patches on average, `[+0.0361,+0.1332]`). The same direction remained at g40.

Therefore the alignment effect can propagate **without direct trait/allele feedback into q**.

## 5. The indirect causal pathway

The parent life cycle identifies the sufficient indirect path.

1. High allele frequency controls the mixture of low- and high-trait recruitment kernels (`two_kernel_recruitment`).
2. Resident trait state contributes through the inheritance mixture.
3. Trait recruits are selected using interaction-dependent trait fitness.
4. High allele state also affects demographic growth; density then enters the next interaction update.

Thus a high-trait/high-allele bundle located in a high-interaction patch receives mutually compatible recruitment and selection conditions. The same coherent bundle located in a weak-interaction patch is initially mismatched to the ecological condition required by the high trait.

This is a **matching-dependent recruitment pathway**.

## 6. Why full feedback removes most of the AA-RR difference

Full feedback introduces an opposing pathway. Trait mass and allele state themselves contribute directly to the next interaction-support signal. Placing a strong eco-genetic bundle in a weak-interaction patch therefore raises local `q`, partially repairing the ecological mismatch.

The same relational configuration can consequently have two opposing effects:

- **matching pathway:** co-location with a favourable interaction environment promotes high-trait recruitment and retention;
- **compensation pathway:** placing eco-genetic support in a weak interaction environment raises that weak environment through feedback.

In the new full-feedback ensemble these pathways nearly cancel for the two coherent endpoint states (`AA` and `RR`). When direct eco-genetic feedback into `q` is removed, the compensation path is suppressed and the underlying matching advantage becomes visible as the robust ~7 pp aligned advantage.

## 7. Updated ecological interpretation

The causal result is therefore not “alignment protects.” It is:

> **Functional fate is governed by competition among relational pathways. Eco-genetic matching can sustain recruitment where the focal function is viable, whereas feedback can compensate spatial mismatch by strengthening weak local interaction states.**

A single scalar alignment score cannot encode both processes. This explains why relationally different systems can reach collapse, compensation or lag without those outcomes being contradictory.

It also clarifies the natural projection. Systems such as Miyake-jima are relevant as examples of compensatory reorganization, whereas systems such as *Crepis* illustrate cases where local functional limitation is not comparably rescued. They remain discussion anchors, not validation data for this finite mechanism.

## Claim ceiling

Supported for the declared closure:

- covariance controls immediate support variance at fixed marginals;
- trait and allele organization interact strongly and non-additively;
- indirect recruitment/selection/demographic pathways can transmit relational mismatch without direct eco-genetic feedback into q;
- direct q feedback can oppose that mismatch by compensating weak patches.

Not supported:

- universal directional protection by positive alignment;
- support variance as a universal risk score;
- a universal functional-refuge threshold or timescale;
- a claim that natural examples validate the finite closure.

## Provenance

- protocol: `experiments/relational_mechanism_decomposition_protocol.json`;
- workflow run: `34012983845`;
- job: `101431872354`;
- artifact: `9983093178`;
- artifact digest: `sha256:843a6bdc4a4d4e9de10ce6346cca27a1a863b1780573f000c0f1ab164a81c7ac`;
- source head: `d28da102d9b520dce459dd69da794913c77ecd38`;
- compact locked result: `artifacts/relational_mechanism_decomposition/locked_result.json`.
