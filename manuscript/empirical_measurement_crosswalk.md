# Empirical measurement crosswalk for functional-fragmentation conditions

## Purpose

A natural functional-fragmentation condition is not identified by a habitat label. It is identified by a **measured joint state before an outcome window** and by the realised functional trajectory that follows.

This crosswalk separates two questions that are easy to conflate:

1. **Is a coordinate measured somewhere in the study programme?**
2. **Is it measured in the same population/site-year as the other coordinates and the future functional outcome?**

Only the second supports a strict empirical state-sufficiency test.

## State coordinates

| code | ecological meaning | example field measurement |
|---|---|---|
| `D` | demographic / local resource support | census, flowering density, floral resources, local effective size |
| `I` | realised interaction support | visitation × effectiveness, compatible pollen receipt, interaction strength |
| `T` | functional / trait state | trait matching, morph balance, partner functional diversity |
| `C` | process-specific movement | pollen flow, seed/propagule flow, demographic movement, partner movement |
| `R` | compensatory route | selfing, reproductive assurance, alternative partners, rewiring |
| `G` | genetic / mating state | heterozygosity, inbreeding, donor diversity, offspring genetics, functional alleles |
| `F` | realised ecological function | pollination rate, seed/fruit set, dispersal effectiveness, recruitment |
| `M` | ecological memory / history | prior disturbance, colonisation history, age/seed-bank/resource legacy |
| `A` | joint spatial alignment | co-location/covariance among `D/I/T/C/G/F`, not separate marginal means |

## Cross-system measurement matrix

Legend: `●` = directly measured in the cited design/programme; `◐` = partial/proxy or measured in a companion study rather than fully synchronized; `○` = major missing axis for the proposed state test.

| natural system | D | I | T | C | R | G | F | M | A | synchronization / immediate use |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Montpellier *Crepis sancta* | ● | ● | ◐ | ● | ● | ● | ● | ● | ◐ | **Near-complete programme, not synchronized.** Interaction/seed-set and parentage/genetics come from different studies/years. Strong process anchor; needs same-patch-year resurvey for strict sufficiency. |
| Miyake-jima *Camellia–Zosterops* | ● | ● | ◐ | ● | ◐ | ● | ● | ● | ◐ | **Near-complete compensation system.** Disturbance, resources, pollination, movement and offspring genetics measured across the same island gradient, but study components span related campaigns/years. |
| Honshu–Izu coastal 40 networks | ◐ | ● | ● | ○ | ○ | ○ | ● | ◐ | ◐ | **Immediate ecological partial-state test.** `I/T/F + season/geography` are matched across 40 site-seasons; add focal-plant genetics/parentage for full eco-genetic state. |
| Zurich 24 garden phytometers | ● | ● | ● | ○ | ○ | ○ | ● | ◐ | ◐ | **Immediate urban ecological partial-state test.** Raw design can test whether urban intensity adds prediction beyond `I/T`; standardized plants intentionally remove natural plant `G`. |
| Chicago *Penstemon hirsutus* green roofs | ● | ◐ | ◐ | ● | ● | ● | ● | ◐ | ◐ | **Connectivity/function-rich partial state.** Add standardized pollinator identity, visitation and effectiveness per roof. |
| Perth *Conospermum undulatum* fragments | ● | ◐ | ◐ | ● | ◐ | ● | ● | ◐ | ◐ | **Interaction-vector / pollen-flow candidate.** Contemporary paternity and genetics are strong; align detailed visitation/effectiveness with the same reproductive windows. |
| fragmented Dutch *Primula elatior* | ● | ● | ● | ◐ | ● | ● | ● | ◐ | ◐ | **Strong terrestrial bridge.** Population size, genetics, morph balance, landscape, pollinators and seed production are jointly informative outside the urban/island framing. |

The matrix is a **measurement registry**, not an evidence score. A system with fewer filled cells can still be the best test of one causal coordinate.

## Two quantitative natural anchor conditions

### Anchor U-LIM — uncompensated interaction limitation (*Crepis*)

Observed pattern:

`D_local ↓ -> I_realised ↓ -> F_reproduction ↓`

with

`R_self` weak/incomplete and `C_pollen/C_seed` nonzero but heterogeneous.

Published anchors include pollinator presence of roughly 10% at low density versus 80% at high density, fertilised ovules of roughly 20% versus 80%, and parentage evidence for restricted local dispersal plus substantial external immigration in companion urban networks.

**Identification rule in nature:** call this pattern a candidate interaction-limited condition only when reduced local support, reduced realised interaction and reduced direct function are measured in the same causal sequence and no measured alternative route explains away the functional decline. Do not use a universal density threshold.

### Anchor I-COMP — movement-compensated local fragmentation (Miyake-jima)

Observed pattern:

`D_local ↓` together with `C_partner ↑ / C_pollen ↑`

while

`F_pollination` is maintained/enhanced and `G_offspring` does not collapse.

Published anchors include flower density from 21 to 2,544 flowers ha⁻¹, *Zosterops* home ranges of approximately 0.26 versus 1.97 ha in contrasted sites, pollen immigration of 0–33.8%, donor diversity of about 0.62–0.96, and higher pollination in heavily damaged sites despite lower pollinator density.

**Identification rule in nature:** call this a candidate compensation condition only when movement/alternative-route variables change in the compensating direction and direct function is measured. Low local resource density plus stable function without a measured compensation process is not enough.

## What counts as the same functional-fragmentation regime

Two natural systems should not be matched by raw units such as flowers ha⁻¹, kilometres of isolation or heterozygosity. Cross-system convergence is a **predictive equivalence claim**:

`future functional trajectory ⟂ fragmentation origin/history | measured joint state at t`.

A practical workflow is:

1. define the focal function and prediction window;
2. measure the candidate state before the outcome;
3. compress each ecological coordinate only with predeclared, biologically interpretable summaries;
4. preserve spatial alignment/covariance across patches;
5. fit the future-function model without habitat origin;
6. add origin/history last and assess held-out prediction/calibration;
7. if origin/history helps, identify the missing process/memory coordinate.

The target is the **smallest sufficient measured state**, not the largest covariate set.

## Existing-data versus new-measurement frontier

### Can be tested now as partial state

- **E1 Honshu–Izu:** ecological residual-origin test using functional diversity, trait matching, season and direct pollination success; no matched genetics.
- **E2 Zurich:** urban residual-context test using local ecological context, guild-/trait-specific interaction support and direct fruit/seed set; no natural plant genetics.
- **E3 *Crepis*:** process audit can be done from existing open parentage/dispersal data, but full state cannot be synchronized retrospectively from the separate 2006 and 2013 studies.
- **E4 Miyake:** published tables permit a quantitative compensation-axis audit; a strict prospective sufficiency test needs repeated synchronized site-years.

### Highest-value new measurement

The largest common gap is **interaction + function + genetics/connectivity measured in the same population-years**. The most efficient additions are:

1. genotype focal plants and offspring/pollen pools in the existing Honshu–Izu repeated network design;
2. resurvey *Crepis* patches with interaction/function and parentage in the same season;
3. repeat Miyake site-years with movement, pollen flow, reproduction and offspring genetics synchronized;
4. add direct pollinator observation/effectiveness to Chicago roofs where paternity and reproduction are already available.

## Interpretation boundary

The model's state variables are not field variables by fiat. `D/I/T/C/R/G/F/M/A` are an empirical **search basis** assembled from measured mechanisms in natural systems. Any coordinate can be removed only if predictive sufficiency survives its removal; any residual origin/history signal is evidence to search for an omitted state or ecological memory variable.
