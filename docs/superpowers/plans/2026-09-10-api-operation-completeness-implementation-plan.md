# API Operation Completeness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement parent-qualified addressable IF-owned operation children and
output-scoped operation-inventory completeness so detailed Provided/Consumed
Interfaces and API Report cannot omit concrete operations without visible
coverage limitations.

**Architecture:** Use existing STM/Technical Model Gate authority, extend
IF-owned structure with subordinate addressable operation children, extend
existing Technical Model Coverage with operation-inventory depth/accounting,
and make detailed Technical Documentation projections consume accepted
inventory snapshots. EXTEND performs targeted enrichment only.

**Tech Stack:** Markdown normative Skill/reference contracts, existing Stage
A/B/F semantic models, existing validation/pressure-test conventions.

**Spec:** `docs/superpowers/specs/2026-09-10-api-operation-completeness-design.md`

## Global Constraints

- THE CANONICAL PLAN WINS. Before executing each task, extract its exact files, semantic changes, verification checks, and commit subject. A conflicting implementation prompt must stop with `IMPLEMENTATION_PROMPT_PLAN_MISMATCH`.
- Preserve Approach C: IF-* remains the authoritative interface/surface identity; operations are parent-qualified addressable children owned by IF-*.
- Preserve C1: child revisions are independent but parent-qualified; reparenting creates a new parent-qualified identity with explicit history.
- The Technical Model Gate remains the sole writer/acceptor of operation facts; no new top-level OP authority family is created.
- Technical Model Coverage remains the sole coverage authority; operation completeness is an output-scoped dimension, not a second coverage authority.
- Ordinary Architecture FULL remains material interface-surface coverage and does not require every operation.
- Detailed Provided Interfaces, detailed Consumed Interfaces, and API Report require accepted operation-inventory completeness for their selected bounded slice.
- Operation inventory completeness means every candidate is accounted for; it does not require every schema/detail field to be known.
- Effective HTTP route composition is evidence-backed and required when resolvable; dynamic routes remain `RESOURCE_BOUNDED` or `UNRESOLVED` with visible limitations.
- Technical Documentation cannot reconstruct private facts from source during rendering. All operation facts and inventory accounting arrive through accepted STM/Coverage dependencies.
- `requested_work` remains distinct from `resolved_work`; internal dependencies never become selected capabilities or outputs.
- Stage B `CURRENT` remains distinct from factual inventory completeness; impact accounting never regenerates automatically.
- Product remains optional, single-project mode remains first-class, and every operation/inventory claim is Project/baseline qualified.
- Preserve independent `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED` views. `TESTED` requires accepted execution evidence.
- Do not redesign CQ, TE, CC, STM identity families, Product composition, projection lifecycle, or runtime execution.
- `DO_NOT_BUILD_HARNESS`: use one compact deterministic Markdown validation artifact and existing repository checks.
- Do not rewrite historical IF records or create retroactive operation children for all existing facts.

## File Map

| Path | Action | Responsibility | Task |
|---|---|---|---|
| `references/shared-technical-model.md` | MODIFY | IF-owned subordinate operation structure, identity, views, protocol fields, parent/revision/history rules | 1–2 |
| `references/shared-evidence-model.md` | MODIFY | Operation-level evidence/provenance and composed-route observation binding | 2 |
| `references/technical-model-coverage.md` | MODIFY | Output-scoped operation depth and deterministic inventory accounting | 3 |
| `references/technical-model-dependencies.md` | MODIFY | Targeted operation-depth dependency slice and resolved_work routing metadata | 6 |
| `references/projection-dependencies.md` | MODIFY | Operation inventory snapshot dependency and membership/revision invalidation | 4 |
| `references/projection-impact.md` | READ-ONLY REFERENCE | Existing membership/revision impact state used by Task 4 | 4 |
| `references/projection-verification.md` | MODIFY | V3/V4 contract checks for operation inventory and limitation rendering | 5 |
| `references/technical-documentation.md` | MODIFY | Detailed Provided/Consumed dependency depth, operation rendering, API Report and complete-claim guard | 4–5 |
| `references/projection-gates-and-packages.md` | READ-ONLY REFERENCE | Existing package membership/freshness rules consumed by Task 4–5 | 4 |
| `references/projection-regeneration.md` | READ-ONLY REFERENCE | Explicit regeneration boundary consumed by Task 4–5 | 4 |
| `references/revalidation-and-freshness.md` | MODIFY | Operation-depth EXTEND/revalidation impact routing and legacy surface-only state | 6, 8 |
| `references/session-orchestration.md` | MODIFY | Output-scoped API Report dependency routing and resolved_work enrichment boundary | 6 |
| `references/review-modes-and-orchestration.md` | READ-ONLY REFERENCE | NEW/EXTEND/RESUME routing vocabulary and authority boundary | 6 |
| `capabilities/code-quality-review/references/code-quality-contract.md` | MODIFY | Operation-child finding references without CQ factual ownership | 7 |
| `capabilities/test-review/references/test-engineering-contract.md` | MODIFY | Operation-targeted test cases and CC operation comparison inputs without TE/CC fact drift | 7 |
| `tests/api-operation-completeness-validation.md` | CREATE | Fail-first evidence and compact D01–D20/A01–A12/final claim checks | 1, 8 |
| `README.md` | MODIFY | User-facing limitation and detailed API scope explanation | 8 |
| `docs/reference/outputs.md` | MODIFY | Output-level operation inventory and complete-claim behavior | 8 |
| `docs/reference/workflows.md` | MODIFY | EXTEND targeted enrichment and API Report routing explanation | 8 |
| `docs/concepts/review-suite.md` | MODIFY | Architecture FULL versus detailed API coverage distinction | 8 |
| `docs/getting-started/quick-start.md` | READ-ONLY REFERENCE | Confirm no contradictory claim; update only if the implementation changes user-visible API wording | 8 |
| `docs/guides/test-engineering.md` | READ-ONLY REFERENCE | Confirm operation-targeted assurance wording remains owned by TE | 7–8 |
| `docs/guides/code-quality-review.md` | READ-ONLY REFERENCE | Confirm operation-targeted findings wording remains owned by CQ | 7–8 |

The READ-ONLY files are reviewed for contradictions and are not modified unless
the exact task's post-change check proves a directly affected user-facing or
normative statement must be corrected; no unrelated documentation expansion is
allowed.

## Canonical-plan execution rule

THE CANONICAL PLAN WINS. Before each task, the executor records:

```text
task_title: <exact task heading>
files: <exact File Map paths for the task>
semantic_changes: <task contract bullets>
verification: <exact commands/checks>
commit_subject: <exact subject below>
```

If an implementation prompt asks for different files, identity, authority,
granularity, lifecycle, or validation semantics, stop with
`IMPLEMENTATION_PROMPT_PLAN_MISMATCH` and do not reinterpret the plan.

## Task 1: Capture fail-first evidence and add IF-owned operation child contract

**Files:**

- Create: `tests/api-operation-completeness-validation.md`
- Modify: `references/shared-technical-model.md`

**Interfaces:**

- Consumes: Existing `IF-*` shape, STM lifecycle/status/freshness/authority fields, `WS-*`/`EV-*` provenance, and Technical Model Gate ownership.
- Produces: Parent-qualified operation child serialization and reference grammar for Tasks 2–8; immutable pre-change checks FF01–FF06.

- [ ] **Step 1: Record fail-first checks before changing normative text.** Add a PRE-CHANGE section to the validation artifact with exactly these checks and expected `GAP PRESENT` results: coarse one-IF/ten-operation CURRENT projection; missing inventory accounting; missing composed route requirement; coarse EXTEND reuse; material-only consumed grouping; and complete-claim absence.
- [ ] **Step 2: Verify fail-first evidence is tied to the base.** Record base `d68b9650a29820d8f9a563a81f5d90fb8f11d5e5`, inspected paths, and the six concrete contract observations. Do not reconstruct this section after editing.
- [ ] **Step 3: Add the exact IF-owned child shape.** Extend the IF contract with:

```text
operation_children:
  - operation_id: OP-<zero-padded-decimal-3-or-more-digits>
    parent_if: IF-*<parent-revision>
    revision: <integer revision>
    interface_kind: <existing closed interface kind>
    direction: PROVIDED | CONSUMED
    contract_role: <existing role vocabulary>
    operation_identity: <protocol-specific normalized identity>
    precision: EXACT | RESOURCE_BOUNDED | UNRESOLVED
    status: CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED
    freshness: VALID | REVALIDATION_REQUIRED | UNKNOWN
    authority: RESOLVED | UNRESOLVED
    observed_views: [DECLARED | IMPLEMENTED | CONSUMED | TESTED ...]
    protocol_properties: <existing controlled properties>
    evidence_refs: WS-* / EV-*
    supersedes: optional parent-qualified operation reference
```

  State explicitly that `operation_id` is unique only within the parent-qualified IF identity and that `IF-*/OP-*` is a reference path, not a new global STM family.
- [ ] **Step 4: Define lifecycle and parent rules.** Specify that the Technical Model Gate accepts/revises/supersedes children; an operation cannot exist without an IF; `operation_id` is allocated monotonically within its parent and never reused; a semantic parent move creates a new parent-qualified child with `supersedes`; historical surface-only IFs remain valid with no inferred children; operation status/freshness/authority do not imply any observed view. Persist `observed_views` as an explicit list so multiple independent existing views can coexist without changing their semantics.
- [ ] **Step 5: Add focused static checks.** Verify the contract contains no top-level `OP-*` family, preserves all existing IF views and status vocabulary, and states that no downstream capability creates an operation.
- [ ] **Step 6: Run verification.**

```bash
rg -n "operation_children|parent_if|operation_id|Technical Model Gate|new global|cannot exist" references/shared-technical-model.md
rg -n "FF01|FF02|FF03|FF04|FF05|FF06|GAP PRESENT" tests/api-operation-completeness-validation.md
git diff --check
```

Expected: all required clauses are present; no placeholder; checks pass.
- [ ] **Step 7: Commit.**

```bash
git add references/shared-technical-model.md tests/api-operation-completeness-validation.md
git commit -m "feat: add IF-owned operation records"
```

## Task 2: Define protocol identity, evidence, and effective route composition

**Files:**

- Modify: `references/shared-technical-model.md`
- Modify: `references/shared-evidence-model.md`

**Interfaces:**

- Consumes: Task 1 parent-qualified operation child shape; existing `interface_kind`, `contract_role`, `operation_identity`, precision, and evidence locators.
- Produces: Deterministic protocol identity and route-composition rules used by Coverage, CQ/TE/CC, and Technical Documentation.

- [ ] **Step 1: Define the protocol identity table.** For HTTP set `operation_identity` to normalized method plus effective route/template, qualified by parent IF and role/direction. For GraphQL use operation type/name or addressable field/schema surface; for gRPC/RPC package/service/method; for WebSocket addressable command/message only when contractually identifiable; for CLI command/subcommand; retain EVENT-* as event identity and use operation children only for addressable command surfaces.
- [ ] **Step 2: Define exact HTTP normalization.** Normalize method to uppercase; normalize an effective path to one leading slash with redundant separators removed; preserve parameter names as contract-visible names; preserve version segments; do not normalize distinct parameter names into one identity unless the protocol contract explicitly treats them as equivalent. A trailing slash is normalized only according to the framework’s evidenced route semantics, otherwise the distinction remains unresolved.
- [ ] **Step 3: Define composition inputs and outcomes.** Record mount/controller/router prefixes and local route declarations as separate evidence. Compose nested prefixes in declaration order. Produce `EXACT` only when method and effective path are evidenced; produce `RESOURCE_BOUNDED` or `UNRESOLVED` for computed, plugin, feature-flag, reflection, runtime-only, or conflicting declarations. Never fabricate a path.
- [ ] **Step 4: Define duplicates, aliases, and reparenting.** Same path with different methods is distinct. Same handler under distinct routes is distinct unless an accepted alias relation proves intentional equivalence. Duplicate declarations are accounted candidates until classified as duplicate or separate. A route exposed under two mounts has two parent-qualified operation identities.
- [ ] **Step 5: Extend evidence semantics.** Add operation-level subject references and composition evidence: route declaration, each prefix/mount, method, parameters/schema, auth middleware, consumer call site, generated contract, and accepted runtime observation where available. Evidence location is never semantic identity; dynamic/partial evidence remains explicit.
- [ ] **Step 6: Run edge checks.** Add A01–A10 rows to the validation artifact covering GET/POST same path, parameter-name behavior, nested prefixes, aliases, flags, declaration/code mismatch, exact method/path with unknown schema, unresolved path, and dynamic consumer base URL.
- [ ] **Step 7: Run verification and commit.**

```bash
rg -n "HTTP_REST|method|effective|route|prefix|nested|RESOURCE_BOUNDED|UNRESOLVED|operation_children" references/shared-technical-model.md references/shared-evidence-model.md
rg -n "A01|A02|A03|A04|A05|A06|A07|A08|A09|A10" tests/api-operation-completeness-validation.md
git diff --check
git add references/shared-technical-model.md references/shared-evidence-model.md tests/api-operation-completeness-validation.md
git commit -m "feat: define protocol operation identity"
```

## Task 3: Add output-scoped operation inventory coverage

**Files:**

- Modify: `references/technical-model-coverage.md`
- Modify: `references/technical-model-dependencies.md`

**Interfaces:**

- Consumes: Task 1–2 operation children, protocol precision, Project/baseline binding, and existing Technical Model Coverage matrix statuses.
- Produces: `OPERATION_INVENTORY` depth and accepted deterministic accounting for detailed Provided/Consumed slices.

- [ ] **Step 1: Add exact coverage depth vocabulary.** Use `SURFACE` / `INTERFACE_SURFACE_COMPLETE` and `OPERATION_INVENTORY` / `OPERATION_INVENTORY_COMPLETE`, `OPERATION_INVENTORY_PARTIAL`, `OPERATION_INVENTORY_UNKNOWN`. Do not add a mandatory `OPERATION_DETAIL` gate.
- [ ] **Step 2: Define the coverage record.** Add exact fields:

```text
  operation_inventory:
  coverage_id: TMC-<stable-id>
  coverage_revision: <integer revision>
  definition_revision: <integer revision>
  scope_id: <bounded scope>
  project_binding: <Project/repository/revision/baseline>
  product_binding: optional exact Product/member bindings
  direction: PROVIDED | CONSUMED
  interface_kind: <closed kind or bounded set>
  parent_if_slice: [IF-*<revision> ...]
  depth: SURFACE | OPERATION_INVENTORY
  discovered_candidates: N
  accepted_exact_operations: N1
  accepted_bounded_or_unresolved_operations: N2
  accepted_not_applicable_or_duplicate_candidates: N3
  unaccounted_candidates: N4
  status: PENDING | IN_PROGRESS | ACCEPTED | PARTIAL | BLOCKED | UNKNOWN
  evidence_refs: WS-* / EV-*
  limitations: [<bounded reason> ...]
```

- [ ] **Step 3: Define acceptance.** `OPERATION_INVENTORY_COMPLETE` is accepted only when `N4 = 0`, every candidate has an evidence-backed accepted exact, bounded/unresolved, not-applicable, or duplicate classification, and the scope/baseline/direction/interface kind are explicit. Dynamic operations count as accounted only with an accepted limitation. Missing/unavailable/unbounded discovery remains PARTIAL, UNKNOWN, or BLOCKED.
- [ ] **Step 4: Define materiality separation.** Preserve ordinary FULL surface acceptance; operation presence becomes material only within a requested detailed API/interface slice. Partial schema/parameter detail does not fail inventory completeness when the operation itself is accounted.
- [ ] **Step 5: Add targeted dependency metadata.** Define an operation-depth requirement in `resolved_work` as an internal dependency slice containing the exact scope, required direction/kind, parent IF revisions, and coverage record revision. It must not select Architecture or any other capability.
- [ ] **Step 6: Add D01, D04, D05, D06, D08, D09, D10, D17–D20 checks.** Verify ten operations under one router, dynamic route limitation, declaration/code mismatch, partial detail, Architecture-only no enumeration, API-only targeted acceptance, 5,000-operation partitioning, GraphQL/gRPC, and Product divergence.
- [ ] **Step 7: Run verification and commit.**

```bash
rg -n "OPERATION_INVENTORY|discovered_candidates|unaccounted_candidates|N4|INTERFACE_SURFACE_COMPLETE|TARGETED" references/technical-model-coverage.md references/technical-model-dependencies.md
rg -n "D01|D04|D05|D06|D08|D09|D10|D17|D18|D19|D20" tests/api-operation-completeness-validation.md
git diff --check
git add references/technical-model-coverage.md references/technical-model-dependencies.md tests/api-operation-completeness-validation.md
git commit -m "feat: add operation inventory coverage"
```

## Task 4: Bind detailed projections to operation inventory snapshots

**Files:**

- Modify: `references/projection-dependencies.md`
- Modify: `references/technical-documentation.md`

**Interfaces:**

- Consumes: Existing IF `SEMANTIC_SELECTOR`, Task 3 accepted coverage record, and Stage B `SEMANTIC_EXACT`/`SEMANTIC_SELECTOR` snapshots.
- Produces: Frozen detailed projection dependency shape detecting operation membership, revision, precision, and coverage-definition changes.

- [ ] **Step 1: Define the detailed dependency snapshot.** For Provided/Consumed detailed projections require exact parent IF revisions, accepted operation-inventory coverage ID/revision, operation-inventory definition revision, and stable ordered parent-qualified operation child IDs/revisions.
- [ ] **Step 2: Define change detection.** Record `SELECTOR_MEMBERSHIP_CHANGED` for operation add/remove or unresolved↔exact membership changes; `SELECTOR_MEMBER_REVISION_CHANGED` for child semantic revisions; exact parent IF revision changes for parent changes; and a dependency-contract impact for coverage definition revision changes. Each makes the projection STALE under existing Stage B rules.
- [ ] **Step 3: Preserve lifecycle separation.** State that the renderer never scans source, projection impact accounting never changes selection, and STALE/BLOCKED is never treated as current or repaired by prose. Regeneration remains a separate explicit `RG-*` workflow.
- [ ] **Step 4: Bind package scope.** Keep `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` and `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` identities unchanged. Detailed package membership follows selected output scope; Integrations/Auth/Failure do not inherit operation inventory unless their own existing contract explicitly consumes it.
- [ ] **Step 5: Run D11–D16 and freshness checks.** Verify EXTEND depth is not hidden in projection generation, new/removed/path/auth/boundary changes create impact, evidence-only changes follow existing revalidation, and no automatic regeneration occurs.
- [ ] **Step 6: Run verification and commit.**

```bash
rg -n "operation-inventory|operation.*snapshot|MEMBERSHIP_CHANGED|MEMBER_REVISION_CHANGED|STALE|Provided Interfaces|Consumed Interfaces" references/projection-dependencies.md references/technical-documentation.md
rg -n "D11|D12|D13|D14|D15|D16" tests/api-operation-completeness-validation.md
git diff --check
git add references/projection-dependencies.md references/technical-documentation.md
git commit -m "feat: bind interface projections to operation inventory"
```

## Task 5: Implement operation rendering, API Report dependencies, and complete-claim guard

**Files:**

- Modify: `references/technical-documentation.md`
- Modify: `references/projection-verification.md`

**Interfaces:**

- Consumes: Task 4 snapshot, Task 1–3 operation/coverage fields, existing API Report umbrella, V1–V4 verification, and existing PRJ identities.
- Produces: Detailed operation rows, explicit limitations, scope-sensitive complete claims, and API Report dependency behavior.

- [ ] **Step 1: Define operation rendering.** Every accounted operation row must show parent IF, operation child reference, direction/role, protocol kind, method/effective path when exact, precision, observed views, and evidence/provenance. Bounded/unresolved operations must be shown with their limitation, not omitted.
- [ ] **Step 2: Classify detail fields.** Mark method/effective path as identity-required when exact; path/query parameters, relevant headers, request media/schema, response statuses/schemas, auth/trust, error contract, pagination, multipart/upload, and boundary evidence as `WHEN_APPLICABLE_REQUIRED` when material and evidenced; additional detail as `WHEN_EVIDENCED`. State that inventory complete does not mean all detail known.
- [ ] **Step 3: Preserve API Report umbrella.** Keep the existing sections 02, 03, 04, 07, 09 and no API identity. Only selected Provided and Consumed sections require their matching operation inventory; deselecting Consumed removes that requirement. Do not add operation depth to Integrations/Auth/Failure without their own existing need.
- [ ] **Step 4: Add complete-claim guard.** Permit “complete API,” “all endpoints,” “full endpoint list,” and equivalent wording only when the exact selected detailed Provided/Consumed scope has accepted `OPERATION_INVENTORY_COMPLETE` and a valid dependency snapshot. Otherwise require PARTIAL/UNKNOWN/UNRESOLVED limitation wording. CURRENT alone is insufficient.
- [ ] **Step 5: Extend V3/V4 obligations.** V3 checks operation inventory status, snapshot, required operation fields, and declared claim rule; V4 checks faithful rendering of every accepted accounted operation and limitation without semantic adjudication.
- [ ] **Step 6: Add D03, D07, D12, D13, D14, D15, D16 and claim checks.** Cover nested route composition, providerless consumers, endpoint add/remove/path/auth/boundary changes, and rejection of complete claims without accepted matching inventory.
- [ ] **Step 7: Run verification and commit.**

```bash
rg -n "OPERATION_INVENTORY_COMPLETE|complete API|all endpoints|full endpoint|PARTIAL|UNRESOLVED|V3|V4|operation" references/technical-documentation.md references/projection-verification.md
rg -n "D03|D07|D12|D13|D14|D15|D16|COMPLETE_CLAIM" tests/api-operation-completeness-validation.md
git diff --check
git add references/technical-documentation.md references/projection-verification.md tests/api-operation-completeness-validation.md
git commit -m "feat: require operation inventory for detailed interfaces"
```

## Task 6: Add targeted EXTEND enrichment and revalidation routing

**Files:**

- Modify: `references/session-orchestration.md`
- Modify: `references/technical-model-dependencies.md`
- Modify: `references/revalidation-and-freshness.md`

**Interfaces:**

- Consumes: Existing NEW/EXTEND/REVALIDATE routing, Task 3 operation-depth requirement, Task 4 projection snapshot, and `requested_work != resolved_work` contract.
- Produces: Deterministic targeted enrichment route for surface-only STM to detailed API output.

- [ ] **Step 1: Define insufficiency detection.** When EXTEND selects detailed Provided/Consumed/API output and the accepted STM has only `SURFACE` depth, emit an operation-depth requirement rather than treating the surface as sufficient.
- [ ] **Step 2: Define targeted resolved_work.** Persist exact Project/baseline, direction, interface kind, parent IF slice, source/evidence scope, and required `OPERATION_INVENTORY` depth. Keep this internal; do not add Architecture, TE, or CQ to `requested_work.capabilities`.
- [ ] **Step 3: Define enrichment flow.** Route existing accepted surface facts plus targeted discovery/evidence → Technical Model Gate operation acceptance → targeted coverage acceptance → projection dependency satisfaction → explicit generation/regeneration → V1–V4 → CURRENT. Existing surface facts remain accepted throughout.
- [ ] **Step 4: Define revalidation behavior.** Preserve requested operation scope during REVALIDATE; new/removal/revision/precision changes affect the matching inventory snapshot and projection freshness only. Do not add outputs or regenerate automatically.
- [ ] **Step 5: Add D11, D12, R01–R04, A11–A12 checks.** Verify EXTEND does not rerun unrelated work, new/removal changes stale the projection, Product member divergence remains qualified, and removed operations retain history.
- [ ] **Step 6: Run verification and commit.**

```bash
rg -n "EXTEND|OPERATION_INVENTORY|resolved_work|targeted|REVALIDATE|regenerat|requested_work" references/session-orchestration.md references/technical-model-dependencies.md references/revalidation-and-freshness.md
rg -n "D11|D12|R01|R02|R03|R04|A11|A12" tests/api-operation-completeness-validation.md
git diff --check
git add references/session-orchestration.md references/technical-model-dependencies.md references/revalidation-and-freshness.md tests/api-operation-completeness-validation.md
git commit -m "feat: deepen interface inventory during extend"
```

## Task 7: Add minimum CQ, TE, and CC operation references

**Files:**

- Modify: `capabilities/code-quality-review/references/code-quality-contract.md`
- Modify: `capabilities/test-review/references/test-engineering-contract.md`

**Interfaces:**

- Consumes: Parent-qualified operation references, existing CQ finding shape, TE boundary/test-case shape, CC provider/consumer comparison inputs, and existing TESTED evidence rules.
- Produces: Operation-targeted downstream references without transferring factual ownership.

- [ ] **Step 1: Extend CQ references.** Permit a CQ finding to carry `interface_ref: IF-*<revision>`, `operation_ref: IF-*/OP-*<revision>`, and a specific operation property/boundary evidence pointer. State CQ cannot create, revise, or classify operation inventory facts.
- [ ] **Step 2: Extend TE references.** Permit boundary/negative/contract cases to target an operation child and operation field. Preserve `accepted_test_case != executed_test != tested_result`; generated/accepted cases never populate STM TESTED.
- [ ] **Step 3: Extend CC inputs only.** Permit provider/consumer operation references in existing comparison records; same method/path is only a matching input, never automatic compatibility. Keep schemas, statuses, auth, errors, and adjudication under CC’s existing authority.
- [ ] **Step 4: Add A06–A10 and D05–D08 checks.** Verify declaration/implementation mismatch, unknown schema, consumer dynamic base, partial operation detail, and TE/CQ/CC ownership boundaries.
- [ ] **Step 5: Run verification and commit.**

```bash
rg -n "operation_ref|interface_ref|TESTED|accepted_test_case|provider.*operation|consumer.*operation|compatib" capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md
rg -n "A06|A07|A08|A09|A10|D05|D06|D07|D08" tests/api-operation-completeness-validation.md
git diff --check
git add capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md tests/api-operation-completeness-validation.md
git commit -m "feat: reference operations from quality and test contracts"
```

## Task 8: Preserve compatibility, sync affected docs, and run integrated validation

**Files:**

- Modify: `README.md`
- Modify: `docs/reference/outputs.md`
- Modify: `docs/reference/workflows.md`
- Modify: `docs/concepts/review-suite.md`
- Review: `docs/getting-started/quick-start.md`
- Review: `docs/guides/test-engineering.md`
- Review: `docs/guides/code-quality-review.md`
- Modify: `tests/api-operation-completeness-validation.md`

**Interfaces:**

- Consumes: All prior task contracts and the approved design’s compatibility/documentation requirements.
- Produces: User-facing explanation, final validation evidence, and promotion-ready implementation state.

- [ ] **Step 1: Define compatibility checks.** Verify historical surface-only IF records remain valid with operation inventory `UNASSESSED`/`UNKNOWN`; they satisfy surface-depth consumers but not detailed inventory dependencies. Do not create child records retroactively, invalidate projections, or rewrite Product/STM/CQ/TE/CC artifacts.
- [ ] **Step 2: Update human docs minimally.** Explain that detailed API outputs enumerate accounted operations, may show PARTIAL/UNKNOWN limitations, Architecture FULL is not every endpoint, EXTEND may perform targeted enrichment, and complete claims require accepted inventory. Keep API Report as the existing umbrella and distinguish factual docs from CQ/TE/CC/Architecture outputs.
- [ ] **Step 3: Verify unchanged docs for contradiction.** Search quick-start and guides for claims that Architecture FULL or CURRENT projection means all endpoints; edit only directly contradictory wording, keeping internal operation schema out of beginner documentation.
- [ ] **Step 4: Complete the validation artifact.** Add final deterministic rows for D01–D20, A01–A12, FF01–FF06, exact complete-claim checks, Product qualification, no private reconstruction, no automatic regeneration, and the final expected summary: `20/20` design scenarios, `12/12` adversarial scenarios, `6/6` fail-first corrected, `DO_NOT_BUILD_HARNESS`.
- [ ] **Step 5: Run integrated checks.**

```bash
rg -n "all endpoints|complete API|FULL|CURRENT|operation inventory|PARTIAL|EXTEND|API Report|Architecture" README.md docs/reference/outputs.md docs/reference/workflows.md docs/concepts/review-suite.md docs/getting-started/quick-start.md docs/guides/test-engineering.md docs/guides/code-quality-review.md
rg -n "FF01|FF02|FF03|FF04|FF05|FF06|D01|D20|A01|A12|20/20|12/12|6/6|DO_NOT_BUILD_HARNESS" tests/api-operation-completeness-validation.md
git diff --check
git diff --name-status d68b9650a29820d8f9a563a81f5d90fb8f11d5e5..HEAD
```

Expected: only File Map implementation surfaces and validation/docs are changed; all six fail-first gaps are corrected; no contradictory complete-claim route exists.
- [ ] **Step 6: Commit.**

```bash
git add README.md docs/reference/outputs.md docs/reference/workflows.md docs/concepts/review-suite.md docs/getting-started/quick-start.md docs/guides/test-engineering.md docs/guides/code-quality-review.md tests/api-operation-completeness-validation.md
git commit -m "docs: document operation-complete API outputs"
```

## Integrated acceptance and pressure verification

Run once after Task 8; do not create one file per case. The single validation
artifact must map every case to an owning task, concrete contract check, and
expected outcome.

### D01–D20 acceptance matrix

The artifact must retain the exact scenario IDs and verify: one router/ten
operations; nested prefixes; same-path methods; dynamic paths; declaration/code
mismatch in both directions; providerless consumers; partial schema; ordinary
Architecture-only surface behavior; API Report-only targeted depth; EXTEND;
add/remove/path/auth/boundary impact; 5,000-operation scale; GraphQL; gRPC; and
Product member divergence. Expected: `20/20 DETERMINISTIC`.

### A01–A12 adversarial matrix

The artifact must verify parameter-name identity, dual mounts, aliases, feature
flags, declaration/implementation gaps, partial operation fields, unresolved
paths, dynamic consumer base URLs, Product v1/v2 divergence, and operation
removal history. Expected: `12/12 MAPPED` and deterministic outcomes.

### Exact complete-claim checks

The final checks must reject complete-API wording when selected detailed
Provided or Consumed coverage is not accepted, allow it only for the exact
bounded scope with valid `OPERATION_INVENTORY_COMPLETE`, and allow Provided-only
claims without requiring Consumed coverage. Projection CURRENT alone must not
pass.

## Commit strategy

The implementation target is eight commits, one per task, in this order:

1. `feat: add IF-owned operation records`
2. `feat: define protocol operation identity`
3. `feat: add operation inventory coverage`
4. `feat: bind interface projections to operation inventory`
5. `feat: require operation inventory for detailed interfaces`
6. `feat: deepen interface inventory during extend`
7. `feat: reference operations from quality and test contracts`
8. `docs: document operation-complete API outputs`

After all eight commits and integrated validation, perform exactly one
independent implementation review. If that review finds HIGH or MEDIUM issues,
perform targeted remediation and one bounded re-review; do not create review
gates after individual tasks or recursive review loops.

## Completion gate

Before declaring the plan complete, verify:

- design direction, Approach C, and C1 are preserved;
- operation child serialization, identity, route composition, and lifecycle are frozen;
- Technical Model Coverage remains the sole authority with a frozen accounting rule;
- projection snapshots detect operation membership/revision/coverage changes;
- Provided, Consumed, and API Report dependency depth is selected-output scoped;
- EXTEND enrichment is targeted and remains in resolved_work;
- CQ/TE/CC references do not create factual operation authority;
- legacy surface-only IFs remain valid and migration is `COMPATIBLE_EXTENSION`;
- complete-claim guard is implemented and visible limitations remain explicit;
- D01–D20 map 20/20 and A01–A12 map 12/12;
- FF01–FF06 are captured before implementation and corrected after implementation;
- no runtime scanner, projection-private source reconstruction, automatic regeneration, Product requirement, or harness exists;
- one independent implementation review remains after all tasks and integrated validation.

The next step after plan approval is implementation, not another architecture
decision. The plan does not authorize implementation in the planning session.
