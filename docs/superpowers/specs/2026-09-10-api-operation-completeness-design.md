# API / Interface Operation Completeness Design

## 1. Problem

The Shared Technical Model can currently represent a material API surface as one
`IF-*` while a source baseline contains many concrete operations. Provided and
Consumed Interfaces projections select accepted `IF-*` facts, so a projection
can render every selected member and still omit operations that were never
represented in the accepted model.

## 2. Current failure mode

`IF-*` is the identity of one material interaction surface or contract and its
`operation_identity` is optional. FULL Technical Model Coverage means all known
material externally visible or architecturally relevant surfaces, not every
HTTP route. The existing selectors and V1–V4 projection gates verify accepted
IF membership and faithful rendering, not source-operation inventory. A coarse
router-level IF can therefore satisfy current coverage and produce a CURRENT
projection without proving endpoint completeness.

## 3. Goals

- Preserve `IF-*` as the factual interface/surface authority.
- Represent concrete addressable operations without creating a new top-level
  authority family.
- Make operation presence complete for a bounded detailed Provided or Consumed
  Interfaces request when the evidence permits accounting.
- Keep operation detail completeness separate from operation presence.
- Require effective route composition when it can be evidenced and preserve
  explicit limitations when it cannot.
- Make EXTEND request only targeted operation-depth enrichment.
- Make operation membership and revision changes affect dependent projections
  through existing Stage B dependency/impact mechanics.

## 4. Non-goals

This design does not redefine ordinary FULL Architecture coverage as every
endpoint, require OpenAPI-equivalent schemas, add a fourth capability, create an
API Report identity, perform source scanning inside projections, add runtime
crawling/fuzzing, redesign Contract Verification, or regenerate projections
automatically.

## 5. Preserved invariants

STM is WHAT EXISTS and the Technical Model Gate is the sole writer of accepted
fact semantics. Technical Documentation is HOW VERIFIED SYSTEM IS DESCRIBED;
CQ owns implementation-quality findings; TE owns WHAT MUST BE PROVEN; Contract
Verification owns compatibility adjudication; Architecture owns architectural
meaning. Requested output is distinct from resolved dependencies, and CURRENT
projection state is distinct from factual inventory completeness. Product is
optional, single-project scope remains first-class, permissions do not expand,
and historical facts are not rewritten.

## 6. Alternatives considered

### Approach A — one IF per concrete operation

This makes selectors simple, but creates excessive top-level identity churn,
weakens router/resource grouping, complicates non-HTTP protocols, and causes
large APIs to couple every operation to global IF membership. It also changes
the established meaning of IF from surface/contract to operation.

### Approach B — operation collection embedded without addressable children

This limits identity growth and is easy to render, but cannot address one
operation cleanly from evidence, CQ, TE, or CC. A large collection causes
monolithic revision churn and weak per-operation impact and compatibility
history.

### Approach C — parent-owned addressable operation children (chosen)

An IF remains the interface/surface identity. Its accepted STM structure owns a
bounded collection of addressable operation children. Children are qualified by
their parent IF, can be referenced by evidence and downstream contracts, and
support deterministic inventory accounting without becoming independent
top-level authority. This preserves grouping, addressability, and non-HTTP
genericity while avoiding 5,000 unrelated top-level IF identities.

### Approach D — projection-time source reconstruction

Rejected. It would create a second private factual model outside the Technical
Model Gate, make projection content depend on unrecorded source interpretation,
and prevent reliable revalidation and provenance.

### Approach E — existing structure

Insufficient. Optional `operation_identity` and protocol properties can enrich
an IF, but there is no operation collection, operation inventory accounting,
effective-route rule, or output-scoped completeness requirement.

## 7. Chosen model

Approach C is adopted. An operation is a subordinate addressable factual child
of an accepted IF. The child is not a fourth capability, not a new independent
factual authority, and not a Technical Documentation record. It is represented
within the STM's existing IF-owned structure and is accepted, revised, and
superseded only by the Technical Model Gate.

## 8. IF / operation ownership

`IF-*` owns the interface/surface and its operation inventory. The Technical
Model Gate owns both accepted IF meaning and accepted child operation meaning.
Technical Documentation, Architecture, CQ, TE, CC, and projection generation
may reference operation children but cannot create, accept, revise, or remove
them.

An operation cannot exist without a parent IF. An operation reference is
parent-qualified, conceptually `IF-USER-API@rev3/OP-GET-USER@rev5`; the `OP-*`
token is not a globally searchable STM family. The same semantic operation is
not shared across IF parents. A provider and consumer expectation remain
separate IF-owned children even when their protocol identity matches.

Moving an operation to another IF changes its parent-qualified semantic identity
and creates a new child with an explicit `supersedes` relation to the prior
child when the evidence establishes continuity. It is not silently reparented.

## 9. Operation identity

The stable child identity is based on normalized protocol semantics, never a
filename, line number, generated symbol, or source location. The structured
identity contains the applicable interface kind, parent IF qualification,
perspective/contract role, and protocol address. For HTTP this is method plus
effective route template, qualified by the parent and view role. Path and method
changes create a new semantic identity with history; source refactors that
preserve the normalized operation identity retain the child identity. API
version changes are distinct when the qualified contract/path/version changes.

Aliases are separate evidenced addresses linked as aliases only when the
Technical Model Gate can establish that they intentionally expose the same
operation semantics; otherwise they are separate operations. Duplicate route
declarations are retained as unresolved/duplicate candidates until the gate
classifies them. Conditional or feature-flag variants retain their condition
and availability limitation rather than being collapsed.

## 10. Protocol-general model

The generic concept is an addressable interface operation, used only where the
protocol has a meaningful operation surface:

- HTTP REST: method, effective route/template, media/contract references.
- GraphQL: operation type/name or addressable field/schema surface.
- gRPC/RPC: package/service and RPC/procedure method.
- WebSocket: addressable command/message/topic operation when contractually
  identifiable.
- CLI: command/subcommand and option contract where modeled as an IF.
- Library/IPC/file protocols: public symbol, call, channel, or protocol
  operation when the existing interface kind defines one.

`EVENT-*` remains the primary identity for semantic events/messages. Publish or
subscribe edges remain `INT-*`; an operation child is used only for a
contract-addressable command surface, not to replace event identity.

## 11. Route composition

For composed HTTP declarations, discovery records evidence for each contributing
prefix/mount and local route, then the Technical Model Gate resolves the
effective method plus path. FastAPI router prefixes, Express mounts, Django
includes, Spring class/method mappings, ASP.NET controller/action templates, and
NestJS controller/method decorators are composition inputs, not identities.

The operation records `EXACT` when composition is resolved from baseline-bound
evidence. Computed, conditional, plugin, reflection, or runtime-only routes
record `RESOURCE_BOUNDED` or `UNRESOLVED` with the bounded limitation and
available evidence. No path is fabricated. An operation can be inventory-
accounted while its exact route remains unresolved.

## 12. Evidence and provenance

Each operation child retains evidence references for route/method declarations,
composition inputs, contract/schema declarations, parameter detail, auth
middleware, consumer call sites, generated contracts, and accepted runtime
observations where applicable. Evidence location is not identity. Evidence
revisions may trigger revalidation without changing identity, while semantic
method/path/parent changes revise identity as described above.

## 13. Coverage model

Technical Model Coverage remains the sole coverage authority. It gains a
qualified depth dimension for an explicitly requested interface slice; it does
not gain a second coverage authority or redefine global FULL:

```text
SURFACE
  INTERFACE_SURFACE_COMPLETE
OPERATION_INVENTORY
  OPERATION_INVENTORY_COMPLETE
  OPERATION_INVENTORY_PARTIAL / UNKNOWN
OPERATION_DETAIL
  optional factual enrichment; not required for inventory completion
```

Ordinary Architecture Review may close `FULL` with material surface coverage.
Detailed Provided Interfaces requires `OPERATION_INVENTORY_COMPLETE` for its
bounded provided slice. Detailed Consumed Interfaces requires the analogous
accepted consumed inventory. API Report requires both directions when both
sections are selected. These are output-scoped dimensions of the existing
Technical Model Coverage record, not global endpoint requirements.

Targeted operation inventory acceptance does not satisfy FULL Architecture
coverage, and an accepted FULL surface row does not automatically satisfy
operation inventory depth.

## 14. Operation inventory accounting

For a fixed Project or Product member, baseline, repository/source scope,
interface direction, interface kind, and selected IF slice, the coverage record
persists deterministic accounting:

```text
discovered_candidates: N
accepted_exact_operations: N1
accepted_bounded_or_unresolved_operations: N2
accepted_not_applicable_or_duplicate_candidates: N3
unaccounted_candidates: N4
```

`OPERATION_INVENTORY_COMPLETE` requires `N4 = 0` and an evidence-backed
classification for every candidate. Bounded or unresolved operations count as
accounted but remain visible limitations. A source gap, unavailable source, or
unresolved dynamic registration yields PARTIAL/UNKNOWN, never silent success.

## 15. Materiality interaction

Materiality may group routine surfaces in ordinary Architecture Review. Once a
detailed API/interface projection is requested, operation presence in the
selected bounded surface is material by definition. A concrete operation cannot
be omitted as “not architecturally material” from that inventory. This does not
make every parameter, field, or response schema mandatory: operation presence
completeness and operation detail completeness are separate.

## 16. Detail completeness

Operation identity requires the protocol identity applicable to its kind. For
HTTP, method and effective path are `IDENTITY_REQUIRED` when exact; a bounded or
unresolved limitation is required when they cannot be exact. The following are
`WHEN_APPLICABLE_REQUIRED` when material to the operation and evidenced:
path/query parameters, relevant headers, request media type and schema,
response statuses/schemas, auth/trust binding, error contract, pagination,
multipart/upload behavior, and boundary evidence. Additional schema fields are
`WHEN_EVIDENCED` or optional enrichment. Missing detail is rendered as an
explicit limitation and does not invalidate an otherwise complete inventory.

## 17. Provided interfaces

Provided operation children describe what the bounded system exposes. The
Provided Interfaces selector resolves the selected accepted IF surfaces plus
their frozen operation-inventory coverage snapshot. The detailed projection
renders every accepted exact or bounded operation and its limitations; it must
not silently render only parent surfaces.

## 18. Consumed interfaces

Consumed operation children describe consumer expectations and observed use.
They remain separate from provider operations and may exist without a known
provider. Matching is a candidate relationship until Contract Verification or
another existing owning contract resolves it. A consumed operation inventory is
complete only for the bounded consumer source/scope requested; a service-level
consumer IF without operation accounting is sufficient only for ordinary
material surface coverage, not the detailed Consumed Interfaces projection.

## 19. DECLARED / IMPLEMENTED / CONSUMED / TESTED views

One parent-qualified operation child may carry multiple observed views using the
existing IF vocabulary, but views remain independent observations. A declared
OpenAPI operation, implemented handler, consumer call, and executable test do
not imply one another. `TESTED` still requires accepted execution evidence under
Test Engineering. A provider declaration does not become implementation, and a
consumer expectation does not become provider behavior.

## 20. CQ integration

CQ findings may reference `IF@revision/OP@revision` and, where applicable, a
specific operation property or boundary observation. CQ remains the authority
for whether implementation is poor or unsafe; it cannot create or adjudicate
the operation fact. A missing body limit on one operation may cite the operation
and its evidence without changing operation inventory status.

## 21. TE integration

TE boundary and negative cases may target an operation child and its operation
fields. Generated or accepted cases remain WHAT MUST BE PROVEN and cannot
populate STM `TESTED`, PASSED, FAILED, or runtime-observed state. TE does not
create operation children. Unknown operation or boundary detail produces an
explicit test requirement/assumption rather than an invented route or limit.

## 22. Contract Verification integration

CC may use provider and consumer operation references as qualified comparison
inputs. Same method/path is not compatibility. Request/response schemas,
statuses, auth, errors, and other existing CC inputs remain under CC authority;
the operation child supplies identity and provenance only. Provider and consumer
operations are never merged by the documentation projection.

## 23. Technical Documentation dependencies

`PRJ-TECH-DOC-02-PROVIDED-INTERFACES` and
`PRJ-TECH-DOC-03-CONSUMED-INTERFACES` retain their existing stable identities
and selectors. In detailed mode, each declares the exact bounded operation
inventory coverage record and resolved operation membership/revisions consumed.
V1–V4 then verify the required fields, snapshot, and faithful rendering. A
projection can be CURRENT only relative to accepted dependencies and an
accepted inventory-completeness state for the requested detailed scope.

Inventory limitations are rendered as PARTIAL/UNKNOWN/UNRESOLVED; they are not
replaced with an empty section or a complete claim. Existing coarse projections
remain valid when their package explicitly requests surface depth.

## 24. API Report

The existing human-facing API Report remains an umbrella over Provided
Interfaces, Consumed Interfaces, Integrations, Auth and Trust, and Failure
Behavior. It creates no identity. Its default detailed Provided/Consumed
sections require the corresponding operation inventory acceptance. It does not
automatically select Architecture, CQ, or TE and does not require unrelated FULL
Architecture coverage. Internal enrichment remains `resolved_work`.

## 25. EXTEND behavior

When EXTEND requests detailed Provided/Consumed Interfaces or API Report and
the accepted STM has only surface depth, dependency resolution reports an
insufficient operation-depth requirement. It requests targeted interface
enrichment for the exact Project/baseline/direction/interface scope, then
targeted Technical Model Coverage acceptance. Existing surface facts remain
accepted; unrelated domains and capabilities are not rebuilt or selected.

## 26. TARGETED/FULL interaction

Operation inventory can be accepted in a TARGETED slice such as “all provided
HTTP operations for backend service X at commit Y.” This does not imply FULL
STM, FORENSIC Architecture coverage, or operation completeness outside the
slice. A prior FULL surface acceptance is reusable evidence but does not satisfy
the deeper operation requirement without an accepted inventory dimension.

## 27. Freshness/revision impact

New/removed operations change inventory membership and make dependent detailed
projections STALE. Method/path/parent changes revise operation identity and
history; schema, auth, boundary, or evidence changes revise the affected
operation/IF semantic revision as applicable. Selector or inventory snapshot
membership changes record projection impact. Impact accounting never regenerates
content automatically.

## 28. Parent/child revision strategy

Use parent-qualified independent child revisions with parent binding (C1):
`IF-USER-API@3/OP-GET-USER@5`. This avoids rewriting all sibling references when
one operation changes and scales better than parent-bound child versions. A
parent IF revision changes when the surface identity/contract changes or when
the IF-owned inventory contract requires a parent revision; ordinary child
membership/revision changes are captured by the inventory coverage snapshot.
Reparenting creates a new parent-qualified child and an explicit history link.
Any revision-bound dependency must include the parent IF revision, child
revision, and inventory/selector definition revision.

## 29. Selector/projection dependency behavior

The existing IF selector remains the entry point. Detailed projection
dependencies include:

1. exact accepted parent IF revisions;
2. an operation-inventory coverage record and its definition revision;
3. a deterministic frozen membership snapshot of parent-qualified operation
   children and revisions.

This is a qualified extension of existing `SEMANTIC_EXACT`/
`SEMANTIC_SELECTOR` dependency contracts, not private renderer traversal. New,
removed, unresolved/resolved, or revised operation membership changes the
snapshot and marks the projection STALE.

## 30. Dynamic routes

Dynamic, plugin, feature-flag, reflection-generated, framework-generated, and
runtime-only operations are inventory candidates. The accepted coverage record
classifies them as EXACT, RESOURCE_BOUNDED, or UNRESOLVED with source/evidence
limitations. A bounded dynamic group may count as accounted if its finite scope
and limitation are accepted; unknown/unbounded discovery remains PARTIAL or
UNKNOWN. Technical Documentation renders the limitation and never fabricates
an exact path.

## 31. Large API scalability

The model keeps one surface IF and searchable child records/snapshots rather
than requiring thousands of top-level IF identities or one opaque monolithic
field. Inventory accounting is partitionable by parent IF, direction,
interface kind, and bounded source scope. Projection dependencies can snapshot
stable ordered child references; one changed operation need not revise every
sibling.

## 32. Non-HTTP interface behavior

Operation completeness applies when the interface kind defines addressable
operations: GraphQL fields/operations, gRPC/RPC methods, WebSocket commands,
CLI commands, and similar modeled surfaces. It does not force an operation
child onto semantic events; EVENT-* and INT-* retain their existing roles.
For protocol kinds without a meaningful operation unit, surface completeness
and explicit protocol-specific limitations are sufficient.

## 33. Product qualification

Every operation and inventory record is qualified to exact Project/source
revision or Product member/baseline. A Product view may aggregate qualified
operation inventories but cannot flatten divergent paths, versions, schemas,
limits, auth, or availability. Product remains a composition/view authority,
not factual authority, and membership grants no source, test, write, commit,
push, deploy, or runtime permission.

## 34. Complete-claim guard

Technical Documentation may use “complete API,” “all endpoints,” “full endpoint
list,” or equivalent only when the requested detailed Provided/Consumed scope
has accepted operation inventory completeness and its dependency snapshot is
valid. CURRENT alone is insufficient. Without that accepted state, the output
must say PARTIAL, UNKNOWN, or UNRESOLVED and state the bounded limitation.
Technical Documentation checks the accepted coverage/dependency state; it does
not decide factual completeness itself.

## 35. Backward compatibility

Historical surface-only IF records remain valid and are not rewritten. Their
operation inventory status is `UNASSESSED`/`UNKNOWN` unless an accepted record
proves otherwise. They can satisfy existing surface-depth consumers but cannot
satisfy a new detailed operation-inventory dependency. Existing IF views,
identities, evidence, CQ/TE/CC records, Product records, and projections remain
interpretable.

## 36. Migration classification

`COMPATIBLE_EXTENSION`. No blanket migration or historical rewrite is required.
The first detailed request may route to targeted enrichment. A missing
operation inventory is insufficient evidence, not a failed or invalid old fact.

## 37. Pressure scenarios

| ID | Expected behavior |
|---|---|
| D01 | Ten operations under one router become ten accounted children under one IF; ordinary surface review may remain grouped. |
| D02 | Nested prefixes compose to an exact effective route when evidence permits; otherwise limitation is retained. |
| D03 | GET and POST on one path are distinct operation identities. |
| D04 | Computed path is accounted as bounded/unresolved, never fabricated. |
| D05 | Declaration/code mismatch remains separate DECLARED/IMPLEMENTED evidence and is visible to CC/coverage. |
| D06 | Undeclared implemented operation is an operation candidate and mismatch evidence, not silently omitted. |
| D07 | Consumer operation can be complete without a provider IF; provider match remains unresolved. |
| D08 | Operation inventory can be complete while partial schema detail is rendered as a limitation. |
| D09 | Architecture-only surface review does not trigger operation enumeration. |
| D10 | API Report-only request triggers targeted operation depth without selecting Architecture. |
| D11 | EXTEND from surface-only STM requests only targeted operation enrichment. |
| D12 | Added operation changes membership and makes the detailed projection STALE; regeneration remains explicit. |
| D13 | Removed operation changes membership and freshness impact. |
| D14 | Path change creates revised/new identity with explicit history. |
| D15 | Auth change revises affected operation/IF evidence and dependent projection freshness. |
| D16 | Boundary-limit change affects operation/IF semantic revision and dependent CQ/TE/projection inputs as applicable. |
| D17 | 5,000 operations remain parent-partitioned/searchable without 5,000 top-level IF families. |
| D18 | GraphQL operation/field surface uses protocol-specific child semantics. |
| D19 | gRPC service/RPC method uses operation children; service IF remains parent surface. |
| D20 | Product aggregates exact member inventories and visibly qualifies divergent operation sets. |

## 38. Open questions

The implementation plan must choose concrete serialization for IF-owned child
records and the exact coverage-record field names, define the operation-key
normalizer per supported protocol, and update selector grammar to carry the
inventory snapshot. These are bounded contract details, not unresolved authority
decisions. The authority decision is fixed here: parent-owned addressable
operations, C1 revision strategy, existing Technical Model Coverage as owner,
and output-scoped operation completeness.

## 39. Acceptance criteria

1. IF remains the parent factual surface; no fourth capability, API authority,
   or independent OP authority exists.
2. Operations are parent-qualified, addressable, evidence-bound, revisioned,
   and protocol-general; HTTP identity includes method and effective path when
   exact.
3. Composed routes are resolved from evidence or exposed with explicit
   bounded/unresolved limitations.
4. Technical Model Coverage can account discovered candidates with zero
   unaccounted candidates for a bounded detailed slice.
5. Ordinary Architecture FULL remains material surface coverage and does not
   require every endpoint.
6. Detailed Provided/Consumed/API projections require accepted operation
   inventory coverage and render every accounted operation/limitation.
7. Operation detail gaps do not invalidate inventory completeness.
8. DECLARED/IMPLEMENTED/CONSUMED/TESTED remain independent views; TESTED still
   requires accepted execution evidence.
9. CQ, TE, CC, Product, and Stage B lifecycle references preserve ownership and
   exact scope.
10. EXTEND performs targeted operation enrichment and does not restart unrelated
    review work or silently regenerate projections.
11. New/removal/revision/limitation changes create correct impact and freshness
    transitions.
12. Complete API claims are blocked unless accepted operation inventory
    completeness exists; partial/unknown limitations are visible.
13. Historical surface-only IF facts remain valid and interpretable.
14. All D01–D20 scenarios have deterministic expected authority, coverage, and
    projection behavior.
