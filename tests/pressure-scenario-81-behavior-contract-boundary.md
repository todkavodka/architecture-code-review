# PS-81 — Behavior Contract boundary

## Purpose

Prove that Test Engineering keeps one independently verifiable product behavior
(`BC-*`) separate from assurance targets (`MAT-*`), findings (`RF-*`), gaps
(`GAP-*`), remediation work (`TASK-*`), and executable evidence (`TM-*`).

## Fixture and required behavior

The candidate record contains a material behavior, its assurance target, and an
existing test. A compliant capability must model the behavior as `BC-*`, map it
to `MAT-*` through `TM-*`, and keep executable-evidence verdicts out of the BC.

Required distinctions: `BC != MAT`, `BC != RF`, `BC != GAP`, and `BC` does not
own test-evidence verdicts.

## Pre-remediation baseline

Static contract check against the unchanged `capabilities/test-review/SKILL.md`
and the umbrella references found only Test Review assurance accounting and
`MAT-*`/`GAP-*`/`TM-*` vocabulary. No `BC-*` model, writer ownership, or
prohibition on embedding `existing_test_evidence` in a behavior record was
defined. Two independent compliant readers could therefore reuse `MAT-*` as a
behavior ID or place evidence inside the behavior record.

Evidence type: static contract inspection; no executable coordinator exists.

Observed verdict: `PS81_RED_BEHAVIOR_IDENTITY_COLLAPSED` and
`PS81_RED_EVIDENCE_EMBEDDED_IN_BC`.

## Verdict vocabulary

`PS81_GREEN_BEHAVIOR_BOUNDARY` / `PS81_INCONCLUSIVE`
