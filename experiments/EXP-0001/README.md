# EXP-0001 — Energy Accounting and Conversion Graph

## Question

Can different energy-conversion systems be compared using one common graph and complete energy accounting rather than only nominal efficiency?

## Hypothesis

A common state-transition representation will expose where useful energy is retained, transferred, converted and rejected. The shortest conversion path is not assumed to be the most efficient.

## Systems to compare

1. Electrical generator driven by a heat engine.
2. Fuel cell.
3. Photovoltaic conversion.
4. Electromechanical generator.
5. Nuclear heat cycle.
6. Direct-energy-conversion concepts.

## Variables

`E_in` — input energy.

`E_useful` — useful exported energy.

`E_storage` — change in stored energy.

`E_rejected` — energy leaving the useful channel.

`η = E_useful / E_in`

`P = E_useful / Δt`

## Protocol

For every system:

1. Define the system boundary.
2. Identify the initial state.
3. Identify the energy carrier(s).
4. Identify every physical interaction.
5. Record each state transition.
6. Account for useful output.
7. Account for rejected energy.
8. Calculate efficiency.
9. Record uncertainty and source.
10. Compare graphs only after equivalent boundaries are established.

## Controls

- Do not compare thermal efficiency with electrical efficiency without defining the same boundary.
- Do not count the same energy twice.
- Do not treat fuel mass as energy without a defined calorific or physical energy value.
- Do not infer practical efficiency from theoretical energy density.
- Distinguish calculated values from measured values.

## Expected result

A normalized table and graph showing:

`SOURCE → CARRIER → INTERACTION → CONVERTER → USEFUL OUTPUT`

plus every identified rejected-energy branch.

## Status

`HYPOTHESIS / NOT YET RUN`

No experimental result is claimed by this document.
