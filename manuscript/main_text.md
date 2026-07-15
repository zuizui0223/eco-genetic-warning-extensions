# Directional recurrent mutation partitions trait-loss regimes in finite eco-genetic systems

## Abstract

Genetic early-warning analyses usually ask whether a genetic signal precedes demographic or functional loss, but they rarely ask whether the underlying genetic closure permits a comparable loss-event regime in which warning performance can be evaluated. We extended a theorem-guided finite eco-genetic model by separating recurrent-mutation relaxation strength from mutation direction. Across 15 preregistered mutation coordinates, we independently reconstructed high-trait sources and performed warning-blind trait-loss calibration. Stage I comprised 3,375 source-reconstruction and projection attempts. Stage II comprised 20,250 calibration attempts across 810 candidate cells. Of 648 candidates with complete five-seed blocks, 322 lay entirely above the preregistered trait-loss band, 242 lay entirely below it, and 84 crossed the band among seeds. No candidate satisfied the requirement that every seed block have trait-loss frequency between 0.30 and 0.70; consequently, no coordinate entered warning validation. These finite-model results show that mutation direction can partition a system into rapid-loss, persistent, and seed-heterogeneous regimes, thereby controlling whether genetic warning can be meaningfully validated. The result does not establish failure of genetic warning. Instead, it identifies warning-validation feasibility as a biological and experimental boundary condition.

## Introduction

Ecological deterioration can remove an interaction-dependent or functional trait before population extinction. Genetic monitoring may therefore be useful when genetic change precedes realised trait loss, but population abundance, allele persistence, genetic diversity, interaction state, and realised trait occupancy are not interchangeable variables.

The predecessor framework established exact and finite-model links among interaction thresholds, fragmentation, local effective size, realised high-trait occupancy, and genetic diversity. Under one independently calibrated symmetric-mutation configuration, baseline-relative diversity erosion preceded observed trait loss. That result was explicitly conditional on one declared closure and one selected deterioration domain.

Here we address a separate boundary condition: recurrent mutation need not be symmetric between high-trait-associated and low-trait-associated allelic states. Holding the contraction strength of the mutation map fixed while changing its equilibrium direction changes the balance of recurrent input and loss without silently changing the rest of the ecological life cycle.

Our primary question is not whether warning always leads or lags. It is whether mutation direction changes (i) the feasibility of a high-trait source, (ii) the probability regime of realised trait loss, and (iii) the existence of a preregistered domain in which warning performance can be evaluated without selecting on warning outcomes.

## Model and mechanism

Let `p` denote the high-trait-associated allele frequency. The recurrent mutation operator is

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

Here `kappa_mu` controls contraction toward the mutation-only equilibrium, whereas `p_mu*` controls direction. The directional transition rates are

\[
u_{L\to H}=\kappa_\mu p_\mu^\ast,
\qquad
u_{H\to L}=\kappa_\mu(1-p_\mu^\ast).
\]

At a local post-mutation threshold `p_c`, the required pre-mutation frequency is

\[
\theta(p_c)=\frac{p_c-\kappa_\mu p_\mu^\ast}{1-\kappa_\mu}.
\]

This algebra predicts that increasing `p_mu*` lowers the pre-mutation frequency required to remain above the high-state boundary. Whether this local mechanism organizes the finite stochastic system is tested rather than assumed.

## Protocol

We evaluated three relaxation strengths (`0.05`, `0.20`, `0.35`) and five mutation equilibria (`0.10`, `0.25`, `0.50`, `0.75`, `0.90`). Selection, migration, finite drift, trait recruitment, source transfer, projection, and trait-loss semantics were inherited from a pinned predecessor commit.

Stage I independently reconstructed sources for every mutation coordinate using three area-reference values, three interaction scalings, five master seeds, and five replicates. Stage II evaluated two horizons and three normalized barrier increases using five fresh calibration seeds and five replicates. Calibration loaded only source eligibility and realised trait-loss endpoints. Diversity, warning times, lead/lag status, and usable lead time were unavailable to selection.

A candidate was eligible only when every seed block had post-baseline trait-loss frequency in `[0.30, 0.70]`. Eligible candidates would have been ranked by distance of pooled loss frequency from `0.50`, followed by horizon, barrier increase, area reference, and interaction scaling. If none were eligible, the protocol required `no_domain_selected` without expanding the candidate family.

## Results

### Independent source reconstruction

Stage I completed all 3,375 planned attempts. The publication analysis will report coordinate-resolved source support, full-state preparation, and projection support with their exact denominators. No predecessor source was treated as qualified evidence for this extension.

### Trait-loss regime separation

Stage II completed all 20,250 planned attempts in 810 resumable batches. A total of 648 candidates had complete five-seed blocks. Across these candidates, 322 had all seed-block trait-loss frequencies above the eligibility band, 242 had all rates below it, and 84 mixed rates across the band.

Low mutation equilibria were dominated by rapid-loss candidates. High mutation equilibria at stronger relaxation were dominated by persistent candidates with little or no realised trait loss. Intermediate transitions included candidates whose pooled rate approached one half but whose seed blocks crossed both sides of the preregistered interval.

### No warning-validation domain under Protocol 002

None of the 648 complete candidates satisfied the all-seed eligibility rule. All 15 mutation coordinates were therefore recorded as `no_domain_selected`, and no Stage III warning validation was run. This outcome is a result of the preregistered decision rule, not a retrospective claim that warning failed.

## Discussion

The central result is that mutation direction altered not only expected trait persistence but also the experimental regime in which warning performance could be assessed. A system with almost certain rapid loss offers little discrimination among warning rules, while a system with almost no loss provides few event pairs. Seed-heterogeneous regimes create a third problem: pooled event frequencies can appear suitable even when the result is not reproducible across seed blocks.

This has three ecological implications. First, mutation or effective state-transition direction can influence functional-trait loss before population extinction. Second, genetic monitoring rules cannot be assumed transferable across genetic closures that generate different event regimes. Third, warning-validation feasibility should be treated as an explicit design outcome rather than hidden by post hoc changes to horizons, thresholds, or parameter ranges.

The result is finite and conditional. `p_mu*` is an effective recurrent-transition equilibrium, not an estimated mutation spectrum for a particular species. The current analysis does not establish a universal rescue effect, nor does it evaluate warning lead time under directional mutation. Instead, it bounds where such evaluation was possible under the declared source and deterioration families.

## Relationship to the predecessor

The predecessor paper and this extension form a companion pair. The predecessor asks when interaction feedback, fragmentation, and genetic change can produce a conditional warning result under a symmetric closure. This paper asks how changing the mutation closure modifies source feasibility, loss-event regimes, and the availability of a warning-validation domain. The predecessor's selected trajectory is context, not evidence for the present numerical claims.

## Data and code availability

All model code, protocols, immutable grid locks, batch workflows, result-selection code, and diagnostic artifacts are maintained in this repository. The pinned predecessor commit is recorded in the protocol and workflow metadata.