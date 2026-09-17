# Package Lifecycle and Code Quality Topology Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make package validity depend on verified Stage B lifecycle evidence, eliminate undeclared-path exceptions, and move Code Quality delivery projections into capability-owned paths.

**Architecture:** Preserve existing semantic authority and stable `PRJ-*` identities. Change only delivery path registration, package reconciliation rules, coordinator meta-path declarations, and completion verification. Historical paths remain legacy input but are not current output topology.

**Tech Stack:** Markdown skill contracts, Stage B projection lifecycle, package reconciliation.

**Spec:** `references/internal/package-lifecycle-and-code-quality-topology-design.md`

## Global Constraints

- Keep human-facing `README.md` and `docs/**` unchanged.
- Keep Code Quality `PRJ-*` identities stable while changing declared paths.
- Do not create a second projection lifecycle.
- Do not permit ad-hoc checksums as accepted lifecycle fingerprints.
- `PACKAGE_VALID` requires `ARTIFACT_PACKAGE_RECONCILED: ACCEPTED`.

---

### Task 1: Normalize Code Quality delivery paths

**Files:**
- Modify: `capabilities/code-quality-review/references/code-quality-projection.md`
- Modify: `capabilities/code-quality-review/SKILL.md`
- Modify: `references/artifact-layout-and-package-completeness.md`

- [ ] Replace the four registered `working/projections/code-quality/*` paths with `capabilities/code-quality-review/00-03*.md` paths while preserving `PRJ-CQ-*` identities.
- [ ] Add an explicit legacy-path migration statement.
- [ ] Make the capability entrypoint reference only the new paths.
- [ ] Update package-layout examples and invalid-path guidance.

### Task 2: Make projection lifecycle evidence part of package reconciliation

**Files:**
- Modify: `references/artifact-layout-and-package-completeness.md`
- Modify: `references/final-editorial-review.md`

- [ ] Add `PROJECTION_LIFECYCLE_INCOMPLETE`.
- [ ] Require active PRJ identity, contract revision, accepted dependency snapshot, V1-V4, canonical fingerprint, accepted revision/NO_CHANGE, and CURRENT for every selected package projection.
- [ ] State that generated Markdown and reconciliation-time hashes are insufficient.
- [ ] Make missing lifecycle evidence block `ARTIFACT_PACKAGE_RECONCILED`.

### Task 3: Declare coordinator meta paths and remove undeclared exceptions

**Files:**
- Modify: `references/artifact-layout-and-package-completeness.md`
- Modify: `references/session-orchestration.md`

- [ ] Declare `working/ARTIFACT_LAYOUT_MANIFEST.md` as canonical manifest persistence path.
- [ ] Declare `working/project-profile.md` when Project Profile is materialized.
- [ ] State that undeclared paths are always drift until explicitly reconciled; there is no non-blocking undeclared category.
- [ ] Treat root-level legacy manifest as migration input, not accepted current layout.

### Task 4: Tighten verdict and INDEX reconciliation semantics

**Files:**
- Modify: `references/artifact-layout-and-package-completeness.md`
- Modify: `references/final-editorial-review.md`

- [ ] Add mutually exclusive package verdict vocabulary.
- [ ] Allow `PACKAGE_VALID` only when package reconciliation is accepted.
- [ ] Require INDEX repair from owning authority/gates, not execution-plan prose.
- [ ] Add the latest pressure-run regression case.

### Task 5: Verify net contract consistency

- [ ] Search/fetch changed files and confirm no active Code Quality registration still points to `working/projections/code-quality/`.
- [ ] Confirm `working/projections/` remains documented for operational Stage B views only.
- [ ] Confirm every selected projection must have V1-V4 + canonical fingerprint + revision/NO_CHANGE + CURRENT before package acceptance.
- [ ] Confirm undeclared files cannot be called non-blocking.
- [ ] Confirm `README.md` and user-facing `docs/**` are unchanged.
