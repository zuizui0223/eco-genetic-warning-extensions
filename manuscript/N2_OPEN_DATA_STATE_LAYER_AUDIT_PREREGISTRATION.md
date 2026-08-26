# N2 preregistration — open-data state-layer audit across urban and island pollination systems

## Scientific purpose

The failed locked four-archive bridge showed that a cross-origin test can fail before outcome modelling because process and response measurements are not jointly available in enough independent systems. N2 is a new prospective programme, not an amendment or rescue of that failed candidate set.

N2 asks a measurement question before any new outcome analysis:

> Across a bounded set of urban and island pollination studies selected for relevant study design and public data description, which future-relevant state layers were measured, which were actually co-archived at a joinable ecological unit, and where does information disappear between biological measurement and reusable analysis representation?

N2 does **not** estimate an urban-versus-island ecological effect. It is a response-firewalled design audit intended to determine what empirical cross-origin tests are currently identifiable and what coordinated measurements are still required.

## Search and candidate lock

Search cutoff: **2026-08-26**.

Candidates were selected before any N2 outcome modelling from bounded searches for studies with at least one of the following:

- urbanization / urban-fragmentation context plus pollinator process data;
- island / island-mainland / continental-oceanic context plus pollinator process data;
- direct plant reproduction or an explicitly defined pollination-function response;
- public raw data, public repository metadata, or sufficiently explicit supplementary metadata to audit measurement availability.

Published effect directions, p-values and preferred ecological conclusions are not eligibility criteria and are excluded from the N2 registry.

The locked systems are:

### Urban

1. `U_ZURICH_2025` — Reji Chacko et al. 2025; EnviDat `10.16904/envidat.676`.
2. `U_CHICAGO_2024` — Zink et al. 2024; Dryad `10.5061/dryad.44j0zpcm6`.
3. `U_TORONTO_2025` — Sookhan et al. 2025; Dryad `10.5061/dryad.b8gtht7r4`.
4. `U_COMMELINA_2014` — Ushimaru et al. 2014; Dryad `10.5061/dryad.pd775`.
5. `U_POLLEN_RECEIPT_2022` — Carper et al. 2022; Dryad `10.5061/dryad.5mkkwh78r`.

### Island

1. `I_HIRAIWA_2017` — Hiraiwa & Ushimaru 2017; Dryad `10.5061/dryad.pm29d`.
2. `I_HAWAII_2019` — Aslan et al. 2019; Dryad `10.5061/dryad.tm575v4`.
3. `I_WANG_2025` — Wang et al. 2025; Dryad `10.5061/dryad.t76hdr8bj`.
4. `I_AZORES_2020` — Pardo et al. 2020; article + supplementary material, DOI `10.3390/insects11060351`.
5. `I_CARIBBEAN_2015` — Martén-Rodríguez et al. 2015; article + supporting information, DOI `10.1111/1365-2745.12457`.

No candidate is added or removed after the registry is scored merely to improve urban–island balance.

## Two distinct audit questions

For every system, N2 records separately:

1. **study measurement** — whether the biological layer was reported as measured under the source design;
2. **reusable representation** — whether public repository/supplement metadata demonstrate that the layer is available in a form that can be joined to the other required layers without inferring values from published effect summaries.

A layer measured in the paper but absent from the public archive is therefore `measured_but_not_demonstrated_as_coarchived`, not `biologically_absent`.

## State-layer dictionary

The audit uses the already fixed future-state vocabulary:

- `O` — upstream origin/context or fragmentation coordinate (urban intensity, island class, management/landscape context, etc.);
- `D` — focal density, flower abundance or sampling denominator needed to interpret process intensity;
- `I` — direct pollinator visitation/interaction intensity with effort, or a clearly labelled proxy when direct visitation is absent;
- `T` — mechanism-relevant pollinator/plant traits or functional matching information;
- `F` — realised plant function/reproduction (open fruit set, seed set, pollen receipt/deposition, or another explicitly defined direct function); exact semantics are retained;
- `C` — process-specific pollen, mate, seed or partner connectivity;
- `R` — reproductive assurance / compensating route measured by breeding or exclusion treatments;
- `G` — contemporary mating, offspring or population-genetic state;
- `A` — retained ecological-unit key allowing cross-layer alignment rather than only separate study-level marginals.

`O` is upstream context, not part of the candidate proximal state itself. `A` means actual joinable cross-layer organization; the mere fact that two measurements occurred in the same publication is insufficient.

## Allowed statuses

Each layer is scored only as:

- `yes` — explicit in public metadata/method description;
- `partial` — a proxy, aggregate, incomplete subset or uncertain unit alignment;
- `no` — explicitly absent or the public archive is explicitly limited to other data;
- `unclear` — public information does not resolve the layer without opening unavailable bytes or making an inference.

No numerical outcome values are required to assign these statuses.

## Direct residual-context eligibility gate

A system may proceed later to the narrower within-system test

`M0: F ~ I + fixed baseline/support terms`

versus

`M1: F ~ I + fixed baseline/support terms + O`

only if the reusable representation demonstrates all of:

1. `O` defined at the held-out ecological unit or a defensible parent unit;
2. direct `I` with effort or denominator;
3. direct `F` at the same or prospectively joinable unit;
4. stable `A` join keys;
5. at least five independent ecological holdout units;
6. source-defined response semantics that need no generic z-score rescue.

If direct visitation is replaced by pollen receipt, abundance, richness or another proxy, the system is retained in the registry but is not admitted to the direct `I_visit -> F` residual-context test.

## Cross-origin claim gate

N2 does not pool individual rows across studies. A cross-origin statement becomes eligible only if at least two independent urban and two independent island systems pass the **same process and response semantic gate**, with system/landscape held out as the transfer unit.

If this is not achieved, the correct N2 result is a measurement/representation boundary, not an ecological urban–island difference.

## Stop rules

Do not:

1. use a published effect direction, p-value or model coefficient to change a layer score;
2. infer an archived reproductive variable merely because the paper reports a reproductive result;
3. call pollen receipt, pollinator abundance, richness and direct flower visitation the same `I` coordinate;
4. call fruit set, seed number, seed mass, pollen receipt and autofertility the same `F` response by generic standardisation;
5. treat multiple plant species or endpoints within one study as independent systems;
6. add a new system after N2 scoring merely to restore a desired two-versus-two comparison;
7. interpret missing archive layers as evidence that the biological mechanism was absent;
8. infer full `D/I/T/C/R/G/A` sufficiency from a partial `I -> F` bridge.

## Permitted conclusion ceiling

N2 may establish which measurements and reusable representations are currently co-available in this bounded registry, and may identify systems suitable for later prospectively frozen within-system residual-context tests.

N2 alone cannot establish that urban and island systems share the same future law.
