# Stage F — Interface, API & Data Integration Catalog
## Design

### 1. Metadata and baseline

| Field | Value |
|---|---|
| Repository | `/home/tod/skills/architecture-code-review` |
| Branch | `main` |
| Approved Discovery checkpoint | `9d5c09b6e1dc2686d640e66b1760dcd47640ef42` |
| Discovery checkpoint subject | `docs: record approved Stage F discovery` |
| Discovery artifact | `docs/superpowers/specs/2026-09-07-stage-f-interface-api-data-integration-discovery.md` |
| Independent Review | `docs/superpowers/reviews/2026-09-08-stage-f-interface-api-data-integration-discovery-review.md` |
| Design artifact | `docs/superpowers/specs/2026-09-08-stage-f-interface-api-data-integration-design.md` |
| Direction | `OPTION B — Extend existing STM contracts` |
| Migration | `COMPATIBLE_EXTENSION` |
| New identity family | `NO` |

This is a semantic and projection Design. It defines target meaning, ownership,
qualification, compatibility, and document boundaries. It does not edit the
current normative contracts, implement runtime behavior, create tests, or define
an Implementation Plan.

### 2. Problem and design objective

Stage F makes the existing STM useful for complete, evidence-bounded interface
and data integration catalogs while preserving its authority model. The target
must answer, for one service and for an optional Product:

- what interfaces are provided;
- what interface expectations and calls are consumed;
- which internal and external systems are involved;
- which events are produced and consumed;
- which stores and addressable data resources are accessed;
- who owns data state and schema evolution;
- what evidence supports every reported fact;
- how exactness and uncertainty are shown; and
- what provider/consumer compatibility is known, unknown, or incompatible.

The Design deliberately separates four different things:

```text
surface/contract     IF-*
concrete interaction INT-*
data resource       DS-*
derived document    PRJ-*
```

Events and material flows remain their own existing families. No catalog becomes
a source of factual authority.

### 3. Approved Discovery constraints

The approved Discovery and its independent review establish these constraints:

1. The current model is `PARTIAL` for operation/entity-level catalogs.
2. `IF-*` and `DS-*` need compatible semantic extension.
3. `INT-*` and `FLOW-*` remain existing families; exact qualifier placement is
   resolved here without changing their conceptual ownership.
4. No new `API-*`, `SQL-*`, `DB-*`, `DATA-*`, `ProductAPI-*`, or
   `ProductIntegration-*` identity family is required.
5. Product is optional and remains a qualified projection context, not a second
   factual model.
6. Historical broad facts remain valid at their prior precision.
7. Existing projection, dependency, package, and revalidation lifecycles are
   reused.
8. Weak hints cannot create accepted concrete interaction facts.
9. Missing information is represented as limitation or indeterminate precision,
   never as fabricated exactness.

### 4. Authority architecture

The target authority chain is:

```text
WS-* / EV-* evidence
    -> Technical Model Gate
       -> COMP-* / IF-* / INT-* / DS-* / EVENT-* / FLOW-*
          + AUTH-* / CFG-* / ERR-* and controlled relations
       -> Contract Verification automatically when its material-applicability rule is met
       -> PRJ-* Technical Documentation and Product projections
```

Authority ownership remains:

| Concern | Authority |
|---|---|
| Source observations and provenance | `WS-*` / `EV-*` Shared Evidence |
| Accepted technical facts | STM and the Technical Model Gate |
| Components | `COMP-*` |
| Interface surfaces and contracts | `IF-*` |
| Concrete interaction edges | `INT-*` |
| Stores and addressable data resources | `DS-*` |
| Event/message semantics | `EVENT-*` |
| Material flows | `FLOW-*` |
| Auth/trust, configuration, errors | `AUTH-*`, `CFG-*`, `ERR-*` |
| Architecture interpretation/findings | `RF-*` |
| Code Quality | `CQ-*`, `CQRA-*` |
| Test Engineering | `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` |
| User-facing projection identity | `PRJ-*` |
| Projection execution session | `RG-*` |

An Interface/API/Data Catalog is a projection over those authorities. It is not
an `API-*`, `SQL-*`, `DB-*`, or Product factual authority.

### 5. Core semantic model

The families have these non-overlapping responsibilities:

```text
COMP-*   service, process, worker, gateway, repository layer, external system
IF-*     material interaction surface or contract at a boundary
INT-*    concrete source-to-target interaction or access edge
DS-*     store or addressable resource inside a store
EVENT-*  semantic event/message and its publication/subscription meaning
FLOW-*   material end-to-end/system/business/control flow
PRJ-*    derived human-facing documentation
```

The existing relations remain valid:

```text
PROVIDES, CONSUMES, CALLS,
PUBLISHES, SUBSCRIBES,
READS_FROM, WRITES_TO, OWNS_STATE,
PROTECTED_BY, CONFIGURED_BY, EMITS_ERROR,
PARTICIPATES_IN, DEPLOYS_AS, DEPENDS_ON
```

Stage F adds the controlled relation `MIGRATION_AUTHORITY` to the existing STM
relation vocabulary. It means responsibility for schema/data-resource evolution;
it does not mean runtime DDL access, ownership of all descendants, or a
dependency edge. The relation remains STM factual authority and is not a new
identity family.

Every Stage F fact continues to carry the existing STM identity, revision,
status, freshness, baseline, authority state, relevant relations, and
`WS-*`/`EV-*` references. New fields are optional when evidence does not support
them.

### 6. IF-* extension

`IF-*` remains the identity of one material interaction surface or contract. It
does not become a call edge, data access edge, event identity, or compatibility
result.

#### Common IF record

The common semantic shape is:

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
  precision: EXACT | RESOURCE_BOUNDED | STORE_ONLY | UNRESOLVED
  observed_view: DECLARED | IMPLEMENTED | CONSUMED | TESTED
  project_binding: optional Project/repository/revision qualification
  evidence_refs: WS-*/EV-* references
```

This is a semantic shape, not a requirement that every record physically
contain every nullable property. `direction`, `interface_kind`, `precision`,
identity/revision, baseline, and evidence are the core fields. Operation,
address, version, contract, auth, error, and provider fields are required only
when applicable or evidenced.

`contract_role` is a perspective qualifier, not a new lifecycle. The existing
`observed_view` remains the observation vocabulary. The two fields prevent the
consumer expectation from being confused with a provider declaration while
allowing both to use the existing observed-view semantics.

The dimensions are orthogonal but constrained by this closed validation
matrix. `contract_role` identifies whose semantic record this is;
`observed_view` identifies the evidence perspective represented by the record.
`TESTED` is valid for every role when a test directly exercises that role; it
is not a replacement lifecycle and does not make tested behavior the provider
or consumer authority.

| `contract_role` | Valid primary views | Meaning of `TESTED` for the role |
|---|---|---|
| `PROVIDER_DECLARATION` | `DECLARED`, `TESTED` | A test exercises the declared provider contract; it does not prove implementation equivalence by itself. |
| `PROVIDER_IMPLEMENTATION` | `IMPLEMENTED`, `TESTED` | A test exercises implemented provider behavior; it does not turn implementation into a declaration. |
| `CONSUMER_EXPECTATION` | `DECLARED`, `TESTED` | A test asserts the consumer expectation; it does not prove a provider satisfies it. |
| `CONSUMER_OBSERVED_USE` | `CONSUMED`, `TESTED` | A test exercises consumer use; it does not make the consumer a provider. |

`DECLARED`, `IMPLEMENTED`, and `CONSUMED` are invalid as primary views for
roles that do not have that perspective, such as
`CONSUMER_EXPECTATION + IMPLEMENTED` and
`PROVIDER_IMPLEMENTATION + CONSUMED`. An invalid combination is rejected by
the Technical Model Gate or retained only as unresolved evidence; it is never
accepted silently. When a test supports a role that also has a non-test view,
the accepted record retains the role's primary view and test evidence; a
separate tested record/revision may be used when the tested view itself must be
addressed. Historical IF facts without `contract_role` remain valid with their
existing `observed_view`; the matrix does not infer a role for them.

#### Protocol-specific property boundary

Common IF fields remain protocol-neutral. Protocol-specific properties are held
under one controlled `protocol_properties` object whose schema is selected by
`interface_kind`. Unsupported or unobserved properties are absent, not null
claims.

| Kind | Minimum protocol-specific properties when evidenced |
|---|---|
| `HTTP_REST` | method, path/template, host/provider reference when safe, media/content contract references |
| `GRPC_RPC` | package/service, method, protobuf contract reference/fingerprint |
| `GRAPHQL` | operation type, operation/name, field or schema address, schema reference/fingerprint |
| `WEBSOCKET` | endpoint/channel, message direction, message/topic identity where material |
| `WEBHOOK` | callback address, callback event/type, sender/receiver direction |
| `CLI` | command/subcommand, option contract reference, exit/error contract reference |
| `LIBRARY` | public symbol/module/package and call contract reference |
| `FILE_PROTOCOL` | safe file/protocol address, command/record/message shape where material |
| `IPC` | channel/name, operation, process/provider reference where evidenced |

Protocol-specific properties cannot create a second identity family. An IF
identity remains the material contract surface; a change to its semantic
operation identity follows the identity/revision rules in section 30.

### 7. Provider / consumer model

Provider and consumer records remain separate accepted facts when they arise
from different evidence, perspectives, or revisions.

```text
COMP-CUSTOMER --PROVIDES--> IF-PROVIDER@revP
  direction: PROVIDED
  contract_role: PROVIDER_DECLARATION

COMP-BILLING --CONSUMES--> IF-CONSUMER@revC
  direction: CONSUMED
  contract_role: CONSUMER_EXPECTATION
```

`IF-CONSUMER` is not rewritten to `IF-PROVIDER`. An `INT-*` may link the
consumer expectation to a concrete source and target and may optionally record
the matched provider IF after candidate matching and compatibility verification.

The minimum interaction binding is:

```text
INT-*:
  source_ref: COMP-*
  consumed_interface_ref: optional IF-*@revision
  target_ref: optional COMP-* | DS-* | qualified external identity
  provided_interface_ref: optional IF-*@revision
  event_ref: optional EVENT-*
  evidence_refs: WS-*/EV-*
  project_bindings: exact source/revision/Product qualification as applicable
```

The target or provided interface may be unknown. An unknown target is an
accepted bounded fact only when the source interaction itself is evidenced and
the unresolved precision is recorded.

Provider declaration and consumer expectation may differ:

```text
consumer expectation: GET /api/v1/customer/{id}
provider declaration:  GET /api/v1/customers/{id}
```

Both remain independently addressable. Compatibility is not implied by a
shared provider name, similar path text, or a `CONSUMES` relation.

### 8. Protocol-specific interface properties

The common model deliberately avoids a giant nullable HTTP-shaped schema.
Protocol property validation is bounded by the declared kind:

- HTTP/REST uses method plus path/template and optional request/response
  contract references.
- gRPC/RPC uses service plus method and a protobuf contract reference or
  fingerprint.
- GraphQL uses operation type/name and schema/field address; a whole schema may
  be referenced without duplicating it in STM.
- WebSocket uses endpoint/channel and message direction or topic when that is
  material.
- Webhook uses callback address and event/callback identity; sender and
  receiver remain distinct through relations and INT source/target.
- CLI uses command/subcommand and optional argument/error references.
- Public library API uses public symbol/module/package identity.
- File/protocol and IPC use safe resource/channel and operation identifiers.

An unsupported protocol-specific field does not invalidate a broad IF fact. It
produces `RESOURCE_BOUNDED` or `UNRESOLVED` precision as appropriate;
`STORE_ONLY` is not an interface precision and is never assigned to an IF
record.

### 9. EVENT-* relationship

`EVENT-*` owns the semantic event/message. Its minimum shape remains:

```text
EVENT-*:
  semantic_id
  name_or_topic
  producer_refs: COMP-*
  consumer_refs: COMP-* where evidenced
  transport_ref: optional COMP-* / DS-* / INT transport fact
  payload_ref: optional bounded schema/contract reference
  version: optional evidenced event version
  delivery_properties: optional ordering/retry/DLQ/idempotency facts
  precision
  project_binding
  evidence_refs
```

An event does not require an IF duplicate merely to appear in documentation.
`PUBLISHES` and `SUBSCRIBES` are sufficient for a Kafka topic or message fact
when the semantic event is evidenced.

Use `EVENT-* + IF-* + INT-*` for a webhook or other boundary where all three
meanings are material:

```text
EVENT-*  = order.created semantic message
IF-*     = HTTP callback contract
INT-*    = producer-to-callback interaction
```

A broker/topic binding alone is a declaration or infrastructure fact. It does
not automatically create a semantic event, producer, or consumer fact.

### 10. INT-* interaction model

`INT-*` is the primary accepted fact for one concrete interaction edge. It is
not direct dependency metadata and does not own the identity of the interface,
event, or data resource it references.

```text
INT-*:
  source_ref: COMP-*
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
  evidence_refs: required
  project/revision/baseline qualification: required
```

For data access, `target_ref` is a `DS-*` resource and `access_mode` is one of
the controlled values in section 12. For event transport, the event reference
and transport target may both be present. For an external API, target identity
is a qualified external `COMP-*`-like identity or an external source binding,
not a secret-bearing URL.

Dependency metadata remains owned by the dependent artifact and retains
`DEPENDS_ON` plus impact strength. An `INT-* CALLS` or `INT-* READ_WRITE` fact
does not automatically become a dependency edge. A dependency edge does not
prove a runtime interaction.
### 11. DS-* store/resource model

One `DS-*` identity family represents both a store-level resource and an
addressable resource inside a store. Store and child resources share the STM
identity/lifecycle model; child resources do not create `TABLE-*`, `BUCKET-*`,
or other new families.

```text
DS-*:
  semantic_id
  revision
  status / freshness / authority
  resource_kind
  parent_resource_ref: optional DS-*
  technology: optional store technology
  safe_address: optional evidence-backed logical address
  precision: EXACT | RESOURCE_BOUNDED | STORE_ONLY | UNRESOLVED
  project_binding
  evidence_refs
```

#### Controlled resource kinds

Minimum relational kinds:

```text
STORE | DATABASE | SCHEMA | TABLE | VIEW | MATERIALIZED_VIEW |
PROCEDURE | FUNCTION
```

`TRIGGER`, `INDEX`, and `SEQUENCE` are supported as optional resource kinds
when their identity is material to an accepted architectural interaction. They
are not required for the minimum service catalog.

`PROCEDURE` and `FUNCTION` are DS identities because they are database-owned
schema objects. They are not callable-interface identities by themselves. When
an independently evidenced callable contract exists—such as a declared
database API, provider/consumer contract, or materially compared invocation
surface—an IF-* may additionally represent that callable boundary. The IF and
DS records have distinct stable identities and explicit cross-references; one
does not alias or replace the other. INT-* represents the concrete invocation
with `access_mode=EXECUTE`, targets the DS schema object, and may reference the
IF callable contract.

DS-only is sufficient when evidence establishes execution against the
database-owned procedure/function but no independent callable contract or
provider/consumer comparison surface is evidenced. IF + DS is required when
the callable boundary is declared, implemented, consumed, or tested as a
contract whose operation, request/response, auth, error, or compatibility
semantics matter. A callable IF without a known database object is also valid
for an external or abstract callable surface; a known DS without such a
surface does not force an IF. This keeps DS as schema-object authority, IF as
optional callable-surface authority, and INT as invocation authority.

Minimum non-SQL kinds:

```text
COLLECTION
NAMESPACE
KEY_PATTERN
BUCKET
PREFIX
SEARCH_INDEX
VECTOR_COLLECTION
VECTOR_INDEX
FILE
PATH_PATTERN
```

The ontology is intentionally bounded. A technology-specific resource that does
not fit a controlled kind remains a store-level or resource-bounded DS fact with
its safe technology/address properties; it does not force a new family.

#### Parent/child semantics

`parent_resource_ref` records containment or address context only. No child
inherits ownership, access, or migration authority automatically. A database
connection does not imply access to every table; a database owner does not
automatically own every descendant.

When an explicit policy or evidence establishes inherited ownership, the
projection must show the inheritance source, scope, and override rule. The
default is explicit ownership on the affected resource.

### 12. Data access modes

Concrete data access is represented primarily on `INT-*`, because INT owns the
source-to-resource interaction edge.

```text
READ
WRITE
READ_WRITE
EXECUTE
DDL
MIGRATION
```

`MIGRATION` means execution of a schema/data migration operation. It is distinct
from generic `DDL`, which describes runtime or administrative schema operation.
`MIGRATION_AUTHORITY` is not an access mode; it is the separate ownership/
authority relation described in section 13.

The existing `READS_FROM` and `WRITES_TO` relations remain valid factual
navigation relations. For new precise data access, INT is the authored source
of truth. A materialized relation for the same qualified source, target,
Project/revision, and baseline is a derived STM navigation relation with an
explicit derivation link to INT; it is not a second access authority. A
projection may compute the relation without materializing it, but must use the
same derivation rule.

The derivation rule is: `READ` derives `READS_FROM`, `WRITE` derives
`WRITES_TO`, and `READ_WRITE` derives both. `EXECUTE`, `DDL`, and `MIGRATION`
do not derive either relation unless separate evidence establishes a read or
write edge. If a legacy relation exists without INT, it remains an accepted
broad historical fact and carries no inferred access mode. If a new INT
contradicts such a relation, INT is authoritative for the precise current
edge, the legacy relation is preserved with `REVALIDATION_REQUIRED` or a stale
limitation as applicable, and the contradiction is routed to bounded
revalidation; it is not silently overwritten. A relation-only record is never
upgraded to an exact INT without new evidence. Direct dependency metadata never
owns access mode.

Examples:

```text
INT-BILLING-READ:
  source_ref: COMP-REPORTING
  target_ref: DS-BILLING-INVOICES
  interaction_kind: DATA_ACCESS
  access_mode: READ

INT-BILLING-WRITE:
  source_ref: COMP-BILLING
  target_ref: DS-BILLING-INVOICES
  access_mode: READ_WRITE

INT-BILLING-MIGRATION:
  source_ref: COMP-BILLING-MIGRATIONS
  target_ref: DS-BILLING-INVOICES
  access_mode: MIGRATION
```

### 13. Ownership and migration authority

Ownership, use, and dependency remain independent dimensions:

```text
COMP-BILLING --OWNS_STATE--> DS-BILLING-INVOICES
COMP-REPORTING --READS_FROM--> DS-BILLING-INVOICES
COMP-OTHER --WRITES_TO--> DS-BILLING-INVOICES
COMP-BILLING-MIGRATIONS --MIGRATION_AUTHORITY--> DS-BILLING-INVOICES
```

The migration relation records schema/data-evolution responsibility. Its
minimum factual relation metadata is:

```text
MIGRATION_AUTHORITY:
  owner_ref: COMP-* or qualified Project owner
  resource_ref: DS-*
  source_refs: WS-*/EV-* and migration source locator
  project/revision/baseline qualification
  scope: exact resource or bounded resource set
  status: accepted / unresolved according to STM lifecycle
```

Migration source facts may additionally be represented by `CFG-*`, `DS-*`, or
`COMP-*` as appropriate, but the relation binds the authority to the affected
resource. Multiple authorities may coexist as independently accepted facts when
the evidence shows multiple migration owners or unresolved conflict. The STM
preserves the conflict; it does not automatically create `RF-*`.

Architecture Review interprets multiple writers, cross-owned writes, migration
conflicts, runtime DDL, and shared-store coupling. Stage F records facts and
does not generate findings.

### 14. SQL interaction model

The catalog records architectural access, not a full SQL AST. The minimum
semantic answer is:

```text
source -> DS resource -> access mode -> evidence -> precision -> revision
```

The following mappings are accepted when evidence supports them:

| SQL behavior | Stage F representation |
|---|---|
| SELECT | `INT-* access_mode=READ` to table/view/resource |
| INSERT / UPDATE / DELETE | `INT-* access_mode=WRITE` |
| UPSERT / MERGE | `INT-* access_mode=READ_WRITE` unless evidence distinguishes phases |
| Procedure/function call | `INT-* access_mode=EXECUTE` to `PROCEDURE`/`FUNCTION` DS |
| DDL | `INT-* access_mode=DDL` to schema/database/resource |
| Migration/schema evolution | `INT-* access_mode=MIGRATION` plus `MIGRATION_AUTHORITY` where responsibility is evidenced |
| Dynamic SQL | same model with `UNRESOLVED` or `RESOURCE_BOUNDED` precision |

Raw SQL, ORM-generated SQL, repositories, and migrations remain evidence
acquisition paths, not separate semantic authorities. The catalog does not
preserve every SQL verb/token when a bounded access mode sufficiently explains
the architectural interaction.

### 15. Non-SQL interaction model

The same DS/INT model applies across non-SQL stores:

| Store | Example accepted resource | Access representation |
|---|---|---|
| Redis | `NAMESPACE` or `KEY_PATTERN` | `READ`, `WRITE`, or `READ_WRITE` |
| MongoDB/document store | `COLLECTION` | `READ`, `WRITE`, or `READ_WRITE` |
| Elasticsearch/OpenSearch | `SEARCH_INDEX` | `READ`, `WRITE`, or `READ_WRITE` |
| S3/object storage | `BUCKET` or `PREFIX` | `READ`, `WRITE`, or `READ_WRITE` |
| Vector database | `VECTOR_COLLECTION` or `VECTOR_INDEX` | `READ`, `WRITE`, or `READ_WRITE` |
| Filesystem | `FILE` or `PATH_PATTERN` | `READ`, `WRITE`, or `READ_WRITE` |
| Embedded store | database/file/resource DS | applicable data access mode |

Only evidence-supported precision is accepted. A Redis client proves Redis use,
not a key pattern. A bucket/prefix is recorded only when the source establishes
it. A generic object-storage client with a runtime-generated bucket remains
store-level or unresolved.

### 16. Evidence strength and acceptance

Evidence strength, fact precision, observed view, and STM acceptance are
separate dimensions.

```text
evidence strength -> what the source supports
precision         -> how exact the accepted fact is
observed view     -> DECLARED / IMPLEMENTED / CONSUMED / TESTED perspective
STM lifecycle     -> CANDIDATE ... ACCEPTED ...
```

#### Evidence classes

`DIRECT_DECLARATION` is a source that explicitly declares a surface, contract,
binding, schema, migration, or resource. It can support a declared fact when
baseline-bound and contextually applicable.

`STRONG_INFERENCE` is an implementation path whose concrete call, binding, or
resource use is materially clear even if no formal declaration exists. It can
support an implemented or consumed fact with its inference limitation retained.

`WEAK_HINT` is contextual evidence such as a dependency declaration, a generic
database connection, a configuration URL, an unused generated client, or a
provisioned infrastructure resource. It cannot alone create an accepted
concrete API call, event use, or entity-access fact.

Required prohibitions:

```text
config URL exists       != API definitely called
SDK installed           != external service used
DB connection exists    != table accessed
migration mentions X    != runtime access to X
generated client exists != client method is used
```

The accepted STM fact records supporting evidence and limitations. A weak hint
may motivate targeted evidence discovery but is not factual acceptance.

### 17. Precision / unresolved-state model

Precision is an explicit semantic dimension, independent of status, freshness,
coverage, confidence, and observed view:

Precision applicability is family-specific. `EXACT`, `RESOURCE_BOUNDED`, and
`UNRESOLVED` are valid for IF, EVENT, FLOW, and all applicable INT facts.
`STORE_ONLY` is valid only for a DS store-level fact or a DATA_ACCESS INT whose
target DS entity is unresolved but whose parent store is known. It is invalid
for IF, EVENT, FLOW, and non-data INT facts. Precision remains one semantic
dimension, but selectors must validate its family-specific subset; it is never
confidence, coverage, freshness, or observed view.

```text
EXACT
RESOURCE_BOUNDED
STORE_ONLY
UNRESOLVED
```

| Precision | Meaning |
|---|---|
| `EXACT` | Operation/resource identity and relevant target are evidenced at the represented granularity. |
| `RESOURCE_BOUNDED` | A bounded pattern, range, family, or parent/child resource is known, but not one exact operation/resource. |
| `STORE_ONLY` | A DS store or DATA_ACCESS target's parent store is known, but an entity-level target is not established. |
| `UNRESOLVED` | The interaction is known, but a required target or operation cannot be resolved from available evidence. |

Examples:

- A runtime-generated customer path has a known provider and HTTP surface but
  unresolved exact operation: `UNRESOLVED` operation precision.
- PostgreSQL is used but no table can be proven: `STORE_ONLY`.
- Redis `invoice:*` is evidenced: `RESOURCE_BOUNDED` with `KEY_PATTERN`.
- S3 `bucket/invoices/` is evidenced: `RESOURCE_BOUNDED` or `EXACT` according
  to whether the operation/address is fully established.

An interface with an unresolved method, operation, or protocol property uses
`UNRESOLVED` or `RESOURCE_BOUNDED`, never `STORE_ONLY`. A non-data interaction
with a known system but unknown operation is likewise unresolved rather than
store-only.

Precision never upgrades silently. A later stronger observation creates a new
accepted revision or enrichment while preserving the earlier limitation and
evidence history.

### 18. Observed views

The existing observed views remain the only view vocabulary:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

Recommended usage:

| Evidence perspective | IF/INT/EVENT view |
|---|---|
| OpenAPI/protobuf/router/schema declaration | `DECLARED` |
| Executable route, handler, client, producer, or repository path | `IMPLEMENTED` |
| Client expectation or observed outbound/use path | `CONSUMED` |
| Contract/compatibility test | `TESTED` |

These views do not establish precedence. A provider may have declared and
implemented views; a consumer may have declared expectation and consumed call;
tests may support either side. The Technical Model Gate and Contract
Verification boundary adjudicate meaning; projections do not choose a winner.

### 19. Provider/consumer matching

Candidate matching is a bounded, non-authoritative relation between accepted
provider and consumer IF revisions. It is not compatibility and it is not a
fuzzy identity merge.

Candidate matching may use, in decreasing evidentiary strength:

1. explicit declared linkage;
2. qualified provider identity and Project relation;
3. protocol/interface kind;
4. operation identity;
5. address/path/topic or protocol-specific operation;
6. contract/version reference or fingerprint;
7. generated-client/OpenAPI/protobuf provenance.

The output is one of:

```text
MATCH_CANDIDATE
NO_MATCH_ESTABLISHED
MATCHING_INDETERMINATE
```

`MATCH_CANDIDATE` never aliases or merges the IF identities. Exact accepted
provider and consumer revisions remain the inputs to compatibility verification.
Fuzzy path/name similarity alone cannot establish a match.

### 20. Compatibility verification

Compatibility is a derived Contract Verification result over two accepted,
revision-qualified IF facts. It is not a new STM family, a new engine, an
`RF-*`, or an automatic runtime action.

The comparison input is:

```text
provider_if_ref: IF-*@revision
consumer_if_ref: IF-*@revision
provider_project/revision/baseline
consumer_project/revision/baseline
protocol and operation/address properties
contract/version references or fingerprints
request/input contract where applicable
response/output contract where applicable
auth expectations where relevant
error contract where relevant
supporting WS-*/EV-* evidence
```

The bounded result vocabulary is:

```text
COMPATIBLE
INCOMPATIBLE
INDETERMINATE
NOT_COMPARABLE
```

`INDETERMINATE` is mandatory when required comparison data is missing or
unresolved. `NOT_COMPARABLE` is used when the records are different kinds of
surfaces or no valid comparison relation exists. Missing data never means
compatible.

When a materially relevant declared external contract exists, Contract
Verification runs automatically under the existing Test Engineering
applicability rule. It creates or updates the existing `CC-*` record with the
exact provider/consumer IF revisions, compared views, mismatch evidence, and
adjudication state. Stage F does not add a result field or classification to
CC; the four Stage F values are a normalized projection of the existing CC
state:

| Stage F result | Required existing CC state |
|---|---|
| `COMPATIBLE` | `CC.status=RESOLVED` and its adjudication explicitly accepts the compared behavior as compatible; `INTENTIONAL_COMPATIBILITY_BEHAVIOR` may be the recorded classification. |
| `INCOMPATIBLE` | `CC.status=RESOLVED` and its adjudication explicitly accepts a material incompatibility, with a material mismatch classification such as `DECLARATION_STALE`, `IMPLEMENTATION_DEFECT`, `CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR`, or `TEST_ENCODES_STALE_CONTRACT`. |
| `INDETERMINATE` | Required comparison data is absent/unresolved, or CC remains `OPEN`, `CLASSIFIED`, or `WONT_RESOLVE`, including `AUTHORITY_UNRESOLVED` or `CONTRACT_UNRESOLVED`. |
| `NOT_COMPARABLE` | The accepted records do not form a valid comparison pair under the selected contract type, so no CC comparison is created. |

`COMPATIBLE` is never inferred from the absence of a mismatch, and an
unresolved or non-final CC record never becomes compatible. If the existing
Contract Verification applicability rule is not met, there is no Stage F
compatibility result; a catalog may show only non-authoritative candidate or
not-evaluated information tied to the exact inputs. That display cannot become
an `CC-*`, `RF-*`, or STM fact by appearing in a document. Architecture Review
may interpret a resolved material incompatibility as `RF-*`; Test Engineering
remains the owner of the `CC-*` record and may consume the normalized result
for verification planning.
### 21. External integration model

No external-service identity family is introduced. External identity uses
existing `COMP-*`, `IF-*`, `INT-*`, `DS-*`, `AUTH-*`, and `CFG-*` with an
external/source qualification:

```text
external_identity:
  logical_name
  kind: THIRD_PARTY_SAAS | IDENTITY_PROVIDER | PAYMENT_PROVIDER |
        CLOUD_API | EXTERNAL_DATABASE | OBJECT_STORE | OTHER
  source_binding: external locator/revision or limitation
  owner/provider: known logical owner where evidenced
  safe_identifier: safe non-secret display identity
```

An external consumed API is an `IF-*` expectation plus an `INT-*` interaction
when the call is evidenced. An external data source is a `DS-*` resource plus
an `INT-*` access edge. `AUTH-*` is referenced for the mechanism; secret values
are never copied.

Internal Product-member, internal non-member, and external identities remain
distinct through Project/Product qualification and source binding. A configured
URL, SDK, or infrastructure declaration alone remains a weak hint.

### 22. Secret and sensitive-identifier policy

Stage F projections and catalog fields have a deterministic safety rule:

```text
secret values never appear in STM catalog fields, copied evidence excerpts,
generated Interface/Data catalogs, projection metadata, or package summaries
```

The following are always `SECRET` and must be omitted/redacted:

- passwords, API keys, access/refresh tokens, client secrets, and private keys;
- credentials embedded in URLs or connection strings;
- secret query parameters;
- raw environment secret values;
- database credentials and equivalent bearer material.

Evidence may reference a file, symbol, line/range, variable name, and baseline
without copying the value.

Identifiers use three bounded sensitivity classes:

```text
SECRET
SENSITIVE_INTERNAL
SAFE_TECHNICAL_IDENTIFIER
```

`SAFE_TECHNICAL_IDENTIFIER` may include logical service/store names, ordinary
API paths, schema/table names, event names, and non-secret operation names.
`SENSITIVE_INTERNAL` covers private hostnames, usernames, sensitive filesystem
paths, and internal locators; projections show a logical alias or redacted
form unless a source policy explicitly marks the identifier safe. `SECRET` is
never displayed.

For a connection string, a projection may show technology, logical store,
database/schema, and safe endpoint class, but not the full credential-bearing
value. Redaction must preserve enough safe architecture identity to make the
catalog useful.

### 23. Service documentation projections

The Design selects shape **B: multiple standardized projections inside the
existing Technical Documentation package**, with the existing files extended
by Stage F semantics. This avoids a second lifecycle and avoids unnecessary
file proliferation while keeping an obvious user path.

The standard Service experience is:

```text
# <Service>
## Interfaces provided          -> PRJ-TECH-DOC-02-PROVIDED-INTERFACES
## Interfaces consumed          -> PRJ-TECH-DOC-03-CONSUMED-INTERFACES
## Integrations and external    -> PRJ-TECH-DOC-04-INTEGRATIONS
## Events produced/consumed     -> PRJ-TECH-DOC-04-INTEGRATIONS
## Datastores and data access   -> PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE
## Schema/migration authority   -> PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE
## Dependencies                 -> existing dependency projection/section
## Evidence and limitations     -> every selected section and overview
## Unknown/unresolved           -> every selected section and overview
```

The existing `00-system-overview` is the entry point and links the sections.
The existing projections remain distinct and keep their current identities;
Stage F adds their controlled selectors and section content rather than
creating a parallel Service Catalog authority. If a future package needs a
single landing document, it is a projection assembly over these sections, not
a new factual record.

Required Service package members are the existing Technical Documentation
overview plus selected provided interfaces, consumed interfaces, integrations,
and data/persistence sections. Event content is conditionally required only
when accepted event facts exist or the explicit documentation scope selects it.
Empty-but-verified and not-applicable sections are represented by existing
projection/package status rather than omitted silently.

Every section must answer the user questions without requiring STM internals:

- What API/interface does this service provide?
- What API/interface does it call or expect?
- What external systems does it call?
- What data stores and addressable entities does it access?
- What does it own or evolve?
- Which details are unknown or unresolved?

### 24. Product documentation projections

Product mode reuses Stage E Product identity, accepted Product revision,
immutable baseline vector, qualified Project/source references, and Product
Technical Documentation package mechanics. It introduces no Product factual
authority.

The standard Product projections are:

| Projection | Purpose | Authority inputs |
|---|---|---|
| Product Interface Catalog | Qualified provided and consumed interface inventory | accepted qualified IF-* and provider/consumer relations |
| Product Integration Map | Service-to-service, service-to-external, event, and interaction topology | qualified INT-*, EVENT-*, IF-* references |
| Product Data Access Map | Qualified store/entity access, ownership, and migration authority | qualified DS-*, INT-* access facts, ownership/migration relations |
| External Integrations Catalog | External providers, APIs, stores, auth references, and evidence limitations | qualified external COMP/IF/INT/DS/AUTH facts |
| Provider/Consumer Matrix | Optional matrix of exact expectations, matches, and compatibility results | qualified IF revisions and Contract Verification results |

All Product references include stable Project identity, family, local identity,
accepted revision, and Product baseline binding. A Product projection can show
unavailable or partial members using the existing independent availability
dimensions. It cannot collapse them into a universal Product success/failure
status.

### 25. Projection/package lifecycle integration

Stage F uses the existing Stage B projection lifecycle without modification in
meaning:

```text
PRJ-* identity
-> contract and dependency binding
-> selector resolution snapshot
-> generation
-> V1-V4 verification
-> accepted projection revision/fingerprint
-> CURRENT | STALE | BLOCKED
```

`RG-*` remains the explicit regeneration session. A changed IF, INT, DS, EVENT,
or dependency/selector contract marks only affected projections stale or
blocked. No automatic regeneration occurs.

Stage F selectors may use controlled STM dimensions such as `entity_type`,
`direction`, `resource_kind`, `interaction_kind`, `access_mode`, `precision`,
formal relations, accepted status, freshness, authority, and qualified Product
scope. Selectors remain deterministic and finite. They cannot interpret prose,
execute SQL, or infer facts from filenames.

Package membership remains an explicit finite declaration with required,
optional, and conditional members. Package policy remains `PERMISSIVE`,
`REQUIRED_SCOPE_CURRENT`, or `ALL_SCOPED_CURRENT`.

### 26. Revalidation and impact

Stage F preserves bounded, impact-driven `REVALIDATE`:

```text
changed evidence/fact
 -> direct semantic dependencies and affected relations
 -> affected IF/INT/DS/EVENT facts
 -> affected Service/Product projections
 -> affected package scope only
```

Examples:

- A changed provider operation revalidates its provider IF, matched consumer
  candidates/compatibility results, and dependent projections.
- A changed table access revalidates the affected INT and DS resource plus
  dependent Service/Product data projections.
- An unavailable Project limits only Product projections whose qualified scope
  requires that Project; it does not mark unrelated Product or Project facts
  clean, failed, or universally invalid.

Projection impact accounting does not regenerate. A full re-audit is not
automatic and remains governed by existing impact/revalidation rules.

### 27. Single-project compatibility

Stage F is fully valid without Product identity, Product membership, Product
baseline, or cross-project evidence. A single Project can produce:

- provided and consumed interface projections;
- event catalog content;
- internal and external integration content;
- store/entity access and migration content;
- evidence, precision, and limitation views.

Product is additive qualification and aggregation. Single-project mode is not a
degraded Product mode and does not require Product state.

### 28. Stage E Product compatibility

Stage F preserves the Stage E invariants:

- Product is optional and not a universal semantic owner;
- Product revision and Product baseline remain distinct;
- baseline is an immutable vector of exact Project/source bindings, not one SHA;
- local Project facts remain locally authoritative;
- cross-project facts retain qualified Project/revision/baseline provenance;
- external sources retain exact locator/revision or explicit limitation;
- source availability, semantic availability, projection freshness, and package
  gate remain separate dimensions;
- `EXTEND` is additive and `REVALIDATE` is bounded and impact-driven;
- Product membership grants no repository or publication permission;
- Product projections and packages reuse Stage B lifecycle and package rules.

### 29. Historical/backward compatibility

Migration is additive and compatible:

- an old broad HTTP IF remains a valid broad IF with absent or unknown
  operation properties;
- an old PostgreSQL DS remains a valid store-level DS;
- an old INT without access mode remains valid at prior precision;
- an old EVENT without a protocol-specific transport property remains valid;
- old Project-local facts require no Product conversion;
- old IDs are not rewritten;
- historical evidence is not enriched by silently changing its meaning;
- newly evidenced qualifiers create a new revision or new child fact;
- a materially ambiguous old fact receives an explicit limitation or targeted
  revalidation, not a silent precision upgrade.

Existing projections remain interpretable. New selectors must treat absent Stage
F qualifiers as absent/unknown, not as false and not as exact. Historical facts
do not become stale solely because the Design adds optional fields; they become
subject to contract/impact revalidation only when a selected projection or
semantic dependency requires it.

### 30. Identity/revision rules

Identity is stable semantic identity, not a mutable display string. A record uses
the same identity with a new revision when the logical contract/resource or
interaction remains the same and the change is a revision of its accepted
description, evidence, precision, or non-identity property.

A new identity is used when the semantic subject changes. Default rules:

| Change | Identity rule |
|---|---|
| HTTP method/path changes | New IF identity unless explicit stable operation identity and provider evidence establish continuity; otherwise new identity supersedes old. |
| API version changes | New IF identity for a distinct externally addressable version; same identity revision only for a corrected/non-semantic version annotation. |
| Table rename | New DS identity by default; `supersedes` may preserve proven logical continuity. |
| Schema move | New DS identity unless an explicit migration/continuity fact proves the same logical resource. |
| Redis key-pattern change | New DS identity when the addressed population changes; revision for a non-semantic normalization. |
| Provider change | New INT identity for a changed concrete edge; existing consumer IF remains independent. |
| Consumer change | New INT identity and, when the expectation changes, new consumed IF identity. |
| Evidence/precision enrichment | Same identity, new revision when semantic subject is unchanged. |

Where continuity is uncertain, preserve both identities with explicit
`supersedes` history and `UNRESOLVED`/limitation state. No universal mutable
string canonicalization engine is required.
### 31. Architecture Review/Test Engineering consumers

Architecture Review consumes accepted IF/INT/DS/EVENT/FLOW facts to interpret
properties and findings. Stage F does not create automatic `RF-*` for multiple
writers, cross-owned writes, migration conflicts, DDL rights, or external
dependencies.

Test Engineering may consume:

- IF provider/consumer facts for behavior and contract verification;
- exact provider/consumer revisions for `CC-*` comparison;
- EVENT facts for event behavior and E2E planning;
- INT/DS access facts for environment and integration scenarios;
- precision and evidence limitations for assurance scope.

Test Engineering remains the owner of `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`,
and `TASK-*`. The catalog does not rewrite those authorities.

Code Quality may consume the same accepted STM facts and remains the owner of
`CQ-*`/`CQRA-*`. Product aggregation does not transfer any of these ownerships.

### 32. Design invariants

1. Catalog is not factual authority.
2. `IF-* != INT-* != DS-* != EVENT-* != FLOW-*`.
3. Provider declaration is not consumer expectation.
4. A consumer expectation may exist without a matched provider.
5. Compatibility requires exact accepted provider and consumer revisions.
6. Missing comparison data is not compatibility.
7. Store-level knowledge is not entity-level access.
8. A database connection is not table access.
9. Migration evidence is not runtime access.
10. Usage is not ownership.
11. Relation is not dependency.
12. A fact is not an `RF-*` finding.
13. Evidence precision never increases silently.
14. A weak hint alone cannot become an accepted concrete interaction.
15. Secret values never appear in user-facing catalogs.
16. Product remains optional.
17. Project-local factual authority remains reusable.
18. Existing projection/package lifecycle authority is reused.
19. Historical broad facts remain valid at their prior precision.
20. No automatic regeneration or full re-audit occurs from a semantic change.

### 33. Pressure scenarios

The following fail-first scenarios are Design acceptance inputs for later
validation. They are not tests or implementation tasks in this artifact.

| ID | Required behavior |
|---|---|
| PS-F01 | Provider REST operation from router/OpenAPI becomes a provided IF with declaration evidence. |
| PS-F02 | Consumer exact internal call becomes a consumed IF and INT linked to the provider when evidenced. |
| PS-F03 | Different consumer/provider paths coexist without aliasing; an applicable Contract Verification produces `INCOMPATIBLE` only after a resolved material mismatch, otherwise `INDETERMINATE` or no result when not comparable/applicable. |
| PS-F04 | Known provider with dynamic operation remains unresolved at operation precision. |
| PS-F05 | External base config without call evidence remains a weak hint, not an accepted call. |
| PS-F06 | Generated client that is unused does not become an external integration. |
| PS-F07 | One PostgreSQL table read becomes a DS table plus INT READ at evidence-supported precision and derives `READS_FROM` without a second access authority. |
| PS-F08 | A write into another service's owned table remains a fact, not an automatic RF. |
| PS-F09 | Two services writing one table are retained as separate INT WRITE facts, each deriving `WRITES_TO`; ownership and architecture interpretation remain separate. |
| PS-F10 | Migration owner differs from runtime writer and both facts coexist. |
| PS-F11 | Dynamic raw SQL records known store/resource bounds and unresolved target. |
| PS-F12 | ORM model plus ambiguous operation preserves evidence and precision limitation. |
| PS-F13 | Redis store is known while unknown key pattern remains STORE_ONLY. |
| PS-F14 | S3 bucket/prefix access is represented only when evidenced. |
| PS-F15 | Event production/consumption works without a duplicate IF. |
| PS-F16 | Webhook uses EVENT + IF + INT when all three semantics are material. |
| PS-F17 | Secret-bearing connection string is referenced safely without secret output. |
| PS-F18 | Private hostname is redacted or replaced by a safe logical identifier. |
| PS-F19 | Historical broad IF remains valid after extension. |
| PS-F20 | Historical store-level DS remains valid without entity enrichment. |
| PS-F21 | Single Project produces a complete Service catalog without Product. |
| PS-F22 | Product aggregates exact Project revisions into Product Interface Catalog. |
| PS-F23 | Unavailable Project yields partial Product availability, not universal failure or clean state. |
| PS-F24 | Provider change impacts only dependent consumers and projections. |
| PS-F25 | Weak-hint configuration does not become an accepted API call. |
| PS-F26 | Missing schema in an applicable provider/consumer comparison creates/updates CC and returns `INDETERMINATE`, never `COMPATIBLE`; non-applicable comparison remains candidate/not-evaluated only. |

### 34. Explicit non-goals

Stage F does not include:

- live database scanning or runtime database introspection;
- runtime traffic capture or distributed tracing;
- service mesh or API gateway behavior;
- schema registry replacement;
- OpenAPI generator implementation;
- a full SQL parser or generic ORM framework;
- a database reverse-engineering engine;
- CMDB or required graph database;
- a new RAG system or runtime service;
- an automatic API compatibility engine;
- automatic `RF-*` generation;
- automatic projection regeneration.

### 35. Migration classification

```text
migration: COMPATIBLE_EXTENSION
```

The target extends existing STM meanings with optional, evidence-bounded
properties, child DS identities, controlled relation vocabulary, and projection
selectors. It does not rewrite IDs, invalidate all historical facts, force
Product mode, or require a destructive migration.

Historical `READS_FROM`/`WRITES_TO` relations remain accepted broad facts when
no INT exists; they are not assigned inferred access modes. New precise INT
facts become authoritative for their qualified edge and may derive navigation
relations. Existing `CC-*` records retain their own status, classification,
and adjudication semantics; Stage F only normalizes them for catalog display.
Absent Stage F qualifiers do not create unsafe defaults or invalidate the old
record.

If a historical fact later proves materially incompatible with a new semantic
definition, the owning Technical Model Gate performs bounded revalidation or
supersession. The old record remains historical evidence; Design does not
silently change the classification.

### 36. Likely implementation contract surface

This is a future contract-impact preview, not an Implementation Plan and not a
file-change authorization. Exact files must be verified at the next gate.

| Contract area | Likely semantic concern |
|---|---|
| `references/shared-technical-model.md` | IF common/protocol properties, DS resource kinds, INT access modes, precision, and `MIGRATION_AUTHORITY` relation. |
| `references/shared-evidence-model.md` | Only if evidence-class or redaction metadata must be shared by accepted facts; existing WS/EV ownership remains. |
| `references/technical-model-dependencies.md` | Only if Stage F selectors or aspect dependencies require controlled extension; data interactions are not dependency edges. |
| `references/technical-documentation.md` | Stage F selectors, Service section semantics, Product catalog projections, and package membership. |
| `references/projection-lifecycle.md` / dependency contracts | Only if controlled Stage F selector dimensions require compatible contract extension. |
| Product contract | Qualified Product projection selectors and external/source limitations only; no Product fact family. |
| Capability contracts | Contract Verification consumption/adjudication boundary, Architecture interpretation boundary, and Test Engineering consumers where required. |
| Pressure-scenario references | Later validation of PS-F01 through PS-F26. |

No file in this preview is modified by this Design gate.

### 37. Nine-question decision table

| Question | Decision | Alternatives considered | Reason | Authority impact | Backward compatibility | Product impact | Implementation consequence | Remaining ambiguity |
|---|---|---|---|---|---|---|---|---|
| Q1 provider/consumer record | Separate provider and consumer IF facts; INT binds concrete interaction and optional match | Alias both sides; make provider/consumer one IF; new API family | Preserves expectation/declaration differences and two-sided provenance | Existing IF/INT/STM only | Additive; old direction facts remain valid | Qualified sides remain distinct | Add roles/references and match status | None foundational |
| Q2 operation/address fields | Common neutral core plus kind-specific `protocol_properties` | HTTP-shaped universal schema; fully separate families | Avoids meaningless nullable fields and preserves protocol semantics | IF extension only | Broad IF may omit properties | Qualified protocol fields project safely | Add controlled property validation | Exact field vocabulary is bounded by this Design |
| Q3 DS entity identity | One DS family with store and addressable child resources | Nested prose only; new table/entity family | Stable targets are needed for relations, ownership, access, and impact | DS extension, no new family | Store-level DS remains valid | Child resources are Project-qualified | Add resource kind/parent/address/precision | Technology-specific kinds remain bounded |
| Q4 access-mode owner | INT-* owns concrete source-to-resource access mode; `READS_FROM`/`WRITES_TO` are derived navigation relations with explicit INT derivation when precise access exists | DS ownership; FLOW ownership; dependency metadata | Access mode describes an interaction, not resource identity or impact; `READ_WRITE` derives both relations | INT extension; no dependency authority | Legacy relation-only facts remain broad and are not upgraded without evidence | Qualified INTs project maps; contradictions are revalidated | Add access modes, derivation links, and conflict handling | None foundational |
| Q5 migration authority | `OWNS_STATE` for state ownership plus `MIGRATION_AUTHORITY` for evolution responsibility | Treat migration as WRITE/DDL; new ownership family | Authority is not a runtime operation | Controlled relation extension | Existing ownership remains valid | Product shows qualified authority conflicts | Bind owner/resource/source/baseline | Conflict policy is explicit unresolved fact |
| Q6 precision state | One vocabulary with family-specific applicability: `STORE_ONLY` only for DS store facts and DATA_ACCESS INT; IF/EVENT/FLOW/non-data INT use `EXACT`, `RESOURCE_BOUNDED`, or `UNRESOLVED` | Confidence-only; prose limitations; nullable fields; one unrestricted enum | Precision must not be confused with confidence or freshness, and selectors must not treat store-only as interface precision | STM property with family validation | Old facts retain historical/broad precision; absent fields are not inferred | Product preserves partial precision without false interface filtering | Add applicability validation and family-aware selectors | None foundational |
| Q7 compatibility | Automatic Contract Verification when applicable; existing `CC-*` owns the exact comparison/adjudication, while Stage F values are a normalized projection of CC state | New compatibility engine; RF result; fuzzy matcher; optional competing display truth | Reuses existing verification boundary, maps final CC adjudication to results, and prevents missing-data optimism | Existing CC authority; non-applicable comparisons are candidate/not-evaluated only | No historical rewrite; existing CC records remain valid | Product matrix consumes only exact qualified CC-derived results | Map CC status/classification/adjudication without redefining CC | None foundational |
| Q8 redaction | `SECRET`, `SENSITIVE_INTERNAL`, `SAFE_TECHNICAL_IDENTIFIER`; deterministic omission/redaction | Copy source values; redact everything; security-only prose | Protect secrets without destroying architectural utility | Projection/evidence boundary; no new fact family | Existing evidence pointers remain usable | Product applies same safe policy | Add redaction metadata/rules | Source-specific safe allowlist policy |
| Q9 standard documents | Extend existing Technical Documentation package sections; standard Product maps reuse PRJ lifecycle; Provider/Consumer Matrix optional | One giant document; parallel catalog lifecycle; all documents mandatory | Fits existing projections and avoids file/lifecycle proliferation | Existing PRJ/package authority | Existing docs remain interpretable | Product outputs are qualified projections | Add selectors/package conditions | Exact optional-output selection remains package-owned |

### 38. Remaining questions

Foundational open questions: **0**.

The remaining matters are implementation-level choices within the resolved
semantics: exact serialization, filenames, selector IDs, storage layout,
fingerprint algorithm, and validation tooling. They must not alter the
authority, identity, precision, compatibility, redaction, or lifecycle decisions
above.

### 39. Design verdict

```text
recommended_direction: B
new_identity_family_required: NO
IF_model: RESOLVED
provider_consumer_model: RESOLVED
protocol_property_model: RESOLVED
INT_model: RESOLVED
EVENT_relationship: RESOLVED
DS_entity_model: RESOLVED
data_access_mode: RESOLVED
data_ownership: RESOLVED
migration_authority: RESOLVED
sql_model: RESOLVED
non_sql_model: RESOLVED
precision_model: RESOLVED
evidence_acceptance: RESOLVED
compatibility_boundary: RESOLVED
external_identity: RESOLVED
redaction_policy: RESOLVED
service_document_package: RESOLVED
product_document_package: RESOLVED
single_project_compatibility: PRESERVED
stage_e_compatibility: PRESERVED
historical_compatibility: PRESERVED
projection_lifecycle_reuse: YES
package_authority_reuse: YES
migration: COMPATIBLE_EXTENSION
foundational_open_questions: 0
```

**Verdict:** `STAGE_F_DESIGN_COMPLETE`

This Design is ready for the required Independent Design Review. It is not
`STAGE_F_DESIGN_APPROVED` and does not authorize implementation.
