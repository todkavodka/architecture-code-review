# PS-128 — REVALIDATE uses the minimum impacted CQ slice

## Observed RED baseline

The baseline has no Code Quality source/dependency/configuration binding or
impact-routing contract. Shared freshness guidance cannot route a CQ-specific
minimum slice that distinguishes source, addenda, STM, and related-record
changes.

Observed verdict: `PS128_PASS_AS_RED`

## Setup / input state

A single file, symbol, dependency version, framework/addendum version,
configuration value, targeted STM fact, or related RF/TE record changes while
other reviewed scope remains unchanged.

## Required semantic behavior

Impact analysis identifies affected CQ findings/candidates and revalidates only
that semantic slice. Equivalent refactors may retain identity when bindings
remain valid.

## Forbidden behavior

- rerunning the entire repository review for every source change;
- marking every CQ finding stale without dependency evidence;
- regenerating projections as an implicit part of semantic REVALIDATE.

## Expected post-implementation invariant

`REVALIDATE != full rerun` and `REVALIDATE != projection regeneration`.

## Verdict vocabulary

`PS128_PASS_AS_RED`
`PS128_GREEN_MINIMUM_IMPACTED_SLICE`
