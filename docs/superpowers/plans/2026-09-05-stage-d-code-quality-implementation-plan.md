# Stage D — Code Quality Review Implementation Plan

## 1. Baseline and authority inputs

Implementation baseline: `7a7021ecbb68c1357d084f800195be1e38cdd062`.

Approved inputs:

- `docs/superpowers/specs/2026-09-05-stage-d-code-quality-discovery.md`;
- `docs/superpowers/reviews/2026-09-05-stage-d-code-quality-discovery-review.md`;
- `docs/superpowers/specs/2026-09-05-stage-d-code-quality-design.md`;
- `docs/superpowers/reviews/2026-09-05-stage-d-code-quality-design-review.md`;
- `SKILL.md`, Shared Evidence/STM, orchestration, revalidation, remediation,
  and Stage B projection contracts.

The Design is the semantic authority for this plan. This plan introduces no
new semantic choices and does not modify accepted Stage A, B, or C contracts.

## 2. Current-state re-check

The current tree contains no `capabilities/code-quality-review/**`, no
`CQ-*`/`CQRA-*` implementation, no Code Quality capability contract, no Code
Quality projection registration, and no Code Quality-specific pressure suite.
Reachable history contains no material Stage D implementation. Existing
Architecture maintainability checks, Shared Evidence/STM, Test Engineering,
and Stage B references are reusable foundations, not Code Quality authority.

| Implementation area | Status | Evidence |
|---|---|---|
| Code Quality capability entrypoint | MISSING | Only `capabilities/test-review/SKILL.md` exists |
| CQ semantic contract and finding authority | MISSING | No `CQ-*` contract or records |
| CQRA remediation authority | MISSING | `TASK-*` is Test Engineering-owned; no capability-neutral authority exists |
| Coverage/session state | MISSING | Generic coordinator contracts exist, but no CQ registration/state |
| Orchestration/output selection | MISSING | No CQ capability or selectors |
| Revalidation/freshness integration | MISSING | Shared rules exist, no CQ bindings/impact declarations |
| Stage B CQ projections/packages | MISSING | No CQ `PRJ-*` registration or package |
| Language/framework addenda contract | MISSING | Existing stack addenda are not CQ addenda |
| Pressure scenarios and validation | MISSING | Existing PS ranges stop at `PS-99`; none are CQ-specific |
| Public discoverability | PARTIALLY_PRESENT | README/roadmap describe Stage D as planned only |

No material implementation was found; planning may proceed.

## 3. Implementation goals and non-goals

Goals:

- add a selectable Code Quality capability with `CQ-*` semantic findings;
- add Code Quality-owned `CQRA-*` remediation actions;
- persist bounded CQ coverage/session state and provenance;
- reuse `WS-*`/`EV-*`, targeted accepted/fresh STM, existing orchestration,
  revalidation, and Stage B lifecycle;
- provide independently selectable Findings View/Report and Summary, with
  optional derived Hotspots and Roadmap Contribution;
- establish proportional, human-readable pressure and contract validation.

Non-goals:

- no automatic refactoring or source changes;
- no formatter/linter replacement, pentesting, vulnerability scanner,
  performance profiler, runtime test execution, simulator, or architecture
  redesign;
- no private factual model, second package manager, generic graph framework,
  parallel projection lifecycle, or large agent-testing harness;
- no changes to Stage A/B/C semantic authority.

## 4. Expected file inventory

### Create

- `capabilities/code-quality-review/SKILL.md` — concise user-facing entrypoint,
  scope, outputs, non-goals, and links to detailed contracts.
- `capabilities/code-quality-review/references/code-quality-contract.md` — CQ
  authority, `CQ-*` identity, taxonomy, evidence/materiality, boundaries,
  relations, addenda, and tooling authority.
- `capabilities/code-quality-review/references/code-quality-lifecycle.md` —
  candidate state, lifecycle, applicability, disposition, freshness, CQRA,
  coverage state, source bindings, and remediation transitions.
- `capabilities/code-quality-review/references/code-quality-projection.md` —
  CQ outputs, selection, Stage B registration/package declarations, impact
  handoff, and projection-only boundaries.
- `tests/pressure-scenario-100-smell-vs-finding.md` through
  `tests/pressure-scenario-114-package-selection.md` — the bounded fail-first
  suite defined in section 5.

### Modify

- `references/review-modes-and-orchestration.md` — capability registration,
  independent selection, persistent CQ scope/coverage/output references, and
  resume routing.
- `references/revalidation-and-freshness.md` — CQ binding/impact routing only;
  shared freshness semantics remain authoritative.
- `references/projection-gates-and-packages.md` — only if the existing
  capability-owned declaration placement requires a registration pointer;
  do not alter shared policy semantics.
- `README.md` — concise discoverability and non-goals.

### Optional

- one small language/framework addendum example under
  `capabilities/code-quality-review/references/addenda/`, only if a real
  implementation uncertainty demonstrates that the core contract cannot
  validate applicability without it. The first implementation should prefer
  the addenda contract alone.

### Forbidden unless independently reviewed

Any source/runtime code, migrations, CI, broad stack addenda, Stage A/B/C
contract edits, new package manager, generic relationship framework, or
repository-wide tooling configuration. `working/INDEX.md` is a runtime
coordinator artifact and must not be created as CQ semantic authority by this
plan; only the existing coordinator contract is extended with CQ references.

## 5. Fail-first pressure-scenario plan

Stage B already owns `PS-100` through `PS-116`; reserve the first unused
contiguous Stage D range, `PS-117` through `PS-131`. These are plain Markdown
acceptance artifacts, not a runner or
fixture framework. Each records the pressure condition, current expected RED
reason, future GREEN invariant, and exact contract references. Do not weaken a
scenario to manufacture RED evidence.

| ID | Pressure condition | Expected RED before implementation | Future GREEN invariant |
|---|---|---|---|
| `PS-117` | metric, smell label, or LOC threshold without consequence | no CQ materiality gate | warning/metric alone is not a finding |
| `PS-118` | local issue versus material cross-boundary mechanism | no CQ/RF boundary | CQ-only remains distinct; escalation is adjudicated by Architecture |
| `PS-119` | same evidence interpreted as CQ and TE GAP/TASK | no independent ownership relation | CQ cannot write or replace TE authority |
| `PS-120` | heuristic candidate versus accepted finding | no transient candidate boundary | only adjudicated material candidates create `CQ-*` |
| `PS-121` | lifecycle, applicability, disposition, and freshness combination | no legal-state matrix | invalid combinations are rejected and axes remain independent |
| `PS-122` | completed remediation with unresolved finding | no CQRA/revalidation rule | `CQRA COMPLETED != CQ RESOLVED` |
| `PS-123` | materiality, severity, and confidence disagreement | no bounded CQ severity gate | each dimension is independent; warning count cannot decide severity |
| `PS-124` | generated/vendor code, exception, or false positive | no applicability/disposition control | exclusion, exception, false positive, and resolution remain distinct |
| `PS-125` | security-relevant quality mechanism | no current security handoff | CQ may retain quality meaning; Architecture/security owns adjudication |
| `PS-126` | unsupported or conflicting language/framework addenda | no applicability/conflict rule | core review degrades safely; heuristics do not create authority automatically |
| `PS-127` | dirty and partial selected scope | no provenance/coverage authority | dirty provenance and `COMPLETE/PARTIAL/BLOCKED` qualify claims |
| `PS-128` | file/dependency/configuration change | no CQ impact routing | only impacted CQ slice revalidates; no automatic full rerun |
| `PS-129` | interrupted workflow resume | no persisted CQ state | `RESUME` restores scope, outputs, blockers, and semantic references |
| `PS-130` | semantic finding versus generated report | no Stage B boundary | semantic authority is separate from `PRJ-*` projection |
| `PS-131` | selected output with stale optional output | no package closure policy | policy evaluates selected output plus dependency closure only |

The suite collectively covers all 26 Design pressure cases through grouped
conditions. `PS-117`–`PS-131` are new and do not collide with existing Stage A,
B, or C ranges. Task 1 creates these files and establishes historical RED
observations; no custom harness is authorized.

Task 1 is a hard sequencing gate. After creating only the scenario files,
evaluate every scenario against the exact unchanged approved implementation
baseline and record the actual RED evidence, including why the failure is
attributable to the missing Stage D contract. An expected RED reason is not
actual RED evidence. If any scenario is unexpectedly GREEN before Task 2,
stop with `STAGE_D_TASK_1_UNEXPECTED_GREEN`; do not weaken or rewrite the
scenario, add implementation to manufacture RED, fabricate evidence, or
proceed automatically. Adjudicate whether the result reflects existing
behavior, a scenario defect, hidden implementation, duplicated baseline
contract, an incorrect expectation, or another evidence-backed cause. Task 2
may begin only after all required scenarios have genuine historical RED
evidence and no implementation code or contract was added during its
establishment.

## 6. Semantic contract implementation

**Purpose:** implement the approved CQ authority in
`capabilities/code-quality-review/references/code-quality-contract.md` and
`code-quality-lifecycle.md`.

The contract must map:

- `CQ-<stable allocation>` finding identity and persistence;
- one primary language-neutral taxonomy category and source/evidence bindings;
- observation → transient candidate → applicability/evidence/materiality →
  accepted finding;
- `ACTIVE`, `RESOLVED`, `SUPERSEDED` finding lifecycle;
- `APPLICABLE`, `NOT_APPLICABLE`, `EXCLUDED` applicability;
- `FALSE_POSITIVE`, `ACCEPTED_EXCEPTION`, `WONT_FIX` disposition;
- `CURRENT`, `STALE`, `BLOCKED` freshness;
- `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` severity and independent confidence;
- `COMPLETE`, `PARTIAL`, `BLOCKED` Code Quality session/assessment coverage;
- `DUPLICATE`, `CORRELATED`, `CAUSAL`, `ESCALATED`, `DERIVED`, `INDEPENDENT`;
- minimum evidence and no-tool-authority rules;
- Architecture/RF, TE, Shared Evidence/STM, and security ownership boundaries.

Verification: targeted static contract checks and review against the approved
Design; each PS-117–PS-131 must cite the relevant contract rule. Commit
boundary recommendation: `feat: define code quality semantic contract`.

## 7. Shared Evidence and STM integration

**Purpose:** consume existing factual infrastructure without duplication.

Implementation must:

- use `WS-*` for bounded evidence grouping and `EV-*` for source-local
  observations;
- consume accepted, sufficiently covered, fresh, and resolved targeted STM
  (`COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, `FLOW-*`, `AUTH-*`, `CFG-*`,
  `ERR-*`) only when system-level context is required;
- block only the dependent CQ interpretation when required STM is missing,
  stale, disputed, or insufficiently covered, then route through the existing
  STM workflow;
- never rewrite STM or construct a private CQ factual model.

Prefer reference integration and existing Technical Model Gate wiring. Extend
shared wiring only if the current coordinator has no capability registration
point; do not duplicate Stage A mechanisms. Verification: trace each STM
dependency in a targeted contract check and confirm local EV observations do
not become CQ findings automatically. Commit with Task 2 or a small follow-up
only if the change is independently reviewable.

## 8. Architecture, Test Engineering, and security integration

**Purpose:** preserve independent authority while making relationships useful.

Add explicit capability adapters/references for:

- Architecture `RF-*`: CQ may remain CQ-only, correlate/relate causally, or
  request escalation; it never writes or changes RF authority;
- Test Engineering `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*`: CQ may
  record a distinct interpretation and relation; it never mutates TE records;
- current Architecture/security semantics: there is no dedicated Security
  capability; security-relevant mechanisms route to the existing owner, while
  CQ quality meaning may remain correlated.

Verify relation direction/cardinality and no lifecycle/severity transfer by
targeted checks for `DUPLICATE`, `CORRELATED`, `CAUSAL`, `ESCALATED`, `DERIVED`,
and `INDEPENDENT`. Commit boundary recommendation: included with the semantic
contract if cohesive, otherwise `feat: integrate code quality authority boundaries`.

## 9. Orchestration and output selection

**Purpose:** make Code Quality independently selectable and resumable.

Modify the existing coordinator/capability registration in
`references/review-modes-and-orchestration.md` to persist references to CQ
scope/assessment authority, selected outputs, current phase, blockers, STM
prerequisite state, freshness/verification state, and projection impact state.
`working/INDEX.md` remains coordinator authority only.

Implement these boundaries:

- `NEW`: select CQ independently and require evidence/targeted STM before CQ
  semantic authority;
- `EXTEND`: add only requested CQ scope/output and reuse valid upstream work;
- `REVALIDATE`: route source/dependency/config/STM/related-record impact to the
  minimum CQ slice, not a full rerun;
- `RESUME`: restore persisted CQ scope, outputs, semantic references,
  blockers, and phase without chat/prose reconstruction.

Expose independent output selections for Findings View/Report and Summary;
Hotspots and Roadmap Contribution are optional derived selections and are not
implicitly enabled. CQ semantic findings are not an output toggle. Verification:
resume-state contract checks, selected-output minimum-slice checks, and
PS-129. Commit boundary recommendation: `feat: integrate code quality review orchestration`.

## 10. CQRA remediation implementation

**Purpose:** implement Code Quality-owned remediation without creating a generic
project-management system.

In `code-quality-lifecycle.md`, define `CQRA-<stable allocation>` with linked
CQ findings, action/rationale, owner/scope, semantic/evidence basis,
provenance, status, and source/freshness dependencies. Use the approved
minimal lifecycle `PROPOSED → PLANNED → COMPLETED` or `CANCELLED`, with
`SUPERSEDED` for replacement. Permit one CQ finding to many actions and one
action to many findings.

Completion records implementation evidence but never resolves CQ; CQ
resolution requires independent revalidation. Underlying semantic changes
make the action stale or require re-evaluation. Verify `CQRA COMPLETED != CQ
RESOLVED`, no `TASK-*` mutation, and no projection identity on CQRA. Commit
boundary recommendation: `feat: add code quality remediation lifecycle`.

## 11. Coverage and dirty-state handling

**Purpose:** represent qualified scope without a second factual model.

Add the Code Quality session/assessment coverage fields to the owning CQ
session state: requested, reviewable, excluded, unavailable, unsupported,
dirty/noncanonical scope, status, limitation reason, and affected claims/
outputs. Use `COMPLETE`, `PARTIAL`, and `BLOCKED`.

`PARTIAL` preserves unaffected accepted findings but qualifies aggregate claims;
`BLOCKED` blocks only dependent claims/projections. Reports must disclose
coverage and never imply repository-wide review. Dirty review requires the
committed repository base, explicit working-tree marker, actual file/content
bindings, untracked-source status, and a non-reproducibility note. Verification:
PS-127 plus targeted checks for selected scope, excluded vendor/generated
regions, and unavailable source. Commit boundary recommendation: with
orchestration, unless coverage state is independently reviewable.

## 12. Freshness and impact-driven revalidation

**Purpose:** bind findings to evidence and revalidate only affected semantics.

In `references/revalidation-and-freshness.md` and CQ lifecycle references,
declare bindings for repository/dirty baseline, file, symbol/content identity,
dependency and framework versions, configuration, addendum revision, targeted
STM, and related RF/TE records. Route file/symbol moves, semantic refactors,
dependency/framework/configuration changes, STM revisions, generated-code
regeneration, deleted source, and related-record changes through impact
analysis.

Equivalent refactors may retain CQ identity only when semantic bindings remain
valid. `REVALIDATE` marks affected findings/candidates stale and validates the
minimum slice; it does not regenerate projections. Verification: PS-128,
targeted changed-binding checks, and stale-action checks. Commit boundary
recommendation: `feat: add code quality revalidation and freshness`.

## 13. Language/framework addenda and tooling boundary

**Purpose:** keep the core contract language-neutral and evidence-first.

Implement the addenda contract in `code-quality-contract.md` first: applicability
declaration, language/framework/version context, idioms, evidence expectations,
known false positives, conflict handling, and unsupported-language fallback to
core semantics. Do not add a catalog initially. Add one small example only if
the core implementation cannot demonstrate applicability otherwise.

Tool output, AST matches, linter warnings, grep hits, dependency analyzer
results, and framework scanner results enter as observations/candidate evidence.
They cannot create accepted CQ authority or set materiality/severity. Verify
PS-126 and the no-tool-authority invariant. Commit boundary recommendation:
`feat: establish code quality addenda and tooling boundary` only if this is a
separate coherent change.

## 14. Stage B projection and package integration

**Purpose:** register generated CQ views in the shared lifecycle.

In `code-quality-projection.md`, declare each independently regeneratable output
with stable `PRJ-*` identity, owning capability and projection contract
revision, exact semantic dependencies, upstream projection dependencies where
applicable, frozen dependency-resolution snapshot, candidate generation,
`V1`–`V4`, canonical fingerprint, verified revision, freshness, and `RG-*`
regeneration routing. Semantic `CQ-*`, `CQRA-*`, and coverage/session state do
not receive PRJ identities.

Declare finite package membership as explicit selected outputs plus dependency
closure. Reuse exactly:

- `PERMISSIVE` — stale/blocked optional projections may be visible with
  limitations;
- `REQUIRED_SCOPE_CURRENT` — selected output/scope closure must be current;
- `ALL_SCOPED_CURRENT` — every explicitly required scoped member must be
  current.

Selecting Findings View and Summary does not require Hotspots or Roadmap
Contribution unless selected or dependency-required. Semantic changes perform
Projection Impact Analysis and persist `PROJECTION_IMPACT_ACCOUNTED`; explicit
regeneration is separate. `PROJECTION_REPAIR` cannot modify CQ semantics.
Verification: package membership/freshness checks, PS-130, PS-131, and shared
Stage B contract review. Commit boundary recommendation: `feat: integrate code quality projections`.
## 15. README and discoverability

Modify `README.md` minimally so users can see that Code Quality Review is a
separate, independently selectable capability. Mention the Findings View/
Report and Summary, optional derived outputs, evidence-first behavior, and the
fact that it does not automatically modify code. Link to the capability
entrypoint rather than copying the semantic contract. Verify no Stage D status
change or semantic duplication is introduced. Commit boundary recommendation:
`docs: document code quality review`.

## 16. Validation strategy and proportionality

Apply evidence first → automation second → framework last.

1. Evaluate the plain PS-117–PS-131 files against the unchanged baseline and
   establish actual historical RED evidence before implementation.
2. Run targeted deterministic static/contract checks for identifiers, state
   combinations, ownership, coverage, freshness, package closure, and
   projection metadata.
3. Use focused agent acceptance only where agent behavior or user-facing
   selection cannot be proven by static inspection.
4. Optionally perform a small lightweight MiMo real-agent acceptance after the
   semantic and orchestration gates are stable.

`DO_NOT_BUILD_HARNESS` is the default. No reusable agent E2E framework, Skill
Lab successor, fixture engine, or harness-for-harness infrastructure is
planned. If a concrete uncertainty later demonstrates strong reuse and lower
cost, stop and obtain a separately reviewed plan. Stop-loss tokens:
`STOP_HARNESS_EXPANSION` and `VALIDATION_BUDGET_EXCEEDED`.

## 17. Task dependency DAG

```text
Task 1 pressure scenarios
    ↓
Task 2 semantic contract ───────────────┐
    ↓                                   │
Task 3 capability entrypoint/boundaries │
    ↓                                   │
Task 4 orchestration/output/resume/coverage
    ↓                                   │
Task 5 CQRA + freshness/revalidation ──┤
    ↓                                   │
Task 6 Stage B projections/packages ────┤
    ↓                                   │
Task 7 addenda/tooling boundary ───────┤
    ↓                                   │
Task 9 targeted validation/finalization │

Task 8 README/discoverability ──────────┘ (may follow Task 3; before Task 9)
```

Mandatory ordering is pressure evidence before contract implementation;
semantic authority before orchestration and CQRA; orchestration/coverage and
freshness before projection packages; all semantic and projection boundaries
before final validation. Task 8 is independent after the capability entrypoint
exists and must not block semantic implementation.

## 18. Ordered task list

### Task 1 — Establish fail-first Code Quality pressure scenarios

**Purpose:** create PS-117–PS-131 as cheap, deterministic acceptance pressure.

**Create:** the 15 scenario files listed in section 5. **Modify:** none.
**Preconditions:** clean implementation branch at the approved baseline and
existing PS range confirmed. **Invariants:** no implementation guidance is
added; candidates do not pass by prose. **Verification:** execute/evaluate
each scenario against the unchanged approved baseline, record actual RED
evidence and its intended missing-contract cause, and confirm no implementation
files/contracts changed. An expected RED reason alone is insufficient. If any
scenario is unexpectedly GREEN, stop with
`STAGE_D_TASK_1_UNEXPECTED_GREEN` for sequencing adjudication; do not weaken
the scenario or proceed to Task 2. Task 2 is blocked until the RED checkpoint
passes. No custom runner is authorized.
**Commit:** `test: add fail-first code quality pressure scenarios`.

### Task 2 — Implement Code Quality semantic and lifecycle contracts

**Purpose:** establish `CQ-*`, candidate flow, taxonomy, evidence, lifecycle,
applicability, disposition, freshness, severity/materiality/confidence,
coverage fields, relation types, and no-tool authority.

**Create/modify:** `code-quality-contract.md` and
`code-quality-lifecycle.md`. **Preconditions:** Task 1 committed; Design
checkpoint present. **Invariants:** no RF/TE/STM mutation; no private facts;
transient candidate is not a finding; `CQRA COMPLETED != CQ RESOLVED`.
**Verification:** focused static contract checks plus independent semantic
review; PS-117–PS-127 should turn GREEN where applicable.
**Commit:** `feat: define code quality semantic contract`.

### Task 3 — Add capability entrypoint and authority boundaries

**Purpose:** expose a concise Code Quality capability and wire references for
Architecture, TE, security routing, Shared Evidence, and STM.

**Create:** `capabilities/code-quality-review/SKILL.md`.
**Modify:** only the minimum capability registration points required by the
existing public/umbrella entrypoint conventions. **Preconditions:** Task 2.
**Invariants:** CQ is distinct from RF and TE; no dedicated Security capability;
tooling is evidence only. **Verification:** entrypoint discoverability and
authority-boundary checks; PS-118, PS-119, and PS-125.
**Commit:** `feat: add code quality review capability`.

### Task 4 — Integrate orchestration, output selection, resume, and coverage

**Purpose:** support independent CQ selection and persistent minimum-slice
workflow state.

**Modify:** `references/review-modes-and-orchestration.md` and the narrow
coordinator integration points. **Preconditions:** Tasks 2–3.
**Invariants:** `NEW`, `EXTEND`, `REVALIDATE`, `RESUME` remain existing modes;
`working/INDEX.md` is coordinator authority only; coverage state is owned by
the CQ session/assessment; `COMPLETE/PARTIAL/BLOCKED` qualify claims.
**Verification:** selected output persistence, resume recovery, partial/blocked
scope checks; PS-127 and PS-129.
**Commit:** `feat: integrate code quality review orchestration`.

### Task 5 — Implement CQRA and targeted freshness/revalidation

**Purpose:** add Code Quality remediation and source/dependency impact behavior.

**Create/modify:** `code-quality-lifecycle.md` and the narrow CQ integration in
`references/revalidation-and-freshness.md`. **Preconditions:** Tasks 2–4.
**Invariants:** stable CQRA identity; one-to-many/many-to-one links; completed
CQRA never resolves CQ automatically; changed dependencies trigger impact
analysis, not a full rerun. **Verification:** state-combination checks, stale
binding checks, and PS-122/PS-128.
**Commit:** `feat: add code quality remediation and revalidation`.

### Task 6 — Integrate Stage B projections and package policies

**Purpose:** register generated Findings View/Report and Summary projections
without a parallel lifecycle.

**Create/modify:** `code-quality-projection.md` and only the existing package
registration pointer if required. **Preconditions:** Tasks 2–5.
**Invariants:** semantic CQ/CQRA/coverage authority has no PRJ identity;
projection uses dependency snapshot, V1–V4, fingerprint, verified revision,
freshness, `RG-*`, PIA, and explicit package membership. **Verification:**
projection dependency and package policy checks; PS-130/PS-131. Do not run a
full regeneration framework as part of this task.
**Commit:** `feat: integrate code quality projections`.

### Task 7 — Add language/framework applicability and tooling boundary

**Purpose:** establish core/addenda behavior without a large catalog or tool
stack.

**Modify:** `code-quality-contract.md`; **optionally create** one addendum only
if a concrete applicability check cannot be demonstrated otherwise.
**Preconditions:** Task 2 and Task 3; no addendum is required for the initial
contract if core fallback is testable. **Invariants:** unsupported addendum is
not whole-capability N/A; conflicting heuristics do not create authority;
tools do not adjudicate. **Verification:** PS-126 and focused applicability
checks. **Commit:** `feat: establish code quality addenda and tooling boundary`.

### Task 8 — Update README discoverability

**Purpose:** make the capability visible without duplicating detailed semantics.

**Modify:** `README.md` only. **Preconditions:** Task 3 capability entrypoint.
**Invariants:** independent selection and non-goals are clear; no roadmap
status change. **Verification:** targeted text/link check and review for
semantic duplication. **Commit:** `docs: document code quality review`.

### Task 9 — Targeted validation, independent review, and finalization

**Purpose:** prove the implementation against the approved Design and preserve
historical RED → GREEN evidence.

**Modify:** only implementation-owned validation artifacts if a prior task
explicitly created them; do not add a harness. **Preconditions:** Tasks 1–8,
all semantic/projection gates implemented. **Invariants:** all pressure
scenarios GREEN under current contracts; no blocking implementation findings;
no unauthorized files or harness. **Verification:** `git diff --check`,
targeted deterministic checks, focused agent acceptance where necessary,
independent implementation review, and final Stage B/package/authority audit.
**Commit:** small final correction commit only when review identifies one;
otherwise no extra commit.

## 19. Commit strategy

Use the logical boundaries above, not one commit per file. Keep Task 1,
semantic authority, orchestration, remediation/revalidation, projections, and
discoverability independently reviewable. Never include `task-5-report.md`.
Do not modify accepted Discovery/Design artifacts to make implementation
validation pass.

## 20. Review checkpoints

Request independent review after:

1. Task 2 — semantic authority/lifecycle;
2. Tasks 4–5 — orchestration, coverage, CQRA, and freshness;
3. Task 6 — Stage B projection/package integration;
4. Task 9 — final implementation acceptance.

Task 1 and Task 8 receive lightweight targeted inspection. Avoid review
ceremony that does not reduce semantic risk.

## 21. Baseline hygiene policy

If implementation discovers failures or dirty state predating Stage D, stop with
`STAGE_D_BASELINE_HYGIENE_REQUIRED`. Do not repair unrelated baseline debt,
weaken pressure scenarios, or edit historical accepted artifacts. A dirty
implementation worktree must be reconciled before claiming a Stage D result.

## 22. Implementation stop conditions

Stop and request a bounded re-review if any of the following occurs:

- a change would make CQ own RF, TE, STM, or Architecture/security authority;
- a new private factual model, generic relationship framework, package manager,
  or parallel projection lifecycle is proposed;
- a required STM slice is missing, stale, disputed, or insufficiently covered;
- a semantic change is hidden as `PROJECTION_REPAIR` or triggers implicit
  regeneration;
- package membership is inferred globally rather than explicitly resolved;
- coverage claims exceed reviewable evidence;
- `CQRA COMPLETED` is treated as CQ resolution without revalidation;
- validation expands beyond proportional checks; use
  `STOP_HARNESS_EXPANSION` / `VALIDATION_BUDGET_EXCEEDED`;
- unexpected Stage D implementation is found outside the planned inventory.

## 23. Completion criteria

Stage D implementation is complete only when:

- PS-117–PS-131 have actual pre-implementation RED evidence attributable to
  the intended missing Stage D contracts and are GREEN under the implemented
  contracts;
- CQ identity, lifecycle, applicability, disposition, freshness, coverage,
  and severity/materiality/confidence are implemented;
- CQRA is implemented with evidence-backed revalidation semantics;
- Architecture, Test Engineering, security routing, Shared Evidence, and STM
  ownership remain intact;
- `NEW`, `EXTEND`, `REVALIDATE`, and `RESUME` use minimum slices and persistent
  state;
- Stage B projection/package policies and PIA are integrated without global
  regeneration;
- README discoverability is updated without semantic duplication;
- targeted deterministic validation and focused acceptance pass;
- independent implementation review has no material blocking findings;
- no unauthorized harness or broad infrastructure was built.

## 24. Promotion prerequisites

Before promotion, require a clean implementation worktree, review of the
implementation diff against this plan and the approved Design, all required
targeted checks, final acceptance of semantic and projection boundaries, and
an explicit checkpoint commit. Preserve historical pressure evidence and the
approved Discovery/Design lineage. Promotion/roadmap closeout is a separate
gate and must not be performed by implementation Task 9.
