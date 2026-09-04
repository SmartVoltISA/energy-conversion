# EXP-0002 — Low-Voltage RC Energy Accounting

**Date:** 2026-09-04  
**Status:** READY FOR PHYSICAL RUN  
**Parent:** EXP-0001

## 1. Objective

Validate the measurement architecture on a closed, low-voltage electrical system before testing more complex converters.

The experiment does **not** search for anomalous energy gain. It tests whether input, capacitor storage, load dissipation and remaining losses can be separated and balanced within uncertainty.

## 2. Concrete bench configuration

Use a **5.00 V DC current-limited source**, a **1000 µF electrolytic capacitor rated ≥10 V**, and a **100 Ω resistor rated ≥0.5 W**.

Nominal capacitor storage at 5.00 V:

`E_C = 1/2 · 0.001 F · (5 V)^2 = 0.0125 J = 12.5 mJ`

Initial resistor power at 5 V:

`P_R = V²/R = 0.25 W`

The load is therefore intentionally low-energy and manageable on a normal laboratory bench.

### Wiring

```text
                 S1
+5 V ───────────/ ────────┬──── R = 100 Ω ────┐
                          │                    │
                          ├──── C = 1000 µF ──┤
                          │                    │
0 V ──────────────────────┴────────────────────┘
```

For charging, S1 connects the source to the RC network. For discharge, disconnect the source and connect the capacitor to the resistor/load through a separate switch or relay arrangement.

**Do not short the capacitor.** The resistor is the controlled discharge path.

## 3. System boundary

For the primary accounting run, define the boundary around the source, switching, capacitor, resistor, wiring and measurement channels as explicitly as the instrumentation permits.

If source energy is measured at the source terminals, the source-side wiring is outside the energy-transfer boundary; if measured at the supply output connector, state that boundary explicitly and keep it unchanged between runs.

Instrument grounds, probe loading and power-supply return paths must be documented.

## 4. Minimum state variables

Record:

- capacitor voltage `V_C(t)`;
- resistor voltage `V_R(t)`;
- current `I(t)`;
- source voltage `V_in(t)`;
- source current `I_in(t)`;
- elapsed time `t`;
- capacitor and resistor temperature if it can materially affect the result.

## 5. Energy channels

Capacitor storage:

```text
E_C(t) = 1/2 C_eff V_C(t)^2
```

Use measured/calibrated `C_eff` where available; do not silently substitute nominal capacitance when precision matters.

Resistor dissipation:

```text
P_R(t) = V_R(t) I(t)
E_R = ∫ P_R(t) dt
```

Source input:

```text
E_in = ∫ V_in(t) I_in(t) dt
```

For discharge-only accounting:

```text
E_C(initial) = E_R + E_other + ΔE_unaccounted
```

For a complete charge/discharge cycle:

```text
E_source = ΔE_C + E_R + E_other + E_residual
```

`E_other` includes identified wiring resistance, capacitor ESR, leakage, instrument loading and other losses that belong to the chosen boundary.

## 6. Primary run sequence

### Run 0 — Instrument zero / baseline

1. Record all instrument channels with the circuit unpowered.
2. Record offset and noise for the same acquisition duration used in the experiment.
3. Verify that current measurement does not report a significant false current with the circuit open.

### Run 1 — Charge

1. Start acquisition before switching the source.
2. Apply 5.00 V through the controlled source.
3. Charge the capacitor until `V_C` reaches approximately 5 V.
4. Stop source input and continue recording briefly to capture settling/leakage.
5. Calculate `E_in` by numerical integration of measured `V_in(t) I_in(t)`.
6. Calculate `ΔE_C` from measured capacitor voltage and calibrated capacitance.

### Run 2 — Controlled discharge

1. Start acquisition before closing the discharge path.
2. Disconnect the source.
3. Discharge the capacitor through 100 Ω.
4. Continue acquisition until `V_C < 0.1 V` or the predefined endpoint is reached.
5. Calculate `E_R = ∫V_R I dt`.
6. Compare discharged capacitor energy with resistor energy plus independently identified losses.

### Runs 3–7 — Repeat

Repeat the complete charge/discharge cycle at least five times without changing component values or measurement configuration.

## 7. Controls

### Control A — resistor-only

Run the source through the resistor without the capacitor storage path, using the same measurement channels. This estimates baseline source/load behavior.

### Control B — capacitor-only observation

Charge the capacitor with the same source and observe its voltage without intentionally extracting energy through the load. This estimates storage and leakage behavior.

### Control C — reversal

Where the switching arrangement allows it, reverse the sequence while maintaining the same measurement boundary. The expected change is in the state trajectory, not creation of energy.

## 8. Calibration

Before physical runs:

- verify voltage measurement against a known reference;
- verify current measurement against a known reference;
- measure the resistor with the available calibrated meter;
- measure capacitor value/ESR with an LCR meter if available;
- record component tolerances;
- record ADC/sample rate and timing uncertainty;
- record supply voltage stability and current-limit setting.

## 9. Sampling and numerical integration

Use simultaneous voltage/current acquisition where possible. Target at least **1 kS/s** for this slow RC system; higher sampling is preferable if available.

For the 100 Ω × 1000 µF nominal values:

`τ = RC = 0.1 s`

so 1 kS/s provides about 1000 samples per nominal time constant.

Store raw time-series data. Integrate using the recorded timestamps (trapezoidal integration is sufficient for the first pass). Do not round intermediate samples.

## 10. Uncertainty budget

At minimum include:

```text
u(E_in)
 u(E_C)
 u(E_R)
 u(E_other)
 u(E_residual)
```

For a first pass, propagate independent component/instrument uncertainties in quadrature where justified. If uncertainties are correlated, record the correlation assumption rather than treating them as independent.

The acceptance interval is defined before inspecting the final residual.

## 11. Balance decision rule

For each run calculate:

```text
residual = E_in - ΔE_C - E_R - E_other
```

and compare `|residual|` with the predefined combined uncertainty.

Classification:

- **BALANCED:** residual consistent with uncertainty;
- **OPEN ACCOUNT:** residual exceeds uncertainty and an identified channel is missing or inadequately measured;
- **UNRESOLVED:** residual exceeds uncertainty after identified channels are checked;
- **INVALID:** calibration, boundary or acquisition requirements failed.

An unexplained residual is **not** evidence of excess energy.

## 12. What would count as a useful result

The first success criterion is not efficiency. It is demonstrating that repeated runs close the energy account within uncertainty.

Only after that should we introduce a more interesting coupling or converter and ask whether the same state-transition architecture predicts a measurable difference.

## 13. Safety

Use only a low-voltage, current-limited supply. Verify capacitor polarity. Use a capacitor rated comfortably above the applied voltage. Use the 100 Ω discharge resistor; do not short the capacitor. No mains voltage or high-energy capacitor bank is part of this experiment.

## 14. Data package

Archive:

```text
EXP-0002/
├── protocol.md
├── raw/
│   ├── run_01.csv
│   ├── run_02.csv
│   └── ...
├── calibration.md
├── components.md
├── analysis.py
└── results.md
```

The raw files are primary evidence. Derived plots and energy values must be reproducible from them.

## 15. Result status

**No physical result is claimed yet.** This document defines a reproducible bench protocol.

**Calculation ≠ Experiment.**  
**UNKNOWN ≠ TRUE.**  
**Model cost ≠ physical work.**
