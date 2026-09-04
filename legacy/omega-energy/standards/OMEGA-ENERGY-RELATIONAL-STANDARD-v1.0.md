# OMEGA-ENERGY-RELATIONAL-STANDARD-v1.0

**Provenance:** migrated from `SmartVoltISA/Omega-lab-.--.-/00_CORE/STANDARDS/OMEGA-ENERGY-RELATIONAL-STANDARD-v1.0.md`  
**Status:** PROVISIONAL / CROSS-DOMAIN WORKING STANDARD  
**Migration date:** 2026-09-04

## Purpose

This document is a provisional working standard for the Ω-Lab energy branch. It defines common language and bookkeeping across relational, electrical, magnetic, mechanical and other conversion experiments. It is **not** a validated physical theory.

## Core distinctions

- symmetry ≠ energy;
- potential ≠ transferred energy;
- difference/gradient ≠ energy by itself;
- force/flux ≠ work;
- power ≠ energy;
- memory ≠ energy;
- model cost ≠ physical work;
- mathematical asymmetry ≠ physical irreversibility;
- source ≠ conversion mechanism;
- calculation ≠ experiment;
- UNKNOWN ≠ TRUE.

## Working relational chain

```text
STATE → DIFFERENCE / GRADIENT / POTENTIAL → COUPLING → FORCE / FLUX → WORK → POWER → NEW STATE
```

For conversion experiments, use:

```text
SOURCE → CARRIER → INTERACTION → CONVERTER → USEFUL OUTPUT
                                      ├→ STORAGE
                                      └→ REJECTED / DISSIPATED
```

## Energy accounting standard

For a defined system boundary:

```text
E_in - E_out = ΔE_system + E_rejected
```

A proposed conversion mechanism is not treated as demonstrated unless the relevant terms are independently defined/measured and the balance closes within stated uncertainty.

## State and memory

The effective state may include both present structure and persistent history:

```text
S_eff = (structure, memory, constraints)
```

Memory is treated as a state variable whose physical meaning must be identified before it is called energy or work.

## Directionality and irreversibility

Reversible structural rules do not by themselves establish physical time direction. Directionality must be connected to an explicit physical asymmetry, reservoir, irreversible process, dissipative channel, boundary condition, or constitutive law and then tested experimentally.

## Visualization convention

A provisional red/green/blue coding may be used for state visualization. These labels are not physical quantities and must not be interpreted as proof of three fundamental energetic states.

## Experimental requirements

Every closeout should identify:

1. system boundary;
2. initial and final states;
3. physical quantities and SI units;
4. input energy/work;
5. useful output;
6. stored/internal energy change;
7. rejected/dissipated energy;
8. measurement uncertainty;
9. controls and reversal where possible;
10. repeatability;
11. evidence status and provenance.

## Promotion rule

An abstract relational observation may generate a hypothesis, but promotion toward a physical claim requires a reproducible mapping to calibrated physical quantities and an independently closed energy account.

## Linked research position

The legacy Ω-Lab experiments are retained as provenance and hypothesis-generating evidence. The `energy-conversion` repository continues from them with explicit separation between abstract models and physical converter experiments.

**Rule:** do not claim energy creation, free energy, a new definition of physical energy, or universal energetic laws from toy relational models without a closed independent physical measurement.
