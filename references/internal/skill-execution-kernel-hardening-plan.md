# SKILL.md Execution Kernel Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans or an equivalent task-by-task workflow. Steps use checkbox syntax for tracking.

**Goal:** Restore execution-critical guards to the root `SKILL.md` so an agent cannot begin persistent artifact writes, dispatch unconstrained workers, or claim `REVIEW_COMPLETE` without loading and enforcing the owning artifact/package contracts.

**Architecture:** Keep detailed semantics in existing references, but make the root skill a small executable kernel. The root must force required reference loading before irreversible boundaries: investigation, semantic write, filesystem/artifact write, subagent dispatch, and completion claim.

**Tech Stack:** Markdown skill contracts and existing Stage A/Stage B workflow vocabulary.

**Spec:** Approved conversation design: executable kernel + references own detail.

## Global Constraints

- Skill internals remain English.
- Do not expand user-facing `docs/**`.
- Do not duplicate detailed capability or layout semantics in the root.
- Root guards must be short, explicit, and mandatory.
- No persistent review artifact write before `ARTIFACT_LAYOUT_MANIFEST` is resolved and persisted.
- Subagents may write only explicitly assigned paths.
- `REVIEW_COMPLETE` requires both workflow-authority and artifact-package reconciliation.

---

### Task 1: Harden Start Gate

**Files:** Modify `SKILL.md`.

- [ ] Require reading `session-orchestration.md`, `review-modes-and-orchestration.md`, and `artifact-layout-and-package-completeness.md` before substantive work or filesystem mutation.
- [ ] Require requested work/capability/output configuration to be resolved before the layout manifest.
- [ ] Persist `ARTIFACT_LAYOUT_MANIFEST` in coordinator state before the first persistent artifact write.
- [ ] Add `NO_PERSISTENT_WRITE_BEFORE_ARTIFACT_LAYOUT_MANIFEST` as a hard invariant.

### Task 2: Harden capability/output resolution and dispatch

**Files:** Modify `SKILL.md`.

- [ ] Require reading the owning capability/output contract before selected output paths are added to the manifest.
- [ ] Require each worker/subagent dispatch to include `artifact_owner`, `allowed_output_paths`, `required_output_paths`, and `forbidden_output_policy: ALL_OTHER_PATHS`.
- [ ] Remove permission for workers to invent `working/*.md` files.
- [ ] Unknown paths must stop with `ARTIFACT_PATH_NOT_DECLARED`.

### Task 3: Harden the main executable flow

**Files:** Modify `SKILL.md`.

- [ ] Insert artifact manifest resolution before STM/bootstrap writes.
- [ ] Insert `ARTIFACT_PACKAGE_RECONCILIATION` before final editorial acceptance.
- [ ] Require `ARTIFACT_PACKAGE_RECONCILED` before completion.

### Task 4: Harden completion gate

**Files:** Modify `SKILL.md`.

- [ ] Require both `FINAL_WORKFLOW_AUTHORITY_RECONCILED` and `ARTIFACT_PACKAGE_RECONCILED`.
- [ ] Explicitly reject missing selected capability outputs, undeclared aggregate files, undeclared directories, and manifest/actual-tree mismatches.
- [ ] Return `REVIEW_PARTIALLY_COMPLETE` with exact blockers when package reconciliation fails.

### Task 5: Verification

- [ ] Confirm root Start Gate names all three mandatory contracts.
- [ ] Confirm the old `write their own working/*.md files` permission is gone.
- [ ] Confirm no persistent write is allowed before manifest resolution.
- [ ] Confirm dispatch path restrictions are present.
- [ ] Confirm the executable review flow includes package reconciliation.
- [ ] Confirm `REVIEW_COMPLETE` requires both reconciliation gates.
- [ ] Confirm no human-facing README/docs files changed.
