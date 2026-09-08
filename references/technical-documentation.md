# Technical Documentation projection

Technical Documentation is the human-facing factual projection of the accepted,
fresh Shared Technical Model (STM). It helps a reader understand the system; it
does not own, accept, revise, or resolve technical facts.

Its factual inputs and acceptance boundary belong to
[`shared-technical-model.md`](shared-technical-model.md). Required system
surface coverage belongs to
[`technical-model-coverage.md`](technical-model-coverage.md), and dependency
metadata and impact semantics belong to
[`technical-model-dependencies.md`](technical-model-dependencies.md).

## Scope and authority boundary

The projection may document verified system, component, provided and consumed
interface, integration, data and persistence, runtime and deployment,
authentication and trust, material flow, and failure-behavior facts.

It does not own Stage A developer enablement content. In particular, it does
not produce onboarding tutorials, local environment setup instructions,
instructions for running the application, instructions for modifying or
extending code, or step-by-step developer guides. Configuration can be
documented when it is a behaviorally relevant system fact; that does not make
the projection a setup guide.

Only accepted, fresh STM authority may be synthesized as a current fact. A
`PARTIAL`, `UNKNOWN`, stale, missing, or authority-unresolved input remains
visible as such in the projection. If authoritative factual inputs conflict,
the projection preserves the conflict and links to the owning resolution path;
prose cannot choose a winner or turn uncertainty into certainty.

## Recommended human package

The following is a projection taxonomy, not a second semantic model and not a
requirement to create every file for every project:

```text
00-system-overview.md
01-components.md
02-provided-interfaces.md
03-consumed-interfaces.md
04-integrations.md
05-data-and-persistence.md
06-runtime-and-deployment.md
07-auth-and-trust.md
08-material-flows.md
09-failure-behavior.md
```

Each selected section is a readable synthesis of the STM facts required for
that subject. A section may summarize several STM artifacts and link to their
identifiers without copying every evidence record.

## Registered Stage B projections

The selected documents above are fully generated Stage B projections. Their
stable identities are independent of output path or section title:

| Projection | Human-readable output | Controlled STM dependency focus |
|---|---|---|
| `PRJ-TECH-DOC-00-SYSTEM-OVERVIEW` | `00-system-overview.md` | accepted STM facts across the registered families |
| `PRJ-TECH-DOC-01-COMPONENTS` | `01-components.md` | accepted `COMP-*` facts and their controlled runtime relations |
| `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` | `02-provided-interfaces.md` | `IF-*` where `direction = PROVIDED` |
| `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` | `03-consumed-interfaces.md` | `IF-*` where `direction = CONSUMED` |
| `PRJ-TECH-DOC-04-INTEGRATIONS` | `04-integrations.md` | accepted `INT-*` and `EVENT-*` facts |
| `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` | `05-data-and-persistence.md` | accepted `DS-*` facts and controlled data relations |
| `PRJ-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT` | `06-runtime-and-deployment.md` | accepted `COMP-*`, `CFG-*`, and controlled runtime relations |
| `PRJ-TECH-DOC-07-AUTH-AND-TRUST` | `07-auth-and-trust.md` | accepted `AUTH-*`, `IF-*`, `CFG-*`, and controlled trust relations |
| `PRJ-TECH-DOC-08-MATERIAL-FLOWS` | `08-material-flows.md` | accepted `FLOW-*`, `INT-*`, `EVENT-*`, and controlled flow relations |
| `PRJ-TECH-DOC-09-FAILURE-BEHAVIOR` | `09-failure-behavior.md` | accepted `ERR-*`, `IF-*`, `INT-*`, `EVENT-*`, and controlled failure relations |

The projection itself owns its direct outbound metadata. For every fact it
names individually, that metadata records a revision-bound `SEMANTIC_EXACT`
dependency. Each dynamic fact set below instead records the named
`SEMANTIC_SELECTOR` contract. STM inclusion has already applied its
evidence/materiality boundary; these selectors do not make a second subjective
materiality or prose-scope decision.

All `SEL-TECH-DOC-*` contracts use only the following authoritative record and
formal fields:

```text
authoritative_record_type: STM_FACT
allowed_dimensions:
  entity_type | status | freshness | authority | structured_properties |
  formal_relations | project_binding
structured_properties:
  direction | interface_kind | contract_role | operation_identity |
  resource_kind | interaction_kind | access_mode | precision |
  external_identity.kind
allowed_operators: = | IN | HAS_ANY
logical_connectors: AND | OR
base_predicate:
  status = ACCEPTED
  AND freshness = VALID
  AND authority = RESOLVED when that formal field is present on the STM record
stable_order: semantic_id ASC, revision ASC
resolved_members: [<STM-ID>@<revision> ...] in stable_order
```

`HAS_ANY` applies only to the closed STM relation vocabulary in
[`shared-technical-model.md`](shared-technical-model.md). A fact without an
applicable authority axis is evaluated only on `status = ACCEPTED` and
`freshness = VALID`; it is not excluded or promoted by prose interpretation.
Every selector definition is revisioned as `definition_revision: 1`.

| Selector | Consumer projection | Authoritative record type | Additional bounded predicate |
|---|---|---|---|
| `SEL-TECH-DOC-00-SYSTEM-OVERVIEW` | `PRJ-TECH-DOC-00-SYSTEM-OVERVIEW` | `STM_FACT` | `entity_type IN [COMP, IF, INT, DS, EVENT, FLOW, AUTH, CFG, ERR]` |
| `SEL-TECH-DOC-01-COMPONENTS` | `PRJ-TECH-DOC-01-COMPONENTS` | `STM_FACT` | `entity_type = COMP OR formal_relations HAS_ANY [DEPENDS_ON, DEPLOYS_AS]` |
| `SEL-TECH-DOC-02-PROVIDED-INTERFACES` | `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` | `STM_FACT` | `entity_type = IF AND structured_properties.direction = PROVIDED` plus optional `interface_kind`, `contract_role`, `precision`, `status`, `freshness`, and Project predicates |
| `SEL-TECH-DOC-03-CONSUMED-INTERFACES` | `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` | `STM_FACT` | `entity_type = IF AND structured_properties.direction = CONSUMED` plus optional `interface_kind`, `contract_role`, `precision`, `status`, `freshness`, and Project predicates |
| `SEL-TECH-DOC-04-INTEGRATIONS` | `PRJ-TECH-DOC-04-INTEGRATIONS` | `STM_FACT` | `entity_type IN [INT, EVENT]` plus optional `interaction_kind`, `access_mode`, `precision`, `formal_relations`, `status`, `freshness`, and Project predicates |
| `SEL-TECH-DOC-05-DATA-AND-PERSISTENCE` | `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` | `STM_FACT` | `entity_type = DS OR formal_relations HAS_ANY [READS_FROM, WRITES_TO, OWNS_STATE, MIGRATION_AUTHORITY]` plus optional `resource_kind`, `interaction_kind`, `access_mode`, `precision`, `status`, `freshness`, and Project predicates |
| `SEL-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT` | `PRJ-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT` | `STM_FACT` | `entity_type IN [COMP, CFG] OR formal_relations HAS_ANY [DEPLOYS_AS, DEPENDS_ON, CONFIGURED_BY]` |
| `SEL-TECH-DOC-07-AUTH-AND-TRUST` | `PRJ-TECH-DOC-07-AUTH-AND-TRUST` | `STM_FACT` | `entity_type IN [AUTH, IF, CFG] OR formal_relations HAS_ANY [PROTECTED_BY, CONFIGURED_BY]` |
| `SEL-TECH-DOC-08-MATERIAL-FLOWS` | `PRJ-TECH-DOC-08-MATERIAL-FLOWS` | `STM_FACT` | `entity_type IN [FLOW, INT, EVENT] OR formal_relations HAS_ANY [CALLS, PUBLISHES, SUBSCRIBES, PARTICIPATES_IN]` |
| `SEL-TECH-DOC-09-FAILURE-BEHAVIOR` | `PRJ-TECH-DOC-09-FAILURE-BEHAVIOR` | `STM_FACT` | `entity_type IN [ERR, IF, INT, EVENT] OR formal_relations HAS_ANY [EMITS_ERROR]` |

### Stage F selector extension

Stage F selectors remain instances of the existing selector grammar. They may
constrain only formal STM fields that the Technical Model Gate has accepted;
they do not inspect prose, filenames, source text, or evidence hints. The
bounded Stage F dimensions are:

```text
IF:  direction, interface_kind, contract_role, operation_identity, precision
INT: interaction_kind, access_mode, precision
DS:  resource_kind, precision
all: status, freshness, authority, formal_relations, Project qualification
```

`formal_relations` may select `READS_FROM`, `WRITES_TO`, `OWNS_STATE`, and
`MIGRATION_AUTHORITY` only as accepted relations. A precise `INT-*` access
remains the authority for new access; a selector may show a derived
`READS_FROM`/`WRITES_TO` relation but never infer an `access_mode` from a
containment relation or from `parent_resource_ref`. `STORE_ONLY` is selectable
for DS store facts and applicable DATA_ACCESS INT facts only; it is not a
valid IF, EVENT, FLOW, or non-data INT precision.

When Product mode is active, Project and external qualification are explicit
selector inputs and remain separate from semantic availability, projection
freshness, and package status. An absent historical Stage F field is absent or
unknown; it is never treated as a false exact match. Selector resolution
persists the exact member IDs and revisions in stable order, and a changed
membership or selector definition makes the affected projection stale rather
than silently regenerating it.

## Stage F rendered content

The following content is rendered from accepted, fresh STM facts and their
recorded evidence/provenance links. Rendering is explanatory and traceable;
it cannot accept, revise, match, resolve, or enrich a technical fact.

### Provided and consumed interfaces

`PRJ-TECH-DOC-02-PROVIDED-INTERFACES` renders each selected `IF-*` with its
Project/repository/revision qualification, direction, `contract_role`,
`interface_kind`, provider reference, operation identity, safe address,
contract/version reference, protocol properties, observed view, precision,
status/freshness, and evidence links when those fields are applicable and
classified safe. Provider declaration and provider implementation remain
distinct views of the same or separately revised accepted interface; the
projection does not choose between them.

`PRJ-TECH-DOC-03-CONSUMED-INTERFACES` renders accepted consumer expectations
and observed uses separately, including the consumer IF identity/revision,
operation and protocol details, known provider or explicit unmatched-provider
limitation, Project qualification, precision, evidence, and freshness. A
consumer expectation does not require a provider match and is never rewritten
to a provider IF. Candidate matching is displayed only as the existing
non-authoritative candidate/not-established state; compatibility is displayed
only from an existing resolved `CC-*` result and is never inferred by this
projection.

Unknown operation, `UNRESOLVED` or `RESOURCE_BOUNDED` precision, bounded
resource, unresolved provider, partial source, and stale or unavailable input
are rendered as explicit limitations. They are not replaced with an empty
section, `EXACT`, `COMPATIBLE`, or a clean result.

### Integrations and events

`PRJ-TECH-DOC-04-INTEGRATIONS` renders concrete `INT-*` edges with source,
target, interaction kind, protocol/transport, access mode where applicable,
precision, Project/revision qualification, and evidence/provenance. It keeps
the identities distinct:

```text
IF-*    surface or contract
INT-*   concrete interaction or access edge
EVENT-* semantic event or message
```

An `EVENT-*` may be rendered without an IF. A webhook may render an EVENT, an
IF, and an INT together when all three accepted facts exist, without aliasing
their identities. External integrations render only qualified external
logical identity, safe source binding or explicit limitation, provider/owner
when evidenced, and safe identifier fields. A configured URL, SDK, or
infrastructure declaration alone remains a weak hint and is not rendered as a
called external system.

### Data, persistence, and migration

`PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` renders accepted DS store/resource
identity, `resource_kind`, `parent_resource_ref` containment, safe address,
precision, Project qualification, and evidence. Containment is shown as
containment only; it does not imply access, ownership, migration authority, or
dependency.

The section renders accepted data access through precise `INT-*` facts and
the controlled modes `READ`, `WRITE`, `READ_WRITE`, `EXECUTE`, `DDL`, and
`MIGRATION`. `READ`/`WRITE`/`READ_WRITE` may display their explicitly derived
navigation relations. `EXECUTE`, `DDL`, and `MIGRATION` are not displayed as
READ or WRITE without separate accepted evidence. Relation-only historical
`READS_FROM`/`WRITES_TO` remains visibly broad and does not gain a fabricated
access mode or precision.

Ownership and evolution are separate rendered facts:

```text
OWNS_STATE             state ownership
MIGRATION_AUTHORITY    schema/data-evolution responsibility
INT access_mode=MIGRATION runtime migration operation
```

The projection may show all three, but it never derives one from another.
Procedure/function DS identity remains distinct from an optional callable IF;
an EXECUTE INT targets the DS object and may reference the callable IF.

### Evidence and limitations

Every selected Stage F section exposes safe evidence/provenance links and a
bounded limitation when the source is dynamic, partial, stale, unavailable,
weak, or unresolved. Evidence source-support classes
`DIRECT_DECLARATION`, `STRONG_INFERENCE`, and `WEAK_HINT` are displayed as
evidence metadata only; they do not replace global confidence/severity,
create STM facts, or promote a weak hint. The projection never infers an API
call from a config URL, service use from an SDK dependency, table access from
a DB connection, runtime access from a migration declaration, or client use
from an unused generated client.

The Technical Documentation projection is not a factual authority. It can
repair presentation of unchanged accepted facts, but semantic disagreement
routes to the owning STM, evidence, coverage, or revalidation gate.

A later matching fact, a removed member, or a member revision change is
selector impact even when no individually named exact dependency changed. The
selector and snapshot follow
[`projection-dependencies.md`](projection-dependencies.md); a filename,
directory listing, generated index, or the phrase "documented scope" is never
a substitute for the recorded predicate and snapshot.

Each selected projection also records a `SEMANTIC_EXACT` dependency on the
accepted Technical Model Coverage record bound to that projection. A `FULL`
coverage record may satisfy that binding; a bounded document records its
accepted targeted-coverage record instead. The coverage binding preserves
`NOT_APPLICABLE`, partial, unknown, stale, and authority-unresolved states as
visible limitations. It does not let the document fill a missing STM fact or
turn incomplete coverage into accepted system knowledge.

`PKG-TECHNICAL-DOCUMENTATION` is the capability-owned publication package:

The conditional `documentation_sections.01..09` values are a persisted
`TECH-DOC-SCOPE-*` section-selection record owned by Technical Documentation.
`NEW` initializes the record from the requested documentation scope, `EXTEND`
preserves it, and legacy registration must create or explicitly block until it
can create the binding. A path, filename, or inferred prose relevance cannot
resolve conditional membership.

```text
package_id: PKG-TECHNICAL-DOCUMENTATION
owner: Technical Documentation
gate: Technical Documentation publication
freshness_policy: ALL_SCOPED_CURRENT
required_members:
  - projection_id: PRJ-TECH-DOC-00-SYSTEM-OVERVIEW
    purpose: required entry projection for the accepted system context
    mandatory_prerequisites: []
optional_members: []
conditional_members:
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_01_SELECTED
    when: persisted documentation_sections.01 = true
    projection_id: PRJ-TECH-DOC-01-COMPONENTS
    purpose: publish the selected component/runtime-unit section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_02_SELECTED
    when: persisted documentation_sections.02 = true
    projection_id: PRJ-TECH-DOC-02-PROVIDED-INTERFACES
    purpose: publish the selected provided-interface section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_03_SELECTED
    when: persisted documentation_sections.03 = true
    projection_id: PRJ-TECH-DOC-03-CONSUMED-INTERFACES
    purpose: publish the selected consumed-interface section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_04_SELECTED
    when: persisted documentation_sections.04 = true
    projection_id: PRJ-TECH-DOC-04-INTEGRATIONS
    purpose: publish the selected integration section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_05_SELECTED
    when: persisted documentation_sections.05 = true
    projection_id: PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE
    purpose: publish the selected data-and-persistence section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_06_SELECTED
    when: persisted documentation_sections.06 = true
    projection_id: PRJ-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT
    purpose: publish the selected runtime-and-deployment section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_07_SELECTED
    when: persisted documentation_sections.07 = true
    projection_id: PRJ-TECH-DOC-07-AUTH-AND-TRUST
    purpose: publish the selected authentication-and-trust section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_08_SELECTED
    when: persisted documentation_sections.08 = true
    projection_id: PRJ-TECH-DOC-08-MATERIAL-FLOWS
    purpose: publish the selected material-flow section
    mandatory_prerequisites: []
  - condition_id: TECHNICAL_DOCUMENTATION_SECTION_09_SELECTED
    when: persisted documentation_sections.09 = true
    projection_id: PRJ-TECH-DOC-09-FAILURE-BEHAVIOR
    purpose: publish the selected failure-behavior section
    mandatory_prerequisites: []
```

The controlled section-selection conditions resolve to a finite list of the
listed `PRJ-*` identities before the gate runs. They do not use a filename
glob, an open-ended subject query, or a selector to calculate package
membership. A project may therefore omit unselected recommended sections
without treating them as stale required output.

## Stage F redaction and safety

Projection rendering consumes the shared evidence sensitivity classification;
it does not create a second classification authority. Every technical
identifier selected for display is exactly one of:

```text
SECRET
SENSITIVE_INTERNAL
SAFE_TECHNICAL_IDENTIFIER
```

`SECRET` values are omitted. This includes passwords, API keys, tokens,
private keys, raw environment values, secret query parameters, and
credential-bearing URL or DSN material. A projection may retain a safe source
pointer and the fact that secret material was present, but never the value.

`SENSITIVE_INTERNAL` values are rendered only as an approved safe logical
alias or redacted form. Private hostnames, usernames, sensitive filesystem
paths, and internal locators are not silently treated as safe. A
`SAFE_TECHNICAL_IDENTIFIER` may render when the source policy permits it,
including a logical service/store name, ordinary public path template,
schema/table name, event name, or non-secret operation name.

For credential-bearing URLs and DSNs, the generated section may show the
technology, logical store, database/schema, and safe endpoint class, but not
the raw value or secret query string. An unclassified value is not safe merely
because a user-facing section would be useful. The same rule applies to
Service sections, Product-qualified views, dependency metadata, fingerprints,
and package summaries.

## Stage F Product-qualified views and lifecycle

Task 3 registers Product views as qualified uses of the existing Service
projections. These names are rendering views, not new factual families or
projection identities:

| Product view | Existing projection and selector | Existing package section |
|---|---|---|
| Product Interface Catalog | `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` / `SEL-TECH-DOC-02` and `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` / `SEL-TECH-DOC-03` | 02 and 03 |
| Product Integration Map | `PRJ-TECH-DOC-04-INTEGRATIONS` / `SEL-TECH-DOC-04` | 04 |
| External Integrations Catalog | external subsection of `PRJ-TECH-DOC-04-INTEGRATIONS` / `SEL-TECH-DOC-04`; `PRJ-TECH-DOC-07-AUTH-AND-TRUST` when auth is selected | 04, and 07 when selected |
| Product Data Access Map | `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` / `SEL-TECH-DOC-05` | 05 |
| optional Provider/Consumer Matrix | qualified view in the existing interface/integration projections | 04 when selected |

Each selected Product view retains the existing selector identity and records
an explicit selector `definition_revision`. Its Product-qualified resolution
snapshot contains, as separate fields:

```text
product_identity/revision
immutable_product_baseline
finite_qualified_project_and_external_inputs
exact_local_stm_ids_and_revisions
source_bindings_and_limitations
semantic_availability / coverage / projection_freshness / package_status
```

Dynamic membership uses `SEMANTIC_SELECTOR`; named IF/INT/DS/CC/coverage
inputs use `SEMANTIC_EXACT`; `PROJECTION_EXACT` is used only when an existing
upstream projection is explicitly consumed. A Product snapshot cannot alias
same-named records across Projects, turn unavailable inputs into clean or
failed global Product results, or grant repository, read/write, test, or Git
permission.

Every mapped `PRJ-*` retains the existing lifecycle fields: stable identity,
owning capability, projection contract revision, semantic dependencies,
resolved dependency/selector snapshot, `V1 STRUCTURAL`, `V2 DEPENDENCY /
PROVENANCE`, `V3 CONTRACT COMPLETENESS`, `V4 AUTHORITY CONSISTENCY`, canonical
fingerprint, verified revision, and `CURRENT`/`STALE`/`BLOCKED` freshness. A
dependency, selector, Product qualification, or contract change marks only
the affected projection stale or blocked. Regeneration remains an explicit
`RG-*` action; Technical Documentation never regenerates automatically and
never becomes semantic input.

## Historical compatibility and authority invariants

This projection extension is a compatible additive migration. An old broad
HTTP IF remains valid when operation properties are absent; an old store-level
DS remains valid without child resources; an old INT remains valid without an
access mode; and an old EVENT remains valid without protocol-specific
transport details. Relation-only `READS_FROM`/`WRITES_TO` remains a broad
historical fact and is not backfilled into a precise INT. Existing Project-
local facts require no Product conversion, and no old ID or evidence meaning
is rewritten.

Selectors treat absent Stage F qualifiers as absent, unknown, or
inapplicable. They do not treat absence as false exactness, compatibility,
clean output, or permission. New qualifiers require accepted STM/evidence
authority and create a new revision or child fact under the STM rules; the
projection does not bulk-regenerate or silently enrich history.

The projection consumes these authorities without duplicating them:

```text
WS-* / EV-*        evidence and provenance
STM                accepted technical facts and precision
CC-*               compatibility status and adjudication
PRJ-*              rendered documentation projection
Architecture Review interpretation and findings
```

No projection text, selector, package, fingerprint, or freshness state can
create an accepted IF/INT/DS/EVENT fact, infer access or migration authority,
resolve compatibility, promote a weak hint, or become a second redaction or
projection-lifecycle authority. Product remains optional and single-project
operation remains first-class.

## Human synthesis contract

Write coherent explanatory prose. Use tables, relative cross-links, and
Mermaid diagrams when they improve comprehension. Internal IDs provide
traceability, but they never replace an explanation of the system behavior,
boundaries, or limitations.

Technical Documentation is distinct from the final Architecture Review and its
findings ledger. For the final-report package and cross-link rules, see
[`report-contract.md`](report-contract.md). Neither a generated document nor a
generated index becomes factual authority because it is newer, longer, or
easier to read.

## Authority and projection dependencies

Each Technical Documentation projection records direct `PROJECTS_FROM`
dependencies with the projection artifact. The Stage A spelling is mapped
losslessly to the Stage B `SEMANTIC_EXACT` and `SEMANTIC_SELECTOR` contracts
above before it can drive regeneration. It records both the accepted/fresh STM
objects it names directly and selectors for each fact set it covers. The
selector form is necessary: a newly accepted matching fact can make a section
stale even when no recorded object changed.

For example, a projection package can record dependencies equivalent to:

```text
PROJECTS_FROM the recorded SEL-TECH-DOC-00-SYSTEM-OVERVIEW resolution
PROJECTS_FROM the recorded SEL-TECH-DOC-01-COMPONENTS resolution
PROJECTS_FROM the recorded SEL-TECH-DOC-02-PROVIDED-INTERFACES resolution
PROJECTS_FROM the recorded SEL-TECH-DOC-03-CONSUMED-INTERFACES resolution
PROJECTS_FROM the recorded selected-section selector resolutions
PROJECTS_FROM the accepted required-domain coverage record
```

The source projection owns this direct metadata. Reverse indexes are
reconstructable navigation aids, not authority. A dependency change follows the
impact semantics of `technical-model-dependencies.md`; it does not permit the
projection to change facts. `PRJ-TECH-DOC-*` is never STM authority: projection
generation, verification, package freshness, or a readable document's newer
revision cannot accept, revise, resolve, or supersede an STM fact or coverage
record. Missing, stale, partial, or conflicting authority blocks or limits the
projection through its owning STM/coverage gate rather than being repaired in
documentation prose.

## Product Technical Documentation scope

Product Technical Documentation reuses `PRJ-TECH-DOC-*`,
`TECH-DOC-SCOPE-*`, and `PKG-TECHNICAL-DOCUMENTATION`. A Product-qualified
selector snapshot records the accepted Product identity/revision/baseline,
selector contract revision, finite qualified STM IDs and revisions, and the
Project/external source bindings used for each selected section. It records
limitations and coverage requirements without making documentation the STM or
coverage authority.

Product section membership is explicit and finite. `ALL_SCOPED_CURRENT` is
evaluated only over the resolved required Technical Documentation members and
their dependency closure. A stale or unavailable member limits or blocks the
affected package scope according to the existing gate policy, while unrelated
Project packages remain independent. Product member changes are handled by
Projection Impact Analysis before an explicit `RG-*` regeneration; no
regeneration is implicit.
