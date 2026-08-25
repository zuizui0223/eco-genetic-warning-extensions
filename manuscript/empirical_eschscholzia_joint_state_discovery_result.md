# Eschscholzia joint-state discovery result

## Decision

**`joint_state_identifiable`**

The schema-only discovery gate for the June 2015 Hillesden *Eschscholzia californica* experiment succeeded without inspecting any outcome row.

All four fixed EIDC products share the same experiment hierarchy at least through **Block + Experimental array**. The two seed products and the paternity product additionally share a focal **Plant identification number**. Therefore the preregistered identifiability rule is satisfied.

The correct hierarchy for analysis is:

`Block -> Experimental array -> focal plant -> fruit/progeny where applicable`.

The pollinator product stops at the array level, so pollinator abundance/trait information must be treated as an **array-level availability state** and copied only downward to plants in that array. It must not be represented as direct focal-plant visitation.

## Locked schema

### Pollinator availability / traits

DOI `10.5285/01906784-6742-44bf-b244-a4b63bed8d82`

CSV columns:

`Block`, `Experimental array`, `Grid reference`, `Habitat`, `Treatment`, `Survey date`, `Pollinator species`, `Intertegular span (mm)`.

### Direct seed function / supplementation

DOI `10.5285/8caf2d8a-564d-4f2e-a797-174165a83796`

CSV columns include:

`Block`, `Experimental_array`, `Plant_identification_number`, `Habitat`, `Treatment`, `Mean_number_of_seeds_from_field_exposed_flowers`, `Number_of_fruits`, `Number_of_seeds_from_supplemented_flowers`.

### Exposed versus excluded seed function / reproductive assurance

DOI `10.5285/5b400b69-b828-45e8-b04e-7ccbfdb0987f`

CSV columns include:

`Block`, `Experimental array`, `Plant identification number`, `Sample type`, `Fruit number`, `Habitat`, `Treatment`, `Number of seeds`.

### Paternity / mating state

DOI `10.5285/7b721c07-bc38-4815-8669-4675867663d0`

CSV columns include:

`Block`, `Experimental_array`, `Plant_identification_number`, `Fruit_number`, `Habitat`, `Treatment`, `Sample_identification`, seven microsatellite loci, `Parentage`, `Paternity_analysis`, `Distance_of_pollen_movement`, `Habitat_crossed`.

## Why this passes the preregistered gate

The prospectively fixed rule required:

1. common block and array identifiers in all four process datasets; and
2. a common focal-plant key across both seed products and paternity.

Both conditions are met by header identity after normalizing spaces versus underscores only. No row values were used to decide this.

## Scientific consequence

This system can support a hierarchical multi-endpoint test of whether one measured pollinator availability/trait state is enough to make habitat context predictively redundant for:

- direct exposed seed function (`F_seed`);
- reproductive assurance from pollinator exclusion (`R`); and
- mating/outcrossing state (`G_mating/C`).

Because the pollinator state is array-level while the downstream outcomes are plant/fruit/progeny-level, **leave-one-array-out** is the minimum acceptable held-out unit. Row-wise or plant-wise validation would leak the same upstream pollinator state across train and test sets.

## Claim ceiling

`joint_state_identifiable` means only that a defensible common hierarchy exists. It does not establish state sufficiency and it does not imply that habitat context will disappear after conditioning on pollinator state.

A second exact-model preregistration is required before any outcome row is opened.

## Provenance

- discovery head: `6b016b41bffb1232cc619dd83b48570b87e9e756`
- workflow run: `32736330920`
- job: `97459926747`
- artifact: `9523523742`
- artifact digest: `sha256:d33b6542c715eba77d1e1bff38942cd474daaf3d8b3ca9f25774d41dce266d79`
- schema, Protocol invariant, Paper completion and two-repository reproducibility workflows all succeeded on the discovery head.
