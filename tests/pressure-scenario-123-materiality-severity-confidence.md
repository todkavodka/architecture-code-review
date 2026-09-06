# PS-123 — Materiality, severity, and confidence are separate

## Observed RED baseline

No Code Quality severity/materiality/confidence contract exists at the
baseline. Existing evidence guidance rejects warnings, counts, and size as
sufficient findings, but does not define CQ-specific adjudication.

Observed verdict: `PS123_PASS_AS_RED`

## Setup / input state

Compare three candidates: a high-confidence localized low-impact issue, a
low-confidence issue with a potentially severe consequence, and a repeated
large-count smell without a demonstrated material consequence.

## Required semantic behavior

Materiality decides whether a persistent finding is warranted. Severity
describes the accepted CQ consequence, and confidence describes certainty.
Informational/non-material observations remain outside accepted `CQ-*` state.

## Forbidden behavior

- deriving severity from confidence, warning level, LOC, or repetition count;
- persisting a non-material observation as a CQ finding;
- allowing security or Architecture severity to overwrite CQ severity.

## Expected post-implementation invariant

`materiality != severity != confidence`; each accepted finding has independently
adjudicated dimensions.

## Verdict vocabulary

`PS123_PASS_AS_RED`
`PS123_GREEN_DIMENSIONS_INDEPENDENT`
