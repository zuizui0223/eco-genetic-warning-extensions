# Eco-genetic warning extensions

Independent, predeclared biological closures for submitting and testing new
finite eco-genetic hypotheses.

## Why this is a separate repository

`eco-genetic-criticality` closed a finite-model campaign with three canonical
questions: interaction-conditioned high-trait viability (H1), fragmentation and
migration effects (H3), and a conditional relative-diversity warning result
(H2-R). Its numerical results are bounded by its declared symmetric mutation,
trait-recruitment, source-transfer, and deterioration closures.

This repository does **not** finish, broaden, or rewrite that campaign. It uses
identified boundary conditions to pose new biological mechanisms and new dynamic
hypotheses. No numerical output from the predecessor is evidence for this
repository.

## Paper program: mutation direction and eco-genetic warning

Paper 001 asks whether direction-specific recurrent mutation changes the
persistence boundary of a high-trait state, the realised trait-loss hazard, and
the reliability of relative genetic warnings.

The recurrent mutation operator is

\[
p_{t+1}^{\mathrm{mut}}
= u_{L\to H}+(1-u_{L\to H}-u_{H\to L})p_t.
\]

For the main campaign, it is parameterised as

\[
\kappa_\mu=u_{L\to H}+u_{H\to L},\qquad
p_\mu^\ast=\frac{u_{L\to H}}{\kappa_\mu},
\]

where \(\kappa_\mu\) controls mutation-map relaxation strength and
\(p_\mu^\ast\) controls its directionality. A fixed \(\kappa_\mu\) does not
imply fixed frequency-dependent mutation flux; that distinction is an explicit
part of the biological mechanism.

The principal paper question is therefore not “is the old H2-R result robust?”
It is:

> At fixed mutation relaxation strength, how does mutation direction alter
> high-trait persistence, realised trait loss, and genetic-warning reliability?

## Protocols

- **Protocol 001 — asymmetric recurrent mutation:** a three-anchor bridge/pilot
  (`SYM`, `UP`, `DOWN`) that locks the directional operator and verifies the
  exact symmetric bridge.
- **Protocol 002 — mutation-direction phase diagram:** the primary Paper 001
  campaign across 15 predeclared \((\kappa_\mu,p_\mu^\ast)\) coordinates, with
  independent source reconstruction, trait-loss-only calibration, and fresh-seed
  validation.

Both protocols preserve the same stage separation:

```text
new closure
-> independent H1 source reconstruction
-> trait-loss-only deterioration calibration
-> domain freeze
-> fresh-seed warning validation
-> fixed-threshold secondary audit
```

No genetic-warning value is used while selecting a deterioration schedule.

## Stage 0 certificate

Protocol 002 begins with an algebraic, no-simulation certificate for the 15
predeclared mutation coordinates:

```bash
protocol002 write-stage0 --output artifacts/protocol002/stage0_operator_certificate.json --force
```

The command records directional rates, contraction factors, mutation-only
equilibria, SYM bridge status, and expected mutation flux at \(p=0,0.5,1\). It
does not run source reconstruction, deterioration calibration, or warning
validation.

## Status

**Design and invariant-test stage. No new simulation result exists yet.**

See:

- [`docs/PROJECT_BOUNDARY.md`](docs/PROJECT_BOUNDARY.md)
- [`docs/HYPOTHESIS_PROGRAM.md`](docs/HYPOTHESIS_PROGRAM.md)
- [`docs/PAPER_001_MUTATION_DIRECTION_PHASE_DIAGRAM.md`](docs/PAPER_001_MUTATION_DIRECTION_PHASE_DIAGRAM.md)
- [`docs/PROTOCOL_001_ASYMMETRIC_MUTATION.md`](docs/PROTOCOL_001_ASYMMETRIC_MUTATION.md)
- [`docs/PROTOCOL_002_MUTATION_DIRECTION_PHASE_DIAGRAM.md`](docs/PROTOCOL_002_MUTATION_DIRECTION_PHASE_DIAGRAM.md)
- [`docs/NOVELTY_REVIEW_PROTOCOL.md`](docs/NOVELTY_REVIEW_PROTOCOL.md)
- [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md)

## Evidence labels

- **T** — theorem under explicitly stated mathematical assumptions.
- **C** — conditional theorem after a stated ecological closure.
- **H** — dynamic hypothesis.
- **S** — finite, model-specific simulation evidence.

All numerical outcomes produced by this repository are Type S unless a separate
proof establishes a different label.
