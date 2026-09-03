# Test Engineering Capability Design

Date: 2026-09-03
Status: DESIGN DRAFT FOR REVIEW
Repository: `todkavodka/architecture-code-review`

## 1. Purpose

Extend the existing Test Review capability into a broader Test Engineering capability without weakening the existing evidence-first review model.

The capability should help answer, in order:

1. What tests already exist?
2. What behavior do they actually prove?
3. Which important behavior remains unproven or only partially proven?
4. Which additional tests should be created, and at what test boundary?
5. What environment or controlled substitutes are required to run those tests reliably?
6. How should the reviewed service itself be simulated so that its consumers can test against it without running the real service?
7. Which multi-component scenarios are valuable enough to become E2E tests?
8. If a Service Simulator is desired, what implementation plan is required to build and integrate it safely?

This design deliberately separates review, behavioral modeling, test design, environment design, simulator design, and E2E design. The Skill may design and plan these outputs, but does not automatically implement a simulator or test infrastructure during an architecture review.

## 2. Existing foundation that remains valid

The current Test Review behavior remains the assurance layer.

It already aims to determine:

- what material contracts have executable evidence;
- where coverage is partial or absent;
- where tests may provide false confidence;
- what important verification gaps remain;
- what should be fixed first.

The existing user-facing output remains:

- `00-test-assurance-summary.md` — concise human decision summary;
- `01-test-assurance-map.md` — detailed evidence map;
- optional test plan output.

The new capability must build on accepted Test Review evidence rather than silently replacing or reinterpreting it.

## 3. Core architectural principle

One bounded model of material system behavior should be the shared source for downstream test design.

Conceptually:

```text
accepted architecture / observed implementation / declared contracts / consumers
                              |
                              v
                     Behavior Contract Model
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
     Test Design       Test Environment     Service Simulator
          |                   Design                Design
          +-------------------+-------------------+
                              |
                              v
                           E2E Design
```

Test Plan, Service Simulator scenarios, and E2E scenarios must not independently invent conflicting models of the product.

## 4. Test Engineering layers

The proposed capability consists of six logical layers.

### 4.1 Test Assurance

Purpose:

- inspect the existing test system;
- determine freshness and relevance;
- map executable evidence to material contracts;
- identify false-confidence patterns;
- identify gaps.

Primary outputs:

- Test Assurance Summary;
- Test Assurance Map.

This is the existing Test Review core and remains evidence-first.

### 4.2 Behavior Model

Purpose:

Reconstruct a bounded set of material behaviors that are relevant to testing.

The model must be based on evidence such as:

- accepted As-Built architecture;
- real code paths;
- state transitions;
- public protocols;
- schema definitions;
- external side effects;
- existing tests;
- declared API/event contracts;
- observed consumer behavior.

This is not a second architecture model. It is a test-oriented projection of material behavior.

### 4.3 Test Design

Purpose:

For each material behavior that is inadequately evidenced, recommend the smallest useful test boundary capable of proving it.

Possible test classes include:

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

### 4.4 Test Environment Design

Purpose:

Determine what the reviewed service needs around it to execute meaningful and deterministic tests.

This layer covers dependencies of the reviewed service.

Examples:

- PostgreSQL;
- Redis;
- Kafka/NATS/RabbitMQ;
- S3/object storage;
- OAuth provider;
- SMTP;
- external HTTP APIs;
- filesystem;
- clock/time source;
- DNS or network boundary where materially relevant.

The capability must not assume that every dependency should be mocked.

### 4.5 Service Simulator Design

Purpose:

Design a controllable simulation of the reviewed service itself so that its consumers can execute development, integration, CI/CD, and E2E tests without running the real service.

This is distinct from substitutes used by the reviewed service's own tests.

### 4.6 E2E Design

Purpose:

Identify scenarios whose assurance value depends on multiple real components interacting across material boundaries.

E2E design must be derived from the Behavior Contract Model rather than from generic UI happy paths.

## 5. Behavior Contract

The central reusable unit is a Behavior Contract.

A Behavior Contract should be bounded and traceable.

Example conceptual shape:

```text
BC-004
name: payment timeout recovery

kind:
  lifecycle / failure-recovery

entrypoints:
  POST /orders

preconditions:
  authenticated user
  valid order

expected_behavior:
  payment timeout does not create a duplicate order
  retry is bounded according to accepted behavior
  successful retry reaches COMPLETED

state_transitions:
  CREATED -> PROCESSING -> COMPLETED

side_effects:
  payment request
  order event

existing_test_evidence:
  happy path: ADEQUATE
  timeout: NOT_EVIDENCED
  retry: NOT_EVIDENCED

contract_sources:
  declared API
  observed implementation
  consumer dependency
```

A Behavior Contract is not accepted merely because it looks plausible. Its scope must not exceed investigated evidence.

## 6. Contract model for the Service Simulator

The Service Simulator must distinguish at least two classes of consumer-facing contract.

### 6.1 `DECLARED_CONTRACT`

Behavior explicitly promised by the service through accepted authoritative sources such as:

- OpenAPI;
- protobuf/gRPC definitions;
- AsyncAPI/event schemas;
- documented status codes;
- documented headers;
- documented state transitions;
- other accepted interface specifications.

### 6.2 `OBSERVED_CONSUMER_CONTRACT`

Behavior that real consumers demonstrably depend on even though it is not part of the declared contract.

Sources may include:

- frontend code;
- other services;
- CLI clients;
- integration adapters;
- existing consumer tests.

Observed consumer behavior must never be silently promoted into the declared contract.

### 6.3 Contract drift

When declared and observed behavior differ, record the mismatch explicitly.

Example:

```text
SC-017

Declared:
  409 is not part of the public API contract

Observed:
  Web UI handles 409 as ACCOUNT_MIGRATING

Classification:
  OBSERVED_CONSUMER_CONTRACT

Drift:
  DECLARED_CONTRACT_MISMATCH
```

The simulator may support the observed scenario when useful, but provenance must remain visible.

## 7. Test dependency strategies

For every material dependency of the reviewed service, Test Environment Design should select an explicit strategy.

Initial strategy vocabulary:

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
  reason: external network dependency and failure injection are required
```

Key rule:

> Mock external uncertainty, not the behavior under test.

The capability should actively avoid replacing core business logic with mocks merely because mocking is convenient.

## 8. Service Simulator

The mock of the reviewed service is called the Service Simulator in this design because it may need state, lifecycle, scenarios, faults, and events rather than only fixed request/response stubs.

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

### 8.1 Consumer API

Consumers interact with the same relevant protocol surface they would use with the real service:

- HTTP;
- gRPC;
- WebSocket;
- events/messages;
- another protocol when justified by the real service.

The simulator should not expose test-control concepts through the normal consumer contract unless the real service does so.

### 8.2 Control plane

The simulator should have a separate test-only control plane.

Illustrative endpoints:

```text
/__test/health
/__test/reset
/__test/scenario
/__test/state
/__test/seed
```

The exact shape is implementation-specific and must be defined by the simulator specification, not assumed universally.

### 8.3 Scenario Engine

The simulator should support normal and failure/edge scenarios derived from accepted Behavior Contracts.

Examples:

- normal success;
- rejected request;
- timeout;
- delayed response;
- transient 500 then success;
- permanent failure;
- duplicate event;
- out-of-order event;
- rate limit;
- partial response when that behavior is relevant and evidenced.

A scenario should carry provenance such as:

```text
scenario: PAYMENT_TIMEOUT_THEN_SUCCESS

derived_from:
  BC-042

contract_class:
  DECLARED_CONTRACT

consumer_relevance:
  checkout-ui
  order-worker

purpose:
  retry/recovery verification
```

## 9. E2E design

An E2E candidate should exist when assurance depends on multiple real components and the behavior cannot be adequately proven at a smaller boundary.

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

E2E Design must state:

- source Behavior Contract;
- participating real components;
- allowed simulators/fakes;
- initial state;
- stimulus;
- material assertions;
- failure observability;
- cleanup/reset requirements;
- CI suitability;
- estimated execution cost where useful.

The capability should prefer smaller tests when they prove the same contract more reliably and cheaply.

## 10. Proposed outputs

Names and numbering remain provisional until implementation design is reviewed, but the conceptual package is:

```text
test-review/
|
+-- test-assurance-summary.md
+-- test-assurance-map.md
+-- behavior-test-model.md
+-- test-plan.md
+-- test-environment-strategy.md
+-- service-simulator-spec.md
+-- service-simulator-implementation-plan.md   # optional
+-- e2e-test-plan.md
```

The final implementation may preserve the existing numbered filenames for compatibility and add new files around them.

## 11. Configuration model

Do not turn Test Engineering outputs into one long mutually-exclusive level such as `REVIEW_PLUS_E2E_PLUS_SIMULATOR`.

Prefer explicit output selection.

Conceptually:

```text
Test Review / Test Engineering

[required when enabled] Test Assurance
[ ] Test Plan
[ ] Test Environment Design
[ ] Service Simulator Design
[ ] Service Simulator Implementation Plan
[ ] E2E Test Plan
```

Dependencies:

```text
Test Assurance
      |
      +-- Behavior Model
             |
             +-- Test Plan
             +-- Test Environment Design
             +-- Service Simulator Design
             |       |
             |       +-- Service Simulator Implementation Plan
             |
             +-- E2E Test Plan
```

The UI/interaction may simplify this, but stored configuration must make selected outputs explicit.

The Skill may recommend outputs after inspecting the project, but must not silently enable substantial additional work.

## 12. Freshness and reuse

The existing umbrella session model remains applicable.

### `NEW`

A new Test Engineering package may select the desired outputs during configuration.

### `RESUME`

Continue from accepted current artifacts and the first unfinished valid gate.

### `USE_EXISTING`

Reuse accepted current Test Engineering results without recomputing technical analysis.

### `REVALIDATE`

When the project changed, use change-impact analysis to determine which Behavior Contracts, evidence, dependency strategies, simulator scenarios, and E2E scenarios are affected.

Do not automatically regenerate the whole Test Engineering package.

### `EXTEND`

A common use case is adding a new Test Engineering output later, for example:

- accepted Test Review -> add Test Environment Design;
- accepted Test Review -> add Service Simulator Design;
- accepted Service Simulator Design -> add implementation plan;
- accepted Test Review -> add E2E Design.

Reuse only the minimum accepted dependency slice needed by the added endpoint.

### `PROJECTION_REPAIR`

May repair final Test Engineering documents without changing accepted technical semantics. Semantic changes still require the appropriate technical revalidation.

## 13. Authority and provenance

Downstream outputs must identify which accepted artifacts and evidence they rely on.

Examples:

- Test Plan references Behavior Contract IDs;
- Test Environment Strategy references the tests/behaviors requiring each dependency;
- Service Simulator scenarios reference Behavior Contract IDs and contract class;
- E2E scenarios reference Behavior Contract IDs and selected topology;
- implementation plan references an accepted Service Simulator specification revision.

No output should silently become a new source of truth for product behavior merely because it was generated later.

## 14. Service Simulator Implementation Plan

The capability may optionally produce a complete implementation plan after the Service Simulator specification has been accepted.

The plan may cover:

- project/repository placement;
- language/runtime selection when constrained by the host project;
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

The architecture-code-review Skill must not automatically implement this plan during review. Code implementation remains a separate explicitly authorized action.

## 15. Non-goals

This capability does not:

- chase line coverage as the primary measure of assurance;
- assume every uncovered line needs a test;
- require every dependency to be mocked;
- generate mocks before understanding material behavior;
- replace the system under test with mocks and then claim integration assurance;
- silently convert observed consumer behavior into official contract;
- infer undocumented product behavior without evidence;
- create E2E tests merely because a UI flow exists;
- automatically write simulator production code during review;
- automatically restart unrelated accepted architecture-review gates.

## 16. Key invariants

1. **Claim scope <= evidence scope.**
2. Existing Test Assurance remains evidence-first.
3. Behavior Contracts are traceable to accepted evidence.
4. Test Plan, simulator scenarios, and E2E scenarios derive from the same bounded behavior model.
5. `DECLARED_CONTRACT` and `OBSERVED_CONSUMER_CONTRACT` remain distinct.
6. Contract drift is surfaced, not normalized away.
7. Test dependency substitution strategy is chosen per dependency; mocking is not the default.
8. The behavior under test should not be mocked away.
9. Service Simulator has a consumer plane and a separate test-control plane.
10. Service Simulator implementation requires a separately accepted specification and explicit implementation authorization.
11. E2E is used only where multi-component assurance adds material value.
12. Existing accepted evidence is reused only while its revision/freshness binding remains valid.

## 17. Open implementation questions

The following questions are intentionally deferred to the implementation planning stage unless design review changes them:

1. Exact artifact numbering and backward compatibility with current `00/01/02` Test Review files.
2. Whether `Behavior Contract` IDs should be `BC-*` or reuse/extend an existing Test Review identifier family.
3. Exact stored configuration schema for output selection.
4. Which new pressure scenarios are required for Test Engineering behavior.
5. Whether Service Simulator Design should live entirely inside `capabilities/test-review/` or become a nested capability module while remaining under Test Engineering ownership.
6. Exact terminology for user-facing Russian prose versus formal internal tokens.
7. Whether E2E Design should be selectable without Service Simulator Design when no simulator is required. The expected answer is yes, but implementation must preserve dependency correctness.
8. Whether Test Environment Design should distinguish `FAKE` and `SERVICE_EMULATOR` as separate formal strategies or treat fake as a broader implementation category.

## 18. Expected next step

After design review and approval:

1. create an implementation plan;
2. add fail-first pressure scenarios for the new behavior;
3. update the Test Review/Test Engineering capability contract;
4. add orchestration/configuration rules;
5. update README examples and output structure;
6. run static contract validation and any available runtime canary without overstating unsupported runtime claims.
