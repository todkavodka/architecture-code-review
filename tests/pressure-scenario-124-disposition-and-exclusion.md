# PS-124 — Applicability, exclusion, exception, and false positive differ

## Observed RED baseline

The baseline has no Code Quality applicability/disposition model for generated,
vendored, compatibility, or intentionally accepted code. It cannot preserve
the distinction between a candidate that does not apply and a real issue that
is intentionally not remediated.

Observed verdict: `PS124_PASS_AS_RED`

## Setup / input state

Evaluate candidates in generated code, vendored code, a compatibility shim, a
real issue accepted as an exception, a real issue marked `WONT_FIX`, and a
candidate disproven as a false positive.

## Required semantic behavior

`NOT_APPLICABLE`, `EXCLUDED`, `FALSE_POSITIVE`, `ACCEPTED_EXCEPTION`, `WONT_FIX`,
and `RESOLVED` retain distinct meanings and effects on CQ authority.

## Forbidden behavior

- treating excluded or not-applicable scope as proof of no quality risk;
- treating an accepted exception or WONT_FIX as resolved;
- persisting a false positive as an active finding.

## Expected post-implementation invariant

Applicability and disposition are explicit, auditable, and do not collapse into
one generic status.

## Verdict vocabulary

`PS124_PASS_AS_RED`
`PS124_GREEN_DISPOSITION_SEMANTICS_PRESERVED`
