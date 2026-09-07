# Stage E — Product / Multi-Project Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Add opt-in Product / multi-Project review support while preserving
Project-local semantic authority and existing single-project behavior.

**Architecture:** Implement approved Option C — Hybrid. A focused Product
contract owns Product context, identity, membership, baseline vectors, routing,
and cross-project coordination; STM, Architecture Review, Test Engineering,
Code Quality, projection, package, and authorization contracts retain their
existing semantic ownership. State remains file-based in the coordinator
review workspace.

**Tech Stack:** Markdown normative references, Markdown pressure/contract
validation artifacts, existing `working/INDEX.md` coordinator state, and the
existing `WS-*`, `EV-*`, STM, `RF-*`, `CQ-*`, `CQRA-*`, Test Engineering,
`PRJ-*`, `RG-*`, and `PKG-*` families.

**Spec:** `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-design.md`

## Global Constraints

- Product mode is opt-in; single-project review requires no Product state.
- Product identity, Product revision, and Product baseline are distinct.
- `PROD-*` is the only new identity family; technical/evidence/capability/projection/package families are reused.
- Product baseline is an exact multi-source vector and is never one Git SHA.
- STM remains factual authority and the Technical Model Gate remains its accepted-fact writer.
- Architecture Review owns `RF-*`; Code Quality owns `CQ-*`/`CQRA-*`; Test Engineering owns `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, and `TASK-*`.
- Reports, summaries, indexes, projections, and packages are never authority.
- Relation, dependency, reverse index, and impact result remain distinct.
- `REVALIDATE` is impact-driven/minimum-slice; `EXTEND` is additive.
- Source availability, review coverage, semantic availability, projection freshness, and package gate result remain independent.
- Product membership grants no repository, worktree, code, test, commit, PR, push, or deployment permission.
- Stage B package policies and `ALL_SCOPED_CURRENT` retain their existing scoped meanings.
- `PRJ-*` and `RG-*` remain distinct; regeneration is explicit and never automatic.
- No database, service, graph database, vector/RAG infrastructure, daemon, or generic registry backend is introduced.
- Approved Design, Discovery, reviews, roadmap, and normative files are not modified by this planning task.

---

## 1. Approved baseline and scope

Implementation planning starts from Design checkpoint
`25c08ffcb741d7d23056a0ef84c59f17610f804f`, subject
`docs: record approved Stage E design`.

Approved semantic inputs:

- `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-design.md`;
- `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-discovery.md`;
- `docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-design-review.md`;
- `docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-design-rereview.md`;
- the approved Discovery review and targeted rereview.

The Design resolves D-01 through D-04. Mechanical serialization, filenames
under the approved ownership classes, indexes, and UI/CLI details may be
chosen during implementation. Identity, ownership, lifecycle, provenance,
scope, package, authorization, and revalidation semantics may not be changed.

In scope:

1. focused Product contract;
2. Product/Project identity, membership, revisions, baselines, coherency, and availability;
3. qualified evidence, STM relations, dependencies, and impact routing;
4. Product `REVALIDATE`, `EXTEND`, authorization, projections, and packages;
5. Product-scoped Architecture Review, Code Quality, and Test Engineering;
6. deterministic pressure and backward-compatibility validation.

Out of scope: repository automation, source modification, execution, migration
engine, external service, compatibility engine, Product nesting, and roadmap
publication during implementation.

## 2. Current contract inventory

| Authority | Current role | Planned treatment |
|---|---|---|
| `SKILL.md` | umbrella invariants/routing | `EXTEND` Product opt-in references only |
| `references/session-orchestration.md` | startup, selection, authorization, baseline | `EXTEND` Product routing and source binding |
| `references/review-modes-and-orchestration.md` | coordinator state, intents, resume | `EXTEND` Product fields, outputs, and gates |
| `references/shared-evidence-model.md` | `WS-*`/`EV-*` observations | `EXTEND` qualified multi-source Product evidence |
| `references/shared-technical-model.md` | STM factual authority/Gate | `EXTEND` qualified Product relations |
| `references/technical-model-dependencies.md` | dependency metadata and traversal | `EXTEND` qualified endpoints |
| `references/revalidation-and-freshness.md` | impact-driven change handling | `EXTEND` Product roots/preserved sets |
| `references/projection-lifecycle.md` | `PRJ-*` lifecycle | `EXTEND` Product scope metadata |
| `references/projection-impact.md` | impact before regeneration | `EXTEND` Product dependency propagation |
| `references/projection-regeneration.md` | `RG-*` execution | `EXTEND` frozen Product scope |
| `references/projection-gates-and-packages.md` | Stage B package authority | `EXTEND` Product finite declarations |
| `references/projection-dependencies.md` | exact/selector snapshots | `EXTEND` Product-qualified selectors |
| `references/technical-documentation.md` | `PRJ-TECH-DOC-*`, section/package semantics | `EXTEND` Product STM inputs and limitations |
| `references/technical-model-coverage.md` | accepted STM coverage | `EXTEND` Product coverage bindings |
| `references/projection-verification.md` | V1–V4 | `NO_CHANGE`; verify coverage |
| Architecture references | RF ownership, boundaries, verification, severity, reporting | `EXTEND` Product RF scope |
| `capabilities/test-review/SKILL.md` and `test-engineering-contract.md` | TE families, `TRS-*`, selectors/packages | `EXTEND` Product scope |
| Code Quality capability references | CQ/CQRA authority, lifecycle, projections | `EXTEND` Product allocation/scope |
| `docs/roadmap.md` | strategic status | read-only until final closeout |

## 3. Proposed file impact inventory

### Create

```text
references/product-multi-project-review.md
tests/pressure-scenario-132-product-single-project-compatibility.md
tests/pressure-scenario-133-product-three-clean-projects.md
tests/pressure-scenario-134-product-unavailable-member.md
tests/pressure-scenario-135-product-dirty-member.md
tests/pressure-scenario-136-product-baseline-advancement.md
tests/pressure-scenario-137-product-api-compatibility.md
tests/pressure-scenario-138-product-shared-component.md
tests/pressure-scenario-139-product-architecture-finding.md
tests/pressure-scenario-140-product-local-finding-isolation.md
tests/pressure-scenario-141-product-extend-add-project.md
tests/pressure-scenario-142-product-targeted-revalidate.md
tests/pressure-scenario-143-product-stale-projection.md
tests/pressure-scenario-144-product-compatible-old-version.md
tests/pressure-scenario-145-product-conflicting-evidence.md
tests/pressure-scenario-146-product-blocked-package.md
tests/pressure-scenario-147-product-two-products.md
tests/pressure-scenario-148-product-extend-requiredness.md
tests/pressure-scenario-149-product-single-member-transition.md
tests/stage-e-product-multi-project-contract-validation.md
tests/stage-e-product-multi-project-backward-compatibility.md
```

### Modify

```text
SKILL.md
references/session-orchestration.md
references/review-modes-and-orchestration.md
references/shared-evidence-model.md
references/shared-technical-model.md
references/technical-model-dependencies.md
references/revalidation-and-freshness.md
references/projection-lifecycle.md
references/projection-impact.md
references/projection-regeneration.md
references/projection-gates-and-packages.md
references/projection-dependencies.md
references/technical-documentation.md
references/technical-model-coverage.md
references/review-method.md
references/ownership-and-scenarios.md
references/boundary-contract-audit.md
references/independent-verification.md
references/root-boundary-adjudication.md
references/evidence-and-severity.md
references/report-contract.md
capabilities/test-review/SKILL.md
capabilities/test-review/references/test-engineering-contract.md
capabilities/code-quality-review/SKILL.md
capabilities/code-quality-review/references/code-quality-contract.md
capabilities/code-quality-review/references/code-quality-lifecycle.md
capabilities/code-quality-review/references/code-quality-projection.md
```

The following exact paths are `READ_ONLY` during implementation:

```text
references/projection-verification.md
tests/pressure-validation-matrix.md
tests/pressure-scenarios.md
docs/roadmap.md
references/remediation-roadmap-review.md
docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-discovery.md
docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-discovery-review.md
docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-discovery-rereview.md
docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-design.md
docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-design-review.md
docs/superpowers/reviews/2026-09-06-stage-e-product-multi-project-design-rereview.md
docs/superpowers/plans/2026-09-07-stage-e-product-multi-project-implementation-plan.md
docs/superpowers/reviews/2026-09-07-stage-e-product-multi-project-implementation-plan-review.md
```

The grouped `Architecture references` row above expands exactly to the seven
paths listed in the `MODIFY` block; it is not an open-ended file class. The
two existing test files are read-only conventions/input references, not
modified validation authorities. No source/runtime file, migration, CI file,
or service is in the inventory. Runtime Product state may be created only in
the approved coordinator `working/products/<PROD-key>/` namespace. The
inventory contains 21 `CREATE`, 27 `MODIFY`, and 13 `READ_ONLY` entries; every
implementation-relevant path has exactly one primary action.

## 3a. Contract-impact and implementation-classification matrix

| Surface/work | Classification | Exact owner and boundary |
|---|---|---|
| Focused Product reference | `NEW_CONTRACT` / `NEW_REFERENCE_REQUIRED` | `references/product-multi-project-review.md`; Product context only, links to existing owners. |
| Product identity, revision, membership, baseline | `EXTEND_CONTRACT` | Product reference plus session/review orchestration; no new backend. |
| Project descriptors and repository bindings | `ORCHESTRATION_CHANGE` | session and review-mode references; provenance/routing only. |
| Product WS/EV | `EXTEND_CONTRACT` | `references/shared-evidence-model.md`; observations only. |
| Product STM relations | `EXTEND_CONTRACT` | `references/shared-technical-model.md`; Technical Model Gate authority. |
| Qualified dependency metadata | `EXTEND_CONTRACT` | `references/technical-model-dependencies.md`; dependent owns edge. |
| Product `REVALIDATE`/`EXTEND` | `EXTEND_CONTRACT` + `ORCHESTRATION_CHANGE` | `references/revalidation-and-freshness.md`, session/review modes. |
| Product authorization | `ORCHESTRATION_CHANGE` | `SKILL.md`, session/review modes; membership grants none. |
| Product `PRJ-*` lifecycle/impact/regeneration | `PROJECTION_EXTENSION` | projection lifecycle, impact, and regeneration references; retain `PRJ-*`/`RG-*`. |
| Product selectors and snapshots | `PROJECTION_EXTENSION` | `references/projection-dependencies.md`; exact/selector kinds unchanged. |
| Product package declarations/gates | `PACKAGE_EXTENSION` | `references/projection-gates-and-packages.md`; Stage B authority retained. |
| Product Technical Documentation | `PROJECTION_EXTENSION` + `EXTEND_CONTRACT` | `references/technical-documentation.md`, `technical-model-coverage.md`. |
| Architecture Product `RF-*` | `CAPABILITY_EXTENSION` | listed Architecture references; no new finding family. |
| Code Quality Product `CQ-*`/`CQRA-*` | `CAPABILITY_EXTENSION` | three Code Quality references and entrypoint. |
| Test Engineering Product `TRS-*`/records | `CAPABILITY_EXTENSION` | Test Engineering entrypoint and contract. |
| Compatibility ownership | `NO_IMPLEMENTATION_CHANGE` beyond owner-scope extensions | STM facts, TE conclusions, Architecture consequences; no engine. |
| Pressure scenarios and compatibility gate | `VALIDATION_ONLY` | PS-132–149 and two integrated validation artifacts. |
| Roadmap status | `NO_IMPLEMENTATION_CHANGE` | `docs/roadmap.md` read-only until closeout. |

Normative contract impact is explicit: current surfaces are `EXTEND` or
`NO_CHANGE`, and only the focused Product reference is
`NEW_REFERENCE_REQUIRED`. No implementation task may silently add another
contract or capability owner.

## 4. Dependency graph and checkpoints

```text
Task 1 Product contract
  -> Task 2 identity/membership/baseline/coherency
  -> Task 3 evidence/STM/dependencies
  -> Task 4 revalidation/extend/orchestration/authorization
  -> Task 5 projections/packages/documentation selectors
       -> Task 6 Architecture Review
       -> Task 7 Code Quality
       -> Task 8 Test Engineering
            -> Task 9 integrated validation/backward compatibility
```

Checkpoint A is Tasks 1–2 (Product context foundation). Checkpoint B is Tasks
3–4 (factual substrate and impact routing). Checkpoint C is Tasks 5–8
(projection/package and capability integration). Checkpoint D is Task 9
(final acceptance). Each checkpoint is independently reviewable and must be
green before the next dependency group starts.

Before implementation, a separate `STAGE_E_IMPLEMENTATION_WORKSPACE_SETUP`
gate must create branch
`feature/stage-e-product-multi-project-review` from the approved future plan
checkpoint in worktree
`../architecture-code-review-stage-e-product-multi-project-review`. This task
does not create either. The gate verifies exact ancestry, clean tracked tree,
present normative sources, and recorded validation baseline.

### 4a. Task-level fail-first validation protocol

Each row below is a one-off bounded assertion, not a reusable harness. It is
run at the stated execution point against the exact task-precondition state.
The postcondition requires a tuple of fields/rules and forbidden behavior, so
one keyword or file-existence check cannot make the task green. The regression
guard is rerun at the named checkpoint or final acceptance.

| Task | Execution point | Precondition and fail-first action | Expected pre-result | Postcondition | Regression guard |
|---|---|---|---|---|---|
| 1 | `BEFORE_TASK`, `AFTER_TASK` | Before creation, assert the file is absent. After creation, read `references/product-multi-project-review.md` and assert the same Product context section contains `PROD-*`, Product revision, Product baseline, existing-owner links, local-mode opt-in, and explicit non-authority rules. | Creation target is absent and the required semantic tuple cannot be read. | All tuple members are present and no second authority or Product-mandatory local rule is present. | Existing contracts are byte-for-byte untouched by Task 1 and local mode is described as Product-free. |
| 2 | `BEFORE_TASK`, `AFTER_TASK` | Before Task 2, assert the joint Product routing tuple (`product_mode`, selected revision, baseline reference, membership snapshot, accepted-revision pinning) is absent from both orchestration files. | No Product context can be selected or pinned. | The tuple, immutable historical binding, coherency classification, dirty-state binding, and Product-absent route all appear together. | Existing local intent routing remains available without any Product field. |
| 3 | `BEFORE_TASK`, `AFTER_TASK` | Before Task 3, assert the joint Product evidence/STM/dependency tuple is absent from the three named contracts: Product scope, Product baseline, qualified Project bindings, STM Gate, consumer-owned dependency, and all three strengths. | No bounded Product cross-project factual/dependency slice can be represented. | The tuple is present, while report/index authority and relation-as-dependency promotion are explicitly forbidden. | Existing bare local WS/EV/STM/dependency records and direction remain valid. |
| 4 | `BEFORE_TASK`, `AFTER_TASK` | Before Task 4, assert Product-specific routing terms are absent: Product impact root, Product membership-change handling, Product preserved set, Product availability dimensions, and Product authorization boundary. Do not negate existing generic `CONTEXT_EXPANSION_REQUIRED` or `FULL_REAUDIT_RECOMMENDED`. | Generic revalidation exists, but Product impact/authorization routing is missing. | The changed-binding chain, bounded escalation, preserved set, five independent dimensions, no-full-reread rule, and membership-grants-no-permissions rule are all present. | Product-absent `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, and `PROJECTION_REPAIR` remain unchanged. |
| 5 | `BEFORE_TASK`, `AFTER_TASK` | Before Task 5, assert the joint Product projection/package tuple is absent from the seven named contracts: Product selector snapshot, Product baseline dependency, finite resolved membership, exact Project reference, `PRJ-*`, `RG-*`, and scoped `ALL_SCOPED_CURRENT`. | Product projections/packages cannot resolve a bounded Product scope. | The tuple is present with unchanged Stage B dependency kinds, V1–V4 reuse, impact-before-regeneration, and no automatic regeneration. | Existing Project projection/package declarations and gate policies remain valid. |
| 6 | `BEFORE_TASK`, `AFTER_TASK` | Before Task 6, assert no Product RF tuple exists in the seven Architecture references. The tuple requires Product scope/revision, immutable baseline, affected Projects, qualified evidence/STM, consequence, lifecycle, and Architecture writer. | Product RF cannot be independently adjudicated. | All required fields and local-RF non-promotion/report non-authority rules are present together. | Existing local RF scope, IDs, severity, lifecycle, and root boundaries remain valid. |
| 7 | `BEFORE_TASK`, `AFTER_TASK` | Before Task 7, assert no Product CQ tuple exists in the four Code Quality files. The tuple requires disjoint allocation, Product baseline, qualified evidence, material consequence, Code Quality adjudication, lifecycle, and CQRA independence. | Product CQ/CQRA cannot be represented without inventing allocation or ownership. | All tuple members are present; local repository namespace, projection-only summary, and CQRA/CQ independence are explicit. | Existing local CQ/CQRA selectors, IDs, lifecycle, package, and projection rules remain valid. |
| 8 | `BEFORE_TASK`, `AFTER_TASK` | Before Task 8, assert no Product TE tuple exists in the two Test Engineering files. The tuple requires Product `TRS-*`, exact Product selector, Product baseline, qualified Projects, all six TE families, Assurance projection/package, and no-execution rule. | Product TE scope cannot be selected without inventing authority. | All tuple members and TASK/GAP independence are present; local TE selectors remain separate. | Existing local TRS and TE record identities remain valid. |
| 9 | `BEFORE_TASK`, `AFTER_TASK`, `FINAL_ACCEPTANCE` | Before Tasks 1–8, assert both integrated validation files are absent and that no Product contract/routing tuple passes. After Tasks 1–8, require both files to assert the complete authority/availability/package/compatibility tuple and reference PS-132–149. | Integrated Product validation is missing and the completed contract graph cannot pass. | All assertions and all 18 scenario artifacts pass; no unplanned semantic or file scope appears. | Final tracked scope, Product-absent compatibility, and all approved invariants pass. |

For implementation, each “assert tuple” instruction is a bounded inline
`python3`/shell assertion over the named Markdown files: it must check
`all(required_fields in text)` and `not any(forbidden_rules in text)` for that
row, and print the missing field/rule before exiting nonzero. It is not a
created script, shared runtime, or reusable test harness. The task sections
below refer to these rows and retain their task-specific stop conditions.

## 5. Detailed tasks

### Task 1 — Focused Product contract

**Purpose:** Establish one Product authority boundary before any existing
contract references Product semantics.

**Design decisions implemented:** Product opt-in; Option C; `PROD-*`
identity; `PROD-*@revN` revision; Product baseline as a separate exact vector;
Product Context Workflow and Product Baseline Acceptance Gate ownership; no
Product factual/evidence/package authority.

**Files allowed:** Create `references/product-multi-project-review.md`.

**Files forbidden or untouched:** all existing contracts, capability files,
approved artifacts, roadmap, and runtime/source files.

**Preconditions:** approved Design checkpoint verified; no Product contract
exists.

**Exact contract changes:** Add sections for scope/authority, identity and
revision lifecycle, Project/repository distinction, membership and
multi-Product isolation, baseline vector/coherency/dirty state, availability,
qualified addressing, cross-project routing, `REVALIDATE`, `EXTEND`, outputs,
packages, storage, authorization, lifecycle/ownership, and invariants. Link to
existing owner contracts instead of copying them. State local mode creates no
synthetic Product.

**Backward compatibility constraints:** The new reference must not require
Product state for any existing single-project invocation or alter existing
identity families.

**Fail-first validation:** Use §4a row Task 1 at `BEFORE_TASK` and `AFTER_TASK`.
The required tuple must prove Product context ownership and non-authority
boundaries together; file existence alone is insufficient.

**Implementation steps:**

- [ ] Create the focused reference with the exact sections above.
- [ ] Link existing STM/evidence/capability/projection/package authorities.
- [ ] Add the Product lifecycle/ownership and forbidden-behavior tables.

**Verification:** No `TBD`/`TODO`; no identity family except `PROD-*`; no
Product-as-fact-owner language; local mode remains Product-free.

**Expected changed files:** `references/product-multi-project-review.md`.

**Checkpoint/commit:** `feat: add Stage E Product review contract`.

**Stop conditions:** second Product authority, Product mandatory for local
review, duplicated owner contract, or any new semantic choice required.

### Task 2 — Product/Project identity, membership, baseline, and coherency

**Purpose:** Make approved Product context records selectable, immutable,
exact, and session-pinnable.

**Design decisions implemented:** stable Project descriptor; all four explicit
repository cardinalities; embedded membership and Product isolation; Product
revision lifecycle; exact baseline vector; dirty/noncanonical binding;
`COHERENT`/`MIXED_EXPLICIT`/`UNKNOWN` predicates and policy.

**Files allowed:** Modify `references/session-orchestration.md` and
`references/review-modes-and-orchestration.md`; create PS-132 through PS-136.
`references/product-multi-project-review.md` is read-only in this task; all
required links are established by Task 1.

**Files forbidden or untouched:** all semantic capability/projection/package
contracts, roadmap, approved artifacts, and repository automation.

**Preconditions:** Task 1 green.

**Exact contract changes:** Add explicit coordinator fields
`product_mode`, `product_id`, `selected_product_revision`,
`product_baseline_ref`, and membership snapshot reference. Require accepted
Product revision for baselines, scopes, projections, packages, and Product
semantic records. Pin exact revision per session. Record all clean/dirty,
detached, local-only, missing-remote, untracked, and diverged source states.
Define Product Context Workflow authorization separately from source-read and
dirty-admission authorization. Keep `INDEX.md` routing-only.

**Backward compatibility constraints:** Product-absent sessions keep their
current coordinator shape and local artifact references; Product fields are
absent or `NONE`, not synthetic one-member Product state.

**Fail-first validation:** Use §4a row Task 2 at `BEFORE_TASK` and
`AFTER_TASK`. The pre-check is the joint absence of Product selection,
accepted-revision pinning, baseline, and membership fields; the post-check also
proves Product-absent routing.

**Implementation steps:**

- [ ] Add Product selection, accepted-revision pinning, and baseline references.
- [ ] Add immutable membership/baseline/coherency routing constraints.
- [ ] Create PS-132 through PS-136 with exact Design §40 fields.

**Verification:** Product `current_revision` is a convenience pointer; old
baselines/sessions remain addressable; no baseline is one SHA; coherency is not
availability/coverage/freshness/package state.

**Expected changed files:**
`references/session-orchestration.md`,
`references/review-modes-and-orchestration.md`,
`tests/pressure-scenario-132-product-single-project-compatibility.md`,
`tests/pressure-scenario-133-product-three-clean-projects.md`,
`tests/pressure-scenario-134-product-unavailable-member.md`,
`tests/pressure-scenario-135-product-dirty-member.md`, and
`tests/pressure-scenario-136-product-baseline-advancement.md`.

**Checkpoint/commit:** `feat: add Product identity and baseline routing`.

**Stop conditions:** merged revision/baseline acceptance, optional exact source
binding, universal Product status, or cross-Product mutation.

### Task 3 — Product evidence, STM, and dependency qualification

**Purpose:** Make cross-project observations and factual relationships
addressable and impact-traversable without a second authority.

**Design decisions implemented:** Product-scoped `WS-*`/`EV-*` observations,
STM-gated qualified relations, consumer-owned qualified dependencies, and
derived reverse-index navigation.

**Files allowed:** Modify `references/shared-evidence-model.md`,
`references/shared-technical-model.md`, and
`references/technical-model-dependencies.md`; create PS-137 through PS-140.

**Files forbidden or untouched:** Product capability contracts, projections,
packages, `SKILL.md`, orchestration, roadmap, approved artifacts, and any
report or generated index as authority.

**Preconditions:** Tasks 1–2 green.

**Exact contract changes:** Product `WS-*`/`EV-*` records retain Product
revision, baseline, every qualified Project/repository/scope and exact
revision/content, external sources, observed view, conflict, and limitation.
STM accepts cross-project relations only through the Technical Model Gate;
Project-local facts stay local. Direct dependencies remain dependent-artifact
owned with existing types and `HARD`/`CONDITIONAL`/`INFORMATIONAL` strengths:

```text
CONSUMER -> PREREQUISITE
```

Generated reverse indexes only locate candidates. A relation never becomes a
dependency automatically.

**Backward compatibility constraints:** Existing local WS/EV/STM records and
bare local identities remain valid. Qualification is required only for
cross-project Product records; no local identity is rewritten.

**Fail-first validation:** Use §4a row Task 3 at `BEFORE_TASK` and
`AFTER_TASK`. The post-check jointly proves qualified evidence, STM Gate
ownership, consumer-owned dependencies, all three strengths, and forbidden
report/index authority.

**Implementation steps:**

- [ ] Add Product multi-source observation and conflict rules.
- [ ] Add qualified STM relation/provenance rules.
- [ ] Add qualified direct dependency endpoints and traversal boundaries.
- [ ] Create PS-137 through PS-140.

**Verification:** report/projection/index is never authority; same local IDs
cannot collide in Product scope; external ownership remains explicit.

**Expected changed files:**
`references/shared-evidence-model.md`,
`references/shared-technical-model.md`,
`references/technical-model-dependencies.md`,
`tests/pressure-scenario-137-product-api-compatibility.md`,
`tests/pressure-scenario-138-product-shared-component.md`,
`tests/pressure-scenario-139-product-architecture-finding.md`, and
`tests/pressure-scenario-140-product-local-finding-isolation.md`.

**Checkpoint/commit:** `feat: extend Product evidence and technical dependencies`.

**Stop conditions:** Product writes STM, report authority, relation/dependency
conflation, or changed global dependency direction.

### Task 4 — Product `REVALIDATE`, `EXTEND`, availability, context, authorization

**Purpose:** Apply minimum necessary semantic work to Product changes.

**Files allowed:** Modify `SKILL.md`,
`references/session-orchestration.md`,
`references/review-modes-and-orchestration.md`, and
`references/revalidation-and-freshness.md`; create PS-141 through PS-144.

**Files forbidden or untouched:** shared evidence/STM, dependency, capability,
projection, package, roadmap, approved artifacts, and source/execution files.

**Preconditions:** Tasks 1–3 green.

**Exact contract changes:** Add changed binding → Project-local root → direct
qualified dependency → affected Product relation/capability → projection
impact → package evaluation. Preserve `LOCAL`, `BOUNDARY`, `SYSTEMIC`,
`CONTEXT_EXPANSION_REQUIRED`, and `FULL_REAUDIT_RECOMMENDED`; SYSTEMIC only
recommends full review. Define membership add/remove/replace/role/shared
resource behavior, preserved accepted sets, unavailable limitations, and
explicit authorization for every read/write/execute/publication action.
Product `EXTEND` preserves unaffected state. `SKILL.md` only routes Product
mode and restates invariants; it does not change generic intent semantics.

**Backward compatibility constraints:** Product-absent `NEW`, `RESUME`,
`REVALIDATE`, `EXTEND`, and `PROJECTION_REPAIR` retain current single-project
routing and require no Product identity, registry, baseline, or membership.

**Fail-first validation:** Use §4a row Task 4 at `BEFORE_TASK` and
`AFTER_TASK`. The pre-check targets Product-specific anchors only; it does not
negate the already-existing generic `CONTEXT_EXPANSION_REQUIRED` or
`FULL_REAUDIT_RECOMMENDED` tokens.

**Implementation steps:**

- [ ] Add Product impact roots, preserved-set, membership, and escalation rules.
- [ ] Add explicit Product `EXTEND` and authorization routing.
- [ ] Add bounded context-budget/minimum-slice recording.
- [ ] Create PS-141 through PS-144.

**Verification:** no default full Product reread; unavailable is not failed or
negative; membership grants no permissions; local Product-absent flows remain
unchanged.

**Expected changed files:** `SKILL.md`,
`references/session-orchestration.md`,
`references/review-modes-and-orchestration.md`,
`references/revalidation-and-freshness.md`,
`tests/pressure-scenario-141-product-extend-add-project.md`,
`tests/pressure-scenario-142-product-targeted-revalidate.md`,
`tests/pressure-scenario-143-product-stale-projection.md`, and
`tests/pressure-scenario-144-product-compatible-old-version.md`.

**Checkpoint/commit:** `feat: add Product impact and authorization routing`.

**Stop conditions:** full reread default, universal status, hidden permission,
or unrelated state reopened by `EXTEND`.

### Task 5 — Product projections, selectors, Technical Documentation, packages

**Purpose:** Integrate Product outputs with Stage B without a second lifecycle,
package authority, or projection family.

**Design decisions implemented:** existing `PRJ-*`, `RG-*`, and Stage B package
mechanics; Product-qualified selector snapshots; finite Product package
membership; and explicit impact-before-regeneration.

**Files allowed:** Modify `references/projection-lifecycle.md`,
`references/projection-impact.md`, `references/projection-regeneration.md`,
`references/projection-dependencies.md`,
`references/projection-gates-and-packages.md`,
`references/technical-documentation.md`, and
`references/technical-model-coverage.md`; create PS-145 through PS-149.
Do not modify `references/projection-verification.md`.

**Files forbidden or untouched:** `SKILL.md`, session/orchestration, semantic
capability contracts, roadmap, approved artifacts, and generated projection
content in the canonical tree.

**Preconditions:** Tasks 1–4 green.

**Exact contract changes:** Product selector snapshots record selector contract
revision, Product identity/revision/baseline, and qualified resolved IDs and
revisions. Technical Documentation reuses `PRJ-TECH-DOC-*`,
`TECH-DOC-SCOPE-*`, `PKG-TECHNICAL-DOCUMENTATION`, Product STM selectors,
coverage, limitations, and finite section membership. Product packages use
exact Project package/projection references and resolved required/optional/
conditional membership. Extend impact/regeneration for Product member changes
without automatic regeneration. Existing V1–V4 remain unchanged.

**Backward compatibility constraints:** Existing Project `PRJ-*`, selector,
regeneration, and package declarations retain their current identity, scope,
and Stage B policy. Product qualification is additive only.

**Fail-first validation:** Use §4a row Task 5 at `BEFORE_TASK` and
`AFTER_TASK`. The post-check jointly proves Product selector/baseline/package
resolution, exact Project references, Stage B policy reuse, scoped
`ALL_SCOPED_CURRENT`, and explicit regeneration.

**Implementation steps:**

- [ ] Add Product exact/selector snapshots and member impact.
- [ ] Add Product Technical Documentation selectors, limitations, and package inputs.
- [ ] Add finite Product package resolution and exact Project references.
- [ ] Add Product projection impact/regeneration propagation.
- [ ] Create PS-145 through PS-149.

**Verification:** stale projection cannot mutate authority; only scoped
required package members block; unrelated Project packages do not block;
Technical Documentation cannot adjudicate STM conflicts.

**Expected changed files:** `references/projection-lifecycle.md`,
`references/projection-impact.md`,
`references/projection-regeneration.md`,
`references/projection-dependencies.md`,
`references/projection-gates-and-packages.md`,
`references/technical-documentation.md`,
`references/technical-model-coverage.md`,
`tests/pressure-scenario-145-product-conflicting-evidence.md`,
`tests/pressure-scenario-146-product-blocked-package.md`,
`tests/pressure-scenario-147-product-two-products.md`,
`tests/pressure-scenario-148-product-extend-requiredness.md`, and
`tests/pressure-scenario-149-product-single-member-transition.md`.

**Checkpoint/commit:** `feat: integrate Product projections and packages`.

**Stop conditions:** global redefinition of `ALL_SCOPED_CURRENT`, second
package system, automatic regeneration, or weakened V1–V4.

### Task 6 — Architecture Review Product `RF-*`

**Purpose:** Independently adjudicate true Product architectural consequences.

**Design decisions implemented:** Product-scoped existing `RF-*`, independent
Architecture Review adjudication, qualified baseline/evidence provenance, and
local-RF non-promotion.

**Files allowed:** Modify `references/review-method.md`,
`references/ownership-and-scenarios.md`,
`references/boundary-contract-audit.md`,
`references/independent-verification.md`,
`references/root-boundary-adjudication.md`,
`references/evidence-and-severity.md`, and `references/report-contract.md`.

**Files forbidden or untouched:** Product/STM/TE/CQ authority contracts,
projection/package authority, roadmap, approved artifacts, and local RF
identity/lifecycle rules except for the explicit Product scope extension.

**Preconditions:** Tasks 1–5 green.

**Exact contract changes:** Require Product RF scope, Product revision and
immutable baseline, affected Projects, qualified STM/WS/EV inputs, Product
consequence, lifecycle, severity, dependencies, and provenance. Local RF is
never promoted by aggregation; Product report/correlation is navigation only.
Architecture Review remains the writer and no new RF family is created.

**Backward compatibility constraints:** Existing local RF records, severity,
lifecycle, root boundaries, review targets, and reports remain valid without
Product fields.

**Implementation steps:**

- [ ] Add Product RF scope, baseline, evidence, and affected-Project requirements.
- [ ] Add local-versus-Product RF promotion and correlation boundaries.
- [ ] Add Product RF dependency, severity, lifecycle, and projection checks.

**Fail-first validation:** Use §4a row Task 6 at `BEFORE_TASK` and
`AFTER_TASK`. The post-check jointly proves Product RF identity/baseline,
qualified evidence/STM, affected Projects, Architecture adjudication, and
local-RF/report isolation.

**Verification:** existing local RF identifiers, targets, severity, lifecycle,
and root rules pass unchanged; Product RF cannot be accepted without qualified
baseline/evidence/STM.

**Expected changed files:** `references/review-method.md`,
`references/ownership-and-scenarios.md`,
`references/boundary-contract-audit.md`,
`references/independent-verification.md`,
`references/root-boundary-adjudication.md`,
`references/evidence-and-severity.md`, and
`references/report-contract.md`.

**Checkpoint/commit:** `feat: extend Architecture Review for Product scope`.

**Stop conditions:** new Product finding family, automatic local promotion,
report adjudication, or Architecture writing another capability's authority.

### Task 7 — Code Quality Product `CQ-*`/`CQRA-*`

**Purpose:** Add collision-free Product Code Quality semantics and output
selection while preserving Code Quality ownership.

**Design decisions implemented:** existing `CQ-*`/`CQRA-*` families, disjoint
Product allocation, Code Quality ownership, material cross-project scope,
local-finding preservation, and projection-only summaries.

**Files allowed:** Modify `capabilities/code-quality-review/SKILL.md`,
`capabilities/code-quality-review/references/code-quality-contract.md`,
`code-quality-lifecycle.md`, and `code-quality-projection.md`.

**Files forbidden or untouched:** Architecture Review, Test Engineering, STM,
Product report authority, roadmap, and local CQ/CQRA allocation semantics.

**Preconditions:** Tasks 1–5 green.

**Exact contract changes:** Add `scope_kind: PRODUCT`, stable Product-keyed
allocation namespace `PRODUCT:<PROD-*>`, Product revision/baseline, affected
Projects, qualified evidence/STM, material consequence, lifecycle, freshness,
and Code Quality adjudication. Keep local namespace `REPOSITORY:<repository>`
and IDs unchanged. Define Product CQRA only for coordinated action; completion
does not resolve CQ. Product Summary remains projection over explicit CQ
dependencies and snapshots.

**Backward compatibility constraints:** Existing local `CQ-*`/`CQRA-*` IDs,
repository-scoped selectors, lifecycle, package declarations, and projections
remain valid and are not migrated.

**Fail-first validation:** Use §4a row Task 7 at `BEFORE_TASK` and
`AFTER_TASK`. The post-check jointly proves disjoint Product allocation,
baseline/evidence/materiality, Code Quality adjudication, local namespace
preservation, CQRA/CQ independence, and summary non-authority.

**Implementation steps:**

- [ ] Add the disjoint Product allocation and Product scope fields.
- [ ] Add Product baseline/evidence/materiality/adjudication requirements.
- [ ] Add Product CQ/CQRA lifecycle, freshness, and revalidation rules.
- [ ] Add Product selector and Summary projection/package dependencies.

**Verification:** existing local selectors, lifecycle, package, and V1–V4
checks pass; Product scope is never moved to Architecture Review.

**Expected changed files:** `capabilities/code-quality-review/SKILL.md`,
`capabilities/code-quality-review/references/code-quality-contract.md`,
`capabilities/code-quality-review/references/code-quality-lifecycle.md`, and
`capabilities/code-quality-review/references/code-quality-projection.md`.

**Checkpoint/commit:** `feat: extend Code Quality for Product scope`.

**Stop conditions:** collision-prone allocation, summary-created CQ, CQRA
completion changing CQ lifecycle, or ownership transfer.

### Task 8 — Test Engineering Product scope

**Purpose:** Bind existing TE families to Product `TRS-*` without a second
Behavior Model or implicit execution.

**Design decisions implemented:** existing TE families, Product `TRS-*` scope,
qualified Project/baseline provenance, finite Product Assurance projection,
TASK/GAP independence, and separately authorized execution.

**Files allowed:** Modify `capabilities/test-review/SKILL.md` and
`capabilities/test-review/references/test-engineering-contract.md`.

**Files forbidden or untouched:** Product fact authority, Architecture Review,
Code Quality, existing local Test Engineering IDs, execution tooling, roadmap,
approved artifacts, and package authority.

**Preconditions:** Tasks 1–5 green.

**Exact contract changes:** Extend `TRS-*` with `scope_kind: PRODUCT`, stable
Product scope allocation, Product revision, and immutable baseline. Product
records use exact Product `test_review_scope_id`; local records retain local
scope IDs. Qualified provider/consumer/contributor Projects and provenance
are required. Product `BC/CC/MAT/TM/GAP/TASK` remain TE authority; Product
Assurance is finite projection/package. `TASK-*` completion never resolves
`GAP-*`; execution remains separately authorized.

**Backward compatibility constraints:** Existing local `TRS-*` selectors and
all local Test Engineering records remain valid. Product scope is a separate
binding and does not migrate local records.

**Fail-first validation:** Use §4a row Task 8 at `BEFORE_TASK` and
`AFTER_TASK`. The post-check jointly proves Product `TRS-*` selection,
qualified baseline/Project provenance, all TE family ownership, Assurance
projection/package semantics, TASK/GAP independence, and no execution.

**Implementation steps:**

- [ ] Add Product `TRS-*` scope identity and exact selector binding.
- [ ] Add qualified Project and Product baseline provenance to TE records.
- [ ] Add Product Assurance projection/package inputs.
- [ ] Preserve TASK/GAP independence and the no-execution boundary.

**Verification:** local TRS and record identities remain valid; Product
Assurance is not a Behavior Model authority; no test execution is implicit.

**Expected changed files:** `capabilities/test-review/SKILL.md` and
`capabilities/test-review/references/test-engineering-contract.md`.

**Checkpoint/commit:** `feat: extend Test Engineering for Product scope`.

**Stop conditions:** second Behavior Model, all-member scan, local overwrite,
or implicit execution authorization.

### Task 9 — Integrated validation and backward compatibility

**Purpose:** Prove the completed contract graph and additive local behavior.

**Files allowed:** Create
`tests/stage-e-product-multi-project-contract-validation.md` and
`tests/stage-e-product-multi-project-backward-compatibility.md`. PS-132–149
are read-only in this task; if an assertion contradicts the approved Design,
stop and return to the owning task rather than modifying a scenario during
integration validation.

**Files forbidden:** all normative contracts and approved artifacts; this task
adds validation only.

**Design decisions implemented:** no new semantic decision. This task only
checks the completed contract graph, all 18 pressure scenarios, availability,
authority ownership, package scope, authorization, and local compatibility.

**Preconditions:** Tasks 1–8 and Checkpoints A–C green.

**Exact validation changes:** Assert Product optionality; identity distinctions;
exact vector/no SHA; STM/RF/CQ/TE ownership; projection/report/index/package
non-authority; relation/dependency/index/impact distinctions; minimum-slice
revalidation; additive EXTEND; five availability dimensions; Stage B package
reuse; PRJ/RG separation; no hidden permission; no backend/service/graph/RAG.
The compatibility artifact asserts local operation requires no Product ID,
registry migration, membership, baseline, evidence, package, or identity
rewrite, and existing local WS/EV/STM/RF/CQ/TE/PRJ records remain valid.

**Backward compatibility constraints:** This task may add validation evidence
only; it may not alter any local contract or existing artifact identity.

**Fail-first validation:** Use §4a row Task 9 at `BEFORE_TASK`, `AFTER_TASK`,
and `FINAL_ACCEPTANCE`. The pre-state is the exact pre-Stage-E plan
checkpoint; the post-state checks the complete authority tuple and all
PS-132–149 artifacts. Do not fabricate RED or weaken scenarios.

**Verification:** all 18 scenarios have input, expected, forbidden, authority,
impact, and package/projection outcome; final tracked scope exactly matches
this plan; no unapproved semantic divergence.

**Expected changed files:** the two validation files and no normative file or
pressure-scenario file.

**Checkpoint/commit:** `test: validate Stage E Product contract integration`.

**Stop conditions:** invented semantics, unresolved HIGH/MEDIUM finding,
Product-absent compatibility failure, weakened/dropped scenario, or unplanned
tracked path.

## 6. Identifier and ownership map

| Object | Identity/allocation | Writer and lifecycle owner | Provenance/consumer |
|---|---|---|---|
| Product | New stable `PROD-*` | Product Context Workflow | explicit creation/history; sessions and membership |
| Product revision | `PROD-*@revN` | Product Context Workflow / Acceptance Gate | prior context and membership; baselines/scopes |
| Project | stable coordinator `project_key` | coordinator identity registry | explicit descriptor/source; Products and sessions |
| Membership | embedded `membership_key` | Product Context Workflow | authorized request; Product revision/package selectors |
| Product baseline | Product-scoped `baseline_key` | Baseline Acceptance Workflow | exact source/content vector, external sources, WS/EV |
| Evidence | existing `WS-*`/`EV-*` | Shared Evidence Model | qualified sources/baseline; STM/capability gates |
| STM relation | existing STM relation vocabulary | Technical Model Gate | qualified accepted STM/evidence; capabilities |
| RF | existing `RF-*` | Architecture Review | Product baseline/STM/evidence; Architecture projections |
| CQ/CQRA | existing families; disjoint `PRODUCT:<PROD-*>` allocation | Code Quality Review | qualified evidence/STM/baseline; CQ projections/actions |
| TE scope | existing `TRS-*`, `scope_kind: PRODUCT` | Test Engineering | Product baseline and qualified Projects; TE selectors |
| TE records | existing `BC/CC/MAT/TM/GAP/TASK` | Test Engineering | Product TRS/evidence/baseline; Assurance projection |
| Projection | existing `PRJ-*` | owning capability/endpoint | semantic/projection dependency snapshots |
| Regeneration | existing `RG-*` | regeneration workflow | frozen Product scope; verified projection output |
| Package | existing `PKG-*` mechanics | consuming endpoint | finite resolved membership and exact references |

Stable identities do not contain transient source revisions unless the object
is explicitly revision-specific. Existing single-project IDs are not rewritten.

## 7. Availability, compatibility, and output rules

| Dimension/output | Owner | Product implementation rule |
|---|---|---|
| Source Availability | source/baseline workflow | exactness, access, dirty/noncanonical state, limitation |
| Review Coverage | selected capability | investigated scope is separate from source presence |
| Semantic Availability | STM or owning capability | accepted/insufficient/disputed/absent follows owner lifecycle |
| Projection Freshness/Availability | projection lifecycle/impact owner | `CURRENT`/`STALE`/`BLOCKED` only for selected dependencies |
| Package Gate Result | named package owner | finite resolved closure under existing policy |
| Product Technical Documentation | Technical Documentation | selected Product STM selectors, coverage, limits; existing package |
| Product Code Quality Summary | Code Quality | projection over declared local/Product CQ dependencies |
| Product Test Assurance | Test Engineering | projection/package over Product `TRS-*` records |

Compatibility remains `STM facts → TE contract conclusions → Architecture
consequence`; `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED` are views,
not precedence. No matrix or version comparison is authority by itself.

## 8. Pressure-scenario coverage matrix

| Scenarios | Task | Contract/validation | Required result |
|---|---|---|---|
| 1 | 2, 9 | orchestration, compatibility artifact | local flow unchanged; no implicit Product |
| 2–5 | 2, 4 | Product baseline/coherency/revalidation | exact vector, truthful classification, preserved history |
| 6–7 | 3, 8 | STM/dependencies/TE | qualified contract and resource ownership |
| 8–9 | 6 | Architecture Review | Product RF only by independent adjudication |
| 10–11 | 4 | membership/EXTEND/revalidation | bounded additive/minimum slice |
| 12 | 5 | projection lifecycle/impact | stale only where dependent; explicit RG |
| 13 | 3, 8 | compatibility/TE | owner-gated older supported version |
| 14 | 3, 5 | evidence/coherency | preserved conflict; no precedence invention |
| 15 | 5 | package gates | only scoped package blocks |
| 16 | 2, 4 | membership isolation | Product X/Y independent; local reuse proven |
| 17–18 | 4, 2 | membership/optionality | targeted revision; local mode remains valid |

Each PS-132–149 file must repeat the complete six-field scenario shape:
input state, expected behavior, forbidden behavior, affected authority,
impact scope, and package/projection outcome. The suite covers all 18 Design
scenarios without adding a reusable harness.

## 9. Commit, rollback, and roadmap policy

Use one conceptual commit per task, with the subjects specified in Tasks 1–9.
Do not amend, squash, merge, tag, or push. Each commit contains only its
expected files.

On mismatch, stop at the last green commit; do not reset or rewrite history.
Revert only the offending conceptual task in the isolated branch after
recording the mismatch. Use `STAGE_E_IMPLEMENTATION_CONTRACT_CONFLICT` for
owner conflicts, `STAGE_E_PRODUCT_STORAGE_AUTHORITY_VIOLATION` for Product
state inside a member repository, `STAGE_E_PRODUCT_AUTHORIZATION_BOUNDARY_VIOLATION`
for hidden permissions, `STOP_HARNESS_EXPANSION` for reusable harness growth,
and `VALIDATION_BUDGET_EXCEEDED` for disproportionate validation cost.
Historical baselines, evidence, findings, and local IDs must survive recovery.

Do not modify `docs/roadmap.md` during implementation. At final authorized
Stage E promotion/closeout, synchronize Stage D actual completion and Stage E
implementation status. Roadmap publication is not an implementation
prerequisite.

## 10. Final acceptance and implementation-review entry

Final acceptance requires Product opt-in, unchanged local mode, exact Product
identity/revision/membership/baseline semantics, qualified provenance, STM and
capability ownership, distinct relation/dependency/index/impact semantics,
impact-driven revalidation, additive EXTEND, independent availability,
Stage B package reuse, PRJ/RG lifecycle, explicit regeneration, no hidden
permissions, no new backend, additive migration, and all 18 scenarios green.

Independent implementation review may begin only after all nine tasks,
Checkpoints A–D, task validations, backward compatibility, pressure scenarios,
and scope checks are green; no HIGH/MEDIUM implementation finding is known; no
unapproved contract divergence or migration exists; and the feature work is
committed on the isolated branch/worktree without push/merge/promotion.

## 11. Plan completeness and metadata

An implementation agent can execute this plan without inventing semantic
identity, ownership, lifecycle, provenance, scope, package, authorization, or
revalidation rules: every contract surface has an exact task/file, every task
has preconditions, fail-first evidence, verification, expected files,
checkpoint, and stop conditions, and all 18 approved scenarios are mapped.

| Field | Value |
|---|---|
| Plan baseline | `25c08ffcb741d7d23056a0ef84c59f17610f804f` |
| Planned tasks | `9` |
| Planned checkpoints | `4` |
| New contract | `references/product-multi-project-review.md` |
| New identity families | `PROD-*` only |
| Harness | `DO_NOT_BUILD_HARNESS` |
| Migration | `ADDITIVE` |
| Pressure scenarios | `18/18` |
| Workspace branch | `feature/stage-e-product-multi-project-review` |
| Workspace path | `../architecture-code-review-stage-e-product-multi-project-review` |
| Roadmap | read-only until final promotion/closeout |
| Implementation/workspace/commit/push in this gate | `NO` |
