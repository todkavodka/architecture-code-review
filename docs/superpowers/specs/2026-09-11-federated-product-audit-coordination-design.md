# Federated Product Audit Coordination — Design

Date: 2026-09-11  
Status: DESIGN APPROVED IN CHAT / INDEPENDENT REVIEW REMEDIATED / IMPLEMENTATION NOT STARTED  
Scope: Product-mode orchestration over independently auditable child Projects and repositories

## 1. Problem

The repository already defines Product / Multi-Project semantics, immutable Product baselines, Project-local authority, Change Review, Revalidation, projection lifecycle, and session orchestration. What is missing is an explicit coordination workflow for a common layout:

```text
/projects
├── backend/
├── frontend/
├── gateway/
└── shared/
```

`/projects` is not itself a Git repository. Each child may be an independent repository and may already have its own accepted or in-progress audit package. A user running the review skill from `/projects` expects it to discover and qualify child state, reuse accepted local work, coordinate missing/stale/incomplete child audits, compose an exact Product baseline, and then perform only the cross-project/Product work that remains necessary.

Without this workflow a Product run can degrade into a mega-audit of the whole directory tree, duplicate local authority, and lose accumulated Project-local knowledge.

## 2. Architectural classification

This is an architectural orchestration change. It does not introduce a new semantic capability, technical-fact authority, runtime scanner, or generic Product fact authority. It composes existing repository discovery, previous-audit qualification, Product baseline, Change Review, Revalidation, capability, projection, and authority contracts.

Implementation remains documentation/contract-first. Stop tokens remain applicable:

```text
DO_NOT_BUILD_HARNESS
STOP_HARNESS_EXPANSION
VALIDATION_BUDGET_EXCEEDED
```

## 3. Goals

Federated mode must provide:

- bounded recursive discovery of child repository roots from a non-repository coordination root;
- explicit Product membership confirmation rather than path-implied membership;
- reuse of independently-created accepted child audits even when created outside Product context;
- top-down coordination of child audit actions;
- bottom-up discovery and reuse of independently advanced child authorities;
- exact Product baseline vectors rather than a synthetic root SHA;
- dependency/output-specific readiness rather than one binary child-ready flag;
- parallel-by-default execution of independent child work over one frozen Product coordination context;
- one confirmation before child execution and a separate gate before Product baseline acceptance;
- exact requalification immediately before Product baseline acceptance;
- incremental Product impact routing after member changes using existing dependency/freshness/capability authorities;
- durable provenance from child source/authority changes to Product baseline/review outcomes;
- accumulated Product context that references existing authorities and preserves Product-qualified cross-project semantics without becoming a new technical authority.

## 4. Non-goals

This design does not:

- turn a parent directory into a Project or repository identity;
- add a fourth semantic capability;
- add a new persisted Session Intent;
- copy child STM, Architecture, Code Quality, Test Engineering, or Contract Verification authority into Product-owned duplicates;
- make Product context the authority for technical facts, dependencies, findings, test contracts, or code-quality conclusions;
- introduce a `PIA-*` Product impact authority, identity family, or freshness lifecycle;
- introduce a universal persisted Product readiness/freshness state;
- infer Product membership from directory layout;
- auto-run Change Review, Revalidation, reconciliation, or projection regeneration;
- treat reports/summaries/projections as authority;
- require a daemon, watcher, database, crawler, or new runtime harness;
- full-scan source merely to route Product startup.

## 5. Core terminology

### 5.1 Coordination Root

A `Coordination Root` is the filesystem boundary from which federated discovery begins, for example `/projects`. It may be a plain directory. It is only a locator/discovery boundary and is not a Project, repository identity, Product identity, workspace identity, semantic authority, or Product baseline.

### 5.2 Product identity

Product retains the existing stable `PROD-*` identity and accepted Product revision lifecycle.

```text
Product Identity   PROD-<stable-id>
Coordination Root  /projects
```

Moving the root changes a locator, not Product identity or historical baselines.

### 5.3 Child Project

A child Project is an existing stable Project identity. Existing cardinalities remain valid: one Project may bind one or several repositories, and one monorepository may contain several Project scopes. Repository discovery therefore yields source candidates; it does not authoritatively allocate Project identity when mapping is ambiguous.

### 5.4 Federated Product Audit Coordinator

The coordinator is Product-side orchestration behavior. It discovers child source/audit state, proposes child actions, records a coordination plan, dispatches existing child workflows, and composes Product baseline candidates from qualified accepted local state.

It is not a semantic authority.

## 6. Selected approach

Three approaches were considered:

1. **Discovery-only reuse** — too weak because the Product layer could not manage stale/incomplete/missing child work.
2. **Federated coordinator with child actions** — selected. It discovers/qualifies local state, dispatches existing workflows, and composes accepted results without taking local ownership.
3. **Mega-audit of the root** — rejected because it conflates repository identities, duplicates authority, weakens reuse, and makes incremental analysis expensive.

## 7. Repository discovery

Discovery is bounded-recursive under the explicit Coordination Root. When an ordinary repository root is found, discovery records that repository/source candidate and stops ordinary descent into it for additional Product-member discovery by default. Nested repositories, submodules, worktrees, and explicit monorepository scopes are explicit source-binding cases rather than automatic sibling members.

Startup discovery uses escalating levels:

```text
LEVEL 1 — repository metadata
LEVEL 2 — local audit package metadata
LEVEL 3 — semantic authority loading
```

Level 1 may inspect repository identity, exact current binding, dirty/noncanonical state, and source availability. Level 2 may inspect audit `INDEX`/handoff/package metadata, accepted revisions, status, lineage, and authority bindings. Level 3 loads STM/capability/evidence details only when requested work, impact routing, ambiguity resolution, or reconciliation needs them.

### 7.1 Deterministic traversal and identity safety

The discovery contract is conservative and metadata-oriented:

- canonicalize filesystem locators only for traversal/cycle detection; a canonicalized path is not semantic identity;
- maintain a visited filesystem/source-worktree set so aliases and symlink loops cannot cause repeated or unbounded traversal;
- do not follow symlinks outside the explicit Coordination Root by default;
- stop ordinary recursive descent at a discovered repository boundary;
- treat nested repositories, submodules, and linked worktrees as explicit source-binding candidates requiring normal qualification, never as automatic Product members;
- deduplicate source candidates only by qualified repository/worktree/source identity, not by path string, directory name, timestamp, or remote URL text alone;
- do not collapse distinct Project scopes merely because they share the same repository identity;
- do not split one known multi-repository Project into several Product members merely because several repository roots were discovered;
- when canonical remote identity is missing, changed, or ambiguous, record an explicit qualification limitation and rely on the existing repository/source identity and provenance contract rather than guessing sameness or difference;
- when repository→Project or Project→repository mapping cannot be resolved from an existing Product/Project descriptor and accepted provenance, require explicit user/existing-contract resolution.

Discovery prunes obvious generated/dependency areas according to existing source conventions. Filesystem presence never implies Product membership. This contract does not require a generic filesystem crawler framework.

## 8. Existing child audit qualification

Federated discovery reuses the existing previous-audit qualification semantics per repository/Project; it does not create a second package resolver.

For each candidate package validate at least repository identity, Project/source qualification, selected scope, exact source binding, readable coordinator/index/handoff state, package state, coherent authority/revision bindings, provenance, lineage, freshness/coverage required by the consuming dependency, and current-source relation.

```text
FOUND != REUSABLE
```

Competing packages are ranked by existing identity/authority/lineage rules before recency. Remaining ambiguity is surfaced rather than guessed.

An independently-created accepted child audit is eligible for Product reuse even if it was created with no Product context, provided exact Project identity, repository/source identity, source binding, accepted authority revision, lineage, provenance, selected scope, freshness/coverage, availability, and Product/member qualification at consumption time all satisfy existing contracts.

Stale local projections do not invalidate otherwise-current semantic authority unless the requested Product output depends on that projection.

## 9. Product membership confirmation

Discovery produces member candidates; it never mutates Product membership automatically.

```text
filesystem containment != Product membership
```

For an existing Product, accepted membership is the starting point. Discovery validates known members, moved locators, missing sources, and new repository candidates. New candidates join only through normal Product revision acceptance.

Excluding a discovered candidate from a coordination plan does not mutate an already accepted Product membership snapshot. An actual membership change requires the normal Product revision lifecycle.

## 10. Child action model

No new Session Intents are added. Child state maps onto existing workflows:

```text
no usable audit                         → NEW
IN_PROGRESS + matching source           → RESUME
accepted audit + matching source        → USE_EXISTING / REUSE
accepted audit + advanced source        → offer REVALIDATE or CHANGE_REVIEW
accepted audit + diverged/unknown       → conservative existing mismatch routing
competing packages                      → reconciliation/user selection
unavailable source/package              → BLOCKED or EXCLUDE
```

Product-facing coordination labels may be:

```text
REUSE | RESUME | REVALIDATE | CHANGE_REVIEW | NEW | EXCLUDE | BLOCKED
```

They are plan labels, not Session Intents, capabilities, freshness states, or semantic lifecycle states.

## 11. Coordination policies

Two Product orchestration policies are useful:

```text
REFRESH_EXISTING
  refresh_existing: true
  create_missing: false

PREPARE_COMPLETE_PRODUCT_BASELINE
  refresh_existing: true
  create_missing: true
```

These are policy presets only. The concrete coordination plan is still shown and confirmed before child work starts.

## 12. Product Coordination Plan and frozen execution context

Example plan:

```text
backend
  audit: COMPLETE
  accepted source: A
  intended source: B
  baseline relation: BASELINE_ADVANCED
  proposed action: REVALIDATE

frontend
  audit: IN_PROGRESS
  intended source: F1
  baseline relation: BASELINE_MATCH
  proposed action: RESUME

gateway
  audit: NONE
  intended source: G1
  proposed action: NEW

shared
  audit: COMPLETE
  intended source: S1
  baseline relation: BASELINE_MATCH
  proposed action: REUSE
```

The user may change/exclude individual entries before confirmation.

Once confirmed, the coordinator persists one immutable/superseding orchestration record for that execution. It is coordinator authority/provenance only, not semantic authority. The frozen context must bind at least:

```text
coordination_plan:
  plan_id_or_revision: <stable orchestration ref>
  product_id: PROD-*
  selected_product_revision: PROD-*@revN
  membership_snapshot_ref: <immutable snapshot>
  base_product_baseline_ref: <immutable accepted baseline or NONE>
  selected_members:
    - membership/project key
      repository/source qualification
      selected scope
      intended exact source binding
      proposed/confirmed child Session Intent or coordination action
  requested_work:
    capabilities: [...]
    standalone_outputs: [...]
    Product scope/lenses as confirmed
  authorization_result: <confirmed routing authorization>
```

A mutable `current_revision`, child HEAD, filesystem path, or "latest audit" pointer must not retarget this plan after confirmation.

Any later Product revision, membership change, intended-source change, requested-work change, or action change creates a new/superseding plan rather than mutating the frozen execution meaning.

## 13. First human gate — coordination authorization

There is one Product-level confirmation before substantive child execution.

```text
Confirm Product Coordination Plan?
backend    REVALIDATE
frontend   RESUME
gateway    NEW
shared     REUSE
```

This authorizes only selected child work under the frozen plan. It does not accept a Product baseline, modify Product conclusions, authorize unrelated capabilities/reconciliation/regeneration, or waive any local child gate required by existing owner contracts.

Child workflows retain all existing source-access, candidate/reconciliation, capability, test, acceptance, and owner-specific authorization gates. The Product confirmation avoids redundant orchestration confirmation; it does not replace substantive local authorization.

## 14. Child execution and stable barrier

Every child action remains governed by that Project's existing workflow and authority owners. The coordinator dispatches but does not write child STM, Architecture, Code Quality, Test Engineering, Contract Verification, or projection authority.

Independent child work is parallel-by-default when the execution environment permits it, but only for worksets that do not conflict in writer scope. Two child tasks may read shared repositories/scopes concurrently when safe, but must not concurrently mutate the same coordinator record, audit package, capability artifact, or other owner-controlled writer target. Overlapping monorepo scopes, shared audit-package locations, locks, source constraints, authorization constraints, or explicit policy may require serialization.

Each child workflow retains its own Project-local workset/package ownership. Product dispatch never causes several Projects to write one mutable child audit package merely because the Product launched them together.

Product aggregation waits for stable child checkpoints bound to the frozen coordination plan. A checkpoint must identify at least:

```text
member/project key
exact source binding actually analyzed
accepted owner revisions/results consumed
requested dependency/output coverage
limitations
completion/provenance timestamp or equivalent trace
coordination_plan_ref
```

Product-side convenience summaries may use:

```text
REUSE_READY
UPDATED_READY
PARTIAL_USABLE
UNAVAILABLE
BLOCKED
```

These labels are derived coordination views only. They are not local lifecycle, semantic authority, freshness, or package-gate states.

If a child completed against a source or Product context different from the frozen plan, its result may remain valid in its own local lifecycle but cannot be silently aggregated into this Product candidate. The coordinator must requalify/replan.

## 15. Derived dependency-readiness view

Readiness is dependency/output-specific and derived from existing owner state, revision, availability, coverage, and freshness. It is not a new capability or status model.

Example presentation:

```text
              STM dep   ARCH cap   CQ cap   TE cap   TD projection/output
backend       OK        OK         OK       OK       OK
frontend      OK        OK         -        OK       OK
gateway       ?         ?          ?        ?        ?
shared        OK        OK         OK       -        OK
```

Only Architecture Review, Test Engineering, and Code Quality Review are top-level semantic capabilities. STM is a technical-model dependency and TD is a projection/output dependency. Each cell must be derived from the exact authoritative owner state/freshness required by the selected Product output; `OK`, `?`, and `-` are presentation labels only.

A Product Architecture request may consume qualified local STM/Architecture even if local CQ is absent. Product CQ synthesis must expose missing CQ authority rather than infer it from general Project readiness.

## 16. Product baseline candidate

After the stable barrier, the coordinator composes an immutable Product baseline candidate from exact selected child source bindings, availability/limitations, and qualified references required by the existing Product contract.

```text
PB-N+1 candidate
  product_id: PROD-*
  product_revision: PROD-*@revN
  coordination_plan_ref: <frozen plan>
  members:
    backend: exact source binding + qualified refs
    frontend: exact source binding + qualified refs
    ...
  limitations: ...
```

There is no synthetic Coordination Root SHA.

A candidate created from one frozen coordination plan cannot mix child results dispatched under another Product revision, membership snapshot, plan revision, or requested-work scope.

## 17. Second human gate — Product baseline acceptance and exact requalification

Child updates do not silently advance Product state.

```text
child work
  ↓
stable checkpoints
  ↓
exact requalification
  ↓
Product Baseline Candidate
  ↓
Product Baseline Acceptance Gate
  ↓
accepted immutable Product baseline
```

Immediately before Product Baseline Acceptance, the coordinator must re-resolve and compare all acceptance-relevant bindings against the frozen coordination plan and the candidate:

- `product_id` and selected accepted Product revision;
- immutable membership snapshot and selected member set;
- base Product baseline reference when applicable;
- each selected member's Project/repository/scope qualification;
- each intended and completed exact source binding;
- accepted owner revisions/results used by the candidate;
- requested work/lenses/outputs and authorization scope;
- availability/dirty/noncanonical limitations relevant to Product policy.

If Product revision, membership, intended source, completed child source, or required accepted authority moved, the candidate is not silently widened or retargeted. It is invalidated/superseded for current acceptance and routed to bounded requalification/replanning.

Example:

```text
child work completes at B
repository advances to C before Product acceptance
```

B may only be accepted if the user/policy explicitly chooses B as the exact historical Product member binding and all other Product rules allow that exact composition. It must never be represented as current C.

A failed/unavailable child may be accepted only as an explicit limitation when existing Product requiredness/coherency policy permits it. Otherwise acceptance blocks.

The two Product-level gates are distinct:

1. Coordination Plan confirmation authorizes selected child orchestration under the frozen plan.
2. Product Baseline Acceptance accepts the resulting exact Product composition after requalification.

Neither gate accepts findings or technical facts on behalf of their semantic owners.

## 18. Product-level analysis

After baseline acceptance, Product-scoped work may evaluate cross-project interfaces, provider/consumer relationships, integrations, end-to-end flows, data/migration dependencies, auth/trust boundaries, configuration/deployment dependencies, and Product-scoped Architecture/Test/CQ conclusions.

Authority does not move to Product context. New factual cross-project relations are accepted by the existing Technical Model Gate/STM authority with Product/member qualification. Product-scoped Architecture, Test Engineering, Code Quality, and Contract Verification conclusions remain owned by their existing capability authorities. Product context stores composition, qualification, baseline/provenance links, routing records, and references to those authoritative records.

## 19. Bidirectional coordination and exact bottom-up Product routing

Federated coordination is bidirectional.

Top-down:

```text
Product detects child mismatch
  → proposes bounded child action
  → child workflow updates local authority
  → Product consumes qualified accepted result
```

Bottom-up:

```text
child audited independently
  → new accepted local authority
  → Product discovery detects advancement
  → Product exact-vector update route
```

A new child revision never silently retargets an accepted Product baseline.

An independently accepted child authority at source B may satisfy child readiness after normal qualification, but it does not substitute for Product-level vector comparison and is not itself a reusable Product Change Review.

When the accepted Product baseline PB-N differs from a candidate member vector because one or more independently-audited children advanced, Product adoption is deterministic:

- if the user wants to update/re-evaluate accepted Product state, route PB-N to the candidate vector through existing Product `REVALIDATE` semantics and minimum qualified impact scope;
- if the user wants candidate/read-only change assessment, create a new Product `CHANGE_REVIEW` bound to the complete exact base and candidate member vectors;
- contextual `RECONCILE_CHANGE` is available only after an eligible completed Product Change Review satisfies the existing base-binding, full-vector, material-delta, owner-completion, and user-confirmation gates;
- an older Product Change Review whose complete qualified Product vector differs is not reusable merely because one child audit at B is reusable locally.

No direct "adopt child and advance Product" shortcut exists.

## 20. Detecting member advancement

Product discovery tracks two independent axes:

```text
SOURCE ADVANCEMENT
SEMANTIC AUTHORITY ADVANCEMENT
```

Examples:

```text
source changed, audit did not
  → child audit stale

source changed, accepted audit already covers new source
  → bottom-up qualified child reuse candidate; Product still needs exact-vector update routing

source unchanged, accepted semantic/capability revision advanced
  → semantic authority advancement

nothing changed
  → no child action
```

Git SHA comparison is therefore not the only freshness signal. Semantic-authority advancement on the same exact source does not itself change the member source vector, but it may require Product freshness/impact re-evaluation for claims that depend on the advanced authority.

## 21. Product Impact Analysis is derived coordination, not authority

When a member advances, the coordinator does not automatically re-run all members. "Product Impact Analysis" is the name of a coordination phase/view over existing dependency, freshness, Change Review, and capability authorities; it is not a new semantic owner.

```text
accepted PB-N
  ↓
child advancement
  ↓
changed authoritative scope identified
  ↓
existing dependency/freshness/capability evaluation
  ↓
derived Product impact routing
  ↓
affected dependency slice
  ↓
minimum required Project/capability work
  ↓
PB-N+1 candidate
```

No new `PIA-*` semantic identity family, Product impact authority, impact-strength registry, or Product-specific freshness lifecycle is introduced. If an implementation persists an impact coordination record, it is non-authoritative orchestration/provenance that references existing owner decisions.

Impact propagates from changed accepted facts/contracts/assessments through known qualified dependencies, not merely because a repository changed.

Typical semantic paths include:

```text
IF-*    → provider/consumer compatibility
EVENT-* → producer/consumer compatibility
DS-*    → schema/persistence/migration impact
AUTH-*  → trust-boundary/caller impact
CFG-*   → deployment/integration impact
FLOW-*  → end-to-end scenario impact
```

Product coordination may present:

```text
UNAFFECTED
AFFECTED
UNKNOWN_IMPACT
```

These are derived routing/summary labels only. Their evidence must come from existing authoritative dependency/freshness/capability records. `UNAFFECTED` requires sufficient accepted evidence; absence of a known edge alone is not proof. `UNKNOWN_IMPACT` opens only the minimum bounded discovery/revalidation slice needed to resolve uncertainty.

Stage B Projection Impact Analysis remains a separate projection concern after semantic stabilization and is not replaced by this Product coordination view.

## 22. Product knowledge accumulation without new authority

The Product layer accumulates durable composition and provenance while authoritative semantics remain with existing owners.

### 22.1 Product Context Workflow may own

- stable Product identity and accepted Product revisions;
- membership snapshots and shared-resource declarations;
- immutable Product baselines;
- Product coordination plans/results;
- qualified references to child/local and cross-project authoritative records;
- Product scope/provenance bindings and limitations;
- Product review/package composition requests and history pointers.

### 22.2 Existing semantic authorities continue to own

- `WS-*` / `EV-*` evidence;
- accepted `COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, `FLOW-*`, `AUTH-*`, `CFG-*`, `ERR-*` facts/relations through STM/Technical Model Gate;
- dependency/impact strengths through existing dependency semantics;
- Architecture findings;
- Code Quality findings;
- Test Engineering records;
- Contract Verification results;
- projection lifecycle/freshness;
- substantive freshness/revalidation decisions.

A Product-level cross-project relation is therefore Product-qualified but not Product-context-owned technical truth. For example:

```text
frontend/INT-orders-client
  depends_on
backend/IF-orders
```

is accepted through existing technical authority and referenced by Product context/baseline/review records.

Product projections may present an accumulated integration graph or end-to-end flow, but the projection does not become source authority.

## 23. Freshness and provenance

Product-scoped authoritative records and projections may become stale relative to a newer accepted Product baseline according to their existing owners' freshness contracts. A child can be current while a Product-qualified relation/projection referring to an older member revision is stale.

Provenance must reconstruct:

```text
PB-1
  ↓
Product Review PR-1
  ↓
backend A → B
  ↓
backend accepted local authority rev19
  ↓
existing Product impact/revalidation owner records
  ↓
PB-2 candidate
  ↓
PB-2 accepted
  ↓
Product Review PR-2
```

Each Product review revision binds one immutable accepted Product baseline. Historical reviews remain reproducible after children advance.

Every accepted Product baseline transition must record why the member vector advanced, the frozen coordination plan that produced it, which child actions occurred, which exact child source/authority revisions were consumed, which Product scopes were affected/unknown/unaffected, which existing authority records support those determinations, limitations, and supersession lineage.

Mutable `current`, `latest`, or filesystem-locator pointers are never sufficient historical dependencies.

## 24. Product coordination workspace

Because the Coordination Root may not be a repository, Product coordination state must not depend on root Git history. Physical placement is configurable and is not Product identity.

The logical coordinator namespace must reuse the existing coordinator/Product ownership model rather than create a second Product store:

```text
<selected coordinator workspace>/
└── working/
    ├── INDEX.md
    └── products/
        └── <PROD-key>/
            ├── <existing Product context/revision records>
            ├── <membership/baseline records>
            ├── <coordination-plan records>
            ├── <derived coordination/impact views if persisted>
            └── <Product projection/package references>
```

`working/INDEX.md` remains the single coordinator workflow authority. A Coordination Root-local physical workspace may be used, for example under `/projects/.architecture-code-review/`, but it must contain/use this existing logical Product-qualified namespace rather than a singular parallel `/product/INDEX.md` authority.

Multiple Products under one physical workspace are separated by stable `PROD-*` / `<PROD-key>` namespaces. Workspace/Coordination Root locator and provenance are persisted separately from Product identity. Moving `/projects` or the physical workspace does not allocate a new Product identity when identity/provenance can be resolved safely.

Child audit authority remains in each child's own accepted workflow state. Product workspace records reference it; they do not absorb it.

## 25. Startup UX

### First run

From non-Git `/projects`, a request such as `проведи аудит продукта` resolves approximately as:

```text
1. recognize coordination-root candidate
2. discover child repository/source candidates safely
3. resolve known Project identities where possible
4. discover/qualify local audit packages
5. confirm Product context/membership
6. build Product Coordination Plan
7. freeze exact coordination context and obtain one plan confirmation
8. execute/reuse child actions
9. collect stable child checkpoints
10. build derived dependency-readiness view
11. perform exact frozen-context/member/source/authority requalification
12. build Product Baseline Candidate
13. obtain Product baseline acceptance
14. run Product-scoped cross-project analysis
```

### Repeat run

`обнови аудит продукта` first performs cheap metadata comparison.

Example:

```text
backend: Product=A, current=B, accepted local audit=B
  → qualified child reuse; choose Product REVALIDATE or new exact-vector CHANGE_REVIEW according to user intent

frontend: unchanged
  → NONE

shared: Product=S1, current=S2, accepted local audit=S1
  → REVALIDATE / CHANGE_REVIEW candidate
```

Useful natural-language requests include status, refresh existing children, bring all selected members current, show changes since the previous Product review, assess impact of one member, top-down update one member, or consume an independently-updated child. Natural-language normalization never bypasses requested-work or authorization rules.

## 26. Product status view

A cheap informational status view may show:

```text
Product: PROD-42
Current baseline: PB-17

Member       Current Source  Local Audit Source  Product Binding  Action
backend      B               B                   A                REVALIDATE/NEW_CR
frontend     F1              F1                  F1               NONE
gateway      G1              G1                  G1               NONE
shared       S2              S1                  S1               REVALIDATE
```

This is a derived view, not authority or lifecycle state.

## 27. Failure and ambiguity handling

- Competing child packages that remain ambiguous return existing previous-audit reconciliation routing; never guess by timestamp.
- `IN_PROGRESS` on an older source is not resumed as current; existing baseline mismatch semantics apply.
- Unavailable members remain explicit and are subject to existing requiredness/coherency policy.
- Partial accepted authority is reusable only for outputs whose dependencies are satisfied.
- Dirty/noncanonical member sources use existing Product baseline semantics; coordinator exposes rather than normalizes them.
- Legacy packages that fail current provenance/authority qualification remain historical context until existing migration/reconciliation rules qualify them.
- Moving a repository path does not change Project/Product identity when source identity/provenance safely resolves it.
- A newly discovered repository is a candidate only; no automatic `NEW` audit runs before membership/action confirmation.
- Symlink loops/root escapes are prevented by traversal rules; aliasing never defines semantic identity.
- Duplicate/linked worktrees or changed/missing remotes require qualified source resolution or an explicit limitation; path/remote text alone never resolves identity.
- If Product revision, membership, source binding, or required accepted authority moves after plan confirmation, affected Product candidate aggregation is invalidated/superseded and requalified; results are not silently merged across plan revisions.
- A child source that advances B→C after completing work for B cannot be treated as current C at Product acceptance.

## 28. Mandatory invariants

1. Coordination Root is not a repository, Project, Product, workspace identity, baseline, or semantic authority.
2. Product membership remains explicit and immutable per accepted Product revision.
3. Child Project authority remains local when work is dispatched from Product scope.
4. Product reuses authority by qualified reference; it does not clone it.
5. Cross-project technical facts/relations remain owned by existing STM/Technical Model authority, even when Product-qualified.
6. Product-scoped findings/test/CQ/contract conclusions remain owned by their existing capability authorities.
7. Product baseline is an exact immutable vector, never one synthetic root SHA.
8. Existing seven Session Intents remain unchanged.
9. Existing top-level capability set remains exactly Architecture Review, Test Engineering, and Code Quality Review.
10. Coordination labels/policies/readiness views do not become Session Intents, capabilities, semantic authority, or freshness lifecycles.
11. Child advancement never silently advances Product baseline.
12. Independently advanced child authority never substitutes for Product exact-vector Revalidation/Change Review routing.
13. An older Product Change Review is not reusable when the complete qualified Product vector differs.
14. Product impact routing is a derived orchestration view over existing owners; no `PIA-*` semantic family or Product impact authority is introduced.
15. Product impact routing never automatically authorizes child work.
16. Unknown dependency is not equivalent to unaffected.
17. Reports/projections are never substitute authority.
18. Independent local audits are reusable when exact identity/source/authority/lineage/provenance/scope/freshness qualification passes.
19. Product-level accumulation is composition/provenance plus qualified references to existing semantic authorities, not a new Product fact store.
20. No automatic projection regeneration follows child or Product reconciliation.
21. Confirmed Product coordination freezes the Product revision, membership snapshot, base baseline, selected members, intended source/action bindings, and requested work for that execution.
22. Product baseline acceptance requires exact final requalification; moving Product/member/source/authority bindings cannot be silently accepted.
23. `working/INDEX.md` remains the single coordinator workflow authority; Product records remain Product-key-qualified under the existing logical coordinator namespace.
24. TD is a projection/output dependency, not a fourth capability.

## 29. Pressure scenarios

Implementation/contract changes must cover at least these cases:

1. non-Git root with four child repos and exact accepted audits → reuse local authority, perform only missing Product work;
2. one child source advanced but local audit stale → offer bounded Change Review/Revalidation, not full Product rescan;
3. one child independently revalidated → reuse child authority, then route Product through Product `REVALIDATE` or a new exact-vector Product Change Review according to user intent;
4. accepted child audit created outside Product context → reuse when qualification passes;
5. one child `IN_PROGRESS` with matching source → offer RESUME;
6. `IN_PROGRESS` child with changed source → baseline mismatch rules, no unsafe resume;
7. selected child with no audit → `NEW` only after confirmed policy/plan;
8. competing packages → ambiguity surfaced;
9. optional unavailable child → limitation if policy permits;
10. required unavailable child → baseline acceptance blocks when policy requires;
11. existing Product context found → reuse/resume it rather than silently duplicate identity;
12. same Project in multiple Products → isolation preserved;
13. one Project spans multiple repos → preserve one Project with all required bindings;
14. monorepo contains multiple Projects → explicit scope qualification;
15. root itself is Git plus nested repos → never conflate root repo with Product identity/membership;
16. nested submodule/worktree/symlink alias → safe traversal and qualified source candidate; no automatic sibling member or path-based deduplication;
17. vendor/example repo under root → candidate only, not automatic member;
18. local STM/Architecture current but CQ missing → architecture reuse allowed, CQ dependency remains missing;
19. local projection stale but semantic authority current → semantic reuse independent of projection freshness;
20. backend interface changes → use existing dependency/freshness authority to reopen only consumers/routes/unknown slices;
21. dependency coverage incomplete for legacy tool → `UNKNOWN_IMPACT`, not `UNAFFECTED`;
22. accepted dependency evidence proves no path to shared library → shared remains `UNAFFECTED`;
23. local semantic authority advances on same source commit → Product detects semantic advancement without changing source vector merely for that reason;
24. historical PB-1 remains reproducible while children advance;
25. user says “analyze everything” from root → membership and plan confirmation still precede substantive work;
26. Product membership changes → new accepted Product revision; in-flight older plan cannot aggregate against the new revision;
27. same Product revision with newer member sources → new immutable Product baseline;
28. one child update blocks → explicit readiness/limitation, unrelated ready members still reusable;
29. child finding IDs collide → references remain Project-qualified;
30. Product-qualified relation becomes stale after member update → existing technical/freshness owner revalidates it rather than Product context cloning a fact;
31. Product revision changes while child work is running → frozen-plan aggregation rejects cross-revision mixing and requires requalification/replan;
32. child completes at B, then source advances to C before baseline acceptance → final exact recheck rejects treating B as current C; explicit historical B remains possible only if policy/user intent allows;
33. Product Change Review covers only part of material delta → existing material-delta/reconciliation gate prevents current baseline advancement;
34. one monorepo contains two Product Projects with overlapping scopes → discovery preserves Project qualification and serializes conflicting writer scopes;
35. one Project spans two repositories → discovery does not auto-create two Product members;
36. canonical remote metadata changes while source identity/provenance still resolves → record provenance/qualification change, do not use remote text alone as identity;
37. all child audits are current but Product-qualified relations/projections are stale → child readiness remains separate from Product semantic/projection freshness.

## 30. Contract integration points

Implementation should extend existing contracts rather than build a parallel framework. Primary integration points are expected to include:

- `references/session-orchestration.md` for coordination-root startup, frozen Product coordination context, federated child discovery, plan routing, exact final requalification, and human authorization boundaries;
- `references/product-multi-project-review.md` for Product context/workspace, member qualification, baseline candidate composition, Product revision/vector pinning, derived readiness, and reuse composition;
- `references/revalidation-and-freshness.md` for Product `REVALIDATE`, substantive freshness/impact/revalidation semantics, and minimum qualified impact slices;
- Shared Technical Model and dependency contracts for Product-qualified cross-project facts/relations and dependency evidence;
- Change Review contracts for changed-member candidate analysis, complete Product-vector review semantics, and contextual reconciliation eligibility;
- capability contracts for Product-scoped Architecture/Test/CQ/Contract conclusions;
- projection/package contracts for Product projections/packages without automatic regeneration.

A focused additional reference is acceptable if clearer, but it must remain orchestration/contract documentation and must not create new semantic ownership.

## 31. Validation strategy

This is a Markdown skill/reference repository. Validation should emphasize contract consistency and existing static/acceptance checks rather than inventing a runtime harness.

At minimum verify:

- no new Session Intent or top-level capability;
- no generic Product technical-fact or Product impact authority;
- Product baseline remains exact-vector based;
- Product membership remains explicit;
- child/local and cross-project authority ownership remains with existing owners;
- previous-audit qualification semantics are reused;
- frozen coordination context prevents cross-revision/member/source mixing during parallel work;
- exact final requalification rejects B-as-current-C and other moving-target cases;
- discovery handles symlink/root escape, linked worktree, submodule/nested repo, missing/changed remote, monorepo, and multi-repo Project cases conservatively;
- independently advanced child authority routes Product adoption through existing Product `REVALIDATE` or a new exact-vector Product Change Review; old Product CR reuse is rejected when the vector differs;
- Change Review/Revalidation remain explicit and non-automatic;
- Product baseline acceptance remains human-controlled;
- Product impact/readiness labels remain derived views with no new identity/lifecycle;
- TD remains a projection/output dependency, not a capability;
- `UNAFFECTED | AFFECTED | UNKNOWN_IMPACT` routing does not infer unaffected from missing evidence;
- top-down, bottom-up, partial, ambiguous, unavailable, multi-repo/monorepo, independently-updated child, moving-Product-revision, and B→C-before-acceptance scenarios are covered.

Do not build a new runtime scanner/test harness merely to validate this textual contract.

## 32. Success criteria

The design succeeds when a user can start from a plain non-Git coordination root and safely:

1. recognize the root as a coordination boundary rather than one repository;
2. discover child repositories/Projects cheaply and safely without path-based identity assumptions;
3. discover and qualify existing child audit packages;
4. present one editable Product Coordination Plan;
5. freeze an exact Product/member/source/requested-work execution context before dispatch;
6. reuse/resume/revalidate/change-review/create selected child audits through existing workflows;
7. execute independent child work in parallel where appropriate without overlapping writer conflicts;
8. summarize derived dependency/output readiness and limitations without creating a new status authority;
9. requalify Product revision, membership, sources, and accepted child authority immediately before acceptance;
10. compose and explicitly accept an immutable Product baseline vector;
11. run cross-project Product review without duplicating semantic authority;
12. detect later source or semantic-authority advancement;
13. assess impact incrementally through existing owner semantics and reopen only affected/unknown slices;
14. reuse independently-created child analysis bottom-up while preserving exact Product Revalidation/Change Review routing;
15. preserve exact provenance and historical reproducibility.

## 33. Independent review remediation record

Independent Codex design review returned `APPROVE WITH REMEDIATION` / `READY_AFTER_SPEC_REMEDIATION`, with no HIGH findings. This revision closes the six required remediation areas before implementation planning:

1. **Frozen coordination context and final recheck** — §§12–17 now freeze Product revision/membership/base baseline/member source/action/requested-work scope and require exact pre-acceptance requalification.
2. **Discovery identity and traversal safety** — §7.1 and §27 now define conservative symlink/cycle/root-escape/worktree/submodule/remote/Project-mapping behavior without introducing a crawler framework.
3. **Bottom-up Product routing** — §19 now requires Product `REVALIDATE` or a new complete-vector Product Change Review according to intent and forbids old Product CR reuse across differing complete vectors.
4. **Workspace namespace alignment** — §24 reuses the single `working/INDEX.md` coordinator authority and `working/products/<PROD-key>/` logical namespace while keeping physical placement configurable.
5. **No Product impact authority** — §21 explicitly forbids a `PIA-*` semantic family/authority/freshness lifecycle and defines Product Impact Analysis as derived coordination over existing owners.
6. **Readiness is derived, TD is not a capability** — §15 makes readiness presentation-only/dependency-specific and keeps TD as a projection/output dependency.

The remediation also upgrades Product baseline transition provenance from optional wording to a mandatory historical requirement and adds targeted pressure scenarios for the previously failing Product-revision-during-child-work and B→C-before-acceptance cases.

## 34. Implementation boundary

This document approves the remediated design only. No implementation plan or implementation work is authorized by the spec itself.

After targeted written-spec re-review and explicit user approval, the next process step is the `writing-plans` workflow. The implementation plan must preserve minimum-slice behavior and prefer focused contract edits plus existing validation over new framework construction.