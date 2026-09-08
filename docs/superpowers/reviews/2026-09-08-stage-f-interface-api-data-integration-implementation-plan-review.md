# Stage F — Interface, API & Data Integration Catalog
## Independent Implementation Plan Review

### Review metadata

| Field | Value |
|---|---|
| Repository | `/home/tod/skills/architecture-code-review` |
| Branch | `main` |
| Plan baseline | `ae31f1cc41b666bbcee963a6c27586206913747f` |
| Design checkpoint | `9aff0356724b600bf539cbdce912de60d1ad977b` |
| Plan | `docs/superpowers/plans/2026-09-08-stage-f-interface-api-data-integration-implementation-plan.md` |
| Review type | Independent Implementation Plan Review only |
| Review date | 2026-09-08 |

### Scope

This review compares the published Plan with the approved Discovery, Design,
both Design reviews, and current repository contracts. It does not implement
or remediate the Plan and creates no branch, worktree, commit, or publication.
The approved Design is semantic authority; the Plan may decide only bounded
mechanical details already permitted by that Design.

### Published baseline verification

Branch is `main`; local `HEAD` and `origin/main` are both
`ae31f1cc41b666bbcee963a6c27586206913747f`; the Plan parent is
`9aff0356724b600bf539cbdce912de60d1ad977b`; Design ancestry passed; tracked
state was clean. The local branch was fast-forwarded by exactly one commit,
`ae31f1c docs: add Stage F implementation plan`. The four historical
untracked files were preserved.

### Plan inventory extracted

The actual Plan states: `plan_tasks: 10`,
`implementation_commits_expected: 9`, `semantic_checkpoints: 4`,
`modified_existing_files_expected: 6`, `new_pressure_scenarios: 26`,
`new_integrated_validation_files: 2`, `expected_changed_paths: 34`,
branch `feature/stage-f-interface-api-data-integration-catalog`, worktree
`../architecture-code-review-stage-f-interface-api-data-integration-catalog`,
`harness: DO_NOT_BUILD_HARNESS`, and read-only roadmap during implementation.

Existing paths are exactly:

- `SKILL.md`;
- `references/shared-technical-model.md`;
- `references/shared-evidence-model.md`;
- `references/technical-documentation.md`;
- `references/product-multi-project-review.md`;
- `capabilities/test-review/references/test-engineering-contract.md`.

New paths are 26 pressure scenarios `tests/pressure-scenario-154-*.md` through
`tests/pressure-scenario-179-*.md`, plus
`tests/stage-f-interface-api-data-integration-contract-validation.md` and
`tests/stage-f-interface-api-data-integration-backward-compatibility.md`.
The arithmetic `6 + 26 + 2 = 34` is correct. Task 4 conditionally repeats
`technical-documentation.md`, but the final inventory counts it once.

The nine commits are six contract/orchestration commits, two pressure-scenario
commits, and one integrated-validation commit. Task 10 is verification-only.
The main checkpoints are CP1 semantic/evidence core, CP2 projections/Product,
CP3 CC/orchestration, and CP4 integrated validation; CP1A is the Task 1 gate.

### Repository contracts inspected

The complete current versions inspected were `SKILL.md`,
`references/shared-evidence-model.md`, `references/shared-technical-model.md`,
`references/technical-model-dependencies.md`,
`references/revalidation-and-freshness.md`, `references/projection-lifecycle.md`,
`references/projection-dependencies.md`,
`references/projection-gates-and-packages.md`,
`references/technical-documentation.md`,
`references/product-multi-project-review.md`,
`capabilities/test-review/references/test-engineering-contract.md`, and
`references/evidence-and-severity.md`, plus current Stage A–E validation and
pressure-scenario contracts. The complete Discovery, Discovery Review, Design,
original Design Review, targeted Design Re-Review, and Plan were also read.

The Design remains `STAGE_F_DESIGN_APPROVED`, direction B,
`COMPATIBLE_EXTENSION`, no new identity family, and zero foundational open
questions. The targeted review resolves DRF-001..DRF-005 and records 26/26 and
15/15 GREEN with no new findings.

### Design-to-plan traceability

| Design item | Plan coverage | Result |
|---|---|---|
| IF/protocol/role-view/observed-view semantics | Task 1 | PASS |
| Provider/consumer matching and EVENT boundary | Tasks 1, 3, 5, 7, 9 | PASS |
| INT authority and READ/WRITE derivation | Tasks 1, 7, 9 | PASS |
| DS children, callable boundary, SQL/non-SQL | Tasks 1, 7, 9 | PASS |
| Migration authority and precision | Tasks 1, 3, 9 | PASS |
| Evidence strength and weak hints | Tasks 2, 7, 9 | PASS |
| External identity and exact sensitivity classes | Tasks 3–4, but no owning STM/evidence shape | FINDING IPR-F-001 |
| CC mapping and ownership | Tasks 5, 9 | PASS |
| Service projections | Task 3 | PASS |
| Product projections/lifecycle/package registration | Task 4 by reuse prose, no exact mapping | FINDING IPR-F-002 |
| Bounded REVALIDATE, single-project, historical rules | Sections 5, 9; Tasks 1–6, 9 | PASS |
| Identity/revision semantics | Task 1 | PASS |

### Implementation inventory review

`references/shared-technical-model.md` is REQUIRED: it owns IF/INT/DS facts,
relations, precision, identity, and historical meaning. `references/shared-
evidence-model.md` is JUSTIFIED for shared WS/EV source-support and safe
excerpt rules, provided it does not redefine confidence/severity.
`references/technical-documentation.md` and
`references/product-multi-project-review.md` are REQUIRED for capability-owned
Service/Product projections. The Test Engineering contract is REQUIRED for
the CC mapping. `SKILL.md` is JUSTIFIED only for a small reference-driven
orchestration route.

`references/technical-model-dependencies.md`,
`references/projection-dependencies.md`, `references/projection-lifecycle.md`,
and `references/projection-gates-and-packages.md` are correctly treated as
reuse contracts: their existing typed dependency, selector, snapshot, V1–V4,
fingerprint, freshness, and finite package rules are sufficient if Task 3/4
register Stage F outputs explicitly. No Architecture Review or additional Test
Engineering file is missing from the current inventory.

`implementation_inventory: FINDINGS` because the exact external/redaction
owner and Product projection registration are not closed by the Plan.

### STM implementation coverage

Task 1 covers IF direction/kind/role/properties, the closed role/view matrix,
INT source/target/kinds/access, DS store/child resources and procedure/function
identity, `MIGRATION_AUTHORITY`, INT-backed `READS_FROM`/`WRITES_TO`,
`READ_WRITE`, legacy relations, precision applicability, and identity/history.
It preserves the Technical Model Gate and forbids a new identity family.

`stm_contract_coverage: PASS`.

### Evidence / redaction coverage

Task 2 correctly preserves WS/EV ownership and adds
`DIRECT_DECLARATION`, `STRONG_INFERENCE`, and `WEAK_HINT` as source-support
classes rather than lifecycle or confidence replacements. It covers weak-hint
prohibitions, dynamic limitations, baseline bindings, safe pointers, and
secret-bearing URL/DSN handling.

It does not name the approved exact vocabulary `SECRET`,
`SENSITIVE_INTERNAL`, `SAFE_TECHNICAL_IDENTIFIER`, nor assign the Design's
`external_identity` fields (logical name, bounded kind, source binding,
provider/owner, safe identifier) to an owner. This leaves material choices
open. `evidence_redaction_coverage: FINDINGS` via IPR-F-001.

### Test Engineering / CC boundary

Task 5 preserves automatic Contract Verification, `CC-*` ownership, existing
status/classification/adjudication, exact provider/consumer revisions,
Project/Product qualification, candidate matching as non-authoritative, and
the approved mapping: resolved accepted CC acceptance gives `COMPATIBLE`;
resolved material mismatch gives `INCOMPATIBLE`; absent/unresolved/non-final
state gives `INDETERMINATE`; no valid pair and no CC comparison gives
`NOT_COMPARABLE`. No catalog-owned compatibility authority is introduced.

`test_engineering_cc_boundary: PASS`.

### Technical Documentation implementation

Task 3 correctly preserves existing `PRJ-TECH-DOC-00..09` identities and
extends formal selectors/content for interfaces, integrations/events, data,
ownership, migration, evidence, limitations, and redaction. The task does not
create a parallel lifecycle. Its Product implementation depends on IPR-F-002.

`technical_documentation_coverage: FINDINGS`.

### Selector feasibility

Current selectors allow `structured_properties` and `formal_relations` with
bounded `=`, `IN`, and `HAS_ANY` operators. Direction, resource kind,
interaction kind, access mode, precision, and `MIGRATION_AUTHORITY` are
expressible there once the relation is added to STM. Product qualification must
remain the existing finite Product-qualified snapshot, not an open-ended query.

`selector_implementation_feasibility: PASS`.

### Package integration

`PKG-TECHNICAL-DOCUMENTATION` already defines explicit required/conditional
`PRJ-TECH-DOC-*` membership and `ALL_SCOPED_CURRENT`. Product scope reuses this
package and qualified snapshots. The mechanics are feasible, but the Plan does
not specify exact Product output-to-projection mapping or finite conditions.

`package_integration: FINDINGS` via IPR-F-002.

### Projection lifecycle integration

The current lifecycle requires stable PRJ identity, owner, contract revision,
semantic exact/selector and upstream dependencies, frozen resolution snapshot,
V1–V4, canonical fingerprint, verified revision, and freshness. Product scope
also requires Product identity/revision/baseline and qualified inputs.

Tasks 3–4 say to reuse these rules but do not identify which existing
`PRJ-TECH-DOC-*` identity carries Product Interface Catalog, Product Integration
Map, Product Data Access Map, External Integrations Catalog, or optional
Provider/Consumer Matrix, nor their selectors, snapshots, or package members.
`projection_lifecycle_integration: FINDINGS` via IPR-F-002.

### Product integration

Task 4 preserves Product optionality, single-project behavior, immutable
baseline vectors, Project-local STM authority, qualified cross-project
identity, external limitations, separate availability/coverage/freshness/
package dimensions, bounded REVALIDATE, additive EXTEND, and derived outputs.

`stage_e_product_compatibility: PASS`.

### Historical compatibility

Section 5 preserves old IF/DS/INT/EVENT/relation/CC/selector records without ID
rewrite, forced enrichment, fabricated defaults, Product conversion, or
destructive migration. Absent Stage F fields remain absent/unknown/inapplicable.

`historical_compatibility: PASS`.

### Task ordering

The order is correct: STM/evidence, Service/Product projections, CC/orchestration,
pressure scenarios, integrated/backward validation, then final verification.

`task_ordering: PASS`.

### Task atomicity

Tasks are bounded and coherent. Task 1 is appropriately broad as one STM
authority extension; Service and Product are separated; pressure scenarios are
split into two reviewable batches; Task 10 is verification-only.

`task_atomicity: PASS`.

### Commit boundaries

The nine commit subjects have coherent purposes and the four checkpoints are
semantic verification boundaries rather than label-only commits. No intended
commit creates a second factual authority.

`commit_boundary_quality: PASS`.

### Semantic checkpoints

CP1A/CP1 establish STM/evidence, CP2 establishes projections/Product, CP3
establishes CC/orchestration, and CP4 establishes pressure/integrated
validation. `checkpoint_strategy: PASS`.

### Pressure-scenario inventory

The Plan maps each approved scenario exactly once: PS-F01..PS-F13 to exact
files 154..166 in Task 7 and PS-F14..PS-F26 to exact files 167..179 in Task 8.
The filename list in section 4.3 gives every basename. All 26 are COVERED;
there are 0 PARTIAL, 0 MISSING, 0 unintended duplicates, and 0 semantic drift.
The required fields correspond to the repository's established six-field
scenario contract. `pressure_scenario_inventory: PASS`.

### Pressure-scenario numbering

Current Stage E files end at 149. The proposed 154..179 range is unused; the
historical experimental 150..153 paths are absent and are not resurrected.
`pressure_scenario_numbering: PASS`; approved range: `PS-154..PS-179`.

### Integrated validation

The two planned validation files are complementary: one covers joint
IF/INT/DS/EVENT, evidence, redaction, selectors/packages, CC, lifecycle, and
authority; the other covers Stage A–E ownership, historical records/relations/
CC, Product-free operation, and permissions. They are SUFFICIENT and not
redundant, assuming they retain the repository's deterministic static-contract
record style.

`integrated_validation_quality: PASS`.

### Harness / validation proportionality

This is a Markdown contract repository with no coordinator/runtime. Targeted
inspection, pressure scenarios, and two integrated records are proportional.
`harness_decision: DO_NOT_BUILD_HARNESS` and
`validation_proportionality: PASS`.

### Workspace / Git discipline

The Plan requires the approved Plan checkpoint before creating the isolated
branch/worktree, names the exact branch/worktree, preserves unrelated
untracked files in main, and forbids implementation on main.

`workspace_and_git_discipline: PASS`.

### Roadmap / permission boundaries

The roadmap is read-only during implementation. Push, PR, merge, tag, release,
deploy, reset, rebase, force operations, and unrelated cleanup are prohibited.
`roadmap_policy: PASS`; `permission_boundaries: PASS`.

### Fail-first scenarios PF-01..PF-18

PF-01, PF-02, PF-03, PF-04, PF-05, PF-06, PF-07, PF-08, PF-09, PF-10, PF-11,
PF-12, PF-13, PF-14, PF-16, and PF-18 are `PLAN_PREVENTS` through Tasks 1–5,
the migration section, or the workspace gate. PF-15 (projection lifecycle
registration) and PF-17 (bounded Product impact registration) are
`PLAN_AMBIGUOUS` because of IPR-F-002. No case is `PLAN_ALLOWS_FAILURE`.

`PF_total: 18`; `PF_prevents: 16`; `PF_ambiguous: 2`;
`PF_allows_failure: 0`; `fail_first_coverage: FINDINGS`.

### Scope control

The Plan excludes live DB scanning/introspection, traffic capture, tracing,
mesh/gateway, schema-registry replacement, OpenAPI generation, full SQL/ORM
frameworks, CMDB/graph/RAG/runtime services, automatic compatibility/RF
generation, and automatic projection regeneration.

`scope_control: PASS`.

### Authority boundaries

WS/EV remain evidence; STM facts remain Technical Model authority; IF, INT, DS,
EVENT, and FLOW retain their distinct meanings; CC remains Test Engineering;
RF remains Architecture; CQ/CQRA remain Code Quality; BC/MAT/TM/GAP/TASK
remain Test Engineering; PRJ/RG remain projection lifecycle. Product/catalog
outputs are derived only. `authority_boundaries: PASS`.

### Findings

#### IPR-F-001 — External identity and sensitivity-class ownership is not closed

**Severity:** MEDIUM
**Plan sections/tasks:** 4.1, Task 1, Task 2, Task 3, Task 4
**Targeted re-review:** Yes.

The approved Design sections 21–22 require an `external_identity` with logical
name, bounded kind, source binding, provider/owner, and safe identifier, plus
the exact classes `SECRET`, `SENSITIVE_INTERNAL`, and
`SAFE_TECHNICAL_IDENTIFIER`. The current STM has no external identity shape;
the Shared Evidence contract defines observations and optional short excerpts,
but not these Stage F classes.

Task 1 does not specify the external identity record. Task 2 uses general safe
alias/redaction language and secret-bearing URL/DSN rules but does not require
the exact classes or distinguish safe STM fields from render-time transforms.

Failure scenario: implementers represent a private host, DSN, or provider
differently across STM, evidence, Service docs, and Product output, or copy a
credential-bearing value into an evidence excerpt while still claiming Plan
conformance.

Required remediation: assign the exact external identity shape and sensitivity
vocabulary to owning contracts; specify deterministic omission/redaction, safe
URL/DSN handling, and evidence-pointer behavior. No new family is required.

#### IPR-F-002 — Product projection lifecycle registration and mapping is underspecified

**Severity:** MEDIUM
**Plan sections/tasks:** 4.1, Task 3, Task 4, Sections 8 and 13
**Targeted re-review:** Yes.

Current Technical Documentation registers stable `PRJ-TECH-DOC-00..09`
identities, selector IDs and revisions, `SEMANTIC_EXACT`/
`SEMANTIC_SELECTOR` dependencies, frozen snapshots, and finite package
membership under `ALL_SCOPED_CURRENT`. Projection contracts also require
Product-qualified identity/revision/baseline, V1–V4, fingerprint, verified
revision, and freshness.

Task 4 names Product Interface Catalog, Product Integration Map, Product Data
Access Map, External Integrations Catalog, and optional Provider/Consumer
Matrix, but does not map them to existing PRJ identities/sections or specify
selector revisions, Product-qualified snapshots, dependency kinds, or finite
package conditions. The conditional second Technical Documentation edit makes
the boundary less precise.

Failure scenario: an implementer adds Product prose or new PRJ IDs without
package/dependency registration, or creates a selector without a Product
baseline-qualified snapshot. The output cannot be proven CURRENT and bounded
provider impact may stale too much, too little, or nothing.

Required remediation: add an exact mapping table for every named Product output
to an existing PRJ section, or explicitly define a new stable identity with
owner/package registration. Specify selector and contract revisions, Product
identity/revision/baseline, qualified inputs, dependency kinds/snapshots,
V1–V4, fingerprint/revision/freshness, and finite membership. Prohibit a
parallel Product projection lifecycle.

### Findings summary

| Severity | Count |
|---|---:|
| HIGH | 0 |
| MEDIUM | 2 |
| LOW | 0 |

finding_ids: `IPR-F-001`, `IPR-F-002`

### Review dimensions

| Dimension | Result |
|---|---|
| baseline_integrity | PASS |
| plan_scope_integrity | PASS |
| implementation_inventory | FINDINGS |
| inventory_arithmetic | PASS |
| stm_contract_coverage | PASS |
| evidence_redaction_coverage | FINDINGS |
| test_engineering_cc_boundary | PASS |
| technical_documentation_coverage | FINDINGS |
| selector_implementation_feasibility | PASS |
| package_integration | FINDINGS |
| projection_lifecycle_integration | FINDINGS |
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
| foundational_completeness | FINDINGS |
| design_plan_traceability | FINDINGS |
| scope_control | PASS |
| authority_boundaries | PASS |
| fail_first_coverage | FINDINGS |

### Recommended next gate

`STAGE_F_IMPLEMENTATION_PLAN_REMEDIATION`

The two MEDIUM findings are plan-closure defects, not a request for a new
architecture direction, identity family, migration class, or implementation
scope. Targeted independent plan re-review is sufficient after remediation.

### Final verdict

```text
HIGH: 0
MEDIUM: 2
LOW: 0
pressure_scenarios: 26 COVERED / 0 PARTIAL / 0 MISSING
approved_pressure_range: PS-154..PS-179
migration: COMPATIBLE_EXTENSION
new_identity_family: NO
foundational_open_questions: 0 in approved Design; 2 plan findings remain
harness: DO_NOT_BUILD_HARNESS
single_project_compatibility: PRESERVED
stage_e_compatibility: PRESERVED
CC_ownership: PRESERVED
projection_package_lifecycle: INCOMPLETE_IN_PLAN
verdict: STAGE_F_IMPLEMENTATION_PLAN_REVIEW_FINDINGS
```

The Plan is not approved for checkpointing until IPR-F-001 and IPR-F-002 are
remediated and independently re-reviewed. No implementation, commit, push,
merge, PR, tag, release, deployment, branch, or worktree was created by this
review.
