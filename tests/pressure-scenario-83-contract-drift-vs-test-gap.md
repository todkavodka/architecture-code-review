# PS-83 — Contract drift versus assurance gap

## Purpose

Keep a contract mismatch (`CC-*`) orthogonal to a missing or misleading test
evidence gap (`GAP-*`).

## Fixtures and required behavior

Case A: Swagger omits `409`, while implementation, consumer behavior, and tests
fully cover it. Expected: `CC-*`, with no automatic `GAP-*`.

Case B: the same drift has missing executable evidence. Expected: the same
`CC-*` plus a separate `GAP-*` through `BC -> MAT -> TM/GAP`.

## Pre-remediation baseline

Static inspection of the unchanged Test Review guidance found assurance gaps
and test evidence, but no independent contract-drift record or rule preventing
drift from being collapsed into a gap. Both cases could therefore receive the
same assurance disposition, or the drift could be forced into `GAP-*` even in
Case A.

Evidence type: static contract inspection; no executable coordinator exists.

Observed verdict: `PS83_RED_DRIFT_FORCED_TO_GAP` and
`PS83_RED_GAP_HIDES_DRIFT`.

## Verdict vocabulary

`PS83_GREEN_ORTHOGONAL_DRIFT_AND_GAP` / `PS83_INCONCLUSIVE`
