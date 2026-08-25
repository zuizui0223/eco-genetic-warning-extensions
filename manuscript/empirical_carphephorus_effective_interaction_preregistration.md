# Prospective realised-interaction discovery — *Carphephorus bellidifolius*

## Purpose

The Eschscholzia multi-process test showed that an array-level pollinator-availability proxy (`I_count` + mean ITD from pan traps) did not establish reproducible held-out predictive information for mating state or pollen-movement distance. The next empirical target therefore moves one step downstream in the measurement hierarchy: **realised focal-plant pollinator visitation**.

The scientific question is fixed prospectively:

> **After fragmentation geometry/context is represented, does realised pollinator visitation to the focal plant add transferable predictive information for pollination/reproductive function, and does fragmentation context retain residual information after that realised interaction state is supplied?**

This is a measurement-calibration test of `I_realised -> F`, not a test of genetic warning.

## Source lock before row inspection

Primary dataset:

- Hulting, Smith & Haddad (2025), Dryad doi:`10.5061/dryad.w9ghx3g48`.

Author analysis code:

- `hultingk/review-SRS-CARBEL`
- pinned public commit: `622e5266db24e99a983bcf89d63a2258ebf93662`.

The following Dryad files are fixed before schema inspection:

1. `CARBEL-arthropods.csv` — focal-plant arthropod visitation;
2. `CARBEL-floral.csv` — focal/local floral state;
3. `CARBEL-seeds.csv` — reproductive/pollination outcome;
4. `Patch_type.csv` — fragmentation patch type/context.

No alternative file or endpoint family may be substituted after the data are inspected.

## Source-code constraint

The pinned author wrangling code is part of the prospective biological mapping. It explicitly:

- counts `visitor_type == "pollinator"` by `plant_ID × sampling_round`;
- derives plant-level mean pollinator visitation across sampling rounds;
- joins that realised visitation to the seed table by `plant_ID`;
- computes source-defined `pollination_rate = (viable + no_predation) / (viable + no_predation + nonviable)`;
- joins patch type by block/patch.

The project may reproduce these source-defined transformations but may not search alternative visitation summaries or reproductive outcomes because they are more favorable.

## Schema-only discovery boundary

This first stage may inspect only:

- Dryad metadata and file identifiers;
- byte size and SHA-256/digest;
- CSV header labels;
- pinned author-code variable names and join declarations.

It must not read data rows, calculate visitation or pollination summaries, fit models, calculate effect directions, or inspect outcome distributions.

## Prospective identifiability rule

Discovery ends in exactly one of:

- **`realised_interaction_state_identifiable`** if:
  - `CARBEL-arthropods.csv` contains `plant_ID`, `visitor_type`, `sampling_round`;
  - `CARBEL-seeds.csv` contains `plant_ID` plus the source-defined components needed for `pollination_rate` (`viable`, `no_predation`, `nonviable`);
  - `Patch_type.csv` contains the block/patch mapping needed for fragmentation context;
  - visitation and reproductive outcome can therefore be synchronized without inventing a new join key;
- **`partial_realised_interaction_state_identifiable`** if visitation and reproductive function can be synchronized by `plant_ID` but fragmentation context or the declared local floral support cannot be mapped from the fixed files;
- **`not_identifiable_from_archive`** if the required files/keys/source-defined outcome components cannot be mapped without post-hoc reconstruction.

All outcomes are acceptable.

## Next-stage model target if identifiable

No row-level analysis is allowed in this branch. If the gate is identifiable, a second preregistration must be committed before outcome rows are read. That second stage must preserve whole-patch or whole-plant grouping and compare a fixed sequence separating:

1. fragmentation/context state;
2. realised focal-plant pollinator visitation;
3. residual fragmentation information after visitation.

The exact response scale, validation unit and model family will be fixed from schema + pinned source code only, not from outcome values.

## Claim ceiling

Even a positive result would establish only that realised focal-plant visitation carries endpoint-relevant information in this experimental fragmentation system. It would not make visitation a universally sufficient interaction state; pollen receipt, donor identity or other effective-service coordinates may still be required.

## Stop rule

Do not switch from realised visitation to pollinator availability, choose a subset of pollinator taxa, replace the source-defined pollination outcome, repair IDs from outcome values, tune a fragmentation contrast after fitting, or reopen alternate validation schemes because the result is weak or surprising.
