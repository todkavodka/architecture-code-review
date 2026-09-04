# Stage B — Audit Projection & Regeneration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Stage B projection lifecycle, impact accounting, deterministic regeneration, verification, and gate-scoped freshness on top of the Stage A semantic authorities without introducing a competing authority layer.

**Architecture:** Stage B remains a Markdown/Git Skill contract evolution. Capabilities own projection meaning; the shared Projection Layer owns projection identity, freshness, dependency lifecycle, impact analysis, regeneration planning/execution, verification, fingerprints, and scoped freshness gates. Semantic changes only mark projections stale; regeneration is an explicit separate workflow.

**Tech Stack:** Markdown, Git, existing Skill/reference contracts, pressure scenarios, static/contract validation. No database, runtime service, generic query engine, or executable coordinator is introduced.

**Spec:**
- `docs/superpowers/specs/2026-09-04-audit-projection-regeneration-design.md`
- `docs/superpowers/specs/2026-09-04-audit-projection-regeneration-design-remediation.md`

## Global Constraints

- Base implementation from canonical `main@0ba7c4b5b556ba0de78200d6a6792b408b42523b` unless the execution prompt explicitly pins a later verified main.
- The remediation addendum is normative and supersedes conflicting wording in the base design.
- Projection never becomes semantic authority.
- Semantic change must not implicitly regenerate projection content.
- Projection regeneration must not mutate semantic authority.
- `working/INDEX.md` remains coordinator-owned workflow authority and must never enter `PRJ-*`, regeneration, fingerprint, drift, retirement, or Projection Impact lifecycles.
- Existing Stage A `PROJECTION_REPAIR` semantics remain valid for bounded presentation-only correction when semantic meaning is unchanged.
- Projection dependency edge direction is always `CONSUMER -> PREREQUISITE`.
- Direct dependency metadata belongs to the consumer; reverse/global dependency views remain generated.
- Projection-to-projection regeneration prerequisite graph must be acyclic; the wider semantic/artifact graph may contain cycles.
- `TARGETED` execution scope is requested targets plus required stale upstream prerequisites only; downstream consumers are impact propagation, not automatic execution scope.
- `ALL_STALE` uses a frozen stale-at-planning snapshot and never loops until globally clean.
- `REGENERATED != CURRENT`; V1–V4 verification is required before CURRENT.
- Identical verified output creates `NO_CHANGE`, no new projection revision, and no downstream revision invalidation.
- Generated projection content is fully generated. Persistent human meaning must live in semantic authority.
- Existing final Architecture Review composite-authority behavior must be migrated so persistent architecture meaning resides in Architecture semantic authority before fully generated final-report projection behavior is permitted.
- Implementation remains Markdown/Git based; runtime validation is unavailable unless the repository gains an executable coordinator independently of this stage.
- Every behavior-changing contract update follows fail-first pressure discipline where applicable.
- Do not merge, tag, release, deploy, or delete branches as part of this implementation plan.

---

## Planned File Structure

The implementation should follow existing repository patterns and keep root orchestration thin.

### Shared Stage B authority/reference contracts

Create focused references:

- `references/projection-lifecycle.md`
  - PRJ identity/revision/lifecycle/freshness/required-action semantics
  - fully-generated projection policy
  - fingerprints and `NO_CHANGE`
  - manual drift semantics

- `references/projection-dependencies.md`
  - `SEMANTIC_EXACT`, `SEMANTIC_SELECTOR`, `PROJECTION_EXACT`
  - controlled selector contract
  - direct dependency authority
  - canonical `CONSUMER -> PREREQUISITE` edge direction
  - DAG/cycle rules

- `references/projection-impact.md`
  - semantic-delta input
  - exact/selector/contract/drift impact
  - stale/BLOCKED propagation
  - `PROJECTION_IMPACT_ACCOUNTED`
  - freshness reconciliation after upstream `NO_CHANGE`

- `references/projection-regeneration.md`
  - `RG-*`
  - TARGETED / ALL_STALE
  - frozen plan
  - upstream closure
  - topological execution
  - partial progress / failure isolation
  - input drift
  - session outcomes

- `references/projection-verification.md`
  - V1 STRUCTURAL
  - V2 DEPENDENCY / PROVENANCE
  - V3 CONTRACT COMPLETENESS
  - V4 AUTHORITY CONSISTENCY
  - verification failure vocabulary
  - verifier may compare against authority but never adjudicate it

- `references/projection-gates-and-packages.md`
  - projection packages
  - `PERMISSIVE`, `REQUIRED_SCOPE_CURRENT`, `ALL_SCOPED_CURRENT`
  - unrelated stale projections visible but non-blocking outside gate scope
  - closeout/publication chain

### Existing shared references to update

Modify as required:

- `SKILL.md`
- `references/session-orchestration.md`
- `references/revalidation-and-freshness.md`
- `references/shared-assurance-principles.md`
- `references/report-contract.md`
- `references/review-modes-and-orchestration.md`
- `references/technical-documentation.md`
- `references/technical-model-dependencies.md`

### Capability integration

Modify as required:

- `capabilities/test-review/SKILL.md`
- `capabilities/test-review/references/test-engineering-contract.md`

Architecture remains primarily rooted in the shared root references plus `references/report-contract.md`; do not create a parallel Architecture projection authority file unless a pressure failure proves it necessary.

### Tests / pressure artifacts

Create:

- `tests/projection-regeneration-foundation-validation.md`

Extend:

- `tests/pressure-validation-matrix.md`

Use the next available pressure IDs after the current Stage A range. At the Stage B baseline this plan expects `PS-100..PS-114`; if the repository has gained newer accepted IDs before execution, preserve monotonic numbering and record the resolved range before editing tests.

---

## Task 1: Freeze Stage B fail-first pressure contracts

**Files:**
- Modify: `tests/pressure-validation-matrix.md`
- Create: `tests/projection-regeneration-foundation-validation.md`
- Read: both approved Stage B design documents
- Read: current Stage A validation and pressure ranges

**Interfaces:**
- Consumes: approved Stage B design semantics.
- Produces: pressure scenarios that later tasks must make GREEN without changing their expected semantics.

- [ ] **Step 1: Resolve the next pressure range**

Run:

```bash
grep -R "PS-[0-9][0-9]*" tests | sed -E 's/.*PS-([0-9]+).*/\1/' | sort -n | tail -20
```

Record the highest accepted pressure ID. Use `PS-100..PS-114` only if `99` is still the current maximum.

Expected: monotonic unused Stage B range.

- [ ] **Step 2: Add fail-first Stage B scenarios**

Add explicit scenarios covering at minimum:

```text
Projection classification protects semantic authorities and working/INDEX.md
Semantic change marks projection STALE without regeneration
Selector membership add/remove causes stale impact
Projection dependency edge direction is CONSUMER -> PREREQUISITE
Upstream STALE propagates freshness uncertainty downstream
Upstream NO_CHANGE permits freshness reconciliation
Verified upstream new revision invalidates downstream
TARGETED expands only stale prerequisites
ALL_STALE freezes planning snapshot
Independent branch failure permits partial progress
Manual projection drift is detected and disposable
Missing/stale/conflicting semantic authority blocks regeneration
V1..V4 required before CURRENT
Gate-scoped freshness ignores unrelated stale projections
Legacy projection cannot become CURRENT without registration + verification
```

Each scenario must include:

```text
pressure
required behavior
forbidden behavior
expected verdict token
validation type
```

Do not claim runtime execution.

- [ ] **Step 3: Record baseline/RED observations**

Inspect current Stage A contracts before Stage B guidance exists. For each scenario record either:

```text
RED — required Stage B contract absent/incomplete
```

or:

```text
BASELINE_COMPLIANT — Stage A already satisfies this invariant
```

Never manufacture a RED when current contracts already satisfy it.

- [ ] **Step 4: Run static baseline checks**

Use focused `grep`, `rg`, and file inspections. Record exact commands/results in `tests/projection-regeneration-foundation-validation.md`.

- [ ] **Step 5: Commit**

```bash
git add tests/pressure-validation-matrix.md tests/projection-regeneration-foundation-validation.md
git commit -m "test: add Stage B projection pressure contracts"
```

---

## Task 2: Introduce projection identity and lifecycle authority

**Files:**
- Create: `references/projection-lifecycle.md`
- Modify: `SKILL.md`
- Modify: `references/shared-assurance-principles.md`
- Modify: `references/revalidation-and-freshness.md`
- Test: Stage B pressure scenarios for projection identity/lifecycle/manual drift

**Interfaces:**
- Consumes: Stage A semantic/projection separation.
- Produces: `PRJ-*`, projection revision, ACTIVE/RETIRED, CURRENT/STALE/BLOCKED, required-action, fingerprint and fully-generated projection contracts.

- [ ] **Step 1: Strengthen the failing pressure cases for lifecycle semantics if needed**

Verify the tests explicitly reject:

```text
projection == authority
path == projection identity
Git commit == projection revision
manual edit == semantic input
REGENERATED == CURRENT
```

- [ ] **Step 2: Write `references/projection-lifecycle.md`**

It must normatively define:

```text
PRJ-* stable logical identity
PRJ-*@revN verified content revision
ACTIVE / RETIRED identity lifecycle
CURRENT / STALE / BLOCKED freshness
NONE / REGENERATE / PROJECTION_REPAIR / SEMANTIC_REVALIDATION / CONTRACT_ADJUDICATION required action
projection contract revision
verified fingerprint
NO_CHANGE
PROJECTION_CONTENT_DIVERGED
PROJECTION_FILE_MISSING
```

Include the invariant:

```text
Anything that must survive regeneration lives in semantic authority.
```

Also explicitly preserve Stage A `PROJECTION_REPAIR` semantics for presentation-only correction with unchanged semantic meaning.

- [ ] **Step 3: Protect non-projection authorities**

In the lifecycle contract explicitly exclude:

```text
working/INDEX.md
STM semantic artifacts
Architecture findings/semantic ledgers
Test Engineering BC/CC/MAT/TM/GAP authorities
```

from automatic projection classification.

- [ ] **Step 4: Keep `SKILL.md` thin**

Add only high-level Stage B routing/invariants and links to the owning reference. Do not duplicate the lifecycle schema into root Skill.

- [ ] **Step 5: Update shared assurance/freshness wording**

Clarify:

```text
semantic freshness != projection freshness
semantic workflow may finish with stale projections
projection stale != semantic false
```

- [ ] **Step 6: Run focused static GREEN checks**

Check the relevant Stage B pressure scenarios plus Stage A freshness regressions.

- [ ] **Step 7: Commit**

```bash
git add SKILL.md references/projection-lifecycle.md references/shared-assurance-principles.md references/revalidation-and-freshness.md
git commit -m "feat: define projection lifecycle authority"
```

---

## Task 3: Define projection dependency and selector contracts

**Files:**
- Create: `references/projection-dependencies.md`
- Modify: `references/technical-model-dependencies.md`
- Modify: `SKILL.md` only if routing text is missing
- Test: selector and edge-direction pressure scenarios

**Interfaces:**
- Consumes: projection identities from Task 2; existing Stage A dependency ownership.
- Produces: exact/selector/projection dependency semantics and canonical edge direction.

- [ ] **Step 1: Ensure the pressure contract rejects arrow reversal**

The canonical three-node example must mean:

```text
PRJ-C -> PRJ-B -> PRJ-A

C consumes B
B consumes A

prerequisite-first execution:
A, B, C
```

- [ ] **Step 2: Write dependency reference**

Define:

```text
SEMANTIC_EXACT
SEMANTIC_SELECTOR
PROJECTION_EXACT
```

Direct dependency authority rule:

```text
consumer owns outbound dependency metadata
CONSUMER -> PREREQUISITE
```

Reverse dependent traversal remains derived.

- [ ] **Step 3: Define controlled selectors**

Initial selector dimensions may include only structured authoritative properties:

```text
entity_type
accepted status
freshness where formally meaningful
structured properties
formal relations
capability owner
```

Explicitly forbid free-form semantic interpretation, SQL, JMESPath, arbitrary scripts.

- [ ] **Step 4: Define selector snapshots**

Require both:

```text
selector contract
resolved membership at successful generation
```

with separate handling for member add/remove/revision change.

- [ ] **Step 5: Define projection DAG scope**

Only the projection regeneration prerequisite graph must be acyclic. Preserve the possibility of cycles in the broader semantic/artifact graph.

- [ ] **Step 6: Reconcile with Stage A dependency reference**

Do not redefine Stage A dependency authority. Add the Stage B specialization consistently.

- [ ] **Step 7: Run GREEN checks and commit**

```bash
git add references/projection-dependencies.md references/technical-model-dependencies.md SKILL.md
git commit -m "feat: define projection dependency contracts"
```

---

## Task 4: Implement Projection Impact Analysis contract

**Files:**
- Create: `references/projection-impact.md`
- Modify: `references/revalidation-and-freshness.md`
- Modify: `references/session-orchestration.md`
- Test: stale impact, selector impact, upstream propagation, impact-accounted scenarios

**Interfaces:**
- Consumes: Tasks 2–3 lifecycle/dependency semantics; stabilized semantic changes.
- Produces: `PROJECTION_IMPACT_ACCOUNTED`, deterministic stale/BLOCKED marking and direct impact records.

- [ ] **Step 1: Define impact inputs**

Impact consumes stabilized semantic identities/revisions and contract changes, not raw Git paths as semantic proof.

- [ ] **Step 2: Define direct impact algorithm**

Cover:

```text
exact semantic revisions
selector membership/revision changes
projection contract changes
manual drift / missing projection
```

- [ ] **Step 3: Define stale propagation**

With declared edges `CONSUMER -> PREREQUISITE`, propagation to dependents must use the derived reverse graph.

Example:

```text
C -> B -> A
A becomes STALE
reverse traversal marks B, then C, as freshness-uncertain
```

Do not redefine the declared arrow direction for diagrams.

- [ ] **Step 4: Define BLOCKED propagation**

Required downstream consumers become BLOCKED when a required prerequisite is structurally BLOCKED.

- [ ] **Step 5: Define `PROJECTION_IMPACT_ACCOUNTED`**

Meaning:

```text
accepted semantic changes evaluated against projection dependency/selector/contracts
resulting projection freshness persisted
```

Explicitly NOT `all projections current`.

- [ ] **Step 6: Define impact failure semantics**

Semantic authority is not rolled back if impact accounting fails technically. Projection-sensitive gates remain blocked until impact is accounted for.

- [ ] **Step 7: Define idempotent stale reasons**

Repeated impact pass must not duplicate reasons or erase unresolved prior causes.

- [ ] **Step 8: Run GREEN/regression checks and commit**

```bash
git add references/projection-impact.md references/revalidation-and-freshness.md references/session-orchestration.md
git commit -m "feat: define projection impact accounting"
```

---

## Task 5: Define deterministic regeneration planner and execution DAG

**Files:**
- Create: `references/projection-regeneration.md`
- Modify: `references/session-orchestration.md`
- Test: TARGETED, ALL_STALE, DAG ordering, partial failure, frozen scope, input drift

**Interfaces:**
- Consumes: projection freshness/dependencies/impact from Tasks 2–4.
- Produces: `RG-*`, TARGETED/ALL_STALE planning and execution semantics.

- [ ] **Step 1: Define regeneration session identity**

`RG-*` is operational execution/history identity, never projection content identity.

- [ ] **Step 2: Define TARGETED**

```text
requested projection targets
+ required stale projection prerequisites
```

Using `CONSUMER -> PREREQUISITE`, upstream expansion follows outbound dependency edges from target toward prerequisites.

Do not add downstream consumers automatically.

- [ ] **Step 3: Define ALL_STALE**

Take a stale-at-planning snapshot. Do not loop until repository-global freshness.

- [ ] **Step 4: Define frozen plans**

Freeze:

```text
mode
requested targets
expanded prerequisites
skipped current prerequisites
input revisions
execution DAG/order
```

Newly stale projections during execution are recorded/deferred unless already in scope.

- [ ] **Step 5: Define topological order**

For:

```text
C -> B -> A
```

execution is:

```text
A, B, C
```

- [ ] **Step 6: Define execution states**

```text
PENDING
READY
RUNNING
REGENERATED
VERIFIED
FAILED
BLOCKED_UPSTREAM
SKIPPED_CURRENT
RECONCILED_NO_CHANGE
```

Keep execution state orthogonal to persistent freshness.

- [ ] **Step 7: Define failure isolation and session outcomes**

Independent branches continue. Session outcomes:

```text
COMPLETE
PARTIAL
BLOCKED
NO_OP
```

Successful verified independent projections are not rolled back because another subtree failed.

- [ ] **Step 8: Define input drift**

Unexpected semantic/upstream revision change during frozen RG yields `REGENERATION_INPUT_DRIFT`; do not silently mutate plan scope.

- [ ] **Step 9: Run GREEN checks and commit**

```bash
git add references/projection-regeneration.md references/session-orchestration.md
git commit -m "feat: define projection regeneration workflow"
```

---

## Task 6: Define projection verification and revision publication

**Files:**
- Create: `references/projection-verification.md`
- Modify: `references/projection-lifecycle.md`
- Modify: `references/projection-regeneration.md`
- Test: V1–V4, NO_CHANGE, new revision, failed verification, semantic conflict

**Interfaces:**
- Consumes: Tasks 2 and 5 generation lifecycle.
- Produces: authoritative projection verification criteria and revision publication rules.

- [ ] **Step 1: Define V1–V4**

```text
V1 STRUCTURAL
V2 DEPENDENCY / PROVENANCE
V3 CONTRACT COMPLETENESS
V4 AUTHORITY CONSISTENCY
```

- [ ] **Step 2: Bound V4**

Verifier may compare projection content to accepted authority but must never adjudicate semantic authority.

If semantic authority is missing/stale/conflicting:

```text
verification blocked
→ owning semantic gate
```

- [ ] **Step 3: Define revision publication algorithm**

```text
generate candidate
→ V1..V4
→ FAIL: no accepted revision, remain STALE/BLOCKED
→ PASS + same fingerprint: NO_CHANGE, same rev, CURRENT
→ PASS + changed fingerprint: revN+1, CURRENT, then downstream impact
```

- [ ] **Step 4: Define freshness reconciliation**

If a consumer was stale only because a prerequisite was stale and prerequisite returns CURRENT at the exact same consumed revision, allow reconciliation without content regeneration.

- [ ] **Step 5: Keep candidate output non-propagating**

Downstream revision impact occurs only after a verified changed projection revision.

- [ ] **Step 6: Run GREEN checks and commit**

```bash
git add references/projection-verification.md references/projection-lifecycle.md references/projection-regeneration.md
git commit -m "feat: define projection verification gates"
```

---

## Task 7: Define projection packages and gate-scoped freshness

**Files:**
- Create: `references/projection-gates-and-packages.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/session-orchestration.md`
- Modify: capability contracts only where package membership is required
- Test: unrelated stale projection non-blocking; required package projections blocking

**Interfaces:**
- Consumes: Tasks 2–6 projection freshness/verification.
- Produces: named package and freshness policy semantics.

- [ ] **Step 1: Define policies**

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

- [ ] **Step 2: Define package contract**

Package is a named non-authoritative deliverable scope with explicit required/optional/controlled conditional projection membership.

Do not introduce arbitrary selector language for package membership.

- [ ] **Step 3: Define closeout/publication chain**

```text
semantic gates accepted
→ PROJECTION_IMPACT_ACCOUNTED
→ package membership resolved
→ required scoped projections CURRENT
→ closeout/publication permitted
```

- [ ] **Step 4: Define unrelated stale behavior**

Stale projection outside gate scope must be reported/visible but must not block unrelated capability closeout.

- [ ] **Step 5: Run GREEN checks and commit**

```bash
git add references/projection-gates-and-packages.md references/review-modes-and-orchestration.md references/session-orchestration.md capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: add projection freshness gate policies"
```

Only include capability files actually changed.

---

## Task 8: Migrate Architecture Review final-report authority safely

**Files:**
- Modify: `references/report-contract.md`
- Modify: `references/review-method.md` if needed
- Modify: `SKILL.md` only for routing/invariant wording
- Modify/Create: focused Architecture semantic authority guidance only if required by existing patterns
- Test: composite authority migration scenario

**Interfaces:**
- Consumes: Stage A Architecture authority and Stage B fully-generated projection contract.
- Produces: safe mapping where persistent architectural meaning lives upstream before final report becomes fully generated.

- [ ] **Step 1: Inventory current final-report authority**

Identify which parts of the current `01-architecture-review.md` contract are persistent semantic authority versus already-derived projection.

At minimum distinguish:

```text
factual As-Built projection
RF/SER semantics
architectural properties/invariants
Target Architecture semantics
Roadmap semantics
presentation-only prose
```

- [ ] **Step 2: Define upstream ownership for every persistent meaning class**

Do not demote semantics into generated prose.

Required rule:

```text
fully generated final report allowed only when every persistent meaning class has an owning semantic authority
```

- [ ] **Step 3: Add migration blocker**

If any persistent meaning is not yet mapped upstream:

```text
PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY
```

or the exact approved equivalent.

Do not regenerate destructively.

- [ ] **Step 4: Convert final report contract to generated assembly semantics**

Once mapped, define the report as projection assembled from Architecture-owned semantic authorities plus factual projections as appropriate.

- [ ] **Step 5: Preserve findings and Architecture ownership**

Ensure Stage B cannot create/change/delete/reinterpret:

```text
RF-*
SER-*
architecture invariants/properties
Target Architecture semantics
Roadmap semantics
```

- [ ] **Step 6: Run Stage A Architecture regressions plus Stage B composite-authority GREEN check**

- [ ] **Step 7: Commit**

```bash
git add references/report-contract.md references/review-method.md SKILL.md
git commit -m "feat: migrate architecture report to generated projection"
```

Include only actually modified files.

---

## Task 9: Integrate Technical Documentation and Test Engineering projections

**Files:**
- Modify: `references/technical-documentation.md`
- Modify: `capabilities/test-review/SKILL.md`
- Modify: `capabilities/test-review/references/test-engineering-contract.md`
- Modify: `references/projection-gates-and-packages.md`
- Test: Technical Documentation selector completeness; Test Review package freshness

**Interfaces:**
- Consumes: Tasks 3–7 projection lifecycle/dependency/package contracts.
- Produces: explicit capability-owned projection contracts for existing generated outputs without changing capability semantic ownership.

- [ ] **Step 1: Technical Documentation projection contracts**

Define its generated documents as `PRJ-*` projections with exact/selector dependencies where appropriate.

For dynamic completeness such as provided APIs, use controlled selector snapshots rather than frozen exact-only membership.

- [ ] **Step 2: Preserve Technical Documentation non-authority**

No Technical Documentation projection may become STM authority.

- [ ] **Step 3: Test Engineering projection contracts**

Keep:

```text
BC/CC/MAT/TM/GAP = semantic authority
numbered/human-readable Test Review documents = projections where already derived by Stage A contract
working/INDEX.md = coordinator authority, never projection
```

- [ ] **Step 4: Define Test Review package membership**

Respect optional/conditional outputs such as Test Plan, Service Simulator Design, E2E Plan rather than forcing all files required in all sessions.

- [ ] **Step 5: Re-run PS-81..99 compatibility**

Ensure targeted STM acquisition remains mandatory and Stage B does not bypass it.

- [ ] **Step 6: Commit**

```bash
git add references/technical-documentation.md capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md references/projection-gates-and-packages.md
git commit -m "feat: integrate capability projection contracts"
```

---

## Task 10: Protect coordinator workflow authority and define operational projection records

**Files:**
- Modify: `references/session-orchestration.md`
- Modify: `SKILL.md`
- Create/Modify: operational projection record guidance in the focused Stage B references rather than creating a hidden monolithic authority
- Test: working/INDEX protection scenario

**Interfaces:**
- Consumes: approved SBD-003 remediation.
- Produces: explicit boundary between coordinator authority and generated Stage B operational views.

- [ ] **Step 1: Declare `working/INDEX.md` coordinator authority**

Use existing repository vocabulary and make it explicit that it owns resume-critical session/gate/handoff state.

- [ ] **Step 2: Exclude it from all Stage B projection mechanics**

No:

```text
PRJ identity
fingerprint drift detection
regeneration
retirement
projection freshness
RG execution
```

for authoritative `working/INDEX.md`.

- [ ] **Step 3: Define any generated projection registry/impact/session views with non-conflicting names**

Do not use a path/name that can be confused with coordinator `working/INDEX.md`.

Prefer focused generated/operational views such as conceptually:

```text
working/projections/registry.md
working/projections/impact.md
working/projections/sessions/RG-*.md
```

Exact paths may be refined here within approved boundaries, but never create one giant manually maintained projection authority registry.

- [ ] **Step 4: Run protection checks and commit**

```bash
git add SKILL.md references/session-orchestration.md references/projection-*.md
git commit -m "feat: protect coordinator state from projection lifecycle"
```

Use explicit paths rather than shell glob if it would stage unrelated files.

---

## Task 11: Define legacy projection registration and migration

**Files:**
- Modify: `references/projection-lifecycle.md`
- Modify: `references/projection-verification.md`
- Modify: `references/session-orchestration.md`
- Modify: `references/report-contract.md` where legacy Architecture reports are affected
- Test: legacy projection scenario

**Interfaces:**
- Consumes: Tasks 2–10 projection model.
- Produces: conservative registration path for pre-Stage-B generated/human-readable artifacts.

- [ ] **Step 1: Define legacy registration**

Required flow:

```text
legacy artifact
→ identify capability owner
→ assign PRJ identity
→ define contract
→ resolve dependencies
→ verify against accepted authority
→ establish fingerprint/revision
→ CURRENT
```

- [ ] **Step 2: Prevent silent CURRENT**

Existing Markdown file alone never proves CURRENT.

- [ ] **Step 3: Prevent human prose authority promotion**

Historical manual wording must not become semantic authority merely because it appears in a legacy projection.

- [ ] **Step 4: Block on insufficient authority**

If required authority is absent/stale/conflicting, route to owning semantic revalidation/migration rather than weakening verification.

- [ ] **Step 5: Run GREEN checks and commit**

```bash
git add references/projection-lifecycle.md references/projection-verification.md references/session-orchestration.md references/report-contract.md
git commit -m "feat: add legacy projection registration"
```

---

## Task 12: Wire NEW / EXTEND / REVALIDATE / closeout orchestration

**Files:**
- Modify: `SKILL.md`
- Modify: `references/session-orchestration.md`
- Modify: `references/revalidation-and-freshness.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: capability contracts only where explicit closeout/package behavior is required
- Test: orchestration and Stage A regression scenarios

**Interfaces:**
- Consumes: complete Stage B lifecycle from Tasks 2–11.
- Produces: end-to-end orchestration without automatic regeneration.

- [ ] **Step 1: NEW semantics**

Semantic work completes first; Projection Impact Analysis accounts for affected projections; regeneration is separately invoked when output/package freshness is required.

- [ ] **Step 2: EXTEND semantics**

Preserve Stage A minimum semantic dependency slices. Stage B adds projection impact accounting and only targeted regeneration for requested deliverables.

- [ ] **Step 3: REVALIDATE semantics**

Preserve impact-driven semantic revalidation. After semantic state stabilizes, run Projection Impact Analysis once; do not regenerate implicitly.

- [ ] **Step 4: Closeout semantics**

Apply the appropriate gate-scoped freshness policy and package membership. Unrelated stale outputs are visible but non-blocking.

- [ ] **Step 5: PROJECTION_REPAIR semantics**

Ensure presentation-only repair remains bounded and cannot mutate semantic authority or create persistent manual sections.

- [ ] **Step 6: Run Stage A + Stage B orchestration regressions and commit**

```bash
git add SKILL.md references/session-orchestration.md references/revalidation-and-freshness.md references/review-modes-and-orchestration.md capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: integrate Stage B orchestration"
```

Only include capability files if changed.

---

## Task 13: Complete auditable Stage B validation record

**Files:**
- Modify: `tests/projection-regeneration-foundation-validation.md`
- Modify: `tests/pressure-validation-matrix.md`
- Test: all Stage B scenarios plus named Stage A regressions

**Interfaces:**
- Consumes: completed implementation contracts.
- Produces: auditable static/contract evidence for Stage B completion candidate.

- [ ] **Step 1: Record per-scenario evidence**

For every Stage B pressure scenario record:

```text
scenario_id
run_id
candidate_head / semantic_head as appropriate
validation_type: STATIC_CONTRACT
execution_context
authoritative_files_inspected
check/probe
expected_behavior
observed_behavior
violations
verdict
```

Do not label static checks as runtime.

- [ ] **Step 2: Record named regression groups**

At minimum cover the existing accepted ranges relevant to:

```text
context/freshness
Architecture authority/discovery
capability integration
orchestration/projection/language
Test Engineering
Stage A STM foundation
```

Name exact pressure IDs/ranges present in the repository at execution time.

- [ ] **Step 3: Explicitly record runtime limitation**

If no executable coordinator exists:

```text
runtime_validation: UNAVAILABLE
reason: repository is Markdown Skill/reference based with no executable coordinator/runtime
```

- [ ] **Step 4: Run final static integrity checks**

```bash
git diff --check origin/main..HEAD
rg -n "working/INDEX\.md" SKILL.md references capabilities tests
rg -n "PROJECTION_REPAIR" SKILL.md references capabilities tests
rg -n "CONSUMER -> PREREQUISITE|PRJ-C -> PRJ-B -> PRJ-A" references tests
rg -n "projection.*authority|source of truth|authoritative" SKILL.md references capabilities tests
```

Inspect every suspicious hit semantically; string presence alone is not failure.

- [ ] **Step 5: Commit**

```bash
git add tests/projection-regeneration-foundation-validation.md tests/pressure-validation-matrix.md
git commit -m "test: record Stage B projection validation"
```

---

## Task 14: Update roadmap and public Stage B status as implementation candidate

**Files:**
- Modify: `docs/roadmap.md`
- Modify: other public docs only if Stage B implementation materially changes an already-documented contract

**Interfaces:**
- Consumes: implementation candidate and validation record.
- Produces: roadmap state suitable for independent review, not final DONE/promotion.

- [ ] **Step 1: Update Stage B roadmap details**

Record implemented sub-capabilities at high level but do not mark Stage B `DONE` before independent review/promotion.

Use a status such as repository-conventional implementation candidate/review pending wording.

- [ ] **Step 2: Preserve Stage C/D/E sequencing**

Do not start Stage C implementation in this task.

- [ ] **Step 3: Verify docs-only intent and commit**

```bash
git diff --check
git add docs/roadmap.md
git commit -m "docs: record Stage B implementation candidate"
```

---

## Task 15: Independent implementation review and remediation gate

**Files:**
- No implementation changes during the first review pass.
- Review artifacts: follow existing repository review conventions if an artifact is required.

**Interfaces:**
- Consumes: complete feature branch from Tasks 1–14.
- Produces: independent verdict and, if necessary, bounded remediation findings.

- [ ] **Step 1: Run independent full implementation review**

Use a fresh reviewer context. Review the full range from approved design baseline through feature HEAD.

High-risk review areas:

```text
projection vs semantic authority
Architecture composite authority migration
working/INDEX.md protection
PROJECTION_REPAIR compatibility
edge direction / DAG ordering
selector snapshots
impact vs execution closure
candidate vs verified propagation
NO_CHANGE reconciliation
TARGETED / ALL_STALE scope
partial progress
V1..V4 boundary
package-scoped freshness
legacy registration
Stage A compatibility
```

- [ ] **Step 2: Classify findings**

Use repository review severity convention. Critical/Important findings block promotion.

- [ ] **Step 3: If findings exist, remediate in bounded commits**

Do not reopen architecture unless a true spec contradiction is discovered.

- [ ] **Step 4: Run targeted independent re-review**

Close all Critical/Important findings.

- [ ] **Step 5: Stop at implementation candidate**

Do not merge, tag, release, deploy, or mark roadmap `DONE` in this task.

Expected final token before promotion workflow:

```text
STAGE_B_IMPLEMENTATION_CANDIDATE
```

with exact feature HEAD, verification summary, independent review verdict, and remaining documented limitations.

---

## Final Verification Checklist

Before declaring the Stage B implementation candidate ready for promotion-readiness review, verify all of the following:

- [ ] `projection != semantic authority` remains explicit.
- [ ] `working/INDEX.md` is explicitly coordinator authority and excluded from Stage B projection lifecycle.
- [ ] Final Architecture Review fully-generated behavior cannot demote persistent Architecture semantics.
- [ ] Stage A `PROJECTION_REPAIR` examples remain valid for presentation-only repair with unchanged semantics.
- [ ] Dependency edge convention is globally consistent: `CONSUMER -> PREREQUISITE`.
- [ ] Prerequisite-first topological execution is unambiguous.
- [ ] Selector membership add/remove/revision changes cause deterministic stale impact.
- [ ] Semantic changes do not regenerate projections implicitly.
- [ ] `PROJECTION_IMPACT_ACCOUNTED` means impact known, not all projections current.
- [ ] Candidate generation cannot invalidate downstream revisions.
- [ ] Upstream `NO_CHANGE` can reconcile downstream freshness safely when no other stale cause exists.
- [ ] Verified new upstream revision causes downstream stale impact.
- [ ] TARGETED executes requested targets + required stale prerequisites only.
- [ ] ALL_STALE is frozen at planning snapshot.
- [ ] Independent branch failure does not rollback successful verified branches.
- [ ] `REGENERATED != CURRENT`; V1–V4 gates are explicit.
- [ ] Identical inputs/output do not create projection revision churn.
- [ ] Manual edits are disposable drift and do not become authority.
- [ ] Legacy projection files cannot become CURRENT without registration + verification.
- [ ] Unrelated stale projections do not block unrelated capability gates.
- [ ] Stage A STM, Architecture, Test Engineering ownership contracts remain intact.
- [ ] Static/contract evidence is auditable and not mislabeled as runtime.
- [ ] `git diff --check` passes.
- [ ] Working tree is clean.
- [ ] No merge/tag/release/deployment performed.
