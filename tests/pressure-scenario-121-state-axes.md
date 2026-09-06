# PS-121 — Lifecycle, applicability, disposition, and freshness are separate

## Observed RED baseline

The baseline has no Code Quality state model or legal-combination matrix for
finding lifecycle, applicability, disposition, and freshness. Existing shared
freshness vocabulary cannot supply the missing CQ lifecycle semantics.

Observed verdict: `PS121_PASS_AS_RED`

## Setup / input state

Evaluate these combinations for an accepted CQ finding:

- `ACTIVE + CURRENT`;
- `ACTIVE + WONT_FIX + CURRENT`;
- `ACTIVE + ACCEPTED_EXCEPTION + CURRENT`;
- `ACTIVE + STALE`;
- `RESOLVED + CURRENT`;
- `SUPERSEDED + CURRENT`.

Also evaluate invalid combinations such as an active persistent finding with
`FALSE_POSITIVE`, or an accepted finding with `NOT_APPLICABLE` or `EXCLUDED`.

## Required semantic behavior

The axes remain independent and legal combinations are explicit. Applicability
and disposition do not silently become lifecycle or freshness states.

## Forbidden behavior

- placing `CANDIDATE` in the persistent finding lifecycle;
- treating `WONT_FIX` or `ACCEPTED_EXCEPTION` as `RESOLVED`;
- using freshness as a substitute for lifecycle;
- retaining an accepted finding for a false-positive, not-applicable, or
  excluded candidate.

## Expected post-implementation invariant

Lifecycle, applicability, disposition, and freshness are independently
validated; invalid combinations cannot become accepted CQ authority.

## Verdict vocabulary

`PS121_PASS_AS_RED`
`PS121_GREEN_STATE_AXES_VALIDATED`
