# Test Engineering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the existing Test Review capability into the approved Test Engineering capability with Behavior Contracts (`BC-*`), Contract Consistency records (`CC-*`), contract verification across declared/implemented/consumed/tested views, dependency-sliced outputs, simulator/E2E design, and impact-driven revalidation.

**Architecture:** Keep `capabilities/test-review/SKILL.md` as the concise discoverable entrypoint. Put the heavier semantic contract in `capabilities/test-review/references/test-engineering-contract.md`. Preserve the umbrella orchestrator as owner of shared session, freshness, artifact, and completion rules. Implement with fail-first pressure scenarios: record RED behavior before guidance changes, then make the smallest guidance changes required to turn the same scenarios GREEN.

**Tech Stack:** Markdown Skill contracts, repository-owned pressure scenarios, Git, existing architecture-code-review orchestration/reference system.

**Spec:** `docs/superpowers/specs/2026-09-03-test-engineering-capability-design.md`

## Global Constraints

- Preserve existing Test Assurance behavior and compatibility outputs `00-test-assurance-summary.md`, `01-test-assurance-map.md`, and optional `02-test-plan.md`.
- `BC-*` is a reusable behavior entity, not `MAT-*`, `RF-*`, `GAP-*`, or executable evidence.
- One `BC-*` expresses one independently verifiable material behavior.
- Test evidence belongs to `TM-*`; do not put executable-evidence verdicts inside `BC-*`.
- Contract views are `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED`.
- Contract Verification records mismatch in `CC-*` and does not automatically choose Swagger/OpenAPI, code, consumer, or tests as truth.
- `CC-*` and `GAP-*` are independent axes.
- Behavior Model is the only writer of accepted `BC-*`; Contract Verification is the owner/writer of `CC-*`.
- Keep lifecycle, freshness, and authority as separate axes.
- Contract Verification runs automatically when a materially relevant declared external contract exists; Contract Consistency Report remains optional.
- Capabilities form a dependency DAG; execute only the minimum required dependency slice.
- `REVALIDATE` is impact-driven. Test-only changes do not automatically invalidate `BC-*`; consumer-only changes may invalidate consumer-facing simulator/E2E projections without a service-repository change.
- Before extended TE semantics, require the minimum targeted STM slice to be accepted, sufficiently covered, fresh enough, and sufficiently resolved; TE must not privately reconstruct technical truth.
- `TASK-*` is a Test Engineering-owned actionable work item derived from accepted TE semantic state; it is not a finding, contract, assurance target, evidence record, or generic project-management task.
- Every generated TE output uses the shared Stage B `PRJ-*` lifecycle, dependency snapshot, V1–V4 verification, fingerprint/revision publication, and persisted freshness state.
- Accepted semantic changes go through `PROJECTION_IMPACT_ACCOUNTED`; regeneration is a separate explicit `RG-*` workflow under the shared package policy.
- `RESUME` restores coordinator state from `working/INDEX.md` and owning records, not narrative prose or chat memory.
- Service Simulator has separate consumer and test-control planes.
- E2E Design does not require Service Simulator Design when the selected topology does not need a simulator.
- No project production code is written during review; simulator implementation remains separately authorized.
- Follow RED-GREEN-REFACTOR for Skill changes.
- Apply `evidence first → automation second → framework last`; use `DO_NOT_BUILD_HARNESS` unless later concrete uncertainty proves a reusable harness is cheaper and more reliable.

---

## File Structure

**Create:**

- `capabilities/test-review/references/test-engineering-contract.md` — detailed Test Engineering semantic contract.
- `tests/pressure-scenario-81-behavior-contract-boundary.md`
- `tests/pressure-scenario-82-contract-verification-authority.md`
- `tests/pressure-scenario-83-contract-drift-vs-test-gap.md`
- `tests/pressure-scenario-84-test-engineering-dependency-slice.md`
- `tests/pressure-scenario-85-test-engineering-revalidation.md`
- `tests/pressure-scenario-86-service-simulator-e2e-boundaries.md`
- `tests/test-engineering-capability-validation.md`

**Modify:**

- `capabilities/test-review/SKILL.md`
- `SKILL.md`
- `references/session-orchestration.md`
- `references/review-modes-and-orchestration.md`
- `references/revalidation-and-freshness.md`
- `references/report-contract.md`
- `README.md`

---

### Task 1: Establish fail-first Test Engineering pressure scenarios

**Files:** create PS-81 through PS-86 listed above.

**Interfaces:**
- Consumes: current `capabilities/test-review/SKILL.md`, current umbrella orchestration, approved design spec.
- Produces: six observed RED baselines and stable GREEN verdict tokens.

Validation for these scenarios is a targeted manual or small deterministic
contract check. Do not create a reusable agent E2E harness, Skill Lab, or test
infrastructure whose primary subject is the validation infrastructure itself.

- [ ] **Step 1: Write and run PS-81 against the unchanged capability**

Scenario pressure: reuse `MAT-*` as the behavior ID or store `existing_test_evidence` inside a broad behavior record.

Required GREEN contract:

```text
BC-* = independently verifiable material behavior
MAT-* = bounded assurance target
TM-* = executable evidence mapping
RF-* = finding/root cause
GAP-* = assurance gap
TASK-* = remediation work

BC != MAT
BC != RF
BC != GAP
BC does not own test-evidence verdicts
```

Verdicts:

```text
PS81_RED_BEHAVIOR_IDENTITY_COLLAPSED
PS81_RED_EVIDENCE_EMBEDDED_IN_BC
PS81_GREEN_BEHAVIOR_BOUNDARY
PS81_INCONCLUSIVE
```

- [ ] **Step 2: Write and run PS-82 against the unchanged capability**

Fixture behavior:

```text
OpenAPI: POST /orders -> 201, 400
Implementation: POST /orders -> 201, 400, 409 DuplicateOrder
Consumer: handles 409 DuplicateOrder
Tests: cover 201 and 400 only
```

Pressure the reviewer to "trust Swagger" or "trust production code". GREEN must preserve `DECLARED`, `IMPLEMENTED`, `CONSUMED`, `TESTED`, create `CC-*`, and keep authority unresolved until adjudicated.

Verdicts:

```text
PS82_RED_AUTOMATIC_CONTRACT_WINNER
PS82_RED_DRIFT_NORMALIZED_AWAY
PS82_GREEN_CONTRACT_AUTHORITY_PRESERVED
PS82_INCONCLUSIVE
```

- [ ] **Step 3: Write and run PS-83 against the unchanged capability**

Case A: Swagger omits `409`, but implementation/consumer behavior is fully tested. Expected: `CC-*`, no automatic `GAP-*`.

Case B: same drift plus missing executable evidence. Expected: `CC-*` plus a separate `GAP-*` through `BC -> MAT -> TM/GAP`.

Verdicts:

```text
PS83_RED_DRIFT_FORCED_TO_GAP
PS83_RED_GAP_HIDES_DRIFT
PS83_GREEN_ORTHOGONAL_DRIFT_AND_GAP
PS83_INCONCLUSIVE
```

- [ ] **Step 4: Write and run PS-84 against the unchanged capability**

Case A: user selects only `E2E Test Plan`. Required dependency slice: Test Assurance + Behavior Model + Contract Verification when applicable + E2E Design. Service Simulator Design is added only when topology requires it.

Case B: `EXTEND` accepted Test Review -> Service Simulator Design. Reuse accepted upstream work; do not restart the full review.

Verdicts:

```text
PS84_RED_LINEAR_PIPELINE_EXPANSION
PS84_RED_FULL_REVIEW_RESTART
PS84_GREEN_MINIMUM_DEPENDENCY_SLICE
PS84_INCONCLUSIVE
```

- [ ] **Step 5: Write and run PS-85 against the unchanged capability**

Change sets:

```text
A: tests only changed
B: service implementation/OpenAPI changed
C: consumer repository changed while service repository stayed unchanged
```

Required GREEN routing:

```text
A -> TM/MAT/GAP impact; BC not automatically invalidated
B -> affected IMPLEMENTED/DECLARED views -> CC/BC impact analysis
C -> affected CONSUMED view -> consumer-facing simulator/E2E impact
```

Verdicts:

```text
PS85_RED_GLOBAL_REVALIDATION
PS85_RED_SERVICE_ONLY_FRESHNESS_MODEL
PS85_GREEN_IMPACT_DRIVEN_REVALIDATION
PS85_INCONCLUSIVE
```

- [ ] **Step 6: Write and run PS-86 against the unchanged capability**

Require explicit distinction:

```text
A) substitutes for dependencies OF the reviewed service
B) Service Simulator OF the reviewed service for its consumers
```

GREEN requires a real consumer-protocol plane where relevant, a separate test-control plane, smaller-boundary preference, and E2E without mandatory simulator use.

Verdicts:

```text
PS86_RED_SIMULATOR_BOUNDARIES_COLLAPSED
PS86_RED_CONTROL_PLANE_LEAKED
PS86_RED_E2E_ALWAYS_REQUIRES_SIMULATOR
PS86_GREEN_SIMULATOR_E2E_BOUNDARIES
PS86_INCONCLUSIVE
```

- [ ] **Step 7: Commit RED pressure contracts before capability edits**

```bash
git add tests/pressure-scenario-81-behavior-contract-boundary.md \
        tests/pressure-scenario-82-contract-verification-authority.md \
        tests/pressure-scenario-83-contract-drift-vs-test-gap.md \
        tests/pressure-scenario-84-test-engineering-dependency-slice.md \
        tests/pressure-scenario-85-test-engineering-revalidation.md \
        tests/pressure-scenario-86-service-simulator-e2e-boundaries.md
git commit -m "test: add fail-first test engineering scenarios"
```

Expected: scenario files contain actual observed RED evidence; no capability guidance changed yet.

---

### Task 2: Add the authoritative Test Engineering semantic contract

**Files:**
- Create: `capabilities/test-review/references/test-engineering-contract.md`
- Modify: `capabilities/test-review/SKILL.md`

**Interfaces:**
- Consumes: PS-81..86 RED failures and approved spec.
- Produces: detailed semantic contract plus concise capability entrypoint.

- [ ] **Step 0: Establish the factual STM precondition**

Before constructing or materially revising any BC, CC, MAT, TM, GAP, TASK,
environment, simulator, or E2E semantic artifact, calculate the minimum STM
slice required by the selected scope. Reuse an accepted/fresh `FULL` model when
its exact binding satisfies the request; otherwise acquire targeted facts from
Shared Evidence through the Technical Model Gate. Require:

```text
present + ACCEPTED + sufficiently covered for scope
+ fresh enough for operation + sufficiently resolved
+ independent targeted STM coverage acceptance
```

If facts are missing, stale, disputed, or insufficiently covered, emit the
existing STM request and block only the dependent TE slice. Do not inspect
repository material and persist a competing private factual model. Record the
accepted STM revisions and coverage decision as dependencies of downstream TE
authority/projections.

- [ ] **Step 1: Create the detailed reference**

Required sections:

```text
Behavior Contract Model
Contract Verification
Contract Consistency Record
Identifier Relationships
Lifecycle / Freshness / Authority
Ownership
Test Environment Design
Service Simulator Design
E2E Design
Capability Dependency DAG
Output Package
Reuse / Extend / Revalidate
```

Required BC axes:

```text
status: CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED
freshness: VALID | REVALIDATION_REQUIRED | UNKNOWN
authority: RESOLVED | UNRESOLVED
```

Required CC axes:

```text
status: OPEN | CLASSIFIED | RESOLVED | WONT_RESOLVE | SUPERSEDED
freshness: VALID | REVALIDATION_REQUIRED | UNKNOWN
```

Required contract views:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

Required classifications:

```text
AUTHORITY_UNRESOLVED
DECLARATION_STALE
IMPLEMENTATION_DEFECT
CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR
TEST_ENCODES_STALE_CONTRACT
INTENTIONAL_COMPATIBILITY_BEHAVIOR
CONTRACT_UNRESOLVED
```

Required invariants:

```text
Resolution of CC-* does not silently rewrite BC-*.
Contract drift and assurance gaps are independent axes.
```

- [ ] **Step 2: Route the capability entrypoint to the new reference**

Add to `capabilities/test-review/SKILL.md`:

```markdown
For Test Engineering outputs beyond the existing Test Assurance core, read
`capabilities/test-review/references/test-engineering-contract.md` before
constructing Behavior Contracts, Contract Verification records, environment
strategy, simulator design, or E2E design.
```

Expose these selectable outputs:

```text
Test Assurance [required]
Test Plan [optional]
Contract Consistency Report [optional projection]
Test Environment Design [optional]
Service Simulator Design [optional]
Service Simulator Implementation Plan [optional; requires accepted simulator spec]
E2E Test Plan [optional]
```

Do not expose Behavior Model as a checkbox. Contract Verification is automatic when materially applicable.

- [ ] **Step 3: Re-run PS-81, PS-82, and PS-83**

Expected:

```text
PS81_GREEN_BEHAVIOR_BOUNDARY
PS82_GREEN_CONTRACT_AUTHORITY_PRESERVED
PS83_GREEN_ORTHOGONAL_DRIFT_AND_GAP
```

- [ ] **Step 4: Commit semantic contract**

```bash
git add capabilities/test-review/SKILL.md \
        capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: define test engineering semantic contract"
```

---

### Task 3: Integrate output selection, dependency slicing, and artifact ownership

**Files:**
- Modify: `SKILL.md`
- Modify: `references/session-orchestration.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/report-contract.md`

**Interfaces:**
- Consumes: selectable outputs and dependency DAG from Task 2.
- Produces: startup selection, persisted capability state, artifact ownership, and `EXTEND` behavior.

- [ ] **Step 0: Register the shared Stage B projection contract**

For each generated `00`–`08` output, bind the stable `PRJ-*` identity to the
Test Review capability and projection-contract revision. Persist exact semantic
dependencies, applicable `SEMANTIC_SELECTOR` contract/resolution snapshots,
applicable STM/coverage dependencies, and direct `PROJECTION_EXACT` upstream
dependencies. Route candidate output through shared `V1`–`V4`, compute the
canonical fingerprint, publish only verified `PRJ-*@revN`, and persist
`CURRENT | STALE | BLOCKED`. Do not assign `PRJ-*` to BC/CC/MAT/TM/GAP/TASK
semantic authority or build a TE-specific projection engine.

- [ ] **Step 1: Persist explicit selected outputs**

Canonical stored shape:

```text
outputs:
  test_assurance: true
  test_plan: false
  contract_consistency_report: false
  test_environment_design: false
  service_simulator_design: false
  service_simulator_implementation_plan: false
  e2e_test_plan: true
```

Never encode a compound mode such as `REVIEW_PLUS_SIMULATOR_PLUS_E2E`.

- [ ] **Step 2: Encode minimum dependency slices**

```text
E2E Test Plan
  -> Test Assurance
  -> Behavior Model
  -> Contract Verification if applicable
  -> E2E Design
  -> Service Simulator Design only when the chosen topology requires it

Service Simulator Implementation Plan
  -> accepted + fresh Service Simulator Spec
```

`EXTEND` reuses the minimum accepted fresh upstream slice and does not restart unrelated gates.

Persist projection dependencies in the canonical direction
`CONSUMER -> PREREQUISITE`; execute prerequisites first. Keep semantic
dependencies separate from projection dependencies. Initial generation follows
the same shared lifecycle and is not silently treated as regeneration.

Resolve and persist the finite Test Review package membership before closeout.
Apply the selected `PERMISSIVE`, `REQUIRED_SCOPE_CURRENT`, or
`ALL_SCOPED_CURRENT` policy; do not impose global projection freshness and do
not use package membership as a second semantic authority.

- [ ] **Step 3: Encode persisted output ownership**

```text
00-test-assurance-summary.md
01-test-assurance-map.md
02-test-plan.md                              # optional, compatibility
03-behavior-contract-model.md                # when extended model is required
04-contract-consistency-report.md            # optional projection
05-test-environment-design.md                # optional
06-service-simulator-spec.md                 # optional
07-service-simulator-implementation-plan.md  # optional
08-e2e-test-plan.md                          # optional
```

Authoritative `BC-*` and `CC-*` ledgers live under capability `working/`; numbered files are human-facing projections.

- [ ] **Step 3a: Persist resume-critical coordinator state**

Reconcile `working/INDEX.md` with the owning Test Engineering records after
each material transition. Persist only coordinator state needed to resume:
selected scope and outputs, current TE phase, STM prerequisite and coverage
gate, BC/CC/MAT/TM/GAP/TASK registry references, blockers, environment strategy
references, required verification state, and projection impact/package/
freshness state. Keep semantic meaning in the owning ledgers; `INDEX.md` is
workflow authority only and is never a `PRJ-*` projection.

Distinguish:

```text
NOT_APPLICABLE
NOT_VERIFIED
VERIFIED_NO_MATERIAL_DRIFT
```

- [ ] **Step 4: Re-run PS-84**

Expected: `PS84_GREEN_MINIMUM_DEPENDENCY_SLICE`.

- [ ] **Step 5: Commit orchestration integration**

```bash
git add SKILL.md references/session-orchestration.md \
        references/review-modes-and-orchestration.md \
        references/report-contract.md
git commit -m "feat: orchestrate test engineering outputs"
```

---

### Task 4: Add impact-driven Test Engineering revalidation

**Files:**
- Modify: `references/revalidation-and-freshness.md`
- Modify: `capabilities/test-review/references/test-engineering-contract.md`

**Interfaces:**
- Consumes: BC/CC source bindings and umbrella freshness model.
- Produces: service/test/consumer-specific impact routing.

- [ ] **Step 1: Define revision-bound source bindings**

Canonical field names:

```text
BC-042
source_bindings:
  architecture_revision: RF-012@rev4
  declared_revision: openapi.yaml@service_baseline_sha
  implementation_revision: src/orders/handler.py@service_baseline_sha
  consumer_revision: checkout-ui@consumer_baseline_sha

CC-017
compared_views:
  declared_revision: openapi.yaml@service_baseline_sha
  implementation_revision: src/orders/handler.py@service_baseline_sha
  consumer_revision: checkout-ui@consumer_baseline_sha
  tested_revision: tests/orders/test_orders.py@service_baseline_sha
```

`service_baseline_sha` and `consumer_baseline_sha` are canonical persisted field names populated with concrete revision values at runtime; they are not literal placeholder values.

- [ ] **Step 2: Encode impact routing**

```text
tests-only change
  -> revalidate affected TM/MAT/GAP
  -> BC remains valid unless independent semantic evidence says otherwise

implementation or declared-contract change
  -> revalidate affected IMPLEMENTED/DECLARED views
  -> run CC/BC impact analysis

consumer-only change
  -> revalidate affected CONSUMED views
  -> revalidate consumer-facing simulator/E2E projections as needed
```

A changed bound file triggers impact analysis, not automatic semantic invalidation of every related BC.

- [ ] **Step 2a: Persist the post-semantic projection handoff**

After the affected semantic slice is accepted, run shared Projection Impact
Analysis once and persist `PROJECTION_IMPACT_ACCOUNTED`, including direct and
propagated `CURRENT | STALE | BLOCKED` results, selector membership/revision
changes, projection-contract changes, missing/diverged files, and upstream
freshness. Do not regenerate content here. A requested fresh output starts a
separate explicit `RG-*` workflow using the frozen prerequisite-first DAG.

- [ ] **Step 3: Re-run PS-85**

Expected: `PS85_GREEN_IMPACT_DRIVEN_REVALIDATION`.

- [ ] **Step 4: Commit freshness integration**

```bash
git add references/revalidation-and-freshness.md \
        capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: add test engineering revalidation rules"
```

---

### Task 5: Harden Test Environment, Service Simulator, and E2E boundaries

**Files:**
- Modify: `capabilities/test-review/references/test-engineering-contract.md`
- Modify: `capabilities/test-review/SKILL.md`

**Interfaces:**
- Consumes: accepted BCs and selected outputs.
- Produces: dependency strategy, simulator boundaries, and E2E selection rules.

Environment strategy is Test Engineering execution configuration and assurance
strategy. It is not an STM fact, Architecture authority, or Stage B projection
authority. Persist the decision with the smallest relevant TE artifact and its
accepted BC/STM dependencies.

- [ ] **Step 1: Encode dependency strategy vocabulary**

```text
REAL_DISPOSABLE
SERVICE_EMULATOR
CONTROLLABLE_MOCK
IN_PROCESS_DOUBLE
TEMP_RESOURCE
NOT_REQUIRED
```

Require a reason per material dependency and preserve:

```text
Mock external uncertainty, not the behavior under test.
```

- [ ] **Step 2: Encode the two simulation classes**

```text
Dependency substitutes
  -> environment around the reviewed service

Service Simulator
  -> simulation of the reviewed service for its consumers
```

The simulator exposes relevant real consumer protocols and a separate test-only control plane. Illustrative controls:

```text
/__test/health
/__test/reset
/__test/scenario
/__test/state
/__test/seed
```

Simulator scenarios carry `BC-*` provenance and relevant contract-view/authority classification. Do not generate them blindly from Swagger alone.

- [ ] **Step 3: Encode E2E selection contract**

Each E2E design states source `BC-*`, participating real components, allowed simulators/fakes, initial state, stimulus, material assertions, failure observability, cleanup/reset, CI suitability, and execution cost where useful.

Prefer a smaller test boundary when it proves the same material behavior more reliably and cheaply.

- [ ] **Step 4: Re-run PS-86**

Expected: `PS86_GREEN_SIMULATOR_E2E_BOUNDARIES`.

- [ ] **Step 5: Commit simulator/E2E contract**

```bash
git add capabilities/test-review/SKILL.md \
        capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: define simulator and e2e boundaries"
```

---

### Task 6: Add consolidated validation and compatibility checks

**Files:**
- Create: `tests/test-engineering-capability-validation.md`

**Interfaces:**
- Consumes: PS-81..86 and existing PS-79 Test Assurance Summary behavior.
- Produces: acceptance matrix for the complete capability.

The validation task is intentionally proportional: evidence first, automation
second, framework last. It must contain the guard:

```text
DO_NOT_BUILD_HARNESS
```

Use targeted deterministic checks, focused contract checks, and manual real-agent
acceptance where agent behavior is the subject. A reusable harness requires a
later concrete implementation uncertainty, measured reuse, stable behavior,
and a demonstrated cost/reliability advantage; it is not pre-authorized here.

- [ ] **Step 1: Create the validation matrix**

Require:

```text
PS-79 remains GREEN
PS-81 GREEN behavior identity boundary
PS-82 GREEN contract authority preservation
PS-83 GREEN drift/gap orthogonality
PS-84 GREEN minimum dependency slice
PS-85 GREEN impact-driven revalidation
PS-86 GREEN simulator/E2E boundaries
```

Static invariants:

```text
00/01/02 compatibility preserved
Behavior Model is not a user checkbox
Contract Verification automatic when applicable
Contract Consistency Report optional
accepted BC writer = Behavior Model
CC writer = Contract Verification
CC resolution cannot silently rewrite BC
USE_EXISTING requires accepted/fresh dependency slice
PROJECTION_REPAIR cannot alter BC/CC/MAT/TM/GAP semantics
accepted/fresh targeted STM gate precedes extended TE semantics
TE cannot privately reconstruct STM facts
every generated TE output has PRJ identity, dependency snapshot, V1–V4, fingerprint/revision, and freshness
semantic change -> PROJECTION_IMPACT_ACCOUNTED; regeneration remains explicit RG-*
RESUME restores workflow state from INDEX/owning records
TASK-* is TE work-item authority only
```

- [ ] **Step 2: Run all pressure scenarios in fresh contexts**

Record actual verdicts and any new rationalizations. Do not substitute static reading for behavioral validation.

- [ ] **Step 3: Run a Test Review-only compatibility canary**

Request only Test Assurance. Expected:

```text
00 + 01 are produced/targeted
02 only when Test Plan is selected
03-08 are not forced
Contract Consistency Report is not forced
no substantial optional capability is silently enabled
```

- [ ] **Step 4: Commit validation evidence**

```bash
git add tests/test-engineering-capability-validation.md \
        tests/pressure-scenario-81-behavior-contract-boundary.md \
        tests/pressure-scenario-82-contract-verification-authority.md \
        tests/pressure-scenario-83-contract-drift-vs-test-gap.md \
        tests/pressure-scenario-84-test-engineering-dependency-slice.md \
        tests/pressure-scenario-85-test-engineering-revalidation.md \
        tests/pressure-scenario-86-service-simulator-e2e-boundaries.md
git commit -m "test: validate test engineering capability"
```

---

### Task 7: Update user-facing documentation after behavioral acceptance

**Files:**
- Modify: `README.md`
- Modify only for non-semantic entrypoint cleanup if required: `capabilities/test-review/SKILL.md`

**Interfaces:**
- Consumes: accepted GREEN capability contract.
- Produces: user-facing documentation that describes, but does not redefine, capability behavior.

- [ ] **Step 1: Document selectable outputs**

```text
Test Assurance
Test Plan
Contract Consistency Report
Test Environment Design
Service Simulator Design
Service Simulator Implementation Plan
E2E Test Plan
```

Explain that Behavior Model and materially applicable Contract Verification are internal gates, not user checkboxes.

- [ ] **Step 2: Document output package `00` through `08`**

Mark optional artifacts and state that authoritative working ledgers remain under `working/` while numbered documents are projections.

- [ ] **Step 3: Document Swagger/OpenAPI comparison correctly**

Use this semantic rule:

```text
When an external declared contract exists, Test Engineering compares it with
observed implementation, consumer dependencies, and executable tests. A
mismatch is recorded and adjudicated; no source wins merely because it is
newer, executable, or machine-readable.
```

- [ ] **Step 4: Re-run PS-79 and PS-81..86**

Expected: all accepted GREEN verdicts remain GREEN.

- [ ] **Step 5: Commit documentation**

```bash
git add README.md capabilities/test-review/SKILL.md
git commit -m "docs: document test engineering capability"
```

---

## Final Verification Gate

Before declaring implementation complete:

- [ ] `git status --short` contains only the known preserved `task-5-report.md` after the final commit.
- [ ] Implementation matches `docs/superpowers/specs/2026-09-03-test-engineering-capability-design.md`.
- [ ] RED evidence exists for PS-81..86 from before behavior-changing Skill edits.
- [ ] GREEN evidence exists for PS-81..86 after changes.
- [ ] Existing PS-79 remains GREEN.
- [ ] `capabilities/test-review/SKILL.md` remains concise; heavy semantics live in `capabilities/test-review/references/test-engineering-contract.md`.
- [ ] Swagger/OpenAPI remains `DECLARED`, not automatic truth.
- [ ] `BC-*` does not own executable-test evidence verdicts.
- [ ] `CC-*` and `GAP-*` remain independent.
- [ ] `EXTEND` and `REVALIDATE` use the minimum affected dependency slice.
- [ ] Consumer-repository freshness works independently of service-repository freshness.
- [ ] Dependency substitutes and Service Simulator remain distinct.
- [ ] Simulator consumer plane and test-control plane remain separate.
- [ ] E2E can exist without Service Simulator when topology does not require it.
- [ ] `00/01/02` compatibility remains intact.
- [ ] README is only a projection of accepted capability semantics.
- [ ] Accepted/fresh targeted STM and independent coverage acceptance precede extended TE semantics.
- [ ] TE does not privately reconstruct STM facts.
- [ ] `TASK-*` ownership and non-authority are explicit.
- [ ] Every generated TE projection has Stage B identity, dependency snapshot, V1–V4, fingerprint/revision, and freshness.
- [ ] `PROJECTION_IMPACT_ACCOUNTED` precedes package-sensitive closeout and regeneration is explicit `RG-*`.
- [ ] `RESUME` uses `working/INDEX.md` and owning records rather than prose.
- [ ] `DO_NOT_BUILD_HARNESS` remains in force absent new evidence.

Expected final verdict:

```text
TEST_ENGINEERING_CAPABILITY_IMPLEMENTED
```

If any behavioral scenario remains RED or INCONCLUSIVE, return:

```text
TEST_ENGINEERING_CAPABILITY_NOT_ACCEPTED
```

with the exact blocking scenario IDs. Do not weaken a scenario contract merely to obtain GREEN.
