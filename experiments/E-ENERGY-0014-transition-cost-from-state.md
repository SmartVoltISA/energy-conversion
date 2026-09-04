# E-ENERGY-0014 — Transition Cost from State

**Date:** 2026-09-04  
**Status:** COMPLETED — NEGATIVE / PRODUCTIVE  
**Parent:** E-ENERGY-0012 / H-ENERGY-05  
**Method:** exhaustive finite-state enumeration

## 1. Question

Can a cost-like quantity emerge from the difference between two structural states and their allowed transition paths, without assigning an energy variable or an arbitrary edge weight?

Target architecture:

```text
STRUCTURE → POTENTIAL → TRANSITION PATH → COST / RELEASE
```

The decisive requirement is directional: if `A → B` represents a release and `B → A` represents a cost, the distinction must emerge from the model rather than be programmed into the labels.

## 2. Minimal model

Four labeled nodes are used. All undirected simple graphs on the four nodes are enumerated.

Admissible states satisfy:

- graph is connected;
- maximum node degree ≤ 3.

A legal elementary transition toggles exactly one edge (add or remove) while preserving the admissibility constraints.

No variable named energy is introduced.

## 3. Exhaustive state space

The enumeration produced:

- **38 admissible structural states**;
- **84 undirected one-step transitions** between them;
- each state's local transition capacity `P(S)` is simply its number of legal neighbors;
- observed local transition capacities range from **3 to 6**.

Thus the state space itself is finite and completely enumerable for this model.

## 4. Test of state potential

Different states have different transition capacities. For example, the 3-edge star has `P = 3`, while an adjacent 4-edge state can have `P = 5`.

Therefore the earlier observation survives:

> Static structure can carry a measurable difference in available future transformations.

But this still does not establish energy.

## 5. Test of transition distance

For every pair of mutually reachable states, the shortest number of legal edge toggles was treated as a transition distance.

Because every legal graph edit is reversible, the state-transition graph is undirected. Consequently:

```text
d(A,B) = d(B,A)
```

for every connected pair.

The same applies to any path barrier constructed only from a symmetric state property: traversing the path in reverse reproduces the same states in reverse order.

## 6. Directionality test

Suppose a state function `U(S)` is proposed as a potential.

Then:

```text
ΔU(A→B) = U(B) − U(A)
ΔU(B→A) = U(A) − U(B) = −ΔU(A→B)
```

The sign reversal is mathematically consistent with a potential difference, but it does **not** create an independent physical rule saying that one direction consumes energy and the reverse releases energy.

If instead transition cost is defined as a non-negative path length or barrier, then the reverse process has the same cost rather than a negative release.

Therefore the tested model does not generate energetic directionality from structure and reversible connectivity alone.

## 7. Result

**NEGATIVE for the stronger hypothesis.**

The exhaustive model confirms three separate facts:

1. structural states can differ in transformation capacity;
2. structural states can be connected by measurable transition paths;
3. reversible transition rules do not by themselves produce an intrinsic cost/release asymmetry.

This is consistent with E-ENERGY-0012 and strengthens its negative result.

## 8. Falsification boundary

The following proposition is rejected for this model class:

> **A physical energy-like cost/release asymmetry can be derived from static relational structure plus reversible graph-edit rules alone.**

The experiment does **not** reject the possibility that energy-like behavior requires additional state variables or genuinely non-reversible dynamics.

## 9. What is now separated

The experiments now support a cleaner decomposition:

```text
STRUCTURE
   ↓
STATE SPACE / ACCESSIBLE TRANSITIONS
   ↓
TRANSITION PATH
   ↓
[additional mechanism required]
   ↓
COST / RELEASE
   ↓
TRANSFER / CONSERVATION
```

The missing layer is not simply "more graph structure". It must distinguish at least one of:

- irreversible dynamics;
- interaction with an external reservoir;
- history-dependent state;
- hidden/internal degrees of freedom;
- a dynamical law that assigns physical work to transitions.

## 10. Important consequence

This experiment prevents a common category error:

```text
number of possible changes ≠ energy
transition distance ≠ energy
state difference ≠ automatically work
```

These quantities may be useful observables, but physical energy requires a stronger bridge to measurable work, heat, momentum, field energy, or another established physical quantity.

## 11. Next decisive experiment

The next branch should introduce the **smallest possible non-reversible or history-dependent mechanism** and test whether a conserved quantity emerges without being explicitly imposed.

Candidate:

`E-ENERGY-0015 — History-Dependent Transition / Dissipation Test`

Question:

> Can a minimal internal memory variable make forward and reverse transition costs differ while allowing total accounting against an explicit reservoir?

The reservoir must be included in the system boundary. Otherwise an apparent violation of conservation may simply be an omitted degree of freedom.

## 12. Conclusion

The current evidence is getting more useful precisely because the attractive hypothesis keeps failing in its strongest form.

We have not found "energy in a graph".

We have established a narrower and more defensible chain:

> **Relational structure can define a state space and constrain possible transformations, but reversible structure alone does not generate physical energetic directionality.**

That is the current boundary of the evidence.
