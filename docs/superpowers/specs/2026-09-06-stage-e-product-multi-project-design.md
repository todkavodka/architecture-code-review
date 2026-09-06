# Stage E — Product / Multi-Project Review: Architecture Design

**Date:** 2026-09-06
**Artifact type:** Architecture Design / Planning Baseline
**Approved Discovery checkpoint:** `5342650769d8c33d6b4cd9a675203b3d3b706be5`
**Chosen direction:** `OPTION C — HYBRID`

## 1. Executive summary

Stage E adds an optional Product scope around independently authoritative
Projects. A Product is a durable logical identity and a versioned membership
context; it is not a mandatory hierarchy root, repository, review session,
workspace, or universal semantic owner. A Project is a durable logical
descriptor that can span repositories and can be reused by multiple Products;
its Project-local facts and capability semantics remain owned by the existing
STM, Architecture Review, Test Engineering, and Code Quality contracts.

The Product layer owns only Product context: identity, membership revisions,
baseline snapshots, Product-scoped routing, and the coordination of accepted
cross-project interpretations. It does not create a second factual model.
Cross-project observations reuse `WS-*`/`EV-*` with qualified source and
baseline bindings. Cross-project technical relationships are accepted through
the existing STM Technical Model Gate. Product-scoped Architecture, Test
Engineering, and Code Quality records reuse their existing families with an
explicit Product scope and qualified provenance.

Product baselines are immutable vectors of exact Project source bindings. A
vector can be temporally mixed, but the mixed state is explicit and cannot be
described as an atomic moment. Source availability, review coverage, semantic
availability, projection freshness, and package gate results remain independent
dimensions. `REVALIDATE` is impact-driven and minimum-slice by default;
membership changes create Product revisions and use explicit adjudication.
`EXTEND` is additive unless the requested membership change alters Product
meaning, in which case the new Product revision enters targeted impact-driven
revalidation.

The design remains file-based and compatible with the current Markdown
Skill/reference architecture. It requires no database, service, graph store,
vector store, daemon, automatic repository operation, or hidden write
permission. Product projections are ordinary `PRJ-*` projections governed by
Stage B lifecycle, impact, regeneration, and package contracts.

## 2. Approved Discovery basis

This Design consumes the approved Discovery package without reopening its
resolved findings:

- `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-discovery.md`
- `docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-discovery-review.md`
- `docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-discovery-rereview.md`

The Discovery checkpoint is approved with F-01 through F-04 resolved,
`option_c_recommendation = SUPPORTED`, and passing decision-register,
pressure-scenario, invariant, revalidation, partial-availability, and package
gates. The design therefore resolves the remaining foundational questions; it
does not change the Discovery artifacts or current normative contracts.

## 3. Architecture invariants

The following are design invariants, not implementation preferences:

1. Product mode is opt-in. A single-project review is valid without Product
   identity, membership, baseline vector, cross-project evidence, or Product
   package.
2. Product is not a mandatory parent, universal semantic owner, repository,
   review target, review session, or workspace.
3. Project identity is independent of repository identity and source revision.
4. Repository bindings provide provenance and revision state; they do not
   define Project identity.
5. `WS-*`/`EV-*` remain shared observations, not findings or factual authority.
6. STM remains the sole accepted authority for shared technical facts and
   relations. The Technical Model Gate remains their sole acceptance writer.
7. Architecture Review owns `RF-*`; Test Engineering owns `BC-*`, `CC-*`,
   `MAT-*`, `TM-*`, `GAP-*`, and `TASK-*`; Code Quality Review owns `CQ-*` and
   `CQRA-*`.
8. A projection, generated index, package, or report is never semantic or
   evidence authority merely because it is Product-scoped.
9. A factual relation is not a semantic dependency. A reverse index is not
   direct dependency authority. An impact result is neither.
10. Persisted does not mean current; accepted does not mean complete; coverage
    does not mean depth.
11. `REVALIDATE` is impact-driven and preserves unrelated accepted state.
12. `EXTEND` is additive unless a membership-semantic change is explicitly
    adjudicated and revalidated.
13. `PRJ-*` projection identity and `RG-*` regeneration-session identity remain
    separate.
14. `PROJECTION_REPAIR` cannot conceal source/baseline change or alter semantic
    authority.
15. Product membership grants no repository read/write, checkout, worktree,
    execution, deployment, commit, PR, or push permission.

## 4. Chosen architecture

The chosen architecture is a bounded hybrid:

```text
coordinator review workspace
├── Product identity and revision history
├── Product membership and immutable baseline vectors
├── Project descriptors and repository source bindings
├── Product-scoped WS/EV worksets with qualified bindings
└── Product routing/index projections

Project-local authorities remain independent:
Project WS/EV → STM facts/relations → Architecture/Test/CQ semantics → PRJ-* / packages

Product cross-project path:
qualified Project facts + multi-source WS/EV
    → STM-accepted cross-project relation/fact
    → independently adjudicated Product-scoped capability record
    → PRJ-* Product projection/package
```

The Product context may reference shared resources and accepted Project
authority, but it does not absorb those authorities. Product-scoped semantic
records are accepted by their existing capability owner, not by a generic
Product aggregate. Product state is stored in the coordinator review workspace
and never inside an arbitrary member Project.

## 5. Product identity

### Decision

Introduce one new stable identity family, `PROD-*`, for an explicitly created
Product logical scope. This is necessary because no existing `PRJ-*`, `WS-*`,
`EV-*`, STM family, capability family, package identity, or session identity
means durable Product identity. The new family is limited to Product context;
it is not a generic Product fact or finding family.

Conceptually:

```text
Product Identity
  product_id: PROD-<opaque-stable-key>
  display_name: <human label>
  created_by: <explicit human/session authority>
  lifecycle: ACTIVE | RETIRED
  current_revision: <accepted revision or NONE>
```

The identifier is immutable after creation. Display names, descriptions,
ownership metadata, and membership do not mutate the identity; they create a
new Product revision. Product may be created before any review is complete. A
Product with one Project is valid. Product may be consumed by multiple
independent review sessions, provided each session selects an explicit Product
revision and creates its own immutable review baseline.

Mutable Product state lives in the coordinator-owned Product namespace. Product
identity is not itself a semantic authority for technical facts. Product
membership history is Product semantic context because it determines which
Projects and resources were in scope; it does not determine what those
Projects technically are.

Product identity allocation is performed once by the Product Context Workflow.
Only that workflow may retire the identity, after explicit authorization and
without deleting historical revisions, baselines, or findings.
`current_revision` is a coordinator-maintained convenience pointer to the
latest `ACCEPTED` revision; it is not a fact-authority field and never
retargets an already pinned session. An active Product may have no current
revision while its initial context is being proposed.

## 6. Product revisions

Product revision uses the existing revision convention on the new identity:
`PROD-<key>@revN`. No separate revision family is introduced. A Product
revision is immutable and contains:

```text
product_id
revision
metadata_snapshot
membership_snapshot
shared_resource_declarations
membership_policy_snapshot
created_at / created_by
provenance
supersedes / superseded_by when applicable
lifecycle: PROPOSED | ACCEPTED | SUPERSEDED | RETIRED
coherency_policy: REQUIRE_COHERENT | ALLOW_MIXED_EXPLICIT
```

The following create a new Product revision:

- adding, removing, replacing, or reactivating a Project member;
- changing a member role or requiredness/configuration that affects Product
  meaning;
- adding, removing, or materially changing a shared-resource declaration;
- changing Product-scoped membership semantics or explicit interpretation
  configuration;
- correcting Product metadata that is part of the accepted Product context.

Creating a new review baseline at the same Product revision does not itself
create a Product revision. A review baseline captures source state for one
review event; a Product revision captures the accepted Product context. The
two records reference each other but are never silently treated as identical.

Revision lifecycle is explicit. The Product Context Workflow is the sole
writer and revision allocator for a Product identity. A proposed revision is
an immutable candidate context and can be changed only by superseding it with
a new proposed revision; it cannot be used for accepted semantic records or a
Product baseline. The Product Context Acceptance Gate, operated by the
authorized Product context workflow, changes `PROPOSED` to `ACCEPTED` after
validating identity, membership, policy, and provenance, and advances
`current_revision` atomically. A later accepted revision marks the former
revision `SUPERSEDED`; explicit Product retirement may mark an accepted or
superseded revision `RETIRED` without rewriting it.

Only an `ACCEPTED` revision may be referenced by a Product baseline, Product
scope binding, Product-scoped capability record, projection, or package.
Every session stores the exact Product revision it selected, so concurrent
sessions may use different accepted historical revisions and are unaffected by
a later proposal or acceptance. Product-context lifecycle/currentness belongs
to this workflow; STM, capability, projection, and package freshness remains
owned by their existing contracts. A source change makes dependent baselines
or semantic records stale or blocked; it does not mutate a historical Product
revision or make Product context freshness a substitute for artifact freshness.

## 7. Project identity

### Decision

Use a persistent stable Project descriptor, separate from Project-local STM
and capability semantic authority. The descriptor has an opaque stable
`project_key` in the coordinator registry. It is not a new STM family and not
the `PRJ-*` projection family. Its role is identity and source-context
routing, not technical fact ownership.

The descriptor contains:

```text
project_key: <opaque stable key>
display_name
status: ACTIVE | RETIRED
repository_bindings: [binding references]
profile_refs: [Project Profile revisions]
created_by / created_at
identity_history
```

Changing repository URL, local path, branch, worktree, ref, or repository set
does not change Project identity. Retiring a descriptor preserves historical
references and does not turn a new descriptor into the same Project.

### Separation of concepts

| Concept | Meaning | Mutable/history | Authority |
|---|---|---|---|
| Project Identity | Stable logical unit reused across Products | Descriptor history | Coordinator identity registry |
| Project Revision/Source Binding | Exact source state selected for a review | Immutable per binding | Baseline/evidence owner |
| Repository Binding | Provenance link to a repository and selected scope | Revisioned | Baseline/evidence owner |
| Project Profile | Cheap inventory/routing metadata | Collected per source revision | Session orchestration |
| Review Target | Selected analytical scope inside a Project | Session-specific | Review workflow |
| Review Session | Temporary coordination and authorization context | Ephemeral/persisted workflow state | Coordinator |
| Project semantic authority | Accepted STM/capability records | Revision/lifecycle governed | STM or owning capability |

Project identity can exist without a completed review. A descriptor does not
assert that the Project is currently available, reviewed, or semantically
accepted.

## 8. Repository bindings and cardinality

All four useful cardinalities are supported:

| Relationship | Supported meaning |
|---|---|
| 1 Project → 1 repository | The Project's selected scope is in one repository. |
| 1 Project → N repositories | One logical Project is composed of multiple source repositories. |
| N Projects → 1 repository | A monorepository contains multiple disjoint or explicitly scoped Projects. |
| N Projects → N repositories | A general many-to-many topology, with each Project-to-repository edge explicitly scoped. |

Each `Repository Binding` contains repository identity, locator/ref metadata,
selected path/scope selector, exact source revision or dirty content binding,
baseline type, availability, and provenance. A Project revision is a set of
these bindings, not a repository alias.

Monorepository boundaries are explicit path/scope selectors owned by the
Project source binding. Overlapping selectors are allowed only when each
overlap is explicit and the dependent semantic record qualifies which Project
scope it consumes. An overlap does not make the Projects identical and does
not infer ownership. One Project spanning multiple repositories requires every
contributing binding to be present in the selected baseline or explicitly
marked unavailable.

No Git tooling behavior is specified here. The design only requires that future
implementation preserve exact bindings and never infer identity from a path or
repository URL.

## 9. Product membership

Membership is an embedded immutable entry in each Product revision rather than
a new standalone semantic family:

```text
membership_entry:
  membership_key: <stable key within Product history>
  product_id: PROD-*
  project_key: <stable Project descriptor key>
  role: <bounded Product role>
  requiredness: REQUIRED | OPTIONAL | CONDITIONAL
  condition_ref: <controlled condition or NONE>
  status: ACTIVE | RETIRED
  source/provenance: <explicit human or accepted coordination source>
  effective_from_revision
  effective_to_revision: <or OPEN>
```

The Product context owner writes membership revisions after explicit human
authorization. The Product revision owns membership lifecycle; Project
semantic owners do not change Product membership implicitly. A member's
effective source revision belongs to the Product baseline, not to membership
identity itself.

Membership does not imply technical ownership, repository access, write access,
or semantic authority. Roles describe Product context only. A shared resource
declaration is a separate entry and cannot be represented as a Project member
unless it has an actual Project identity.

## 10. Multi-Product membership

One Project may belong to multiple Products. Each Product owns a separate
membership entry, Product revision history, baseline vector, Product-scoped
interpretation set, and package membership snapshot. Product X cannot mutate
Product Y by changing its own membership or baseline.

Project-local STM and capability records may be reused by both Products only
when their exact qualified identity, accepted revision, baseline binding,
freshness, and scope are suitable for each consumer. Reuse is a dependency
reference, not transfer of ownership. A Product-scoped finding or relation is
never reused as another Product's semantic fact merely because it references
the same Project.

Product does not contain Product. No Product-to-Product nesting or membership
cycle rule is introduced. A graph cycle among technical Projects is a factual
or dependency question handled by STM/dependency contracts, not a Product
membership rule.

## 11. Product baseline vector

### Decision

Use an immutable `Product Baseline` record scoped to a Product revision and
review session. It has a stable local baseline key under the Product namespace;
no additional global identifier family is required.

```text
product_baseline:
  product_id: PROD-*
  product_revision: PROD-*@revN
  baseline_key: <opaque Product-scoped key>
  members:
    - project_key
      binding_set:
        - repository_identity
          selected_scope
          exact_revision_or_content_binding
          branch/ref metadata
          baseline_type
          dirty_state
          source_availability
      project_profile_ref
      evidence_refs
  shared_external_sources:
    - source identity
      exact contract/source revision or content binding
      availability
      provenance
  accepted_at / accepted_by
  coherency
  limitations
  supersedes / superseded_by
```

Every contributing source has an exact revision or exact content binding. A
single Git SHA is never used as the Product baseline identity. Project-local
and external contract revisions are retained alongside the Product baseline;
cross-project claims reference the complete contributing vector, not only the
repository where the claim was written.

Baseline acceptance is a human-controlled Product Baseline Acceptance Gate.
It verifies membership revision, source bindings, availability disclosure,
evidence addressability, the coherency predicate below, and the Product
revision's `coherency_policy`. Acceptance does not imply every member has been
reviewed or every projection is current. The gate may accept a baseline only
for an `ACCEPTED` Product revision and is the authority for the baseline's
classification, not for technical conclusions.

## 12. Baseline coherency

Use one explicit classification dimension, `coherency`, with these values:

| Value | Meaning |
|---|---|
| `COHERENT` | Every required binding is exact and available, and the baseline includes a declared coordination marker or bounded capture protocol plus evidence tying the bindings to one logical review event. No required source advanced between capture and acceptance. This is not atomic Git state. |
| `MIXED_EXPLICIT` | Every required binding is exact and provenance-complete, but capture times/branches/source states differ or no shared coordination marker exists. It is admissible only when the pinned Product revision has `ALLOW_MIXED_EXPLICIT` policy and the temporal mixture and limitations are recorded. |
| `UNKNOWN` | A required binding is not exact/provenance-complete, required availability or coordination evidence is unresolved, or a conflict prevents classification as either of the other values. |

`COHERENT` is an evidence-backed claim about the selected review context, not
a claim that multiple repositories share a transaction. Under `COHERENT`,
cross-project facts, relations, and capability conclusions may proceed when
their own evidence and owner gates pass. Under `MIXED_EXPLICIT`, only claims
whose semantics tolerate temporal mixture may proceed; each must retain the
full vector and limitations, and no claim requiring a simultaneous state or
change ordering may be accepted without additional evidence. Product RF,
CQ, or TE adjudication may proceed only when its owning gate explicitly
accepts the mixed scope. Under `UNKNOWN`, Product cross-project facts,
relations, and interpretations requiring the unresolved binding are blocked
or insufficient; bounded Project-local work and explicitly limited
projections may continue under their own contracts.

The Product Baseline Acceptance Gate records the evidence and rationale for
the selected value. `REQUIRE_COHERENT` rejects `MIXED_EXPLICIT`; it never
converts it to `UNKNOWN`. `ALLOW_MIXED_EXPLICIT` permits only
`MIXED_EXPLICIT` subject to the limitations above. No policy permits unknown
bindings for claims that require them. Source advancement, changed
coordination evidence, or a changed policy creates a new baseline candidate;
the accepted historical baseline and its classification remain immutable.
Impact analysis then determines targeted Product revalidation. A new baseline
may supersede the old one without rewriting accepted evidence or Product
findings.

Baseline supersession creates a new immutable baseline record. It never rewrites
the prior vector or changes the historical meaning of accepted evidence.

## 13. Dirty and noncanonical states

Product baselines may include dirty or noncanonical Project bindings when the
selected Product policy permits them. They are never automatically invalid or
automatically accepted.

| Source state | Required binding | Design consequence |
|---|---|---|
| Clean committed revision | Commit SHA, repository identity, selected scope, ref metadata | Normal revision-bound evidence. |
| Dirty tracked state | Base commit plus changed-path/content fingerprints and selected scope | Dirty limitation is visible; acceptance is explicit. |
| Selected untracked content | Explicit file/content fingerprints and inclusion decision | Untracked content is excluded unless explicitly selected. |
| Detached HEAD | Exact commit plus absence of branch identity | No inferred branch provenance. |
| Local-only commit | Exact commit/ref plus local-only marker | Cannot be represented as remote canonical. |
| Missing remote | Local/source locator and unavailable remote state | No guessed publication or canonicality. |
| Diverged branches/worktrees | Exact binding per source/worktree and scope | Bindings remain separate; no implicit merge. |

If a dirty or noncanonical source is not admitted, the Product workflow may
still proceed with available members and bounded Project-local conclusions, but
claims requiring that source are unavailable and corresponding package members
cannot be accepted as current. No cleanup, branch switch, clone, checkout, or
worktree removal is an implicit recovery action.

## 14. Availability dimensions

Product state uses independent dimensions rather than a universal Product
`PARTIAL` or `BLOCKED` status:

1. **Source Availability** — whether the declared source/binding can be read
   and exact provenance established.
2. **Review Coverage** — which selected scope was actually investigated.
3. **Semantic Availability** — whether the required STM/capability conclusion
   is accepted, insufficiently evidenced, disputed, or absent.
4. **Projection Availability/Freshness** — whether a selected `PRJ-*` exists,
   is verified, `CURRENT`, `STALE`, or `BLOCKED`.
5. **Package Gate Result** — whether the named package policy permits the
   consuming gate.

These dimensions can legitimately disagree. For example, a Project source may
be unavailable while Project A/B semantics remain accepted, one Product
projection is blocked, another remains current, and an independent Project
package closes under its own policy. `PARTIAL` and `BLOCKED` may describe a
bounded scope or gate result, but neither is a new universal Product status.

Missing source is never a negative finding. Each unavailable binding retains
the attempted access, expected baseline, limitation, and minimum action needed
to expand context.

## 15. Cross-project evidence

### Decision

Reuse `WS-*`/`EV-*` through a Product-scoped evidence context. No new evidence
family or alternate evidence authority is introduced.

A Product workset remains a shared evidence record owned by the Shared
Evidence Model. It may contain multiple qualified source bindings:

```text
product_workset:
  id: WS-*
  scope: PRODUCT
  product_revision: PROD-*@revN
  baseline_ref: <Product baseline>
  source_bindings:
    - project_key / repository_binding / source revision
    - project_key / repository_binding / source revision
    - external contract/source binding
  EV records: EV-* observations with qualified source references
  limitations / conflicts
```

The `WS-*`/`EV-*` owner writes observations, not findings or accepted STM
meaning. A cross-project observation must preserve every contributing Project,
repository/scope, exact revision/content binding, external source, and observed
view (`DECLARED`, `IMPLEMENTED`, `CONSUMED`, `TESTED`) where applicable.

Cross-project evidence can be accepted only to the same extent as current
shared evidence: the observation is baseline-bound and addressable. Its use in
an STM fact or capability conclusion still passes through the owning acceptance
gate. Reports, summaries, Product indexes, and package documents cannot be
used as evidence authority.

Conflicting observations remain independently preserved and are marked as a
conflict or limitation. No source precedence is invented here.

## 16. Cross-project STM strategy

### Decision: hybrid STM extension

Project-local STM facts remain authoritative for their qualified Project scope.
Cross-project factual relationships are represented as accepted STM relations
or existing STM fact records with:

- qualified endpoints identifying each Project and local STM identity;
- exact source and Product baseline bindings;
- `WS-*`/`EV-*` provenance for every contributing observation;
- the existing STM lifecycle, freshness, authority, and revision axes;
- direct dependency metadata only where a semantic prerequisite actually
  exists.

The Technical Model Gate remains the only writer of accepted cross-project STM
meaning. Capabilities may emit `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT`, or
`TECH_FACT_REVALIDATION_REQUEST`; they do not write accepted STM facts.

No generic Product fact authority is introduced. A Product identity supplies
scope/context only. A relation/index layer may be used as a derived navigation
or candidate-edge record when existing STM identity cannot express a qualified
relationship, but it cannot accept facts, override STM, or become a second
semantic model.

Shared components are represented by existing STM component/resource families
with qualified ownership and provenance. Product membership may catalogue a
shared resource, but cataloguing does not make the Product the technical owner.

## 17. Qualified addressing

Every cross-project reference uses a qualified address with these semantic
parts:

```text
coordinator/project namespace
  + stable project_key
  + artifact family
  + local artifact identity
  + accepted artifact revision
  + Product baseline binding when the conclusion is Product-scoped
```

The textual form is implementation-defined; `PROJECT-A::IF-001@rev3` is only
illustrative. Qualification must be unambiguous even when two Projects use the
same local family/id. A bare `IF-001`, `RF-001`, or `CQ-001` is insufficient in
cross-project Product authority.

A qualified reference identifies an existing owner; it does not relocate the
artifact. Product-scoped records retain both the qualified input references and
their own owning-family identity.

## 18. Relation versus dependency representation

The existing distinction is preserved:

```text
STM factual relation
  != direct semantic dependency
  != generated reverse index
  != impact traversal result
```

Direct dependencies remain outbound metadata on the dependent artifact, using
`EVIDENCED_BY`, `DERIVED_FROM`, `DEPENDS_ON`, `REFERENCES`, `SUPERSEDES`, and
`PROJECTS_FROM` as applicable. A cross-project dependent record stores a
qualified prerequisite reference and the existing impact strength:

```text
dependency:
  type: DEPENDS_ON
  artifact: <qualified Project/STM/capability/projection reference>
  impact: HARD | CONDITIONAL | INFORMATIONAL
```

The dependent artifact owns the edge. Generated reverse indexes locate
candidates but cannot create, modify, or adjudicate direct edges. Traversal
starts from changed source/baseline bindings, resolves direct metadata, follows
qualified `HARD` and unresolved `CONDITIONAL` edges, and records the bounded
impact result. A factual `CALLS`, `CONSUMES`, `PROVIDES`, or similar STM
relation does not automatically become a dependency.

## 19. Shared resources

A shared resource is catalogued in Product context only when its relationship
to the Product is explicit. The resource's technical facts remain in STM and
its interpretation remains with the appropriate capability.

| Resource context | Meaning | Technical owner |
|---|---|---|
| `PROJECT_OWNED` | One Project owns the technical resource and other Projects consume/use it. | Owning Project's STM/capability owner |
| `EXTERNAL` | The source and change authority are outside the Product. | External authority; Product records provenance and limitations |
| `PRODUCT_CONTEXT_MANAGED` | Product coordinates membership, version/reference, and review context without becoming generic technical owner. | Explicit existing STM or capability owner per fact/conclusion |

`PRODUCT_CONTEXT_MANAGED` is not a fourth factual authority. If a technical
resource genuinely has no existing owner, the implementation plan must route an
explicit ownership adjudication to STM or the relevant capability before any
Product conclusion consumes it. A Product catalogue cannot resolve ownership
by convenience.

## 20. Product Architecture Review

`RF-*` remains the Architecture Review finding family. A Product-level finding
is an independently adjudicated Architecture Review interpretation, not an
aggregation of Project findings.

A Product-scoped `RF-*` must record:

- `scope: PRODUCT` and the `PROD-*` identity/revision;
- immutable Product baseline reference;
- affected Project identities and qualified relevant records;
- accepted STM facts/relations and all contributing `WS-*`/`EV-*` evidence;
- consequence that exists at Product scope, not merely repeated local text;
- Architecture Review owner, lifecycle, severity, dependencies, and
  projection behavior.

Project-local `RF-*` remains local. It is not promoted automatically because
another Project has a similar finding. Correlation and summarization are
projection/navigation. Product Architecture Review may produce Product
findings only after the Architecture Review gate independently adjudicates the
cross-project consequence.

## 21. Product Code Quality

`CQ-*` and `CQRA-*` remain owned by Code Quality Review. A Product-scoped
`CQ-*` is allowed when the concern itself spans Projects and has material
cross-project evidence, Product baseline bindings, affected Projects, and
Code Quality adjudication. Its stable allocation is in a disjoint Product
namespace keyed by `PROD-*` while retaining the `CQ-*` family; local
repository-scoped allocations remain unchanged and cannot collide with the
Product allocation. The same rule applies to Product-scoped `CQRA-*`. Product
scope, Product revision, baseline, affected Projects, evidence, material
consequence, and lifecycle are explicit fields; Product identity is not part
of the finding's mutable revision identity.

Project-local `CQ-*` records remain unchanged. A Product Code Quality Summary
that merely groups local findings is a projection and does not create a Product
finding. `CQRA-*` remains Project-local when remediation is local. A
Product-scoped `CQRA-*` is allowed only when one coordinated remediation action
truly spans multiple Projects; it must name affected Projects, owner, action
scope, dependencies, and evidence. It never closes or supersedes local
remediation actions automatically.

Product Code Quality interpretation is never moved to Architecture Review just
because its evidence crosses a Project boundary. A Product CQ remains stale or
blocked when its Product baseline or required evidence changes. A Product
CQRA has a Code Quality owner and coordinated action scope; completion remains
independent of CQ resolution and does not close local CQRA actions.

## 22. Product Test Engineering

Existing Test Engineering families remain valid at qualified multi-Project
scope:

- `BC-*` describes a behavior contract whose provider/consumer and exact
  revisions may belong to different Projects.
- `CC-*` compares declared, implemented, consumed, or tested contract views
  with qualified source bindings.
- `MAT-*` records assurance mapping and retains the relevant Product and
  Project scope.
- `TM-*` records test-model material with qualified behavior/source context.
- `GAP-*` identifies missing assurance evidence, not merely an unavailable
  repository; the missing scope and required evidence are explicit.
- `TASK-*` records work for one or more Projects with an explicit owner and
  dependency set.

Product Test Engineering uses the existing `TRS-*` Test Review Scope family,
with `scope_kind: PRODUCT`, stable Product scope allocation, `product_id`,
selected accepted Product revision, and immutable Product baseline binding.
Product TE records carry that Product `test_review_scope_id`; Project-local
records continue to carry their existing Project/session scope IDs. Product
selectors match the Product scope ID exactly and may include only qualified
local or cross-project records explicitly admitted to that scope. This keeps
local and Product selector membership disjoint while allowing a Product scope
to reference local records through qualified dependencies.

The Product Test Assurance package consumes accepted records resolved through
the Product `TRS-*` scope, including exact Project provenance, Product
revision/baseline bindings, lifecycle, freshness, and authority state. It does
not consume every record in member Projects and does not become a Behavior
Model authority. Product `TASK-*` records retain Test Engineering ownership;
completion of a task does not resolve a `GAP-*` or alter its evidence state.

A Product-level `BC-*` is created only when the behavior contract itself spans
Projects. If the behavior remains local and only has a cross-project relation,
retain local `BC-*` records and a qualified relation. Product Test Assurance is
a projection/package of accepted Test Engineering authority, not a new
Behavior Model authority. Cross-project E2E, simulator, environment, and test
execution remain separately selected and explicitly authorized.

## 23. Compatibility semantics

Compatibility has no single global owner or automatic engine. The semantic
pipeline is:

```text
STM facts:
  exact versions, interfaces, declared/implemented/consumed representations
        ↓
Test Engineering:
  contract comparison and tested evidence → CC-* / related TE records
        ↓
Architecture Review:
  material architectural consequence → RF-* when independently present
```

The existing observed views `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED`
remain observations, not precedence rules. A declared supported range does not
prove implemented compatibility; a compatible version number does not prove
runtime behavior. Conflicting views remain explicit until the relevant owner
adjudicates them.

A compatibility matrix is either an explicitly selected controlled input with
its own provenance or a `PRJ-*` projection. It is never authority solely because
it is tabular. No automatic version resolver or compatibility engine is part of
Stage E.

## 24. Product `REVALIDATE`

Product `REVALIDATE` is an impact-driven overlay against an accepted Product
revision and Product baseline. It does not rerun a full Product review by
default.

```text
changed source binding(s)
  → changed Project-local evidence/STM roots
  → direct dependency metadata and qualified cross-project edges
  → affected Project capability records
  → affected Product relations and Product-scoped findings
  → affected Product projections/packages
  → minimum fresh evidence and adjudication slice
```

The semantic algorithm is:

1. Bind previous accepted Product revision/baseline and current source state.
2. Record changed source bindings, including availability and dirty changes.
3. Identify direct Project-local evidence/STM roots.
4. Read dependent artifacts' direct dependency metadata; use reverse indexes
   only to locate candidates.
5. Traverse qualified `HARD` dependencies and unresolved `CONDITIONAL`
   dependencies; inspect `INFORMATIONAL` edges without default invalidation.
6. Identify affected cross-project STM relations, capability records, Product
   findings, and selected projections/packages.
7. Preserve accepted records only when dependency/evidence mapping demonstrates
   that fresh verification is unnecessary. Unknown linkage requires targeted
   investigation, not preservation by assumption.
8. Load the minimum affected evidence/STM/capability slice and adjudicate it.
9. Run Product Projection Impact Analysis once after semantic stabilization.
10. Record `LOCAL`, `BOUNDARY`, or `SYSTEMIC`, limitations, and any
    `CONTEXT_EXPANSION_REQUIRED` result.

Project-only revalidation is sufficient when the changed bindings have no
demonstrated material Product dependency after direct metadata and bounded
investigation are checked. Product scope is required for changed Product
membership, Product baseline context, accepted cross-project facts/relations,
Product-scoped findings, or affected cross-project dependencies. `SYSTEMIC`
may emit `FULL_REAUDIT_RECOMMENDED` with an explicit user decision; it never
automatically expands to a full Product audit.

## 25. Membership changes

Membership change creates a new immutable Product revision. The previous
revision and its baselines remain historical and addressable.

| Change | Operation | Required semantic handling |
|---|---|---|
| Add Project | `EXTEND` entry point | Create Product revision; bind the new member; adjudicate only newly affected Product edges/meaning; preserve unrelated accepted state. |
| Remove Project | Product semantic change | Create Product revision; identify removed dependencies/claims; run targeted Product impact/revalidation before accepting affected interpretations. |
| Replace Project | Product semantic change | Create Product revision; treat old removal and new addition as one change set; revalidate affected boundaries and baseline. |
| Change Project role/requiredness | Product semantic change | Create Product revision; re-evaluate Product claims and package conditions that depend on the role. |
| Change shared-resource declaration | Product semantic change | Create Product revision; revalidate ownership/context, affected relations, and package membership. |

Adding a Product projection or capability without changing member meaning is an
ordinary additive `EXTEND`. A membership change cannot be hidden as a
projection extension. Product baseline creation after the revision is a
separate review snapshot and does not rewrite earlier baseline vectors.

## 26. Product `EXTEND`

Allowed additive operations are:

- add a Project member;
- add a capability/output selected for Product scope;
- add a bounded cross-project relationship investigation;
- add a Product projection/output;
- add a shared-resource reference.

The coordinator preserves accepted unaffected Project and Product state. It
adds only the minimum dependency/evidence slice required for the requested
addition. Adding a Project enters the membership-revision route above; it does
not reopen unrelated Project findings. If the addition changes requiredness,
role, shared-resource meaning, or another Product interpretation, the operation
creates a Product revision and enters targeted impact/revalidation.

`EXTEND` never silently deselects or reconfigures previously accepted
capabilities, outputs, Architecture depth, or endpoint. Product projection
freshness is accounted for separately; regeneration remains explicit.

## 27. Partial and unavailable behavior

| Layer | Unavailable Project/source behavior |
|---|---|
| Evidence | Preserve local observations and limitations; do not accept an observation whose required source binding is absent; no report substitution. |
| STM | Existing accepted facts remain valid at their own exact bindings; cross-project facts requiring the missing binding become insufficient, disputed, or revalidation-required under STM lifecycle. |
| Architecture Review | Evaluate claims whose evidence and dependencies are sufficient; Product claims requiring the missing member cannot be accepted; absence is not a finding. |
| Test Engineering | Local contracts may remain valid; provider/consumer or end-to-end contracts become insufficient when the missing side is required, producing bounded coverage/gap semantics only through Test Engineering authority. |
| Code Quality | Project-local conclusions remain local and can remain usable; a Product CQ interpretation is blocked/insufficient when required cross-project evidence is absent. |
| Projections | A Product projection may remain current only when its exact accepted inputs and contract permit that bounded scope; otherwise it becomes `STALE` or `BLOCKED` through impact accounting. No automatic regeneration. |
| Packages | The named package resolves finite required/optional/conditional membership. Only a missing required member blocks that package gate under its policy; unrelated Project gates/packages are unaffected. |

Unavailable is not failed, verified, complete, or negative. Each layer records
its own availability/coverage/freshness outcome and limitation. The Product
summary may present the dimensions together, but it cannot collapse them into a
universal status.

## 28. Product outputs

Product semantic substrate (Product identity, revision, membership, baseline,
and accepted Product-scoped records where selected) is required whenever
Product mode is explicitly selected. No candidate projection is universally
required for every Stage E invocation.

| Candidate output | Classification | Owner and reason |
|---|---|---|
| Product Architecture Review | `CONDITIONAL_OUTPUT` | Architecture Review, only when Architecture and Product scope are selected; Product RF/projections require accepted inputs and independent review. |
| Cross-Project Dependency View | `OPTIONAL_STAGE_E_OUTPUT` | Derived index/projection for navigation; direct dependency metadata remains authority. |
| Product Target Architecture | `CONDITIONAL_OUTPUT` | Architecture target endpoint only; requires accepted Product Architecture authority and target review. |
| Product Remediation Roadmap | `CONDITIONAL_OUTPUT` | Roadmap endpoint only; consumes accepted findings/target/dependency decisions and follows roadmap review. |
| Product Test Assurance | `CONDITIONAL_OUTPUT` | Test Engineering selected; projection/package of accepted records selected by the Product `TRS-*` scope and exact Product revision/baseline, not a second authority. |
| Product Code Quality Summary | `CONDITIONAL_OUTPUT` | Code Quality selected; aggregation is projection over declared local/Product CQ dependencies, while Product CQ/CQRA findings use disjoint Product allocation and Code Quality adjudication. |
| Product Technical Documentation | `OPTIONAL_STAGE_E_OUTPUT` | Technical Documentation owns the output contract; it consumes selected Product-scoped STM selectors, qualified WS/EV references, and explicit availability/limitation dimensions. It reuses `PRJ-TECH-DOC-*`, `TECH-DOC-SCOPE-*`, and `PKG-TECHNICAL-DOCUMENTATION` with Product-qualified exact/selector dependencies and finite package membership. |

Output selection is explicit and independent. Dependencies, selectors, package
membership, freshness, and owner/writer must be declared before a projection is
consumed. No output is auto-created merely because Product exists.

## 29. Product package

Product packages reuse the Stage B package contract. A Product package is a
named non-authoritative delivery scope, represented by an existing package
declaration shape and a resolved membership snapshot. A Product package may be
identified by an existing `PKG-*` namespace with a Product-scoped declaration;
no second package authority is introduced.

Project subpackages are references to exact Project package/projection revisions,
not embedded copies. The Product package records:

- Product package declaration and revision;
- selected Product `PRJ-*` members;
- required, optional, and controlled conditional members;
- exact referenced Project package/projection revisions;
- mandatory dependency closure;
- Product baseline and semantic authority dependencies;
- freshness policy and resolved membership snapshot;
- blocked/unavailable member and gate result.

The package owner is the selected capability or endpoint, not the generic
Product aggregate. A changed selection, declaration, or condition requires a
new resolved snapshot; ambiguous membership blocks that package gate.

## 30. `ALL_SCOPED_CURRENT` at Product scope

`ALL_SCOPED_CURRENT` retains its Stage B meaning. For one named Product package
instance, it requires every member resolved as required by that package's
finite declaration, including mandatory upstream projection prerequisites. It
does not mean every artifact, document, Project package, or projection in every
Product member Project.

Optional members remain optional. Conditional members become required only when
their controlled condition resolves true. An independent Project package that
is not in the Product package's resolved required closure cannot block the
Product gate. Conversely, a required Product reference to an exact Project
package revision blocks the Product gate when that reference is stale or
blocked. `PERMISSIVE` and `REQUIRED_SCOPE_CURRENT` retain their existing
scopes. Impact accounting precedes membership resolution and gate evaluation;
regeneration is never automatic.

## 31. Freshness and regeneration

Product projections use ordinary `PRJ-*` identity, verified revisions,
dependency snapshots, fingerprints, and `CURRENT`/`STALE`/`BLOCKED` freshness.
They do not receive a new Product projection family. Product regeneration uses
ordinary `RG-*` sessions and does not change Product semantic authority.

Example propagation:

```text
Project B IF-* revision changes
  → qualified STM relation/direct dependency is impacted
  → Product-scoped CC/RF/CQ/TE record may be stale or blocked
  → Product Architecture/Assurance/Summary projection is impacted
  → Product package gate evaluates its resolved required closure
```

The coordinator persists direct and propagated impact reasons, preserving the
declared `CONSUMER → PREREQUISITE` dependency direction. A stale Product
projection is not regenerated during semantic revalidation. A separate
targeted or all-stale `RG-*` session resolves exact package/projection scope,
freezes dependencies, verifies outputs, and publishes only a changed verified
projection revision.

## 32. Authorization

Every future Product workflow action is separately human-authorized:

| Action | Authorization boundary |
|---|---|
| Read repository/source | Explicit source access for each binding |
| Select revision/branch/worktree | Explicit baseline selection |
| Admit dirty/untracked content | Explicit baseline acceptance |
| Create Product / change membership | Product context owner and human approval |
| Write Project-local semantic records | Existing Project STM/capability owner |
| Write Product-scoped semantic records | Existing owning capability plus Product scope authorization |
| Generate projections/packages | Selected capability/endpoint and package policy |
| Run tests/simulators/environments | Explicit Test Engineering/environment authorization |
| Modify code/worktree/branch | Explicit implementation authorization outside this Design |
| Commit/PR/push/deploy | Separate human-controlled publication/deployment authorization |

Membership, Product identity, a report, index, package, or cross-project
reference grants none of these permissions. No clone, checkout, cleanup,
worktree creation/removal, code modification, execution, commit, PR, push, or
deployment is hidden in Product support.

## 33. Context and scale

The bounded acquisition strategy is:

```text
Product revision/membership/baseline
  → direct dependency and generated-index lookup
  → minimum Project STM/evidence/capability slices
  → cross-project adjudication for affected edges only
  → targeted raw source reads where authority/evidence is insufficient
  → accepted Product-scoped semantics
  → Product projections/packages
```

Navigation summaries and indexes may locate candidate authorities. They cannot
replace the owning semantic artifact, direct dependency metadata, or
baseline-bound evidence. Raw repositories are not concatenated into one
context. Context budgets are explicit per session: requested Product scope,
required dependency closure, evidence loaded, raw reads, unavailable sources,
and deferred slices are recorded. Unknown linkage triggers targeted context
expansion rather than an unsupported preserved conclusion.

No mandatory database, backend service, graph database, vector/RAG service, or
daemon is required. Generated Product indexes remain reproducible navigation
projections.

## 34. Storage and layout

Choose the existing review workspace with a Product-scoped namespace (option C
from Discovery). Product authority is stored in the coordinator review
workspace, not inside one arbitrary member Project and not in a new external
service.

Conceptual layout:

```text
working/
├── INDEX.md                         # coordinator workflow authority
├── projects/<project-key>/
│   ├── descriptor.md                # stable identity/source-context descriptor
│   └── bindings/<revision>.md       # repository/source bindings
├── products/<PROD-key>/
│   ├── identity.md                  # Product identity and lifecycle
│   ├── revisions/<rev>.md            # immutable membership/context revisions
│   ├── baselines/<baseline-key>.md   # immutable Product baseline vectors
│   ├── evidence/WS-*.md              # Product-scoped shared evidence
│   ├── relations/                    # STM/dependency references only if owned there
│   └── projections/                  # non-authoritative operational views
└── projections/                      # existing Stage B operational records
```

The exact paths are implementation detail; ownership, stable identity,
revision, provenance, and authority boundaries are normative. `working/INDEX.md`
remains coordinator authority and never becomes a Product semantic artifact or
`PRJ-*` projection. Product-scoped semantic records may be stored under the
Product namespace for navigation, but their owning capability/STM gate remains
authoritative.

## 35. Identity and identifier strategy

| Concept | Strategy | Reason and boundary |
|---|---|---|
| Product identity | New `PROD-*` family | Existing families do not represent durable Product scope. It identifies context only, never facts/findings. |
| Product revision | `PROD-*@revN` | Reuses existing revision semantics; no new revision family. |
| Project identity | Stable opaque `project_key` in coordinator descriptor | A Project is not a projection or STM fact; a new global semantic family is unnecessary. |
| Product membership | Embedded `membership_key` in immutable Product revision | Membership has no independent authority outside Product context. |
| Product baseline | Product-scoped `baseline_key` in immutable baseline record | Baseline is a snapshot binding, not a new semantic fact family. |
| Cross-project evidence | Existing `WS-*`/`EV-*` with Product scope and qualified bindings | Reuses shared evidence lifecycle and preserves source authority. |
| Cross-project factual relation | Existing STM family/relation vocabulary | STM Technical Model Gate already owns accepted factual relations. |
| Product Architecture finding | Existing `RF-*` with Product scope | Architecture Review already owns architectural interpretation. |
| Product Code Quality | Existing `CQ-*`/`CQRA-*` with disjoint Product namespace allocation | Code Quality Review retains ownership; the stable allocation is keyed by Product identity and cannot collide with repository-local allocation. Product revision/baseline are scope and provenance, not identity. |
| Product Test Review scope | Reuse existing `TRS-*` with `scope_kind: PRODUCT` | The existing persisted `test_review_scope_id` selector model is sufficient when extended with Product identity/revision and exact baseline binding; no second TE scope family is needed. |
| Product Test Engineering | Existing `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` | Test Engineering contracts retain semantic ownership; Product records use the Product `TRS-*` scope and qualified Project provenance. |
| Product projection | Existing `PRJ-*` | Product scope is a contract/dependency attribute, not a new projection family. |
| Regeneration session | Existing `RG-*` | Execution identity remains separate from projection and semantic identity. |
| Product package | Existing named package mechanics and `PKG-*` declarations | No second package authority. |

Textual qualified-address syntax is implementation-defined, but the semantic
parts are mandatory: stable Project identity, family, local identity, accepted
revision, and Product baseline when Product-scoped.

## 36. Lifecycle and ownership matrix

| Object | Identity owner | Writer | Revision owner | Lifecycle/freshness owner | Provenance | Consumers |
|---|---|---|---|---|---|---|
| Product identity | Product context coordinator | Explicit Product context workflow | Product context coordinator | Product context coordinator; freshness is context validity | Creation authorization and Product history | Product sessions, membership, baselines |
| Product revision | Product context coordinator | Membership/context adjudication | Product context coordinator | Product context workflow | Prior revision, explicit membership sources | Baseline and Product semantic workflows |
| Product membership entry | Product context coordinator | Product Context Workflow only | Product revision owner | Product context lifecycle | Authorized membership request and referenced Project descriptor | Product revision, baseline resolution, package selectors |
| Project descriptor | Coordinator identity registry | Project identity workflow | Project identity workflow | Coordinator routing state | Explicit identity/source declaration | Products, bindings, review sessions |
| Repository/source binding | Baseline/evidence workflow | Authorized review session | Baseline/evidence workflow | Evidence/baseline workflow | Repository/ref/content and access result | WS/EV, STM, capabilities |
| Product baseline | Baseline acceptance workflow | Authorized Product review session | Baseline owner | Baseline acceptance plus revalidation | Member bindings, Profiles, WS/EV, external sources | STM/capabilities/projections |
| Product WS/EV evidence | Shared Evidence Model | Evidence workset writer | Evidence workset owner | Evidence/freshness workflow | Raw repository/external source bindings | STM and capability gates |
| Cross-project STM relation/fact | Technical Model Gate | Technical Model Gate only | Technical Model Gate | STM lifecycle/freshness | Qualified WS/EV and exact baseline | Architecture/Test/CQ as applicable |
| Product `RF-*` | Architecture Review | Architecture Review | Architecture Review | Architecture Review authority plus semantic freshness | Accepted STM, WS/EV, Product baseline | Product Architecture projections/roadmap |
| Product `CQ-*` | Code Quality Review | Code Quality Review | Code Quality Review | Code Quality lifecycle/freshness | WS/EV/STM and Product baseline | CQ projections/package |
| Product `CQRA-*` | Code Quality Review | Code Quality Review | Code Quality Review | Action lifecycle and linked finding revalidation | Finding/evidence/dependencies | Project/Product remediation projections |
| Product TE scope (`TRS-*`) | Test Engineering scope workflow | Authorized Test Engineering scope workflow | Test Engineering scope owner | Test scope lifecycle/freshness | Product revision, baseline, qualified Project bindings | TE selectors, records, Product Assurance package |
| Product TE records | Test Engineering | Test Engineering gates | Test Engineering | Test lifecycle/freshness | WS/EV/STM and contract views | Test projections/package |
| Product projection | Owning capability/endpoint | Projection generator | Projection lifecycle | Projection lifecycle/impact owner | Declared semantic/projection dependencies | Named package/gate/user |
| Product package | Consuming capability/endpoint | Package coordinator | Package declaration owner | Package gate owner | Resolved membership and projection revisions | Closeout/publication gate |

No row makes Product identity the owner of another row's technical meaning.
Freshness of semantic artifacts and freshness of projections remain separate.

## 37. Contract impact matrix

The following are future implementation impacts only. No normative contract is
modified by this Design.

| Contract | Impact | Required future extension |
|---|---|---|
| `SKILL.md` | `EXTEND` | Document opt-in Product scope and preserve single-project routing/invariants. |
| Session orchestration | `EXTEND` | Route Product identity/revision selection, membership authorization, Product baseline acceptance, and multi-source availability without changing six Session Intents. |
| Review modes/orchestration | `EXTEND` | Persist Product-scoped coordinator references and capability configuration while keeping `INDEX.md` outside semantic/projection authority. |
| Shared evidence | `EXTEND` | Allow Product worksets and multiple qualified source bindings while preserving WS/EV observation ownership and historical binding. |
| Shared Technical Model | `EXTEND` | Allow qualified cross-project STM context/relations and Product baseline references without creating a second fact authority. |
| Technical model dependencies | `EXTEND` | Permit qualified cross-project endpoints and bounded traversal while preserving direct metadata, edge vocabulary, and impact strengths. |
| Revalidation/freshness | `EXTEND` | Define Product baseline deltas, membership-change roots, multi-project preserved sets, and Product impact classification. |
| Projection lifecycle | `EXTEND` | Bind Product projections to Product semantic/baseline dependencies using existing `PRJ-*` revisions and freshness states. |
| Projection impact | `EXTEND` | Resolve Product baseline/member selectors and propagate impact across qualified Product dependencies. |
| Projection regeneration | `EXTEND` | Resolve Product package scope and exact Project references in frozen `RG-*` plans; no implicit regeneration. |
| Projection packages | `EXTEND` | Define Product package declarations, resolved membership snapshots, exact Project package references, and scoped gate behavior using existing policies. |
| Architecture Review contracts | `EXTEND` | Permit Product-scoped `RF-*` with independent consequence, qualified evidence, Product baseline, and owner/lifecycle rules. |
| Test Engineering contracts | `EXTEND` | Permit qualified multi-Project BC/CC/MAT/TM/GAP/TASK and Product Assurance projection membership. |
| Code Quality contracts | `EXTEND` | Define the disjoint Product namespace allocation for `CQ-*`/`CQRA-*`, Product scope and baseline fields, qualified evidence/affected Projects, lifecycle/freshness, and coordinated-action semantics without weakening local repository scope. |
| Technical Documentation contract (`references/technical-documentation.md`) | `EXTEND` | Define Product-qualified STM selector inputs, `TECH-DOC-SCOPE-*` section selection, availability/limitation rendering, `PRJ-TECH-DOC-*` dependencies, and `PKG-TECHNICAL-DOCUMENTATION` membership/freshness for finite Product scope. |
| Projection Dependencies contract (`references/projection-dependencies.md`) | `EXTEND` | Define collision-safe Product-qualified `SEMANTIC_EXACT` and `SEMANTIC_SELECTOR` bindings, Product baseline/member resolution snapshots, and selector dimensions without changing dependency ownership. |
| Projection Verification contract (`references/projection-verification.md`) | `NO_CHANGE` | Existing V1–V4 verification rules apply to Product `PRJ-*` outputs; Product-specific semantic prerequisites are expressed as dependencies and selectors, not a second verification model. |
| Technical Model Coverage contract (`references/technical-model-coverage.md`) | `EXTEND` | Bind Product documentation and Product capability selectors to explicit accepted STM coverage and availability dimensions without converting coverage into authority. |
| New Product contract reference | `NEW_REFERENCE_REQUIRED` | Add one focused authoritative reference for Product identity, membership, baseline, and cross-project routing; it must not duplicate existing ownership contracts. |

No contract requires a database or service. Any implementation extension must
pass the owning contract's independent review and preserve existing single-
project behavior.

## 38. Backward compatibility

An existing single-project invocation remains semantically equivalent when
Product mode is not explicitly selected. It does not require Product identity,
Project registry, Product baseline, Product membership, cross-project evidence,
or Product package.

Existing `WS-*`, `EV-*`, STM, Architecture Review, Test Engineering, Code
Quality, `PRJ-*`, `RG-*`, and package identities remain valid under their
current scopes. Existing Project Profile and review session state is not
migrated merely to continue single-project operation. Product fields are
absent or `NONE` in the single-project route, not synthetic one-member Product
objects. A Product may be selected explicitly later without changing the
identity of pre-existing local artifacts.

Product support must not make an existing package globally depend on Product
state. A Product package is a separate named scope with its own resolved
membership and gate.

## 39. Migration implications

The selected strategy is `ADDITIVE`. No semantic migration of existing
single-project artifacts is required. Existing artifacts remain Project-local
and are referenced by qualified Product records only when a user explicitly
creates Product context and the artifacts' accepted revision/freshness is
suitable.

Historical text, reports, or summaries are not silently promoted into Product
authority. If an implementation needs to import such material, it must pass
through the existing evidence/STM/capability acceptance gates and retain its
historical limitations. No automatic migration, bulk rewrite, or identity
renumbering is part of Stage E.

## 40. Design-level pressure scenarios

The following scenarios are semantic design tests, not implementation tests.
Each identifies input, expected behavior, forbidden behavior, affected
authority, and Product/package outcome.

| # | Input state | Expected semantic behavior | Forbidden behavior | Affected authority | Outcome |
|---:|---|---|---|---|---|
| 1 | Single-project review with no Product selection | Run existing local flow unchanged. | Create implicit Product or require Product baseline. | Existing local owners | Local package proceeds under existing policy. |
| 2 | Three clean Projects with exact vector bindings and a shared capture record | Accept an immutable baseline as `COHERENT` only when the Product Baseline Acceptance Gate verifies the coordination marker/protocol and capture-to-acceptance predicate; otherwise classify it `MIXED_EXPLICIT` or `UNKNOWN`. | Collapse vector into one SHA or call exactness alone atomic. | Product baseline, STM/evidence | Claims proceed only under the classification's permitted conclusion rules. |
| 3 | Required member Project source unavailable | Preserve limitation; evaluate independent/local slices; block only claims/package members requiring it. | Treat unavailable as verified, failed, or universal Product `PARTIAL`. | Evidence, STM, capability gate | Dimension-specific blocked/insufficient result. |
| 4 | Member repository has dirty tracked changes | Admit only with explicit content binding and policy; retain dirty limitation. | Auto-reject or silently accept dirty state; clean worktree. | Baseline/evidence | Local or bounded Product work may proceed; dependent claims disclose limitation. |
| 5 | Project B advances after accepted Product baseline, or coordination evidence changes | Keep the accepted baseline immutable; create a candidate replacement, classify it through the acceptance predicate, and run targeted impact/revalidation. | Rewrite old baseline, retarget a pinned session, or claim simultaneous state. | Baseline, Product context, dependencies, revalidation | Historical classification is preserved; only affected Product claims/projections/packages become stale or blocked. |
| 6 | Provider/consumer API compatibility break under a Product `TRS-*` scope | Preserve views/evidence; CC/TE adjudicates the qualified Product contract; RF only for architectural consequence. | Resolve from version number, report precedence, or an unqualified local selector. | STM, Test Engineering, Architecture Review | Affected Product TE/CQ/RF records and projections are changed only through their owners and exact scope/baseline dependencies. |
| 7 | Shared component used by two Projects | Record usage and owner separately; classify project-owned/external/context-managed. | Make Product aggregate technical owner automatically. | STM/shared-resource context | Product relation/projection reflects owner and consumers. |
| 8 | True Product finding supported by two Projects | Create independently adjudicated Product-scoped `RF-*` with full provenance, accepted Product baseline, and Product Architecture scope; use a Product `TRS-*` or Code Quality scope only for their own capability records. | Sum local findings into Product finding or allow a Product report to adjudicate it. | Architecture Review, Test Engineering, Code Quality | Product RF and only its declared dependent projections/packages are impacted. |
| 9 | Local RF resembles another Project's RF | Keep findings local; correlate only as navigation unless new consequence is adjudicated. | Auto-promote or merge identities. | Architecture Review | Local packages remain independent; no Product RF. |
| 10 | `EXTEND` adds Project D | Create Product revision and investigate only affected new edges/meaning. | Reopen unrelated A–C findings or full audit by default. | Product membership/revalidation | Additive scope plus targeted Product impact. |
| 11 | Project B changes with direct dependency only to Project A | Traverse direct qualified edges and revalidate minimum affected slice. | Re-read every Product member. | Dependencies, STM, affected capabilities | Product output stale only where dependent. |
| 12 | Product projection stale while Project semantics are current | Record projection freshness and offer explicit `RG-*` regeneration. | Demote semantic authority or regenerate implicitly. | Projection lifecycle/impact | Semantic gate may proceed if package policy permits. |
| 13 | Older but supported Project version | Compare declared/implemented/consumed/tested views and supported range. | Treat old as incompatible or current solely by age. | STM, Test Engineering | Compatibility conclusion owned by appropriate gate. |
| 14 | Conflicting Project and external evidence in a Product baseline | Preserve all observations; the Baseline Acceptance Gate classifies coherency only from binding/coordination evidence, while STM/TE/CQ/Architecture owners adjudicate technical meaning. | Apply invented source precedence or treat `COHERENT` as evidence precedence. | Evidence, baseline gate, STM, capability owners | Conflicted Product claims remain blocked/insufficient; the immutable baseline records its classification and limitations. |
| 15 | Product package has blocked required member | Resolve finite package snapshot and block that package only under its policy. | Apply global zero-stale rule or block unrelated Project gate. | Package/projection gate | Scoped `BLOCKED`; unrelated packages remain independent. |
| 16 | Same Project used in Product X and Product Y | Keep memberships, revisions, baselines, interpretations, and packages isolated. | Mutate Y from X's membership/baseline. | Product contexts, local reusable authority | Local accepted records may be reused only by exact dependency/freshness proof. |
| 17 | `EXTEND` changes requiredness/meaning of existing member | Create Product revision and targeted membership-semantic revalidation. | Treat as ordinary projection addition. | Product revision, baseline, affected capability records | Affected claims/packages revalidated; unrelated state preserved. |
| 18 | Standalone Project enters or leaves a one-Project Product | Create/use explicit Product context and preserve local Project identity/operation. | Make Product mandatory or impose a cycle rule. | Product membership/revision, local Project | Product-scoped outputs are separate; local gate remains valid. |

## 41. Accepted design decisions

| Topic | Decision class | Accepted decision |
|---|---|---|
| Product identity | `ACCEPTED_DESIGN_DECISION` | Stable immutable `PROD-*` identity, optional, coordinator-owned; Product state is revisioned. |
| Product revision | `ACCEPTED_DESIGN_DECISION` | `PROD-*@revN`; immutable lifecycle `PROPOSED → ACCEPTED → SUPERSEDED` (or `RETIRED`); only the Product Context Acceptance Gate may accept/advance `current_revision`; baselines and sessions bind accepted exact revisions. |
| Project identity | `ACCEPTED_DESIGN_DECISION` | Persistent opaque coordinator descriptor; independent of repositories, targets, sessions, and revisions. |
| Project/repository cardinality | `ACCEPTED_DESIGN_DECISION` | Full 1:1, 1:N, N:1, and N:N support through explicit scoped bindings. |
| Membership | `ACCEPTED_DESIGN_DECISION` | Embedded versioned entries with role, requiredness, status, provenance, and explicit owner/writer. |
| Multi-Product membership | `ACCEPTED_DESIGN_DECISION` | Allowed; Product histories, baselines, interpretations, and packages are isolated. |
| Baseline vector | `ACCEPTED_DESIGN_DECISION` | Immutable Product-scoped vector of exact Project/repository/external bindings. |
| Baseline coherency | `ACCEPTED_DESIGN_DECISION` | Baseline Gate predicate distinguishes `COHERENT` (coordination evidence), `MIXED_EXPLICIT` (exact but temporally mixed and policy-allowed), and `UNKNOWN` (insufficient exactness/evidence); allowed conclusions and limitations are classification-specific. |
| Dirty state | `ACCEPTED_DESIGN_DECISION` | Admit only with explicit content bindings and policy; never auto-invalid or auto-accepted. |
| Availability dimensions | `ACCEPTED_DESIGN_DECISION` | Source, coverage, semantic availability, projection freshness, and package result remain independent. |
| Cross-project evidence | `ACCEPTED_DESIGN_DECISION` | Reuse Product-scoped WS/EV with qualified multi-source bindings; no report authority. |
| Cross-project STM | `ACCEPTED_DESIGN_DECISION` | Hybrid: local facts plus STM-gated qualified cross-project relations; no second fact model. |
| Qualified addressing | `ACCEPTED_DESIGN_DECISION` | Stable Project + family + local identity + revision + Product baseline as needed. |
| Dependency semantics | `ACCEPTED_DESIGN_DECISION` | Existing typed direct dependencies and impact strengths; relations/indexes/results remain distinct. |
| Shared resource ownership | `ACCEPTED_DESIGN_DECISION` | `PROJECT_OWNED`, `EXTERNAL`, or `PRODUCT_CONTEXT_MANAGED`; Product catalogue is not technical ownership. |
| Product RF | `ACCEPTED_DESIGN_DECISION` | Existing `RF-*`, Product scope only after independent Architecture adjudication. |
| Product CQ | `ACCEPTED_DESIGN_DECISION` | Existing `CQ-*`/`CQRA-*` with disjoint Product-keyed allocation; Code Quality ownership, Product scope, baseline, evidence, lifecycle, and CQRA independence retained. |
| Product TE | `ACCEPTED_DESIGN_DECISION` | Existing TE families bound to a Product `TRS-*` scope with exact Product revision/baseline and qualified Project provenance; Product Assurance is projection/package. |
| Compatibility | `ACCEPTED_DESIGN_DECISION` | STM facts, Test Engineering contract conclusions, Architecture consequences by owner. |
| REVALIDATE | `ACCEPTED_DESIGN_DECISION` | Changed bindings → direct impact → minimum affected semantic slice → Product impact; no default full audit. |
| Membership change | `ACCEPTED_DESIGN_DECISION` | New Product revision; add may begin as EXTEND, semantic changes require targeted revalidation. |
| EXTEND | `ACCEPTED_DESIGN_DECISION` | Additive scope and outputs; no unrelated reopening or silent reconfiguration. |
| Partial availability | `ACCEPTED_DESIGN_DECISION` | Layer-specific bounded outcomes; unavailable is not verified, failed, or negative. |
| Projections | `ACCEPTED_DESIGN_DECISION` | Explicit conditional/optional outputs; `PRJ-*` and existing lifecycle contracts. |
| Packages | `ACCEPTED_DESIGN_DECISION` | Stage B named finite package and snapshot model; Project subpackages are exact references. |
| Freshness | `ACCEPTED_DESIGN_DECISION` | Existing semantic/projection freshness and impact accounting; regeneration is explicit `RG-*`. |
| Authorization | `ACCEPTED_DESIGN_DECISION` | Separate human-controlled permission for every read, write, execution, and publication action. |
| Context/scale | `ACCEPTED_DESIGN_DECISION` | Dependency-directed minimum slices, targeted raw reads, explicit bounded context; no repository concatenation. |
| Storage/layout | `ACCEPTED_DESIGN_DECISION` | Coordinator review workspace with Product namespace; no arbitrary member ownership. |
| Identifier strategy | `ACCEPTED_DESIGN_DECISION` | Only `PROD-*` is new; all technical/evidence/capability/projection/package families are reused. |

No foundational semantic decision is left as a question for implementation.
Implementation may choose file names, serialization, indexing algorithms, and
CLI/UI details only within these accepted boundaries.

## 42. Deferred future scope and non-goals

The following are explicitly outside Stage E implementation unless a later
approved design changes scope:

- automatic repository cloning, branch switching, cleanup, or worktree removal;
- multi-repository code modification, automatic remediation, commit, PR, or
  push;
- test execution, simulator implementation/execution, and environment
  provisioning;
- deployment or production configuration changes;
- database/backend service, graph database, vector/RAG infrastructure, or
  daemon;
- Product hierarchy nesting or Product-to-Product membership;
- compatibility engine or automatic version resolver;
- automatic migration or bulk identity rewrite;
- automatic projection regeneration;
- exact UX, CLI, storage serialization, and indexing algorithms;
- new identifier families beyond the explicitly justified `PROD-*` identity.

These are deferred implementation or future-scope concerns, not unresolved
foundational semantics.

## 43. Risks

1. Product context could be accidentally made mandatory by startup or package
   routing; single-project tests must remain a hard compatibility gate.
2. Product-scoped records could become a second factual authority if the
   Technical Model Gate boundary is not enforced.
3. Mixed vectors could be presented as coherent moments unless the coherency
   dimension is carried into every Product conclusion.
4. Qualified references could be dropped during projection, creating identity
   collisions or provenance loss.
5. Product package selectors could widen beyond the resolved finite snapshot
   and block unrelated packages.
6. Revalidation could become a full Product reread or preserve unknown
   dependencies incorrectly.
7. Shared-resource cataloguing could be mistaken for technical ownership.
8. Multi-Product reuse could leak Product-scoped findings or baselines between
   Products.
9. Dirty/noncanonical source states could be hidden by summaries or package
   reports.
10. A Product-level CQ/TE record could bypass its existing capability owner.
11. A new `PROD-*` identity could be overextended into a generic semantic
    object family.

Each risk is addressed by the ownership, qualification, immutable revision,
bounded impact, package, and authorization rules above.

## 44. Implementation-plan entry criteria

Implementation planning may begin only after an independent review accepts this
Design. The plan must establish, before runtime behavior is implemented:

1. the Product contract reference and exact ownership map;
2. serialization schemas for Product identity, revisions, membership entries,
   Project descriptors, source bindings, and baseline vectors;
3. qualified addressing and collision tests;
4. Product WS/EV multi-source binding and STM Technical Model Gate extensions;
5. direct dependency and bounded cross-project impact traversal rules;
6. Product-scoped RF/CQ/TE allocation and adjudication contracts;
7. independent availability dimensions and unavailable-source behavior;
8. Product package declarations, resolved snapshots, and Stage B gate tests;
9. `PRJ-*`/`RG-*` lifecycle and impact propagation tests;
10. authorization checks proving membership grants no repository or publication
    permissions;
11. backward-compatibility tests showing Product-absent single-project flows
    are unchanged;
12. the 18 pressure scenarios translated into semantic acceptance tests before
    implementation claims are made.

The implementation plan must remain additive, preserve the approved Product
direction, and route any semantic drift back through a new Design decision and
independent review.

## 45. Design conclusion

The foundational Stage E architecture is complete as a planning baseline:
optional durable Product identity and revisions provide stable membership
context; stable Project descriptors and explicit source bindings preserve
repository-independent identity; exact baseline vectors preserve provenance;
STM and existing capability owners retain semantic authority; and Product
outputs/packages remain bounded projections with scoped freshness gates.

No Product parent is required for a single-project review, no Product baseline
is a single SHA, no report/projection/index becomes authority, no relation is
silently a dependency, no Product change triggers automatic full revalidation,
no second package system is created, and no hidden write authorization is
introduced.
