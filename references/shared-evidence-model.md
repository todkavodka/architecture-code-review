# Shared Evidence Model

This reference owns the shared, baseline-bound evidence layer for the review
suite. It captures bounded observations from repository and external sources so
the Shared Technical Model (STM) and capabilities can reuse provenance without
duplicating it. Baseline selection remains owned by
[Session Orchestration](session-orchestration.md); evidence strength, candidate
lifecycle, and severity remain owned by
[Evidence and severity](evidence-and-severity.md).

## 1. Ownership boundary

```text
WS-* = bounded investigation/workset and physical evidence grouping
EV-* = logical addressable observation within a WS
```

`WS-*` and `EV-*` are shared cross-capability evidence records. An evidence
record is an observation, not a finding, technical fact, Behavior Contract,
assurance target, gap, recommendation, or verdict. Semantic artifacts retain
ownership of every conclusion they derive from evidence.

## 2. Worksets

A `WS-*` is one bounded investigation and the physical grouping of its evidence
records. It is suitable for a focused agent pass and review; it is not a
product-behavior or capability-semantic authority.

Each workset records at least:

```text
id: WS-*
name
scope
baseline
baseline_type
status
investigated_sources
limitations
EV records
HANDOFF SUMMARY
```

`baseline` identifies the source revision or other selected baseline and
`baseline_type` identifies how that baseline was selected. `status` follows the
shared workflow vocabulary in [Review modes and orchestration](review-modes-and-orchestration.md).
`investigated_sources` identifies what was actually examined; `limitations`
identifies unavailable, incomplete, or otherwise bounded evidence.

One workset has one active writer. Write the complete workset, verify its
required content, and persist its `HANDOFF SUMMARY` before a coordinator uses
it for resume or routing, following the handoff discipline in
[Review modes and orchestration](review-modes-and-orchestration.md). A
capability may add a new shared workset when it gathers new reusable evidence;
that does not transfer ownership of capability-specific conclusions.

## 3. Evidence observations

An `EV-*` is a logical, globally addressable observation within a workset. Refer
to it as `WS-###-name#EV-###`; it may live in the workset file rather than in a
separate physical Markdown file.

Each `EV-*` records at least:

```text
id: EV-*
source_type
repository/path or external locator
symbol or range, when available
baseline binding
observed fact/behavior
optional short excerpt, only when useful
```

The observation states only what the cited source shows at its bound baseline.
Use a short excerpt only to disambiguate the observation; do not copy large
source blocks into evidence. The raw repository or external source remains the
ultimate source and must be reopened when the available evidence is
insufficient, disputed, or stale for the decision being made.

## 4. Historical binding

An `EV-*` remains evidence of the baseline at which it was observed. When a new
baseline needs evidence, create new observations as needed; do not rewrite old
observations to make historical evidence look current. Freshness and impact
decisions are governed by [Revalidation and compact-state freshness](revalidation-and-freshness.md),
not by silently changing the earlier record.

## 4.1 Change Review immutable bindings and review-local artifacts

Change Review persists two separate, immutable source bindings. A friendly
branch, tag, PR ref, checkout state, or `HEAD` is input metadata only; none is
sufficient without its resolved commit and tree. Each binding contains:

```text
base_binding:
  repository_id
  project_binding
  product_member_binding: <optional exact Product member/vector qualification>
  ref_input
  resolved_commit
  resolved_tree
  qualification
  source_availability
  evidence_availability

candidate_binding:
  repository_id
  project_binding
  product_member_binding: <optional exact Product member/vector qualification>
  ref_input
  resolved_commit
  resolved_tree
  qualification
  source_availability
  evidence_availability
```

`qualification` records the exact Project scope and, when applicable, accepted
Product revision and member baseline vector. Source and evidence availability
remain independent limitations. Persist both bindings with the review; later
branch movement or a different checkout cannot retarget them.

`CR-*` is the stable, review-qualified Change Review identity. `CF-*` candidate
facts and `CRF-*` candidate findings are unique only within their owning
`CR-*`; use the qualified identities `CR-*/CF-*` and `CR-*/CRF-*`. They are
neither global STM identities nor canonical finding identities. A CR record
contains its two bindings, bounded scope/lenses, candidate references, and:

```text
review_status: DRAFT | IN_PROGRESS | REVIEW_REQUIRED | COMPLETE | BLOCKED |
               SUPERSEDED
decision: NOT_RECONCILED | RECONCILED | KEPT_REVIEW_ONLY
```

The normal CR lifecycle is `DRAFT → IN_PROGRESS → REVIEW_REQUIRED → COMPLETE`;
unavailable required evidence may produce `BLOCKED`, and later linked review
work may mark the prior CR `SUPERSEDED` without rewriting it. `COMPLETE`
describes bounded review work only, never candidate acceptance. Candidate fact
and finding status is separate from canonical lifecycle and is recorded on the
qualified candidate, for example:

```text
candidate_status: CANDIDATE | UNRESOLVED | DUPLICATE_OF |
                  SUPERSEDES_CANDIDATE | NON_MATERIAL | REJECTED
```

`CR-*`, `CF-*`, and `CRF-*` are accepted only as review evidence, routing
context, historical comparison, or reconciliation input. Candidate records
cannot become STM facts, canonical findings, tests, compatibility decisions,
Product state, or projection dependencies merely through persistence in an
evidence workset.

## 4.2 Change Inventory

Each Change Review may persist one bounded, immutable `CI-*` Change Inventory
for its frozen base/candidate bindings and selected scope. The inventory
records factual source delta observations; it does not clone the STM schema or
assign severity, materiality, compatibility, architectural meaning, finding
lifecycle, or owner decisions.

Each entry contains:

```text
change_inventory:
  inventory_id: CI-*
  review_id: CR-*
  base_binding_ref
  candidate_binding_ref
  entries:
    - delta_type: ADDED | MODIFIED | REMOVED
      source_path_or_locator
      source_evidence_binding: WS-*/EV-* or explicit limitation
      candidate_surface_kind: COMPONENT | INTERFACE | OPERATION |
                             INTEGRATION | DATA_STORE | MIGRATION | EVENT |
                             FLOW | AUTH_CONFIG | CONTRACT | OTHER
      correlated_accepted_ref: <STM/owner ref or NONE>
      candidate_ref: <qualified candidate ref or NONE>
      discovery_status: COMPLETE | PARTIAL | UNKNOWN
      limitation: <bounded source, evidence, or scope limitation>
    - delta_type: MOVED
      moved:
        base:
          source_binding: BASE
          old_source_locator
          old_source_evidence_binding: WS-*/EV-* or explicit limitation
        candidate:
          source_binding: CANDIDATE
          new_source_locator
          new_source_evidence_binding: WS-*/EV-* or explicit limitation
      candidate_surface_kind: COMPONENT | INTERFACE | OPERATION |
                             INTEGRATION | DATA_STORE | MIGRATION | EVENT |
                             FLOW | AUTH_CONFIG | CONTRACT | OTHER
      correlated_accepted_ref: <STM/owner ref or NONE>
      candidate_ref: <qualified candidate ref or NONE>
      discovery_status: COMPLETE | PARTIAL | UNKNOWN
      limitation: <bounded source, evidence, or scope limitation>
```

`source_path_or_locator` and `source_evidence_binding` remain qualified to the
exact source state; a changed path alone is not an observed fact. `ADDED`
entries may have `correlated_accepted_ref: NONE` and remain candidate
observations. `REMOVED` entries preserve the correlated accepted reference and
record the candidate absence; they do not delete or retire canonical state.
`MOVED` entries must use the two-sided `moved.base` and `moved.candidate`
structure: the old locator and evidence are bound to BASE, and the new locator
and evidence are bound to CANDIDATE. A MOVED entry must not collapse either
side into the scalar fields used by the other delta types. Multiple entries may
refer to one source path when independently bounded surfaces are observed.

## 4.3 Reuse and tree-equivalence proof

A completed CR may be reused only after the coordinator records one exact
reuse classification and its evidence. `TREE_EQUIVALENT` has exactly two
permitted proof levels:

```text
reuse_proof:
  reuse_state: TREE_EQUIVALENT
  level: WHOLE_TREE_EQUAL | FROZEN_RELEVANT_SCOPE_EQUAL
  repository_id
  project_product_qualification
  scope_and_lenses
  candidate_commit
  candidate_tree
  proof_evidence
```

`WHOLE_TREE_EQUAL` requires equal resolved whole-tree identity, matching
repository identity, exact Project/Product qualification, and compatible
review scope/lenses. `FROZEN_RELEVANT_SCOPE_EQUAL` requires the persisted
manifest of included paths, selectors, and member bindings; an equal
relevant-tree fingerprint; and proof that omitted paths cannot affect the
reviewed scope. The manifest and proof are retained with the reuse decision.

Inspected-files coincidence, branch name, ancestry, fuzzy text, or missing
proof yields `NOT_TREE_EQUIVALENT` and cannot authorize reuse. A commit SHA
comparison without the required repository, qualification, scope, and proof
is not a reuse decision. A merge, squash, or cherry-pick may therefore reuse
only when its applicable whole-tree or frozen-scope proof is retained.

The inventory is `WHAT CHANGED` only. Interpretation, risk, finding effects,
test impact, contract impact, and predicted projection impact belong to the
separate Change Assessment and its owning authorities.

## 5. Shared reuse and reading order

Consumers use the smallest sufficient context in this order:

```text
INDEX
-> semantic artifact
-> WS#EV
-> raw source
```

The semantic artifact explains the consumer-owned fact or conclusion and
references `WS#EV` for its observation. It does not turn an `EV-*` into
semantic authority. Reuse the same addressable evidence across STM and
capabilities instead of creating architecture or test evidence silos for the
same observation. The cross-capability invariant is also recorded in
[Shared assurance principles](shared-assurance-principles.md).

## 6. Product-scoped multi-source evidence

When Product mode is selected, a `WS-*` may investigate more than one Project
or an explicitly declared external source. The existing `WS-*`/`EV-*`
identities and evidence ownership are reused; Product scope does not create a
second evidence family. A Product-scoped workset and each observation record
must additionally retain:

```text
product_id: PROD-*
product_revision: <accepted revision>
product_baseline_ref: <immutable baseline vector>
project_bindings:
  - project_id
    repository_binding
    scope_selector
    exact_revision_or_content_binding
external_source_bindings: <exact locator/revision or limitation>
observed_view: DECLARED | IMPLEMENTED | CONSUMED | TESTED
conflict: <independent observations and unresolved disagreement, if any>
limitations: <availability, coverage, freshness, or source limitations>
```

Every source binding is qualified by stable Project identity and exact Product
baseline context; equal local IDs in different Projects therefore remain
distinct. External participation records the external source and provenance,
not Product ownership. The evidence writer records observations and conflicts;
the owning STM or capability gate adjudicates their meaning. A report,
summary, `INDEX.md`, or generated reverse index may route to this evidence but
cannot accept, revise, or replace it.

The Product baseline may be `COHERENT`, `MIXED_EXPLICIT`, or `UNKNOWN` as
defined by the Product context contract. That value is provenance metadata and
does not override an unavailable source, stale observation, insufficient
coverage, or a package gate. Conflicting observations remain independently
preserved until the appropriate owner emits a bounded conflict or
revalidation request; evidence does not auto-resolve by precedence.

## 7. Stage F source-support qualification

Stage F adds a bounded source-support classification for technical interaction
extraction. It describes what an observation supports; it does not create a
second evidence lifecycle or semantic authority:

```text
DIRECT_DECLARATION
STRONG_INFERENCE
WEAK_HINT
```

`DIRECT_DECLARATION` is an explicit declaration of a surface, contract,
binding, schema, migration, resource, provider, or consumer expectation.
`STRONG_INFERENCE` is an implementation path whose concrete call, binding,
resource use, or access operation is materially clear even without a formal
declaration. `WEAK_HINT` is contextual evidence such as a dependency
declaration, generic connection, configuration URL, unused generated client,
or provisioned infrastructure resource.

These classes are evidence metadata only. They do not replace the existing
`HIGH`/`MEDIUM`/`LOW` confidence semantics, candidate lifecycle, severity,
authority, precision, coverage, freshness, or observed-view vocabulary owned by
the relevant contracts. A class may be recorded alongside those dimensions;
none is inferred from another.

### 7.1 Acceptance boundary

The evidence writer records what the source shows and its limitations. Only the
Technical Model Gate accepts a technical fact. A `WEAK_HINT` may route further
investigation, support a bounded unresolved observation, or explain why a
candidate was considered, but it cannot alone create an accepted concrete
`IF-*`, `INT-*`, `DS-*` child-resource access, or `EVENT-*` producer/consumer
fact.

The following distinctions are mandatory:

```text
configured base URL       != confirmed consumed API
SDK installed              != confirmed runtime integration
generated client exists    != confirmed client method use
ORM model exists           != confirmed table access
connection string exists   != confirmed resource-level access
database connection exists != confirmed table access
migration declaration      != confirmed runtime access
broker configuration       != confirmed semantic event producer/consumer
```

`DIRECT_DECLARATION` and `STRONG_INFERENCE` still require baseline binding,
contextual applicability, and sufficient subject-level provenance before an
STM gate can accept a fact. Evidence strength never silently promotes a
candidate, fills an absent locator, or upgrades precision.

### 7.2 Fine-grained observation shape

An `EV-*` may qualify the semantic subject at the smallest useful granularity
without requiring a separate physical file for every observation:

```text
EV-*:
  id: WS-###-name#EV-###
  source_type
  repository/path or external locator
  symbol/range/variable: optional exact locator
  baseline_binding: exact revision/content/product baseline
  project_binding: exact Project when applicable
  product_binding: exact Product revision/baseline when applicable
  observed_view: DECLARED | IMPLEMENTED | CONSUMED | TESTED
  stage_f_source_support: DIRECT_DECLARATION |
                          STRONG_INFERENCE | WEAK_HINT
  subject_kind: interface | provider | consumer | interaction | operation |
                data_store | data_resource | access_operation |
                event | migration | migration_authority | other
  subject_ref: optional IF/INT/DS/EVENT/COMP or qualified external subject;
               operation uses parent-qualified IF-*@revision/OP-* reference
  provider_or_consumer_side: PROVIDER | CONSUMER | BOTH | NOT_APPLICABLE
  observed_fact
  limitation: optional bounded/dynamic/partial limitation
  safe_excerpt: optional short non-secret excerpt
  sensitivity: SECRET | SENSITIVE_INTERNAL | SAFE_TECHNICAL_IDENTIFIER
```

The exact locator may be a file, symbol, line/range, configuration key, schema
object, operation, or external source revision. If the source cannot support
that precision, record the available locator and an explicit limitation rather
than inventing one. Operation-level, entity-level, access-level, event-level,
migration, and migration-authority observations retain their own binding and
are not widened to the whole file or store by default.

Provider-side evidence and consumer-side evidence are independently addressable
through `provider_or_consumer_side`, exact subject references, and their own
baseline/revision bindings. A provider declaration may support one IF revision;
a consumer expectation may support another; runtime use may support an INT;
and a test may support a TESTED view. Evidence does not automatically alias
provider and consumer semantics, match their identities, or decide
compatibility. Candidate matching and Contract Verification remain later
semantic/verification concerns.

### 7.3 Operation-level and route-composition evidence

An operation-level `EV-*` uses the parent-qualified operation reference when
the child is known; otherwise it may identify the parent `IF-*` and state the
explicit operation-resolution limitation. Record each independently observed
composition input as its own addressable evidence, rather than collapsing it
into a handler or route-location claim:

```text
operation_evidence_role:
  ROUTE_DECLARATION | PREFIX_OR_MOUNT | HTTP_METHOD |
  PARAMETERS_OR_SCHEMA | AUTH_MIDDLEWARE | CONSUMER_CALL_SITE |
  GENERATED_CONTRACT | RUNTIME_OBSERVATION

composition_order: required for each PREFIX_OR_MOUNT and ROUTE_DECLARATION
                   input when route composition applies
accepted_runtime_observation_ref: optional accepted runtime observation,
                                  when available
```

Route declaration, every controller/router/mount prefix, method,
parameters/schema, authentication middleware, consumer call site, and generated
contract each retain their own source locator and baseline binding. When an
accepted runtime observation is available, reference it explicitly without
letting the evidence record itself decide acceptance. Evidence location is
never semantic identity: it supports an operation or composition input but
cannot turn a file, symbol, handler, or generated artifact into the operation's
identity.

Dynamic, partial, computed, plugin-provided, feature-flagged, reflected,
runtime-only, and conflicting composition evidence remains explicit through
its individual `limitation` and subject binding. Missing inputs are not filled
from a nearby declaration, configuration value, or consumer base URL. In
particular, a dynamic consumer base URL is evidence of a bounded consumer call
site, not proof of an exact remote address or operation identity.

### 7.4 Dynamic and partial evidence

Dynamic targets, generated operations, unresolved resource names, unavailable
external sources, and partial repository coverage remain explicit limitations.
The evidence record may state that a service, store, event, or migration path
is known while its exact operation, child resource, provider, consumer, or
authority cannot be resolved. Such an observation remains bounded or
unresolved and cannot be presented as exact solely because a related weak hint
exists.

## 8. Safe evidence excerpts and technical identifiers

Evidence may preserve a file path, symbol, line/range, variable or configuration
key name, baseline, and a short excerpt when those details are useful for
reopening the source. It must not copy secret material merely because it is
present in source. The safe evidence representation is provenance, a bounded
logical fact, and a limitation—not a credential cache.

Every technical identifier used by Stage F evidence is classified as exactly
one of:

```text
SECRET
SENSITIVE_INTERNAL
SAFE_TECHNICAL_IDENTIFIER
```

`SECRET` includes passwords, API keys, access/refresh tokens, client secrets,
private keys, raw environment secret values, credentials in URLs or connection
strings, and secret query parameters. `SECRET` values are omitted from EV
excerpts and stored fields. The evidence may retain a safe source pointer and a
statement that secret material was present. Secret-bearing URLs and DSNs are
represented only by safe logical facts and redacted examples.

`SENSITIVE_INTERNAL` includes private hostnames, usernames, sensitive filesystem
paths, private aliases, and internal locators that are useful for provenance
but not approved for general display. Evidence may retain a source pointer and
a safe logical alias or redacted representation; it must not silently upgrade
the identifier to `SAFE_TECHNICAL_IDENTIFIER`.

`SAFE_TECHNICAL_IDENTIFIER` may be retained when the source policy permits it,
including a logical provider/store name, ordinary public path template, schema
or table name, event name/topic, or non-secret operation name. It remains
subject to baseline and scope binding.

Credential-bearing examples must be represented only in safe form, for example:

```text
https://<redacted>@logical-provider.example/<redacted-path>
postgresql://<redacted>@logical-database/<redacted-database>
DSN: technology=postgresql; host=<redacted>; credential=<omitted>
```

These are safe logical examples, not copied observed values. An evidence
pointer may identify the source file, symbol, range, variable/config key, and
baseline without reproducing the value. The classification is evidence
metadata consumed by STM and projection owners; it is not a new lifecycle,
confidence level, or presentation authority.

Evidence safety and projection rendering remain separate responsibilities:

```text
evidence layer       -> safe observation, provenance, classification, limitation
STM                  -> accepted non-secret technical facts
projection layer     -> later safe rendering/redaction contract
```

Task 2 does not implement Technical Documentation formatting or decide that an
unclassified value is safe to render. A later projection may omit, alias, or
redact according to its own contract, but it cannot recover or copy a secret
that the evidence layer did not persist.

## 9. Historical and Product compatibility

The new source-support and sensitivity fields are additive. Existing `WS-*`
and `EV-*` records remain valid without fabricated `stage_f_source_support`,
subject-level provenance, locator precision, or sensitivity classifications.
Old evidence is not rewritten, enriched by assumption, or invalidated merely
because Stage F adds optional fields. A later observation may create a new
revision or observation with stronger qualification while preserving the
historical binding and limitation.

Product-scoped evidence continues to use the existing `WS-*`/`EV-*` families.
Product remains optional; Project evidence remains Project-qualified; equal
local IDs in different Projects remain distinct; external evidence remains
external; and Product membership does not grant evidence acceptance. Exact
Product revision/baseline and source availability limitations remain separate
from evidence strength, precision, freshness, and coverage. The migration
classification remains `COMPATIBLE_EXTENSION`.
