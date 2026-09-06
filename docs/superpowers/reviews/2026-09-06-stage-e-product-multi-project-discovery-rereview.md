# Stage E — Product / Multi-Project Discovery: Targeted Independent Re-Review

**Review date:** 2026-09-06  
**Review type:** Targeted independent Discovery re-review only  
**Baseline:** `63bef65c765d0a381b63a7b4fdffe1679d89eee5`  
**Branch:** `main`

## Scope and reviewed artifacts

This re-review independently verifies closure of F-01 through F-04 from the
original Discovery review. It is not a broad Stage E Discovery, Design, or
implementation review.

- Discovery artifact: `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-discovery.md`
- Original review: `docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-discovery-review.md`
- Reviewed remediation: the current Discovery artifact above
- Normative checks: only the relevant evidence, STM, dependency, revalidation,
  and package contracts

Repository state was verified before review: `main`, `HEAD` equal to the
canonical baseline, and `origin/main` equal to the canonical baseline. The
Discovery and original review artifacts were hash-checked before this artifact
was written and were not modified during the re-review.

## F-01 closure — Product identity, persistence, and baseline

**Original severity:** MEDIUM  
**Result:** `RESOLVED`

The original concern was that Product persistence, identity, and history were
presented too strongly as a constraint without proving that a persistent
Product aggregate was required. The required correction was to preserve
Product optionality and revision-bound provenance while deferring the exact
persistence, ownership, lifecycle, aggregate, and schema decisions to Design.

The remediated Discovery satisfies that boundary:

- Product is explicitly optional and is not required for `NEW`
  single-project review.
- Product is explicitly not a universal semantic owner and is not a mandatory
  parent of Project.
- The text distinguishes a durable Product identity/membership direction from
  a proven need for a persistent Product aggregate.
- Design is required to prove which membership-continuity, revalidation, and
  historical package guarantees require persistence.
- Vector/revision-bound provenance remains required, while baseline acceptance,
  coherency, partiality, dirty-vector policy, and snapshot timing remain Design
  decisions.
- Option C is retained as a bounded direction, not a completed schema or
  lifecycle.

The decision register classifies Product identity and Product baseline as
`DESIGN_DECISION_REQUIRED`, consistently with these boundaries. No
contradictory statement making Product mandatory or making Product the
universal owner remains in the reviewed sections.

## F-02 closure — Cross-project evidence and STM boundary

**Original severity:** MEDIUM  
**Result:** `RESOLVED`

The original concern was that cross-project evidence was marked resolved even
though its representation, owner, lifecycle, acceptance gate, and conflict
handling were still open. The required correction was to separate resolved
evidence constraints from unresolved authority and representation decisions.

The remediated Discovery satisfies that boundary:

- Cross-project claims require addressable multi-source bindings and complete
  contributing baseline context.
- Reports do not become evidence authority; a combined report cannot establish
  a cross-project fact.
- Co-location of Projects in one report does not establish compatibility or
  cross-project evidence.
- Project-local `WS-*`/`EV-*` evidence remains preserved and source bindings,
  revisions, contract views, and other contributing sources remain mandatory.
- The form of the cross-project record is explicitly deferred to Design:
  extension of `WS-*`/`EV-*`, an STM fact/relation, or a capability-owned
  interpretation.
- Owner/writer, lifecycle, acceptance gate, coherent baseline binding, and
  conflict handling are explicitly unresolved Design decisions.
- Cross-project STM is constrained to existing STM authority first; a narrow
  relation/index layer is permitted only if a contract gap is demonstrated and
  must not accept STM facts.
- Dependency metadata, factual relations, and generated indexes remain
  distinct; the index is not an alternate factual authority.

The decision register now classifies both Cross-project evidence and
Cross-project STM as `DESIGN_DECISION_REQUIRED`. This is consistent with the
original closure requirement and with the normative STM/evidence contracts.

## F-03 closure — REVALIDATE, partial availability, and package semantics

**Original severity:** MEDIUM  
**Result:** `RESOLVED`

This was the most important remediation item. The Discovery now preserves the
required semantic route:

```text
changed Project
→ direct cross-project dependency/impact analysis
→ affected contracts and semantic slice
→ affected Product interpretations/projections
→ minimum necessary revalidation
```

It explicitly states that one changed Project does not imply a full Product
audit. Direct dependency metadata and cross-project edges are inspected first;
`LOCAL`, `BOUNDARY`, and `SYSTEMIC` remain impact classifications; and
`SYSTEMIC` may recommend a full re-audit without starting one automatically.
Product impact root, traversal persistence, cross-project classification,
baseline coherency, membership-change handling, and preserved-set behavior
remain Design decisions. Minimum necessary work and
`CONTEXT_EXPANSION_REQUIRED` remain mandatory.

Partial availability is also correctly separated into source availability,
review coverage, semantic conclusion availability, projection
availability/freshness, and package gate result. The text explicitly prevents
`PARTIAL` or `BLOCKED` from becoming a universal Product status and states:

- an unavailable Project is not a verified Project;
- an unavailable Project is not a negative finding;
- absence of source is not itself a finding;
- missing scope blocks only claims or package gates for which it is explicitly
  required;
- independent Project gates are not automatically blocked.

Package semantics remain grounded in Stage B. The Discovery proposes reuse of
named finite packages, explicit required/optional/conditional members, resolved
membership snapshots, dependency closure, and freshness policies. It defers
Product membership snapshots, subpackage/reference semantics,
requiredness, unavailable-member handling, freshness aggregation, and the
relationship between Product and independent Project packages to Design. It
does not create a second package authority or redefine `ALL_SCOPED_CURRENT`:
the phrase is bounded to all required resolved Product package members, not all
documents of all Projects.

The decision register classifies Product `REVALIDATE`, Partial availability,
and Package model as `DESIGN_DECISION_REQUIRED`; Product `EXTEND` is likewise
design-required while retaining the resolved additive constraint. The
classification is internally consistent and the former over-commitment is
closed.

## F-04 closure — Cardinality and pressure scenarios

**Original severity:** LOW  
**Result:** `RESOLVED`

The original gap was the absence of an explicit single-member Product and
standalone-to-Product transition case. The remediated pressure scenarios now
include both:

- reuse of one Project in two Products, if permitted, to pressure identity,
  membership, baseline, provenance isolation, and impact/revalidation
  handling; and
- a standalone Project entering or leaving a single-member Product context, to
  pressure Product optionality, cardinality, and absence of mandatory parent
  assumptions.

The Discovery also states that these cases are Design pressure tests, not
premature policy: cardinality, multiple membership, cycle/contradiction
constraints, membership authority, and history remain unresolved decisions.
The scenarios require baseline/provenance isolation, minimum dependency slice,
partial/blocked result handling, package freshness, and no hidden writes to
another semantic authority. No invented cycle rule is imposed.

## Decision-register result

`decision_register = PASS`

The targeted rows and directly dependent rows are correctly classified:

- Product identity — `DESIGN_DECISION_REQUIRED`
- Product membership — `DESIGN_DECISION_REQUIRED`
- Product baseline — `DESIGN_DECISION_REQUIRED`
- Cross-project evidence — `DESIGN_DECISION_REQUIRED`
- Cross-project STM — `DESIGN_DECISION_REQUIRED`
- Product `REVALIDATE` — `DESIGN_DECISION_REQUIRED`
- Product `EXTEND` — `DESIGN_DECISION_REQUIRED`, with additive extension
  retained as a resolved constraint
- Partial availability — `DESIGN_DECISION_REQUIRED`
- Package model — `DESIGN_DECISION_REQUIRED`

No affected row is incorrectly presented as a completed semantic or
implementation decision. Existing `DISCOVERY_RESOLVED` rows remain bounded
constraints rather than hidden authority decisions.

## Pressure-scenario result

`pressure_scenarios = PASS`

The remediated scenarios are architecture pressure tests. They exercise
partial/unavailable state at distinct availability, coverage, semantic,
projection, and package layers; distinguish Product package behavior from
independent Project gates; cover additive extension and membership-semantic
revalidation; and cover one Project participating in multiple Products and
single-member Product transitions. They do not prescribe implementation policy.

## Narrow regression result

The previously passing areas remain intact:

- `architecture_invariants = PASS`
- `single_project_compatibility = PASS`
- `authority_boundaries = PASS`
- `baseline_provenance = PASS`
- `revalidation_model = PASS`
- `partial_availability = PASS`
- `package_model = PASS`

In particular, Product is not mandatory, Project is not repository/workspace/
session, projections are not authority, dependencies are not relations,
existing STM/evidence authority is not silently replaced, no multi-repository
write permission is introduced, `EXTEND` remains additive, `REVALIDATE` remains
impact-driven, and minimum necessary work is preserved.

## Option C assessment

`option_c_recommendation = SUPPORTED`

The remediation strengthens Option C's safety boundary without invalidating
the direction. It remains a bounded hybrid: optional Product context and
membership, independent Project authority and packages, revision-vector
provenance, and a minimal cross-project layer only where existing contracts
prove insufficient. Product persistence, cross-project authority shape, and
package policy remain Design work.

## Normative and scope checks

- `normative_files_changed = NO`
- `roadmap_changed = NO`
- `implementation_performed = NO`
- `commit_performed = NO`
- `push_performed = NO`
- `discovery_changed_during_rereview = NO`
- `original_review_changed = NO`

The only file created by this re-review is this targeted re-review artifact.
Unrelated untracked files were preserved.

## Design-entry recommendation

`STAGE_E_DISCOVERY_CHECKPOINT`

The remediated Discovery is safe to approve as the input to Stage E Design.
Proceed to a separate Design artifact and Design review; do not treat this
re-review as approval of a Product schema, persistence model, cross-project
fact owner, package policy, or runtime implementation.

## Final verdict

`STAGE_E_DISCOVERY_APPROVED`

Counts: HIGH `0`; MEDIUM `0` blocking; LOW `0` blocking.
