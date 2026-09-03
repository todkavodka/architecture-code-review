# PS-87 — Test Engineering output-selection persistence

## Purpose

Prove that persisted capability state can reconstruct the exact Test Engineering
dependency slice through `RESUME`, `EXTEND`, `USE_EXISTING`, and `REVALIDATE`.

## Required distinguishable states

The state model must distinguish all of these without compound endpoint enums:

```text
Test Assurance only
Test Assurance + Test Plan
Test Assurance + E2E
Test Assurance + Simulator + E2E
Test Assurance + Contract Consistency Report
```

`test_assurance` is required when enabled. Behavior Model is an internal
dependency, and applicable Contract Verification is an internal automatic gate;
neither is a user-selected output. `EXTEND` adds only explicitly requested
outputs, and `RESUME` reuses exactly the persisted selection without inventing
outputs or asking again.

Legacy normalization must be additive and conservative:

```text
REVIEW_ONLY
  -> test_assurance=true; all optional outputs=false

REVIEW_PLUS_TEST_PLAN
  -> test_assurance=true; test_plan=true; all other optional outputs=false
```

## Pre-remediation baseline

Static inspection of the current capability registry found only:

```text
endpoint: REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN
```

The independent `outputs` fields were present in Session Orchestration prose,
but not in the persisted `INDEX` capability registry schema. Therefore the
registry could not distinguish the five requested states or reconstruct them
reliably after `RESUME`/`EXTEND`.

Evidence type: contract-level RED; no file or runtime coordinator was executed.

Observed verdict: `PS87_RED_OUTPUT_SELECTION_NOT_PERSISTED`.

## Post-remediation target

`PS87_GREEN_OUTPUT_SELECTION_PERSISTED` / `PS87_INCONCLUSIVE`
