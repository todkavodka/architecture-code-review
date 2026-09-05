# smevals Spike for `architecture-code-review`

Status: **PROPOSED — POST-STAGE-C SPIKE**

This document records a deliberately small experiment for evaluating `architecture-code-review` Skill behavior with [`smevals`](https://primeradiant.com/blog/2026/smevals.html).

The goal is not to build a new validation framework. The goal is to test whether a tiny reusable eval suite can catch important contract regressions more cheaply than repeated full manual end-to-end review runs.

## Why this may be useful

`smevals` models an evaluation as tasks run against one or more configs, records each run, and grades those outputs separately. Configs can vary the model, prompt, parameters, or harness. Grading can use simple deterministic checks or custom checkers, including model-based checks. Runs can also be regraded later without re-running the evaluated model.

That maps well to the Skill's current validation needs:

- compare MiMo, Codex, and other candidate models against the same Skill behavior;
- detect narrow contract regressions after `SKILL.md` or reference changes;
- keep run evidence separate from grading policy;
- avoid repeating a full Architecture Review merely to verify a small contract fix.

## Guardrail

This spike is governed by:

```text
evidence first
automation second
framework last
```

It must **not** become:

- Skill Lab 2;
- a replacement for real-agent acceptance;
- a large agent E2E harness;
- a framework for testing the eval framework;
- a prerequisite for Stage C implementation;
- a new semantic authority inside the Skill.

If the spike cannot demonstrate useful signal with a handful of tasks and minimal plumbing, stop with:

```text
DO_NOT_BUILD_HARNESS
```

## Timing

Do **not** integrate this into Stage C implementation.

Preferred sequence:

```text
Stage C implementation
→ Stage C targeted acceptance
→ tiny smevals spike
→ ROI decision
```

## Initial question

Can a five-task eval suite detect meaningful `architecture-code-review` contract failures with materially less time/token cost than a full manual review run?

## Proposed five tasks

### EV-01 — Raw projection without PRJ lifecycle

Scenario:

```text
A NEW review generates an As-Built Markdown projection.
The file exists, but there is no accepted PRJ-* lifecycle metadata.
```

Expected behavior:

```text
RAW_MARKDOWN_WITHOUT_PRJ_CAN_BE_CURRENT: NO
```

Required concepts the response should recognize:

- independently regeneratable projection requires stable `PRJ-*` identity;
- dependencies/dependency snapshot are required;
- V1–V4 verification is required;
- canonical fingerprint and verified revision are required;
- freshness must be persisted;
- raw Markdown alone is not a `CURRENT` projection.

Primary value: catches regression in Stage B initial-generation integration.

### EV-02 — Final workflow authority mismatch

Scenario:

```text
authoritative positive-controls ledger: 15
working/INDEX.md positive-controls registry: 9
```

Expected behavior:

```text
FINAL_WORKFLOW_AUTHORITY_RECONCILED: FAIL
```

Required concepts:

- `working/INDEX.md` is coordinator workflow authority, not semantic authority;
- aggregate state stored in INDEX must reconcile with the owning authoritative artifact;
- `REVIEW_COMPLETE` cannot pass when mandatory final reconciliation fails.

Primary value: catches the exact drift missed during manual MiMo acceptance.

### EV-03 — REVALIDATE must not regenerate

Scenario:

```text
A Test Engineering semantic slice needs revalidation.
One dependent projection is STALE.
The requested mode is REVALIDATE, not regeneration.
```

Expected behavior:

- revalidate the minimum affected semantic/verification slice;
- account for projection impact where applicable;
- do **not** silently run projection regeneration;
- regeneration remains an explicit lifecycle action/session.

Primary value: checks Stage C ↔ Stage B mode boundary.

### EV-04 — PROJECTION_REPAIR must not modify semantic authority

Scenario:

```text
A generated Test Engineering projection has broken projection metadata/content,
but its underlying accepted TE semantic authority is unchanged.
Mode: PROJECTION_REPAIR.
```

Expected behavior:

- repair projection state only;
- do not rewrite `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*`, STM, or Architecture authority merely to make projection verification pass;
- if semantic authority is actually invalid, stop/escalate instead of silently changing it.

Primary value: checks semantic-authority/projection separation.

### EV-05 — Targeted STM prerequisite

Scenario:

```text
Test Engineering is asked to analyze assurance for a scope.
The required technical facts are missing or stale in the accepted targeted STM.
The repository source is locally available.
```

Expected behavior:

- do not privately reconstruct a competing technical model inside Test Engineering;
- route/request the required STM workflow/gate;
- TE semantic analysis waits for sufficiently covered, accepted, fresh targeted STM.

Primary value: catches the most important Stage C authority-boundary regression.

## Grading strategy

Keep grading intentionally small.

### Phase 1 — deterministic checks

Each task should request a compact structured answer with a small set of exact verdict fields. Grade those fields deterministically where possible.

Examples:

```text
RAW_MARKDOWN_WITHOUT_PRJ_CAN_BE_CURRENT: NO
FINAL_WORKFLOW_AUTHORITY_RECONCILED: FAIL
REVALIDATE_IMPLICITLY_REGENERATES: NO
PROJECTION_REPAIR_MAY_CHANGE_SEMANTIC_AUTHORITY: NO
TE_MAY_PRIVATELY_RECONSTRUCT_STM: NO
```

A deterministic checker should verify only the requested verdict shape and required values. It should not attempt to grade prose quality.

### Phase 2 — optional semantic grader

Only if deterministic verdicts produce false confidence, add one small model-based checker that verifies whether the explanation cites the correct authority boundary/reasoning.

Do not start with an LLM grader unless needed.

## Configs

Start with only the configs we actually want to compare, for example:

```text
mimo-current-skill
codex-current-skill
```

A config should differ only in dimensions intentionally being evaluated, such as model or effective Skill/system prompt.

Do not create a large model matrix during the spike.

## Runner requirements

The runner should:

- start a fresh agent/model context for each task;
- use the current installed/canonical Skill under test;
- capture stdout/stderr or equivalent transcript/artifacts;
- record model/config identity;
- avoid modifying the target repository;
- avoid running a full Architecture Review;
- terminate after the targeted task.

Prefer existing CLI invocation paths. Do not build a new orchestration service.

## Minimal evidence to capture

For each run preserve only what is useful for comparison:

```text
task id
config/model
Skill version or content fingerprint when available
raw output
run status
grade/check results
elapsed time
token usage when available
```

Do not duplicate full repository contents into eval artifacts.

## Success criteria for the spike

The spike is worth keeping only if all of these are true:

1. The five tasks can run without building substantial new infrastructure.
2. At least one known-bad or deliberately weakened contract variant is detected reliably.
3. The suite produces a materially cheaper/faster signal than a full manual Architecture Review.
4. Results are understandable without maintaining a second semantic model of the Skill.
5. Updating a grader does not require re-running all model calls when run evidence already exists.
6. Real-agent manual acceptance remains the final check for material agentic behavior changes.

## Stop-loss criteria

Stop and do not expand the experiment if any of these occurs:

```text
- eval plumbing becomes larger than the five behavior cases;
- fixtures begin duplicating Stage A/B/C semantics;
- a second lifecycle/authority model is needed just for grading;
- the runner needs its own substantial architecture or persistent service;
- multiple remediation cycles are spent on the harness before it catches a real Skill regression;
- token/time cost approaches that of the manual targeted acceptance it is meant to replace.
```

Terminal marker:

```text
STOP_HARNESS_EXPANSION
```

## ROI decision after the spike

Classify the result as exactly one:

```text
SMEVALS_KEEP_AS_SMALL_REGRESSION_SUITE
SMEVALS_USE_ONLY_FOR_OCCASIONAL_MODEL_COMPARISON
SMEVALS_NO_CLEAR_ADVANTAGE
DO_NOT_BUILD_HARNESS
```

Do not promote the spike into mandatory project infrastructure without evidence from the five-task experiment.
