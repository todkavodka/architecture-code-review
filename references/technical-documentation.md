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
| `PRJ-TECH-DOC-00-SYSTEM-OVERVIEW` | `00-system-overview.md` | system context and the material cross-domain facts selected for the documented scope |
| `PRJ-TECH-DOC-01-COMPONENTS` | `01-components.md` | `COMP-*` runtime-unit facts and their material relations |
| `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` | `02-provided-interfaces.md` | `IF-*` where `direction = PROVIDED` |
| `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` | `03-consumed-interfaces.md` | `IF-*` where `direction = CONSUMED` |
| `PRJ-TECH-DOC-04-INTEGRATIONS` | `04-integrations.md` | material `INT-*` and `EVENT-*` facts |
| `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` | `05-data-and-persistence.md` | material `DS-*` facts and their data relations |
| `PRJ-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT` | `06-runtime-and-deployment.md` | material `COMP-*`, `CFG-*`, and runtime relations |
| `PRJ-TECH-DOC-07-AUTH-AND-TRUST` | `07-auth-and-trust.md` | material `AUTH-*`, `IF-*`, and `CFG-*` trust facts |
| `PRJ-TECH-DOC-08-MATERIAL-FLOWS` | `08-material-flows.md` | material `FLOW-*`, `INT-*`, and `EVENT-*` facts |
| `PRJ-TECH-DOC-09-FAILURE-BEHAVIOR` | `09-failure-behavior.md` | material `ERR-*`, `IF-*`, `INT-*`, and `EVENT-*` failure facts |

The projection itself owns its direct outbound metadata. For every fact it
names individually, that metadata records a revision-bound `SEMANTIC_EXACT`
dependency. For every dynamic fact set in the table, it records a
`SEMANTIC_SELECTOR` dependency with all of the following:

```text
selector_id: <stable projection-local selector ID>
definition_revision: <revision of the selector predicate>
predicate: STM family/relation/direction and documented scope
eligibility: ACCEPTED + VALID freshness + RESOLVED authority
resolved_members: [<STM-ID>@<revision> ...]
```

For example, `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` owns a selector whose
predicate is accepted, fresh, resolved `IF-*` facts in its documented scope
where `direction = PROVIDED`; its verified projection revision stores the
resulting `IF-*` identities and revisions. A later matching interface, a
removed member, or a member revision change is selector impact, even when no
previously named exact dependency changed. The selector and snapshot follow
[`projection-dependencies.md`](projection-dependencies.md); a filename,
directory listing, or generated index is never a substitute for either.

Each selected projection also records a `SEMANTIC_EXACT` dependency on the
accepted Technical Model Coverage record for the documented scope. A `FULL`
coverage record may satisfy that binding; a bounded document records its
accepted targeted-coverage record instead. The coverage binding preserves
`NOT_APPLICABLE`, partial, unknown, stale, and authority-unresolved states as
visible limitations. It does not let the document fill a missing STM fact or
turn incomplete coverage into accepted system knowledge.

`PKG-TECHNICAL-DOCUMENTATION` is the capability-owned publication package:

```text
owner: Technical Documentation
gate: Technical Documentation publication
freshness_policy: ALL_SCOPED_CURRENT
required_members:
  - PRJ-TECH-DOC-00-SYSTEM-OVERVIEW
conditional_members:
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:01
    -> PRJ-TECH-DOC-01-COMPONENTS
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:02
    -> PRJ-TECH-DOC-02-PROVIDED-INTERFACES
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:03
    -> PRJ-TECH-DOC-03-CONSUMED-INTERFACES
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:04
    -> PRJ-TECH-DOC-04-INTEGRATIONS
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:05
    -> PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:06
    -> PRJ-TECH-DOC-06-RUNTIME-AND-DEPLOYMENT
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:07
    -> PRJ-TECH-DOC-07-AUTH-AND-TRUST
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:08
    -> PRJ-TECH-DOC-08-MATERIAL-FLOWS
  - TECHNICAL_DOCUMENTATION_SECTION_SELECTED:09
    -> PRJ-TECH-DOC-09-FAILURE-BEHAVIOR
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
PROJECTS_FROM accepted/fresh STM facts selected for system overview
PROJECTS_FROM accepted/fresh component facts
PROJECTS_FROM accepted/fresh interface facts where direction = PROVIDED
PROJECTS_FROM accepted/fresh interface facts where direction = CONSUMED
PROJECTS_FROM accepted/fresh facts for integrations, data, runtime, auth, flows,
              and failure behavior when their sections are included
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
