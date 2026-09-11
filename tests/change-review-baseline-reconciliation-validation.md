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

## Baseline-binding gate regression BB01–BB05

| ID | Deterministic scenario | Required contract outcome |
|---|---|---|
| BB01 | A completed reusable `A→B` CR has `base_binding` exactly equal to the current accepted binding A, including repository, Project/Product/member qualification, and source commit/tree/vector; its candidate binding is exact intended B. | `RECONCILE_CHANGE` is eligible, and `BASELINE_ADVANCE_ALLOWED` may be evaluated only after the existing evidence, delta, owner, technical/coverage, and policy gates pass. |
| BB02 | A completed reusable `A→B` CR still has exact intended candidate B, but the current accepted source binding is independently advanced to A'. | Return `REVIEW_BASELINE_MISMATCH`; do not dispatch reconciliation or emit `BASELINE_ADVANCE_ALLOWED`; preserve the CR and classify/review from the current accepted binding. |
| BB03 | CR and intended candidate match, but the current accepted binding differs in repository or Project qualification. | Return `REVIEW_BASELINE_MISMATCH`; source text/tree similarity does not permit reconciliation or baseline advancement. |
| BB04 | CR and intended candidate match, but the current accepted Product revision, member qualification, or member baseline vector differs. | Return `REVIEW_BASELINE_MISMATCH`; do not flatten Product/member identity or advance the baseline. |
| BB05 | A linked immutable `B→C` CR has `base_binding == parent_review.candidate_binding ==` current accepted binding B and exact intended candidate C. | The linked chain is eligible only with that equality; any broken parent/child or current-accepted-base equality returns `REVIEW_BASELINE_MISMATCH` and requires classification/review from the current accepted binding. |

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

## Complete Change Review matrix CR01–CR36

| ID | Source relation | Allowed intent | Mutation | Candidate/canonical/projection state | Next action |
|---|---|---|---|---|---|
| CR01 | baseline matches candidate | `CHANGE_REVIEW` | none | candidate review only; canonical unchanged; projections unchanged | complete review or explicit reconciliation |
| CR02 | baseline advanced to descendant | `CHANGE_REVIEW` | candidate evidence only | candidate bound to advanced source; canonical unchanged | classify reuse as `ADVANCED` or create linked CR |
| CR03 | baseline diverged | `CHANGE_REVIEW` | none | candidate is not reusable; canonical unchanged | create new CR |
| CR04 | baseline relation unknown | `CHANGE_REVIEW` | none | candidate relation unresolved; canonical/projection unchanged | resolve source relation or record limitation |
| CR05 | branch resolves to exact commit/tree | `CHANGE_REVIEW` | none | exact base/candidate bindings; candidate-only outputs | retain immutable bindings |
| CR06 | pull request resolves to candidate tree | `CHANGE_REVIEW` | none | PR metadata is input; CR remains source-bound | review selected lenses |
| CR07 | dirty or noncanonical candidate source | `CHANGE_REVIEW` | none | candidate limitation; no accepted state | stop or obtain authorized clean binding |
| CR08 | added file or interface | `CHANGE_REVIEW` | candidate `CF-*` | candidate-only fact; no STM/projection write | route through reconciliation if confirmed |
| CR09 | modified accepted fact | `CHANGE_REVIEW` | candidate delta | affected accepted ref plus candidate interpretation | owner adjudication |
| CR10 | removed source fact | `CHANGE_REVIEW` | candidate removal | accepted fact remains canonical; removal is candidate evidence | Technical Model Gate after reconciliation |
| CR11 | moved source entry | `CHANGE_REVIEW` | two-sided MOVED observation | base and candidate locators/evidence remain distinct | correlate, then reconcile explicitly |
| CR12 | changed method/path | `CHANGE_REVIEW` | candidate operation/property claim | candidate API evidence; accepted IF/OP unchanged | Technical Model Gate and applicable CC |
| CR13 | changed auth boundary | `CHANGE_REVIEW` | candidate boundary claim | candidate evidence only; no accepted auth mutation | owner review and reconciliation |
| CR14 | changed schema/error contract | `CHANGE_REVIEW` | candidate contract claim | candidate CF/CC input; compatibility not decided | Contract Verification adjudication |
| CR15 | changed transport/container limit | `CHANGE_REVIEW` | candidate limit claim | candidate CQ/TE input; no `TESTED` claim | CQ/TE owner routing |
| CR16 | changed dependency edge | `CHANGE_REVIEW` | candidate dependency observation | candidate dependency cannot satisfy accepted dependency | bounded dependency expansion |
| CR17 | uninspected material boundary reached | `CHANGE_REVIEW` | none | candidate completeness partial/unknown | `CONTEXT_EXPANSION_REQUIRED` |
| CR18 | evidence unavailable or dynamic | `CHANGE_REVIEW` | limitation only | candidate limitation; no inferred no-change | preserve limitation and bound scope |
| CR19 | candidate finding appears | `CHANGE_REVIEW` | candidate `CRF-*` | review-local finding; no canonical lifecycle | CQ/owner adjudication |
| CR20 | existing finding may be mitigated | `CHANGE_REVIEW` | effect record | candidate effect only; existing finding unchanged | reconcile with finding owner |
| CR21 | candidate adds risk while resolving existing finding | `CHANGE_REVIEW` | two effect records | many-to-many candidate effects; canonical unchanged | adjudicate each owner result |
| CR22 | candidate Architecture interpretation | `CHANGE_REVIEW` | review-local assessment | no accepted `RF-*` mutation | Architecture authority |
| CR23 | candidate TE assurance need | `CHANGE_REVIEW` | candidate case/impact | not executed and not `TESTED` | Test Engineering reproof/planning |
| CR24 | candidate provider/consumer match | `CHANGE_REVIEW` | comparison input | same method/path is not compatibility | CC adjudication |
| CR25 | candidate Product member change | `CHANGE_REVIEW` | member-qualified effect | no Product-wide unqualified delta | Product-qualified reconciliation |
| CR26 | candidate projection prediction | `CHANGE_REVIEW` | prediction record | no `CURRENT`/`STALE`/`BLOCKED` write | retain until accepted impact pass |
| CR27 | accepted owner result is required | contextual `RECONCILE_CHANGE` | owner disposition | candidate identity not reused; canonical owner may write | record owner result |
| CR28 | completed reusable CR with explicit confirmation | contextual `RECONCILE_CHANGE` | accepted-owner writes only | candidate remains evidence; canonical writes owner-controlled | run bounded reconciliation |
| CR29 | incomplete or non-reusable CR | none | no dispatch | candidate remains non-authoritative | complete/new review first |
| CR30 | exact intended binding still current | `RECONCILE_CHANGE` | accepted delta accounting | eligible for baseline gate | verify all material delta |
| CR31 | candidate commit/tree changes during reconciliation | none | discard pending eligibility | CR immutable; baseline unchanged | reclassify reuse |
| CR32 | qualified Product/member vector changes | none | discard pending eligibility | member-qualified CR immutable | reclassify vector/reuse |
| CR33 | all material delta accounted | contextual `RECONCILE_CHANGE` | owner results recorded | technical/coverage gates may be evaluated | evaluate baseline gate |
| CR34 | partial reconciliation | none | no baseline advancement | accepted baseline remains prior state | resolve remaining owners |
| CR35 | open finding permitted by policy | contextual reconciliation | no forced closure | finding remains explicit; baseline may advance if all gates pass | retain policy/accounting evidence |
| CR36 | accepted semantic delta stabilized | contextual reconciliation then Stage B | one actual impact handoff | actual freshness owned by Projection Impact Analysis; prediction retained | explicit `RG-*` only if requested |

## Partial reconciliation matrix PRC01–PRC05

| ID | Scenario | Required deterministic result |
|---|---|---|
| PRC01 | only CF/STM owner result is complete | reconciliation remains partial; no baseline advancement |
| PRC02 | Architecture or CQ owner remains pending | baseline gate is blocked; candidate identity is not canonical |
| PRC03 | TE/CC owner is required but unresolved | required gate remains blocked; no compatibility or `TESTED` shortcut |
| PRC04 | unknown delta is not covered by explicit policy | baseline advancement is blocked; limitation remains visible |
| PRC05 | HIGH finding is resolved while MEDIUM finding remains open under existing policy | record both owner outcomes; baseline may advance only if every other gate passes, and the MEDIUM remains open |

## Candidate authority-barrier matrix

| ID | Forbidden shortcut | Required barrier |
|---|---|---|
| AB01 | `CF-*` used as accepted STM fact | Technical Model Gate must adjudicate; candidate remains evidence |
| AB02 | `CF-*` used as accepted dependency | dependency metadata may use accepted owner output only |
| AB03 | `CRF-*` promoted to `CQ-*` | Code Quality independently adjudicates and allocates canonical identity |
| AB04 | candidate Architecture result mutates `RF-*` | Architecture authority owns canonical write |
| AB05 | candidate TE case becomes `TESTED` | accepted execution evidence is required |
| AB06 | candidate provider/consumer match becomes compatibility | CC remains adjudicator; method/path similarity is insufficient |
| AB07 | candidate Product record becomes Product fact/status | Product qualification composes member-bound accepted records only |
| AB08 | candidate prediction or projection text changes freshness | Projection Impact Analysis owns freshness; `RG-*` remains explicit |

## Intent-routing matrix

| ID | Intent case | Required route |
|---|---|---|
| IR01 | `USE_EXISTING` with matching accepted baseline | consume accepted package as current; metadata-only startup |
| IR02 | `USE_EXISTING` with changed source | show A historical and B separately; do not treat A as current |
| IR03 | `NEW` with no prior package | start independently from selected B and confirmed work |
| IR04 | `NEW` with accepted A present | do not inherit or enrich A without explicit selection |
| IR05 | `RESUME` with `BASELINE_MATCH` | restore and continue first unfinished gate |
| IR06 | `RESUME` with advanced/diverged/unknown source | stop with `SOURCE_BASELINE_MISMATCH`; offer review/revalidation/reusable reconcile; none automatic |
| IR07 | `REVALIDATE` with complete CR available | reevaluate accepted state; CR is routing evidence only |
| IR08 | `EXTEND` with changed baseline | stop with `BASELINE_RECONCILIATION_REQUIRED`; no implicit chain |
| IR09 | `PROJECTION_REPAIR` with matching source | repair selected current projection only |
| IR10 | `PROJECTION_REPAIR` with changed source | block current repair; no historical-repair mode |

## Complete-claim checks

| Check | Required result |
|---|---|
| Candidate freshness claim | No CR prediction may claim accepted `CURRENT`, `STALE`, or `BLOCKED`; only Stage B impact authority writes those states. |
| Review-only lifecycle claim | No review-only `CR-*`, `CF-*`, or `CRF-*` finding may use canonical `RESOLVED`, `CLOSED`, or `ACCEPTED` as its own lifecycle. |
| Baseline completion claim | No baseline advances on `COMPLETE` alone; exact source binding, material-delta accounting, required owner results, technical/coverage gates, and policy-explicit unknown handling are required. |
| Scope claim | CR01–CR36, MR01–MR10, BB01–BB05, PRC01–PRC05, AB01–AB08, IR01–IR10, PI01–PI06, and PD01–PD06 are all deterministic and retained in this artifact. |

## Final validation checks

Required tokens exist in their owning contracts and this artifact; no design,
plan, or review artifact is modified by the implementation. Final checks:

```text
CHANGE_REVIEW lifecycle documented
candidate/canonical/projection authority separated
baseline mismatch and reconciliation routes explicit
safe reuse and Product qualification explicit
projection regeneration explicit
complete claims bounded
```

### Bounded no-placeholder validation

The canonical plan and this validation note contain the literal expression
used to describe this check, so both are intentionally excluded from the
phrase scan. Inspect only the four Task 10 human-facing implementation files;
validate this artifact separately with its matrix/count checks. An empty
phrase-scan result is the expected pass condition. Do not scan plans, designs,
or reviews.

```bash
if rg -n "placeholder|deferred architecture decision|architecture contradiction" \
  README.md \
  docs/reference/workflows.md \
  docs/concepts/review-suite.md \
  docs/getting-started/quick-start.md
then
  echo "FAIL: forbidden placeholder phrase found in bounded implementation scope"
  exit 1
else
  echo "PASS: no forbidden placeholder phrase in bounded implementation scope"
fi
```
