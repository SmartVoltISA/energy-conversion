# E-ENERGY-HIDDEN-BOUNDARY-001 — Apparent residual from omitted internal state

**Status:** COMPUTATIONAL RESULT  
**Model:** deliberately defined toy state + hidden reservoir

## Question
If an internal state is omitted from the system boundary, does the energy account produce an apparent residual that disappears when the hidden state is restored?

## Protocol
The complete state is `(x,m)`.

- visible storage: `E_visible = 0.5*x²`
- hidden reservoir: `E_hidden = 0.5*m²`
- complete input is defined as the change in `E_visible + E_hidden`

Two histories were replayed:

- positive: `0 → +1 → −1 → 0 → +1`
- negative: `0 → −1 → +1 → 0 → +1`

Both finish at the same visible state `x=+1`, but their hidden states differ.

## Results

| History | E_input | ΔE_visible | ΔE_hidden | residual visible-only | residual full |
|---|---:|---:|---:|---:|---:|
| positive | 0.595703125 | 0.500000000 | 0.095703125 | 0.095703125 | 0 |
| negative | 0.658203125 | 0.500000000 | 0.158203125 | 0.158203125 | 0 |

The visible-only account therefore reports a nonzero residual, while the full `(x,m)` account closes exactly to numerical precision.

## Interpretation

The experiment confirms a **structural statement inside this toy model**:

> Omitting a state variable that stores transferable/accountable state can create an apparent unexplained energy term.

The residual is not newly generated energy. It is exactly the omitted change in the hidden reservoir.

The result strengthens the architectural requirement that the system boundary must include relevant internal state when performing energy accounting. It does **not** establish that any particular physical material has the chosen `m` dynamics or reservoir law.

## Important limitation

This is intentionally constructed. The input-energy law and hidden reservoir are part of the model definition. Therefore this is a test of accounting architecture, not a discovery of a new physical effect.

## Next test

Replace the abstract `m` with a physically grounded history-dependent element (for example, magnetic hysteresis) and test whether independently measurable input/output data require an internal state for closure.

**Calculation ≠ Experiment.**  
**Model result ≠ physical measurement.**  
**UNKNOWN ≠ TRUE.**
