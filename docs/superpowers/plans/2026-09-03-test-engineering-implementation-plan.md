# Test Engineering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the existing Test Review capability into the approved Test Engineering capability with Behavior Contracts (`BC-*`), Contract Consistency records (`CC-*`), contract verification against declared/implemented/consumed/tested views, dependency-sliced outputs, simulator/E2E design, and impact-driven revalidation.

**Architecture:** Keep `capabilities/test-review/SKILL.md` as the discoverable capability entrypoint and move the heavier Test Engineering semantic contract into a focused capability reference. Preserve the existing umbrella orchestrator as owner of shared session, freshness, artifact, and completion rules. Implement the design through fail-first pressure scenarios: record RED behavior on the current skill before changing capability guidance, then add the minimum rules needed to turn those same scenarios GREEN.

**Tech Stack:** Markdown Skill contracts, repository-owned pressure scenarios, Git, existing architecture-code-review orchestration/reference system.

**Spec:** `docs/superpowers/specs/2026-09-03-test-engineering-capability-design.md`

## Global Constraints

- Preserve existing Test Assurance semantics and compatibility outputs `00-test-assurance-summary.md`, `01-test-assurance-map.md`, and optional `02-test-plan.md`.
- `BC-*` is a reusable behavioral semantic entity; it is not `MAT-*`, `RF-*`, `GAP-*`, or test evidence.
- One `BC-*` expresses one independently verifiable material behavior.
- Test evidence belongs to `TM-*`; do not store executable-evidence verdicts inside `BC-*`.
- Contract views are `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED`.
- Contract Verification records observable mismatch in `CC-*` and does not automatically choose Swagger/OpenAPI, code, consumer, or tests as truth.
- `CC-*` and `GAP-*` are orthogonal; contract drift is not automatically a test gap.
- Behavior Model is the only writer of accepted `BC-*`; Contract Verification is the only writer of accepted/classified `CC-*`.
- Separate semantic lifecycle, freshness, and authority axes.
- Contract Verification runs automatically when a materially relevant declared external contract exists; the human-readable Contract Consistency Report remains optional.
- Capabilities form a dependency DAG; execute only the minimum required dependency slice.
- `REVALIDATE` is impact-driven; test-only change does not automatically invalidate `BC-*`, while consumer changes may invalidate consumer-facing simulator/E2E projections without a service-repository change.
- Service Simulator has separate consumer and test-control planes.
- E2E Design does not require Service Simulator Design when the selected topology does not need a simulator.
- No production/project implementation code is written by the review capability; Service Simulator implementation remains a separately authorized action after an accepted simulator specification and implementation plan.
- Follow RED-GREEN-REFACTOR for Skill changes: every behavior-changing guidance edit requires an observed failing pressure scenario first.

---

## File Structure

**Create:**

- `capabilities/test-review/references/test-engineering-contract.md` — authoritative detailed semantics for `BC-*`, `CC-*`, Contract Verification, output DAG, Test Environment Design, Service Simulator Design, E2E Design, ownership, lifecycle, and revalidation.
- `tests/pressure-scenario-81-behavior-contract-boundary.md` — RED/GREEN contract for keeping `BC-*` distinct from `MAT/RF/GAP/TM` and keeping evidence in `TM-*`.
- `tests/pressure-scenario-82-contract-verification-authority.md` — RED/GREEN contract for Swagger/OpenAPI vs code/consumer/tests without automatic winner selection.
- `tests/pressure-scenario-83-contract-drift-vs-test-gap.md` — RED/GREEN contract proving `CC-*` and `GAP-*` are independent.
- `tests/pressure-scenario-84-test-engineering-dependency-slice.md` — RED/GREEN contract for explicit outputs and minimum dependency DAG.
- `tests/pressure-scenario-85-test-engineering-revalidation.md` — RED/GREEN contract for implementation/test/consumer-specific freshness impact.
- `tests/pressure-scenario-86-service-simulator-e2e-boundaries.md` — RED/GREEN contract for dependency substitutes vs reviewed-service simulator, consumer/control planes, and E2E selection.
- `tests/test-engineering-capability-validation.md` — consolidated static/behavioral validation checklist covering PS-81..86 and existing Test Assurance compatibility.

**Modify:**

- `capabilities/test-review/SKILL.md` — concise discoverable Test Engineering entrypoint, Test Assurance compatibility, required reference loading, user-selectable outputs, and hard gates.
- `SKILL.md` — umbrella integration wording so Test Review/Test Engineering can be selected/extended while umbrella retains shared authority/freshness/artifact ownership.
- `references/session-orchestration.md` — startup/output selection rules for Test Engineering.
- `references/review-modes-and-orchestration.md` — capability state, minimum dependency-slice execution, `EXTEND`, and persisted artifact ownership.
- `references/revalidation-and-freshness.md` — `BC/CC` source bindings and impact-driven invalidation rules including multi-repository consumer freshness.
- `references/report-contract.md` — capability-owned output package and final-package linking rules.
- `README.md` — user-facing capability description and output examples after the behavioral contract is GREEN.

---

### Task 1: Establish fail-first Test Engineering pressure scenarios

**Files:**
- Create: `tests/pressure-scenario-81-behavior-contract-boundary.md`
- Create: `tests/pressure-scenario-82-contract-verification-authority.md`
- Create: `tests/pressure-scenario-83-contract-drift-vs-test-gap.md`
- Create: `tests/pressure-scenario-84-test-engineering-dependency-slice.md`
- Create: `tests/pressure-scenario-85-test-engineering-revalidation.md`
- Create: `tests/pressure-scenario-86-service-simulator-e2e-boundaries.md`

**Interfaces:**
- Consumes: current `capabilities/test-review/SKILL.md`, current umbrella orchestration, approved design spec.
- Produces: six observed RED baselines and stable GREEN verdict tokens used by all later tasks.

- [ ] **Step 1: Write PS-81 and run it against the unchanged capability**

Use a scenario where the agent is asked to extend a Test Review and is tempted to put `existing_test_evidence` inside a broad behavior record or reuse `MAT-*` as the behavior identifier.

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

Record the actual pre-change failure and one of:

```text
PS81_RED_BEHAVIOR_IDENTITY_COLLAPSED
PS81_RED_EVIDENCE_EMBEDDED_IN_BC
PS81_GREEN_BEHAVIOR_BOUNDARY
PS81_INCONCLUSIVE
```

- [ ] **Step 2: Write PS-82 and run it against the unchanged capability**

Scenario: OpenAPI declares `201/400`; code additionally returns `409`; frontend handles `409`; tests cover only `201/400`. Pressure the reviewer to "trust Swagger" or "trust production code".

Required GREEN response must preserve four views:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

and create a `CC-*` record with unresolved authority until evidence adjudicates it. Explicitly prohibit automatic winner selection.

Verdicts:

```text
PS82_RED_AUTOMATIC_CONTRACT_WINNER
PS82_RED_DRIFT_NORMALIZED_AWAY
PS82_GREEN_CONTRACT_AUTHORITY_PRESERVED
PS82_INCONCLUSIVE
```

- [ ] **Step 3: Write PS-83 and run it against the unchanged capability**

Scenario A: Swagger omits `409`, but implementation/consumer behavior is fully tested. Expected: `CC-*` exists, no automatic `GAP-*`.

Scenario B: same drift plus missing executable evidence. Expected: `CC-*` and a separate `GAP-*` through `BC -> MAT -> TM/GAP`.

Verdicts:

```text
PS83_RED_DRIFT_FORCED_TO_GAP
PS83_RED_GAP_HIDES_DRIFT
PS83_GREEN_ORTHOGONAL_DRIFT_AND_GAP
PS83_INCONCLUSIVE
```

- [ ] **Step 4: Write PS-84 and run it against the unchanged capability**

Scenario: user selects only `E2E Test Plan`. Expected implicit dependencies are Test Assurance + Behavior Model + Contract Verification when applicable; Service Simulator Design must not be enabled unless the topology needs it.

Add a second case for `EXTEND accepted Test Review -> Service Simulator Design`, which must reuse the accepted upstream slice rather than restart the whole review.

Verdicts:

```text
PS84_RED_LINEAR_PIPELINE_EXPANSION
PS84_RED_FULL_REVIEW_RESTART
PS84_GREEN_MINIMUM_DEPENDENCY_SLICE
PS84_INCONCLUSIVE
```

- [ ] **Step 5: Write PS-85 and run it against the unchanged capability**

Use three change sets:

```text
A: tests only changed
B: service implementation/OpenAPI changed
C: consumer repository changed while service repository stayed unchanged
```

Expected:

```text
A -> TM/MAT/GAP impact; BC not automatically invalidated
B -> affected IMPLEMENTED/DECLARED views -> CC/BC impact analysis
C -> CONSUMED view and consumer-facing simulator/E2E freshness impact
```

Verdicts:

```text
PS85_RED_GLOBAL_REVALIDATION
PS85_RED_SERVICE_ONLY_FRESHNESS_MODEL
PS85_GREEN_IMPACT_DRIVEN_REVALIDATION
PS85_INCONCLUSIVE
```

- [ ] **Step 6: Write PS-86 and run it against the unchanged capability**

Scenario must distinguish:

```text
A) substitutes for dependencies OF the reviewed service
B) Service Simulator OF the reviewed service for its consumers
```

Require consumer plane to match relevant real protocols and require a separate test-control plane. E2E must prefer a smaller boundary when equivalent assurance exists and must be selectable without a simulator when topology does not need one.

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

Expected: commit contains scenario definitions plus observed RED evidence; no capability guidance changed yet.

---

### Task 2: Add the authoritative Test Engineering semantic contract

**Files:**
- Create: `capabilities/test-review/references/test-engineering-contract.md`
- Modify: `capabilities/test-review/SKILL.md`

**Interfaces:**
- Consumes: PS-81..86 failure modes and approved design spec.
- Produces: one focused semantic reference loaded by Test Review/Test Engineering and a concise discoverable entrypoint.

- [ ] **Step 1: Add the minimal reference contract required to address PS-81..86**

The new reference must define these exact sections:

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

Required `BC-*` axes:

```text
status: CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED
freshness: VALID | REVALIDATION_REQUIRED | UNKNOWN
authority: RESOLVED | UNRESOLVED
```

Required `CC-*` axes:

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

Required unresolved/drift classifications include at least:

```text
AUTHORITY_UNRESOLVED
DECLARATION_STALE
IMPLEMENTATION_DEFECT
CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR
TEST_ENCODES_STALE_CONTRACT
INTENTIONAL_COMPATIBILITY_BEHAVIOR
CONTRACT_UNRESOLVED
```

State explicitly:

```text
Resolution of CC-* does not silently rewrite BC-*.
Contract drift and assurance gaps are independent axes.
```

- [ ] **Step 2: Keep `capabilities/test-review/SKILL.md` concise and route heavy detail to the reference**

Add a required-reference instruction similar to:

```markdown
For Test Engineering outputs beyond the existing Test Assurance core, read
`capabilities/test-review/references/test-engineering-contract.md` before
constructing Behavior Contracts, Contract Verification records, environment
strategy, simulator design, or E2E design.
```

Add the explicit user-selectable outputs:

```text
Test Assurance [required]
Test Plan [optional]
Contract Consistency Report [optional projection]
Test Environment Design [optional]
Service Simulator Design [optional]
Service Simulator Implementation Plan [optional; requires accepted simulator spec]
E2E Test Plan [optional]
```

Do not expose Behavior Model as a user checkbox; it is an internal dependency when extended outputs require it. Contract Verification is automatic when a materially relevant declared external contract exists.

- [ ] **Step 3: Re-run PS-81, PS-82, and PS-83**

Expected:

```text
PS81_GREEN_BEHAVIOR_BOUNDARY
PS82_GREEN_CONTRACT_AUTHORITY_PRESERVED
PS83_GREEN_ORTHOGONAL_DRIFT_AND_GAP
```

If a scenario finds a new rationalization, update only the smallest relevant wording and re-run the same scenario.

- [ ] **Step 4: Commit semantic contract**

```bash
git add capabilities/test-review/SKILL.md \
        capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: define test engineering semantic contract"
```

---

### Task 3: Integrate Test Engineering into umbrella orchestration and output ownership

**Files:**
- Modify: `SKILL.md`
- Modify: `references/session-orchestration.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/report-contract.md`

**Interfaces:**
- Consumes: user-selectable output list and dependency DAG from Task 2.
- Produces: startup selection, persisted capability state, artifact ownership, and minimum dependency-slice orchestration.

- [ ] **Step 1: Add startup/output-selection contract**

Persist explicit selected outputs; never encode them as a compound mode such as `REVIEW_PLUS_SIMULATOR_PLUS_E2E`.

Use this conceptual stored set:

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

The orchestrator may recommend outputs but must not silently enable substantial optional work.

- [ ] **Step 2: Define dependency-slice rules**

Required examples:

```text
E2E Test Plan
  -> Test Assurance
  -> Behavior Model
  -> Contract Verification if applicable
  -> E2E Design
  -> Service Simulator Design only if selected topology requires it

Service Simulator Implementation Plan
  -> accepted + fresh Service Simulator Spec
```

`EXTEND` reuses the minimum accepted fresh upstream slice and does not restart unrelated gates.

- [ ] **Step 3: Define persisted output ownership**

Preserve compatibility numbering and add:

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

Persist authoritative ledgers under capability `working/`, including `BC-*` and `CC-*`; human-readable numbered files are projections and must not silently become semantic authority.

Represent these states distinctly:

```text
NOT_APPLICABLE
NOT_VERIFIED
VERIFIED_NO_MATERIAL_DRIFT
```

- [ ] **Step 4: Re-run PS-84**

Expected:

```text
PS84_GREEN_MINIMUM_DEPENDENCY_SLICE
```

- [ ] **Step 5: Commit orchestration integration**

```bash
git add SKILL.md \
        references/session-orchestration.md \
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
- Consumes: `BC-*`/`CC-*` source bindings and umbrella freshness model.
- Produces: precise change-impact rules for Test Engineering and multi-repository consumer bindings.

- [ ] **Step 1: Define source bindings for accepted BC and CC records**

Use revision-bound references rather than only one repository HEAD:

```text
BC-042
source_bindings:
  architecture: RF-012@rev4
  declared: openapi.yaml@<service-baseline>
  implemented: src/orders/handler.py@<service-baseline>
  consumed: checkout-ui@<consumer-baseline>
```

and:

```text
CC-017
compared_views:
  declared: openapi.yaml@<service-baseline>
  implemented: src/orders/handler.py@<service-baseline>
  consumed: checkout-ui@<consumer-baseline>
  tested: tests/orders/...@<service-baseline>
```

- [ ] **Step 2: Define impact routing**

Required rules:

```text
tests-only change
  -> revalidate affected TM/MAT/GAP
  -> do not automatically invalidate BC

implementation or declared-contract change
  -> revalidate affected IMPLEMENTED/DECLARED views
  -> run CC/BC impact analysis

consumer-only change
  -> revalidate affected CONSUMED views
  -> revalidate consumer-facing simulator/E2E projections as needed
  -> service repository may remain unchanged
```

A changed bound file triggers impact analysis, not automatic semantic invalidation of every related BC.

- [ ] **Step 3: Re-run PS-85**

Expected:

```text
PS85_GREEN_IMPACT_DRIVEN_REVALIDATION
```

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
- Consumes: accepted `BC-*`, selected outputs, dependency DAG.
- Produces: deterministic dependency strategies, simulator consumer/control-plane contract, and E2E selection rules.

- [ ] **Step 1: Encode dependency strategy vocabulary**

Use exactly:

```text
REAL_DISPOSABLE
SERVICE_EMULATOR
CONTROLLABLE_MOCK
IN_PROCESS_DOUBLE
TEMP_RESOURCE
NOT_REQUIRED
```

Preserve the rule:

```text
Mock external uncertainty, not the behavior under test.
```

Require a reason per material dependency.

- [ ] **Step 2: Encode the two simulation classes**

```text
Dependency substitutes
  -> environment around the reviewed service

Service Simulator
  -> simulation of the reviewed service for its consumers
```

Service Simulator must support a real consumer-protocol surface where relevant and a separate test-only control plane. Illustrative control endpoints may include:

```text
/__test/health
/__test/reset
/__test/scenario
/__test/state
/__test/seed
```

Simulator scenarios must carry `BC-*` provenance and the relevant contract view/authority classification; they must not be generated blindly from Swagger alone.

- [ ] **Step 3: Encode E2E selection rule**

Require source `BC-*`, real participating components, allowed simulators/fakes, initial state, stimulus, material assertions, failure observability, cleanup/reset, CI suitability, and cost where useful.

Prefer a smaller test boundary when it proves the same material behavior more reliably and cheaply.

- [ ] **Step 4: Re-run PS-86**

Expected:

```text
PS86_GREEN_SIMULATOR_E2E_BOUNDARIES
```

- [ ] **Step 5: Commit simulator/E2E contract**

```bash
git add capabilities/test-review/SKILL.md \
        capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: define simulator and e2e test engineering boundaries"
```

---

### Task 6: Add consolidated validation and compatibility checks

**Files:**
- Create: `tests/test-engineering-capability-validation.md`
- Modify only if a discovered contract failure requires correction: files from Tasks 2-5.

**Interfaces:**
- Consumes: PS-81..86, existing PS-79 Test Assurance Summary behavior, current Test Review capability.
- Produces: one acceptance checklist proving new Test Engineering behavior without regressing the existing assurance layer.

- [ ] **Step 1: Create validation matrix**

The validation document must require:

```text
PS-79 remains GREEN
PS-81 GREEN behavior identity boundary
PS-82 GREEN contract authority preservation
PS-83 GREEN drift/gap orthogonality
PS-84 GREEN minimum dependency slice
PS-85 GREEN impact-driven revalidation
PS-86 GREEN simulator/E2E boundaries
```

Also verify static invariants:

```text
00/01/02 compatibility preserved
Behavior Model not a user checkbox
Contract Verification automatic when applicable
Contract Consistency Report optional
accepted BC writer = Behavior Model
accepted/classified CC writer = Contract Verification
CC resolution cannot silently rewrite BC
USE_EXISTING requires accepted/fresh dependency slice
PROJECTION_REPAIR cannot alter BC/CC/MAT/TM/GAP semantics
```

- [ ] **Step 2: Run all pressure scenarios in fresh contexts**

Do not treat a textual inspection of the Skill as behavioral validation. Record actual result/verdict for each scenario and preserve any new rationalizations found during GREEN testing.

- [ ] **Step 3: Run a compatibility canary for existing Test Review-only use**

Prompt a fresh agent for only Test Assurance on a fixture/project with no request for simulator/E2E/environment design.

Expected behavior:

```text
produces/targets 00 + 01
02 only if Test Plan selected
no forced 03-08 outputs
no unnecessary Contract Consistency Report
no silent optional capability expansion
```

- [ ] **Step 4: Commit validation contract and any minimal corrections**

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
- Modify: `capabilities/test-review/SKILL.md` only if final wording needs non-semantic projection cleanup.

**Interfaces:**
- Consumes: accepted GREEN capability contract from Task 6.
- Produces: user-facing documentation that describes, but does not redefine, Test Engineering behavior.

- [ ] **Step 1: Update README capability description**

Explain that Test Review now supports broader Test Engineering outputs while preserving Test Assurance as the required base. Show the selectable outputs:

```text
Test Assurance
Test Plan
Contract Consistency Report
Test Environment Design
Service Simulator Design
Service Simulator Implementation Plan
E2E Test Plan
```

Explain briefly that Behavior Model and applicable Contract Verification are internal gates rather than user checkboxes.

- [ ] **Step 2: Document output package**

Show `00` through `08`, mark optional files, and explain that authoritative working ledgers remain under `working/` while numbered documents are user-facing projections.

- [ ] **Step 3: Document Swagger/OpenAPI comparison without claiming Swagger is always authoritative**

Use wording equivalent to:

```text
When an external declared contract exists, Test Engineering compares it with
observed implementation, consumer dependencies, and executable tests. A
mismatch is recorded and adjudicated; no source wins merely because it is
newer, executable, or machine-readable.
```

- [ ] **Step 4: Re-run PS-79 and PS-81..86 after documentation changes**

Expected: all previously accepted GREEN verdicts remain GREEN.

- [ ] **Step 5: Commit documentation**

```bash
git add README.md capabilities/test-review/SKILL.md
git commit -m "docs: document test engineering capability"
```

---

## Final Verification Gate

Before declaring implementation complete:

- [ ] `git status --short` shows only expected state or is clean after commits.
- [ ] The implementation is based on `docs/superpowers/specs/2026-09-03-test-engineering-capability-design.md` and does not introduce semantics absent from the approved design.
- [ ] RED evidence exists for PS-81..86 from before behavior-changing Skill edits.
- [ ] GREEN evidence exists for PS-81..86 after the edits.
- [ ] Existing PS-79 Test Assurance Summary behavior remains GREEN.
- [ ] `capabilities/test-review/SKILL.md` remains concise enough to serve as the entrypoint; heavy semantics live in `capabilities/test-review/references/test-engineering-contract.md`.
- [ ] No output selection silently enables substantial optional work.
- [ ] Swagger/OpenAPI is treated as `DECLARED`, not automatic truth.
- [ ] `BC-*` contains behavior/provenance/authority but not executable-test evidence verdicts.
- [ ] `CC-*` and `GAP-*` remain independent.
- [ ] `EXTEND` and `REVALIDATE` execute the minimum affected dependency slice.
- [ ] Consumer-repository freshness is supported independently of service-repository freshness.
- [ ] Service Simulator and dependency substitutes remain distinct concepts.
- [ ] Simulator consumer plane and test-control plane remain separate.
- [ ] E2E can exist without a Service Simulator when topology does not require one.
- [ ] `00/01/02` compatibility behavior is preserved.
- [ ] README is only a projection of accepted capability semantics.

Expected final implementation verdict:

```text
TEST_ENGINEERING_CAPABILITY_IMPLEMENTED
```

If any behavioral scenario remains RED or INCONCLUSIVE, return instead:

```text
TEST_ENGINEERING_CAPABILITY_NOT_ACCEPTED
```

with the exact blocking scenario(s); do not weaken the scenario contract merely to obtain a GREEN result.
