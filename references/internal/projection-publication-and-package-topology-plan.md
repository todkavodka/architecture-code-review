# Projection Publication and Package Topology Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans or equivalent disciplined execution. Steps are ordered because later contract edits depend on earlier owning-path decisions.

**Goal:** Make capability output topology coherent, make first-generation projection publication mandatory, and make undeclared persistent paths blocking.

**Architecture:** Keep stable projection identities and semantic ownership unchanged. Change only declared delivery paths, publication/closeout guards, and package-topology enforcement. `working/projections/` remains operational Stage B state; user-facing capability projections live under `capabilities/<capability>/`.

**Tech Stack:** Markdown skill contracts and GitHub repository metadata.

**Spec:** `references/internal/projection-publication-and-package-topology-design.md`

## Global Constraints

- Do not change `PRJ-CQ-*` stable identities.
- Do not change CQ semantic authority or lifecycle.
- Do not weaken V1–V4 or package freshness policy.
- Human documentation remains Russian; internal skill contracts remain English.
- No generic "non-blocking undeclared path" exception.

---

### Task 1: Normalize Code Quality delivery paths

**Files:**
- Modify: `capabilities/code-quality-review/references/code-quality-projection.md`
- Modify: `capabilities/code-quality-review/SKILL.md`

- [ ] Replace four `working/projections/code-quality/*` declared paths with capability-owned numbered paths.
- [ ] Preserve stable `PRJ-CQ-*` identities and dependency/package semantics.
- [ ] Explicitly define path migration as same identity, new declared path.
- [ ] Ensure examples and path-discipline text match the new locations.

### Task 2: Harden package topology

**Files:**
- Modify: `references/artifact-layout-and-package-completeness.md`

- [ ] Update Code Quality examples to new capability-owned paths.
- [ ] Declare a canonical persistent path for `ARTIFACT_LAYOUT_MANIFEST` under `working/`.
- [ ] Define Project Profile file persistence as allowed only at an explicitly declared coordinator path; otherwise keep it as INDEX/ref state.
- [ ] State that any undeclared generated path is blocking until reconciled; remove any possibility of generic non-blocking classification.
- [ ] Add `PACKAGE_LIFECYCLE_INVALID` to final verdict vocabulary.

### Task 3: Make first-generation projection lifecycle a package gate

**Files:**
- Modify: `references/projection-lifecycle.md`
- Modify: `SKILL.md`

- [ ] State that a selected generated output cannot satisfy package membership merely by existing on disk.
- [ ] Require registered identity, contract revision, dependency snapshot, V1–V4, canonical fingerprint, accepted projection revision/NO_CHANGE, and `CURRENT`.
- [ ] State Git tracked/untracked status and ad-hoc hashes are irrelevant to projection revision/fingerprint acceptance.
- [ ] Add root-kernel completion guard for lifecycle-invalid selected outputs.

### Task 4: Verify pressure regressions

- [ ] Check that no current contract still registers CQ outputs under `working/projections/code-quality/`.
- [ ] Check root completion contract rejects selected outputs with missing V1–V4/fingerprint/revision/freshness.
- [ ] Check artifact-layout contract rejects undeclared persistent files as blocking.
- [ ] Compare net diff from pre-hardening HEAD and confirm only internal skill files changed.
