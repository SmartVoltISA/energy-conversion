# E-ENERGY-STRESS-TEST-001 — 10,000-case computational control

**Date:** 2026-09-04  
**Status:** COMPUTATIONAL RESULT  
**Seed:** 20260904  
**Samples:** 10,000 parameter sets per model class  
**Threshold:** relative residual > 1e-10 classified as failure

## Scope

Randomized ideal RC charge, RL step, and free series-RLC systems were tested over logarithmic parameter ranges. The stress-test implementation uses closed-form trajectories and analytic energy integrals for the ideal models. This avoids confusing coarse numerical quadrature with a failure of the accounting identity.

## Result

The verified run produced **0 accounting failures** above the 1e-10 relative-residual threshold.

The worst observed RLC residual was approximately **1.9e-13** relative to the energy scale.

## Important control finding

An earlier implementation used trapezoidal numerical integration for RC/RL and RK4 time stepping for RLC. Coarse discretization produced apparent residuals up to about 2e-3 in RC and 1e-4 in RL during stress testing. After replacing those terms with analytic integrals, the residuals collapsed to numerical round-off scale.

Therefore those earlier deviations were correctly classified as **numerical-method error**, not unexplained energy.

## Interpretation

For the ideal equations tested, the proposed bookkeeping does not spontaneously create an additional energy term. The result is a control of the computational representation, not evidence for a new physical law.

The experiment also establishes a useful rule for the project:

> Before interpreting an accounting residual physically, first eliminate solver/discretization error with an independent or analytic calculation.

## Next test

Proceed to the stronger case: a history-dependent/internal-state model where identical instantaneous observables can correspond to different future transitions. Then search explicitly for apparent energy creation when hidden state or an external reservoir is omitted from the accounting boundary.

**Calculation ≠ Experiment.**  
**Model result ≠ physical measurement.**  
**UNKNOWN ≠ TRUE.**
