# PS-119 — Code Quality authority is distinct from Test Engineering

## Observed RED baseline

The baseline defines Test Engineering ownership for `BC-*`, `CC-*`, `MAT-*`,
`TM-*`, `GAP-*`, and `TASK-*`, but has no Code Quality relation contract for a
distinct interpretation of testability or nondeterminism evidence.

Observed verdict: `PS119_PASS_AS_RED`

## Setup / input state

A component has a hard-to-isolate dependency and nondeterministic behavior.
The same evidence may support a Code Quality maintainability finding and a
Test Engineering gap.

## Required semantic behavior

Code Quality may record its own `CQ-*` interpretation and relation to TE
records. Test Engineering remains the authority for its own semantic families.

## Forbidden behavior

- creating or mutating `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, or `TASK-*`;
- treating a CQ finding as Test Engineering behavior truth;
- collapsing two distinct interpretations into one finding authority.

## Expected post-implementation invariant

`CQ-* != BC/CC/MAT/TM/GAP/TASK`; shared evidence may support independent
interpretations.

## Verdict vocabulary

`PS119_PASS_AS_RED`
`PS119_GREEN_CQ_TE_OWNERSHIP_PRESERVED`
