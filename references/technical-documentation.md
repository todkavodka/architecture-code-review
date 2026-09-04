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
  formal_relations
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
| `SEL-TECH-DOC-02-PROVIDED-INTERFACES` | `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` | `STM_FACT` | `entity_type = IF AND structured_properties.direction = PROVIDED` |
| `SEL-TECH-DOC-03-CONSUMED-INTERFACES` | `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` | `STM_FACT` | `entity_type = IF AND structured_properties.direction = CONSUMED` |
| `SEL-TECH-DOC-04-INTEGRATIONS` | `PRJ-TECH-DOC-04-INTEGRATIONS` | `STM_FACT` | `entity_type IN [INT, EVENT]` |
| `SEL-TECH-DOC-05-DATA-AND-PERSISTENCE` | `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` | `STM_FACT` | `entity_type = DS OR formal_relations HAS_ANY [READS_FROM, WRITES_TO, OWNS_STATE]` |
| `SEL-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT` | `PRJ-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT` | `STM_FACT` | `entity_type IN [COMP, CFG] OR formal_relations HAS_ANY [DEPLOYS_AS, DEPENDS_ON, CONFIGURED_BY]` |
| `SEL-TECH-DOC-07-AUTH-AND-TRUST` | `PRJ-TECH-DOC-07-AUTH-AND-TRUST` | `STM_FACT` | `entity_type IN [AUTH, IF, CFG] OR formal_relations HAS_ANY [PROTECTED_BY, CONFIGURED_BY]` |
| `SEL-TECH-DOC-08-MATERIAL-FLOWS` | `PRJ-TECH-DOC-08-MATERIAL-FLOWS` | `STM_FACT` | `entity_type IN [FLOW, INT, EVENT] OR formal_relations HAS_ANY [CALLS, PUBLISHES, SUBSCRIBES, PARTICIPATES_IN]` |
| `SEL-TECH-DOC-09-FAILURE-BEHAVIOR` | `PRJ-TECH-DOC-09-FAILURE-BEHAVIOR` | `STM_FACT` | `entity_type IN [ERR, IF, INT, EVENT] OR formal_relations HAS_ANY [EMITS_ERROR]` |

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
