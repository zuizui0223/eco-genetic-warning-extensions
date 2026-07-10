# Protocol 002 minimal life-cycle fixture

## Purpose

This fixture fixes the local ordering required before Protocol 002 can move
toward Stage I source reconstruction:

```text
resident frequency
-> deterministic selection fixture
-> deterministic migration fixture
-> mutation slot
-> deterministic/no-op drift fixture
```

It is still not the full eco-genetic simulator. It is a regression gate showing
that the Protocol 002 mutation coordinate can be inserted at the declared
post-migration, pre-drift position without changing the symmetric bridge.

## Symmetric bridge requirement

For the pinned upstream symmetric mutation map

\[
p\mapsto \mu+(1-2\mu)p,
\]

Protocol 002 uses

\[
\kappa_\mu=2\mu,\qquad p_\mu^\ast=0.5.
\]

The fixture requires Protocol 002 and the upstream symmetric reference to return
identical per-generation states when they share the same deterministic
selection, migration, and drift fixtures.

## What is intentionally absent

- no stochastic finite drift;
- no ecological interaction dynamics;
- no trait recruitment;
- no source transfer;
- no barrier deterioration;
- no diversity metrics;
- no warning or trait-loss event calculation.

Therefore this fixture produces no Type S ecological evidence. Its only purpose
is to lock the life-cycle insertion order before the first H1 source-reconstruction
runner is introduced.

## Next gate

The next gate is a deterministic H1-source-runner skeleton that records source
attempt statuses and artifact schemas, still without launching the full Protocol
002 source grid. Once that skeleton is stable, the declared Stage I source seeds
can be run in a separate campaign PR.
