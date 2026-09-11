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
