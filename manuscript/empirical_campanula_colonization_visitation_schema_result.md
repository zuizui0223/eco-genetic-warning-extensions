# Campanula experimental-colonization realised-visitation schema result

## Decision

**`realised_visitation_function_state_identifiable`**

Schema-only workflow `32819251801` succeeded before any data row or outcome value was inspected.

Source: Zenodo `10.5281/zenodo.10814705`.

- `PLdataindividual.csv` MD5 `b84fa5c83513dbe75c0bf7840d1c74aa`
- `pollinator.csv` MD5 `81e0deaa78a6a97e1211484cb9d0d3b3`

## Header-only evidence

`PLdataindividual.csv` contains:

`source.population, autonomy, individual, experimental.population, site, size, date.initiated, dayfromstartofexperiment, treatment, seednumber`

`pollinator.csv` contains:

`experimental.population, site, start.date, end.date, source population, autonomy, size, number of plants, ... , total.poll.visits, visits.per.flower`

The preregistered hierarchy is therefore directly identifiable:

`site -> experimental population -> individual -> treatment`

Population-level realised visitation (`visits.per.flower`) can be joined to individual reproductive-treatment rows by `experimental.population`. Context coordinates `site`, source population, `autonomy`, and `size` are represented on both sides and can be checked for consistency before fitting.

## Boundary

`visits.per.flower` is realised visitation at the experimental-population level, not stigma pollen receipt or donor identity. The next stage must hold out whole experimental populations so one population's shared visitation state cannot leak across train/test rows.

## Provenance

Schema artifact: `9552497285`, workflow `32819251801`. The discovery artifact contains hashes and headers only. No seed number, visit count, pollen-limitation value, effect direction, model or p-value was inspected in making this decision.
