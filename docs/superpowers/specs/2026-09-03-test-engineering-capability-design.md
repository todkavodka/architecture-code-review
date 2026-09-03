# Test Engineering Capability Design

Date: 2026-09-03
Status: DESIGN APPROVED FOR IMPLEMENTATION PLANNING
Repository: `todkavodka/architecture-code-review`

## 1. Purpose

Extend the existing Test Review capability into a broader Test Engineering capability without weakening the existing evidence-first review model.

The capability should help answer, in order:

1. What tests already exist?
2. What material behavior do they actually prove?
3. Which important behavior remains unproven or only partially proven?
4. Do declared contracts such as Swagger/OpenAPI agree with the implementation, real consumers, and tests?
5. Which additional tests should be created, and at what test boundary?
6. What environment or controlled substitutes are required to run those tests reliably?
7. How should the reviewed service itself be simulated so that its consumers can test against it without running the real service?
8. Which multi-component scenarios are valuable enough to become E2E tests?
9. If a Service Simulator is desired, what implementation plan is required to build and integrate it safely?

This design separates assurance review, behavioral modeling, contract verification, test design, environment design, simulator design, and E2E design. The Skill may design and plan these outputs, but does not automatically implement tests, simulator code, or test infrastructure during review.

## 2. Existing foundation that remains valid

The current Test Review behavior remains the assurance layer.

It already aims to determine:

- what material contracts have executable evidence;
- where evidence is partial or absent;
- where tests may provide false confidence;
- what important verification gaps remain;
- what should be fixed first.

Existing compatibility outputs remain:

- `00-test-assurance-summary.md` — concise human decision summary;
- `01-test-assurance-map.md` — detailed assurance/evidence map;
- `02-test-plan.md` — optional existing-compatible Test Plan output.

The broader Test Engineering capability builds on accepted Test Review evidence rather than silently replacing or reinterpreting it.

## 3. Core architectural principle

One bounded model of material system behavior is the shared semantic source for downstream test engineering.

Conceptually:

```text
accepted architecture / observed implementation / declared contracts / consumers
                              |
                              v
                     Behavior Contract Model
                           BC-*
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
 Contract Verification   Test Design       Scenario Design
       CC-*                  |              /          \
                             v             v            v
                    Test Environment   Simulator       E2E
                         Design          Design        Design
```

Test Plan, Contract Verification, Service Simulator scenarios, and E2E scenarios must not independently invent conflicting models of product behavior.

## 4. Test Engineering layers

### 4.1 Test Assurance

Purpose:

- inspect the existing test system;
- determine freshness and relevance;
- map executable evidence to material assurance targets;
- identify false-confidence patterns;
- identify gaps.

Primary outputs:

- Test Assurance Summary;
- Test Assurance Map.

This remains the evidence-first core.

### 4.2 Behavior Model

Purpose:

Reconstruct a bounded set of material, independently verifiable behaviors relevant to testing.

The model may use evidence such as:

- accepted As-Built architecture;
- accepted architecture/root findings;
- real code paths;
- state transitions;
- public protocols;
- schema definitions;
- external side effects;
- declared API/event contracts;
- observed consumer behavior;
- existing tests as observations, but not as the semantic owner of product behavior.

This is not a second architecture model. It is a test-oriented semantic projection of material behavior.

### 4.3 Contract Verification

Purpose:

Compare materially relevant contract representations when a declared or machine-readable contract exists.

Typical inputs:

- OpenAPI / Swagger;
- protobuf / gRPC definitions;
- AsyncAPI / event schemas;
- documented API contracts;
- implementation routes, handlers, DTOs, serializers, auth behavior and error paths;
- real consumers such as frontend, SDK, CLI, adapters, or peer services;
- tests that encode or claim contract behavior.

Contract Verification is an internal automatic gate when materially applicable. A user-facing Contract Consistency Report is optional.

### 4.4 Test Design

For each inadequately evidenced material behavior, recommend the smallest useful test boundary capable of proving it.

Possible classes include:

- unit;
- component;
- integration;
- contract;
- lifecycle;
- concurrency;
- negative/failure-path;
- recovery;
- E2E candidate.

A proposed test must explain why that boundary is appropriate.

### 4.5 Test Environment Design

Determine what the reviewed service needs around it to execute meaningful and deterministic tests.

This covers dependencies of the reviewed service, such as:

- PostgreSQL;
- Redis;
- Kafka/NATS/RabbitMQ;
- S3/object storage;
- OAuth provider;
- SMTP;
- external HTTP APIs;
- filesystem;
- time/clock;
- DNS/network boundary where materially relevant.

The capability must not assume every dependency should be mocked.

### 4.6 Service Simulator Design

Design a controllable simulation of the reviewed service itself so its consumers can run development, integration, CI/CD, or E2E tests without the real service.

This is distinct from substitutes used by the reviewed service's own tests.

### 4.7 E2E Design

Identify scenarios whose assurance value depends on multiple real components interacting across material boundaries.

E2E scenarios derive from accepted Behavior Contracts rather than generic UI happy paths.

## 5. Semantic identifier model

The following identifier families remain semantically distinct:

```text
RF-*    Architecture/root finding
        Why an existing mechanism or architecture is problematic.

BC-*    Behavior Contract
        One bounded, independently verifiable material behavior.

CC-*    Contract Consistency Record
        An observable mismatch among declared, implemented, consumed, or tested views.

MAT-*   Material Assurance Target
        A behavior/risk that Test Assurance commits to account for in its bounded inventory.

TM-*    Test Mapping
        Executable evidence mapped to a MAT/BC and its evidence boundary.

GAP-*   Assurance Gap
        Missing, partial, misleading, or otherwise inadequate evidence for a material target.

TASK-*  Test Engineering remediation task
        Work required to close an accepted assurance gap or produce required test capability.

WS-*    Working-set / investigation record
        Temporary discovery/evidence state; not product behavior authority.
```

Normative separations:

```text
BC != MAT
BC != RF
BC != GAP
CC != RF
CC != GAP
```

A Root Finding may motivate one or more Behavior Contracts. A Behavior Contract may support multiple assurance targets and downstream scenarios.

## 6. Behavior Contract (`BC-*`)

### 6.1 Definition

One `BC-*` expresses one independently verifiable material behavior.

Bad:

```text
BC-001
Order processing works correctly including auth, validation,
payment retries, persistence, and events.
```

Preferred:

```text
BC-001
Unauthenticated POST /orders is rejected.

BC-002
A payment timeout does not create a duplicate order.

BC-003
A successful retry can transition the same order to COMPLETED.

BC-004
Exactly one completion event is emitted for an order.
```

A single test may prove several BCs, and one BC may require evidence at more than one boundary.

### 6.2 Conceptual record

```text
BC-042

name:
  payment timeout does not duplicate order

kind:
  failure-recovery

materiality:
  persistent-state

scope:
  order creation / payment execution

preconditions:
  authenticated request
  valid order
  payment provider reachable but timing out

stimulus:
  POST /orders

expected_behavior:
  one durable order identity exists
  retry does not create a second order

state_constraints:
  at most one authoritative order record

side_effect_constraints:
  no duplicate payment initiation caused by order duplication

sources:
  RF-012
  OpenAPI POST /orders
  src/orders/handler.py
  checkout-ui consumer path

contract_views:
  declared: ...
  implemented: ...
  consumed: ...

contract_conflicts:
  CC-017

baseline_bindings:
  service: <commit>
  consumer: <commit when applicable>
```

Existing test evidence is deliberately not owned by the BC. Test evidence belongs to `TM-*`; otherwise changing tests would mutate the product semantic contract.

### 6.3 Writer ownership

The Behavior Model gate is the single writer of accepted `BC-*` semantics.

Other gates may emit:

```text
BC_CANDIDATE
BC_REVALIDATION_REQUEST
BC_CONFLICT_OBSERVED
```

but they do not directly rewrite accepted Behavior Contracts.

Examples:

- Test Assurance may discover a material behavior and emit `BC_CANDIDATE`;
- Contract Verification may observe drift and request revalidation;
- Service Simulator Design may discover a missing scenario contract;
- E2E Design may discover cross-component behavior that needs explicit modeling.

Only the Behavior Model gate accepts, revises, rejects, or supersedes a BC.

## 7. Behavior Contract lifecycle, freshness, and authority

Do not collapse lifecycle, freshness, and authority into one large enum.

### 7.1 Semantic lifecycle

```text
status:
  CANDIDATE
  UNDER_REVIEW
  ACCEPTED
  SUPERSEDED
  REJECTED
```

### 7.2 Freshness

```text
freshness:
  VALID
  REVALIDATION_REQUIRED
  UNKNOWN
```

### 7.3 Authority

```text
authority:
  RESOLVED
  UNRESOLVED
```

An accepted BC may therefore be semantically accepted while requiring freshness revalidation:

```text
status: ACCEPTED
freshness: REVALIDATION_REQUIRED
authority: RESOLVED
```

Downstream technical use requires an accepted BC whose required dependency slice is fresh and whose authority is sufficiently resolved for the requested decision.

### 7.4 Revisions and supersession

Preserve BC identity when semantic identity remains the same:

```text
BC-042@rev1
BC-042@rev2
BC-042@rev3
```

If the behavior changes enough to become a different semantic contract:

```text
BC-042
status: SUPERSEDED
superseded_by: BC-091
```

Downstream artifacts should bind to the accepted revision used, for example:

```text
derived_from: BC-042@rev3
```

## 8. Contract representations

Do not treat contract source classes as competing automatic authorities.

The model distinguishes four observable representations:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

Examples:

- `DECLARED` — OpenAPI, protobuf, AsyncAPI, accepted documentation;
- `IMPLEMENTED` — actual route/handler/serializer/auth/error behavior;
- `CONSUMED` — behavior real clients demonstrably depend on;
- `TESTED` — behavior encoded or asserted by executable tests.

These are views of behavior, not a precedence order.

Authority resolution is tracked separately, for example:

```text
authority_resolution:
  ACCEPTED_DECLARED
  ACCEPTED_IMPLEMENTED
  ACCEPTED_COMPATIBILITY_BEHAVIOR
  AUTHORITY_UNRESOLVED
```

Swagger/OpenAPI is therefore not automatically true merely because it is declared, and code is not automatically normative merely because it currently executes.

## 9. Contract Verification and `CC-*`

### 9.1 Required comparison

When materially applicable, Contract Verification compares at least:

- HTTP method and path;
- request schema;
- required/optional fields;
- types;
- nullable/default behavior;
- enum values;
- status codes;
- response schema;
- headers;
- authentication/authorization contract;
- error body/schema;
- pagination/versioning;
- event/message schema.

Where contract sources express behavioral semantics, also compare relevant:

- state transitions;
- side effects;
- ordering;
- idempotency;
- retry/cancellation behavior.

OpenAPI comparison is therefore part of Contract Verification, not the whole Behavior Model.

### 9.2 Contract Consistency Record

Example:

```text
CC-017

subject:
  POST /orders duplicate-order response

related_behavior:
  BC-044

DECLARED:
  OpenAPI: 201, 400

IMPLEMENTED:
  code: 201, 400, 409 DuplicateOrder

CONSUMED:
  checkout-ui handles 409 DuplicateOrder

TESTED:
  integration tests cover 201 and 400

status:
  OPEN

classification:
  AUTHORITY_UNRESOLVED
```

### 9.3 Classification

A CC may later be classified as one of the following, when evidence supports it:

```text
DECLARATION_STALE
IMPLEMENTATION_DEFECT
CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR
TEST_ENCODES_STALE_CONTRACT
INTENTIONAL_COMPATIBILITY_BEHAVIOR
CONTRACT_UNRESOLVED
```

Do not select a winner automatically when declared, implemented, consumed, and tested views conflict.

### 9.4 CC lifecycle

```text
status:
  OPEN
  CLASSIFIED
  RESOLVED
  WONT_RESOLVE
  SUPERSEDED

freshness:
  VALID
  REVALIDATION_REQUIRED
  UNKNOWN
```

Contract Verification is the owner/writer of `CC-*`. Other gates may emit `CONTRACT_CONFLICT_OBSERVED` but do not directly reclassify accepted consistency records.

### 9.5 CC resolution does not silently rewrite BC

Resolving a CC triggers BC impact analysis.

```text
CC resolved
    |
    v
BC impact analysis
    |
    +-- no semantic change -> BC remains valid
    |
    +-- semantic impact -> BC freshness = REVALIDATION_REQUIRED
```

A projection or Contract Verification gate does not rewrite accepted BC semantics to match its preferred interpretation.

## 10. Contract drift and assurance gaps are orthogonal

A Contract Consistency problem is not automatically a Test Assurance gap.

Example:

```text
CC-017
Swagger omits 409, but implementation and consumer behavior are well tested.
```

This can be a contract-governance/documentation problem without a `GAP-*`.

If the behavior is also inadequately evidenced:

```text
CC-017
   |
   +-- BC-044
          |
          +-- MAT-031
                 |
                 +-- GAP-012
```

Normative invariant:

> Contract drift and assurance gaps are independent axes and must not be collapsed into one finding type.

## 11. Relationship among `RF/BC/MAT/TM/GAP/TASK`

Example:

```text
RF-012
Stale generation can overwrite terminal state
        |
        +-- BC-027
        |     Only current generation may publish terminal state
        |
        +-- BC-028
        |     Superseded generation completion must not mutate authoritative state
        |
        +-- BC-029
              Cancellation/retry must not transfer publication ownership
```

Test Assurance may then create material assurance targets:

```text
MAT-021 -> BC-027
MAT-022 -> BC-028
MAT-023 -> BC-029
```

Evidence mapping remains separate:

```text
BC-027 / MAT-021
      |
      +-- TM-017 existing integration test
      +-- TM-018 executable probe
      +-- GAP-009 stale-generation branch not proven
```

Accepted gaps may create remediation tasks:

```text
GAP-009 -> TASK-014
```

## 12. Test dependency strategies

For every material dependency of the reviewed service, Test Environment Design selects an explicit strategy.

Initial vocabulary:

- `REAL_DISPOSABLE` — real isolated instance, commonly containerized;
- `SERVICE_EMULATOR` — compatible external emulator/fake service;
- `CONTROLLABLE_MOCK` — programmable external service mock;
- `IN_PROCESS_DOUBLE` — in-process fake/stub/mock at a narrow boundary;
- `TEMP_RESOURCE` — temporary filesystem/database/resource where appropriate;
- `NOT_REQUIRED` — dependency is outside the selected test boundary.

Example:

```text
PostgreSQL
  strategy: REAL_DISPOSABLE
  reason: transaction, constraint, and persistence semantics are material

Redis
  strategy: REAL_DISPOSABLE
  reason: expiry/atomic behavior is material

Clock
  strategy: IN_PROCESS_DOUBLE
  reason: deterministic time control

Payment API
  strategy: CONTROLLABLE_MOCK
  reason: external uncertainty and failure injection are required
```

Key rule:

> Mock external uncertainty, not the behavior under test.

The capability should actively avoid replacing core business logic with mocks merely because mocking is convenient.

## 13. Service Simulator

The simulation of the reviewed service is called the Service Simulator because it may require state, lifecycle, scenarios, faults, and events rather than fixed request/response stubs.

Conceptual structure:

```text
Service Simulator
|
+-- Contract API
+-- State Store
+-- Scenario Engine
+-- Fault Injection
+-- Event Emitter
+-- Control API
+-- Health / Reset / Seed
```

### 13.1 Consumer plane

Consumers interact with the same relevant protocol surface they would use with the real service:

- HTTP;
- gRPC;
- WebSocket;
- events/messages;
- another protocol when justified by the real service.

Test-control concepts must not leak into the normal consumer contract unless the real service itself exposes them.

### 13.2 Control plane

The simulator has a separate test-only control plane.

Illustrative endpoints:

```text
/__test/health
/__test/reset
/__test/scenario
/__test/state
/__test/seed
```

Exact shape is implementation-specific and belongs to the accepted simulator specification.

### 13.3 Scenario Engine

Simulator scenarios derive from accepted Behavior Contracts and may include:

- normal success;
- rejected request;
- timeout;
- delayed response;
- transient 500 then success;
- permanent failure;
- duplicate event;
- out-of-order event;
- rate limit;
- partial response when materially relevant and evidenced.

Example provenance:

```text
scenario: PAYMENT_TIMEOUT_THEN_SUCCESS

derived_from:
  BC-042@rev3

contract_view:
  DECLARED + IMPLEMENTED

consumer_relevance:
  checkout-ui
  order-worker

purpose:
  retry/recovery verification
```

A Service Simulator must not be generated blindly from Swagger. Contract Verification and accepted Behavior Contracts mediate declared, implemented, and consumed differences.

## 14. E2E design

An E2E candidate exists when assurance depends on multiple real components and cannot be adequately proven at a smaller boundary.

Example:

```text
BC-042 Payment timeout recovery

Topology:
  Browser
    -> real Frontend
    -> real Order Service
    -> real PostgreSQL

  Order Service
    -> Payment Simulator
       timeout -> success

Expected outcome:
  no duplicate order
  bounded retry occurs
  order reaches COMPLETED
  UI reaches success state
```

E2E Design states:

- source Behavior Contract revision;
- participating real components;
- allowed simulators/fakes;
- initial state;
- stimulus;
- material assertions;
- failure observability;
- cleanup/reset requirements;
- CI suitability;
- estimated execution cost where useful.

Prefer smaller tests when they prove the same contract more reliably and cheaply.

E2E Design does not require Service Simulator Design when the selected topology needs no simulator.

## 15. Capability menu

User-selectable outputs:

```text
Test Engineering

[x] Test Assurance
[ ] Test Plan
[ ] Contract Consistency Report
[ ] Test Environment Design
[ ] Service Simulator Design
[ ] Service Simulator Implementation Plan
[ ] E2E Test Plan
```

`Behavior Model` is not a checkbox. It is an internal dependency automatically executed when an extended capability requires accepted BC semantics.

`Contract Verification` is also not a checkbox. It is an internal automatic gate when a materially relevant declared contract exists.

`Contract Consistency Report` is only the optional human-readable projection of Contract Verification results.

The Skill may recommend additional outputs but must not silently enable substantial additional work.

## 16. Capability dependency DAG

The capability structure is a dependency DAG, not a fixed linear pipeline.

```text
Test Assurance
    |
    +-- Test Plan
    |
    +-- Behavior Model [internal when needed]
           |
           +-- Contract Verification [automatic when applicable]
           |
           +-- Test Environment Design
           |
           +-- Service Simulator Design
           |       |
           |       +-- Service Simulator Implementation Plan
           |
           +-- E2E Test Plan
```

Important rules:

- execute only the minimum dependency slice required by selected outputs;
- Test Plan does not automatically require every extended Test Engineering output;
- E2E does not automatically require a Service Simulator;
- Service Simulator Implementation Plan requires an accepted/fresh Service Simulator specification;
- independent downstream capabilities may reuse the same accepted BC set.

## 17. Artifact structure and backward compatibility

Preserve existing numbered compatibility outputs:

```text
test-review/
|
+-- 00-test-assurance-summary.md
+-- 01-test-assurance-map.md
+-- 02-test-plan.md                              # optional, existing compatibility
+-- 03-behavior-contract-model.md                # generated when extended behavior model is required
+-- 04-contract-consistency-report.md            # optional user-facing projection
+-- 05-test-environment-design.md                 # optional
+-- 06-service-simulator-spec.md                  # optional
+-- 07-service-simulator-implementation-plan.md   # optional
+-- 08-e2e-test-plan.md                           # optional
+-- working/
    +-- INDEX.md
    +-- behavior-contracts.md                     # authoritative BC ledger
    +-- contract-verification.md                  # authoritative CC ledger
    +-- test-mappings.md
    +-- assurance-gaps.md
    +-- ...
```

Dependency order does not need to match file numbering. Compatibility of the existing `00/01/02` names is preferred over renumbering them.

Authoritative technical ledgers live in `working/`. Human-readable files are projections and do not become new product-behavior authority merely because they are generated later.

Distinguish these output states:

```text
NOT_APPLICABLE
NOT_VERIFIED
VERIFIED_NO_MATERIAL_ISSUES
```

For example, a requested Contract Consistency Report may report `NOT_APPLICABLE` when no materially relevant declared contract exists, which is not equivalent to failure to verify.

## 18. Session and reuse semantics

The umbrella session model remains applicable.

### 18.1 `NEW`

The user selects desired outputs. The Skill automatically adds only the internal dependencies required for those outputs.

Example:

```text
Selected:
  E2E Test Plan

Implicit:
  Test Assurance
  Behavior Model
  Contract Verification if applicable
```

Do not automatically add Service Simulator Design unless the selected E2E topology requires or explicitly requests it.

### 18.2 `RESUME`

Continue from accepted current artifacts and the first unfinished valid gate. Reuse accepted upstream artifacts whose freshness and authority bindings remain valid.

### 18.3 `USE_EXISTING`

Allowed only when the entire dependency slice for the requested output is:

```text
accepted
+ freshness VALID
+ authority sufficiently RESOLVED
```

If a source BC is `REVALIDATION_REQUIRED`, reuse of a dependent Simulator/E2E/Test Engineering output is rejected until the affected dependency slice is revalidated.

### 18.4 `EXTEND`

Add a new output later without replaying accepted upstream work unnecessarily.

Examples:

```text
accepted Test Review -> add Test Environment Design
accepted Test Review -> add Service Simulator Design
accepted Simulator Spec -> add Implementation Plan
accepted Test Review -> add E2E Design
```

Create or reuse only the minimum accepted dependency slice required by the added endpoint.

### 18.5 `REVALIDATE`

Revalidation is impact-driven rather than whole-package replay.

Potential change classes include:

```text
implementation changed
OpenAPI/declared contract changed
tests changed
consumer changed
dependency topology changed
```

Examples:

#### Declared contract changed

```text
OpenAPI changed
    -> affected CC-* revalidation
    -> affected BC-* impact analysis
    -> affected MAT/TM/GAP if semantics changed
    -> affected Test Plan/Simulator/E2E scenarios
```

#### Tests changed

```text
tests changed
    -> TM-* revalidation
    -> MAT assurance verdict may change
    -> GAP may close/open
```

Test evidence drift does not automatically imply Behavior Contract drift.

#### Implementation changed

```text
implementation changed
    -> IMPLEMENTED view impact
    -> Contract Verification when relevant
    -> BC impact analysis
```

A file-level diff alone does not prove semantic impact. Use conservative change-impact analysis.

#### Consumer changed

```text
service unchanged
consumer changed
    -> CONSUMED view impact
    -> CC-* may change
    -> consumer-facing simulator scenarios may require revalidation
```

Multi-repository source bindings are first-class freshness inputs.

### 18.6 `PROJECTION_REPAIR`

May repair:

- wording;
- formatting;
- tables;
- Mermaid;
- cross-links;
- human-readable structure.

It must not change:

- BC semantics;
- CC classification;
- MAT accounting;
- TM verdict;
- GAP existence;
- TASK semantic priority;
- simulator scenario behavior;
- E2E topology semantics.

If such meaning must change, return `TECHNICAL_REVALIDATION_REQUIRED`.

## 19. Freshness bindings

A BC or CC may depend on more than one repository revision.

Example BC bindings:

```text
BC-042

baseline_bindings:
  service_repo: abc123
  architecture_authority: RF-012@rev4
  declared_contract: openapi.yaml@abc123
  implementation: src/orders/handler.py@abc123
  consumer_repo: checkout-ui@def789
```

Example CC bindings:

```text
CC-017

compared_views:
  declared: openapi.yaml@abc123
  implemented: handler.py@abc123
  consumed: checkout-ui@def789
  tested: test_orders.py@abc123
```

A consumer change can therefore require contract/simulator revalidation even when the service repository has not changed.

## 20. Authority and provenance

Downstream outputs identify the accepted technical authority they rely on.

Examples:

- Test Plan references BC and MAT/GAP IDs;
- Test Environment Design references tests/scenarios/BCs requiring each dependency strategy;
- Service Simulator scenarios reference accepted BC revisions and relevant contract views;
- E2E scenarios reference BC revisions and selected topology;
- Service Simulator Implementation Plan references an accepted Simulator Spec revision.

No downstream output silently becomes the source of truth for product behavior merely because it was generated later.

## 21. Service Simulator Implementation Plan

The capability may optionally produce a complete implementation plan after the Service Simulator specification has been accepted and is fresh.

The plan may cover:

- repository/project placement;
- language/runtime selection where constrained;
- protocol adapters;
- contract schema reuse/generation;
- state engine;
- scenario engine;
- fault injection;
- reset/seed/control plane;
- event simulation;
- container image;
- healthchecks;
- local compose integration;
- CI job integration;
- deterministic startup/shutdown;
- test data fixtures;
- acceptance tests for the simulator itself;
- contract drift checks against authoritative schemas where feasible.

The architecture-code-review/Test Engineering capability does not automatically implement this plan during review. Code implementation remains a separate explicitly authorized action.

## 22. Non-goals

This capability does not:

- chase line coverage as the primary assurance measure;
- assume every uncovered line needs a test;
- require every dependency to be mocked;
- generate mocks before understanding material behavior;
- replace the behavior under test with mocks and then claim integration assurance;
- treat Swagger/OpenAPI as automatically correct authority;
- treat executing code as automatically normative authority;
- silently convert observed consumer behavior into official contract;
- infer undocumented product behavior without evidence;
- convert every contract drift into a test gap;
- create E2E tests merely because a UI flow exists;
- automatically write simulator production code during review;
- automatically restart unrelated accepted architecture-review gates.

## 23. Normative invariants

1. **Claim scope <= evidence scope.**
2. Existing Test Assurance remains evidence-first.
3. One `BC-*` expresses one independently verifiable material behavior.
4. `BC-*` is a separate reusable semantic layer and does not replace `MAT-*`.
5. Test evidence belongs to `TM-*`, not inside BC semantic authority.
6. Behavior Model is the single writer of accepted BC semantics.
7. Contract Verification is the single writer of `CC-*` classification/state.
8. `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED` are observable views, not automatic precedence levels.
9. Contract conflict does not automatically choose Swagger, code, consumer, or tests as truth.
10. Contract drift and Test Assurance gaps are orthogonal.
11. CC resolution does not silently rewrite accepted BC semantics.
12. Test Plan, simulator scenarios, and E2E scenarios derive from the same accepted bounded behavior model.
13. Contract Verification runs automatically when a materially relevant declared contract exists.
14. Contract Consistency Report remains an optional projection.
15. Test dependency substitution strategy is selected per dependency; mocking is not the default.
16. The behavior under test must not be mocked away.
17. Service Simulator has a consumer plane and a separate test-control plane.
18. Service Simulator must not be generated blindly from Swagger.
19. Service Simulator implementation requires a separately accepted/fresh specification and explicit implementation authorization.
20. E2E is used only where multi-component assurance adds material value.
21. E2E does not require a simulator when the selected topology does not need one.
22. Capabilities form a dependency DAG, not a fixed linear pipeline.
23. `EXTEND` reuses accepted upstream work and executes the minimum required dependency slice.
24. `REVALIDATE` is impact-driven rather than whole-package replay.
25. Test changes do not automatically invalidate product Behavior Contracts.
26. Consumer changes may invalidate consumer-facing contract/simulator state even when the service repo is unchanged.
27. `USE_EXISTING` is allowed only for a fresh, accepted, sufficiently resolved dependency slice.
28. Projection repair never mutates technical semantic authority.
29. Existing `00/01/02` user-facing filenames remain compatible.
30. `NOT_APPLICABLE`, `NOT_VERIFIED`, and `VERIFIED_NO_MATERIAL_ISSUES` remain distinct states.

## 24. Remaining implementation-planning questions

The following are implementation details rather than unresolved architecture decisions:

1. Exact stored configuration schema for selected outputs and implicit gates.
2. Exact file syntax/schema used inside authoritative `working/behavior-contracts.md` and `working/contract-verification.md`.
3. Exact impact-analysis heuristics for changed files, generated schemas, shared types, router registration, and cross-repository consumers.
4. Which fail-first pressure scenarios are required to prove the new Test Engineering behavior.
5. Whether Service Simulator implementation code lives in the analyzed repository, a sibling repository, or another explicitly selected destination.
6. Exact terminology for localized user-facing prose while preserving formal internal tokens.
7. Whether `FAKE` needs a distinct formal dependency-strategy token beyond `SERVICE_EMULATOR` / `IN_PROCESS_DOUBLE`, based on implementation pressure tests.

## 25. Expected next step

The design is approved for implementation planning.

Next:

1. create a detailed implementation plan;
2. define fail-first pressure scenarios for BC/CC ownership, contract drift, DAG execution, freshness, and revalidation behavior;
3. update the Test Review/Test Engineering capability contract only after the pressure-test baseline is established;
4. add orchestration/configuration rules;
5. update README examples and output structure;
6. validate static contract behavior and available runtime canaries without overstating unsupported runtime claims.
