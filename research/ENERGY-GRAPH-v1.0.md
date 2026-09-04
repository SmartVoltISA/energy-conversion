# ENERGY GRAPH v1.0

**Date:** 2026-09-04  
**Status:** WORKING GRAPH / AUDIT OUTPUT

## Master graph

```text
                         PHYSICAL SYSTEM
                                │
                                ▼
                             STATE
                  ┌─────────────┼─────────────┐
                  ▼             ▼             ▼
             STRUCTURE       MEMORY       CONSTRAINT
                  │             │             │
                  └──────┬──────┴──────┬──────┘
                         ▼             ▼
                      DIFFERENCE     BARRIER
                         │             │
                         ▼             │
                     POTENTIAL        │
                         │             │
                    GRADIENT/FIELD    │
                         │             │
                         └──────┬──────┘
                                ▼
                             COUPLING
                                │
                         ┌──────┴──────┐
                         ▼             ▼
                       FORCE         FLUX
                         │             │
                         └──────┬──────┘
                                ▼
                              WORK
                                │
                              TIME
                                │
                                ▼
                             POWER
                                │
                                ▼
                         NEW SYSTEM STATE
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
                 STORAGE                 REJECTED
                    │                       │
                    └──────────┬────────────┘
                               ▼
                            BALANCE
                               │
                               ▼
                         VERIFICATION
```

## Experiment anchors

```text
0010 ── structure → transformation capacity
  │
0011 ── transfer / conditional invariant
  │
0012 ── binding symmetry → structure insufficient
  │
0013 ── reversible no-go
  │
0014 ── transition graph symmetry
  │
0015 ── memory → path-dependent model cost
  │
  ▼
EXP-0001 ── physical energy accounting
  │
  ▼
PHYSICAL CONVERTER
```

Parallel legacy branch:

```text
0020–0021 → barriers
0022–0025 → history / memory / effective state
0026–0028 → transfer / invariant / conservation boundary
0029       → directionality
0030       → redistribution
0031–0035 → channel / spatial organization / memory representation
0036–0037 → state differentiation / bifurcation
```

Physical bridge:

```text
ENVIRONMENT / SOURCE
        ↓
   ENERGY CARRIER
        ↓
     DIFFERENCE
        ↓
      COUPLING
        ↓
   TRANSITION / FLOW
        ↓
     CONVERTER
        ↓
 USEFUL OUTPUT
        ├── STORAGE
        └── REJECTED ENERGY
        ↓
      BALANCE
        ↓
   MEASUREMENT
```

## Critical missing edge

The graph is structurally complete enough to define the research program, but one edge remains experimentally unresolved:

`MEASURABLE DIFFERENCE + PHYSICAL COUPLING → MEASURABLE ENERGY TRANSFER`

Everything after that edge must be tied to SI units, calibrated instruments, defined system boundaries and uncertainty.

## Status semantics

- **KNOWN:** established physical concept/result.
- **CALCULATED:** follows from an explicit model and inputs.
- **OBSERVED:** measured under a defined protocol.
- **HYPOTHESIS:** proposed relation awaiting test.
- **UNKNOWN:** unresolved.
- **REJECTED:** contradicted under stated conditions.
- **UNVERIFIED:** claimed result lacking successful independent reproduction.

## Guardrail

A graph edge is not evidence merely because it is visually plausible. Each research edge must have provenance and an evidence status.
