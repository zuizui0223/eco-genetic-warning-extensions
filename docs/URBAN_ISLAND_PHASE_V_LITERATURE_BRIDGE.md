# Literature bridge: urban/island fragmentation routes and Phase-V state sufficiency

## Scope

Urban and island systems are **not ecological equivalents**. They are contrasting causal routes for testing whether different fragmentation mechanisms can converge on the same operational **interaction-mediated functional-fragmentation regime**.

Phase V is now complete. It did not simulate cities or islands. It tested a necessary mathematical condition for cross-system convergence: whether matching layer-wise snapshot marginals is enough to define the same dynamical state.

## Literature-derived causal decomposition

### Landscape structure is not one fragmentation scalar

Benitez et al. (2025) argue for a functional/connectivity-based view of fragmentation because vegetation geometry alone cannot represent all barriers. Fletcher et al. (2026) experimentally separated habitat loss, fragmentation and surrounding matrix quality and found important independent and interactive demographic effects. Olhnuud et al. (2025) and Gama et al. (2025) further show that habitat amount, species turnover and network responses need not track fragmentation per se in one common direction.

**Consequence:** habitat amount, configuration, matrix quality and movement remain separate causal inputs.

### Interaction structure and function are not reducible to richness

Hiraiwa & Ushimaru (2024) found pollinator functional diversity, rather than species diversity itself, associated with community-wide trait matching and pollination function across 40 coastal networks. Hackett et al. (2024) showed landscape-scale interaction complementarity, evenness, robustness and pollination success that could not be recovered by simply summing component habitat webs. Ward et al. (2026) and Dominguez-Garcia et al. (2026) emphasize temporal rewiring and interaction-strength change as dynamic components of persistence and resilience.

**Consequence:** a functional state must retain interaction identity/strength and relevant joint organization, not only species counts or a scalar support score.

### Urban route: interaction turnover can decouple from gene flow

Marcacci et al. (2023) found interaction composition across Bengaluru farms to vary more with season and local urbanization intensity than with geographic distance, with rewiring and plant turnover major components. Hardion et al. (2026) review evidence that urban plant populations often retain genetic diversity comparable with non-urban populations and that long-distance and anthropogenic dispersal can maintain gene flow. Alaasam et al. (2026) likewise describe cities as heterogeneous mosaics connected by human infrastructure rather than isolated genetic islands.

**Consequence:** urban demographic/genetic support can remain high while local interaction support is reorganised.

### Island route: turnover, local interactions, mutualist filters and reproductive assurance

Traveset et al. (2016) found oceanic-island pollination networks smaller and lower in interaction diversity than mainland/continental-island networks, while area did not explain every network metric. Vitali et al. (2024) showed that Canary Island spatial network structure reflects both regional species turnover and local interaction structure. Delavaux et al. (2024) identifies mutualist association as a candidate island-biogeographic filter beyond classic area/isolation, but this global result has a published critique/response and is not used here as a universal law. Reproductive assurance is a further process that can decouple demographic persistence from the focal interaction-dependent function.

**Consequence:** island distance or area alone cannot define the functional-loss regime.

### Genetic state is not a universal proxy for function

Whitlock (2014) separates adaptive/genotypic from neutral molecular diversity in ecological relationships. Miguel-Penaloza et al. (2023) found no consistent overall fine-scale genetic-structure difference among fragmented, degraded and undisturbed plant habitats, with strong heterogeneity and dispersal effects. Peled et al. (2026) show that landscape-fragmentation trajectories can generate different genetic monitoring trajectories before rapid genetic transitions.

**Consequence:** neutral diversity, adaptive/functional state, interaction support and realised function must remain distinct measurements.

## Phase V result

Aligned and anti-aligned four-patch states were matched for:

- habitat area and census;
- interaction-state multiset;
- allele-frequency multiset;
- realised high-trait-mass multiset;
- complete global trait-bin totals;
- `H_alpha`, `H_gamma` and `FST`.

Only the cross-patch alignment between interaction support and the paired genetic/trait-support bundle differed.

The exact next interaction state nevertheless changed:

- q-by-bundle covariance `+.025` versus `-.025`;
- maximum patchwise generation-1 q difference **`.2543`**.

Therefore the declared layer-wise marginals are **not a sufficient Markov state** for the local nonlinear feedback dynamics.

The stronger long-horizon claim was not supported. Over one preregistered 60-generation deterioration schedule:

- aligned loss: `339/500 = .678`;
- anti-aligned loss: `361/500 = .722`;
- paired McNemar `p=.143`.

Phase V therefore establishes a **state-representation boundary**, not a directional alignment-risk effect.

## Refined convergence hypothesis

The cross-system hypothesis is now:

> **Different fragmentation mechanisms converge on one operational functional-fragmentation regime only if their transition-relevant joint state is sufficiently equivalent and their downstream functional transition/loss dynamics are invariant to causal-route label.**

Matching independent layer means, diversity indices or marginal distributions is not enough. This is an exact consequence of the declared local feedback whenever multiple layers enter the same local transition rule and their patchwise pairing is discarded.

## Empirical translation

An urban/island comparison should retain at minimum:

1. habitat amount/configuration and matrix quality;
2. patch-specific population/demographic state;
3. patch-specific realised interaction strength and partner identity;
4. partner functional diversity, contribution evenness, turnover and rewiring;
5. patch-specific realised functional endpoint;
6. pollen, seed/propagule, demographic and partner movement as separate processes;
7. reproductive assurance or alternative functional routes;
8. neutral and, where available, adaptive/functional genetic state;
9. **cross-layer joint alignment/covariance or another transition-sufficient joint representation**.

Convergence should then be tested by **transition invariance/transport**: after conditioning on the joint state, does route identity (`urban`, `island`, or finer mechanism labels) still improve prediction of the next functional state or loss process? A non-significant city-versus-island coefficient alone is not sufficient evidence of convergence.

## Practical interpretation

The framework suggests looking for **mismatch hotspots** rather than only “high fragmentation”:

- high census/genetic support but weak interaction/function support;
- high habitat amount but poor process-specific matrix connectivity;
- strong local interaction support but low reproductive assurance or propagule connectivity;
- high species richness but low functional trait matching.

Management then targets the process-specific bottleneck rather than one generic fragmentation, network or diversity score.

## Provenance

Phase V scientific run `32636913615`; artifact `9492558602`; digest `sha256:a5754ab2d54dea868a72fed582a9862cbc88b83510e1cf81e0a872f56b70a1bd`. Exact finite result is locked in `artifacts/cross_layer_alignment/phase_v_locked_summary.json`; the general state-sufficiency proposition is in `docs/CROSS_LAYER_ALIGNMENT_STATE_SUFFICIENCY_THEOREM.md`.

## Core references

- Alaasam, V. et al. (2026). *Nature Reviews Biodiversity* 2:170–185. doi:10.1038/s44358-026-00138-0.
- Benitez, L.M. et al. (2025). *Trends in Ecology & Evolution* 40:27–36. doi:10.1016/j.tree.2024.09.004.
- Delavaux, C.S. et al. (2024). *Nature* 627:335–339. doi:10.1038/s41586-024-07110-y; interpret with subsequent critique/response.
- Dominguez-Garcia, V. et al. (2026). *Ecology Letters* 29:e70293. doi:10.1111/ele.70293.
- Fletcher, R.J. Jr. et al. (2026). *Nature Ecology & Evolution* 10:1265–1272. doi:10.1038/s41559-026-03095-1.
- Gama, M. et al. (2025). *Biological Conservation* 311:111419. doi:10.1016/j.biocon.2025.111419.
- Hackett, T.D. et al. (2024). *Nature* 633:114–119. doi:10.1038/s41586-024-07825-y.
- Hardion, L., Sotillo, A. & Muratet, A. (2026). *Perspectives in Plant Ecology, Evolution and Systematics* 70:125920. doi:10.1016/j.ppees.2025.125920.
- Hiraiwa, M.K. & Ushimaru, A. (2024). *Functional Ecology* 38:1296–1308. doi:10.1111/1365-2435.14527.
- Marcacci, G. et al. (2023). *Ecology Letters* 26:1951–1962. doi:10.1111/ele.14324.
- Miguel-Penaloza, A. et al. (2023). *AoB PLANTS* 15:plad019. doi:10.1093/aobpla/plad019.
- Olhnuud, A. et al. (2025). *Journal of Applied Ecology* 62:2502–2514. doi:10.1111/1365-2664.70161.
- Peled, O., Kim, J. & Greenbaum, G. (2026). *PNAS* 123:e2515033123. doi:10.1073/pnas.2515033123.
- Traveset, A. et al. (2016). *Global Ecology and Biogeography* 25:880–890. doi:10.1111/geb.12362.
- Vitali, A. et al. (2024). *Journal of Animal Ecology*. doi:10.1111/1365-2656.14174.
- Ward, C.A. et al. (2026). *Nature Reviews Biodiversity* 2:355–369. doi:10.1038/s44358-026-00159-9.
- Whitlock, R. (2014). *Journal of Ecology* 102:857–872. doi:10.1111/1365-2745.12240.
