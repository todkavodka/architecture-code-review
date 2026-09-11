# Change Review & Baseline Reconciliation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement first-class read-only Change Review over immutable base/candidate source states, explicit candidate/canonical authority separation, contextual reconciliation, baseline mismatch routing, safe review reuse, and post-reconciliation projection impact without automatic regeneration.

**Architecture:** CHANGE_REVIEW is an orchestration intent, not a capability. CR/CF/CRF candidate artifacts are non-authoritative and may be consumed only as review evidence/reconciliation input; canonical mutation occurs only through existing owning authorities during explicit RECONCILE_CHANGE. Baseline advancement occurs only after coherent material-delta reconciliation, then existing Projection Impact Analysis runs, with projection regeneration remaining explicit.

**Tech Stack:** Markdown normative contracts, repository/reference contracts, deterministic Markdown validation artifacts, Git-based immutable source bindings; no runtime service, database, parser framework, SCM daemon, or new execution engine.

**Spec:** docs/superpowers/specs/2026-09-11-change-review-baseline-reconciliation-design.md

## Global Constraints

- Preserve `Shared Technical Model = WHAT EXISTS` and Technical Model Gate as sole accepted factual authority.
- Preserve Architecture Review, Test Engineering, Code Quality Review, Contract Verification, Product, and Technical Documentation ownership boundaries.
- `CHANGE_REVIEW != REVALIDATE != RECONCILE_CHANGE != PROJECTION_REGENERATION`.
- `CHANGE_REVIEW` is one new orchestration intent and not a capability; the top-level semantic capabilities remain exactly three.
- Persist exact repository, Project/Product qualification, ref input, commit, and tree for both base and candidate; `HEAD` is not special.
- CR/CF/CRF are review-local evidence and cannot satisfy accepted STM, finding, test, compatibility, Product, or projection dependencies.
- Candidate review cannot mutate canonical state, mark projections `STALE`, advance baseline, or regenerate projections.
- Reconciliation is contextual, explicitly selected, routed through existing owners, and source-state coherent.
- `TREE_EQUIVALENT` requires an exact proof; branch names, ancestry, fuzzy text, or inspected-files coincidence are insufficient.
- `RESUME`, `EXTEND`, and current `PROJECTION_REPAIR` stop on unresolved baseline mismatch.
- Prediction is not actual Stage B Projection Impact Analysis; regeneration remains explicit and never automatic.
- Product qualification uses exact member baseline vectors; Product is optional and single-project mode remains supported.
- Operation/API completeness remains owned by STM and Technical Model Coverage; candidate API facts are not accepted until reconciliation.
- No runtime scanner, OpenAPI generator, parser framework, generic workflow engine, SCM service, release/merge approval, or implementation plan is introduced by implementation.
- Validation uses one bounded Markdown artifact and targeted repository checks: `DO_NOT_BUILD_HARNESS`.

---

## File Map

### NORMATIVE_CHANGE

| Path | Responsibility | Design sections implemented | Contract consumers |
|---|---|---|---|
| `references/session-orchestration.md` | Startup intent, baseline relation, mismatch routing, requested/resolved work, contextual actions, source binding, candidate-mode dispatch | 8–11, 27, 30–34, 44–45 | `review-modes-and-orchestration.md`, revalidation, Product, capability contracts |
| `references/review-modes-and-orchestration.md` | Persistent coordinator state, CR lifecycle/handoff, candidate execution mode, reconciliation closeout | 12, 19–21, 27–29, 35–37 | session coordinator and all selected capability workflows |
| `references/shared-evidence-model.md` | Exact base/candidate evidence binding, review-local evidence qualification, candidate provenance | 9, 13–19, 24, 42, 45–46 | STM Gate, candidate discovery, reconciliation owners |
| `references/shared-technical-model.md` | Accepted-versus-candidate fact boundary and reconciliation input contract | 16, 19, 41–42, 43 | Technical Model Gate and all factual consumers |
| `references/technical-model-dependencies.md` | Candidate dependency exclusion and minimum reconciliation dependency slice | 14, 19, 27–29, 42 | STM, projections, EXTEND/REVALIDATE routing |
| `references/revalidation-and-freshness.md` | Strict Change Review/Revalidate distinction, mismatch and reconciliation handoff | 8, 26, 30–32, 35–37, 50 | session orchestration and actual impact handoff |
| `references/projection-impact.md` | Actual impact boundary after accepted reconciliation; prediction exclusion | 35–37, 50 | Stage B projection lifecycle |
| `references/projection-dependencies.md` | Candidate-ref exclusion from semantic dependencies and accepted snapshot rules | 19, 35–37, 42 | Technical Documentation and all projections |
| `references/product-multi-project-review.md` | Project/member-qualified base/candidate vectors and Product reconciliation | 43, 48, 62 | Product views and qualified owners |
| `capabilities/code-quality-review/references/code-quality-contract.md` | Candidate CQ mode, CRF/effect references, canonical CQ promotion boundary | 17–19, 28, 38 | CQ capability and reconciliation |
| `capabilities/test-review/references/test-engineering-contract.md` | Candidate TE impact and execution-evidence barrier | 17–19, 28, 39 | TE capability and reconciliation |
| `references/ownership-and-scenarios.md` | Candidate Architecture interpretation and accepted Architecture promotion boundary | 18, 28, 40 | Architecture review/reconciliation |

### VALIDATION

| Path | Responsibility | Design sections implemented | Contract consumers |
|---|---|---|---|
| `tests/change-review-baseline-reconciliation-validation.md` | Preserve pre-change gaps and deterministic FF/CR/MR/PRC/authority/routing/impact/Product checks | 13–15, 20–25, 41, 48, 50 | implementation task-local and final verification |

### HUMAN_DOC

| Path | Responsibility | Design sections implemented | Contract consumers |
|---|---|---|---|
| `README.md` | Concise feature discovery and candidate/canonical boundary | 7, 10, 44, 45, 56 | new users |
| `docs/reference/workflows.md` | User-facing intent, mismatch, review, reconcile, and regeneration flow | 8, 10–11, 21–37, 44 | workflow users |
| `docs/concepts/review-suite.md` | Conceptual lifecycle and authority distinction | 5–7, 12, 19, 27, 35–37, 46 | users learning the suite |
| `docs/getting-started/quick-start.md` | Minimal branch/PR review entry point and explicit next action | 10, 37, 44 | new users |

### READ_ONLY_REFERENCE

| Path | Why read-only for this feature |
|---|---|
| `SKILL.md` | Existing evidence-first, ownership, completion, and no-runtime-work rules are preserved. |
| `references/projection-lifecycle.md` | Existing `PRJ-*`, revision, freshness, and explicit regeneration authority remains unchanged. |
| `references/projection-regeneration.md` | Existing `RG-*` explicit execution remains unchanged. |
| `references/projection-gates-and-packages.md` | Existing package closeout policies remain unchanged. |
| `references/projection-verification.md` | V1–V4 and accepted projection verification remain unchanged. |
| `references/technical-documentation.md` | Existing factual projection and API operation-completeness semantics remain unchanged except for consuming accepted post-reconciliation state. |
| `references/technical-model-coverage.md` | Existing coverage authority remains the sole authority; only Change Review routing references it. |
| `capabilities/code-quality-review/SKILL.md` | CQ capability boundary and Product authorization remain authoritative. |
| `capabilities/test-review/SKILL.md` | TE methodology and accepted execution evidence remain authoritative. |
| `capabilities/test-review/references/test-engineering-contract.md` | CC ownership and compatibility adjudication remain authoritative except candidate input references. |
| `references/review-method.md` | Existing Architecture methodology remains the owner of accepted interpretation. |

No new capability directory, projection family, runtime subsystem, database, or generic menu engine is planned.

## Frozen Contract Decisions

Implementation must use the following exact concepts from the approved design:

```text
CHANGE_REVIEW
RECONCILE_CHANGE                 # contextual action, not startup intent
BASELINE_MATCH | BASELINE_ADVANCED | BASELINE_DIVERGED | BASELINE_UNKNOWN
EXACT | TREE_EQUIVALENT | ADVANCED | DIVERGED | UNAVAILABLE
CR-* / CF-* / CRF-*              # review-qualified only
CHANGE_REVIEW_CANDIDATE          # read-only execution mode
CONTEXT_EXPANSION_REQUIRED
NO_EXPECTED_IMPACT | LIKELY_AFFECTED |
DEFINITELY_AFFECTED_IF_ACCEPTED | UNKNOWN_IMPACT
```

`CR-*` is the review identity. `CF-*` and `CRF-*` are scoped under a CR and never global semantic families. Existing finding effects are `UNAFFECTED`, `POTENTIALLY_RESOLVES`, `MITIGATES`, `WORSENS`, `INVALIDATES_PRIOR_ASSUMPTION`, and `UNKNOWN_IMPACT`. Candidate change types are `ADDED`, `MODIFIED`, `REMOVED`, and `MOVED`; candidate assessment effects are a separate axis.

## Validation Strategy

Use the single Markdown artifact as deterministic contract evidence. Each matrix row cites the normative section/file that establishes the outcome and clearly labels contract expectation versus runtime proof. No endpoint scanner, Git simulator, PR service, parser, or test runner is introduced. Run `rg` checks for required identifiers, `git diff --check`, and a final inspection of changed files. The artifact must preserve pre-change rows bound to the canonical base, then append post-change closure rows; it must not replace the original evidence.

## Fail-First Baseline

Before any normative edit, create `tests/change-review-baseline-reconciliation-validation.md` with a `PRE-CHANGE` section bound to `5be8bbd8a5869bb74d4a2ee804c695cb19620008` and these expected gaps:

| ID | Pre-change observation | Expected |
|---|---|---|
| FF01 | accepted A/current B has no first-class Change Review mismatch route | GAP PRESENT |
| FF02 | no immutable base/candidate CR binding | GAP PRESENT |
| FF03 | no review-local candidate fact/finding authority barrier | GAP PRESENT |
| FF04 | no exact TREE_EQUIVALENT proof contract | GAP PRESENT |
| FF05 | no contextual reconciliation dispatch through owners | GAP PRESENT |
| FF06 | no complete baseline-advancement gate after reconciliation | GAP PRESENT |
| FF07 | candidate projection prediction is not separated from actual Stage B impact | GAP PRESENT |
| FF08 | branch/commit/PR candidate mode is not first-class | GAP PRESENT |

Run before normative changes:

```bash
git rev-parse HEAD
rg -n "FF01|FF08|PRE-CHANGE|5be8bbd8" tests/change-review-baseline-reconciliation-validation.md
git diff --check
```

Expected: the file records 8/8 `GAP PRESENT` rows and no post-change claim.

---

## Task 1: Add fail-first evidence and Change Review startup routing

**Files:**

- Create: `tests/change-review-baseline-reconciliation-validation.md`
- Modify: `references/session-orchestration.md`
- Modify: `references/review-modes-and-orchestration.md`
- Read-only: `references/revalidation-and-freshness.md`

**Interfaces:**

- Consumes: existing six-intent routing, Product pinning, `requested_work` /\n  `resolved_work`, dirty/baseline metadata, and `PROJECTION_REPAIR` guard.
- Produces: `CHANGE_REVIEW` intent; baseline relation classification; explicit mismatch outcomes; candidate-mode requested/resolved work shape for Tasks 2–4.

- [ ] **Step 1: Write and run fail-first rows.** Use the exact FF01–FF08 table above. Expected: 8/8 `GAP PRESENT`, bound to the base commit.
- [ ] **Step 2: Add the intent contract.** Add `CHANGE_REVIEW` to the intent family without adding a capability. Define the startup order `Session Intent → Scope Context → Baseline Relation → Contextual Available Actions → Requested Work → Capability/Output Configuration → Dependency Resolution → Authorization Summary → Substantive Work`.
- [ ] **Step 3: Define mismatch routes.** `RESUME` returns `SOURCE_BASELINE_MISMATCH`, `EXTEND` returns `BASELINE_RECONCILIATION_REQUIRED`, and current `PROJECTION_REPAIR` blocks until source reconciliation. Each offers review/revalidation and contextual reconciliation only; none auto-runs.
- [ ] **Step 4: Define Change Review requested/resolved work.** Requested lenses/outputs remain user intent; resolved diff/evidence/owner slices are internal dependencies. Candidate mode is read-only and does not populate selected capabilities from internal dependencies.
- [ ] **Step 5: Add post-change rows FF01–FF08** describing closure and run:
```bash
rg -n "CHANGE_REVIEW|BASELINE_MATCH|SOURCE_BASELINE_MISMATCH|BASELINE_RECONCILIATION_REQUIRED" references/session-orchestration.md references/review-modes-and-orchestration.md
git diff --check
```
Expected: all routing terms are defined once in their owning contracts and FF01–FF08 remain visibly pre-change.
- [ ] **Step 6: Commit.**
```bash
git add tests/change-review-baseline-reconciliation-validation.md references/session-orchestration.md references/review-modes-and-orchestration.md
git commit -m "feat: add change review startup routing"
```

## Task 2: Freeze immutable source bindings and candidate artifact barrier

**Files:**

- Modify: `references/shared-evidence-model.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/shared-technical-model.md`
- Modify: `references/technical-model-dependencies.md`
- Read-only: `references/product-multi-project-review.md`

**Interfaces:**

- Consumes: Task 1 `CHANGE_REVIEW` routing and existing `WS-*`/`EV-*`, STM identity, Product baseline, and dependency contracts.
- Produces: exact `base_binding`/`candidate_binding`; CR/CF/CRF contract; candidate authority barrier consumed by every later owner and projection.

- [ ] **Step 1: Add the source binding shape** with `repository_id`, `project_binding`, optional `product_member_binding`, `ref_input`, `resolved_commit`, `resolved_tree`, `qualification`, and source/evidence availability. Persist separate base and candidate bindings; never only branch names or checkout state.
- [ ] **Step 2: Define CR/CF/CRF identity scope and states.** CR is stable and review-qualified; CF/CRF uniqueness is within CR. Define CR lifecycle and `decision: NOT_RECONCILED | RECONCILED | KEPT_REVIEW_ONLY`; preserve candidate status separate from canonical lifecycle.
- [ ] **Step 3: Add the barrier** to STM acceptance, dependency resolution, CQ, TE, Architecture, CC, Product, and projection dependency rules: candidate records are accepted only as review evidence, routing context, historical comparison, or reconciliation input. They cannot satisfy accepted gates.
- [ ] **Step 4: Define candidate execution mode** `CHANGE_REVIEW_CANDIDATE` and require owner outputs in this mode to be candidate-qualified. Canonical writes are legal only inside explicit `RECONCILE_CHANGE` dispatch.
- [ ] **Step 5: Validate forbidden use cases** in the artifact: CF as STM, CRF as CQ, candidate TE as `TESTED`, candidate result as CC compatibility, candidate Product state, and CF as projection dependency. Run:
```bash
rg -n "base_binding|candidate_binding|CHANGE_REVIEW_CANDIDATE|candidate.*cannot|CR-|CF-|CRF-" references/shared-evidence-model.md references/shared-technical-model.md references/technical-model-dependencies.md references/review-modes-and-orchestration.md
git diff --check
```
Expected: every barrier is explicit and no candidate token is an accepted dependency.
- [ ] **Step 6: Commit.**
```bash
git add references/shared-evidence-model.md references/review-modes-and-orchestration.md references/shared-technical-model.md references/technical-model-dependencies.md
git commit -m "feat: bind change review candidates immutably"
```
+
## Task 3: Add Change Inventory and bounded delta discovery

**Files:**

- Modify: `references/shared-evidence-model.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/technical-model-dependencies.md`
- Read-only: `references/shared-technical-model.md`

**Interfaces:**

- Consumes: immutable bindings and accepted canonical references from Task 2.
- Produces: bounded Change Inventory, candidate additions/modifications/removals, `CONTEXT_EXPANSION_REQUIRED`, and review completeness dimensions.

- [ ] **Step 1: Define inventory fields** for source delta type `ADDED | MODIFIED | REMOVED | MOVED`, source path/evidence binding, candidate surface kind, correlated accepted ref, candidate ref, and limitation. Cover components, interfaces/operations, integrations, data stores/migrations, events, flows, auth/config, and contracts without cloning STM schema.
- [ ] **Step 2: Define discovery flow** as diff-guided, bounded discovery. A changed path starts discovery but proves nothing by itself. If a changed boundary references an uninspected material dependency, persist `CONTEXT_EXPANSION_REQUIRED` and expand only that evidence slice.
- [ ] **Step 3: Define review completeness** as bounded `change_inventory`, `affected_authority_coverage`, `candidate_discovery_coverage`, and `selected_capability_assessment`, each `COMPLETE | PARTIAL | UNKNOWN`, plus explicit `unknown_impact`. Completion cannot claim exhaustive repository impact.
- [ ] **Step 4: Validate new-fact and removal cases** where no accepted edge exists, and where canonical deletion is prohibited before reconciliation. Run:
```bash
rg -n "Change Inventory|ADDED|MODIFIED|REMOVED|MOVED|CONTEXT_EXPANSION_REQUIRED|change_inventory|candidate_discovery_coverage" references/shared-evidence-model.md references/review-modes-and-orchestration.md references/technical-model-dependencies.md
git diff --check
```
Expected: the artifact distinguishes factual inventory from assessment and records bounded unknowns.
- [ ] **Step 5: Commit.**
```bash
git add references/shared-evidence-model.md references/review-modes-and-orchestration.md references/technical-model-dependencies.md
git commit -m "feat: define bounded change inventory discovery"
```

## Task 4: Add candidate assessment and finding-effect contracts

**Files:**

- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/ownership-and-scenarios.md`
- Modify: `capabilities/code-quality-review/references/code-quality-contract.md`
- Modify: `capabilities/test-review/references/test-engineering-contract.md`
- Read-only: `references/shared-technical-model.md`

**Interfaces:**

- Consumes: Task 2 CR/CF/CRF barrier and Task 3 Change Inventory.
- Produces: candidate-qualified assessments, existing finding effects, capability-lens outputs, and owner-promotion traceability.

- [ ] **Step 1: Define Change Assessment** separately from inventory with affected existing facts, candidate facts, removed facts, existing finding effects, candidate findings, Architecture/Test/contract impacts, risk, and limitations.
- [ ] **Step 2: Define exact effect axes.** Change types remain `ADDED | MODIFIED | REMOVED | MOVED`; assessment effects are `INTRODUCES_RISK | WORSENS_EXISTING | MITIGATES | POTENTIALLY_RESOLVES | NO_MATERIAL_IMPACT | UNKNOWN_IMPACT`; existing finding effects use the six frozen vocabulary values.
- [ ] **Step 3: Prohibit candidate lifecycle misuse.** `RESOLVED`, `CLOSED`, and `ACCEPTED` may only quote an existing canonical state; they are not CRF outcomes. Add `candidate_origin: CR-*/CRF-*` traceability for later owner records.
- [ ] **Step 4: Add minimal candidate owner references:** Architecture records candidate interpretation only; CQ references operation/property evidence and CRF; TE references changed assurance needs without `TESTED`; CC consumes provider/consumer candidate refs but adjudicates compatibility itself.
- [ ] **Step 5: Validate the dual effect cases**: a modified change can potentially resolve an existing finding; one candidate can fix HIGH and add MEDIUM. Run:
```bash
rg -n "POTENTIALLY_RESOLVES|INVALIDATES_PRIOR_ASSUMPTION|INTRODUCES_RISK|candidate_origin|CHANGE_REVIEW_CANDIDATE|TESTED" references/review-modes-and-orchestration.md references/ownership-and-scenarios.md capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md
git diff --check
```
Expected: candidate effects are visible and canonical lifecycle remains owner-controlled.
- [ ] **Step 6: Commit.**
```bash
git add references/review-modes-and-orchestration.md references/ownership-and-scenarios.md capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md
git commit -m "feat: separate change assessment from canonical findings"
```

## Task 5: Define review reuse, equivalence, and candidate evolution

**Files:**

- Modify: `references/session-orchestration.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/shared-evidence-model.md`
- Modify: `references/product-multi-project-review.md`
- Read-only: `references/revalidation-and-freshness.md`

**Interfaces:**

- Consumes: Task 2 immutable bindings and Task 4 completed CR lifecycle.
- Produces: exact reuse classifier and proof contract used by contextual reconciliation and review update routing.

- [ ] **Step 1: Define `EXACT`** as same repository, exact candidate commit and tree, exact Project/Product qualification, complete review, usable evidence, and compatible scope/lenses.
- [ ] **Step 2: Define `TREE_EQUIVALENT` proof** with two permitted levels: `WHOLE_TREE_EQUAL` requires equal resolved whole-tree identity plus matching repository/qualification/scope; `FROZEN_RELEVANT_SCOPE_EQUAL` requires the persisted manifest of included paths/selectors/member bindings, equal relevant-tree fingerprint, and proof that omitted paths cannot affect the reviewed scope. Inspected-files coincidence, branch name, ancestry, fuzzy text, or missing proof yields `NOT_TREE_EQUIVALENT`.
- [ ] **Step 3: Define `ADVANCED` and `DIVERGED`.** An advanced candidate gets a linked immutable incremental CR (`B→C`); a diverged candidate requires a new CR. A completed CR is never rewritten to change its base/candidate meaning.
- [ ] **Step 4: Define merge cases:** no-ff and squash can reuse only after whole-tree or frozen-scope proof; conflict-resolution changes require a new or supplemental review; partial cherry-pick is conditional only with independently decomposable subset proof.
- [ ] **Step 5: Define Product reuse rejection** when member vectors, selected Product revision, or member qualification differ, even if text/tree appears equal. Define candidate comparison as a view over immutable CRs.
- [ ] **Step 6: Validate MR01–MR10** in the single artifact and run:
```bash
rg -n "TREE_EQUIVALENT|WHOLE_TREE_EQUAL|FROZEN_RELEVANT_SCOPE_EQUAL|ADVANCED|DIVERGED|cherry-pick|squash|conflict|member vector" references/session-orchestration.md references/review-modes-and-orchestration.md references/shared-evidence-model.md references/product-multi-project-review.md
git diff --check
```
Expected: 10/10 merge/reuse cases are deterministic and no SHA-only path exists.
- [ ] **Step 7: Commit.**
```bash
git add references/session-orchestration.md references/review-modes-and-orchestration.md references/shared-evidence-model.md references/product-multi-project-review.md
git commit -m "feat: define safe change review reuse"
```
+
## Task 6: Add contextual RECONCILE_CHANGE and baseline advancement gate

**Files:**

- Modify: references/session-orchestration.md
- Modify: references/review-modes-and-orchestration.md
- Modify: references/shared-technical-model.md
- Modify: references/technical-model-dependencies.md
- Read-only: references/revalidation-and-freshness.md, references/product-multi-project-review.md

**Interfaces:**

- Consumes: reusable completed CR, CF/CRF evidence, exact candidate binding, owner contracts from Tasks 2–5.
- Produces: contextual reconciliation eligibility, owner dispatch, accepted-delta accounting, and baseline advancement gate.

- [ ] **Step 1: Define eligibility** as completed CR, reusable candidate state, exact intended binding, usable evidence, bounded material-delta accounting, and explicit confirmation. Non-reusable or incomplete CRs cannot dispatch.
- [ ] **Step 2: Define owner dispatch**: CF to Technical Model Gate; Architecture assessment to Architecture authority; CRF/effects to CQ; test impact to TE; provider/consumer contract impact to CC; Product composition through existing Product semantics. Record owner result and candidate_origin without reusing candidate identity.
- [ ] **Step 3: Define baseline advancement** with exact gate BASELINE_ADVANCE_ALLOWED: exact intended source binding, all material delta accounted, required owners complete, required technical/coverage gates satisfied, and policy-explicit handling of unknowns. Partial reconciliation never completes the baseline; open findings may remain when existing policy allows.
- [ ] **Step 4: Define source-change invalidation** during reconciliation: if the candidate commit/tree or qualified vector changes, discard eligibility and classify reuse again; do not mutate the CR or advance baseline.
- [ ] **Step 5: Validate PRC01–PRC05** and the case that a HIGH finding is resolved while a MEDIUM finding remains open. Run:
```bash
rg -n "RECONCILE_CHANGE|BASELINE_ADVANCE_ALLOWED|candidate_origin|partial reconciliation|open findings|exact intended" references/session-orchestration.md references/review-modes-and-orchestration.md references/shared-technical-model.md references/technical-model-dependencies.md
git diff --check
```
Expected: reconciliation is contextual, owner-routed, and baseline advancement is not release approval.
- [ ] **Step 6: Commit.**
```bash
git add references/session-orchestration.md references/review-modes-and-orchestration.md references/shared-technical-model.md references/technical-model-dependencies.md
git commit -m "feat: route change reconciliation through owners"
```

## Task 7: Integrate RESUME, REVALIDATE, EXTEND, PROJECTION_REPAIR, USE_EXISTING, and NEW

**Files:**

- Modify: references/session-orchestration.md
- Modify: references/review-modes-and-orchestration.md
- Modify: references/revalidation-and-freshness.md
- Read-only: references/projection-lifecycle.md, references/projection-gates-and-packages.md

**Interfaces:**

- Consumes: Tasks 1, 5, and 6 baseline relation/reuse/reconciliation contracts.
- Produces: deterministic lifecycle routing for all existing intents and the new intent.

- [ ] **Step 1: Preserve accepted-baseline behavior** for USE_EXISTING and NEW; show accepted A versus current B, and never infer current B from accepted package A.
- [ ] **Step 2: Define RESUME**: match restores; advanced/diverged/unknown returns SOURCE_BASELINE_MISMATCH, offers review/revalidation/reusable reconcile, and performs none automatically.
- [ ] **Step 3: Define REVALIDATE** as accepted-state reevaluation. A complete CR is routing evidence only; it cannot satisfy the revalidation gate or bypass owner adjudication.
- [ ] **Step 4: Define EXTEND** mismatch as BASELINE_RECONCILIATION_REQUIRED; after accepted B, it may perform only the requested additive extension. No implicit review-plus-reconcile-plus-extend chain is allowed.
- [ ] **Step 5: Define PROJECTION_REPAIR** as current-only when source matches; mismatch blocks current repair. Do not add a new historical-repair mode.
- [ ] **Step 6: Validate CR01–CR04, CR28, CR30–CR36 and the ten intent-routing cases** in the artifact. Run:
```bash
rg -n "SOURCE_BASELINE_MISMATCH|BASELINE_RECONCILIATION_REQUIRED|USE_EXISTING|CHANGE_REVIEW|REVALIDATE|EXTEND|PROJECTION_REPAIR|RECONCILE_CHANGE" references/session-orchestration.md references/review-modes-and-orchestration.md references/revalidation-and-freshness.md
git diff --check
```
Expected: no existing intent silently treats changed source as accepted current state.
- [ ] **Step 7: Commit.**
```bash
git add references/session-orchestration.md references/review-modes-and-orchestration.md references/revalidation-and-freshness.md
git commit -m "feat: guard existing intents against source mismatch"
```

## Task 8: Separate predicted impact from actual impact and qualify Product candidates

**Files:**

- Modify: references/review-modes-and-orchestration.md
- Modify: references/projection-impact.md
- Modify: references/product-multi-project-review.md
- Read-only: references/projection-lifecycle.md, references/projection-dependencies.md

**Interfaces:**

- Consumes: CR assessment, exact source bindings, accepted owner results, and existing Stage B impact authority.
- Produces: candidate prediction record, post-reconciliation actual impact handoff, and qualified Product vector semantics.

- [ ] **Step 1: Define prediction** using only NO_EXPECTED_IMPACT, LIKELY_AFFECTED, DEFINITELY_AFFECTED_IF_ACCEPTED, and UNKNOWN_IMPACT, qualified to CR/base/candidate/scope. Prohibit candidate writes of CURRENT, STALE, and BLOCKED.
- [ ] **Step 2: Define actual handoff**: owner reconciliation stabilizes accepted semantic state, then existing Projection Impact Analysis runs once for the accepted delta and persists existing reasons/freshness. Prediction is retained unchanged.
- [ ] **Step 3: Define Product Change Review** over exact member vectors; member A/B effects are separately bound, and a missing member/source causes explicit limitation or context expansion. No Product-wide unqualified delta is admitted.
- [ ] **Step 4: Preserve explicit regeneration** with existing RG-*; declining leaves affected projections stale/deferred and does not change canonical semantics.
- [ ] **Step 5: Validate six projection separation cases and six Product cases** in the artifact. Run:
```bash
rg -n "NO_EXPECTED_IMPACT|LIKELY_AFFECTED|DEFINITELY_AFFECTED_IF_ACCEPTED|predicted|actual|Projection Impact|member vector|Product" references/review-modes-and-orchestration.md references/projection-impact.md references/product-multi-project-review.md
git diff --check
```
Expected: candidate prediction cannot create actual freshness and Product membership cannot flatten source state.
- [ ] **Step 6: Commit.**
```bash
git add references/review-modes-and-orchestration.md references/projection-impact.md references/product-multi-project-review.md
git commit -m "feat: separate predicted and accepted projection impact"
```

## Task 9: Add candidate-mode capability and API operation references

**Files:**

- Modify: references/ownership-and-scenarios.md
- Modify: capabilities/code-quality-review/SKILL.md
- Modify: capabilities/code-quality-review/references/code-quality-contract.md
- Modify: capabilities/test-review/SKILL.md
- Modify: capabilities/test-review/references/test-engineering-contract.md
- Modify: references/shared-technical-model.md
- Read-only: references/technical-documentation.md and CC sections of capabilities/test-review/references/test-engineering-contract.md

**Interfaces:**

- Consumes: Task 2 candidate execution mode and Task 4 assessment contracts.
- Produces: candidate-qualified Architecture/CQ/TE/CC references that preserve all existing semantic ownership.

- [ ] **Step 1: Add candidate Architecture mode**: candidate interpretation and affected accepted refs are review-local; no accepted RF-* mutation.
- [ ] **Step 2: Add candidate CQ mode**: CRF can reference operation/property/boundary evidence; owner later decides new, duplicate, reject, or canonical finding. Candidate cannot decide CQ lifecycle.
- [ ] **Step 3: Add candidate TE mode**: candidate may identify new/invalidated assurance cases; generated cases do not become executed or TESTED.
- [ ] **Step 4: Add candidate CC routing**: candidate provider/consumer refs are inputs; same method/path is not compatibility; CC remains adjudicator and no new CC family is created.
- [ ] **Step 5: Preserve API operation completeness**: candidate additions/removals/method/path/auth/schema/limit changes remain CFs; accepted operation inventory and coverage update only through Technical Model Gate after reconciliation.
- [ ] **Step 6: Validate candidate authority cases** for CQ, TE, Architecture, CC, STM, Product, and projection dependencies. Run:
```bash
rg -n "CHANGE_REVIEW_CANDIDATE|candidate|canonical|TESTED|compatible|Technical Model Gate|RF-|CQ-|CC-" references/ownership-and-scenarios.md capabilities/code-quality-review/SKILL.md capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md references/shared-technical-model.md
git diff --check
```
Expected: no capability can promote candidate evidence or create a shadow authority.
- [ ] **Step 7: Commit.**
```bash
git add references/ownership-and-scenarios.md capabilities/code-quality-review/SKILL.md capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md references/shared-technical-model.md
git commit -m "feat: isolate candidate capability assessments"
```

## Task 10: Update human docs and complete deterministic validation

**Files:**

- Modify: README.md
- Modify: docs/reference/workflows.md
- Modify: docs/concepts/review-suite.md
- Modify: docs/getting-started/quick-start.md
- Modify: tests/change-review-baseline-reconciliation-validation.md
- Read-only: all normative files changed in Tasks 1–9 and approved design/review artifacts

**Interfaces:**

- Consumes: all finalized contracts from Tasks 1–9.
- Produces: user-facing explanation, complete validation evidence, and implementation-ready closeout evidence.

- [ ] **Step 1: Document** branch/commit/PR review, accepted-versus-candidate state, explicit reconciliation, mismatch routing, safe reuse after equivalent merge, and explicit regeneration. Keep CR/CF/CRF jargon out of beginner copy unless needed.
- [ ] **Step 2: Append deterministic matrices** to the validation artifact:
  - CR01–CR36 with source relation, allowed intent, mutation, candidate/canonical/projection state, and next action;
  - MR01–MR10 exact/tree/scope reuse;
  - PRC01–PRC05 partial reconciliation;
  - 8 authority-barrier cases;
  - 10 intent-routing cases;
  - 6 projection prediction/actual cases;
  - 6 Product qualification cases.
- [ ] **Step 3: Add exact complete-claim checks**: no CR prediction may claim accepted freshness; no review-only finding may use canonical lifecycle; no baseline advances on COMPLETE alone.
- [ ] **Step 4: Run the final checks:**
```bash
rg -n "CHANGE_REVIEW|RECONCILE_CHANGE|BASELINE_MATCH|BASELINE_ADVANCED|BASELINE_DIVERGED|BASELINE_UNKNOWN|TREE_EQUIVALENT|WHOLE_TREE_EQUAL|FROZEN_RELEVANT_SCOPE_EQUAL|CONTEXT_EXPANSION_REQUIRED|UNKNOWN_IMPACT|candidate_origin|CR01|CR36|MR01|MR10|PRC01|PRC05" references README.md docs tests/change-review-baseline-reconciliation-validation.md
rg -n "placeholder|deferred architecture decision|architecture contradiction" docs/superpowers/plans/2026-09-11-change-review-baseline-reconciliation-implementation-plan.md
git diff --check
```
Expected: all required tokens exist in owning contracts and the plan has no placeholders.
- [ ] **Step 5: Verify scope:**
```bash
git status --short
git diff --name-status <plan-head>..HEAD
```
Expected: only File Map files and no design/plan/review artifact modification.
- [ ] **Step 6: Commit.**
```bash
git add README.md docs/reference/workflows.md docs/concepts/review-suite.md docs/getting-started/quick-start.md tests/change-review-baseline-reconciliation-validation.md
git commit -m "docs: document change review lifecycle"
```

The implementer must stop and report STOP_HARNESS_EXPANSION if validation begins to introduce a parser, DSL, runner, Git simulator, PR service, or generic workflow framework.
+
## Independent Implementation Review

After Task 10, stop implementation and perform one separate read-only review of the implementation feature branch. The reviewer reads the approved design, this plan, all 10 task commits, and the final validation artifact. The review verifies candidate/canonical authority barriers, exact base/candidate binding, TREE_EQUIVALENT proof, advanced/diverged and merge/squash/cherry-pick handling, partial reconciliation, mismatch routing, baseline advancement, prediction/actual projection separation, Product qualification, API operation completeness, backward compatibility, and validation proportionality.

The review must report HIGH, MEDIUM, and LOW findings. If HIGH or MEDIUM findings exist, implementation stops; remediation is a separate bounded task followed by one re-review of changed areas. The independent review does not modify files, promote findings, alter baseline, regenerate projections, or merge the branch.

## Promotion Readiness

Promotion is not part of implementation. Before a future promotion request, verify the implementation branch has the 10 planned commits, clean tracked state, no design/plan artifact edits, no unrelated files, and a successful git diff --check. A future promotion must separately re-fetch canonical main, verify it has not moved, perform a normal non-squashed merge, run integrated checks, and push only with explicit authorization.

## Backward Compatibility

The implementation must preserve the six existing intents and all existing accepted packages, STM facts, findings, tests, Product vectors, projection identities, and lifecycle records. Missing Change Review metadata in a historical package does not imply that the package is changed or current for a different source. It routes to BASELINE_UNKNOWN until the source relation is resolved. Existing accepted state remains valid for its own baseline; only a requested candidate comparison or reconciliation adds CR/CF/CRF records.

## Migration

Migration classification is COMPATIBLE_EXTENSION. No historical package rewrite, CR backfill, candidate fact synthesis, candidate finding synthesis, projection regeneration, or baseline advancement occurs as a storage migration. New records are additive and source-qualified. Existing owners continue to interpret their historical records under their existing contracts.

## Authority Audit

The implementation closeout must show:

| Authority | Expected count/status |
|---|---|
| top-level semantic capabilities | exactly 3 |
| new orchestration intent | exactly 1: CHANGE_REVIEW |
| new startup capability | 0 |
| new accepted factual authority | 0 |
| new CQ authority | 0 |
| new projection authority | 0 |
| new Product authority | 0 |
| new runtime execution authority | 0 |
| RECONCILE_CHANGE | contextual coordinator action only |
| candidate CR/CF/CRF downstream use | evidence/routing/reconciliation input only |
| automatic regeneration | 0 |

Run:
```bash
rg -n "CHANGE_REVIEW|RECONCILE_CHANGE|CR-|CF-|CRF-|candidate.*cannot|top-level semantic capabilities|automatic regeneration" references capabilities tests
git diff --check
```

Expected: the audit has no second owner, no shadow registry, and no candidate-to-canonical shortcut.

## Design-to-Task Traceability

| Approved design area | Implementing task |
|---|---|
| Problem, goals, non-goals, invariants | Tasks 1–10 |
| baseline relation and source resolution | Tasks 1–2, 5, 7 |
| Change Review intent/configuration | Task 1 |
| CR artifact and candidate barrier | Task 2 |
| inventory and discovery | Task 3 |
| assessment, candidate facts/findings, effects | Task 4 |
| reuse, equivalence, advanced/diverged candidates | Task 5 |
| reconciliation and baseline advancement | Task 6 |
| REVALIDATE/RESUME/EXTEND/PROJECTION_REPAIR/USE_EXISTING/NEW | Task 7 |
| prediction, actual impact, regeneration boundary | Task 8 |
| CQ/TE/Architecture/STM/CC/API ownership | Task 9 |
| Product/multi-project behavior | Tasks 5, 8, 10 |
| UX, security, backward compatibility, migration | Tasks 1, 5, 7, 10 |
| CR01–CR36 and acceptance criteria | Task 10 |

Every approved design decision is assigned to at least one task; no task is permitted to reopen it.

## Scenario-to-Validation Traceability

| Scenario group | Validation location | Required result |
|---|---|---|
| FF01–FF08 | validation artifact PRE-CHANGE and closure sections | 8/8 mapped; pre-change evidence retained |
| CR01–CR36 | Change Review scenario matrix | 36/36 deterministic |
| MR01–MR10 | reuse matrix | 10/10 deterministic |
| PRC01–PRC05 | reconciliation matrix | 5/5 deterministic |
| candidate barrier | authority matrix | 8/8 prevented |
| intent routing | intent matrix | 10/10 deterministic |
| projection separation | prediction/actual matrix | 6/6 deterministic |
| Product qualification | Product matrix | 6/6 deterministic |
| complete-claim guard | validation artifact claim checks | all forbidden claims rejected unless explicitly qualified |
| API operation completeness | candidate API rows and owner checks | existing operation authority preserved |

## Final Acceptance Criteria

The implementation is ready for independent review only when:

- [ ] CHANGE_REVIEW is an orchestration intent and no new capability exists.
- [ ] Base and candidate exact source bindings are persisted before review.
- [ ] CR/CF/CRF are non-authoritative and review-qualified.
- [ ] FF01–FF08 remain intact and closure is evidenced.
- [ ] TREE_EQUIVALENT has whole-tree and frozen-relevant-scope proof rules.
- [ ] Advanced/diverged/merge/squash/partial-cherry behavior is deterministic.
- [ ] RECONCILE_CHANGE is contextual, explicit, and owner-routed.
- [ ] Partial reconciliation cannot advance the whole baseline.
- [ ] Existing findings are not resolved by Change Review alone.
- [ ] Candidate prediction cannot write Stage B freshness.
- [ ] Actual Projection Impact Analysis runs only after accepted reconciliation.
- [ ] Regeneration remains explicit.
- [ ] RESUME, EXTEND, and current PROJECTION_REPAIR stop on mismatch.
- [ ] Product member vectors never flatten.
- [ ] API operation completeness and requested/resolved separation remain intact.
- [ ] CR01–CR36, MR01–MR10, PRC01–PRC05 and all authority/routing matrices pass.
- [ ] No runtime or generic validation framework was introduced.
- [ ] Human documentation is synchronized.
- [ ] git diff --check passes and only mapped files changed.
- [ ] The one independent implementation review is complete with zero HIGH/MEDIUM findings.

