# Urban and island tests of interaction-mediated functional fragmentation

## Central question

Urban and island systems are **contrasting causal routes through the same condition map, not ecological equivalents**.

> **Do different fragmentation mechanisms converge on the same future-relevant functional-fragmentation regime?**

The word *future-relevant* is essential. Matching habitat category, occupancy, mean interaction, mean genetic diversity, or even separate marginal distributions is not enough if hidden spatial alignment or ecological memory still changes subsequent functional loss.

Because `functional fragmentation` is already used in landscape ecology for organism-centred functional connectivity, manuscript prose should use **interaction-mediated functional fragmentation** for the focal process here: weakening or destabilisation of the biotic interaction support required to maintain realised ecological function while focal populations or patches may remain present.

## What the completed model programme establishes

### 1. Function can be lost before population disappearance

The parent model establishes a high-function interaction-supported state and shows that equal isolation of the same prepared state lowers interaction, local effective size and realised high-trait mass before demographic disappearance. The fixed-area 1–16-patch sensitivity shows that the first split already produces most of the interaction/Ne disruption.

### 2. Recurrent turnover changes source feasibility and functional-loss incidence

The extension separates source feasibility from post-establishment loss. The high-precision recurrent-turnover frontier changes pooled functional-loss incidence from about `.682` at `p_star=.325` to `.273` at `.400`, with no detected excess block heterogeneity at the tested frontier coordinates. Historical R1–R4 labels are therefore calibration screens rather than biological regimes.

### 3. Connectivity is operator- and ensemble-dependent, not a universal rescue axis

The historical allele-only Phase-M `m=.10` equal-rate signal (`p=.0205`) did not reproduce in one preregistered fresh Phase-U ensemble (`m=.10 p=.745`; McNemar `p=.694`). It also did not port to whole-individual dispersal (Phase R) or pollen-only paternal gene flow (Phase S) in the historical seed family.

**Current claim ceiling:** no robust portable connectivity heterogeneity effect was established across the tested seed ensembles and biological operators. `migration_rate` remains allele-frequency mixing only and must not be translated directly into demographic, pollen, seed, pollinator or recolonisation movement.

### 4. Aggregate and partner perturbations do not define a universal network boundary

High-precision `kappa=3.0,4.5,6.0` conditions remained intermediate and block-homogeneous. Reduced-form partner loss and Phase-T matched-expected-support temporal partner variability changed some trajectory identities but produced no detected population-level incidence, block-heterogeneity or paired marginal-risk effect. The preregistered adaptive-rewiring gate stayed closed.

These are bounded negative results, not evidence that real partner identity, functional diversity or rewiring are irrelevant.

### 5. Genetic warning is downstream and conditional

Only after the loss process was fixed warning-blind did baseline-relative `H_alpha/H_gamma` erosion precede observed losses in one calibrated benchmark. Absolute thresholds were not robust, and warning behaviour was not fully portable across independently calibrated domains.

The warning result is therefore not a universal genetic threshold. It is a property of a specified eco-genetic loss-generating domain.

## New state-sufficiency audit

The parent repository now contains a prospective state-sufficiency audit (`eco-genetic-criticality` PR #70) that sharpens what *convergence on the same regime* can mean.

### Full-state sufficiency under the declared closure

The finite simulator is Markov in its explicit state—patch population, interaction state, high-associated allele frequency and realised trait-bin state—together with the fixed future forcing and stochastic law. Under this model closure, two different histories that arrive at exactly the same full state have the same future trajectory distribution. With the same RNG seed they produce the same realised trajectory.

This is a **model theorem**, not a claim that real ecological systems have no memory. Any omitted ecological memory variable would need to be added to the state.

### Coarse-state insufficiency

A constructive two-patch counterexample holds constant:

- patch and total census;
- the marginal distribution and weighted mean of interaction state;
- the marginal distribution and weighted mean of allele frequency;
- `H_alpha`, `H_gamma`, `F_ST`;
- realised trait state.

Only patchwise interaction–genetic alignment changes. One state has high interaction aligned with high allele support; the other anti-aligns them. Because the interaction update is local, the next interaction field differs despite all the above coarse summaries being identical.

**Consequence:** an operational functional-fragmentation regime cannot be defined only by averages, occupancy, genetic diversity, or separate marginals. It must retain the future-relevant **joint spatial state**, or use a lower-dimensional statistic whose predictive sufficiency has been demonstrated.

## Literature synthesis: why urban and island routes should differ upstream

### Urban route — ecological interaction and genetic connectivity can decouple

Urban landscapes are heterogeneous mosaics rather than simple oceanic islands. The 2026 urban eco-evolution review explicitly notes both island-like features and distinctive human-connected mosaic structure. A 2026 review of urban plant population genetics reports that plant genetic diversity is often comparable to non-urban populations and that gene flow can remain high despite spatial fragmentation, including through animal and anthropogenic dispersal.

Plant–pollinator interactions can nevertheless turn over strongly. In Bengaluru, interaction composition differed more with season and local urbanisation intensity than with spatial distance; environmental filtering, plant turnover and rewiring dominated the pattern. This creates a plausible urban route in which neutral genetic connectivity remains substantial while local realised interaction support changes.

**Urban implication:** neutral genetic isolation is not a safe proxy for interaction-mediated functional isolation.

### Island route — colonisation, mutualist filtering and reproductive assurance matter

Oceanic-island pollination networks are often smaller and lower in interaction diversity than mainland and continental-island networks, but island area and isolation do not explain every network property. Recent island comparisons continue to show strong differences in species composition and network structure between oceanic and continental island communities.

Global island biogeography also identifies mutualist availability as a serious candidate establishment filter: plants associated with animal pollinators or microbial mutualists are disproportionately underrepresented on oceanic islands, although this global effect should be interpreted with its published critique/response. Reproductive assurance provides another route by which demographic persistence can become decoupled from the original interaction-dependent function.

**Island implication:** geographic isolation alone does not specify the functional-loss regime; mutualist availability, interaction identity, functional redundancy, reproductive assurance and stepping-stone movement are separate coordinates.

### Fragmentation literature rejects one universal structural axis

A 2025 global meta-analysis of 80 insect-pollinator studies found negative fragmentation associations but identified reduced habitat area as the strongest component. A 2025 plant–vertebrate pollination-network study similarly found habitat loss, rather than fragmentation per se, associated with richness and structural change; roughly 90% of interaction dissimilarity across strongly contrasting landscapes came from species turnover, while rewiring mattered more where species pools overlapped.

The implication is direct: patch count or isolation alone cannot define interaction-mediated functional fragmentation.

### Dynamic interaction literature shows why hidden joint state matters

Recent network work emphasizes that interaction rewiring is dynamic and can alter resilience. An eight-year, 12-site study found that most year-to-year interaction changes arose from species turnover, while rewiring among persistent species was especially important for pollinator persistence. A 2026 review likewise treats changes in topology and interaction strength as central resilience mechanisms.

This literature supports the state-sufficiency result: partner identity, interaction strength and their spatial/temporal alignment can carry predictive information that is invisible in simple richness or mean-support summaries.

## Revised convergence hypothesis

The correct cross-system hypothesis is not:

> cities and islands have the same fragmentation effect.

Nor is it:

> systems with the same mean interaction or genetic diversity occupy the same regime.

It is:

> **Distinct fragmentation mechanisms converge only if, after conditioning on a candidate future-relevant joint functional state, system origin and fragmentation history no longer add predictive information about subsequent realised functional loss.**

This gives an explicit falsification rule.

### Convergence test

For repeated populations or population-years:

1. measure candidate state variables before the outcome window;
2. estimate subsequent realised functional loss independently of genetic warning variables;
3. fit a common loss model using the candidate regime state;
4. add `urban/island` origin and fragmentation-history terms;
5. test whether those origin/history terms improve out-of-sample prediction or alter calibrated loss probabilities.

- **If origin/history adds no information:** the candidate state is sufficient at the tested scale, supporting convergence.
- **If origin/history still predicts loss:** the proposed regime is incomplete; add the missing process or memory variable rather than declaring cities and islands intrinsically different regimes.

This is stronger than a category comparison because it asks whether two systems become dynamically equivalent after conditioning on state.

## Minimum candidate regime state for empirical work

The current model and literature jointly imply retaining at least:

1. **spatial support** — habitat amount, configuration and matrix resistance/quality;
2. **local demographic state** — abundance/density and effective size where estimable;
3. **realised interaction support** — interaction/visitation strength and partner identity;
4. **interaction architecture** — partner functional diversity, contribution evenness, specialisation, turnover and rewiring;
5. **joint spatial alignment** — whether high demographic/genetic/trait support occurs in the same patches as high interaction support;
6. **biological connectivity by process** — pollen, seed/propagule, demographic and partner movement separately;
7. **alternative functional routes** — reproductive assurance or compensatory partners;
8. **realised function through time** — compatible pollen delivery, seed set, dispersal effectiveness or another focal endpoint;
9. **genetic state through time** — neutral and adaptive/functional information distinguished where possible;
10. **history/memory candidates** — prior disturbance, age structure, persistent soil/seed-bank/epigenetic or interaction legacies when biologically plausible.

The list is not a claim that all ten are always necessary. The empirical goal is to find the smallest state representation for which origin/history ceases to improve future functional-loss prediction.

## Concrete empirical interpretation of the present results

The current model already yields four practical implications.

**First, persistence is not function.** Similar occupancy can conceal very different realised interaction support and functional performance.

**Second, establishment and deterioration are separate filters.** Urban co-occurrence/interaction filtering and island colonisation/mutualist filtering may primarily alter whether a high-function state can be established, rather than the subsequent loss probability.

**Third, connectivity must be process-specific.** Genetic connectivity, whole-organism movement, pollen flow and partner movement cannot be collapsed into one scalar without validation.

**Fourth, monitoring must preserve joint spatial structure.** Averaging interaction and genetic variables across sites can erase the alignment information that determines local feedback and future functional state even when standard diversity summaries are unchanged.

## Manuscript-level synthesis

The sharper conceptual contribution is therefore:

> **Fragmentation does not define functional risk by geometry alone. Different fragmentation mechanisms can become dynamically equivalent only when they produce the same future-relevant joint ecological state. Genetic warning is interpretable only downstream of that state-defined loss process.**

This connects landscape fragmentation, ecological-network dynamics and conservation genetics without asserting that urban and island systems are already equivalent.

## Key references

- Alaasam, V. et al. (2026). Eco-evolutionary dynamics shaping biodiversity in the urban mosaic. *Nature Reviews Biodiversity* 2:170–185. doi:10.1038/s44358-026-00138-0.
- Hardion, L., Sotillo, A. & Muratet, A. (2026). Urban plant population genetics: A review. *Perspectives in Plant Ecology, Evolution and Systematics* 70:125920. doi:10.1016/j.ppees.2025.125920.
- Marcacci, G. et al. (2023). Urbanization alters the spatiotemporal dynamics of plant–pollinator networks in a tropical megacity. *Ecology Letters*. doi:10.1111/ele.14324.
- Olhnuud, A. et al. (2025). Responses of insect pollinators to habitat fragmentation: A global meta-analysis. *Journal of Applied Ecology* 62:2502–2514. doi:10.1111/1365-2664.70161.
- Gama, M. et al. (2025). Habitat loss, not fragmentation per se, drives structural changes and species turnover in plant–vertebrate pollinator networks. *Biological Conservation* 311:111419. doi:10.1016/j.biocon.2025.111419.
- Traveset, A. et al. (2016). Global patterns of mainland and insular pollination networks. *Global Ecology and Biogeography*. doi:10.1111/geb.12362.
- Wang, X.-P. et al. (2025). Differences in plant–pollinator network structure and pollinator importance between a continental and an oceanic island community. *Biotropica* 57:e70027. doi:10.1111/btp.70027.
- Delavaux, C.S. et al. (2024). Mutualisms weaken the latitudinal diversity gradient among oceanic islands. *Nature* 627:335–339. doi:10.1038/s41586-024-07110-y.
- Hiraiwa, M.K. & Ushimaru, A. (2024). Loss of functional diversity rather than species diversity of pollinators decreases community-wide trait matching and pollination function. *Functional Ecology* 38:1296–1308. doi:10.1111/1365-2435.14527.
- Domínguez-Garcia, V. et al. (2026). Plant–pollinator interaction rewiring boosts year-to-year community persistence. *Ecology Letters*. doi:10.1111/ele.70293.
- Ward, C.A. et al. (2026). The rewiring of ecological networks in a variable world. *Nature Reviews Biodiversity* 2:355–369. doi:10.1038/s44358-026-00159-9.
- Marjakangas, E.-L., Dalsgaard, B. & Ordonez, A. (2025). Fundamental interaction niches: towards a functional understanding of ecological networks' resilience. *Ecology Letters* 28:e70146. doi:10.1111/ele.70146.
- Peled, O., Kim, J. & Greenbaum, G. (2026). Network-based genetic monitoring of landscape fragmentation. *PNAS* 123:e2515033123. doi:10.1073/pnas.2515033123.
