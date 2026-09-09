# API Input Robustness & Boundary Validation — Design

## Goal

Extend the existing review system so it can identify API input-boundary gaps
using static and contract evidence and can generate concrete negative and
boundary test cases. The extension covers request bodies, fields, collections,
uploads, protocol metadata, parsers, and validation ordering. It must expose the
canonical failure in which a field has a schema limit but a server can buffer a
multi-gigabyte request before applying that limit.

The design adds an API input robustness aspect to existing Code Quality Review
and an API boundary test dimension to existing Test Engineering. It does not
add a new top-level capability or change the meaning of existing facts,
findings, projections, lifecycle states, or authorities.

## Non-goals

Version 1 is limited to static analysis, contract analysis, and generated
negative/boundary test cases. Runtime execution is unavailable. The system does
not send attack payloads, run active fuzzing or DAST, generate an automatic
2 GiB request, run load tests, execute parser or decompression bombs, provision
environments, crawl live endpoints, or discover APIs automatically at runtime.
It also does not build a framework-specific scanner, generic parser, DSL,
simulation framework, or new validation engine.

Runtime execution, active fuzzing, and live endpoint validation remain
`UNAVAILABLE` unless a separately approved future stage authorizes them.

## Authority ownership

The three semantic top-level capabilities remain exactly:

1. Architecture Review;
2. Test Engineering;
3. Code Quality Review.

The extension uses the existing `requested_work` and `resolved_work` model.
Selecting a boundary analysis output or CQ-owned output is requested work only
when the applicable existing routing rules say so. Internal STM, evidence,
Behavior Model, Technical Documentation, and Contract Verification dependencies
are resolved work and never become implicit selected capabilities.

### Stage F relationship

Stage F / Interface, API & Data Integration Catalog remains factual authority
for what API and interface facts exist. It may record or qualify:

- endpoint, method, operation, and protocol;
- request and response media types;
- request schemas, field types, declared constraints, and requiredness;
- provider, consumer, Project, Product, revision, and baseline qualifiers;
- implementation observations and their provenance;
- observed configuration or code evidence relevant to a boundary.

Stage F may expose a declared limit, an observed implementation claim, or an
unknown/unavailable qualifier. It does not decide whether the implementation is
safe, assign CQ severity, or establish enforcement merely because a schema
contains a constraint.

Boundary metadata is optional evidence on existing interface facts. Missing
metadata does not invalidate an old Stage F fact and does not establish a
finding by itself.

### Code Quality relationship

Code Quality Review owns conclusions about what is poorly or unsafely
implemented. API input robustness is a CQ review aspect, not a new semantic
capability. CQ findings cite accepted STM/interface facts and shared evidence;
they do not rewrite those facts.

The controlled v1 finding classes are:

`MISSING_REQUEST_SIZE_LIMIT`, `UNBOUNDED_STRING`, `UNBOUNDED_COLLECTION`,
`UNBOUNDED_UPLOAD`, `SCHEMA_NOT_ENFORCED`, `VALIDATION_AFTER_MATERIALIZATION`,
`UNEXPECTED_FIELD_ACCEPTANCE`, `PARSER_RESOURCE_EXHAUSTION`,
`UNBOUNDED_PAGINATION`, `UNBOUNDED_NUMERIC_INPUT`, `UNBOUNDED_NESTING`,
`UNBOUNDED_MULTIPART`, and `COMPRESSION_EXPANSION_RISK`.

These are finding classifications within the existing CQ finding model. They
are not identity families, factual families, lifecycle states, authorities, or
security capabilities. A security-relevant consequence may be described in a
CQ finding without creating a separate Security Review owner.

### Test Engineering relationship

Test Engineering owns what must be proven. Its existing Test Assurance,
Behavior Model, Contract Verification, `BC-*`, `CC-*`, `MAT-*`, `TM-*`, and
`GAP-*` semantics remain in force. The extension supplies boundary dimensions
and generated case records to the existing Test Engineering workflow.

Contract Verification remains the applicability mechanism for contract
comparison and compatibility. Boundary cases do not create a compatibility
authority and do not turn a generated case into runtime execution. A generated
case can be proposed or accounted for even when execution is unavailable; its
execution status and limitations remain explicit.

## Two-layer boundary model

Every applicable API input analysis distinguishes two independent layers:

1. **TRANSPORT / CONTAINER BOUNDARY** — limits before or during request
   container handling, such as HTTP body bytes, compressed bytes, headers,
   query/cookie aggregate size, multipart count, upload bytes, parser nesting,
   and decompression expansion.
2. **SCHEMA / FIELD BOUNDARY** — limits on the decoded representation, such as
   string length, array item count, object properties, numeric range,
   requiredness, media type, and unknown-field policy.

The analysis follows this model:

```text
request arrives
  → transport/server/framework limit
  → parser or materialization
  → schema validation
  → business processing
```

The two layers are complementary. A `maxLength: 255` field constraint does not
substitute for a 1 MiB request-body limit. If the server buffers the complete
request before schema validation, a 2 GiB string can consume resources before
the field validator rejects it. Conversely, a transport limit does not prove
that individual fields, collections, numeric values, or nesting are acceptable.

For every boundary claim, evidence records the applicable layer, scope,
enforcement point, and whether rejection is expected before materialization,
after parsing, at schema validation, or later. If the actual enforcement point
is not evidenced, the result is `ENFORCEMENT_UNKNOWN` or
`VALIDATION_ORDER_UNKNOWN`; the review does not assume safety.

## Controlled taxonomy

The following are controlled `boundary_category` and Test Engineering
`boundary_dimension` values. They are dimensions of existing facts, CQ
findings, and test cases rather than new identity families:

| Category | Primary layer | Typical question |
|---|---|---|
| `REQUEST_BODY_SIZE` | transport/container | Is the complete request body bounded before materialization? |
| `STRING_LENGTH` | schema/field | Is each relevant string length bounded and enforced? |
| `COLLECTION_SIZE` | schema/field | Are array items or object properties bounded? |
| `NUMERIC_RANGE` | schema/field | Are numeric values bounded before resource-sensitive use? |
| `NESTING_DEPTH` | both | Is recursive decoded structure bounded before expensive traversal? |
| `UPLOAD_SIZE` | transport/container | Are uploaded bytes bounded before storage or buffering? |
| `MULTIPART_LIMITS` | transport/container | Are parts, headers, fields, and aggregate bytes bounded? |
| `HEADER_LIMITS` | transport/container | Are header count and aggregate/per-header sizes bounded? |
| `QUERY_LIMITS` | both | Are query count, size, and parameter values bounded? |
| `COOKIE_LIMITS` | transport/container | Are cookie count and aggregate size bounded? |
| `CONTENT_TYPE` | transport/container | Are accepted media types explicit and rejected otherwise? |
| `MALFORMED_PAYLOAD` | parser | Is malformed input rejected at a bounded parser boundary? |
| `UNEXPECTED_FIELDS` | schema/field | Is the unknown-property policy explicit and enforced? |
| `SCHEMA_ENFORCEMENT` | schema/field | Does the request path actually invoke the declared validator? |
| `VALIDATION_ORDER` | ordering | Does validation occur before unsafe materialization or processing? |
| `PARSER_RESOURCE_EXHAUSTION` | parser | Are parser recursion, token, expansion, or allocation risks bounded? |
| `COMPRESSION_EXPANSION` | transport/container | Is compressed input bounded by compressed and expanded limits? |
| `PAGINATION_LIMITS` | schema/query | Are page, offset, cursor, and page-size values bounded? |

One input can have multiple categories. For example, a compressed JSON upload
can have `COMPRESSION_EXPANSION`, `REQUEST_BODY_SIZE`, `NESTING_DEPTH`, and
`SCHEMA_ENFORCEMENT` observations. The category does not imply a finding: the
finding depends on evidence, context, and the relevant expected boundary.

## Evidence semantics

Boundary observations reuse the existing evidence provenance and strength
model: `DIRECT_DECLARATION`, `STRONG_INFERENCE`, and `WEAK_HINT`. They also
record a state for the proposition being evaluated:

- `DECLARED` — a contract or configuration states a limit or policy, such as
  OpenAPI `maxLength: 255`, a server maximum body size of 1 MiB, or an explicit
  unknown-field policy;
- `IMPLEMENTED` — code or an evidenced framework/server configuration shows
  that the relevant request path enforces the declaration at the stated point;
- `TESTED` — an existing executable test or accepted Test Engineering case
  proves the boundary. In v1, execution may remain unavailable, so a generated
  case is not `TESTED` merely because it was created.

The useful result is the combination, not a precedence rule. An OpenAPI
declaration is not implementation evidence. A frontend `maxlength` is a
`WEAK_HINT` about client behavior and cannot establish server enforcement. A
documented framework API whose configured value and active path are evidenced
can be `STRONG_INFERENCE`, but an undocumented or deployment-dependent default
is `ENFORCEMENT_UNKNOWN`. Field schema evidence never establishes a transport
limit, and a proxy declaration does not prove the application is protected if
the app is directly reachable.

Evidence should identify the exact interface, input location, Project/source
revision, configuration/code path, and provenance. For multi-hop systems,
record the relevant limits at each reachable boundary; the effective early
limit is not silently substituted for missing downstream evidence.

## Finding semantics

An API input robustness finding uses the existing CQ finding authority and
expresses at least:

```text
finding_class: <controlled CQ class>
interface: <qualified IF-* or exact endpoint reference>
input_location: <body, field, upload, query, header, cookie, or parser scope>
boundary_category: <controlled category>
observed_state: <DECLARED | IMPLEMENTED | TESTED | UNKNOWN combination>
expected_boundary: <context-derived boundary or unresolved>
evidence: <exact evidence/provenance references and strength>
impact: <concrete resource, correctness, or assurance consequence>
recommendation: <bounded corrective direction>
severity: <LOW | MEDIUM | HIGH with rationale>
```

The finding may classify the observed condition as `UNBOUNDED`,
`DECLARED_ONLY`, `DECLARED_BUT_NOT_ENFORCED`, `ENFORCEMENT_UNKNOWN`, or
`ENFORCED`. These labels describe evidence state; they do not replace CQ
finding classes or create a new lifecycle.

The review identifies a missing bound, an implausibly broad bound, a declared
but unenforced bound, or unknown enforcement without inventing a business
requirement. There is no universal rule that every string must be 255 bytes.
The expected boundary must come from the accepted contract, implementation
context, explicit policy, resource budget, or a clearly bounded review
assumption. If none exists, the recommendation can request a bound while the
numeric threshold remains unresolved.

For the motivating case, a finding can state: the endpoint accepts JSON and a
field has a schema maximum, but no request-body limit or pre-materialization
enforcement is evidenced; the impact is resource consumption before schema
rejection; the recommendation is to enforce a bounded transport/framework
limit before full materialization. It must not claim a runtime exploit was
executed.

## Generated test-case semantics

Test Engineering may derive a case from accepted interface facts, CQ findings,
and explicit review assumptions using the existing test/verification artifact
model. A compact generated case has this shape:

```text
test_id: NEG-API-<stable case key>
interface: <qualified interface reference>
input_location: <exact location>
boundary_dimension: <controlled category>
precondition: <required route/configuration state>
input_class_or_value_strategy: <type-aware construction>
expected_rejection_or_acceptance: <precise outcome>
expected_rejection_stage: <transport | parser | schema | processing | UNKNOWN>
evidence_basis: <declaration/implementation/test references and strength>
open_assumptions: <bounded unresolved facts, or NONE>
execution_status: PROPOSED | EXECUTED | UNAVAILABLE
```

`NEG-API-*` is a case identifier convention, not a new authority family. A
case must say whether it is negative, boundary acceptance, or boundary
rejection. For example, `STRING_LENGTH` at `maxLength + 1` expects a 4xx schema
rejection when the exact maximum and validator path are evidenced. A body above
an evidenced transport maximum expects rejection before complete
application-level materialization. If no numeric maximum is known, the case
may be proposed using “above the configured maximum once identified”, but it
must retain an unresolved assumption and must not invent a threshold.

Generated cases do not grant authorization to send requests, execute tests,
modify code, or access runtime environments. Any execution remains separately
authorized and is unavailable in this v1 design.

## Boundary-value generation

When an exact bound is accepted, generation is deterministic and type-aware:

- numeric minimum/maximum: `min - 1`, `min`, `min + 1`, `max - 1`, `max`,
  `max + 1` where the type and range make each value meaningful;
- string or byte length: lengths immediately below, at, and above the exact
  bound;
- arrays/collections: item counts immediately below, at, and above the exact
  `minItems`/`maxItems` or equivalent;
- request bodies/uploads: byte sizes immediately below, at, and above the
  exact transport/upload bound, without automatically creating the payload;
- pagination: valid lower/upper values and just-outside values for page,
  offset, limit, or cursor dimensions;
- enum: valid member and unsupported member;
- required values: present, absent, and null distinctions only where the
  accepted contract defines them.

Generation omits nonsensical candidates, respects integer/string/byte semantics,
and records unknown limits instead of fabricating values. Boundary cases for
compressed content distinguish compressed size from expansion size. Recursive,
multipart, header, cookie, and parser cases use counts/depths only when a
corresponding exact or proposed policy is evidenced.

## Static implementation checks

The v1 review applies framework-agnostic, evidence-first checks to the
available code, configuration, contracts, and accepted STM observations. It
may identify:

- a body parser with no evidenced maximum;
- reliance on an undocumented or deployment-dependent framework default;
- buffering/materialization before validation;
- upload handlers without byte, part, or count limits;
- strings, collections, pagination, or numeric inputs without relevant
  validation;
- a schema whose request path bypasses the validator;
- validation present only in frontend/UI code;
- permissive unknown fields where the accepted contract requires rejection;
- recursive/nested parsing without an evidenced depth/resource boundary;
- decompression before bounded compressed and expanded-size enforcement.

These are review patterns, not a requirement for AST analyzers or a framework
catalog in v1. A static conclusion is limited by the evidence actually
available. Missing runtime or deployment evidence remains a stated limitation.

## Severity guidance

Severity is evidence- and context-dependent and remains separate from
correctness verification.

- `HIGH` may be appropriate when an externally reachable, credible resource-
  exhaustion path is evidenced, such as a materially unbounded body before
  materialization, unrestricted upload with serious resource impact, or a
  declared validator systematically bypassed on the live request path.
- `MEDIUM` may be appropriate for an important unbounded string/collection,
  pagination or numeric input, missing multipart/expansion protection, or a
  material enforcement gap whose runtime condition is not fully reproduced.
- `LOW` may be appropriate when a defense-in-depth boundary is absent but an
  effective, evidenced hard boundary limits the relevant impact.

A missing `maxLength` is not automatically HIGH. Severity must explain the
reachable path, affected resource, evidence strength, and whether the boundary
is transport-level, parser-level, schema-level, or only a test gap.

## Product and single-project behavior

The design works in a product-free single Project and in an explicitly
selected Product-qualified review. Single-project analysis remains first-class
and does not require Product state. Each finding and generated case retains the
exact Project, repository/source revision, baseline, interface identity, and
evidence qualification needed to support its claim.

Product mode is optional context and qualification. Product membership does not
grant repository read, source admission, test execution, runtime, semantic
write, or deployment permissions. Product-qualified API findings are qualified
views over the contributing Projects and exact baselines; they do not create a
Product factual authority or a duplicate interface identity. If member Projects
have different limits, the result preserves each member's evidence and reports
the cross-project limitation or weakest evidenced boundary rather than
silently treating one Project's limit as universal.

Unavailable Project/source/configuration evidence remains unavailable. It is
not evidence that a limit is absent and does not become a clean or safe result.

## Backward compatibility and preserved boundaries

This is a compatible extension. Historical Stage F facts remain valid even if
they lack boundary metadata; they may be insufficient to establish boundary
safety. No historical artifact, Project record, Product revision, `IF-*`,
`CC-*`, existing CQ finding, or projection is rewritten solely to add this
design. New observations and findings use new revisions or records under the
existing lifecycle rules.

The extension preserves:

- Stage F and STM as factual authorities;
- Code Quality as finding authority;
- Test Engineering as test and verification authority;
- the existing Contract Verification and CC compatibility route;
- Product optionality and single-project behavior;
- existing projection lifecycle and `requested_work`/`resolved_work` rules;
- authorization separation, redaction, and safe rendering boundaries;
- the unsupported runtime execution boundary.

Boundary analysis does not imply code modification, worktree creation, commit,
push, PR, deployment, runtime scanning, or test execution. Secrets remain
omitted/redacted under the existing evidence and rendering contracts.

## Acceptance scenarios

The following bounded scenarios define the v1 acceptance set. Each result must
identify the applicable owner, evidence state, boundary layer, and limitation.

| # | Scenario | Required result |
|---:|---|---|
| 1 | String `maxLength` is present and enforced on the request path | Stage F records declaration; CQ does not claim a missing bound; TE generates exact boundary cases. |
| 2 | String `maxLength` is absent | CQ may report `UNBOUNDED_STRING` only with contextual evidence; no universal threshold is invented. |
| 3 | String maximum exists but request-body transport limit is unknown | Separate field and transport states; body enforcement remains unknown. |
| 4 | A 2 GiB string can be buffered before validation | CQ reports the ordering/body risk when evidence supports it; no runtime 2 GiB request is generated. |
| 5 | Body transport limit is lower than practical field maximum | Early transport boundary and later field boundary are both represented; neither substitutes for the other. |
| 6 | Array `maxItems` is absent | CQ may report `UNBOUNDED_COLLECTION` with the exact location and evidence. |
| 7 | Pagination limit is absent | CQ may report `UNBOUNDED_PAGINATION`; TE proposes type-aware cases with unresolved threshold. |
| 8 | Upload size is absent | CQ may report `UNBOUNDED_UPLOAD` and identify buffering/storage impact. |
| 9 | UI `maxlength` exists but backend validation is absent | UI evidence remains a weak hint; server enforcement is unresolved or missing. |
| 10 | OpenAPI declares `maxLength` but implementation bypasses the validator | Stage F declaration remains factual; CQ reports `SCHEMA_NOT_ENFORCED`. |
| 11 | Wrong `Content-Type` is submitted | TE proposes an explicit media-type rejection case when accepted media types are known. |
| 12 | Malformed JSON is submitted | TE proposes parser rejection and records the expected parser stage when evidenced. |
| 13 | Unexpected fields are accepted | CQ reports `UNEXPECTED_FIELD_ACCEPTANCE` only when the contract's unknown-field policy supports that conclusion. |
| 14 | JSON is deeply nested | `NESTING_DEPTH` and parser/resource evidence are distinguished; unknown depth protection remains unresolved. |
| 15 | Multipart part count is missing | CQ may report `UNBOUNDED_MULTIPART`; TE proposes count/aggregate cases without invented limits. |
| 16 | Compressed payload expansion protection is unknown | CQ reports `COMPRESSION_EXPANSION_RISK` when the path is evidenced; compressed and expanded sizes remain separate. |
| 17 | API is analyzed in one Project | Analysis is valid without Product and retains exact Project/source qualification. |
| 18 | API is analyzed in an explicitly selected Product | Findings/cases are Product-qualified views over exact member Project baselines; membership grants no permissions. |
| 19 | Exact maximum is known | TE generates deterministic below/at/above boundary candidates appropriate to the type. |
| 20 | Numeric maximum is unknown | TE proposes a case with an unresolved threshold and does not invent a number. |
| 21 | Runtime fuzzing is requested | The request is explicitly `UNAVAILABLE`; v1 produces no active execution. |
| 22 | No API evidence is available | No interface or boundary finding is fabricated; the limitation is recorded. |
| 23 | Header/query/cookie count or size is bounded | Transport/container and query-specific cases are generated from the exact bound. |
| 24 | `Content-Length` is absent and transfer is chunked | The analysis checks configured streaming/aggregate limits; absent length alone is not treated as safe or unsafe. |
| 25 | Gateway rejects earlier than the application | Gateway evidence is recorded separately; application enforcement is not inferred unless reachable paths are qualified. |
| 26 | Validation occurs after expensive deserialization | CQ reports `VALIDATION_AFTER_MATERIALIZATION` or parser risk according to the evidenced order. |
| 27 | Consumer sends data larger than provider contract | Existing Contract Verification/CC handles contract comparison; CQ boundary findings remain separately owned. |
| 28 | Streaming upload uses different limits from buffered JSON | Each input path has its own qualified boundary record and generated cases. |

## Pressure scenarios and resolutions

The design is pressure-tested against these cases. Each resolution is a
constraint on interpretation, not a new runtime mechanism.

| # | Pressure case | Resolution |
|---:|---|---|
| 1 | Frontend validates but backend does not | Frontend is `WEAK_HINT`; server enforcement remains unknown/missing and CQ/TE retain the gap. |
| 2 | OpenAPI says `maxLength` but code skips the schema | Declaration and implementation are separate; report `SCHEMA_NOT_ENFORCED`. |
| 3 | Framework default has a limit but deployed value is not evidenced | Do not promote the default to implementation evidence; classify enforcement unknown. |
| 4 | Streaming upload and buffered JSON have different protection | Qualify by input path and layer; do not generalize one route's limit. |
| 5 | Reverse proxy has a body limit but app is directly reachable | Analyze every reachable ingress; proxy protection does not prove direct-app protection. |
| 6 | Product projects have different body limits | Preserve Project-qualified evidence and disclose divergence; Product does not flatten limits. |
| 7 | Consumer sends larger data than provider contract | CC owns compatibility; boundary CQ findings and generated TE cases remain independent. |
| 8 | API gateway rejects before application | Record gateway boundary and expected stage; do not claim application validation ran. |
| 9 | Schema precision is unknown | Keep expected values/stage unresolved and generate no fabricated threshold. |
| 10 | Multipart and JSON limits differ | Use separate category records and cases for each media/container path. |
| 11 | GraphQL or equivalent request is deeply nested | Use `NESTING_DEPTH` and parser/resource categories without inventing a GraphQL authority. |
| 12 | Millions of tiny array items evade byte-size intuition | Check item-count and downstream allocation boundaries separately from body bytes. |
| 13 | Tiny compressed input expands massively | Require evidence for compressed and expanded limits; classify expansion risk when absent. |
| 14 | Numeric values trigger allocation/resource blow-up | Treat numeric range and resource-sensitive use separately; no arbitrary numeric policy is invented. |
| 15 | `Content-Length` is absent or transfer is chunked | Require an aggregate streaming/container boundary or report it unknown; header presence is not the limit. |
| 16 | Validation follows expensive deserialization | Use evidence of ordering to report late validation and expected parser/materialization impact. |

These resolutions close the main ambiguity classes: evidence is qualified by
path and revision, transport and schema are not conflated, and absence or
unknown state never becomes a fabricated safe result.

## Migration classification

`COMPATIBLE_EXTENSION` is the correct classification. Existing facts and
historical artifacts remain interpretable. Boundary metadata is optional, and
its absence can limit a new finding or generated case without invalidating the
fact. Product remains optional. No runtime execution or new permission is
required. New boundary observations, CQ findings, and Test Engineering cases
are additive and follow existing revisions, freshness, provenance, redaction,
and acceptance rules. No historical artifact or existing Stage F fact is
rewritten.

## Implementation implications

Future implementation should be a small extension to the existing Stage F,
Code Quality, and Test Engineering routing and evidence contracts. It should
reuse existing `IF-*`, STM observations, evidence strength, CQ finding shape,
Test Engineering case/assurance records, Contract Verification applicability,
Product qualification, projection lifecycle, authorization, and redaction.

The implementation should add controlled boundary dimensions and deterministic
checks to existing workflows, not a fourth capability, parallel fact ledger,
new projection identity family, runtime API engine, fuzzing system, parser,
DSL, or harness. It should make the two-layer boundary and enforcement stage
visible in the relevant evidence and finding records, preserve unresolved
limitations, and keep generated cases useful even when execution is
unavailable. The eventual feature can therefore be delivered as one bounded
feature branch with a small number of semantic blocks and existing validation
mechanisms.
