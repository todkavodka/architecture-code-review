# Stage E — Product / Multi-Project Review: Independent Design Review

**Review date:** 2026-09-06  
**Review type:** Independent Design Review only  
**Reviewed baseline:** `5342650769d8c33d6b4cd9a675203b3d3b706be5`  
**Branch:** `main`  
**Chosen architecture:** `OPTION C — HYBRID`

## Scope and sources

Reviewed completely:

- `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-design.md`
- `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-discovery.md`
- `docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-discovery-review.md`
- `docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-discovery-rereview.md`

The Design was checked against the current normative sources, including:

- `SKILL.md`
- session and review-mode orchestration;
- shared evidence and Shared Technical Model contracts;
- technical dependency, revalidation, projection lifecycle, impact,
  regeneration, dependency-selector, and package contracts;
- Architecture Review ownership and boundary contracts;
- `capabilities/test-review/SKILL.md` and
  `capabilities/test-review/references/test-engineering-contract.md`;
- `capabilities/code-quality-review/SKILL.md` and its contract, lifecycle, and
  projection references;
- `references/technical-documentation.md` where the Design's selected output
  set requires it.

No source artifact was modified during this review. The Design remains the
sole uncommitted tracked-scope artifact; unrelated untracked files were
preserved.

## Repository and baseline verification

Repository state before review:

- branch: `main`;
- `HEAD`: `5342650769d8c33d6b4cd9a675203b3d3b706be5`;
- `origin/main`: `63bef65c765d0a381b63a7b4fdffe1679d89eee5`;
- `origin/main` is an ancestor of `HEAD`;
- no tracked changes other than the uncommitted Design artifact;
- no changes under `SKILL.md`, `references/**`, `capabilities/**`, or
  `docs/roadmap.md`.

## Summary verdict

The Design is directionally sound and preserves the approved Discovery and
Option C. It keeps Product optional, separates Project from repository and
session, uses exact Product baseline vectors, preserves STM and capability
ownership, keeps projections/packages non-authoritative, retains bounded
impact-driven `REVALIDATE`, and introduces no hidden repository or publication
permissions.

It is not yet safe to become the implementation-plan basis. Four material
semantic gaps would force implementation to invent behavior at boundaries that
the Design declares accepted: Product revision currentness/acceptance,
Product-scoped CQ/TE identity and scope integration, the contract impact of
the selected Technical Documentation and projection-selector paths, and the
acceptance meaning of baseline coherency. None is a contradiction requiring a
new architecture direction, but each needs Design remediation before planning.

**Verdict:** `STAGE_E_DESIGN_REVIEW_FINDINGS`

## Findings

### D-01 — MEDIUM — Product revision lifecycle and currentness are not fully defined

**Classification:** `MISSING_FOUNDATIONAL_DECISION`

**Evidence:**

- Section 5 defines Product identity lifecycle as `ACTIVE | RETIRED` and a
  `current_revision` pointer.
- Section 6 makes Product revisions immutable and lists their contents and
  revision-creation triggers, but does not define a revision lifecycle,
  acceptance state, or currentness transition.
- Section 11 defines baseline acceptance against a Product revision, while
  Section 36 assigns Product context lifecycle/freshness ownership but only
  describes freshness as “context validity.”

**Concern:**

The Design does not say whether a newly created Product revision is draft,
accepted, superseded, or current before a review baseline is accepted. It also
does not define whether a Product baseline may bind an unaccepted Product
revision, how concurrent sessions select or pin a revision, or how the
`current_revision` pointer changes when a later revision is created but not yet
accepted.

Product identity, Product revision, and Product baseline are correctly
separated, but the lifecycle boundary between them is incomplete. An
implementation would have to invent whether revision acceptance is a Product
context gate, a baseline gate, or both, and whether a revision can be consumed
by Product-scoped semantic records before acceptance.

**Required remediation:**

Define the Product revision state/currentness model and transitions, including:

- draft/proposed versus accepted/current versus superseded/retired semantics;
- the exact writer and acceptance gate for a revision;
- whether a Product baseline may reference only an accepted revision;
- how `current_revision` is selected and whether it is merely a convenience
  pointer or an authority field;
- how multiple independent sessions pin historical revisions without being
  affected by later Product changes;
- which lifecycle/freshness concepts apply to Product context and which remain
  exclusive to semantic artifacts and projections.

This can remain additive to Option C, but it must be resolved in Design rather
than deferred to implementation.

### D-02 — MEDIUM — Product-scoped Code Quality and Test Engineering scope/identity integration is incomplete

**Classification:** `MISSING_FOUNDATIONAL_DECISION`

**Evidence:**

- Section 21 allows Product-scoped `CQ-*` and `CQRA-*`, but explicitly says a
  future contract extension must define how Product-scoped allocation avoids
  collision with the current repository-scoped CQ allocation.
- Section 22 allows qualified multi-Project TE records but does not define a
  Product Test Review scope identity or how Product records participate in the
  existing `TRS-*`/`test_review_scope_id` selector and package model.
- Section 35 classifies both families as reused existing identifiers, while
  Section 37 only states that future contracts should permit Product scope.

**Concern:**

The Design declares Product CQ/TE semantics accepted while leaving the
identity and scope binding required by the current contracts open. For CQ,
implementation still has to decide whether a Product-scoped finding receives a
Product namespace, a qualified repository allocation, or another stable
allocation that cannot collide with local `CQ-*`; the same gap affects
Product-scoped `CQRA-*` actions.

For Test Engineering, the current selectors use a persisted Test Review scope
record and exact `test_review_scope_id` membership. The Design does not decide
whether Product TE records use a new Product-bound scope record, extend an
existing scope, or remain in separate Project scopes linked by qualified
relations. It therefore does not yet determine which records enter Product
Test Assurance projections/packages or how local and Product selectors remain
disjoint.

This is not merely serialization detail: identity allocation and selector
membership determine authority, revalidation, package closure, and collision
behavior.

**Required remediation:**

Resolve, at Design level, both capability boundaries:

- define stable, collision-free Product CQ/CQRA allocation and scope semantics
  while preserving Code Quality ownership and local repository-scoped IDs;
- define Product Test Engineering scope identity, binding to the existing
  `TRS-*`-style selector model, local-versus-Product record membership, and
  Product Assurance package inputs;
- state how Product-scoped records retain qualified Project provenance and how
  CQRA completion/revalidation and TE `TASK-*` work remain independent;
- reflect the decisions in the contract-impact matrix with the exact selector,
  lifecycle, and package surfaces to extend.

Until this is decided, `product_code_quality`, `product_test_engineering`, and
the identifier strategy cannot be considered fully resolved.

### D-03 — MEDIUM — Contract-impact matrix omits selected Technical Documentation and projection-selector contracts

**Classification:** `INCOMPLETE_CONTRACT_IMPACT_ACCOUNTING`

**Evidence:**

- Section 28 classifies Product Technical Documentation as an
  `OPTIONAL_STAGE_E_OUTPUT`.
- Section 29 says Product packages use Stage B package mechanics, and Section
  31 relies on Product projection dependency snapshots and selectors.
- Section 37 lists extensions for projection lifecycle, impact, regeneration,
  and packages, but does not list `references/technical-documentation.md` or
  `references/projection-dependencies.md`.
- The current Technical Documentation contract owns the `PRJ-TECH-DOC-*`
  selectors and `PKG-TECHNICAL-DOCUMENTATION`; the projection dependency
  contract owns `SEMANTIC_SELECTOR`, resolution snapshots, and Product
  projection dependency semantics.

**Concern:**

The Design offers Product Technical Documentation as a supported output but
does not identify the normative contract that owns its Product scope, selected
sections, STM selector qualification, package membership, or exact dependency
closure. It also relies on Product-scoped selector resolution without naming
the contract surface that defines qualified selector dimensions and snapshots.

The omission means an implementation plan could treat the generic package and
projection extensions as sufficient and invent Product Technical Documentation
semantics or selector behavior in implementation. That would weaken the
contract-impact matrix's purpose as the planning boundary.

**Required remediation:**

Add the omitted normative surfaces to the matrix and specify their conceptual
extensions:

- Technical Documentation: Product-scoped STM selector inputs, Product
  availability/limitation rendering, section-selection scope, and
  `PKG-TECHNICAL-DOCUMENTATION` membership/freshness behavior;
- Projection Dependencies: qualified Product semantic selectors, exact
  Product baseline/member resolution snapshots, and collision-safe
  `SEMANTIC_EXACT`/`SEMANTIC_SELECTOR` bindings;
- Projection Verification, if Product-specific verification dimensions are
  needed, or explicitly record `NO_CHANGE` with the reason that existing V1–V4
  rules fully cover Product projections.

Alternatively, the Design may explicitly defer Product Technical Documentation
and remove it from the supported output set. It cannot remain a supported
optional output with its owning contract impact unaccounted.

### D-04 — MEDIUM — Baseline coherency has labels but no acceptance predicate

**Classification:** `MISSING_ACCEPTANCE_SEMANTICS`

**Evidence:**

- Section 12 introduces `COHERENT`, `MIXED_EXPLICIT`, and `UNKNOWN` and
  correctly keeps them separate from availability, coverage, freshness, and
  package status.
- `COHERENT` is defined as satisfying “declared coordination/evidence
  conditions for one logical review moment,” but those conditions are not
  defined anywhere in the Design.
- `MIXED_EXPLICIT` is acceptable “when the Product policy permits it,” but the
  policy and permitted Product conclusions are not defined.
- Section 11 says baseline acceptance verifies the coherency classification,
  but does not state the evidence or authority that can establish each value.

**Concern:**

The classification vocabulary is sound, but the acceptance meaning is still
open. Two implementations could classify the same vector differently: one
could call independently captured committed revisions `COHERENT` because all
bindings are exact, while another could call them `MIXED_EXPLICIT` because no
coordination evidence exists. They could also disagree about which Product
claims are allowed under `MIXED_EXPLICIT` or `UNKNOWN`.

This directly affects cross-project evidence acceptance, Product RF/CQ/TE
adjudication, revalidation roots, and package eligibility. It is therefore a
semantic decision, not an implementation algorithm.

**Required remediation:**

Define the baseline acceptance predicate and authority for each classification:

- what evidence establishes `COHERENT` without claiming atomic Git capture;
- what exact conditions force `MIXED_EXPLICIT`;
- when `UNKNOWN` is required;
- which cross-project facts, relations, capability conclusions, and projections
  may proceed under each value;
- whether a Product policy may permit mixed baselines and who accepts that
  policy;
- how a later source advancement or changed coordination evidence supersedes
  the classification and triggers Product revalidation.

The three labels should remain independent from availability, coverage,
freshness, and package gate states.

## Product/Project identity assessment

**Result:** `FINDINGS` due D-01 and D-02.

The Design correctly establishes:

- optional durable `PROD-*` identity separate from Product revision;
- Product revisions separate from review baselines;
- stable Project descriptors separate from repository, source revision, review
  target, and review session;
- one-to-one, one-to-many, many-to-one, and many-to-many Project/repository
  cardinalities;
- explicit membership entries and multi-Product isolation;
- no Product-to-Product nesting.

The remaining gaps are Product revision acceptance/currentness and
capability-specific Product scope/identity integration.

## Baseline and provenance assessment

**Result:** `FINDINGS` due D-04.

The vector model is correct and preserves exact repository, path/scope,
revision/content, branch/ref, dirty, external, availability, Profile, and
evidence bindings. Historical baselines are immutable and supersedable; a
single SHA is not used. Dirty, detached, local-only, missing-remote, and
untracked states are handled transparently.

The unresolved issue is the acceptance predicate for `COHERENT`,
`MIXED_EXPLICIT`, and `UNKNOWN`. Exact binding and coherency classification
are not sufficient until the Design defines what claims each classification
supports.

## Evidence and STM assessment

**Result:** `PASS`

The Design reuses Product-scoped `WS-*`/`EV-*` worksets with qualified
multi-source bindings and keeps reports, summaries, indexes, and packages out
of evidence authority. Project-local STM remains authoritative for local facts;
cross-project relations use qualified accepted STM records and the existing
Technical Model Gate. No generic Product factual model is introduced.

The relation/dependency/index/impact distinction and qualified collision
handling are preserved.

## Capability ownership assessment

**Result:** `FINDINGS` due D-02.

Architecture Review retains `RF-*`; Test Engineering retains `BC-*`, `CC-*`,
`MAT-*`, `TM-*`, `GAP-*`, and `TASK-*`; Code Quality retains `CQ-*` and
`CQRA-*`. Product summaries remain projections, and cross-project scope does
not move CQ or TE into Architecture Review.

However, Product CQ allocation and Product TE scope-selector integration are
not sufficiently designed for implementation planning.

## REVALIDATE assessment

**Result:** `PASS`

The Design preserves the required route from changed source binding to local
impact roots, direct dependencies, qualified cross-project relations,
affected capability records, Product interpretations, projections, and
packages. It preserves unrelated accepted state, requires minimum necessary
work, treats unknown linkage conservatively, uses `CONTEXT_EXPANSION_REQUIRED`,
and allows `SYSTEMIC` to produce `FULL_REAUDIT_RECOMMENDED` without automatic
full review.

Reverse indexes remain navigation only, and Product membership changes enter a
separate revision/revalidation path.

## Partial availability assessment

**Result:** `PASS`

Source availability, review coverage, semantic availability, projection
freshness/availability, and package gate result remain independent. The Design
correctly handles unavailable members without treating them as verified,
failed, or negative findings. Local conclusions and independent packages may
remain usable while dependent Product claims or packages are blocked.

## Package and projection assessment

**Result:** `FINDINGS` due D-03.

The Design correctly reuses Stage B named finite packages, resolved membership
snapshots, required/optional/conditional members, exact Project package
references, scoped `ALL_SCOPED_CURRENT`, `PRJ-*`, `RG-*`, impact accounting,
and explicit regeneration. It does not create a second package authority or a
Product-specific projection identity family.

The supported Product Technical Documentation output and Product selector
dependencies are not represented in the contract-impact matrix, leaving a
planning boundary incomplete.

## Authorization assessment

**Result:** `PASS`

Read, revision selection, dirty admission, Product creation/membership,
semantic writes, projection generation, tests, worktrees, code changes,
commit, PR, push, and deployment are explicitly separated. Product membership
grants none of these permissions, and no automatic repository operation is
introduced.

## Storage/layout assessment

**Result:** `PASS`

The coordinator review workspace with a Product-scoped namespace is compatible
with the current file-based architecture. Product state is not hidden inside
an arbitrary member Project, `working/INDEX.md` remains coordinator authority,
and Project-local semantic artifacts retain their owners. The layout is
portable in principle; exact paths are correctly left as implementation detail.

## Identifier assessment

**Result:** `FINDINGS` due D-02.

Introducing only `PROD-*` is justified for durable Product identity. Product
revision reuses `PROD-*@revN`; membership, baseline, cross-project evidence,
STM relations, RF, TE, CQ, projections, packages, and regeneration reuse
existing concepts.

The Product CQ/CQRA allocation and Product TE scope identity are not resolved
enough to prove uniqueness, selector membership, or package behavior.

## Backward compatibility assessment

**Result:** `PASS`

Product-absent single-project operation requires no Product identity, registry,
baseline vector, membership, cross-project evidence, or Product package.
Existing local identities and packages remain valid, no synthetic one-member
Product is created, and no migration is required merely to continue current
operation.

## Migration assessment

**Result:** `ADDITIVE_CONFIRMED`

The Design can remain additive: existing local artifacts are not rewritten or
renumbered, and Product references are introduced only when Product mode is
explicitly selected. Historical prose is not silently promoted into authority.

## Contract-impact assessment

**Result:** `FINDINGS` due D-03, with D-02 also affecting capability rows.

The matrix correctly identifies additive impact for orchestration, shared
evidence, STM, dependency traversal, revalidation, projections, packages,
Architecture, Test Engineering, and Code Quality. It correctly requires one
focused Product contract reference and avoids contract modification during
Design.

It is incomplete because the supported Technical Documentation output and the
projection selector/dependency contract are absent. The exact Product CQ/TE
scope and allocation extensions also need to be made concrete in their rows.

## Pressure-scenario assessment

**Result:** `PASS`

All 18 approved Discovery pressure scenarios are present. Each includes input,
expected behavior, forbidden behavior, affected authority, and the relevant
Product/package/projection outcome. Coverage includes single-project
compatibility, clean and mixed vectors, unavailable and dirty sources,
baseline advancement, API compatibility, shared resources, Product and local
findings, additive and membership-semantic `EXTEND`, targeted `REVALIDATE`,
projection freshness, version compatibility, conflicting evidence, blocked
packages, multi-Product reuse, and standalone/single-member Product
transitions.

The scenarios are architecture tests rather than implementation specifications.
D-01 through D-04 are semantic gaps exposed by otherwise sufficient scenarios,
not missing scenario coverage.

## Design completeness assessment

**Result:** `FINDINGS`

The final decision table marks all listed topics as
`ACCEPTED_DESIGN_DECISION`, and the document contains no `TBD`/`TODO` or
unqualified foundational question. However, D-01 through D-04 show that the
accepted labels overstate completion in four areas. The implementation plan
would still need to invent revision state, CQ/TE scope allocation, Technical
Documentation contract routing, selector impact surfaces, and coherency
acceptance semantics.

The Design is therefore coherent in direction but not yet complete as an
implementation-plan authority.

## Invariant and risk regression

| Invariant | Result |
|---|---|
| Product optional; single-project first-class | `PASS` |
| Product != Project/repository/session/workspace | `PASS` |
| Repository is provenance/revision source | `PASS` |
| STM remains factual authority | `PASS` |
| Architecture/Test/CQ ownership retained | `PASS` with D-02 scope gap |
| Projection != authority | `PASS` |
| Dependency != relation; index != dependency authority | `PASS` |
| Persisted != current; accepted != complete; coverage != depth | `PASS` |
| Impact-driven `REVALIDATE`; no default full Product review | `PASS` |
| Additive `EXTEND` | `PASS` |
| Product membership grants no permissions | `PASS` |
| No unnecessary service/database architecture | `PASS` |

No HIGH authority, provenance, or backward-compatibility flaw was found.

## Required remediation before implementation planning

1. Resolve Product revision lifecycle, acceptance, currentness, pinning, and
   concurrent-session semantics (D-01).
2. Resolve Product CQ/CQRA allocation and Product Test Engineering scope,
   selector, and package integration without moving ownership (D-02).
3. Complete the contract-impact matrix for Technical Documentation,
   projection dependencies/selectors, and any Product-specific projection
   verification extension (D-03).
4. Define the baseline coherency acceptance predicate, permitted conclusions,
   and supersession/revalidation behavior for each coherency value (D-04).

Remediation should remain a Design-only correction/re-review. No implementation,
contract edit, roadmap edit, Discovery edit, commit, or push is required for
this review.

## Implementation-plan entry recommendation

`STAGE_E_DESIGN_REMEDIATION`

After the four findings are corrected and independently re-reviewed, the
Design can become the basis for the Stage E Implementation Plan. Option C
remains viable and does not need architectural replacement.

## Review metadata

- `HIGH`: 0
- `MEDIUM`: 4
- `LOW`: 0
- `finding_ids`: `D-01`, `D-02`, `D-03`, `D-04`
- `architecture_invariants`: `PASS`
- `single_project_compatibility`: `PASS`
- `normative_files_changed`: `NO`
- `design_artifact_changed`: `NO`
- `discovery_artifacts_changed`: `NO`
- `roadmap_changed`: `NO`
- `implementation_performed`: `NO`
- `commit_performed`: `NO`
- `push_performed`: `NO`

## Final verdict

`STAGE_E_DESIGN_REVIEW_FINDINGS`
