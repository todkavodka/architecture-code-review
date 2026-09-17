# Code Quality Stage B projection contract

This reference maps Code Quality semantic authority to the approved Stage B
projection lifecycle. It defines Code Quality's projection identities,
dependencies, delivery paths, and package declaration; it does not create
semantic authority or redefine Stage B lifecycle, verification, impact,
regeneration, or package policies.

## Authority boundary

The source authorities are accepted `CQ-*` findings, `CQRA-*` remediation
actions where a projection explicitly needs remediation data, and the bounded
Code Quality assessment/session coverage state. Projections are
reconstructable, non-authoritative outputs:

```text
CQ/CQRA/coverage authority != PRJ-* projection
projection prose != semantic authority
```

Findings View/Report, Summary, Hotspots, and Roadmap Contribution cannot create,
resolve, reclassify, or mutate `CQ-*`, `CQRA-*`, `RF-*`, Test Engineering
authority, `STM`, or roadmap authority. A disagreement is handled by the
owning semantic or projection gate; the projection does not adjudicate it.

## Registered projections

The following stable identities are independently regeneratable. Registration
declares each artifact path; package selection selects registered projections
and does not supply missing registration metadata. Paths remain distinct from
projection identities, and a path change does not create a new identity when
the projection meaning and contract remain unchanged.

Code Quality human-readable delivery projections live with the capability, not
under `working/`. The canonical paths are relative to the architecture-review
package root:

| Projection | Declared artifact path | Human-readable output | Direct semantic inputs |
|---|---|---|---|
| `PRJ-CQ-00-FINDINGS-VIEW` | `capabilities/code-quality-review/00-code-quality-findings.md` | Code Quality Findings View/Report | selected accepted `CQ-*` records; Code Quality coverage state |
| `PRJ-CQ-01-SUMMARY` | `capabilities/code-quality-review/01-code-quality-summary.md` | Code Quality Summary | selected accepted `CQ-*` records; linked `CQRA-*` records when remediation status is shown; Code Quality coverage state |
| `PRJ-CQ-02-HOTSPOTS` | `capabilities/code-quality-review/02-maintainability-hotspots.md` | Maintainability Hotspots | selected accepted `CQ-*` records; Code Quality coverage state |
| `PRJ-CQ-03-ROADMAP-CONTRIBUTION` | `capabilities/code-quality-review/03-roadmap-contribution.md` | Code Quality Roadmap Contribution | selected accepted `CQ-*` and linked `CQRA-*` records; Code Quality coverage state |

These are all Stage B `PRJ-*` identities. Each is a `DERIVED_PROJECTION` and
`USER_SELECTABLE` output: it is derived from the listed accepted semantic
authority, but selection is explicit and no projection is automatically enabled
or mandatory merely because Code Quality Review is selected. They use the
shared projection contract revision, freshness states, dependency snapshots,
`V1`–`V4`, fingerprint, verified revision, and `RG-*` regeneration workflow. No
Code-Quality-specific lifecycle or validation ladder exists.

### Delivery-path migration

The earlier declared paths under:

```text
working/projections/code-quality/
```

are superseded delivery locations. Moving an existing verified Code Quality
projection to the capability-owned path preserves its stable `PRJ-CQ-*`
identity and semantic dependencies, but the declared path is part of the
projection contract. Therefore the path migration is a projection-contract
change and requires the normal lifecycle reconciliation before the moved output
may be `CURRENT`.

Do not keep both paths as current copies. The `working/projections/` namespace
is reserved for operational Stage B views such as registry, impact, and
regeneration-session state; it is not the publication location for Code Quality
human-readable deliverables.

## Direct dependency and selector contract

Each projection owns its direct dependency metadata. The selected Code Quality
scope is a persisted scope binding owned by the Code Quality assessment/session
state; a filename, directory, report prose, or inferred relevance cannot
provide membership.

The controlled selectors use only the existing Stage B dimensions. CQ-specific
fields are formal structured properties of the selected authoritative records,
not additional Stage B selector dimensions:

```text
CODE_QUALITY_FINDING_SELECTOR:
  authoritative_record_type: CQ_FINDING
  allowed dimensions: entity_type | status | freshness |
                      structured_properties | formal_relations | capability_owner
  allowed operators: = | IN | HAS_ANY
  logical_connectors: AND | OR
  predicate: status = ACCEPTED AND freshness = CURRENT
             AND capability_owner = CODE_QUALITY
             AND structured_properties.cq_scope_binding = <persisted Code Quality scope>
  formal structured properties: cq_scope_binding | lifecycle | applicability |
                                disposition | severity | category
  stable_order: semantic_id ASC, revision ASC

CODE_QUALITY_REMEDIATION_SELECTOR:
  authoritative_record_type: CQRA_ACTION
  allowed dimensions: entity_type | status | freshness |
                      structured_properties | formal_relations | capability_owner
  allowed operators: = | IN | HAS_ANY
  logical_connectors: AND | OR
  predicate: status IN [PROPOSED, PLANNED, COMPLETED]
             AND freshness = CURRENT
             AND capability_owner = CODE_QUALITY
             AND structured_properties.cq_scope_binding = <persisted Code Quality scope>
  formal structured properties: cq_scope_binding | lifecycle
  stable_order: semantic_id ASC, revision ASC

coverage_dependency:
  kind: SEMANTIC_EXACT
  authority: accepted Code Quality assessment/session coverage state + revision
```

The selector resolution snapshot records the selector contract revision and
the exact ordered `CQ-*`/`CQRA-*` identities and revisions consumed. A change
in membership or member revision is Stage B selector impact. The selectors do
not perform materiality adjudication, reinterpret prose, or promote a
projection to authority.

### Product Code Quality selectors and summary

When Product mode is selected, a Code Quality selector may resolve Product
records only from the exact persisted Product scope binding. Product selector
resolution records the selected `PROD-*` identity, accepted Product revision,
immutable Product baseline, qualified affected Projects, and the ordered
`CQ-*`/`CQRA-*` identities and revisions consumed. Local
`REPOSITORY:<repository>` selectors remain valid and are not rewritten or
implicitly widened by Product membership.

Product Code Quality projections reuse the existing `PRJ-*` identities,
`RG-*` regeneration sessions, Stage B dependency kinds, V1–V4 gates, and
package policies. Their Product dependencies include the selected Product
semantic CQ/CQRA records, required Code Quality coverage state, and any
declared qualified evidence/STM or baseline dependency. A Product Summary is a
derived projection/navigation output: it may aggregate explicit local and
Product dependencies but cannot create, revise, resolve, or supersede CQ or
CQRA authority. Product scope does not make unselected member-project records
package members.

Product CQ/CQRA freshness follows semantic impact accounting separately from
projection freshness. A changed Product baseline or required cross-project
binding can make a dependent projection `STALE` or `BLOCKED`; it does not
automatically regenerate the projection or invalidate unrelated local CQ
authority. `ALL_SCOPED_CURRENT` applies only to the resolved named package
scope and its mandatory dependencies.

The direct projection dependencies are:

| Projection | Dependency declarations |
|---|---|
| `PRJ-CQ-00-FINDINGS-VIEW` | `SEMANTIC_SELECTOR CODE_QUALITY_FINDING_SELECTOR`; `SEMANTIC_EXACT` Code Quality coverage state |
| `PRJ-CQ-01-SUMMARY` | `SEMANTIC_SELECTOR CODE_QUALITY_FINDING_SELECTOR`; `SEMANTIC_SELECTOR CODE_QUALITY_REMEDIATION_SELECTOR` when remediation data is rendered; `SEMANTIC_EXACT` Code Quality coverage state |
| `PRJ-CQ-02-HOTSPOTS` | `SEMANTIC_SELECTOR CODE_QUALITY_FINDING_SELECTOR`; `SEMANTIC_EXACT` Code Quality coverage state |
| `PRJ-CQ-03-ROADMAP-CONTRIBUTION` | `SEMANTIC_SELECTOR CODE_QUALITY_FINDING_SELECTOR`; `SEMANTIC_SELECTOR CODE_QUALITY_REMEDIATION_SELECTOR`; `SEMANTIC_EXACT` Code Quality coverage state |

No projection depends on another CQ projection by default. If a later contract
adds such a dependency, it must be declared as `PROJECTION_EXACT` in the
consumer-owned metadata with the canonical direction `consumer -> prerequisite`.

## Stage B generation and freshness

For a new projection type, registration precedes publication:

```text
assign PRJ identity
→ bind owning capability and projection-contract revision
→ resolve semantic selectors and coverage dependency snapshot
→ generate candidate output
→ V1 STRUCTURAL
→ V2 DEPENDENCY / PROVENANCE
→ V3 CONTRACT COMPLETENESS
→ V4 AUTHORITY CONSISTENCY
→ canonical fingerprint
→ publish verified PRJ-*@revN
→ persist CURRENT
```

For an existing verified projection, a requested regeneration follows the
shared `RG-*` workflow and may publish a new revision or verified `NO_CHANGE`.
The normative meanings and failure routing for these stages remain in
`references/projection-lifecycle.md` and
`references/projection-verification.md`.

A selected Code Quality Markdown file does not satisfy the delivery package by
existing on disk. Git tracked/untracked state, file timestamp, YAML prose, or an
ad-hoc hash computed after generation is not a projection revision or canonical
verification fingerprint. Until the lifecycle record contains the accepted
`PRJ-*` revision, dependency snapshot, V1–V4 results, canonical fingerprint,
and `CURRENT`, that selected projection is not publishable package evidence.

Semantic change or changed selector/coverage dependency flows through the
existing Projection Impact Analysis. It identifies affected projections and
records freshness/required action; it does not regenerate content. A requested
fresh output uses the shared `RG-*` workflow. `PROJECTION_REPAIR` repairs only
presentation of unchanged accepted meaning and cannot change Code Quality
semantics.

Therefore all of these remain valid and distinct:

```text
CQ semantic freshness != projection freshness
REVALIDATE != regeneration
PROJECTION_REPAIR != semantic remediation
```

If CQ semantic authority is stale or blocked, the affected projection follows
the shared dependency and authority gates. A projection may accurately render
`PARTIAL` coverage while remaining `CURRENT`; coverage state does not become
projection freshness, and a stale projection does not invalidate semantic
findings.

## Code Quality delivery package

Code Quality uses the existing package policies exactly. Each package instance
persists one of:

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

The package declaration is finite and output-driven:

```text
package_id: PKG-CODE-QUALITY-DELIVERY
owner: Code Quality Review
gate: Code Quality projection publication/closeout
freshness_policy: PERMISSIVE | REQUIRED_SCOPE_CURRENT | ALL_SCOPED_CURRENT
required_members: []
optional_members: []
conditional_members:
  - condition_id: CODE_QUALITY_FINDINGS_VIEW_SELECTED
    when: persisted outputs.findings_view = true
    projection_id: PRJ-CQ-00-FINDINGS-VIEW
    mandatory_prerequisites: []
  - condition_id: CODE_QUALITY_SUMMARY_SELECTED
    when: persisted outputs.code_quality_summary = true
    projection_id: PRJ-CQ-01-SUMMARY
    mandatory_prerequisites: []
  - condition_id: CODE_QUALITY_HOTSPOTS_SELECTED
    when: persisted outputs.maintainability_hotspots = true
    projection_id: PRJ-CQ-02-HOTSPOTS
    mandatory_prerequisites: []
  - condition_id: CODE_QUALITY_ROADMAP_CONTRIBUTION_SELECTED
    when: persisted outputs.roadmap_contribution = true
    projection_id: PRJ-CQ-03-ROADMAP-CONTRIBUTION
    mandatory_prerequisites: []
```

Resolved package membership is explicit selected output plus declared
dependency closure, not all supported projections. Thus selecting Findings
View and Summary does not require unselected Hotspots or Roadmap Contribution;
because the registered CQ projections currently consume semantic authority
directly, that closure contains no CQ projection prerequisite by default.

`PERMISSIVE` permits stale or blocked non-required projections with explicit
limitations. `REQUIRED_SCOPE_CURRENT` requires only selected projections and
their mandatory dependency closure to be `CURRENT`. `ALL_SCOPED_CURRENT`
requires every projection resolved into the named package scope to be current.
These meanings are inherited without CQ-specific variants. Package state
governs projection usability only; it does not validate or invalidate CQ
semantic authority.

A selected package member whose lifecycle evidence is missing or incomplete is
not `CURRENT` and therefore cannot satisfy a package gate that requires current
members. Do not classify such a package as valid merely because all declared
files exist.

CQRA completion or a linked CQ finding revalidation is a semantic dependency
change for projections that consume the affected record. PIA may mark those
projections stale or blocked, but CQRA lifecycle never becomes projection
lifecycle and completion never implicitly regenerates an output.
