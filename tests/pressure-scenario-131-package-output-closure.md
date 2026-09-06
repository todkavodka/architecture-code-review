# PS-131 — Package policy uses selected-output dependency closure

## Observed RED baseline

The baseline has no CQ output selection, package membership, or Stage B
projection registration. Existing shared package policies cannot yet express a
CQ package whose required scope is limited to selected outputs and their
dependency closure.

Observed verdict: `PS131_PASS_AS_RED`

## Setup / input state

Select Findings View and Summary. Do not select Maintainability Hotspots or
Roadmap Contribution. Evaluate `PERMISSIVE`, `REQUIRED_SCOPE_CURRENT`, and
`ALL_SCOPED_CURRENT` with optional projections stale or blocked.

## Required semantic behavior

Package membership is explicit selection plus dependency closure. Findings View
and Summary do not implicitly require every possible CQ projection. Policy
controls projection usability and does not invalidate semantic findings.

## Forbidden behavior

- globally requiring all CQ projections;
- making unselected Hotspots or Roadmap Contribution package-required;
- treating package state as semantic CQ validity;
- inventing a CQ-specific projection lifecycle.

## Expected post-implementation invariant

Stage B package policies remain exactly `PERMISSIVE`,
`REQUIRED_SCOPE_CURRENT`, and `ALL_SCOPED_CURRENT`, applied to the selected
output dependency closure.

## Verdict vocabulary

`PS131_PASS_AS_RED`
`PS131_GREEN_SELECTED_OUTPUT_CLOSURE`
