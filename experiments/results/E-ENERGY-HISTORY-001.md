# E-ENERGY-HISTORY-001 — Hidden-state counterexample

**Status:** COMPUTATIONAL RESULT

## Question
Can two histories produce the same visible state but different future transition costs when an internal memory variable is present?

## Result
Yes, in the deliberately defined toy model. The paths `0 → +1 → -1 → 0` and `0 → -1 → +1 → 0` end at the same visible state `x=0`, but retain opposite internal memory values `m=-0.128` and `m=+0.128`. The same next visible transition `x: 0 → 1` therefore has different model-defined costs: `0.936` versus `1.064`.

## Interpretation
This is a structural counterexample to a **visible-state-only** representation: `x` alone is not a sufficient state variable once history/internal memory affects future transitions.

It is **not** evidence that physical energy is history-dependent in this particular numerical form. The cost law is explicitly chosen by the toy model. The useful result is architectural: if a real physical system has hysteresis or another internal state, that state must be included in the system description before energy transfer can be accounted for correctly.

## Accounting warning
If `m` is omitted from the boundary, a difference in transition cost can look like unexplained energy. Once the internal state/reservoir is represented, the apparent anomaly becomes an accounted state-dependent term. This motivates the next experiment: deliberately omit the hidden state, measure the apparent residual, then restore it and test whether the residual closes.

**Calculation ≠ Experiment.**
**Model result ≠ physical measurement.**
**UNKNOWN ≠ TRUE.**
