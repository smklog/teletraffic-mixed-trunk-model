# Mixed-Traffic Trunk Group — Engineering Analysis Summary

## Objective

Evaluate blocking probability, retry behavior, and carried traffic for a large
mixed-traffic full-availability trunk group under realistic SS7/PSTN
inter-network conditions.

## Methodology

- Erlang-B recursive blocking formula
- Equivalent-load representation for dual-link (two-line) calls
- Fixed-point iteration for repeated outgoing call attempts (retry traffic)

## Sample Findings (example scenario)

- Blocking probability grows non-linearly as outgoing offered load increases.
- Retry load amplifies congestion effects and may significantly contribute
  to the total offered traffic under high blocking conditions.
- Carried traffic saturates near trunk capacity while blocking and retry
  behavior become the dominant performance characteristics.

## Engineering Value

The model provides scalable and computationally efficient estimates that are
suitable for:

- Trunk capacity planning
- Network performance engineering
- Scenario analysis and "what-if" evaluations
- Research and academic experimentation in teletraffic engineering
