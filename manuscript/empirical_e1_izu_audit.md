# E1 empirical audit — Honshu–Izu coastal interaction–function state

## Status

This is a **secondary audit of the published results and declared open-data design** of Hiraiwa & Ushimaru (2024), *Functional Ecology* 38:1296–1308, DOI `10.1111/1365-2435.14527`. The paper states that data and code are archived at Figshare `10.6084/m9.figshare.25025000.v1`.

It is not presented as a new refit of the archived network data. The purpose is to identify which **measured ecological conditions**, rather than the category `island`, are already supported as function-relevant in a natural island–mainland system and to specify the exact residual-origin test required by the state-sufficiency hypothesis.

## Why this system is unusually informative

The study analysed **40 spatiotemporally variable coastal plant–pollinator networks (8 sites × 5 seasons)** spanning Japanese continental and oceanic islands. It simultaneously quantified:

- pollinator species richness and conventional diversity;
- pollinator functional diversity, including Rao-type functional diversity `FD_Q` and functional evenness `FEve`;
- community-level pollinator and plant functional generality;
- proboscis–corolla trait matching;
- pollination success of focal plant species;
- mainland/island geography and distance from the mainland;
- repeated seasonal networks.

This is much closer to the present theory than a generic island–mainland comparison because the proposed interaction state `I/T` and direct realised function `F` were both measured.

The study does **not** include matched focal-population plant genetics, parentage-based pollen/seed connectivity, reproductive assurance, or long-term population-history variables for the same 40 networks. It is therefore an **ecological partial-state test**, not a complete `D/I/T/G/C/R/F/M` test.

## Empirically recovered condition chain

### A. Geography changes several upstream network coordinates

The published best models included distance from the mainland for pollinator species richness, `FEve`, `FD_Q` and community-level trait matching; these values decreased with increasing distance from the main island. Season also entered best models for several diversity and functional-generality metrics.

Thus island geography is a real upstream filter in this system, but it does not identify which downstream coordinate is functionally decisive.

### B. Functional diversity, not species diversity, predicts trait matching

The published best model for community-level trait matching included **functional-diversity metrics (`FEve` and `FD_Q`) rather than pollinator species diversity**. The species-level trait-matching analysis likewise retained `FD_Q` as the key predictor.

Low `FD_Q` in this system corresponds in part to low abundance of long-tongued pollinators. Functionally similar species counts therefore cannot substitute for the trait composition of the interacting pollinator pool.

### C. Trait matching predicts realised pollination function

The study reports that lower community-level trait matching reduced community-level plant pollination success, with the effect applying across flower morphologies. Its overall conclusion is that loss of pollinator functional diversity, rather than species diversity, was the principal measured factor associated with pollination functional loss in these networks.

This provides a natural empirical chain:

`island geography / season -> pollinator functional state -> flower–pollinator trait matching -> realised pollination function`

The arrows summarise the published model sequence; they are **not** a new causal mediation analysis.

## Condition recovered from nature

For this system, the most defensible candidate ecological state is not `island distance` or `pollinator richness`. It is a joint state containing at least:

1. **functional partner composition** — especially `FD_Q` / representation of long-tongued pollinators;
2. **interaction–trait alignment** — community/species-level proboscis–corolla matching;
3. **seasonal state** — because several network metrics vary through the five surveys;
4. **direct realised function** — pollen receipt / pollination-success endpoint used for each focal plant.

This is an empirical analogue of the model result that marginal summaries can miss future-relevant interaction structure.

## What the published analysis does not yet prove

The paper establishes that geography is associated with upstream diversity/trait-matching coordinates and that functional diversity / trait matching are associated with pollination function. It does **not**, from the results audited here, establish the strict state-sufficiency statement:

> after conditioning on functional diversity, trait matching and season, mainland/island origin or distance contains no residual predictive information about realised function.

That residual-origin claim requires a direct joint predictive comparison and should not be inferred from variable-selection results in separate models.

## Exact next empirical convergence test

Using the archived 40-network data, compare models at the network / focal-plant level while respecting repeated site and season structure:

- `E1-M0`: species richness + season + basic sampling/context terms;
- `E1-M1`: `M0 + FD_Q + FEve + functional generality + trait matching`;
- `E1-M2`: `M1 + mainland/island origin and/or distance from mainland`;
- `E1-M3`: if needed, interactions between geography and the functional state, evaluated prospectively rather than selected to obtain significance.

Primary comparison:

**Does `E1-M2` improve held-out prediction/calibration of pollination success over `E1-M1` when whole sites or site-seasons are held out?**

Interpretation:

- no meaningful improvement: supports ecological-state convergence at the tested scale;
- improvement: the candidate `I/T` state is incomplete and geography is retaining information about an unmeasured process, such as partner movement, resource context, reproductive assurance or history;
- strong site/season residuals: treat them as clues to missing state variables rather than as nuisance variation to average away.

## Urban–island connection after E1 and E2

The Izu and Zurich systems expose complementary parts of the same idea.

- **Izu:** a coarse island-distance/species-richness description is replaced by functional partner diversity and trait matching as measured function-relevant conditions.
- **Zurich:** a coarse urban-intensity description has plant/function-specific effects, while the guilds associated with fruit/seed set differ among focal plants.

Neither system alone proves full cross-system convergence. Together they show empirically why the state must retain **interaction identity, functional traits and focal function**, rather than treating `urbanisation`, `isolation` or total partner richness as the regime.

## Missing axes for a decisive full test

The key missing layer in Izu is the same one that would most strongly connect the present theory to conservation genetics:

- focal-plant population and offspring genotypes;
- pollen-mediated connectivity / donor diversity;
- seed or propagule connectivity where relevant;
- breeding system / autonomous reproductive assurance;
- repeated direct function measured in the same population-years.

Adding those measurements to the existing Honshu–Izu network design would permit direct estimation of interaction–genetic spatial alignment and a true eco-genetic state-sufficiency test.

## Provenance / claim boundary

- Published article: Hiraiwa & Ushimaru (2024), DOI `10.1111/1365-2435.14527`.
- Data/code statement: Figshare `10.6084/m9.figshare.25025000.v1`.
- This audit uses published reported model selections/results and does not reconstruct unavailable raw observations.
- No new significance threshold, network metric or island-distance cut-off is introduced.
