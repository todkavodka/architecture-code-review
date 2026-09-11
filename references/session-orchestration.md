# Session Orchestration v0.3

This reference is the sole authority for startup/session orchestration.

## Requested-work startup routing

The coordinator confirms requested work separately from the internal dependency
plan. The only selectable semantic capabilities remain `Architecture Review`,
`Test Engineering`, and `Code Quality Review`. A valid session has at least one
selected capability or at least one valid standalone output. Zero capabilities
and zero outputs returns `NO_REVIEW_SCOPE_SELECTED`; Product context alone is
not requested work.

The canonical startup layers are:

```text
Session Intent
Scope Context
Baseline Relation
Contextual Available Actions
Requested Work
Capability/Output Configuration
Dependency Resolution
Authorization Summary
Substantive Work
```

Persist the routing record as:

```text
requested_work:
  capabilities: [<canonical capability ids>]
  standalone_outputs: [<canonical output ids>]
  scope: PROJECT | PRODUCT
  confirmation_status: CANDIDATE | CONFIRMED

capability_configuration:
  architecture:
    configuration_status: UNRESOLVED | CONFIRMED
    depth: STANDARD_FULL | FORENSIC
    endpoint: REVIEW_ONLY | REVIEW_PLUS_TARGET_ARCHITECTURE | REVIEW_PLUS_TARGET_AND_ROADMAP
  test_engineering:
    configuration_status: UNRESOLVED | CONFIRMED
    outputs: <required Test Assurance plus resolved optional selections>
  code_quality:
    configuration_status: UNRESOLVED | CONFIRMED
    outputs: <resolved independent projection selections>

standalone_output_configuration:
  status: UNRESOLVED | CONFIRMED
  selection: [<canonical standalone output ids>]
  explicit_none: true | false
```

Internal STM, Evidence, Behavior Model, Contract Verification, Product
qualification, and projection prerequisites belong to `resolved_work`; they
never populate `requested_work.capabilities`.

Natural-language input is a candidate normalization only. Use the exact
classes `EXACT`, `BOUNDED_BUT_MULTI_OUTPUT`, and `AMBIGUOUS_BROAD`. Exact
outputs remain bounded; broad Technical Documentation requires explicit
subsection confirmation. A materially ambiguous request with no confirmed
selection returns `REQUESTED_OUTPUT_AMBIGUOUS` and presents alternatives.

### Explicit-selection conflict reconciliation

An explicit confirmed user selection has precedence over an inferred
natural-language normalization, but material contradiction must not be silently
overwritten. When inferred work conflicts with an explicit confirmed selection,
the coordinator identifies both choices, emits `REQUESTED_WORK_CONFLICT`, shows
the conflict, and requires confirmation of the resulting `requested_work`
before persistence or substantive work. It does not silently change the
explicit selection and does not start substantive work while unresolved.

Examples:

| Explicit confirmed selection | Inferred/requested wording | Required route |
|---|---|---|
| Architecture Endpoint = `REVIEW_ONLY` | “also build Target Architecture” | `REQUESTED_WORK_CONFLICT`; show `REVIEW_ONLY` and the inferred target endpoint; reconcile and confirm. |
| `REVIEW_PLUS_TARGET_ARCHITECTURE` | “do not generate Target Architecture” | `REQUESTED_WORK_CONFLICT`; show both choices and confirm resulting `requested_work`. |
| External Integrations Catalog only | “make all technical documentation” | Do not expand confirmed requested work; reconcile and confirm any broader scope. |

Product context with no requested work is `NO_REVIEW_SCOPE_SELECTED`, not
`REQUESTED_WORK_CONFLICT`. A resolved internal dependency differing from a
user-selected capability is also not conflict: preserve
`requested_work != resolved_work`.

## Coordinator workflow authority boundary

`working/INDEX.md` is the explicit `COORDINATOR_WORKFLOW_AUTHORITY`. It owns
resume-critical session, gate, handoff, and coordinator routing state under the
Stage A workflow. Only the coordinator updates that authority through the
workflow reconciliation rules; its meaning is not reconstructed from a
projection view.

The authoritative `working/INDEX.md` is excluded from every Stage B projection
mechanic. It is never classified as `PRJ-*`, fingerprinted for projection
drift, regenerated, retired, assigned projection freshness, or given `RG-*`
execution/session state. Projection Impact Analysis must not overwrite its
gate state, resume routing, or handoff/coordinator state. A filename containing
`INDEX` does not change this boundary.

Stage B operational views are separate, non-authoritative records under
`working/projections/`:

```text
working/projections/registry.md       # generated active projection registry view
working/projections/impact.md         # generated impact-accounting view
working/projections/sessions/RG-*.md  # one frozen regeneration session view
```

These views are scoped projections of their owning lifecycle, impact, or
regeneration records. They are reconstructable and disposable, must not reuse
the path or identity of `working/INDEX.md`, and cannot be used to mutate or
replace coordinator authority. The focused Stage B references define their
record contents; this startup contract defines only the authority boundary.

## Ownership

Owns:

- repository identity and previous-audit discovery/usability;
- lineage-aware source-audit selection;
- Session Intent recommendation and selection;
- Review Suite startup configuration;
- Project Profile lifecycle, migration, and backfill;
- dirty-working-tree baseline choice.

Does not own:

- execution-stage lifecycle or capability registry mechanics (`review-modes-and-orchestration.md`);
- substantive freshness or project-change decision evidence (`revalidation-and-freshness.md`);
- specialist Test Review methodology (`capabilities/test-review/SKILL.md`).

Startup is routing and metadata work, not a blanket repository read:

```text
START
→ repository identity
→ discover previous audit packages
→ validate usability/lineage
→ establish committed baseline + dirty state
→ reuse/refresh/backfill Project Profile
→ recommend/select Session Intent
→ context-sensitive Review Suite Configuration
→ for NEW, persistent STM baseline bootstrap
→ persist/reconcile INDEX
→ substantive workflow
```

Do not inspect every project file in the model context merely to route a session.

## Repository identity and previous audits

Record a stable repository identity from the repository root and canonical remote identity where available. Discover candidate audit packages without selecting by file timestamp alone. For each candidate validate:

- repository identity;
- readable `INDEX.md` and persisted handoffs;
- known previous baseline and current source-audit revision;
- coherent authority/status/revision bindings;
- lineage suitability, including ancestor/descendant relation to the selected baseline.

An unsafe or ambiguous package yields `PREVIOUS_AUDIT_RECONCILIATION_REQUIRED`; stale compact state is not downstream authority. When multiple valid packages compete, rank identity, authority state, and lineage before recency and show the competing choices when user intent remains ambiguous.

## Session Intent

Persist exactly these seven intents:

```text
USE_EXISTING | NEW | RESUME | REVALIDATE | EXTEND | CHANGE_REVIEW |
PROJECTION_REPAIR
```

`CHANGE_REVIEW` is a startup orchestration intent, not a semantic capability.
It compares an accepted baseline with an explicitly selected candidate source,
then performs only the user-confirmed review lenses and outputs in read-only
candidate mode. It does not select a capability, mutate accepted authority, or
promote a candidate. `RECONCILE_CHANGE` is not a startup intent: it is a
contextual action available only for a completed reusable review and after
explicit confirmation.

### Baseline relation and mismatch routing

After Session Intent and Scope Context, the coordinator compares the accepted
Project baseline (or exact Product member baseline vector) with the intended
source and records exactly one routing relation:

```text
BASELINE_MATCH | BASELINE_ADVANCED | BASELINE_DIVERGED | BASELINE_UNKNOWN
```

`BASELINE_MATCH` permits normal `RESUME`, `EXTEND`, and current
`PROJECTION_REPAIR`. `BASELINE_ADVANCED` records a descendant or other advance
from the accepted binding; `BASELINE_DIVERGED` records that no safe linear
relation was established; `BASELINE_UNKNOWN` records an unavailable source or
relation. These are routing metadata only: none marks STM or a projection
stale, resolves a finding, or proves semantic change.

For any non-match, Contextual Available Actions show Change Review and/or
Revalidate, plus `RECONCILE_CHANGE` only when a reusable completed review is
available. They never invoke review, revalidation, or reconciliation
automatically:

- `RESUME` returns `SOURCE_BASELINE_MISMATCH` and does not continue as current.
- `EXTEND` returns `BASELINE_RECONCILIATION_REQUIRED`; it cannot add work as if
  accepted semantics described the candidate source.
- Current `PROJECTION_REPAIR` is blocked until source reconciliation; it does
  not repair a current representation against a mismatched source baseline.

`USE_EXISTING` may present the accepted package as historical context, but
must show it separately from the candidate and cannot treat it as current.
`NEW` remains independently available. Where no accepted baseline exists,
`CHANGE_REVIEW` may compare two authorized sources without creating accepted
semantic state.

### Reuse and candidate-update routing

When a completed Change Review is considered for contextual reuse, route the
candidate through the classifier and proof contract owned by the Change Review
artifacts. `EXACT` or proven `TREE_EQUIVALENT` may expose contextual
`RECONCILE_CHANGE` only after the existing completion, evidence, qualification,
and scope checks. `ADVANCED` creates a linked incremental review for the next
candidate; `DIVERGED` or `UNAVAILABLE` requires a new review or an explicit
limitation. A completed CR is never rewritten to change its source meaning.

No-ff, squash, and partial cherry-pick cases do not bypass proof. Candidate
comparison remains a read-only view over immutable CRs. In Product mode, a
changed member vector, selected Product revision, or member qualification
rejects reuse even when source text or tree appears equal.

### Contextual reconciliation and baseline advancement

`RECONCILE_CHANGE` is eligible only when the completed CR is reusable
(`EXACT`, `TREE_EQUIVALENT`, or a supported `ADVANCED` continuation), its
candidate binding is the exact intended source binding, its evidence is usable,
the bounded material-delta accounting is complete, and the user explicitly
confirms the action. An incomplete or non-reusable CR cannot dispatch. This is
a contextual action after `CHANGE_REVIEW`, never a startup intent.

Dispatch only the minimum candidate slices to their existing owners:

| Candidate input | Owner | Required record |
|---|---|---|
| `CF-*` technical facts | Technical Model Gate | owner result and `candidate_origin` |
| Architecture assessment | Architecture authority | owner result and `candidate_origin` |
| `CRF-*` and existing-finding effects | Code Quality authority | owner result and `candidate_origin` |
| test impact | Test Engineering | owner result and `candidate_origin` |
| provider/consumer contract impact | Contract Verification / CC | owner result and `candidate_origin` |
| Product composition | existing Product semantics | owner result and `candidate_origin` |

`candidate_origin` remains the originating `CR-*`/`CRF-*` traceability value;
the owner result records the owner-controlled disposition and any new
canonical reference. Reconciliation never reuses a candidate identity as an
accepted owner identity.

Baseline advancement is a separate coordinator gate:

```text
BASELINE_ADVANCE_ALLOWED
```

The gate requires the exact intended source binding, all material delta
accounted for, required owners complete, required technical and coverage
gates satisfied, and unknowns handled by an explicit applicable policy. The
gate is not release, merge, or deployment approval. partial reconciliation
never completes the baseline; open findings may remain when existing policy
allows them, but every such finding remains explicitly accounted for.

Before this gate is accepted, compare the candidate commit/tree and qualified
Project/Product/member vector with the bound candidate. If any changes, discard
reconciliation eligibility and classify reuse again; do not mutate the CR or
advance the baseline.

The recommendation matrix is:

| State | Recommendation |
|---|---|
| no previous audit | `NEW` |
| `IN_PROGRESS` + same baseline | `RESUME` |
| `IN_PROGRESS` + changed baseline | `SOURCE_BASELINE_MISMATCH`; offer contextual review/revalidation/reconciliation |
| `COMPLETE` + same committed baseline, consume accepted result | `USE_EXISTING` |
| `COMPLETE` + same committed baseline, repair only final/user-facing documents | `PROJECTION_REPAIR` |
| `COMPLETE` + changed committed baseline | offer `CHANGE_REVIEW` or `REVALIDATE` |
| new assurance scope/capability/endpoint with changed baseline | `BASELINE_RECONCILIATION_REQUIRED` before `EXTEND` |
| new assurance scope/capability/endpoint with matching baseline | `EXTEND` |

`RESUME_WITH_RECONCILIATION` is a flow/recommendation under `RESUME`, never a separate persisted intent. Explicit `NEW` remains available in every reusable case.

`USE_EXISTING` performs no technical stage transition solely for startup. It may run metadata-only actions. `REVALIDATE` delegates impact and fresh-evidence semantics to `revalidation-and-freshness.md`; it does not imply a full audit. `EXTEND` adds only the requested assurance scope and does not reopen unrelated accepted stages.

`PROJECTION_REPAIR` is a bounded repair intent for accepted final/user-facing projections. It is not a project-change audit and is not a substitute for `REVALIDATE` when source/baseline changes may affect accepted semantics. It requires reusable accepted technical authority and delegates the repair/re-review boundary to `PROJECTION_REVALIDATION` in `revalidation-and-freshness.md`.

### Deterministic existing-intent routing

For every intent, the coordinator presents the accepted baseline as A and the
selected/current source as B when both exist. A package accepted at A is
historical context only; current B is established from its own exact source
binding and is never inferred from package A, a projection, or compact state.

The routing decision is deterministic:

| Intent | `BASELINE_MATCH` | `BASELINE_ADVANCED`, `BASELINE_DIVERGED`, or `BASELINE_UNKNOWN` |
|---|---|---|
| `USE_EXISTING` | consume the accepted A package as current | show A as historical and B separately; do not treat A as current; `NEW`, `CHANGE_REVIEW`, or `REVALIDATE` remain explicit alternatives |
| `RESUME` | restore and continue the first non-accepted gate | return `SOURCE_BASELINE_MISMATCH` and stop; offer `CHANGE_REVIEW`, `REVALIDATE`, and contextual `RECONCILE_CHANGE` only when reusable; none runs automatically |
| `REVALIDATE` | reevaluate accepted state only where applicable | bind A to B and perform accepted-state impact/revalidation; a CR is routing evidence only and cannot satisfy its revalidation gate |
| `EXTEND` | perform only the confirmed additive request | return `BASELINE_RECONCILIATION_REQUIRED` and stop; no implicit review-plus-reconcile-plus-extend chain |
| `PROJECTION_REPAIR` | repair only selected projections from unchanged accepted authority | block current repair until source reconciliation; do not create a historical-repair mode |
| `NEW` | start an independently confirmed new flow | start from B with independently confirmed scope/configuration; never enrich or silently continue A |
| `CHANGE_REVIEW` | compare explicitly selected sources in candidate mode | compare explicitly selected A/B sources in candidate mode; it does not promote B |

`RECONCILE_CHANGE` remains a contextual action after a completed reusable
Change Review, not a startup intent. It cannot be inserted automatically into
any row above, and it cannot make a changed source appear matched.

## Product context selection and pinning

Product mode is explicit and opt-in. A normal session remains Product-free;
the coordinator does not synthesize a one-member Product from a repository or
Project. Composition semantics are owned by
[`product-multi-project-review.md`](product-multi-project-review.md), while
this contract owns session routing and selection.

When Product mode is selected, the coordinator records this routing tuple:

```text
product_mode: PRODUCT
product_id: PROD-*
selected_product_revision: <accepted Product revision>
product_baseline_ref: <immutable Product baseline>
membership_snapshot_ref: <immutable membership snapshot>
```

`selected_product_revision` must resolve to an accepted historical Product
revision and is pinned for the session; the Product identity's convenience
`current_revision` pointer cannot retarget an in-progress or historical
session. The Product revision and Product baseline are distinct: the revision
records accepted Product meaning and membership, while the baseline binds the
exact source vector reviewed by that session. Product scopes, Product
semantic records, projections, and packages require that accepted revision
and exact baseline reference.

The coordinator verifies that the referenced membership snapshot and baseline
remain immutable and addressable before resume or downstream dispatch. A
baseline is a vector of per-Project and external source bindings, never one
Git SHA. Its coherency classification is `COHERENT`, `MIXED_EXPLICIT`, or
`UNKNOWN`; that classification describes temporal/source coordination only,
not availability, review coverage, semantic availability, projection
freshness, or package gate state.

Product Context Workflow authorization covers selecting an existing Product,
creating or changing Product context, and pinning an accepted revision. It is
separate from authorization to read each additional repository/source and
from authorization to admit dirty or noncanonical content. Product membership
grants none of those permissions and grants no semantic-write, test, code,
worktree, commit, push, PR, or deployment authority.

When Product mode is absent, Product fields are absent or `NONE`, local
`Session Intent` and repository routing remain unchanged, and all existing
single-project artifact identities remain valid. Product context selection is
not a semantic gate and does not replace the owning evidence, STM, capability,
projection, package, or revalidation contracts.

### Product impact and authorization routing

For a Product session, a changed source first creates a Project-local impact
root. The coordinator then follows qualified direct dependency metadata and
accepted cross-project relations to the minimum affected Product semantic
slice. It records affected and preserved sets, source availability limitations,
and the independent coverage, semantic, projection, and package dimensions.
`CONTEXT_EXPANSION_REQUIRED` requests only the missing minimum slice. `LOCAL`,
`BOUNDARY`, and `SYSTEMIC` retain their existing meanings; `SYSTEMIC` may emit
`FULL_REAUDIT_RECOMMENDED`, but no full Product review starts without explicit
user choice.

Product `REVALIDATE` does not reread every member repository and does not
reopen unrelated accepted state. Product `EXTEND` is additive: adding a
Project, capability, cross-project investigation, output, or shared resource
uses the minimum new slice and preserves unaffected accepted state. Removing
or replacing a member, changing its role, or changing shared-resource meaning
creates a new Product revision and invokes bounded impact adjudication while
preserving historical baselines and findings.

Product Context Workflow authorization is separate from every source and
execution permission. The coordinator must obtain distinct authorization for
reading an additional repository/source, selecting its revision, admitting
dirty/noncanonical content, writing Product semantic records, writing
Project-local semantic records, generating projections, running tests,
modifying code, creating/removing worktrees or branches, committing, pushing,
creating a PR, and deploying. Membership or Product selection grants none of
these permissions. Product state is routing/composition state; existing
capability contracts remain the semantic writers.

## Intent lifecycle and projection handoff

The coordinator keeps semantic completion separate from projection freshness.
For each stabilized semantic delta, the post-semantic handoff runs Projection
Impact Analysis once, persists its result, and only then evaluates any
projection-sensitive closeout. Impact accounting is not regeneration.

`NEW` follows the selected semantic workflow and its required STM/capability
slice to an accepted semantic state. It then accounts for all affected active
projections with Projection Impact Analysis and persists
`PROJECTION_IMPACT_ACCOUNTED`. `NEW` may therefore finish with projections
`STALE`; if a requested deliverable must be fresh, the coordinator starts a
separate `RG-*` workflow after semantic completion rather than regenerating as
part of impact analysis.

`EXTEND` preserves accepted Stage A semantic work and derives only the minimum
fresh dependency slice needed for the explicitly requested capability/output.
After that extension reaches a stabilized accepted semantic state, run the same
single impact-accounting handoff. If output freshness is requested, use
`TARGETED` regeneration for the requested deliverable and its required stale
upstream prerequisites only; downstream impact is not silently added to the
execution scope.

### Targeted operation-depth enrichment during `EXTEND`

When `EXTEND` selects detailed `Provided Interfaces`, detailed `Consumed
Interfaces`, or the corresponding detailed sections of `API Report`, inspect
the accepted Technical Model Coverage depth for the exact selected
Project/baseline, direction, interface kind, and parent `IF-*` slice. If the
accepted STM has only `SURFACE` depth (including
`INTERFACE_SURFACE_COMPLETE`) and no accepted operation inventory for that
slice, emit an `OPERATION_INVENTORY` depth requirement. Surface acceptance is
not treated as detailed-operation acceptance, and the old surface facts are
not invalidated.

The resolved plan persists this requirement as internal work:

```text
resolved_work:
  dependency_slice:
    - kind: OPERATION_INVENTORY
      project_binding:
        project_id: <exact Project identity>
        repository: <exact repository identity>
        source_revision: <exact committed source revision>
        baseline_ref: <exact Project baseline>
      scope_id: <exact bounded operation scope>
      required_direction: PROVIDED | CONSUMED
      required_interface_kind: <closed kind or bounded set>
      parent_if_revisions: [IF-*<revision> ...]
      source_scope: <bounded declarations/implementations/consumer scope>
      evidence_scope: <bounded WS-*/EV-* scope>
      required_depth: OPERATION_INVENTORY
      coverage_record_id: TMC-<stable-id>
      coverage_record_revision: <integer revision>
```

For Product scope, the same record additionally binds the accepted Product
revision and exact member/baseline bindings. This dependency remains internal
to `resolved_work`: it does not add Architecture Review, Test Engineering, or
Code Quality Review to `requested_work.capabilities`, and it does not add an
output that the user did not select. Detailed sections not selected in the
umbrella `API Report` do not create an operation-depth requirement.

The targeted enrichment route is:

```text
accepted surface STM facts
→ exact Project/baseline and parent-IF binding
→ targeted operation discovery and evidence
→ Technical Model Gate operation acceptance/revision
→ targeted OPERATION_INVENTORY coverage acceptance
→ detailed projection dependency satisfaction
→ explicit generation/regeneration request
→ V1–V4
→ CURRENT
```

The existing surface facts remain accepted throughout. Discovery is bounded by
the persisted source/evidence scope; unresolved dynamic operations remain
explicit inventory limitations. Projection dependency satisfaction consumes
accepted operation children, the matching coverage record, and its frozen
membership/revision snapshot; it never reconstructs private facts from source.
If fresh output was not explicitly requested, the route ends after semantic
acceptance and `PROJECTION_IMPACT_ACCOUNTED`, with any detailed projection
remaining `STALE` or otherwise visible under the package policy. Impact
accounting and `EXTEND` never start generation or regeneration implicitly.

`REVALIDATE` uses the impact-driven semantic flow in
`revalidation-and-freshness.md`. Once its semantic delta is stabilized, the
coordinator runs Projection Impact Analysis as a separate accounting step using
`references/projection-impact.md`. It persists direct exact/selector/contract/
drift impact and propagates `STALE`/`BLOCKED` through the derived reverse graph
while preserving the declared `CONSUMER -> PREREQUISITE` edge direction. A
regeneration request is a separate explicit `RG-*` session, never an implicit
consequence of revalidation or impact accounting.
`PROJECTION_IMPACT_ACCOUNTED` records that this evaluation and its freshness
results were persisted; it does not assert that all projections are current or
that regeneration occurred. A technical accounting failure does not undo
accepted semantic work, but blocks projection-sensitive downstream gates until
accounting succeeds. Repeated passes retain unresolved reasons without
duplicating them.

Projection-sensitive closeout then follows the package gate contract:

```text
semantic gates accepted
→ PROJECTION_IMPACT_ACCOUNTED
→ package membership resolved
→ required scoped projections CURRENT
→ closeout/publication permitted
```

The coordinator applies the package's declared `PERMISSIVE`,
`REQUIRED_SCOPE_CURRENT`, or `ALL_SCOPED_CURRENT` policy. Stale projections
outside the resolved required scope remain visible and actionable but do not
block unrelated capability closeout. See
[`projection-gates-and-packages.md`](projection-gates-and-packages.md); package
membership is explicit and is not inferred from arbitrary selector language.

For `PERMISSIVE`, semantic closeout may proceed after successful impact
accounting while stale projection work remains visible and deferred. For
`REQUIRED_SCOPE_CURRENT`, the consumed projection and mandatory upstream
prerequisites must be `CURRENT`. For `ALL_SCOPED_CURRENT`, every resolved
required package member must be `CURRENT`. If the required scope is not current,
closeout is blocked until the user explicitly requests the needed regeneration or
other owning action; the closeout gate does not start it implicitly.

When requested output freshness requires regeneration, start a separate
`RG-*` session under [Projection regeneration workflow](projection-regeneration.md).
Its `TARGETED` or `ALL_STALE` plan is a frozen operational execution record,
not a Session Intent, semantic stage transition, or `working/INDEX.md`
authority. Projection Impact Analysis never starts regeneration implicitly.

Legacy package reconciliation is conservative: an accepted As-Built with no
STM is valid legacy state, not corruption. `USE_EXISTING` may consume it without
modernizing; `RESUME` reconciles only the first unfinished dependency;
`EXTEND` backfills/builds only the requested STM slice; `REVALIDATE` uses old
As-Built/evidence as historical context and requires impact-driven fresh STM
acceptance. Extracted legacy facts are candidates until evidence and baseline
validation pass through the Technical Model Gate. A forensic upgrade builds the
required forensic depth and never relabels compact prose as forensic evidence.

This package-reconciliation compatibility rule is separate from legacy
projection registration. A pre-Stage-B generated or human-readable artifact
without accepted `PRJ-*` lifecycle metadata follows the projection registration
path:

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

`USE_EXISTING` may reuse the surrounding accepted package state, but it does
not make an unregistered artifact `CURRENT`. The coordinator records the
registration work and routes it to the owning capability; projection-sensitive
closeout may consume the artifact only after its registration record, accepted
dependencies, authority bindings, fingerprint/revision, and `V1`–`V4` evidence
are present. A readable file, path, age, Git history, or prior human acceptance
never substitutes for that evidence.

If required authority is absent, stale, conflicting, or unresolved, preserve
the legacy artifact as non-current context and route
`SEMANTIC_REVALIDATION`/migration to the owning semantic gate. Do not weaken
the projection verification gate, infer authority from historical prose, or
silently convert a legacy As-Built into STM. If the artifact's contract or
classification is insufficient, route `CONTRACT_ADJUDICATION`; neither outcome
permits `CURRENT`.

For the legacy Architecture final report, apply the authority inventory in
[`report-contract.md`](report-contract.md) before registering
`01-architecture-review.md`. Its historical As-Built, `RF-*`/`SER-*`, Target,
and Roadmap wording remains non-authoritative until each persistent meaning is
mapped to a current accepted owner. An unmapped meaning blocks registration;
the coordinator must not infer an owner from the report or preserve it as a
hidden authority island.

Typical `PROJECTION_REPAIR` targets include broken relative links, malformed Markdown structure, bad navigation/headings/tables, invalid Mermaid syntax/renderability, inconsistent terminology/language, duplicated or stale presentation text whose accepted replacement is already known, and malformed cross-references to accepted identifiers.

For `PROJECTION_REPAIR`, do not reopen technical discovery, candidate verification, root/severity adjudication, As-Built verification, Target technical review, or Roadmap technical review merely because final documents are being corrected. Load only the accepted authority refs needed to constrain the changed projection. If a requested correction requires changing accepted evidence, root identity/boundary, severity/exploitability, owner, invariant, product-intent status, target mechanism, roadmap prerequisite/dependency/gate, security assumption, or safe-activation semantics, stop the projection path and return:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

A completed projection repair does not make preserved technical evidence freshly verified and does not change the project baseline merely because review documents changed.
The repaired projection remains governed by its generated/projection contract:
manual edits are disposable, and no persistent human-owned section may be used to
carry meaning across a later regeneration. Anything that must survive belongs in
semantic authority.

## Review Suite Configuration

For `NEW`, always show this complete startup shape before substantive work:

```text
Review Suite
  at least one confirmed requested work item must be selected

  [ ] Architecture Review
      if selected:
        Depth:
          STANDARD_FULL | FORENSIC
        Endpoint:
          REVIEW_ONLY | REVIEW_PLUS_TARGET_ARCHITECTURE | REVIEW_PLUS_TARGET_AND_ROADMAP

  [ ] Test Engineering
      if selected:
        Test Assurance: required core
        Test Plan: optional
        Contract Consistency Report: optional
        Test Environment Design: optional
        Service Simulator Design: optional
        Service Simulator Implementation Plan: optional
        E2E Test Plan: optional

  [ ] Code Quality Review
      if selected:
        Findings View/Report: user-selectable derived projection
        Code Quality Summary: user-selectable derived projection
        Maintainability Hotspots: user-selectable derived projection
        Roadmap Contribution: user-selectable derived projection

  Standalone Outputs / Technical Documentation
      always shown in NEW after selected capability configuration:
        applicable registered Technical Documentation outputs
        NONE (explicitly confirm no standalone outputs)

  requested work item = selected capability OR valid standalone output/view
  zero capabilities + zero outputs: invalid (`NO_REVIEW_SCOPE_SELECTED`)
  standalone-output-only: valid
  capability-only: valid
  mixed capability + output: valid

Stack Addenda
  detected automatically; confirmed before substantive use
```

For a selected Architecture Review, Depth and Endpoint must both be explicitly
resolved and confirmed before its configuration_status becomes CONFIRMED;
recommendations are not defaults. For Test Engineering, Test Assurance is
visibly required/selected and every optional output is explicitly resolved as
SELECTED or NOT_SELECTED. For Code Quality, every listed projection is
explicitly resolved as SELECTED or NOT_SELECTED; zero selected projections is
valid only after the user explicitly confirms the semantic review with no
human-readable projections.

In fresh NEW state, an optional output begins as UNSPECIFIED. It is not
equivalent to NOT_SELECTED, FALSE, or a completed default. The coordinator must
not set a selected capability's configuration to CONFIRMED while any
applicable optional output remains UNSPECIFIED. Legacy confirmed packages may
interpret historical true/false values through their existing accepted package
state; this rule does not rewrite them.

requested_work.standalone_outputs is only standalone output/view routing. It
does not contain or replace Architecture depth/endpoint or Test Engineering
and Code Quality capability-owned output selections. Standalone selection and
capability-owned selection are separate configuration states. In fresh NEW,
empty selection without explicit completion evidence is UNRESOLVED; it is not
explicit NONE.

After all selected capability configurations are resolved and before the final
Requested Work summary, NEW always shows a compact Standalone Outputs /
Technical Documentation step. It offers applicable registered Technical
Documentation outputs and an explicit NONE choice. The step is shown even when
the user did not mention documentation. It does not add a fourth capability.
The user either selects one or more canonical standalone output identities or
explicitly confirms NONE; only then does standalone_output_configuration.status
become CONFIRMED.

The human-facing umbrella request API Report normalizes to the bounded existing
Technical Documentation set Provided Interfaces, Consumed Interfaces,
Integrations, Auth and Trust, and Failure Behavior. The coordinator shows this
candidate set for adjustment and confirmation, then persists only the existing
canonical output identities; API Report is not a capability or projection
identity. Full review and selecting all three semantic capabilities do not
select standalone outputs.

Before top-level requested-work confirmation, the coordinator presents one
normalized, read-only summary containing scope, selected capabilities, all
applicable capability configuration, standalone outputs, and resolved/internal
work separately. The user may Confirm or Change selection. The hard gate is
REQUESTED_WORK_CONFIGURATION_COMPLETE.

It is reached only when scope is resolved, every selected capability has
configuration_status=CONFIRMED, no applicable optional output is UNSPECIFIED,
standalone_output_configuration.status=CONFIRMED, conditional dependencies
are sufficient to validate the selection, and the normalized summary explicitly
shows standalone outputs as NONE or the selected identities and has been
confirmed. Otherwise stop with
REQUESTED_WORK_CONFIGURATION_INCOMPLETE.

Only after REQUESTED_WORK_CONFIGURATION_COMPLETE may
requested_work.confirmation_status become CONFIRMED, resolved dependency
closure proceed, authorization be evaluated, or substantive work begin.

The three top-level capabilities are independently selectable. No capability is
the implicit parent of another. Configuration under a capability is shown only
when that capability is selected. A `NEW` session with no selected capability is
valid when it has a confirmed valid standalone output; it is invalid only when
no confirmed requested work item exists.

Architecture `Depth` and `Endpoint` are independent user selections. The
Architecture menu therefore exposes the full Cartesian product: each of
`STANDARD_FULL` and `FORENSIC` may be paired with each of `REVIEW_ONLY`,
`REVIEW_PLUS_TARGET_ARCHITECTURE`, and `REVIEW_PLUS_TARGET_AND_ROADMAP`.
The recommendation may identify a default pair, but it does not restrict the
other five valid pairs or require a custom answer.

When Architecture Review is not selected, do not ask for Architecture depth or
endpoint and do not create Architecture-only work. Shared evidence, STM, or a
targeted factual dependency may still be resolved internally for a selected
capability; that internal dependency does not select Architecture Review.

For a selected full Architecture Review, the selected depth fixes the required Shared
Technical Model coverage/depth projection: `STANDARD_FULL` requires
`FULL/COMPACT` and `FORENSIC` requires `FULL/FORENSIC`. Persist the selected
requirement, but do not represent it as accepted coverage at startup. The
authoritative matrix, review, and acceptance semantics are in
[`technical-model-coverage.md`](technical-model-coverage.md).

Test Engineering is a separate startup choice from Architecture Review. When it
is enabled, `Test Assurance` is the required core and each other listed output
is selected independently as SELECTED or NOT_SELECTED after initially being
UNSPECIFIED. Lightweight reconnaissance may recommend Test
Engineering when a material automated-test surface exists, but it must never be
silently enabled. Stack addenda are lenses, not capabilities. `RESUME` reuses
reconciled persisted configuration by default; `REVALIDATE` shows the previous
suite as default; `EXTEND` shows only additions. `PROJECTION_REPAIR` reuses the
accepted suite only to locate and constrain the projections being repaired; it
does not reopen configuration choices by default.

Code Quality Review is an independent capability selection, separate from
Architecture Review and Test Engineering. Selecting the capability does not
implicitly select every Code Quality projection. When enabled, initialize its
configuration as UNRESOLVED, resolve each output as SELECTED or NOT_SELECTED,
then persist its selected outputs and retain the capability's owning semantic
records and qualified coverage state by reference. `NEW` may select Code
Quality without selecting either other capability; `EXTEND` adds only the
requested Code Quality slice and reuses accepted/fresh shared evidence or STM
dependencies; `RESUME` restores the persisted Code Quality selection rather
than reconstructing it from conversation. Detailed Code Quality semantics live
in `capabilities/code-quality-review/SKILL.md` and its referenced contracts.

Each listed Code Quality document is a derived projection of accepted Code
Quality authority. `DERIVED_PROJECTION` describes the document's relationship
to its source; it does not mean the document is automatically selected or
always generated. Output selection remains explicit and user-selectable.

Direct natural-language requests normalize through the existing capability
owner before confirmation:

| Direct request | Canonical capability | Existing output selection |
|---|---|---|
| Code Quality Findings / Findings View or Report | Code Quality Review | findings view/report |
| Code Quality Summary | Code Quality Review | code quality summary |
| Maintainability Hotspots | Code Quality Review | maintainability hotspots |
| Code Quality Roadmap Contribution | Code Quality Review | roadmap contribution |

This is capability-owned normalization, not standalone output routing and not a
new authority. Explicit confirmed selections remain subject to
`REQUESTED_WORK_CONFLICT` when later inferred wording materially contradicts
them.

When Test Review is selected, its optional Test Engineering outputs are
persisted as independent booleans, never as a compound mode:

```text
outputs:
  test_assurance: true
  test_plan: false
  contract_consistency_report: false
  test_environment_design: false
  service_simulator_design: false
  service_simulator_implementation_plan: false
  e2e_test_plan: false
```

Behavior Model is an internal dependency, not a user checkbox. Contract
Verification is automatic when materially applicable. `EXTEND` and
`REVALIDATE` reuse only the minimum accepted, fresh dependency slice; they do
not restart unrelated accepted stages.

For `NEW`, persist the selected Test Engineering outputs directly as the
independent `outputs` fields. Do not encode a new selection as a legacy
endpoint. Legacy Test Review configuration is input for old persisted packages
only; normalize only the existing endpoint:

```text
REVIEW_ONLY → test_assurance=true; all optional outputs=false
REVIEW_PLUS_TEST_PLAN → test_assurance=true; test_plan=true; all other optional outputs=false
```

The legacy endpoint never implies an extended Test Engineering output.

The legacy values `REVIEW_ONLY` and `REVIEW_PLUS_TEST_PLAN` are
`LEGACY_COMPATIBILITY_STATE`, not current user-menu options:

```text
LEGACY_COMPATIBILITY_STATE != CURRENT_USER_MENU_OPTION
```

They may be consumed only while loading or reconciling legacy persisted state
for `RESUME`, `USE_EXISTING`, or migration. Modern `NEW` and `EXTEND` show only
the independent `OFF`/enabled Test Engineering menu and its output booleans.
Legacy normalization remains conservative:

```text
REVIEW_ONLY
  → Test Engineering enabled
  → Test Assurance selected
  → every optional output false

REVIEW_PLUS_TEST_PLAN
  → Test Engineering enabled
  → Test Assurance selected
  → Test Plan selected
  → every other optional output false
```

For `EXTEND`, first read the accepted capability registry and its freshness and
authority bindings. Show already selected outputs separately from available
additions; do not reopen the full `NEW` configuration. If Test Engineering was
previously `OFF`, show the complete independent output selection. If it was
already enabled, preserve its selected outputs and show only outputs that can
still be added. Persist the result as the previous `outputs` union the user's
explicit additions.

The general `EXTEND` presentation is:

```text
EXTEND
├── Existing / preserved
│   └── selected capabilities and outputs [read-only; not checkboxes]
└── Available additions
    └── only capabilities and outputs not already selected
```

The persisted result is the previous accepted selection union explicit
additions union structurally required dependencies. Existing selections cannot
be silently deselected or reconfigured.

Architecture-specific extension is conditional on the accepted capability
registry:

```text
Architecture absent
└── Available addition: Architecture Review
    └── if selected: choose Depth and Result using the normal NEW choices

Architecture accepted
├── Existing / preserved: depth and endpoint [read-only]
└── Available endpoint additions
    ├── REVIEW_ONLY → REVIEW_PLUS_TARGET_ARCHITECTURE
    ├── REVIEW_ONLY → REVIEW_PLUS_TARGET_AND_ROADMAP
    ├── REVIEW_PLUS_TARGET_ARCHITECTURE → REVIEW_PLUS_TARGET_AND_ROADMAP
    └── REVIEW_PLUS_TARGET_AND_ROADMAP → no addition
```

The endpoint additions are monotonic: Target Architecture and Roadmap cannot be
removed or replaced. `EXTEND` never changes an accepted Architecture depth;
depth changes or semantic reconsideration use the appropriate technical flow.
When Architecture is absent, adding it does not modify existing Test
Engineering or Code Quality selections.

Required upstream dependencies may be added only when structurally necessary
and must be explained before execution. In particular, requesting
`Service Simulator Implementation Plan` without an accepted and fresh
`Service Simulator Design` means the minimum extension includes that design
first. Requesting only `E2E Test Plan` does not add Service Simulator Design
unless the selected topology requires it. Behavior Model and applicable
Contract Verification remain internal dependencies.

## Shared Technical Model bootstrap

After `NEW` configuration is resolved and before any selected capability begins
substantive execution, create the persistent Shared Technical Model baseline and
register its compact routing state in `working/INDEX.md`. This establishes
the model manifest and selected baseline; it does not require population of a
complete model when the requested downstream scope needs only a bounded factual
slice.

STM fact authority, the Technical Model Gate, and persisted model shape belong
to [Shared Technical Model](shared-technical-model.md). Startup records only
the routing state defined by
[Review Modes and Orchestration](review-modes-and-orchestration.md); it must not
copy the technical model into `INDEX.md`.

## Project Profile

Project Profile is cheap local routing/estimation metadata, not architecture evidence. For v0.3 it uses `schema_version: 1` and `collector_version: 1` and contains:

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

The local collector uses substantive tracked files as its primary inventory. For a
commit-bound baseline, inventory is the exact Git tree at
`collected_for_revision`; current working-tree content is never substituted. It
processes bytes locally and does not require putting each file into model
context. Every file belongs to exactly one primary classification bucket, using
repository-relative POSIX-style paths with path separators normalized to `/`.
Paths are not case-folded. Classification precedence is exactly:

```text
1. binary
2. generated
3. vendor/dependency
4. build artifact
5. substantive text
```

### Deterministic classification

A tracked or snapshot file is binary when Git identifies it as binary for diff
purposes while the relevant Git object is available, or when its first 8192 raw
bytes contain a NUL byte. Binary classification never comes from an extension
alone. A binary file is counted only in `excluded.binaries`; it contributes no
text lines or characters.

A non-binary file is generated when its normalized path has a component exactly
equal to `generated`, `gen`, or `dist-generated`; when `.gitattributes` in the
inspected tree gives it `linguist-generated=true`; or when one of its first five
logical text lines contains one of these exact case-insensitive markers:
`@generated`, `generated file`, `do not edit`, or `code generated`. The only
repository-declared metadata inputs for this contract are these exact
`.gitattributes` values: `true` marks generated and `false` marks
non-generated/source-owned. Metadata is evaluated before heuristic marker
matching and wins over it. Repetitive-looking content is not a rule.

A non-binary, non-generated file is vendor/dependency material when a normalized
path component exactly equals one of `node_modules`, `vendor`, `vendors`,
`third_party`, `third-party`, `deps`, `dependencies`, `packages-cache`,
`.venv`, or `venv`, or when it is Git submodule content in the inspected tree.
The project-owned source directory `packages/` is not dependency material by
name alone.

A remaining file is a build artifact when a normalized path component exactly
equals one of `build`, `dist`, `out`, `target`, `coverage`, `.next`, `.nuxt`, or
`.cache`. `.gitattributes linguist-generated=false` explicitly marking material
under such a path as source-owned overrides this path rule; without that exact
metadata the path rule wins.

Everything else that decodes as text is substantive text. If UTF-8 decoding
fails, a non-binary file is classified as binary for Project Profile purposes.

### Deterministic language mapping and text counts

Language mapping is filename-first, case-sensitive, and never uses model
inference. Suffix rules match the final suffix of the basename exactly;
directory names do not participate.

| Filename suffix | Language |
|---|---|
| `.py` | Python |
| `.js`, `.mjs`, `.cjs` | JavaScript |
| `.ts`, `.tsx` | TypeScript |
| `.jsx` | JavaScript JSX |
| `.rs` | Rust |
| `.go` | Go |
| `.java` | Java |
| `.kt`, `.kts` | Kotlin |
| `.c` | C |
| `.h` | C Header |
| `.cpp`, `.cc`, `.cxx` | C++ |
| `.hpp`, `.hh`, `.hxx` | C++ Header |
| `.cs` | C# |
| `.rb` | Ruby |
| `.php` | PHP |
| `.swift` | Swift |
| `.sh`, `.bash` | Shell |
| `.ps1` | PowerShell |
| `.sql` | SQL |
| `.html`, `.htm` | HTML |
| `.css` | CSS |
| `.scss` | SCSS |
| `.less` | Less |
| `.vue` | Vue |
| `.svelte` | Svelte |
| `.md`, `.markdown` | Markdown |
| `.rst` | reStructuredText |
| `.json` | JSON |
| `.yaml`, `.yml` | YAML |
| `.toml` | TOML |
| `.xml` | XML |

Exact filenames map as follows: `Dockerfile` → Dockerfile, `Makefile` → Make,
`CMakeLists.txt` → CMake, `requirements.txt` → Requirements,
`pyproject.toml` → TOML, and `package.json` → JSON. For text files not matched
by these exact filename or suffix rules, language is `Other Text`; unknown text
extensions are never discarded.

Decode text as UTF-8. Remove a UTF-8 BOM before counting, then normalize CRLF
and lone CR to LF. Character count is Unicode scalar value/code point count
after those transformations, not byte count. Empty text has zero lines;
otherwise line count is the number of LF characters plus one when normalized
text does not end in LF. Thus `""` → 0, `"a"` → 1, `"a\\n"` → 1,
`"a\\nb"` → 2, and `"a\\nb\\n"` → 2.

Each substantive text file contributes exactly one to `substantive.files` and
one to exactly one `languages.<language>.files` bucket. Excluded files
contribute only their exclusion-category file count; the approved schema does
not invent excluded line/character totals.

For historical backfill, collect from the historical Git tree/object content.
If required Git objects are unavailable, record
`HISTORICAL_PROFILE_UNAVAILABLE`; do not substitute current filesystem content
or partially reconstruct historical statistics.

Profile lifecycle is:

```text
MISSING → COLLECTED
OUTDATED → REFRESHED
OLD_SCHEMA → MIGRATED | BACKFILLED
CURRENT → REUSED
```

When a historical baseline commit is accessible, collect its profile locally. When it is unavailable, record `HISTORICAL_PROFILE_UNAVAILABLE` and do not invent statistics. The current profile remains usable and accepted technical evidence is not invalidated solely for this metadata gap. For `REVALIDATE`, compare both profiles over files, lines, characters, and language footprint when available. Profile totals and deltas never establish architecture materiality.

For a legacy v0.2 `COMPLETE` audit at the same HEAD with no profile, select `USE_EXISTING` and perform `METADATA_BACKFILL`. The audit remains `COMPLETE` and accepted technical gates remain closed. Schema migration is additive and does not reopen technical gates unless it exposes an authority or freshness inconsistency.

## Dirty working tree and baseline

The reproducible default is the exact committed `HEAD`. If the working tree is dirty, show this explicit choice:

```text
1. Audit committed HEAD only — recommended
2. Include working-tree changes as EPHEMERAL snapshot
3. Stop
```

Committed-HEAD-only records dirty state but excludes uncommitted paths from the evidence scope. An `EPHEMERAL` selection records:

```text
git_revision: <commit>
working_tree_snapshot: <deterministic fingerprint>
working_tree_snapshot_algorithm: sha256-v1
baseline_type: EPHEMERAL
```

### Canonical EPHEMERAL snapshot

The snapshot record set contains modified, added, deleted, renamed, and
type-changed tracked files, plus untracked files not ignored by Git. Ignored
files are excluded. Use repository-relative POSIX-style paths, with separators
normalized to `/`, and do not case-fold them. Normalize Git status letters to
these canonical states: modified `M`, tracked addition `A`, deletion `D`,
rename `R`, type change `T`, and untracked `U`. A rename is one record with the
old and new path and the new-content digest. A deletion has
`content_digest = -`; no digest is computed for it. If Git exposes composite
status letters, map them to the applicable canonical semantic state before
serialization.

For status inventory, use Git's porcelain status with rename detection fixed at
50% similarity. A reported rename is normalized to `R`; a copy is represented
as a tracked addition `A`. Otherwise apply
the first matching state in this order when composite status letters occur:
`D`, `T`, `A`, `M`. Untracked entries are `U`. This makes the status mapping
independent of index/worktree column placement; a rename record always carries
the old path, new path, and new-content digest.

Content digests are SHA-256 over raw working-tree bytes exactly as present;
there is no newline normalization. Render digests as lowercase hexadecimal,
exactly 64 characters. The snapshot fingerprint does not include timestamps,
inode numbers, filesystem ordering, absolute paths, or other filesystem
metadata.

Serialize ordinary records as the UTF-8 bytes of:

```text
STATUS<TAB>PATH<TAB>CONTENT_SHA256<LF>
```

Serialize a rename as:

```text
R<TAB>OLD_PATH<TAB>NEW_PATH<TAB>CONTENT_SHA256<LF>
```

`<TAB>` is ASCII 0x09 and `<LF>` is ASCII 0x0A. Do not escape ordinary spaces
or non-ASCII UTF-8 path bytes. If a path contains TAB or LF, encode that path
field using a JSON string with `ensure_ascii=false`, including surrounding
quotes; apply the rule independently to old and new rename paths. Sort records
by their complete serialized UTF-8 byte sequence in ascending byte order and
concatenate them without a header or footer. The final
`working_tree_snapshot` is the lowercase hexadecimal SHA-256 of those
concatenated bytes.

If there are no included dirty records, the baseline is not EPHEMERAL and no
snapshot fingerprint is created. `working_tree_snapshot_algorithm: sha256-v1`
is stable under `collector_version: 1`; incompatible future hashing changes
require a new fingerprint algorithm version. EPHEMERAL is never equivalent to
a reproducible commit baseline. If the snapshot cannot later be reconstructed,
resume/revalidation reports that limitation rather than claiming full
recoverability.

### Product baseline source bindings

For Product mode, the immutable `product_baseline_ref` contains one exact
binding for every selected Project/source and declared external source. Each
binding records the source identity, repository/scope selector, exact commit
or content binding, and the state needed to interpret that source:

| Source state | Required Product baseline binding |
|---|---|
| clean committed revision | commit SHA plus repository identity and selected scope |
| dirty tracked state | base commit, changed paths, raw-content fingerprints, and explicit admission decision |
| selected untracked content | selected paths, raw-content fingerprints, and explicit inclusion decision |
| detached HEAD | exact commit SHA plus detached state; no branch is inferred |
| local-only commit | exact local commit SHA plus local-only marker; it is not called remote-canonical |
| missing remote | observed revision and missing-remote limitation; remote existence is not inferred |
| diverged source/worktree | exact selected binding plus divergence marker and relevant compared refs |

The existing dirty-working-tree contract supplies the deterministic snapshot
algorithm. Product acceptance composes that evidence and does not make dirty
state automatically invalid or automatically accepted. A Product baseline may
contain dirty or noncanonical members only when the baseline acceptance owner
records the required binding and limitations. Product baseline acceptance,
source-read authorization, and semantic acceptance remain separate decisions.

## INDEX coordinator-state reconciliation

Persist this compact workflow state, without treating it as substantive technical authority:

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
revalidation:
  change_range
  impact_status
  impact_classification
  affected_domains
  affected_findings
  affected_capabilities
  preserved_domains
  context_expansions
projection_repair:
  requested_artifacts
  changed_artifacts
  accepted_authority_refs
  projection_validation_status
  semantic_escalation_status
legacy_projection_registration:
  artifact_refs
  owning_capability
  registration_status: NOT_REGISTERED | IN_PROGRESS | BLOCKED | REGISTERED
  blocking_action
  verified_projection_refs
```

Legacy packages missing these fields are legacy state requiring additive reconciliation/backfill, not automatically corrupt state. Before downstream use validate owning-artifact freshness and authority as required by `revalidation-and-freshness.md`.
