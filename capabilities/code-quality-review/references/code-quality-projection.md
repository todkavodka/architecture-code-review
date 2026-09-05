# Code Quality Stage B projection contract

This reference maps Code Quality semantic authority to the approved Stage B
projection lifecycle. It defines Code Quality's projection identities,
dependencies, and package declaration; it does not create semantic authority or
redefine Stage B lifecycle, verification, impact, regeneration, or package
policies.

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

The following stable identities are independently regeneratable. Output paths
are declared by the selected package and do not define identity.

| Projection | Human-readable output | Direct semantic inputs |
|---|---|---|
| `PRJ-CQ-00-FINDINGS-VIEW` | Code Quality Findings View/Report | selected accepted `CQ-*` records; Code Quality coverage state |
| `PRJ-CQ-01-SUMMARY` | Code Quality Summary | selected accepted `CQ-*` records; linked `CQRA-*` records when remediation status is shown; Code Quality coverage state |
| `PRJ-CQ-02-HOTSPOTS` | Maintainability Hotspots | selected accepted `CQ-*` records; Code Quality coverage state |
| `PRJ-CQ-03-ROADMAP-CONTRIBUTION` | Code Quality Roadmap Contribution | selected accepted `CQ-*` and linked `CQRA-*` records; Code Quality coverage state |

These are all Stage B `PRJ-*` identities. They use the shared projection
contract revision, freshness states, dependency snapshots, `V1`–`V4`,
fingerprint, verified revision, and `RG-*` regeneration workflow. No
Code-Quality-specific lifecycle or validation ladder exists.

## Direct dependency and selector contract

Each projection owns its direct dependency metadata. The selected Code Quality
scope is a persisted scope binding owned by the Code Quality assessment/session
state; a filename, directory, report prose, or inferred relevance cannot
provide membership.

The controlled selectors use only the existing Stage B dimensions:

```text
CODE_QUALITY_FINDING_SELECTOR:
  authoritative_record_type: CQ_FINDING
  allowed dimensions: lifecycle | freshness | applicability | disposition |
                      severity | category | capability_owner | scope_binding
  eligibility: accepted semantic authority AND capability_owner = CODE_QUALITY
               AND scope_binding = <persisted Code Quality scope>
  stable_order: semantic_id ASC, revision ASC

CODE_QUALITY_REMEDIATION_SELECTOR:
  authoritative_record_type: CQRA_ACTION
  allowed dimensions: lifecycle | freshness | capability_owner | scope_binding
  eligibility: Code Quality semantic authority AND capability_owner = CODE_QUALITY
               AND scope_binding = <persisted Code Quality scope>
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

For a new projection type, registration precedes regeneration:

```text
assign PRJ identity
→ bind owning capability and projection-contract revision
→ resolve semantic selectors and coverage dependency snapshot
→ generate candidate output
→ V1 STRUCTURAL
→ V2 DEPENDENCY / PROVENANCE
→ V3 CONTRACT COMPLETENESS
→ V4 AUTHORITY CONSISTENCY
→ canonical fingerprint comparison
→ publish verified PRJ-*@revN or NO_CHANGE
→ persist CURRENT, STALE, or BLOCKED
```

The normative meanings and failure routing for these stages remain in
`references/projection-lifecycle.md` and
`references/projection-verification.md`. An unchanged fingerprint returns
`NO_CHANGE` and retains the existing revision; a changed fingerprint publishes
a new verified revision only after all applicable gates pass. Running a
generator alone does not create a revision or `CURRENT` state.

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

CQRA completion or a linked CQ finding revalidation is a semantic dependency
change for projections that consume the affected record. PIA may mark those
projections stale or blocked, but CQRA lifecycle never becomes projection
lifecycle and completion never implicitly regenerates an output.
