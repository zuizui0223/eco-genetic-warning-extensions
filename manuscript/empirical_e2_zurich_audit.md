# E2 empirical audit — Zurich urban garden interaction–function state

## Status

This is a **secondary audit of openly released data structures, analysis code and stored model outputs** from the BetterBlooms / Reji Chacko et al. urban-garden study programme. It is **not** a new refit of the raw pollination-success observations.

The source repository is `mrejichacko/BetterBlooms`. Its README states that the full reproductive-success analyses require raw EnviDat files to be downloaded into the project, while cleaned pollinator summaries and model-result tables are committed. The underlying dataset is Reji Chacko, Moretti & Frey (2025), EnviDat `10.16904/envidat.676`; the associated 2026 analysis is *No one-size-fits-all: trait-dependent effects of local plant diversity on pollinators and pollination service in a densifying city*.

## Why this system matters for the state-sufficiency hypothesis

The 24-garden design supplies a real ecological partial state rather than an abstract habitat label:

- **spatial / urban context:** garden coordinates and impervious/built cover at 50, 100, 250 and 500 m (`Urban_50` … `Urban_500`);
- **local ecological support:** garden plant/floral variables;
- **realised interaction support `I`:** plant-specific daily abundance and species richness of pollinator guilds;
- **direct realised function `F`:** seed set and/or fruit set for four phytometer species;
- **trait layer `T`:** individual pollinator traits and trait-filtering analyses in the source programme.

The design deliberately standardises phytometer plants. It therefore does **not** provide natural among-population plant genetic state `G`, pollen/seed connectivity `C`, natural mating-system variation `R`, or long-term ecological memory `M`. It cannot by itself test the complete `D/I/T/G/C/R/F/M` state.

Observed `Urban_500` in the released explanatory table spans approximately **0.191–0.818** across the 24 gardens, so the study samples a substantial within-city urbanisation gradient rather than a binary urban/non-urban contrast.

## What the released model outputs already show

### A. Urban intensity is not a universal signed predictor of pollination function

The source repository stores plant-specific garden/landscape model coefficients with uncertainty intervals. For the standardised `Urban_500` effect:

| focal function | mean effect | interval | audit interpretation |
|---|---:|---:|---|
| carrot seed set | -0.145 | [-0.260, -0.032] | negative |
| radish fruit set | -0.134 | [-0.215, -0.050] | negative |
| radish seed set | -0.017 | [-0.053, 0.018] | no clear effect |
| sainfoin fruit set | -0.009 | [-0.301, 0.279] | no clear effect |
| comfrey fruit set | -0.444 | [-0.744, -0.143] | negative |
| comfrey seed set | -0.044 | [-0.087, 0.0002] | borderline / interval includes zero |

Local plant diversity also interacts with urban intensity in a function-specific way: the stored interval is positive for radish fruit set and sainfoin fruit set, negative for radish seed set, and unresolved for the other listed endpoints.

**Empirical implication:** even within one city and one common experimental design, `urban intensity` does not define a single functional-fragmentation response. The focal function and local ecological context condition the response.

### B. The interaction state is guild- and function-specific

The released pollinator-abundance models also reject a one-dimensional `more pollinators = more function` state.

Examples from stored coefficients:

- **carrot seed set:** hoverfly abundance `+0.26 [0.09, 0.42]` and beetle abundance `+0.20 [0.03, 0.37]`, while honeybee abundance is negative `-0.15 [-0.25, -0.05]`;
- **sainfoin fruit set:** combined bee abundance `+0.34 [0.05, 0.63]`;
- **comfrey fruit set:** social-bee abundance `+0.44 [0.15, 0.73]`;
- **radish fruit set:** social-bee abundance is positive in mean but its interval touches zero (`+0.15 [0, 0.30]`).

Species-richness models are likewise non-universal. For example, carrot seed set is negatively associated with social-bee richness and positively associated with hoverfly richness, while radish fruit set is positively associated with social-bee richness.

**Empirical implication:** the biologically relevant `I` is not total pollinator abundance or richness. It is a focal-function-specific composition/effectiveness state. This is the empirical analogue of retaining interaction identity rather than collapsing support into one scalar.

## What is and is not tested by the available outputs

The source authors fitted two relevant model families:

1. direct garden/landscape models of reproductive function (`F ~ garden/urban/local plant context`);
2. interaction models of reproductive function (`F ~ guild-specific pollinator abundance` or `F ~ guild-specific richness`).

These are sufficient to demonstrate that both landscape and interaction effects are conditional. They are **not sufficient to test the strict state-sufficiency criterion**, because the released coefficient tables do not correspond to one joint model of the form

`F ~ measured interaction state + urban intensity + local context`.

Therefore this audit does **not** claim that interaction state statistically mediates the urban effect or that urban history becomes irrelevant after conditioning on `I/T`.

## Exact next empirical test

For each focal plant/function, prospectively compare nested predictive models:

- `M0`: local ecological state only;
- `M1`: `M0 +` guild-specific interaction support / trait-weighted interaction state;
- `M2`: `M1 + Urban_500 + local-context × Urban_500`;
- optionally `M3`: `M2 +` spatial coordinates / spatial random structure if residual spatial dependence remains.

The convergence/state-sufficiency question is not whether `Urban_500` has a small p-value. It is whether adding `Urban_500` to a measured interaction-functional state improves **held-out prediction and calibration of future/reproductive function**.

Interpretation:

- if `M2` does not improve prediction relative to `M1`, the measured ecological interaction state is a candidate sufficient compression of the urban route at this scale;
- if `M2` improves prediction, the measured state is incomplete; the residual urban term points to omitted habitat/resource/microclimate or interaction information;
- if effects differ among focal plants, those differences identify multiple natural functional states rather than one universal urban-fragmentation coefficient.

## Connection to the current model result

This natural dataset already reproduces the **logic** of coarse-state insufficiency without requiring the model's exact variables:

- one scalar landscape coordinate has non-universal effects across functions;
- pollinator abundance and richness are not interchangeable with interaction composition;
- the sign and importance of interaction guilds depend on the focal ecological function.

The decisive empirical state should therefore preserve at least **local context × interaction composition × focal function**, and later add natural genetic/connectivity layers in systems where they are available.

Zurich is consequently a strong **partial-state test**, not yet a full urban–island convergence test. Its value is to identify which ecological coordinates must be measured before genetic warning is even evaluated.

## Provenance / identification boundary

- BetterBlooms README: raw EnviDat files are required to rerun the full reproductive-success scripts; only cleaned summaries and stored results are committed in the GitHub repository.
- Stored landscape coefficients: `results/beta_coefficients_reproductive_success_garden_landscape.txt`.
- Stored pollinator coefficients: `results/beta_coefficients_reproductive_success_all.txt`.
- Garden urban-gradient table: `raw_data/explanatory_variables.txt`.
- Carrot interaction-function model code: `scripts/02_analyses/3b_reproductive_succ_2_carrot~abundance.R`.

No raw observations are reconstructed or imputed in this audit, and no significance threshold is tuned.
