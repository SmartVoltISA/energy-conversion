# E-ENERGY-0015 — History-Dependent Transition / Dissipation Test

**Status:** TOY MODEL / OPEN — mechanism isolation
**Type:** Native continuation of E-ENERGY-0014
**Date:** 2026-09-04

## 1. Question

Can a stored difference (memory) make the cost of the same structural transition depend on history, thereby producing an effective asymmetry in time?

The experiment is deliberately separated from physical energy. `C` below is a **model-defined transition cost**, not measured physical work.

## 2. Working model

The complete state is:

`STATE = (G, M)`

where:

- `G` — structural state (the graph),
- `M` — stored memory representing a persistent difference left by previous transitions.

A legal structural transition is the same one-edge toggle used in E-ENERGY-0014.

The constitutive rule is:

`C = C0 + alpha*M`

with:

`C0 = 1`, `alpha = 0.5`, `M ∈ {0,1}`.

Therefore the identical structural transition has:

- `C = 1.0` when `M = 0`;
- `C = 1.5` when `M = 1`.

This is the minimal test of the statement that **memory is a preserved difference**: the structural state can be identical while the complete state is different.

## 3. Controls

### Control A — no memory coupling

Set `alpha = 0`.

Prediction: `C = 1` regardless of memory. History cannot affect the transition cost.

### Control B — memory coupling enabled

Set `alpha = 0.5`.

Prediction: the same `G → G'` transition costs differently depending on `M`.

### Control C — expanded-state symmetry

Treat `(G,M)` as the actual state. The apparent asymmetry in the structural projection must not be confused with spontaneous asymmetry: it follows from the explicitly defined memory-dependent constitutive law.

## 4. Minimal result

For the same structural transition `G → G'`:

| Memory | Model cost C |
|---:|---:|
| 0 | 1.0 |
| 1 | 1.5 |

Thus a prior history that leaves `M=1` changes the subsequent transition cost without changing `G` itself.

With `alpha=0`, both cases give `C=1.0`.

## 5. Interpretation

**Supported by the toy model:**

1. A persistent difference can be represented as an internal memory variable.
2. Once memory is part of the state, transition behavior can depend on history.
3. The same visible structural transition can therefore have different model costs at different times.
4. An apparent temporal asymmetry can emerge in the structural projection even though the underlying structural edit itself remains reversible.

**Not established:**

- `C` is physical energy;
- `C` is physical work;
- dissipation has been experimentally demonstrated;
- a conservation law has emerged;
- asymmetry appeared spontaneously.

The asymmetry is **encoded by the memory-dependent rule**. This is a mechanism-isolation result, not a discovery of a new physical law.

## 6. Balance

If an explicit external reservoir `R` pays the model cost, bookkeeping can be written:

`R_final = R_initial - ΣC`

and the corresponding system transition records the same modeled cost.

This closes the accounting **by construction**. It must not be presented as an emergent conservation result.

The physical research target is stronger:

`external exchange ↔ internal difference ↔ memory ↔ state transition ↔ measurable work`

with every term independently measurable.

## 7. Relation to E-ENERGY-0014

E-ENERGY-0014 showed that reversible structural graph dynamics alone do not produce an intrinsic temporal direction: the transition graph is symmetric.

E-ENERGY-0015 adds the missing variable identified by that result:

`G  →  (G, M)`

The experiment shows mathematically how a stored difference can make future transitions history-dependent.

Therefore the next step is not to invent more abstract asymmetry. It is to test the same structure in a **physical converter** where:

- the internal difference is measurable;
- memory is measurable;
- input/output work is measurable;
- rejected energy is measurable;
- the balance closes independently of the model assumptions.

## 8. Working principle extracted

`SYMMETRY → POTENTIAL`

`DIFFERENCE → MEMORY`

`ASYMMETRY + TIME → WORK-LIKE TRANSITION`

`BALANCE → ACCOUNTING BETWEEN INTERNAL AND EXTERNAL`

The word **work-like** is intentional until the quantity is connected to physical units and a calibrated measurement protocol.

## 9. Epistemic boundary

This experiment is a controlled mathematical construction. It demonstrates that history-dependent transition costs are possible when memory is included in the state and coupled to the transition rule. It does **not** demonstrate that physical energy is memory, nor that all physical work can be reduced to this model.

**UNKNOWN ≠ TRUE.**
**Calculation ≠ Experiment.**
**Model cost ≠ physical work.**
