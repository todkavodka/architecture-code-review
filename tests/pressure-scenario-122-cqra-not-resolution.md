# PS-122 — CQRA completion is not CQ resolution

## Observed RED baseline

The baseline has no Code Quality remediation authority, no `CQRA-*` identity,
and no explicit rule that completing remediation requires CQ revalidation.
Test Engineering `TASK-*` cannot supply this Code Quality-owned semantics.

Observed verdict: `PS122_PASS_AS_RED`

## Setup / input state

An accepted `CQ-*` finding has a linked remediation action. The action reaches
`COMPLETED`, but the affected source has not yet been revalidated.

## Required semantic behavior

The action records completion, while the CQ finding remains unresolved until
evidence-backed revalidation establishes that the issue no longer exists.

## Forbidden behavior

- treating `CQRA COMPLETED` as automatic `CQ RESOLVED`;
- using `TASK-*` as the Code Quality remediation authority;
- closing the finding without new evidence or revalidation.

## Expected post-implementation invariant

`CQRA COMPLETED != CQ RESOLVED`; remediation completion and semantic finding
resolution have independent authority.

## Verdict vocabulary

`PS122_PASS_AS_RED`
`PS122_GREEN_REMEDIATION_REQUIRES_REVALIDATION`
