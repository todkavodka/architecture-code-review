# REVALIDATE Closeout Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make invalid REVALIDATE closeout paths impossible to justify from the skill contracts: semantic authority cannot be regenerated as `PRJ-*`, baseline advancement cannot precede owner-gated delta acceptance, and projection `CURRENT` cannot be asserted without complete Stage B verification evidence.

**Architecture:** Preserve the existing authority model and workflows. Add one focused closeout hardening contract plus explicit preflight/closeout invariants in the owning projection, revalidation, and umbrella contracts. Do not introduce a new runtime subsystem, Session Intent, capability, or semantic authority family.

**Spec:** `references/internal/revalidate-closeout-hardening-design.md`

## Global Constraints

- Skill internals remain English.
- Human-facing `README.md` and `docs/**` remain Russian.
- Preserve existing formal identifiers and authority ownership.
- `RG-*` may target only active explicitly registered `PRJ-*` identities.
- Baseline advancement follows owner-gated revalidation and delta reconciliation.
- `CURRENT` requires complete Stage B verification evidence.

## Task 1 — Central closeout hardening contract

Create `references/revalidate-closeout-hardening.md` containing the observed invalid regression, valid recovery chain, baseline role split, strict `ALL_STALE`, semantic-authority exclusions, `REGENERATION_TARGET_NOT_PROJECTION`, `CURRENT` evidence requirements, and final reconciliation checks.

## Task 2 — Projection lifecycle and regeneration

Modify `references/projection-lifecycle.md` and `references/projection-regeneration.md` so that semantic authority cannot enter `PRJ-*` / `RG-*`, `ALL_STALE` is registry-defined, invalid targets fail before plan creation, and `CURRENT` requires complete accepted lifecycle evidence.

## Task 3 — REVALIDATE semantic closeout

Modify `references/revalidation-and-freshness.md` so the overlay is explicitly `PROPOSED_REVALIDATION_DELTA`, baseline roles are distinct, every material delta is owner-reconciled, current-baseline model/coverage gates precede advancement, and `RG-*` occurs only after semantic acceptance and impact accounting.

## Task 4 — Umbrella completion guard

Modify `SKILL.md` so every project-change REVALIDATE must load the hardening contract, completion rejects contradictory baseline/model/coverage state, and projection-sensitive closeout requires active registered `PRJ-*`, V1-V4, fingerprint, and accepted revision or `NO_CHANGE`.

## Task 5 — Verification

Verify all of the following with fresh repository reads:

```text
02-authoritative-findings-ledger.md is explicitly non-RG authority
03-target-architecture.md is explicitly non-RG authority
04-remediation-roadmap.md is explicitly non-RG authority
ALL_STALE == ACTIVE registered PRJ-* with STALE freshness
accepted_baseline cannot move before BASELINE_ADVANCE_ALLOWED
rewritten Markdown != CURRENT
RG completed != CURRENT
CURRENT requires PRJ + contract + dependencies + V1-V4 + fingerprint + revision/NO_CHANGE
FINAL_WORKFLOW_AUTHORITY_RECONCILED rejects contradictory baseline/coverage bindings
README.md and ordinary docs/** were not modified by this hardening
```

Only claim completion after those checks pass.
