# Shared Technical Model Foundation Design

Date: 2026-09-04
Status: DESIGN APPROVED FOR IMPLEMENTATION PLANNING
Repository: `todkavodka/architecture-code-review`
Roadmap stage: Stage A — Shared Technical Model Foundation

## 1. Purpose

Introduce a persistent shared factual substrate for the entire review system so that architecture review, Test Engineering, future Code Quality Review, and technical documentation do not independently reconstruct the same system facts.

The design separates four concerns that are currently partially combined inside Architecture Review:

1. repository observations and bounded evidence;
2. accepted factual technical model;
3. capability-specific interpretation;
4. human-readable documents.

The target architecture is:

```text
Repository / external sources
        |
        v
Shared Evidence Layer
   WS-* / EV-*
        |
        v
Shared Technical Model
 factual semantic authority
        |
        +-----------------------+----------------------+----------------------+
        |                       |                      |                      |
        v                       v                      v                      v
Architecture Review       Test Engineering       Code Quality       Technical Documentation
semantic authority        semantic authority     semantic authority      projection
        |                       |                      |
        +-----------------------+----------------------+
                                |
                                v
                    Dependency / Impact Graph
                                |
                                v
                           Projections
```

The Shared Technical Model is not an architecture finding registry, not a test model, and not a human report. It is a reusable factual representation of what the system is and how its material technical surfaces behave.

## 2. Core principles

### 2.1 Facts before interpretation

The foundational separation is:

```text
Technical Fact != Finding
Technical Fact != Risk
Technical Fact != Test Gap
Technical Fact != Recommendation
```

Examples:

```text
OrdersService synchronously calls PaymentService.
```

is a Shared Technical Model fact.

```text
The synchronous dependency creates availability coupling.
```

is an Architecture Review interpretation.

```text
Payment timeout behavior requires an integration assurance target.
```

is Test Engineering semantics.

```text
The PaymentService URL is duplicated across three modules.
```

is a future Code Quality interpretation.

One factual object may therefore support several capability-specific conclusions without those capabilities owning or rewriting the fact.

### 2.2 Shared Technical Model is persistent

Every `NEW` session creates a persistent Shared Technical Model baseline.

Persistence does not imply freshness:

```text
persisted != fresh
accepted != complete
coverage != depth
```

The model survives `RESUME`, `EXTEND`, and `REVALIDATE` and is reused when its accepted factual slice remains sufficiently fresh for the requested downstream capability.

### 2.3 Shared Technical Model is always created, but may be partial

Every `NEW` creates the model.

This does not mean every `NEW` must immediately build every possible technical domain.

```text
always create model
!=
always build complete model
```

A bounded capability may build only the technical slices it requires.

A full Architecture Review is different: both architecture modes require full factual coverage.

### 2.4 Architecture Review is a consumer, not the factual owner

The future Architecture Review must not maintain a parallel factual system model once the equivalent Shared Technical Model slice is accepted and fresh.

Architecture Review owns:

- architectural properties and invariants;
- responsibility and coupling analysis;
- architecture risks;
- security/correctness interpretation;
- candidate and root findings;
- supporting engineering risks;
- positive controls as architectural significance;
- root-boundary adjudication;
- severity;
- target architecture;
- remediation implications.

It does not own factual inventories of components, interfaces, interactions, stores, runtime topology, flows, or trust mechanisms.

### 2.5 Shared evidence, owned interpretation

Evidence is shared across capabilities.

Interpretation remains capability-owned.

```text
EV-*       shared observation

COMP-*
IF-*
INT-*
DS-*
EVENT-*
FLOW-*
AUTH-*
CFG-*
ERR-*      shared technical facts

RF-*
SER-*      Architecture-owned

BC-*
CC-*
MAT-*
TM-*
GAP-*      Test Engineering-owned

future CQ-* Code Quality-owned
```

A capability may discover new evidence and technical fact candidates, but it must not silently mutate accepted shared facts.

## 3. Required high-level workflow

### 3.1 NEW

```text
START
  |
  v
Session Orchestration
  |
  v
Repository / previous-state reconciliation
  |
  v
Requested capabilities and endpoints
  |
  v
Technical Model dependency planning
  |
  v
Technical bootstrap
  |
  v
Persistent Shared Technical Model baseline
  |
  v
Build/revalidate required factual slices
  |
  v
Technical Model Gate
  |
  v
Capability-specific analysis
  |
  v
Capability semantic authority
  |
  v
Human-readable projections
```

### 3.2 EXTEND

```text
existing audit package
        |
        v
existing Shared Technical Model
        |
        v
requested new capability/output
        |
        v
required factual slice calculation
        |
        +-- reuse ACCEPTED + VALID facts
        |
        +-- build missing facts
        |
        +-- revalidate stale/disputed facts
        |
        v
execute minimum downstream capability slice
```

Adding a capability does not trigger a full factual rediscovery by default.

### 3.3 REVALIDATE

```text
old baseline
    |
    v
new baseline
    |
    v
change / impact analysis
    |
    v
affected evidence and STM artifacts
    |
    v
affected technical aspects/slices
    |
    v
targeted technical revalidation
    |
    v
dependency propagation
    |
    v
only affected capability semantics and projections
```

Repository change does not automatically rebuild the complete Shared Technical Model.

Revalidation is impact-driven.

## 4. Architecture mode projection

The existing Architecture Review modes remain:

```text
STANDARD_FULL
FORENSIC
```

Both require full factual coverage.

They differ in required depth, evidence granularity, decomposition, and review rigor.

The Shared Technical Model therefore has two independent dimensions:

```text
coverage:
  TARGETED
  FULL

depth:
  COMPACT
  FORENSIC
```

### 4.1 STANDARD_FULL

```text
Architecture mode:
  STANDARD_FULL

STM requirement:
  coverage: FULL
  depth: COMPACT
  evidence: MATERIAL
  flows: REPRESENTATIVE
  contradictions: MATERIAL
  review: full-model independent review
```

`STANDARD_FULL` means complete coverage of all material applicable technical domains, with sufficient aggregation for reliable full architectural analysis.

It does not mean shallow or incomplete factual discovery.

### 4.2 FORENSIC

```text
Architecture mode:
  FORENSIC

STM requirement:
  coverage: FULL
  depth: FORENSIC
  evidence: GRANULAR
  flows: MECHANISM_COMPLETE_WHERE_MATERIAL
  contradictions: EXPLICIT_MULTI_VIEW
  review: critical-slice review + full-model integration review
```

The same semantic schema is used in both modes.

`FORENSIC` enriches the model; it does not create another factual model.

Normative compatibility:

```text
FULL / FORENSIC
satisfies
FULL / COMPACT
```

An upgrade from `STANDARD_FULL` to `FORENSIC` is model enrichment rather than a restart.

## 5. Shared Evidence Layer

### 5.1 Purpose

The Shared Evidence Layer captures bounded repository/source observations from which shared technical facts and capability-specific conclusions may be derived.

It must not become a giant copied source tree or a capability-specific evidence silo.

Conceptually:

```text
Raw repository/source
        |
        v
WS-* bounded investigation
        |
        v
EV-* addressable observation
        |
        v
technical facts / capability semantics
```

### 5.2 Worksets (`WS-*`)

A workset is the physical grouping and bounded investigation unit.

Examples:

```text
WS-001-runtime-bootstrap
WS-002-http-api
WS-003-persistence
WS-004-payment-integration
WS-005-auth-boundaries
```

A workset should record at minimum:

```text
id
name
scope
baseline
status
investigated sources
limitations
EV records
handoff
```

A workset is optimized for bounded agent work and review.

It is not product-behavior authority.

### 5.3 Evidence observations (`EV-*`)

`EV-*` is the logical addressable evidence unit.

An `EV-*` may physically live inside a `WS-*` file.

Example:

```text
WS-004-payment-integration.md

## EV-041

source:
  src/payments/client.ts

symbol:
  PaymentClient.createPayment

baseline:
  <commit>

observed:
  outbound HTTP request to PaymentService
  timeout configured to 5 seconds
```

A factual artifact may then reference:

```text
evidenced_by:
  - WS-004#EV-041
  - WS-004#EV-042
```

The design deliberately avoids one file per evidence observation because that would create excessive tiny-file fragmentation.

### 5.4 Evidence is historical, not rewritten

Evidence belongs to the baseline at which it was observed.

If the repository changes, old evidence is not rejected or rewritten.

Example:

```text
EV-041 @ baseline A
  timeout = 5s

EV-318 @ baseline B
  timeout = 10s
```

The technical fact revision changes; the historical evidence remains a valid observation of the old baseline.

### 5.5 Reading hierarchy

Consumers should prefer the smallest sufficient context:

```text
INDEX
  |
  v
semantic artifact
  |
  v
evidence observation
  |
  v
original source
```

Raw repository rereading is performed when accepted artifacts/evidence are insufficient, stale, disputed, or a new factual slice is required.

## 6. Shared Technical Model semantic objects

The model should use semantically addressable objects rather than one monolithic Markdown document.

Initial first-class families:

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

This taxonomy is intentionally bounded. New first-class types should be introduced only when repeated cross-capability use shows that a property/relation can no longer be represented cleanly.

### 6.1 `COMP-*` — Component / Runtime Unit

Represents a material system unit such as:

- service;
- major module;
- worker;
- scheduler;
- gateway;
- adapter;
- repository layer;
- public library surface;
- native/desktop process.

Do not create one component object for every class, function, or trivial helper.

### 6.2 `IF-*` — Interface

Represents a material interaction surface, including where applicable:

- HTTP;
- gRPC;
- IPC;
- CLI/public command;
- WebSocket;
- webhook/callback;
- public library API;
- file/protocol surface.

Direction is a property/view such as:

```text
PROVIDED
CONSUMED
```

### 6.3 `INT-*` — Interaction

Represents a material relationship between producer/caller and consumer/provider.

Typical properties:

```text
source
target
interface
protocol
sync_or_async
timeout
retry
identity/correlation where material
failure behavior where material
```

`INT-*` is central for reuse by Architecture Review, integration Test Engineering, E2E design, and technical documentation.

### 6.4 `DS-*` — Data Store

Represents material persistence/storage such as:

- PostgreSQL;
- SQLite;
- Redis;
- object storage;
- filesystem;
- Elasticsearch;
- domain-specific durable store.

Ownership, read/write participation, migration/consistency behavior are represented through relations/properties rather than automatically creating separate schema-object taxonomies.

### 6.5 `EVENT-*` — Event / Message

Represents material events/messages and their transport semantics.

Where applicable:

```text
name/topic
producer
consumer
payload/schema
delivery assumptions
ordering
retry
DLQ
idempotency
```

### 6.6 `FLOW-*` — Material Flow

Represents significant business/system/control flows, not every internal call chain.

Examples:

- startup/readiness;
- central read;
- central write;
- background/scheduled work;
- external integration;
- persistent write;
- failure/recovery;
- shutdown;
- security-sensitive operation.

### 6.7 `AUTH-*` — Auth / Trust Boundary

Represents factual authentication, authorization, identity propagation, principal, credential, and trust-boundary mechanisms.

Security quality/risk remains Architecture Review semantics.

### 6.8 `CFG-*` — Configuration Fact

Represents behaviorally relevant configuration:

- environment variables;
- config files;
- feature flags;
- runtime options;
- settings that influence interfaces, dependencies, persistence, security, lifecycle, or behavior.

Do not index cosmetic configuration by default.

### 6.9 `ERR-*` — Error / Failure Contract

Represents material error/failure behavior across boundaries:

- HTTP status/error representation;
- exception/error class;
- retryable/non-retryable mapping;
- fallback;
- partial result;
- event/process failure;
- context preservation.

## 7. Shared Technical Model relations

Relations are first-class semantic links even when they are stored as metadata rather than standalone files.

Initial controlled vocabulary includes:

```text
PROVIDES
CONSUMES
CALLS
PUBLISHES
SUBSCRIBES
READS_FROM
WRITES_TO
OWNS_STATE
PROTECTED_BY
CONFIGURED_BY
EMITS_ERROR
PARTICIPATES_IN
DEPLOYS_AS
DEPENDS_ON
```

The relation vocabulary should remain controlled and reviewable.

Arbitrary free-form relation names are discouraged because they destroy reliable cross-capability indexing.

## 8. Full Technical Model coverage domains

`FULL` is defined by material domain coverage, not by raw object count.

For every full model, classify the following domains where materially applicable:

1. System Context
2. Components / Runtime Units
3. Entry Points
4. Provided Interfaces
5. Consumed Interfaces
6. Interactions
7. Events / Messaging
8. Data Stores / Persistence
9. State Ownership
10. Material Flows
11. Lifecycle / State Machines
12. Authentication / Authorization / Trust
13. Error / Failure Contracts
14. Configuration Surface
15. Concurrency / Serialization / Idempotency Mechanisms
16. Deployment / Runtime Topology
17. Observability Mechanisms
18. Platform-Specific Behavior

The list is materiality-driven. A domain may be absent by design.

### 8.1 Coverage status

Each domain must be classified using explicit coverage state.

Recommended closed vocabulary:

```text
PENDING
IN_PROGRESS
ACCEPTED
PARTIAL
BLOCKED
NOT_APPLICABLE
UNKNOWN
```

`PARTIAL`, `BLOCKED`, and `UNKNOWN` are not silently equivalent to complete.

Every non-accepted state requires an explicit reason and downstream impact assessment.

### 8.2 Full does not mean every internal function

For interfaces/interactions, full coverage means:

> all material externally visible or architecturally relevant interface and interaction surfaces known within the evidence-bounded scope.

It does not mean a call graph for every private helper or local function.

## 9. Properties that remain embedded rather than first-class initially

To avoid over-modeling, the initial design does not require separate families for:

```text
ENTRYPOINT-*
STATE-*
LIFECYCLE-*
CONCURRENCY-*
DEPLOYMENT-*
OBSERVABILITY-*
```

These concerns are represented as properties/relations on the first-class technical objects.

If later capabilities repeatedly require stable identity and revisioning for one of these concepts, the design may promote it to a first-class family.

## 10. Multi-view technical observations

Technical facts may need to preserve different observed representations without prematurely choosing a winner.

Useful views include:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

Example:

```text
IF-021

DECLARED:
  OpenAPI exposes 201 / 400

IMPLEMENTED:
  code exposes 201 / 400 / 409

CONSUMED:
  client handles 409

TESTED:
  tests cover only 201 / 400
```

The Shared Technical Model preserves the observations.

It must not automatically decide that OpenAPI, implementation, consumer, or tests are authoritative.

Where authority resolution is required, a dedicated capability gate such as Test Engineering Contract Verification may resolve the relevant semantic decision.

## 11. Technical fact lifecycle

Lifecycle, freshness, and authority are separate concerns.

### 11.1 Semantic lifecycle

```text
CANDIDATE
UNDER_REVIEW
ACCEPTED
SUPERSEDED
REJECTED
```

### 11.2 Freshness

```text
VALID
REVALIDATION_REQUIRED
UNKNOWN
```

### 11.3 Authority

Where relevant:

```text
RESOLVED
UNRESOLVED
```

An accepted fact may therefore remain historically accepted while requiring revalidation against a later repository baseline.

### 11.4 Revisions

Preserve semantic identity when the same technical object changes:

```text
INT-033@rev1
INT-033@rev2
INT-033@rev3
```

When the semantic identity itself changes, supersede it explicitly:

```text
INT-033
status: SUPERSEDED
superseded_by: INT-091
```

Do not rewrite history.

## 12. Technical Model Gate

The Technical Model Gate is the sole writer of accepted shared technical fact semantics.

Other capabilities may emit:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

They may not directly rewrite accepted facts.

Example:

```text
Architecture Review
  observes a retry behavior that conflicts with INT-033
        |
        v
TECH_FACT_CONFLICT
        |
        v
Technical Model Gate
        |
        +-- verify evidence
        +-- revise/reject candidate
        +-- create new technical revision
        +-- run impact analysis
        |
        v
Architecture Review resumes
```

This generalizes the current `ARCH-CORRECTION-CANDIDATE` concept from Architecture-owned As-Built to shared factual authority.

## 13. Persistent artifact layout

The authoritative technical model should be stored as small semantically addressable artifacts.

Recommended conceptual shape:

```text
working/
├── evidence/
│   ├── INDEX.md
│   ├── WS-001-runtime-bootstrap.md
│   ├── WS-002-http-api.md
│   └── ...
│
├── technical-model/
│   ├── INDEX.md
│   ├── coverage.md
│   ├── components/
│   │   ├── COMP-001.md
│   │   └── ...
│   ├── interfaces/
│   │   ├── IF-001.md
│   │   └── ...
│   ├── interactions/
│   ├── data-stores/
│   ├── events/
│   ├── flows/
│   ├── auth/
│   ├── errors/
│   └── configuration/
│
├── architecture/
├── capabilities/
└── indexes/
```

Exact project-local paths may vary.

The invariant is artifact role and authority, not one universal filesystem spelling.

### 13.1 Artifact granularity

One semantically addressable object should normally map to one technical artifact.

Preferred:

```text
IF-021.md
INT-033.md
FLOW-008.md
```

Avoid both extremes:

```text
one giant technical-model.md
```

and:

```text
IF-021-method.md
IF-021-path.md
IF-021-auth.md
IF-021-response-201.md
```

## 14. Indexes and dependency graph

Indexes are navigation and generated infrastructure, not competing semantic authority.

### 14.1 Hybrid dependency model

Each authoritative artifact stores its direct outbound dependency metadata.

A generated central registry builds reverse and aggregate indexes.

```text
artifact
  |
  +-- direct typed dependencies
  |
  v
generated dependency graph
  |
  +-- reverse edges
  +-- capability indexes
  +-- stale-impact index
  +-- projection dependencies
```

Normative rule:

> Generated indexes must be reproducible entirely from authoritative artifact metadata.

If a reverse index is lost or stale, rebuild it.

Do not treat the generated reverse index as the source of semantic truth.

### 14.2 Initial dependency types

Controlled vocabulary:

```text
EVIDENCED_BY
DERIVED_FROM
DEPENDS_ON
REFERENCES
SUPERSEDES
PROJECTS_FROM
```

Not every relation has identical invalidation semantics.

### 14.3 Dependency impact strength

Initial impact vocabulary:

```text
HARD
CONDITIONAL
INFORMATIONAL
```

Semantics:

```text
HARD dependency changed
  -> dependent becomes REVALIDATION_REQUIRED

CONDITIONAL dependency changed
  -> dependent becomes IMPACT_REVIEW_REQUIRED

INFORMATIONAL dependency changed
  -> no semantic invalidation by default
```

The exact persisted status vocabulary may be normalized during implementation planning, but the three-way impact distinction is part of the design.

### 14.4 Future aspect-level precision

The dependency schema should remain extensible for future aspect-level impact, for example:

```text
depends_on:
  artifact: IF-021
  aspects:
    - auth
    - responses
  impact: HARD
```

Aspect-level impact is not required for the first implementation slice.

Do not create field-level artifacts merely to gain field-level invalidation.

## 15. Projection dependencies

Human-readable projections may depend on:

1. explicit technical/capability object IDs;
2. set/query selectors.

Example:

```text
Technical Documentation / Consumed APIs
projects_from:
  all IF-* where direction = CONSUMED
```

Set/query dependencies are necessary because a newly created object can make a projection stale even though that object did not exist when the projection was last generated.

Example:

```text
new IF-085 direction=CONSUMED
        |
        v
Consumed API documentation becomes stale
```

This design is the foundation for Stage B — Audit Projection & Regeneration.

## 16. Human-readable projections

Authoritative audit state is optimized for correctness, selective retrieval, revisioning, and reuse.

Human documents are optimized for comprehension.

Normative principle:

> Authoritative audit state is stored as small, persistent, semantically addressable artifacts. Indexes organize those artifacts. Human-readable documents are projections assembled from accepted authority.

### 16.1 Technical Documentation

Technical Documentation is a human-facing factual projection from accepted Shared Technical Model state.

Candidate projections include:

```text
technical-documentation/
├── 00-system-overview.md
├── 01-components.md
├── 02-provided-api.md
├── 03-consumed-api.md
├── 04-integrations.md
├── 05-data-and-persistence.md
├── 06-runtime-and-deployment.md
├── 07-auth-and-trust.md
├── 08-material-flows.md
└── 09-failure-behavior.md
```

The exact document taxonomy is implementation-planning detail.

Technical Documentation must not become semantic authority merely because it is easier for a human to read.

### 16.2 As-Built Architecture

The existing human-readable As-Built concept remains valuable, but its authority changes.

Current model:

```text
accepted As-Built
= factual source of truth
```

Future model:

```text
Shared Technical Model
= factual source of truth

As-Built Architecture
= architecture-oriented human projection
  from accepted STM
```

Downstream capabilities must not parse the As-Built projection as factual authority when the Shared Technical Model exists.

### 16.3 Architecture Report

The final Architecture Review becomes a projection over:

```text
accepted Shared Technical Model
+
accepted Architecture Review semantic authority
```

Its factual architecture chapter is synthesized from STM.

Its findings and architectural conclusions are synthesized from Architecture-owned authority.

## 17. Architecture Review migration map

The current Architecture Review already performs much of the future technical-model discovery inside its As-Built phase.

The migration separates factual ownership from architectural interpretation.

| Current Architecture responsibility | Future owner |
|---|---|
| repository/source evidence gathering | Shared Evidence Layer |
| repository baseline identity | Session Orchestration |
| factual As-Built model | Shared Technical Model |
| components/runtime topology | STM |
| API/IPC/process surfaces | STM |
| consumed/provided interfaces | STM |
| interactions/integrations | STM |
| state ownership facts | STM |
| persistence/data-store facts | STM |
| material flows | STM |
| lifecycle/state-machine facts | STM |
| auth/trust mechanism facts | STM |
| configuration facts | STM |
| error/failure mechanism facts | STM |
| concurrency/idempotency mechanisms | STM |
| observability/platform facts | STM |
| architecture invariants | Architecture Review |
| architectural responsibility/coupling assessment | Architecture Review |
| architecture candidates/findings | Architecture Review |
| security/correctness risk interpretation | Architecture Review |
| `RF-*`, `SER-*`, architecture `OQ-*` | Architecture Review |
| root-boundary adjudication | Architecture Review |
| severity | Architecture Review |
| human As-Built | Projection |
| Technical Documentation | Projection |
| final Architecture Report | Projection over STM + Architecture authority |
| reverse indexes / impact maps | Generated infrastructure |

## 18. Architecture and technical coverage are separate authorities

The current Architecture Review Discovery Coverage Matrix answers:

> Did Architecture Review investigate every material architecture/security/reliability mechanism class required by its review contract?

The future Technical Model Coverage answers:

> Did factual discovery describe every material technical domain required for this Shared Technical Model scope/depth?

These must not be collapsed.

```text
TECHNICAL_MODEL_COVERAGE_ACCEPTED
!=
ARCHITECTURE_COVERAGE_ACCEPTED
```

For full Architecture Review:

```text
Shared Evidence
        |
        v
FULL STM
        |
        v
Technical Model Coverage Review
        |
        v
TECHNICAL_MODEL_COVERAGE_ACCEPTED
        |
        v
Architecture thematic discovery
        |
        v
Architecture Discovery Coverage
        |
        v
ARCHITECTURE_COVERAGE_ACCEPTED
        |
        v
candidate verification / adjudication
```

## 19. Future STANDARD_FULL Architecture Review

```text
STANDARD_FULL
|
+-- Session Orchestration / baseline
|
+-- Shared Evidence
|
+-- Shared Technical Model
|    coverage: FULL
|    depth: COMPACT
|    material evidence
|    representative material flows
|    full-model independent review
|
+-- TECHNICAL_MODEL_COVERAGE_ACCEPTED
|
+-- Architecture Review
|    compact thematic investigation
|    architecture candidates
|    Architecture Discovery Coverage Matrix
|    coverage closeout
|    candidate verification
|    root adjudication
|    severity adjudication
|
+-- projections
     As-Built Architecture
     Architecture Review
     Technical Documentation when selected
```

Existing Architecture correctness gates remain conceptually valid.

The factual discovery that currently produces As-Built is moved to shared ownership.

## 20. Future FORENSIC Architecture Review

```text
FORENSIC
|
+-- Session Orchestration / baseline
|
+-- Shared Evidence
|
+-- Shared Technical Model
|    coverage: FULL
|    depth: FORENSIC
|    granular WS/EV trail
|    explicit multi-view contradictions
|    deeper technical decomposition
|    critical-slice review where material
|    full-model integration review
|
+-- TECHNICAL_MODEL_COVERAGE_ACCEPTED
|
+-- Architecture Review
|    separated ownership/isolation analysis
|    lifecycle/concurrency analysis
|    boundary analysis
|    frontend/state/events where applicable
|    security analysis
|    maintainability analysis
|    Independent Architecture Coverage Review
|    verification
|    root adjudication
|    severity adjudication
|
+-- projections
```

Forensic mode keeps a deeper evidence trail and more explicit review gates, but shares the same factual schema.

## 21. Test Engineering integration

The accepted Test Engineering semantic model remains intact.

The Shared Technical Model does not replace:

```text
BC-*
CC-*
MAT-*
TM-*
GAP-*
TASK-*
```

It replaces repeated technical rediscovery where those capabilities need factual system boundaries.

Future relationship:

```text
Shared Technical Model
        |
        v
Behavior Model / Contract Verification / Test Assurance
        |
        v
BC / CC / MAT / TM / GAP authority
```

A Behavior Contract remains a test-oriented material behavior contract, not an `IF-*`, `INT-*`, or `FLOW-*`.

Technical facts may reduce context and discovery cost, but capability semantic boundaries remain unchanged.

## 22. Code Quality integration

Future Code Quality Review may consume:

- components;
- interfaces;
- configuration facts;
- interaction facts;
- dependency relationships;
- evidence worksets.

It still owns code-quality judgments such as:

- duplication;
- hardcodes;
- bad abstractions;
- framework anti-patterns;
- maintainability risks;
- resource/error management quality.

A code-quality finding is not automatically an Architecture finding.

## 23. Product / multi-project compatibility

The model should be project-local initially but designed so later Product / Multi-Project Review can compose project graphs.

First-class objects and controlled relations are therefore preferred over prose-only architecture descriptions.

Future composition may connect:

```text
Project A COMP-* / IF-*
        |
        v
cross-project INT-*
        |
        v
Project B IF-* / COMP-*
```

No Product-level semantic authority is introduced in Stage A.

## 24. Legacy package reconciliation

Existing audit packages may contain:

```text
accepted As-Built
STM absent
```

This is legacy state, not corruption.

`RESUME`, `EXTEND`, or `REVALIDATE` may require additive backfill.

Legacy migration rule:

```text
legacy As-Built
      |
      v
candidate factual extraction
      |
      +-- original evidence / source validation
      |
      v
Technical Model Gate
      |
      v
accepted STM
```

The old As-Built may seed candidate facts.

It must not be silently renamed or reclassified as Shared Technical Model authority.

Normative invariant:

> No existing semantic authority is silently reclassified.

## 25. Migration sequence

Stage A should be implemented incrementally rather than by a single rewrite.

### A1 — Shared Evidence Layer

Introduce:

- shared worksets;
- addressable evidence records;
- baseline binding;
- shared evidence indexing;
- cross-capability evidence reuse contract.

Do not change Architecture Review authority yet.

### A2 — Shared Technical Model Core

Introduce:

- technical object schema;
- relation vocabulary;
- lifecycle/freshness/revision semantics;
- Technical Model Gate;
- persistent technical artifacts.

### A3 — Technical Model Coverage

Introduce:

- required FULL domains;
- TARGETED/FULL coverage semantics;
- COMPACT/FORENSIC depth semantics;
- Technical Model Coverage Matrix;
- full-model review gates.

### A4 — Dependency / Index Infrastructure

Introduce:

- local typed direct dependencies;
- generated reverse index;
- impact strength;
- stale-impact traversal;
- projection dependency selectors.

### A5 — Technical Documentation

Build human factual projections from accepted STM.

Use this as an early pressure test of whether the factual schema is sufficiently complete for human technical understanding.

### A6 — As-Built Projection Migration

Change As-Built from factual authority to human projection.

Require parity validation against the existing As-Built contract.

Suggested gate:

```text
AS_BUILT_PROJECTION_PARITY_ACCEPTED
```

The new projection must not lose material factual content previously required from full Architecture Review.

### A7 — Architecture Review Integration

Remove duplicate factual system-model ownership from Architecture Review.

Architecture Review consumes accepted/fresh STM and requests factual expansion/revalidation via `TECH_FACT_*`.

### A8 — Legacy Audit Reconciliation

Support legacy packages without forcing full restart.

Backfill STM conservatively and evidence-first.

## 26. Compatibility and migration invariants

The migration must preserve these behaviors:

1. `STANDARD_FULL` remains a full Architecture Review.
2. `FORENSIC` remains the deeper, more explicit investigation mode.
3. Existing candidate verification, root adjudication, severity, and architecture coverage gates are not weakened.
4. Test Engineering semantic identifiers and authorities remain distinct.
5. Existing packages without STM remain resumable through reconciliation.
6. No old As-Built is automatically treated as accepted STM.
7. No capability silently mutates shared accepted facts.
8. A full Architecture Review cannot complete with less than required full factual STM coverage.
9. `FULL/FORENSIC` satisfies `FULL/COMPACT`.
10. Technical Documentation and As-Built are projections, not factual authority.
11. Generated indexes are rebuildable and non-authoritative.
12. Revalidation is impact-driven rather than full-rebuild-by-default.

## 27. Context-efficiency objective

A major purpose of the design is smaller bounded context.

Consumers should be able to request a narrow working set such as:

```text
RF-041
+ HARD factual dependencies
+ unresolved CONDITIONAL dependencies
+ linked evidence
```

rather than loading:

```text
entire As-Built
+ entire Architecture Report
+ entire Test Engineering package
+ whole repository
```

Expected benefits:

- smaller model context;
- less repeated repository reading;
- better provenance;
- cheaper `EXTEND`;
- targeted `REVALIDATE`;
- precise impact analysis;
- simpler projection regeneration;
- better cross-capability consistency.

Context reduction must not weaken evidence requirements. If a fact is disputed, stale, incomplete, or insufficient, consumers must expand back to evidence and source.

## 28. Out of scope for Stage A

Stage A does not automatically include:

- implementation of Stage B projection regeneration engine beyond the dependency foundations it needs;
- automatic Product-level multi-project authority;
- replacement of Test Engineering Behavior Contracts;
- complete AST/call-graph indexing;
- a database or graph database;
- automatic resolution of OpenAPI/code/consumer conflicts;
- code-quality findings;
- test execution infrastructure;
- simulator implementation;
- automatic source-code modification;
- field-level dependency invalidation as a mandatory first release requirement.

## 29. Design acceptance criteria

The Stage A implementation plan must preserve all of the following:

### 29.1 Factual model

- every `NEW` creates a persistent technical model baseline;
- `STANDARD_FULL` requires `FULL/COMPACT`;
- `FORENSIC` requires `FULL/FORENSIC`;
- the same technical semantic schema serves both;
- full coverage is materiality-driven and evidence-bounded.

### 29.2 Evidence

- evidence is shared;
- evidence observations are addressable;
- worksets bind evidence into manageable physical artifacts;
- evidence is baseline-bound and historical;
- old evidence is not silently rewritten.

### 29.3 Authority

- Technical Model Gate is sole writer of accepted technical facts;
- capability interpretation remains owned by its capability;
- As-Built and Technical Documentation are projections;
- indexes are generated infrastructure.

### 29.4 Architecture integration

- current Architecture As-Built factual requirements are represented by STM coverage;
- Architecture Review does not maintain duplicate factual authority;
- Architecture Discovery Coverage remains separate from Technical Model Coverage;
- architecture findings/root/severity semantics remain Architecture-owned.

### 29.5 Reuse and freshness

- persisted does not imply fresh;
- accepted does not imply complete;
- stale/disputed facts block unsafe downstream use;
- `EXTEND` reuses accepted/fresh minimum slices;
- `REVALIDATE` is impact-driven.

### 29.6 Dependency model

- direct dependencies live with authoritative artifacts;
- reverse/aggregate indexes are generated;
- dependency types are controlled;
- impact distinguishes at least HARD, CONDITIONAL, and INFORMATIONAL;
- the schema remains extensible for later aspect-level impact.

### 29.7 Legacy compatibility

- legacy As-Built packages are not treated as corrupt;
- legacy backfill is evidence-validated;
- no semantic authority is silently reclassified.

## 30. Recommended next step

After this design is accepted in Git, produce a separate implementation plan.

The implementation plan should:

1. inspect the current Architecture Review and Test Engineering contracts file by file;
2. define minimum safe migration slices A1-A8;
3. preserve current architecture/test regression canaries;
4. introduce new tests for authority, lifecycle, mode projection, legacy reconciliation, and impact behavior before changing existing Architecture Review ownership;
5. treat As-Built projection migration as a separate compatibility gate;
6. avoid one giant rewrite of `SKILL.md` or the orchestration references.

Implementation begins only after that plan is independently reviewed and accepted.
