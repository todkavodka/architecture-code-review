# Code Quality lifecycle and assessment contract

This reference defines state and transition semantics for Code Quality
findings, remediation actions, and assessment coverage. It does not implement
coordinator wiring or Stage B projection registration.

## Candidate and finding axes

These are independent axes, not one status enum.

### Candidate state

`CANDIDATE` is transient, pre-authority analysis state. A candidate contains its
observation/evidence and may result in:

```text
ACCEPTED_FINDING
REJECTED_FALSE_POSITIVE
NOT_APPLICABLE
EXCLUDED
```

Only `ACCEPTED_FINDING` creates an `ACTIVE` `CQ-*`. An audit trail may retain a
rejected candidate and its rationale, but it is not semantic CQ authority.

### Finding lifecycle

Persistent accepted findings use the minimal lifecycle:

```text
ACTIVE -> RESOLVED
ACTIVE -> SUPERSEDED
```

Acceptance is an adjudication event that creates `ACTIVE`; `CANDIDATE` and
`ACCEPTED` are not lifecycle states. `RESOLVED` requires evidence-backed
revalidation that the issue no longer exists. `SUPERSEDED` requires a
materially different replacement authority or an equivalent adjudication
record; it does not silently mutate the old identity.

### Applicability

Applicability is one of:

```text
APPLICABLE
NOT_APPLICABLE
EXCLUDED
```

`NOT_APPLICABLE` means the rule/addendum does not apply to the target.
`EXCLUDED` means the target is intentionally outside selected scope or policy.
Neither creates an accepted CQ finding and neither proves absence of quality
risk.

### Disposition

Disposition is separate from lifecycle and applicability:

- `FALSE_POSITIVE` rejects the candidate interpretation; no active CQ authority
  persists from it;
- `ACCEPTED_EXCEPTION` records a real active finding intentionally accepted
  with an explicit rationale and owner/approval provenance;
- `WONT_FIX` records a real active finding whose remediation is declined with
  rationale.

`ACCEPTED_EXCEPTION != RESOLVED` and `WONT_FIX != RESOLVED`. `SUPPRESSED` is not
a hidden fourth meaning: use `EXCLUDED` for scope exclusion or one of the
accepted-finding dispositions for a real issue.

### Freshness

Freshness is independent:

```text
CURRENT
STALE
BLOCKED
```

It describes whether required source/evidence/dependency bindings are valid;
it does not replace lifecycle or disposition.

Legal examples include:

| Combination | Meaning |
|---|---|
| `ACTIVE + CURRENT` | Accepted finding with valid bindings. |
| `ACTIVE + WONT_FIX + CURRENT` | Real current finding with declined remediation. |
| `ACTIVE + ACCEPTED_EXCEPTION + CURRENT` | Real current finding with accepted exception. |
| `ACTIVE + STALE` | Accepted finding requiring bounded revalidation. |
| `RESOLVED + CURRENT` | Current evidence supports resolution. |
| `SUPERSEDED + CURRENT` | Historical finding replaced by a different current authority. |

Invalid combinations include `FALSE_POSITIVE + ACTIVE` persistent authority,
`NOT_APPLICABLE +` accepted finding, and `EXCLUDED +` accepted finding.
`RESOLVED + STALE` is not presented as a valid active semantic state: if the
resolution evidence becomes unverifiable, the record is reopened through
adjudication or retained as historical `SUPERSEDED` rather than silently shown
as resolved.

## CQRA remediation authority

**Decision: `CODE_QUALITY_OWNS_CQRA`.** `TASK-*` is Test Engineering-owned and
does not have compatible Code Quality remediation semantics. Physical storage
patterns may be reused later, but semantic ownership remains Code Quality.

`CQRA-<repository-scoped stable allocation>` is stable, persistent,
monotonically allocated, session-safe, and contains no category or severity.
The authoritative action includes:

- identity and action/title;
- one or more linked `CQ-*` findings;
- scope and responsible owner where applicable;
- rationale and semantic/evidence basis;
- status and transition provenance;
- created/updated provenance;
- relevant CQ/source/freshness dependencies.

The minimal lifecycle is:

```text
PROPOSED -> PLANNED -> COMPLETED
PROPOSED -> CANCELLED
PLANNED -> CANCELLED
PROPOSED|PLANNED -> SUPERSEDED
```

Code Quality writers propose actions. Code Quality adjudicators/owners accept
or plan, cancel, supersede, and record completion. One CQ finding may link to
many actions, and one action may address many findings. `COMPLETED` requires
implementation evidence but never resolves a CQ finding; resolution requires
separate evidence-backed CQ revalidation. If the semantic basis changes, the
action becomes `STALE` or requires re-evaluation. CQRA never creates or mutates
`TASK-*`, `RF-*`, STM, TE authority, or projections.

### Product CQ/CQRA lifecycle binding

Product-scoped existing `CQ-*` and coordinated `CQRA-*` records use the same
candidate, lifecycle, disposition, freshness, and revalidation axes as local
records. Their required scope binding is:

```text
scope_kind: PRODUCT
product_id: PROD-*
product_revision: accepted revision
product_baseline: immutable baseline reference
affected_projects: qualified Project identities
allocation_namespace: PRODUCT:<PROD-*>
```

The Code Quality Review owner allocates and adjudicates these records. A
Product CQ remains `ACTIVE` only with sufficient Product evidence, accepted
relevant STM context, a material cross-project consequence, and valid
provenance. A change to a Product baseline, qualified evidence, STM dependency,
or affected Project binding marks only the dependent Product record or action
`STALE`/`BLOCKED` through the existing impact-driven revalidation rules; it
does not rewrite local CQ/CQRA history or make a stale record current.

Product CQRA completion records implementation evidence for the coordinated
action but never resolves, supersedes, or changes the lifecycle of a linked
CQ. Local CQRA actions remain local unless independently adjudicated as one
Product-spanning action. Product membership and a Product summary cannot write
upstream CQ/CQRA authority.

## Source bindings and freshness triggers

An accepted CQ finding binds to the selected repository or dirty baseline,
file revision, symbol identity/content fingerprint where available, relevant
dependency and framework versions, configuration and addendum revisions,
targeted STM revision, and related RF/TE records when those relations affect
interpretation. Algorithms are implementation decisions.

Impact analysis is required for source/symbol move or deletion, semantic
refactor, dependency or framework upgrade, configuration or addendum change,
generated-code regeneration, STM revision, and related Architecture or TE
authority changes. A rename or equivalent refactor may retain identity only
when semantic bindings remain valid.

`REVALIDATE` marks affected findings/candidates `STALE`, identifies the minimum
impacted CQ slice, and validates only that slice. It is not a full review rerun
and does not regenerate projections. The impact decision is recorded against
the changed binding and affected CQ identities; unrelated findings remain
reusable when their bindings remain valid.

### Operational freshness and revalidation outcomes

For an accepted finding, freshness transitions are driven by its material
dependencies, not by source change alone:

```text
CURRENT
  → STALE       when a material binding changes or its validity is unknown
STALE
  → CURRENT     after sufficient targeted evidence preserves the interpretation
STALE
  → BLOCKED     when required evidence or factual context cannot be obtained
BLOCKED
  → CURRENT     only after the blocking dependency is resolved and rechecked
```

Targeted revalidation adjudicates each affected finding independently:

- if the same mechanism and material consequence remain supported, preserve the
  `CQ-*` identity and set freshness to `CURRENT`;
- if the issue no longer exists, retain its history and transition the finding
  to `RESOLVED` with resolution evidence;
- if the mechanism has materially changed, transition the old finding to
  `SUPERSEDED` only with a replacement authority or explicit adjudication, and
  allocate a new identity for the distinct issue;
- if evidence or required context is insufficient, retain the lifecycle and
  set freshness to `BLOCKED` rather than deleting or resolving the finding.

`STALE` never directly becomes `RESOLVED`. `ACTIVE + STALE` is a valid pending
state, and `RESOLVED + CURRENT` remains the valid state for an evidenced
resolution.

### CQRA completion procedure

When a `CQRA-*` action becomes `COMPLETED`, the coordinator records its
completion evidence and identifies every linked `CQ-*` finding. Each linked
finding is independently placed in the affected revalidation slice. Completion
does not itself change any finding lifecycle or resolve a finding; linked
findings become `STALE` when their post-remediation evidence requires
revalidation:

```text
CQRA COMPLETED
  → identify linked CQ findings
  → mark only dependent findings STALE
  → obtain targeted post-remediation evidence
  → adjudicate each finding independently
  → CURRENT + ACTIVE, CURRENT + RESOLVED, or SUPERSEDED/BLOCKED as supported
```

For one action linked to many findings, one finding may become `RESOLVED` while
another remains `ACTIVE`; the action may remain `COMPLETED`. For many actions
linked to one finding, completing one action does not resolve the finding while
the accepted semantic issue remains. `CQRA COMPLETED != CQ RESOLVED`.

The completion record preserves the action's provenance and freshness. If its
semantic basis or required dependency changes, the action becomes `STALE` or
requires re-evaluation, but this does not rewrite the linked finding history.

## Assessment coverage authority

The Code Quality session/assessment owns one bounded coverage state rather than
a separate factual model. It records:

```text
requested_scope
reviewable_scope
excluded_scope
unavailable_scope
unsupported_scope
dirty_or_noncanonical_scope
coverage_status
limitation_reason
affected_claims_or_outputs
```

`coverage_status` is:

```text
COMPLETE
PARTIAL
BLOCKED
```

`PARTIAL` qualifies aggregate claims about unreviewed scope but does not
invalidate independent accepted findings whose dependencies remain sufficient.
`BLOCKED` prevents only claims requiring unavailable evidence. Reports and
summaries must disclose limitations and cannot imply repository-wide coverage.
Excluded, unavailable, unsupported, or dirty scope is not silently treated as
reviewed canonical scope.

Dirty source may be reviewed only when selected. The assessment records the
committed base, working-tree dirty marker, actual file/content bindings,
untracked-source status, and a non-reproducibility warning. Dirty content is
not the canonical Git baseline.

## Cross-capability relation state

Relations are bounded records attached to owning semantic records. They use
these meanings:

| Relation | Direction/cardinality | State effect |
|---|---|---|
| `DUPLICATE` | Directional during adjudication; many-to-one | One retained authority; duplicate is rejected or superseded. |
| `CORRELATED` | Symmetric; many-to-many | No severity, lifecycle, or freshness coupling. |
| `CAUSAL` | Directional; many-to-many | Rechecked when bindings change; no ownership transfer. |
| `ESCALATED` | Directional to external owner; many-to-many | Requests adjudication; target owner controls its lifecycle/severity. |
| `DERIVED` | Directional; one-to-many | Downstream record cannot override source authority; freshness depends on source. |
| `INDEPENDENT` | Symmetric; many-to-many | Explicitly preserves distinct meanings and no automatic effects. |

The relation itself carries rationale and relevant freshness dependencies. It
does not merge identities, transfer lifecycle, copy severity, or make a
projection authoritative.

## State invariants

- candidate state is transient and never a CQ lifecycle state;
- rejected, not-applicable, and excluded candidates do not create active CQ authority;
- `CQRA COMPLETED != CQ RESOLVED`;
- accepted exceptions and WONT_FIX findings remain real active findings;
- freshness does not substitute for lifecycle or disposition;
- coverage state qualifies claims and package usability, not semantic finding validity;
- `working/INDEX.md` may reference CQ state but is coordinator workflow authority only;
- projections and package manifests are not semantic authority;
- `PROJECTION_REPAIR != semantic remediation`;
- no CQ transition mutates Architecture, TE, STM, or security authority.
