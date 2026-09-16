# Review Modes and Workflow Orchestration

## Requested and resolved work state

The coordinator persists confirmed user selections separately from dependency closure:

```text
requested_work:
  capabilities: [<explicit or confirmed capability ids>]
  standalone_outputs: [<explicit or confirmed output ids>]
  scope: PROJECT | PRODUCT
  confirmation_status: CANDIDATE | CONFIRMED

resolved_work:
  dependency_slice: [<minimum accepted/fresh or required refs>]
  required_gates: [<owning gate states>]
  projection_members: [<selected existing projection/package members>]
  limitations: [<availability, coverage, freshness, authority limits>]
  authorization_requirements: [<separate approvals still required>]
```

`requested_work != resolved_work`. Internal STM, Evidence, Behavior Model, Contract Verification, Product qualification, and projection dependencies are never backfilled into selected capabilities. Multiple requested items use a deduplicated minimum dependency union and never escalate automatically to the complete Review Suite.

### Change Review requested and resolved work

For `CHANGE_REVIEW`, the user's requested work records only their confirmed review lenses and outputs. Lenses are user-facing review choices, not implicit capability selections; the ordinary three semantic capabilities remain the only selectable capabilities.

```text
requested_work:
  change_review:
    lenses: [change-only | architecture | code-quality | test |
             interface-contract | explicit-full-change-review]
    outputs: [summary | inventory | affected-facts | candidate-findings |
              existing-finding-effects | test-impact | projection-prediction]

resolved_work:
  change_review:
    diff_slice: [<minimum candidate comparison slice>]
    evidence_slice: [<minimum accepted and candidate evidence refs>]
    owner_slices: [<minimum owning-authority review/reconciliation inputs>]
```

Candidate mode is read-only with respect to accepted authority. Its diff, evidence, and owner slices are internal dependencies and do not populate `requested_work.capabilities`, select an otherwise unselected capability, or expand the request to the complete Review Suite. Candidate findings and source bindings are defined by their owning Change Review contracts; this routing shape does not make them accepted state.

### Change Review candidate execution mode

`CHANGE_REVIEW_CANDIDATE` is the execution mode for a configured `CHANGE_REVIEW`. Every owner output in this mode is candidate-qualified to its `CR-*` and exact base/candidate bindings. A candidate output may contain `CF-*`, `CRF-*`, capability assessment, existing-finding effect, or reconciliation input, but cannot write or revise accepted STM, Architecture, Code Quality, Test Engineering, Contract Verification/CC, Product, or projection authority.

Canonical writes are legal only inside an explicit, confirmation-gated `RECONCILE_CHANGE` dispatch to the existing owning authority. Completing, blocking, superseding, or retaining a candidate review is separate from the canonical lifecycle of every referenced fact, finding, test, compatibility, Product record, or projection.

### Bounded Change Inventory and delta discovery

`CHANGE_REVIEW` starts from the exact `BASE..CANDIDATE` bindings and performs bounded, diff-guided discovery:

```text
BASE..CANDIDATE diff
→ changed paths and evidence scope
→ bounded candidate discovery
→ ADDED | MODIFIED | REMOVED | MOVED inventory entries
→ correlate with accepted references
→ Change Assessment
```

A changed path starts discovery but proves nothing by itself. The coordinator inspects only the selected scope and the minimum evidence needed to identify a candidate surface. If a changed boundary references an uninspected material dependency, it records `CONTEXT_EXPANSION_REQUIRED`, names the missing slice, and expands only that evidence/dependency slice after resolving availability and authorization. Dynamic or unavailable source evidence is an explicit limitation, not an assertion of no change; full repository rediscovery is not the default.

Change Inventory is factual delta observation and remains separate from Change Assessment. In particular, a new candidate with no accepted edge is retained as candidate-only evidence, while a candidate removal never deletes an accepted STM fact or owner record before explicit reconciliation.

Persist bounded review completeness with the CR:

```text
review_completeness:
  change_inventory: COMPLETE | PARTIAL | UNKNOWN
  affected_authority_coverage: COMPLETE | PARTIAL | UNKNOWN
  candidate_discovery_coverage: COMPLETE | PARTIAL | UNKNOWN
  selected_capability_assessment: COMPLETE | PARTIAL | UNKNOWN
  unknown_impact: NONE | PRESENT
```

`COMPLETE` means complete for the frozen base, candidate, qualified scope, available evidence, and selected lenses only. It may coexist with `unknown_impact: PRESENT` and never claims exhaustive repository impact or that every semantic effect was found.

### Change Assessment and effect axes

Change Assessment is a separate, candidate-qualified interpretation of the immutable Change Inventory. It records:

```text
change_assessment:
  affected_existing_facts: [<accepted fact/revision refs>]
  candidate_facts: [<CR-*/CF-* refs>]
  removed_facts: [<accepted refs plus candidate removal refs>]
  existing_finding_effects: [<existing finding effect records>]
  candidate_findings: [<CR-*/CRF-* refs>]
  architecture_impact: <candidate-qualified interpretation or NONE>
  test_impact: <candidate-qualified assurance impact or NONE>
  contract_impact: <candidate-qualified contract impact or NONE>
  risk: <candidate-qualified risk interpretation or UNKNOWN>
  limitations: [<bounded limitations>]
```

Inventory change types remain `ADDED | MODIFIED | REMOVED | MOVED`. Assessment effects use this independent axis:

```text
INTRODUCES_RISK | WORSENS_EXISTING | MITIGATES |
POTENTIALLY_RESOLVES | NO_MATERIAL_IMPACT | UNKNOWN_IMPACT
```

Existing finding effects use exactly:

```text
UNAFFECTED | POTENTIALLY_RESOLVES | MITIGATES | WORSENS |
INVALIDATES_PRIOR_ASSUMPTION | UNKNOWN_IMPACT
```

Effect records are many-to-many and preserve the affected existing finding, candidate ref, evidence, and limitation. A `MODIFIED` candidate may therefore have `POTENTIALLY_RESOLVES` for one existing finding while another effect is `INTRODUCES_RISK`; one candidate may fix a HIGH existing issue and add a MEDIUM candidate issue. No effect is a lifecycle decision.

### Candidate projection-impact prediction

Change Review may record a prediction for projection impact, but prediction is not Stage B impact accounting. The prediction is qualified to the immutable `CR-*`, exact base binding, exact candidate binding, and selected scope:

```text
projection_prediction:
  review: CR-*
  base_binding: <exact CR base binding>
  candidate_binding: <exact CR candidate binding>
  scope: <frozen review scope/lenses>
  classification: NO_EXPECTED_IMPACT | LIKELY_AFFECTED |
                 DEFINITELY_AFFECTED_IF_ACCEPTED | UNKNOWN_IMPACT
  evidence: [<candidate assessment/evidence refs>]
  limitations: [<bounded limitations>]
```

`projection_prediction.classification` is the complete vocabulary. A candidate review cannot write `CURRENT`, `STALE`, or `BLOCKED`, cannot alter a `PRJ-*` freshness state, and cannot imply that regeneration occurred. Once owner reconciliation stabilizes accepted semantic state, the coordinator hands the accepted delta to the existing Projection Impact Analysis exactly once; that later actual result is not a rewrite of this prediction.

`RESOLVED`, `CLOSED`, and `ACCEPTED` may appear only as quoted state from an existing canonical owner record. They are not CRF outcomes. Every candidate owner record carries `candidate_origin: CR-*/CRF-*` traceability when it references a candidate finding or interpretation; promotion creates or links an owner-controlled canonical identity and never reuses the CRF identity.

### Review reuse and candidate evolution

Reuse is classified against the completed CR's immutable bindings, scope, lenses, and usable evidence. The classifier is:

```text
EXACT | TREE_EQUIVALENT | ADVANCED | DIVERGED | UNAVAILABLE
```

`EXACT` requires the same repository, exact candidate commit and tree, exact Project/Product qualification, a `COMPLETE` review, usable evidence, and compatible requested scope/lenses. `TREE_EQUIVALENT` requires a separate proof under one of the permitted levels in the shared evidence contract; a matching SHA alone is never sufficient.

An `ADVANCED` candidate is a supported continuation of the reviewed candidate. It creates a linked immutable incremental CR, for example `B→C` with `parent_review: CR-*`. The linked CR must persist `base_binding == parent_review.candidate_binding` and its `candidate_binding` must be the exact next source state after B (for example, C), with the transition evidence retained. It does not rewrite the prior CR. For reconciliation eligibility, the linked CR's `base_binding` must also equal the current accepted baseline binding, including repository, Project/Product/member qualification and source commit/tree/vector. A broken chain or any other base-binding inequality returns `REVIEW_BASELINE_MISMATCH`; it cannot dispatch reconciliation and must classify/review from the current accepted binding. `DIVERGED` means the candidate no longer safely represents the reviewed candidate and requires a new CR. `UNAVAILABLE` means the required relation or proof cannot be established. A completed CR's base, candidate, scope, and meaning are never rewritten.

No-ff merges and squash merges can reuse a completed review only after a `WHOLE_TREE_EQUAL` or `FROZEN_RELEVANT_SCOPE_EQUAL` proof. A conflict resolution that changes relevant content requires a supplemental or new CR. Partial cherry-pick reuse is conditional and requires independently decomposable subset proof covering omitted commits; otherwise bind a new CR.

Comparing candidates is a read-only view over immutable CR artifacts. It may show differences in effects, risks, migration impact, and unknowns, but it cannot adjudicate, accept, or create canonical semantic authority.

### Contextual `RECONCILE_CHANGE` owner dispatch

After a completed reusable CR passes exact `CR.base_binding ==` current accepted baseline binding, including repository, Project/Product/member qualification and source commit/tree/vector; the exact intended source-binding; usable evidence; bounded material-delta; and explicit-confirmation checks, the coordinator may expose contextual `RECONCILE_CHANGE`. A base-binding inequality returns `REVIEW_BASELINE_MISMATCH`; it does not dispatch reconciliation and must classify/review from the current accepted binding. Incomplete or non-reusable CRs are blocked from dispatch, and reconciliation is not a startup intent. Dispatch is owner-routed: `CF-*` goes to the Technical Model Gate; Architecture assessment goes to the Architecture authority; `CRF-*` and finding effects go to Code Quality; test impact goes to Test Engineering; provider/consumer contract impact goes to Contract Verification / CC; and Product composition uses existing Product semantics.

Each dispatch records the owner result and `candidate_origin` while retaining the candidate as review evidence. An owner may create or link a canonical record, but candidate identity is never reused as that owner identity.

The coordinator may emit `BASELINE_ADVANCE_ALLOWED` only after `CR.base_binding` still exactly equals the current accepted baseline binding, including repository, Project/Product/member qualification and source commit/tree/vector; the exact intended source binding is still current; all material delta is accounted for; required owner results are complete; required technical and coverage gates pass; and unknowns are handled by explicit policy. A base-binding inequality returns `REVIEW_BASELINE_MISMATCH`; do not emit the gate and classify/review from the current accepted binding. Partial reconciliation never completes the baseline, and open findings may remain only where existing policy allows. This gate is baseline bookkeeping and authority advancement, not release approval.

If the candidate commit/tree or qualified Project/Product/member vector changes before advancement, invalidate eligibility, reclassify reuse, and abandon pending dispatch. The completed CR remains immutable and the baseline does not advance.

`NEW` accepts capability-only, output-only, and mixed valid work only after the selected capability configuration and standalone-output selection pass `REQUESTED_WORK_CONFIGURATION_COMPLETE`. `USE_EXISTING` consumes only an accepted/current registered output; a missing or new output routes to `EXTEND`. `RESUME` restores persisted requested and resolved scope without silently adding work. `REVALIDATE` preserves requested work and revalidates only impacted slices. `EXTEND` is additive and reuses accepted/fresh dependencies. `PROJECTION_REPAIR` is presentation-only and escalates semantic drift to `SEMANTIC_DRIFT_DETECTED` plus `TECHNICAL_REVALIDATION_REQUIRED`.

Legacy records without standalone-output state read as an empty standalone output list. Existing capability selections, Architecture Endpoint state, Test Engineering output booleans, Product sessions, accepted `COMPLETE` packages, and old `RESUME` state remain readable. No historical package or `PRJ-*` identity is rewritten or silently enriched.

This file is the **authoritative source** for review-mode selection, endpoint selection, working-package structure, `working/INDEX.md`, workflow statuses, resume behavior, handoffs between agents, and progress presentation. Shared Technical Model semantics, factual authority, and the Technical Model Gate are defined in `shared-technical-model.md`.

Discovery Coverage semantics are defined in `discovery-coverage.md`; this file defines only their place in workflow state, artifacts, resume behavior, and revalidation. Factual STM domain coverage and the separate `TECHNICAL_MODEL_COVERAGE_ACCEPTED` gate are owned by `technical-model-coverage.md`. Direct STM/capability/projection dependency metadata, generated indexes, and impact semantics are owned by `technical-model-dependencies.md`. Gate-scoped projection freshness and named package membership are owned by [`projection-gates-and-packages.md`](projection-gates-and-packages.md).

## 1. Startup selection

Before substantive investigation, present a recommendation and two independent choices to the user.

### Depth

`STANDARD_FULL` — a complete evidence-first review with detailed factual architecture, thematic discovery, Discovery Coverage closeout, independent candidate verification, root-boundary review, and separate severity adjudication. Working artifacts are more compact than in forensic mode.

`FORENSIC` — maximum depth for complex, concurrent, security-sensitive, or disputed systems. Thematic areas are investigated in separate working passes, Discovery Coverage has an explicit independent gate, correction/refutation history is retained in greater detail, and gates are more visibly separated.

Both modes require `FULL` factual STM coverage before downstream use that requires the full model: `STANDARD_FULL` uses `COMPACT` depth and `FORENSIC` uses `FORENSIC` depth. Coverage/depth semantics, preservation of a single schema, and independent review belong to `technical-model-coverage.md`.

The Skill may recommend a mode, but must not silently choose `FORENSIC`.

### Endpoint

Depth does not determine endpoint automatically.

- `REVIEW_ONLY` — review plus authoritative findings ledger.
- `REVIEW_PLUS_TARGET_ARCHITECTURE` — review plus Target Architecture after the review is accepted.
- `REVIEW_PLUS_TARGET_AND_ROADMAP` — review plus Target Architecture plus remediation roadmap after preceding artifacts are accepted.

Do not add time estimates or labels such as “easy”, “hard”, or “maximum”.

## 2. Artifact package

Recommended root:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md          # when requested
├── 04-remediation-roadmap.md          # when requested
└── working/
    ├── README.md
    ├── INDEX.md
    └── ...
```

Follow the project's local review directory if the repository already has an established convention.

### STANDARD_FULL

```text
working/
├── README.md
├── INDEX.md
├── evidence/                         # shared WS-* worksets
├── technical-model/                  # persistent STM facts + coverage/review
├── 00-baseline-and-as-built-projection.md
├── 00a-as-built-projection-review.md
├── 01-discovery-and-scenarios.md
├── 01a-discovery-coverage-matrix.md
├── 01b-independent-coverage-review.md
├── 01c-coverage-correction.md       # conditional
├── 01d-coverage-re-review.md        # conditional
├── 02-independent-verification.md
├── 03-root-and-severity-adjudication.md
├── 04-target-consistency.md         # when needed
├── 05-roadmap-consistency.md        # when needed
└── 06-final-editorial-review.md
```

### FORENSIC

```text
working/
├── README.md
├── INDEX.md
├── evidence/                         # shared WS-* worksets
├── technical-model/                  # persistent STM facts + coverage/review
├── 00-baseline-as-built-projection.md
├── 00a-as-built-projection-review.md
├── 01-invariants-ownership-isolation.md
├── 02-lifecycle-cancellation-concurrency.md
├── 03-boundary-contracts.md
├── 04-frontend-state-events.md
├── 05-security-trust-boundaries.md
├── 06-maintainability-tests.md
├── 06a-discovery-coverage-matrix.md
├── 06b-independent-coverage-review.md
├── 06c-coverage-correction.md       # conditional
├── 06d-coverage-re-review.md        # conditional
├── 07-independent-verification.md
├── 08-root-boundary-adjudication.md
├── 09-severity-adjudication.md
├── 10-authoritative-compaction-check.md
├── 11-target-consistency-review.md
├── 11a-target-correction.md
├── 11b-target-re-review.md
├── 12-roadmap-execution-consistency.md
├── 12a-roadmap-correction.md
├── 12b-roadmap-re-review.md
├── 13-final-editorial-review.md
├── 13a-editorial-correction.md
└── 13b-final-editorial-re-review.md
```

Create conditional correction/re-review files only when the corresponding pass is actually required.

## 3. Authority map

Do not duplicate one normative contract across several locations.

| Concept | Authoritative source |
|---|---|
| mode / endpoint / workflow state / resume / subagent handoff | `review-modes-and-orchestration.md` |
| factual STM families / fact lifecycle / Technical Model Gate | `shared-technical-model.md` |
| STM factual domain coverage / mode projection / technical coverage review | `technical-model-coverage.md` |
| dependency/index semantics / impact traversal | `technical-model-dependencies.md` |
| shared evidence-first method | `review-method.md` |
| discovery coverage matrix / domains / coverage verdicts / coverage review | `discovery-coverage.md` |
| ownership / invariants / adversarial scenarios | `ownership-and-scenarios.md` |
| interaction / interpreter / resource / authority boundary dimensions | `boundary-contract-audit.md` |
| evidence / candidate lifecycle / severity / security attack chain | `evidence-and-severity.md` |
| independent candidate falsification | `independent-verification.md` |
| root / projection / SER split | `root-boundary-adjudication.md` |
| lifecycle diagrams | `lifecycle-and-mermaid.md` |
| final package / cross-links / writing | `report-contract.md` |
| target review | `target-architecture-review.md` |
| roadmap review | `remediation-roadmap-review.md` |
| editorial gate | `final-editorial-review.md` |
| projection packages / freshness gates | `projection-gates-and-packages.md` |

`SKILL.md` orchestrates these contracts and must not redefine them in detail.

## 4. `working/INDEX.md`

`INDEX.md` is the persistent source of workflow state. It must remain compact.

### Product mode coordinator state

Product mode is selected explicitly; it is not inferred from repository membership or a multi-repository path. When selected, `INDEX.md` records only the compact routing tuple below and references the owning Product records:

```text
product_context:
  product_mode: NONE | PRODUCT
  product_id: PROD-*
  selected_product_revision: <accepted Product revision>
  product_baseline_ref: <immutable Product baseline>
  membership_snapshot_ref: <immutable membership snapshot>
  baseline_coherency: COHERENT | MIXED_EXPLICIT | UNKNOWN
```

The coordinator pins the exact accepted Product revision and baseline for the session. Historical revisions, membership snapshots, and baselines remain addressable even when the Product identity's `current_revision` advances. Product revision is Product meaning/membership; Product baseline is the exact per-Project and external source vector reviewed by the session, not one Git SHA. The coherency value is independent of source availability, review coverage, semantic availability, projection freshness/availability, and package gate result.

For `product_mode: NONE`, the existing local session shape and artifact references remain valid and no synthetic one-member Product is created. `INDEX.md` remains coordinator routing authority only: Product semantic records, evidence, STM, findings, capability records, projections, and package gates remain owned by their existing contracts. Product Context Workflow authorization is separate from source-read authorization and dirty-admission authorization; membership grants no repository, semantic-write, test, code, worktree, commit, push, PR, or deployment permission.

### Frozen federated coordination state

When Product coordination is dispatched from a Coordination Root, the resume-critical coordinator state stores references to one immutable or superseding plan under the existing `working/INDEX.md` authority:

```text
coordination_plan_ref
selected_product_revision
membership_snapshot_ref
base_product_baseline_ref
selected child actions
child checkpoint refs
Product baseline candidate ref
limitations
```

On resume, reload the frozen plan and compare the current Product, member, and source context with it. A mismatch routes to bounded requalification or a new plan; it never mutates the old plan. The coordinator stores references rather than a second Product semantic record, and no Product root path, `HEAD`, `latest` audit, or convenience pointer retargets in-flight work.

### Product `REVALIDATE` and `EXTEND` routing

In Product mode, `REVALIDATE` starts from the pinned Product baseline and routes only the changed Project/source binding, its Project-local impact root, qualified direct dependencies, affected cross-project relations and capability records, and their Product outputs. It preserves accepted unaffected state and records `CONTEXT_EXPANSION_REQUIRED` when a material dependency is missing. `LOCAL`, `BOUNDARY`, and `SYSTEMIC` remain impact classifications; `SYSTEMIC` may recommend `FULL_REAUDIT_RECOMMENDED`, but it does not automatically execute a full Product review.

`EXTEND` adds only the requested Project, capability, cross-project investigation, output, or shared-resource context and the minimum dependency slice required for it. Removing or replacing a member, changing its role, or changing shared-resource meaning creates a new Product revision and receives explicit bounded impact adjudication. Historical Product revisions, baselines, and findings remain addressable; unrelated accepted Projects are not reopened.

These routes do not grant operations authority. Product Context Workflow, source-read, revision-selection, dirty-admission, semantic-write, projection, test, code, worktree, branch, commit, push, PR, and deployment authorization are separate decisions. No Product-wide status is inferred from a missing member, and no projection is regenerated implicitly.

### Session Orchestration coordinator state

Startup selection is owned by `references/session-orchestration.md`. Persist its compact coordinator routing state here, without turning it into substantive technical authority:

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
working_tree_snapshot_algorithm
review_suite
stack_addenda
product_context:
  product_mode: NONE | PRODUCT
  product_id
  selected_product_revision
  product_baseline_ref
  membership_snapshot_ref
  baseline_coherency: COHERENT | MIXED_EXPLICIT | UNKNOWN
project_profile:
  schema_version
  collector_version
  collected_for_revision
  status
  artifact_or_projection_ref
technical_model:
  owning_manifest
  model_revision
  baseline
  coverage_requirement
  depth_requirement
  coverage_status
  freshness
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

Absent v0.3 fields in a legacy package indicate legacy state requiring additive reconciliation/backfill, not automatic corruption. Validate owning-artifact freshness before using any projection downstream.

Session integration rules:

```text
USE_EXISTING → no technical stage transition solely for startup; metadata actions may update projection.
RESUME → with BASELINE_MATCH, reconstruct true workflow state and continue the first non-accepted gate; otherwise return SOURCE_BASELINE_MISMATCH and stop. Offer CHANGE_REVIEW or REVALIDATE and, only for a reusable completed review, contextual RECONCILE_CHANGE; none auto-runs.
REVALIDATE → delegate project-change evidence semantics to revalidation-and-freshness.md.
EXTEND → with BASELINE_MATCH, reuse the capability registry/minimal dependency slice without reopening unrelated accepted stages; otherwise return BASELINE_RECONCILIATION_REQUIRED and stop. Offer CHANGE_REVIEW or REVALIDATE and, only for a reusable completed review, contextual RECONCILE_CHANGE; none auto-runs.
NEW → enter existing full review flow with selected mode/endpoints/capabilities.
CHANGE_REVIEW → compare the accepted baseline with the selected candidate in read-only candidate mode; selected lenses and outputs remain requested work, and internal diff/evidence/owner slices remain resolved work.
RECONCILE_CHANGE (contextual action, not a startup intent) → after explicit confirmation, route a completed reusable review through its existing owning authorities.
PROJECTION_REPAIR → with BASELINE_MATCH, repair only selected presentation projections from unchanged accepted authority; otherwise block current repair until source reconciliation. Semantic drift returns to technical revalidation.
```

These rules consume the coordinator's deterministic intent matrix: an accepted package at A is always shown separately from current source B, and no intent may infer B from A. `USE_EXISTING` can consume A as current only on a matching binding; `NEW` starts an independently confirmed flow from B and never silently enriches A. `REVALIDATE` reevaluates accepted state against B, while a completed CR supplies routing evidence only and cannot satisfy the revalidation gate or bypass owner adjudication. `EXTEND` is additive only after an accepted matching B and never performs an implicit review-plus-reconcile-plus-extend chain. A mismatched `PROJECTION_REPAIR` is blocked as current repair; no historical-repair mode is created.

After `NEW`, `EXTEND`, or `REVALIDATE` reaches a stabilized semantic state, the coordinator performs one Projection Impact Analysis handoff and persists `PROJECTION_IMPACT_ACCOUNTED`. This is an accounting gate, not a regeneration command. A separately requested fresh deliverable starts an explicit `RG-*` session; `TARGETED` execution contains the requested projections and required stale upstream prerequisites, while downstream impact remains outside execution scope. `PROJECTION_REPAIR` does not use this path to carry semantic meaning or create persistent manual sections.

For a dependency-sliced capability dispatch, request the current semantic object, its HARD dependencies, unresolved CONDITIONAL dependencies, and required evidence. Resolve this bounded set through the generated indexes and owning direct metadata; do not preload unrelated accepted artifacts. The dependency contract owns the detailed traversal and impact rules.

For `NEW`, create the persistent STM manifest and this compact coordinator routing state before capability execution. The manifest, not `INDEX.md`, owns the model. Model creation does not require complete population: the selected downstream requirement determines the initially required factual slice. See `shared-technical-model.md` for fact authority and persistence.

Test Review methodology remains in `capabilities/test-review/SKILL.md`; startup visibility and selection remain in Session Orchestration.

Minimum sections:

1. repository path/ref/commit and initial dirty state;
2. selected capability configuration (Architecture `mode`/`endpoint` only when Architecture Review is selected);
3. current phase;
4. execution plan;
5. artifact registry;
6. candidate registry;
7. Positive Controls;
8. open questions;
9. architecture-correction candidates;
10. Discovery Coverage projection;
11. supersessions and corrections;
12. authoritative-document registry;
13. capability registry.

### Discovery Coverage coordinator summary

The complete matrix belongs to the `01a-...` or `06a-...` artifact. `INDEX.md` stores only the compact coordinator summary:

```text
coverage_artifact: working/<coverage-matrix-file>
coverage_review: <verdict>
baseline: <commit/ref>

domains:
  total: <n>
  covered: <n>
  not_applicable: <n>
  partial: <n>
  blocked: <n>

high_risk:
  applicable: <n>
  accepted: <n>
```

Before downstream use, the coordinator must verify freshness and revision binding of the owning coverage artifact and independent coverage review.

Only the coordinator edits `INDEX.md`. Thematic agents write their own files and persisted handoffs.

### Capability registry

`INDEX.md` records capability ownership and dependency freshness in a compact registry. The following statuses reuse the existing workflow state vocabulary:

```text
capabilities:
  - id: architecture-review
    selected: false
    configuration_status: UNRESOLVED | CONFIRMED   # present only when selected
    status: NOT_APPLICABLE | PENDING | IN_PROGRESS | REVIEW_REQUIRED | REVALIDATION_REQUIRED | BLOCKED | COMPLETE
    mode: STANDARD_FULL | FORENSIC        # present only when selected
    endpoint: REVIEW_ONLY | REVIEW_PLUS_TARGET_ARCHITECTURE | REVIEW_PLUS_TARGET_AND_ROADMAP  # present only when selected
    owning_artifact: <Architecture authority path>
    owning_artifact_revision: <revision>
    dependencies:
      - <artifact/ref + revision>
  - id: test-review
    selected: false
    configuration_status: UNRESOLVED | CONFIRMED   # present only when selected
    status: PENDING | IN_PROGRESS | REVIEW_REQUIRED | REVALIDATION_REQUIRED | BLOCKED | COMPLETE | NOT_APPLICABLE
    endpoint: REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN  # legacy Test Review input/projection
    outputs:
      test_assurance: true
      test_plan: false
      contract_consistency_report: false
      test_environment_design: false
      service_simulator_design: false
      service_simulator_implementation_plan: false
      e2e_test_plan: false
    owning_artifact: <path>
    owning_artifact_revision: <revision>
    dependencies:
      - <artifact/ref + revision>
  - id: code-quality-review
    selected: false
    configuration_status: UNRESOLVED | CONFIRMED   # present only when selected
    status: PENDING | IN_PROGRESS | REVIEW_REQUIRED | REVALIDATION_REQUIRED | BLOCKED | COMPLETE | NOT_APPLICABLE
    outputs:
      findings_view: false
      code_quality_summary: false
      maintainability_hotspots: false
      roadmap_contribution: false
    owning_artifact: <Code Quality semantic/session artifact path>
    owning_artifact_revision: <revision>
    dependencies:
      - <WS/EV/STM or related semantic ref + revision>
```

Architecture-specific persisted configuration is conditional:

```text
architecture-review.selected == true
  → mode is REQUIRED: STANDARD_FULL | FORENSIC
  → endpoint is REQUIRED: REVIEW_ONLY | REVIEW_PLUS_TARGET_ARCHITECTURE | REVIEW_PLUS_TARGET_AND_ROADMAP

architecture-review.selected == false
  → mode is ABSENT_BY_CONTRACT
  → endpoint is ABSENT_BY_CONTRACT
  → Architecture work is not enabled
```

`ARCHITECTURE_NOT_SELECTED` therefore implies `ARCHITECTURE_MODE_NOT_REQUIRED` and `ARCHITECTURE_ENDPOINT_NOT_REQUIRED`. The absence of Architecture mode/endpoint does not prevent a selected Test Engineering or Code Quality capability from resolving its own shared factual dependencies.

For Test Engineering, `outputs` is the persisted configuration authority; the fresh NEW menu represents each optional output as UNSPECIFIED until the user explicitly selects it or declines it as NOT_SELECTED. A false-valued registry example is not an explicit user decision. The legacy `endpoint` is retained only for backward-compatible Test Review packages and must not be used as the sole output selection or exposed as a current `NEW`/`EXTEND` menu option. `LEGACY_COMPATIBILITY_STATE` is not a `CURRENT_USER_MENU_OPTION`. When normalizing legacy state:

`NEW` writes the user's independent Test Engineering selection directly to `outputs`. `RESUME`, `EXTEND`, `USE_EXISTING`, and `REVALIDATE` read that persisted independent selection; `EXTEND` preserves accepted selected outputs and adds only explicitly requested outputs plus structurally required upstream dependencies. The legacy endpoint is not the primary `NEW` or `EXTEND` UI or source of truth.

```text
REVIEW_ONLY
  → test_assurance=true; every optional output=false

REVIEW_PLUS_TEST_PLAN
  → test_assurance=true; test_plan=true; every other optional output=false
```

Normalization is additive and conservative: it never infers an extended output. `test_assurance` is required when the capability is enabled. Behavior Model is an internal dependency and materially applicable Contract Verification is an automatic gate; neither is a persisted user-selected output.

Test Review may be selected initially, recommended from a discovered material test surface, or attached to an existing audit. Later attachment resumes from `INDEX`:

```text
resume INDEX
→ verify baseline/freshness
→ register capability
→ determine minimal accepted dependency slice
→ execute capability-owned pass
→ capability review/adjudication
→ reconcile cross-capability findings/corrections
→ targeted revalidation only for affected dependencies
```

Adding a capability does not restart unrelated accepted stages by default. A stale or disputed dependency blocks downstream use under the freshness contract.

For the Test Engineering extension, the capability registry may project these separate outputs and their owning artifacts:

```text
00-test-assurance-summary.md
01-test-assurance-map.md
02-test-plan.md                              # optional compatibility output
03-behavior-contract-model.md                # when extended model is required
04-contract-consistency-report.md            # optional projection
05-test-environment-design.md                # optional
06-service-simulator-spec.md                 # optional
07-service-simulator-implementation-plan.md  # optional
08-e2e-test-plan.md                          # optional
working/                                     # authoritative BC/CC/TM/GAP ledgers
```

The registry stores output selection as the independent `outputs` fields above. For `EXTEND`, the coordinator first separates accepted/fresh selected outputs from available additions, then persists the union of the existing selection and the requested additions. It explains any structurally required dependency addition before execution. An E2E Test Plan requires Test Assurance, the internal Behavior Model, applicable Contract Verification, and E2E Design; Service Simulator Design is added only when the selected topology requires it. A Service Simulator Implementation Plan requires an accepted and fresh simulator specification, so a missing simulator design is the minimum upstream addition for that request. `EXTEND` reuses the accepted upstream slice instead of replaying the full review.

The same `EXTEND` presentation rule applies to every capability: existing capabilities and outputs are shown read-only for context, while only unselected capabilities and outputs are offered as additions. For Architecture Review, adding an absent capability opens its normal depth/endpoint configuration; extending an accepted capability preserves depth and offers only monotonic endpoint additions. No accepted capability or output is silently removed or reconfigured.

Capability-owned artifacts may use project-local paths, for example:

```text
capabilities/test-review/01-test-assurance-map.md
capabilities/test-review/02-test-plan.md
working/capabilities/test-review/...
```

The `INDEX` ownership and revision binding are the invariant, not the exact paths.

For Code Quality Review, the `outputs` fields are independent coordinator selection state, not semantic authority and not Stage B projection records. Fresh NEW state keeps each output UNSPECIFIED until explicit selection or decline; zero selected outputs is valid only after `configuration_status` is CONFIRMED by the user. Each listed Code Quality output is both `USER_SELECTABLE` and a `DERIVED_PROJECTION`: it is derived from accepted CQ authority, but it is not implicitly selected, mandatory, or always generated. `Code Quality Summary`, `Maintainability Hotspots`, and `Roadmap Contribution` are selected only when requested or structurally required by a selected output. Package membership is resolved later as explicit selection plus dependency closure under the shared Stage B package policies; this registry does not register `PRJ-*` records.

Code Quality session state keeps the qualified coverage reference alongside the capability entry. The owning Code Quality assessment/session state records `COMPLETE`, `PARTIAL`, or `BLOCKED` coverage and its requested, reviewable, excluded, unavailable, unsupported, dirty/noncanonical, limitation, and affected-claim context. A partial or blocked slice qualifies aggregate claims but does not invalidate unrelated accepted CQ findings whose dependencies remain sufficient.

For the Code Quality capability, coordinator transitions are:

```text
NEW
  → register independent CQ selection and selected outputs
  → persist scope, semantic references, coverage reference, and blockers

EXTEND
  → preserve accepted upstream capabilities and shared evidence/STM
  → add only the requested CQ scope and outputs

RESUME
  → verify baseline and persisted revisions
  → restore CQ selection, scope, outputs, blockers, handoff, and coverage reference
  → continue from the first non-accepted durable boundary
```

`RESUME` does not restart the full review, become `NEW`, or become automatic `REVALIDATE`; it never reconstructs workflow state from chat or prose memory. `working/INDEX.md` stores only this coordinator routing state and references the owning Code Quality semantic artifacts. It is not CQ semantic authority.

Code Quality participates in the existing `REVALIDATE` intent, but the impact-driven CQ freshness and semantic revalidation contract is implemented by the Code Quality revalidation contract in `references/revalidation-and-freshness.md`. This section preserves the routing/dependency boundary. Missing or stale shared evidence/STM blocks only the dependent CQ slice and does not rewrite shared facts or invalidate unrelated findings.

## 5. Statuses

Common artifact/stage statuses:

```text
PENDING
IN_PROGRESS
ARTIFACT_WRITTEN
REVIEW_REQUIRED
CORRECTION_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
COMPLETE
NOT_APPLICABLE
```

Coverage-row states and coverage-review verdicts belong to `discovery-coverage.md` and do not replace the common lifecycle status.

`ARTIFACT_WRITTEN` means only that the artifact was written. For an artifact with mandatory review, the next status is `REVIEW_REQUIRED`, not `COMPLETE`.

Typical lifecycle:

```text
PENDING
→ IN_PROGRESS
→ ARTIFACT_WRITTEN
→ REVIEW_REQUIRED
→ COMPLETE
```

When review finds issues:

```text
REVIEW_REQUIRED
→ CORRECTION_REQUIRED
→ IN_PROGRESS
→ ARTIFACT_WRITTEN
→ REVIEW_REQUIRED
→ COMPLETE | BLOCKED
```

Coverage-specific semantic loop:

```text
Discovery artifacts COMPLETE
→ Coverage Matrix closeout
→ Independent Coverage Review
→ COVERAGE_ACCEPTED
```

On a coverage gap:

```text
COVERAGE_CORRECTION_REQUIRED
→ targeted coverage correction
→ matrix update
→ impacted-domain coverage re-review
→ COVERAGE_ACCEPTED | COVERAGE_BLOCKED
```

`COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT`, and `COVERAGE_CORRECTION_REQUIRED` cannot be projected as `COMPLETE` for downstream candidate verification.

After a confirmed As-Built correction:

```text
COMPLETE
→ impact scan
→ affected technical/coverage stages REVALIDATION_REQUIRED
→ IN_PROGRESS
→ ARTIFACT_WRITTEN/REVIEW_REQUIRED
→ COMPLETE | CORRECTION_REQUIRED | BLOCKED
```

`REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED`, and `BLOCKED` **are not accepted authoritative input** for dependent downstream stages.

## 6. Persisted handoff

No state required for resume may exist only in chat.

Every agent-owned working artifact ends with a strictly structured section:

```markdown
## HANDOFF SUMMARY

status: ARTIFACT_WRITTEN
baseline: <commit/ref>
artifact: <relative path>
new_candidates:
- ...
positive_controls:
- ...
open_questions:
- ...
architecture_correction_candidates:
- ...
supersedes:
- ...
```

Coverage artifacts additionally reference the owning matrix/review baseline and affected domains when the pass is a correction or re-review.

`none` is allowed, but every field must be present.

Safe ordering:

```text
write complete artifact
→ verify required headings/content
→ persist HANDOFF SUMMARY inside artifact
→ coordinator validates baseline + artifact path
→ coordinator updates INDEX
→ stage may advance
```

If a file exists but `INDEX.md` was not updated because a response or context was lost:

```text
read persisted HANDOFF SUMMARY
→ validate artifact identity and baseline
→ reconcile INDEX
→ continue
```

## 7. Visible execution plan

The user must be able to see the current plan and status of a long-running review.

`INDEX.md` is always persistent authority. Any native Todo/task/plan UI is only a **non-authoritative projection** of that state.

- If the host provides a native todo/task/plan **tool**, the coordinator must **actually invoke that tool** to create and subsequently update the visible plan. Merely editing `INDEX.md`, writing prose such as “plan synchronized”, or relying on internal reasoning does not synchronize the UI.
- If no native tool exists, show a compact text plan in the CLI or chat.

### Native Plan Projection Sync Contract

After every **material coordinator state transition**, this order is mandatory:

```text
validate completed artifact / persisted handoff
→ update working/INDEX.md
→ call the native todo/task/plan tool with the current projection, if available
→ only then advance/dispatch the next visible phase
```

Material transitions include:

- any tracked-stage change among `PENDING`, `IN_PROGRESS`, `ARTIFACT_WRITTEN`, `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED`, `BLOCKED`, `COMPLETE`, and `NOT_APPLICABLE`;
- a coverage-review verdict change that opens or closes a downstream gate;
- a change of active top-level phase;
- completion of a subagent batch after its persisted handoffs are validated and reflected in `INDEX.md`;
- an accepted architecture correction followed by setting dependent stages or domains to `REVALIDATION_REQUIRED`.

During initial setup, if a native tool is available, call it immediately after creating and populating `INDEX.md`.

On resume, the required order is:

```text
read INDEX
→ verify/reconcile persisted artifacts and handoffs
→ validate coverage matrix/review baseline binding
→ reconstruct true workflow state
→ call native todo/task/plan tool with that reconstructed state, if available
→ identify first non-accepted gate
→ continue
```

If the host tool has a specific name such as `todowrite`, use the actual runtime tool that is available. Do not bind the Skill to one vendor name: the requirement is **actual tool invocation**, not a particular API name.

Do not update native UI after every microscopic tool call, file read, shell command, or internal reasoning step. The goal is an accurate coarse-grained projection, not a noisy progress ticker.

If the native plan diverges from `INDEX.md`, that is `NATIVE_PLAN_DRIFT`. Do not trust the UI and do not rerun accepted work. Restore the projection from `INDEX.md` by actually invoking the native tool, then continue from the first genuinely non-accepted gate.

Example:

```text
[✓] Factual architecture — COMPLETE
[✓] Thematic discovery — COMPLETE
[!] Discovery Coverage — COVERAGE_CORRECTION_REQUIRED
[ ] Independent Candidate Verification — PENDING
```

The plan is dynamic: accepted architecture corrections and coverage-review gaps may add targeted correction, impact, or revalidation stages. Do not restart the whole review when the impact scan shows only local impact.

## 8. Subagents and stability

### Context Orchestration v0.3

Capability dispatch uses the minimum fresh authoritative context needed for the current decision. Start with structure/inventory, then materiality and evidence pointers, then targeted reads; deepen only for unresolved material questions.

The dispatch envelope contains exact baseline/revision, mission and narrow scope, forbidden scope, accepted dependency artifact pointers with revisions, required shared/reference contracts, output path, and the `HANDOFF SUMMARY` contract. Routing projections select reads but cannot replace owning decision evidence. Unrelated accepted artifacts are not preloaded. A material omission or boundary discovered outside the initial slice is a recorded `CONTEXT_EXPANSION_REQUIRED`, not a blindfold or an unbounded restart.

Subagents are a context-isolation mechanism, not only a speed optimization.

Every substantial agent receives:

- exact baseline;
- mode/endpoint;
- `INDEX.md`;
- accepted/fresh required STM factual slice and its coverage/revision binding;
- As-Built projection only when its human-readable context is useful, never as factual authority;
- narrow scope;
- forbidden scope;
- its own output path;
- `HANDOFF SUMMARY` contract.

The Technical Model Coverage Reviewer receives a bounded STM factual packet, the owning technical coverage matrix, and baseline/revision binding. The Architecture Coverage Reviewer receives the accepted/fresh required STM slice, Architecture Discovery Coverage matrix, thematic artifact registry, candidate/PC/OQ registries, and baseline binding. Neither reviewer receives predecessor reasoning or As-Built prose as factual authority.

One file has one active writer. Parallel agents do not edit the same file.

Run Baseline/session orchestration first, then required Shared Evidence/STM build, then the independent STM coverage/review gate, and accept the required full STM. Only after that may Architecture thematic passes start. The As-Built projection is assembled from accepted/fresh STM and receives parity/projection review; it never replaces the factual gate.

After thematic discovery, the required order is:

```text
discovery artifacts complete
→ coverage matrix closeout
→ Independent Coverage Review
→ targeted correction/re-review if needed
→ COVERAGE_ACCEPTED
→ candidate verification
```

Parallelism is bounded and adaptive. When uncertain, execute sequentially. Stability comes first.

## 9. Factual reconciliation and Architecture correction

A thematic agent does not modify STM or the As-Built projection directly. A factual contradiction creates `TECH_FACT_CONFLICT`; a new fact creates `TECH_FACT_CANDIDATE`; a stale or impact-affected fact creates `TECH_FACT_REVALIDATION_REQUEST`. The request records the current STM fact/revision, contradiction or candidate, evidence, expected impact, and affected technical domains or projections.

A separate fresh-context reviewer returns one of:

```text
CONFIRMED_CORRECTION
REFUTED_CORRECTION
PARTIALLY_CORRECT
INSUFFICIENT_EVIDENCE
```

The Technical Model Gate confirms, rejects, or revises the factual STM artifact and then runs impact analysis. Architecture Review may continue only within unaffected scope; a disputed required fact is not accepted downstream input.

The impact scan must include Discovery Coverage:

```text
confirmed STM change
→ determine affected technical and architecture coverage domains
→ only affected accepted rows/stages become REVALIDATION_REQUIRED
```

Do not reset unrelated accepted coverage without concrete impact.

`ARCH-CORRECTION-CANDIDATE` remains the mechanism for correcting an Architecture-owned invariant, adverse-scenario or race interpretation, finding/root/severity, or remediation implication. It is not a factual correction record and does not modify STM owner/writer/boundary inventory.

## 10. Candidate verification gate

Independent candidate verification is allowed only when:

```text
DISCOVERY_COMPLETE
AND
COVERAGE_ACCEPTED
```

The following states block progression:

```text
PARTIALLY_COVERED
BLOCKED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
REVALIDATION_REQUIRED on material affected coverage
```

Coverage Review does not verify correctness of each candidate; candidate verification is not a substitute for coverage review.

## 10a. Technical Model Coverage precondition

For a full Architecture Review, `TECHNICAL_MODEL_COVERAGE_ACCEPTED` from `technical-model-coverage.md` is required before Architecture thematic discovery or another capability that needs the complete factual substrate. `PARTIAL`, `BLOCKED`, or `UNKNOWN` material technical-domain rows block that transition; a prose reviewer verdict cannot override them. This is separate from the later Architecture Discovery Coverage gate above.

## 11. As-Built projection authority

Accepted/fresh required STM is **technical factual authority**. The controlled working As-Built (`00-...as-built-projection.md`) is a substantial human-readable projection of accepted/fresh STM plus architecture-oriented synthesis, not a second technical source of truth.

`01-architecture-review.md` contains the user-facing projection of factual STM and renders Architecture Review authority from named upstream semantic owners; it is not the sole persistence location of that authority. If STM revision/coverage or a projection selector changes after assembly, dependent sections are stale until synthesis and review are repeated. `PROJECTION_REPAIR` repairs only presentation derived from unchanged accepted authority; semantic drift requires technical revalidation.

Technical Model Coverage Review is mandatory in both modes; in `STANDARD_FULL`, its evidence depth may be compact. As-Built parity/projection review is also mandatory but does not accept factual STM.

Projection-sensitive capability or endpoint closeout uses the named package and policy in [`projection-gates-and-packages.md`](projection-gates-and-packages.md). After semantic gates are accepted, the coordinator must persist `PROJECTION_IMPACT_ACCOUNTED`, resolve package membership, and enforce the package's required scoped projections before permitting closeout or publication. Unrelated stale projections remain visible but do not block an unrelated gate; the coordinator must not apply a repository-wide zero-stale rule.

The same closeout rule applies to `NEW`, `EXTEND`, and `REVALIDATE`: semantic gates stabilize first, impact is accounted once, and only the resolved package scope is freshness-gated. `PERMISSIVE` permits semantic closeout with deferred stale projections; `REQUIRED_SCOPE_CURRENT` and `ALL_SCOPED_CURRENT` block only when their resolved required scope is non-current. The closeout gate never implicitly invokes regeneration.

## 12. Recovery

In a new session:

```text
read INDEX
→ verify baseline and referenced artifacts
→ reconcile any persisted handoff not reflected in INDEX
→ validate STM facts, technical coverage, Architecture coverage and projection baseline/revision bindings
→ reconstruct true workflow state
→ call native todo/task/plan tool with reconstructed state, if available
→ identify first non-accepted required gate
→ continue
```

If `INDEX.md` claims accepted coverage while the owning technical or Architecture matrix/review is stale, missing, or bound to another STM revision or baseline, do not trust the compact projection. Apply the freshness/reconciliation contract and return the corresponding coverage stage to a non-accepted state.

Do not rely on memory from a previous chat and do not use stale native UI as authority.