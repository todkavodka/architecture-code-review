# Projection impact accounting

This reference owns the Stage B impact pass between accepted semantic work and
projection regeneration. It consumes the projection identity/lifecycle rules
in [Projection lifecycle authority](projection-lifecycle.md) and the dependency
and selector rules in [Projection dependency contracts](projection-dependencies.md).
It records which projections lost a freshness proof; it does not regenerate
projections, change semantic authority, or treat projection prose as evidence.

## 1. Stabilized semantic-delta input

Impact analysis runs once the semantic workflow has reached a stabilized
decision for the selected baseline. Its input is a deterministic delta record,
not an unreviewed Git diff:

```text
semantic_delta:
  baseline_revision: <accepted source/baseline identity>
  current_revision: <selected source/baseline identity>
  accepted_changes:
    - semantic_id: <stable accepted RF/STM/BC/etc. identity>
      previous_revision: <revision or ABSENT>
      current_revision: <revision or ABSENT>
      change_kind: ADDED | REMOVED | SUPERSEDED | REVISION_CHANGED | STATUS_CHANGED
      authority_ref: <owning accepted artifact + revision>
  contract_changes:
    - contract_change_id: <stable contract-change identity>
      contract_id: <stable projection contract identity>
      contract_kind: PROJECTION | SELECTOR
      selector_id: <selector identity when contract_kind is SELECTOR>
      previous_revision: <revision>
      current_revision: <revision>
      authority_ref: <owning contract authority + revision>
  selector_resolutions:
    - selector_id: <controlled selector identity>
      contract_change_id: <matching contract_changes identity, or NONE>
      previous_contract_revision: <revision>
      current_contract_revision: <revision>
      contract_revision: <revision>
      previous_membership: [<semantic_id>@<revision> ...]
      current_membership: [<semantic_id>@<revision> ...]
```

`accepted_changes` contains only accepted, revision-bound semantic identity
changes. A changed path, file timestamp, generated index, or projection text
may route investigation to a candidate but cannot by itself establish semantic
impact. A missing, stale, conflicting, or otherwise unaccepted authority is
an unresolved input: record the authority problem and route the affected
projection to `SEMANTIC_REVALIDATION`/`BLOCKED` rather than guessing.

Inputs are canonicalized before comparison: stable IDs are compared by exact
identity, revisions are compared as opaque authority revisions, and selector
memberships are compared as stable ordered sets of identity-plus-revision
tuples. The same stabilized input and dependency snapshot must produce the
same impact records and statuses.

## 2. Direct impact analysis

Evaluate every active projection against its consumer-owned direct dependency
metadata, current selector resolution, contract revision, and verified content
fingerprint. Emit a direct impact record before propagation. A projection is
directly impacted when any of these conditions holds:

| Input difference or observation | Required reason | Result |
|---|---|---|
| An exact semantic dependency is newly present | `DEPENDENCY_ADDED` | `STALE`, `REGENERATE` when inputs remain usable |
| An exact semantic dependency is no longer present | `DEPENDENCY_REMOVED` | `STALE`, `REGENERATE` when inputs remain usable |
| An exact semantic dependency is superseded by another accepted identity | `DEPENDENCY_SUPERSEDED` | `STALE`, `REGENERATE` when inputs remain usable |
| An exact semantic dependency's accepted revision changes | `DEPENDENCY_REVISION_CHANGED` | `STALE`, `REGENERATE` when inputs remain usable |
| An exact semantic dependency's accepted freshness/status changes | `DEPENDENCY_FRESHNESS_CHANGED` | `STALE`, `REGENERATE` when inputs remain usable |
| A projection contract revision changes | `PROJECTION_CONTRACT_CHANGED` | `STALE`, `REGENERATE` |
| A selector contract revision changes | `SELECTOR_CONTRACT_CHANGED` | `STALE`, `REGENERATE` |
| Selector resolved membership changes (addition or removal) | `SELECTOR_MEMBERSHIP_CHANGED` | `STALE`, `REGENERATE` |
| A retained selector member's consumed revision changes | `SELECTOR_MEMBER_REVISION_CHANGED` | `STALE`, `REGENERATE` |
| A required upstream projection revision changes | `UPSTREAM_PROJECTION_REVISION_CHANGED` | `STALE`, `REGENERATE` when usable |
| A required upstream projection is no longer fresh | `UPSTREAM_PROJECTION_STALE` | `STALE`, `REGENERATE` when usable |
| A required upstream projection is `BLOCKED` | `UPSTREAM_PROJECTION_BLOCKED` | `BLOCKED`, same owning semantic/contract action as the blocker |
| Current content differs from the verified fingerprint | `PROJECTION_CONTENT_DIVERGED` | `STALE`, `REGENERATE` |
| The classified projection file is absent | `PROJECTION_FILE_MISSING` | `STALE`, `REGENERATE` |
| Required authority is missing, stale, conflicting, or unresolved | `DEPENDENCY_FRESHNESS_CHANGED` | `BLOCKED`, `SEMANTIC_REVALIDATION` |
| Classification/contract is disputed or insufficient to determine build behavior | `PROJECTION_METADATA_INVALID` | `BLOCKED`, `CONTRACT_ADJUDICATION` |

The mapping above is deterministic: `accepted_changes.change_kind` maps
`ADDED` to `DEPENDENCY_ADDED`, `REMOVED` to `DEPENDENCY_REMOVED`,
`SUPERSEDED` to `DEPENDENCY_SUPERSEDED`, `REVISION_CHANGED` to
`DEPENDENCY_REVISION_CHANGED`, and `STATUS_CHANGED` to
`DEPENDENCY_FRESHNESS_CHANGED`. A change that cannot be classified by this
mapping is unresolved authority and uses `DEPENDENCY_FRESHNESS_CHANGED` with
`SEMANTIC_REVALIDATION`.
The exact reason may include the affected dependency ID and
`previous_revision -> current_revision`; the reason code remains stable.

Selector contract detection is explicit. For every selector resolution, the
analyzer compares `previous_contract_revision` with
`current_contract_revision`, requires `contract_change_id` to identify the
matching `contract_changes` record when they differ, and emits
`SELECTOR_CONTRACT_CHANGED` for that bound change. `contract_revision` is the
current consumed revision and must equal `current_contract_revision`; a
mismatch is `PROJECTION_METADATA_INVALID` with `CONTRACT_ADJUDICATION`. A selector is re-resolved
against accepted authority every pass. Comparing only old member IDs is
insufficient because membership and member-revision changes also invalidate
the consumer's freshness proof.

Direct impact does not rewrite the projection file or create a projection
revision. It persists at least:

```text
impact_record:
  projection_id: PRJ-<stable-id>
  analyzed_input_revision: <stabilized semantic-delta identity>
  direct_reasons: [<unique reason records>]
  freshness: STALE | BLOCKED
  required_action: REGENERATE | SEMANTIC_REVALIDATION | CONTRACT_ADJUDICATION
```

## 3. Reverse-graph propagation

The declared dependency arrow remains `CONSUMER -> PREREQUISITE`. For impact,
derive a reverse graph from that consumer-owned metadata:

```text
declared:  PRJ-C -> PRJ-B -> PRJ-A
derived:   PRJ-A -> PRJ-B -> PRJ-C
```

If `PRJ-A` becomes `STALE`, traverse the derived reverse graph and mark `B`,
then `C`, freshness-uncertain. Do not write the derived graph back as direct
dependency authority and do not redefine the declared arrow direction.

Propagation rules are:

1. A required prerequisite that is `STALE` makes each dependent projection
   `STALE` with `UPSTREAM_PROJECTION_STALE`, unless that dependent is already
   `BLOCKED` for a stronger structural reason.
2. A required prerequisite that is `BLOCKED` makes each downstream consumer
   `BLOCKED` with `UPSTREAM_PROJECTION_BLOCKED`; it cannot be regenerated from
   stale, missing, or conflicting authority. The dependent records the direct
   prerequisite, preserves the blocker’s owning semantic/contract action, and
   routes to that same owning gate. This applies both when the prerequisite is
   observed as blocked during direct evaluation and when `BLOCKED` is reached
   through reverse-graph propagation.
3. Optional or informational dependencies do not structurally block a
   consumer. Their impact remains visible and follows the dependency contract's
   declared impact strength.
4. Traversal is bounded to active projection identities and uses a visited set;
   a dependency cycle is a contract error (`PROJECTION_DEPENDENCY_CYCLE`), not
   permission to recurse indefinitely.

Propagation never creates a new downstream projection revision. Each consumer
   must later be regenerated and verified against its own dependency snapshot.

## 4. Freshness reconciliation and `NO_CHANGE`

An upstream verified regeneration with byte-identical canonical output returns
`NO_CHANGE`, keeps the upstream `PRJ-*@revN`, and does not invalidate
downstream revisions. If downstream was marked uncertain while the upstream
was `STALE`, the impact pass may reconcile it to `CURRENT` only after checking
that all required semantic revisions, selector membership/revisions, contract
revision, upstream revision, and local fingerprint still match. Otherwise its
existing stale reason remains.

`NO_CHANGE` is an observed verified result, not proof that every downstream
projection is current. A verified upstream revision change always propagates
`UPSTREAM_PROJECTION_REVISION_CHANGED` until each consumer is separately
reconciled or regenerated.

## 5. `PROJECTION_IMPACT_ACCOUNTED`

The coordinator may persist:

```text
PROJECTION_IMPACT_ACCOUNTED
```

only when the accepted stabilized semantic delta has been evaluated against
all in-scope projection dependencies, selector contracts/resolution snapshots,
projection contracts, upstream freshness, and drift/missing-file checks, and
the resulting direct/propagated freshness records have been persisted.

This means **impact is known and recorded**. It does not mean all projections
are `CURRENT`, that regeneration happened, or that a projection-sensitive
closeout gate is open. `STALE`, `BLOCKED`, and unresolved technical failures
remain visible and must be honored by the applicable gate or explicit
regeneration process.

## 6. Technical failure semantics

Impact accounting is a technical persistence/analysis step after semantic
authority is accepted. If it fails because the dependency graph cannot be
loaded, a selector cannot be resolved, a required record cannot be persisted,
or the analysis result cannot be durably reconciled:

```text
PROJECTION_IMPACT_ACCOUNTING_FAILED
PROJECTION_IMPACT_ACCOUNTED: false
```

Do not roll back or demote accepted semantic authority. Do not claim impact
accounting, `CURRENT`, or projection-sensitive closeout. Mark the affected
projection scope `BLOCKED`/unknown as appropriate, retain the technical error
and inputs for retry, and require a successful rerun before any projection-
sensitive gate proceeds. A partially persisted result may be retried only
through the idempotent rules below; it is not silently treated as complete.

## 7. Idempotency and reason retention

Impact records are keyed by `(projection_id, analyzed_input_revision,
reason_code, affected_dependency_or_selector)`. Repeating a pass upserts that
record rather than appending a duplicate. Reason details may be refreshed with
the same canonical evidence, but an unresolved prior cause is not erased by a
later pass that cannot disprove it.

When a cause is resolved, record its resolution/reconciliation event and remove
it from the active reason set only after the corresponding dependency,
selector, contract, upstream revision, and fingerprint checks pass. A new
reason is added without replacing unrelated active causes. Status is derived
from the complete active reason set, with `BLOCKED` taking precedence over
`STALE`, and no reason is cleared merely because an attempted regeneration
failed.
