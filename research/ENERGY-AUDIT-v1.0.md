# ENERGY AUDIT v1.0

**Date:** 2026-09-04  
**Status:** ACTIVE RESEARCH MAP / AUDIT  
**Scope:** architecture, legacy Ω-Lab experiments, native experiments, physical bridges, provenance

## 1. Purpose

This document audits the energy branch as a connected research graph rather than a list of files.

The governing chain is:

```text
DISTINCTION → RELATION → STATE → TRANSITION → TRANSFER → CONVERSION → OUTPUT → BALANCE → VERIFICATION
```

Epistemic rules:

- UNKNOWN ≠ TRUE
- Hypothesis ≠ Result
- Calculation ≠ Experiment
- Model cost ≠ physical work
- Correlation ≠ mechanism
- Local release ≠ energy creation
- Conservation ≠ efficiency
- Shorter path ≠ automatically better conversion

## 2. Architecture graph

```text
                         ┌──────────────┐
                         │ PHYSICAL      │
                         │ SYSTEM        │
                         └──────┬───────┘
                                │
                         ┌──────▼───────┐
                         │ STATE         │
                         │ structure +   │
                         │ internal state│
                         └──────┬────────┘
                                │
             ┌──────────────────┼──────────────────┐
             ▼                  ▼                  ▼
         DIFFERENCE          MEMORY             CONSTRAINT
             │                  │                  │
             ▼                  ▼                  ▼
          GRADIENT        HISTORY/STATE         BARRIER
             │                  │                  │
             └──────────┬───────┴──────────┬───────┘
                        ▼                  ▼
                     COUPLING         ACCESSIBLE CHANGE
                        │                  │
                        └────────┬─────────┘
                                 ▼
                           FORCE / FLUX
                                 │
                                 ▼
                               WORK
                                 │
                                 ▼
                              POWER
                                 │
                                 ▼
                         NEW PHYSICAL STATE
                                 │
                         ┌───────┴────────┐
                         ▼                ▼
                      STORAGE          REJECTED
                         │                │
                         └───────┬────────┘
                                 ▼
                              BALANCE
                                 │
                                 ▼
                            VERIFICATION
```

Physical conversion graph:

```text
SOURCE → CARRIER → INTERACTION → CONVERTER → USEFUL OUTPUT
                                      ├────→ STORAGE
                                      └────→ REJECTED
```

Required accounting:

`E_in - E_out = ΔE_system + E_rejected`

or, for an explicitly defined boundary:

`E_in = E_useful + ΔE_storage + E_rejected`.

## 3. Evidence layers

### Layer A — established physical concepts

Energy, work, heat, power, force, fields, potentials, fluxes, conservation and thermodynamic accounting are established physical concepts. The repository uses them as the external reference layer, not as discoveries of Ω-Lab.

### Layer B — relational research scaffold

The properties map proposes connections among state, difference, potential, memory, coupling, transition, work and balance. It is a research scaffold, not a finished physical theory.

### Layer C — toy-model evidence

Experiments 0010–0037 test structural analogues: transformation capacity, transfer, symmetry, barriers, memory, redistribution, channelization and bifurcation. Their strongest value is hypothesis reduction and mechanism isolation.

### Layer D — physical bridge

Lightning/electromagnetic work and EXP-0001 define measurable physical boundaries and conversion accounting. These are the bridge from abstract relational models to calibrated physical tests.

## 4. Legacy experiment graph

```text
0010 Structural Potential
  │
  ▼
0011 Transfer / conditional conservation
  │
  ▼
0012 Binding symmetry ──→ structure alone insufficient
  │
  ▼
0013 No-Go: reversible structure lacks directionality
  │
  ├───────────────┐
  ▼               ▼
0020–0021       0022–0025
barriers        history / memory
  │               │
  └───────┬───────┘
          ▼
0026 Transfer between coupled systems
          │
          ▼
0027 Candidate invariant
          │
          ▼
0028 Conservation + barrier
          │
          ▼
0029 Directionality requires extra mechanism
          │
          ▼
0030 Local release can be redistribution
          │
          ▼
0031 Resource → feedback → channel
          │
          ▼
0032 Memory-assisted channel
          │
          ├── 0032R reproduction failure / unresolved exact numbers
          ▼
0033 Spatial channel
          ▼
0034–0035 operational state / memory representation
          ▼
0036–0037 state differentiation / bifurcation
```

## 5. Native continuation

```text
0013 NO-GO
   ↓
0014 Transition Cost from State
   ↓
0015 History-Dependent Transition / Dissipation Test
   ↓
EXP-0001 Physical Energy Accounting
   ↓
physical converter
```

E-ENERGY-0014 exhaustively tests the four-node admissible state space. The verified target is 38 admissible states, 84 undirected one-step transitions, local transition capacity P=3..6, and symmetric shortest-path distance. A reproducibility script is now stored under `experiments/code/e_energy_0014_repro.py`.

E-ENERGY-0015 isolates history dependence using an explicit memory variable and model cost. It shows a mechanism for path-dependent transition cost but does not establish physical energy or spontaneous asymmetry.

## 6. What survived the audit

1. Static relational structure can have different transformation capacity under specified rules.
2. A structural observable can be redistributed in selected toy transitions, but is not automatically conserved.
3. Reversible structural rules alone do not produce energetic directionality.
4. Transition barrier is distinct from transformation capacity.
5. Conservation and barrier are logically separable.
6. Local apparent release must be checked against the complete accounting boundary.
7. Memory/history can be part of effective state and alter future transitions.
8. Channelization can emerge in toy systems with limited resource, feedback and memory.
9. 0032 exact numerical reproduction remains unresolved; original and reproduction must remain separate.
10. State differentiation/bifurcation is not equivalent to energy release.
11. A physical interpretation requires measurable variables and independent energy accounting.

## 7. Major audit warnings

### 0032 / 0032R

The original 0032 numerical result is not independently reproduced. It must not be promoted to established quantitative evidence.

### 0036

The migrated compact record currently claims emergence of three states. Provenance must be reconciled against the authoritative Ω-Lab source before this is used as evidence. Until reconciliation, mark the stronger claim as provenance-sensitive.

### 0037

The migrated compact record preserves the qualitative bifurcation conclusion but omits the detailed quantitative source record. The primary source should be preserved separately before quantitative reuse.

### 0014–0019

Do not manufacture legacy files for the numbering gap. E-ENERGY-0014 in the new repository is a native continuation, not a recovered legacy experiment.

### 0015 duplicates

There have been two filenames/versions of the 0015 record. They must be normalized to one canonical experiment record and one optional archived draft, not treated as two experiments.

## 8. Physical bridge graph

The electromagnetic/lightning branch gives a concrete testable chain:

```text
ENVIRONMENT
   ↓
gradient / field / difference
   ↓
potential
   ↓
storage / coupling
   ↓
threshold / asymmetry
   ↓
restructuring / discharge / motion
   ↓
changed state
   ↓
measurable output + rejected energy
```

For the atmospheric-field example, field magnitude alone does not imply useful harvestable power; geometry, conductivity, leakage and coupling determine the usable scale. The safe lightning analogue is a controlled low-energy capacitor/discharge experiment, not natural-lightning capture.

## 9. Research gaps

The audit identifies five decisive gaps:

1. **Physical mapping:** connect an abstract state variable to a calibrated physical observable.
2. **Constitutive law:** specify how a difference/coupling produces force or flux.
3. **Energy identity:** demonstrate that the measured quantity corresponds to energy/work in joules, not only to a model score.
4. **Independent balance:** measure input, useful output, internal storage change and rejected energy independently.
5. **Reproducibility:** make every numerical claim executable from source-controlled code and parameters.

## 10. Next experiment selection rule

Prefer the physical converter that maximizes:

`measurement completeness × repeatability × controllability × safety`

and minimizes:

`hidden degrees of freedom × uncontrolled environmental coupling × ambiguous boundary`.

This favors a low-energy electrical or magnetic bench experiment before any attempt at large-energy phenomena.

## 11. Current graph conclusion

The research has moved through a useful sequence:

```text
STRUCTURE
   ↓
TRANSFORMATION CAPACITY
   ↓
TRANSFER
   ↓
NO-GO FOR SIMPLE REVERSIBLE DIRECTIONALITY
   ↓
BARRIER
   ↓
HISTORY / MEMORY
   ↓
PATH DEPENDENCE
   ↓
ACCOUNTING
   ↓
PHYSICAL CONVERTER
```

The unresolved central edge is:

`MEASURABLE DIFFERENCE + PHYSICAL COUPLING → MEASURABLE ENERGY TRANSFER`.

That is now the highest-value experimental target.
