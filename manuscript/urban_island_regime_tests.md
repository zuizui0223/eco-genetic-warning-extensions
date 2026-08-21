# Urban and island tests of the eco-genetic regime map

## Purpose

Use urban and island systems as **contrasting empirical tests of the same condition map**, not as decorative applications. The unit of prediction is not "urbanization" or "insularity" itself. It is the combination of effective connectivity, interaction support, reproductive assurance, local population support and disturbance.

A relevant parent-model Type T result already exists for connectivity. In a symmetric two-patch migration step,

`p1'=(1-m)p1+m p2`, `p2'=m p1+(1-m)p2`,

and for `0<m<1/2`,

`|p1'-p2'|=(1-2m)|p1-p2|`.

Thus migration strictly homogenizes nonidentical allele frequencies while conserving the mean. A separate rescue certificate can coexist with that homogenization. Connectivity therefore cannot be represented as a generic "more diversity = better function" axis.

## New finite connectivity result from Phase E

The Phase-E condition experiment fixed the independently reproduced R4 anchor and varied only allele-frequency migration among the four fragmented patches.

- `m=0, 0.025, 0.05` remained **R4-highrep**;
- `m=0.10, 0.20` became **R3-highrep**;
- pooled trait-loss probability changed only modestly (`0.549–0.626` across the five levels);
- relative to isolation, paired loss-status switching increased from 8/91 at `m=0.025` to 25/91 at `m=0.20`;
- both `loss→no loss` and `no loss→loss` occurred at every nonzero migration level.

This adds a finite condition result to the exact homogenisation theorem:

> **effective genetic connectivity can change the reproducibility of functional loss without acting as a simple universal rescue or collapse process.**

The empirical translation is therefore stronger than "connected patches do better." Connectivity may change *which* populations or years cross the functional-loss boundary even when average loss risk changes little.

The current simulator still mixes allele frequencies only. It does not simulate demographic migration, pollen vectors, seed dispersal, recolonisation or trait-bin dispersal.

## 1. Urban systems: fragmentation with variable effective connectivity

Urban habitat patches can be spatially isolated yet biologically connected, or spatially close yet functionally isolated, depending on pollinator movement and species life history.

Two recent empirical patterns make this especially useful for the model:

- direct pollen tracking in isolated urban green spaces detected frequent pollen transfer among patches, including movement across streets and built surfaces;
- specialized-pollinator systems can show strong functional pollen isolation across built urban gaps.

Thus the same urban matrix can generate very different effective migration/interaction regimes.

### Urban regime hypotheses

**U1 — connectivity-rescue regime.** Small urban patches with frequent pollinator-mediated or anthropogenic movement can remain genetically connected even when habitat area is small. These systems should shift away from the most drift-dominated/source-infeasible region.

**U2 — rescue–homogenization trade-off.** Increased movement can support demographic/high-trait persistence while reducing allele-frequency differentiation among patches. A monitoring strategy based on spatial genetic contrast may therefore become less sensitive precisely when connectivity is providing ecological rescue.

**U3 — interaction-loss without immediate diversity loss.** If connectivity or repeated introductions maintain allele diversity while native pollination function deteriorates, genetic diversity can remain relatively high despite impaired ecological function. This directly tests support–diversity decoupling.

**U4 — specialised-pollinator rapid-loss regime.** Plants whose effective pollen movement depends on short-ranging or habitat-sensitive pollinators should enter rapid-loss/source-limited regimes at lower spatial fragmentation than species served by mobile/generalist pollinators.

**U5 — urban heterogeneous frontier.** Mixed urban mosaics, where some patches are connected by pollinators and others are effectively isolated, should be enriched for population/year-heterogeneous event regimes rather than a single monotone urbanization response.

**U6 — connectivity can alter evaluability before warning.** Phase E predicts that increasing effective genetic connection need not greatly change pooled functional-loss frequency to change whether loss is reproducible across comparable populations/years. Empirically, urban networks with similar mean reproductive failure could therefore differ in whether a genetic warning is estimable because connectivity changes among-patch/year event heterogeneity.

### Urban observations needed

At minimum, measure the same distinct layers rather than collapsing them into one urbanization index:

1. patch area and matrix resistance;
2. contemporary pollen/gene flow or pollinator movement;
3. pollinator visitation and successful compatible pollen delivery;
4. realised reproductive/function endpoint;
5. local effective size/genetic diversity through time;
6. among-patch allele-frequency differentiation;
7. disturbance/heat/pollution covariates.

Good empirical designs include paternity assignment, pollen tracking, repeated reproductive-success measurements and temporal genomic monitoring in the same patch network.

## 2. Island systems: isolation with strong colonization and mutualist filters

Island functional biogeography explicitly predicts that isolation filters dispersal, establishment, mutualists and reproductive strategies. Mutualist/pollinator diversity generally decreases with isolation, while generalist pollination, self-compatibility and vegetative reproduction become more common.

At the same time, island isolation does not force one reproductive outcome. Obligate outcrossing can persist on remote islands when a suitable pollination niche is available. This provides a direct analogue of the model result that interaction support can change the regime even under strong spatial isolation.

### Island regime hypotheses

**I1 — mutualist-limited source regime.** Small/remote islands with low pollinator availability should have lower establishment/high-function source feasibility for obligately outcrossing or specialist-pollinated lineages.

**I2 — reproductive-assurance persistence regime.** Self-compatibility, autonomous selfing, vegetative reproduction or highly generalised pollination can maintain demographic persistence after specialist interaction support weakens. Population persistence and the original interaction-dependent function can therefore decouple.

**I3 — stepping-stone rescue–homogenization.** Archipelagic stepping-stone gene flow can rescue low-support local populations while homogenizing allele frequencies across islands. Thus low among-island differentiation need not imply absence of ecological vulnerability; it can be a consequence of the same connectivity that provides rescue.

**I4 — pollination-niche rescue.** Remote islands with a stable effective pollination niche can retain outcrossing/high-function states despite strong geographic isolation, shifting them away from the regime predicted from distance alone.

**I5 — intermediate-isolation warning frontier.** The most promising warning-evaluable systems should not necessarily be the most isolated islands. They should occur where interaction-dependent function is vulnerable enough to be lost, but loss is neither nearly deterministic nor nearly absent across comparable populations/years.

**I6 — connectivity-sensitive reproducibility.** Phase E predicts that stepping-stone genetic connection can change the reproducibility class of functional loss without a large monotone change in mean loss risk. Therefore island distance alone should not define the warning domain; contemporary effective connectivity and interaction support must be measured separately.

### Island observations needed

1. island area and distance/stepping-stone connectivity;
2. colonization/population history where available;
3. pollinator/mutualist richness and realised visitation;
4. breeding system/self-compatibility/reproductive assurance;
5. successful pollen flow and realised reproduction/function;
6. temporal effective size/diversity and among-island differentiation.

An archipelago with repeated populations of the same or closely related lineage is preferable to a cross-species island-mainland contrast because it can separate spatial isolation from breeding-system and interaction differences.

## 3. The urban–island contrast

The useful comparison is:

```text
same apparent patchiness/isolation
        +
variable effective connectivity
        +
variable interaction support
        +
variable reproductive assurance
        ↓
different eco-genetic regimes
```

Cities and islands therefore test complementary parts of the model:

- **urban systems** are strongest for showing that spatial fragmentation does not uniquely determine gene flow or genetic diversity;
- **island systems** are strongest for showing that geographic isolation interacts with mutualist availability and reproductive strategy to filter establishment and persistence;
- both can test the predicted coexistence of connectivity-mediated rescue, homogenization and altered functional-loss reproducibility.

A successful empirical translation would classify populations first by source/functional-loss regime and its reproducibility, and only then ask whether a genetic warning is observable. That preserves the same logic as the warning-blind simulation program.

## 4. Concrete empirical design

The cleanest field test is not "city versus island." It is a replicated network design in which the same biological lineage spans gradients of:

- local patch/island support;
- realised interaction/pollination support;
- effective gene flow/connectivity;
- reproductive assurance;
- repeated functional success/failure through time.

The primary response should first be **event-regime class**: persistent, rapid-loss, heterogeneous or reproducible intermediate-risk. Genetic warning is a second-stage analysis only for systems that occupy the reproducible intermediate-risk class.

This directly tests the study's core methodological prediction that warning estimability is a biological property of the event-generating regime rather than an automatic property of the measured genetic statistic.

## Literature and theory anchors

- Parent Type T migration trade-off: `causal_model/canonical_h3_migration_tradeoff.py` at the pinned parent scientific commit — exact two-patch allelic homogenization plus separate rescue certificate.
- Phase-E finite condition result: `artifacts/migration_condition/phase_e_summary.json` and `manuscript/migration_condition_phase_e_results.md`.
- Miles et al. (2019), *Molecular Ecology*, doi:10.1111/mec.15221 — urbanization can either restrict or facilitate dispersal; quantitative review found only weak average within-population diversity loss and no consistent increase in differentiation.
- Youngsteadt & Keighron (2023), *Annual Review of Ecology, Evolution, and Systematics*, doi:10.1146/annurev-ecolsys-102221-044616 — urban pollination shows a global negative signal but strong heterogeneity; pollen movement remains difficult to predict.
- Pollinator-mediated connectivity in fragmented urban green spaces (2024), *Acta Oecologica* 123:103985, doi:10.1016/j.actao.2024.103985 — direct evidence of pollen movement among isolated urban green spaces.
- Schrader et al. (2021), *Biological Reviews*, doi:10.1111/brv.12782 — functional island-biogeography hypotheses linking isolation to mutualist diversity, pollination generalism and self-compatibility.
- Grossenbacher et al. (2017), *New Phytologist*, doi:10.1111/nph.14534 — self-compatibility over-represented on islands (66% versus 41% in the sampled families).
- Xu et al. (2018), *Scientific Reports* 8:13765, doi:10.1038/s41598-018-32143-5 — an obligately outcrossing island plant can persist when an effective pollination niche is available.
