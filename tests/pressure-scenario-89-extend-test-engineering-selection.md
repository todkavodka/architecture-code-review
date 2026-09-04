# PS-89 — EXTEND Test Engineering output selection

## Purpose

Prove that `EXTEND` exposes the modern Test Engineering selection model for an
accepted audit, reconstructs existing outputs, and resolves only the minimum
required dependency slice.

## Fixtures and required behavior

### Case A — Test Engineering was OFF

```yaml
session_intent: EXTEND
test_engineering:
  enabled: false
outputs:
  test_assurance: false
  test_plan: false
  contract_consistency_report: false
  test_environment_design: false
  service_simulator_design: false
  service_simulator_implementation_plan: false
  e2e_test_plan: false
```

For a request to extend the existing audit with testing, `EXTEND` must show the
modern independent Test Engineering output choices. It must not reduce the
user to `REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN`.

### Case B — Partial Test Engineering already exists

```yaml
outputs:
  test_assurance: true
  test_plan: true
  contract_consistency_report: false
  test_environment_design: false
  service_simulator_design: false
  service_simulator_implementation_plan: false
  e2e_test_plan: false
```

`EXTEND` must show Test Assurance and Test Plan as already selected, show only
the remaining outputs as available additions, reuse accepted/fresh upstream
work, and avoid restarting the full `NEW` configuration.

### Case C — E2E only

When the user adds only `E2E Test Plan`, `EXTEND` must not select
`Service Simulator Design` unless the actual topology requires it.

### Case D — Simulator implementation dependency

When `service_simulator_design` and
`service_simulator_implementation_plan` are both false and the user requests
`Service Simulator Implementation Plan`, `EXTEND` must explain and resolve the
required upstream `Service Simulator Design` dependency. It must not silently
enable unrelated outputs.

All cases keep Behavior Model internal and Contract Verification automatic when
materially applicable. Updated selections are persisted in independent
`outputs` fields.

## RED evidence

Fresh independent probes against the pre-PS-89 guidance observed:

```text
Case A: only a general `EXTEND` “shows only additions” rule existed; no explicit
independent Test Engineering menu or mapping from the request to outputs.
Case B: persisted outputs were described as authoritative, but no explicit menu
distinguished existing selections from available additions.
Case C: E2E was independently addable and did not force Service Simulator Design.
Case D: the simulator-spec prerequisite existed, but no EXTEND procedure
explained or resolved missing Service Simulator Design.
```

Observed RED verdicts:

```text
PS89_RED_OUTPUT_SELECTION_HIDDEN
PS89_RED_REQUIRED_DEPENDENCY_NOT_RESOLVED
```

Evidence type: fresh independent Skill pressure runs; no executable coordinator
exists in this repository.

## Verdict vocabulary

```text
PS89_GREEN_EXTEND_OUTPUT_SELECTION
PS89_INCONCLUSIVE
```
