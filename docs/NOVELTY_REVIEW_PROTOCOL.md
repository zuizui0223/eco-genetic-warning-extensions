# Novelty review protocol — mandatory before a hypothesis is promoted

## Status

**Protocol 001's mathematical hypothesis is declared; its literature-level novelty
claim is not yet declared.** No README, paper, PR description, or result summary
may call H2-R-AS "novel" until this review is completed and archived.

## Why this gate exists

Directional mutation, mutation bias, evolutionary rescue, genetic erosion, and
early-warning analysis are each established research areas. The potential
contribution of Protocol 001 is therefore not any one of those concepts alone.
The review must determine whether the specific conjunction below has already been
analysed:

```text
directional recurrent mutation
+ finite stochastic drift
+ explicit ecological interaction feedback
+ realised trait-loss first passage as the event
+ relative H-alpha / H-gamma first passages as warnings
+ trait-loss-only calibration before warning evaluation
+ independent fresh-seed validation with censoring retained
```

## Search sources

Search independently in Web of Science Core Collection, Scopus, PubMed, OpenAlex,
Crossref, and Google Scholar. Record search date, exact query, database, returned
count, duplicate count, screening decision, and reason for exclusion.

## Search families

Run each family in title/abstract/keyword fields where the database permits it.

1. `("early warning" OR "early-warning" OR "critical transition" OR tipping OR collapse)
   AND (genetic OR genomic OR heterozygosity OR "genetic diversity")`
2. `("evolutionary rescue" OR eco-evolutionary OR "eco genetic")
   AND (mutation OR "mutation bias" OR "asymmetric mutation" OR "directional mutation")`
3. `("trait loss" OR phenotypic OR trait OR viability OR persistence)
   AND (heterozygosity OR diversity OR allele) AND (warning OR first-passage OR lead)`
4. `(fragmentation OR metapopulation OR spatial OR patch)
   AND (mutation OR genetic diversity) AND (warning OR collapse OR transition)`

Use forward and backward citation chasing from every included review and every
candidate model paper.

## Eligibility rules

Include a study if it provides a model, empirical analysis, or formal review that
connects at least two of: mutation directionality; eco-evolutionary feedback;
genetic-diversity warning; ecological/trait-loss event; finite stochasticity;
spatial structure; censoring or event-time inference.

Exclude a study only with a recorded reason, including: no genetic state, no
warning/event ordering, non-biological optimisation algorithm, duplicate,
conference abstract without methods, or inaccessible record with insufficient
metadata.

## Comparison matrix

For each included study record:

| field | required entry |
|---|---|
| ecological event | exact event and whether it is first passage |
| genetic state | allele frequency, heterozygosity, genome-wide diversity, or other |
| mutation mechanism | absent, symmetric, directional/asymmetric, state dependent, or unspecified |
| eco-evolutionary coupling | none, one-way, or bidirectional |
| population closure | deterministic/stochastic; finite/infinite; spatial/non-spatial |
| warning definition | metric, threshold, trend, or classifier |
| calibration separation | whether event calibration is blind to warning outcomes |
| validation | same data, held-out replication, or independent seed/data |
| censoring | retained, excluded, or unreported |
| closest overlap with Protocol 001 | precise statement |
| remaining distinction | precise statement, or `none` |

## Permitted novelty statement

Only after the matrix is complete may the project use one of these outcomes:

1. **Distinct combination found.** State exactly which combination is new and cite
   the nearest prior studies.
2. **Partial precedent found.** Narrow the hypothesis and state what is replicated
   versus newly combined.
3. **Direct precedent found.** Do not claim novelty; reposition Protocol 001 as an
   independent replication, boundary test, or implementation audit.

The final statement must never claim that directional mutation or genetic warning
in general is new.
