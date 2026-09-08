# Stage F — Interface, API & Data Integration Catalog
## Discovery

**Date:** 2026-09-07
**Artifact type:** Discovery only
**Repository:** `/home/tod/skills/architecture-code-review`
**Branch:** `main`
**Baseline:** `7cace524785aa70bbe2d47797e44134bc878bb06`
**Stage E closeout:** `7cace524785aa70bbe2d47797e44134bc878bb06`
**Stage E promotion merge:** `c0cb853e9c7656f0e045816773c9e79d650186fb`

This document is an evidence-bounded Discovery artifact. It does not define a
Stage F Design, implementation plan, new runtime capability, normative contract
change, or roadmap change.

### 1. Baseline

The repository gate passed before discovery:

| Check | Result |
|---|---|
| Branch | `main` |
| Local `HEAD` | `7cace524785aa70bbe2d47797e44134bc878bb06` |
| `origin/main` | `7cace524785aa70bbe2d47797e44134bc878bb06` |
| Tracked modifications | None |
| Pre-existing untracked files | Exactly the four user-whitelisted paths; preserved unchanged |

The four pre-existing untracked files are outside this Discovery scope. No
branch, worktree, commit, push, merge, tag, release, deployment, reset, stash,
clean, or roadmap operation was performed.

### 2. Problem statement

The current model deliberately separates observations, accepted technical facts,
capability interpretations, and projections. Stage F asks whether that model
can produce complete, evidence-backed catalogs of interfaces and data
interactions without turning a report into a new factual authority.

The question is not whether a document can mention an endpoint or database. The
question is whether the accepted model can preserve, independently and
revision-safely:

- what a service provides versus what it consumes;
- provider, consumer, protocol, operation, address, version, contract, auth,
  errors, direction, and provenance;
- event publication and subscription;
- store-level and entity-level data access, access mode, and ownership;
- schema/migration authority;
- external-system identity and integration evidence;
- uncertainty where repository evidence cannot resolve the exact target; and
- Project/Product qualification and projection freshness.

### 3. Existing authority model

The current authority chain is already suitable for Stage F in principle:

```text
WS-* / EV-* Shared Evidence
        -> accepted STM facts and relations
           COMP-* IF-* INT-* DS-* EVENT-* FLOW-* AUTH-* CFG-* ERR-*
        -> capability interpretations such as RF-* where applicable
        -> PRJ-* projections and packages
```

`WS-*` is a bounded workset and `EV-*` is a baseline-bound observation with a
source, symbol/range where available, observed fact, and baseline binding
(`references/shared-evidence-model.md`, sections 1–4). STM facts retain stable
identity, revision, baseline, lifecycle, freshness, relations, and provenance
references (`references/shared-technical-model.md`, sections 2–5).

The STM Technical Model Gate is the sole writer of accepted technical fact
semantics. A report, generated index, projection, or package cannot accept or
revise a technical fact. This preserves the required boundary:

```text
catalog != factual authority
relation != dependency
reverse index != dependency authority
projection != semantic owner
```

The controlled STM relation vocabulary already includes `PROVIDES`, `CONSUMES`,
`CALLS`, `PUBLISHES`, `SUBSCRIBES`, `READS_FROM`, `WRITES_TO`, `OWNS_STATE`,
`DEPENDS_ON`, and related relations (`references/shared-technical-model.md`,
section 2). Direct dependency metadata and reverse indexes remain separate
(`references/technical-model-dependencies.md`, sections 1–5).

Stage E preserves this model for Product scope. Product is optional; Project
facts remain locally owned; cross-project facts use qualified Project identity,
family, local ID, revision, Product revision, baseline, and evidence. Product
does not become a second factual model or universal technical owner
(`references/product-multi-project-review.md`, sections 7–10 and 13–14).

### 4. Current IF-* capability

#### Current meaning

`IF-*` is a material interaction surface. The current foundation design
explicitly lists HTTP, gRPC, IPC, CLI/public command, WebSocket,
webhook/callback, public library API, and file/protocol surfaces. It has a
`direction` property with `PROVIDED` and `CONSUMED` values
(`docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`,
sections 6.2 and 7).

The current Technical Documentation selectors independently project
`IF-* direction = PROVIDED` and `IF-* direction = CONSUMED`
(`references/technical-documentation.md`, selector table and projections
`PRJ-TECH-DOC-02-PROVIDED-INTERFACES` and
`PRJ-TECH-DOC-03-CONSUMED-INTERFACES`).

#### Capability matrix

| Question | Current result | Evidence / discovery gap |
|---|---|---|
| What is an IF-*? | YES | Material interaction surface; foundation design §6.2. |
| HTTP / REST endpoint | PARTIAL | HTTP is explicit; REST resource/method semantics are not separately defined. A REST endpoint can be represented as an HTTP interface only if the structured properties are extended or the evidence is kept at HTTP-surface granularity. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| gRPC/RPC method | PARTIAL | gRPC is explicit, but method/service/address/version fields are not normatively defined. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| GraphQL operation | NO / AMBIGUOUS | GraphQL is not named in the supported kinds. It may fit “HTTP” or “public API,” but operation/schema identity is not defined. **AMBIGUOUS_CONTRACT / IMPORTANT**. |
| WebSocket endpoint | YES at surface level | WebSocket is explicitly supported; message/channel operation detail is not specified. **INSUFFICIENT_GRANULARITY / NICE_TO_HAVE** for message-level catalogs. |
| Webhook | YES at surface level | Webhook/callback is explicitly supported; sender/receiver callback contract details are not defined. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| CLI interface | YES at surface level | CLI/public command is explicitly supported; command, options, exit/error contract fields are not defined. **INSUFFICIENT_GRANULARITY / NICE_TO_HAVE**. |
| Event/message interface | PARTIAL | Event/message has its own `EVENT-*` family; an event may be an integration surface, but the current contract does not state when an event is also an `IF-*`. **AMBIGUOUS_CONTRACT / IMPORTANT**. |
| Provider/owner | PARTIAL | `PROVIDES` and component relations can identify a provider; an explicit provider-owner field and ownership semantics are not defined. **MISSING_OWNERSHIP / FOUNDATIONAL**. |
| Consumer | PARTIAL | `CONSUMES`, `CALLS`, and `INT-*` can identify a consumer; a first-class consumer binding on an interface is not defined. **MISSING_DIRECTIONALITY / FOUNDATIONAL**. |
| Protocol | PARTIAL | `INT-*` explicitly has `protocol`; `IF-*` does not have a stable protocol field in the current definition. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| Operation/method | NO as a guaranteed IF field | No controlled field for method, RPC method, GraphQL operation, command, or message operation. **INSUFFICIENT_GRANULARITY / FOUNDATIONAL** for complete API catalogs. |
| Address/path/topic | NO as a guaranteed IF field | No controlled address/path/topic identity is specified. **INSUFFICIENT_GRANULARITY / FOUNDATIONAL**. |
| Version | NO / AMBIGUOUS | Revisions exist for STM artifacts, but API contract/version identity is not separately defined. **AMBIGUOUS_CONTRACT / IMPORTANT**. |
| Authentication | PARTIAL | `AUTH-*`, `CFG-*`, `PROTECTED_BY`, and Technical Documentation auth projection exist, but IF-to-auth qualifier and observed mechanism granularity are not specified. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| Request/response contracts | PARTIAL | `ERR-*` covers error behavior and observed views include `DECLARED`, `IMPLEMENTED`, `CONSUMED`, `TESTED`; a request/response schema field is not defined. **INSUFFICIENT_GRANULARITY / FOUNDATIONAL**. |
| Errors | YES at boundary level | `ERR-*` explicitly represents HTTP/error representation, retry mapping, fallback, and partial result; exact error linkage to an individual operation is not defined. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| Exact source/provenance | YES | Every STM artifact retains supporting `WS-*`/`EV-*` references, with baseline binding. **CURRENT**. |
| Project/revision/baseline qualification | YES | STM identity/revision/baseline and Stage E qualified Project/Product bindings support it. **CURRENT**. |
| Multiple consumers | PARTIAL | Relations are many-to-many in principle, but no explicit cardinality/consumer-binding contract for one IF is stated. **MISSING_DIRECTIONALITY / IMPORTANT**. |
| Provider declaration vs consumer expectation | NO | Observed views preserve `DECLARED`, `IMPLEMENTED`, `CONSUMED`, `TESTED`, but do not define provider declaration and consumer expectation as separately matchable roles. **MISSING_VALIDATION / FOUNDATIONAL**. |
| Compatibility representation | NO / DESIGN DECISION | Contract Verification can compare declared/implemented/consumed/tested views, but an API provider/consumer compatibility object or adjudication boundary is not defined. **MISSING_VALIDATION / FOUNDATIONAL**. |

Conclusion: IF-* is a suitable identity family, but it is not yet a complete
operation-level API contract model. The existing model can produce bounded
provided/consumed surface inventories; it cannot guarantee complete method,
address, schema, version, consumer-expectation, or compatibility catalogs.

### 5. Provided vs consumed interfaces

The current model can express the high-level distinction:

```text
COMP-A --PROVIDES--> IF-X(direction=PROVIDED)
COMP-B --CONSUMES/CALLS--> IF-X or IF-Y(direction=CONSUMED)
```

It can therefore generate separate lists when accepted facts have been entered
with the appropriate `direction` property. The Technical Documentation package
already registers separate provided and consumed interface projections.

It cannot yet prove that the consumer-side `IF-*` is the same interface as the
provider-side `IF-*`, nor can it preserve a complete pair of exact provider and
consumer revisions plus consumer expectation and provider declaration as
independent, matchable records. A consumer may be represented as an
`IF-* direction=CONSUMED`, an `INT-*`, or a `CONSUMES` relation, but the current
contract does not define which representation is authoritative for an operation
identity.

Therefore:

- “all APIs this service exposes” is **PARTIALLY GENERATABLE** from
  `IF-* direction=PROVIDED`, subject to accepted coverage and whatever detail
  was captured;
- “all APIs this service calls” is **PARTIALLY GENERATABLE** from
  `IF-* direction=CONSUMED`, `INT-*`, and `CALLS`, subject to the same limits;
- reliable provider/consumer matching is **NOT GENERATABLE** as a complete
  compatibility result without a Stage F design decision.

### 6. INT-* and FLOW-* integration capability

`INT-*` represents a material relationship between producer/caller and
consumer/provider. Its typical properties are `source`, `target`, `interface`,
`protocol`, `sync_or_async`, `timeout`, `retry`, correlation identity, and
material failure behavior (`docs/superpowers/specs/2026-09-04-shared-technical-
model-foundation-design.md`, §6.3). It is the natural factual owner for a
concrete call or integration edge, while `IF-*` owns the interaction surface.

`INT-*` can therefore identify source, target, direction by its endpoints and
relations, protocol, and synchronous/asynchronous behavior. Data movement and
external-system identity are only partial: they can be represented through
target components, stores, events, flows, and relations, but the current
contract does not define a complete payload/data-class or external-provider
identity shape.

`FLOW-*` represents significant business/system/control flows rather than every
internal call chain. It explicitly covers startup, reads, writes, scheduled
work, external integrations, persistence, failure/recovery, shutdown, and
security-sensitive operations (§6.6). It can summarize request/response,
event, and data flows, but the contract does not require it to preserve exact
interface references for every flow. Thus it is a projection/useful synthesis
surface, not a replacement for operation-level `IF-*` or call-level `INT-*`.

`IF-* + INT-* + FLOW-*` are sufficient for a high-level Service Integration
Catalog. They are insufficient for a complete operation/entity-level catalog
unless the existing families receive minimal qualifiers. No new identity family
is indicated by this finding.

### 7. EVENT-* capability

`EVENT-*` explicitly represents material events/messages and, where applicable,
`name/topic`, producer, consumer, payload/schema, delivery assumptions,
ordering, retry, dead-letter queue, and idempotency
(`docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`,
§6.5). The controlled relations `PUBLISHES` and `SUBSCRIBES` identify producer
and consumer roles.

This is enough to represent “produces” and “consumes” event catalogs when the
event facts are accepted and evidence-backed. It is not enough to assert that
every Kafka/RabbitMQ/NATS binding found in configuration is an event fact: the
source must show a material producer/consumer behavior or an explicitly bounded
declared view.

Transport/broker is not a separate required family. It can remain an
`INT-*`/`COMP-*`/`DS-*`-related fact or an event property depending on what the
evidence actually establishes. The current contract does not resolve the exact
relationship between an event interface and `IF-*`; this is a Stage F Design
decision, not a reason to add an `API-*` or `MESSAGE-*` authority.

### 8. DS-* capability

`DS-*` represents material persistence/storage. The current supported examples
are PostgreSQL, SQLite, Redis, object storage, filesystem, Elasticsearch, and
domain-specific durable stores. Ownership, read/write participation,
migration, and consistency behavior are intended as properties or relations,
not as separate schema-object taxonomies
(`docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`,
§6.4).

#### Granularity classification

| Resource | Current classification | Finding |
|---|---|---|
| Database instance / database | PARTIALLY_SUPPORTED | Store-level `DS-*` can represent it. Instance/database identity fields are not specified. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| Schema | PARTIALLY_SUPPORTED | Can be a DS property or relation target, but no schema identity contract exists. **INSUFFICIENT_GRANULARITY / FOUNDATIONAL** for ownership maps. |
| Table / view / materialized view | NOT_SUPPORTED as controlled entity identity | Store-level DS does not guarantee entity-level addresses. **INSUFFICIENT_GRANULARITY / FOUNDATIONAL**. |
| Index / sequence | NOT_SUPPORTED | No entity kind or access relationship is defined. **NICE_TO_HAVE** unless architecture scope requires it. |
| Stored procedure / function / trigger | NOT_SUPPORTED as distinct target | Could be an interface/interaction or DS property, but separate identity and invocation semantics are absent. **IMPORTANT**. |
| MongoDB collection/document store | PARTIALLY_SUPPORTED | Domain-specific durable store can cover the store; collection/document granularity is not defined. **IMPORTANT**. |
| Redis namespace/key pattern | PARTIALLY_SUPPORTED | Redis store is explicit; namespace/key-pattern identity is absent. **IMPORTANT**. |
| Object-storage bucket/prefix | PARTIALLY_SUPPORTED | Object storage is explicit; bucket/prefix identity is absent. **IMPORTANT**. |
| Search index | PARTIALLY_SUPPORTED | Elasticsearch is explicit; index identity is absent. **IMPORTANT**. |
| Vector-store collection/index | AMBIGUOUS | “Domain-specific durable store” may fit, but vector stores are not explicit and collection/index fields are absent. **AMBIGUOUS_CONTRACT / IMPORTANT**. |
| Cache | PARTIALLY_SUPPORTED | Redis or domain-specific store can represent it, but cache role is not a defined qualifier. **AMBIGUOUS_CONTRACT / NICE_TO_HAVE**. |

The current model can say “billing-service uses PostgreSQL” but cannot
reliably say “billing-service reads/writes `billing.invoices`” as a distinct
entity-level fact with ownership and access mode. This is the central Stage F
granularity gap.

### 9. SQL and database entity interactions

The current STM has material `READS_FROM`, `WRITES_TO`, `OWNS_STATE`,
`PARTICIPATES_IN`, and `DEPENDS_ON` relations, and the DS contract mentions
read/write participation and migration/consistency behavior. It does not define
an SQL operation taxonomy or a target-entity identity.

| Interaction | Current result | Discovery gap |
|---|---|---|
| SELECT from table/view | PARTIAL | `READS_FROM` can express store usage; exact table/view and SELECT operation are not guaranteed. **INSUFFICIENT_GRANULARITY / FOUNDATIONAL**. |
| INSERT / UPDATE / DELETE | PARTIAL | `WRITES_TO` can express mutation broadly; operation-specific evidence is not retained by contract. **MISSING_ACCESS_MODE / IMPORTANT**. |
| UPSERT/MERGE | NO as a controlled mode | No operation/access-mode vocabulary. **MISSING_ACCESS_MODE / IMPORTANT**. |
| DDL | NO | No schema-operation mode. **MISSING_ACCESS_MODE / IMPORTANT**. |
| Migration ownership | PARTIAL | DS design names migration behavior, but migration file-to-entity and owner authority are not defined. **MISSING_OWNERSHIP / FOUNDATIONAL**. |
| EXECUTE procedure/function | NO as a distinct mode | No executable database-object target or operation mode. **INSUFFICIENT_GRANULARITY / IMPORTANT**. |
| Transactional access | PARTIAL | `sync_or_async`, consistency, and flow concepts exist; transaction scope/isolation is not defined. **INSUFFICIENT_GRANULARITY / NICE_TO_HAVE**. |
| Raw SQL | PARTIAL evidence source | Raw SQL can be inspected as repository evidence, but acceptance rules for unresolved/dynamic targets are not defined. **MISSING_VALIDATION / IMPORTANT**. |
| ORM-generated access | PARTIAL evidence source | ORM models/configuration can support a fact, but the model does not state how inferred SQL targets are bounded. **MISSING_VALIDATION / IMPORTANT**. |
| Repository/data-access layer | YES as component/interaction context | `COMP-*`, `INT-*`, and `FLOW-*` can preserve the layer; it does not prove the underlying entity target by itself. **CURRENT with evidence limitation**. |
| Dynamic SQL | NO safe precision rule | No explicit unresolved-target representation is defined. **MISSING_VALIDATION / FOUNDATIONAL**. |

The current model therefore needs an extension or explicit design decision for
entity granularity and access mode. Discovery does not select whether access
mode belongs on `DS-*`, `INT-*`, `FLOW-*`, relation metadata, or dependency
metadata; it only establishes that direct dependency metadata is the wrong
authority for observed access facts because dependency metadata governs impact
traversal (`references/technical-model-dependencies.md`, §§1–4).

### 10. Data ownership and access mode

The model can distinguish ownership from usage at a conceptual level:

```text
COMP-A --OWNS_STATE--> DS/entity-X
COMP-B --READS_FROM--> DS/entity-X
COMP-C --WRITES_TO--> DS/entity-X
```

`OWNS_STATE` is an existing relation, and Stage E explicitly preserves the
invariant `membership != ownership != usage != dependency` and `relation !=
dependency`. However, the current contracts do not make ownership of a schema,
table, collection, bucket/prefix, or index an explicitly addressable fact. They
also do not define an access-mode vocabulary such as `READ`, `WRITE`,
`READ_WRITE`, `DDL`, `MIGRATION_OWNER`, or `EXECUTE`.

Consequently, “Service A writes directly into data owned by Service B” can be
represented only at a broad relation level if both sides are already modeled;
it cannot be reliably generated as an entity-specific architectural signal.
The access fact must remain STM/evidence. Architecture Review must decide
whether it is a defect, preserving the rule that an observed fact is not itself
an `RF-*` finding.

### 11. Migration/schema ownership

The current DS definition acknowledges migration and consistency behavior, and
`CFG-*` can represent behaviorally relevant configuration. The current evidence
model can point to migration files with `WS-*`/`EV-*`. What is missing is a
normative, revisioned representation that connects:

- migration owner Project/service;
- migration file or declared schema source;
- affected schema/entity;
- observed current schema;
- runtime access;
- multiple Projects modifying the same entity; and
- schema evolution authority versus runtime usage.

Therefore the current model cannot answer reliably who is responsible for
evolving `billing.invoices`, even though it can preserve evidence that a
migration file exists and a service uses a database. This is **MISSING_OWNERSHIP
and MISSING_PROVENANCE at entity level / FOUNDATIONAL**.

### 12. Non-SQL data stores

The current DS family is intentionally store-oriented and can represent Redis,
object storage, filesystem, Elasticsearch, and domain-specific durable stores.
It does not support a universal live scanner or reverse-engineering precision.
Stage F should accept only the finest address supported by evidence:

| Store | Evidence-backed realistic precision today | Current result |
|---|---|---|
| Redis | Redis instance/store; namespace or key pattern only when directly declared or strongly evidenced | PARTIAL |
| MongoDB | Store/database; collection only when directly evidenced | PARTIAL |
| Elasticsearch/OpenSearch | Store; index only when directly evidenced | PARTIAL |
| S3/object storage | Store; bucket/prefix/object operation only when evidenced | PARTIAL |
| Vector database | Domain-specific store only; collection/index requires explicit extension or bounded representation | AMBIGUOUS |
| Embedded store | SQLite/domain-specific durable store; file/path only when evidenced | PARTIAL |
| Filesystem-backed state | Filesystem store; path/root/pattern only when evidenced and safely redacted | PARTIAL |
| Queue/stream as data infrastructure | Event/interaction/store combination may be appropriate; current contract does not settle the combination | AMBIGUOUS |

### 13. External integrations

An internal service, Product member service, corporate service, third-party
SaaS/API, identity provider, payment gateway, cloud API, and external database
can be represented as a `COMP-*`, `INT-*`, `IF-*`, `EVENT-*`, or `DS-*` with
external/source qualification when evidence supports it. The current Product
contract explicitly allows external source bindings and preserves their exact
locator/revision or limitation (`references/shared-evidence-model.md`, §6;
`references/product-multi-project-review.md`, §§5 and 8).

The current model can therefore project an external integration at a bounded
identity level. It cannot guarantee a complete inventory of provider, base URL,
operation/path, protocol, auth mechanism, version, and consumer because IF/INT
structured properties for those dimensions are not fully defined. Configuration
URLs and installed SDK dependencies are evidence sources or hints, not proof
of use.

Examples such as Stripe `POST /v1/payment_intents`, Keycloak token endpoint,
and S3 `PutObject`/`GetObject` are generatable only when direct declarations or
strong implementation evidence identify the operation. The catalog must not
promote a configured base URL, a dependency declaration, or a secret-bearing
environment value into a called API fact.

### 14. Evidence acquisition sources

The existing evidence model supports addressable repository observations:
source type, repository/path or external locator, symbol/range where available,
baseline binding, and observed fact (`references/shared-evidence-model.md`, §3).
The following source classes are appropriate under that contract:

| Source | Evidence strength for a factual interaction |
|---|---|
| HTTP/router declaration | DIRECT_DECLARATION for provided surface; implementation linkage still needs evidence. |
| OpenAPI/Swagger | DIRECT_DECLARATION for declared contract; not proof of runtime consumption. |
| Protobuf/RPC definition | DIRECT_DECLARATION for declared RPC surface. |
| GraphQL schema/resolver | DIRECT_DECLARATION for declared schema; operation use needs separate evidence. |
| Client SDK call / HTTP wrapper | STRONG_INFERENCE of consumption when a concrete call path and target are shown. |
| Service-discovery/config URL | WEAK_HINT unless linked to a concrete call path. |
| Message producer/consumer registration | STRONG_INFERENCE or DIRECT_DECLARATION depending on binding and execution evidence. |
| Kafka/RabbitMQ/NATS binding | DIRECT_DECLARATION of configured binding; not by itself proof of runtime publication/consumption. |
| ORM model/query/repository | STRONG_INFERENCE; exact entity/access mode requires query/schema evidence. |
| SQL migration/raw SQL | DIRECT_DECLARATION for declared schema/query target when statically resolvable. |
| Database configuration | WEAK_HINT of possible store use; not proof of entity access. |
| Redis/S3/search client call | STRONG_INFERENCE when concrete resource operation and target are visible. |
| Terraform/Helm/Kubernetes wiring | DIRECT_DECLARATION of provisioned/configured resource; not proof of application use. |
| Generated client | STRONG_INFERENCE only with generated method call/use evidence; generated artifact alone is insufficient. |
| Test fixture/contract test | DIRECT_DECLARATION of tested expectation; not proof of production behavior. |

The current evidence contract already prevents the two unsafe promotions:

```text
config value exists -> API definitely called       (forbidden inference)
dependency installed -> service definitely used    (forbidden inference)
```

What is missing is a Stage F acceptance rule that records the confidence class,
unresolved target, and observed view on the accepted STM fact without
fabricating precision.

### 15. Ambiguity / dynamic interactions

The current STM can preserve `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and
`TESTED` observed views, and it can expose `PARTIAL`, `UNKNOWN`, stale, and
unresolved limitations in Technical Documentation. That provides a useful
uncertainty boundary, but no explicit representation currently says:

- interface exists but exact operation is unresolved;
- database is used but entity-level target is unknown;
- URL is runtime-resolved through service discovery;
- SQL table name is dynamic;
- gateway/proxy forwards to an unresolved provider; or
- ORM/runtime reflection hides the concrete target.

The gap is **MISSING_VALIDATION / FOUNDATIONAL**. Stage F needs a bounded
unresolved/precision state or equivalent accepted property. It must preserve the
fact at the highest supported granularity, link the evidence and limitation,
and prevent a projection from printing a guessed path/table/topic as fact.

### 16. Current Technical Documentation outputs

Current Technical Documentation already registers these projections:

| Requested output | Current classification |
|---|---|
| Service API Reference | PARTIALLY_SUPPORTED; provided-interface projection exists, but no complete operation/schema contract. |
| Service Consumed API Catalog | PARTIALLY_SUPPORTED; consumed-interface projection exists, but consumer expectation and exact call identity are incomplete. |
| Service Integration Dependencies | PARTIALLY_SUPPORTED; `PRJ-TECH-DOC-04-INTEGRATIONS` projects `INT-*`/`EVENT-*`, but does not define a complete dependency catalog or entity access. |
| Service Event Catalog | PARTIALLY_SUPPORTED; event facts can be projected, but the current package has no dedicated event document and event/interface relation is unresolved. |
| Service Data Access Catalog | PARTIALLY_SUPPORTED; `05-data-and-persistence.md` exists, but DS is store-level and access-mode/entity granularity is missing. |
| External Integrations | PARTIALLY_SUPPORTED through integrations/data/persistence projections; no dedicated standardized external catalog. |
| Product API Catalog | PARTIALLY_SUPPORTED conceptually through Product Technical Documentation and qualified STM selectors; no dedicated standard catalog. |
| Product Integration Map | PARTIALLY_SUPPORTED conceptually through Product Technical Documentation and cross-project relations; no dedicated standard projection contract. |
| Product Data Interaction Map | PARTIALLY_SUPPORTED conceptually; entity/access/ownership semantics are not sufficient. |

The contract distinguishes semantic data from user-facing documents: a
projection exists only when its registered dependency selectors, accepted STM
coverage, lifecycle, verification, and package policy are satisfied
(`references/technical-documentation.md`; `references/projection-lifecycle.md`).

### 17. Per-Service user documentation gap

| Section | Current status | Reason |
|---|---|---|
| Interfaces provided | PARTIALLY_GENERATABLE | `IF-* direction=PROVIDED` projection exists; operation/path/schema/version completeness is not guaranteed. |
| Interfaces consumed | PARTIALLY_GENERATABLE | `IF-* direction=CONSUMED` exists; exact consumer call and expectation matching are incomplete. |
| External integrations | PARTIALLY_GENERATABLE | `INT-*`/`COMP-*`/`DS-*` can carry bounded external facts; no complete external identity qualifier. |
| Events produced | CURRENTLY_GENERATABLE at event level | `EVENT-*` plus `PUBLISHES`; transport/schema precision depends on accepted facts. |
| Events consumed | CURRENTLY_GENERATABLE at event level | `EVENT-*` plus `SUBSCRIBES`; same evidence limitation. |
| Datastores used | CURRENTLY_GENERATABLE at store level | `DS-*` is explicitly a store family. |
| Data entities read | NOT GENERATABLE reliably | No entity-level DS identity or read access mode. |
| Data entities written | NOT GENERATABLE reliably | No entity-level DS identity or write access mode. |
| Schema / migration ownership | PARTIALLY_GENERATABLE | Migration behavior and evidence can be shown; ownership-to-entity contract is missing. |
| Other infrastructure interactions | PARTIALLY_GENERATABLE | Components, interactions, events, flows, and config cover broad facts; queue/cache/vector roles are ambiguous. |
| Dependencies | CURRENTLY_GENERATABLE at typed-edge level | Direct dependency metadata, reverse indexes, and relation/dependency distinction exist. |
| Evidence / provenance | CURRENTLY_GENERATABLE | WS/EV source and baseline references are part of the authority model; projection must link rather than copy secrets. |

The minimum standard package should therefore be treated as a Stage F
projection design target, not as evidence that all sections are currently
complete.

### 18. Product-level documentation gap

Stage E provides the necessary Product context: optional Product, exact Product
revision, immutable baseline vector, qualified Project references, external
source bindings, independent availability dimensions, and reuse of Project-local
STM. Product technical documentation is already described as a projection over
selected Product STM/evidence inputs (`references/product-multi-project-review.md`,
§10; `references/technical-documentation.md`, Product scope section).

The current model can conceptually generate a Product Interface Catalog,
Integration Map, Data Access Map, Provider/Consumer Matrix, and External
Integrations Catalog without a new factual Product authority. However, the
qualified cross-project facts still lack the Stage F operation/entity/access
qualifiers. Product baseline qualification is sufficient for source identity
and revision, but not sufficient for the missing semantic dimensions.

The safe composition remains:

```text
qualified WS/EV evidence
  -> Project-local or STM-gated cross-project fact/relation
  -> dependency/compatibility semantics where applicable
  -> Product projection/package
```

### 19. Provider/consumer compatibility

The current model can preserve distinct observed views and can expose the
provider and consumer as separate components and interfaces. It cannot safely
adjudicate this example as a compatibility result:

```text
consumer expects: GET /api/v1/customer/{id}
provider exposes: GET /api/v1/customers/{id}
```

The mismatch is visible only if method/path are first-class captured properties;
they are not currently guaranteed. Matching dimensions that require an explicit
Stage F decision are protocol, method/operation, path/topic, version, schema,
provider revision, and consumer revision.

The existing Contract Verification boundary is a useful consumer for
`DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED` views, but Stage F must
decide whether provider/consumer compatibility is represented as a bounded
STM relation/property, a capability-owned adjudication, or only a projection
comparison. Discovery does not create a matcher or compatibility authority.

### 20. Data-access architectural signals

Once entity-level data facts exist, the following can be derived without making
the catalog an Architecture Review finding authority:

| Observed STM fact | Possible Architecture Review interpretation |
|---|---|
| Multiple services write one table | Shared-state coupling or intentional coordination; review decides. |
| Service A writes entity owned by Service B | Ownership boundary violation candidate; not automatically `RF-*`. |
| Cross-Project shared database | Product integration/shared-state fact; review decides whether it is acceptable. |
| Read-only reporting access | Lower mutation coupling fact; not automatically safe. |
| Migration ownership conflict | Conflicting schema authority fact; review adjudicates consequence. |
| Runtime service has DDL rights | Capability/configuration fact; review assesses risk and boundary. |
| External database dependency | External integration/data dependency fact; review assesses resilience/trust. |
| Hidden coupling through a shared store | Fact requires evidence of shared entity and access; review determines architectural consequence. |

### 21. Security / secret-redaction boundary

The current contracts recognize secrets, credentials, configuration, trust, and
security-sensitive flows as review material, but they do not define an explicit
catalog redaction contract for credentials, tokens, connection strings,
passwords, secret query parameters, database usernames, API keys, or private
hostnames. `EV-*` requires source and observed fact, not unrestricted source
copying; final report guidance also discourages leaking sensitive material, but
there is no Stage F-specific deterministic rule.

This is **SECURITY_GUARD_MISSING / FOUNDATIONAL**. Stage F must require useful
technical identifiers and evidence pointers while prohibiting secret values and
full sensitive environment/configuration values from catalog prose or copied
evidence excerpts. The Discovery artifact contains no secret values.

### 22. Practical capability matrix

Representative shape: one service provides REST, consumes REST, calls an
external API, publishes and consumes events, uses PostgreSQL with table read and
write, owns migrations, uses Redis, and uses object storage.

| Fact | Current STM family | Exact current representation | Sufficient? | Gap | Likely projection |
|---|---|---|---|---|---|
| REST API provided | `IF-*`, `COMP-*`, `PROVIDES` | IF direction `PROVIDED`; HTTP kind; provider relation | Partial | Method/path/schema/version not guaranteed | Provided interfaces |
| REST API consumed | `IF-*`, `INT-*`, `CONSUMES`, `CALLS` | IF direction `CONSUMED`; interaction to provider | Partial | Consumer expectation and exact operation identity | Consumed interfaces / integrations |
| External API | `COMP-*`, `IF-*`, `INT-*`, `AUTH-*`, `CFG-*` | External component/target plus interaction if evidenced | Partial | External identity, operation, auth/version qualifiers | Integrations / external catalog |
| Event producer | `EVENT-*`, `PUBLISHES`, `INT-*` | Event name/topic, producer, payload/transport where captured | Yes at event level | Event/IF relationship and full delivery contract | Integrations / event catalog |
| Event consumer | `EVENT-*`, `SUBSCRIBES`, `INT-*` | Event name/topic, consumer, payload/transport where captured | Yes at event level | Same | Integrations / event catalog |
| PostgreSQL store | `DS-*` | PostgreSQL store fact | Yes at store level | Database/schema/entity identity | Data and persistence |
| Table READ | `DS-*`, `READS_FROM`, `INT-*` | Broad read relation to DS | No for entity catalog | Entity identity and `READ` mode | Data access catalog |
| Table WRITE | `DS-*`, `WRITES_TO`, `INT-*` | Broad write relation to DS | No for entity catalog | Entity identity and `WRITE` mode | Data access catalog |
| Migration ownership | `DS-*`, `COMP-*`, `CFG-*`, evidence | Migration evidence and possible ownership relation | Partial | Migration authority and affected entity binding | Data/migration section |
| Redis usage | `DS-*`, `INT-*`, `CFG-*` | Redis store fact and client interaction | Yes at store level | Namespace/key pattern and role | Data and persistence |
| Object storage usage | `DS-*`, `INT-*`, `CFG-*` | Object-store fact and interaction | Yes at store level | Bucket/prefix/object operation | Data and persistence / external |

### 23. Gap inventory

| ID | Classification | Severity | Gap |
|---|---|---|---|
| F-01 | INSUFFICIENT_GRANULARITY | FOUNDATIONAL | IF-* lacks guaranteed operation/method/address/path/topic identity. |
| F-02 | MISSING_DIRECTIONALITY | FOUNDATIONAL | Provider, consumer, and consumer binding are not a complete first-class pair. |
| F-03 | MISSING_VALIDATION | FOUNDATIONAL | Provider declaration versus consumer expectation and compatibility result are not represented. |
| F-04 | INSUFFICIENT_GRANULARITY | FOUNDATIONAL | DS-* is store-level; table/schema/collection/bucket/index/function targets are not controlled identities. |
| F-05 | MISSING_ACCESS_MODE | FOUNDATIONAL | No controlled read/write/DDL/migration-owner/execute access modes. |
| F-06 | MISSING_OWNERSHIP | FOUNDATIONAL | Entity ownership and migration ownership cannot be bound precisely to Project/service. |
| F-07 | MISSING_VALIDATION | FOUNDATIONAL | Dynamic/unresolved interfaces and data targets lack an explicit bounded precision state. |
| F-08 | SECURITY_GUARD_MISSING | FOUNDATIONAL | No explicit Stage F secret-redaction contract for catalog and evidence excerpts. |
| F-09 | AMBIGUOUS_CONTRACT | IMPORTANT | REST, GraphQL, RPC method, webhook, CLI, and event/interface relationship semantics are not complete. |
| F-10 | INSUFFICIENT_GRANULARITY | IMPORTANT | Request/response schema, version, auth linkage, and operation-specific errors are incomplete. |
| F-11 | INSUFFICIENT_GRANULARITY | IMPORTANT | Non-SQL resource precision is limited to store-level unless evidence supports a bounded entity property. |
| F-12 | MISSING_PROVENANCE | IMPORTANT | Migration file/current schema/entity and external operation evidence cannot be represented as a complete linked tuple. |
| F-13 | MISSING_USER_PROJECTION | IMPORTANT | Dedicated Service Event, Service Data Access, External Integration, and Product map packages are not standardized as separate documents. |
| F-14 | MISSING_VALIDATION | IMPORTANT | Evidence-strength/acceptance rules for config, generated clients, ORM, bindings, and runtime resolution are not explicit in STM. |
| F-15 | MISSING_DIRECTIONALITY | IMPORTANT | Event broker/transport and data movement direction are not consistently qualified across IF/INT/EVENT/FLOW. |
| F-16 | INSUFFICIENT_GRANULARITY | NICE_TO_HAVE | Index, sequence, trigger, transaction isolation, cache role, and CLI option precision are not currently needed for the minimum catalog. |
| F-17 | MISSING_USER_PROJECTION | NICE_TO_HAVE | No standard provider/consumer matrix document is registered. |
| F-18 | AMBIGUOUS_CONTRACT | NICE_TO_HAVE | Queue/stream as event transport versus data infrastructure is not resolved. |

### 24. Architecture options A/B/C

#### Option A — Projection-only

**Advantages:** no STM migration; lowest authority impact; immediately usable
for broad provided/consumed interfaces, integrations, events, and store-level
documentation; preserves single-project and Stage E behavior.

**Disadvantages:** cannot truthfully promise operation-level APIs, exact entity
access, access modes, migration ownership, compatibility, or safe unresolved
precision. It risks catalogs that look complete but silently omit material
semantics.

**Authority impact:** none.
**Migration impact:** none.
**Single-project impact:** safe but limited.
**Stage E impact:** Product projections remain qualified but shallow.
**Projection impact:** extend selectors and package taxonomy only.
**Complexity/risk:** low implementation complexity; high completeness and
false-precision risk.

#### Option B — Extend existing STM contracts

**Advantages:** preserves all current identity families and authority owners;
fits the existing IF/INT/DS/EVENT/FLOW relation model; can add minimal
provider/consumer, operation/address/version, entity/access-mode, ownership,
precision, and provenance qualifiers; keeps catalogs as projections; supports
single-project first and qualified Product reuse.

**Disadvantages:** requires careful backward-compatible semantics and explicit
matching/validation boundaries; DS entity granularity may be complex if
over-generalized; existing projections and selectors need bounded extension.

**Authority impact:** extends STM only; no new API/Data authority.
**Migration impact:** additive records/defaults if old store/interface facts
remain valid at their prior granularity.
**Single-project impact:** improves local catalogs without requiring Product.
**Stage E impact:** qualified cross-project relations gain usable detail without
changing Product ownership.
**Projection impact:** standard Service/Product catalog projections and package
selectors can be added over accepted STM fields.
**Complexity/risk:** medium; principal risk is semantic overreach and precision
that exceeds evidence.

#### Option C — New semantic family

**Advantages:** could give a purpose-built integration catalog an apparently
clean schema.

**Disadvantages:** duplicates IF/INT/DS/EVENT/relational authority; creates
cross-family synchronization and provenance problems; risks turning a catalog
into a second factual model; complicates Product qualification, lifecycle,
dependency routing, and migration; violates the current “promote a new family
only when repeated use proves existing properties cannot represent the concept”
principle.

**Authority impact:** high and potentially conflicting.
**Migration impact:** historical rewrite or dual authority risk.
**Single-project impact:** adds unnecessary identity burden.
**Stage E impact:** requires a new qualified Product factual path.
**Projection impact:** parallel selectors/package dependencies.
**Complexity/risk:** high; not justified by current evidence.

### 25. Recommended direction

Recommend **Option B — Extend existing STM contracts**, with a projection
package layered over the accepted STM. This is a Discovery recommendation, not
a Design decision.

The minimum semantic direction should remain within `IF-*`, `INT-*`, `DS-*`,
`EVENT-*`, `FLOW-*`, and existing relations. It should add only the qualifiers
needed to preserve:

1. provider/consumer role and expectation/declaration distinction;
2. protocol and operation/address/version identity where evidence supports it;
3. request/response/schema/error linkage;
4. store entity granularity with bounded precision;
5. access mode and ownership/migration authority;
6. unresolved/dynamic target state;
7. exact evidence/provenance and redaction metadata.

The final Design must decide the exact field placement and compatibility
boundary. Discovery does not choose those fields or add a new family.

### 26. Stage F scope

Stage F should define the minimum semantic and projection contract for:

- provided and consumed interface inventories;
- provider/consumer expectations and safe comparison inputs;
- internal and external integrations;
- produced and consumed events;
- store and entity-level data interactions where evidenced;
- access mode, ownership, and migration authority;
- non-SQL resource addressing at evidence-supported precision;
- unresolved/dynamic interaction representation;
- evidence/provenance and secret redaction;
- standard per-Service and Product-facing documentation packages.

### 27. Explicit non-goals

Stage F should not become a database reverse-engineering engine, live database
scanner, runtime traffic capture system, distributed tracing platform, API
gateway, service mesh, schema-registry replacement, OpenAPI generator
implementation, full SQL parser framework, ORM-specific framework, generic
CMDB, graph database, RAG system, or runtime service. The system should reason
over repository and explicitly bounded external evidence, not provide runtime
observability.

### 28. Migration classification

Expected migration class: **COMPATIBLE_EXTENSION**, with an additive path
preferred for existing broad `IF-*`, `DS-*`, `INT-*`, `EVENT-*`, and `FLOW-*`
facts. Existing store/interface facts must remain valid at their prior
granularity; enrichment should not require rewriting historical evidence or
silently upgrading a broad fact into an exact entity fact.

If Design proves that old facts cannot retain meaning after adding direction,
ownership, or entity qualifiers, the affected slice must be explicitly
versioned and revalidated. Discovery does not find evidence requiring a
foundational redesign or historical rewrite.

### 29. Decisions required in Design

#### Resolved by existing contract

- STM remains the factual authority; catalogs remain projections.
- `WS-*`/`EV-*` provide baseline-bound evidence and provenance.
- Existing identity families are `COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EVENT-*`,
  `FLOW-*`, `AUTH-*`, `CFG-*`, and `ERR-*`.
- `PROVIDES`, `CONSUMES`, `CALLS`, `PUBLISHES`, `SUBSCRIBES`, `READS_FROM`,
  `WRITES_TO`, and `OWNS_STATE` are controlled relation vocabulary.
- Relation, dependency, reverse index, impact result, projection, and package
  remain distinct.
- Product is optional, qualified, baseline-bound, and not a second factual
  owner.
- Projection lifecycle, selectors, dependencies, and package gates are reused.
- `PARTIAL`, `UNKNOWN`, stale, disputed, and unresolved states must remain
  visible rather than be turned into certainty.

#### Requires Stage F Design decision

- IF provider/consumer semantics and whether consumed IFs are expectations,
  observed calls, or both.
- Exact operation/address/path/topic/version representation and supported
  protocol kinds, including GraphQL.
- Request/response/schema/error linkage and auth qualifier placement.
- DS entity granularity and bounded precision for relational and non-SQL stores.
- Access mode representation and whether it belongs on a relation, `INT-*`,
  `FLOW-*`, or DS interaction property.
- Ownership versus usage representation for entities and migration authority.
- SQL object/function/procedure and schema evolution representation.
- Event/interface/broker relationship and queue/stream classification.
- External provider identity and safe base URL/operation representation.
- Evidence-strength and acceptance rules for direct declarations, strong
  inference, and weak hints.
- Dynamic/unresolved interaction representation and projection wording.
- Provider/consumer matching dimensions and compatibility adjudication owner.
- Standard Service and Product documentation package membership and selectors.
- Secret-redaction and sensitive-identifier policy.

### 30. Open questions

The following **9 foundational open questions** remain for Design:

1. What is the smallest provider/consumer/expectation/declaration record that
   preserves both sides without making a consumer guess a provider identity?
2. Which operation/address fields are common enough for IF-* and which remain
   protocol-specific structured properties?
3. Is entity-level DS identity a property of `DS-*`, a relation target, or a
   bounded nested address while preserving DS store identity?
4. Where does access mode live without turning factual relations into impact
   dependencies?
5. How is migration authority linked to exact schema entities and Project
   revisions?
6. What accepted precision states distinguish exact, store-level, unresolved,
   and evidence-limited facts?
7. What is the compatibility adjudication owner and how does it avoid becoming
   a new compatibility authority?
8. Which external identifiers may be shown while preventing secret and private
   infrastructure disclosure?
9. Which Service/Product documents become standard package members versus
   optional projections?

### 31. Discovery verdict

The current model is **PARTIAL**, not sufficient for the complete Stage F
mission. It already has the correct authority architecture and enough
high-level semantics to document broad interfaces, integrations, events, and
stores. It does not yet preserve the operation/entity/access/ownership/
compatibility precision required for complete user-facing API and data catalogs.

The evidence does not justify a new API, SQL, DB, or Product Integration
identity family. The minimum likely change is a compatible extension of existing
STM families plus standardized projections, bounded ambiguity representation,
and an explicit redaction guard.

```text
current_model_sufficient: PARTIAL
IF_extension_needed: YES
DS_extension_needed: YES
INT_FLOW_extension_needed: DESIGN_DECISION
new_identity_family_required: NO
standard Service Interface/API document missing: YES
standard Service Data Access document missing: YES
Product Interface/Integration projection missing: YES
data ownership/access-mode gap: YES
SQL entity granularity gap: YES
external integration gap: YES
secret-redaction guard gap: YES
recommended architecture option: B
migration: COMPATIBLE_EXTENSION
```

#### Required success-criteria result

| Criterion | Result |
|---|---|
| Current model sufficient | PARTIAL |
| IF-* extension needed | YES |
| DS-* extension needed | YES |
| INT/FLOW extension needed | DESIGN_DECISION |
| New identity family required | NO |
| Standard Service Interface/API document missing | YES |
| Standard Service Data Access document missing | YES |
| Product Interface/Integration projection missing | YES |
| Data ownership/access-mode gap | YES |
| SQL entity granularity gap | YES |
| External integration gap | YES |
| Secret-redaction guard gap | YES |
| Recommended architecture option | B |
| Migration | COMPATIBLE_EXTENSION |
| Foundational open questions | 9 |
| Important gaps | 7 |
| Nice-to-have gaps | 3 |

**Recommended next step:** `STAGE_F_INDEPENDENT_DISCOVERY_REVIEW`.

**Verdict:** `STAGE_F_DISCOVERY_COMPLETE` / `STAGE_F_DISCOVERY_FINDINGS`.
