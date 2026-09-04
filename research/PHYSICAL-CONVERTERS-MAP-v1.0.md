# PHYSICAL CONVERTERS MAP v1.0

**Date:** 2026-09-04  
**Purpose:** choose the first physical experiment for EXP-0001 using measurement completeness, not novelty.

## Selection rule

The first converter should make the following chain experimentally visible:

```text
MEASURABLE DIFFERENCE
        ↓
PHYSICAL COUPLING
        ↓
FORCE / FLUX / CURRENT / FLOW
        ↓
USEFUL WORK OR EXPORTED ENERGY
        ↓
REJECTED ENERGY + INTERNAL STORAGE
        ↓
CLOSED BALANCE
```

The experiment is successful epistemically only when the measured quantities map to SI quantities and the system boundary is explicit.

## Candidate map

| Family | Driving difference / potential | Coupling | Useful output | Main rejected/storage channels | Measurement completeness | First-test suitability |
|---|---|---|---|---|---|---|
| Electrical RC | Voltage difference / electric field | Capacitive current | Electrical energy delivered to load | ESR heat, leakage, capacitor stored energy | Very high | **Excellent** |
| Electrical RL | Voltage/current difference | Inductive coupling | Electrical/mechanical output depending on load | Coil resistance, magnetic stored energy | High | **Excellent** |
| Magnetic actuator | Magnetic field configuration / current | Force/torque | Mechanical work | Copper loss, hysteresis, eddy currents, magnetic storage | High | **Excellent** |
| Mechanical spring/damper | Displacement/force difference | Elastic/dissipative force | Mechanical work | Spring storage, friction, heat | Very high | **Excellent** |
| Thermal engine | Temperature difference | Heat transfer + expansion/pressure | Mechanical/electrical work | Heat rejection, internal energy, friction | Medium–high | Moderate |
| Photovoltaic | Electromagnetic/radiative flux | Semiconductor carrier generation | Electrical power | Reflection, thermalization, recombination | Medium–high | Moderate |
| Electrochemical | Chemical potential difference | Charge-transfer reactions | Electrical work | Polarization, heat, chemical storage | Medium | Moderate |
| Nuclear heat cycle | Nuclear binding-energy change | Nuclear reaction + heat transport | Heat → mechanical/electrical work | Radiation, heat rejection, activation products | Lower for a small lab | **Not first** |

## Why electrical/mechanical/magnetic first

These families allow the boundary to be made small and explicit, use calibrated laboratory instruments, and permit time-resolved measurement of both state and power. They also allow reversal and null controls without introducing a large uncontrolled environmental energy source.

## Candidate A — RC converter

### Minimal architecture

```text
DC SOURCE → SWITCH → R/C NETWORK → LOAD
                         │
                         └→ STORAGE / LOSS
```

### Direct measurements

- `V(t)` across relevant elements;
- `I(t)` through the circuit;
- elapsed time;
- component temperature where needed.

### Energy reconstruction

For a capacitor:

```text
E_C = 1/2 C V²
```

For a resistor:

```text
P_R(t) = V(t) I(t)
E_R = ∫ P_R(t) dt
```

This gives a clean first test of the accounting architecture because electrical input, stored field energy and dissipated energy can all be measured or independently calculated from calibrated quantities.

## Candidate B — spring/damper

### Minimal architecture

```text
ACTUATOR → SPRING / DAMPER → MASS / LOAD
             │
             └→ STORED / DISSIPATED ENERGY
```

Measure force and displacement directly. Mechanical work is reconstructed from:

```text
W = ∫ F dx
```

A spring provides a particularly clear reversible-storage control, while a damper provides a deliberately irreversible channel. This is useful for separating storage from dissipation.

## Candidate C — magnetic actuator

### Minimal architecture

```text
ELECTRICAL INPUT → COIL + MAGNETIC CIRCUIT → FORCE / TORQUE → MECHANICAL LOAD
                         │                         │
                         ├→ magnetic storage       └→ useful work
                         └→ copper / core losses
```

Measure electrical input power and mechanical output independently. Where possible, measure current, voltage, displacement/angle, force/torque and temperature. This candidate is especially valuable for testing the Ω-Lab magnetic-loop hypothesis without using uncontrolled environmental energy.

## Decision

**First physical implementation: start with a low-voltage RC experiment.**

Reason: it has the smallest controllable boundary and the simplest independent accounting. Use the RC test to validate the measurement protocol before moving to magnetic or mechanical coupling.

The first experiment must not attempt to demonstrate anomalous gain. Its purpose is to validate that the architecture can distinguish:

```text
INPUT ENERGY
vs
STORED ENERGY
vs
USEFUL OUTPUT
vs
REJECTED ENERGY
```

Only after this accounting chain closes should a more complex converter be tested.

## Falsification / failure criteria

The protocol is considered inadequate if:

- the system boundary cannot be defined;
- a relevant energy channel is unmeasured and cannot be bounded;
- the result depends on an uncalibrated instrument;
- input and output use incompatible reference conditions;
- repeated runs do not reproduce within stated uncertainty;
- an apparent energy excess disappears after accounting for storage, instrument loading, wiring losses, leakage or timing.

## Next experiment

Create `EXP-0002` as a concrete low-voltage RC energy-accounting protocol with:

1. component values and tolerances;
2. instrument specifications;
3. wiring topology;
4. sampling plan;
5. calibration checks;
6. baseline/control/mechanism runs;
7. numerical integration method;
8. uncertainty budget;
9. acceptance criterion for balance closure.

**Boundary:** this map selects an experimental platform. It does not claim that any converter creates energy or reveals a new energy law.
