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

## Projection dependencies

Each Technical Documentation projection records direct `PROJECTS_FROM`
dependencies with the projection artifact. It records both the accepted/fresh
STM objects it names directly and selectors for each fact set it covers. The
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
projection to change facts. This metadata is the Stage A foundation for future
Stage B regeneration, which is not implemented here.
