# PS-130 — Semantic authority is distinct from generated projections

## Observed RED baseline

The baseline has no CQ semantic records or CQ projection registration. Existing
Stage B contracts distinguish semantic authority from generated `PRJ-*`
projections, but no Code Quality output binds to that lifecycle.

Observed verdict: `PS130_PASS_AS_RED`

## Setup / input state

Accepted CQ semantic state changes while a generated Findings View/Report is
stale. Separately, a presentation-only `PROJECTION_REPAIR` is requested with
no semantic change.

## Required semantic behavior

Semantic CQ state remains authoritative. The report becomes stale and is
handled through Projection Impact Analysis and explicit regeneration. A
presentation-only repair cannot change CQ findings.

## Forbidden behavior

- treating report content as CQ semantic authority;
- hiding semantic change as `PROJECTION_REPAIR`;
- regenerating a projection as part of semantic revalidation.

## Expected post-implementation invariant

`semantic CQ authority != generated projection`; `PROJECTION_REPAIR != semantic
remediation`.

## Verdict vocabulary

`PS130_PASS_AS_RED`
`PS130_GREEN_SEMANTIC_PROJECTION_BOUNDARY`
