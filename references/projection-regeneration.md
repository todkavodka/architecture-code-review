# Projection regeneration workflow

This reference owns deterministic planning and execution of fully generated
projection regeneration. It consumes projection lifecycle, dependency, and
impact records; it does not change semantic authority, classify projections,
or define projection verification criteria.

Regeneration is separately requested after projection impact has been
accounted for. `PROJECTION_IMPACT_ACCOUNTED` records known impact, not a
request to regenerate or a claim that every projection is current.

## 1. Regeneration session identity

Each planned regeneration session has an operational identity:

```text
RG-<stable-session-id>
```

`RG-*` identifies one execution/history record: its frozen plan, inputs,
attempts, state transitions, and outcome. It is not a projection content
identity, projection revision, semantic identity, or Git commit identity:

```text
RG-* != PRJ-*
RG-* != PRJ-*@revN
RG-* != semantic authority identity
RG-* != Git commit
```

An `RG-*` record preserves the plan that was actually executed. Retrying after
an execution failure creates a new `RG-*` plan rather than mutating the old
history into a different execution.

## 2. Planning modes and scope

Planning operates only on active, explicitly classified `PRJ-*` identities and
their consumer-owned `PROJECTION_EXACT` metadata. The canonical declared edge
remains:

```text
CONSUMER -> PREREQUISITE
```

Following outbound edges from a consumer finds its upstream prerequisites.
Reverse impact edges are not direct dependency authority and never add a
downstream consumer to a regeneration plan.

### `TARGETED`

`TARGETED` starts with the explicitly requested projection targets. Its scope
is exactly:

```text
requested targets
+ required stale or BLOCKED projection prerequisites reachable upstream
```

For each target, expand only through outbound `CONSUMER -> PREREQUISITE` edges.
Include an upstream projection only when the target cannot be safely restored
without regenerating or resolving that stale/BLOCKED prerequisite. Record a
current prerequisite as `SKIPPED_CURRENT`; do not regenerate it merely because
it is in transitive closure. Do not add reverse-reachable downstream consumers,
unrelated stale projections, or semantic work to the plan.

For example, for `PRJ-C -> PRJ-B -> PRJ-A`, a `TARGETED(PRJ-C)` plan can include
`PRJ-C` plus stale `PRJ-B` and `PRJ-A`, then execute `A, B, C`. A downstream
projection that consumes `C` remains outside this plan even if impact analysis
has marked it stale.

### `ALL_STALE`

`ALL_STALE` first takes one stale-at-planning snapshot of active projections.
The snapshot set, plus any required stale/BLOCKED upstream prerequisites needed
by its members, is the only candidate execution scope. Current prerequisites
are recorded as `SKIPPED_CURRENT` rather than regenerated.

`ALL_STALE` is not a loop that continues until repository-global freshness. A
projection that becomes stale after the snapshot is recorded as deferred for a
later regeneration plan unless it was already frozen in scope. An in-scope
input drift is handled by the drift rules below, not by silently adding work.

## 3. Frozen regeneration plan

Before any generation begins, persist a complete, immutable plan under its
`RG-*` identity. At minimum it freezes:

```text
mode: TARGETED | ALL_STALE
requested_targets: ordered PRJ-* set
stale_snapshot: ordered PRJ-* set for ALL_STALE
expanded_prerequisites: ordered PRJ-* set and inclusion reason
skipped_current_prerequisites: ordered PRJ-* set and freshness proof
input_revisions: semantic exact revisions, selector contracts/resolutions,
                 projection contract revisions, and upstream projection revisions
dependency_snapshot: direct consumer-owned metadata used for the plan
execution_dag: in-scope vertices and declared prerequisite edges
execution_order: deterministic prerequisite-first topological order
```

The plan also records the input/freshness observations that justified each
member's inclusion, skip, or pre-execution block. Stable identity ordering is
the deterministic tie-breaker among independent ready vertices.

No later discovery may rewrite `requested_targets`, expand the closure, replace
an input revision, or alter the DAG/order of the frozen `RG-*`. Newly stale
out-of-scope projections are retained as deferred work. A retry or a request
with a different scope or input snapshot is a new `RG-*` session.

## 4. Prerequisite-first DAG execution

The in-scope projection prerequisite graph must be acyclic. A detected cycle
is `PROJECTION_DEPENDENCY_CYCLE`: do not choose an arbitrary order or attempt
partial generation within that cyclic component.

Topological ordering reverses the declared dependency direction for execution.
For the canonical chain:

```text
PRJ-C -> PRJ-B -> PRJ-A

execution: PRJ-A, PRJ-B, PRJ-C
```

A consumer becomes `READY` only after every in-scope required prerequisite has
reached a successful terminal state. Independent `READY` branches may execute
concurrently, but their records and outcome are deterministic. A current
prerequisite outside execution work may satisfy the dependency only when its
frozen freshness proof and consumed revision still match.

## 5. Execution states

The following states describe work inside one `RG-*` session. They are
orthogonal to the persistent lifecycle freshness `CURRENT | STALE | BLOCKED`;
in particular, `REGENERATED` and `VERIFIED` are not aliases for `CURRENT`.

| State | Meaning |
|---|---|
| `PENDING` | Frozen in scope but not yet eligible to run. |
| `READY` | All required frozen prerequisites succeeded or are proven current at their frozen revisions. |
| `RUNNING` | Candidate generation or its required verification is in progress. |
| `REGENERATED` | Candidate output was produced; it has not yet completed the required verification/publication path. |
| `VERIFIED` | Candidate completed the applicable verification path and its accepted lifecycle result was persisted. |
| `RECONCILED_NO_CHANGE` | Regeneration verified byte-identical canonical output; the existing `PRJ-*@revN` remains and no downstream revision impact is created. |
| `FAILED` | Generation, required verification, persistence, cycle detection, or frozen-input check failed for this projection. |
| `BLOCKED_UPSTREAM` | A required in-scope prerequisite failed, drifted, or is structurally blocked, so this consumer cannot safely run. |
| `SKIPPED_CURRENT` | A prerequisite was considered by closure planning but remained proven current at its frozen consumed revision and was not regenerated. |

Normal execution transitions are:

```text
PENDING -> READY -> RUNNING -> REGENERATED -> VERIFIED
                                      \-> RECONCILED_NO_CHANGE
                         \------------> FAILED
PENDING -> BLOCKED_UPSTREAM | SKIPPED_CURRENT
```

`FAILED` never creates an accepted projection revision. A downstream consumer
cannot use a failed candidate as an upstream revision. The lifecycle contract
alone determines whether the persistent freshness after a terminal state is
`CURRENT`, `STALE`, or `BLOCKED`.

## 6. Failure isolation and session outcome

Failure is isolated to the failed projection and its dependent in-scope
subtree. Mark only consumers that require the failed prerequisite
`BLOCKED_UPSTREAM`; keep independent `READY` branches eligible to run. Never
roll back an independent projection that already reached `VERIFIED` or
`RECONCILED_NO_CHANGE`, and never publish a failed candidate revision.

The `RG-*` outcome is exactly one of:

| Outcome | Meaning |
|---|---|
| `COMPLETE` | Every non-skipped in-scope projection reached `VERIFIED` or `RECONCILED_NO_CHANGE`. |
| `PARTIAL` | At least one independent projection reached a successful terminal state and at least one in-scope projection is `FAILED` or `BLOCKED_UPSTREAM`. |
| `BLOCKED` | No in-scope projection could successfully complete because required prerequisites or plan structure blocked execution. |
| `NO_OP` | Planning found no execution work: every considered target/prerequisite was already proven current and recorded `SKIPPED_CURRENT`. |

`COMPLETE` and `NO_OP` describe only the frozen scope. Neither asserts that
projections outside the plan are current.

## 7. Frozen-input drift

Before generation and before accepting a candidate, compare the frozen input
record with the currently resolved required semantic revisions, selector
membership/revisions, projection contract revision, and upstream verified
projection revisions. An unexpected difference is:

```text
REGENERATION_INPUT_DRIFT
```

Persist both planned and observed values and the affected `PRJ-*`. Do not
silently substitute the new value, extend scope, or reorder the plan. The
affected work item becomes `FAILED`; in-scope consumers that require it become
`BLOCKED_UPSTREAM`. The changed or newly stale work is deferred to a later
`RG-*` plan after normal impact accounting establishes its new freshness state.

Drift discovered outside frozen scope is recorded/deferred and does not alter
the running plan. A verified candidate may be accepted only against the exact
frozen inputs it was generated from; accepting it against observed drift would
misrepresent its dependency snapshot.
