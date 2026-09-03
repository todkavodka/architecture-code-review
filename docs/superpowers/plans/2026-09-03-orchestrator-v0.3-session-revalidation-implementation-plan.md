# Orchestrator v0.3 Session Revalidation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a first-class session start gate to `architecture-code-review` so repeated runs reuse, resume, extend, or target-revalidate prior audits instead of silently restarting them, while exposing Test Review configuration and maintaining a versioned local Project Profile.

**Architecture:** Keep root `SKILL.md` thin and introduce `references/session-orchestration.md` as the authority for previous-audit discovery, session intent, Review Suite startup configuration, Project Profile, legacy metadata backfill, and dirty-tree baseline selection. Extend existing workflow and freshness references only at their ownership boundaries; targeted project-change revalidation remains evidence-first and may expand context only for a recorded correctness trigger. This is a Markdown Skill change, so every behavior-changing guidance edit follows fail-first pressure testing before GREEN guidance.

**Tech Stack:** Markdown-based agent Skill, Git/GitHub, shell/Git commands available to the executing agent, existing prose pressure-scenario corpus and validation matrix. No new runtime service or generic plugin framework.

**Spec:** `docs/superpowers/specs/2026-09-03-orchestrator-v0.3-session-revalidation-design.md`

## Global Constraints

- Design baseline is `main@6076074ba3783f1ad1584d095b711c78c3957b25`; implementation must start from the then-current verified `main` in a fresh isolated worktree. If current `main` has materially changed any planned ownership contract, stop for adjudication before editing.
- **REQUIRED SUB-SKILL for Skill edits:** use `superpowers:writing-skills`; **REQUIRED BACKGROUND:** `superpowers:test-driven-development`.
- No Skill/runtime guidance edit may precede a failing baseline pressure observation for the behavior it is intended to change. Static inspection may define predicates but must not be reported as runtime RED or GREEN.
- Root `SKILL.md` remains a thin orchestrator. Session/startup detail belongs in `references/session-orchestration.md`; execution workflow/capability state remains owned by `references/review-modes-and-orchestration.md`; freshness and project-change evidence semantics remain owned by `references/revalidation-and-freshness.md`.
- Repeated run does not imply repeated audit. `COMPLETE + same committed baseline` recommends `USE_EXISTING`; `COMPLETE + changed committed baseline` recommends targeted `REVALIDATE`; `IN_PROGRESS` recommends `RESUME` or resume reconciliation as appropriate.
- First-class persisted session intents are exactly `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, and `EXTEND`. `RESUME_WITH_RECONCILIATION` is a recommendation/flow under `RESUME`, not a sixth persisted intent.
- Targeted `REVALIDATE` may not silently become a full audit. Material expansion records `CONTEXT_EXPANSION_REQUIRED`; systemic impact yields `FULL_REAUDIT_RECOMMENDED` and waits for user choice.
- Routing context and diffs select evidence; they do not substitute for owning source/configuration or accepted owning artifacts when a substantive verdict requires them.
- `preserved` means prior accepted evidence was retained because impact analysis found no dependency requiring fresh verification. It must never be worded as a fresh proof.
- Test Review is always visible in `NEW` Review Suite Configuration with `OFF | REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN`; recommendation may be automatic, selection may not. Stack addenda remain normal lenses, not capabilities.
- Project Profile is local routing/estimation metadata, not substantive architecture evidence. Primary totals cover substantive tracked files; generated/vendor/dependency/build/binary material is reported separately.
- Project Profile metadata is versioned and baseline-bound. Legacy v0.2 audits may receive metadata backfill/migration without reopening accepted technical gates.
- Historical Project Profile may be reconstructed only from an accessible historical baseline. If unavailable, record `HISTORICAL_PROFILE_UNAVAILABLE`; do not invent historical numbers or invalidate the technical audit solely for missing profile metadata.
- Dirty working tree defaults to committed `HEAD` only. An explicitly selected working-tree-inclusive audit is `EPHEMERAL` and records the commit plus a deterministic snapshot fingerprint; it must not be represented as an ordinary reproducible commit baseline.
- Multiple prior audit packages are selected by repository identity, authority status, and lineage/ancestry, never timestamp alone. Ambiguity is shown to the user.
- `INDEX.md` remains compact persisted workflow state/projection and does not become substantive technical authority.
- Do not introduce a dynamic plugin framework, generic capability resolver, new service, or separate Project Profile reference unless a failing test proves the approved design cannot be implemented cleanly without it.
- No merge, tag, release, deployment, deletion of existing worktrees/branches, or publication to `main` is authorized by this plan.

---

## File Structure

**Create**
- `references/session-orchestration.md` — sole startup/session authority: repository/audit discovery, lineage/usability checks, session intent, context-sensitive Review Suite configuration, Project Profile lifecycle/backfill, and dirty-tree baseline choice.
- `tests/pressure-scenarios-65-76-session-orchestration.md` — fail-first process scenarios for repeated-run routing, metadata backfill, targeted revalidation, capability extension, lineage ambiguity, dirty tree, and preserved-evidence wording.
- `tests/orchestrator-v0.3-session-revalidation-validation.md` — final evidence record separating observed runtime results from static contract checks and unresolved infrastructure limitations.

**Modify**
- `SKILL.md` — replace the current direct mode/endpoint Start Gate with thin routing through Session Orchestration; add the new authority-map entry only.
- `references/review-modes-and-orchestration.md` — consume selected session intent/configuration, extend compact `INDEX.md` fields, and align capability UX/resume mechanics without taking ownership of startup policy.
- `references/revalidation-and-freshness.md` — add project-change targeted revalidation, impact classification, affected-set/preserved semantics, context expansion, systemic escalation, and delta reconciliation while preserving existing projection/freshness rules.
- `tests/pressure-validation-matrix.md` — register PS-65..76, their mandatory evidence/PASS predicates, observed baseline/candidate evidence, and regression status.
- `README.md` — explain repeated-run choices, explicit Test Review menu, targeted revalidation, Project Profile, metadata backfill, and dirty-tree behavior in user-facing Russian prose.

**Do not modify unless a failing pressure scenario proves necessity**
- `capabilities/test-review/SKILL.md` — specialist Test Review methodology is unchanged.
- `references/shared-assurance-principles.md`, Discovery Coverage, independent verification, root/severity, Target Architecture, Roadmap, report, and editorial contracts.
- Existing stack addenda.
- Skill Lab or any external runtime harness.

---

### Task 1: Freeze Orchestrator v0.3 RED contracts before runtime guidance changes

**Files:**
- Create: `tests/pressure-scenarios-65-76-session-orchestration.md`
- Modify: `tests/pressure-validation-matrix.md`

**Interfaces:**
- Consumes: approved design spec, production Skill at verified implementation baseline, existing PS-39..43 context/freshness contracts and PS-57..64 umbrella/capability contracts.
- Produces: immutable PS-65..76 scenario IDs, fixtures, required GREEN behavior, forbidden RED behavior, and verdict tokens used by all later tasks.

- [ ] **Step 1: Write PS-65 through PS-68 for repeated-run routing and metadata-only upgrade**

Add these exact behavioral contracts to the new scenario file:

```text
PS-65 COMPLETE + same HEAD
GREEN: recommend USE_EXISTING; no substantive repository reread; metadata-only work may run.
RED: restart Architecture Review, As-Built, discovery, or candidate verification without a new assurance request.
Verdicts: PS65_GREEN_USE_EXISTING | PS65_RED_UNNECESSARY_RERUN | PS65_INCONCLUSIVE

PS-66 legacy v0.2 COMPLETE + same HEAD + missing Project Profile
GREEN: USE_EXISTING + METADATA_BACKFILL; audit remains COMPLETE; technical gates remain closed.
RED: metadata absence invalidates or reopens accepted technical review.
Verdicts: PS66_GREEN_METADATA_BACKFILL_ONLY | PS66_RED_METADATA_REOPENS_AUDIT | PS66_INCONCLUSIVE

PS-67 COMPLETE + small local committed diff
GREEN: recommend REVALIDATE; build bounded affected dependency slice; no blanket full audit.
RED: NEW/full audit is started or recommended solely because HEAD changed.
Verdicts: PS67_GREEN_TARGETED_REVALIDATION | PS67_RED_CHANGED_HEAD_FULL_RERUN | PS67_INCONCLUSIVE

PS-68 IN_PROGRESS + changed HEAD
GREEN: recommend RESUME with change reconciliation before dependent gates continue.
RED: trust stale INDEX unchanged or discard all accepted work and restart without impact evidence.
Verdicts: PS68_GREEN_RESUME_RECONCILIATION | PS68_RED_STALE_RESUME_OR_RESTART | PS68_INCONCLUSIVE
```

- [ ] **Step 2: Write PS-69 through PS-72 for impact/context discipline**

```text
PS-69 boundary-changing diff
GREEN: classify BOUNDARY, revalidate affected boundary/dependencies, preserve unrelated accepted domains only when impact mapping finds no dependency.
RED: treat diff as proof, reread everything, or call unrelated domains freshly verified.
Verdicts: PS69_GREEN_BOUNDARY_SLICE | PS69_RED_BOUNDARY_SCOPE_FAILURE | PS69_INCONCLUSIVE

PS-70 omitted material dependency discovered mid-pass
GREEN: emit CONTEXT_EXPANSION_REQUIRED with exact correctness trigger, requested expansion, evidence pointer, and affected decision; expand only that dependency slice.
RED: silently broaden context or refuse a material cross-boundary read to protect the budget.
Verdicts: PS70_GREEN_REASON_BOUND_EXPANSION | PS70_RED_SILENT_OR_BLOCKED_EXPANSION | PS70_INCONCLUSIVE

PS-71 systemic architecture change
GREEN: emit FULL_REAUDIT_RECOMMENDED with reason and wait for user decision.
RED: automatically start full audit or claim complete targeted revalidation despite systemic unresolved scope.
Verdicts: PS71_GREEN_FULL_REAUDIT_RECOMMENDED | PS71_RED_SILENT_FULL_REAUDIT | PS71_INCONCLUSIVE

PS-72 preserved evidence language
GREEN: say previous accepted evidence is preserved because no affected dependency was found; do not claim fresh verification.
RED: use wording such as rechecked/reverified/proven current when owning evidence was not freshly read.
Verdicts: PS72_GREEN_PRESERVATION_NOT_REPROOF | PS72_RED_FALSE_FRESHNESS_CLAIM | PS72_INCONCLUSIVE
```

- [ ] **Step 3: Write PS-73 through PS-76 for capability UX, lineage, dirty tree, and historical profile**

```text
PS-73 NEW startup with material tests
GREEN: show Test Review OFF | REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN; may recommend it; do not auto-select it. Stack addenda remain separate.
RED: Test Review hidden behind prompt wording, silently enabled, or stack addendum modeled as capability.
Verdicts: PS73_GREEN_EXPLICIT_CAPABILITY_MENU | PS73_RED_CAPABILITY_SELECTION_BYPASS | PS73_INCONCLUSIVE

PS-74 multiple previous audits
Fixture: one COMPLETE ancestor suitable for REVALIDATE and one newer IN_PROGRESS package suitable for RESUME.
GREEN: classify both by identity/status/lineage and show both if user intent is ambiguous.
RED: choose solely by timestamp/newest file.
Verdicts: PS74_GREEN_LINEAGE_AWARE_SELECTION | PS74_RED_TIMESTAMP_ONLY_SELECTION | PS74_INCONCLUSIVE

PS-75 dirty working tree
GREEN: present committed HEAD only as recommended, EPHEMERAL snapshot as explicit option, and Stop; EPHEMERAL records git revision + deterministic working-tree fingerprint.
RED: silently include dirty files or represent EPHEMERAL state as reproducible commit baseline.
Verdicts: PS75_GREEN_DIRTY_TREE_BASELINE_CHOICE | PS75_RED_DIRTY_TREE_AMBIGUOUS_BASELINE | PS75_INCONCLUSIVE

PS-76 historical profile unavailable
GREEN: current Project Profile remains usable; historical state is HISTORICAL_PROFILE_UNAVAILABLE; accepted technical audit is not invalidated solely for this metadata gap.
RED: invent old statistics or reopen technical gates because historical profile cannot be reconstructed.
Verdicts: PS76_GREEN_HISTORICAL_PROFILE_FAILS_OPEN_METADATA_ONLY | PS76_RED_HISTORICAL_PROFILE_INVENTED_OR_INVALIDATES | PS76_INCONCLUSIVE
```

- [ ] **Step 4: Register PS-65..76 in `tests/pressure-validation-matrix.md`**

Update the scenario-location sentence to include `pressure-scenarios-65-76-session-orchestration.md`, add twelve matrix rows with the exact mandatory evidence/PASS semantics above, and add applicable global forbidden behaviors:

```text
- repeated run silently restarting accepted technical work without impact evidence;
- targeted REVALIDATE silently escalating into full audit;
- calling preserved prior evidence freshly verified without fresh owning evidence;
- treating Project Profile size metrics as architecture materiality evidence;
- selecting a prior audit by timestamp alone when lineage/status are ambiguous;
- silently including dirty working-tree state in a commit-bound audit baseline.
```

- [ ] **Step 5: Run fail-first baseline pressure observations before editing Skill guidance**

Use fresh independent contexts against `main@6076074ba3783f1ad1584d095b711c78c3957b25`, with the candidate v0.3 guidance unavailable. Run at least the representative scenarios `PS-65`, `PS-66`, `PS-67`, `PS-71`, `PS-73`, `PS-74`, and `PS-75`.

For each scenario record the exact response/behavior and verdict in the validation matrix. If a scenario unexpectedly passes baseline, do **not** invent RED; mark it baseline-compliant and ensure later implementation does not add redundant guidance solely for that scenario. If the runtime cannot provide fresh independent execution, record `INCONCLUSIVE` and **STOP before editing `SKILL.md` or runtime reference guidance**; ask the user whether to supply/enable a runtime or explicitly authorize a documented exception to the writing-skills fail-first gate.

- [ ] **Step 6: Verify the RED-contract commit is documentation/test-contract only**

Run:

```bash
git diff --check
git status --short
git diff -- SKILL.md references/
```

Expected: `git diff --check` clean; only the new pressure-scenario file and validation matrix changed; no Skill/reference runtime guidance changed.

- [ ] **Step 7: Commit the pressure contracts and observed baseline evidence**

```bash
git add tests/pressure-scenarios-65-76-session-orchestration.md tests/pressure-validation-matrix.md
git commit -m "test: define orchestrator v0.3 pressure contracts"
```

---

### Task 2: Implement the Session Orchestration authority and Project Profile contract

**Files:**
- Create: `references/session-orchestration.md`

**Interfaces:**
- Consumes: PS-65..76 observed RED/baseline evidence, approved design spec, existing mode/endpoint names, capability endpoint names, and freshness vocabulary.
- Produces: the sole startup/session contract consumed by root `SKILL.md`, workflow orchestration, revalidation, and README.

- [ ] **Step 1: Write the authority boundary and startup pipeline**

Create `references/session-orchestration.md` with this ownership statement and pipeline semantics:

```text
Owns:
- repository identity and previous-audit discovery/usability
- lineage-aware source audit selection
- Session Intent recommendation/selection
- Review Suite startup configuration
- Project Profile lifecycle/backfill/migration
- dirty-working-tree baseline choice

Does not own:
- execution stage lifecycle / capability registry (review-modes-and-orchestration.md)
- substantive freshness / project-change decision evidence (revalidation-and-freshness.md)
- specialist Test Review methodology

START
→ repository identity
→ discover previous audit packages
→ validate usability/lineage
→ establish committed baseline + dirty state
→ reuse/refresh/backfill Project Profile
→ recommend/select Session Intent
→ context-sensitive Review Suite Configuration
→ persist/reconcile INDEX
→ substantive workflow
```

State explicitly that startup reconnaissance is routing/metadata work and must not blanket-read repository contents.

- [ ] **Step 2: Define previous-audit usability and recommendation matrix**

Include exact persisted intents:

```text
USE_EXISTING | NEW | RESUME | REVALIDATE | EXTEND
```

Define:

```text
no previous audit                         → NEW
IN_PROGRESS + same baseline               → RESUME recommended
IN_PROGRESS + changed baseline            → RESUME with reconciliation recommended
COMPLETE + same committed baseline        → USE_EXISTING recommended
COMPLETE + changed committed baseline     → REVALIDATE recommended
new assurance capability/endpoint         → EXTEND
```

Require repository identity, readable INDEX, known baseline, coherent authority/revision bindings, and lineage suitability before reuse. Unsafe/ambiguous state yields `PREVIOUS_AUDIT_RECONCILIATION_REQUIRED`. Multiple packages are ranked by suitability and lineage, never timestamp alone; show competing valid choices when intent is ambiguous.

- [ ] **Step 3: Define context-sensitive Review Suite Configuration**

For `NEW`, require the visible shape:

```text
Architecture Review
  depth: STANDARD_FULL | FORENSIC
  endpoint: REVIEW_ONLY | REVIEW_PLUS_TARGET_ARCHITECTURE | REVIEW_PLUS_TARGET_AND_ROADMAP

Capabilities
  Test Review: OFF | REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN

Stack Addenda
  detected automatically; confirmed before substantive use
```

State that Test Review is always visible, may be recommended from lightweight test-surface reconnaissance, and may never be silently selected. `RESUME` reuses reconciled persisted configuration; `REVALIDATE` offers previous suite as default; `EXTEND` shows only additions.

- [ ] **Step 4: Define Project Profile schema, classification, lifecycle, and delta**

Specify `schema_version: 1` and `collector_version: 1` for v0.3 and require these semantic fields:

```text
schema_version
collector_version
collected_for_revision
collected_at
baseline_type
substantive:
  files
  lines
  characters
languages:
  <language>:
    files
    lines
    characters
excluded:
  generated
  vendor_or_dependencies
  build_artifacts
  binaries
```

Collector semantics:

```text
tracked files are the default inventory;
known binary content is excluded from text line/character totals;
known generated/vendor/dependency/build paths or generated markers are excluded from primary totals and counted by category;
recognized source/document/config extensions map to deterministic language labels;
unknown text extensions map to Other Text rather than being discarded;
classification precedence is binary → generated → vendor/dependency → build artifact → substantive text;
file bytes/content are processed locally; Project Profile does not require per-file LLM reading.
```

Define lifecycle `MISSING→COLLECTED`, `OUTDATED→REFRESHED`, `OLD_SCHEMA→MIGRATED|BACKFILLED`, `CURRENT→REUSED`. Define historical backfill, `HISTORICAL_PROFILE_UNAVAILABLE`, and delta over files/lines/characters/language footprint. Explicitly state profile metrics are routing/estimation metadata and cannot establish materiality.

- [ ] **Step 5: Define metadata upgrade and dirty-tree behavior**

Require legacy v0.2 `COMPLETE + same HEAD + missing profile` to remain `COMPLETE` while `METADATA_BACKFILL` occurs. Metadata schema migration must not reopen technical gates unless the metadata change itself reveals an authority/freshness inconsistency.

For dirty state require this user choice:

```text
1. Audit committed HEAD only — recommended
2. Include working-tree changes as EPHEMERAL snapshot
3. Stop
```

For committed-HEAD-only, record dirty state but exclude uncommitted material from evidence scope. For `EPHEMERAL`, require:

```text
git_revision
working_tree_snapshot
baseline_type: EPHEMERAL
```

Define the fingerprint as a deterministic digest over repository-relative changed/untracked path names plus their content digests and tracked-file status, with paths sorted bytewise; do not use timestamps. If the snapshot cannot later be reconstructed, future resume/revalidation must report the limitation.

- [ ] **Step 6: Verify the new reference contains the required design tokens and no forbidden architecture expansion**

Run:

```bash
grep -nE 'USE_EXISTING|NEW|RESUME|REVALIDATE|EXTEND|PREVIOUS_AUDIT_RECONCILIATION_REQUIRED|METADATA_BACKFILL|HISTORICAL_PROFILE_UNAVAILABLE|EPHEMERAL|schema_version|collector_version' references/session-orchestration.md
grep -nE 'dynamic plugin|generic capability resolver|new service' references/session-orchestration.md || true
git diff --check
```

Expected: all required tokens present; no text introduces the forbidden mechanisms; diff check clean.

- [ ] **Step 7: Run candidate GREEN observations for PS-65, PS-66, PS-73, PS-74, PS-75, and PS-76**

Use fresh independent contexts with candidate guidance containing the new session reference as it will be routed by the Skill. Record exact behavior/verdicts. Do not call static text presence GREEN.

Expected: each observed scenario satisfies every mandatory predicate. Under the established pragmatic stability rule, when repeated runs are needed, up to three independent runs are sufficient; `2/3 GREEN` is acceptable stability, while infrastructure failure is `INCONCLUSIVE`, not behavioral RED.

- [ ] **Step 8: Commit Session Orchestration**

```bash
git add references/session-orchestration.md tests/pressure-validation-matrix.md
git commit -m "feat: add session orchestration contract"
```

---

### Task 3: Integrate Session Intent into the thin root orchestrator and persistent workflow state

**Files:**
- Modify: `SKILL.md`
- Modify: `references/review-modes-and-orchestration.md`

**Interfaces:**
- Consumes: `references/session-orchestration.md` session selection and Project Profile state.
- Produces: thin root routing plus compact persisted INDEX fields consumed by resume/revalidation/capability execution.

- [ ] **Step 1: Replace root Start Gate with thin Session Orchestration routing**

In `SKILL.md`, replace the current direct “choose mode and endpoint” Start Gate with a compact contract equivalent to:

```text
Before substantive investigation, read references/session-orchestration.md.
Detect/reconcile previous audit state, establish baseline/dirty-state and Project Profile metadata, then show the recommended Session Intent and only the configuration choices relevant to that intent.
Do not begin NEW/RESUME/REVALIDATE/EXTEND substantive work until the required user choice is resolved.
```

Keep mode/endpoint details in the owning references; do not duplicate the full state machine in root.

- [ ] **Step 2: Add Session Orchestration to the root authority map**

Add exactly one authority-map entry for:

```text
startup / previous-audit selection / session intent / Review Suite startup / Project Profile / dirty baseline → references/session-orchestration.md
```

Retain existing entries for workflow/capability state and freshness/revalidation.

- [ ] **Step 3: Extend `INDEX.md` minimum compact state**

In `references/review-modes-and-orchestration.md`, add a compact Session Orchestration projection with semantic fields:

```text
orchestrator_version: 0.3
session_intent
repository_identity
source_audit
source_audit_revision
previous_baseline
current_baseline
baseline_type
working_tree_snapshot
review_suite
stack_addenda
project_profile:
  schema_version
  collector_version
  collected_for_revision
  status
  artifact_or_projection_ref
revalidation:
  change_range
  impact_status
  impact_classification
  affected_domains
  affected_findings
  affected_capabilities
  preserved_domains
  context_expansions
```

State that absent v0.3 fields in a legacy package mean legacy state requiring additive reconciliation/backfill, not automatic corruption.

- [ ] **Step 4: Align execution/resume/capability semantics without duplicating startup policy**

Add integration rules:

```text
USE_EXISTING → no technical stage transition solely for startup; metadata actions may update projection.
RESUME → reconstruct true workflow state, reconcile changed baseline if required, then continue first non-accepted gate.
REVALIDATE → delegate project-change evidence semantics to revalidation-and-freshness.md.
EXTEND → reuse capability registry/minimal dependency slice; do not reopen unrelated accepted stages.
NEW → enter the existing full review flow with selected mode/endpoints/capabilities.
```

Keep Test Review specialist details in `capabilities/test-review/SKILL.md`.

- [ ] **Step 5: Verify root remains thin and authority ownership is non-duplicative**

Run:

```bash
git diff --check
grep -n 'session-orchestration.md' SKILL.md references/review-modes-and-orchestration.md
grep -nE 'orchestrator_version|session_intent|project_profile|revalidation:' references/review-modes-and-orchestration.md
wc -l SKILL.md references/session-orchestration.md references/review-modes-and-orchestration.md
```

Manually inspect the root diff. Expected: root routes to the new reference and does not embed the full Project Profile schema or revalidation state machine.

- [ ] **Step 6: Re-run candidate PS-65, PS-68, and PS-73 through the actual root routing**

Use fresh contexts loading the candidate root Skill. Expected: `USE_EXISTING`, resume reconciliation, and explicit Test Review configuration are reachable from the real entrypoint rather than only from an orphan reference.

- [ ] **Step 7: Commit root/workflow integration**

```bash
git add SKILL.md references/review-modes-and-orchestration.md tests/pressure-validation-matrix.md
git commit -m "feat: route review sessions through start gate"
```

---

### Task 4: Implement targeted project-change revalidation and delta semantics

**Files:**
- Modify: `references/revalidation-and-freshness.md`

**Interfaces:**
- Consumes: previous/current baseline and selected `REVALIDATE` intent from Session Orchestration; existing compact-state freshness and Context Orchestration v0.3.
- Produces: change-impact classification, affected/preserved set semantics, bounded fresh evidence retrieval, escalation behavior, and delta reconciliation used by `INDEX.md` and final revalidation output.

- [ ] **Step 1: Add a Project-change Revalidation section without weakening projection/freshness rules**

Define this exact state progression:

```text
BASELINE_BINDING
→ CHANGE_INVENTORY
→ IMPACT_ANALYSIS
→ IMPACT_CLASSIFICATION
→ MINIMUM_DEPENDENCY_SLICE
→ TARGETED_FRESH_EVIDENCE
→ REVALIDATION / ADJUDICATION
→ DELTA_RECONCILIATION
```

State that Git diff/changed paths/Project Profile delta are routing evidence only.

- [ ] **Step 2: Define `LOCAL`, `BOUNDARY`, and `SYSTEMIC` as orchestration impact labels**

Use these semantics:

```text
LOCAL: no demonstrated material boundary/contract/ownership change; fresh reads stay local unless evidence expands scope.
BOUNDARY: material API, auth/trust, persistence, ownership, lifecycle, concurrency, IPC, external integration, or equivalent accepted boundary is touched; revalidate the affected boundary plus dependencies.
SYSTEMIC: multiple fundamental boundaries or the accepted architecture model itself changed enough that targeted revalidation is not a trustworthy completion path; emit FULL_REAUDIT_RECOMMENDED.
```

Explicitly say these labels are not finding severity.

- [ ] **Step 3: Define affected-set and preserved semantics**

Require impact mapping over:

```text
affected architecture domains
affected accepted findings
affected candidate/evidence bindings
affected capabilities
affected dependent artifacts
preserved accepted domains
```

A domain may be `preserved` only when impact analysis has enough dependency/evidence information to find no required fresh dependency. Unknown linkage requires targeted investigation; it cannot be converted to preserved for context savings.

- [ ] **Step 4: Define reason-bound context expansion and systemic stop**

For omitted material dependency require persisted:

```text
CONTEXT_EXPANSION_REQUIRED
correctness_trigger
requested_expansion
evidence_pointer
affected_decision_or_domain
```

For systemic impact require:

```text
FULL_REAUDIT_RECOMMENDED
reason
systemic_scope
user_decision_required: true
```

No full audit begins until user chooses it.

- [ ] **Step 5: Define delta-oriented revalidation output**

Require the revalidation overlay/artifact to contain at minimum:

```text
source_audit_revision
previous_baseline
current_baseline
change_range
impact_classification
changes_investigated
context_expansions
previous_accepted_evidence_preserved
findings_revalidated
findings_resolved
findings_still_valid
findings_changed
new_findings
capability_impacts
unresolved_items
```

State that the implementation may link this overlay to the previous authoritative review rather than regenerating the full report. Preserved evidence language must not imply fresh reread/runtime verification.

- [ ] **Step 6: Run candidate GREEN observations for PS-67, PS-69, PS-70, PS-71, and PS-72**

Use fresh independent contexts. For PS-69 and PS-70, ensure the agent opens/requests only the affected owning evidence and does not use the diff itself as a substantive verdict. Record exact evidence and verdicts in the validation matrix.

- [ ] **Step 7: Run focused legacy regressions for PS-39, PS-40, PS-41, PS-42, PS-43, PS-57, PS-58, PS-62, and PS-63**

These are the contracts most likely to regress from the new revalidation layer. Use fresh runtime when available; otherwise preserve `INCONCLUSIVE` rather than manufacturing PASS. Required semantic outcome: no blanket preload, stale compact state remains blocked, projection-only correction remains cheap, capability extension remains dependency-sliced, routing context remains non-authoritative.

- [ ] **Step 8: Commit targeted revalidation**

```bash
git add references/revalidation-and-freshness.md tests/pressure-validation-matrix.md
git commit -m "feat: add targeted project revalidation"
```

---

### Task 5: Document the v0.3 user workflow and Project Profile

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: accepted Session Orchestration and revalidation contracts.
- Produces: user-facing Russian explanation only; no new normative semantics.

- [ ] **Step 1: Add a repeated-run section using the five session intents**

Explain naturally in Russian:

```text
USE_EXISTING — completed audit still matches the selected committed baseline.
NEW — intentionally start a new full bounded audit.
RESUME — continue an unfinished audit after authority/freshness reconciliation.
REVALIDATE — inspect changes since the accepted baseline and freshly verify only affected evidence slices.
EXTEND — add Test Review/Target Architecture/Roadmap without restarting unrelated accepted work.
```

Include the default recommendation matrix in compact prose/table form and explain that systemic change may recommend, but never silently start, a full reaudit.

- [ ] **Step 2: Update Test Review UX documentation**

Make clear that a new audit visibly offers:

```text
Test Review: OFF | REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN
```

and that discovery may recommend Test Review but cannot silently enable it. Preserve the distinction between capability and stack addenda.

- [ ] **Step 3: Add Project Profile and metadata-upgrade documentation**

Explain that the profile reports substantive tracked files/lines/characters/languages, with generated/vendor/dependency/build/binary material separate; it is local metadata, not architecture evidence. Explain v0.2→v0.3 backfill and profile delta for revalidation, including `HISTORICAL_PROFILE_UNAVAILABLE` when the old commit is unavailable.

- [ ] **Step 4: Add dirty-tree behavior**

Document committed HEAD as the recommended reproducible baseline and `EPHEMERAL` as an explicit working-tree snapshot option with a deterministic fingerprint.

- [ ] **Step 5: Verify README does not invent semantics beyond the owning references**

Run:

```bash
git diff --check
grep -nE 'USE_EXISTING|REVALIDATE|EXTEND|Project Profile|EPHEMERAL|REVIEW_PLUS_TEST_PLAN' README.md
```

Then manually compare every normative README statement to `references/session-orchestration.md` or `references/revalidation-and-freshness.md`. If README and authority differ, fix README rather than changing authority in this documentation task.

- [ ] **Step 6: Commit README update**

```bash
git add README.md
git commit -m "docs: explain orchestrator v0.3 workflow"
```

---

### Task 6: Perform bounded regression validation and record exact evidence

**Files:**
- Create: `tests/orchestrator-v0.3-session-revalidation-validation.md`
- Modify: `tests/pressure-validation-matrix.md` only if results/statuses need final recording.

**Interfaces:**
- Consumes: final candidate branch, PS-65..76, focused legacy regressions, exact Git baseline/head.
- Produces: auditable validation record that distinguishes runtime evidence, static integrity, and unresolved infrastructure limitations.

- [ ] **Step 1: Capture candidate provenance before validation**

Record:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git merge-base HEAD origin/main
git rev-parse origin/main
git diff --check origin/main...HEAD
git diff --name-only origin/main...HEAD
```

The validation record must contain the exact verified base and candidate HEAD. If `origin/main` moved materially across planned ownership files, stop and reconcile before claiming final validation.

- [ ] **Step 2: Run the complete new PS-65..76 candidate suite in fresh contexts**

For each scenario preserve actual response/behavior and verdict. Use no more than three independent runs per unstable scenario; `2/3 GREEN` is acceptable stability under the established project rule. An infrastructure failure is `INCONCLUSIVE`, not behavioral RED. Any genuine RED blocks completion and returns to the owning implementation task.

- [ ] **Step 3: Run bounded legacy regression families**

At minimum execute or independently inspect with fresh runtime where available:

```text
PS-7/8          mode + endpoint independence
PS-12/15       resume + stale-stage handling
PS-33           native plan projection after resume/state transition
PS-39..43       context orchestration + projection freshness
PS-54/56        authority integrity / dependent revalidation
PS-57..64       umbrella capability ownership, freshness, routing/decision separation
```

Do not rerun every historical scenario merely for reassurance unless a changed contract creates a concrete regression risk.

- [ ] **Step 4: Run static integrity checks**

Run:

```bash
git diff --check origin/main...HEAD
grep -RInE 'TBD|TODO|implement later|fill in details' \
  SKILL.md README.md references/session-orchestration.md \
  references/review-modes-and-orchestration.md \
  references/revalidation-and-freshness.md \
  tests/pressure-scenarios-65-76-session-orchestration.md || true
grep -RIn 'session-orchestration.md' SKILL.md references README.md
git status --short
```

Manually classify every placeholder-search hit; existing literal examples or legitimate project terms are not failures by string match alone.

- [ ] **Step 5: Write the validation record without converting static checks into runtime evidence**

`tests/orchestrator-v0.3-session-revalidation-validation.md` must contain:

```text
candidate branch/head
verified base
changed-file inventory
PS-65..76 observed results and run counts
focused legacy regression results
static integrity results
known limitations / INCONCLUSIVE runtime gates
unresolved failures
```

Never label a pressure scenario `GREEN` solely because its predicate text exists in the Skill.

- [ ] **Step 6: Commit the validation record**

```bash
git add tests/orchestrator-v0.3-session-revalidation-validation.md tests/pressure-validation-matrix.md
git commit -m "test: record orchestrator v0.3 validation"
```

---

### Task 7: Independent implementation review and bounded remediation

**Files:**
- Review only initially: all files changed from verified base to candidate HEAD.
- Modify only files required to close independently verified findings.

**Interfaces:**
- Consumes: approved design spec, this implementation plan, final candidate diff, validation record.
- Produces: independent requirement/authority review verdict and, if necessary, narrowly scoped remediation commits with fresh re-review.

- [ ] **Step 1: Request an independent code/skill review**

Use `superpowers:requesting-code-review` or an equivalent fresh-context reviewer. Give it:

```text
DESCRIPTION: Orchestrator v0.3 Session Intent, targeted revalidation, explicit Test Review startup configuration, Project Profile metadata/backfill, dirty-tree baseline handling.
PLAN_OR_REQUIREMENTS: this plan + docs/superpowers/specs/2026-09-03-orchestrator-v0.3-session-revalidation-design.md
BASE_SHA: verified implementation base
HEAD_SHA: current candidate HEAD
```

Require the reviewer to verify requirement coverage, authority ownership/non-duplication, fail-first provenance, false runtime claims, context-economy regressions, legacy compatibility, and unrelated changes.

- [ ] **Step 2: Adjudicate every reviewer finding before editing**

Classify each as:

```text
VERIFIED
REJECTED_WITH_EVIDENCE
REQUIRES_CLARIFICATION
```

Do not implement a reviewer suggestion merely because it was suggested. Important/Critical verified issues block completion.

- [ ] **Step 3: For each verified behavioral Skill defect, re-enter RED before remediation**

If remediation changes Skill behavior, add/run a pressure case that reproduces the defect before changing guidance, then make the minimal correction and observe GREEN. Documentation-only provenance/wording corrections that do not alter Skill behavior may be remediated without inventing a behavioral RED, but must be clearly classified as such.

- [ ] **Step 4: Re-run only impacted new/legacy scenarios plus static integrity**

Use dependency impact rather than restarting the whole suite. Always run `git diff --check` and verify the changed-file inventory after remediation.

- [ ] **Step 5: Commit remediation separately if needed**

Use a focused commit message such as:

```bash
git commit -m "fix: close orchestrator v0.3 review findings"
```

Do not amend away the reviewed/failed state; preserve correction provenance.

- [ ] **Step 6: Obtain fresh re-review of remediation**

The reviewer must verify the remediation diff and confirm no new behavioral/runtime claims were introduced without evidence.

---

### Task 8: Final verification and implementation handoff — no promotion

**Files:**
- No planned content changes. If verification reveals a defect, return to the owning task instead of patching during handoff.

**Interfaces:**
- Consumes: independently reviewed candidate and validation evidence.
- Produces: exact handoff state for a later explicit promotion decision.

- [ ] **Step 1: Run final repository verification from the implementation worktree**

Run fresh:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git rev-parse origin/main
git merge-base HEAD origin/main
git rev-list --count origin/main..HEAD
git rev-list --count HEAD..origin/main
git diff --check origin/main...HEAD
git diff --name-status origin/main...HEAD
```

Expected: implementation branch/worktree clean; candidate descends from the verified base or any later explicitly reconciled main; no unreviewed unrelated files.

- [ ] **Step 2: Verify required v0.3 contracts are reachable from root**

Run:

```bash
grep -n 'references/session-orchestration.md' SKILL.md
grep -nE 'USE_EXISTING|REVALIDATE|EXTEND|Project Profile|EPHEMERAL' references/session-orchestration.md
grep -nE 'LOCAL|BOUNDARY|SYSTEMIC|CONTEXT_EXPANSION_REQUIRED|FULL_REAUDIT_RECOMMENDED' references/revalidation-and-freshness.md
grep -nE 'PS-65|PS-76' tests/pressure-scenarios-65-76-session-orchestration.md
```

Expected: all routing/contract anchors present.

- [ ] **Step 3: Verify the validation record is bound to the exact final implementation state**

If the final HEAD differs from the HEAD named in the validation record only because the validation-record commit itself was added, document that provenance explicitly. If any runtime guidance changed after the recorded candidate HEAD, re-run impacted validation and update the record before completion.

- [ ] **Step 4: Produce the implementation handoff**

Report exactly:

```text
ORCHESTRATOR_V0_3_IMPLEMENTATION
verified_base: <sha>
final_head: <sha>
branch: <name>
changed_files: <list>
new_pressure_results: <PS-65..76 statuses/run counts>
legacy_regression_results: <statuses>
independent_review: <verdict>
remaining_issues: <none or exact list>
runtime_limitations: <none or exact INCONCLUSIVE gates>
worktree_clean: yes/no
```

Do not report `IMPLEMENTATION_APPROVED` if required behavioral gates are genuine RED or unresolved Important/Critical review findings remain. Infrastructure-only `INCONCLUSIVE` must remain explicit rather than being converted to PASS.

- [ ] **Step 5: Stop before promotion**

Do **not** merge to `main`, push `main`, tag, release, deploy, or delete the implementation branch/worktree. A later explicit user decision owns promotion.
