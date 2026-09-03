# PS-84 — Test Engineering minimum dependency slice

## Purpose

Ensure selected outputs execute as a dependency DAG and reuse accepted work
without restarting unrelated review stages.

## Cases and required behavior

Case A: only `E2E Test Plan` is selected. Required slice is Test Assurance,
Behavior Model, Contract Verification when applicable, and E2E Design;
Service Simulator Design is added only when topology requires it.

Case B: `EXTEND` adds Service Simulator Design to an accepted Test Review. The
accepted upstream slice is reused and the full review is not restarted.

## Pre-remediation baseline

Static inspection of the unchanged entrypoint and orchestration references found
only Test Review as a composable capability. No Test Engineering output menu,
dependency DAG, persisted output selection, or `EXTEND` minimum-slice rule was
present. A compliant implementation could run a linear full pipeline or restart
the full review for the extension.

Evidence type: static contract inspection; no executable coordinator exists.

Observed verdict: `PS84_RED_LINEAR_PIPELINE_EXPANSION` and
`PS84_RED_FULL_REVIEW_RESTART`.

## Verdict vocabulary

`PS84_GREEN_MINIMUM_DEPENDENCY_SLICE` / `PS84_INCONCLUSIVE`
