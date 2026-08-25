# Prospective direct-interaction measurement discovery — *Witheringia solanacea*

## Purpose

The Eschscholzia campaign established an empirical measurement boundary: an array-level pan-trap abundance + mean-ITD state was ecologically plausible but did not receive reproducible held-out support for mating or pollen-movement endpoints. The next natural-data step therefore asks whether **direct focal-plant visitation** can be synchronized with reproduction and mating outcomes in one sampling programme.

This is a **measurement-validation system**, not a fragmentation-regime test. Common-garden identity is an upstream context label whose residual information may be tested later only if the archive supports a preregistered comparison.

## Fixed source before workbook inspection

Stone, VanWyk & Hale (2014), *Evolution* 68:1845–1855, doi:`10.1111/evo.12419`; Dryad dataset doi:`10.5061/dryad.f8539`.

The source files are fixed to:

1. `pollinators_all.xls` — direct pollinator visitation rates to **single focal plants** across nine common gardens and two rainy + two dry seasons (`I_realised` candidate);
2. `FruitSet.xlsx` — marked flowers and fruit development for plants in nine common gardens across the same seasonal design (`F_reproduction` candidate);
3. `paternity.xlsx` — parental and progeny microsatellite genotypes from seven common gardens (`G_mating/C_pollen` candidate);
4. `abortion_data_2011.xlsx` — time to fruit/embryo abortion for self-compatible and self-incompatible plants (`R/offspring-cost` secondary candidate).

No alternative file, response or interaction variable may be selected because a later result is favorable.

## Schema-only discovery boundary

Before any outcome row is inspected, discovery may record only:

- Dryad DOI/version metadata;
- exact filename and resolved file id/download relation;
- byte size and SHA-256;
- workbook sheet names and dimensions;
- first-row column labels.

It must not record or compute any data-row value, visit rate, fruit-set rate, selfing rate, genotype frequency, effect direction, coefficient, p-value or descriptive outcome statistic.

## Fixed biological mapping target

Using **header names only**, map whether the files provide a defensible common hierarchy for:

- garden identity;
- season/year or observation period;
- focal plant identity;
- compatibility/genotype class where present;
- direct focal-plant visitation (`I_realised`);
- fruit production from marked flowers (`F_reproduction`);
- parent/progeny identity sufficient to derive or use mating state (`G_mating/C_pollen`);
- abortion/reproductive-assurance or offspring-cost state (`R`) where directly mappable.

The discovery must preserve the distinction between direct visitation and reproductive/mating outcomes; it must not treat common-garden identity itself as a mechanistic state.

## Required decision

The schema-only campaign must end in exactly one of:

- **`direct_joint_state_identifiable`** — direct focal visitation and fruit set share garden + focal-plant/time keys, and paternity can be mapped to the same garden/plant hierarchy strongly enough for a prospectively declared held-out multi-endpoint test;
- **`direct_partial_state_identifiable`** — direct visitation and fruit set can be synchronized, but paternity is available only at a coarser garden/family hierarchy or another endpoint lacks a common key;
- **`not_identifiable_from_archive`** — the required keys cannot be mapped without inspecting outcomes, guessing identities or performing post hoc reconstruction.

All three outcomes are acceptable.

## Prospective scientific question if identifiable

> **Does direct realised focal-plant interaction provide endpoint-relevant predictive information for reproduction and mating, and after that process state is supplied does common-garden/season context retain transferable information?**

The exact models, held-out unit and decision rules must be committed in a second preregistration after schema-only discovery and before any outcome row is read.

## Claim ceiling

Even a successful later analysis would establish a measurement principle for direct interaction state, not a universal fragmentation threshold and not equivalence among natural habitat types.

## Stop rule

Do not inspect outcome values while choosing join keys. Do not substitute abortion for fruit set, derive a new visitation metric, drop a garden/season, redefine compatibility classes, or choose a paternity summary after seeing results. If the archive cannot be synchronized under source-defined identifiers, retain the non-identifiability result.