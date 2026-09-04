# Energy Graph

## Purpose

Represent an energy process as a graph rather than as a single efficiency number.

## Node types

- `SOURCE` — initial physical system or process.
- `STATE` — defined state of the system.
- `CARRIER` — physical degree of freedom carrying energy.
- `INTERACTION` — mechanism coupling systems or degrees of freedom.
- `CONVERTER` — mechanism producing the desired output form.
- `OUTPUT` — useful exported energy.
- `REJECTED` — energy exported or dispersed outside the useful channel.
- `STORAGE` — energy retained in the system.
- `MEASUREMENT` — observation used to verify the transition.

## Edge

Each edge represents a physical transition:

`A --[mechanism, ΔE, Δt]--> B`

Minimum record:

- input energy;
- output energy;
- stored energy change;
- rejected energy;
- duration;
- mechanism;
- system boundary;
- uncertainty;
- evidence status.

## Balance

For every node or complete path:

`E_in = E_out + ΔE_storage + E_rejected`

The exact terms depend on the selected system boundary.

## Efficiency

For a defined useful output:

`η = E_useful / E_input`

For a chain of independent conversion stages:

`η_total = η1 × η2 × ... × ηn`

This multiplication is only valid when the stage boundaries and energy definitions are compatible.

## Research principle

Do not optimize the number of stages alone. Optimize the physical path and identify the dominant loss at each transition.

## Example

### Conventional generator

`CHEMICAL STATE → COMBUSTION → THERMAL STATE → PRESSURE/MOTION → ROTATION → ELECTROMAGNETIC INDUCTION → ELECTRIC OUTPUT`

### Direct-conversion hypothesis

`ENERGETIC REACTION → CARRIER → FIELD INTERACTION → ELECTRIC OUTPUT`

The second graph is a hypothesis about path reduction, not a claim of superior efficiency. It must be evaluated by complete energy accounting.
