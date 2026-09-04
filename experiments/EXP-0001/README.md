# EXP-0001 — Energy Accounting and Conversion Graph

**Canonical record:** `experiments/EXP-0001-energy-accounting-and-conversion-graph.md`  
**Status:** OPEN / FOUNDATION EXPERIMENT

This directory is retained as a compatibility/provenance location. The flat file above is the canonical experiment record; no separate experimental result is claimed here.

## Core question

Which physical converter most cleanly exposes the transition from potential to flow to useful work while allowing the complete energy account to be closed?

## Common chain

```text
SOURCE → CARRIER → INTERACTION → CONVERTER → OUTPUT
```

## Accounting

```text
E_in - E_out = ΔE_system + E_rejected
```

The physical system must have a defined boundary and independently measurable channels.

## Required measurements

- input energy;
- useful output energy/work;
- internal stored-energy/state change;
- rejected/dissipated energy;
- time-resolved state variables where possible;
- uncertainty and repeatability.

## Decision rule

An apparent gain with an open account is **UNRESOLVED**, not excess energy.

**UNKNOWN ≠ TRUE. Calculation ≠ Experiment. Model cost ≠ physical work.**
