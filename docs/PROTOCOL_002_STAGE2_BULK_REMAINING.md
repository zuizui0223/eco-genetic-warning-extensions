# Protocol 002 Stage II bulk remaining submission

The remaining calibration campaign covers batch indices 20–809.

```text
790 batches × 25 attempts = 19,750 attempts
```

GitHub Actions permits at most 256 jobs in one matrix. The submission therefore
uses one workflow containing four independent matrices:

```text
20–275   = 256 batches
276–531  = 256 batches
532–787  = 256 batches
788–809  = 22 batches
```

All matrices use `fail-fast: false`. Each job writes and uploads one retained
trait-loss-only Stage II batch artifact. Failed batches can therefore be rerun
without discarding successful artifacts.

No warning, diversity, lead/lag, or event-pair endpoints are inspected.
