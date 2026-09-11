# Code Quality semantic contract

This reference defines the semantic authority owned by Code Quality Review. It
does not implement orchestration, projection generation, source modification,
or a static-analysis toolchain.

## Authority and identity

Code Quality owns accepted, materially consequential implementation-quality
findings identified as `CQ-*`. It also owns Code Quality remediation actions
identified as `CQRA-*`; their lifecycle and state axes are defined in
`code-quality-lifecycle.md`.

The following are not Code Quality semantic authority:

- tool warnings, metrics, grep hits, AST matches, or heuristic hits;
- `EV-*` observations or `WS-*` worksets;
- STM facts;
- Architecture `RF-*` findings;
- Test Engineering `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, or `TASK-*`;
- generated reports, summaries, hotspots, package manifests, or
  `working/INDEX.md`.

### Product-scoped CQ and CQRA

Product mode is opt-in. A Product-scoped finding uses the existing `CQ-*`
family with `scope_kind: PRODUCT` and a stable allocation in the disjoint
`PRODUCT:<PROD-*>` namespace. A Product-scoped remediation action uses the
existing `CQRA-*` family and the same Product namespace rule. The Product
allocation is keyed by stable Product identity, not by a transient revision,
and cannot collide with the local `REPOSITORY:<repository>` namespace. Local
IDs and their selectors remain unchanged.

Product `CQ-*` acceptance requires all of the following as one semantic tuple:

- selected Product identity and revision;
- immutable Product baseline;
- affected Project identities and qualified source bindings;
- contributing `WS-*`/`EV-*` evidence and relevant accepted STM facts;
- a material consequence that spans Projects rather than repeated local text;
- Code Quality ownership and independent adjudication;
- lifecycle, freshness, dependencies, and provenance.

Product participation, membership, correlation, or a grouped summary is not
materiality and cannot create a Product finding. Project-local CQ findings
remain Project-scoped. A Product `CQRA-*` is permitted only for one genuinely
coordinated action spanning named Projects; it records its owner, scope,
dependencies, evidence, and lifecycle, and completion does not resolve or
supersede a linked CQ or local CQRA.

Product Code Quality interpretation remains Code Quality-owned even when
evidence crosses Project boundaries. It does not create `RF-*` or Test
Engineering authority. A Product finding is `STALE` or `BLOCKED` when its
Product baseline or required evidence is no longer valid, using the lifecycle
rules below; this does not silently invalidate independent local findings.

`CQ-<repository-scoped stable allocation>` is stable, persistent, and carries
no category, severity, location, or confidence. A candidate receives a CQ
identity only when accepted as semantic authority. Revalidation retains the
identity when the mechanism remains the same across a move, rename, or
semantics-preserving refactor. A materially different mechanism receives a new
identity; supersession records the relationship rather than mutating one
finding into another.

## Accepted finding contract

An accepted `CQ-*` record must contain, or reference, all of the following:

| Field | Semantic requirement |
|---|---|
| `identity` | Stable `CQ-*` identity. |
| `scope` | Explicit repository, package, component, file, symbol, or focused scope. |
| `category` | One primary language-neutral taxonomy category; secondary tags may add context. |
| `mechanism` | Concrete implementation pattern or mechanism under review. |
| `evidence` | Direct source evidence and addressable `EV-*` observations where used. |
| `consequence` | Concrete maintainability, change-cost, defect, reliability, testability, operational, or security-adjacent consequence. |
| `materiality` | Adjudication that the issue warrants persistent CQ authority. |
| `severity` | CQ consequence severity, independent of materiality and confidence. |
| `confidence` | Certainty of the observation and interpretation. |
| `applicability` | `APPLICABLE`, `NOT_APPLICABLE`, or `EXCLUDED`. |
| `disposition` | `FALSE_POSITIVE`, `ACCEPTED_EXCEPTION`, or `WONT_FIX` where applicable. |
| `source_bindings` | Baseline, file/symbol/content, dependency, framework/configuration, and addendum bindings. |
| `freshness` | `CURRENT`, `STALE`, or `BLOCKED`. |
| `lifecycle` | `ACTIVE`, `RESOLVED`, or `SUPERSEDED`. |
| `relationships` | Explicit bounded relations to other semantic records. |
| `remediation` | Links to zero or more `CQRA-*` actions. |
| `provenance` | Author, evidence revision, adjudication, and update provenance. |

Counts, rankings, hotspot scores, labels, and prose summaries are derived or
display fields, not substitutes for these fields.

### Parent-qualified operation references

An accepted `CQ-*` finding may narrow its interface or boundary context with
references to accepted STM records. These references are addressability and
evidence links, not Code Quality-owned operation facts:

```text
interface_ref: IF-*<accepted parent revision>
operation_ref: IF-*/OP-*<accepted child revision>
operation_property_evidence:
  property: <method | effective_path | parameter | schema | auth | error |
            request_boundary | response_boundary | other evidenced operation field>
  evidence_ref: EV-*<addressable observation>
  workset_ref: optional WS-*<accepted workset>
```

`operation_ref` is used only when the parent-qualified operation child is
accepted and addressable. A bounded, unresolved, conflicting, dynamic, or
partial observation may instead reference the accepted parent `interface_ref`
and its specific `operation_property_evidence` with the limitation preserved;
Code Quality must not guess an operation identity from a file, handler,
configuration value, consumer base URL, or route fragment. An exact operation
identity with unknown schema remains exact for identity purposes while the
missing schema is an explicit limitation.

Code Quality may use these references to explain an implementation-quality
mechanism, request-boundary consequence, or evidence location. It cannot
create, revise, classify, accept, supersede, or otherwise mutate the STM
operation inventory or its operation-child facts. Operation identity,
precision, inventory accounting, and operation-detail authority remain with the
existing Technical Model and Coverage contracts.

## Candidate-to-finding rule

The semantic flow is:

```text
WS/EV observation
  -> transient candidate
  -> applicability and evidence sufficiency
  -> materiality adjudication
  -> accepted CQ-* finding
```

`CANDIDATE` is pre-authority and transient. It may be rejected as
`FALSE_POSITIVE`, marked `NOT_APPLICABLE`, or marked `EXCLUDED`; none of those
outcomes creates an active CQ finding. A warning, metric, line count, repeated
text fragment, or framework rule cannot bypass evidence and materiality.

### Change Review candidate assessment

In `CHANGE_REVIEW_CANDIDATE` mode, Code Quality may record a candidate
interpretation without creating a canonical `CQ-*` finding:

```text
candidate_cq_assessment:
  candidate_origin: CR-*/CRF-*
  operation_ref: <accepted IF-*/OP-* ref or bounded parent ref>
  operation_property_evidence: <property plus WS-*/EV-* evidence>
  candidate_finding_ref: CR-*/CRF-*
  assessment_effect: INTRODUCES_RISK | WORSENS_EXISTING | MITIGATES |
                     POTENTIALLY_RESOLVES | NO_MATERIAL_IMPACT | UNKNOWN_IMPACT
  limitation
```

The operation/property references remain evidence and addressability inputs;
they do not make Code Quality an operation authority. `CRF-*` remains
review-local and cannot become `CQ-*` through candidate assessment.
`RESOLVED`, `CLOSED`, and `ACCEPTED` are never CRF outcomes; they may only
quote an existing canonical state. On explicit `RECONCILE_CHANGE`, Code
Quality independently adjudicates the input and creates or links the
owner-controlled `CQ-*` identity, retaining `candidate_origin`.

For API changes, the candidate assessment may separately reference an
operation addition/removal or a changed method, path, auth, schema, error, or
transport/container limit. These are candidate claims qualified to their
parent `IF-*`, exact source binding, and evidence; they do not change the
accepted operation inventory or CQ lifecycle. The owner must explicitly
decide `NEW`, `DUPLICATE`, `REJECT`, or canonical finding treatment during
adjudication rather than allowing a candidate label to decide lifecycle.

## Language-neutral taxonomy

The bounded primary categories are:

```text
DUPLICATION
HARDCODED_ASSUMPTION
LOCALIZATION
DEAD_OR_OBSOLETE_CODE
COMPLEXITY_OR_COHESION
ABSTRACTION_MISUSE
ERROR_HANDLING
RESOURCE_MANAGEMENT
ASYNC_CONCURRENCY
FRAMEWORK_MISUSE
DEPENDENCY_USAGE
TESTABILITY
API_OR_LIFECYCLE_MISUSE
MAINTAINABILITY
```

Categories are semantic lenses, not a framework-rule catalog. One semantic
issue has one primary category and may use secondary tags; symptoms do not
automatically create duplicate findings.

### API input robustness categories and findings

API input robustness reuses the primary-category field and existing `CQ-*`
finding lifecycle. The following controlled boundary categories are attributes
of an observation/finding, not identity families:

```text
REQUEST_BODY_SIZE       STRING_LENGTH          COLLECTION_SIZE
NUMERIC_RANGE           NESTING_DEPTH          UPLOAD_SIZE
MULTIPART_LIMITS        HEADER_LIMITS          QUERY_LIMITS
COOKIE_LIMITS           CONTENT_TYPE           MALFORMED_PAYLOAD
UNEXPECTED_FIELDS       SCHEMA_ENFORCEMENT     VALIDATION_ORDER
PARSER_RESOURCE_EXHAUSTION  COMPRESSION_EXPANSION  PAGINATION_LIMITS
```

The controlled implementation-quality classifications are:

```text
MISSING_REQUEST_SIZE_LIMIT       UNBOUNDED_STRING
UNBOUNDED_COLLECTION             UNBOUNDED_UPLOAD
SCHEMA_NOT_ENFORCED              VALIDATION_AFTER_MATERIALIZATION
UNEXPECTED_FIELD_ACCEPTANCE      PARSER_RESOURCE_EXHAUSTION
UNBOUNDED_PAGINATION             UNBOUNDED_NUMERIC_INPUT
UNBOUNDED_NESTING                UNBOUNDED_MULTIPART
COMPRESSION_EXPANSION_RISK
```

These values classify CQ observations; they do not create a second API fact
record, a compatibility result, a projection lifecycle, or a security
authority. One input may carry several category tags, while one accepted
semantic issue retains one primary CQ category and explicit secondary context.

The API boundary review records the qualified interface/input location, layer
(`TRANSPORT_CONTAINER` or `SCHEMA_FIELD`), observed state, expected boundary,
evidence/provenance, impact, recommendation, source/baseline binding, and
severity. It distinguishes:

- `DECLARED`: a contract or configuration states a constraint;
- `IMPLEMENTED`: the relevant server path enforces it at an evidenced point;
- `TESTED`: accepted execution evidence supports the existing Test Engineering
  tested view; a generated or accepted test case alone is not tested evidence.

The transport/container check covers body bytes, upload/multipart limits,
headers, query/cookie aggregates, parser/resource limits, and compression
expansion. The schema/field check covers string/collection/numeric limits,
unknown-field policy, media type, nesting, pagination, and validator use. A
field `maxLength` with an unknown body limit and buffering before validation
therefore records field evidence but unresolved transport protection and may
support `VALIDATION_AFTER_MATERIALIZATION` or
`MISSING_REQUEST_SIZE_LIMIT`; it never implies `SAFE`.

Static patterns include an unbounded parser or upload handler, an undocumented
framework default, validation after buffering/deserialization, a bypassed
schema validator, frontend-only validation, permissive unknown fields,
unbounded pagination/numeric input, recursive parsing, and decompression before
bounded enforcement. Tool output remains candidate/evidence and must pass the
normal CQ applicability, materiality, lifecycle, and adjudication chain.

## Materiality, severity, and confidence

Materiality answers whether an observation deserves persistent CQ identity. A
metric, LOC threshold, warning level, duplication count, or style preference
alone is not materiality.

Severity applies only after materiality is accepted:

- `CRITICAL`: rare, immediate and severe CQ consequence affecting safety, data
  integrity, availability, or catastrophic release/maintainability risk;
- `HIGH`: serious quality, reliability, security-adjacent, or change-risk
  consequence with broad, recurring, or failure-prone impact;
- `MEDIUM`: clear material maintainability, reliability, testability, or
  change-cost issue with bounded impact and non-urgent remediation;
- `LOW`: real material issue with localized consequence and low urgency.

Severity reflects the CQ consequence, breadth, blast radius, likelihood,
recoverability, recurrence, and urgency. Size, count, linter severity, category,
confidence, or security relevance alone does not determine it. Security and
Architecture owners retain their own severity semantics; security relevance
does not automatically make a CQ finding `CRITICAL`.

Confidence records certainty of evidence and interpretation as `HIGH`,
`MEDIUM`, `LOW`, or `UNKNOWN`. Confidence may qualify or block acceptance but
does not reduce the consequence severity. Informational or non-material notes
remain evidence/review notes and do not receive `CQ-*` identity.

## Evidence contract

Accepted findings must answer: what code, where, what mechanism, what evidence,
why it is materially problematic, under which applicability, and with what
expected or observed consequence.

Minimum evidence by category:

| Category | Minimum evidence |
|---|---|
| `DUPLICATION` | Comparable regions, repeated behavior/logic, scope, and consequence beyond similarity. |
| `COMPLEXITY_OR_COHESION` | Observable structure plus responsibility or change consequence; size alone is insufficient. |
| `DEAD_OR_OBSOLETE_CODE` | Reachability/usage and build or feature-flag context, including intentional compatibility checks. |
| `RESOURCE_MANAGEMENT` | Acquisition/release path, exceptional or lifecycle path, and plausible resource consequence. |
| `ASYNC_CONCURRENCY` | Shared state/scheduling path, unsafe ordering or isolation, and plausible consequence; an incident is not required. |
| `FRAMEWORK_MISUSE` | Applicable framework/version rule, concrete misuse, and consequence in scope. |
| `LOCALIZATION` | User-facing path, localization context, affected locale behavior, and consequence. |
| `DEPENDENCY_USAGE` | Dependency/version/use site, applicable contract, and concrete maintenance, reliability, security, or lifecycle consequence. |
| `API_OR_LIFECYCLE_MISUSE` | Qualified API/input path, applicable transport or schema layer, concrete enforcement/order evidence, and material consequence. |

For API boundary findings, a missing or broad limit is not material solely
because a field lacks a maximum. The expected threshold must come from an
accepted contract, explicit policy, resource budget, or evidenced context. A
frontend `maxlength` is a weak hint, an OpenAPI limit is a declaration, a
framework default requires deployed applicability, and a reverse-proxy limit
requires qualified traffic-path reachability. Unknown enforcement is not safe
and is not by itself a confirmed vulnerability; severity remains dependent on
reachability, resource consequence, evidence strength, and effective alternate
boundaries.

Observation, interpretation, and consequence remain distinguishable. A static
tool result is evidence for adjudication, never an accepted finding by itself.

## Shared Evidence and STM

`WS-*` is the Shared Evidence workset and `EV-*` is an addressable observation
within that workset. Code Quality may store source-local facts as `EV-*`; an
observation is not a CQ finding and is not an STM fact.

STM remains factual authority for accepted system/topology/interface/interaction/
data/event/flow/auth/configuration/error facts:

```text
COMP-* IF-* INT-* DS-* EVENT-* FLOW-* AUTH-* CFG-* ERR-*
```

When a CQ interpretation depends on system-level facts, it requires the
accepted, sufficiently covered, sufficiently fresh, and sufficiently resolved
targeted STM slice. Missing, stale, disputed, or insufficiently covered STM
blocks only the dependent CQ interpretation and routes through the existing STM
workflow. Code Quality never rewrites STM or reconstructs a private factual
model.

## Architecture, Test Engineering, and security boundaries

`CQ-* != RF-*`. A local issue remains CQ-only when its consequence does not
materially alter a system boundary, invariant, cross-component contract, trust
boundary, ownership/lifecycle rule, or system-level reliability/security
mechanism. Code Quality never creates, mutates, closes, downgrades, or
suppresses `RF-*`; an Architecture escalation is a request for Architecture
adjudication.

`CQ-* != BC/CC/MAT/TM/GAP/TASK`. Code Quality may interpret implementation
quality around seams, isolation, nondeterminism, observability, dependency use,
concurrency, and fragile setup. Test Engineering owns its behavior, contract,
assurance, evidence, gap, and task records. Shared evidence may support both
interpretations, but Code Quality cannot create or mutate TE authority.

An operation-targeted CQ finding may cite a provider or consumer operation
evidence record, including a dynamic-base or declaration/implementation
limitation, but that citation does not create a `CC-*` comparison or decide
compatibility. Same method/path text is only an input to the existing Contract
Verification process; it is never automatic compatibility.

There is currently no independent Security Review capability. Security-relevant
mechanisms route through existing Architecture/security semantics and severity
ownership. Code Quality may retain a distinct quality finding when that
interpretation is independently valid; it must not downgrade, replace, close,
or suppress the security interpretation. A future dedicated Security
capability requires a separate architecture/design decision.

## Bounded cross-capability relations

Relations preserve independent identities and are not a generic graph
framework:

| Relation | Meaning and effects |
|---|---|
| `DUPLICATE` | Same semantic issue represented twice; directional during adjudication, many-to-one, no automatic severity change, and one retained authority. |
| `CORRELATED` | Distinct records share evidence or mechanism; symmetric, many-to-many, no lifecycle/severity transfer. |
| `CAUSAL` | Source issue materially contributes to target issue; directional, many-to-many, informs reasoning without ownership transfer. |
| `ESCALATED` | CQ evidence requests external Architecture/security/TE adjudication; directional, many-to-many, target owner decides. |
| `DERIVED` | A downstream semantic/view record is produced from an accepted source; directional, one-to-many, source remains authoritative. |
| `INDEPENDENT` | Same evidence or area, intentionally distinct interpretations; symmetric, many-to-many, no automatic effect. |

Relations carry endpoints, rationale, direction/cardinality where applicable,
and freshness bindings. They do not copy severity, couple lifecycles, or make a
projection authoritative. `CQRA-*` is not `TASK-*` and does not change these
boundaries.

## Applicability and addenda

The core is language- and framework-neutral. Optional language/framework
addenda may declare an identity, language/framework/runtime binding, version or
configuration constraint, selected-scope binding, guidance/check families,
evidence expectations, known limitations, known false positives, and associated
tool guidance. An addendum is non-authoritative guidance: it does not define
CQ identity, authority, materiality, severity, lifecycle, disposition,
remediation, or coverage.

Applicability requires evidence from the selected scope and accepted repository
context, such as confirmed language, framework, runtime, build/dependency or
configuration facts. A file extension, directory name, repository name, or tool
availability alone is not sufficient. An applicable addendum may refine
candidate generation and interpretation; a non-applicable addendum is ignored.
An unknown or unsupported environment uses the language-neutral core and
qualifies any affected limitation. Unsupported addenda therefore do not make
the whole capability `NOT_APPLICABLE` or `BLOCKED`.

If two applicable addenda provide incompatible guidance, the conflict is
recorded with the competing addendum identities, applicability evidence, and
affected interpretation. Registration order, execution order, specificity,
or a tool's preferred answer is not precedence. Code Quality adjudicates the
conflict against the core contract and available evidence; unresolved
ambiguity blocks only the affected interpretation or leaves it as a candidate.
An addendum rule hit remains subject to the normal evidence and materiality
chain and cannot bypass identity, lifecycle, applicability, disposition,
severity, confidence, or coverage rules. Addendum/tool specificity is not
materiality, and an addendum cannot directly create an accepted `CQ-*`.

Generated, vendored, migration, fixture, boilerplate, compatibility,
feature-flagged, transitional, and performance-specialized code requires
applicability and ownership checks. `EXCLUDED` is a scope decision, not proof
that no quality risk exists.

### Tooling boundary

Tools and agent heuristics are optional evidence producers, not semantic
adjudicators. Grep, linters, formatters, AST analyzers, language servers,
static analyzers, dependency/framework scanners, complexity or duplication
detectors may emit an observation or candidate, but:

```text
tool output != EV-* observation
tool output != accepted CQ-* finding
tool warning severity != CQ severity
tool success/completion != semantic adjudication
```

Where tool output materially contributes evidence, the accepted evidence
records the tool identity, invocation or relevant analysis context, selected
scope, observation, and material limitation using the existing `EV-*`/`WS-*`
provenance conventions. No execution database or tool-finding ledger is
created. A tool result still passes candidate applicability, evidence,
materiality, and Code Quality adjudication; it may result in
`FALSE_POSITIVE`, `NOT_APPLICABLE`, or `EXCLUDED`.

Tool selection is bounded by the review question, applicable language or
framework evidence, scope, expected evidence value, and cost. The default is
not to run every available analyzer or collect redundant signals. An
unavailable optional tool leaves other evidence usable and blocks only a
dependent slice when that tool is materially required for the requested claim.
Disagreement between tools is recorded as evidence and adjudicated; neither
tool order nor consensus automatically creates or rejects a finding. Tool
changes contribute to the existing Task 5 dependency/freshness and minimum-
slice revalidation rules rather than creating an addenda- or tool-specific
revalidation mechanism.

## Invariants

- `CQ finding != Architecture RF finding`.
- `CQ finding != TE GAP/TASK/BC/CC/MAT/TM`.
- `CQRA-* != TASK-*`.
- `tool warning != accepted CQ finding`.
- `evidence observation != semantic finding`.
- `semantic CQ authority != generated projection`.
- `working/INDEX.md != semantic authority`.
- `PROJECTION_REPAIR != semantic remediation`.
- `REVALIDATE != projection regeneration`.
- `confidence != severity` and `materiality != severity`.
- `WONT_FIX != FALSE_POSITIVE` and `ACCEPTED_EXCEPTION != RESOLVED`.
- `generated/vendor exclusion != proof of absence of quality risk`.
