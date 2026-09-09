# Test Engineering semantic contract

This reference extends Test Review's evidence-first Test Assurance layer. It
defines reusable behavior semantics and downstream test-engineering designs; it
does not implement tests, a Service Simulator, or production code.

## Behavior Contract Model

The Behavior Model reconstructs a bounded set of material behaviors from
accepted architecture, observed implementation, declared contracts, real
consumers, and relevant tests. One `BC-*` is one independently verifiable
material behavior. It is not a finding, assurance target, gap, task, or test
result.

```text
BC-*   independently verifiable behavior
RF-*   architecture/root finding
MAT-*  material assurance target
TM-*   executable evidence mapping
GAP-*  missing, partial, misleading, or inadequate evidence
TASK-* remediation work
WS-*   temporary working/investigation state
```

The accepted behavior model is the single semantic source for Test Plan,
Contract Verification, Service Simulator scenarios, and E2E scenarios. Existing
tests are observations mapped by `TM-*`; executable-evidence verdicts do not
belong inside a `BC-*` record.

## Contract Verification

When a materially relevant declared external contract exists, Contract
Verification is an internal automatic gate. It compares method/path, request and
response schemas, required fields, types, nullable/default and enum behavior,
status codes, headers, auth, errors, pagination/versioning, and material state,
side-effect, ordering, idempotency, retry, or cancellation semantics.

The four observable views are:

```text
DECLARED      OpenAPI/Swagger, protobuf, AsyncAPI, accepted documentation
IMPLEMENTED   routes, handlers, serializers, auth, errors, side effects
CONSUMED      behavior real clients, SDKs, CLIs, or peer services depend on
TESTED        behavior encoded or asserted by executable tests
```

These are views, not a precedence order. Swagger/OpenAPI, code, consumers, and
tests do not automatically win a conflict merely because they are declared,
executable, recent, or machine-readable.

## Contract Consistency Record

Contract Verification owns and writes `CC-*`. A record preserves the compared
views, relevant `BC-*`, revisions, mismatch, and adjudication state. Other gates
may emit `CONTRACT_CONFLICT_OBSERVED`, but do not rewrite accepted consistency
records.

```text
status: OPEN | CLASSIFIED | RESOLVED | WONT_RESOLVE | SUPERSEDED
freshness: VALID | REVALIDATION_REQUIRED | UNKNOWN
classification:
  AUTHORITY_UNRESOLVED
  DECLARATION_STALE
  IMPLEMENTATION_DEFECT
  CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR
  TEST_ENCODES_STALE_CONTRACT
  INTENTIONAL_COMPATIBILITY_BEHAVIOR
  CONTRACT_UNRESOLVED
```

Resolving a `CC-*` triggers impact analysis of related behavior; it never
silently rewrites an accepted `BC-*`.

## Stage F compatibility boundary

Stage F compatibility is a normalized catalog-facing view over the existing
Contract Verification and `CC-*` authority. It does not create a new
compatibility identity, result ledger, engine, or Product semantic family.
`CC-*` remains the sole owner of comparison status, classification,
adjudication, lifecycle, and historical meaning.

### Exact comparison inputs

When the existing Contract Verification applicability rule is met, the exact
comparison pair and its qualified inputs are recorded or referenced without
fabrication:

```text
provider_if_ref: IF-*@accepted_revision
consumer_if_ref: IF-*@accepted_revision
provider_project/repository/revision/baseline
consumer_project/repository/revision/baseline
protocol/interface_kind
operation_identity
safe_address/path/endpoint identity when material
contract/API version
schema/contract reference or fingerprint when applicable
auth references when material
error references when material
supporting WS-*/EV-* evidence/provenance references
bounded missing/unresolved limitations
```

The provider and consumer IFs remain independently addressable accepted STM
identities. A `CC-*` comparison references both exact IF revisions and their
qualified Project/source bindings; it never aliases, rewrites, or merges the
two IFs. Product identity, membership, or baseline does not replace either
Project/revision qualification.

Similarity of path, method, service name, Product membership, or external
provider name is not sufficient to fabricate a comparison input. Candidate
matching remains a non-authoritative discovery relation with the bounded
states:

```text
MATCH_CANDIDATE
NO_MATCH_ESTABLISHED
MATCHING_INDETERMINATE
```

None of these states is a compatibility result. In particular,
`MATCH_CANDIDATE` does not mean `COMPATIBLE`, `NO_MATCH_ESTABLISHED` does not
mean `INCOMPATIBLE`, and `MATCHING_INDETERMINATE` does not mean
`NOT_COMPARABLE`.

### Normalized catalog-facing result

The normalized Stage F result is derived only from the exact qualified pair
and existing `CC-*` state. It is not stored as a new semantic authority:

```text
normalized_result:
  COMPATIBLE | INCOMPATIBLE | INDETERMINATE | NOT_COMPARABLE
  source_cc_ref: optional CC-*@accepted_revision
  provider_if_ref: exact qualified IF revision
  consumer_if_ref: exact qualified IF revision
```

The mapping is:

| Stage F result | Required existing authority state |
|---|---|
| `COMPATIBLE` | Exact provider/consumer inputs are present; `CC.status = RESOLVED` and `CC.freshness = VALID`; the accepted adjudication explicitly accepts the compared behavior as compatible, including `INTENTIONAL_COMPATIBILITY_BEHAVIOR` where applicable. |
| `INCOMPATIBLE` | Exact provider/consumer inputs are present; `CC.status = RESOLVED` and `CC.freshness = VALID`; the accepted adjudication explicitly accepts a material mismatch using the existing classifications such as `DECLARATION_STALE`, `IMPLEMENTATION_DEFECT`, `CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR`, or `TEST_ENCODES_STALE_CONTRACT`. |
| `INDETERMINATE` | A required input or exact revision is absent/unresolved, comparison evidence is insufficient, or `CC` is non-final (`OPEN`, `CLASSIFIED`, or `WONT_RESOLVE`), stale, revalidation-required, authority-unresolved, or contract-unresolved. |
| `NOT_COMPARABLE` | The accepted records do not form a valid comparison pair under the existing applicability/contract semantics and no `CC-*` comparison exists for that pair. It is not a missing-data or unresolved-CC substitute. |

Missing data never means `COMPATIBLE`. A resolved result for an old provider
or consumer revision does not prove compatibility for a changed current
revision. A current comparison remains `INDETERMINATE` until its exact inputs
and accepted `CC-*` adjudication are established.

When a materially relevant declared external contract exists, the existing
automatic rule remains unchanged:

```text
materially relevant declared external contract
    -> Contract Verification automatic gate
```

The absence of a catalog output does not narrow this gate. If the rule is not
applicable, Test Engineering does not create a `CC-*` result merely for
catalog completeness. A catalog may show only non-authoritative `candidate`,
`not evaluated`, or `not applicable comparison context` information tied to
the exact available inputs. It must not manufacture `COMPATIBLE`,
`INCOMPATIBLE`, or a competing compatibility truth.

### Product and report consumption

Product mode may consume the normalized result only as a derived view over an
exact qualified comparison. The consumed record preserves:

```text
Product ID/revision/baseline
provider Project/revision
consumer Project/revision
provider IF/revision
consumer IF/revision
CC identity/revision/status/classification/adjudication
normalized derived result
```

Product membership and baseline qualification do not grant compatibility,
rewrite Project-local facts, or create a Product compatibility authority. The
Contract Consistency Report remains the existing
`PRJ-TEST-REVIEW-04-CONTRACT-CONSISTENCY-REPORT` projection over current,
non-superseded `CC-*` records and referenced `BC-*` revisions. A catalog or
report may format the same accepted state, but neither may adjudicate it.

Historical `CC-*` identity, revision, status, classification, adjudication,
and meaning remain unchanged. Missing Stage F qualifiers remain absent or
unknown until bounded revalidation creates new accepted state; no old `CC-*`
record is bulk-enriched, retroactively Product-qualified, automatically
re-run, or used to reinterpret a newer IF revision.

## Identifier Relationships

`BC != MAT`, `BC != RF`, `BC != GAP`, and `BC != TM`. A behavior may support
several assurance targets, and one target may have several evidence mappings.
An accepted gap may produce a `TASK-*`, but no identifier is collapsed into
another.

Contract drift and assurance gaps are orthogonal. Fully tested undocumented
compatibility behavior can produce `CC-*` without `GAP-*`; missing evidence for
the same behavior can additionally produce a separate `GAP-*` through
`BC -> MAT -> TM/GAP`.

## Lifecycle / Freshness / Authority

Keep the three axes independent:

```text
status: CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED
freshness: VALID | REVALIDATION_REQUIRED | UNKNOWN
authority: RESOLVED | UNRESOLVED
```

Only the Behavior Model gate accepts, revises, rejects, or supersedes accepted
`BC-*` semantics. Other gates may request revalidation or emit candidates. A
downstream output may reuse a BC only when the required dependency slice is
accepted, fresh, and sufficiently resolved.

## Ownership

Test Review retains ownership of the Test Assurance semantics rendered by its
Summary and Map; the numbered Summary and Map remain human-facing projections.
Behavior Model owns accepted `BC-*`; Contract Verification owns `CC-*`; Test
Assurance owns `MAT-*`, `TM-*`, and `GAP-*` evidence accounting. Those
`BC/CC/MAT/TM/GAP` records are capability semantic authority. Authoritative
ledgers live under the capability's `working/` directory and do not become
product-behavior authority merely by being generated later.

`working/INDEX.md` is coordinator workflow authority for the capability. It is
not a `PRJ-*` artifact and is excluded from projection identity, dependency
snapshots, package membership, fingerprints, drift detection, freshness,
regeneration, retirement, and `RG-*` execution. A generated document or index
does not become a substitute for the accepted `BC-*`, `CC-*`, `MAT-*`, `TM-*`,
or `GAP-*` records it renders.

## Product Test Review scope

Product mode is opt-in. It uses the existing `TRS-*` Test Review Scope family
with `scope_kind: PRODUCT` and a stable Product-keyed scope allocation. The
persisted Product scope binding is:

```text
test_review_scope_id: TRS-<stable Product scope allocation>
scope_kind: PRODUCT
product_id: PROD-*
product_revision: accepted Product revision
product_baseline: immutable Product baseline reference
qualified_projects: [<Project identity + exact source/revision binding> ...]
```

Product `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, and `TASK-*` retain their
existing Test Engineering semantic ownership. A Product record must use the
exact Product `test_review_scope_id` and preserve qualified provider,
consumer, contributor, or other boundary-role Project identities as
applicable, exact source/revision bindings, evidence provenance, lifecycle,
freshness, and dependencies. Local records continue to use their existing
Project/session scope IDs; local and Product selector membership is disjoint,
although a Product scope may reference a local record through an explicit
qualified dependency.

The Product Test Assurance Summary/Map and other selected Product Test Review
outputs are finite projections/packages over accepted records resolved through
the Product `TRS-*` scope. They do not become Behavior Model, Contract
Verification, assurance-gap, or task authority, and they do not select every
record in a member Project. `TASK-*` completion remains independent of `GAP-*`
resolution and evidence state. Test execution, simulator/environment
provisioning, code modification, commit, and publication require their
separate authorization; Product membership grants none of them.

## Stage B Test Review projection contracts

The numbered files in the Output Package are registered as the following
capability-owned projections. The identities are stable even if a repository
chooses a different output directory.

| Projection | Human-readable output | Direct semantic inputs |
|---|---|---|
| `PRJ-TEST-REVIEW-00-ASSURANCE-SUMMARY` | `00-test-assurance-summary.md` | accepted `MAT-*`, `TM-*`, and `GAP-*` accounting in the persisted Test Review scope |
| `PRJ-TEST-REVIEW-01-ASSURANCE-MAP` | `01-test-assurance-map.md` | accepted `MAT-*`, `TM-*`, and `GAP-*` records in the persisted Test Review scope |
| `PRJ-TEST-REVIEW-02-TEST-PLAN` | `02-test-plan.md` | accepted `BC-*`, `MAT-*`, `TM-*`, and `GAP-*` records in the persisted Test Review scope |
| `PRJ-TEST-REVIEW-03-BEHAVIOR-CONTRACT-MODEL` | `03-behavior-contract-model.md` | accepted `BC-*` records |
| `PRJ-TEST-REVIEW-04-CONTRACT-CONSISTENCY-REPORT` | `04-contract-consistency-report.md` | current, non-superseded `CC-*` records and their referenced `BC-*` revisions |
| `PRJ-TEST-REVIEW-05-TEST-ENVIRONMENT-DESIGN` | `05-test-environment-design.md` | accepted behavior/assurance semantics and its exact accepted STM dependency slice |
| `PRJ-TEST-REVIEW-06-SERVICE-SIMULATOR-SPEC` | `06-service-simulator-spec.md` | accepted `BC-*`, current `CC-*`, and its exact accepted consumer-boundary STM slice |
| `PRJ-TEST-REVIEW-07-SERVICE-SIMULATOR-IMPLEMENTATION-PLAN` | `07-service-simulator-implementation-plan.md` | accepted `BC-*`/`CC-*` provenance plus `PROJECTION_EXACT PRJ-TEST-REVIEW-06-SERVICE-SIMULATOR-SPEC` at its verified revision |
| `PRJ-TEST-REVIEW-08-E2E-TEST-PLAN` | `08-e2e-test-plan.md` | accepted `BC-*`, assurance semantics, and its exact accepted multi-component STM slice |

Every projection owns direct Stage B dependency metadata. Individually named
semantic records are `SEMANTIC_EXACT` dependencies at their accepted revision.
Dynamic sets use only the following deterministic `SEMANTIC_SELECTOR` form.

```text
test_review_scope_id: TRS-<stable scope identity>
scope_source: persisted Test Review capability scope record
scope_membership: every selected Test Engineering record carries the exact
                  test_review_scope_id; no filename, prose topic, or inferred
                  "relevance" may add a member

TEST_ENGINEERING_SEMANTIC_RECORD:
  authoritative record families: BC | MAT | TM | GAP
  allowed dimensions: family | status | freshness | authority |
                      capability_owner | test_review_scope_id
  allowed operators: = | IN
  logical connectors: AND | OR
  eligibility: status = ACCEPTED AND freshness = VALID
               AND authority = RESOLVED AND capability_owner = TEST_REVIEW

TEST_ENGINEERING_CONSISTENCY_RECORD:
  authoritative record family: CC
  allowed dimensions: family | status | freshness | capability_owner |
                      test_review_scope_id
  allowed operators: = | IN
  logical connectors: AND | OR
  eligibility: status IN [OPEN, CLASSIFIED, RESOLVED, WONT_RESOLVE]
               AND freshness = VALID AND capability_owner = TEST_REVIEW

stable_order: semantic_id ASC, revision ASC
resolved_members: [<ID>@<revision> ...] in stable_order
definition_revision: 1
```

The `test_review_scope_id` is an explicit persisted scope binding owned by Test
Review. It only bounds projection dependency resolution; it does not promote a
projection or its scope record to `BC/CC/MAT/TM/GAP` semantic authority.

| Selector | Consumer projection | Authoritative record type | Additional bounded predicate |
|---|---|---|---|
| `SEL-TEST-REVIEW-00-ASSURANCE` | `PRJ-TEST-REVIEW-00-ASSURANCE-SUMMARY` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family IN [MAT, TM, GAP] AND test_review_scope_id = <persisted TRS>` |
| `SEL-TEST-REVIEW-01-ASSURANCE` | `PRJ-TEST-REVIEW-01-ASSURANCE-MAP` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family IN [MAT, TM, GAP] AND test_review_scope_id = <persisted TRS>` |
| `SEL-TEST-REVIEW-02-TEST-PLAN` | `PRJ-TEST-REVIEW-02-TEST-PLAN` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family IN [BC, MAT, TM, GAP] AND test_review_scope_id = <persisted TRS>` |
| `SEL-TEST-REVIEW-03-BEHAVIOR-MODEL` | `PRJ-TEST-REVIEW-03-BEHAVIOR-CONTRACT-MODEL` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family = BC AND test_review_scope_id = <persisted TRS>` |
| `SEL-TEST-REVIEW-04-CONSISTENCY` | `PRJ-TEST-REVIEW-04-CONTRACT-CONSISTENCY-REPORT` | `TEST_ENGINEERING_CONSISTENCY_RECORD` | `family = CC AND test_review_scope_id = <persisted TRS>`; each referenced `BC-*` is a `SEMANTIC_EXACT` dependency |
| `SEL-TEST-REVIEW-05-ENVIRONMENT` | `PRJ-TEST-REVIEW-05-TEST-ENVIRONMENT-DESIGN` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family IN [BC, MAT, TM, GAP] AND test_review_scope_id = <persisted TRS>` |
| `SEL-TEST-REVIEW-06-BC` | `PRJ-TEST-REVIEW-06-SERVICE-SIMULATOR-SPEC` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family = BC AND test_review_scope_id = <persisted TRS>` |
| `SEL-TEST-REVIEW-06-CC` | `PRJ-TEST-REVIEW-06-SERVICE-SIMULATOR-SPEC` | `TEST_ENGINEERING_CONSISTENCY_RECORD` | `family = CC AND test_review_scope_id = <persisted TRS>` |
| `SEL-TEST-REVIEW-07-BC` | `PRJ-TEST-REVIEW-07-SERVICE-SIMULATOR-IMPLEMENTATION-PLAN` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family = BC AND test_review_scope_id = <persisted TRS>`; the simulator specification remains the declared `PROJECTION_EXACT` prerequisite |
| `SEL-TEST-REVIEW-07-CC` | `PRJ-TEST-REVIEW-07-SERVICE-SIMULATOR-IMPLEMENTATION-PLAN` | `TEST_ENGINEERING_CONSISTENCY_RECORD` | `family = CC AND test_review_scope_id = <persisted TRS>`; the simulator specification remains the declared `PROJECTION_EXACT` prerequisite |
| `SEL-TEST-REVIEW-08-E2E` | `PRJ-TEST-REVIEW-08-E2E-TEST-PLAN` | `TEST_ENGINEERING_SEMANTIC_RECORD` | `family IN [BC, MAT, TM, GAP] AND test_review_scope_id = <persisted TRS>` |

A selector addition, removal, or member revision change is projection impact;
it must not be hidden by a previously generated map or report. The exact
accepted STM slice and targeted-coverage acceptance consumed by projections
`05`, `06`, and `08` are `SEMANTIC_EXACT` dependencies. They are not
open-ended selectors that re-interpret a topology, consumer boundary, or
"qualifying" fact set from prose.

Any Test Review projection that presents factual system boundaries also records
the exact accepted STM dependency slice and targeted-coverage acceptance it
consumed. It does not use a Stage B selector to infer that slice. The
precondition remains:

```text
present + ACCEPTED + sufficiently fresh + sufficiently resolved
  + TARGETED STM COVERAGE ACCEPTED
```

An accepted/fresh `FULL` STM may satisfy that exact binding. A projection never
creates a private factual model, reuses its own prose as a factual source, or
bypasses targeted STM acquisition, the Technical Model Gate, or independent
targeted coverage review.

`PKG-TEST-REVIEW-DELIVERY` is the Test Review publication package.

The `test_review_scope_id` used by selectors is a persisted `TRS-*`
scope-binding record owned by Test Review. `NEW` initializes it from the
selected Test Review scope, `EXTEND` preserves it, and legacy migration must
create or explicitly block until it can create the binding. A filename or
prose topic cannot supply one.

```text
package_id: PKG-TEST-REVIEW-DELIVERY
owner: Test Review
gate: Test Review publication/closeout
freshness_policy: ALL_SCOPED_CURRENT
required_members:
  - projection_id: PRJ-TEST-REVIEW-00-ASSURANCE-SUMMARY
    purpose: required decision-facing summary of accepted Test Assurance
    mandatory_prerequisites: []
  - projection_id: PRJ-TEST-REVIEW-01-ASSURANCE-MAP
    purpose: required detailed map supporting the Test Assurance summary
    mandatory_prerequisites: []
optional_members: []
conditional_members:
  - condition_id: BEHAVIOR_CONTRACT_MODEL_DOCUMENT_REQUIRED
    when: persisted behavior_model_document_requirement = REQUIRED
    projection_id: PRJ-TEST-REVIEW-03-BEHAVIOR-CONTRACT-MODEL
    purpose: publish the required human-readable Behavior Contract Model
    mandatory_prerequisites: []
  - condition_id: TEST_PLAN_SELECTED
    when: persisted outputs.test_plan = true
    projection_id: PRJ-TEST-REVIEW-02-TEST-PLAN
    purpose: publish the selected Test Plan
    mandatory_prerequisites: []
  - condition_id: CONTRACT_CONSISTENCY_REPORT_SELECTED
    when: persisted outputs.contract_consistency_report = true
    projection_id: PRJ-TEST-REVIEW-04-CONTRACT-CONSISTENCY-REPORT
    purpose: publish the selected Contract Consistency Report
    mandatory_prerequisites: []
  - condition_id: TEST_ENVIRONMENT_DESIGN_SELECTED
    when: persisted outputs.test_environment_design = true
    projection_id: PRJ-TEST-REVIEW-05-TEST-ENVIRONMENT-DESIGN
    purpose: publish the selected Test Environment Design
    mandatory_prerequisites: []
  - condition_id: SERVICE_SIMULATOR_DESIGN_SELECTED
    when: persisted outputs.service_simulator_design = true
    projection_id: PRJ-TEST-REVIEW-06-SERVICE-SIMULATOR-SPEC
    purpose: publish the selected Service Simulator Design
    mandatory_prerequisites: []
  - condition_id: SERVICE_SIMULATOR_IMPLEMENTATION_PLAN_SELECTED
    when: persisted outputs.service_simulator_implementation_plan = true
    projection_id: PRJ-TEST-REVIEW-07-SERVICE-SIMULATOR-IMPLEMENTATION-PLAN
    purpose: publish the selected Service Simulator Implementation Plan
    mandatory_prerequisites: [PRJ-TEST-REVIEW-06-SERVICE-SIMULATOR-SPEC]
  - condition_id: E2E_TEST_PLAN_SELECTED
    when: persisted outputs.e2e_test_plan = true
    projection_id: PRJ-TEST-REVIEW-08-E2E-TEST-PLAN
    purpose: publish the selected E2E Test Plan
    mandatory_prerequisites: []
```

Each condition is an explicit persisted output-selection or capability-gate
result, never an inference from a file's presence. Resolve the package's finite
required and conditional membership snapshot before its gate runs. Optional
output selection makes the corresponding projection required for that package
instance; an unselected Test Plan, Service Simulator Design, E2E Test Plan, or
other optional output is not silently required and cannot block closeout.

## Test Environment Design

For each material dependency of the reviewed service, select one strategy and a
reason:

```text
REAL_DISPOSABLE | SERVICE_EMULATOR | CONTROLLABLE_MOCK |
IN_PROCESS_DOUBLE | TEMP_RESOURCE | NOT_REQUIRED
```

Use real isolated dependencies when their semantics are material. Mock external
uncertainty, not the behavior under test. Do not assume every dependency should
be mocked.

Each dependency record includes the selected strategy and a reason tied to the
material behavior and boundary being proved. The strategy is not inferred from
the convenience of the test harness.

## Service Simulator Design

Dependency substitutes model dependencies *of* the reviewed service. A Service
Simulator models the reviewed service *for its consumers*. The simulator uses
the relevant real consumer protocol surface and has a separate test-only
control plane. Illustrative controls are `/__test/health`, `/__test/reset`,
`/__test/scenario`, `/__test/state`, and `/__test/seed`; exact shape is
implementation-specific. Controls must not leak into the consumer contract.

Simulator scenarios carry accepted `BC-*` revision provenance and relevant
contract-view/authority classification; they are not generated blindly from
Swagger. Simulator implementation requires a separately accepted and fresh
specification plus explicit authorization. This capability does not implement
simulator code during review.

The consumer plane may expose HTTP, gRPC, WebSocket, event/message, or another
protocol when that is the real consumer boundary. The control plane is test-only
and may provide health, reset, scenario, state, and seed operations; it is never
used as evidence that the consumer protocol itself works.

## E2E Design

An E2E candidate is justified only when assurance depends on multiple real
components and a smaller boundary cannot prove the same behavior as reliably
and cheaply. Each design records source `BC-*` revision, real components,
allowed simulators/fakes, initial state, stimulus, material assertions, failure
observability, cleanup/reset, CI suitability, and cost where useful. E2E does
not require Service Simulator Design when the topology does not need one.

An E2E record states initial state, stimulus, material assertions, failure
observability, cleanup/reset, CI suitability, and estimated execution cost where
useful. It names participating real components and allowed substitutes, and
references the accepted `BC-*` revision from which the scenario derives.

## Capability Dependency DAG

Selectable outputs are:

```text
Test Assurance [required]
Test Plan [optional]
Contract Consistency Report [optional projection]
Test Environment Design [optional]
Service Simulator Design [optional]
Service Simulator Implementation Plan [optional; accepted simulator spec required]
E2E Test Plan [optional]
```

Behavior Model is an internal dependency, not a checkbox. Contract Verification
is automatic when materially applicable. Execute only the minimum slice:

```text
E2E Test Plan -> Test Assurance -> Behavior Model
  -> Contract Verification when applicable -> E2E Design
  -> Service Simulator Design only when topology requires it
Service Simulator Implementation Plan -> accepted + fresh simulator spec
```

`EXTEND` reuses accepted fresh upstream work and adds only the requested slice;
`USE_EXISTING` requires the requested slice to be accepted, fresh, and resolved.
`REVALIDATE` is impact-driven as defined by the umbrella freshness contract.

Before downstream Test Engineering semantics, the capability must calculate and
persist its minimum factual dependency slice and verify the predicate:

```text
present + ACCEPTED + sufficiently fresh + sufficiently resolved
  + TARGETED STM COVERAGE ACCEPTED
```

For `NEW`, the slice follows persistent STM bootstrap. For `EXTEND`, reuse
accepted/fresh facts, build missing facts, or revalidate stale/disputed facts;
then pass the result through the Technical Model Gate and independent targeted
coverage review. An accepted/fresh `FULL` model satisfies the slice without a
second targeted model. The capability must not inspect arbitrary implementation
and construct a private factual model as a normal fallback.

It preserves `BC-*`, `CC-*`, `MAT-*`, `TM-*`, and `GAP-*` as capability-owned
semantics; STM observations are reusable factual inputs, not behavior contracts,
mismatch classifications, or test-gap authority.

## Output Package

Preserve existing compatibility outputs and add only selected outputs:

```text
00-test-assurance-summary.md
01-test-assurance-map.md
02-test-plan.md                              # optional
03-behavior-contract-model.md                # when required
04-contract-consistency-report.md            # optional projection
05-test-environment-design.md                # optional
06-service-simulator-spec.md                 # optional
07-service-simulator-implementation-plan.md  # optional
08-e2e-test-plan.md                          # optional
working/                                     # authoritative BC/CC/TM/GAP ledgers
```

Persist explicit output booleans, never compound modes. Distinguish
`NOT_APPLICABLE`, `NOT_VERIFIED`, and `VERIFIED_NO_MATERIAL_ISSUES`. Projection
repair can change presentation only; semantic changes require technical
revalidation.

## Reuse / Extend / Revalidate

`RESUME` continues at the first unfinished valid gate. `EXTEND` reuses accepted
upstream artifacts. `REVALIDATE` evaluates changed source bindings and loads
minimum fresh evidence: tests-only changes affect `TM/MAT/GAP` first;
implementation/declared changes affect corresponding views and BC impact; and
consumer-only changes affect `CONSUMED` views plus consumer-facing
simulator/E2E projections. A changed file is routing context, not proof of
semantic impact. No whole-package replay occurs without impact evidence.

Source bindings are revision-bound and populated with concrete values at
runtime, not literal placeholders:

```yaml
BC-042:
  source_bindings:
    architecture_revision: RF-012@rev4
    declared_revision: openapi.yaml@service_baseline_sha
    implementation_revision: src/orders/handler.py@service_baseline_sha
    consumer_revision: checkout-ui@consumer_baseline_sha
  service_baseline_sha: <concrete service revision>
  consumer_baseline_sha: <concrete consumer revision>

CC-017:
  compared_views:
    declared_revision: openapi.yaml@service_baseline_sha
    implementation_revision: src/orders/handler.py@service_baseline_sha
    consumer_revision: checkout-ui@consumer_baseline_sha
    tested_revision: tests/orders/test_orders.py@service_baseline_sha
```

The placeholder names explain the binding shape only; persisted records contain
actual revisions. A changed binding triggers impact analysis rather than
automatic invalidation of every related BC.
