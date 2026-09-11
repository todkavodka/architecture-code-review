# Federated Product Audit Coordination — Design

Date: 2026-09-11  
Status: DESIGN APPROVED IN CHAT / IMPLEMENTATION NOT STARTED  
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
- capability-level readiness rather than one binary child-ready flag;
- parallel-by-default execution of independent child work;
- one confirmation before child execution and a separate gate before Product baseline acceptance;
- incremental Product impact analysis after member changes;
- durable provenance from child source/authority changes to Product baseline/review outcomes;
- accumulated Product context that references existing authorities and preserves Product-qualified cross-project semantics without becoming a new technical authority.

## 4. Non-goals

This design does not:

- turn a parent directory into a Project or repository identity;
- add a fourth semantic capability;
- add a new persisted Session Intent;
- copy child STM, Architecture, Code Quality, Test Engineering, or Contract Verification authority into Product-owned duplicates;
- make Product context the authority for technical facts, dependencies, findings, test contracts, or code-quality conclusions;
- infer Product membership from directory layout;
- auto-run Change Review, Revalidation, reconciliation, or projection regeneration;
- treat reports/summaries/projections as authority;
- require a daemon, watcher, database, crawler, or new runtime harness;
- full-scan source merely to route Product startup.

## 5. Core terminology

### 5.1 Coordination Root

A `Coordination Root` is the filesystem boundary from which federated discovery begins, for example `/projects`. It may be a plain directory. It is only a locator/discovery boundary and is not a Project, repository identity, Product identity, semantic authority, or Product baseline.

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

Discovery is bounded-recursive under the explicit Coordination Root. When an ordinary repository root is found, discovery records that repository candidate and stops descending into it for additional Product-member discovery by default. Nested repositories, submodules, worktrees, and explicit monorepository scopes are special source-binding cases rather than automatic sibling members.

Startup discovery uses escalating levels:

```text
LEVEL 1 — repository metadata
LEVEL 2 — local audit package metadata
LEVEL 3 — semantic authority loading
```

Level 1 may inspect repository identity, exact current binding, dirty/noncanonical state, and source availability. Level 2 may inspect audit `INDEX`/handoff/package metadata, accepted revisions, status, lineage, and authority bindings. Level 3 loads STM/capability/evidence details only when requested work, impact analysis, ambiguity resolution, or reconciliation needs them.

Discovery prunes obvious generated/dependency areas according to existing source conventions. Filesystem presence never implies Product membership.

## 8. Existing child audit qualification

Federated discovery reuses the existing previous-audit qualification semantics per repository/Project; it does not create a second package resolver.

For each candidate package validate at least repository identity, Project/source qualification, readable coordinator/index/handoff state, known source baseline, package state, coherent authority/revision bindings, provenance, lineage, and current-source relation.

```text
FOUND != REUSABLE
```

Competing packages are ranked by existing identity/authority/lineage rules before recency. Remaining ambiguity is surfaced rather than guessed.

An independently-created accepted child audit is eligible for Product reuse even if it was created with no Product context, provided exact identity, source binding, accepted authority, lineage, provenance, and required scope qualify.

## 9. Product membership confirmation

Discovery produces member candidates; it never mutates Product membership automatically.

```text
filesystem containment != Product membership
```

For an existing Product, accepted membership is the starting point. Discovery validates known members, moved locators, missing sources, and new repository candidates. New candidates join only through normal Product revision acceptance.

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

They are plan labels, not Session Intents or capabilities.

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

## 12. Product Coordination Plan

Example:

```text
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

The user may change/exclude individual entries before confirmation.

## 13. First human gate — coordination authorization

There is one Product-level confirmation before substantive child execution.

```text
Confirm Product Coordination Plan?
backend    REVALIDATE
frontend   RESUME
gateway    NEW
shared     REUSE
```

This authorizes only selected child work. It does not accept a Product baseline, modify Product conclusions, or authorize unrelated capabilities/reconciliation/regeneration.

## 14. Child execution and stable barrier

Every child action remains governed by that Project's existing workflow and authority owners. The coordinator dispatches but does not write child STM, Architecture, Code Quality, Test Engineering, Contract Verification, or projection authority.

Independent child work is parallel-by-default when the execution environment permits it. Ordering is required only by real dependency, locking, shared-source, authorization, or explicit policy constraints.

Product aggregation waits for stable child checkpoints. Product-side readiness may be summarized as:

```text
REUSE_READY
UPDATED_READY
PARTIAL_USABLE
UNAVAILABLE
BLOCKED
```

These are coordination views, not new child lifecycle states.

## 15. Capability-level readiness

Readiness is dependency/capability-specific:

```text
              STM   ARCH   CQ    TE    TD
backend       OK    OK     OK    OK    OK
frontend      OK    OK     -     OK    OK
gateway       ?     ?      ?     ?     ?
shared        OK    OK     OK    -     OK
```

A Product Architecture request may consume qualified local STM/Architecture even if local CQ is absent. Product CQ synthesis must expose missing CQ authority rather than infer it from general Project readiness.

## 16. Product baseline candidate

After the child barrier, the coordinator composes an immutable Product baseline candidate from exact selected child source bindings, availability/limitations, and qualified references required by the existing Product contract.

```text
PB-N+1 candidate
  product_id: PROD-*
  product_revision: PROD-*@revN
  members:
    backend: exact source binding + qualified refs
    frontend: exact source binding + qualified refs
    ...
  limitations: ...
```

There is no synthetic Coordination Root SHA.

## 17. Second human gate — Product baseline acceptance

Child updates do not silently advance Product state.

```text
child work
  ↓
Product Baseline Candidate
  ↓
Product Baseline Acceptance Gate
  ↓
accepted immutable Product baseline
```

A failed/unavailable child may be accepted only as an explicit limitation when existing Product requiredness/coherency policy permits it. Otherwise acceptance blocks.

The two gates are distinct:

1. Coordination Plan confirmation authorizes child work.
2. Product Baseline Acceptance accepts the resulting exact composition for Product review.

## 18. Product-level analysis

After baseline acceptance, Product-scoped work may evaluate cross-project interfaces, provider/consumer relationships, integrations, end-to-end flows, data/migration dependencies, auth/trust boundaries, configuration/deployment dependencies, and Product-scoped Architecture/Test/CQ conclusions.

Authority does not move to Product context. New factual cross-project relations are accepted by the existing Technical Model Gate/STM authority with Product/member qualification. Product-scoped Architecture, Test Engineering, Code Quality, and Contract Verification conclusions remain owned by their existing capability authorities. Product context stores composition, qualification, baseline/provenance links, routing records, and references to those authoritative records.

## 19. Bidirectional coordination

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
  → Product reconciliation/impact routing
```

A new child revision never silently retargets an accepted Product baseline. It becomes a reconciliation candidate.

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
  → bottom-up reuse candidate

source unchanged, accepted semantic/capability revision advanced
  → semantic authority advancement

nothing changed
  → no child action
```

Git SHA comparison is therefore not the only freshness signal.

## 21. Product Impact Analysis

When a member advances, the coordinator does not automatically re-run all members. It requests/coordinates bounded Product impact evaluation through the existing dependency, freshness, Change Review, and capability authorities.

```text
accepted PB-N
  ↓
child advancement
  ↓
changed authoritative scope identified
  ↓
Product Impact Analysis / routing
  ↓
affected dependency slice
  ↓
minimum required Project/capability work
  ↓
PB-N+1 candidate
```

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

Product coordination exposes a compact result:

```text
UNAFFECTED
AFFECTED
UNKNOWN_IMPACT
```

These labels are routing/summary outcomes. Their evidence must come from existing authoritative dependency/freshness/capability records. `UNAFFECTED` requires sufficient accepted evidence; absence of a known edge alone is not proof. `UNKNOWN_IMPACT` opens only the minimum bounded discovery/revalidation slice needed to resolve uncertainty.

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
Product impact/revalidation records
  ↓
PB-2 candidate
  ↓
PB-2 accepted
  ↓
Product Review PR-2
```

Each Product review revision binds one immutable accepted Product baseline. Historical reviews remain reproducible after children advance.

Baseline transition provenance should record why a member vector advanced, which child actions occurred, which Product scopes were affected/unknown/unaffected, and which existing authority records support that determination.

## 24. Product coordination workspace

Because the Coordination Root may not be a repository, Product coordination state must not depend on root Git history.

A default layout may be:

```text
/projects/.architecture-code-review/
└── product/
    ├── INDEX.md
    ├── product-context.md
    ├── membership/
    ├── baselines/
    ├── coordination/
    ├── impact/
    └── projections/
```

This is a storage convention, not Product identity. An implementation may permit an explicitly configured workspace elsewhere.

The workspace stores Product context/orchestration records and references. It does not become the writer of child or cross-project technical authority.

## 25. Startup UX

### First run

From non-Git `/projects`, a request such as `проведи аудит продукта` resolves approximately as:

```text
1. recognize coordination-root candidate
2. discover child repository/source candidates
3. resolve known Project identities where possible
4. discover/qualify local audit packages
5. confirm Product context/membership
6. build Product Coordination Plan
7. obtain one plan confirmation
8. execute/reuse child actions
9. build capability readiness matrix
10. build Product Baseline Candidate
11. obtain Product baseline acceptance
12. run Product-scoped cross-project analysis
```

### Repeat run

`обнови аудит продукта` first performs cheap metadata comparison.

Example:

```text
backend: Product=A, current=B, accepted local audit=B
  → reuse existing child update + Product reconciliation

frontend: unchanged
  → NONE

shared: Product=S1, current=S2, accepted local audit=S1
  → REVALIDATE / CHANGE_REVIEW candidate
```

Useful natural-language requests include status, refresh existing children, bring all selected members current, show changes since the previous Product review, assess impact of one member, top-down update one member, or adopt an independently-updated child. Natural-language normalization never bypasses requested-work or authorization rules.

## 26. Product status view

A cheap informational status view may show:

```text
Product: PROD-42
Current baseline: PB-17

Member       Current Source  Local Audit Source  Product Binding  Action
backend      B               B                   A                RECONCILE
frontend     F1              F1                  F1               NONE
gateway      G1              G1                  G1               NONE
shared       S2              S1                  S1               REVALIDATE
```

This view is not authority.

## 27. Failure and ambiguity handling

- Competing child packages that remain ambiguous return existing previous-audit reconciliation routing; never guess by timestamp.
- `IN_PROGRESS` on an older source is not resumed as current; existing baseline mismatch semantics apply.
- Unavailable members remain explicit and are subject to existing requiredness/coherency policy.
- Partial accepted authority is reusable only for outputs whose dependencies are satisfied.
- Dirty/noncanonical member sources use existing Product baseline semantics; coordinator exposes rather than normalizes them.
- Legacy packages that fail current provenance/authority qualification remain historical context until existing migration/reconciliation rules qualify them.
- Moving a repository path does not change Project/Product identity when source identity/provenance safely resolves it.
- A newly discovered repository is a candidate only; no automatic `NEW` audit runs before membership/action confirmation.

## 28. Mandatory invariants

1. Coordination Root is not a repository, Project, Product, or semantic authority.
2. Product membership remains explicit and immutable per accepted Product revision.
3. Child Project authority remains local when work is dispatched from Product scope.
4. Product reuses authority by qualified reference; it does not clone it.
5. Cross-project technical facts/relations remain owned by existing STM/Technical Model authority, even when Product-qualified.
6. Product-scoped findings/test/CQ/contract conclusions remain owned by their existing capability authorities.
7. Product baseline is an exact immutable vector, never one synthetic root SHA.
8. Existing seven Session Intents remain unchanged.
9. Existing top-level capability set remains exactly Architecture Review, Test Engineering, and Code Quality Review.
10. Coordination labels/policies do not become Session Intents or capabilities.
11. Child advancement never silently advances Product baseline.
12. Product impact routing never automatically authorizes child work.
13. Unknown dependency is not equivalent to unaffected.
14. Reports/projections are never substitute authority.
15. Independent local audits are reusable when exact identity/source/authority/lineage/provenance qualify.
16. Product-level accumulation is composition/provenance plus qualified references to existing semantic authorities, not a new Product fact store.
17. No automatic projection regeneration follows child or Product reconciliation.

## 29. Pressure scenarios

Implementation/contract changes must cover at least these cases:

1. non-Git root with four child repos and exact accepted audits → reuse local authority, perform only missing Product work;
2. one child source advanced but local audit stale → offer bounded Change Review/Revalidation, not full Product rescan;
3. one child independently revalidated → detect and offer Product reconciliation without repeating child analysis;
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
16. nested submodule/worktree → explicit source semantics, no auto sibling member;
17. vendor/example repo under root → candidate only, not automatic member;
18. local STM/Architecture current but CQ missing → architecture reuse allowed, CQ dependency remains missing;
19. local projection stale but semantic authority current → semantic reuse independent of projection freshness;
20. backend interface changes → use dependency graph to reopen only consumers/routes/unknown slices;
21. dependency coverage incomplete for legacy tool → `UNKNOWN_IMPACT`, not `UNAFFECTED`;
22. accepted dependency evidence proves no path to shared library → shared remains `UNAFFECTED`;
23. local semantic authority advances on same source commit → Product detects semantic advancement;
24. historical PB-1 remains reproducible while children advance;
25. user says “analyze everything” from root → membership and plan confirmation still precede substantive work;
26. Product membership changes → new accepted Product revision, no historical mutation;
27. same Product revision with newer member sources → new immutable Product baseline;
28. one child update blocks → explicit readiness/limitation, unrelated ready members still reusable;
29. child finding IDs collide → references remain Project-qualified;
30. Product-qualified relation becomes stale after member update → existing technical/freshness owner revalidates it rather than Product context cloning a fact.

## 30. Contract integration points

Implementation should extend existing contracts rather than build a parallel framework. Primary integration points are expected to include:

- `references/session-orchestration.md` for coordination-root startup, federated child discovery, plan routing, and human authorization boundaries;
- `references/product-multi-project-review.md` for Product context/workspace, member qualification, baseline candidate composition, readiness, and reuse composition;
- `references/revalidation-and-freshness.md` for substantive freshness/impact/revalidation semantics;
- Shared Technical Model and dependency contracts for Product-qualified cross-project facts/relations and dependency evidence;
- Change Review contracts for changed-member candidate analysis/reconciliation eligibility;
- capability contracts for Product-scoped Architecture/Test/CQ/Contract conclusions;
- projection/package contracts for Product projections/packages without automatic regeneration.

A focused additional reference is acceptable if clearer, but it must remain orchestration/contract documentation and must not create new semantic ownership.

## 31. Validation strategy

This is a Markdown skill/reference repository. Validation should emphasize contract consistency and existing static/acceptance checks rather than inventing a runtime harness.

At minimum verify:

- no new Session Intent or top-level capability;
- no generic Product technical-fact authority;
- Product baseline remains exact-vector based;
- Product membership remains explicit;
- child/local and cross-project authority ownership remains with existing owners;
- previous-audit qualification semantics are reused;
- Change Review/Revalidation remain explicit and non-automatic;
- Product baseline acceptance remains human-controlled;
- `UNAFFECTED | AFFECTED | UNKNOWN_IMPACT` routing does not infer unaffected from missing evidence;
- top-down, bottom-up, partial, ambiguous, unavailable, multi-repo/monorepo, and independently-updated child scenarios are covered.

Do not build a new runtime scanner/test harness merely to validate this textual contract.

## 32. Success criteria

The design succeeds when a user can start from a plain non-Git coordination root and safely:

1. recognize the root as a coordination boundary rather than one repository;
2. discover child repositories/Projects cheaply;
3. discover and qualify existing child audit packages;
4. present one editable Product Coordination Plan;
5. reuse/resume/revalidate/change-review/create selected child audits through existing workflows;
6. execute independent child work in parallel where appropriate;
7. summarize capability-level readiness/limitations;
8. compose and explicitly accept an immutable Product baseline vector;
9. run cross-project Product review without duplicating semantic authority;
10. detect later source or semantic-authority advancement;
11. assess impact incrementally and reopen only affected/unknown slices;
12. reuse independently-created child analysis bottom-up;
13. preserve exact provenance and historical reproducibility.

## 33. Implementation boundary

This document approves design only. No implementation plan or implementation work is authorized by the spec itself.

After written-spec review and explicit user approval, the next process step is the `writing-plans` workflow. The implementation plan must preserve minimum-slice behavior and prefer focused contract edits plus existing validation over new framework construction.
