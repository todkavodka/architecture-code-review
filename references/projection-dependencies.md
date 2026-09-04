# Projection dependency contracts

This reference specializes the Stage A dependency model for fully generated
projections. It defines the dependency kinds, selector boundaries, projection
dependency direction, and the graph scope used by projection impact and
regeneration. It does not make a projection, generated index, or selector
resolution a semantic authority.

## 1. Dependency kinds

Stage B accepts exactly these dependency kinds:

```text
SEMANTIC_EXACT
SEMANTIC_SELECTOR
PROJECTION_EXACT
```

### `SEMANTIC_EXACT`

An exact dependency names one accepted semantic object and the revision used
by the projection contract. Examples include `RF-041@rev3`, `IF-021@rev4`, and
`INT-008@rev2`. A changed, superseded, missing, stale, or conflicting object
invalidates the dependent projection's freshness proof and is recorded as
impact for that projection.

### `SEMANTIC_SELECTOR`

A selector dependency names a controlled, deterministic contract whose
resolved membership is a set of accepted semantic object identities and
revisions. It is appropriate when completeness depends on dynamic membership,
for example all accepted interfaces with a formally recorded direction.

The selector contract and the successful-generation resolution snapshot are
both required. The contract says what may match; the snapshot says exactly
which members and revisions were consumed. Comparing a later resolution with
that snapshot detects additions and removals that exact-only dependencies
cannot detect.

### `PROJECTION_EXACT`

A projection dependency names a direct upstream projection identity and the
verified revision consumed by the downstream projection. If projection B
consumes projection A, B declares `PRJ-B -> PRJ-A`; B does not copy A's
transitive semantic dependencies unless B consumes those objects independently.
The downstream projection is not current when the required upstream projection
revision changes or its freshness is no longer proven. A verified upstream
revision change records `UPSTREAM_PROJECTION_REVISION_CHANGED` and marks the
downstream projection `STALE` until its own dependency snapshot is verified.

## 2. Direct dependency authority and edge direction

The Stage A authority rule remains unchanged: the consuming artifact owns its
direct outbound dependency metadata. A registry or reverse index may be
generated from that metadata, but it is never the source of truth.

For every Stage B dependency, the canonical edge is:

```text
CONSUMER -> PREREQUISITE
```

The arrow means dependency, not production or data-flow direction. Therefore:

```text
PRJ-C -> PRJ-B -> PRJ-A

C consumes B
B consumes A

prerequisite-first execution:
A, B, C
```

Following declared outbound edges from a consumer finds its upstream
prerequisites. When a prerequisite changes, dependent impact is traversed in
the opposite operational direction only through a reverse graph derived from
consumer-owned metadata:

```text
declared prerequisite traversal:  consumer -> prerequisite
derived dependent traversal:      prerequisite -> consumer
```

The reverse graph must be rebuildable from direct metadata. It must not be
written back as if it were direct dependency authority.

## 3. Controlled selector contract

Selectors are small, structured, deterministic predicates over authoritative
records. The initial selector dimensions are limited to:

```text
entity_type
accepted status
freshness where formally meaningful
structured properties
formal relations
capability owner
```

A selector must identify its authoritative record type, allowed dimensions,
comparison operators, and stable ordering for resolved members. Resolution
must use accepted authority and formal metadata. Free-form semantic
interpretation is not a selector mechanism.

The selector language explicitly forbids:

```text
free-form semantic interpretation
SQL
JMESPath
arbitrary scripts
```

Selectors must not execute code, query an unbounded store, or infer meaning
from prose, filenames, paths, or generated projection text. If a needed
condition cannot be represented by the controlled dimensions and formal
relations, the dependency requires an explicit semantic dependency or a
contract change owned by the appropriate authority.

## 4. Selector resolution snapshots

Each successful projection generation persists both records:

```text
selector_contract:
  <canonical controlled selector and contract revision>

resolved_membership:
  <stable ordered set of semantic object IDs and consumed revisions>
```

The snapshot is part of the projection's dependency/freshness evidence. A
later run re-evaluates the selector against current accepted authority and
compares the result with the stored snapshot.

Handle membership and revision changes separately:

```text
member added
  -> record SELECTOR_MEMBER_ADDED
  -> mark every dependent projection STALE

member removed
  -> record SELECTOR_MEMBER_REMOVED
  -> mark every dependent projection STALE

member revision changed
  -> record SELECTOR_MEMBER_REVISION_CHANGED
  -> mark every dependent projection STALE
```

A changed selector contract is also a dependency change and requires
regeneration under the new contract. Inspecting only the IDs in the previous
snapshot is insufficient: additions and removals must be detected by
re-resolving the controlled selector.

## 5. Projection prerequisite graph

The projection regeneration prerequisite graph contains `PROJECTION_EXACT`
edges and any projection-level prerequisites required by the active
regeneration plan. It must be a DAG. A cycle is reported as:

```text
PROJECTION_DEPENDENCY_CYCLE
```

For example, this is a cycle under the canonical convention:

```text
PRJ-A -> PRJ-C
PRJ-B -> PRJ-A
PRJ-C -> PRJ-B
```

Only the projection regeneration prerequisite graph is required to be
acyclic. The broader semantic/artifact graph may contain legitimate cycles;
those cycles are not silently reinterpreted as projection regeneration edges.

Topological execution always schedules prerequisites before consumers. A
targeted plan follows consumer-to-prerequisite edges and includes only the
required stale or blocking upstream prerequisites; a currently valid
prerequisite is not regenerated merely because it is in transitive closure.
For the canonical chain, a `TARGETED(PRJ-C)` plan may expand to stale or
blocking `PRJ-B` and `PRJ-A`, then execute `PRJ-A`, `PRJ-B`, `PRJ-C`. Downstream
dependents found through reverse impact traversal are not added to that
targeted prerequisite closure merely because they are affected.

An `ALL_STALE` plan, when used by the regeneration layer, freezes the set of
stale projections and dependency/revision state at planning time. Projections
that become stale after that snapshot are recorded for a later plan rather
than silently expanding the running plan. This is a scope rule over the DAG,
not a change to the canonical edge direction.
