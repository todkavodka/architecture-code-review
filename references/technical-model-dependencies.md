# Technical Model dependencies and impact

This contract owns direct dependency metadata, generated dependency indexes,
impact strength, selector dependencies, and bounded dependency traversal. It
applies to authoritative evidence, STM, capability, and projection artifacts.
It does not make an index, a projection, or an impact route semantic authority.

Projection-specific dependency kinds, controlled selector contracts, selector
resolution snapshots, and the projection regeneration DAG are specialized in
[Projection dependency contracts](projection-dependencies.md). That reference
adds Stage B rules without changing the Stage A direct-metadata authority
defined here.

Each authoritative artifact owns its direct outbound dependency metadata. A
generated registry may aggregate that metadata, but direct metadata remains the
source of truth for the artifact's semantic dependencies.

## 1. Typed direct dependencies

Use this controlled edge vocabulary:

```text
EVIDENCED_BY
DERIVED_FROM
DEPENDS_ON
REFERENCES
SUPERSEDES
PROJECTS_FROM
```

- `EVIDENCED_BY` binds a fact or conclusion to an addressable `WS-*` / `EV-*`
  observation that supports it.
- `DERIVED_FROM` identifies an authoritative artifact from which the dependent
  artifact was derived.
- `DEPENDS_ON` identifies a semantic prerequisite for the dependent artifact.
- `REFERENCES` records a material cross-artifact reference that does not itself
  claim derivation or prerequisite semantics.
- `SUPERSEDES` preserves revision or identity history. It is not an ordinary
  invalidation dependency and is not traversed as one.
- `PROJECTS_FROM` identifies authoritative inputs of a human-readable or other
  derived projection.

The edge type and impact strength are separate. An edge records why the
relationship exists; its impact strength records the default route if its input
changes. `SUPERSEDES` is historical metadata and has no ordinary impact route.

## 2. Direct metadata and aspect extension

The initial accepted implementation is artifact-level. A direct dependency
records at least its `type`, target artifact or selector, and impact strength
when it participates in impact traversal. For example:

```text
dependencies:
  - type: DEPENDS_ON
    artifact: IF-021
    impact: HARD
```

The schema may optionally narrow a future dependency to aspects without making
field-level completeness mandatory now:

```text
dependency:
  type: DEPENDS_ON
  artifact: IF-021
  aspects: [auth, responses]
  impact: HARD
```

When aspects are absent, impact is assessed at artifact level. Do not create
field-level artifacts merely to obtain finer invalidation.

## 3. Impact strength

Use exactly these initial impact strengths:

```text
HARD
CONDITIONAL
INFORMATIONAL
```

```text
HARD change
  -> REVALIDATION_REQUIRED for dependent semantic use

CONDITIONAL change
  -> IMPACT_REVIEW_REQUIRED

INFORMATIONAL change
  -> no semantic invalidation by default
```

This is impact-routing default behavior, not proof that a dependent conclusion
changed or became false. Revalidation or impact review evaluates the conclusion
against current evidence and authority.

## 4. Generated indexes

Generated indexes are reproducible navigation and traversal projections of
authoritative artifact metadata. At minimum, the generated set provides:

```text
artifact registry
reverse dependencies
capability/dependency lookup
stale/impact lookup
projection dependencies
```

Exact file names follow repository convention. Every entry is reconstructable
from authoritative direct metadata. If an index is lost or stale, rebuild it;
do not reconstruct direct semantic authority from the index or treat an index
entry as stronger than its owning artifact.

Indexes may identify candidate dependents efficiently. Before a semantic status
is changed, use the dependent artifact's direct metadata and current authority
binding as the governing record.

## 5. Projection object and selector dependencies

A projection records its own direct `PROJECTS_FROM` metadata using either:

```text
explicit object ID
selector/set dependency
```

For example:

```text
PROJECTS_FROM IF-021
PROJECTS_FROM all IF-* where direction = CONSUMED
```

A newly accepted object that matches a recorded selector makes the projection
stale or eligible for regeneration even if the object did not exist at the
projection's prior revision. This establishes Stage A dependency foundations;
it does not implement the Stage B regeneration engine.

For Stage B, map each Stage A `PROJECTS_FROM` record to exactly one of
`SEMANTIC_EXACT`, `SEMANTIC_SELECTOR`, or `PROJECTION_EXACT` before using it in
projection regeneration:

```text
PROJECTS_FROM <accepted semantic object ID>@<revision>
  -> SEMANTIC_EXACT <object ID>@<revision>

PROJECTS_FROM <controlled selector/set>
  -> SEMANTIC_SELECTOR <selector contract> + resolved membership snapshot

PROJECTS_FROM PRJ-<upstream>@<verified revision>
  -> PROJECTION_EXACT PRJ-<upstream>@<verified revision>
```

The mapping is lossless: preserve the consuming projection, target identity,
impact strength, and any Stage A selector meaning while adding the Stage B
revision or resolution snapshot required by the mapped kind. `PRJ-*` targets
are mapped to `PROJECTION_EXACT` only when the target is an upstream generated
projection; semantic object IDs remain `SEMANTIC_EXACT`, even when the object
is mentioned by a projection. The canonical edge remains
`CONSUMER -> PREREQUISITE`; migration must not reverse it or copy transitive
semantic dependencies from an upstream projection.

Until a legacy `PROJECTS_FROM` record is classified, it remains valid Stage A
metadata for dependency discovery and reverse-index reconstruction, but it is
not executable Stage B regeneration input. An unclassifiable or revisionless
record requires targeted migration/contract adjudication before regeneration;
do not infer its kind from prose, filenames, or generated indexes. After
classification, the Stage A spelling may be retained as a compatibility alias
for audit history, while the Stage B kind is authoritative for regeneration.

The projection dependency reference defines the controlled selector and
resolved-membership snapshot required to detect member additions, removals,
and revision changes, as well as the canonical edge direction. These Stage B
specializations do not replace consumer-owned direct metadata or derived
reverse indexes.

## 6. Minimum dependency context

A bounded consumer requests the smallest sufficient working set in this order:

```text
current semantic object
+ HARD dependencies
+ unresolved CONDITIONAL dependencies
+ required evidence
```

Use indexes to locate that set, then read owning artifacts. Exclude unrelated
accepted artifacts by default. Expand from the semantic object to its linked
`EV-*` evidence and raw source only when accepted/fresh authority is missing,
stale, disputed, incomplete, or insufficient for the decision.

## 7. REVALIDATE impact traversal

For a changed source or baseline, route the minimum affected slice as:

```text
changed source/baseline
-> affected EV/STM candidates
-> affected direct dependencies/aspects
-> impact traversal
-> only affected capability semantics/projections
```

Use generated indexes to find candidate reverse edges, verify those edges from
owning direct metadata, and apply the recorded impact strength. Unknown or
missing linkage triggers targeted investigation; it cannot support a
"preserved" conclusion. Do not replay the whole STM, capability package, or
projection set without impact evidence.

The detailed source-delta workflow and preserved-set rules remain in
[Revalidation and compact-state freshness](revalidation-and-freshness.md).
