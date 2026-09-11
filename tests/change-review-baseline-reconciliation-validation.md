# Change Review baseline reconciliation validation

## PRE-CHANGE fail-first evidence

This PRE-CHANGE evidence is bound to canonical base commit
`5be8bbd8a5869bb74d4a2ee804c695cb19620008`. It was recorded before the
normative Change Review contract edits and must remain visible as historical
evidence.

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

Expected pre-change result: `8/8 GAP PRESENT`; there is no post-change claim
in this section.

## Post-change Task 1 routing closure

| ID | Pre-change gap retained above | Task 1 closure evidence | Expected |
|---|---|---|---|
| FF01 | no first-class Change Review mismatch route | `session-orchestration.md` defines `CHANGE_REVIEW`, baseline relation routing, and mismatch actions. | CLOSED FOR TASK 1 |
| FF02 | no immutable base/candidate CR binding | Deferred to Task 2; Task 1 defines only the candidate requested/resolved-work route. | OPEN — TASK 2 |
| FF03 | no review-local candidate fact/finding authority barrier | Deferred to Task 2; Task 1 establishes read-only candidate-mode routing only. | OPEN — TASK 2 |
| FF04 | no exact TREE_EQUIVALENT proof contract | Deferred to Task 2. | OPEN — TASK 2 |
| FF05 | no contextual reconciliation dispatch through owners | `session-orchestration.md` makes `RECONCILE_CHANGE` contextual, explicit, and limited to reusable completed review. | CLOSED FOR TASK 1 |
| FF06 | no complete baseline-advancement gate after reconciliation | Deferred to later reconciliation work. | OPEN — LATER TASK |
| FF07 | prediction not separated from actual Stage B impact | Deferred to later projection-impact work. | OPEN — LATER TASK |
| FF08 | branch/commit/PR candidate mode is not first-class | Task 1 establishes the read-only candidate requested/resolved-work shape; exact source bindings are deferred to Task 2. | PARTIAL — TASK 2 REQUIRED |

Task 1 closure is limited to startup routing and candidate request/dependency
separation. The PRE-CHANGE rows above remain immutable historical evidence.

## Task 1 review regression — later integration routing

| ID | Contract break to catch | Required outcome | Pre-fix result |
|---|---|---|---|
| R01 | The later session-integration table permitted changed-baseline `RESUME`, `EXTEND`, and current `PROJECTION_REPAIR` to proceed without the Task 1 guard. | `RESUME` returns `SOURCE_BASELINE_MISMATCH`; `EXTEND` returns `BASELINE_RECONCILIATION_REQUIRED`; current `PROJECTION_REPAIR` blocks; `CHANGE_REVIEW` and contextual `RECONCILE_CHANGE` are offered without making reconciliation a startup intent. | CORRECTED — later integration rules now preserve all four Task 1 routes. |

| R02 | The Change Inventory schema left `MOVED` on the scalar locator/evidence shape and did not require old BASE and new CANDIDATE sides. | `MOVED` has an explicit `base` old-locator/evidence side and `candidate` new-locator/evidence side; scalar handling remains limited to `ADDED`, `MODIFIED`, and `REMOVED`. | CORRECTED — MOVED now requires the two-sided structure. |

## Task 5 review reuse validation

| ID | Deterministic scenario | Required contract outcome |
|---|---|---|
| MR01 | Same repository, exact candidate commit/tree, exact qualification, complete CR, usable evidence, compatible scope/lenses. | `EXACT`; reuse is allowed. |
| MR02 | No-ff or squash result has equal reviewed-candidate and intended-candidate whole-tree identity and matching repository, qualification, and scope. | `TREE_EQUIVALENT` at `WHOLE_TREE_EQUAL`; reuse is allowed only with the compared prior CR, both trees, compatibility, usability, and retained proof fields. |
| MR03 | Candidate differs in commit but the persisted included path/selector/member-binding manifest, relevant-tree fingerprint, and omitted-path non-impact proof match. | `TREE_EQUIVALENT` at `FROZEN_RELEVANT_SCOPE_EQUAL`; reuse is allowed only with all auditable proof fields retained. |
| MR04 | Only inspected files coincide, or proof is missing; branch name, ancestry, or fuzzy text appears equal. | `NOT_TREE_EQUIVALENT`; reuse is denied. |
| MR05 | Reviewed candidate B advances to supported candidate C. | `ADVANCED`; create linked immutable incremental `B→C` CR whose base binding equals the parent CR's candidate binding and whose candidate binding is the exact next source state. |
| MR06 | Candidate no longer safely represents the reviewed candidate. | `DIVERGED`; create a new CR; never rewrite the completed CR. |
| MR07 | Conflict resolution changes relevant content. | Supplemental or new CR; no reuse from the prior review. |
| MR08 | Only an independently decomposable cherry-picked subset is selected and omitted-commit non-impact proof is retained. | Conditional reuse; absent proof requires a new CR. |
| MR09 | Product member vector, selected Product revision, or member qualification differs despite equal-looking text/tree. | Reuse rejected as `DIVERGED`/`UNAVAILABLE`; preserve member-qualified bindings. |
| MR10 | Compare A→B and A→C after each candidate is bound immutably. | Read-only comparison view over immutable CRs; no adjudication, acceptance, or canonical authority creation. |

## Task 8 projection-separation validation

FF07 above remains immutable pre-change evidence. These rows provide the
post-change validation for prediction versus actual impact and explicit
regeneration boundaries.

| Historical row | Task 8 closure evidence | Expected |
|---|---|---|
| FF07 — candidate projection prediction is not separated from actual Stage B impact | PI01–PI06 below cover immutable candidate prediction, accepted actual handoff, forbidden candidate freshness writes, unknown limitations, and explicit regeneration deferral. | CLOSED FOR TASK 8 |

| ID | Deterministic scenario | Required contract outcome |
|---|---|---|
| PI01 | A completed CR predicts `NO_EXPECTED_IMPACT`, but accepted owner reconciliation later produces an accepted semantic delta affecting a projection. | Retain the prediction unchanged; run existing Projection Impact Analysis once after semantic stabilization and persist the actual impact separately. |
| PI02 | A CR predicts `LIKELY_AFFECTED` or `DEFINITELY_AFFECTED_IF_ACCEPTED`, but reconciliation rejects the candidate delta. | Prediction remains candidate-qualified evidence; no actual impact or freshness change is created from the prediction. |
| PI03 | A candidate prediction attempts to write `CURRENT`. | Reject the candidate write; only the existing accepted Stage B impact authority may determine freshness. |
| PI04 | A candidate prediction attempts to write `STALE` or `BLOCKED`. | Reject both candidate writes; candidate mode cannot create impact reasons or alter projection freshness. |
| PI05 | A candidate is `UNKNOWN_IMPACT` because required authority or linkage is unavailable. | Preserve the bounded limitation and route the affected scope to the existing semantic/contract revalidation path; do not guess freshness. |
| PI06 | Accepted actual impact marks projections `STALE`/deferred and the user declines explicit `RG-*` regeneration. | Leave affected projections stale/deferred, retain reasons, and preserve canonical semantics; no regeneration starts implicitly. |

## Task 8 Product-member qualification validation

| ID | Deterministic scenario | Required contract outcome |
|---|---|---|
| PD01 | Product Change Review compares identical complete qualified member vectors A and B, including Product revision and every member source binding. | Effects are bound to the exact vectors; no unqualified Product-wide delta is admitted. |
| PD02 | One member's source revision/content binding changes while the other member bindings remain equal. | Record a separate member A/B effect qualified to that member; do not flatten the change across the Product. |
| PD03 | A Product candidate omits a member present in the accepted vector. | Record an explicit missing-member limitation; never treat the member as unchanged or silently remove its scope. |
| PD04 | A selected member is present but its source is unavailable or unresolved. | Record the exact limitation and route bounded `CONTEXT_EXPANSION_REQUIRED` when the boundary may be material; do not admit a Product-wide negative. |
| PD05 | Two members use the same local semantic ID or equal-looking text/tree but have different Project/source/revision bindings. | Keep member identities and effects separate; no cross-member alias or equivalence is inferred. |
| PD06 | A Product summary groups effects from multiple members, including differing limits or one unavailable member. | Summary remains qualified to each member vector/evidence/scope; no Product-wide unqualified delta or universal status is created. |
