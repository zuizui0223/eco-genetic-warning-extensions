# Protocol 002 mutation-slot regression fixture

## Purpose

This fixture is the first deterministic runner after the upstream-adapter
contract. It checks the single life-cycle operation that Protocol 002 is allowed
to change: the post-migration, pre-drift mutation transform.

## What the fixture does

Given an initial post-migration allele frequency \(p_0\), the fixture iterates
only the mutation slot:

\[
p_{t+1}=M(p_t).
\]

For Protocol 002,

\[
M(p)=\kappa_\mu p_\mu^\ast+(1-\kappa_\mu)p.
\]

For the pinned upstream symmetric reference,

\[
M_{\rm sym}(p)=\mu+(1-2\mu)p.
\]

The SYM bridge requires

\[
\kappa_\mu=2\mu,\qquad p_\mu^\ast=0.5,
\]

which makes the two mutation-slot trajectories identical for every starting
frequency and every number of fixture generations, up to floating-point
tolerance.

## What the fixture does not do

- no ecological interaction update;
- no selection;
- no migration beyond accepting the already post-migration frequency;
- no finite genetic drift;
- no trait recruitment;
- no source reconstruction;
- no deterioration schedule;
- no diversity warning calculation.

Therefore, this fixture is not Stage I and produces no Type S ecological result.
It is only a regression gate proving that the local mutation replacement is
algebraically compatible with the pinned symmetric closure.

## Next gate

After this fixture passes, the next PR should introduce a minimal finite-life-
cycle runner with deterministic drift disabled or controlled by a fixed fixture.
That runner must still prove SYM equivalence before any H1 source reconstruction
campaign is started.
