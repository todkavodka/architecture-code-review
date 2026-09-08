# Stage F — Interface, API & Data Integration Catalog
## Independent Design Review

### Review metadata

| Field | Value |
|---|---|
| Repository | `/home/tod/skills/architecture-code-review` |
| Branch | `main` |
| Local baseline | `9d5c09b6e1dc2686d640e66b1760dcd47640ef42` |
| Remote relation | `origin/main` is an ancestor of the approved checkpoint |
| Design artifact | `docs/superpowers/specs/2026-09-08-stage-f-interface-api-data-integration-design.md` |
| Review type | Independent Design Review only |
| Review date | 2026-09-08 |

The baseline gate passed. Local `HEAD` equals the approved Discovery checkpoint;
`origin/main` remains the earlier published ancestor. Tracked state is clean.
The four known historical untracked files and the untracked Design artifact were
preserved unchanged.

### Scope

This review pressure-tests the Design against the approved Discovery, current
Stage A–E contracts, authority ownership, backward compatibility, single-project
operation, Product qualification, projection/package lifecycle, and the listed
pressure scenarios. It does not modify the Design or any normative file.

The review treats the Design as a semantic proposal, not as already-authorized
implementation. A finding means the Design must be clarified or remediated
before it can become the authoritative Stage F Design baseline.

### Repository/contracts inspected

The review read the approved Discovery and Independent Discovery Review and the
current contract sources, including:

- `references/shared-evidence-model.md`;
- `references/shared-technical-model.md`;
- `docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`;
- `references/technical-model-dependencies.md`;
- `references/projection-lifecycle.md`;
- `references/projection-dependencies.md`;
- `references/projection-gates-and-packages.md`;
- `references/technical-documentation.md`;
- `references/product-multi-project-review.md`;
- `references/revalidation-and-freshness.md`;
- `capabilities/test-review/references/test-engineering-contract.md`;
- relevant Architecture Review and Code Quality ownership contracts.

The current Test Engineering contract is especially material: Contract
Verification owns `CC-*`; `CC-*` records preserve compared views, relevant
`BC-*`, revisions, mismatch, and adjudication state; and the four observable
views are `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED`. Contract
Verification is an internal automatic gate when a materially relevant declared
external contract exists, not merely an optional report.

### Authority-model assessment

**Result: PASS**

The Design preserves the required split:

```text
WS-* / EV-* -> STM families and relations -> PRJ-* projections/packages
```

It keeps `COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, and `FLOW-*` distinct,
retains `AUTH-*`/`CFG-*`/`ERR-*` ownership, and does not introduce an API,
SQL, DB, Data, or Product factual family. It also preserves `RF-*`,
`CQ-*`/`CQRA-*`, Test Engineering authorities, `PRJ-*`, and `RG-*` ownership.

The proposed `MIGRATION_AUTHORITY` is a controlled relation extension, not an
identity family. The Design correctly keeps relation, dependency, reverse index,
projection, package, and finding meanings separate.

### IF-* assessment

**Result: PASS**

The common IF shape remains a material boundary surface rather than a call
occurrence. Direction, protocol family, optional operation/address/contract
properties, Project qualification, precision, observed view, and evidence are
appropriately separated. Historical broad facts can omit new optional detail.

Protocol-specific properties avoid an HTTP-shaped universal schema. Request and
response contracts are referenced or fingerprinted rather than copied into STM;
`AUTH-*` and `ERR-*` remain authorities for auth and error concepts. An unknown
provider is permitted for a consumer expectation.

The Design is implementation-ready in the main shape, subject to the findings
below concerning precision applicability and role/view validation.

### Provider/consumer assessment

**Result: PASS**

Provider and consumer IF facts remain independently accepted and revisioned.
`INT-*` can connect a source, consumer expectation, target, and optional matched
provider IF without aliasing the two interface identities. This handles:

- provider declaration without a consumer;
- consumer expectation without a known provider;
- provider/consumer disagreement;
- provider implementation differing from declaration;
- multiple consumers of one provider;
- version selection by one consumer; and
- unresolved external providers.

Each side retains its own evidence, Project/revision/baseline qualification, and
observed view. Matching and compatibility do not overwrite either side.

### Contract-role / observed-view assessment

**Result: FINDINGS**

The Design introduces `contract_role` alongside the existing `observed_view`,
which is a reasonable separation of perspective from observation. However, it
does not define a closed validity matrix for their combinations.

The intended examples are clear:

```text
PROVIDER_DECLARATION + DECLARED
PROVIDER_IMPLEMENTATION + IMPLEMENTED
CONSUMER_EXPECTATION + DECLARED
CONSUMER_OBSERVED_USE + CONSUMED
```

But the Design also needs to define valid tested combinations, such as a
provider declaration tested by a contract test and a consumer expectation tested
by an executable test. Without those rules, a record can claim
`PROVIDER_IMPLEMENTATION + CONSUMED` or `CONSUMER_EXPECTATION + IMPLEMENTED`
without a defined semantic meaning. This is recorded as `DRF-002`.

### Protocol-property assessment

**Result: PASS**

The common-core plus controlled `protocol_properties` model is coherent across
HTTP/REST, gRPC/RPC, GraphQL, WebSocket, webhook, CLI, library, file/protocol,
and IPC surfaces. Unsupported properties may remain absent. Operation identity
is not forced into one universal HTTP shape, and broad historical facts remain
valid.

The Design correctly treats operation identity as a semantic identity concern
and uses `supersedes` when continuity is uncertain. The protocol table is
sufficiently bounded for later implementation planning without requiring a
universal canonicalization engine.

### EVENT-* assessment

**Result: PASS**

`EVENT-*` remains the semantic event/message authority. It carries producer,
consumer, name/topic, payload/schema reference, delivery properties, and
provenance where evidenced. A broker binding does not automatically create a
semantic event. A webhook may legitimately use `EVENT-* + IF-* + INT-*` when
event, callback contract, and concrete interaction are all material.

This avoids both erroneous event-to-IF duplication and broker-to-event
overclaiming.

### INT-* assessment

**Result: PASS**

`INT-*` is a coherent owner for a concrete interaction edge. It can reference
source, target, consumed/provided IFs, EVENT, protocol/transport, access mode,
precision, evidence, and exact Project/revision/baseline qualification. It does
not own interface, resource, dependency, or compatibility identity.

The Design correctly states that `INT-* CALLS` or data access does not
automatically become a dependency edge, and a dependency edge does not prove
runtime use.

### READS_FROM / WRITES_TO authority assessment

**Result: FINDINGS**

The Design says `READS_FROM` and `WRITES_TO` remain factual navigation
relations, but when an INT exists they become derived/attached views of the INT
fact. The current STM contract defines relations as semantically meaningful
links and does not itself establish this Stage F derivation direction.

The Design does not fully define:

- whether the INT is always the source of truth for a new data-access fact;
- whether a legacy relation without INT is promoted, preserved, or merely
  projected;
- whether the relation is materialized as a semantic relation or only derived
  for projection/indexing;
- how a historical `READS_FROM` relation conflicts with a new INT `WRITE`; or
- how `READ_WRITE` relates to two separately evidenced READ and WRITE edges.

This is `DRF-003`, a MEDIUM finding. Without a closed rule, implementation can
create two accepted facts that disagree while both appear authoritative.

### DS-* resource assessment

**Result: PASS**

One DS identity family for stores and addressable child resources is compatible
with the current material data-store meaning and avoids a new entity taxonomy.
Parent resource, technology, safe address, precision, Project qualification,
and evidence provide a workable bounded shape. Optional `TRIGGER`, `INDEX`, and
`SEQUENCE` kinds are correctly kept outside the minimum catalog requirement.

The non-SQL kinds are useful bounded resource addresses rather than an
universal ontology. Unknown technology-specific resources can remain
store-level/resource-bounded without forcing a new family.

### Database callable boundary

**Result: FINDINGS**

The Design models database `PROCEDURE` and `FUNCTION` as DS resources targeted
by `INT access_mode=EXECUTE`, which is coherent for database-owned schema
objects. But it does not explicitly resolve the parallel callable-surface case:

```text
DS-* = database-owned procedure/function resource
IF-* = callable boundary/contract when it is a material interface
INT-* = concrete execute interaction
```

Without an explicit rule for when an IF may reference the DS callable and which
identity owns the callable contract versus the database object, implementation
could duplicate or conflate identities. This is `DRF-005`, a MEDIUM finding.

### Parent/child DS assessment

**Result: PASS**

`parent_resource_ref` is correctly limited to containment/address context. The
Design explicitly prevents inherited ownership, access, migration authority, or
dependency. Any future inheritance must be explicit, bounded, traceable,
overridable, and projection-visible. This preserves conservative ownership.

### Data-access modes

**Result: PASS**

The mode set is understandable and separates runtime operation from migration
authority:

```text
READ | WRITE | READ_WRITE | EXECUTE | DDL | MIGRATION
```

`MIGRATION` represents execution, while `MIGRATION_AUTHORITY` represents
responsibility. The model does not require a full SQL verb taxonomy.

`READ_WRITE` is acceptable as an access capability/interaction mode, but its
relationship to separately observed READ and WRITE edges must be closed by the
`DRF-003` remediation.

### Ownership and migration authority

**Result: PASS**

`MIGRATION_AUTHORITY` is an additive controlled relation, not an identity
family. It binds owner, resource, source evidence, Project/revision/baseline,
and bounded scope. It does not imply runtime execution, state ownership, or a
dependency. Multiple authorities and conflicts remain STM facts; Architecture
Review interprets their consequences.

### SQL model

**Result: PASS**

The mappings are architecturally useful and avoid a full parser:

```text
SELECT -> READ
INSERT/UPDATE/DELETE -> WRITE
UPSERT/MERGE -> READ_WRITE unless phases are known
procedure/function -> EXECUTE
DDL -> DDL
migration -> MIGRATION
```

`READ_WRITE` is understood as one interaction whose evidenced behavior includes
both read and write capability, not as proof that every execution performs both
operations. The relation-authority and separate-edge rule still needs the
targeted clarification in `DRF-003`.

### Non-SQL model

**Result: PASS**

Redis, MongoDB, search indexes, S3, vector stores, filesystems, and embedded
stores all use the same DS resource plus INT access pattern. The Design does
not infer key patterns, collections, prefixes, or indexes from a store client
alone. Precision follows evidence.

### Evidence-strength model

**Result: PASS**

`DIRECT_DECLARATION`, `STRONG_INFERENCE`, and `WEAK_HINT` are evidence classes,
not replacements for `EV-*`, confidence, observed view, or STM acceptance. The
Design explicitly rejects configuration-only, dependency-only, connection-only,
migration-only, and unused-client-only promotions to concrete use.

### Precision model

**Result: FINDINGS**

The four-state model is useful and orthogonal to lifecycle, freshness, coverage,
confidence, observed view, and authority:

```text
EXACT | RESOURCE_BOUNDED | STORE_ONLY | UNRESOLVED
```

However, the Design places `STORE_ONLY` in the common IF shape and says an
unsupported protocol field may produce `STORE_ONLY` precision. `STORE_ONLY`
describes known store/system use with unknown entity precision; it is not a
meaningful precision state for an HTTP, gRPC, GraphQL, CLI, or library
interface. This is `DRF-004`, a MEDIUM finding.

The remediation can remain within the same vocabulary by defining
family-specific applicability, for example `STORE_ONLY` only for DS and
DATA_ACCESS INT facts, while IF facts use `EXACT`, `RESOURCE_BOUNDED`, or
`UNRESOLVED`.

### Provider/consumer matching

**Result: PASS**

Candidate matching is explicitly non-authoritative, does not alias IFs, and
uses exact accepted provider/consumer revisions for later verification. It
rejects fuzzy path/name similarity as factual authority.

The remaining ownership concern is addressed by `DRF-001`: the candidate result
must be clearly classified as a derived Contract Verification input or a
non-authoritative projection result, not a second accepted STM relation.

### Compatibility authority

**Result: FINDINGS**

The Design correctly selects the existing Contract Verification boundary and
does not create a compatibility family or engine. The current Test Engineering
contract confirms that Contract Verification owns and writes `CC-*` and that
`CC-*` records preserve compared views, relevant `BC-*`, revisions, mismatch,
and adjudication state.

But the Design introduces the result vocabulary
`COMPATIBLE | INCOMPATIBLE | INDETERMINATE | NOT_COMPARABLE` without mapping it
to the current `CC-*` fields and classification vocabulary. Current `CC-*`
classifications include `AUTHORITY_UNRESOLVED`, `DECLARATION_STALE`,
`IMPLEMENTATION_DEFECT`, `CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR`,
`TEST_ENCODES_STALE_CONTRACT`, `INTENTIONAL_COMPATIBILITY_BEHAVIOR`, and
`CONTRACT_UNRESOLVED`.

The Design also says “when Contract Verification is selected,” while the
current Test Engineering contract makes Contract Verification an internal
automatic gate when materially applicable. The non-selected catalog path is
therefore not sufficiently defined: it must be a pre-verification view or a
projection of an inapplicable result, not a second compatibility truth model.

This is `DRF-001`, a MEDIUM finding. The Design must define the mapping between
the four Stage F comparison outcomes and `CC-*` status/classification, the
automatic applicability rule, exact input ownership, and the non-authoritative
pre-adjudication display.

### Compatibility result model

**Result: FINDINGS**

The safety rule is correct: missing comparison data produces `INDETERMINATE`,
different incomparable surfaces produce `NOT_COMPARABLE`, and `COMPATIBLE`
requires a successful exact comparison. Exact revisions and baselines are
required.

The result remains blocked by `DRF-001` because result semantics cannot be
complete until their `CC-*` ownership/status mapping is explicit.

### External identity

**Result: PASS**

External systems use existing component/interface/interaction/store families
and external source qualification. The Design allows both a logical external
component identity and an external source binding, depending on evidence, while
rejecting configuration-only and dependency-only inference. No hidden external
identity family is introduced.

### Redaction policy

**Result: PASS**

The three classes `SECRET`, `SENSITIVE_INTERNAL`, and
`SAFE_TECHNICAL_IDENTIFIER` provide a usable projection boundary. Secret values
are never copied; evidence pointers remain useful; ordinary API paths, schema
and table names, event names, and logical service names remain available. The
policy conservatively handles private hostnames and credential-bearing URLs.

The future contract must choose one owning redaction policy and have evidence,
STM safe representation, and projections consume it; the Design's stated
boundary is coherent and does not create a second authority.

### Service documentation

**Result: PASS**

Extending the existing Technical Documentation projections is compatible with
the current package:

- provided interfaces;
- consumed interfaces;
- integrations and external systems;
- data/persistence, entities, access, and migration authority; and
- overview links, evidence, limitations, and unresolved states.

The user has an obvious path to answer what the service provides, calls, reads,
writes, owns, evolves, and cannot resolve. No STM internals are required.

### Product projections

**Result: PASS**

Product Interface Catalog, Integration Map, Data Access Map, External
Integrations Catalog, and optional Provider/Consumer Matrix are valid qualified
projections over Project-local STM and Product-scoped evidence. The Design
reuses exact Product baseline vectors, preserves Project-local authority, and
keeps unavailable/stale members dimension-specific. It does not merge same-text
interfaces or data resources without qualified Project identity and revision.

### Projection/package lifecycle

**Result: PASS**

The Design reuses `PRJ-*`, `RG-*`, `CURRENT`/`STALE`/`BLOCKED`, V1–V4,
dependency/selector snapshots, package policies, and explicit regeneration. It
does not redefine lifecycle meaning or auto-regenerate after semantic changes.

### Selector feasibility

**Result: PASS**

The current selector contract already permits controlled dimensions such as
`entity_type`, status, freshness, authority, `structured_properties`, and
formal relations. Stage F dimensions such as direction, resource kind,
interaction kind, access mode, precision, and Product-qualified scope fit as
additive structured properties/relations. Selectors remain finite,
deterministic, prose-free, and non-executable.

### Revalidation

**Result: PASS**

The bounded impact path is coherent for changed interface operations, consumer
expectations, data accesses, migration authority, Project availability, and
Product member revisions. Only affected facts, relations, projections, and
package scopes are revalidated. No full re-audit or automatic regeneration is
implied.

### Single-project compatibility

**Result: PASS**

The Service catalog works without Product identity, Product revision, Product
baseline, or cross-project membership. Product remains additive qualification,
not a required parent or degraded-mode wrapper.

### Stage E compatibility

**Result: PASS**

Product optionality, immutable baseline vectors, qualified Project authority,
external bindings, independent availability dimensions, additive `EXTEND`,
bounded `REVALIDATE`, no permission transfer, and Stage B projection/package
reuse are preserved.

### Historical compatibility

**Result: PASS**

The Design keeps old broad IF, DS, INT, EVENT, and Project-local facts valid,
does not rewrite IDs, and prevents silent enrichment. New selectors are required
to treat absent qualifiers as absent/unknown rather than exact.

The historical fallback is adequate for broad store-level facts and optional
Stage F qualifiers. The review does not find a destructive migration requirement.

### Identity/revision rules

**Result: PASS**

The Design gives explicit default rules for method/path changes, versions,
table renames, schema moves, Redis patterns, provider/consumer changes, and
evidence enrichment. It uses same identity plus revision for enrichment and new
identity plus `supersedes` when the semantic subject changes. It avoids both
silent merging and identity churn by allowing explicit continuity evidence.

### Cross-project identity

**Result: PASS**

Product matching cannot equate `GET /health`, table names, or schema names by
text alone. Qualified Project identity, local semantic identity, revision, and
Product baseline binding remain required for cross-project references and
matching.

### Architecture Review boundary

**Result: PASS**

Multiple writers, cross-owned writes, migration conflicts, runtime DDL, and
external dependencies remain STM facts until Architecture Review interprets
their consequence. Stage F contains no automatic `RF-*` rule.

### Test Engineering boundary

**Result: FINDINGS**

The Design correctly preserves Test Engineering ownership and points to
`BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, and `TASK-*`. However, its exact use of
`CC-*` for Stage F compatibility is incomplete for the reasons in `DRF-001`.
The current contract supports the boundary, but the Design must map Stage F
outcomes into the existing Contract Consistency Record rather than treating
the four new result values as a parallel semantic lifecycle.

### Code Quality boundary

**Result: PASS**

The Design only makes Code Quality a consumer of accepted technical facts and
preserves `CQ-*`/`CQRA-*` ownership. Product/API/Data catalogs do not aggregate,
create, or reinterpret Code Quality findings.

### Pressure scenarios PS-F01..PS-F26

The scenarios were evaluated against the Design as written. Scenarios marked
ambiguous expose the findings above; no scenario was a total semantic failure.

| Scenario | Result | Review note |
|---|---|---|
| PS-F01 | GREEN | Provider declaration maps to provided IF. |
| PS-F02 | GREEN | Consumer IF and INT can bind exact call and provider. |
| PS-F03 | AMBIGUOUS | Mismatch is preserved, but result-to-CC mapping is incomplete. |
| PS-F04 | GREEN | Unresolved operation precision is available. |
| PS-F05 | GREEN | Config-only base remains weak hint. |
| PS-F06 | GREEN | Unused generated client remains non-factual. |
| PS-F07 | AMBIGUOUS | DS/INT read exists, but relation derivation/source-of-truth is incomplete. |
| PS-F08 | GREEN | Cross-owned write remains fact, not RF. |
| PS-F09 | AMBIGUOUS | Multiple INT writes are possible, but relation synchronization is underspecified. |
| PS-F10 | GREEN | Migration authority and runtime writer can coexist. |
| PS-F11 | GREEN | Dynamic SQL can remain bounded/unresolved. |
| PS-F12 | GREEN | ORM ambiguity retains limitation. |
| PS-F13 | GREEN | Redis store-only precision is coherent for DS. |
| PS-F14 | GREEN | S3 address is evidence-gated. |
| PS-F15 | GREEN | Event does not require duplicate IF. |
| PS-F16 | GREEN | Webhook can use all three facts. |
| PS-F17 | GREEN | Secret-bearing connection string is redacted. |
| PS-F18 | GREEN | Private hostname receives safe identifier treatment. |
| PS-F19 | GREEN | Broad historical IF remains valid. |
| PS-F20 | GREEN | Broad historical DS remains valid. |
| PS-F21 | GREEN | Single-project catalog is first-class. |
| PS-F22 | GREEN | Product uses qualified exact Project revisions. |
| PS-F23 | GREEN | Product availability remains dimension-specific. |
| PS-F24 | GREEN | Provider change is impact-routed. |
| PS-F25 | GREEN | Weak hint cannot create accepted call. |
| PS-F26 | AMBIGUOUS | `INDETERMINATE` is correct, but CC ownership/result mapping is incomplete. |

```text
pressure_scenarios_total: 26
pressure_scenarios_green: 22
pressure_scenarios_ambiguous: 4
pressure_scenarios_fail: 0
```

### Adversarial scenarios AR-F01..AR-F15

| Scenario | Result | Review note |
|---|---|---|
| AR-F01 | GREEN | Declaration without implementation remains a compared view/limitation. |
| AR-F02 | AMBIGUOUS | Declared/implemented mismatch reaches CC, but Stage F result mapping is incomplete. |
| AR-F03 | GREEN | Exact Product baseline/revision qualification prevents silent reuse. |
| AR-F04 | GREEN | Identical operation text does not merge two providers. |
| AR-F05 | GREEN | Dynamic selection remains unresolved/qualified. |
| AR-F06 | GREEN | Schema is part of DS parent/address identity. |
| AR-F07 | GREEN | Migration continuity can use supersedes with evidence. |
| AR-F08 | AMBIGUOUS | DS callable resource versus IF callable contract is not explicitly related. |
| AR-F09 | AMBIGUOUS | Legacy relation versus new INT source-of-truth rule is incomplete. |
| AR-F10 | GREEN | Authority can exist without observed execution. |
| AR-F11 | GREEN | Runtime migration can be recorded without inferred authority. |
| AR-F12 | GREEN | Two weak hints do not compose into concrete use. |
| AR-F13 | GREEN | Safe path may remain while credential material is redacted. |
| AR-F14 | GREEN | Unavailable and stale Product members remain separate dimensions. |
| AR-F15 | AMBIGUOUS | Candidate indeterminacy is represented, but compatibility ownership mapping is incomplete. |

```text
adversarial_scenarios_total: 15
adversarial_scenarios_green: 11
adversarial_scenarios_ambiguous: 4
adversarial_scenarios_fail: 0
```

### Migration assessment

**Result: FINDINGS**

The claimed `COMPATIBLE_EXTENSION` direction is otherwise justified: old IDs
remain, optional fields may be absent, Product conversion is not required, DS
children are additive, and historical facts are not silently enriched.

The classification cannot be accepted as a final Design baseline until the
five/related semantic ambiguities are closed. In particular, relation authority,
CC result mapping, and callable/precision applicability must be clarified so
that implementation does not create conflicting meanings. These are compatible
extensions once resolved; they do not currently prove a destructive migration
or foundational redesign.

### Implementation boundary

**Result: PASS**

The Design preview identifies the likely semantic surfaces without turning them
into an implementation plan: shared STM, possibly shared evidence, dependency
selectors, Technical Documentation, projection/dependency lifecycle, package
declarations, Product qualification, Contract Verification/Test Engineering,
Architecture consumption, and later pressure scenarios. It explicitly defers
exact file changes and does not modify implementation or normative files.

### Findings

#### DRF-001 — Compatibility result has no closed `CC-*` mapping

**Severity:** MEDIUM
**Design sections:** 20, 31, 37
**Evidence:** The Design defines `COMPATIBLE`, `INCOMPATIBLE`, `INDETERMINATE`,
and `NOT_COMPARABLE`, says an accepted result is owned by `CC-*`, and says
Contract Verification is used “when selected.” The current
`capabilities/test-review/references/test-engineering-contract.md` defines
`CC-*` status/classification, compared views, mismatch, and adjudication, and
makes Contract Verification automatic when materially applicable; it does not
map the new result vocabulary or establish a non-selected compatibility truth
path.

**Failure scenario:** A provider/consumer pair is compared. One implementation
stores a Stage F `INCOMPATIBLE` result as a `CC-*` classification, another stores
it as a non-authoritative catalog comparison, and a third treats automatic
Contract Verification as not run because no report was selected. Product and
Service projections can then show different compatibility truth for the same
exact IF revisions.

**Why it matters:** This creates two incompatible semantic paths at the
Test Engineering boundary and can make compatibility appear authoritative in a
projection or disappear from the accepted `CC-*` record.

**Required Design remediation:** Define the exact mapping from Stage F result
values to existing `CC-*` status/classification/adjudication fields; state that
Contract Verification runs automatically when its current applicability rule is
met; and define the non-authoritative pre-adjudication view as input/candidate
information that cannot compete with accepted `CC-*`.

**Re-review:** Targeted compatibility/Test Engineering re-review.

#### DRF-002 — `contract_role` and `observed_view` lack a validity matrix

**Severity:** MEDIUM
**Design sections:** 6, 7, 18
**Evidence:** The Design adds four `contract_role` values while retaining the
four existing `observed_view` values, but defines only recommended examples and
does not declare valid/invalid combinations or tested-role semantics.

**Failure scenario:** A record is accepted as
`CONSUMER_EXPECTATION + IMPLEMENTED`, or as
`PROVIDER_IMPLEMENTATION + CONSUMED`, and a projection interprets the pair as
both a provider implementation and an observed consumer dependency. The same
ambiguity affects provider/consumer contract tests.

**Why it matters:** Two dimensions that are intended to be orthogonal become a
second, partially overlapping lifecycle with no deterministic validation rule.

**Required Design remediation:** Define a closed compatibility matrix or an
explicit rule that `contract_role` is a perspective constraint while
`observed_view` is an evidence view, including valid `TESTED` combinations for
provider declarations, implementations, consumer expectations, and observed
use. Invalid combinations must be rejected or represented as unresolved
evidence, not accepted silently.

**Re-review:** Targeted IF/Contract Verification re-review.

#### DRF-003 — `READS_FROM`/`WRITES_TO` derivation and conflict ownership is incomplete

**Severity:** MEDIUM
**Design sections:** 10, 12, 14, 37
**Evidence:** The Design says INT owns access and that existing relations are
“derived/attached views” when INT exists, while also allowing a relation without
INT to remain a broad accepted fact. The current STM contract treats controlled
relations as semantically meaningful links but does not provide this derivation
rule.

**Failure scenario:** A historical `READS_FROM` relation remains accepted while
a new INT says `WRITE`, or an INT says `READ_WRITE` while only a READ relation is
materialized. Different consumers use the relation and INT as authority and
produce conflicting Service/Product maps.

**Why it matters:** The Design has not closed the source-of-truth, derivation,
materialization, conflict, and historical fallback semantics for a central data
catalog relation.

**Required Design remediation:** State that new precise data access is authored
as INT, define whether relation rows are semantic derived records or projection
views, specify how legacy broad relations coexist, define READ_WRITE expansion
and conflict precedence, and define the bounded revalidation path for
contradictions. Do not use dependency metadata for this purpose.

**Re-review:** Targeted data-relation/STM re-review.

#### DRF-004 — `STORE_ONLY` is incorrectly shared as an IF precision value

**Severity:** MEDIUM
**Design sections:** 6, 8, 17, 37
**Evidence:** The common IF record permits `STORE_ONLY`, and the protocol
property section says an unsupported protocol field may produce `STORE_ONLY`.
The Design itself defines `STORE_ONLY` as “the store/system is known, but
entity-level target is not established.”

**Failure scenario:** A REST interface has an unresolved method or GraphQL
operation. The implementation assigns `STORE_ONLY`, which is a data-resource
precision, and a selector treats it as a valid IF precision. Interface catalogs
then mix store-only data facts with unresolved interface operations.

**Why it matters:** A shared enum value with family-inapplicable meaning makes
selectors and projections semantically ambiguous and can cause false filtering.

**Required Design remediation:** Constrain precision applicability by family or
define a family-neutral replacement. At minimum, `STORE_ONLY` must apply only to
DS facts and data-access INT facts; IF facts should use `EXACT`,
`RESOURCE_BOUNDED`, or `UNRESOLVED` unless a distinct interface precision is
defined.

**Re-review:** Targeted precision/selector re-review.

#### DRF-005 — Database callable contract versus DS resource is not explicit

**Severity:** MEDIUM
**Design sections:** 6, 10, 11, 14, 37
**Evidence:** Procedures/functions are DS resource kinds and are targeted by
`INT access_mode=EXECUTE`, while IF-* remains a material callable boundary, but
the Design does not state when both representations are required or how their
identities and contract references relate.

**Failure scenario:** A stored procedure has a public callable contract and a
database schema-object identity. One implementation creates only DS; another
creates IF and DS with unrelated identities; a third treats IF as the procedure
resource. Catalogs and compatibility verification disagree about the callable
surface.

**Why it matters:** The boundary can create duplicate factual authority or omit
the callable contract needed for provider/consumer comparison.

**Required Design remediation:** Explicitly define DS as the database-owned
resource identity, IF as the callable boundary only when independently material,
and INT as the execute edge; require explicit cross-reference rather than
identity aliasing. Define when DS-only is sufficient.

**Re-review:** Targeted database callable-boundary re-review.

### Findings summary

HIGH: 0
MEDIUM: 5
LOW: 0

finding_ids: `DRF-001`, `DRF-002`, `DRF-003`, `DRF-004`, `DRF-005`

### Review dimensions

| Dimension | Result |
|---|---|
| baseline_integrity | PASS |
| design_scope_integrity | PASS |
| authority_model | PASS |
| if_extension_assessment | PASS |
| provider_consumer_assessment | PASS |
| contract_role_observed_view_assessment | FINDINGS |
| protocol_property_assessment | PASS |
| event_relationship_assessment | PASS |
| int_model_assessment | PASS |
| data_relation_authority_assessment | FINDINGS |
| ds_resource_model_assessment | PASS |
| db_callable_boundary_assessment | FINDINGS |
| ds_parent_child_assessment | PASS |
| data_access_mode_assessment | PASS |
| migration_authority_assessment | PASS |
| sql_model_assessment | PASS |
| non_sql_model_assessment | PASS |
| evidence_strength_assessment | PASS |
| precision_model_assessment | FINDINGS |
| matching_boundary_assessment | PASS |
| compatibility_authority_assessment | FINDINGS |
| compatibility_result_assessment | FINDINGS |
| external_identity_assessment | PASS |
| redaction_policy_assessment | PASS |
| service_documentation_assessment | PASS |
| product_projection_assessment | PASS |
| projection_lifecycle_assessment | PASS |
| package_authority_assessment | PASS |
| selector_feasibility_assessment | PASS |
| revalidation_assessment | PASS |
| single_project_compatibility | PASS |
| stage_e_compatibility | PASS |
| historical_compatibility | PASS |
| identity_revision_assessment | PASS |
| cross_project_identity_assessment | PASS |
| architecture_review_boundary | PASS |
| test_engineering_boundary | FINDINGS |
| code_quality_boundary | PASS |
| pressure_scenario_assessment | FINDINGS |
| adversarial_scenario_assessment | FINDINGS |
| migration_assessment | FINDINGS |
| implementation_boundary_assessment | PASS |
| foundational_completeness | FINDINGS |

### Recommended next gate

`STAGE_F_DESIGN_REMEDIATION`

The remediation should be targeted to the five findings and then receive a
fresh Independent Design Review. It must not begin implementation or an
Implementation Plan before the corrected Design passes review.

### Final verdict

`STAGE_F_DESIGN_REVIEW_FINDINGS`

The Design has the correct overall architecture and is close to complete, but
it is not yet an authoritative Stage F Design baseline. The five MEDIUM
findings are semantic closure issues, not requests for a new identity family or
a different architecture direction.
