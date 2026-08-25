# Prospective direct-interaction → function discovery — *Banksia catoglypta*

## Purpose

The natural-state programme has reached a measurement question. In *Eschscholzia californica*, an array-level pan-trap abundance + mean-ITD compression was ecologically plausible but did not receive reproducible held-out support for mating or pollen-movement outcomes. The next executable test therefore moves from pollinator **availability** toward observed floral interaction.

This campaign asks whether the public *Banksia catoglypta* study can synchronize a direct floral-visitor state with a direct reproductive-function endpoint.

This is a **measurement-validation system**. It is not a fragmentation-regime test and it does not contain a preregistered genetic/paternity endpoint.

## Fixed source snapshot before data inspection

Publication:

Wawrzyczek, Davis, Krauss, Hoebee, Ashton & Phillips (2024), *Botanical Journal of the Linnean Society* 206:257–273, doi:`10.1093/botlinnean/boae024`.

Public data repository:

`stanwawrzyczek/Pollination-of-Banksia-catoglypta-Data`

The repository snapshot is fixed to:

- commit `1ab685d62d005865935435bbd49cadba50080741`;
- file `Banksia catoglypta pollination - DATA.zip`;
- Git blob SHA `91cc21eb4d967b702bd18f87f91be1b52cacb6a3`;
- repository README explicitly states that the ZIP contains data associated with the study.

The branch/README may change later; the discovery workflow must download only the fixed commit snapshot and verify the Git blob SHA before inspecting the ZIP.

## Schema-only boundary

The first campaign may inspect only:

- fixed repository/commit/path/blob provenance;
- ZIP byte size and SHA-256;
- ZIP member filenames and member sizes/hashes;
- for CSV/TSV/text tables: first header row only;
- for XLS/XLSX workbooks: sheet names, dimensions and first-row column labels.

It must not read or report any data-row value, visitation rate, visitor frequency, fruit-set value, seedling-emergence value, exclusion-treatment effect, coefficient, p-value, correlation or descriptive outcome statistic.

## Fixed biological mapping target

Using filenames and header labels only, determine whether the fixed archive exposes a defensible common hierarchy for:

- observation/site/plant/inflorescence identity where available;
- pollinator taxon or functional visitor group;
- observed floral visitation or floral-interaction measure (`I_realised` candidate);
- selective pollinator-access/exclusion treatment where present (`R/access-state` candidate);
- fruit/seed or seedling outcome (`F_reproduction` candidate);
- time or observation period needed to synchronize I and F.

Do not infer paternity, genetics or gene flow from this archive unless a source-defined genetic file unexpectedly exists; such a file would be recorded only as schema and would require a new preregistration before scientific use.

## Required discovery decision

The schema-only campaign must end in exactly one of:

- **`direct_IF_joint_state_identifiable`** — observed floral interaction and reproductive function share explicit keys or a source-defined experimental hierarchy strong enough for a prospectively declared held-out I→F state test;
- **`direct_IF_partial_state_identifiable`** — both I and F are present in the same study but only at non-identical or coarser experimental units, permitting at most a bounded hierarchical comparison;
- **`direct_IF_not_identifiable`** — direct interaction and function cannot be synchronized without reading outcomes, guessing IDs, or reconstructing undocumented joins.

All three outcomes are acceptable.

## Scientific question if identifiable

> **Does an observed floral-interaction state carry endpoint-relevant held-out predictive information for reproductive function, and does pollinator-access treatment or other upstream experimental context retain transferable information after that measured interaction state is supplied?**

The exact response, interaction compression, held-out unit, transformations, regularization and decision rules must be committed in a second preregistration before any outcome row is inspected.

## Claim ceiling

A positive result would validate the tested observed-interaction measurement for the tested reproductive endpoint. It would not establish a universal pollinator syndrome, a genetic-warning mechanism, or equivalence between this common pollination experiment and island/urban fragmentation.

## Stop rule

Do not choose among visitor groups, fruit/seed endpoints, exclusion treatments or subsets based on outcome values. Do not repair IDs by fuzzy matching after outcome inspection. If the archive lacks a source-defined bridge between I and F, retain the partial/non-identifiable result.