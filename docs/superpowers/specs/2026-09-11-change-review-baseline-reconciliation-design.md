# Change Review and Baseline Reconciliation

## Status and scope

This is an architecture design for a first-class, read-only review of a source
candidate against an immutable base, followed by an explicit reconciliation
path. It is based on `main` at
`5be8bbd8a5869bb74d4a2ee804c695cb19620008`. It does not implement the design,
change existing contracts, or authorize a plan.

## 1. Problem

The existing suite can review an accepted source baseline and can revalidate
accepted state, but it has no first-class artifact for answering “what would
change if this branch, commit, or PR were considered?” A candidate review must
explain source deltas, affected facts, new and removed candidate facts, risks,
finding effects, assurance impact, contract impact, and predicted projection
impact without treating the candidate as accepted system truth.

## 2. Current failure mode

The current startup contract binds substantive work to one accepted/project
baseline and distinguishes `REVALIDATE` from projection repair, but it does not
persist a two-state `BASE`/`CANDIDATE` comparison. Consequently a non-accepted
branch can be mistaken for current source, a changed baseline can enter
`RESUME`/`EXTEND` without an explicit impact decision, and candidate findings
have no durable review-local boundary. Dependency traversal can identify
affected accepted facts, but it cannot by itself discover entirely new facts
for which no accepted dependency edge exists.

## 3. Goals

This design provides:

- an explicit `CHANGE_REVIEW` orchestration intent;
- immutable, exact base/candidate source bindings for branches, commits, tags,
  PR refs, and arbitrary ref pairs;
- bounded change inventory and delta discovery, with context expansion when
  changed paths cross a material boundary;
- review-local candidate facts and findings that cannot be consumed as
  canonical state;
- explicit effects on existing findings without changing their lifecycle;
- predicted projection impact separate from actual Stage B impact;
- safe review reuse for exact and proven tree-equivalent candidates;
- conservative handling of advanced, diverged, merge, squash, and partial
  cherry-pick candidates;
- a contextual `RECONCILE_CHANGE` action routed through existing owners;
- a coherent baseline-advancement gate after reconciliation;
- Product/member-qualified comparison and single-project support.

## 4. Non-goals

This design does not define Git merge automation, PR approval, CI, release or
deployment approval, branch protection, automatic code changes, OpenAPI
generation, runtime source crawling, a runtime SCM daemon, continuous
monitoring, a new database, a fourth capability, a canonical candidate STM, a
new CQ registry, a Product authority, or a generic workflow engine.

## 5. Preserved invariants

- Shared Technical Model (STM) is **WHAT EXISTS**.
- Architecture Review is **WHAT IT MEANS ARCHITECTURALLY**.
- Test Engineering is **WHAT MUST BE PROVEN**.
- Code Quality Review is **WHAT IS POORLY IMPLEMENTED**.
- Technical Documentation is **HOW VERIFIED SYSTEM IS DESCRIBED**.
- Fact, finding, test gap, recommendation, and projection remain distinct.
- Technical Model Gate is the sole writer/acceptor of accepted shared facts.
- Architecture, CQ, TE, and Contract Verification retain current ownership.
- Product is an optional composition/view authority, never factual authority.
- `requested_work != resolved_work`.
- Accepted semantic state is distinct from projection state and freshness.
- Projection Impact Analysis records actual impact; it does not regenerate.
- No automatic regeneration or permission expansion occurs.
- Single-project mode remains valid.
- `CHANGE_REVIEW != REVALIDATE != RECONCILE_CHANGE !=
  PROJECTION_REGENERATION`.

## 6. Alternatives considered

### A. Extend `REVALIDATE` to absorb candidate review

This reuses a name but conflates “does accepted state remain valid?” with “what
would this unaccepted candidate mean?”. It would make a hypothetical candidate
look like current source and blur baseline advancement. Rejected.

### B. Automatic reconciliation and regeneration

This is convenient but violates the Technical Model Gate, CQ, TE, Architecture,
and projection lifecycle boundaries. It also makes review-only branches mutate
canonical state. Rejected.

### C. Separate read-only Change Review, contextual reconciliation, existing
impact analysis, and explicit regeneration

This adds only an orchestration intent and review-local evidence. It preserves
existing owners, keeps candidate state hypothetical, supports comparison and
reuse, and uses existing reconciliation and Stage B mechanisms after explicit
user choice. **Chosen.**

## 7. Chosen architecture

The startup family becomes:

```text
USE_EXISTING | NEW | RESUME | REVALIDATE | EXTEND |
CHANGE_REVIEW | PROJECTION_REPAIR
```

`CHANGE_REVIEW` is orchestration, not a capability. It resolves two immutable
source states, creates a review-local `CR-*` artifact, performs bounded delta
discovery and selected capability assessment in candidate mode, and ends with
review evidence. It does not change accepted state.

`RECONCILE_CHANGE` is not a startup intent. It is a contextual action shown
only for a completed, reusable review after explicit confirmation.

## 8. Baseline relation model

The coordinator compares the accepted project source binding with the intended
current source and records one routing-only relation:

```text
BASELINE_MATCH | BASELINE_ADVANCED | BASELINE_DIVERGED | BASELINE_UNKNOWN
```

`BASELINE_MATCH` permits normal `RESUME`, `EXTEND`, and
`PROJECTION_REPAIR`. `BASELINE_ADVANCED` means the intended source is a
descendant or otherwise advances the accepted binding; `BASELINE_DIVERGED`
means no safe linear relation is established; `BASELINE_UNKNOWN` means the
relation or source is unavailable. The latter three show the mismatch and
offer `CHANGE_REVIEW` and/or `REVALIDATE`; a reusable review also offers
`RECONCILE_CHANGE`. None of these classifications marks STM or a projection
stale, resolves findings, or proves a semantic change.

## 9. Source ref resolution

Friendly refs are accepted only after existing repository authorization checks
and are resolved before substantive review to:

```text
repository_id
ref_input
resolved_commit
resolved_tree
project_binding
product_member_binding: optional exact vector
```

A persisted Change Review stores `base_ref`, `base_commit`, `base_tree`,
`candidate_ref`, `candidate_commit`, and `candidate_tree`, plus the exact
Project/Product qualification. `HEAD` has no special semantics. Branch movement
cannot alter an existing review. A PR is an input pair, not an approval system.

## 10. Change Review intent

At startup, the coordinator first resolves repository/scope and baseline
relation, then offers context-sensitive actions, then exposes the ordinary
requested-work and capability/output configuration. On a non-accepted branch,
the recommended action is Change Review against the accepted baseline; it is
never automatic promotion.

The intent supports “change impact only”, Architecture impact, Code Quality
impact, Test impact, Interface/contract impact, and explicit full change
review. A full change review selects all requested lenses only when the user
chooses it. Change Review does not silently select all three capabilities.

## 11. Change Review configuration

The compact configuration is:

```text
base: accepted baseline | branch | commit | tag | PR base | custom ref
candidate: current HEAD | branch | commit | tag | PR head | custom ref
scope: PROJECT | PRODUCT
lenses: change-only | architecture | code-quality | test |
        interface-contract | explicit full change review
outputs: summary | inventory | affected facts | candidate findings |
         existing finding effects | test impact | projection prediction
```

Each ref is resolved and displayed with its exact commit/tree before
confirmation. Existing capability configuration is reused; candidate execution
is marked `CHANGE_REVIEW_CANDIDATE` and is read-only with respect to accepted
authority.

## 12. Change Review artifact

`CR-*` is a stable orchestration artifact identity. It is not STM, a finding,
a test result, a projection, or Product state. Revisions may correct a draft,
but a completed review’s meaning is immutable; later source states use linked
reviews rather than rewriting it.

Conceptual record:

```text
review_id: CR-0042
base: {repository_id, ref, commit, tree, qualification}
candidate: {repository_id, ref, commit, tree, qualification}
review_scope: bounded Project/Product scope and lenses
change_inventory: CI-* or embedded immutable inventory
affected_authority_refs: existing STM/finding/test/projection refs
candidate_facts: CF-* review-local entries
candidate_findings: CRF-* review-local entries
existing_finding_effects: effect records
assessment: capability-qualified interpretation
predicted_projection_impact: prediction records
completeness: bounded review dimensions and limitations
review_status: DRAFT | IN_PROGRESS | REVIEW_REQUIRED | COMPLETE | BLOCKED | SUPERSEDED
decision: NOT_RECONCILED | RECONCILED | KEPT_REVIEW_ONLY
reuse_state: EXACT | TREE_EQUIVALENT | ADVANCED | DIVERGED | UNAVAILABLE
```

`COMPLETE` means the selected bounded review work is complete, not that the
candidate is accepted or risk-free. `UNKNOWN_IMPACT` may be reported as an
explicit limitation.

## 13. Change Inventory

The inventory is factual delta observation, separate from assessment. It
records added, modified, removed, and moved files and bounded candidate
surfaces: interfaces/operations, data stores/migrations, integrations,
events, flows, auth/config, contracts, and other observed source candidates.
Each observation carries exact source-state/evidence binding and a discovery
completeness status. The inventory does not label severity, materiality,
compatibility, architectural meaning, or finding lifecycle.

## 14. Delta discovery

The default flow is:

```text
BASE..CANDIDATE diff
→ changed paths and evidence scope
→ bounded candidate discovery
→ additions/modifications/removals
→ reconcile with accepted references
→ Change Assessment
```

Changed paths are routing context, not proof. Discovery may expand to a
necessary related boundary and records `CONTEXT_EXPANSION_REQUIRED` while that
slice is unresolved. It does not require full repository rediscovery by
default. Dynamic or unavailable evidence is reported as an explicit limitation,
not silently treated as no change.

## 15. Change Assessment

Assessment interprets inventory and evidence. It separately records affected
existing facts, new/removed candidate facts, effects on existing findings,
candidate findings, Architecture meaning, test impact, contract impact, risk,
predicted projection impact, and unknowns. `WHAT CHANGED` remains distinct from
`WHAT THE REVIEW THINKS IT MEANS`.

## 16. Candidate facts

New facts use review-qualified `CF-*` entries, qualified by `CR-*`, candidate
source binding, scope, evidence, and candidate status. Statuses may include
`CANDIDATE`, `UNRESOLVED`, `DUPLICATE_OF`, `SUPERSEDES_CANDIDATE`,
`NON_MATERIAL`, and `REJECTED`. A CF is never an accepted STM fact and cannot
be used as a downstream semantic dependency. At reconciliation, the Technical
Model Gate alone decides whether it becomes a new fact, duplicate, supersession,
non-material observation, rejection, or unresolved item.

## 17. Candidate findings

Candidate issues use `CRF-*`, qualified by review, candidate state, owning
capability, severity/classification, evidence, and affected CF/existing refs.
They remain review evidence. CQ, Architecture, TE, or CC may later create,
merge, duplicate, reject, or reclassify a canonical record. A CRF ID is never
reused as a canonical finding ID.

## 18. Existing finding effects

An assessment references existing findings and uses only:

```text
UNAFFECTED | POTENTIALLY_RESOLVES | MITIGATES | WORSENS |
INVALIDATES_PRIOR_ASSUMPTION | UNKNOWN_IMPACT
```

Candidate assessment never writes `RESOLVED`, `CLOSED`, or `ACCEPTED` as its
own lifecycle. At reconciliation, the owning authority may adjudicate an
existing finding using accepted evidence; the CR effect remains historical
traceability.

## 19. Candidate authority barrier

`CR-*`, `CF-*`, and `CRF-*` may be consumed only as review evidence, routing
context, historical comparison, or reconciliation input. They cannot satisfy
STM, CQ, TE, CC, Product, or projection semantic dependencies. Candidate mode
must prevent writes to accepted records; the final reconciliation dispatch is
the only path that may invoke owning writers.

## 20. Review completeness

Review completeness reuses existing evidence and coverage concepts rather than
creating a second global coverage framework. The artifact reports:

```text
change_inventory: COMPLETE | PARTIAL | UNKNOWN
affected_authority_coverage: COMPLETE | PARTIAL | UNKNOWN
candidate_discovery_coverage: COMPLETE | PARTIAL | UNKNOWN
selected_capability_assessment: COMPLETE | PARTIAL | UNKNOWN
unknown_impact: NONE | PRESENT
```

`COMPLETE` is bounded to the frozen base, candidate, scope, evidence, and
selected lenses. It may coexist with `UNKNOWN_IMPACT` when the limitation is
visible; it must not claim all impacts were found.

## 21. Review lifecycle

`DRAFT → IN_PROGRESS → REVIEW_REQUIRED → COMPLETE` is the normal flow;
unavailable evidence may lead to `BLOCKED`, and a superseded review remains
historical as `SUPERSEDED`. Completion and reconciliation are separate. A
completed review normally has `decision: NOT_RECONCILED` until an explicit
contextual action succeeds.

## 22. Reuse state

Reuse is classified as:

- `EXACT`: same repository, exact candidate commit/tree and qualification;
- `TREE_EQUIVALENT`: different commit identity but identical relevant candidate
  tree and qualification, with an equivalence proof and no omitted relevant
  delta;
- `ADVANCED`: intended candidate is a supported continuation of the reviewed
  candidate;
- `DIVERGED`: candidate no longer safely represents it;
- `UNAVAILABLE`: equivalence cannot be established.

SHA equality alone never permits reuse.

## 23. Advanced/diverged candidate behavior

An advanced branch creates an immutable linked review, for example `CR-0043`
for `B→C` with `parent_review: CR-0042`; it does not mutate `CR-0042` into
`A→C`. A desired A→C comparison creates an explicitly bound new review.
Divergence requires a new review. Old reviews remain evidence and cannot supply
current candidate findings without a reuse proof.

## 24. Merge/squash/cherry-pick equivalence

A no-ff merge or squash may reuse a completed review as `TREE_EQUIVALENT` when
repository identity, relevant candidate tree, qualification, and scope all
match. The resulting commit and equivalence proof are retained. Conflict
resolution that changes relevant content requires a supplemental/new review.
Partial cherry-pick reuse is `CONDITIONAL`: it is allowed only when the selected
subset is independently decomposable and the proof covers omitted commits;
otherwise a new bounded review is required.

## 25. Comparative candidate review

Comparing `A→B` with `A→C` is a view over immutable CR artifacts. It can show
different effects, risks, migration impact, and unknowns without adjudicating,
accepting, or creating any semantic authority.

## 26. REVALIDATE relationship

`REVALIDATE` re-evaluates previously accepted technical state against an
intended current baseline and may use a compatible CR as evidence/routing input.
Owning authorities still adjudicate. A CR is not a revalidation result.

## 27. RECONCILE_CHANGE

This contextual action requires a completed review, reusable candidate, usable
evidence, coherent scope, and explicit user choice. It dispatches only the
minimum affected slice to existing owners, then performs accepted semantic
delta accounting, baseline advancement gating, and actual Projection Impact
Analysis. It does not merge Git, approve release, resolve every finding, or
regenerate projections.

## 28. Reconciliation ownership

```text
CF / accepted technical facts       → Technical Model Gate
Architecture impact                 → Architecture Review authority
candidate CQ / CQ effects           → Code Quality authority
test impact and reproof             → Test Engineering authority
provider/consumer contract impact  → Contract Verification authority
Product composition impact          → existing Product semantics
```

The CR only carries qualified inputs and traceability. Existing records are
updated only by their owner.

## 29. Baseline advancement

Review completion never advances the accepted source baseline. Advancement is
allowed only after the intended exact source state is established, all
material candidate delta in the coherent selected scope is accounted by the
owning authorities, required semantic/coverage gates pass, and unresolved
limitations are explicitly allowed by existing policy. Partial reconciliation
cannot mark the whole baseline reconciled. Open findings may remain in an
accepted baseline unless an existing policy blocks acceptance; baseline
reconciliation is not release approval.

## 30. RESUME behavior

If the current source matches the accepted baseline, `RESUME` restores the
persisted package. Otherwise it returns `SOURCE_BASELINE_MISMATCH` and does not
continue as current. It offers `CHANGE_REVIEW`, `REVALIDATE`, and, where a
reusable completed CR exists, `RECONCILE_CHANGE`; none runs automatically.

## 31. EXTEND behavior

With unresolved mismatch, `EXTEND` returns
`BASELINE_RECONCILIATION_REQUIRED`. It cannot extend stale accepted semantics
for B as if they describe B. After reconciliation to B, ordinary additive
EXTEND may proceed. This is not an implicit combined review/reconciliation/
extension workflow.

## 32. PROJECTION_REPAIR behavior

If source differs from the accepted baseline,
`PROJECTION_REPAIR` is blocked for a current representation pending source
reconciliation. Historical repair could be offered only if explicitly labeled
as the accepted historical baseline and already supported; no new historical
repair mode is introduced here.

## 33. USE_EXISTING behavior

`USE_EXISTING` may load accepted package A, but must display A and current B
separately. It cannot present A as current for B or bypass mismatch routing.

## 34. NEW behavior

`NEW` remains a new review package and is unaffected by accepted-state
reconciliation. If no accepted baseline exists, `CHANGE_REVIEW` may still
compare any two authorized refs as an independent candidate comparison; it
creates no accepted semantic state.

## 35. Projection prediction

Candidate assessment may record:

```text
NO_EXPECTED_IMPACT | LIKELY_AFFECTED |
DEFINITELY_AFFECTED_IF_ACCEPTED | UNKNOWN_IMPACT
```

It must never write Stage B `CURRENT`, `STALE`, or `BLOCKED`. A later actual
impact result does not rewrite the historical prediction.

## 36. Actual Projection Impact

Only after reconciliation stabilizes accepted semantic state does existing
Projection Impact Analysis evaluate accepted dependencies. It may find no
impact despite a prediction, or impact despite no prediction. Actual impact is
qualified to accepted source, Project/Product binding, and projection
dependencies.

## 37. Regeneration boundary

After actual impact accounting, the user may explicitly select affected
projections for existing `RG-*` regeneration. Declining leaves them visibly
`STALE` or otherwise pending under current lifecycle policy. There is no
automatic regeneration and no CR-driven freshness mutation.

## 38. CQ integration

Candidate CQ assessment can reference existing or candidate interface,
operation, property, and boundary evidence. It cannot create/revise operations,
accept inventory, or mutate a CQ registry. At reconciliation CQ adjudicates a
CRF or existing-finding effect and creates/links canonical CQ identity as
appropriate.

## 39. TE integration

Candidate TE assessment can identify invalidated tests, new assurance cases,
or changed boundaries per operation. It cannot mark `TESTED`, pass, or fail an
execution without accepted execution evidence. `accepted_test_case`,
`executed_test`, and `TESTED` remain independent.

## 40. Architecture integration

Architecture impact is candidate-qualified interpretation of accepted and
candidate facts. It does not create accepted Architecture findings. On
reconciliation, Architecture authority independently adjudicates the affected
slice.

## 41. STM integration

STM remains the sole accepted factual model and Technical Model Gate remains
the only acceptance writer. New/removal/mutation observations remain CFs until
reconciliation. Deletion preserves canonical history; owner lifecycle decides
retirement/supersession/current membership.

## 42. Contract/API integration

API operation completeness is reused: candidate endpoint additions, removals,
method/path, auth, schema, and boundary changes remain candidate facts. After
reconciliation, operation inventory and coverage are updated through existing
STM/Technical Model Coverage authority. Provider/consumer matching remains
non-authoritative input to Contract Verification; same address is not proof of
compatibility.

## 43. Product/multi-project behavior

Product Change Review binds a Product revision and immutable member baseline
vector. Each member candidate has its own Project/repository/commit/tree
binding. A change in member A does not mark B affected unless qualified
relations justify it. Divergent paths, schemas, auth, limits, availability, and
revisions remain member-qualified. Product selection grants no source or
semantic-write permission.

## 44. User-facing UX

When mismatch exists, show:

```text
Accepted technical baseline: main @ A
Current source: feature/foo @ B
Status: source differs from accepted review baseline

1. Review feature/foo against accepted baseline
2. Revalidate accepted state against feature/foo
3. Review another branch/commit
4. Continue with accepted A as historical context only
5. Reconcile previously reviewed candidate   (only when reusable)
```

Change Review completion shows base, candidate, scope, changed files, candidate
facts/findings, existing effects, impact lenses, predictions, limitations, and
these user-facing actions: `KEEP_REVIEW_ONLY`, `REVIEW_UPDATED_CANDIDATE`,
`COMPARE_ANOTHER_CANDIDATE`, `RECONCILE_CHANGE`, and `MARK_SUPERSEDED`.

## 45. Security/authorization

Ref resolution, source trees, evidence, and Product members use existing
authorization. A branch, commit, PR, or Product selection grants no additional
read or write permission. Review artifacts must disclose only evidence the
user can access. No merge, release, deployment, or SCM administration is
implied.

## 46. Backward compatibility

Existing six intents, accepted facts, findings, tests, Products, projections,
and baselines remain readable. CR/CF/CRF artifacts are additive. Historical
records are not rewritten. A review of a surface-only state may identify
unknown candidate depth, but cannot silently convert it to accepted current
state.

## 47. Migration classification

`COMPATIBLE_EXTENSION`. Existing packages need no blanket migration. New
baseline relation metadata may be absent/`BASELINE_UNKNOWN` until resolved;
absence never proves match. Existing accepted state continues to serve its
historical baseline and is not invalidated merely because Change Review exists.

## 48. Pressure scenarios CR01–CR36

In the table, “mutation” means mutation of accepted authorities. `none` means
the CR may persist review evidence only.

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

## 48a. Explicit architecture decisions

| Question | Frozen answer |
|---|---|
| Is Change Review a new orchestration intent? | Yes, `CHANGE_REVIEW`. |
| Is it a capability? | No; the three semantic capabilities remain unchanged. |
| Is `CR-*` semantic authority? | No; it is a review artifact identity. |
| Are CFs canonical STM? | No; they are review-local candidates. |
| Are CRFs canonical findings? | No; owners adjudicate them later. |
| Can Change Review mark an existing finding resolved? | No; it records only a candidate effect. |
| Can it mark a projection stale? | No; only accepted semantic impact accounting can. |
| Can it regenerate projections? | No; regeneration remains explicit Stage B work. |
| Can it use arbitrary branch/commit/PR refs? | Yes, subject to existing authorization and exact ref resolution. |
| How are refs frozen? | Persist exact repository, commit, tree, and Project/Product qualification. |
| How is tree equivalence used? | Reuse is allowed only with matching relevant tree, scope, qualification, and proof; SHA equality is insufficient. |
| How is an advanced candidate handled? | Create an immutable linked incremental review. |
| How is divergence handled? | Require a new explicitly bound review. |
| How is partial cherry-pick handled? | Conditional reuse only with independently decomposable proof; otherwise review anew. |
| How is conflict-merge handling done? | A changed relevant tree requires supplemental/new review. |
| How are new facts discovered? | Bounded diff-guided discovery with evidence and context expansion. |
| How are removed facts represented? | Candidate removal in the CR; canonical fact remains until owner reconciliation. |
| How are existing facts referenced? | By existing canonical IDs/revisions plus exact source qualification. |
| How are candidate findings traced? | `candidate_origin: CR-*/CRF-*` is recorded on the later owner adjudication. |
| How does reconciliation work? | Explicit contextual action dispatches each affected slice to its existing owner, then gates baseline advancement and actual impact. |
| Is reconciliation a startup intent? | No; it is contextual when a reusable completed CR exists. |
| When does baseline advance? | Only after coherent, complete owner reconciliation for the intended exact source state. |
| How do RESUME/EXTEND behave on mismatch? | They stop current-state continuation and offer review/revalidation/reconciliation. |
| How does PROJECTION_REPAIR behave? | It blocks current repair pending source reconciliation; no new historical mode is introduced. |
| What is predicted projection impact? | A CR-qualified forecast, never a Stage B freshness state. |
| When does actual impact run? | After accepted reconciliation and before optional explicit regeneration. |
| What if regeneration is declined? | Accepted semantics remain; affected projections stay visibly stale/deferred. |
| How does Product qualify review? | By exact member baseline/revision vectors; no unqualified Product diff is created. |
| How does candidate mode preserve authority? | `CHANGE_REVIEW_CANDIDATE` routes outputs to review-local records and forbids accepted writes. |
| What prevents a shadow STM? | Downstream gates/selectors reject CF/CRF/CR as accepted dependencies; only owner reconciliation can create canonical records. |

## 49. Open questions

The following are deliberately implementation-level rather than unresolved
architecture decisions: exact Markdown field ordering, storage path, numeric
allocation mechanism for `CR-*`/`CF-*`/`CRF-*`, and the concrete adapter used
to resolve an authorized PR ref. They must preserve the frozen semantics above.

## 50. Acceptance criteria

The design is accepted only if implementation planning can demonstrate:

1. `CHANGE_REVIEW` is an orchestration intent and not a capability.
2. Base and candidate are exact, immutable, scope-qualified source states.
3. CR/CF/CRF never become shadow canonical authorities.
4. Candidate findings and existing finding effects remain owner-qualified.
5. `RESUME`, `EXTEND`, and `PROJECTION_REPAIR` cannot silently bypass mismatch.
6. Review completion cannot advance the baseline or mark projections stale.
7. Reconciliation invokes existing owners before baseline advancement.
8. Actual Stage B impact and explicit regeneration remain separate from
   prediction and review completion.
9. Exact/tree-equivalent, advanced, diverged, merge, squash, and partial
   cherry-pick behavior is deterministic and provenance-preserving.
10. Product vectors and single-project scope remain qualified and supported.
11. CR01–CR36 resolve deterministically with no hidden approval semantics.
12. No runtime scanner, generic workflow engine, fourth capability, or new
   semantic authority is required.
