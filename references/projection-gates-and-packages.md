# Projection freshness gates and packages

This reference owns gate-scoped projection freshness and named projection
package semantics. It consumes the projection lifecycle, dependency, impact,
regeneration, and verification contracts. It does not own projection meaning,
semantic authority, or regeneration execution.

## 1. Scope and authority

A projection package is a named, non-authoritative deliverable scope. It is a
closeout boundary for a capability or endpoint, not a semantic model and not a
second source of truth. The package owner declares its membership and the gate
that consumes it. A package cannot promote projection prose, generated indexes,
or file paths to authority.

Projection freshness is evaluated against the requested gate and its declared
package scope. There is no repository-wide rule that all projections must be
`CURRENT` before any work may close out.

## 2. Freshness policies

The coordinator records exactly one policy for each projection-sensitive gate:

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

### `PERMISSIVE`

Stale or blocked projections may exist and do not block ordinary semantic work
or a gate that does not consume them. The state remains visible and is carried
as deferred projection work. This policy does not permit a stale projection to
be used as fresh downstream input.

### `REQUIRED_SCOPE_CURRENT`

The specific projection being consumed and every mandatory upstream projection
prerequisite in its declared dependency closure must be `CURRENT`. Projections
outside that closure, including other members of the same broader capability,
do not block this gate.

### `ALL_SCOPED_CURRENT`

Every member resolved as required for the named package must be `CURRENT`,
including each member's mandatory upstream projection prerequisites. Optional
members do not become required merely because they exist. A controlled
conditional member is required only when its explicit condition resolves true
for this package instance.

`STALE` and `BLOCKED` are both non-current. A `BLOCKED` required prerequisite
propagates the applicable blocking action from the projection lifecycle or its
owning semantic/contract gate; it is not repaired by treating the projection as
optional.

## 3. Package contract

Each package has a stable declaration owned by the capability or endpoint that
publishes it:

```text
package_id: <stable package name>
owner: <capability or endpoint owner>
gate: <closeout/publication gate>
freshness_policy: PERMISSIVE | REQUIRED_SCOPE_CURRENT | ALL_SCOPED_CURRENT
required_members:
  - projection_id: PRJ-<stable-id>
    purpose: <why this projection is consumed>
    mandatory_prerequisites: [PRJ-<stable-id> ...]
optional_members:
  - projection_id: PRJ-<stable-id>
    purpose: <available but not required for this package instance>
conditional_members:
  - condition_id: <controlled condition name>
    when: <bounded capability/output/topology condition>
    projection_id: PRJ-<stable-id>
    mandatory_prerequisites: [PRJ-<stable-id> ...]
```

`required_members`, `optional_members`, and `conditional_members` are explicit
finite lists. A package must not introduce arbitrary selector expressions,
path globs, filename conventions, or prose queries to calculate membership.
Selectors remain valid inside a projection's dependency contract where the
projection contract defines and snapshots that selector; they do not define
package membership.

Before a gate is evaluated, the coordinator persists one resolved membership
snapshot:

```text
package_membership:
  package_id: <stable package name>
  declaration_revision: <package contract revision>
  resolved_at: <session/event identity>
  required: [PRJ-<id>@<verified-revision> ...]
  optional: [PRJ-<id>@<verified-revision> ...]
  conditional:
    - condition_id: <condition>
      resolved: true | false
      projection: PRJ-<id>@<verified-revision> | NOT_REQUIRED
```

The snapshot is the gate input. A changed package declaration, output
selection, or controlled condition requires membership resolution again and
must not silently widen or narrow an in-flight gate. Missing or ambiguous
membership is a package-contract failure and blocks the package gate until the
owner resolves it.

## 4. Closeout and publication chain

Projection-sensitive closeout follows this order:

```text
semantic gates accepted
→ PROJECTION_IMPACT_ACCOUNTED
→ package membership resolved
→ required scoped projections CURRENT
→ closeout/publication permitted
```

`PROJECTION_IMPACT_ACCOUNTED` means that the stabilized accepted semantic delta
was evaluated against the applicable projection dependencies, selectors,
contracts, drift, missing files, and upstream freshness, and the results were
persisted. It does not mean that all projections are current or that
regeneration occurred.

The package gate may not consume a projection until the projection's accepted
revision passed the required verification gates and its dependency snapshot is
fresh. A failed or incomplete impact pass keeps projection-sensitive closeout
blocked without rolling back accepted semantic authority.

For `PERMISSIVE`, the chain ends with semantic closeout after impact accounting;
stale projection work is visible and deferred. For `REQUIRED_SCOPE_CURRENT`,
only the consumed projection closure is checked. For `ALL_SCOPED_CURRENT`, all
resolved required package members are checked. Regeneration remains an explicit
`RG-*` workflow and is never started implicitly by this gate.

## 5. Unrelated stale projections

Every gate report and persisted package snapshot must retain visible status for
stale or blocked projections outside the gate's required scope. Visibility
includes the projection identity, freshness, active reason, and required action
when known. Visibility is not membership and does not create a blocking
dependency.

Therefore, if package A is the requested scope and an unrelated projection in
package B is `STALE`, package A may close out when its own policy and required
projection closure pass. A coordinator must not apply a global zero-stale
predicate, hide package B's stale state, or use package B's projection as a
substitute for package A's required evidence.

Conversely, a stale or blocked projection named in the resolved required scope
blocks that package gate. The block is scoped to that gate; it does not reopen
unrelated accepted capability stages.

## 6. Gate result record

The coordinator persists enough information to reproduce the decision:

```text
projection_gate:
  gate_id: <stable gate/event identity>
  package_id: <stable package name or NONE>
  policy: PERMISSIVE | REQUIRED_SCOPE_CURRENT | ALL_SCOPED_CURRENT
  impact_status: PROJECTION_IMPACT_ACCOUNTED | ACCOUNTING_FAILED
  membership_revision: <package declaration revision>
  required_scope: [PRJ-<id> ...]
  current_scope: [PRJ-<id> ...]
  non_current_required: [PRJ-<id> ...]
  unrelated_non_current: [PRJ-<id> ...]
  result: PERMITTED | BLOCKED | NOT_APPLICABLE
```

`PERMITTED` is valid only when every required condition for the selected policy
is satisfied. `BLOCKED` preserves the blocking projection and owning action;
it is not a semantic verdict about the projection's visible content.
