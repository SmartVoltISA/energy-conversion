# EXP-0002 — Low-Voltage RC Energy Accounting

**Date:** 2026-09-04  
**Status:** PROTOCOL / NOT YET RUN  
**Parent:** EXP-0001

## 1. Objective

Validate the measurement architecture on a closed, low-voltage electrical system before testing more complex converters.

The experiment does **not** search for anomalous energy gain. It tests whether input, stored, useful and rejected energy can be separated and balanced within uncertainty.

## 2. System boundary

```text
DC SOURCE → SWITCH → R/C NETWORK → LOAD
             │          │             │
             └──────────┴─────────────┘
                       BOUNDARY
```

The exact physical boundary must be fixed before measurement. Instrument grounds, probe loading and power-supply return paths must be included in the boundary analysis.

## 3. Minimum state variables

- capacitor voltage `V_C(t)`;
- resistor/load voltage `V_R(t)`;
- current `I(t)`;
- elapsed time `t`;
- component temperature if it can materially affect the result.

## 4. Energy channels

Capacitor storage:

```text
E_C(t) = 1/2 C V_C(t)^2
```

Resistive dissipation:

```text
P_R(t) = V_R(t) I(t)
E_R = ∫ P_R(t) dt
```

Source input:

```text
E_in = ∫ V_in(t) I_in(t) dt
```

For a chosen boundary, every remaining channel must either be measured, independently calculated from calibrated parameters, or bounded with an explicit uncertainty term.

## 5. Required controls

### A — baseline

Measure the instrument and wiring system with the intended circuit but without the test mechanism under investigation.

### B — charge/discharge run

Charge the capacitor from the defined source, then discharge through the defined load.

### C — reversal

Where practical, reverse the charge/discharge sequence and verify that the accounting changes consistently with the state transition.

### D — null

Disconnect the capacitor or suppress the intended storage path while preserving measurement conditions as closely as possible.

## 6. Calibration

Before the run:

- verify voltage-channel calibration against a known reference;
- verify current-channel calibration against a known reference;
- record capacitor nominal value and tolerance;
- measure or obtain the resistor value and tolerance;
- record instrument sampling rate and timing uncertainty;
- record wiring and contact resistance where relevant.

## 7. Sampling

Use simultaneous voltage/current acquisition when possible. Sampling rate must be substantially faster than the fastest relevant transient. Store raw time-series data; derived energies must be reproducible from the raw record.

Do not round intermediate samples before numerical integration.

## 8. Balance test

For each run calculate:

```text
residual = E_in - E_useful - ΔE_storage - E_rejected
```

The experiment is a successful accounting validation when the residual is consistent with the combined measurement/model uncertainty.

An unexplained residual is **UNRESOLVED**, not evidence of excess energy.

## 9. Acceptance criteria

A run is valid only if:

1. the boundary is documented;
2. raw `V(t)` and `I(t)` data are preserved;
3. calibration records are attached;
4. component tolerances are included;
5. all identified energy channels are accounted for;
6. repeated runs agree within the predefined uncertainty budget;
7. the balance residual is within that budget.

## 10. Safety

Use only a low-voltage, current-limited supply and components rated for the test conditions. No mains voltage, high-energy capacitor bank or uncontrolled discharge is required for this protocol.

## 11. Result status

No experimental result is claimed until an actual run is performed and raw data are archived.

**Calculation ≠ Experiment.**  
**UNKNOWN ≠ TRUE.**
