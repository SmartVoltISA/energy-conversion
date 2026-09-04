# E-ENERGY-COMPUTATIONAL-CONTROL-001 — Cross-domain accounting

**Date:** 2026-09-04  
**Status:** COMPUTATIONAL RESULT  
**Purpose:** control experiment before physical construction

## Question

Does the proposed accounting structure close on standard ideal models when the system is represented as state → transition → stored/dissipated energy → new state?

## Models

- RC charge: source input = capacitor storage increase + resistor dissipation.
- RC discharge: initial capacitor storage = resistor dissipation + remaining capacitor energy.
- RL step: source input = inductor storage increase + resistor dissipation.
- RLC free response: initial stored energy = final stored energy + resistor dissipation.

## Results

| Model | Input / initial (J) | Stored final (J) | Dissipated (J) | Residual (J) |
|---|---:|---:|---:|---:|
| RC charge | 0.0249988650 | 0.0124988650 | 0.0124988650 | 1.13e-6 |
| RC discharge | 0.0125000000 | 0.0000000000* | 0.0125000000 | -1.59e-11 |
| RL step | 0.00497524979 | 0.0000125000 | 0.0049627500 | -2.08e-10 |
| RLC free | 0.0125000000 | 0.00461425103 | 0.00788574897 | -5.24e-13 |

*The RC discharge endpoint is finite-time (1 s), so the remaining capacitor energy is ~2.58e-11 J and is included in the residual at displayed precision.

## Interpretation

The accounting closes numerically for the ideal models. The small RC-charge residual is numerical endpoint/discretization error relative to ~25 mJ input and is not an unexplained energy term.

This is **not** evidence about nature beyond the equations used. It verifies that the proposed bookkeeping can represent known circuit dynamics without internally creating an energy term.

## Next test

The next computational target should be a history-dependent element (magnetic hysteresis / Preisach-type toy model), because that tests the stronger claim from E-ENERGY-0015: identical instantaneous observables can correspond to different future transitions when internal state/history differs.

Only after that should the physical bench be assembled.

**Calculation ≠ Experiment.**  
**Model result ≠ physical measurement.**  
**UNKNOWN ≠ TRUE.**
