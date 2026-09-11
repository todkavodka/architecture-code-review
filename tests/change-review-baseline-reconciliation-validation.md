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

## POST-IMPLEMENTATION CLOSURE

This section closes the historical findings only as normative contract closure.
It does not claim a runtime SCM/PR service or harness was executed; the
verification evidence is the retained deterministic contract matrices and
their named owner mechanisms.

| finding_id | pre_change_status | closure_status | owning_contract | exact section/mechanism | verification evidence | implementation range/commit | limitations |
|---|---|---|---|---|---|---|---|
| FF01 | GAP PRESENT | CLOSED | `references/session-orchestration.md` | `Session Intent`; `Baseline relation and mismatch routing`: `CHANGE_REVIEW` is a read-only startup intent; non-matches stop `RESUME`, `EXTEND`, and current `PROJECTION_REPAIR`. | R01; IR06, IR08, and IR10 require the three mismatch routes and contextual-only reconciliation. | `bff1460`, `16bb095`, `46062b2` within `bff1460..615862c` | Static contract evidence only; no runtime route execution is claimed. |
| FF02 | GAP PRESENT | CLOSED | `references/shared-evidence-model.md` | `4.1 Change Review immutable bindings and review-local artifacts`: separate immutable `base_binding` and `candidate_binding`, each with repository, qualification, ref input, resolved commit, and resolved tree. | CR04–CR06 require configured/bound A→B and main→PR-head review states; BB01–BB05 require exact binding equality for reconciliation. | `7c6ad7f` within `bff1460..615862c` | Binding resolution is specified and matrix-checked; no live branch or PR resolution is claimed. |
| FF03 | GAP PRESENT | CLOSED | `references/shared-technical-model.md` | `5.1 Change Review candidate barrier`: `CR-*`, `CF-*`, and `CRF-*` remain review-qualified evidence; only explicit `RECONCILE_CHANGE` may present a candidate slice to the Technical Model Gate. | AB01–AB08 forbid candidate use as accepted STM, CQ, TE, CC, Product, or projection authority; Complete-claim checks retain the lifecycle barrier. | `7c6ad7f`, `1be5618`, `9f3d39e` within `bff1460..615862c` | Owner behavior is contract evidence, not runtime promotion/adjudication evidence. |
| FF04 | GAP PRESENT | CLOSED | `references/shared-evidence-model.md` | `4.3 Reuse and tree-equivalence proof`: `TREE_EQUIVALENT` permits only `WHOLE_TREE_EQUAL` or `FROZEN_RELEVANT_SCOPE_EQUAL` with mandatory retained proof fields; fuzzy/partial proof is denied. | MR01–MR09 exercise exact reuse, both proof levels, merge/squash/cherry-pick conditions, and explicit denial without proof; CR09–CR12 and CR31 cover their routing consequences. | `d299700`, `5ef82c4` within `bff1460..615862c` | Proof retention is specified; no Git graph or tree comparison was executed by this artifact. |
| FF05 | GAP PRESENT | CLOSED | `references/review-modes-and-orchestration.md` | `Contextual RECONCILE_CHANGE owner dispatch`: reusable, exact-bound, explicitly confirmed reviews dispatch only the minimum candidate slices to their existing owners and retain `candidate_origin`. | BB01–BB05 verify dispatch eligibility and rejection on binding mismatch; CR27–CR29 require owner-controlled writes or prohibit dispatch. | `bb0281d`, `615862c` within `bff1460..615862c` | The rows prove routing requirements, not that an owner mutation occurred. |
| FF06 | GAP PRESENT | CLOSED | `references/session-orchestration.md` | `Contextual reconciliation and baseline advancement`: `BASELINE_ADVANCE_ALLOWED` requires exact current bindings, complete material-delta accounting, required owner/technical/coverage gates, and policy-handled unknowns. | BB01–BB05 exercise eligibility and mismatches; PRC01–PRC05 and CR30–CR35 retain no-advance partial and policy-accounting cases. | `bb0281d`, `615862c` within `bff1460..615862c` | Baseline advancement remains a gated normative decision; no baseline was advanced by validation. |
| FF07 | GAP PRESENT | CLOSED | `references/projection-impact.md` | `0.1 Candidate prediction versus actual impact`: prediction is CR-bound advisory evidence and cannot write freshness; `1. Stabilized semantic-delta input` reserves actual impact for accepted stabilized semantics. | PI01–PI06 require prediction retention, reject candidate freshness writes, and defer explicit `RG-*`; CR22–CR23 and CR36 retain the prediction/actual split. | `5203e44`, `74b04f1` within `bff1460..615862c` | No Stage B impact analysis or regeneration was run; the closure is contract-level separation. |
| FF08 | GAP PRESENT | CLOSED | `references/shared-evidence-model.md` | `4.1 Change Review immutable bindings and review-local artifacts`: branch, tag, PR ref, checkout state, and `HEAD` are input metadata resolved into immutable commit/tree bindings; `references/review-modes-and-orchestration.md` `Change Review candidate execution mode` defines `CHANGE_REVIEW_CANDIDATE`. | CR04–CR06 require feature-branch, unmerged, and main→PR-head candidate scenarios; CR07–CR08 preserve advance/diverge handling. | `bff1460`, `7c6ad7f`, `9f3d39e` within `bff1460..615862c` | Candidate mode is specified and matrix-checked; no live branch/commit/PR adapter is claimed. |

Expected post-implementation result: `8/8 CLOSED` by directly identified
normative mechanisms, with the limitations stated above.

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

scenario_identity_source: approved design CR01–CR36

| ID | Source relation / request | Allowed intent | Authority mutation | Candidate state | Canonical state | Projection state | Next action |
|---|---|---|---|---|---|---|---|
| CR01 | accepted A, current main B; open RESUME | mismatch route only | none | no CR yet | A retained | unchanged | CHANGE_REVIEW or REVALIDATE |
| CR02 | A/B mismatch; EXTEND API Report | blocked EXTEND | none | no CR yet | A retained | unchanged | review/revalidate/reconcile |
| CR03 | A/B mismatch; PROJECTION_REPAIR | blocked current repair | none | no CR | A retained | unchanged | reconcile or historical context |
| CR04 | accepted A, feature B startup | CHANGE_REVIEW recommended | none | pending CR | A retained | unchanged | configure A→B |
| CR05 | A→unmerged B | CHANGE_REVIEW | none | COMPLETE/NOT_RECONCILED | A | unchanged | keep or reconcile |
| CR06 | main→PR head | CHANGE_REVIEW | none | candidate-bound | main state | unchanged | owner review/reconcile |
| CR07 | reviewed A→B, branch advances C | linked B→C review | none | CR old immutable, new linked | A | unchanged | review C or reconcile reusable |
| CR08 | reviewed B, candidate diverges D | new CHANGE_REVIEW | none | old historical, new candidate | A | unchanged | inspect D |
| CR09 | B no-ff merged M, tree(M)=tree(B) | contextual reconcile | only after owner gates | TREE_EQUIVALENT | M after reconcile | actual impact after reconcile | explicit reconcile |
| CR10 | B squash merged M, relevant tree equal | contextual reconcile | only after gates | TREE_EQUIVALENT | M after reconcile | actual impact after reconcile | explicit reconcile |
| CR11 | conflict merge changes relevant tree | new/supplemental review | none initially | reuse denied | A | unchanged | review B→M or A→M |
| CR12 | only b1,b2 of reviewed b1..b3 cherry-picked | conditional reuse | none without proof | partial/conditional | A | unchanged | decompose or new review |
| CR13 | candidate adds endpoint | CHANGE_REVIEW | none | CF candidate + predicted API impact | old endpoint state | unchanged | reconcile via STM gate |
| CR14 | candidate removes endpoint | CHANGE_REVIEW | none | candidate removal | old fact retained | unchanged | owner retirement on reconcile |
| CR15 | path changes | CHANGE_REVIEW | none | identity delta candidate | old fact retained | unchanged | CC/STM owner adjudication |
| CR16 | handler file moved, route same | CHANGE_REVIEW | none | source movement, likely no semantic delta | A | unchanged | evidence assessment |
| CR17 | new MEDIUM CQ issue | CHANGE_REVIEW CQ | none | CRF MEDIUM | old CQ unchanged | unchanged | CQ adjudication if reconcile |
| CR18 | candidate may fix HIGH CQ | CHANGE_REVIEW CQ | none | effect POTENTIALLY_RESOLVES | HIGH unchanged | unchanged | CQ re-adjudication |
| CR19 | fixes HIGH, adds MEDIUM | CHANGE_REVIEW | none | effect + CRF | both old/new pending | unchanged | reconcile both owner slices |
| CR20 | candidate finding rejected | reconcile | CQ may reject only | CRF historical rejected | no canonical finding | actual impact only if accepted facts changed | retain history |
| CR21 | CRF maps existing CQ-088 | reconcile | CQ adjudicates duplicate/link | CRF origin retained | CQ-088 unchanged until adjudication | unchanged | record origin/adjudication |
| CR22 | prediction says impact, actual none | reconcile then impact | accepted owners only | prediction retained | accepted unchanged | no actual impact | keep historical prediction |
| CR23 | prediction none, actual impact | reconcile then impact | accepted owners only | prediction retained | accepted delta | dependent projections impacted | explicit RG if wanted |
| CR24 | Product A changed only | Product CR | qualified A only | member-qualified | B untouched | Product impact qualified | reconcile affected vector |
| CR25 | multiple member revisions | Product CR | qualified vector | vector-bound | per-member authority | qualified impact | reconcile each required owner |
| CR26 | unknown cross-boundary impact | CR with expansion | none until evidence | CONTEXT_EXPANSION_REQUIRED | A | unchanged | expand or block completion |
| CR27 | bounded review completes with unknown | CHANGE_REVIEW | none | COMPLETE + UNKNOWN_IMPACT | A | unchanged | show limitation; optional reconcile |
| CR28 | user keeps review only | no reconcile | none | COMPLETE/KEPT_REVIEW_ONLY | A | unchanged | historical reuse/comparison |
| CR29 | compare B and C | comparison view | none | two immutable CRs | A | unchanged | user chooses candidate |
| CR30 | reconcile, decline regeneration | reconcile then defer RG | accepted owner changes only | RECONCILED | baseline B accepted if gate passes | affected projections STALE/deferred | explicit later RG |
| CR31 | reviewed B, new main tree equivalent | contextual reconcile | only after proof/gates | TREE_EQUIVALENT | new main after reconcile | actual impact | reuse with proof |
| CR32 | current branch advances B→C | linked incremental CR | none yet | ADVANCED | A | unchanged | review B→C |
| CR33 | current branch diverges | new CR required | none | DIVERGED old review | A | unchanged | bind new candidate |
| CR34 | no accepted baseline, compare commits | standalone CR | none | candidate comparison | no accepted baseline | unchanged | retain/review; no acceptance |
| CR35 | source advances, no semantic delta | REVALIDATE/reconcile | owner confirms no delta | COMPLETE/RECONCILED | baseline may advance to B | actual no impact | continue normal workflow |
| CR36 | documentation-only change | CHANGE_REVIEW | none unless accepted semantic effect | inventory/assessment docs delta | A | unchanged or actual doc-only impact after reconcile | keep or reconcile |

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
