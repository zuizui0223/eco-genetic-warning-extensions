# Prospective natural joint-state discovery — *Miconia affinis*

## Purpose

The next empirical target is a natural system that places multiple downstream consequences of pollination in the **same sampling programme** rather than treating seed production, gene flow and genetics as interchangeable proxies.

The source study is Castilla et al. (2017), *Proceedings of the National Academy of Sciences*, doi:`10.1073/pnas.1619271114`, with data archived at Dryad doi:`10.5061/dryad.1cm80`.

The study explicitly combines individual pollinator visits with seed production/viability, molecular fractional-paternity analysis and pollen-dispersal distance. The archive also contains genotypes and coordinates for reproductive trees and genotypes for seeds from the single-visit experiment.

This makes *Miconia affinis* the current leading candidate for a synchronized natural test of:

`interaction / pollinator trait state I,T -> direct reproductive function F + pollen-connectivity / genetic outcome C,G`

## Source lock before workbook inspection

Dryad version: 20 November 2017.

The four source files and public Dryad file-stream identifiers are fixed before schema inspection:

1. `correlation_dbh_number of inflorescences.xlsx` — file stream `30526`
2. `genotypes_Miconia affinis.xlsx` — file stream `30527`
3. `pollen_dispersal_analysis_data.xlsx` — file stream `30528`
4. `seed_viability_analysis_data.xlsx` — file stream `30529`

The source page states that these contain, respectively, floral-display/tree-size data, reproductive-tree and seed genotypes plus adult coordinates, the variables used in the pollen-dispersal model, and the variables used in the seed-viability model.

## Discovery gate

This branch initially performs **schema-only discovery**. It may record only:

- exact download URL and file-stream id;
- byte size and SHA-256;
- workbook sheet names;
- sheet row/column counts;
- column names.

It must not report outcome means, effect directions, model coefficients, p-values, correlations, distributions or individual cell values.

No ecological conclusion is permitted from the discovery artifact alone.

## Fixed scientific target after schema discovery

The next analysis is allowed to open only if the archive can identify a defensible join or matched sampling structure for at least:

- pollinator identity and/or source-defined functional pollinator trait (`I/T`);
- direct seed function (`F_seed`);
- pollen dispersal / paternity outcome (`C_pollen` and, where directly represented, `G_parentage`);
- plant or neighbourhood state variables supplied by the source study.

The primary conceptual question is fixed now:

> **Does the measured pollinator state provide a sufficient natural representation for both immediate reproductive function and pollen-mediated connectivity, or do the two endpoints require different additional plant/population state coordinates?**

This is deliberately stronger than asking which predictor is significant in each source model. The final test will compare prospectively declared nested state representations using held-out ecological units wherever the source structure permits.

## Required decision after schema discovery

The discovery phase must end in one of three statuses:

- `joint_state_identifiable` — a common or explicitly mappable sampling structure links `I/T`, `F_seed`, and `C_pollen/G_parentage` strongly enough for a preregistered held-out comparison;
- `partial_joint_state_identifiable` — both endpoint families exist but cannot be synchronized at the same individual/event level; a bounded multi-endpoint comparison may still be declared prospectively;
- `not_identifiable_from_archive` — required keys or process variables are absent or cannot be mapped without outcome-informed reconstruction.

All three are acceptable.

## Claim ceiling

Even if the later analysis succeeds, the study will not be used to claim a universal pollinator body-size rule. The scientific use is narrower: determine **which measured present-state coordinates are required to predict distinct components of pollination function in the same natural system**.

## Stop rule

Do not inspect outcome values while choosing join keys, endpoint definitions or predictor families. Do not replace seed function with a more favorable reproductive endpoint, replace pollen-dispersal distance with another connectivity metric, select pollinator species after seeing results, or search alternative neighbourhood metrics after fitting. Any exact model sequence must be committed in a second preregistration after this schema-only gate and before outcome analysis.
