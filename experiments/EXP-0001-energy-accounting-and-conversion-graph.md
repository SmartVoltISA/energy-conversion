# EXP-0001 — Energy Accounting and Conversion Graph

**Date:** 2026-09-04  
**Status:** OPEN / FOUNDATION EXPERIMENT

## Objective

Move the research from abstract relational potential to measurable energy conversion.

## System chain

```text
SOURCE → CARRIER → INTERACTION → CONVERTER → OUTPUT
```

The physical system must have a defined boundary and measurable channels.

## Accounting

For every run, record:

```text
E_in - E_out = ΔE_system + E_rejected
```

where `E_rejected` includes heat, radiation, mechanical loss, electrical loss and any other measured/unmeasured sink that belongs to the boundary.

## Required measurements

1. Input energy.
2. Useful output energy/work.
3. Internal stored-energy/state change.
4. Rejected/dissipated energy.
5. Time-resolved state variables where possible.
6. Repeatability and uncertainty.

## Core tests

### A. Baseline

Run the converter without the proposed special mechanism.

### B. Mechanism enabled

Run with the proposed coupling/conversion mechanism.

### C. Reversal

Reverse the relevant process where physically possible.

### D. Null/control

Disconnect or suppress the proposed coupling while keeping measurement conditions equivalent.

## Decision rule

A conversion mechanism is considered supported only if the excess useful output is larger than measurement uncertainty and is accompanied by a closed energy account.

An apparent gain with an open account is classified as **UNRESOLVED**, not excess energy.

## Relation to Ω-Lab

The legacy relational experiments are used as hypotheses about state, transition, memory and barriers. They are not treated as proof of physical energy. The present experiment is the bridge from abstract state transitions to measurable conversion.

## Current research question

> Which physical converter most cleanly exposes the transition from potential to flow to useful work while allowing the complete energy account to be closed?
