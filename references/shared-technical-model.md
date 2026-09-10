# Shared Technical Model

The Shared Technical Model (STM) is the persistent semantic authority for
accepted shared technical facts. It consumes bounded, baseline-bound
observations from the [Shared Evidence Model](shared-evidence-model.md) and is
separate from capability interpretations and human-readable projections.

This contract owns STM families, relations, lifecycle, fact authority, and
persistence. Direct dependency metadata, generated dependency indexes, and
impact traversal belong to [Technical Model dependencies and impact](technical-model-dependencies.md).
Session routing and compact workflow state belong to
[Session Orchestration](session-orchestration.md) and
[Review Modes and Orchestration](review-modes-and-orchestration.md). Freshness
decisions remain subject to
[Revalidation and compact-state freshness](revalidation-and-freshness.md).

## 1. Scope and materiality

An STM fact records what the evidence-bounded system materially is or does. It
is not a finding, risk, recommendation, test gap, or product-behavior
authority. Those conclusions remain owned by the capability that makes them.

The initial schema is deliberately materiality-based. Do not create a component
for every class, function, or trivial helper; do not promote a new object family
until repeated cross-capability use requires stable identity and revisioning.

## 2. First-class facts and relations

Initial fact families are:

```text
COMP-*    Component / Runtime Unit
IF-*      Interface
INT-*     Interaction
DS-*      Data Store
EVENT-*   Event / Message
FLOW-*    Material Flow
AUTH-*    Auth / Trust Boundary
CFG-*     Configuration Fact
ERR-*     Error / Failure Contract
```

Relations are semantically meaningful links even when persisted as object
metadata rather than standalone artifacts. The initial controlled vocabulary is:

```text
PROVIDES
CONSUMES
CALLS
PUBLISHES
SUBSCRIBES
READS_FROM
WRITES_TO
OWNS_STATE
MIGRATION_AUTHORITY
PROTECTED_BY
CONFIGURED_BY
EMITS_ERROR
PARTICIPATES_IN
DEPLOYS_AS
DEPENDS_ON
```

Do not use arbitrary free-form relation names as a substitute for this
vocabulary.

The following concerns are intentionally embedded as properties or relations
on accepted first-class facts, not separate families initially:

```text
ENTRYPOINT
STATE
LIFECYCLE
CONCURRENCY
DEPLOYMENT
OBSERVABILITY
```

## 3. Identity, provenance, and state

Each STM artifact has stable semantic identity, a revision, baseline binding,
and references to its supporting `WS-*` / `EV-*` observations. A minimum
semantic record includes its family ID, revision, status, freshness, applicable
authority state, relevant relations, and direct outbound dependency metadata.
The evidence contract owns the observation record itself; the STM records only
its provenance reference. Dependency/index authority and impact semantics are
defined in `technical-model-dependencies.md`.

Lifecycle, freshness, and authority are independent axes:

```text
status:
  CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED

freshness:
  VALID | REVALIDATION_REQUIRED | UNKNOWN

authority where applicable:
  RESOLVED | UNRESOLVED
```

Preserve identity when the same object is revised, for example `IF-021@rev3`.
When the semantic identity changes, preserve history with an explicit
`supersedes` / `superseded_by` link; do not rewrite a prior accepted revision to
look current.

## 4. Observed views and interpretation boundary

An STM fact may preserve multiple observed representations:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

These are observations, not an implicit source-precedence rule. The STM does
not decide whether declaration, implementation, consumers, or tests govern a
contract. A required authority decision is adjudicated outside the projection,
by the appropriate specialist gate (for example, Test Engineering Contract
Verification).

## 5. Technical Model Gate

The Technical Model Gate is the sole writer of accepted shared fact semantics:
only it may accept, revise, reject, or supersede an STM fact. Other capabilities
may emit exactly these requests:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

They must not directly rewrite accepted STM artifacts. A capability may continue
within an unaffected bounded scope while a conflict is reconciled, but it must
not consume a disputed required fact or dependency as accepted downstream truth.
This gate governs STM facts only; capability-owned interpretations retain their
own semantic authority.

## 6. Persistent package shape

The recommended package layout is:

```text
working/
  evidence/
    INDEX.md
    WS-*.md
  technical-model/
    INDEX.md
    coverage.md
    components/COMP-*.md
    interfaces/IF-*.md
    interactions/INT-*.md
    data-stores/DS-*.md
    events/EVENT-*.md
    flows/FLOW-*.md
    auth/AUTH-*.md
    errors/ERR-*.md
    configuration/CFG-*.md
  indexes/
    ... generated projections ...
```

Paths are a recommended convention, not the authority rule. Semantic ownership,
stable identity, revision binding, and provenance are the invariant. `INDEX.md`
and generated indexes route readers to owning artifacts; they do not contain a
second technical model or become semantic authority.

## 7. Bootstrap and reuse

Every `NEW` creates the persistent STM baseline before capability execution.
Creation records the selected baseline and model manifest even when the selected
downstream work requires only a partial factual slice:

```text
always create model != always build complete model
```

The selected downstream requirement determines later population, coverage, and
depth. Existing accepted facts are reusable only when their required revision,
authority, and freshness bindings remain suitable for the requested decision.

Legacy Architecture Review As-Built authority and its migration to an STM
projection are governed by the dedicated migration work; this foundation does
not silently relabel existing As-Built material as accepted STM fact.

## 8. Architecture Review and As-Built projection

Architecture Review consumes accepted/fresh required STM facts and the accepted
Technical Model Coverage decision before full thematic discovery. It is a
consumer of factual components, topology, ownership, interfaces/boundaries,
flows, lifecycle, concurrency, failure, trust, configuration, persistence,
observability and platform behavior; it does not maintain an equivalent factual
system model.

The existing substantial As-Built material remains required, but changes role:

```text
accepted/fresh STM + required factual coverage
→ human-readable As-Built projection with architecture-oriented synthesis
```

The projection preserves material factual parity: purpose/key scenarios,
runtime/deployment topology, state ownership, API/IPC/process/persistence/trust
boundaries, command/read/async/external flows, state/lifecycle transitions,
startup/readiness/shutdown/retry/recovery, concurrency/shared-state/
serialization/idempotency, failure/partial-failure, auth/authz/trust,
configuration/secrets, persistence/migration/consistency, observability and
platform-specific behavior. It exposes `PARTIAL`, `UNKNOWN`, stale and
unresolved limitations rather than turning them into certainty.

As-Built is useful human documentation, not factual authority. Architecture
properties/invariants, adverse-scenario and race interpretation, `SER-*`,
findings, root-boundary adjudication, severity and remediation implications
remain Architecture Review authority. A capability that sees a factual gap or
contradiction emits `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT` or
`TECH_FACT_REVALIDATION_REQUEST`; only the Technical Model Gate changes accepted
facts. Projection repair may fix presentation from unchanged accepted authority,
but semantic drift follows technical revalidation and never promotes a
projection into STM authority.

## 9. Product-scoped factual relations

Product mode reuses the existing STM fact families and Technical Model Gate.
Project-local facts remain Project-local. A cross-project factual relation is
accepted only when it references qualified accepted STM records, the accepted
Product revision, the immutable Product baseline, and the supporting
Product-scoped `WS-*`/`EV-*` evidence. It is not a second generic Product fact
model and does not make Product an owner of the referenced technical facts.

Use semantic qualification rather than a new local-ID namespace: a reference
contains stable Project identity, STM family, local artifact identity, and the
relevant revision/baseline binding. Thus `IF-001` in Project A and `IF-001` in
Project B cannot collide in one Product relation. Shared resources such as a
broker, database, SDK, or auth service retain their technical owner or explicit
external status; Product context records the relationship without becoming the
technical writer.

The Technical Model Gate remains the sole writer of accepted cross-project STM
relations. A relation records a factual association such as provider/consumer,
publisher/subscriber, or shared-state participation. It is not automatically a
semantic dependency. Direct dependency metadata remains owned and typed by the
dependent artifact under `technical-model-dependencies.md`; reverse indexes
remain derived navigation. A disputed or insufficiently evidenced relation
stays unresolved/limited and cannot be consumed as accepted downstream truth.

## 10. Stage F interface and interaction extensions

Stage F extends the existing STM families. It does not create a parallel
technical model or a new factual identity family. The Technical Model Gate
remains the sole writer of accepted facts; evidence and projections remain
separate authorities.

### 10.1 IF-* interface and contract shape

`IF-*` remains the identity of one material interaction surface or contract. It
is not a call edge, data-access edge, event identity, dependency, or
compatibility result. A Stage F interface record may carry this common shape
when the corresponding property is applicable and evidence-supported:

```text
IF-*:
  semantic_id
  revision
  status
  freshness
  authority
  direction: PROVIDED | CONSUMED
  interface_kind: HTTP_REST | GRPC_RPC | GRAPHQL | WEBSOCKET |
                   WEBHOOK | CLI | LIBRARY | FILE_PROTOCOL | IPC | OTHER
  contract_role: PROVIDER_DECLARATION |
                 PROVIDER_IMPLEMENTATION |
                 CONSUMER_EXPECTATION |
                 CONSUMER_OBSERVED_USE
  operation_identity: optional structured protocol operation
  address: optional safe protocol/resource address
  contract_version: optional evidenced external/API version
  contract_ref: optional bounded source/schema/artifact reference
  contract_fingerprint: optional stable source-derived fingerprint
  provider_ref: optional qualified COMP-* or external provider
  auth_refs: optional AUTH-* references
  error_refs: optional ERR-* references
  protocol_properties: optional controlled kind-specific properties
  precision: EXACT | RESOURCE_BOUNDED | UNRESOLVED
  observed_view: DECLARED | IMPLEMENTED | CONSUMED | TESTED
  operation_children:
    - operation_id: OP-<zero-padded-decimal-3-or-more-digits>
      parent_if: IF-*<parent-revision>
      revision: <integer revision>
      interface_kind: <existing closed interface kind>
      direction: PROVIDED | CONSUMED
      contract_role: <existing role vocabulary>
      operation_identity: <protocol-specific normalized identity>
      precision: EXACT | RESOURCE_BOUNDED | UNRESOLVED
      status: CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED
      freshness: VALID | REVALIDATION_REQUIRED | UNKNOWN
      authority: RESOLVED | UNRESOLVED
      observed_views: [DECLARED | IMPLEMENTED | CONSUMED | TESTED ...]
      protocol_properties: <existing controlled properties>
      evidence_refs: WS-* / EV-*
      supersedes: optional parent-qualified operation reference
  boundary_evidence: optional qualified transport/schema boundary observations
                     and enforcement-stage references
  project_binding: optional Project/repository/revision qualification
  evidence_refs: WS-* / EV-* references
```

The shape does not require nullable properties to be fabricated. Direction,
interface kind, identity/revision, evidence, and an applicable precision are
the core fields; operation, address, version, contract, provider, auth, error,
and protocol properties are required only when applicable or evidenced.

`operation_children` is an IF-owned collection of subordinate operation
contracts. `operation_id` is unique only within the parent-qualified IF
identity, and `IF-*/OP-*` is a reference path, not a new global STM family.
There is no top-level `OP-*` family. An operation cannot exist without an IF.
The Technical Model Gate accepts, revises, and supersedes operation children;
no downstream capability creates an operation. It allocates each
`operation_id` monotonically within its parent and never reuses it. A semantic
parent move creates a new parent-qualified child with `supersedes`, rather than
moving the existing child. Historical surface-only IFs remain valid with no
inferred children.

Operation `status`, `freshness`, and `authority` do not imply any observed
view. Persist `observed_views` as an explicit list so multiple independent
existing views can coexist without changing their semantics. The child list
does not alter the existing IF-level `observed_view`, lifecycle/status
vocabulary, or the semantics of any existing IF view.

When API input boundary observations are applicable, `boundary_evidence` is an
optional qualified attribute on the existing `IF-*` record. It may reference
transport/container and schema/field limits, evidence state, and the expected
enforcement stage. It does not create a boundary fact family, alter interface
identity, or make Code Quality or Test Engineering authority factual. A
`TESTED` observed view still requires accepted execution evidence under the
existing Test Engineering semantics; a generated or accepted case and its
expected result cannot populate it. Missing boundary metadata remains absent
or unknown and does not invalidate a historical IF record.

`contract_role` is a perspective qualifier, not a lifecycle. `observed_view`
remains the existing observation vocabulary. The Technical Model Gate applies
this closed role/view matrix:

| `contract_role` | Valid primary views | Meaning of `TESTED` |
|---|---|---|
| `PROVIDER_DECLARATION` | `DECLARED`, `TESTED` | A test exercises the declared provider contract; it does not prove implementation equivalence. |
| `PROVIDER_IMPLEMENTATION` | `IMPLEMENTED`, `TESTED` | A test exercises implemented provider behavior; it does not turn implementation into a declaration. |
| `CONSUMER_EXPECTATION` | `DECLARED`, `TESTED` | A test asserts the consumer expectation; it does not prove a provider satisfies it. |
| `CONSUMER_OBSERVED_USE` | `CONSUMED`, `TESTED` | A test exercises consumer use; it does not make the consumer a provider. |

`DECLARED`, `IMPLEMENTED`, and `CONSUMED` are invalid as primary views for
roles without that perspective. For example, `CONSUMER_EXPECTATION` with
`IMPLEMENTED` and `PROVIDER_IMPLEMENTATION` with `CONSUMED` are rejected by the
Technical Model Gate or retained only as unresolved evidence; they are never
accepted silently. `TESTED` is orthogonal evidence and does not replace the
role's primary view. Historical IF records without `contract_role` remain
valid with their existing observed view; the matrix never infers a role or
default precision for them.

Protocol-specific properties remain under one controlled object selected by
`interface_kind`:

| Kind | Properties when evidenced |
|---|---|
| `HTTP_REST` | method, path/template, safe host/provider reference, media/content contract reference |
| `GRPC_RPC` | package/service, method, protobuf contract reference/fingerprint |
| `GRAPHQL` | operation type/name, field or schema address, schema reference/fingerprint |
| `WEBSOCKET` | endpoint/channel, message direction, material message/topic identity |
| `WEBHOOK` | callback address, callback event/type, sender/receiver direction |
| `CLI` | command/subcommand, option contract reference, exit/error contract reference |
| `LIBRARY` | public symbol/module/package and call contract reference |
| `FILE_PROTOCOL` | path/pattern, format/schema reference, transfer direction |
| `IPC` | mechanism, endpoint/channel, message or call contract reference |
| `OTHER` | bounded documented properties only when material and evidenced |

Unsupported or unobserved properties are absent rather than null claims.

#### 10.1.1 Protocol operation identity

An operation child's full semantic identity is parent-qualified: its `parent_if`
revision, `interface_kind`, `direction`, `contract_role`, and normalized
`operation_identity` qualify one another. A source location, handler symbol,
or generated-client location is evidence provenance, never operation identity.
The Technical Model Gate applies the following protocol-specific construction
when an addressable operation surface is evidenced:

| `interface_kind` | Normalized `operation_identity` |
|---|---|
| `HTTP_REST` | Uppercase normalized method plus normalized effective route/template. |
| `GRAPHQL` | Operation type/name when present, or an addressable field/schema surface when no named operation is available. |
| `GRPC_RPC` | Package, service, and method. |
| `WEBSOCKET` | An addressable command or message only when its contract identity is evidenced; an endpoint alone does not invent an operation child. |
| `CLI` | Command and subcommand surface. |
| Other kinds | A bounded, documented protocol-specific identity only when the operation surface is addressable and evidenced. |

`EVENT-*` remains the identity of a semantic event or message. An event is not
recast as an IF operation merely because it has a transport endpoint. An
operation child may represent only an independently addressable command surface
that the event contract exposes; that child does not replace or alias the
`EVENT-*` identity.

#### 10.1.2 HTTP effective-route composition and precision

For `HTTP_REST`, normalize the method to uppercase. Compose the effective path
from separately evidenced mount, controller, and router prefixes plus the local
route declaration, in their declaration order. Normalize that composed path to
one leading slash and remove redundant separators. Preserve contract-visible
template parameter names and version segments: `/v1/orders/{orderId}` and
`/v1/orders/{id}` are distinct identities unless the protocol contract
explicitly evidences them as equivalent. Do not infer equivalence from matching
handler code, parameter position, or framework convention.

Trailing-slash normalization is allowed only when the framework's evidenced
route semantics establish the canonical result. Otherwise retain the declared
slash spelling as provenance, do not collapse slash variants, and record their
equivalence distinction as unresolved. No identity may be fabricated by
silently removing or adding a trailing slash.

Each prefix or mount, local route declaration, and method is a distinct
composition input with its own evidence reference. The operation child records
the normalized result, not an invented replacement for a missing input. Nested
prefixes compose only in declaration order. `EXACT` is valid only when the
method and effective path/template are evidenced; unavailable parameter or
request/response schema evidence remains a separate explicit limitation and
does not lower an otherwise exact method/path identity. When a bounded route
surface is known but a computed, plugin-provided, feature-flagged, reflected,
or runtime-only input prevents an exact result, use `RESOURCE_BOUNDED`; use
`UNRESOLVED` when the effective route or method cannot be determined or the
relevant declarations conflict. Never fabricate a path to upgrade precision.

The same effective path with different methods is distinct. The same handler
under distinct routes is also distinct unless an accepted alias relation,
supported by evidence, proves intentional equivalence. Apparent duplicate
declarations remain separately accounted candidates until the Technical Model
Gate classifies them as a duplicate declaration or separate operations. A route
exposed through two mounts has two parent-qualified operation identities, even
when the local declaration or handler is shared.

### 10.2 INT-* concrete interaction and access shape

`INT-*` is the primary accepted fact for one concrete source-to-target
interaction edge. It is not direct dependency metadata and does not own the
identity of an interface, event, or data resource:

```text
INT-*:
  semantic_id
  revision
  status
  freshness
  authority
  source_ref: COMP-* or qualified source
  target_ref: COMP-* | DS-* | qualified external identity | unresolved
  consumed_interface_ref: optional IF-*@revision
  provided_interface_ref: optional IF-*@revision
  event_ref: optional EVENT-*
  protocol_or_transport: optional evidenced property
  interaction_kind: CALL | EVENT_PUBLISH | EVENT_SUBSCRIBE |
                     DATA_ACCESS | FILE_ACCESS | OTHER
  access_mode: required for DATA_ACCESS
  sync_or_async: optional existing property
  timeout: optional existing property
  retry: optional existing property
  correlation: optional existing property
  precision: required
  project_binding: required Project/revision/baseline qualification
  evidence_refs: required WS-* / EV-* references
```

For a data-access interaction, `target_ref` is a `DS-*` resource and
`access_mode` is one of the controlled values in section 10.4. An external API
uses a qualified external identity or safe source binding, never a
secret-bearing URL. An event interaction may reference both its semantic
`EVENT-*` and its transport target. `CALL`, `DATA_ACCESS`, and event
interactions do not automatically create `DEPENDS_ON`; dependency metadata
remains separately typed and authoritative under
`technical-model-dependencies.md`.

`EVENT-*` remains the identity of a semantic event or message, while
`EVENT_PUBLISH` and `EVENT_SUBSCRIBE` on `INT-*` record concrete interaction
edges. `FLOW-*` remains the identity of a material end-to-end, system,
business, or control flow. Neither event nor flow identity is replaced by an
interface or interaction record.

### 10.3 DS-* store and addressable-resource shape

One `DS-*` identity family represents both a store-level resource and an
addressable resource inside that store. Child resources share the STM identity
and lifecycle model; they do not create `TABLE-*`, `BUCKET-*`, `COLLECTION-*`,
`SQL-*`, or other new identity families:

```text
DS-*:
  semantic_id
  revision
  status
  freshness
  authority
  resource_kind
  parent_resource_ref: optional DS-*
  technology: optional store technology
  safe_address: optional evidence-backed logical address
  precision: EXACT | RESOURCE_BOUNDED | STORE_ONLY | UNRESOLVED
  project_binding: Project/repository/revision qualification
  evidence_refs: WS-* / EV-* references
```

The controlled resource kinds include:

```text
STORE | DATABASE | SCHEMA | TABLE | VIEW | MATERIALIZED_VIEW |
PROCEDURE | FUNCTION | NAMESPACE | KEY_PATTERN | COLLECTION |
SEARCH_INDEX | BUCKET | PREFIX | VECTOR_COLLECTION | VECTOR_INDEX |
FILE | PATH_PATTERN
```

`TRIGGER`, `INDEX`, and `SEQUENCE` may be used as additional bounded resource
kinds when their identity is material to an accepted interaction; they do not
become new families. `parent_resource_ref` records containment or address
context only. It does not imply ownership, access, migration authority, or
dependency. A database connection does not imply access to every table, and a
store owner does not automatically own every descendant. Any inherited
ownership must be separately evidenced with its scope and override rule.

### 10.4 Data-access authority and derived relations

Concrete new precise data access is authored in `INT-*`:

```text
READ
WRITE
READ_WRITE
EXECUTE
DDL
MIGRATION
```

`access_mode` is an interaction property, not a resource identity or a
dependency. The derivation rule is:

```text
INT DATA_ACCESS + READ       -> derived READS_FROM
INT DATA_ACCESS + WRITE      -> derived WRITES_TO
INT DATA_ACCESS + READ_WRITE -> derived READS_FROM and WRITES_TO
INT + EXECUTE / DDL / MIGRATION -> no read/write derivation without separate evidence
```

A materialized `READS_FROM` or `WRITES_TO` relation for the same qualified
source, target, Project/revision, and baseline is derived/navigation state with
an explicit link to the authoritative `INT-*` fact. A projection may compute
the relation without materializing it, but uses the same rule. Direct
dependency metadata never owns access mode.

Relation-only `READS_FROM` and `WRITES_TO` records without `INT-*` remain valid
accepted broad historical facts. They carry no inferred `access_mode`, are not
silently rewritten into INT, and do not receive fabricated precision. If a
new precise INT contradicts a legacy relation, the INT is authoritative for the
precise current edge; the historical relation is preserved with a stale or
`REVALIDATION_REQUIRED` limitation as applicable, and the conflict routes to
bounded revalidation rather than an overwrite.

### 10.5 Database callable boundary

`PROCEDURE` and `FUNCTION` are DS identities because they are database-owned
schema objects. They are not callable-interface identities by themselves. An
independently evidenced callable contract may additionally be represented by
an `IF-*` with its own stable identity and revision when operation,
request/response, auth, error, or compatibility semantics are material.

An invocation is an `INT-*` with `interaction_kind=DATA_ACCESS` and
`access_mode=EXECUTE`, targeting the DS procedure/function and optionally
referencing the callable IF. DS and IF never alias or replace each other.
DS-only is valid when execution is evidenced without an independent callable
contract. An external or abstract callable IF may exist without a known DS.

### 10.6 Precision and family applicability

Precision is independent of evidence strength/confidence, coverage, freshness,
authority, observed view, and lifecycle:

```text
EXACT
RESOURCE_BOUNDED
STORE_ONLY
UNRESOLVED
```

`EXACT`, `RESOURCE_BOUNDED`, and `UNRESOLVED` are applicable to IF, EVENT,
FLOW, and applicable INT facts. `STORE_ONLY` is valid only for a DS store-level
fact or a DATA_ACCESS INT whose parent store is known but entity-level target
is not. It is invalid for IF, EVENT, FLOW, and non-data INT facts. An interface
with an unresolved operation uses `UNRESOLVED` or `RESOURCE_BOUNDED`, never
`STORE_ONLY`. Precision never silently upgrades; a stronger observation creates
a new revision or enrichment while preserving the prior limitation.

### 10.7 Migration authority

`MIGRATION_AUTHORITY` is a controlled STM factual relation meaning
responsibility for schema/data-resource evolution. It is not runtime migration
execution, DDL execution, state ownership, or a dependency edge:

```text
MIGRATION_AUTHORITY:
  owner_ref: COMP-* or qualified Project owner
  resource_ref: DS-*
  source_refs: WS-* / EV-* and migration source locator
  project_binding: Project/revision/baseline qualification
  scope: exact resource or bounded resource set
  status: accepted or unresolved under STM lifecycle
```

`INT access_mode=MIGRATION` records execution of a migration operation.
`MIGRATION_AUTHORITY` records responsibility for evolution. Neither implies
the other, and `MIGRATION_AUTHORITY` never implies `OWNS_STATE`. Multiple or
conflicting authorities remain independently qualified facts or unresolved
conflict; the STM does not automatically create an Architecture finding.

### 10.8 External identity qualification and history

No external-service identity family is introduced. Existing `COMP-*`, `IF-*`,
`INT-*`, and `DS-*` records may carry an external qualification:

```text
external_identity:
  logical_name
  kind: THIRD_PARTY_SAAS | IDENTITY_PROVIDER | PAYMENT_PROVIDER |
        CLOUD_API | EXTERNAL_DATABASE | OBJECT_STORE | OTHER
  source_binding: external locator/revision or explicit limitation
  owner/provider: known logical owner where evidenced
  safe_identifier: safe non-secret technical identity
```

The source binding is exact when the source supports it or explicitly limited
when it does not. A configured URL, SDK, or infrastructure declaration alone is
not an accepted concrete interaction. Credentials, tokens, passwords, private
keys, secret query strings, and complete secret-bearing DSNs are never STM
identifiers or fields. Safe identifier classification and evidence-pointer
handling remain subject to the Shared Evidence contract; this STM contract
accepts only the safe, non-secret representation.

Every new Stage F property remains optional when evidence does not support it.
Existing COMP, IF, INT, DS, EVENT, FLOW, and controlled-relation records retain
their identity, revision, baseline, authority, and prior precision. Historical
absence of `contract_role`, Stage F precision, access mode, child resource, or
external qualification is not interpreted as false, exact, or a fabricated
default. No ID rewrite, bulk enrichment, Product conversion, or destructive
migration is permitted.
