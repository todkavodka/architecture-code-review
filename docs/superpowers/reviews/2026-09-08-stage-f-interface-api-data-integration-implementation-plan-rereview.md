# Stage F — Interface, API & Data Integration Catalog
## Targeted Implementation Plan Re-Review

### Review metadata

- Repository: `/home/tod/skills/architecture-code-review`
- Branch: `main`
- Plan baseline: `ae31f1cc41b666bbcee963a6c27586206913747f`
- Published Design checkpoint: `9aff0356724b600bf539cbdce912de60d1ad977b`
- Review type: targeted independent re-review of IPR-F-001 and IPR-F-002
- Review date: 2026-09-08

### Scope

This review re-evaluates only the two findings from the original independent
Implementation Plan Review, their affected dimensions, the two ambiguous
fail-first scenarios, and bounded regressions in previously passing areas. The
Plan, original review, Design, Discovery, normative contracts, tests, and
roadmap were not modified during this re-review.

### Original findings

The original review recorded:

| Finding | Severity | Affected area | Required closure |
|---|---|---|---|
| IPR-F-001 | MEDIUM | External identity and sensitivity-class ownership | Exact external identity shape, exact sensitivity vocabulary, deterministic URL/DSN handling, safe evidence pointers, and explicit STM/evidence/rendering ownership with no new family. |
| IPR-F-002 | MEDIUM | Product projection lifecycle registration and mapping | Exact output-to-PRJ/selector mapping, Product-qualified snapshots and dependencies, V1–V4/fingerprint/revision/freshness, finite package membership, and no parallel lifecycle. |

The original review classified PF-15 (projection lifecycle registration) and
PF-17 (bounded Product impact registration) as `PLAN_AMBIGUOUS` because of
IPR-F-002. All other PF scenarios were `PLAN_PREVENTS`.

### IPR-F-001 validation

**Result: RESOLVED.**

The remediated Plan closes the finding with explicit ownership and exact
implementation scope:

- Section 4.1 assigns external identity qualification to the existing
  `COMP-*`, `IF-*`, `INT-*`, and `DS-*` STM families in
  `references/shared-technical-model.md`.
- Task 1 defines logical name, bounded external kind, exact source binding or
  limitation, evidenced provider/owner, and a safe non-secret identifier. It
  explicitly excludes credentials, tokens, passwords, private keys, and raw
  secret-bearing locators from STM fields.
- Task 2 assigns the exact classes `SECRET`, `SENSITIVE_INTERNAL`, and
  `SAFE_TECHNICAL_IDENTIFIER` to `references/shared-evidence-model.md`, with
  omission, pointer, alias/redaction, and safe-retention behavior specified.
- Task 3 assigns user-facing rendering rules to
  `references/technical-documentation.md`: `SECRET` is omitted,
  `SENSITIVE_INTERNAL` is redacted or replaced by a safe alias, and only
  permitted `SAFE_TECHNICAL_IDENTIFIER` values may be shown.
- Section 13.1 gives each affected path an owning task and validation.
  Section 13.2 maps external identity, sensitivity classes, and rendering to
  exact task/file/validation rows.
- Task 1, Task 2, and Task 3 verification explicitly checks source binding,
  non-secret STM fields, three-class vocabulary, redacted URL/DSN examples,
  useful evidence pointers, and safe projection rendering.

No implementation-time choice remains about identity family, sensitivity
classes, secret handling, or authority ownership. The remediation does not add
a new identity family or a second evidence/redaction lifecycle.

### IPR-F-002 validation

**Result: RESOLVED.**

The remediated Plan supplies the missing exact Product projection registration:

- Task 3 owns all edits to `references/technical-documentation.md` and maps
  Product Interface Catalog to existing
  `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` /
  `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` and selectors
  `SEL-TECH-DOC-02` / `SEL-TECH-DOC-03`.
- Product Integration Map uses existing
  `PRJ-TECH-DOC-04-INTEGRATIONS` / `SEL-TECH-DOC-04`.
- Product Data Access Map uses existing
  `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` / `SEL-TECH-DOC-05`.
- External Integrations Catalog is an external subsection of the existing
  integration projection, with `PRJ-TECH-DOC-07-AUTH-AND-TRUST` only when
  selected auth facts require it.
- Optional Provider/Consumer Matrix is explicitly a qualified view of existing
  interface/integration projections and never a new `PRJ-*` identity.
- Task 3 requires explicit selector revisions, Product identity/revision and
  immutable baseline, finite qualified Project/external inputs, exact local
  IDs/revisions, source bindings, limitations, dependency kinds, resolved
  snapshots, V1 STRUCTURAL, V2 DEPENDENCY/PROVENANCE, V3 CONTRACT COMPLETENESS,
  V4 AUTHORITY CONSISTENCY, canonical fingerprint, verified revision, and
  freshness.
- Task 3 maps finite membership to existing
  `PKG-TECHNICAL-DOCUMENTATION` conditions for sections 02/03, 04, and 05.
- Task 4 owns only Product qualification and cross-checks the Task 3 mapping;
  it explicitly prohibits a conditional second Technical Documentation edit,
  Product-specific PRJ identities, or a parallel lifecycle.
- Sections 13.1 and 13.2 make the path/task/validation and Design traceability
  explicit. Task 3 owns projection/package registration; Task 4 owns Product
  qualification and bounded impact.

PF-15 and PF-17 are now prevented by explicit Plan text and exact ownership,
not reviewer interpretation.

### Originally failing dimensions

| Dimension | Result |
|---|---|
| implementation_inventory | PASS |
| evidence_redaction_coverage | PASS |
| technical_documentation_coverage | PASS |
| package_integration | PASS |
| projection_lifecycle_integration | PASS |
| foundational_completeness | PASS |
| design_plan_traceability | PASS |
| fail_first_coverage | PASS |

### Corrected implementation inventory

The Plan's exact inventory is internally consistent:

- Plan tasks: 10
- Planned implementation commits: 9
- Semantic checkpoints: 4, plus the explicitly non-semantic CP1A ordering gate
- Existing files modified: 6
- New pressure scenarios: 26
- New integrated validation files: 2
- Other new files: 0
- Total expected implementation paths: 34
- Expected implementation diff: 6 modified + 28 added = 34 paths

The six existing paths are `SKILL.md`, the shared technical model, shared
evidence model, Technical Documentation contract, Product contract, and Test
Engineering contract. The 26 pressure paths are 154–179. The two integration
paths are the Stage F contract validation and backward-compatibility validation
artifacts. Section 13.1 assigns every path to exactly one task and validation.

Commit mapping remains coherent: Tasks 1–9 correspond to the nine planned
implementation commits; Task 10 is verification-only and normally adds no
commit. The four semantic checkpoints remain after Tasks 1–2, 3–4, 5–6, and
7–9.

### Design-to-Plan traceability

All affected Design decisions have exact task/file/validation mappings:

| Design requirement | Plan mapping | Result |
|---|---|---|
| External identity on existing STM families | Task 1 / `references/shared-technical-model.md` / external identity and no-new-family checks | PASS |
| Sensitivity classes and evidence pointers | Task 2 / `references/shared-evidence-model.md` / three classes, non-copy, redacted URL/DSN checks | PASS |
| Safe catalog rendering | Task 3 / `references/technical-documentation.md` / omission and alias/redaction checks | PASS |
| Product-qualified views | Task 4 / `references/product-multi-project-review.md` / Product revision, baseline, source binding, and bounded-impact checks | PASS |
| Existing PRJ/selector/package lifecycle | Task 3 / existing PRJ-TECH-DOC-02/03/04/05 and selectors / V1–V4, snapshots, fingerprint, freshness, package checks | PASS |
| Product lifecycle boundary | Task 4 cross-check / no new PRJ or parallel lifecycle validation | PASS |

No affected requirement uses “as needed”, “where applicable”, or an equivalent
implementation-time architecture decision.

### PF-01..PF-18

All scenarios are explicitly classified as `PLAN_PREVENTS`:

| Scenario | Prevention in the remediated Plan |
|---|---|
| PF-01 | Task 1 role/view matrix and invalid-combination handling |
| PF-02 | Task 1 INT authority and derived legacy relations |
| PF-03 | Task 1 DS callable identity and optional IF/INT boundary |
| PF-04 | Task 1 family-bounded precision and PS-F13 |
| PF-05 | Task 5 resolved CC mapping and PS-F26 |
| PF-06 | Task 4 qualified Project identity and Product baseline |
| PF-07 | Task 4 separate availability/coverage/freshness/package dimensions |
| PF-08 | Section 5 absent fields remain absent/unknown/inapplicable |
| PF-09 | Task 1 separates `OWNS_STATE` and `MIGRATION_AUTHORITY` |
| PF-10 | Task 1 separates runtime `MIGRATION` from authority relation |
| PF-11 | Tasks 2–3 exact sensitivity classes and deterministic redaction |
| PF-12 | Task 2 rejects config-only and unused-client hints |
| PF-13 | Task 1 preserves historical IF role omission |
| PF-14 | Task 1 preserves relation-only history without inferred INT |
| PF-15 | Task 3 exact PRJ/selector/package mapping and lifecycle fields; Task 4 cross-check |
| PF-16 | Tasks 3–4 and Task 9 preserve Product-free single-project behavior |
| PF-17 | Task 3 Product-qualified snapshots and Task 4 bounded impact validation |
| PF-18 | Section 9 isolated workspace gate |

Totals: `PF_total: 18`, `PF_prevents: 18`, `PF_ambiguous: 0`,
`PF_allows_failure: 0`.

### Pressure scenario inventory

The Plan retains exactly 26 Stage F scenarios, PS-F01 through PS-F26, mapped to
numeric repository paths `PS-154..PS-179`. The range is distinct from the
Stage E range through 149 and does not resurrect historical 150–153 artifacts.
Each numeric path appears once in the Plan's canonical allocation. Results:

- count: 26
- covered: 26
- partial: 0
- missing: 0
- semantic drift: 0
- numbering: PASS
- approved range: `PS-154..PS-179`

### Projection/package lifecycle

The corrected Plan reuses the current lifecycle rather than adding a Product
lifecycle. Each mapped existing `PRJ-*` retains owner, projection contract
revision, selector revision, dependency kind, resolved dependency snapshot,
V1–V4 verification, canonical fingerprint, verified revision, and freshness.
Product snapshots bind Product identity/revision/baseline and finite qualified
Project/external inputs. Package membership remains finite under
`PKG-TECHNICAL-DOCUMENTATION` and existing `ALL_SCOPED_CURRENT` behavior.

Results:

- `projection_lifecycle_integration: PASS`
- `package_integration: PASS`

### Evidence/redaction ownership

The Plan distinguishes the boundaries correctly:

- Shared Evidence stores observations, provenance pointers, source-support
  classes, and exact sensitivity classification.
- STM stores accepted non-secret external identity qualifications and safe
  technical identifiers, not raw credentials or secret-bearing locators.
- Evidence pointers can identify source location without copying secret values.
- Technical Documentation rendering applies the approved deterministic policy:
  omit `SECRET`, alias/redact `SENSITIVE_INTERNAL`, and show only permitted
  `SAFE_TECHNICAL_IDENTIFIER` values.
- Product qualification selects and scopes outputs; it does not become factual
  or redaction authority.
- Weak/config-only evidence remains unable to create accepted concrete
  interaction facts.

No duplicate redaction authority or projection-created STM fact is introduced.
Result: `evidence_redaction_coverage: PASS`.

### Technical Documentation coverage

Task 3 explicitly covers Service output for provided and consumed interfaces,
external integrations, events, data/resources, ownership, migration authority,
unresolved limitations, and evidence/provenance links. It explicitly maps all
approved Product outputs to existing PRJ/selector/package surfaces, including
the optional Provider/Consumer Matrix. Result:

`technical_documentation_coverage: PASS`.

### Migration assessment

The remediation is additive and does not alter migration strategy:

- `migration_assessment: PASS`
- `migration_classification: COMPATIBLE_EXTENSION`
- old IDs remain valid;
- no forced enrichment, fabricated defaults, destructive rewrite, or Product
  conversion is planned;
- historical IF, DS, INT, relation-only access, EVENT, CC, selector snapshots,
  and generated projections remain interpretable.

### Foundational completeness

The Plan now fixes authority ownership, identity family, STM family boundaries,
redaction ownership, Product projection authority, lifecycle/package reuse, and
migration classification. Foundational decisions are not deferred to
implementation.

- `foundational_open_questions: 0`
- `foundational_completeness: PASS`

### Bounded regression scan

The remediation does not regress previously passing areas:

| Dimension | Result |
|---|---|
| inventory_arithmetic | PASS |
| stm_contract_coverage | PASS |
| test_engineering_cc_boundary | PASS |
| selector_implementation_feasibility | PASS |
| stage_e_product_compatibility | PASS |
| historical_compatibility | PASS |
| task_ordering | PASS |
| task_atomicity | PASS |
| commit_boundary_quality | PASS |
| checkpoint_strategy | PASS |
| pressure_scenario_inventory | PASS |
| pressure_scenario_numbering | PASS |
| integrated_validation_quality | PASS |
| validation_proportionality | PASS |
| harness_decision_quality | PASS |
| workspace_and_git_discipline | PASS |
| roadmap_policy | PASS |
| permission_boundaries | PASS |
| scope_control | PASS |
| authority_boundaries | PASS |

The no-harness decision remains proportional: `DO_NOT_BUILD_HARNESS`.

### New findings

No new HIGH, MEDIUM, or LOW findings were identified. The remediation did not
introduce a new identity family, authority conflict, secret leakage path,
destructive migration, package lifecycle, selector grammar, or implementation
permission.

### Findings summary

| Category | Count |
|---|---:|
| Original findings resolved | 2 |
| New HIGH | 0 |
| New MEDIUM | 0 |
| New LOW | 0 |

finding_ids: `NONE`

### Plan checkpoint readiness

The Plan is internally consistent, semantically faithful to the approved Design,
and safe to checkpoint as the canonical base for the later isolated workspace
setup gate.

```text
IPR-F-001: RESOLVED
IPR-F-002: RESOLVED
implementation_inventory: PASS
evidence_redaction_coverage: PASS
technical_documentation_coverage: PASS
package_integration: PASS
projection_lifecycle_integration: PASS
foundational_completeness: PASS
design_plan_traceability: PASS
fail_first_coverage: PASS
PF_total: 18
PF_prevents: 18
PF_ambiguous: 0
PF_allows_failure: 0
pressure_scenarios: 26 covered, 0 partial, 0 missing, 0 semantic drift
migration: COMPATIBLE_EXTENSION
new_identity_family: NO
foundational_open_questions: 0
harness: DO_NOT_BUILD_HARNESS
plan_checkpoint_ready: YES
```

### Final verdict

`STAGE_F_IMPLEMENTATION_PLAN_APPROVED`

Recommended next gate: `STAGE_F_IMPLEMENTATION_PLAN_CHECKPOINT`.
