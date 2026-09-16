# REVALIDATE Closeout Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make invalid REVALIDATE closeout paths impossible to justify from the skill contracts: semantic authority cannot be regenerated as `PRJ-*`, baseline advancement cannot precede owner-gated delta acceptance, and projection `CURRENT` cannot be asserted without complete Stage B verification evidence.

**Architecture:** Preserve the existing authority model and workflows. Add a focused closeout hardening contract plus explicit preflight/closeout invariants in the owning projection, revalidation, session, report, and umbrella contracts. The hardening is normative documentation only; it introduces no new runtime subsystem or semantic identity family.

**Tech Stack:** Markdown skill contracts, Stage A/Stage B workflow vocabulary, GitHub repository documentation.

**Spec:** `docs/superpowers/specs/2026-09-16-revalidate-closeout-hardening-design.md`

## Global Constraints

- Skill internals remain English.
- Human-facing `README.md` and ordinary `docs/**` remain Russian; only `docs/superpowers/**` engineering process artifacts are added in English.
- Preserve existing formal identifiers and authority ownership.
- Do not introduce a new Session Intent, capability, semantic authority family, or automatic regeneration behavior.
- `RG-*` may target only active explicitly registered `PRJ-*` identities.
- Baseline advancement must follow owner-gated revalidation and delta reconciliation.
- `CURRENT` requires complete Stage B verification evidence.

---

### Task 1: Add closeout hardening contract

**Files:**
- Create: `references/revalidate-closeout-hardening.md`

**Interfaces:**
- Consumes: existing `REVALIDATE`, projection lifecycle, regeneration, report authority, and coordinator semantics.
- Produces: one compact normative recovery/closeout contract referenced by the owning files.

- [ ] **Step 1: Encode the observed failing regression as an invalid scenario**

Document the exact invalid sequence: overlay accepted directly, semantic authority edited by RG workers, baseline moved early, Markdown rewritten without PRJ/V1-V4, and coordinator falsely reconciled.

- [ ] **Step 2: Encode the valid closeout sequence**

Require proposed delta → owner adjudication → current-baseline gates → delta reconciliation → baseline advancement → PIA → registered PRJ-only RG → V1-V4 → final reconciliation.

- [ ] **Step 3: Define machine-checkable invariants**

Include `REGENERATION_TARGET_NOT_PROJECTION`, strict `ALL_STALE`, baseline role fields, and `CURRENT` evidence requirements.

- [ ] **Step 4: Commit**

Commit message: `docs: add revalidate closeout hardening contract`.

### Task 2: Harden projection lifecycle and regeneration

**Files:**
- Modify: `references/projection-lifecycle.md`
- Modify: `references/projection-regeneration.md`

**Interfaces:**
- Consumes: Task 1 hardening contract.
- Produces: mandatory RG preflight and explicit semantic-authority exclusion.

- [ ] **Step 1: Add explicit authority exclusions to projection lifecycle**

State that `02-authoritative-findings-ledger.md`, `03-target-architecture.md`, `04-remediation-roadmap.md`, `working/INDEX.md`, STM, Architecture, CQ/CQRA, and TE authority cannot receive `PRJ-*`, projection freshness, or `RG-*` state.

- [ ] **Step 2: Add regeneration preflight**

Before an RG plan exists, require each target to resolve to an active registered `PRJ-*` with contract metadata. Otherwise return `REGENERATION_TARGET_NOT_PROJECTION`.

- [ ] **Step 3: Tighten `ALL_STALE`**

Define it exactly as active registered `PRJ-*` identities whose persisted projection freshness is `STALE`.

- [ ] **Step 4: Reassert CURRENT evidence**

Require PRJ identity + contract + dependency snapshot + V1-V4 + fingerprint + accepted revision/NO_CHANGE.

- [ ] **Step 5: Commit**

Commit message: `docs: harden projection regeneration boundaries`.

### Task 3: Harden REVALIDATE semantic closeout and baseline advancement

**Files:**
- Modify: `references/revalidation-and-freshness.md`
- Modify: `references/session-orchestration.md`

**Interfaces:**
- Consumes: proposed delta from REVALIDATE and existing owner gates.
- Produces: explicit baseline role separation and owner-gated advancement.

- [ ] **Step 1: Formalize `PROPOSED_REVALIDATION_DELTA`**

State that the overlay remains proposed until affected owner adjudication accepts revisions.

- [ ] **Step 2: Require delta reconciliation before baseline advancement**

Every material item must be accepted, explicitly preserved/non-material, policy-permitted unresolved, or blocking.

- [ ] **Step 3: Split baseline roles**

Persist `accepted_baseline`, `candidate_baseline`, and `source_head`; forbid moving `accepted_baseline` until `BASELINE_ADVANCE_ALLOWED` is accepted.

- [ ] **Step 4: Require current-baseline model/coverage gates**

Old-baseline acceptance cannot satisfy candidate-baseline advancement.

- [ ] **Step 5: Commit**

Commit message: `docs: gate revalidate baseline advancement`.

### Task 4: Harden report and umbrella closeout

**Files:**
- Modify: `references/report-contract.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: accepted semantic authorities and verified projection lifecycle.
- Produces: explicit closeout validation before any completion claim.

- [ ] **Step 1: Mark 02/03/04 as non-RG semantic authorities**

Keep the existing authority map and add an explicit operational prohibition against including them in `TARGETED`/`ALL_STALE` RG scopes.

- [ ] **Step 2: Add umbrella closeout hard gate**

Before `REVIEW_COMPLETE`, require coherent baseline bindings, owner-gated semantic state, registered/verified projections, package membership, and unresolved-policy accounting.

- [ ] **Step 3: Add anti-shortcut statements**

`Markdown rewritten != CURRENT`; `RG completed != CURRENT`; `baseline pointer changed != baseline accepted`.

- [ ] **Step 4: Commit**

Commit message: `docs: harden final review closeout gate`.

### Task 5: Verification

**Files:**
- Verify all modified files and the hardening reference.

**Interfaces:**
- Consumes: Tasks 1-4.
- Produces: evidence that the observed regression is rejected by every relevant contract boundary.

- [ ] **Step 1: Search/fetch for forbidden RG treatment**

Verify authoritative 02/03/04 files are explicitly excluded from RG/PRJ lifecycle.

- [ ] **Step 2: Verify strict ALL_STALE definition**

Confirm it resolves only registered active `PRJ-*` identities with persisted `STALE` freshness.

- [ ] **Step 3: Verify baseline advancement ordering**

Confirm owner acceptance and current-baseline gates precede accepted-baseline movement.

- [ ] **Step 4: Verify CURRENT evidence**

Confirm no contract permits CURRENT from rewritten Markdown or RG completion alone.

- [ ] **Step 5: Verify human-facing language boundary**

Confirm `README.md` and ordinary `docs/**` were not modified by this hardening.

- [ ] **Step 6: Inspect final commit history and report exact SHAs**

Only claim completion after fresh verification evidence.
