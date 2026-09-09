# Stage F integrated contract validation

## Validation scope and method

This artifact is a deterministic static validation of the accepted Stage F
contracts, their owning references, and pressure scenarios PS-F01 through
PS-F26. It is a validation projection, not a new semantic authority. Each
area records its governing contract, invariant, observed implementation,
scenario support, and a deterministic PASS criterion.

The integrated pressure inventory is `26/26 GREEN`: scenarios `154..166` map
one-to-one to PS-F01..PS-F13 and scenarios `167..179` map one-to-one to
PS-F14..PS-F26. No scenario is marked AMBIGUOUS.

## 1. Identity families

- Governing contract: `references/shared-technical-model.md`, sections 2, 6,
  and 10.
- Expected invariant: accepted facts remain in the existing `COMP-*`, `IF-*`,
  `INT-*`, `DS-*`, `EVENT-*`, `FLOW-*`, `AUTH-*`, `CFG-*`, and `ERR-*`
  families.
- Actual implemented state: Stage F extends IF/INT/DS/EVENT and controlled
  relations; no API, SQL, DB, catalog, Product-interface, Product-data, or
  integration-catalog factual family is defined.
- Pressure support: PS-F01..PS-F04, PS-F07..PS-F13, PS-F15..PS-F16, and
  PS-F22..PS-F26 preserve the existing identities.
- PASS criterion/result: no new authoritative factual family is present;
  `new_identity_family: NO` — **PASS**.

## 2. IF roles and observed views

- Governing contract: `references/shared-technical-model.md`, section 10.1.
- Expected invariant: `PROVIDER_DECLARATION`, `PROVIDER_IMPLEMENTATION`,
  `CONSUMER_EXPECTATION`, and `CONSUMER_OBSERVED_USE` remain perspective
  qualifiers with the controlled observed-view matrix.
- Actual implemented state: provider and consumer IFs remain independently
  addressable; invalid role/view combinations are rejected or unresolved, and
  historical IFs without `contract_role` retain their existing meaning.
- Pressure support: PS-F01..PS-F04, PS-F19, PS-F22, and PS-F24.
- PASS criterion/result: role/view applicability and identity separation are
  explicit, with no historical role defaulting — `if_role_matrix: PASS`,
  `provider_consumer_identity_separation: PASS`,
  `historical_role_defaulting: NO` — **PASS**.

## 3. Protocol-specific property boundary

- Governing contract: `references/shared-technical-model.md`, section 10.1.
- Expected invariant: protocol properties remain under the selected IF kind;
  unsupported or unobserved fields stay absent and do not create identities.
- Actual implemented state: HTTP, gRPC, GraphQL, WebSocket, webhook, CLI,
  library, file, IPC, and bounded `OTHER` properties are extensions of IF;
  broad historical IFs need not gain operation details.
- Pressure support: PS-F01, PS-F04, PS-F16, and PS-F19.
- PASS criterion/result: no protocol property is fabricated, and unknown
  operation precision is not `EXACT` — `protocol_property_boundary: PASS`.

## 4. INT concrete interaction authority

- Governing contract: `references/shared-technical-model.md`, sections 10.2
  and 10.4.
- Expected invariant: `INT-*` is the accepted concrete source-to-target
  interaction/access edge; precise new data access is authored by INT.
- Actual implemented state: INT carries interaction kind, target, access mode,
  precision, Project qualification, and evidence; IF, EVENT, DS, and relation
  identities remain separate.
- Pressure support: PS-F02, PS-F07..PS-F11, PS-F15, PS-F16, and PS-F24.
- PASS criterion/result: all six approved access modes can be represented on a
  DATA_ACCESS INT without converting the access fact into a relation-only
  record — `int_concrete_interaction_authority: PASS`.

## 5. INT navigation derivation

- Governing contract: `references/shared-technical-model.md`, section 10.4,
  and `references/technical-documentation.md`, Stage F data section.
- Expected invariant: READ may derive `READS_FROM`, WRITE may derive
  `WRITES_TO`, READ_WRITE may derive both; EXECUTE, DDL, and MIGRATION derive
  neither without separate evidence.
- Actual implemented state: navigation relations are derived/optional and
  explicitly linked to authoritative INT; selectors directly include precise
  DATA_ACCESS INT facts.
- Pressure support: PS-F07, PS-F08, PS-F09, PS-F10, PS-F13, and PS-F20.
- PASS criterion/result: derivation is mode-specific and does not require
  relation materialization — `int_navigation_derivation: PASS`.

## 6. Legacy relation-only compatibility

- Governing contract: `references/shared-technical-model.md`, section 10.4.
- Expected invariant: relation-only `READS_FROM`/`WRITES_TO` remains a broad
  historical fact with no fabricated access mode or precision.
- Actual implemented state: precise INT is authoritative for new access;
  contradiction routes to bounded revalidation and does not overwrite the
  historical relation.
- Pressure support: PS-F07..PS-F09, PS-F19, and PS-F20.
- PASS criterion/result: legacy relations remain selectable and broad while
  precise INT remains independently authoritative —
  `legacy_relation_compatibility: PASS`.

## 7. DS resource identity and parent/child rules

- Governing contract: `references/shared-technical-model.md`, section 10.3.
- Expected invariant: one `DS-*` family covers stores and addressable resources,
  including database/schema/table/view/procedure/function and approved resource
  kinds; parent containment is not semantic inheritance.
- Actual implemented state: `resource_kind`, `parent_resource_ref`, safe
  address, and precision are optional evidence-backed DS properties.
- Pressure support: PS-F07, PS-F11..PS-F14, PS-F20, and PS-F23.
- PASS criterion/result: containment does not imply access, ownership,
  migration authority, or dependency — `ds_resource_identity: PASS`,
  `ds_parent_child_non_inheritance: PASS`.

## 8. Database callable boundary

- Governing contract: `references/shared-technical-model.md`, section 10.5.
- Expected invariant: PROCEDURE/FUNCTION is a DS schema-object identity; an
  optional callable IF requires independent material evidence; EXECUTE INT
  targets DS and may reference that IF.
- Actual implemented state: DS, IF, and INT remain distinct and no callable
  identity family is introduced.
- Pressure support: PS-F07, PS-F11, and PS-F20.
- PASS criterion/result: DS-only execution and DS+IF execution are both valid
  without aliasing — `db_callable_boundary: PASS`.

## 9. Migration and ownership separation

- Governing contract: `references/shared-technical-model.md`, sections 10.4
  and 10.7, plus Product Technical Documentation contracts.
- Expected invariant: `OWNS_STATE`, `MIGRATION_AUTHORITY`, INT
  `access_mode=MIGRATION`, and DDL remain independent facts.
- Actual implemented state: each is separately qualified by owner/resource,
  operation, evidence, Project, revision, and baseline where applicable.
- Pressure support: PS-F08..PS-F10, PS-F20, and PS-F23.
- PASS criterion/result: no ownership, migration responsibility, DDL, or
  runtime operation is inferred from another —
  `migration_authority_separation: PASS`.

## 10. Precision applicability

- Governing contract: `references/shared-technical-model.md`, section 10.6.
- Expected invariant: the vocabulary is `EXACT`, `RESOURCE_BOUNDED`,
  `STORE_ONLY`, and `UNRESOLVED`; `STORE_ONLY` is limited to DS store facts and
  applicable DATA_ACCESS INT.
- Actual implemented state: IF/EVENT/FLOW/non-data INT exclude STORE_ONLY;
  bounded and unresolved values remain explicit and are not silently upgraded.
- Pressure support: PS-F04, PS-F11..PS-F13, PS-F19, and PS-F20.
- PASS criterion/result: family-specific applicability and no silent precision
  upgrade are enforced — `precision_applicability: PASS`.

## 11. Evidence support classes and weak-hint rejection

- Governing contract: `references/shared-evidence-model.md`, sections 7 and
  7.1–7.3.
- Expected invariant: `DIRECT_DECLARATION`, `STRONG_INFERENCE`, and `WEAK_HINT`
  are evidence metadata only; acceptance remains with the Technical Model Gate.
- Actual implemented state: weak hints route investigation or bounded
  unresolved observations but cannot create concrete IF, INT, DS child access,
  or EVENT facts alone.
- Pressure support: PS-F05, PS-F06, PS-F12, PS-F13, PS-F14, PS-F25, and PS-F26.
- PASS criterion/result: config URL, SDK dependency, DB connection, migration
  declaration, and unused client do not become concrete facts —
  `evidence_support_classes: PASS`, `weak_hint_rejection: PASS`.

## 12. Secret and sensitive safety

- Governing contract: `references/shared-evidence-model.md`, section 8, and
  `references/technical-documentation.md`, Stage F redaction section.
- Expected invariant: `SECRET` is omitted; `SENSITIVE_INTERNAL` is redacted or
  safely aliased; `SAFE_TECHNICAL_IDENTIFIER` renders only when permitted.
- Actual implemented state: safe pointers/logical facts may remain, while
  secret-bearing URLs, DSNs, credentials, tokens, passwords, keys, and private
  locators are excluded from accepted fields and output.
- Pressure support: PS-F17 and PS-F18.
- PASS criterion/result: no secret-bearing output path exists in evidence,
  STM, projections, fingerprints, summaries, or packages —
  `secret_output_path: NONE`, `redaction_contract: PASS`.

## 13. Technical Documentation selectors and package

- Governing contract: `references/technical-documentation.md`, registered
  projections and Stage F selector/package sections.
- Expected invariant: existing PRJ/SEL identities and current per-selector
  definition revisions are reused; selectors inspect formal STM fields only;
  DATA_ACCESS INT is selected directly; package authority remains
  `PKG-TECHNICAL-DOCUMENTATION`.
- Actual implemented state: SEL-02/03/04 are revision 2, SEL-05 is revision 3,
  and the data selector includes DS, DATA_ACCESS INT, and legacy relevant
  relations. Projection prose and filenames cannot accept facts.
- Pressure support: PS-F07, PS-F19..PS-F26.
- PASS criterion/result: selector and package behavior remain formal,
  revision-bound, derived, and explicitly regenerated —
  `technical_documentation_selectors: PASS`,
  `technical_documentation_package: PASS`,
  `projection_authority: DERIVED_ONLY`.

## 14. Product projection qualification and collisions

- Governing contract: `references/product-multi-project-review.md`, sections
  2, 5, 7, and Stage F Product-qualified views.
- Expected invariant: Product is optional and qualifies existing Service
  projections against an exact Product revision/baseline and Project/source
  revisions; equal local IDs do not alias.
- Actual implemented state: Product snapshots retain Product baseline, Project
  identity, local semantic ID/revision, selector revision, source bindings,
  availability dimensions, and existing PRJ lifecycle.
- Pressure support: PS-F22..PS-F24.
- PASS criterion/result: Product creates no factual family or lifecycle fork;
  collision prevention and qualification are explicit —
  `product_projection_qualification: PASS`,
  `product_collision_prevention: PASS`, `product_authority: DERIVED_ONLY`.

## 15. Product availability dimensions

- Governing contract: `references/product-multi-project-review.md`, sections 7
  and Stage F availability/lifecycle behavior.
- Expected invariant: source availability, review coverage, semantic
  availability, projection freshness, and package gate result remain separate.
- Actual implemented state: partial/unavailable Projects constrain affected
  Product views without being converted into clean, compatible, empty, or
  globally failed state.
- Pressure support: PS-F23 and PS-F24.
- PASS criterion/result: unavailable dependencies remain explicit and scoped;
  no dimension is flattened — `product_availability_dimensions: PASS`.

## 16. CC compatibility mapping and applicability

- Governing contract: `capabilities/test-review/references/test-engineering-contract.md`,
  Stage F compatibility boundary.
- Expected invariant: CC-* remains the sole compatibility authority; the
  automatic gate applies to materially relevant declared external contracts;
  normalized display is derived from exact qualified pair and final CC state.
- Actual implemented state: `COMPATIBLE` and `INCOMPATIBLE` require resolved
  valid accepted adjudication; missing, stale, unresolved, or non-final state
  is `INDETERMINATE`; `NOT_COMPARABLE` is only the no-valid-pair case.
- Pressure support: PS-F03, PS-F22, PS-F24, PS-F26.
- PASS criterion/result: authority, applicability, and mapping remain CC-owned
  — `cc_authority: PASS`, `automatic_contract_verification: PASS`.

## 17. Candidate matching boundary and missing data

- Governing contract: Test Engineering Stage F compatibility boundary.
- Expected invariant: `MATCH_CANDIDATE`, `NO_MATCH_ESTABLISHED`, and
  `MATCHING_INDETERMINATE` are non-authoritative; missing data never means
  `COMPATIBLE`.
- Actual implemented state: candidate/no-match context is distinct from CC
  adjudication; old CC for another exact revision cannot prove current result.
- Pressure support: PS-F03, PS-F22, PS-F24, PS-F25, and PS-F26.
- PASS criterion/result: no candidate, no-match, or unresolved state is mapped
  to a false compatibility outcome — `candidate_matching_boundary: PASS`,
  `missing_data_not_compatible: PASS`.

## 18. Stage B projection lifecycle and package reuse

- Governing contract: `references/projection-dependencies.md`,
  `references/projection-lifecycle.md`, Technical Documentation, and Product
  contracts.
- Expected invariant: existing PRJ/RG lifecycle, `SEMANTIC_EXACT`,
  `SEMANTIC_SELECTOR`, `PROJECTION_EXACT`, selector snapshots, V1–V4,
  fingerprints, and CURRENT/STALE/BLOCKED states are reused.
- Actual implemented state: Product views consume existing Service PRJ/SEL
  identities and explicit dependency snapshots; regeneration remains RG-owned
  and explicit.
- Pressure support: PS-F19, PS-F22..PS-F24.
- PASS criterion/result: no Stage F or Product lifecycle fork and no automatic
  regeneration are introduced — `projection_lifecycle_reuse: PASS`,
  `package_authority: PASS`, `automatic_regeneration: NO`.

## 19. Bounded REVALIDATE and dependency direction

- Governing contract: `references/projection-dependencies.md`, sections 2–6,
  and Product `REVALIDATE`/impact sections.
- Expected invariant: dependencies point from consumer to prerequisite; reverse
  indexes and relations are navigation only; source changes affect bounded
  dependent slices.
- Actual implemented state: changed Project/source/fact/selector membership
  marks affected projections stale or blocked and routes unknown linkage to
  bounded investigation, not full reread or regeneration.
- Pressure support: PS-F19, PS-F22..PS-F24.
- PASS criterion/result: dependency direction and bounded impact are explicit;
  `dependency_direction: PASS`, `bounded_revalidate: PASS`.

## 20. Cross-capability authority

- Governing contract: `SKILL.md`, shared evidence/STM contracts, Test
  Engineering, Product, Technical Documentation, and Code Quality ownership
  maps.
- Expected invariant: WS/EV owns evidence, STM owns accepted technical facts,
  Architecture Review owns RF interpretation, Test Engineering owns BC/CC/
  MAT/TM/GAP/TASK, Code Quality owns CQ/CQRA, Technical Documentation owns
  derived PRJ views, and Product owns qualification/composition only.
- Actual implemented state: no Stage F projection, Product view, selector,
  scenario, or umbrella route transfers ownership or creates a competing truth.
- Pressure support: all PS-F01..PS-F26; authority boundaries are explicit in
  every scenario’s GREEN criteria.
- PASS criterion/result: `authority_conflicts: 0`, `ownership_transfer: NO` —
  **PASS**.

## Integrated result

```text
pressure_scenarios: 26/26 GREEN
integrated_contract_validation: PASS
new_identity_family: NO
migration: COMPATIBLE_EXTENSION
single_project: PASS
stage_e_product: PASS
authority_conflicts: 0
```

No harness, runner, parser, registry generator, or new dependency is required
for this deterministic static validation.
