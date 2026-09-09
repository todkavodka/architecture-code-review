# Menu Output Routing Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved requested-work/output routing model so
standalone Stage F and Technical Documentation outputs are cleanly requestable
without artificial semantic capability selection, while preserving all
existing authority, Product, compatibility, projection, session,
authorization, and runtime boundaries.

**Architecture:** The orchestration layer distinguishes confirmed requested
work from internally resolved dependency work. Capability-owned outputs
normalize through their existing owners, while standalone, qualified-view, and
umbrella documentation requests route through existing Evidence, STM,
Technical Documentation, Product, and Test Engineering contracts without
creating new semantic or projection authority.

**Tech Stack:** Markdown Skill/reference contracts, deterministic static
contract/pressure validation, Git.

**Spec:**
docs/superpowers/specs/2026-09-09-menu-output-routing-remediation-design.md

## Global Constraints

- Baseline for implementation is the approved plan commit produced by this task; implementation must not start from the design checkpoint alone.
- Exactly three semantic top-level capabilities remain selectable: `Architecture Review`, `Test Engineering`, and `Code Quality Review`.
- `requested_work` records confirmed user selections; `resolved_work` records only the minimum dependency/gate/projection slice; `requested_work != resolved_work`.
- An internal STM, Evidence, Behavior Model, Contract Verification, Product qualification, or projection dependency never becomes a selected capability.
- Validity is `at least one selected capability OR at least one valid standalone output`; Product context alone is invalid.
- Capability-owned outputs remain owned by their existing capability: Architecture Endpoint owns Target Architecture and Remediation Roadmap; Test Engineering owns Test Plan and all listed Test Engineering outputs; Code Quality owns all listed CQ outputs.
- `CANONICAL_PROJECTION_REQUEST`, `QUALIFIED_VIEW_REQUEST`, and `UMBRELLA_OUTPUT_REQUEST` are orchestration routing classes only; they are not semantic identities, factual families, `PRJ-*` identities, lifecycle states, or authority types.
- Technical Documentation is an umbrella request for broad scope and requires bounded output/subsection confirmation; exact requests remain bounded and never silently select every projection.
- Provider / Consumer Matrix is a Product-qualified `QUALIFIED_VIEW_REQUEST` over existing Technical Documentation projections: no new `PRJ-*`, lifecycle, factual family, or compatibility authority, and no single-project Matrix route is invented.
- Generic compatibility routes directly to applicable Test Engineering Contract Verification and existing `CC-*`; it does not require Matrix or Product. Candidate matching is non-authoritative, and Matrix may render accepted CC results but never create them.
- Product is explicit opt-in context, not requested work, output confirmation, authority, or permission. Canonical output labels are reused with `scope=PRODUCT`; no duplicate Product menu identities are added.
- All six intents remain exact: `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `PROJECTION_REPAIR`.
- Existing Stage B projection identity/lifecycle/freshness/regeneration contracts, shared Evidence semantics, STM factual authority, redaction rules, and authorization contracts remain authoritative and are not duplicated.
- Selecting requested work grants no source-read, dirty-admission, semantic-write, test, code, worktree, commit, push, PR, deployment, runtime E2E, simulator, database-scan, SQL, tracing, or crawling permission.
- Migration is `COMPATIBLE_EXTENSION`: old capability-only sessions, Product sessions, Architecture Endpoint state, Test Engineering output state, old `COMPLETE`/`RESUME` packages, and existing identities remain readable without historical rewrite.
- Validation is static/manual plus deterministic pressure inspection; `DO_NOT_BUILD_HARNESS`. Stop on `STOP_HARNESS_EXPANSION` or `VALIDATION_BUDGET_EXCEEDED`.
- Before any task, the executor must read this plan. If a later prompt conflicts, stop with `IMPLEMENTATION_PROMPT_PLAN_MISMATCH`; this canonical plan wins.

## Plan authority and execution gate

Before implementing any Task N, executor MUST read this canonical plan and
extract: task title, exact files, exact required changes, exact verification,
exact commit subject, and checkpoint behavior. If any later prompt conflicts
with this plan:

```text
STOP:
IMPLEMENTATION_PROMPT_PLAN_MISMATCH
THE CANONICAL PLAN WINS.
```

Implementation must begin from the future approved implementation-plan
checkpoint, use the future worktree described below, and stop for independent
plan review when a checkpoint requires it. This planning task itself creates no
implementation branch or worktree.

### Candidate contract classification

| Candidate file | Classification | Concrete reason |
|---|---|---|
| `SKILL.md` | MODIFY_REQUIRED | The umbrella Skill must expose the requested-work/resolved-plan handoff and route to owners; it currently has no canonical standalone-output startup integration. |
| `references/session-orchestration.md` | MODIFY_REQUIRED | The current `NEW` contract rejects zero-capability sessions and lacks the requested-output menu, normalization classes, and output-aware validity predicate. |
| `references/review-modes-and-orchestration.md` | MODIFY_REQUIRED | Persisted coordinator state and capability registry need additive requested/resolved work and six-intent output routing. |
| `references/revalidation-and-freshness.md` | NO_CHANGE_REQUIRED | Existing `EXTEND`, impact-driven `REVALIDATE`, `PROJECTION_REPAIR`, freshness, and semantic-drift rules already express the approved boundary; implementation only references them. |
| `references/technical-documentation.md` | MODIFY_REQUIRED | The existing projection contract needs the direct routing entry point, umbrella confirmation, and qualified-view classification while retaining its projection authority. |
| `references/product-multi-project-review.md` | MODIFY_REQUIRED | Product output selection needs explicit separation from Product context and canonical output identity reuse for Product-qualified views. |
| `capabilities/test-review/SKILL.md` | MODIFY_REQUIRED | Direct Test Engineering output normalization and the minimum dependency slice must be made explicit at the capability entry point. |
| `capabilities/test-review/references/test-engineering-contract.md` | MODIFY_REQUIRED | Generic compatibility must be explicitly decoupled from Matrix/Product while retaining `CC-*` authority and existing applicability. |

The shared Evidence and Shared Technical Model references are additional
read-only boundary checks, not candidate modifications: their observation,
redaction, factual, and gate semantics already satisfy the approved design.

## Exact implementation file inventory

| Path | Action | Semantic owner | Reason | Task |
|---|---|---|---|---|
| `SKILL.md` | MODIFY | Umbrella orchestration | Expose the canonical requested-work layers, standalone routing entry point, resolved-plan confirmation, and explicit boundaries without duplicating owning semantics. | Task 6 |
| `references/session-orchestration.md` | MODIFY | Session Orchestration | Replace capability-only startup validity with requested-work validity; add canonical output menu, normalization, confirmation, persisted fields, six-intent routing, and legacy defaults. | Task 1 |
| `references/review-modes-and-orchestration.md` | MODIFY | Review Modes / workflow state | Persist `requested_work` separately from `resolved_work`, integrate output-aware capability registry and session-intent transitions, and preserve existing endpoint/output state. | Task 2 |
| `references/technical-documentation.md` | MODIFY | Technical Documentation projection contract | Add routing entry points, canonical Stage F output labels/classes, umbrella confirmation, qualified-view reuse, and projection/limitation references without changing factual or lifecycle authority. | Task 3 |
| `references/product-multi-project-review.md` | MODIFY | Product qualification/composition | Reuse canonical output IDs with `scope=PRODUCT`, separate Product context from output confirmation, and define Product-qualified Matrix behavior without duplicate identity. | Task 4 |
| `capabilities/test-review/SKILL.md` | MODIFY | Test Engineering capability | Make direct Test Engineering output requests normalize into existing capability output booleans and preserve Test Assurance/Behavior Model/automatic CC dependency boundaries. | Task 5 |
| `capabilities/test-review/references/test-engineering-contract.md` | MODIFY | Test Engineering compatibility authority | State generic compatibility’s direct CC route, Matrix independence, Project applicability, candidate non-authority, and combined-view separation. | Task 5 |
| `references/revalidation-and-freshness.md` | READ_ONLY | Stage B freshness/revalidation | Verify `EXTEND`, impact-driven `REVALIDATE`, and `PROJECTION_REPAIR` semantics; no routing authority change is required. | Task 2 |
| `references/shared-evidence-model.md` | READ_ONLY | Shared Evidence | Verify observation/provenance/redaction authority used by standalone outputs; do not alter Evidence semantics. | Task 3 |
| `references/shared-technical-model.md` | READ_ONLY | Shared Technical Model | Verify IF/INT/DS/EVENT/MIGRATION authority and targeted dependency slices; do not add menu or factual identities. | Task 3 |
| `tests/menu-output-routing-remediation-contract-validation.md` | CREATE | Validation projection | Deterministically inspect requested-work, routing, ownership, Product, Matrix, compatibility, intent, authorization, runtime, and 48 acceptance mappings. | Task 7 |
| `tests/menu-output-routing-remediation-backward-compatibility.md` | CREATE | Validation projection | Inspect legacy session/default interpretation and migration `COMPATIBLE_EXTENSION`, plus fail-first evidence and legacy-focused acceptance cases. | Task 7 |

Totals:

```text
existing_files_modified: 7
new_files_created: 2
validation_files_created: 2
pressure_files_created: 0
```

The two new files are validation files, so `new_files_created` and
`validation_files_created` both equal 2. No individual
`tests/pressure-scenario-*` files are planned: existing repository convention
accepts compact integrated pressure inventories for Markdown contracts, and the
approved design’s 32 pressures are mapped below and in Task 7.

## Derived ownership boundaries

The implementation must preserve this authority map:

| Concern | Authority | Routing task |
|---|---|---|
| Observation/evidence and redaction | Shared Evidence | Task 3 read-only boundary |
| Accepted technical facts | Shared Technical Model / Technical Model Gate | Task 3 read-only boundary |
| Architectural interpretation/findings | Architecture Review | Tasks 1 and 6 normalize only |
| Test semantics and CC | Test Engineering | Task 5 |
| CQ semantics | Code Quality Review | Tasks 1 and 6 normalize only |
| Derived documentation | Technical Documentation | Task 3 |
| Product qualification/composition | Product | Task 4 |
| Projection identity/lifecycle/freshness/regeneration | Stage B contracts | Tasks 2–4 read/cross-reference only |
| Requested selection and routing | Session Orchestration / Review Modes | Tasks 1–2 |

No task may transfer authority between these rows.

## Task 1: Requested-work startup model and canonical menu

**Files:**
- Modify: `references/session-orchestration.md`
- Read-only boundary: `references/shared-evidence-model.md`, `references/shared-technical-model.md`, `references/revalidation-and-freshness.md`
- Test/Validate: `tests/menu-output-routing-remediation-contract-validation.md` (Task 7 owner; Task 1 contributes the startup evidence section)

**Interfaces:**
- Consumes: existing Review Suite startup, Product context selection, three capability configuration blocks, six session intents, and existing authorization boundary.
- Produces: canonical `requested_work.capabilities`, `requested_work.standalone_outputs`, `requested_work.scope`, `requested_work.confirmation_status`; requested-work validity; canonical startup layers `Session Intent`, `Scope Context`, `Review Capabilities`, `Requested Outputs`, `Required Internal Work`, and `Authorization / Execution Boundaries`.

- [ ] Step 1: read/extract the approved design sections 5–8, 14–18, 22, 24–27, and invariants `INV-M01`–`INV-M05`, `INV-M07`–`INV-M08`, `INV-M14`–`INV-M20`, `INV-M22`–`INV-M28`, and `INV-M34` from the design file.
- [ ] Step 2: record fail-first evidence `FF-MENU-01`, `FF-MENU-02`, and `FF-MENU-07` by citing the current startup text that requires a top-level capability, lacks standalone Technical Documentation umbrella semantics, and lacks canonical requested-work layers.
- [ ] Step 3: execute the fail-first inspection and confirm the expected gap: `Interface Catalog` cannot be represented with zero capabilities under the current rule, broad Technical Documentation has no mandatory subselection contract, and startup does not separately expose requested outputs versus required internal work.
- [ ] Step 4: replace only the current `NEW` startup/configuration section with a six-layer menu: retain exactly the three capability blocks and all Architecture depth/endpoint combinations; add canonical requested output identities; define `requested_work` as capabilities plus standalone outputs; define validity for 0/0, capability-only, output-only, mixed, unsupported, ambiguous, and Product-context-only cases; and state that Product context and output confirmation are separate confirmations.
- [ ] Step 5: add exact normalization classes `EXACT`, `BOUNDED_BUT_MULTI_OUTPUT`, and `AMBIGUOUS_BROAD`, with the approved Russian examples and routes: external integrations → exact catalog, API plus DB access → candidate `Interface Catalog` + `Data Access Map`, documentation → `Technical Documentation` umbrella with subselection, compatibility → CC route, Matrix → relationship view, and Matrix plus compatibility → two routes.
- [ ] Step 6: define the bounded confirmation payload with `Session Intent`, `Scope Context`, `Review Capabilities`, `Requested Outputs`, `Required Internal Work`, `Excluded Work`, and `Authorization / Execution Boundaries`; explicitly state that confirmation persists requested work and that internal STM/Technical Documentation dependencies do not populate capabilities.
- [ ] Step 7: run focused static verification by checking all required labels, validity rows, normalization examples, Product/context separation, and no fourth capability; record results in the Task 7 validation artifact draft without editing any other contract.
- [ ] Step 8: inspect the exact diff for `references/session-orchestration.md`; verify no authority or runtime semantics were duplicated and no current Architecture Endpoint/Test Engineering selection semantics were removed.
- [ ] Step 9: run `git diff --check`.
- [ ] Step 10: commit exact file with subject `docs: add requested-work startup routing contract`.
- [ ] Step 11: record checkpoint `CP1` as pending independent review; do not publish remotely.

## Task 2: Persisted requested/resolved work and six-intent routing

**Files:**
- Modify: `references/review-modes-and-orchestration.md`
- Read-only boundary: `references/revalidation-and-freshness.md`, `references/session-orchestration.md`
- Test/Validate: `tests/menu-output-routing-remediation-backward-compatibility.md` (Task 7 owner; Task 2 contributes persistence/legacy evidence)

**Interfaces:**
- Consumes: Task 1’s confirmed `requested_work`, canonical output IDs, requested-work validity, and six-layer resolved-plan confirmation.
- Produces: persisted `resolved_work` routing state with dependency slice, required gates, projection members, limitations, and authorization requirements; six-intent behavior and additive legacy interpretation.

- [ ] Step 1: read/extract approved design sections 5, 13–14, 18–20, 24, 27 and invariants `INV-M03`, `INV-M11`–`INV-M15`, `INV-M22`–`INV-M24`, `INV-M30` from the design file.
- [ ] Step 2: record fail-first evidence `FF-MENU-04` and `FF-MENU-07` by identifying the current coordinator state where capability configuration and internal dependency closure are not explicitly separate and the startup menu lacks requested-output layers.
- [ ] Step 3: execute the fail-first inspection and confirm that the current `INDEX.md`/capability registry shape cannot persist a standalone output-only request independently from its resolved dependency slice, while legacy capability state is still the existing compatibility authority.
- [ ] Step 4: add the exact additive coordinator records `requested_work` and `resolved_work`; keep `INDEX.md` routing-only; define `resolved_work.dependency_slice`, `required_gates`, `projection_members`, `limitations`, and `authorization_requirements`; define deduplication and minimum-slice union without full Review Suite escalation.
- [ ] Step 5: encode all six intents exactly: `NEW` accepts capability-only/output-only/mixed; `USE_EXISTING` consumes only accepted/current registered output and sends missing/new output to `EXTEND`; `RESUME` restores requested and resolved state without scope addition; `REVALIDATE` preserves requested work and impacts only affected slices; `EXTEND` is additive and reuses accepted/fresh dependencies; `PROJECTION_REPAIR` is presentation-only and escalates semantic drift to `SEMANTIC_DRIFT_DETECTED` + `TECHNICAL_REVALIDATION_REQUIRED`.
- [ ] Step 6: add conservative legacy interpretation: absent standalone-output state defaults to empty, existing capability-only sessions remain valid, old Architecture Endpoint and Test Engineering output booleans remain authoritative, Product sessions remain interpretable, old `COMPLETE` remains `USE_EXISTING` when accepted/current, old `RESUME` state is readable, and no historical package or `PRJ-*` rewrite occurs.
- [ ] Step 7: run focused static verification against the six intent table, legacy examples, requested/resolved field distinction, minimum-slice rules, and projection-lifecycle references; record exact pass/fail evidence in Task 7’s backward-compatibility artifact.
- [ ] Step 8: inspect the exact diff and verify no Stage B identity/lifecycle, semantic authority, or authorization contract was redefined.
- [ ] Step 9: run `git diff --check`.
- [ ] Step 10: commit exact file with subject `docs: persist requested and resolved work routing`.
- [ ] Step 11: record `CP1` cumulative state after Tasks 1–2; stop if requested/resolved work or legacy interpretation is ambiguous.

## Task 3: Technical Documentation and standalone Stage F routing

**Files:**
- Modify: `references/technical-documentation.md`
- Read-only boundary: `references/shared-evidence-model.md`, `references/shared-technical-model.md`
- Test/Validate: `tests/menu-output-routing-remediation-contract-validation.md` (Task 7 owner; Task 3 contributes routing-table and redaction evidence)

**Interfaces:**
- Consumes: Task 1 canonical output IDs/classes and Task 2 requested/resolved routing state; accepted Evidence/STM facts and existing Technical Documentation selectors/projections.
- Produces: exact output routing table and dependency route for Technical Documentation, Provided Interfaces, Consumed Interfaces, Interface Catalog, Integration Map, Events / Messages, Data Access Map, Persistence / Data Resources, Migration Responsibility, External Integrations Catalog, and Matrix view.

- [ ] Step 1: read/extract approved design sections 7, 11, 13, 15, 19–21, 23, 25–26, and invariants `INV-M06`, `INV-M11`–`INV-M13`, `INV-M16`–`INV-M20`, `INV-M23`–`INV-M26`, `INV-M31`–`INV-M33`.
- [ ] Step 2: record fail-first evidence `FF-MENU-02`, `FF-MENU-05`, and `FF-MENU-07` by citing the current Technical Documentation contract’s projection ownership without a direct umbrella requested-work route and the absence of a menu-level Matrix classification.
- [ ] Step 3: execute the fail-first inspection and confirm that direct Technical Documentation requests lack bounded subselection semantics, that Matrix is not represented as a Product-qualified view with explicit no-new-identity behavior, and that startup layers do not expose the route.
- [ ] Step 4: add the canonical routing table with exact columns: user-facing label, routing class, owning contract, semantic owner, projection identity behavior, output confirmation requirement, Project validity, Product validity, and compatibility implication; use the approved values, including `UMBRELLA_OUTPUT_REQUEST` for Technical Documentation, `CANONICAL_PROJECTION_REQUEST` for exact outputs, and `QUALIFIED_VIEW_REQUEST` for Product-only Matrix.
- [ ] Step 5: define umbrella behavior: broad Technical Documentation resolves supported candidate sections/views, requires bounded confirmation, persists confirmed scope, then resolves dependencies; an exact bounded output selects only its existing section/projection and never silently expands to the complete package.
- [ ] Step 6: define each standalone dependency route through existing Evidence → accepted STM/Technical Model Gate → existing Technical Documentation projection/package; preserve `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, `MIGRATION_AUTHORITY`, and external fact boundaries, including no inference from URLs/connections/migration declarations and no runtime migration implication.
- [ ] Step 7: define Matrix as Product-qualified view only, reusing existing interface/integration projection identities/selectors/lifecycle; state `new_PRJ_identity=NO`, `new_lifecycle=NO`, `new_semantic_authority=NO`, `compatibility_verdict=NOT_IMPLIED`, and `menu_work_item_identity != projection_identity`.
- [ ] Step 8: restate sensitivity/limitation behavior at the routing boundary: `SECRET` omitted, `SENSITIVE_INTERNAL` redacted/aliased, `SAFE_TECHNICAL_IDENTIFIER` rendered only when permitted; partial/unavailable/stale/unresolved inputs remain explicit and never become empty/exact/compatible results.
- [ ] Step 9: run focused static verification of all 11 required routing rows, existing PRJ references, Matrix prohibition, redaction boundary, exact/broad behavior, and no factual identity additions; record checks in Task 7 artifact.
- [ ] Step 10: inspect exact diff, run `git diff --check`, and confirm the file adds routing cross-references without changing selectors, facts, lifecycle, or regeneration authority.
- [ ] Step 11: commit exact file with subject `docs: route standalone technical documentation outputs`.
- [ ] Step 12: record Task 3 contribution to `CP2` and stop if any routing row lacks an owning contract or identity behavior.

## Task 4: Product output confirmation and qualified Matrix view

**Files:**
- Modify: `references/product-multi-project-review.md`
- Read-only boundary: `references/technical-documentation.md`, `references/revalidation-and-freshness.md`
- Test/Validate: `tests/menu-output-routing-remediation-contract-validation.md` (Task 7 owner; Task 4 contributes Product and Matrix evidence)

**Interfaces:**
- Consumes: Task 1 `scope` and output confirmation fields; Task 3 canonical output IDs and existing Product-qualified selectors/snapshots.
- Produces: Product-context/output-confirmation separation, canonical Project/Product output identity reuse, Product umbrella confirmation, and Matrix-qualified-view routing.

- [ ] Step 1: read/extract approved design sections 15–17, 21, 24–25, and invariants `INV-M07`, `INV-M08`, `INV-M21), `INV-M24`–`INV-M30`, `INV-M34`.
- [ ] Step 2: record fail-first evidence `FF-MENU-03`, `FF-MENU-05`, and `FF-MENU-06` by identifying current Product output selection that can be read as context-only/all-output selection and any Product-specific display naming that could imply duplicate identity.
- [ ] Step 3: execute the fail-first inspection and confirm broad Product documentation lacks a separate required output confirmation, Product context can be mistaken for requested work, and the current named Product views need explicit canonical-ID wording.
- [ ] Step 4: add the exact two-step Product flow: confirm Product identity, accepted revision, immutable baseline, membership, availability, coverage, freshness, and limitations; separately confirm requested output scope. Product context alone remains invalid and grants no permissions.
- [ ] Step 5: replace any duplicate Product output identity wording with canonical output plus `scope=PRODUCT`; retain existing Product-qualified resolution snapshots and exact Project/source qualification.
- [ ] Step 6: define broad Product Technical Documentation as `AMBIGUOUS_BROAD`/`UMBRELLA_OUTPUT_REQUEST` requiring deterministic subsection selection before substantive work; keep exact External Integrations, Interface Catalog, Integration Map, Data Access Map, and Migration Responsibility requests bounded.
- [ ] Step 7: define Provider / Consumer Matrix as a Product-qualified `QUALIFIED_VIEW_REQUEST` reusing existing Technical Documentation projections, with no Matrix PRJ identity/lifecycle/factual family and no CC verdict; keep single-project generic compatibility independent and available through Task 5’s CC route.
- [ ] Step 8: run focused static verification for Product context/output confirmation, all exact Product examples, Matrix scope, accepted revision/baseline preservation, partial availability, and no authorization escalation; record in Task 7 artifact.
- [ ] Step 9: inspect exact diff, run `git diff --check`, and verify no Product factual authority or projection lifecycle was added.
- [ ] Step 10: commit exact file with subject `docs: separate Product context from output routing`.
- [ ] Step 11: record `CP2` cumulative state after Tasks 3–4; stop if Product context can satisfy requested-work validity or Matrix receives a new identity.

## Task 5: Capability-owned output normalization and compatibility decoupling

**Files:**
- Modify: `capabilities/test-review/SKILL.md`
- Modify: `capabilities/test-review/references/test-engineering-contract.md`
- Read-only boundary: `references/technical-documentation.md`, `references/shared-technical-model.md`
- Test/Validate: `tests/menu-output-routing-remediation-contract-validation.md` (Task 7 owner; Task 5 contributes capability/CC evidence)

**Interfaces:**
- Consumes: Task 1 direct-output normalization and Task 3 Matrix routing; existing Test Engineering output booleans, Behavior Model dependency, automatic applicability rule, and `CC-*` authority.
- Produces: canonical owner normalization for Test Assurance, Test Plan, Contract Consistency Report, Test Environment Design, Service Simulator Design, Service Simulator Implementation Plan, E2E Test Plan, and direct compatibility requests.

- [ ] Step 1: read/extract approved design sections 7, 9, 12, 15, 18, 22–23, and invariants `INV-M04`, `INV-M09`, `INV-M10`, `INV-M13`, `INV-M15`, `INV-M29), `INV-M31`–`INV-M34`.
- [ ] Step 2: record fail-first evidence `FF-MENU-05` and `FF-MENU-06` by citing current capability/output wording and compatibility wording that do not explicitly state direct Test Engineering ownership for each output and direct CC routing independent of Matrix/Product.
- [ ] Step 3: execute the fail-first inspection and confirm that a direct Test Plan request could be treated as a standalone duplicate or that generic compatibility could be coupled to a Matrix/Product route under the current menu framing.
- [ ] Step 4: add the capability-owned normalization table: each listed Test Engineering output sets its existing independent boolean; Test Assurance remains required core; Behavior Model is internal; applicable Contract Verification is automatic; runtime execution remains unsupported; simulator requests remain design/plan outputs only.
- [ ] Step 5: add direct compatibility routing: exact qualified provider/consumer inputs → applicable Contract Verification → existing `CC-*`; valid Project scope does not require Product or Matrix; missing/stale/unresolved/inapplicable inputs remain CC-owned unresolved/candidate states; candidate matching cannot emit compatibility.
- [ ] Step 6: add combined-request semantics: Matrix/relationship view and compatibility adjudication are separately owned routes; Matrix may render accepted CC outcomes but cannot create/adjudicate them; `matrix_scope != compatibility_scope`.
- [ ] Step 7: preserve old output booleans and legacy endpoint normalization exactly; do not add a compatibility identity, Stage F capability, Product compatibility authority, runtime engine, or second Test Engineering ledger.
- [ ] Step 8: run focused static verification of all seven Test Engineering outputs, core/dependency rules, Project/Product compatibility applicability, Matrix independence, candidate states, and runtime boundary; record in Task 7 artifact.
- [ ] Step 9: inspect both exact diffs, run `git diff --check`, and confirm only Test Engineering-owned cross-references changed.
- [ ] Step 10: commit exact files with subject `docs: preserve capability and CC output ownership`.
- [ ] Step 11: record `CP3` cumulative state after Task 5; stop if any capability-owned output gains a second owner or CC is no longer sole compatibility authority.

## Task 6: Umbrella integration and authorization/runtime boundaries

**Files:**
- Modify: `SKILL.md`
- Read-only boundary: `references/session-orchestration.md`, `references/review-modes-and-orchestration.md`, `references/shared-evidence-model.md`, `references/shared-technical-model.md`, `references/revalidation-and-freshness.md`, `references/technical-documentation.md`, `references/product-multi-project-review.md`, `capabilities/test-review/SKILL.md`, `capabilities/test-review/references/test-engineering-contract.md`
- Test/Validate: `tests/menu-output-routing-remediation-contract-validation.md` (Task 7 owner; Task 6 contributes umbrella boundary evidence)

**Interfaces:**
- Consumes: Tasks 1–5 canonical routing/state contracts and all existing authority boundaries.
- Produces: umbrella-level navigation and resolved-plan handoff that points to owning contracts without restating or transferring their semantics.

- [ ] Step 1: read/extract approved design sections 8–10, 13–14, 16–18, 21–23, 26–27, 31–32 and all authority rows in the approved scope ownership matrix.
- [ ] Step 2: record fail-first evidence `FF-MENU-04`, `FF-MENU-06`, and `FF-MENU-07` by identifying the current umbrella text’s capability-first routing and missing explicit resolved-plan/output-layer handoff.
- [ ] Step 3: execute the fail-first inspection and confirm that the umbrella Skill does not explicitly route standalone outputs through existing owners or expose the separate requested/resolved/authorization/runtime layers.
- [ ] Step 4: add concise umbrella instructions: load requested-work selection from Session Orchestration, load persistence/intent behavior from Review Modes, route Technical Documentation through its owner, route Product through Product qualification, route compatibility through Test Engineering/CC, and use shared Evidence/STM contracts for facts.
- [ ] Step 5: add the resolved-plan confirmation contract with exact fields `Session Intent`, `Scope Context`, `Review Capabilities`, `Requested Outputs`, `Required Internal Work`, and `Authorization / Execution Boundaries`; state `Requested Outputs != Required Internal Work` and `Product Context != Requested Outputs`.
- [ ] Step 6: restate authorization and runtime boundaries by reference: selection does not grant source/test/code/Git/deployment permissions, and the Skill does not execute E2E, simulator runtime, environment provisioning, DB scanning, SQL, tracing, or external crawling.
- [ ] Step 7: run focused static verification of cross-reference completeness, authority non-duplication, exact canonical labels, redaction pointer, all six intents, Product/Matrix/CC separation, and runtime/permission prohibitions; record in Task 7 artifact.
- [ ] Step 8: inspect exact diff, run `git diff --check`, and confirm the umbrella file contains routing guidance only rather than duplicate semantic contracts.
- [ ] Step 9: commit exact file with subject `docs: integrate menu routing into umbrella skill`.
- [ ] Step 10: record `CP3` final semantic-boundary state; stop if any umbrella prose becomes an authority override.

## Task 7: Fail-first, integrated acceptance, pressure, and compatibility validation

**Files:**
- Create: `tests/menu-output-routing-remediation-contract-validation.md`
- Create: `tests/menu-output-routing-remediation-backward-compatibility.md`
- Test/Validate: all modified contract files from Tasks 1–6; no runtime harness

**Interfaces:**
- Consumes: Tasks 1–6 contract changes, approved design tables, existing pressure conventions, and read-only shared authority contracts.
- Produces: deterministic static evidence for FF-MENU-01..07, 48/48 acceptance, 32/32 pressure prevention, 26/26 plan-pressure prevention, migration compatibility, and integrated final verification.

- [ ] Step 1: read/extract the approved design acceptance table M01–M20 and MR01–MR28, pressure table MD-P01–MD-P32, plan-pressure list PF-MENU-01..26, and repository convention from existing integrated validation artifacts; record `harness: DO_NOT_BUILD_HARNESS`.
- [ ] Step 2: record fail-first evidence before normative changes by listing exact current-contract citations for FF-MENU-01..07 and their expected gaps; do not create a simulator, parser, fixture DSL, Markdown test framework, or meta-validator.
- [ ] Step 3: execute each FF-MENU check against the completed contract set and record the expected remediation evidence; any remaining gap is `FAIL`, any unclear route is `AMBIGUOUS`, and validation must stop until corrected.
- [ ] Step 4: create the integrated validation artifact with one deterministic row for every M/MR scenario: scenario ID, expected behavior, owning task, exact contract section/check, and result. Required final result is `48 PASS`, `0 AMBIGUOUS`, `0 FAIL`.
- [ ] Step 5: create the backward-compatibility artifact with explicit checks for capability-only legacy sessions, absent standalone-output defaults, old Architecture Endpoint, old Test Engineering booleans, Product sessions, old `COMPLETE`/`USE_EXISTING`, old `RESUME`, no historical package rewrite, no `PRJ-*` rewrite, and `COMPATIBLE_EXTENSION`.
- [ ] Step 6: map all 32 MD pressure scenarios to Task 1–6 checks in an integrated table with explicit prevention evidence; required final result is `32 PREVENTED`, `0 AMBIGUOUS`, `0 UNPREVENTED`.
- [ ] Step 7: classify every PF-MENU-01..26 as `PLAN_PREVENTS`; include the exact invariant/task/check that prevents it. No PF case may be `PLAN_AMBIGUOUS` or `PLAN_ALLOWS_FAILURE`.
- [ ] Step 8: run integrated final verification for: output-only validity; 0/0 invalidity; Product-context-only invalidity; capability-owned normalization; canonical Architecture Endpoint; Test Engineering ownership; Technical Documentation umbrella/bounded distinction; Product confirmation separation; Product-qualified Matrix/no new PRJ/lifecycle; compatibility without Matrix/Product; Project CC applicability; candidate non-authority; all six intents; legacy interpretation; no permission escalation; runtime unsupported; redaction; and `COMPATIBLE_EXTENSION`.
- [ ] Step 9: inspect both validation files for exact 48/32/26 counts, no unowned scenario, no invented pressure IDs, no placeholder language, and no semantic authority claims; run `git diff --check`.
- [ ] Step 10: commit exact files with subject `test: add menu output routing contract validation`.
- [ ] Step 11: record `CP4` after Task 7 as the final integrated checkpoint; independent review is required before implementation begins or any promotion decision.

## Acceptance scenario map: 48/48

| Scenario ID | Expected behavior | Owning implementation task | Verification artifact/check |
|---|---|---|---|
| M01 | `NEW` Architecture request preserves depth/endpoint routing. | Task 1 | Contract validation M01 |
| M02 | CQ-only `NEW` remains independent. | Task 1 | M02 |
| M03 | Test Engineering + Test Plan uses existing output boolean. | Task 5 | M03 |
| M04 | Standard full + Target uses Architecture Endpoint. | Task 1 | M04 |
| M05 | Forensic + Roadmap uses existing endpoint. | Task 1 | M05 |
| M06 | Accepted/current result uses `USE_EXISTING`. | Task 2 | M06, BC-05 |
| M07 | Changed source uses impact-driven `REVALIDATE`. | Task 2 | M07 |
| M08 | CQ addition uses additive `EXTEND`. | Task 2 | M08 |
| M09 | Broken Mermaid uses `PROJECTION_REPAIR`. | Task 2 | M09 |
| M10 | Provided/consumed API request routes to Interface Catalog. | Task 3 | M10 |
| M11 | DB/table access routes to Data Access Map. | Task 3 | M11 |
| M12 | External integrations routes to exact catalog. | Task 3 | M12 |
| M13 | Product API map uses canonical output with Product scope after confirmation. | Task 4 | M13 |
| M14 | Product data/migration uses two bounded canonical outputs. | Task 4 | M14 |
| M15 | Broad Product “everything available” confirms bounded set and limitations. | Task 4 | M15 |
| M16 | E2E execution is unsupported; E2E Test Plan may be confirmed. | Task 5 | M16 |
| M17 | Simulator runtime is unsupported; design/plan may be confirmed. | Task 5 | M17 |
| M18 | Generic compatibility routes directly to applicable CC; Matrix not required. | Task 5 | M18 |
| M19 | Formatting repair uses `PROJECTION_REPAIR`. | Task 2 | M19 |
| M20 | Interface Catalog works with zero capabilities. | Task 1/3 | M20 |
| MR01 | Standalone Technical Documentation confirms section scope. | Task 3 | MR01 |
| MR02 | Standalone Interface Catalog selects sections 02/03 only. | Task 3 | MR02 |
| MR03 | Standalone Integration Map selects section 04. | Task 3 | MR03 |
| MR04 | Standalone Data Access Map selects section 05. | Task 3 | MR04 |
| MR05 | External catalog selects approved external subsection/section 07 when applicable. | Task 3 | MR05 |
| MR06 | Product Matrix is qualified view with no CC verdict/new PRJ. | Task 4 | MR06 |
| MR07 | Matrix + compatibility uses separate CC route. | Task 4/5 | MR07 |
| MR08 | Product Interface Catalog is canonical `Interface Catalog`, `scope=PRODUCT`. | Task 4 | MR08 |
| MR09 | No capability/output is `NO_REVIEW_SCOPE_SELECTED`. | Task 1 | MR09 |
| MR10 | Product context only is invalid. | Task 1/4 | MR10 |
| MR11 | Direct Test Plan normalizes to Test Engineering. | Task 5 | MR11 |
| MR12 | Direct Target normalizes to Architecture Endpoint. | Task 1 | MR12 |
| MR13 | Interface Catalog does not select Architecture. | Task 1/3 | MR13 |
| MR14 | Multiple outputs deduplicate shared dependency acquisition. | Task 2/3 | MR14 |
| MR15 | `EXTEND` adds Data Access Map without reopening Architecture. | Task 2 | MR15 |
| MR16 | `REVALIDATE` impacts only Data Access slices. | Task 2 | MR16 |
| MR17 | `RESUME` restores requested/resolved output state. | Task 2 | MR17 |
| MR18 | Missing `USE_EXISTING` output routes to `EXTEND`. | Task 2 | MR18, BC-05 |
| MR19 | Stage F formatting repair is projection-only. | Task 2/3 | MR19 |
| MR20 | Stage F semantic correction escalates to technical revalidation. | Task 2/3 | MR20 |
| MR21 | Broad Product documentation requires deterministic output confirmation. | Task 4 | MR21 |
| MR22 | Exact Product external integrations remains bounded. | Task 4 | MR22 |
| MR23 | Product API + DB request confirms only two candidates. | Task 4 | MR23 |
| MR24 | Product context without work is invalid. | Task 1/4 | MR24 |
| MR25 | Single-project compatibility remains CC-applicable without Matrix. | Task 5 | MR25 |
| MR26 | Product compatibility does not implicitly select Matrix. | Task 4/5 | MR26 |
| MR27 | Matrix absence does not block valid CC adjudication. | Task 5 | MR27 |
| MR28 | Matrix with unresolved pair preserves CC unresolved state and no fabricated verdict. | Task 5 | MR28 |

## Design pressure map: 32/32 prevented

| Scenario ID | Prevention owner/check |
|---|---|
| MD-P01 | Task 1 validity predicate |
| MD-P02 | Task 2 requested/resolved separation |
| MD-P03 | Task 1 Architecture Endpoint normalization |
| MD-P04 | Task 5 Test Engineering ownership |
| MD-P05 | Task 1/4 Product context exclusion |
| MD-P06 | Task 4 canonical output + Product scope |
| MD-P07 | Task 5 Matrix/CC separation |
| MD-P08 | Task 5 CC authority |
| MD-P09 | Task 2 minimum dependency union |
| MD-P10 | Task 2 impact-driven revalidation |
| MD-P11 | Task 2 `USE_EXISTING` acceptance requirement |
| MD-P12 | Task 2 persisted RESUME scope |
| MD-P13 | Task 2 additive EXTEND |
| MD-P14 | Task 2/3 semantic-drift escalation |
| MD-P15 | Task 5/6 runtime boundary |
| MD-P16 | Task 6 authorization boundary |
| MD-P17 | Task 2 compatible legacy defaults |
| MD-P18 | Task 1 canonical alias normalization |
| MD-P19 | Task 1 explicit conflict outcome |
| MD-P20 | Task 3 redaction boundary |
| MD-P21 | Task 3 routing-class distinction |
| MD-P22 | Task 3 no Matrix lifecycle |
| MD-P23 | Task 3 umbrella confirmation |
| MD-P24 | Task 4 separate Product/output confirmations |
| MD-P25 | Task 4 revision/baseline vs deliverable distinction |
| MD-P26 | Task 3 exact bounded route |
| MD-P27 | Task 5 Project compatibility applicability |
| MD-P28 | Task 5 direct CC route |
| MD-P29 | Task 4 Matrix remains Product-qualified |
| MD-P30 | Task 5 Matrix render-only CC behavior |
| MD-P31 | Task 5 candidate matching non-authority |
| MD-P32 | Task 4/5 Product qualification vs CC authority |

## Plan-level pressure review: 26/26 PLAN_PREVENTS

| ID | Classification | Exact prevention |
|---|---|---|
| PF-MENU-01 | PLAN_PREVENTS | Task 1 replaces capability-only validity with capability-or-valid-output. |
| PF-MENU-02 | PLAN_PREVENTS | Task 2 persists dependencies under `resolved_work`, never capabilities. |
| PF-MENU-03 | PLAN_PREVENTS | Tasks 1/3 keep Technical Documentation a routing output, not capability. |
| PF-MENU-04 | PLAN_PREVENTS | Tasks 1/5 normalize capability-owned outputs through one owner. |
| PF-MENU-05 | PLAN_PREVENTS | Task 1 routes Target through Architecture Endpoint. |
| PF-MENU-06 | PLAN_PREVENTS | Task 5 routes Test Plan through Test Engineering. |
| PF-MENU-07 | PLAN_PREVENTS | Tasks 1/4 exclude Product context from work validity. |
| PF-MENU-08 | PLAN_PREVENTS | Task 4 separates Product context and output confirmation. |
| PF-MENU-09 | PLAN_PREVENTS | Tasks 1/3 require umbrella subselection. |
| PF-MENU-10 | PLAN_PREVENTS | Tasks 1/3 preserve exact bounded outputs. |
| PF-MENU-11 | PLAN_PREVENTS | Tasks 3/4 Matrix has no new PRJ/lifecycle. |
| PF-MENU-12 | PLAN_PREVENTS | Task 5 generic compatibility bypasses Matrix. |
| PF-MENU-13 | PLAN_PREVENTS | Task 5 generic compatibility bypasses Product requirement. |
| PF-MENU-14 | PLAN_PREVENTS | Task 5 candidate matching is non-authoritative. |
| PF-MENU-15 | PLAN_PREVENTS | Task 5 Matrix cannot manufacture CC verdict. |
| PF-MENU-16 | PLAN_PREVENTS | Task 5 retains single-project CC applicability. |
| PF-MENU-17 | PLAN_PREVENTS | Task 2 `USE_EXISTING` requires accepted/current output. |
| PF-MENU-18 | PLAN_PREVENTS | Task 2 `RESUME` restores persisted scope only. |
| PF-MENU-19 | PLAN_PREVENTS | Task 2 `EXTEND` is additive and bounded. |
| PF-MENU-20 | PLAN_PREVENTS | Task 2 `REVALIDATE` is impact-driven. |
| PF-MENU-21 | PLAN_PREVENTS | Task 2/3 projection repair escalates semantic drift. |
| PF-MENU-22 | PLAN_PREVENTS | Task 6 keeps selection separate from permissions. |
| PF-MENU-23 | PLAN_PREVENTS | Tasks 5/6 retain unsupported runtime boundary. |
| PF-MENU-24 | PLAN_PREVENTS | Task 2 uses additive legacy interpretation, no destructive migration. |
| PF-MENU-25 | PLAN_PREVENTS | Task 3 preserves Evidence redaction and safe rendering. |
| PF-MENU-26 | PLAN_PREVENTS | Tasks 1/3 restrict routing classes to orchestration. |

## Commit and checkpoint strategy

| Checkpoint | After commit | Cumulative range | Scope | Review questions | Stop conditions | Remote publication |
|---|---|---|---|---|---|---|
| CP1 — requested-work/session core | Task 2 | Task 1..2 | `session-orchestration.md`, `review-modes-and-orchestration.md` | Are output-only requests valid? Are requested/resolved state and all six intents distinct? Are legacy sessions additive/readable? | Any capability-only rule remains; Product context counts as work; scope changes on resume; old state requires rewrite. | No; local independent review only. |
| CP2 — documentation/Product routing | Task 4 | Task 1..4 | Session/review modes plus Technical Documentation and Product contracts | Are all routing classes and 11 output rows owned? Does broad documentation confirm scope? Is Matrix Product-qualified with no new identity? | Missing row/owner; exact request expands; Product context substitutes output confirmation; Matrix becomes Project/PRJ/CC authority. | No; local independent review only. |
| CP3 — capability/compatibility/umbrella integration | Task 6 | Task 1..6 | All seven modified normative files | Are capability-owned outputs single-owner? Does compatibility work without Matrix/Product? Are authorization/runtime boundaries preserved? | Duplicate owner/authority; CC displaced; implicit permission/runtime support; umbrella duplicates semantics. | No; local independent review only. |
| CP4 — integrated validation | Task 7 | Task 1..7 | Two validation files plus all contract diffs | Are FF 7/7 closed, acceptance 48/48, pressure 32/32, PF 26/26, and backward compatibility explicit? | Any AMBIGUOUS/FAIL/UNPREVENTED result, placeholder, missing scenario, or harness expansion. | No; final plan/implementation review before any publication. |

Each meaningful implementation task normally ends in exactly one commit with
the subject shown in that task. Do not squash or amend these commits. No push,
merge, promotion, PR, tag, or release is authorized by this plan.

## Future implementation workspace

Implementation must create the isolated workspace only at execution time after
this plan is approved:

```text
branch: feature/menu-output-routing-remediation
worktree: /home/tod/skills/architecture-code-review-menu-output-routing-remediation
baseline: the approved implementation-plan checkpoint, not 6419ad2 alone
```

The executor must verify repository naming conventions and use the exact
approved plan commit as the starting point. This planning task creates neither
branch nor worktree.

## Integrated final verification contract

The final integrated validation must prove, with static citations and exact
contract checks, all of the following: capability OR standalone-output
validity; zero-capability standalone success; zero/zero failure; Product
context-only failure; capability-owned normalization; Architecture Endpoint
canonicality; Test Engineering ownership; Technical Documentation umbrella
confirmation; exact bounded requests; Product confirmation separation;
Product-qualified Matrix/no new PRJ/lifecycle; compatibility without Matrix or
Product; single-project compatibility where applicable; CC authority;
candidate non-authority; all six intents; legacy interpretability; no
permission escalation; unsupported runtime execution; redaction; and
`COMPATIBLE_EXTENSION`. The artifact must conclude exactly:

```text
acceptance: 48/48 PASS
pressure: 32/32 PREVENTED
plan_pressure: 26/26 PLAN_PREVENTS
harness: DO_NOT_BUILD_HARNESS
migration: COMPATIBLE_EXTENSION
```

## Self-review record

- Spec coverage: every material design section 5–34 is owned by Tasks 1–7; the 48 acceptance rows, 32 pressure rows, 26 plan-pressure rows, authority matrix, migration, authorization, runtime, Product, Matrix, CC, and session-intent requirements are explicitly mapped.
- Placeholder scan: no unresolved placeholder markers or vague implementation instructions are present.
- File/task consistency: each implementation file has one primary task owner; read-only authority files are explicitly marked and are not planned for modification; validation files have one owner.
- Interface consistency: `requested_work`, `resolved_work`, `standalone_outputs`, `confirmation_status`, `CANONICAL_PROJECTION_REQUEST`, `QUALIFIED_VIEW_REQUEST`, and `UMBRELLA_OUTPUT_REQUEST` are used consistently.
- Commit consistency: seven unique task subjects are specified; each task has one commit and no amend/squash instruction.
- Checkpoint consistency: CP1–CP4 have exact cumulative task ranges, scopes, questions, stop conditions, and no remote publication.
- Validation completeness: 48/48 acceptance, 32/32 design pressure, 26/26 plan pressure are mapped with required zero ambiguity/failure targets.
- Authority review: no new semantic capability, factual family, PRJ lifecycle, compatibility authority, runtime capability, or implicit authorization is introduced.

## Plan-only prohibitions

```text
normative_contracts_modified: NO (by this planning task)
implementation_performed: NO
tests_created: NO (by this planning task; validation files are planned only)
roadmap_modified: NO
implementation_branch_created: NO
worktree_created: NO
push_performed: NO
PR_created: NO
tag_created: NO
release_performed: NO
deployment_performed: NO
```
