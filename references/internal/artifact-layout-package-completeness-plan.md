# Artifact Layout and Package Completeness Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make artifact topology and package completeness deterministic enough that an agent cannot invent directories, rename/renumber required outputs, collapse capability-owned artifacts, or declare `REVIEW_COMPLETE` without reconciling the expected manifest with the actual tree.

**Architecture:** Add one focused normative artifact-layout contract, then make final editorial acceptance and capability output contracts consume it. Preserve existing mode-specific artifact lists and existing projection paths as owning sources; the hardening contract turns them into a frozen manifest and closeout gate rather than redefining semantic authority.

**Tech Stack:** Markdown skill contracts, Stage A workflow state, Stage B projection metadata, filesystem artifact manifests.

**Spec:** `references/internal/artifact-layout-package-completeness-design.md`

## Global Constraints

- Skill internals remain English.
- Human-facing `README.md` and `docs/**` remain unchanged by this hardening.
- Preserve all existing semantic/projection authority ownership.
- Do not invent a new capability or Session Intent.
- Do not create a new STM filesystem taxonomy.
- Existing valid repository-local package conventions remain supported only when explicitly resolved and frozen.
- Missing or undeclared artifact topology blocks `REVIEW_COMPLETE` rather than being normalized away.

---

### Task 1: Add normative artifact-layout contract

**Files:**
- Create: `references/artifact-layout-and-package-completeness.md`

**Interfaces:**
- Consumes: selected mode/endpoint/output configuration; existing mode artifact list; report role map; capability projection contracts.
- Produces: `ARTIFACT_LAYOUT_MANIFEST`, path errors, and `ARTIFACT_PACKAGE_RECONCILED` closeout state.

- [ ] Encode deterministic root selection and manifest fields.
- [ ] Encode canonical Architecture package filename roles.
- [ ] Prohibit invented paths and speculative directories.
- [ ] Preserve capability-owned output paths from owning projection contracts.
- [ ] Define expected-vs-actual tree reconciliation and completion blockers.
- [ ] Commit as `docs: add artifact package completeness contract`.

### Task 2: Bind final editorial acceptance to package reconciliation

**Files:**
- Modify: `references/final-editorial-review.md`

**Interfaces:**
- Consumes: `ARTIFACT_LAYOUT_MANIFEST`, actual tree, artifact registry, final package.
- Produces: editorial acceptance only after `ARTIFACT_PACKAGE_RECONCILED`.

- [ ] Add package-layout verification to purpose/checks.
- [ ] Add `LAYOUT-*` issue category.
- [ ] Require `ARTIFACT_PACKAGE_RECONCILED` in final acceptance.
- [ ] Ensure missing/undeclared paths cannot be repaired by prose-only editorial changes.
- [ ] Commit as `docs: gate final acceptance on artifact package reconciliation`.

### Task 3: Harden capability output ownership

**Files:**
- Modify: `capabilities/test-review/SKILL.md`
- Modify: `capabilities/code-quality-review/SKILL.md`

**Interfaces:**
- Consumes: capability projection registrations and frozen package manifest.
- Produces: prohibition against umbrella-invented aggregate output paths.

- [ ] Require capability outputs to use declared registered paths only.
- [ ] Reject arbitrary umbrella aggregates unless separately registered.
- [ ] For Code Quality, point to exact declared `working/projections/code-quality/*` paths.
- [ ] For Test Engineering, require exact paths from its owning projection/output contract; do not infer umbrella numbering.
- [ ] Commit capability hardening separately.

### Task 4: Harden STM filesystem behavior

**Files:**
- Modify: `references/technical-model-coverage.md`

**Interfaces:**
- Consumes: STM persistence contract and frozen artifact manifest.
- Produces: explicit rule that semantic domain taxonomy does not imply directory taxonomy.

- [ ] State that the 18 STM domains are coverage semantics, not filesystem directory names.
- [ ] Prohibit creating `working/technical-model/<domain>/` directories unless the owning persistence contract or frozen manifest declares them.
- [ ] Require lazy directory creation.
- [ ] Commit as `docs: prevent inferred technical model directories`.

### Task 5: Verification

**Files:**
- Verify all changed contracts and repository diff.

**Interfaces:**
- Consumes: Tasks 1-4.
- Produces: evidence that the observed malformed FORENSIC package is rejected.

- [ ] Verify `docs/reviews/` cannot replace the default `docs/reviews/architecture-review/` without an established frozen local convention.
- [ ] Verify omission of `02-authoritative-findings-ledger.md` blocks package reconciliation.
- [ ] Verify target/roadmap numbering is contract-owned.
- [ ] Verify arbitrary `05-test-engineering.md` / `06-code-quality.md` paths are rejected unless registered.
- [ ] Verify STM domain names do not authorize directories.
- [ ] Verify `REVIEW_COMPLETE` is impossible without `ARTIFACT_PACKAGE_RECONCILED` because final editorial acceptance is mandatory.
- [ ] Verify net diff does not modify `README.md` or human-facing `docs/**`.
