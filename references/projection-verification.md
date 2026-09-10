# Projection verification and revision publication

This reference owns the acceptance gate between generated projection candidates
and verified projection revisions. It consumes the projection lifecycle,
dependency snapshot, and frozen regeneration inputs. It does not generate
content, alter regeneration scope, or adjudicate semantic authority.

## 1. Candidate boundary

Generation produces a candidate with its exact input snapshot and canonical
content fingerprint. A candidate is neither an accepted `PRJ-*@revN` nor a
freshness result:

```text
candidate != verified projection revision
REGENERATED != CURRENT
candidate output != dependency input
```

Until revision publication succeeds, the candidate MUST NOT replace the last
accepted projection content, satisfy an upstream dependency, appear in a
consumer's dependency snapshot, or create downstream impact. A failed,
abandoned, or superseded candidate is retained only as regeneration evidence;
it never becomes semantic authority.

## 2. Required verification dimensions

Every candidate must pass all applicable dimensions in this order before it
can affect persistent projection lifecycle state:

| Gate | Name | Required check |
|---|---|---|
| `V1` | `STRUCTURAL` | The candidate can be parsed/rendered as required, is well-formed for its artifact kind, and has no required generated section or artifact-structure failure. |
| `V2` | `DEPENDENCY / PROVENANCE` | The recorded exact semantic revisions, selector contract and resolution, projection contract revision, and upstream projection revisions equal the frozen inputs consumed to generate the candidate. |
| `V3` | `CONTRACT COMPLETENESS` | The candidate satisfies every required projection-contract field, section, coverage/format obligation, and declared fully-generated-content rule. |
| `V4` | `AUTHORITY CONSISTENCY` | The candidate faithfully represents the accepted semantic authorities and permitted upstream projections named by its verified input snapshot, without adding, changing, or omitting required accepted meaning. |

`V1` success alone is never acceptance. A verifier records gate evidence and
the first failing condition (and may record all independent failures) against
the candidate and its frozen input snapshot.

## 2.1 Detailed operation and API claim verification

For a selected detailed Provided or Consumed projection, `V3 CONTRACT
COMPLETENESS` additionally checks that the candidate declares the exact
selected scope and represents the matching operation-inventory dependency
state. A limited or blocked inventory state remains limited or blocked under
the existing lifecycle; it cannot be presented as a complete claim. The
check includes:

```text
operation_inventory_status:
  accepted matching OPERATION_INVENTORY_COMPLETE for an unqualified
  complete-operation claim; otherwise an explicit PARTIAL, UNKNOWN, or
  UNRESOLVED limitation
operation_inventory_snapshot:
  exact parent IF revisions, coverage ID/revision, definition revision,
  and stable parent-qualified operation child IDs/revisions, precision,
  and limitation state
required_operation_fields:
  parent IF, operation_ref child reference/revision, direction/role, protocol
  kind, exact method/effective path when established, precision, observed
  views, evidence/provenance, and applicable limitation
declared_claim_rule:
  complete API/all endpoints/full endpoint list wording is permitted only
  for the exact selected scope with the accepted complete inventory and
  valid dependency snapshot; CURRENT alone never satisfies the rule
```

An operation inventory may be complete while individual operations remain
`RESOURCE_BOUNDED` or `UNRESOLVED`; V3 checks that those limitations are
declared and does not turn inventory completeness into a requirement that all
detail fields be known. `WHEN_APPLICABLE_REQUIRED` fields are required when
material and evidenced, and additional fields are `WHEN_EVIDENCED`; absent
detail is not silently rendered as an exact value. For API Report, these
operation checks apply only to selected detailed sections 02 and 03. The
umbrella has no identity of its own, and sections 04, 07, and 09 do not gain
operation-depth obligations without an existing direct requirement.

`V4 AUTHORITY CONSISTENCY` compares the candidate with the accepted snapshot
and verifies one faithful rendered row for every accepted accounted operation,
including every bounded/unresolved operation and its limitation. It checks
that no accepted operation is omitted, duplicated, or replaced by a guessed
identity, and that no unaccepted operation was introduced by rendering. V4
does not adjudicate route conflicts, provider matching, coverage status, or
semantic authority; it reports the mismatch to the owning gate. The verifier
does not scan private source, regenerate a projection automatically, change
selection, or modify STM/Coverage/operation authority to make the candidate
pass.

## 2.2 Legacy registration gate

For a pre-Stage-B artifact without accepted `PRJ-*` lifecycle metadata, the
existing content is only a registration candidate. The verifier must receive
the capability owner, stable projection identity, complete projection contract,
resolved exact dependencies/selectors, and accepted authority references before
it can evaluate the candidate. The legacy path is:

```text
legacy artifact
-> identify capability owner
-> assign PRJ identity
-> define contract
-> resolve dependencies
-> verify against accepted authority
-> establish fingerprint/revision
-> CURRENT
```

The initial canonical fingerprint and accepted projection revision are persisted
only after `V1 STRUCTURAL`, `V2 DEPENDENCY / PROVENANCE`, `V3 CONTRACT
COMPLETENESS`, and `V4 AUTHORITY CONSISTENCY` pass. A readable or parseable
Markdown file, its path or age, a Git commit, or historical human acceptance is
not verification evidence and cannot establish `CURRENT`.

If the artifact contains persistent meaning that is not mapped to an accepted
owning authority, registration fails with
`PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY` where applicable. Historical
manual prose remains candidate/context material; it cannot be promoted into
semantic authority or used to resolve a V4 mismatch. Missing, stale, or
conflicting required authority leaves the legacy projection `BLOCKED` with
`SEMANTIC_REVALIDATION` routed to the owning semantic gate. An insufficient or
disputed contract/classification uses `CONTRACT_ADJUDICATION`. Both outcomes
publish no accepted revision and cannot be relabeled as `CURRENT`.

## 3. Bound on V4 and authority blocking

`V4` is a comparison, not semantic adjudication. The verifier may compare
candidate content with accepted authority and report a mismatch, but it MUST
NOT decide which conflicting semantic value is correct, repair the authority,
promote projection prose to authority, or rewrite a semantic ledger to make a
candidate pass.

If a required semantic authority is missing, stale, conflicting, or otherwise
not accepted, verification is blocked:

```text
verification blocked
-> no accepted projection revision
-> projection freshness: BLOCKED
-> required-action: SEMANTIC_REVALIDATION
-> owning semantic gate / revalidation workflow
```

If the projection contract/classification is insufficient to determine V3 or
V4, use `CONTRACT_ADJUDICATION` and route to its owning contract gate. The
Projection Layer cannot turn either unresolved condition into `CURRENT`.

## 4. Revision publication

Only after `V1` through `V4` pass against the exact required inputs may the
verifier compare the candidate's canonical fingerprint with the last verified
fingerprint and persist an accepted lifecycle result:

```text
generate candidate
-> V1 -> V2 -> V3 -> V4
-> any failure: no accepted revision; remain STALE or become BLOCKED
-> all pass + same fingerprint: NO_CHANGE; keep PRJ-*@revN; CURRENT
-> all pass + changed fingerprint: publish PRJ-*@rev(N+1); CURRENT
                                -> downstream impact accounting
```

Publication atomically binds the accepted canonical content fingerprint,
`PRJ-*@revN`, verification evidence, and the verified dependency/provenance
snapshot. It must not publish a new revision before the full gate completes.
If persistence fails, treat verification/publication as failed: publish no
revision and leave the projection `STALE` (or `BLOCKED` when the unresolved
condition is a structural or authority blocker).

`NO_CHANGE` is a verified reconciliation result, not a revision publication:
the existing `PRJ-*@revN` and fingerprint remain authoritative, the projection
may become `CURRENT`, and no downstream revision invalidation occurs.

## 5. Downstream impact and reconciliation

Only a successfully published, fingerprint-changed projection revision may
trigger reverse dependency impact. The impact record is:

```text
UPSTREAM_PROJECTION_REVISION_CHANGED
-> dependent projection STALE
-> dependent must reconcile or regenerate against its own snapshot
```

A downstream projection made uncertain solely by an upstream `STALE` state may
be reconciled to `CURRENT` without content regeneration after that prerequisite
returns `NO_CHANGE`, but only when its own canonical fingerprint and every
required semantic revision, selector membership/revision, contract revision,
and consumed upstream revision still exactly match. `NO_CHANGE` does not clear
an independent stale or blocked reason.

Neither a generated candidate nor a candidate that fails V1--V4 may create
`UPSTREAM_PROJECTION_REVISION_CHANGED`, clear downstream uncertainty, or be
consumed by a downstream projection.
