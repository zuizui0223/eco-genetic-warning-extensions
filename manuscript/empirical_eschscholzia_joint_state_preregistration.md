# Prospective natural joint-state discovery — *Eschscholzia californica*

## Purpose

This campaign asks whether a common measured ecological state can be synchronized across **pollinator availability, direct reproductive function, pollinator dependence/reproductive assurance, and mating outcome** in one field experiment.

The system is the June 2015 Hillesden estate experiment in Buckinghamshire, UK. Sixteen arrays were distributed across four 100-ha blocks; each array contained three experimental *Eschscholzia californica* plants, giving 48 focal plants. The arrays crossed florally rich and florally poor habitat and were used across a family of EIDC data products from the same larger experiment.

The target state is therefore closer to the natural condition map than a single interaction dataset:

`habitat / array context + pollinator availability/traits I,T + reproductive assurance R -> direct seed function F + mating/paternity G_mating/C`

## Source lock before schema inspection

Four EIDC datasets are fixed before any row-level outcome inspection:

1. **Pollinator availability / traits (`I/T`)**  
   DOI `10.5285/01906784-6742-44bf-b244-a4b63bed8d82`  
   Title: *Pollinator data from pan traps located in habitats comprising different floral cover in Buckinghamshire, UK*.

2. **Direct seed function / pollen limitation (`F_seed`)**  
   DOI `10.5285/8caf2d8a-564d-4f2e-a797-174165a83796`  
   Title: *The seed set of supplemented and pollinator exposed flowers from Eschscholzia californica plants located within habitats comprising different floral cover*.

3. **Pollinator dependence / alternative route (`R`)**  
   DOI `10.5285/5b400b69-b828-45e8-b04e-7ccbfdb0987f`  
   Title: *The seed set of Eschscholzia californica plants introduced into habitats comprising different floral cover*; exposed and pollinator-excluded flowers are represented.

4. **Mating / paternity (`G_mating/C`)**  
   DOI `10.5285/7b721c07-bc38-4815-8669-4675867663d0`  
   Title: *Paternity of Eschscholzia californica plants introduced to habitats comprising different floral cover*.

All four are NERC Environmental Information Data Centre products and are described as parts of the same larger field experiment.

## Fixed access route for discovery

The first machine-access route is the EIDC data-package service:

`https://data-package.ceh.ac.uk/data/<dataset UUID>`

where the UUID is the DOI suffix. This is an access/schema gate, not an outcome analysis. If the service returns an archive, only archive member names, byte hashes/sizes and CSV header labels may be inspected. If it returns one CSV directly, only the first header row may be read. If this route cannot produce a verifiable data payload, the failure is recorded before any alternative access route is considered.

## Schema-only boundary

The discovery artifact may contain only:

- DOI / dataset UUID / fixed package URL;
- HTTP content type and response size;
- SHA-256 of the returned package/file;
- member file names if an archive;
- per CSV: row-independent header labels only;
- no data rows, values, frequencies, means, correlations, coefficients, p-values or effect directions.

The discovery code must not calculate even descriptive outcome summaries.

## Fixed biological mapping target

From **headers/keys only**, the next stage may map source columns to:

- experiment block and array;
- focal plant identity where present;
- floral habitat/context;
- pollinator taxon/count and source-provided body-size/ITD trait (`I/T`);
- exposed and pollen-supplemented seed function (`F_seed` / pollen limitation);
- exposed and pollinator-excluded seed function (`R`, pollinator dependence / autonomous route);
- selfed/outcrossed status and/or assigned father/paternity (`G_mating/C`).

No new endpoint family may be selected from values after the schema is seen.

## Prospective scientific question

> **After conditioning on measured pollinator availability/trait state, does floral habitat context become redundant for both direct reproductive function and mating outcome, or do reproductive assurance and mating connectivity retain distinct state information?**

This question is intentionally multi-endpoint. It does not assume that one sufficient state exists for every downstream process.

## Required discovery decision

After schema-only inspection, the campaign must be classified as exactly one of:

- **`joint_state_identifiable`** — block/array/plant keys permit direct synchronization of `I/T`, `F_seed`, `R`, and `G_mating/C` at a defensible common hierarchy;
- **`partial_joint_state_identifiable`** — the same field experiment and array/block structure are represented but at least one endpoint cannot be mapped to the same focal-plant level; a prospectively declared hierarchical multi-endpoint test may still be possible;
- **`not_identifiable_from_archive`** — required keys or process variables cannot be mapped without inspecting outcomes or inventing post hoc joins.

All outcomes are acceptable.

## Claim ceiling

Pan traps represent **pollinator availability/community state**, not direct visits to each focal plant. Even a successful later test must preserve that proxy boundary.

The campaign will not claim that floral-rich versus floral-poor habitat is itself a functional-fragmentation regime. Habitat context remains an upstream route whose residual predictive information is tested after measured process state.

## Stop rule

No seed-function variable, paternity variable, pollinator group, body-size metric, habitat contrast, spatial scale or join key may be selected because it gives a preferred result. If schema permits analysis, an exact second preregistration must specify the unit hierarchy, fixed model sequence, held-out validation and decision rules **before any outcome row is inspected**.
