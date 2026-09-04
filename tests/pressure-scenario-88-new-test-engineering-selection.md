# PS-88 — NEW Test Engineering output selection

## Purpose

Prove that a first-run `NEW` startup exposes independent Test Engineering
outputs instead of presenting only the legacy Test Review endpoint.

## Fixture

The user starts a session with:

```text
Session Intent: NEW
```

The user wants a new Architecture Review with Test Engineering and wants to
choose Test Assurance, Test Environment Design, and E2E Test Plan while
leaving the other optional outputs disabled.

## Required behavior

The `NEW` startup contract must expose, separately from Architecture Review:

```text
Test Engineering
  OFF
  or independent output selection:
    Test Assurance: required core
    Test Plan: optional
    Contract Consistency Report: optional
    Test Environment Design: optional
    Service Simulator Design: optional
    Service Simulator Implementation Plan: optional
    E2E Test Plan: optional
```

The selected outputs are persisted directly as independent `outputs` fields.
Behavior Model and applicable Contract Verification remain internal
dependencies, not user-facing choices. E2E does not force Service Simulator
Design unless topology requires it, and recommendations must not silently
enable substantial optional work.

Legacy `REVIEW_ONLY` and `REVIEW_PLUS_TEST_PLAN` remain valid only when
reconciling old persisted audit state and normalize conservatively.

## RED check

Run this scenario against the unchanged current Skill in a fresh independent
agent context. Inspect the actual `NEW` startup menu and record observed
violations; do not infer a RED result from the scenario text alone.

Expected baseline verdicts:

```text
PS88_RED_LEGACY_NEW_MENU
PS88_RED_OUTPUT_SELECTION_HIDDEN
```

If the agent exposes Behavior Model or Contract Verification as a checkbox,
also record:

```text
PS88_RED_INTERNAL_GATE_EXPOSED
```

If it silently enables optional outputs without a user selection, record:

```text
PS88_RED_SILENT_OUTPUT_ENABLEMENT
```

## Verdict vocabulary

```text
PS88_GREEN_NEW_OUTPUT_SELECTION
PS88_INCONCLUSIVE
```
