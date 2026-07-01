# Decision log

## 2026-07-01 — project created

**Decision.** Start a separate repository for biological-closure robustness work
rather than extending `eco-genetic-criticality`.

**Reason.** The predecessor repository has a final finite-model evidence ledger.
Its symmetric mutation closure, calibration-selected domain, and H2-R result are
bounded claims. Changing mutation directionality would be a different closure,
not a small implementation refinement.

**Consequence.** This repository begins with a protocol and no inherited
numerical claim or code copy.

## 2026-07-01 — Protocol 001 chosen

**Decision.** First extension is asymmetric recurrent mutation with a fixed total
closure-unit mutation pressure and three predeclared directionality cases:
`SYM`, `UP`, and `DOWN`.

**Reason.** This changes one biologically interpretable mechanism while retaining
a regression bridge to the predecessor's symmetric operator.

**Consequence.** The protocol uses trait-loss-only calibration, fresh validation
seeds, all-six relative-warning endpoints, and a post-validation fixed-threshold
audit. No other mutation pair may be added without a new protocol.
