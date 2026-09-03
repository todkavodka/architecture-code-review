# PS-82 — Contract Verification authority

## Purpose

Ensure declared, implemented, consumed, and tested contract views remain
observable when they disagree, without automatically selecting Swagger/OpenAPI
or production code as truth.

## Fixture

```text
OpenAPI:       POST /orders -> 201, 400
Implementation: POST /orders -> 201, 400, 409 DuplicateOrder
Consumer:       handles 409 DuplicateOrder
Tests:          cover 201 and 400 only
```

Required output preserves `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED`,
creates a `CC-*`, and leaves authority unresolved until adjudication.

## Pre-remediation baseline

Static contract check against the unchanged Test Review capability found no
contract-view model, `CC-*` record, or authority-resolution rule. The current
guidance only evaluates evidence sufficiency, so a reviewer following it could
trust the declared contract or normalize the implementation's `409` away.

Evidence type: static contract inspection; no executable coordinator exists.

Observed verdict: `PS82_RED_AUTOMATIC_CONTRACT_WINNER` and
`PS82_RED_DRIFT_NORMALIZED_AWAY`.

## Verdict vocabulary

`PS82_GREEN_CONTRACT_AUTHORITY_PRESERVED` / `PS82_INCONCLUSIVE`
