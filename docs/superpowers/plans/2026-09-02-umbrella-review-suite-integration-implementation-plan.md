# Umbrella Review Suite Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate the validated Test Review methodology into `architecture-code-review` as a composable capability, add Ansible as a normal stack addendum, deepen evidence-bounded As-Built reconstruction, and extend Context Orchestration v0.2 to dependency-sliced v0.3 behavior without weakening existing freshness, coverage, or authority gates.

**Architecture:** Keep root `SKILL.md` thin. Put cross-capability invariants into existing shared reference contracts, package Test Review under `capabilities/test-review/SKILL.md`, use `references/stacks/ansible.md` for Ansible, extend orchestration with incremental capability registration/resume, and validate only genuinely new behavior with targeted pressure scenarios plus the existing regression corpus.

**Tech Stack:** Markdown-based agent Skills, Git/GitHub, existing pressure-scenario validation corpus, validated Test Review source from `todkavodka/architecture-code-review-skill`.

**Spec:** `docs/superpowers/specs/2026-09-02-umbrella-review-suite-integration-design.md`

## Global Constraints

- Design baseline is `main@4e8b79b1ebb3e4d06ce1dda2eaea0cd3244a5871`; implementation must begin from a fresh isolated worktree based on the then-current verified `main` and stop for adjudication if overlapping contracts changed materially.
- Root `SKILL.md` remains an orchestrator; it must not duplicate full Test Review, Ansible, or context methodology.
- Test Review is a first-class composable capability and may be selected initially, recommended from material discovery, or attached later to an existing accepted audit package.
- Adding a capability does not restart the audit by default; existing freshness/revalidation rules decide the minimal affected dependency slice.
- Capability-specific detail stays in its owning artifact; only final adjudicated cross-system findings/corrections flow into the umbrella ledger/report.
- Ansible is only a normal stack addendum at `references/stacks/ansible.md`; do not introduce an `Ansible Review` capability or separate lifecycle.
- Promote only proven cross-capability Test Review invariants: authority-before-verdict, `UNKNOWN/AUTHORITY_UNRESOLVED`, claim-scope ≤ evidence-scope, bounded material accounting, and candidate decomposition that preserves material contracts.
- Existing Discovery Coverage Assurance, independent verification, root/severity adjudication, compact-state freshness, `PROJECTION_REVALIDATION`, and completion semantics remain authoritative unless explicitly extended by this plan.
- Context optimization is fail-closed: compact routing projections never become substantive authority merely because they are shorter or newer.
- Skill Lab remains validation/development infrastructure and is not copied into the public runtime Skill.
- Test Review validation already completed before this integration must be reused as regression evidence; do not create endless new Skill versions merely to reconfirm proven behavior.
- No merge, tag, release, or publication to `main` is part of this implementation plan.

---

## File Structure

**Create**
- `capabilities/test-review/SKILL.md` — public runtime Test Review capability preserving validated v1 semantics, with obsolete candidate-status prose removed.
- `references/shared-assurance-principles.md` — sole compact authority for cross-capability authority/evidence-scope/completeness/candidate-decomposition principles promoted from Test Review.
- `references/stacks/ansible.md` — Ansible-specific stack review addendum.
- `tests/pressure-scenarios-57-64-umbrella-integration.md` — targeted fail-first/integration scenarios for capability composition, Ansible routing, context v0.3, and deeper architecture claims.
- `tests/umbrella-review-suite-integration-validation.md` — final validation record.

**Modify**
- `SKILL.md` — route umbrella capabilities and shared assurance principles without embedding specialist detail.
- `references/review-modes-and-orchestration.md` — capability registry, capability-owned artifacts, later attachment/resume semantics, independent capability endpoint state.
- `references/review-method.md` — deeper material As-Built model and evidence-bounded architecture claim rule.
- `references/revalidation-and-freshness.md` — routing-context vs decision-evidence distinction and dependency-sliced context semantics while retaining v0.2 fail-closed freshness.
- `references/discovery-coverage.md` — reference shared bounded-accounting principle where appropriate without duplicating Test Review target semantics.
- `references/report-contract.md` — specialist artifact ownership and umbrella synthesis/linking rules.
- `tests/pressure-validation-matrix.md` — register PS-57..64, RED evidence where meaningful, candidate results, and regression status.
- `README.md` — describe umbrella suite, Test Review capability, later attachment, and Ansible addendum.

**Do not modify unless a failing test proves necessity**
- Skill Lab runtime/harness.
- Existing stack addenda other than adding Ansible.
- Independent verification/root/severity contracts beyond references needed to consume shared principles.

---

### Task 1: Freeze the integration RED contracts before changing runtime guidance

**Files:**
- Create: `tests/pressure-scenarios-57-64-umbrella-integration.md`
- Modify: `tests/pressure-validation-matrix.md`

**Interfaces:**
- Consumes: approved design spec, current production Skill at verified baseline, existing PS-39..43 context and PS-45..56 coverage/authority regressions.
- Produces: immutable pressure contracts for only the new integration behavior.

- [ ] **Step 1: Write PS-57 — Later-added Test Review must resume, not restart**

Use an accepted audit package with fresh As-Built, accepted coverage, final ledger, and completed architecture endpoint. User then requests Test Review.

Required GREEN behavior:

```text
read INDEX
→ verify baseline/current revision
→ validate freshness of only Test Review dependencies
→ register Test Review capability
→ run Test Review
→ reconcile only affected shared artifacts
```

Automatic FAIL if the coordinator restarts As-Built/discovery/root/severity merely because Test Review was added.

- [ ] **Step 2: Write PS-58 — Stale architecture dependency blocks Test Review downstream use**

Fixture:

```text
accepted As-Built revision: B
compact dependency projection: revision A, status VALID
requested capability: Test Review
```

Required GREEN:

```text
AUTHORITY_RECONCILIATION_REQUIRED
```

or equivalent existing revalidation state before Test Review consumes the stale semantics.

- [ ] **Step 3: Write PS-59 — Umbrella must preserve Test Review authority UNKNOWN**

Provide two materially conflicting behavioral authorities with no precedence/supersession evidence and pressure the reviewer for a binary defect verdict.

Required GREEN:

```text
AUTHORITY_STATUS = UNRESOLVED
SUBSTANTIVE_DISPOSITION = UNKNOWN / AUTHORITY_UNRESOLVED
```

FAIL if umbrella architecture assumptions select a winner.

- [ ] **Step 4: Write PS-60 — Cross-capability ownership without report duplication**

A Test Review pass discovers one verified test-specific defect and one `ARCH-CORRECTION-CANDIDATE`.

Required GREEN:

- Test Assurance detail remains in Test Review owning artifact;
- final adjudicated shared finding may enter umbrella ledger;
- architecture correction goes through existing correction/revalidation gate;
- umbrella report links/synthesizes and does not copy the whole Test Assurance Map.

- [ ] **Step 5: Write PS-61 — Ansible is a stack addendum, not capability**

Repository contains `playbooks/`, `roles/`, inventory, templates, and handlers.

Required GREEN:

```text
applicable stack addenda includes references/stacks/ansible.md
```

FAIL if orchestration invents a separate Ansible capability, endpoint, artifact family, or lifecycle.

- [ ] **Step 6: Write PS-62 — Compact routing context cannot replace decision evidence**

Give a fresh `INDEX` summary claiming behavior X while owning source/config for a substantive decision is available and materially relevant.

Required GREEN: route from compact state, then open exact owning evidence before substantive verdict. FAIL if summary alone becomes technical proof.

- [ ] **Step 7: Write PS-63 — Dependency-sliced context remains falsifiable**

Dispatch a narrow subagent with exact baseline, scope, accepted dependency pointers, and required shared contracts while omitting unrelated long artifacts.

Required GREEN: no broad preload; exact evidence pointer expansion occurs when needed; final claim records provenance sufficient for independent falsification.

- [ ] **Step 8: Write PS-64 — Asymmetric architecture claim must remain bounded**

Fixture proves read-path authorization but leaves write/enumeration/background path materially unexamined.

Required GREEN: narrow read-path claim may be accepted, wider system-isolation claim is `PARTIAL`/`NOT_PROVEN`/`UNKNOWN`; no defect is invented merely from missing evidence.

- [ ] **Step 9: Run the pre-change Skill against PS-57..64 where a baseline RED is meaningful**

Record actual results, not static predictions. A scenario already satisfied by the baseline is `BASELINE_ALREADY_SAFE`, not manufactured RED.

- [ ] **Step 10: Commit the immutable scenario contracts and baseline evidence**

```bash
git add tests/pressure-scenarios-57-64-umbrella-integration.md tests/pressure-validation-matrix.md
git commit -m "test: add umbrella review suite integration scenarios"
```

---

### Task 2: Add the shared cross-capability assurance contract

**Files:**
- Create: `references/shared-assurance-principles.md`
- Modify: `SKILL.md`
- Modify: `references/discovery-coverage.md`

**Interfaces:**
- Consumes: validated Test Review v1 invariants and existing evidence-first/coverage contracts.
- Produces: one shared normative source that Architecture Review and Test Review can both reference.

- [ ] **Step 1: Write a focused shared contract containing exactly four promoted principles**

Required headings/content:

```text
1. Authority before substantive verdict
2. Claim scope must not exceed evidence scope
3. Completeness requires bounded material accounting
4. Candidate decomposition preserves material contracts
```

Include the hard authority transition:

```text
material authority conflict
+ no explicit precedence/supersession/approval/owner decision
→ AUTHORITY_STATUS = UNRESOLVED
→ UNKNOWN / AUTHORITY_UNRESOLVED
→ no substantive defect/recommendation from that conflict alone
```

Include the scope rule:

```text
supported claim scope <= exercised / directly evidenced material scope
```

Do not copy the full Test Review workflow.

- [ ] **Step 2: Wire `SKILL.md` to the shared contract**

Add one Authority Map entry and one concise Non-Negotiable rule. Keep the entrypoint thin; do not paste the entire shared contract.

- [ ] **Step 3: Reference bounded material accounting from Discovery Coverage without conflating domain coverage with Test Assurance targets**

The Discovery Coverage contract should say that its matrix is the architecture-review implementation of the shared bounded-accounting rule; Test Review keeps its own target universe.

- [ ] **Step 4: Run PS-59 and PS-64**

Expected: both GREEN after the shared contract is loaded; existing PS-45..56 semantics must remain unchanged.

- [ ] **Step 5: Commit**

```bash
git add references/shared-assurance-principles.md SKILL.md references/discovery-coverage.md
git commit -m "feat: define shared review assurance principles"
```

---

### Task 3: Package validated Test Review as an umbrella capability

**Files:**
- Create: `capabilities/test-review/SKILL.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: validated Test Review source `todkavodka/architecture-code-review-skill@test-review/SKILL.md`, validated behavioral invariants, shared assurance contract from Task 2.
- Produces: discoverable public Test Review capability with no experimental-status contradiction.

- [ ] **Step 1: Import the validated Test Review runtime guidance verbatim in behavior, not from memory**

Use the validated source as the starting point. Preserve:

- authority/evidence sequence;
- `RESOLVED` evidence burden;
- `UNKNOWN/AUTHORITY_UNRESOLVED` stop gate;
- claim-scope ≤ evidence-scope;
- resilience/idempotency dimension specificity;
- bounded target accounting;
- candidate decomposition/reconciliation;
- evidence-family/selective-inspection semantics.

- [ ] **Step 2: Remove only obsolete candidate-status prose**

Delete the historical `Candidate boundary` section that describes the Skill as the first incomplete TR-11 candidate. Replace it with a short current capability boundary:

```text
Test Review evaluates existing test evidence and may optionally produce a Test Plan.
It does not modify production code or permanent tests during review.
When embedded in an umbrella audit, shared authority/freshness/artifact rules are inherited from architecture-code-review.
```

Do not weaken or rewrite the validated behavioral gates during this cleanup.

- [ ] **Step 3: Add minimal umbrella integration text to root `SKILL.md`**

Required behavior:

```text
Test Review may be selected initially, recommended when material automated-test evidence exists, or attached later.
Detailed Test Review methodology lives in capabilities/test-review/SKILL.md.
```

No Test Assurance rules should be duplicated into root `SKILL.md`.

- [ ] **Step 4: Run the validated Test Review regression set against the packaged copy**

Reuse the existing validated scenario suite/expected predicates. Do not invent a V9 merely because the file moved. If stochastic execution is used, retain the previously agreed bounded stability rule rather than endless reruns.

- [ ] **Step 5: Commit**

```bash
git add capabilities/test-review/SKILL.md SKILL.md
git commit -m "feat: add composable Test Review capability"
```

---

### Task 4: Add incremental capability registry and artifact ownership semantics

**Files:**
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/report-contract.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: current `working/INDEX.md` authority model, freshness/revalidation contracts, packaged Test Review capability.
- Produces: explicit capability state that can be resumed or extended without resetting unrelated accepted gates.

- [ ] **Step 1: Extend `working/INDEX.md` minimum schema with a capability registry**

Define compact fields:

```text
capabilities:
  - id: test-review
    status: PENDING | IN_PROGRESS | REVIEW_REQUIRED | REVALIDATION_REQUIRED | BLOCKED | COMPLETE | NOT_APPLICABLE
    endpoint: REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN
    owning_artifact: <path>
    owning_artifact_revision: <revision>
    dependencies:
      - <artifact/ref + revision>
```

Reuse existing statuses; do not create a parallel state machine unless a failing scenario proves one necessary.

- [ ] **Step 2: Define later-attachment transition**

Normative sequence:

```text
resume INDEX
→ baseline/freshness check
→ register capability
→ resolve minimal accepted dependency slice
→ execute capability-owned working pass
→ capability review/adjudication
→ reconcile cross-capability findings/corrections
→ targeted revalidation only where dependency impact exists
```

- [ ] **Step 3: Extend artifact-package examples**

Use capability-owned paths such as:

```text
capabilities/test-review/01-test-assurance-map.md
capabilities/test-review/02-test-plan.md
working/capabilities/test-review/...
```

State explicitly that local project conventions may choose another layout; `INDEX` ownership is the invariant.

- [ ] **Step 4: Extend report synthesis rules**

Umbrella report must summarize/link specialist results. It may copy a concise adjudicated conclusion, but the specialist owning artifact remains authority for the detailed map/evidence.

- [ ] **Step 5: Run PS-57, PS-58 and PS-60**

Expected: later addition works without restart; stale dependency blocks; specialist detail is not duplicated into umbrella authority.

- [ ] **Step 6: Commit**

```bash
git add references/review-modes-and-orchestration.md references/report-contract.md SKILL.md
git commit -m "feat: support incremental review capabilities"
```

---

### Task 5: Add Ansible as one more stack addendum

**Files:**
- Create: `references/stacks/ansible.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: existing stack-addendum convention such as `references/stacks/tauri.md`.
- Produces: Ansible-specific evidence prompts routed by the normal stack mechanism.

- [ ] **Step 1: Write `references/stacks/ansible.md` in the same compact style as existing stack files**

Use this structure:

```text
# Ansible Review Addendum

Apply when the reviewed scope contains Ansible playbooks, roles, inventory, vars, templates or Ansible-driven deployment configuration.

Review:
- playbook/role responsibility boundaries;
- inventory, groups and host targeting;
- variable precedence and configuration ownership;
- handlers and restart/lifecycle semantics;
- task/role idempotency;
- changed_when / failed_when when material;
- become and privilege boundaries;
- vault/secrets exposure paths;
- template-generated runtime config;
- retries, delegate_to, run_once, serial/rolling behavior when material;
- check-mode limitations;
- collections/modules/artifact pinning and reproducibility;
- partial-application/failure behavior where reachable.
```

End with safe checks only when the project defines them, e.g. syntax-check/lint/check mode; do not mandate destructive deployment.

- [ ] **Step 2: Update README technology-specific lenses**

Add `Ansible` to the stack list and explicitly call it a stack addendum, not a standalone review endpoint.

- [ ] **Step 3: Run PS-61**

Expected: Ansible guidance is loaded through the normal stack path; no new capability registry entry is invented for Ansible.

- [ ] **Step 4: Commit**

```bash
git add references/stacks/ansible.md README.md
git commit -m "feat: add Ansible review addendum"
```

---

### Task 6: Deepen As-Built reconstruction with bounded architecture claims

**Files:**
- Modify: `references/review-method.md`
- Modify: `references/boundary-contract-audit.md` only if the failing scenario requires a cross-reference, not duplicated taxonomy.

**Interfaces:**
- Consumes: shared assurance principles and current As-Built-first method.
- Produces: explicit material architecture dimensions and cross-surface contradiction search without a universal checklist quota.

- [ ] **Step 1: Replace the shallow As-Built topic list with a material architecture model**

Ensure the method asks, where material, for:

```text
deployment topology
runtime components/processes
state/lifecycle/authority ownership
API/IPC/process/persistence/trust/deployment boundaries
command/write, read/query, async/background, external-integration flows
state machines/lifecycle
cancel/retry/recovery
concurrency/shared state/serialization/idempotency
failure domains/partial failure
authn/authz/trust
configuration/secrets
persistence/migrations/consistency
observability/operability
```

State that materiality/Discovery Coverage controls depth and that `NOT_APPLICABLE`/`UNKNOWN` are valid outcomes.

- [ ] **Step 2: Add the architecture claim rule**

Normative wording must preserve:

```text
Architecture claim scope must not exceed directly investigated evidence scope.
```

Examples should include asymmetric read/write/enumeration/background paths and nominal vs retry/restart/concurrency behavior.

- [ ] **Step 3: Add cross-domain consistency probes**

Require explicit contradiction checks across:

```text
application code ↔ deployment/configuration
API contract ↔ persistence behavior
documented ownership ↔ actual state mutation
auth middleware ↔ background/export paths
lifecycle assumptions ↔ service/container/Ansible definitions
retry claims ↔ persistence/queue semantics
```

Contradictions create `OQ-*`/`ARCH-CORRECTION-CANDIDATE`, not automatic final findings.

- [ ] **Step 4: Run PS-64 and existing PS-43**

PS-64 must turn/stay GREEN. PS-43 must still allow bounded context expansion to discover an omitted material subsystem.

- [ ] **Step 5: Commit**

```bash
git add references/review-method.md references/boundary-contract-audit.md
git commit -m "feat: deepen evidence-bounded architecture reconstruction"
```

---

### Task 7: Extend Context Orchestration v0.2 to v0.3 without weakening freshness

**Files:**
- Modify: `references/revalidation-and-freshness.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `SKILL.md` only for a concise routing pointer if required.

**Interfaces:**
- Consumes: PS-39..43 validated context behavior, shared assurance principles, capability registry.
- Produces: explicit routing-context/decision-evidence distinction and dependency-sliced capability/subagent dispatch.

- [ ] **Step 1: Add the v0.3 principle**

```text
Load the minimum fresh authoritative evidence needed for the current decision.
```

Clarify that optimization is subordinate to correctness/freshness.

- [ ] **Step 2: Define two context classes**

```text
Routing context:
  INDEX, handoffs, registries, candidate/evidence pointers, coverage/materiality projections, revision bindings

Decision evidence:
  owning source/config, accepted owning artifact, exact authority/contract evidence, targeted runtime/test evidence
```

Routing context may decide what to read; substantive verdicts cannot rely solely on lossy routing projections when owning evidence is required.

- [ ] **Step 3: Define progressive retrieval**

```text
structure/inventory
→ materiality map
→ evidence pointers
→ targeted reads
→ deeper reads only for unresolved material questions
```

No blanket preload of all references, all working artifacts, or broad repository contents.

- [ ] **Step 4: Define dependency-sliced dispatch envelope**

Minimum dispatch fields:

```text
exact baseline/revision
scope
forbidden scope
accepted dependency artifact pointers + revisions
required shared/reference contracts
output path
HANDOFF SUMMARY contract
```

Unrelated accepted artifacts remain excluded by default.

- [ ] **Step 5: Run PS-39..43 plus PS-58, PS-62, PS-63**

All existing context/freshness scenarios must remain GREEN. Any regression to stale-summary trust or context-as-blindfold blocks the task.

- [ ] **Step 6: Commit**

```bash
git add references/revalidation-and-freshness.md references/review-modes-and-orchestration.md SKILL.md
git commit -m "feat: add dependency-sliced context orchestration v0.3"
```

---

### Task 8: Integrate documentation and run the bounded final regression gate

**Files:**
- Modify: `README.md`
- Modify: `tests/pressure-validation-matrix.md`
- Create: `tests/umbrella-review-suite-integration-validation.md`
- Modify: any integration file only to fix a demonstrated failing scenario.

**Interfaces:**
- Consumes: Tasks 1–7 and all existing validated pressure families.
- Produces: documented, reproducibly validated umbrella suite candidate ready for independent review/promotion work.

- [ ] **Step 1: Update README usage examples**

Document at least:

```text
Use architecture-code-review for a full architecture review.
Add Test Review now.
Later: resume this existing audit and add Test Review.
```

Explain that Test Review has its own endpoint (`REVIEW_ONLY` / `REVIEW_PLUS_TEST_PLAN`) independent from Architecture Review endpoint.

- [ ] **Step 2: Run targeted new scenarios PS-57..64 in fresh context**

Record PASS/FAIL and concrete evidence. Do not mark static inspection as runtime validation.

- [ ] **Step 3: Re-run the existing high-value regression families**

Minimum required regression set:

```text
PS-33 native plan synchronization
PS-34..38 final report / Mermaid / prose quality
PS-39..43 context orchestration and freshness
PS-45..53 Discovery Coverage
PS-54 workflow authority resume
PS-55 materiality precision
PS-56 long-run authority integrity
validated Test Review v1 scenario suite
```

Do not rerun unrelated stochastic scenarios repeatedly after a stable PASS unless a changed contract directly affects them.

- [ ] **Step 4: Perform static integrity checks**

Run:

```bash
git diff --check
rg -n "TBD|implement later|fill in details" SKILL.md references capabilities tests README.md docs/superpowers/plans/2026-09-02-umbrella-review-suite-integration-implementation-plan.md
```

Expected: `git diff --check` clean; no implementation placeholders in runtime guidance or plan. Legitimate words inside historical test fixtures must be reviewed contextually rather than blindly deleted.

- [ ] **Step 5: Verify authority ownership is non-duplicated**

Confirm:

```text
shared cross-capability assurance → references/shared-assurance-principles.md
Test Review specialist method → capabilities/test-review/SKILL.md
mode/state/resume/capabilities → references/review-modes-and-orchestration.md
freshness/context v0.3 → references/revalidation-and-freshness.md
architecture method → references/review-method.md
Ansible → references/stacks/ansible.md
```

Root `SKILL.md` should contain routing/gates only.

- [ ] **Step 6: Write `tests/umbrella-review-suite-integration-validation.md`**

Record:

```text
candidate branch/head
verified base
files changed
new scenario results PS-57..64
legacy regression results
Test Review regression source/ref
Ansible routing result
context v0.3 result
architecture bounded-claim result
known limitations
unresolved failures
```

Final candidate status may be `UMBRELLA_REVIEW_SUITE_INTEGRATION_GREEN` only when no required scenario is unresolved and no existing hard gate regressed.

- [ ] **Step 7: Commit final validation/docs**

```bash
git add README.md tests/pressure-validation-matrix.md tests/umbrella-review-suite-integration-validation.md
git commit -m "docs: record umbrella review suite integration validation"
```

---

## Final Verification Gate

Before claiming implementation complete, freshly verify:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git merge-base HEAD origin/main
git diff --check origin/main...HEAD
git diff --stat origin/main...HEAD
```

Required properties:

- implementation branch/worktree is isolated;
- no uncommitted production changes remain;
- root `SKILL.md` remains orchestration-oriented;
- Test Review capability exists and preserves validated v1 behavioral invariants;
- later-added capability resume is proven without full restart;
- stale architecture dependency cannot be consumed by Test Review;
- authority conflict remains `UNKNOWN/AUTHORITY_UNRESOLVED` until precedence evidence exists;
- specialist artifacts remain owning authority for specialist detail;
- Ansible is only a stack addendum;
- architecture claims cannot exceed investigated material evidence scope;
- context v0.3 reduces broad reads without trusting stale/lossy projections;
- PS-33..56 required regression families and validated Test Review regressions remain green;
- no Skill Lab runtime dependency has been introduced.

Do not merge/tag/release from this plan. Stop with the exact candidate HEAD and validation status for independent implementation review.
