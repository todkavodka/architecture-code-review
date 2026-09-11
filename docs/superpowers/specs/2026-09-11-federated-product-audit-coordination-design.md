# Federated Product Audit Coordination — Design

Date: 2026-09-11  
Status: DESIGN APPROVED IN CHAT / IMPLEMENTATION NOT STARTED  
Scope: Product-mode orchestration over independently auditable child Projects and repositories

## 1. Problem

The repository already defines Product / Multi-Project semantics, immutable Product baselines, Project-local authority, Change Review, Revalidation, projection lifecycle, and session orchestration. What is missing is an explicit coordination workflow for a common real-world layout:

```text
/projects
├── backend/
├── frontend/
├── gateway/
└── shared/
```

`/projects` is not itself a Git repository. Each child may be an independent repository and may already have its own accepted or in-progress audit package. A user may run the review skill from `/projects` and expect it to:

1. discover the child repositories without treating the whole tree as one repository;
2. discover and qualify existing child audit state;
3. reuse accepted child authorities rather than rediscover the same local facts;
4. resume, revalidate, change-review, or create child audits where needed;
5. coordinate those child actions from the Product level;
6. compose an immutable Product baseline from exact child source bindings and accepted local authority;
7. perform only the Product-level and cross-project analysis that remains necessary;
8. later detect local source or semantic-authority changes and assess their Product-wide impact incrementally.

Without this workflow, a Product-level run can degrade into an expensive mega-audit of the whole directory tree, duplicate local authority, and lose the advantages of accumulated Project-local knowledge.

## 2. Architectural classification

This is an architectural change to orchestration semantics. It does not introduce a new semantic capability, a new technical-fact authority, or a new runtime scanner framework. It extends Product startup and coordination behavior by composing existing repository discovery, previous-audit qualification, Product baseline, Change Review, Revalidation, capability, and projection contracts.

The implementation must remain documentation/contract-first and must not introduce a new execution framework merely to automate the workflow.

Stop tokens remain applicable:

```text
DO_NOT_BUILD_HARNESS
STOP_HARNESS_EXPANSION
VALIDATION_BUDGET_EXCEEDED
```

## 3. Design goals

The federated mode must provide:

- bounded recursive discovery of child repository roots from a non-repository coordination root;
- explicit Product membership confirmation rather than path-implied membership;
- reuse of independently-created accepted child audit packages even when they were created outside any Product context;
- top-down Product coordination of child audit actions;
- bottom-up discovery and adoption of independently advanced child authorities;
- exact Product baseline vectors rather than a synthetic root SHA;
- capability-level readiness rather than a single binary child-ready flag;
- parallel-by-default execution of independent child work;
- explicit user gates before child execution and before Product baseline acceptance;
- incremental Product Impact Analysis after member changes;
- durable provenance linking source changes, child authority revisions, impact analysis, Product baselines, and Product review revisions;
- accumulated Product knowledge limited to cross-project semantics and Product-level assessments.

## 4. Non-goals

This design does not:

- turn a filesystem parent directory into a Project or repository identity;
- create a new semantic capability beyond Architecture Review, Test Engineering, and Code Quality Review;
- add new persisted Session Intents;
- copy child STM, Architecture, Code Quality, or Test Engineering authority into Product-owned duplicates;
- auto-accept Product membership from directory layout;
- auto-run Change Review, Revalidation, reconciliation, or projection regeneration without explicit authorization;
- treat reports, summaries, or generated projections as technical authority;
- require a new daemon, watcher, database, crawler, or runtime service;
- require full source scans merely to determine Product startup state;
- make Product membership transfer authorization or ownership.

## 5. Core terminology

### 5.1 Coordination Root

A `Coordination Root` is the filesystem boundary from which federated Product discovery begins.

Example:

```text
/projects
```

It may be a plain directory and is not required to be a Git repository. It is a locator and discovery boundary only. It is not a Project, repository identity, Product identity, semantic authority, or Product baseline.

### 5.2 Product identity

The Product retains the existing stable `PROD-*` identity and accepted Product revision lifecycle.

```text
Product Identity   PROD-<stable-id>
Coordination Root  /projects
```

These are separate. Moving `/projects` to `/srv/work/product-x` changes a locator, not Product identity or historical Product baselines.

### 5.3 Child Project

A child Project is an existing stable Project identity and is not necessarily one-to-one with a repository. The existing supported cardinalities remain valid:

- one Project to one repository;
- one Project to multiple repositories;
- multiple Projects to one monorepository;
- multiple Projects to multiple repositories.

Repository discovery therefore produces repository/source candidates. It does not itself allocate authoritative Project identity when mapping is ambiguous.

### 5.4 Federated Product Audit Coordinator

The Federated Product Audit Coordinator is a Product-side orchestration behavior. It discovers child source/audit state, proposes child actions, records the Product coordination plan, dispatches existing child workflows, and composes Product baseline candidates from qualified accepted local state.

It is not a new semantic authority.

## 6. Approved architectural approach

Three approaches were considered.

### A. Discovery-only reuse

The Product layer only discovers reusable accepted child audits and cannot coordinate missing, stale, or incomplete child work.

Rejected as too weak: it does not satisfy the requirement to manage child audits from the upper Product scope.

### B. Federated coordinator with child actions

The Product layer discovers child repositories and audit packages, classifies each child, proposes an existing local action such as `USE_EXISTING`, `RESUME`, `REVALIDATE`, `CHANGE_REVIEW`, or `NEW`, executes independent child work through the child workflow, then composes accepted results into Product state.

**Selected approach.** It reuses existing semantics and preserves local ownership.

### C. Mega-audit of the coordination root

The upper-level run recursively inspects all code and creates one synthetic Product-wide audit.

Rejected because it conflates repository identities, duplicates Project-local authority, weakens reuse, and makes incremental change analysis expensive.

## 7. Repository discovery

### 7.1 Discovery rule

Repository discovery is bounded-recursive under the explicit Coordination Root.

When a repository root is found, ordinary discovery stops descending into that repository for further Product-member discovery by default. Nested repositories, submodules, worktrees, and explicitly configured monorepository scopes are handled as special source-binding cases rather than automatically becoming sibling Product members.

Conceptually:

```text
Coordination Root
  ↓
bounded recursive search
  ↓
repository root found
  ↓
record repository candidate
  ↓
stop ordinary descent at that boundary
```

### 7.2 Discovery must be cheap

Startup discovery must not inspect every source file. It uses three escalating levels:

```text
LEVEL 1 — repository metadata
LEVEL 2 — local audit package metadata
LEVEL 3 — semantic authority loading
```

Level 1 may inspect repository identity, current commit/tree binding, dirty/noncanonical state, and source availability.

Level 2 may inspect known audit INDEX/handoff/package metadata, accepted revisions, package state, lineage, and authority bindings.

Level 3 loads STM/capability/evidence details only when needed for requested work, impact analysis, ambiguity resolution, or reconciliation.

### 7.3 Pruning

Discovery should prune obviously irrelevant generated/dependency directories according to existing repository/source conventions. It must not infer Product membership merely from filesystem presence.

Examples of discovered but not automatically selected candidates include:

```text
experiments/
vendor/
tools/
examples/
forks/
tmp/
```

## 8. Existing child audit discovery and qualification

Federated Product discovery reuses the existing previous-audit qualification semantics per repository/Project. It does not invent a second package resolver.

For each candidate package, validate at least:

- repository identity;
- Project/source qualification;
- readable coordinator/index/handoff state;
- known source baseline;
- package completion/acceptance state;
- coherent authority/status/revision bindings;
- provenance and lineage suitability;
- current source relation to the accepted child baseline.

`FOUND` never implies `REUSABLE`.

If multiple packages compete, use existing ordering by identity, authority state, and lineage before recency. Ambiguity is surfaced; it is not resolved by file timestamp alone.

An independently-created accepted child audit is fully eligible for Product reuse even if it was created with no Product context, provided repository/Project identity, source binding, accepted authority, provenance, and lineage qualify.

## 9. Product membership confirmation

Discovery produces Product member candidates. It does not automatically mutate Product membership.

Before a new Product revision or membership snapshot is accepted, the user confirms the selected Projects/resources. A discovered repository that is not selected remains outside Product scope.

This preserves the invariant:

```text
filesystem containment != Product membership
```

If an accepted Product context already exists, its known membership is the primary starting point. Discovery validates known members, detects moved locators, missing sources, and newly appearing repository candidates. New candidates do not join automatically.

## 10. Child action model

The federated coordinator does not add new Session Intents. It maps child state onto existing child workflows.

Typical routing:

```text
no usable audit
  → NEW

IN_PROGRESS + matching source
  → RESUME

accepted audit + matching source
  → USE_EXISTING / reuse

accepted audit + advanced source
  → offer REVALIDATE or CHANGE_REVIEW

accepted audit + diverged/unknown source
  → conservative CHANGE_REVIEW / REVALIDATE / NEW according to existing rules

competing usable packages
  → user selection / reconciliation required

unavailable source or package
  → BLOCKED or EXCLUDE
```

Product-facing coordination labels may summarize actions as:

```text
REUSE
RESUME
REVALIDATE
CHANGE_REVIEW
NEW
EXCLUDE
BLOCKED
```

These are coordination-plan labels, not a new persisted Session Intent enum.

## 11. Coordination policies

Two useful Product coordination policies are supported as orchestration policy, not Session Intent:

### 11.1 Refresh existing

```text
refresh_existing: true
create_missing: false
```

Existing child audit state may be reused, resumed, change-reviewed, or revalidated. Unassessed selected members are reported but do not automatically receive `NEW`.

### 11.2 Prepare complete Product baseline

```text
refresh_existing: true
create_missing: true
```

Existing child state is refreshed as necessary and selected unaudited members are proposed for `NEW`.

In both cases, the user sees and confirms the concrete Product Coordination Plan before substantive child work starts.

## 12. Product Coordination Plan

The coordinator builds a plan similar to:

```text
Product Coordination Plan

backend
  audit: COMPLETE
  accepted source: A
  current source: B
  baseline relation: BASELINE_ADVANCED
  proposed action: REVALIDATE

frontend
  audit: IN_PROGRESS
  baseline relation: BASELINE_MATCH
  proposed action: RESUME

gateway
  audit: NONE
  proposed action: NEW

shared
  audit: COMPLETE
  baseline relation: BASELINE_MATCH
  proposed action: REUSE
```

The user may change or exclude individual actions before confirmation.

## 13. First human gate: coordination authorization

There is one Product-level confirmation before child execution.

```text
Confirm Product Coordination Plan?

backend    REVALIDATE
frontend   RESUME
gateway    NEW
shared     REUSE
```

This authorizes only the selected child work. It does not accept a new Product baseline, mutate Product semantic conclusions, or authorize unrelated work.

A Product coordinator must not silently insert reconciliation, projection regeneration, or additional capabilities beyond the confirmed plan.

## 14. Child execution

### 14.1 Independent lifecycle

Every child action remains governed by that Project's existing workflow and authority owners. The coordinator may dispatch `RESUME`, `REVALIDATE`, `CHANGE_REVIEW`, `NEW`, or reuse state, but it does not become the writer of child STM, Architecture, Code Quality, Test Engineering, Contract Verification, or projections.

### 14.2 Parallel by default

Independent child work should execute in parallel when orchestration/runtime capabilities allow it.

Ordering is required only when there is a real dependency, lock, shared source constraint, authorization constraint, or explicit policy that requires sequencing.

### 14.3 Stable child barrier

Product aggregation waits for each selected child to reach a stable checkpoint, but stable does not mean every Project must be fully complete.

A child may be:

```text
REUSE_READY
UPDATED_READY
PARTIAL_USABLE
UNAVAILABLE
BLOCKED
```

These are Product-side readiness views, not local lifecycle states.

## 15. Capability-level readiness

Readiness is tracked per required authority/capability, not only as one child-ready bit.

Example:

```text
              STM   ARCH   CQ    TE    TD
backend       OK    OK     OK    OK    OK
frontend      OK    OK     -     OK    OK
gateway       ?     ?      ?     ?     ?
shared        OK    OK     OK    -     OK
```

A Product Architecture request may proceed with local Architecture/STM readiness even when local Code Quality is absent. A Product Code Quality synthesis must not treat absent CQ authority as present merely because the Project is otherwise usable.

`PARTIAL_USABLE` therefore means some accepted local authority may be consumed for outputs whose dependencies are satisfied, while other Product claims remain unavailable or limited.

## 16. Product baseline candidate

After the child barrier, the coordinator composes an immutable Product baseline candidate from exact selected child source bindings and qualified authority references.

Conceptually:

```text
Product Baseline Candidate PB-N+1

product_id: PROD-*
product_revision: PROD-*@revN
members:
  backend:
    source_binding: exact commit/tree/content binding
    qualified local authorities: ...
  frontend:
    source_binding: ...
  gateway:
    source_binding: ...
limitations:
  ...
```

The Product baseline remains a vector. There is no synthetic SHA for the Coordination Root.

## 17. Second human gate: Product baseline acceptance

Child updates do not silently advance Product state.

The coordinator presents the resulting candidate and readiness/limitations, then asks for Product baseline acceptance.

```text
child work
  ↓
Product Baseline Candidate
  ↓
Product Baseline Acceptance Gate
  ↓
accepted immutable Product baseline
```

A failed or unavailable child may be accepted as an explicit limitation only when the selected Product policy allows it. Required-member policy may instead block baseline acceptance.

This gate is distinct from the coordination-plan gate:

1. Coordination Plan confirmation authorizes child work.
2. Product Baseline Acceptance accepts the resulting exact Product composition for Product analysis.

## 18. Product-level analysis after baseline acceptance

Only after Product baseline acceptance does the Product-level review consume that composition as current.

Product-level work may include:

- cross-project interface/provider/consumer relationships;
- integration relationships;
- end-to-end Product flows;
- shared data and migration dependencies;
- cross-project authentication/trust boundaries;
- shared configuration and deployment dependencies;
- Product-level Architecture findings;
- Product-level Test Engineering conclusions;
- Product-level Code Quality synthesis where applicable;
- Product Technical Documentation projections.

Local child conclusions remain owned locally and are referenced with qualified identities.

## 19. Bidirectional coordination

Federated Product coordination is explicitly bidirectional.

### 19.1 Top-down flow

A Product run detects a stale or changed member and dispatches bounded local work:

```text
Product
  ↓
detect child source/authority mismatch
  ↓
propose child action
  ↓
child workflow updates accepted local state
  ↓
Product consumes qualified result
```

### 19.2 Bottom-up flow

A child Project may be audited independently outside Product context:

```text
Child Project
  ↓
independent local audit/revalidation/extension
  ↓
new accepted local authority
  ↓
Product discovery detects advancement
  ↓
Product reconciliation / impact analysis
```

The Product can reuse that accepted child advancement if source, identity, lineage, authority, and provenance qualify.

### 19.3 No silent adoption

A new child revision never silently retargets an accepted Product baseline. It becomes a reconciliation candidate.

```text
new accepted child state
  !=
current Product state
```

Product adoption requires comparison, impact/reconciliation, a new baseline candidate, and Product baseline acceptance.

## 20. Detecting member advancement

Product discovery tracks two independent change axes:

```text
SOURCE ADVANCEMENT
SEMANTIC AUTHORITY ADVANCEMENT
```

Examples:

```text
source changed, audit did not
  → child audit stale

source changed, accepted child audit already covers new source
  → bottom-up reuse candidate

source unchanged, accepted Architecture/CQ/TE revision advanced
  → semantic authority advancement

nothing changed
  → no child action
```

This prevents Git SHA comparison from becoming the only freshness signal.

## 21. Product Impact Analysis

When one or more members advance, the Product coordinator does not automatically re-run all member audits. It performs bounded Product Impact Analysis over changed semantic scope and known cross-project dependencies.

Flow:

```text
accepted PB-N
  ↓
child member advances
  ↓
changed local authorities become known
  ↓
Product Impact Analysis
  ↓
affected dependency slice
  ↓
minimum required Project/capability work
  ↓
PB-N+1 candidate
```

### 21.1 Impact is semantic, not merely repository-level

The rule is:

> Impact propagates from changed accepted facts/contracts/assessments through known dependency relations, not from the mere fact that a repository changed.

Examples:

```text
IF-* changed
  → provider / consumer compatibility impact

EVENT-* changed
  → producer / consumer impact

DS-* changed
  → schema / persistence / migration impact

AUTH-* changed
  → trust-boundary / caller impact

CFG-* changed
  → deployment / integration impact

FLOW-* changed
  → end-to-end scenario impact
```

### 21.2 Impact outcomes

Use a compact three-way Product impact conclusion:

```text
UNAFFECTED
AFFECTED
UNKNOWN_IMPACT
```

`UNAFFECTED` requires sufficient accepted dependency evidence to justify that conclusion. Mere absence of a known relation is not enough.

`AFFECTED` means a known dependency invalidates or requires revalidation of an existing Product claim/slice.

`UNKNOWN_IMPACT` means available authority is insufficient to determine whether the changed member affects another Project or Product claim.

### 21.3 Bounded follow-up

For `AFFECTED` or `UNKNOWN_IMPACT`, the coordinator opens only the minimum required Project/capability slice.

Example:

```text
backend IF-orders changed

frontend  AFFECTED       → bounded consumer compatibility revalidation
gateway   AFFECTED       → bounded route/config revalidation
legacy    UNKNOWN_IMPACT → bounded discovery
shared    UNAFFECTED     → no action
```

A bounded follow-up does not imply a full new audit of the affected Project.

## 22. Product knowledge accumulation

Product state accumulates only Product-level meaning. It must not duplicate local technical authority.

### 22.1 Product-owned durable knowledge

The Product may durably own or coordinate:

- Product identity and accepted revisions;
- membership snapshots;
- immutable Product baselines;
- qualified child authority references;
- cross-project relations;
- integration graph;
- end-to-end Product flows;
- Product-wide auth/config/data boundaries;
- Product-level Architecture/Test/CQ assessments where those contracts allow Product scope;
- Product Impact Analyses;
- Product review revisions;
- Product projections and package composition;
- orchestration provenance and limitations.

### 22.2 Product must reference, not copy, local authority

Bad:

```text
Product STM copy: "backend exposes endpoint X"
```

Correct:

```text
qualified reference: backend/IF-X
```

Product may create a Product-level relation that joins local authorities:

```text
frontend/INT-orders-client
  depends_on
backend/IF-orders
```

That relation is Product-level composition semantics and is not a duplicate of either local fact.

### 22.3 Product freshness

Product-owned relations, flows, assessments, and projections have their own freshness relative to the accepted Product baseline.

A local child authority may be current while a Product relation that points to its previous revision is stale.

```text
backend local authority: CURRENT
Product relation: STALE
```

This state must remain visible until Product impact/revalidation resolves it.

## 23. Provenance and history

The Product must preserve a reconstructable chain from source change to Product conclusion.

Example:

```text
PB-1
  ↓
Product Review PR-1
  ↓
backend A → B
  ↓
backend local authority rev19
  ↓
Product Impact Analysis PIA-7
  ↓
PB-2 candidate
  ↓
PB-2 accepted
  ↓
Product Review PR-2
```

An accepted Product baseline records exact member source bindings and qualified accepted local authority references relevant to the Product review.

A Product review revision is always bound to one immutable accepted Product baseline.

Old Product reviews remain reproducible after child Projects advance.

### 23.1 Baseline transition reason

For each accepted Product baseline transition, persist why the vector advanced and what scope was affected.

Example:

```text
PB-1 → PB-2

reason:
  backend source advanced A → B

child action:
  REVALIDATE

affected Product scope:
  frontend consumer compatibility
  gateway routing

unaffected:
  shared-lib
```

## 24. Product coordination workspace

Because the Coordination Root may not be a repository, Product coordination state must not depend on root Git history.

A default filesystem layout may be:

```text
/projects/.architecture-code-review/
└── product/
    ├── INDEX.md
    ├── product-context.md
    ├── membership/
    ├── baselines/
    ├── coordination/
    ├── impact/
    ├── cross-project/
    └── projections/
```

This path is a storage convention, not Product identity. An implementation may allow an explicitly configured Product workspace elsewhere.

The Product workspace owns Product-level orchestration/context records only. Child audit authority remains in each child Project's own accepted audit state.

## 25. Startup UX

### 25.1 First run from a non-repository root

User:

```text
cd /projects
"проведи аудит продукта"
```

Expected flow:

```text
1. recognize non-repository coordination root candidate
2. discover child repository/source candidates
3. resolve known Project identities where possible
4. discover local audit packages
5. qualify local audit/source state
6. confirm Product membership / Product context
7. build Product Coordination Plan
8. obtain one plan confirmation
9. execute/reuse child actions
10. build readiness matrix
11. build Product Baseline Candidate
12. obtain Product baseline acceptance
13. run Product-level cross-project analysis
```

### 25.2 Repeat run

User:

```text
"обнови аудит продукта"
```

Coordinator first compares accepted Product bindings with current child source and accepted authority metadata.

Example:

```text
backend
  Product source: A
  current source: B
  accepted local audit already covers B
  → reuse local update + Product reconciliation

frontend
  unchanged
  → no action

shared
  Product source: S1
  current source: S2
  accepted local audit still S1
  → REVALIDATE / CHANGE_REVIEW candidate
```

### 25.3 Useful natural-language requests

The coordinator should normalize requests such as:

```text
"покажи состояние продукта"
"обнови существующие дочерние аудиты"
"доведи весь продукт до актуального аудита"
"что изменилось с прошлого общего аудита?"
"покажи влияние изменений backend"
"обнови backend и оцени влияние на продукт"
"я уже обновил backend отдельно, подхвати изменения"
```

Natural-language normalization does not bypass existing requested-work confirmation or authorization rules.

## 26. Product status view

A concise Product status view should be derivable from persisted Product state and cheap child metadata:

```text
Product: PROD-42
Current baseline: PB-17

Member       Current Source  Local Audit Source  Product Binding  Action
backend      B               B                   A                RECONCILE
frontend     F1              F1                  F1               NONE
gateway      G1              G1                  G1               NONE
shared       S2              S1                  S1               REVALIDATE
```

The status view is informational and does not become semantic authority.

## 27. Failure and ambiguity handling

### 27.1 Competing child packages

If multiple packages remain materially ambiguous after identity/authority/lineage ranking:

```text
PREVIOUS_AUDIT_RECONCILIATION_REQUIRED
```

The coordinator must not guess.

### 27.2 In-progress audit on changed source

An `IN_PROGRESS` audit bound to an older source is not resumed as current. Existing source-baseline mismatch semantics apply.

### 27.3 Unavailable member

Unavailable selected members are represented explicitly. Whether Product baseline acceptance continues depends on requiredness/coherency policy.

### 27.4 Partial local authority

Partial accepted capability state may be reused only for Product outputs whose dependencies are satisfied. Missing authority must not be synthesized from reports or summaries.

### 27.5 Dirty/noncanonical source

Existing Product baseline dirty/noncanonical semantics remain authoritative. Federated discovery exposes the condition and does not silently canonicalize it.

### 27.6 Legacy package

A legacy package that cannot satisfy current authority/provenance qualification is historical context only until existing migration/reconciliation rules qualify it.

### 27.7 Moved repository

A moved filesystem path does not imply a new Project/Product identity when repository/source identity and provenance safely resolve the same member. Locator metadata may be updated independently of semantic identity.

### 27.8 New repository under root

A newly discovered repository is only a Product member candidate. No automatic `NEW` audit runs until membership and child action are confirmed.

## 28. Authority invariants

The following invariants are mandatory:

1. Coordination Root is not a repository, Project, Product, or semantic authority.
2. Product membership is explicit and immutable per accepted Product revision.
3. Child Project authority remains local even when work is dispatched from Product scope.
4. Product reuses child authority by qualified reference; it does not clone it.
5. Product baseline is an exact immutable vector, never one synthetic Git SHA.
6. Existing Session Intents remain unchanged.
7. Existing capability set remains exactly Architecture Review, Test Engineering, and Code Quality Review.
8. Product coordination labels do not become semantic capabilities or Session Intents.
9. Child update does not silently advance Product baseline.
10. Product Impact Analysis does not automatically authorize child work.
11. Unknown dependency is not equivalent to unaffected.
12. Reports/projections never become substitute authority.
13. Independent local audits are reusable when exact identity, source, authority, lineage, and provenance qualify.
14. Product-wide cross-project semantics may be newly owned at Product scope, but local facts/findings remain local.
15. No automatic projection regeneration follows child or Product reconciliation.

## 29. Pressure scenarios

The implementation/contract change must be checked against at least these scenarios.

1. **Non-Git root, four Git child repositories, all exact accepted audits.** Reuse all local authority and perform only missing Product-level work.
2. **One child source advanced, child audit stale.** Propose Change Review/Revalidation for that child; do not full-scan all members.
3. **One child independently revalidated before Product startup.** Detect accepted local advancement and offer Product reconciliation without repeating child analysis.
4. **Child audit created outside any Product context.** Reuse if identity/source/authority/provenance qualify.
5. **One child audit is IN_PROGRESS.** Offer RESUME when source matches; do not treat partial state as fully accepted.
6. **IN_PROGRESS child source no longer matches.** Apply source mismatch rules; no unsafe resume.
7. **No child audit exists.** Offer `NEW` only for confirmed selected member and according to coordination policy.
8. **Multiple competing packages for one child.** Surface ambiguity; do not select by timestamp.
9. **Optional child unavailable.** Product may continue only with explicit limitation if policy allows.
10. **Required child unavailable.** Baseline acceptance blocks when requiredness/coherency requires it.
11. **Existing Product context found.** Resume/refresh the known Product instead of creating a duplicate identity silently.
12. **Same Project belongs to multiple Products.** Product histories and baselines remain isolated.
13. **Project spans two repositories.** Treat both source bindings as one Project membership when descriptor resolves that mapping.
14. **Monorepo hosts multiple Projects.** Use explicit scope qualification; do not split solely by nested path heuristics.
15. **Root directory itself is also a Git repo with nested child repos.** Do not automatically conflate root source identity with Product identity or child membership.
16. **Nested submodule/worktree.** Preserve explicit source semantics; do not auto-create sibling Product member.
17. **Vendor/example repository under root.** Discovery may see it; membership remains unselected unless user confirms.
18. **Local STM current, local CQ missing.** Product Architecture may reuse STM/Architecture; Product CQ synthesis must expose missing CQ dependency.
19. **Local projection stale but local semantic authority current.** Reuse semantic authority independently from projection freshness.
20. **Backend interface changes.** Use Product dependency graph to revalidate only known consumers/routes plus unknown-impact slices.
21. **No known relation to legacy tool, but dependency coverage incomplete.** Return `UNKNOWN_IMPACT`, not `UNAFFECTED`.
22. **Accepted dependency model proves no path to shared library.** Mark shared library `UNAFFECTED` and avoid reopening it.
23. **Local accepted semantic revision advances on same source commit.** Product detects semantic-authority advancement and evaluates Product impact.
24. **Product baseline PB-1 remains historical while children advance.** Old Product review remains reproducible against PB-1.
25. **User asks “analyze everything” from root.** Still establish Product membership and coordination plan before substantive work; broad wording does not silently mean every repository and every capability.
26. **Product membership changes.** Create/accept a new Product revision; do not mutate historical membership.
27. **New Product baseline uses same Product revision but newer member sources.** Create new immutable Product baseline; do not rewrite previous baseline.
28. **Child audit update results in blocked state.** Product readiness/limitations show it explicitly; unrelated ready members remain reusable.
29. **Two child Projects have colliding local finding IDs.** Product references remain Project-qualified.
30. **Product-level relation becomes stale after child authority update.** Revalidate the Product relation rather than cloning a new child fact.

## 30. Contract integration points

Implementation should extend existing contracts rather than create a parallel framework.

Primary integration points are expected to include:

- `references/session-orchestration.md` for coordination-root startup, federated child discovery, Product coordination-plan routing, and human authorization boundaries;
- `references/product-multi-project-review.md` for Product coordination workspace/context, child authority qualification, baseline candidate composition, Product readiness, Product impact/reuse semantics, and Product-level accumulated knowledge;
- `references/revalidation-and-freshness.md` where Product impact requires existing freshness/revalidation semantics;
- Change Review contracts for changed-member candidate analysis and reconciliation eligibility;
- projection/package contracts only for resulting Product projections/packages, without introducing automatic regeneration.

Implementation may discover that a focused additional reference is clearer than overloading an existing file, but such a file must remain orchestration/contract documentation and must not introduce new semantic ownership.

## 31. Validation strategy

This repository is a Markdown skill/reference system. Validation should therefore emphasize contract consistency and existing static/acceptance checks rather than invent a runtime harness.

At minimum validate:

- no new Session Intent was introduced;
- no new top-level semantic capability was introduced;
- Product baseline remains exact-vector based;
- Product membership remains explicit;
- local authority ownership remains unchanged;
- previous-audit qualification semantics are reused;
- Change Review/Revalidation remain explicit, non-automatic actions;
- Product baseline acceptance remains human-controlled;
- Product Impact Analysis respects `UNAFFECTED | AFFECTED | UNKNOWN_IMPACT` and does not infer unaffected from missing data;
- Product-local knowledge does not duplicate local Project authority;
- key scenario matrices cover top-down, bottom-up, partial, ambiguous, unavailable, and independently-updated child cases.

Do not build a new runtime scanner/test harness merely to validate the textual contract.

## 32. Success criteria

The design is successful when a user can start from a plain non-Git `/projects` directory and the skill can safely:

1. recognize that the root is a coordination boundary rather than one repository;
2. discover candidate child repositories and known Projects cheaply;
3. discover and qualify existing child audit packages;
4. present one editable Product Coordination Plan;
5. reuse, resume, revalidate, change-review, or create selected child audits through existing workflows;
6. execute independent child work in parallel where appropriate;
7. summarize capability-level readiness and limitations;
8. compose and explicitly accept an immutable Product baseline vector;
9. run Product-level cross-project analysis without duplicating child authority;
10. detect later source or semantic-authority advancement in a child;
11. assess Product impact incrementally and reopen only affected/unknown slices;
12. reuse independently-created child analysis bottom-up;
13. preserve exact provenance and historical reproducibility across Product baseline revisions.

## 33. Implementation boundary

This document approves the design only. No implementation plan or implementation work is authorized by this spec itself.

After spec review and explicit user approval, the next process step is to create a dedicated implementation plan using the writing-plans workflow. The implementation plan must preserve the minimal-slice principle and should prefer focused contract edits plus existing validation over new framework construction.
