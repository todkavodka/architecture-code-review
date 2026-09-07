# Product / Multi-Project Review Contract

This reference defines the Product context boundary for explicit Product-mode
review. It composes existing Project-local evidence, STM, capability,
projection, package, freshness, and authorization contracts; it does not
replace any of them or create a generic Product fact authority.

## 1. Scope and authority

Product mode is an explicit opt-in review scope. A Product is an optional
durable logical context that groups selected Projects and shared/external
resources for a bounded review. A Product is not a mandatory parent of a
Project, repository, review target, review session, or workspace.

The Product Context Workflow owns only Product context semantics:

- stable Product identity and Product context revisions;
- immutable membership and shared-resource declarations;
- selection of an accepted Product revision for a session;
- Product baseline acceptance routing;
- qualified cross-project scope and context routing;
- Product output and package composition requests.

The Product context is not authority for technical facts, observations,
findings, test contracts, code-quality conclusions, projections, or package
gate results. Those meanings remain with their existing owners:

| Meaning | Existing authority |
|---|---|
| `WS-*` worksets and `EV-*` observations | [Shared Evidence Model](shared-evidence-model.md) |
| accepted factual technical records and relations | [Shared Technical Model](shared-technical-model.md) and the Technical Model Gate |
| direct dependencies and impact strengths | [Technical Model Dependencies](technical-model-dependencies.md) |
| change impact and freshness decisions | [Revalidation and Freshness](revalidation-and-freshness.md) |
| Architecture `RF-*` | Architecture Review contracts |
| Code Quality `CQ-*` and `CQRA-*` | Code Quality capability contracts |
| Test Engineering `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` | Test Engineering contract |
| `PRJ-*` projection lifecycle and freshness | [Projection Lifecycle](projection-lifecycle.md) and related projection contracts |
| package policy and gate result | [Projection Gates and Packages](projection-gates-and-packages.md) |
| session routing and human authorization | [Session Orchestration](session-orchestration.md) and [Review Modes and Orchestration](review-modes-and-orchestration.md) |

Reports, summaries, indexes, projections, and packages may describe Product
state but never promote themselves into any of these authorities.

## 2. Product identity and revision lifecycle

### Product identity

An explicitly created Product has one stable `PROD-*` identity. This is the
only new Stage E identity family. The identity is immutable after allocation;
display metadata, membership, policy, and Product context changes are
represented by Product revisions.

Conceptually:

```text
Product Identity
  product_id: PROD-<opaque-stable-key>
  display_name: <human label>
  lifecycle: ACTIVE | RETIRED
  current_revision: <accepted Product revision or NONE>
```

The Product Context Workflow allocates the identity once and may retire it
only after explicit human authorization. Retirement preserves all historical
revisions, baselines, evidence, and findings. A Product may exist before a
review is complete and may contain one Project. A Product may be consumed by
multiple independent sessions, but every session selects and pins an explicit
accepted Product revision.

Product identity is context, not a universal semantic owner. Its
`current_revision` is a coordinator convenience pointer and never retargets a
historical or concurrently pinned session.

### Product revision

Product revisions reuse the revision convention on the Product identity:
`PROD-<key>@revN`. No separate Product-revision family is introduced. Each
revision is immutable and records the accepted Product context, including its
membership snapshot, shared-resource declarations, membership policy,
provenance, lifecycle, and coherency policy.

The Product Context Workflow is the sole allocator and writer of Product
revisions. A revision follows:

```text
PROPOSED → ACCEPTED → SUPERSEDED
                    ↘ RETIRED
```

The Product Context Acceptance Gate is the acceptance authority. Only an
`ACCEPTED` Product revision may be referenced by a Product baseline, Product
scope, Product capability record, projection, or package. Acceptance of a
revision advances the Product convenience pointer but does not accept a
baseline or any technical conclusion. A later revision supersedes rather than
rewrites its predecessor.

Product identity, Product revision, and Product baseline are distinct:

```text
stable Product identity
  → immutable accepted Product-context revision
    → immutable review-time Product baseline vector
```

## 3. Project and repository distinction

A Project is a stable logical unit represented by an opaque coordinator
`project_key`. It is not a repository, URL, path, branch, revision, Review
Target, Review Session, or workspace. Project identity is stable when source
locations, repository sets, paths, branches, or worktrees change.

The Project descriptor is routing identity only. It does not become an STM
fact family or a `PRJ-*` projection. Project-local semantic authority remains
owned by STM or the relevant capability contract.

Repository/source bindings are separate, revisioned provenance records. Each
binding identifies the repository, selected path/scope, exact revision or
content binding, ref metadata, baseline type, availability, and provenance.
The source binding owns the relationship between a Project and a source state;
Product membership does not.

The accepted Product context supports all explicit cardinalities:

- one Project to one repository;
- one Project to multiple repositories;
- multiple Projects to one monorepository;
- multiple Projects to multiple repositories.

Monorepository path/scope selectors are explicit. Overlapping selectors are
allowed only when each semantic consumer qualifies the Project scope it uses;
overlap does not merge Project identities or infer technical ownership. A
multi-repository Project requires every contributing binding in the selected
baseline or an explicit unavailable limitation.

## 4. Product membership and multi-Product isolation

Membership is an immutable embedded entry in a Product revision, not a new
global semantic family:

```text
membership_entry:
  membership_key: <stable within Product history>
  product_id: PROD-*
  project_key: <stable Project descriptor>
  role: <bounded Product role>
  requiredness: REQUIRED | OPTIONAL | CONDITIONAL
  condition_ref: <controlled condition or NONE>
  status: ACTIVE | RETIRED
  provenance: <authorized request or accepted coordination source>
  effective_from_revision: PROD-*@revN
  effective_to_revision: <or OPEN>
```

The Product Context Workflow writes membership revisions after explicit human
authorization. Membership lifecycle belongs to the Product revision. A
member's effective source revision belongs to the Product baseline, not to
membership identity.

Membership means Product context participation only. It is not ownership,
usage, dependency, repository access, write authority, or semantic authority.
Shared-resource declarations are separate from Project membership.

One Project may belong to multiple Products. Each Product independently owns
its membership entry, Product revision history, baseline vectors,
Product-scoped interpretations, and package snapshots. Product X cannot
mutate Product Y through membership, baseline, projection, or capability
routing. Project-local records may be reused only through qualified exact
identity, revision, provenance, freshness, and scope dependencies; reuse does
not transfer ownership.

Product-to-Product nesting and Product membership cycles are outside this
contract. Technical graph cycles remain STM/dependency concerns.

## 5. Product baseline vector

A Product baseline is an immutable review-time record scoped to an accepted
Product revision and session. It has a Product-scoped `baseline_key` and is
never represented by one Git SHA.

Conceptually:

```text
product_baseline:
  product_id: PROD-*
  product_revision: PROD-*@revN
  baseline_key: <Product-scoped opaque key>
  members:
    - project_key
      binding_set:
        - repository identity
          selected scope
          exact revision or content binding
          branch/ref metadata
          baseline type
          dirty/noncanonical state
          source availability
      project profile reference
      evidence references
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

Every contributing repository, Project source, and external source has an
exact revision or exact content binding. Cross-project claims retain the
complete contributing vector rather than only the source where a claim was
written. Baseline acceptance is human-controlled by the Product Baseline
Acceptance Gate. The gate verifies bindings, availability disclosure,
addressable evidence, coherency, and the accepted Product revision policy; it
does not adjudicate technical facts or findings.

Product revision and Product baseline have separate lifecycles. A new baseline
at the same Product revision does not rewrite or advance Product context. A
source or coordination change creates a new baseline candidate and targeted
impact/revalidation; accepted historical baselines remain addressable.

## 6. Coherency and dirty/noncanonical state

`coherency` is one independent baseline dimension:

| Value | Product-context meaning |
|---|---|
| `COHERENT` | Required bindings are exact and available, and coordination-marker/protocol evidence ties them to one logical review event without claiming atomic multi-repository Git state. |
| `MIXED_EXPLICIT` | Required bindings are exact and provenance-complete, but capture times, branches, source states, or coordination evidence differ; the accepted Product policy permits the mixture and limitations are recorded. |
| `UNKNOWN` | A required binding, provenance, availability, coordination fact, or conflict prevents classification as either of the other values. |

`REQUIRE_COHERENT` rejects `MIXED_EXPLICIT`; `ALLOW_MIXED_EXPLICIT` permits
only the explicit mixed limitations. `UNKNOWN` cannot satisfy a claim that
requires the unresolved binding. The Product Baseline Acceptance Gate records
the predicate evidence and rationale. The coherency value does not represent
source availability, review coverage, semantic availability, projection
freshness, or package gate status.

Dirty and noncanonical sources are neither automatically invalid nor
automatically accepted. If admitted by explicit Product policy, the baseline
must preserve the applicable binding:

- clean state: commit SHA, repository, selected scope, and ref metadata;
- dirty tracked state: base commit plus changed-path/content fingerprints;
- selected untracked content: explicit inclusion and content fingerprints;
- detached HEAD: exact commit and absent branch identity;
- local-only commit: exact local commit/ref and local-only marker;
- missing remote: source locator and unavailable-remote state;
- diverged sources: separate exact binding per source/worktree.

No Product state may call local-only or dirty content canonical remote state
without its required evidence. If a source is not admitted, bounded local work
may continue, while claims requiring it remain unavailable or insufficient.

## 7. Availability dimensions

Product context records five independent dimensions:

1. **Source Availability** — whether the declared source is accessible and
   exact provenance can be established.
2. **Review Coverage** — which selected scope was investigated.
3. **Semantic Availability** — whether the required STM or capability meaning
   is accepted, insufficient, disputed, or absent.
4. **Projection Freshness/Availability** — whether a selected `PRJ-*` is
   verified and `CURRENT`, `STALE`, or `BLOCKED` for its dependencies.
5. **Package Gate Result** — whether a named package policy permits its finite
   consuming scope.

There is no universal Product `PARTIAL` or `BLOCKED` status. An unavailable
Project is not a verified Project, failed Project, or negative finding. A
Product summary may display these dimensions together, but each dimension is
owned and updated by its existing workflow. Independent local semantics,
projections, and packages may remain usable when a bounded Product dependency
is unavailable.

## 8. Qualified addressing and cross-project routing

Cross-project references qualify the existing owner using at least:

```text
stable project_key
  + artifact family
  + local artifact identity
  + accepted artifact revision
  + Product baseline binding when Product-scoped
```

The textual serialization is implementation-defined. A bare local identifier
is insufficient for a Product-scoped cross-project reference when two Projects
can use the same family and identifier. Qualification prevents collisions but
does not relocate or transfer the referenced authority.

Product cross-project routing is a composition step:

```text
accepted Product revision and baseline
  → qualified Project/source bindings
  → bounded WS/EV evidence and accepted STM relations
  → owning capability interpretation
  → Product projections/packages
```

Product-scoped WS/EV continues to be observation authority under the Shared
Evidence Model. Accepted cross-project factual meaning continues through the
Technical Model Gate. Direct dependencies remain dependent-artifact-owned and
distinct from factual relations, generated reverse indexes, and impact
results. Reports, summaries, and indexes can navigate to these authorities but
cannot adjudicate them.

## 9. REVALIDATE and EXTEND boundary

Product `REVALIDATE` is delegated to the existing revalidation/freshness
contract with Product context supplied as an exact accepted revision and
baseline. Its composition path is:

```text
changed source binding
  → Project-local impact root
  → direct qualified dependency metadata
  → affected cross-project relation/capability slice
  → affected Product interpretation
  → affected projections/packages
```

The route is minimum-slice and impact-driven. It preserves
`CONTEXT_EXPANSION_REQUIRED` and `FULL_REAUDIT_RECOMMENDED`; a systemic result
may recommend a full Product review but never starts one automatically.
Unknown linkage is investigated rather than preserved by assumption. Product
membership changes are Product-revision changes and receive targeted impact
adjudication.

Product `EXTEND` is additive. It may add a Project, capability, bounded
cross-project investigation, output, or shared-resource reference. Accepted
unaffected state is preserved. If the addition changes Product meaning,
requiredness, role, shared-resource meaning, or another Product
interpretation, it creates a new Product revision and enters targeted
revalidation. It does not silently reopen unrelated Project findings or
reconfigure existing output selection.

This reference establishes routing and boundaries only; traversal, freshness,
and regeneration mechanics remain owned by
[Revalidation and Freshness](revalidation-and-freshness.md), dependency, and
projection contracts.

## 10. Product outputs and packages

Output selection is explicit. Product existence does not auto-create outputs.
Each selected output must declare its owner, semantic inputs, qualified
baseline/dependency bindings, prerequisites, freshness inputs, finite package
membership where applicable, and Product/Project scope.

| Output | Classification | Existing owner/boundary |
|---|---|---|
| Product Architecture Review | `CONDITIONAL_OUTPUT` | Architecture Review; Product `RF-*` requires independent Product adjudication. |
| Cross-Project Dependency View | `OPTIONAL_STAGE_E_OUTPUT` | Derived navigation projection; direct dependency metadata remains authority. |
| Product Target Architecture | `CONDITIONAL_OUTPUT` | Architecture target endpoint and review. |
| Product Remediation Roadmap | `CONDITIONAL_OUTPUT` | Roadmap endpoint; roadmap publication remains separately authorized. |
| Product Test Assurance | `CONDITIONAL_OUTPUT` | Test Engineering projection/package over accepted Product-scoped records. |
| Product Code Quality Summary | `CONDITIONAL_OUTPUT` | Code Quality projection over declared local/Product `CQ-*` dependencies. |
| Product Technical Documentation | `OPTIONAL_STAGE_E_OUTPUT` | Technical Documentation projection over selected Product STM/evidence inputs and finite package scope. |

Product packages reuse the Stage B package contract. The package owner is the
selected capability or endpoint, not the Product aggregate. A Product package
uses an existing `PKG-*` declaration shape and records a resolved immutable
membership snapshot containing selected Product `PRJ-*` outputs, required,
optional, and controlled conditional members, exact Project package/projection
references, dependency closure, freshness policy, baseline/semantic
dependencies, and blocked/unavailable member results.

Project subpackages are exact references, not embedded copies. Existing
`PERMISSIVE`, `REQUIRED_SCOPE_CURRENT`, and `ALL_SCOPED_CURRENT` policies retain
their Stage B meanings. At Product scope, `ALL_SCOPED_CURRENT` evaluates only
the resolved required Product members and their mandatory dependencies; an
unrelated Project package cannot block the Product package. No second package
authority is introduced.

## 11. Storage and layout

Product context is stored in the coordinator review workspace under a
Product-scoped namespace. It is not stored inside an arbitrary member Project,
and it does not require a database, service, graph database, vector/RAG
system, daemon, or generic registry backend.

Conceptually:

```text
working/
├── INDEX.md                         # coordinator workflow authority
├── projects/<project-key>/          # stable Project descriptors/bindings
├── products/<PROD-key>/
│   ├── identity.md                  # Product identity/lifecycle
│   ├── revisions/<rev>.md           # immutable Product contexts
│   ├── baselines/<baseline-key>.md  # immutable source vectors
│   ├── evidence/WS-*.md             # Product-scoped evidence references
│   └── projections/                 # non-authoritative Product views
└── projections/                     # existing Stage B operational records
```

`working/INDEX.md` remains coordinator workflow authority and is not a Product
semantic artifact or `PRJ-*` projection. Exact serialization and filenames are
implementation details within this ownership boundary. Product namespace
placement does not change STM or capability ownership.

## 12. Authorization boundary

Product membership, identity, baseline, report, index, projection, package, or
cross-project reference grants no implicit permission. Each action remains
separately human-authorized under session orchestration:

| Action | Required boundary |
|---|---|
| Read another repository/source | Explicit source access for that binding |
| Select revision/branch/worktree | Explicit baseline selection |
| Admit dirty or untracked content | Explicit baseline acceptance |
| Create Product or change membership | Product Context Workflow plus human authorization |
| Write Project-local semantic state | Existing Project STM/capability owner |
| Write Product-scoped semantic state | Existing owning capability/STM Gate plus Product scope authorization |
| Generate projection/package | Selected endpoint/capability and existing package policy |
| Run tests, simulators, or environments | Separate Test Engineering/environment authorization |
| Modify code or create/remove worktrees | Explicit implementation authorization outside Product membership |
| Commit, PR, push, or deploy | Separate human-controlled publication/deployment authorization |

No clone, checkout, cleanup, worktree operation, code modification, test
execution, commit, PR, push, or deployment is hidden in Product support.

## 13. Lifecycle and ownership

| Object | Identity owner | Writer/lifecycle owner | Provenance and consumers |
|---|---|---|---|
| Product identity | Product Context Workflow | Product Context Workflow; explicit retirement authorization | Creation authorization/history; sessions and membership |
| Product revision | Product Context Workflow | Product Context Acceptance Gate; revision history remains immutable | Prior context and authorized membership sources; baselines/scopes |
| Membership entry | Product Context Workflow | Product Context Workflow within Product revision | Authorized request and Project descriptor; baseline/package resolution |
| Project descriptor | Coordinator identity registry | Project identity workflow | Explicit identity/source declaration; Products and sessions |
| Repository/source binding | Baseline/evidence workflow | Authorized session through baseline/evidence owner | Repository/ref/content and access result; WS/EV and semantic gates |
| Product baseline | Product Baseline Acceptance Gate | Authorized Product review session proposes; Baseline Gate accepts | Exact source/content vector, external sources, Profiles, WS/EV; STM/capabilities |
| Product context routing | Product Context Workflow | Coordinator routing state only | Accepted Product revision/baseline; sessions and selected endpoints |
| Product-scoped WS/EV | Shared Evidence Model | Evidence workset writer | Qualified sources/baseline; STM and capability gates |
| Product-scoped factual relation | Technical Model Gate | Technical Model Gate only | Qualified accepted STM/WS/EV; Architecture/TE/CQ consumers |
| Product projection/package | Existing owning endpoint | Projection/package lifecycle owner | Declared dependencies and resolved package scope; users/gates |

No row makes Product identity the writer of technical meaning. Semantic
freshness belongs to the owning semantic contract; projection freshness and
package gate state remain separate downstream concerns.

## 14. Cross-reference and invariants

Implementations of Product mode must compose, rather than redefine:

- [Shared Evidence Model](shared-evidence-model.md) for WS/EV observations;
- [Shared Technical Model](shared-technical-model.md) for factual authority
  and the Technical Model Gate;
- [Technical Model Dependencies](technical-model-dependencies.md) for
  dependent-to-prerequisite direct edges and impact strengths;
- [Revalidation and Freshness](revalidation-and-freshness.md) for impact,
  preserved state, and freshness;
- [Projection Lifecycle](projection-lifecycle.md), projection dependencies,
  impact, regeneration, and verification for `PRJ-*`/`RG-*` behavior;
- [Projection Gates and Packages](projection-gates-and-packages.md) for Stage B
  package policy;
- session/review orchestration for explicit mode selection and authorization;
- Architecture Review, Code Quality, and Test Engineering contracts for their
  respective semantic families and capability gates.

The following invariants are mandatory:

```text
Product != Project
Project != repository
Project != Review Target
Project != Review Session/workspace
Product identity != Product revision != Product baseline
Product baseline != one Git SHA
membership != ownership != usage != dependency
relation != dependency != reverse index != impact result
projection/report/index/package != semantic authority
Product mode is optional
single-project mode requires no Product state
Product membership grants no repository or publication permission
```

Product-local composition cannot make Product a universal fact owner, cannot
transfer Project-local authority, cannot promote a local finding by
aggregation, cannot redefine package policy, and cannot initiate a full
Product revalidation or regeneration implicitly. Any future contract
extension must preserve these boundaries and route semantic changes through
the owning authority.
