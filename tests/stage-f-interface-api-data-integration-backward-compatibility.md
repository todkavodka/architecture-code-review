# Stage F backward-compatibility validation

## Validation scope and method

This artifact validates that Stage F is a compatible extension of the existing
Stage A–E contracts. Each section records the prior invariant, the Stage F
interaction, the compatibility expectation, the actual state in the repository,
and a deterministic PASS/FAIL result. It does not rewrite or become authority
for any prior-stage semantic record.

## 1. Stage A STM families and identities

- Prior invariant: existing STM families and semantic IDs remain stable; a
  capability cannot rewrite accepted factual authority.
- Stage F interaction: IF/INT/DS/EVENT/FLOW receive optional, qualified
  properties and controlled relations.
- Compatibility expectation: new fields are additive; absent fields remain
  absent/unknown and old identities are not rewritten.
- Actual state: `references/shared-technical-model.md` explicitly preserves
  existing COMP/IF/INT/DS/EVENT/FLOW identity, revision, baseline, authority,
  and historical precision.
- Result: `stage_a_compatibility: PASS`.

## 2. Stage B projection lifecycle

- Prior invariant: PRJ identity, dependency direction, freshness states, RG
  regeneration, and package semantics retain their existing meanings.
- Stage F interaction: Service and Product-qualified Stage F views reuse PRJ,
  selector, dependency, lifecycle, and package contracts.
- Compatibility expectation: historical snapshots remain meaningful; changed
  dependencies become stale/blocked and regeneration remains explicit.
- Actual state: selectors carry definition revisions and snapshots; Product
  views consume existing PRJ identities and no automatic regeneration is
  specified.
- Result: `stage_b_compatibility: PASS`.

## 3. Stage C Test Engineering ownership and state

- Prior invariant: Test Engineering owns BC/CC/MAT/TM/GAP/TASK and existing CC
  status, classification, adjudication, and Contract Verification semantics.
- Stage F interaction: catalog-facing compatibility is a normalized view over
  exact CC state.
- Compatibility expectation: old CC records retain meaning; candidate matching
  and projections cannot adjudicate compatibility.
- Actual state: `CC-*` remains sole compatibility authority; missing Stage F
  qualifiers remain absent/unknown until bounded revalidation.
- Result: `stage_c_compatibility: PASS`.

## 4. Stage D Code Quality ownership

- Prior invariant: `CQ-*` and `CQRA-*` remain Code Quality-owned semantic
  records and interpretations.
- Stage F interaction: interface, integration, event, and data observations may
  coexist with code-quality scope.
- Compatibility expectation: Stage F facts do not become CQ findings or alter
  CQ ownership automatically.
- Actual state: authority maps keep Code Quality separate; Product and
  Technical Documentation are projections and do not write CQ records.
- Result: `stage_d_compatibility: PASS`.

## 5. Stage E Product invariants

- Prior invariant: Product is optional, distinct from Project and repository,
  and qualified by Product revision and exact baseline vector.
- Stage F interaction: Product views compose qualified Project-local IF/INT/DS/
  EVENT inputs and existing Service projections.
- Compatibility expectation: Project-local authority remains local; partial or
  unavailable members remain limited; single-project mode stays valid.
- Actual state: Product snapshots preserve Product baseline, Project/source
  bindings, local revisions, availability dimensions, and existing PRJ
  lifecycle; no permissions are granted by membership.
- Result: `stage_e_compatibility: PASS`.

## 6. Historical IF/DS/INT/EVENT facts

- Prior invariant: old facts remain valid even when they lack later optional
  Stage F qualifiers.
- Stage F interaction: operation, role, precision, resource, access, transport,
  external, and evidence fields are added only when supported.
- Compatibility expectation: broad HTTP IF, store-level DS, INT without
  access_mode, and EVENT without transport details remain valid.
- Actual state: the Stage F technical and projection contracts explicitly keep
  absent fields absent/unknown and preserve historical identity/revision.
- Pressure support: PS-F19 and PS-F20, with PS-F04 and PS-F15..PS-F16 covering
  unresolved/optional details.
- Result: `historical_fact_compatibility: PASS`.

## 7. Historical relation-only access

- Prior invariant: relation-only `READS_FROM` and `WRITES_TO` remain broad
  navigation facts.
- Stage F interaction: precise DATA_ACCESS INT becomes authoritative for new
  access and may derive navigation relations.
- Compatibility expectation: old relations gain no fabricated access mode,
  precision, or table target.
- Actual state: the STM, Technical Documentation selector, and data projection
  preserve relation-only records and distinguish them from INT-backed access.
- Pressure support: PS-F07..PS-F09 and PS-F20.
- Result: `historical_relation_compatibility: PASS`.

## 8. No silent defaults or bulk enrichment

- Prior invariant: absence is not false, exact, current, compatible, or empty
  state; accepted history is not rewritten by downstream consumers.
- Stage F interaction: optional fields and Product qualification are populated
  only by current accepted evidence and exact baseline binding.
- Compatibility expectation: no default role, view, precision, operation,
  resource, access, external identity, Product state, or compatibility result.
- Actual state: contracts preserve absent/unknown/bounded limitations and
  prohibit bulk enrichment, historical rewrite, automatic regeneration, and
  retroactive Product qualification.
- Result: `silent_defaults: 0`, `bulk_enrichment: NO`.

## 9. Product-free single-project flow

- Prior invariant: a Project outside a Product is a valid first-class review
  scope with existing STM, Evidence, Test Engineering, and documentation flow.
- Stage F interaction: Service interface, integration, data-access, evidence,
  and applicable Contract Verification paths are available without Product.
- Compatibility expectation: Product context is not required and no Product
  permission is implied.
- Actual state: `SKILL.md`, Technical Documentation, and Product contracts
  explicitly preserve Product-optional routing and single-project output.
- Pressure support: PS-F21.
- Result: `single_project: PASS`, `product_required: NO`.

## 10. Permissions and external actions

- Prior invariant: semantic scope and Product membership grant no repository,
  read, write, test, Git, or deployment permission.
- Stage F interaction: projections, selectors, scenarios, and Product views
  summarize accepted state only.
- Compatibility expectation: no new write/test/Git/deployment authority and no
  automatic external action is introduced.
- Actual state: Product and umbrella contracts keep authorization separate;
  Task 7–9 artifacts are static Markdown and introduce no runner, CI, push,
  regeneration, or deployment path.
- Result: `new_permissions: NO`.

## Backward-compatibility result

```text
stage_a_compatibility: PASS
stage_b_compatibility: PASS
stage_c_compatibility: PASS
stage_d_compatibility: PASS
stage_e_compatibility: PASS
historical_fact_compatibility: PASS
historical_relation_compatibility: PASS
silent_defaults: 0
bulk_enrichment: NO
single_project: PASS
product_required: NO
new_permissions: NO
migration: COMPATIBLE_EXTENSION
```

No prior-stage identity, authority, snapshot, or permission is rewritten.
