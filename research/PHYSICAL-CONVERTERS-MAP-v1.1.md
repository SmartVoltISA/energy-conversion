# PHYSICAL CONVERTERS MAP v1.1

**Date:** 2026-09-04

## Selection rule

Choose the first physical test by measurement completeness, controllability, safety, repeatability and a clearly closed system boundary — not novelty.

| Converter | Coupling | Storage/state | Main loss channels | First-test suitability |
|---|---|---|---|---|
| **RC electrical** | electric field ↔ current | capacitor charge/voltage | resistor heat, ESR, leakage, wiring, instrument loading | **Best** |
| RL electrical | magnetic field ↔ current | inductor current/flux | winding/core losses | Very good |
| Mechanical spring/damper | elastic force ↔ motion | displacement/strain | friction, air drag, heat | Very good |
| Magnetic actuator | magnetic field ↔ force/torque | field/mechanical state | copper, eddy/core losses | Good |
| Photovoltaic | radiation ↔ charge transport | electrical state | reflection, heat, recombination | Moderate |
| Thermal engine | thermal ↔ mechanical | thermal/internal energy | heat rejection, friction | Poor first test |
| Fuel cell | chemical ↔ electrical | chemical/internal state | heat, activation/ohmic losses | Moderate |
| Nuclear cycle | nuclear → thermal → work | thermal state | heat/radiation | Unsuitable first test |

## Decision

**RC → EXP-0002.** It provides an explicit storage state `E_C = 1/2 C V²`, directly measurable voltage/current, a characterizable dissipative element and safe low-voltage operation.

## Bridge under test

```text
MEASURABLE DIFFERENCE
        ↓
PHYSICAL COUPLING
        ↓
MEASURABLE CURRENT / FLOW
        ↓
TRANSFER / WORK
        ↓
STORAGE + REJECTED ENERGY
        ↓
BALANCE + UNCERTAINTY
```

## Boundary

For a complete charge/discharge run:

```text
E_source = ΔE_capacitor + E_load + E_other
```

`E_other` must include measured or bounded leakage, ESR/wiring loss, switching loss and instrument loading where material.

A residual outside the uncertainty budget is **UNRESOLVED** until the missing channel or measurement error is independently resolved.

## Next

Run EXP-0002 with low-voltage isolated DC, synchronized `V(t)`/`I(t)` acquisition, component characterization, repeated cycles and explicit uncertainty propagation.
