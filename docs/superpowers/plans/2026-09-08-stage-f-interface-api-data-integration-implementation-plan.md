# Stage F — Interface, API & Data Integration Catalog
## Implementation Plan

## 1. Plan metadata

| Field | Value |
|---|---|
| Repository | `todkavodka/architecture-code-review` |
| Canonical branch at plan authoring | `main` |
| Published Design baseline | `9aff0356724b600bf539cbdce912de60d1ad977b` |
| Approved Discovery checkpoint | `9d5c09b6e1dc2686d640e66b1760dcd47640ef42` |
| Approved Design | `docs/superpowers/specs/2026-09-08-stage-f-interface-api-data-integration-design.md` |
| Original Design Review | `docs/superpowers/reviews/2026-09-08-stage-f-interface-api-data-integration-design-review.md` |
| Targeted Design Re-Review | `docs/superpowers/reviews/2026-09-08-stage-f-interface-api-data-integration-design-rereview.md` |
| Design verdict | `STAGE_F_DESIGN_APPROVED` |
| Architecture direction | `OPTION B — Extend existing STM contracts` |
| Migration | `COMPATIBLE_EXTENSION` |
| New identity family | `NO` |
| Implementation branch | `feature/stage-f-interface-api-data-integration-catalog` |
| Implementation worktree | `../architecture-code-review-stage-f-interface-api-data-integration-catalog` |
| Harness decision | `DO_NOT_BUILD_HARNESS` |

This document is the implementation plan only. It does not authorize implementation until this plan has passed an independent implementation-plan review and the approved plan checkpoint/workspace gates.

---

## 2. Mission

Implement the approved Stage F Design so the review suite can represent and project, with exact evidence and bounded uncertainty:

- interfaces/APIs provided by a service;
- interfaces/APIs consumed or expected by a service;
- concrete internal/external integration edges;
- events produced and consumed;
- data stores and addressable data resources;
- SQL and non-SQL access modes;
- state ownership and migration authority;
- provider/consumer contract consistency through existing Test Engineering `CC-*` authority;
- Service-level user-facing API/integration/data catalogs;
- Product-level interface/integration/data-access projections;
- safe redaction of secrets and sensitive internal identifiers.

The implementation must preserve the approved authority model:

```text
WS-* / EV-*                         evidence/provenance
STM Technical Model Gate            accepted technical facts
COMP-*                              component/system identity
IF-*                                interaction surface / contract
INT-*                               concrete interaction/access edge
DS-*                                store/addressable data resource
EVENT-*                             semantic event/message
FLOW-*                              material system/business/control flow
AUTH-* / CFG-* / ERR-*              existing specialized factual concerns
CC-*                                Test Engineering Contract Consistency authority
RF-*                                Architecture Review interpretation/findings
CQ-* / CQRA-*                       Code Quality authority
BC/MAT/TM/GAP/TASK                  Test Engineering authority
PRJ-* / RG-*                        projection/regeneration lifecycle
```

No Stage F catalog becomes factual authority.

---

## 3. Non-negotiable Design decisions

Implementation must encode, not reopen, the following approved decisions.

1. `Catalog != factual authority`.
2. `IF-* != INT-* != DS-* != EVENT-* != FLOW-*`.
3. Provider declaration and consumer expectation remain separately addressable accepted facts.
4. A consumer expectation may exist without a matched provider.
5. `INT-*` is the authority for new precise concrete interaction/data-access edges.
6. `READS_FROM` / `WRITES_TO` are derived/navigation relations for new precise INT-backed access; legacy relation-only facts remain broad historical facts.
7. One `DS-*` family represents stores and addressable child resources; no `TABLE-*`, `SQL-*`, `DB-*`, `API-*`, or Product-specific factual family is introduced.
8. Database `PROCEDURE` / `FUNCTION` DS object identity is distinct from an optional independently material callable `IF-*` contract; invocation is `INT-* access_mode=EXECUTE`.
9. `MIGRATION` access is not `MIGRATION_AUTHORITY`.
10. `MIGRATION_AUTHORITY` is an additive controlled STM factual relation for schema/data-resource evolution responsibility.
11. Precision is distinct from confidence, coverage, freshness, observed view, and lifecycle.
12. `STORE_ONLY` applies only to DS and DATA_ACCESS INT facts with known store context; it is invalid for IF/EVENT/FLOW/non-data INT.
13. Weak hints cannot alone create accepted concrete interaction facts.
14. Candidate matching is not compatibility and never aliases provider/consumer identities.
15. When a materially relevant declared external contract exists, Contract Verification is automatic under the existing Test Engineering applicability rule.
16. `CC-*` remains Test Engineering authority. Stage F only provides a normalized catalog-facing compatibility view over accepted/current CC state.
17. Missing required comparison data never means `COMPATIBLE`.
18. Secret values never appear in STM catalog-safe fields, copied evidence excerpts, generated catalogs, projection metadata, or package summaries.
19. Product remains optional; single-project operation remains first-class.
20. Historical broad facts remain valid; no silent precision upgrade or destructive rewrite.
21. Stage B projection/package lifecycle is reused; no automatic regeneration.
22. REVALIDATE remains impact-driven and bounded.

If implementation pressure reveals a need to change one of these decisions, stop with `STAGE_F_DESIGN_DRIFT_DETECTED`; do not resolve it inside implementation.

---

## 4. Canonical implementation inventory

### 4.1 Existing normative files expected to change

The approved implementation should be bounded to these existing contract surfaces unless independent plan review proves another file is required:

1. `references/shared-technical-model.md`
   - IF common/protocol properties;
   - provider/consumer roles;
   - INT interaction/access semantics;
   - DS resource kinds and parent/child addressing;
   - access modes;
   - precision applicability;
   - `MIGRATION_AUTHORITY`;
   - new-vs-legacy `READS_FROM` / `WRITES_TO` authority and derivation rules;
   - DB callable DS/IF/INT boundary;
   - identity/revision/backward-compatibility rules.

2. `references/shared-evidence-model.md`
   - safe evidence-excerpt rule for Stage F technical identifiers;
   - interaction evidence-source classification binding without replacing global confidence/severity semantics;
   - unresolved/dynamic evidence limitation recording;
   - secret/sensitive value non-copy rules at shared evidence boundary.

3. `references/technical-documentation.md`
   - Stage F selector dimensions/predicates;
   - provided/consumed operation-level content;
   - integrations/external integrations;
   - events;
   - data entity access, ownership, migration authority;
   - unknown/unresolved sections;
   - safe redaction behavior;
   - Product Interface Catalog / Integration Map / Data Access Map / External Integrations Catalog projection registration or explicit reuse mapping;
   - package membership/conditions without a second lifecycle.

4. `references/product-multi-project-review.md`
   - qualified cross-project IF/INT/DS Stage F semantics;
   - provider/consumer identity collision prevention;
   - exact Product-baseline-qualified data ownership/access/migration views;
   - Product projection definitions and partial/unavailable Project behavior;
   - no Product factual authority.

5. `capabilities/test-review/references/test-engineering-contract.md`
   - exact Stage F normalized compatibility mapping to existing `CC-*` state/classification/adjudication;
   - automatic applicability rule reuse;
   - candidate/not-evaluated display semantics when no valid CC comparison exists;
   - exact provider/consumer revision inputs;
   - no second compatibility truth model.

6. `SKILL.md`
   - bounded orchestration instructions so Stage F facts are actually gathered/reused during STM construction and Technical Documentation output;
   - safe routing to Contract Verification for materially relevant contracts;
   - Stage F catalog semantics remain reference-driven, not duplicated in prose;
   - no change to Architecture/Test/CQ ownership.

### 4.2 Existing files expected to remain unchanged unless plan review proves necessity

These are dependencies to validate, not default modification targets:

- `references/evidence-and-severity.md` — existing confidence/severity evidence semantics remain authoritative; Stage F source classes must not redefine them.
- `references/technical-model-dependencies.md` — relation/dependency distinction and impact semantics should be reused.
- `references/revalidation-and-freshness.md` — bounded revalidation should be reused.
- `references/projection-lifecycle.md` — `PRJ-*`, `RG-*`, V1–V4, freshness meaning remain unchanged.
- `references/projection-dependencies.md` — existing exact/selector dependency model should be reused.
- `references/projection-gates-and-packages.md` — existing package policies should be reused.
- Architecture Review/CQ capability contracts — consumers of Stage F facts, not owners of the Stage F implementation.

If implementation requires a semantic change to any of these "reuse" contracts, stop and route it through plan/design adjudication before editing.

### 4.3 New validation artifacts

Create:

- `tests/stage-f-interface-api-data-integration-contract-validation.md`
- `tests/stage-f-interface-api-data-integration-backward-compatibility.md`

Create the canonical Stage F pressure scenarios as numeric repository tests, preserving the approved Design scenario semantics. Stage E used the canonical range through `149`; historical deleted experimental `150..153` must not be resurrected or confused with Stage F. Allocate Stage F as:

- `tests/pressure-scenario-154-stage-f-provider-rest.md` — PS-F01
- `tests/pressure-scenario-155-stage-f-consumer-provider-link.md` — PS-F02
- `tests/pressure-scenario-156-stage-f-consumer-provider-mismatch.md` — PS-F03
- `tests/pressure-scenario-157-stage-f-dynamic-operation.md` — PS-F04
- `tests/pressure-scenario-158-stage-f-external-config-weak-hint.md` — PS-F05
- `tests/pressure-scenario-159-stage-f-unused-generated-client.md` — PS-F06
- `tests/pressure-scenario-160-stage-f-postgres-table-read.md` — PS-F07
- `tests/pressure-scenario-161-stage-f-cross-owned-table-write.md` — PS-F08
- `tests/pressure-scenario-162-stage-f-multiple-table-writers.md` — PS-F09
- `tests/pressure-scenario-163-stage-f-migration-owner-runtime-writer.md` — PS-F10
- `tests/pressure-scenario-164-stage-f-dynamic-sql.md` — PS-F11
- `tests/pressure-scenario-165-stage-f-orm-ambiguous-access.md` — PS-F12
- `tests/pressure-scenario-166-stage-f-redis-store-only.md` — PS-F13
- `tests/pressure-scenario-167-stage-f-s3-resource-access.md` — PS-F14
- `tests/pressure-scenario-168-stage-f-event-without-interface.md` — PS-F15
- `tests/pressure-scenario-169-stage-f-webhook-event-interface-interaction.md` — PS-F16
- `tests/pressure-scenario-170-stage-f-secret-connection-redaction.md` — PS-F17
- `tests/pressure-scenario-171-stage-f-sensitive-host-redaction.md` — PS-F18
- `tests/pressure-scenario-172-stage-f-historical-broad-interface.md` — PS-F19
- `tests/pressure-scenario-173-stage-f-historical-store-level-ds.md` — PS-F20
- `tests/pressure-scenario-174-stage-f-single-project-catalog.md` — PS-F21
- `tests/pressure-scenario-175-stage-f-product-interface-catalog.md` — PS-F22
- `tests/pressure-scenario-176-stage-f-product-partial-availability.md` — PS-F23
- `tests/pressure-scenario-177-stage-f-bounded-provider-impact.md` — PS-F24
- `tests/pressure-scenario-178-stage-f-weak-hint-not-call.md` — PS-F25
- `tests/pressure-scenario-179-stage-f-compatibility-indeterminate.md` — PS-F26

Do not create additional pressure scenarios unless independent implementation-plan review identifies a specific uncovered contract risk.

---

## 5. Migration strategy

Classification: `COMPATIBLE_EXTENSION`.

Implementation must preserve these historical rules:

- existing broad `IF-*` remains valid when Stage F operation/role/protocol qualifiers are absent;
- existing store-level `DS-*` remains valid without child entities;
- existing `INT-*` without Stage F access qualifiers remains valid at prior granularity;
- existing relation-only `READS_FROM` / `WRITES_TO` remains a broad accepted historical fact, not backfilled into an inferred INT access mode;
- existing EVENT facts remain valid without IF duplication;
- existing Project-local facts require no Product conversion;
- existing CC records retain current Test Engineering status/classification/adjudication meaning;
- no old IDs are rewritten;
- no historical artifact is silently enriched;
- selectors interpret absent Stage F fields as absent/unknown/inapplicable, never as false exactness;
- a material conflict triggers bounded revalidation/supersession instead of history rewrite.

No data migration executable, database migration, rewrite script, or bulk normalization step is planned.

If any implementation task proves old accepted records cannot retain their existing meaning, stop with `STAGE_F_MIGRATION_REASSESSMENT_REQUIRED`.

---

## 6. Validation strategy

Use proportional validation:

```text
targeted contract inspection
→ fail-first pressure scenarios
→ integrated Stage F contract validation
→ backward-compatibility validation
→ cross-contract consistency scan
```

Do not build a reusable execution framework for Markdown contract tests.

```text
harness_decision: DO_NOT_BUILD_HARNESS
```

A harness may be proposed only if manual/deterministic validation becomes repeatedly expensive across independent stages and has explicit ROI. Otherwise use existing repository conventions.

Stop-loss tokens:

```text
STOP_HARNESS_EXPANSION
VALIDATION_BUDGET_EXCEEDED
```

Large validation output must be written to a file and summarized; do not flood the terminal/context.

---

# 7. Implementation tasks

## Task 1 — Extend the core STM contract

### Goal

Implement the approved Stage F factual model in `references/shared-technical-model.md` without creating a new identity family.

### File

Modify only:

- `references/shared-technical-model.md`

### Required changes

Add/clarify:

1. IF Stage F semantic shape:
   - `direction`;
   - protocol/interface kind;
   - `contract_role`;
   - operation/address/version/contract refs;
   - provider reference;
   - AUTH/ERR links;
   - precision;
   - observed-view constraints;
   - exact Project/revision/evidence binding.

2. Closed `contract_role × observed_view` validation matrix from the remediated Design:
   - provider declaration;
   - provider implementation;
   - consumer expectation;
   - consumer observed use;
   - TESTED orthogonality;
   - invalid-combination handling;
   - legacy records without role do not receive inferred role.

3. Protocol-specific properties for HTTP/REST, gRPC, GraphQL, WebSocket, webhook, CLI, library, file/protocol, IPC.

4. INT concrete interaction model and interaction kinds.

5. DS store/addressable-resource model and resource kinds.

6. DS parent/child semantics with no implicit ownership/access inheritance.

7. Access modes:
   - `READ`;
   - `WRITE`;
   - `READ_WRITE`;
   - `EXECUTE`;
   - `DDL`;
   - `MIGRATION`.

8. `MIGRATION_AUTHORITY` controlled relation and separation from runtime migration/DDL.

9. New precise access authority:
   - INT is authoritative for new precise access;
   - `READ` derives `READS_FROM`;
   - `WRITE` derives `WRITES_TO`;
   - `READ_WRITE` derives both;
   - EXECUTE/DDL/MIGRATION do not derive read/write relations without separate evidence;
   - legacy relation-only facts remain broad;
   - conflict with precise INT routes to bounded revalidation.

10. DB callable boundary:
    - PROCEDURE/FUNCTION as DS schema-object identity;
    - optional IF callable contract only when independently material/evidenced;
    - INT EXECUTE targets DS and may reference IF;
    - no aliasing.

11. Precision vocabulary and applicability:
    - `EXACT`;
    - `RESOURCE_BOUNDED`;
    - `STORE_ONLY`;
    - `UNRESOLVED`;
    - family-specific allowed subsets;
    - no silent upgrade.

12. Identity/revision/history rules from Design.

### Fail-first checks

Before finalizing Task 1, prove current contract fails to guarantee at least:

- provider vs consumer role matrix;
- exact DS table access;
- INT/READS_FROM authority direction;
- STORE_ONLY family restriction;
- procedure/function DS/IF boundary;
- MIGRATION_AUTHORITY relation.

### Verification

- `git diff --check`
- inspect only Task 1 diff
- verify no new family token (`API-*`, `SQL-*`, `DB-*`, `DATA-*`) is introduced as authority
- verify old family list remains unchanged except controlled relation/property extensions

### Commit

`feat: extend Stage F technical model semantics`

### Checkpoint CP1A

Task 1 commit must exist before Task 2.

---

## Task 2 — Extend shared evidence safety and Stage F evidence qualification

### Goal

Define evidence handling required by Stage F without replacing the existing global confidence/severity contract.

### File

Modify only:

- `references/shared-evidence-model.md`

### Required changes

1. Preserve WS/EV ownership and existing evidence model.
2. Add bounded Stage F source-support classification for technical interaction extraction:
   - `DIRECT_DECLARATION`;
   - `STRONG_INFERENCE`;
   - `WEAK_HINT`.
3. State explicitly that these are Stage F source-support classes, not replacements for `HIGH/MEDIUM/LOW` confidence or lifecycle.
4. Encode acceptance prohibitions:
   - config URL != API called;
   - SDK dependency != service used;
   - DB connection != table access;
   - migration declaration != runtime access;
   - generated client != client method used.
5. Add unresolved/dynamic target evidence limitation rules.
6. Add safe excerpt requirements:
   - evidence may retain file/symbol/range/variable name;
   - secret values are never copied;
   - secret-bearing URLs/DSNs are represented by safe logical facts only;
   - sensitive internal identifiers use safe alias/redaction policy where required.
7. Preserve exact baseline/revision/Product bindings.

### Cross-check

Read but do not modify:

- `references/evidence-and-severity.md`

Ensure Stage F terms do not redefine existing confidence/severity semantics.

### Verification

- `git diff --check`
- no new evidence lifecycle statuses
- no new severity/confidence levels
- no secret-bearing examples

### Commit

`feat: add Stage F evidence and redaction rules`

### Checkpoint CP1 — Semantic Core

After Tasks 1–2:

- authority model unchanged;
- no new identity family;
- historical model remains valid;
- Stage F evidence qualification is additive;
- Design drift = none.

Do not proceed if CP1 fails.

---

## Task 3 — Extend Service Technical Documentation projections

### Goal

Make existing Technical Documentation answer the approved Service-level user questions without introducing a parallel catalog lifecycle.

### File

Modify only:

- `references/technical-documentation.md`

### Required changes

1. Preserve existing projection identities:
   - `PRJ-TECH-DOC-02-PROVIDED-INTERFACES`;
   - `PRJ-TECH-DOC-03-CONSUMED-INTERFACES`;
   - `PRJ-TECH-DOC-04-INTEGRATIONS`;
   - `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE`;
   - overview and existing package identity.

2. Extend selector predicates only through deterministic formal STM fields supported by the Stage F STM contract:
   - interface kind/direction/role;
   - interaction kind;
   - DS resource kind;
   - access mode;
   - precision;
   - formal relations including `MIGRATION_AUTHORITY`;
   - accepted/fresh/resolved state;
   - exact Product qualification when Product mode is active.

3. Define rendered content sufficient to answer:
   - what API/interface is provided;
   - what API/interface is consumed/expected;
   - which external systems are called;
   - events produced/consumed;
   - stores/resources read/written/executed;
   - ownership/migration authority;
   - unresolved/partial details;
   - evidence/provenance links.

4. Add deterministic redaction rules for generated documentation.
5. Preserve current package lifecycle and current `PKG-TECHNICAL-DOCUMENTATION` ownership.
6. Use conditional membership and existing status/freshness behavior; do not require meaningless empty documents.
7. Ensure a reader never needs to inspect STM internals to answer the standard Stage F user questions.

### Verification

- `git diff --check`
- selectors use only formal fields/relations, no prose/filename inference
- no new package lifecycle
- no duplicate PRJ identity for existing Service sections

### Commit

`feat: extend technical documentation for Stage F catalogs`

---

## Task 4 — Add Product-qualified Stage F projection semantics

### Goal

Extend Stage E Product semantics so multiple Projects can be aggregated safely into interface/integration/data-access documentation.

### Files

Modify:

- `references/product-multi-project-review.md`
- `references/technical-documentation.md` only if Task 3 did not already complete the Product projection registration cleanly

### Required changes

Define/reconcile these Product outputs as projections, not facts:

- Product Interface Catalog;
- Product Integration Map;
- Product Data Access Map;
- External Integrations Catalog;
- Provider/Consumer Matrix as optional/conditional when useful.

Every selected Product result must preserve:

- Product ID/revision;
- immutable Product baseline vector;
- stable Project identity;
- local family/semantic ID/revision;
- exact source/revision bindings;
- availability/coverage/freshness separately;
- external source binding/limitation;
- provider/consumer qualification;
- data ownership/access/migration qualification.

Explicitly prevent:

- identical method/path in different Projects from aliasing;
- identical table/schema text from aliasing across Projects;
- unavailable Project from turning Product globally clean/failed;
- Product projection from becoming factual authority;
- Product membership from granting read/write/test/Git permission.

### Verification

- single-project contract remains unchanged/first-class
- Product remains optional
- no Product factual family
- Stage E baseline/coherency/availability semantics unchanged
- `git diff --check`

### Commit

`feat: extend Product projections for Stage F catalogs`

### Checkpoint CP2 — Projection and Product Boundary

After Tasks 3–4:

- Service documentation path is complete;
- Product documentation path is complete;
- PRJ/package lifecycle reused;
- no authority transfer;
- single-project mode preserved.

---

## Task 5 — Integrate Stage F compatibility with existing Test Engineering CC authority

### Goal

Implement the remediated Design's compatibility boundary without creating a second compatibility authority.

### File

Modify only:

- `capabilities/test-review/references/test-engineering-contract.md`

### Required changes

1. Preserve existing Contract Verification automatic applicability:

```text
materially relevant declared external contract
→ Contract Verification automatic gate
```

2. Preserve `CC-*` ownership and existing status/classification/adjudication semantics.
3. Define exact Stage F inputs:
   - provider IF revision;
   - consumer IF revision;
   - Project revisions/baselines;
   - protocol/operation/address;
   - contract/version/schema/auth/error references where materially required;
   - evidence references.
4. Define Stage F normalized display mapping:
   - `COMPATIBLE` only from resolved accepted CC adjudication that accepts compatibility;
   - `INCOMPATIBLE` only from resolved accepted material mismatch adjudication;
   - `INDETERMINATE` when required inputs are absent/unresolved or CC is not final;
   - `NOT_COMPARABLE` only when records do not form a valid comparison pair and no CC comparison exists.
5. Candidate matching uncertainty produces no authoritative compatibility result.
6. When Contract Verification is not applicable, catalogs may show candidate/not-evaluated state only; they must not manufacture a competing compatibility truth.
7. Keep Contract Consistency Report projection semantics coherent.

### Verification

- current CC status/classification values remain intact
- no new compatibility identity family
- no catalog-owned compatibility authority
- missing data cannot map to compatible
- `git diff --check`

### Commit

`feat: map Stage F compatibility to Test Engineering`

---

## Task 6 — Wire Stage F into umbrella orchestration

### Goal

Make the approved Stage F semantics reachable in normal review execution without duplicating detailed reference contracts in `SKILL.md`.

### File

Modify only:

- `SKILL.md`

### Required changes

Add bounded routing language that:

1. STM acquisition for interfaces/integrations/data access uses the Stage F semantics in the owning references.
2. Interface/data catalog facts are accepted through Technical Model Gate, never from projection prose.
3. Material declared contracts trigger existing automatic Contract Verification behavior.
4. Technical Documentation Stage F outputs are projections after accepted/fresh required semantic inputs.
5. Product mode reuses exact Stage E qualification.
6. Redaction/sensitive-identifier rules apply before user-facing projection output.
7. Unknown/dynamic details remain explicit limitations.
8. No automatic API compatibility engine, runtime DB scanner, SQL parser, tracing system, or projection regeneration is introduced.

Do not copy the entire Stage F schema into `SKILL.md`; references remain normative.

### Verification

- `SKILL.md` stays orchestration-oriented
- no parallel semantic authority text
- no product-specific mandatory path in single-project mode
- `git diff --check`

### Commit

`feat: route Stage F catalog semantics in review workflow`

### Checkpoint CP3 — Capability Integration

After Tasks 5–6:

- STM authority unchanged;
- Test Engineering ownership unchanged;
- normal Skill route can reach Stage F behavior;
- Product and single-project flows remain valid.

---

## Task 7 — Add pressure scenarios PS-F01 through PS-F13

### Goal

Encode the first half of the approved fail-first Design pressure set as repository validation artifacts.

### Files

Create exactly pressure scenarios `154..166` from section 4.3.

### Required scenario contract

Each file must contain:

- scenario ID and Design mapping;
- setup/evidence shape;
- expected accepted semantic records;
- prohibited inference/authority result;
- expected projection behavior where applicable;
- backward-compatibility constraint where applicable;
- explicit `GREEN` criteria.

Cover PS-F01 through PS-F13 exactly; do not expand scope.

### Verification

- 13 files exactly
- stable numbering/names
- no duplicate/overlapping authority claims
- `git diff --check`

### Commit

`test: add Stage F interface and data pressure scenarios`

---

## Task 8 — Add pressure scenarios PS-F14 through PS-F26

### Goal

Encode the second half of the approved pressure set.

### Files

Create exactly pressure scenarios `167..179` from section 4.3.

### Required coverage

PS-F14 through PS-F26, including:

- S3 evidence precision;
- event without forced IF;
- webhook EVENT+IF+INT;
- secret and sensitive-host redaction;
- historical broad IF/DS compatibility;
- single-project catalog;
- Product catalog and partial availability;
- bounded provider impact;
- weak hint rejection;
- compatibility indeterminate behavior.

### Verification

- 13 files exactly
- total Stage F pressure set = 26
- no AMBIGUOUS expected outcomes
- `git diff --check`

### Commit

`test: complete Stage F catalog pressure scenarios`

---

## Task 9 — Add integrated Stage F contract and backward-compatibility validation

### Goal

Prove the final contract set works as one coherent system and preserves prior stages.

### Files

Create:

- `tests/stage-f-interface-api-data-integration-contract-validation.md`
- `tests/stage-f-interface-api-data-integration-backward-compatibility.md`

### Integrated contract validation must verify

1. No new factual identity family.
2. IF provider/consumer roles and validation matrix.
3. Protocol-specific property boundary.
4. INT concrete interaction authority.
5. New precise INT → READS_FROM/WRITES_TO derivation.
6. Legacy relation-only compatibility.
7. DS store/resource identity and parent/child rules.
8. Procedure/function DS vs optional IF boundary.
9. Access modes and migration authority separation.
10. Precision applicability.
11. Evidence source-support classes and weak-hint rejection.
12. Secret/sensitive output rules.
13. Service Technical Documentation selectors/package behavior.
14. Product projection qualification and collision prevention.
15. CC compatibility mapping and automatic applicability.
16. Candidate matching != compatibility.
17. Missing data != COMPATIBLE.
18. Stage B PRJ/RG/package reuse.
19. Bounded REVALIDATE and no automatic regeneration.
20. Architecture/Test/CQ authority boundaries.

### Backward-compatibility validation must verify

- Stage A STM families/identities remain valid;
- Stage B projection lifecycle meaning unchanged;
- Stage C Test Engineering ownership/state unchanged;
- Stage D CQ ownership unchanged;
- Stage E Product invariants unchanged;
- old IF/DS/INT/EVENT facts remain valid;
- old relation-only read/write facts remain valid broad facts;
- no silent defaults/enrichment;
- Product-free single-project flow remains valid;
- no new write/test/Git permissions.

### Verification

- both validation files complete
- all 26 Stage F pressure scenarios GREEN by deterministic inspection
- `git diff --check`

### Commit

`test: validate Stage F catalog integration and compatibility`

### Checkpoint CP4 — Integrated Validation

Required:

```text
pressure_scenarios: 26/26 GREEN
integrated_contract_validation: PASS
backward_compatibility: PASS
new_identity_family: NO
migration: COMPATIBLE_EXTENSION
single_project: PASS
stage_e_product: PASS
authority_conflicts: 0
```

---

## Task 10 — Final implementation-state verification

### Goal

Verify actual committed feature state before independent implementation review.

### No implementation file changes

Task 10 is verification only. Do not "fix while verifying". A failure creates a separate remediation task after review or returns to the owning implementation task before review, depending on whether the failure is detected before implementation completion.

### Required checks

1. Git state:
   - correct feature branch;
   - correct implementation worktree;
   - approved plan checkpoint is ancestor;
   - tracked state clean;
   - no unrelated commits/files.

2. Planned inventory:
   - every planned modified file present;
   - every pressure scenario `154..179` present;
   - integrated/backcompat validation files present;
   - no unexpected normative file changes.

3. Semantic gates:
   - no new family;
   - no authority drift;
   - no selector prose inference;
   - no secret-output path;
   - CC ownership preserved;
   - migration compatible;
   - historical fallback explicit;
   - Product/single-project invariants preserved.

4. Validation:
   - 26/26 pressure scenarios GREEN;
   - integrated validation PASS;
   - backward compatibility PASS;
   - `git diff --check` across implementation range.

### Commit

No commit unless Task 10 discovers that an already-approved Task artifact itself omitted required verification metadata. Prefer no commit.

### Terminal implementation marker

If complete:

`STAGE_F_IMPLEMENTATION_COMPLETE`

This is not approval. The next gate is independent implementation review.

---

# 8. Commit and checkpoint strategy

Implementation should use narrow commits with these intended subjects:

1. `feat: extend Stage F technical model semantics`
2. `feat: add Stage F evidence and redaction rules`
3. `feat: extend technical documentation for Stage F catalogs`
4. `feat: extend Product projections for Stage F catalogs`
5. `feat: map Stage F compatibility to Test Engineering`
6. `feat: route Stage F catalog semantics in review workflow`
7. `test: add Stage F interface and data pressure scenarios`
8. `test: complete Stage F catalog pressure scenarios`
9. `test: validate Stage F catalog integration and compatibility`

Task 10 should normally add no commit.

Checkpoints are semantic verification boundaries, not merge commits:

- CP1 after Tasks 1–2: semantic/evidence core;
- CP2 after Tasks 3–4: Service/Product projections;
- CP3 after Tasks 5–6: Test Engineering/orchestration integration;
- CP4 after Tasks 7–9: pressure + integrated/backcompat validation.

Do not create checkpoint commits solely to label these boundaries unless the approved execution prompt explicitly requests them.

---

# 9. Implementation workspace gate

After this plan is independently reviewed, remediated if necessary, and checkpointed, create an isolated workspace from the exact approved plan checkpoint.

Intended branch:

`feature/stage-f-interface-api-data-integration-catalog`

Intended worktree:

`../architecture-code-review-stage-f-interface-api-data-integration-catalog`

Workspace setup task must:

- fetch origin;
- verify approved plan checkpoint SHA;
- verify branch/worktree absence or reconcile explicitly;
- create worktree/branch from exact approved checkpoint;
- verify clean tracked state;
- preserve unrelated untracked files in main worktree;
- make no implementation edits;
- make no commit/push/PR.

Implementation begins only after `STAGE_F_IMPLEMENTATION_WORKSPACE_READY`.

---

# 10. Independent implementation-plan review gate

Before workspace setup, a separate reviewer must pressure-test this plan against the approved Design and current published contracts.

At minimum review:

- exact file inventory;
- task ordering/dependencies;
- whether `shared-evidence-model.md` is the correct owner for Stage F source-support/redaction rules without conflicting with `evidence-and-severity.md`;
- whether `technical-documentation.md` can express all Stage F selectors without changing generic projection contracts;
- whether Product projection registration requires only the listed Product/Technical Documentation files;
- whether CC integration is strictly additive and preserves current Test Engineering semantics;
- whether SKILL orchestration change is necessary and bounded;
- pressure-scenario numbering `154..179` and historical `150..153` non-confusion;
- backward-compatibility coverage;
- migration classification;
- scope sufficiency of 10 tasks / 4 checkpoints;
- no accidental new family or authority;
- no unnecessary harness/framework.

Use plan review finding IDs:

`FIPR-001`, `FIPR-002`, ...

Severity:

- HIGH — authority conflict, destructive migration, false acceptance, security leakage, Stage A-E regression;
- MEDIUM — material plan ambiguity likely to produce incorrect implementation;
- LOW — non-blocking clarity/ordering issue.

Plan approval requires:

```text
HIGH: 0
MEDIUM: 0
foundational_open_questions: 0
migration: COMPATIBLE_EXTENSION
harness: DO_NOT_BUILD_HARNESS
verdict: STAGE_F_IMPLEMENTATION_PLAN_APPROVED
```

---

# 11. Scope controls

Implementation must not expand Stage F into:

- live DB scanning;
- runtime DB introspection;
- runtime traffic capture;
- distributed tracing;
- service mesh/API gateway;
- schema-registry replacement;
- OpenAPI generator implementation;
- full SQL parser;
- generic ORM framework;
- database reverse-engineering engine;
- CMDB;
- graph database requirement;
- new RAG system;
- runtime service;
- automatic API compatibility engine;
- automatic RF generation;
- automatic projection regeneration.

No roadmap update during implementation. Roadmap sync belongs to final post-promotion closeout.

No push/PR/merge/tag/release/deploy during implementation unless separately authorized.

---

# 12. Failure / stop conditions

Stop immediately rather than improvising when any of these occurs:

```text
STAGE_F_BASE_CHANGED
STAGE_F_PLAN_DRIFT_DETECTED
STAGE_F_DESIGN_DRIFT_DETECTED
STAGE_F_AUTHORITY_CONFLICT
STAGE_F_NEW_IDENTITY_FAMILY_REQUIRED
STAGE_F_MIGRATION_REASSESSMENT_REQUIRED
STAGE_F_SELECTOR_MODEL_INSUFFICIENT
STAGE_F_CC_AUTHORITY_CONFLICT
STAGE_F_SECRET_OUTPUT_RISK
STAGE_F_SINGLE_PROJECT_REGRESSION
STAGE_F_PRODUCT_REGRESSION
STOP_HARNESS_EXPANSION
VALIDATION_BUDGET_EXCEEDED
```

A stop condition must report evidence and the smallest gate required to resolve it. Do not weaken a contract or test to make implementation green.

---

# 13. Expected final implementation inventory

If the independent plan review confirms this inventory unchanged, the expected Stage F implementation diff is:

### Modified existing files — 6

```text
SKILL.md
references/shared-technical-model.md
references/shared-evidence-model.md
references/technical-documentation.md
references/product-multi-project-review.md
capabilities/test-review/references/test-engineering-contract.md
```

### New pressure scenarios — 26

```text
tests/pressure-scenario-154-stage-f-provider-rest.md
...
tests/pressure-scenario-179-stage-f-compatibility-indeterminate.md
```

### New integrated validation artifacts — 2

```text
tests/stage-f-interface-api-data-integration-contract-validation.md
tests/stage-f-interface-api-data-integration-backward-compatibility.md
```

Expected implementation file count:

```text
6 modified
28 added
34 total changed paths
```

This count is a plan assertion to be independently reviewed. If the plan review establishes that a required existing contract must also change, update the plan through remediation before approval rather than silently expanding implementation scope.

---

# 14. Final implementation acceptance criteria

Before independent implementation review, the committed feature state must satisfy all of the following:

```text
approved_design_baseline: preserved
recommended_direction: B
new_identity_family: NO
STM_authority: preserved
IF_model: implemented
INT_model: implemented
DS_resource_model: implemented
EVENT_boundary: preserved
MIGRATION_AUTHORITY: implemented
precision_model: implemented
contract_role_observed_view_matrix: implemented
legacy_read_write_relation_rule: implemented
db_callable_boundary: implemented
evidence_source_support: implemented
secret_redaction: implemented
service_catalog_projections: implemented
product_catalog_projections: implemented
CC_compatibility_mapping: implemented
single_project_compatibility: PASS
stage_e_product_compatibility: PASS
historical_compatibility: PASS
projection_lifecycle_reuse: PASS
package_authority_reuse: PASS
pressure_scenarios: 26/26 GREEN
integrated_contract_validation: PASS
backward_compatibility_validation: PASS
migration: COMPATIBLE_EXTENSION
authority_conflicts: 0
secret_leakage_paths: 0
tracked_state: CLEAN
```

Final implementation completion marker:

`STAGE_F_IMPLEMENTATION_COMPLETE`

Required next gate:

`STAGE_F_INDEPENDENT_IMPLEMENTATION_REVIEW`

---

# 15. Plan verdict

This plan resolves implementation ordering and scope from the approved Stage F Design without adding a new architecture decision.

```text
plan_tasks: 10
implementation_commits_expected: 9
semantic_checkpoints: 4
modified_existing_files_expected: 6
new_pressure_scenarios: 26
new_integrated_validation_files: 2
expected_changed_paths: 34
migration: COMPATIBLE_EXTENSION
new_identity_family: NO
harness: DO_NOT_BUILD_HARNESS
roadmap_during_implementation: READ_ONLY
foundational_open_questions: 0
```

**Plan status:** `STAGE_F_IMPLEMENTATION_PLAN_DRAFT`

**Required next gate:** `STAGE_F_INDEPENDENT_IMPLEMENTATION_PLAN_REVIEW`
