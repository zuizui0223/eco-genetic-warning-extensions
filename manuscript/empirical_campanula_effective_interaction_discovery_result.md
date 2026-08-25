# Campanula effective-interaction discovery result

## Decision

**`effective_interaction_state_identifiable`**

The schema-only discovery for Koski et al. (2018) completed successfully without inspecting numeric study-cell values.

Locked source:

- Dryad doi:`10.5061/dryad.5nj81nf`;
- Zenodo record `4969330`;
- `Koski et al. 2018_Data_ProcRoySoc.xlsx`;
- MD5 `2d26307743e8a22384781854b8f2f33b`;
- observed workbook SHA-256 `b81b77248b75330049e1ddd8ae026db127f838e979620a0415a5addb9a7e8f27`.

Discovery provenance:

- workflow `32821856698`;
- job `97721487444`;
- artifact `9553407497`;
- artifact digest `sha256:66c4c9f7956fd1edb58c5349ba25d92cd3f75bb115a3724363a6387cabd3cbbf`.

## Schema evidence

The workbook contains six sheets:

1. `PopVis Rates_ PL_Depletion`
2. `Grains To Seeds `
3. `Pollen Deposition Efficiency`
4. `Seed Set Efficiency`
5. `Pollen Removal Efficiency`
6. `Metadata`

The population sheet contains 23 population rows plus a header and exposes, by label only:

- `Population`;
- `Bumblebee Rate`;
- `Megachile Rate`;
- `Small Rate`;
- `Pollen Limitation 2016`;
- sex-phase-specific visitation proportions/rates;
- source-defined grains-deposited and grains-removed coordinates, including per-hour forms.

The Metadata sheet defines the population visitation columns as visits/flower/hour and defines `Pollen Limitation 2016` independently as the hand-pollinated versus control seed response.

## Independent efficiency calibration is identifiable

The separate single-visit sheets use explicit pollinator labels and the Metadata sheet supplies a common group code:

- `B` = bumblebee;
- `H` = small bee (Halictidae);
- `M` = *Megachile campanulae*.

The labels show three outcome-independent calibration families:

- `Pollen Deposition Efficiency`: `Pollinator`, `TotalPoll`, `MeanUnvisited`, `ScaledPoll`;
- `Seed Set Efficiency`: `Pollinator`, `Seeds`;
- `Pollen Removal Efficiency`: `Poll`, `PollenCounted`, `PollenCountedScaled`, `MeanUnvisitedScaled`, `TotalRemoved`.

Most importantly, the Metadata sheet explicitly defines source-derived population-state coordinates without reference to pollen limitation:

- `Bumblebee Grains Dep` = pollen grains deposited by one bumblebee visit;
- `Megachile Grains Dep` = pollen grains deposited by one *Megachile* visit;
- `Small Grains Dep` = pollen grains deposited by one small-bee visit;
- corresponding `... Grains Dep Per Hour` = female-phase visitation rate × per-visit deposition;
- `... Grains Rem` = pollen grains removed by one visit;
- corresponding `... Grains Rem Per Hour` = male-phase visitation rate × per-visit removal.

Thus the archive contains both the independent calibration data and source-defined effective pollen-transfer fluxes that can be compared prospectively with raw visitation.

## What this permits next

A second preregistration may compare population pollen-limitation prediction under alternative present-state representations, for example:

- raw group-specific visitation;
- phase-matched visitation;
- source-defined efficiency-calibrated pollen deposition/removal fluxes.

The exact feature aggregation, model family, held-out validation and decision rule must be fixed before reading any numeric values.

## What this does not establish

No numerical visitation rate, pollen-limitation value, deposition efficiency, seed-set efficiency, removal efficiency, coefficient, group contrast or effect direction was used for this decision.

Therefore this discovery does not support any statement about which pollinator group is beneficial, harmful or more efficient. It establishes only that an outcome-independent effective-interaction adequacy test is identifiable.

## Stop rule

The discovery workflow is closed after this result. Numeric outcome analysis must occur in a separate branch/PR whose exact model preregistration is committed before the first numeric study row is inspected.