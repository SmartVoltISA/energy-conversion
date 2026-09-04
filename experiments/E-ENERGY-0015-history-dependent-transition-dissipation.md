# E-ENERGY-0015 — History-Dependent Transition / Dissipation Test

**Date:** 2026-09-04  
**Status:** COMPLETED — PRODUCTIVE / TOY MODEL  
**Type:** Native continuation of E-ENERGY-0014 / H-ENERGY-05

## Question

Can a stored difference (memory) make the cost of the same structural transition depend on history, thereby producing an effective asymmetry in time?

The experiment is deliberately separated from physical energy. `C` is a **model-defined transition cost**, not measured physical work.

## Minimal model

Use the same admissible four-node graph state space as E-ENERGY-0014. Add an internal memory variable `M` representing a persistent difference left by previous transitions.

The complete state is:

```text
STATE = (G, M)
```

A legal structural transition is the same one-edge toggle used in E-ENERGY-0014.

Define the transition cost:

```text
C = C0 + alpha*M
```

with `C0 = 1`, `alpha = 0.5`, and `M ∈ {0,1}` for the minimal mechanism-isolation test.

Thus the identical visible structural transition has:

```text
M = 0  →  C = 1.0
M = 1  →  C = 1.5
```

For the original forward/reverse demonstration, memory evolves with the transition:

```text
edge added:   M' = M + 1
edge removed: M' = max(0, M - 1)
```

Starting from `M=0`:

```text
forward: G0 → G1   C = 1.0, M → 1
reverse: G1 → G0   C = 1.5, M → 0
```

## Controls

### Control A — no memory coupling

Set `alpha = 0`.

Prediction and observed model behavior: `C = 1` regardless of memory. History cannot affect the transition cost.

### Control B — memory coupling enabled

Set `alpha = 0.5`.

Prediction: the same structural transition costs differently depending on `M`.

### Control C — expanded-state symmetry

Treat `(G,M)` as the actual state. The apparent asymmetry in the structural projection must not be confused with spontaneous asymmetry: it follows from the explicitly defined memory-dependent constitutive law.

## Result

**Supported by the toy model:** a persistent internal difference can make subsequent transition cost history-dependent.

The forward/reverse demonstration gives:

```text
forward cost  = 1.0
memory after  = 1.0
reverse cost  = 1.5
memory after  = 0.0
```

With `alpha=0`, forward and reverse costs are both `1.0`.

Therefore the stronger temporal asymmetry appears only when the additional memory variable is coupled into the transition rule.

## Accounting boundary

If an explicit external reservoir `R` pays the model cost, bookkeeping can be written:

```text
R_final = R_initial - ΣC
```

or, in work/energy-accounting notation for a future physical realization:

```text
W_in - W_out = ΔU_internal + E_rejected
```

The toy model closes its accounting **by construction**. This is not an emergent conservation result and `C` is not physical energy.

## Interpretation

This experiment supports the following narrow mechanism statement:

> A history-dependent state can create directional transition costs even when the underlying graph edit itself is reversible.

It does **not** establish:

- that memory is required for physical energy;
- that `C` is physical work;
- that dissipation has been experimentally demonstrated;
- that hysteresis is a universal source of energy;
- that the model generates energy;
- that the asymmetry appeared spontaneously.

The asymmetry is encoded by the chosen memory-dependent rule.

## Relation to E-ENERGY-0014

E-ENERGY-0014 showed that reversible structural graph dynamics alone do not produce intrinsic temporal direction: the structural transition graph is symmetric.

E-ENERGY-0015 adds the missing variable identified there:

```text
G → (G, M)
```

The result is a mathematical mechanism for history-dependent transition behavior. The next decisive step is therefore physical, not another abstract asymmetry model.

## Next decisive step

Replace the abstract cost `C` with a measurable physical quantity in a controlled converter. Candidate systems include a mechanical spring/damper, electrical RC/RL system, or magnetic actuator.

The physical experiment must independently measure:

- internal difference/state;
- memory/state history;
- input energy/work;
- useful output;
- rejected energy;
- force/flux and power versus time;
- uncertainty and repeatability;
- complete balance closure.

**UNKNOWN ≠ TRUE.**  
**Calculation ≠ Experiment.**  
**Model cost ≠ physical work.**
