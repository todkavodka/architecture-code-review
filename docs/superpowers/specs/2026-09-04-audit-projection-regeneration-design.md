# Stage B — Audit Projection & Regeneration

Status: DESIGN CANDIDATE

Baseline:

```text
main@0ba7c4b5b556ba0de78200d6a6792b408b42523b
```

Stage A is complete and establishes Shared Evidence, the persistent Shared Technical Model (STM), Technical Model Gate, STM coverage, dependency/index infrastructure, Architecture Review consumption of STM, Technical Documentation projections, Test Engineering targeted STM acquisition, and impact-driven EXTEND/REVALIDATE foundations.

Stage B adds a shared lifecycle for non-authoritative projections derived from those semantic authorities.

---

## 1. Purpose

Stage B solves one problem:

> When accepted semantic authority changes, derived documents and indexes may become stale. The system needs one explicit mechanism to detect that impact, persist projection freshness, regenerate only the required projections in dependency order, verify the generated result, and enforce freshness only at the gates that actually require those projections.

The intended flow is:

```text
Semantic Authorities
  STM
  Architecture semantics
  Test Engineering semantics
  future capability semantics
        |
        | accepted/stabilized semantic changes
        v
Projection Impact Analysis
        |
        +--> unaffected
        |
        +--> affected -> STALE/BLOCKED
                        |
                        | separate explicit process
                        v
                Regeneration Planner
                        |
                        v
                  Execution DAG
                        |
                        v
                   Verification
                        |
                        v
                     CURRENT
```

Stage B is not a new semantic authority. It is a projection lifecycle/orchestration layer.

---

## 2. Projection definition and classes

A **Projection** is any derived, non-authoritative artifact that can be reconstructed from semantic authority, other projections, and its projection contract.

Initial classes:

```text
USER_PROJECTION
CAPABILITY_PROJECTION
WORKFLOW_PROJECTION
DERIVED_INDEX
```

Examples:

- USER_PROJECTION: final Architecture Review report, Technical Documentation.
- CAPABILITY_PROJECTION: Architecture As-Built projection, Test Assurance Map, Test Plan.
- WORKFLOW_PROJECTION: generated handoff, compact workflow summary, projection registry view.
- DERIVED_INDEX: reverse dependency index, artifact registry, stale-impact view.

Core invariant:

```text
projection != semantic authority
```

Projection class may affect policy or presentation, but never authority.

---

## 3. Ownership boundary

Capability owners define **what a projection means**.

A capability-owned projection contract defines:

- projection content semantics;
- required and optional sections;
- semantic exact dependencies;
- semantic selector dependencies;
- direct upstream projection dependencies;
- domain-specific completeness rules;
- rendering rules;
- package membership and controlled conditional membership.

The shared Stage B Projection Layer defines **how a projection lives**:

- projection identity and revisioning;
- freshness;
- direct dependency lifecycle metadata;
- selector resolution snapshots;
- stale reasons;
- impact propagation;
- regeneration planning;
- DAG execution;
- verification lifecycle;
- fingerprints;
- package freshness gates;
- regeneration session state.

Invariant:

```text
Capability owns WHAT.
Projection Layer owns HOW IT LIVES.
```

The Projection Layer must never invent missing capability semantics.

If a projection needs authority that is absent, stale, conflicting, or unresolved, Stage B blocks the projection and returns to the owning semantic gate.

Examples:

```text
STM conflict -> Technical Model Gate
Architecture semantic conflict -> Architecture authority workflow
BC/CC conflict -> Test Engineering owning gate
```

---

## 4. Layering and authority flow

The shared model remains:

```text
L0 Repository / external sources
        v
L1 Shared Evidence
        v
L2 Shared Technical Model
        v
L3 Capability Semantic Authority
        v
L4 Projection contracts / dependency lifecycle
        v
L5 Generated Projections
```

Stage B operates between L3 and L5 as lifecycle/orchestration, not as another semantic layer.

Two mandatory boundaries:

```text
projection content must not mutate semantic authority
```

and:

```text
semantic changes must not implicitly rewrite projection content
```

---

## 5. No automatic regeneration

Accepted semantic change does **not** automatically rewrite derived documents.

The semantic workflow first stabilizes its own authority. Then one Projection Impact Analysis pass calculates projection impact and persists freshness.

```text
semantic workflow
  -> semantic gates accepted
  -> semantic state stabilizes
  -> Projection Impact Analysis
  -> projection freshness persisted
  -> semantic workflow may close
```

A valid end state is:

```text
semantic authority: ACCEPTED / VALID
projections: some CURRENT, some STALE
```

Regeneration is always a separate explicit process.

Invariants:

```text
semantic workflow may mark projections stale
but must not regenerate them implicitly
```

```text
projection regeneration may update projections
but must not mutate semantic authority
```

---

## 6. Regeneration, repair, semantic revalidation

The three operations have different meaning.

### REGENERATE

Use when accepted authority, dependency membership, upstream projection revision, or projection contract changed and the projection can be rebuilt deterministically.

### PROJECTION_REPAIR

A narrow infrastructure-only mechanism for projection mechanics while semantic authority is unchanged, for example:

- broken generated reference;
- invalid generated metadata;
- corrupt derived index;
- broken generated Mermaid or equivalent rendering metadata.

It is not a generic “fix document” operation.

### SEMANTIC_REVALIDATION

Use when regeneration cannot proceed because the authority itself is stale, missing, conflicting, or unresolved.

Invariant:

```text
Projection follows authority.
Authority never follows projection merely to make documents consistent.
```

---

## 7. Fully generated projections

Generated projections contain no human-owned sections.

```text
projection = fully generated artifact
```

Anything that must survive regeneration must live in semantic authority, not in projection.

Manual edits to a generated projection are drift, not semantic input.

If the verified fingerprint differs from the current file fingerprint without a successful regeneration that produced that content:

```text
PROJECTION_CONTENT_DIVERGED
-> STALE
-> required action: REGENERATE
```

Stage B does not automatically extract the manual edit into STM, RF, BC, or any other authority.

Stage B does not create `.bak`, `.old`, or a parallel forensic archive. Git is the history of projection files; semantic authority is the history of meaning.

---

## 8. Projection identity and lifecycle

Each independently regeneratable projection has a stable logical identity:

```text
PRJ-*
```

The filesystem path is not identity.

A projection may move without receiving a new logical ID if its meaning and contract remain the same.

Projection identity lifecycle:

```text
ACTIVE
RETIRED
```

A retired `PRJ-*` ID is never reassigned to another meaning.

Freshness for ACTIVE projections is orthogonal:

```text
CURRENT
STALE
BLOCKED
```

Required action is also orthogonal:

```text
NONE
REGENERATE
PROJECTION_REPAIR
SEMANTIC_REVALIDATION
CONTRACT_ADJUDICATION
```

`BLOCKED` means the Projection Layer cannot restore CURRENT without resolving a structural prerequisite or semantic authority problem.

---

## 9. Projection revisions

Projection revisions are content identities of successfully verified projection state:

```text
PRJ-020@rev7
```

A new projection revision is created only when:

```text
generation succeeds
+ V1..V4 verification passes
+ canonical content fingerprint changed
```

If verified output is byte-identical:

```text
NO_CHANGE
-> keep revN
-> CURRENT
-> no downstream revision invalidation
```

If generation or verification fails, no new accepted projection revision is created.

Regeneration attempt/session identity is distinct:

```text
RG-* = execution/history identity
PRJ-*@revN = verified projection content identity
```

Git commit identity is also distinct from projection revision identity.

---

## 10. Projection contract revisions

A projection contract has its own revision.

If a capability changes how a projection must be built, the projection becomes stale even if semantic authority did not change:

```text
PROJECTION_CONTRACT_CHANGED
-> STALE
-> REGENERATE
```

Projection contract changes are capability-owned design changes. The Projection Layer never rewrites them automatically.

---

## 11. Dependency model

Stage B initially supports:

```text
SEMANTIC_EXACT
SEMANTIC_SELECTOR
PROJECTION_EXACT
```

### Semantic exact dependency

Examples:

```text
RF-041@rev3
IF-021@rev4
INT-008@rev2
```

### Semantic selector dependency

Used when completeness depends on dynamic membership, for example:

```text
all ACCEPTED IF-* where direction=PROVIDED
```

A selector stores both:

1. the selector contract;
2. the resolved membership at successful generation time.

This catches additions and removals that exact-only dependencies would miss.

### Projection exact dependency

A projection may consume another projection directly:

```text
PRJ-B -> PRJ-A
```

This does not make `PRJ-A` semantic authority.

Rule:

```text
declare dependency at the boundary actually consumed
```

If B consumes A, declare B -> A. Do not copy all of A's transitive semantic dependencies into B unless B actually consumes them independently.

---

## 12. Controlled selector contract

The selector language remains intentionally small and deterministic.

Initial structured dimensions may include:

- entity type;
- accepted status;
- freshness where formally meaningful;
- structured properties;
- formal relations;
- capability owner.

Selectors may only operate on already-authoritative structured properties.

Forbidden:

- SQL;
- JMESPath;
- arbitrary scripts;
- free-form semantic interpretation such as “all important interfaces” unless `important` is a formal property.

Selectors are local to their owning projection contract, for example:

```text
SEL-PRJ020-01
```

They are not independent semantic entities.

---

## 13. Direct dependency authority and generated indexes

Direct dependency metadata belongs with the consuming artifact/contract.

Reverse/global dependency graphs are generated views.

Invariant:

```text
direct dependency metadata = authority
reverse/global graph = projection/cache
```

Loss of a reverse index must not destroy dependency semantics.

---

## 14. Projection regeneration graph

Projection-to-projection dependencies are allowed, but the projection regeneration prerequisite graph must be acyclic.

```text
PRJ-A -> PRJ-B -> PRJ-C
```

is allowed.

```text
PRJ-A -> PRJ-B -> PRJ-C -> PRJ-A
```

is blocked with:

```text
PROJECTION_DEPENDENCY_CYCLE
```

The wider semantic/artifact graph may contain cycles. Only the projection regeneration prerequisite graph must be a DAG.

---

## 15. Freshness semantics and stale reasons

`CURRENT` means the projection was successfully verified against the currently required dependency snapshot, selector resolution, upstream projection revisions, and projection contract revision.

`STALE` means freshness is no longer proven. It does not mean the content is necessarily false.

Controlled stale reasons include:

### Semantic dependency causes

```text
DEPENDENCY_ADDED
DEPENDENCY_REMOVED
DEPENDENCY_SUPERSEDED
DEPENDENCY_REVISION_CHANGED
DEPENDENCY_FRESHNESS_CHANGED
```

### Selector causes

```text
SELECTOR_MEMBERSHIP_CHANGED
SELECTOR_MEMBER_REVISION_CHANGED
SELECTOR_CONTRACT_CHANGED
```

### Projection dependency causes

```text
UPSTREAM_PROJECTION_REVISION_CHANGED
UPSTREAM_PROJECTION_STALE
UPSTREAM_PROJECTION_BLOCKED
```

### Contract/drift causes

```text
PROJECTION_CONTRACT_CHANGED
PROJECTION_CONTENT_DIVERGED
PROJECTION_FILE_MISSING
PROJECTION_METADATA_INVALID
```

Verification failure reasons are tracked separately from the original stale causes.

A projection may preserve multiple unresolved stale reasons at once. Impact analysis must not erase earlier unresolved causes.

Successful verification clears current stale causes, while the regeneration/impact session history remains auditable.

---

## 16. Determinism and fingerprints

Given identical:

- semantic revisions;
- selector resolutions;
- upstream projection revisions;
- projection contract revision;

generation should produce the same canonical bytes where technically possible.

The generator must stabilize ordering and avoid run-specific values in generated content.

Operational data such as timestamps, regeneration session IDs, or execution timing belongs in lifecycle/session records, not the generated document body.

Invariant:

```text
NO_CONTENT_CHANGE
-> no new projection revision
-> no downstream revision invalidation
```

---

## 17. Projection Impact Analysis

Projection Impact Analysis runs only after semantic changes are accepted and stabilized.

It consumes semantic identities/revisions, not raw Git-path changes as semantic proof.

High-level algorithm:

```text
1. load accepted semantic delta
2. load active projection contracts
3. evaluate exact semantic dependencies
4. re-resolve semantic selectors
5. evaluate projection contract revisions
6. detect projection drift/missing artifacts
7. mark direct impacts
8. propagate STALE/BLOCKED through projection DAG
9. detect cycles
10. preserve existing unresolved stale reasons
11. persist freshness/action state
12. generate derived impact views
13. declare PROJECTION_IMPACT_ACCOUNTED
```

Projection Impact Analysis may update freshness metadata and generated impact views, but must not regenerate projections or mutate semantic authority.

---

## 18. Upstream freshness propagation

If B directly consumes A and A becomes STALE, B can no longer be safely considered CURRENT:

```text
A STALE
-> B STALE: UPSTREAM_PROJECTION_STALE
```

This expresses freshness uncertainty, not proof that B's content changed.

If A is regenerated and verifies to the same revision/content:

```text
A remains @rev7 CURRENT
```

and B's only stale cause was `UPSTREAM_PROJECTION_STALE`, B may return to CURRENT through lightweight freshness reconciliation without content regeneration.

If A verifies to a new revision:

```text
A@rev7 -> A@rev8
```

B receives:

```text
UPSTREAM_PROJECTION_REVISION_CHANGED
```

and requires regeneration.

Candidate or unverified upstream output never propagates downstream revision impact.

---

## 19. BLOCKED propagation

If an upstream projection is BLOCKED because a prerequisite cannot be restored by Stage B, required downstream projections become BLOCKED through their direct projection dependencies.

Local records store the direct blocker. Full root-cause closure is generated in impact/session views.

This keeps artifacts bounded while preserving global traceability.

---

## 20. PROJECTION_IMPACT_ACCOUNTED gate

The internal gate:

```text
PROJECTION_IMPACT_ACCOUNTED
```

means all accepted semantic changes in the current semantic session were evaluated against projection dependencies, selectors, contracts, and the resulting projection freshness state was persisted.

It does **not** mean all projections are CURRENT.

If semantic authority is accepted but Projection Impact Analysis fails technically, the semantic transaction is not rolled back. The workflow records projection impact as pending/failed.

Projection-sensitive publication gates cannot proceed until impact is accounted for.

---

## 21. Regeneration process and modes

Regeneration is separately initiated and creates an `RG-*` session.

Initial modes:

```text
TARGETED
ALL_STALE
```

### TARGETED

Explicit requested targets plus required stale upstream projection prerequisites.

### ALL_STALE

All stale projections in the frozen snapshot at planning time, plus required upstream prerequisites.

`ALL_STALE` does not loop until the repository contains zero stale projections.

Newly stale projections discovered during execution are recorded and deferred to a later regeneration session unless they were already in the frozen scope.

---

## 22. Target resolution

Regeneration targets must resolve to explicit projection identities from one of:

- projection ID;
- named projection package;
- well-defined capability projection set;
- `ALL_STALE`.

Ambiguous free-form scopes must be resolved into explicit IDs before planning.

---

## 23. Upstream closure vs downstream impact

This is a core Stage B boundary.

```text
execution scope
= requested targets
+ required stale upstream projection closure
```

Downstream consumers are not automatically added to the running regeneration session.

If a regenerated projection gets a new verified revision, its downstream consumers are marked stale through impact propagation, but remain for a later regeneration scope unless already present in the frozen plan.

Invariant:

```text
upstream closure = execution prerequisite
downstream closure = impact propagation only
```

---

## 24. Frozen regeneration plan

Before execution, the planner freezes:

- mode;
- requested targets;
- expanded upstream prerequisites;
- current projections skipped;
- dependency/revision snapshot;
- execution DAG/order.

The running plan does not silently expand when new stale projections appear.

This makes regeneration reproducible and auditable.

---

## 25. Execution states

Per projection in an `RG-*` session:

```text
PENDING
READY
RUNNING
REGENERATED
VERIFIED
FAILED
BLOCKED_UPSTREAM
SKIPPED_CURRENT
RECONCILED_NO_CHANGE
```

Execution state is not the same as persistent projection freshness.

Examples:

```text
execution: FAILED
freshness: STALE
```

```text
execution: VERIFIED
freshness: CURRENT
```

---

## 26. Topological execution and partial progress

Execution respects the projection prerequisite DAG.

Parallel execution is optional implementation detail; dependency ordering is mandatory.

Failure in one subtree must not stop independent branches.

Verified progress in independent branches is durable and is not rolled back because another branch failed.

A downstream blocked projection records its immediate blocker; session diagnostics may derive the full root failure chain.

---

## 27. Generation and verification lifecycle

For each projection:

```text
load contract
-> resolve current dependencies
-> generate candidate content
-> V1..V4 verification
-> compare verified fingerprint
```

A candidate may be temporary/in-memory/scratch. Stage B does not require a permanent candidate file.

Verified changed output creates a new projection revision.

Verified identical output produces `NO_CHANGE` and no new revision.

Failed generation/verification leaves the previous verified revision as historical state but keeps the projection STALE or BLOCKED according to the cause.

---

## 28. Verification model

Successful regeneration requires four levels:

```text
V1 STRUCTURAL
V2 DEPENDENCY / PROVENANCE
V3 CONTRACT COMPLETENESS
V4 AUTHORITY CONSISTENCY
```

### V1 — Structural

Checks required file/sections, structural validity, links/rendering metadata, and projection metadata.

### V2 — Dependency / provenance

Checks exact dependencies, selector resolutions, upstream projection revisions, `generated_from`, and provenance continuity.

### V3 — Contract completeness

Checks that the projection fully satisfies its projection contract and current selector membership.

### V4 — Authority consistency

Checks that generated content does not contradict or omit required accepted authority.

The verifier may detect a mismatch with authority but may not adjudicate authority.

If authority itself is conflicting or unresolved:

```text
VERIFICATION_BLOCKED_SEMANTIC_CONFLICT
-> owning semantic gate
```

Invariant:

```text
REGENERATED != CURRENT
```

Only successful V1..V4 can establish CURRENT.

---

## 29. Input drift and concurrency

A regeneration session is planned against a semantic/projection dependency snapshot.

If required semantic inputs or upstream projection revisions change unexpectedly during execution:

```text
REGENERATION_INPUT_DRIFT
```

The affected branch does not silently mutate the frozen plan. It is deferred to a new impact/regeneration cycle.

Stage B does not require a global regeneration lock. Snapshot/revision checking and optimistic drift detection are sufficient architectural requirements.

---

## 30. Retry semantics

A later retry normally creates a new `RG-*` session after the blocking prerequisite has been addressed.

Stage B does not perform hidden unbounded retries or mutate semantic scope during retry.

A bounded technical retry for transient execution may exist as an implementation detail but may not alter the frozen semantic/projection plan.

---

## 31. Regeneration session outcomes

An `RG-*` session ends as one of:

```text
COMPLETE
PARTIAL
BLOCKED
NO_OP
```

### COMPLETE

All projections in the frozen requested scope are CURRENT after `NEW_REVISION`, `NO_CHANGE`, or `RECONCILED_NO_CHANGE`.

### PARTIAL

Some branches succeed while others fail or remain blocked.

### BLOCKED

No required work in the requested scope can be completed because prerequisites cannot be satisfied by Stage B.

### NO_OP

All requested targets and required prerequisites are already CURRENT.

`COMPLETE` is scoped to that `RG-*`, not the repository as a whole.

---

## 32. Regeneration session record

A session record should capture at least:

- `RG-*` identity;
- mode;
- planning baseline/snapshot;
- requested targets;
- expanded upstream prerequisites;
- skipped current projections;
- execution ordering/DAG;
- per-projection before/after revision;
- execution result;
- failures/blockers;
- newly stale downstream projections discovered during the run;
- overall outcome.

This is operational audit history, not semantic authority.

---

## 33. Dependency contract completeness

If generation discovers that a projection actually consumes an input not declared by its contract, Stage B must not silently read it and continue.

Return:

```text
PROJECTION_DEPENDENCY_CONTRACT_INCOMPLETE
-> CONTRACT_ADJUDICATION
```

Invariant:

```text
Actual consumed input must be declared dependency.
```

---

## 34. Gate-scoped freshness policies

Projection freshness is evaluated against the output/gate being produced, not globally across the repository.

Initial policies:

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

### PERMISSIVE

Stale projections may exist and do not block ordinary semantic work.

### REQUIRED_SCOPE_CURRENT

Only the specific projection/output being consumed, plus mandatory upstream prerequisites, must be CURRENT.

### ALL_SCOPED_CURRENT

All required projections in a named deliverable/package must be CURRENT.

Unrelated stale projections must remain visible but must not block a gate outside their scope.

---

## 35. Projection packages

A projection package is a named deliverable scope, not semantic authority.

Example:

```text
PACKAGE: ARCHITECTURE_REVIEW
```

may define:

- explicit required projections;
- controlled conditional projections.

Package membership should remain explicit/conditional rather than use arbitrary selectors in the first Stage B version.

A publication/closeout chain is:

```text
semantic gates accepted
-> PROJECTION_IMPACT_ACCOUNTED
-> package membership resolved
-> required package projections CURRENT
-> closeout/publication allowed
```

---

## 36. Legacy projection migration

Existing generated/readable files without `PRJ-*` lifecycle metadata must not automatically become CURRENT.

Migration path:

```text
legacy projection
-> identify owning capability
-> assign stable projection identity
-> define projection contract
-> resolve declared dependencies/selectors
-> verify against accepted authority
-> establish verified fingerprint/revision
-> CURRENT
```

If required semantic authority is insufficient, the projection becomes BLOCKED and routes to semantic revalidation.

Historical human-edited projection content is not silently promoted into semantic authority.

---

## 37. Physical organization principles

The exact filesystem layout may follow existing repository patterns, but Stage B must keep three things conceptually separate:

1. capability-owned projection contracts/direct dependencies;
2. generated projection content;
3. projection lifecycle/impact/regeneration operational records.

A likely operational area is conceptually:

```text
working/projections/
  INDEX.md
  registry.md
  dependencies.md
  stale-impact.md
  sessions/RG-*.md
```

These operational views/records must not become semantic authority.

The final implementation plan may refine exact paths after checking current repository conventions.

---

## 38. Stage B scope boundary

Stage B includes:

- projection identity/lifecycle;
- dependency contracts;
- selectors and selector-resolution snapshots;
- impact analysis;
- stale/block propagation;
- regeneration planning;
- dependency-ordered execution;
- partial progress/failure isolation;
- verification;
- fingerprints/idempotency;
- package freshness gates;
- legacy projection registration/reconciliation.

Stage B does not include:

- new semantic analysis authority;
- Architecture redesign;
- Test execution engine;
- Code Quality implementation;
- executable coordinator/runtime creation;
- database/backend/API/vector infrastructure.

The repository remains Markdown/Git Skill architecture unless a later approved stage changes that decision.

---

## 39. Required pressure coverage

Stage B implementation should pressure-test at least:

1. semantic change marks affected projection stale without regenerating it;
2. selector membership addition/removal is detected;
3. projection-to-projection stale propagation works;
4. upstream verified NO_CHANGE enables downstream freshness reconciliation;
5. verified upstream new revision invalidates downstream;
6. TARGETED regenerates target plus only required stale upstream closure;
7. ALL_STALE uses a frozen start snapshot;
8. independent branch failure does not stop other branches;
9. projection dependency cycle blocks the affected graph;
10. manual projection drift is detected and disposable;
11. regeneration is deterministic/idempotent;
12. missing/stale/conflicting semantic authority blocks regeneration instead of being mutated;
13. projection cannot mutate semantic authority;
14. undeclared consumed input produces dependency-contract failure;
15. package closeout requires only scoped projections CURRENT;
16. unrelated stale projection does not block another capability gate;
17. failed candidate generation does not propagate downstream revision impact;
18. input drift does not mutate a running frozen plan;
19. legacy projection is not declared CURRENT without contract/dependency verification.

---

## 40. Core invariants

```text
Projection != semantic authority.

Impact != regeneration.

Stale != wrong.

Regenerated != current.

Regeneration attempt != projection revision.

Regeneration scope != impact closure.

Upstream closure != downstream closure.

Candidate output != accepted projection revision.

NO_CHANGE != new projection revision.

Projection dependency != semantic authority.

Direct dependencies are authoritative at the consuming boundary;
reverse/global indexes are derived.

Semantic selectors preserve both their contract and resolved membership.

Projection regeneration prerequisite graph must be acyclic.

Manual projection edits are disposable.

Anything that must survive regeneration lives in semantic authority.

Semantic workflow may finish with stale projections.

Projection Impact Analysis must finish before projection-sensitive
publication/closeout can claim freshness is accounted for.

Required projections must be CURRENT at the gate that consumes them;
unrelated stale projections do not block unrelated gates.

Same accepted inputs must produce stable output where technically possible.

No content change means no new projection revision and no downstream
revision invalidation.

A projection verifier may compare against authority but may not adjudicate authority.

Stage B never silently expands semantic scope or repairs semantic authority.
```

---

## 41. Design success criterion

Stage B is correctly designed if the system can answer, for every required derived artifact:

```text
What is this projection?
Who owns its content contract?
Which semantic/projection inputs does it actually consume?
Which exact revisions/memberships produced the current verified version?
Is it CURRENT, STALE, or BLOCKED?
Why?
What action is required?
Which projections must be regenerated before this target can be regenerated?
Which downstream projections become stale after a verified changed revision?
Can unrelated branches continue if one branch fails?
Which gate, if any, is blocked by the stale state?
```

without treating generated prose/indexes as semantic authority, without rereading or regenerating unrelated outputs by default, and without hiding uncertainty behind a broad “everything is fresh” claim.
