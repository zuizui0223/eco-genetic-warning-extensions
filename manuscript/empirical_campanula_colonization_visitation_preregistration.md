# Prospective realised-visitation discovery — experimental colonization in *Campanula americana*

## Purpose

The empirical programme now requires a machine-accessible system in which **realised pollinator visitation** and reproductive function share an explicit sampling hierarchy. This campaign uses the experimental-colonization dataset archived at Zenodo doi:`10.5281/zenodo.10814705`.

The fixed scientific question is:

> **Does realised pollinator visitation per flower add transferable information about reproductive limitation after colonization context is represented, and does colonization context retain residual predictive information after realised visitation is supplied?**

This is a natural/field measurement-calibration test of `I_realised -> F` with an explicit alternative reproductive route (`autonomy`), not a genetic-warning test.

## Source lock before row inspection

Zenodo record: `10814705`, version v1, published 13 March 2024.

Two files are fixed by the archive before row inspection:

1. `PLdataindividual.csv` — MD5 `b84fa5c83513dbe75c0bf7840d1c74aa`;
2. `pollinator.csv` — MD5 `81e0deaa78a6a97e1211484cb9d0d3b3`.

The record description states that the first file contains individual seed set under control and supplemented pollination treatments and the second contains pollinator observations for the experimental populations.

No alternative response file or pollinator file may be substituted after inspection.

## Schema-only boundary

This branch may inspect only:

- the two fixed files and their MD5/SHA-256;
- CSV header labels;
- Zenodo-declared field descriptions.

It must not read data rows, calculate visitation/seed summaries, calculate pollen limitation, inspect effect directions, fit models or compute p-values.

## Prospective state mapping

The Zenodo record predeclares the biological coordinates to be mapped from headers only.

Seed/reproductive file is expected to contain:

- `experimental.population` — experimental population ID;
- `individual` — focal plant ID;
- `site`;
- source population;
- `autonomy` — high/low autonomous-selfing category (`R` candidate);
- `size` — single/small experimental-population context;
- `treatment` — control/supplemented;
- seed-number outcome.

Pollinator file is expected to contain:

- `experimental.population`;
- `site`;
- source population;
- `autonomy`;
- `size` / number of plants;
- flower counts;
- bee-group visit counts;
- `total.poll.visits`;
- `visits.per.flower` — realised population-level interaction rate (`I_realised`).

## Identifiability rule fixed before header inspection

Discovery ends as exactly one of:

- **`realised_visitation_function_state_identifiable`** if both files share `experimental.population`, the pollinator file contains a realised visitation-rate coordinate, and the seed file contains plant ID + pollination treatment + seed outcome, permitting a hierarchy `site -> experimental population -> individual -> treatment` without invented joins;
- **`partial_realised_visitation_function_state_identifiable`** if visitation and reproductive outcome can be joined at experimental-population level but one declared context coordinate (`site`, source population, autonomy or size) cannot be matched from headers;
- **`not_identifiable_from_archive`** if the fixed files/keys do not support that hierarchy without post-hoc reconstruction.

All outcomes are acceptable.

## Next-stage target if identifiable

A separate second preregistration must be committed before any data row is read. It must preserve whole experimental populations as the held-out unit and prospectively distinguish:

1. colonization/context state;
2. realised `visits.per.flower`;
3. residual context after realised visitation;
4. paired control-versus-supplemented reproductive information as a pollen-limitation/capacity check.

The exact outcome transformation and model family must be fixed from schema and source definitions only.

## Claim ceiling

The experiment can test whether population-level realised visitation is more endpoint-relevant than an availability proxy. It does not measure stigma pollen receipt or donor identity, and positive visitation information would not prove a universally sufficient interaction state.

## Stop rule

Do not select bee subgroups, population-size contrasts, autonomy classes, seed transformations or treatment subsets because they improve the result. Do not replace `visits.per.flower` with another interaction metric after seeing outcomes. Do not use row-wise validation when population-level visitation is shared.
