# Stage F — Interface, API & Data Integration Catalog
## Independent Discovery Review

### Review metadata

| Field | Value |
|---|---|
| Repository | `/home/tod/skills/architecture-code-review` |
| Branch | `main` |
| Canonical baseline | `7cace524785aa70bbe2d47797e44134bc878bb06` |
| Discovery artifact | `docs/superpowers/specs/2026-09-07-stage-f-interface-api-data-integration-discovery.md` |
| Review type | Independent Discovery Review only |
| Review date | 2026-09-08 |
| Review writer | Independent review pass |

The repository gate passed. Local `HEAD` and `origin/main` both equal the
canonical baseline. Tracked state is clean. The four named pre-existing
untracked files are present and were preserved; the Stage F Discovery artifact
is present and was not modified.

### Scope

This review verifies whether the Stage F Discovery accurately describes the
current semantic model, its projection contracts, evidence/provenance
boundaries, Product compatibility, and remaining Design decisions. It does not
remediate Discovery, change contracts, or design fields.

The review distinguishes:

```text
factual discovery gap  = current contract cannot express or guarantee the fact
design decision        = current facts and boundaries are known, but alternatives remain
```

### Repository evidence reviewed

The review read the complete Discovery artifact and the current contract sources
at the canonical baseline, including:

- `references/shared-evidence-model.md` — `WS-*`/`EV-*`, source/baseline binding,
  observed views, Product-qualified evidence;
- `references/shared-technical-model.md` — STM families, controlled relations,
  identity/revision/provenance, lifecycle, Technical Model Gate, Product
  relations;
- `docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`
  — current family meanings and material properties for `IF-*`, `INT-*`,
  `DS-*`, `EVENT-*`, and `FLOW-*`;
- `references/technical-model-dependencies.md` — direct dependency authority,
  relation/dependency distinction, reverse indexes, impact strengths;
- `references/revalidation-and-freshness.md` — bounded revalidation and
  projection-only boundaries;
- `references/projection-lifecycle.md` and `references/projection-dependencies.md`
  — `PRJ-*`, `RG-*`, selector, dependency, and freshness rules;
- `references/technical-documentation.md` — current Technical Documentation
  sections, selectors, package, and Product-qualified documentation;
- `references/product-multi-project-review.md` — Product identity, baseline
  vector, qualified addressing, availability, outputs, and authority boundary;
- `references/discovery-coverage.md` and `references/report-contract.md` —
  evidence coverage and security-sensitive review boundaries.

### Discovery accuracy

The Discovery accurately concludes that the current model is **PARTIAL** for the
complete Stage F mission. It correctly separates broad surface-level capability
from missing operation/entity/access precision and does not mistake existing
projection names for complete semantics.

Its principal conclusion is supported:

```text
existing STM families + existing authority model
    are sufficient as the semantic home
missing qualifiers and standardized projections
    require a compatible extension
new factual API/Data/Product family
    is not justified
```

The gap inventory is materially accurate. Its `FOUNDATIONAL`, `IMPORTANT`, and
`NICE_TO_HAVE` labels are planning classifications, not Architecture Review
severity assignments.

### IF-* assessment

**Result: PASS**

The current STM explicitly includes `IF-*` as Interface and gives it a
material interaction-surface meaning. The foundation design names HTTP, gRPC,
IPC, CLI/public command, WebSocket, webhook/callback, public library API, and
file/protocol surfaces, with `PROVIDED` and `CONSUMED` direction views
(`docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`,
§6.2). The shared STM contract also preserves stable identity, revision,
baseline, lifecycle, freshness, authority, and `WS-*`/`EV-*` provenance
references (`references/shared-technical-model.md`, §§2–5).

The Discovery correctly identifies that the current contract does not guarantee
the following as operation-level IF semantics: method/operation, path/address/
topic, API version, request/response schema, provider declaration versus
consumer expectation, or compatibility adjudication. It also correctly treats
GraphQL as unlisted/ambiguous rather than silently claiming complete support.

The gap fits an extension of `IF-*` and related existing families. The evidence
does not require a new identity family. Protocol-specific structured properties
and the boundary between interface identity and interaction identity remain
legitimate Design decisions.

### Provided / consumed interface assessment

**Result: PASS**

The current model can support broad separate views because:

- `IF-*` has `direction = PROVIDED | CONSUMED` in the current foundation
  design;
- STM relations include `PROVIDES`, `CONSUMES`, and `CALLS`;
- `INT-*` can connect source, target, and interface;
- Technical Documentation registers separate selectors and projections for
  provided and consumed interfaces:
  `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` and
  `PRJ-TECH-DOC-03-CONSUMED-INTERFACES`.

The Discovery is also correct that this does not yet guarantee a reliable
operation-level answer to both “what does Service X expose?” and “what exact
interfaces does Service X consume?” A broad consumed interface, a concrete
call, and a consumer expectation are not currently defined as a complete,
matchable tuple. The missing semantics primarily span `IF-*` and `INT-*`, with
projection selectors consuming the result. Dependency metadata must remain
separate because its canonical direction is consumer-to-prerequisite and its
purpose is impact traversal, not data-flow authority
(`references/technical-model-dependencies.md`, §§1–4).

### DS-* assessment

**Result: PASS**

`DS-*` currently means a material data store. The current foundation design
explicitly names PostgreSQL, SQLite, Redis, object storage, filesystem,
Elasticsearch, and domain-specific durable stores. It states that ownership,
read/write participation, migration, and consistency are represented through
properties/relations rather than an automatic schema-object taxonomy
(`docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`,
§6.4).

The Discovery correctly classifies store-level support as present but entity
level support as incomplete. The current contract can represent a broad fact
such as:

```text
billing-service uses PostgreSQL
```

It cannot guarantee an exact, separately addressable and access-qualified fact
such as:

```text
billing-service READ_WRITE PostgreSQL billing.invoices
```

The same conclusion applies to schemas, tables, views, materialized views,
procedures, functions, triggers, MongoDB collections, Redis namespaces/key
patterns, object-store buckets/prefixes, search indexes, and vector-store
collections/indexes. The Discovery does not overclaim support for these
entities and correctly keeps evidence-supported precision as a Design concern.

### SQL/data access assessment

**Result: PASS**

The current relation vocabulary includes `READS_FROM`, `WRITES_TO`, and
`OWNS_STATE`, but it does not define operation/access modes equivalent to
`READ`, `WRITE`, `READ_WRITE`, `DDL`, `MIGRATION_OWNER`, or `EXECUTE`. The DS
contract mentions migration and consistency behavior but does not establish an
entity-level SQL object and operation model.

The Discovery correctly identifies gaps for SELECT/INSERT/UPDATE/DELETE,
UPSERT/MERGE, DDL, procedure/function execution, transaction detail, raw SQL,
ORM-generated access, and dynamic SQL. It also correctly leaves ownership of
access-mode semantics undecided among DS interaction properties, INT/FLOW
facts, and relation metadata. That placement is a legitimate Design choice;
the factual absence of the access-mode vocabulary is a Discovery finding.

### Ownership / migration assessment

**Result: PASS**

The current model does preserve an important distinction. `OWNS_STATE` is a
controlled STM relation, while `READS_FROM`, `WRITES_TO`, and `DEPENDS_ON` have
different meanings. Stage E explicitly preserves:

```text
membership != ownership != usage != dependency
relation != dependency
```

However, current contracts do not provide precise entity ownership for a
schema/table/collection/bucket or a separate migration-authority record tied to
the affected entity and Project revision. The Discovery correctly calls this a
partial/missing capability rather than inventing a second ownership model.

It also preserves the interpretation boundary: direct cross-service database
access is first an STM/evidence fact; whether it is an architectural defect is
owned by Architecture Review and may become an `RF-*` only after independent
adjudication.

The migration findings are accurate. Evidence can point to migration files and
schema declarations through `WS-*`/`EV-*`, but current semantics do not provide
the complete tuple of migration owner, source file, affected entity, current
schema, runtime access, and competing Project authorities.

### INT-* / FLOW-* assessment

**Result: PASS**

**INT_FLOW_DECISION: LEGITIMATE_DESIGN_DECISION**

The current contracts establish enough meaning to decide what these families
already own, but not enough to decide their future Stage F qualifiers without
choosing among coherent alternatives. `INT-*` is a material relationship
between caller/provider and consumer, with typical `source`, `target`,
`interface`, `protocol`, sync/async, timeout, retry, correlation, and failure
properties. `FLOW-*` is a material business/system/control flow, not a complete
call graph. These meanings are sufficient for Discovery to identify the
families as the likely owners of integration and flow facts.

They do not settle whether operation-level data movement, access mode, event
transport, or exact interface references belong on INT, FLOW, IF/EVENT, or
controlled relation properties. Deferring that placement is a legitimate Design
decision, not incomplete repository inspection. Discovery did not defer the
factual conclusion that the current model lacks complete entity/access
precision.

### EVENT-* assessment

**Result: PASS**

The current foundation design gives `EVENT-*` an independent Event/Message
meaning and names `name/topic`, producer, consumer, payload/schema, delivery
assumptions, ordering, retry, DLQ, and idempotency where applicable
(`§6.5`). The relation vocabulary includes `PUBLISHES` and `SUBSCRIBES`.

The Discovery correctly treats event identity as owned by `EVENT-*`, not as a
forced subtype of `IF-*`. It also correctly notes that transport/broker
infrastructure is not identical to event semantics and leaves the exact
relationship among EVENT, INT, IF, and DS/COMP infrastructure for Design.
Provenance and Project/revision qualification come from the shared STM/evidence
contracts rather than a separate event authority.

### External integration assessment

**Result: PASS**

Current Product and evidence contracts distinguish Project-local facts,
qualified cross-project facts, and explicitly declared external sources. A
shared resource or external provider retains its technical owner or external
status; Product context records the qualified relationship without becoming a
second technical writer (`references/shared-technical-model.md`, §9;
`references/product-multi-project-review.md`, §§5, 8, and 13).

The Discovery correctly identifies that internal services, Product members,
third-party SaaS, identity providers, cloud APIs, and external data sources can
be represented with existing families, but complete provider/operation/protocol/
auth/version identity is not guaranteed. It correctly rejects the inference
that a configured URL or installed client dependency proves runtime use.

The standard Technical Documentation package has a broad integrations section,
not a dedicated external-integration document. Therefore
`external_integrations_document_missing = YES` is accurate as a
standardization result, while the underlying capability remains partial rather
than absent.

### Provenance assessment

**Result: PASS**

The Discovery’s `provenance_gap = YES` is not a claim that Stage A–E lacks a
general provenance model. The current model is strong: `EV-*` records source,
locator, symbol/range where available, baseline, and observed fact; STM facts
retain baseline, revision, and supporting `WS-*`/`EV-*` references; Product
evidence adds exact Project/source bindings and Product baseline qualification.

The bounded gap is precise and legitimate: current semantics do not guarantee
that provenance can be attached at the missing operation/entity/access tuple or
to both sides of a provider declaration versus consumer expectation comparison.
The Discovery correctly identifies this as a granularity/linkage gap, not a
missing evidence foundation.

### Dynamic/uncertain interaction assessment

**Result: PASS**

The current projection and STM contracts preserve `PARTIAL`, `UNKNOWN`, stale,
unresolved, and conflicting states. The foundation design also preserves
multiple observed views (`DECLARED`, `IMPLEMENTED`, `CONSUMED`, `TESTED`).

The Discovery correctly finds that these mechanisms do not yet define a
specific accepted precision representation for “known service, unknown
operation,” “known datastore, unknown table,” dynamic URL/service discovery,
dynamic SQL, reflection-generated routes, uncertain ORM targets, or generic
proxies. It does not demand false precision; it requests an explicit bounded
representation that keeps the known portion and limitation visible.

### Security/redaction assessment

**Result: PASS**

Current review coverage treats secrets and sensitive-data propagation as a
material security domain, including credentials, tokens, DSNs, passwords,
query strings, logs, traces, argv/env, caches, and exporters
(`references/discovery-coverage.md`, §6.6). The current contracts also include
configuration/secrets and trust as factual review domains.

The review found no explicit deterministic rule in the current Technical
Documentation or STM contracts that governs redaction of secret values and
sensitive locators in generated Interface/Data catalogs. Therefore the
Discovery’s `secret_redaction_gap = YES` is valid, narrowly scoped to the
catalog/evidence-output boundary. It does not claim that the wider review
method ignores secrets or that Stage F should duplicate the security review
capability.

### User documentation assessment

**Result: PASS**

Current Technical Documentation explicitly registers:

- provided interfaces;
- consumed interfaces;
- integrations;
- data and persistence;
- material flows;
- auth/trust and failure sections.

It does not register dedicated standard outputs named Service API Reference,
Service Consumed API Catalog, Service Data Access Catalog, External
Integrations, Product Interface Catalog, Product Integration Map, Product Data
Access Map, or Provider/Consumer Matrix. The broad existing sections can carry
some of those facts, but that is not equivalent to a dedicated user-facing
projection contract.

The Discovery’s classifications are accurate:

| Requested output | Review classification |
|---|---|
| Service API Reference | PARTIAL |
| Service Consumed API Catalog | PARTIAL |
| Service Integration Dependencies | PARTIAL |
| Service Event Catalog | GENERATABLE_BUT_NOT_STANDARDIZED / PARTIAL |
| Service Data Access Catalog | PARTIAL |
| External Integrations | GENERATABLE_BUT_NOT_STANDARDIZED / PARTIAL |
| Product Interface Catalog | GENERATABLE_BUT_NOT_STANDARDIZED / PARTIAL |
| Product Integration Map | GENERATABLE_BUT_NOT_STANDARDIZED / PARTIAL |
| Product Data Access Map | PARTIAL |
| Provider/Consumer Matrix | MISSING as a registered standard document |

The existing `PRJ-TECH-DOC-*` lifecycle and package contract remains reusable;
the review does not find a need for a parallel document lifecycle.

### Product projection assessment

**Result: PASS**

Stage E supplies the required Product identity/revision, immutable baseline
vector, Project/source qualification, external source binding, availability
dimensions, and cross-project relation boundary. Product Technical
Documentation already reuses `PRJ-TECH-DOC-*`, `TECH-DOC-SCOPE-*`, and
`PKG-TECHNICAL-DOCUMENTATION`, with Product-qualified selectors and finite
membership (`references/technical-documentation.md`, Product scope;
`references/product-multi-project-review.md`, §10).

The Discovery correctly keeps Product Interface, Integration, Data Access,
External Integration, and Provider/Consumer views as projections over qualified
Project STM/evidence. It introduces no `ProductAPI-*`, `ProductData-*`, Product
fact store, or parallel package lifecycle. Product baseline qualification is
sufficient for source identity and revision; it does not cure the missing
operation/entity/access semantics.

### Compatibility assessment

**Result: PASS**

The current model has relevant ingredients but not a complete compatibility
data model or automatic matcher. It preserves observed views and can compare
declared/implemented/consumed/tested concerns through the existing Contract
Verification boundary, but it does not define a complete provider declaration ↔
consumer expectation record with protocol, method/path/topic, version, schema,
provider revision, and consumer revision.

The Discovery accurately describes the gap as compatibility matching/adjudication
missing, not as a request to build a standalone compatibility engine. The exact
owner and representation are legitimate Design decisions.

### Evidence acquisition assessment

**Result: PASS**

The Discovery’s evidence classification is consistent with the shared evidence
contract and the required anti-inference guards:

| Source | Review assessment |
|---|---|
| Router/OpenAPI/protobuf/GraphQL declaration | DIRECT_DECLARATION for declared surface; not proof of runtime use. |
| Concrete client/wrapper/generated method call | STRONG_INFERENCE when a call path and target are evidenced. |
| Service-discovery/config URL | WEAK_HINT unless tied to a concrete call path. |
| Producer/consumer binding | DIRECT_DECLARATION of binding or STRONG_INFERENCE of use depending on evidence. |
| ORM/repository/raw SQL/migration | Direct or strong evidence for the declared target; exact runtime access remains bounded by evidence. |
| Database/client configuration | WEAK_HINT of possible store use, not proof of entity access. |
| Kubernetes/Helm/Terraform | DIRECT_DECLARATION of provisioned/configured infrastructure, not application use. |
| Tests/contracts | DIRECT_DECLARATION of tested expectation, not proof of production behavior. |

The Discovery correctly rejects:

```text
dependency installed != service used
config URL exists != API called
database connection exists != specific table accessed
migration mentions entity != runtime access
```

### Practical capability matrix review

**Result: PASS**

The matrix includes every required representative case: provided and consumed
REST, external API, event producer and consumer, PostgreSQL, table READ and
WRITE, migration ownership, Redis, and object storage. Its family choices are
plausible, its broad store/event representations match current contracts, and
its table/entity/access-mode rows correctly remain insufficient. The matrix
does not promote any projection into authority.

### Architecture option review

**Result: PASS**
**Recommended direction: B**

Option A is correctly recognized as safe but materially incomplete: current
projections can document broad interfaces, integrations, events, and stores but
cannot truthfully promise operation/entity/access/compatibility completeness.

Option B is supported by the evidence. Existing families are intentionally
bounded but already close to the required concepts; current contracts explicitly
allow properties and relations before promoting a new family. A compatible
extension can preserve old broad facts and add evidence-bounded qualifiers.

Option C is correctly rejected because it would create a second factual model,
duplicate provenance and lifecycle, complicate Product qualification, and blur
relation/dependency/projection authority.

No HYBRID recommendation is required at this gate. Design may later choose to
extend only some families while adjusting selectors/relations for others, but
that is an implementation of the recommended existing-family direction, not a
different authority architecture.

### Identity-family assessment

**Result: PASS**

The “no new identity family” conclusion is justified. Interface surfaces,
interactions, stores/entities, events, flows, and external/provider components
can remain under `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, `FLOW-*`, and `COMP-*`, with
controlled properties/relations and shared provenance. The missing concepts are
qualifiers, precision states, matching inputs, and projection contracts—not a
fact class that cannot fit any existing family.

The existing rule that a new family requires repeated cross-capability need for
stable identity and revisioning is preserved (`references/shared-technical-
model.md`, §1).

### Migration assessment

**Result: PASS**

`COMPATIBLE_EXTENSION` is justified. Existing STM artifacts have stable family
identity, revision, baseline, provenance, status, and freshness. Existing broad
facts such as “uses PostgreSQL” or “provided HTTP surface” can remain valid at
their prior precision while new qualifiers are absent, unknown, or added in a
later revision. No identifier rewrite or historical artifact rewrite is
required by the Discovery conclusion.

Existing Technical Documentation projections and Product baselines remain
interpretable because projection contracts already support accepted/fresh
selectors, explicit limitations, Product-qualified snapshots, and stale/
blocked outcomes. A future semantic extension would require ordinary impact and
revalidation, not a foundational redesign.

### Foundational open-question adjudication

**Total: 9**

All nine are **VALID_DESIGN_DECISION**. None is a repository-state question
that Discovery could resolve from the current contracts without selecting a
future semantic design.

1. **Provider/consumer/expectation/declaration record.** Known now: IF direction,
   relations, observed views, and provenance exist. Design must choose the
   minimum representation that keeps provider declaration and consumer
   expectation distinct. The current contract does not choose this shape.
2. **Common versus protocol-specific operation/address fields.** Known now:
   supported surface kinds and broad IF identity exist, but common method/path/
   topic/version fields do not. Design must choose a coherent shared property
   boundary without falsely normalizing protocols.
3. **DS entity identity placement.** Known now: DS owns material stores and
   relations cover broad reads/writes/ownership. Design must decide whether
   entity addressing is nested, relation-targeted, or a DS qualifier while
   preserving store identity.
4. **Access-mode placement.** Known now: current controlled relations do not
   define the required mode vocabulary and dependency metadata is not the right
   factual owner. Design must choose among existing STM property/relation
   placements.
5. **Migration authority linkage.** Known now: migration behavior/evidence is
   in scope but the owner-to-entity tuple is absent. Design must choose how to
   bind schema evolution authority to Project revisions and entity targets.
6. **Precision states.** Known now: the system already preserves partial,
   unknown, unresolved, stale, and conflict limitations. Design must choose the
   Stage F-specific accepted precision vocabulary and projection wording.
7. **Compatibility owner.** Known now: Contract Verification can consume
   declared/implemented/consumed/tested views, but no compatibility authority
   exists. Design must choose a bounded owner/adjudication boundary without a
   standalone engine.
8. **External identifiers and disclosure.** Known now: external source
   bindings/provenance exist, while deterministic catalog redaction is absent.
   Design must choose the safe display/redaction policy.
9. **Standard document/package membership.** Known now: Technical Documentation
   has existing broad projections, selectors, and package lifecycle, while the
   requested dedicated catalogs are not registered. Design must choose which
   are standard members and which remain optional projections.

No question is `DISCOVERY_SHOULD_HAVE_RESOLVED`, `NOT_FOUNDATIONAL`,
`OUT_OF_SCOPE`, or a duplicate.

### Scope and non-goals

**Scope completeness: PASS**

The Discovery covers all required service goals: provided/consumed interfaces,
external APIs, event production/consumption, stores, entity reads/writes,
migration ownership, infrastructure interactions, dependencies, and evidence.
It also covers Product interface/integration/data maps, provider/consumer view,
external integrations, baseline qualification, uncertainty, redaction,
compatibility, and ownership versus usage.

**Scope control: PASS**

The explicit non-goals correctly exclude live database scanning, reverse
engineering, runtime traffic capture, tracing, gateways, service mesh, schema
registry replacement, OpenAPI generation, full SQL parsing, ORM frameworks,
CMDB/graph/RAG infrastructure, and runtime services. The Discovery keeps Stage
F repository/evidence bounded and does not expand it into observability.

### Authority boundary review

**Result: PASS**

The Discovery preserves the existing authority map:

| Concern | Preserved owner |
|---|---|
| Worksets/observations | `WS-*` / `EV-*` Shared Evidence |
| Technical facts | STM and Technical Model Gate |
| Interfaces | `IF-*` |
| Integrations | `INT-*` according to its current interaction meaning |
| Data stores/entities if extended | `DS-*` and controlled relations/properties |
| Events | `EVENT-*` |
| Flows | `FLOW-*` |
| Architecture findings | `RF-*` / Architecture Review |
| Code Quality | `CQ-*` / `CQRA-*` |
| Test Engineering | `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` |
| Projection identity | `PRJ-*` |
| Regeneration session | `RG-*` |

The required principle is preserved:

```text
API/Data Integration Catalog != new factual authority
direct database write = STM fact first
architectural defect = Architecture Review interpretation
```

### Findings

No HIGH, MEDIUM, or LOW findings were identified. The Discovery is accurate
enough to proceed to the Stage F checkpoint without remediation.

### Findings summary

HIGH: 0
MEDIUM: 0
LOW: 0

finding_ids: NONE

### Review dimensions

| Dimension | Result |
|---|---|
| baseline_integrity | PASS |
| current_model_assessment | PASS |
| if_model_assessment | PASS |
| provided_consumed_gap_assessment | PASS |
| ds_model_assessment | PASS |
| data_access_mode_assessment | PASS |
| data_ownership_assessment | PASS |
| schema_migration_assessment | PASS |
| int_flow_decision_quality | PASS |
| event_model_assessment | PASS |
| external_integration_assessment | PASS |
| provenance_gap_assessment | PASS |
| dynamic_interaction_assessment | PASS |
| secret_redaction_assessment | PASS |
| user_documentation_gap_assessment | PASS |
| product_projection_assessment | PASS |
| compatibility_gap_assessment | PASS |
| evidence_acquisition_assessment | PASS |
| practical_matrix_assessment | PASS |
| architecture_option_assessment | PASS |
| new_identity_family_assessment | PASS |
| migration_assessment | PASS |
| open_question_quality | PASS |
| scope_completeness | PASS |
| scope_control | PASS |
| authority_boundary_assessment | PASS |
| single_project_compatibility | PASS |
| stage_e_compatibility | PASS |

### Recommended next gate

`STAGE_F_DISCOVERY_CHECKPOINT`

The Discovery should proceed to the next independently authorized Stage F gate.
The next gate must preserve the current boundaries: existing STM families,
STM Technical Model Gate, Product qualification, projection lifecycle, and
single-project validity.

### Final verdict

`STAGE_F_DISCOVERY_APPROVED`

The Stage F Discovery is independently approved. It accurately identifies the
current model as partial, the real semantic and documentation gaps, the
compatible existing-family direction, and the nine legitimate Design decisions.
It contains no unresolved factual repository question that must be corrected
before Design.
