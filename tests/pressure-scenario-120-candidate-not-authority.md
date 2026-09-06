# PS-120 — Candidate is not semantic authority

## Observed RED baseline

No Code Quality candidate-to-finding flow exists at the baseline. Existing
tooling or inspection can identify a possible smell, but there is no explicit
transient candidate boundary before persistent semantic authority.

Observed verdict: `PS120_PASS_AS_RED`

## Setup / input state

A heuristic identifies a possible duplication issue. Evidence review rejects it
as a false positive, or determines the rule is not applicable or the target is
excluded.

## Required semantic behavior

The result remains a transient candidate disposition and does not create an
ACTIVE persistent `CQ-*` finding.

## Forbidden behavior

- persisting every heuristic hit as CQ authority;
- treating `FALSE_POSITIVE`, `NOT_APPLICABLE`, or `EXCLUDED` as an active issue;
- allowing a rejected candidate to drive remediation or projections.

## Expected post-implementation invariant

`candidate != persistent CQ finding`; only an adjudicated material candidate
may become `CQ-*` authority.

## Verdict vocabulary

`PS120_PASS_AS_RED`
`PS120_GREEN_CANDIDATE_REMAINS_PRE_AUTHORITY`
