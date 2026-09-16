# Finding Lifecycle & Progress Reporting — Design

## 1. Status

`DESIGN REVIEW REMEDIATED`

`IMPLEMENTATION NOT STARTED`

This document records discovery and a proposed compatible extension. It does
not approve or change any normative runtime or skill contract.

## 2. Problem Statement

The repository already preserves accepted semantic records, revisions,
provenance, source bindings, and derived projections. It does not yet give all
finding families one equally explicit way to distinguish the historical
registry from the materially current risk set. A cumulative registry count can
therefore be mistaken for current risk: a product can register 100 findings,
resolve 40, and discover 10 more while the historical total rises to 110 and
the current risk falls to 70.

The design must preserve traceability and authority while making every finding
metric identify whether it is a stock, a flow, or a classification.

## 3. Existing Architecture Findings

### EXISTING authority and identity

The authority map in `docs/concepts/authority-and-provenance.md` (§ “Карта
источников истины”) identifies `RF-*` as the source of truth for architectural
conclusions and `CQ-*` as the source of truth for Code Quality conclusions;
reports, `INDEX.md`, and projections are not semantic authority.
`references/root-boundary-adjudication.md` (§ “Root finding (`RF-*`)” and “Product RF root
boundary”) requires one concrete mechanism, coherent owner/scope, correction
boundary, reachable effect, and qualified Product provenance where applicable.

`docs/reference/artifacts.md` (§ Families and operational rules) says that an
`RF-*` has stable identity, boundary, consequence, severity, and STM/evidence
links; changes to facts, boundary, consequences, or limitations trigger
revalidation or a replacement finding. The concise artifact table does not
enumerate every RF lifecycle field, but `references/evidence-and-severity.md`
§ “Product RF evidence and severity binding” and `references/review-method.md`
§ 7 explicitly preserve an existing Architecture RF lifecycle vocabulary and
make it authoritative. This design therefore extends that owner contract; it
does not replace or create a competing RF lifecycle.

### EXISTING lifecycle semantics

`capabilities/code-quality-review/references/code-quality-lifecycle.md` §§
“Finding lifecycle”, “Applicability”, “Freshness”, and “Targeted revalidation”
already define:

```text
ACTIVE -> RESOLVED
ACTIVE -> SUPERSEDED
```

`RESOLVED` requires evidence-backed revalidation that the issue no longer
exists. `SUPERSEDED` requires a materially different replacement authority or
equivalent adjudication and allocates a new identity for a distinct issue.
`ACCEPTED_EXCEPTION` and `WONT_FIX` are real active findings, not resolution;
`CQRA COMPLETED != CQ RESOLVED`. `ACTIVE + STALE` is valid, while
`RESOLVED + CURRENT` is the evidenced resolution state.

The same contract states that a stale or insufficiently evidenced finding is
not deleted or resolved, and that invalidated resolution evidence is reopened
through adjudication or retained as historical superseded material. This is
the closest existing complete finding lifecycle and is the model to reuse.

### EXISTING candidate and Change Review semantics

`references/evidence-and-severity.md` (§ Candidate lifecycle) requires
candidate → independent verification → root-boundary adjudication →
authoritative finding → severity adjudication → authoritative ledger.
`references/review-modes-and-orchestration.md` §§ “Change Review candidate
execution mode” and “Change Assessment and effect axes” make Change Review
read-only against accepted authority. `POTENTIALLY_RESOLVES` is an effect
record, not a lifecycle decision; only explicit, confirmation-gated
`RECONCILE_CHANGE` can hand the accepted delta to an owner.

### EXISTING freshness and projections

`docs/concepts/lifecycle-and-freshness.md` distinguishes semantic lifecycle,
semantic freshness, process state, and projection freshness. `references/
projection-lifecycle.md` §§ 1–4 explicitly excludes architecture findings and
semantic ledgers from `PRJ-*`, requires semantic changes to mark dependent
projections `STALE`, and requires explicit regeneration/verification. A stale
report cannot alter the finding authority.

### EXISTING Product semantics

`references/product-multi-project-review.md` §§ 1, 6–9 establish that Product
is context/composition, not technical finding authority. Its immutable Product
baseline stores an exact qualified member/source vector and accepted owner
references; baseline acceptance verifies bindings and limitations but does not
adjudicate child findings. The “Bottom-up child advancement” subsection
requires Product `REVALIDATE` or a complete-vector Product `CHANGE_REVIEW`;
child authority advancement never directly advances an accepted Product
baseline. `docs/roadmap.md` at the federated coordination milestone confirms
these semantics at the current canonical closeout.

### EXISTING gap relevant to this mission

The repository does not expose the complete Architecture RF lifecycle schema in
one concise artifact table, and it has no common derived Current Findings
contract. Product aggregation has exact qualification/freshness rules but does
not yet define the finding-level counters requested here. The discrepancies
described as “29 vs 17” and “36 vs 20” are therefore not proven to be one
specific bug: they may be historical/current ambiguity, stale INDEX or
projection material, or both. The future validation must inspect the ledger
and dependency snapshot before attributing any discrepancy.

## 4. Goals

- Reuse one minimal lifecycle model for authoritative finding families where
  the owning capability accepts it.
- Preserve immutable history, identity, revision, provenance, source/baseline
  binding, severity, and resolution/supersession evidence.
- Define deterministic derived Historical, Current, Resolved, Superseded, and
  accepted-risk views without a second finding authority.
- Make Product current-risk and baseline-to-baseline progress reproducible.
- Keep single-Project reporting complete without Product state.
- Keep Change Review candidate effects, semantic freshness, and projection
  freshness separate from accepted lifecycle.
- Provide conservative legacy migration and bounded Markdown validation.

## 5. Non-Goals

No runtime findings database, event-sourcing framework, analytics service,
dashboard, scheduler, watcher, ticket integration, remediation engine,
Finding Management/Risk/Progress capability, Product finding authority, new
Session Intent, new top-level capability, automatic reconciliation, or
automatic projection regeneration is proposed.

## 6. Authority Model

Finding authority remains capability-local:

| Finding | Authority | Product role |
|---|---|---|
| `RF-*` | Architecture Review | qualify and compose accepted child views |
| `CQ-*` | Code Quality Review | qualify and compose accepted child views |
| Test Engineering result/gap | Test Engineering | qualify its existing owned records |
| Product-scoped architectural root, if independently adjudicated | Architecture Review under Product scope | present only after owner adjudication |

The ledger is an authoritative owner artifact, not a generic Product registry.
Product may store qualified references in an immutable baseline and derive
reports, but may not create, resolve, supersede, reopen, or change severity of
a child finding. Cross-member equal IDs remain qualified by Product member,
owner, local identity, and accepted revision.

### Architecture RF Lifecycle Ownership

The existing Architecture Review authority remains the sole owner and writer
of the lifecycle, severity, disposition, and revision of `RF-*`. The exact
normative owner contract to extend in a future implementation is
`references/report-contract.md` § 4, “`02-authoritative-findings-ledger.md`”;
its ledger schema is the Architecture-owned persistence boundary for stable RF
ID, severity, evidence/provenance, supersession references, and accepted
owner decisions. The lifecycle vocabulary and root rules it must preserve are
cross-checked against `references/evidence-and-severity.md` § 10 and
`references/root-boundary-adjudication.md` §§ 1–6. No Product document,
projection, or index is an alternative RF owner.

The implementation extends the existing Architecture ledger by reference to
the shared reporting vocabulary below, while keeping acceptance local to
Architecture Review. It does not copy the CQ ledger or create a shared finding
database. Architecture Review (through its owner/adjudicator gate) alone may
accept:

| Change | Required Architecture authority |
|---|---|
| `ACTIVE → RESOLVED` | accepted evidence, owner revalidation, owner adjudication, and a new accepted RF revision bound to the proving source/evidence snapshot |
| `ACTIVE → SUPERSEDED` | owner adjudication, a qualified replacement/merge authority, and a new accepted revision/history link |
| `RESOLVED → ACTIVE` | owner adjudication of recurrence or invalidated resolution, a new accepted active revision, and `reopened_from` provenance |
| severity change | owner severity adjudication and a new accepted RF revision; identity is preserved when the root mechanism remains the same |
| disposition change | owner/governance decision recorded by the Architecture authority with rationale, scope, approver, and any policy-required reconsideration metadata |

The resolution acceptance gate is therefore:

```text
accepted RF evidence
→ Architecture owner revalidation against exact source/evidence binding
→ Architecture owner adjudication
→ accepted Architecture RF revision
```

Product is not a participant in this gate. Change Review may supply
candidate-qualified evidence and `POTENTIALLY_RESOLVES`, but accepted RF
mutation is impossible until explicit reconciliation routes the minimum slice
back to Architecture authority. Product can later qualify the accepted
revision; it cannot accept it.

### Scope of the common reporting model

The lifecycle/current/progress model in §§ 7–18 is normative for canonical
Architecture `RF-*` and Code Quality `CQ-*` findings only. Test Engineering
records (`BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*`) remain distinct
owner-owned semantic families. Their existing lifecycle and assurance
projections may be reported alongside findings, but they are not coerced into
RF/CQ lifecycle, accepted-risk, or Current Findings counters. Product consumes
their existing qualified TE views under `capabilities/test-review/SKILL.md` §§
163–184, not this finding adapter.

## 7. Finding Identity and Revision Model

The canonical identity is the stable owner-qualified finding identity (`RF-*`
or `CQ-*`), not a report row, candidate `CRF-*`, remediation action, or
projection. The same identity remains in use when the same mechanism and
correction boundary persist. Each accepted owner revision records at least:

```text
finding_id
owner_capability / qualified_project_or_product_scope
accepted_revision
lifecycle
disposition (when supported)
severity
source_binding / analyzed_baseline
freshness
evidence_refs
stm_refs
resolution_evidence (when RESOLVED)
supersedes / superseded_by (when SUPERSEDED)
reopened_from / resolution_invalidated_by (when reopened)
```

This is a revisioned extension of existing owner ledgers, not a new global
ledger. A revision is immutable after acceptance; a changed severity or
lifecycle is a new owner revision of the same identity when identity
semantics still hold. A materially different mechanism gets a new identity and
an explicit supersession/correlation link, as already required for `CQ-*` and
root-boundary adjudication.

## 8. Lifecycle Model

### EXISTING reused core

The canonical lifecycle after this design is:

```text
ACTIVE -> RESOLVED
ACTIVE -> SUPERSEDED
```

`ACTIVE` means the accepted problem remains materially applicable. `RESOLVED`
means accepted owner evidence proves the problem no longer materially exists
for the accepted source/evidence scope. `SUPERSEDED` means this identity is no
longer the current representation because another authority replaces it; it
does not prove the underlying risk was fixed.

`REOPENED` is deliberately a derived transition label, not a fourth persisted
lifecycle state. A resolved identity that recurs or whose resolution evidence
is invalidated receives a new owner-controlled `ACTIVE` revision with explicit
reopen provenance. A baseline comparison labels `RESOLVED → ACTIVE` as
`REOPENED`. This reuses the existing CQ lifecycle rather than introducing an
overloaded state enum.

No finding may become `RESOLVED` merely because remediation is complete,
source diff looks favorable, a candidate says so, or a projection omits it.

## 9. Disposition / Accepted-Risk Model

### EXISTING

For `CQ-*`, `ACCEPTED_EXCEPTION` and `WONT_FIX` already model a real active
finding with an explicit rationale/owner decision. They are not lifecycle
states and are not `RESOLVED`. `EXCLUDED` is applicability/scope exclusion,
not risk acceptance.

### PROPOSED compatible extension

Accepted risk is not a lifecycle state. It is an owner-controlled treatment
decision on an otherwise active finding, reported separately from technical
applicability:

```text
lifecycle: ACTIVE | RESOLVED | SUPERSEDED
disposition: ACTION_REQUIRED | owner-specific accepted-risk/deferred decision
remediation_status: owner-specific action/execution state (for example BLOCKED)
```

`ACTION_REQUIRED` is the reporting default, not a new authority. The canonical
stored disposition remains owner-qualified:

| Owner record | Common reporting classification | Exact equivalence |
|---|---|---|
| CQ `ACCEPTED_EXCEPTION` | `ACCEPTED_RISK` | yes: real active finding with explicit exception rationale and owner approval |
| CQ `WONT_FIX` | `OWNER_DECLINED_REMEDIATION` | no: remediation is declined, but this token is not automatically a governance risk acceptance |
| Architecture accepted-risk decision | `ACCEPTED_RISK` only after Architecture adopts it in the owner contract | defined by Architecture authority, not Product |
| Architecture/CQ deferred decision | `DEFERRED` only when that owner contract defines it | not inferred from age, remediation status, or report prose |

Architecture Review owns RF disposition changes through the § 6 gate;
Code Quality Review owns CQ disposition changes under
`capabilities/code-quality-review/references/code-quality-lifecycle.md` §§
“Applicability” and “State invariants”. Every accepted-risk decision requires
explicit human/governance approval, rationale, qualified scope, approver
provenance, and any owner-policy expiry/reconsideration metadata. Product may
normalize presentation only when the owner meaning is exactly equivalent; it
cannot create, approve, or change the disposition.

An accepted-risk finding remains materially current and remains in technical
Current Findings while its owner evidence is usable. It may become stale or
blocked exactly like any other active finding. A later owner decision can
change `ACCEPTED_RISK`/`ACCEPTED_EXCEPTION` or `WONT_FIX`/declined treatment to
`ACTION_REQUIRED` on a new accepted revision of the same identity; this emits
`ACCEPTED_RISK_REMOVED`, not `RESOLVED` or `NEW`. Accepted risk is excluded from
“actionable/open requiring remediation” only when the explicit owner decision
exists; remediation `BLOCKED` alone never qualifies as accepted risk.

## 10. Resolution Verification

Minimum transition evidence is:

1. accepted owner revalidation against an exact source/evidence baseline;
2. independent verification appropriate to the owner contract;
3. evidence showing the same mechanism/correction boundary no longer exists;
4. explicit owner adjudication creating the `RESOLVED` revision;
5. retained provenance to prior active revision, evidence, source binding, and
   resolution evidence.

For a changed mechanism, use replacement authority plus explicit owner
adjudication for `SUPERSEDED`; do not call the old record resolved. If required
evidence is missing, retain `ACTIVE` and mark freshness `STALE` or `BLOCKED`
under the existing freshness rules. Resolution evidence becoming
unverifiable causes owner adjudication to reopen the finding; it is never
silently presented as resolved.

### Resolution binding and source advancement

Every `RESOLVED` revision is an assertion about its exact accepted
source/evidence/dependency snapshot, not a timeless property of the identity.
When a material source binding, STM fact, dependency, or other resolution
prerequisite advances, the prior resolution remains historical but loses its
claim to prove absence for the newer state. Existing revalidation rules mark
the affected finding stale and require owner revalidation; the owner must then
either create an accepted `ACTIVE` revision (with `reopened_from` and the new
binding) or create/retain a qualified supersession outcome if the mechanism is
materially different.

Until that owner decision, the new baseline must not count the old revision as
`RESOLVED + CURRENT`, and must not invent `ACTIVE` without evidence. The
derived view exposes a separate `RESOLUTION_REVALIDATION_REQUIRED` uncertainty
row/limitation linked to the historical resolved identity. Thus the report
preserves both facts: “resolved for B” and “absence on C is not yet verified.”
This is a freshness/qualification condition, not a new lifecycle state.

## 11. Supersession Semantics

Supersession is identity replacement, not technical debt retirement. The old
record remains in the Historical Finding Registry with a directional
`superseded_by`/replacement reference.

- Duplicate merge: `RF-102 SUPERSEDED by RF-101`; this is not one issue fixed,
  and neither record contributes twice to Current Findings.
- Better representation: `RF-010 SUPERSEDED by RF-044`; `RF-044` is evaluated
  independently, and the old record does not count as resolved.
- A replacement must identify the owner, material mechanism/boundary, and
  adjudication evidence. Equal-looking IDs across Product members are never
  merged without qualified owner/scope authority.

## 12. Reopen Semantics

If the same root mechanism returns, preserve the finding identity and create a
new accepted `ACTIVE` revision with `reopened_from` pointing to the prior
resolved revision. The delta view emits `REOPENED`; historical “resolved at
least once” remains true, while current state is active.

If later evidence proves the prior resolution was invalid, record the evidence
that invalidated the resolution and owner adjudication. Use the same identity
when root identity remains valid; use a replacement identity only when the
mechanism/correction boundary is materially different. Never erase the prior
resolution claim.

## 13. Severity Evolution

Severity is an adjudicated field of an accepted owner revision, not identity.
`HIGH → MEDIUM` and `MEDIUM → HIGH` preserve the finding ID and emit derived
`SEVERITY_DECREASED` or `SEVERITY_INCREASED` transitions. They do not emit
`RESOLVED + NEW` and do not change lifecycle unless separate evidence does so.

Every severity revision keeps its prior severity, evidence, rationale, and
baseline binding. Current severity distribution counts only included current
findings at the selected accepted baseline.

## 14. Current Findings View

`Current Findings` is a deterministic derived view over one accepted owner
authority snapshot:

```text
finding_id, owner, accepted_revision, lifecycle, disposition, severity,
source/baseline_binding, freshness, evidence_refs,
resolution_ref, supersession_ref, reopen_ref
```

State dimensions are independent:

| Dimension | Values | Owner/meaning |
|---|---|---|
| Finding lifecycle | `ACTIVE | RESOLVED | SUPERSEDED` | Finding owner; technical applicability/history. |
| Disposition | owner-qualified `ACTION_REQUIRED`, accepted-risk/exception, deferred, or declined-remediation treatment | Finding owner/governance; treatment decision, never resolution. |
| Finding freshness | `CURRENT | STALE | BLOCKED` | Existing owner/revalidation semantics; strength of current evidence. |
| Remediation/execution | owner-specific action/availability state (for example `BLOCKED`) | Work status; does not mutate lifecycle. |

`BLOCKED` in remediation/execution is not a lifecycle value. A finding stays
`ACTIVE`, remains in technical Current Findings, and is reported as
blocked-remediation when its remediation is blocked. It is not `RESOLVED` and
is not accepted risk unless a separate owner disposition says so. A finding
with freshness `BLOCKED` is likewise never silently omitted: it is included in
the technical-risk/uncertainty presentation with its limitation, while the
verified-current subset excludes it.

Inclusion rule:

| State | Current Findings | Separate reporting |
|---|---:|---|
| `ACTIVE + CURRENT` | included | actionable or accepted-risk by disposition |
| `ACTIVE + STALE` | included with freshness limitation | revalidation required |
| `ACTIVE + BLOCKED` freshness | included in technical Current Findings and current-risk stock with freshness limitation | not in `VERIFIED_CURRENT`; revalidation required |
| `RESOLVED + CURRENT` | excluded | resolved transition/history |
| `RESOLVED + STALE` after source/dependency advancement | excluded from verified current absence, but included in `RESOLUTION_REVALIDATION_REQUIRED` uncertainty/limitation set | historical resolution for its old binding; owner revalidation required |
| `SUPERSEDED` | excluded | superseded history and replacement link |
| `LEGACY_STATUS_UNKNOWN` | excluded from definitive lifecycle counts and verified current findings | mandatory migration/owner-adjudication limitation |
| unavailable owner/member | no invented finding rows or zero count | availability limitation; Product policy decides whether baseline acceptance blocks |

An `ACTIVE` accepted-risk finding is included in technical current risk and
separately reported as accepted residual risk. It is not included in
“actionable/open requiring remediation.” A stale/blocked item is not
reclassified as resolved merely because current evidence is incomplete. A
stale resolved item is not treated as active without new evidence, but its
uncertainty is mandatory in the current-risk presentation.

“Current HIGH findings” therefore means: active, materially applicable,
accepted findings in the selected owner/baseline scope whose current accepted
revision has severity `HIGH`, with accepted-risk and freshness qualifiers
shown separately.

## 15. Historical Findings View

The Historical Finding Registry is the union of all owner-accepted finding
identities and their immutable revisions that are in scope, including active,
resolved, superseded, reopened, and legacy/unknown records. It is not a second
authority and need not be materialized: it is a derived view over owner ledgers.

Required counters are separately labeled:

- `REGISTERED_RF`: identities ever accepted in the selected scope;
- `RESOLVED_RF_HISTORICALLY`: identities with at least one accepted resolved
  revision, regardless of current status;
- `SUPERSEDED_RF_HISTORICALLY`: identities accepted as superseded;
- `CURRENT_RF`: identities included by §14 at the selected baseline;
- `ACCEPTED_RISK_RF`: current active identities with accepted-risk disposition.

These counters are not assumed to partition arithmetically. An identity can
be resolved and later reopened, or superseded after an earlier active period.
Historical count may rise while current count falls.

## 16. Progress / Delta Model

Progress compares two exact accepted baselines for the same qualified scope,
owner/member vector, and compatible Product context. It joins findings by
qualified identity first, then compares accepted revisions and fields.

Derived transition labels are:

```text
NEW, RESOLVED, REOPENED, SUPERSEDED,
SEVERITY_INCREASED, SEVERITY_DECREASED, UNCHANGED,
ACCEPTED_RISK_ADDED, ACCEPTED_RISK_REMOVED
```

They are normally derived, not persisted events. Persist only the owner
revision/disposition and baseline references already needed for authority and
provenance. A transition is emitted once per identity per baseline pair;
severity and disposition classifications attach to the same identity and do
not create extra new/resolved rows.

Accounting types:

| Metric | Type | Meaning |
|---|---|---|
| `CURRENT_RF`, current severity buckets | stock | state at one accepted baseline |
| `NEW`, `RESOLVED`, `REOPENED`, `SUPERSEDED` | flow | identity/lifecycle movement between baselines |
| severity increase/decrease, accepted-risk added/removed | classification flow | field/disposition change on an identity |
| registered historically, resolved historically | cumulative stock/history | provenance across all accepted history |

For the simple lifecycle subset:

```text
CURRENT(N+1) = CURRENT(N) + NEW + REOPENED - RESOLVED - SUPERSEDED
```

This equation applies only when the pair has complete comparable scope and
does not count replacements as resolved. With incomplete/unknown members it is
reported as not reconciled, not forced. Severity movement and disposition
movement never alter that equation unless a separate lifecycle transition is
also present.

## 17. Accounting Invariants

1. A historical identity is never deleted to reduce a current count.
2. Every current row has exactly one qualified owner, accepted revision, and
   selected baseline binding.
3. A current-risk row is an owner-accepted active finding, including stale or
   blocked freshness, or an explicit `RESOLUTION_REVALIDATION_REQUIRED`
   uncertainty row for a resolved finding whose proof binding advanced. Neither
   absence of evidence nor blocked remediation is resolved or accepted risk.
4. Resolved and superseded are mutually distinct meanings; superseded is not
   a resolved flow.
5. Accepted risk is never counted as resolved.
6. A reopened identity can count in historical resolved statistics and current
   active risk simultaneously, because those are different questions.
7. Current severity buckets sum to current included active identities, with
   blocked or unavailable limitations disclosed according to scope policy;
   stale resolved uncertainty is not silently placed in a severity bucket as
   active.
8. Progress flows are computed from a frozen baseline pair and each identity
   receives at most one lifecycle transition classification per pair.
9. Product totals are sums of qualified child Current Findings views plus any
   independently adjudicated Product-scoped finding, never sums of raw IDs.
10. Registered history is not defined as `current + resolved + superseded`.

## 18. Single-Project Reporting

A single Project can report without Product state:

```text
CURRENT STATE
Current findings: N
Verified current findings: N
Severity distribution: Critical / High / Medium / Low / Informational
Actionable: N; accepted residual risk: N; stale-resolution uncertainty: N
Blocked-remediation: N; freshness/availability limitations: N

PROGRESS SINCE PREVIOUS ACCEPTED BASELINE
New / Resolved / Reopened / Superseded
Severity increased / decreased
Accepted-risk added / removed

HISTORICAL
Registered identities / resolved historically / superseded historically
```

The report names the owner capability and accepted baseline. A missing prior
baseline yields `NO_COMPARABLE_BASELINE`, not an invented zero.

## 19. Product Aggregation

Product consumes each qualified child’s accepted Current Findings view, not
its raw ledger and not its Markdown projection. Each row retains member/
Project, owner capability, local finding ID, accepted owner revision, source
binding, baseline, freshness, and limitations. Local equal IDs remain separate.

Product reports current technical risk, verified-current findings, actionable/
open subset, accepted residual risk, stale-resolution uncertainty, and
unavailable/blocked member limitations separately. It may
also show independently adjudicated Product-scoped `RF-*` records, which
remain Architecture-owned. Product cannot alter child lifecycle, disposition,
severity, or resolution.

For progress, Product compares qualified child views at Product baseline N and
N+1 and reports per-member deltas plus a cross-project roll-up. A member that
is unavailable or not comparable is excluded from a falsely precise total and
listed as a limitation; requiredness/coherency policy decides whether Product
acceptance blocks. Absence of that member is never `UNCHANGED`, zero findings,
or zero transitions.

## 20. Product Baseline Binding

The minimum sufficient binding is the existing immutable Product baseline
vector plus, for every consumed finding view:

```text
Product baseline key and Product revision
member/project qualification
owner capability and local finding identity
accepted owner revision
exact source/baseline binding
view contract/version and resolved selector snapshot
freshness and availability/limitations
```

No new Product finding revision or duplicated child finding ledger is needed.
The baseline stores a deterministic `current_findings_view_fingerprint` over
the qualified Current Findings snapshot used for that baseline, not over the
historical registry. The fingerprint is derived and cannot replace the owner
revision references. Historical ledger revisions remain separately addressable
through those owner references.

The fingerprint contract is versioned as `CFV-1` and has this canonical payload:

```text
schema: CFV-1
product_revision
product_baseline_key
rows: [
  member_key, project_key, owner_capability, finding_family, finding_id,
  accepted_owner_revision, lifecycle, owner_qualified_disposition,
  severity, freshness, exact_source_or_content_binding,
  semantic_limitation_marker
]
```

The payload is serialized as UTF-8 canonical JSON with fixed field order shown
above, no insignificant whitespace, explicit `null` for an absent optional
field, and normalized string encoding. `rows` are sorted lexicographically by
`member_key`, `project_key`, `owner_capability`, `finding_family`, `finding_id`,
and `accepted_owner_revision`; ties are impossible after full qualification.
Only limitations that change the meaning or qualification of the view are
included. Timestamps, filesystem/workspace paths, Markdown text, rendering
order, and other volatile presentation metadata are excluded. A change to
severity, lifecycle, disposition, freshness classification, semantic source
binding, or an interpretation-changing limitation changes the fingerprint;
Markdown wording/order or workspace path changes do not. A future payload
change uses a new schema identifier and cannot silently compare as `CFV-1`.

This is the minimum needed to reproduce PB-N vs PB-N+1, prevent cross-member ID
collisions, and detect semantic-authority advancement on unchanged source.

## 21. Bottom-Up Child Advancement

If a child independently accepts `RF-017 RESOLVED` while Product PB-10 still
pins the prior active child revision, the Product baseline remains PB-10 and
continues to show the old accepted state. The newer child revision is
`SEMANTIC_AUTHORITY_ADVANCEMENT` for the Product dependency, not automatic
Product current state.

Product routes through existing `REVALIDATE` over the pinned baseline and a
candidate replacement vector, or through complete-vector `CHANGE_REVIEW` and
explicit reconciliation. Only Product Baseline Acceptance can accept PB-11.
If source commit is unchanged, source advancement is `NONE` while semantic
authority advancement is `PRESENT`; these axes remain separate.

## 22. Change Review Interaction

`CHANGE_REVIEW` may report `POTENTIALLY_RESOLVES` for `RF-017`, with exact base
and candidate bindings and candidate evidence. It cannot change Current
Findings, write `RESOLVED`, mark a projection current, or update Product
baseline. Current Findings still includes the accepted active RF until the
owning Architecture authority verifies the accepted candidate through the
existing reconciliation/owner gate. Candidate progress is never accepted
progress.

## 23. Projection Freshness / Regeneration

When an accepted owner revision changes, dependent `PRJ-*` reports become
`STALE` under existing Projection Impact rules. A stale Markdown report may
still display the old active row; that is projection staleness, not semantic
authority. Explicit `RG-*` regeneration and V1–V4 verification update the
projection. Regeneration cannot resolve, supersede, reopen, or otherwise edit
the finding authority, and `REGENERATED != CURRENT` until verification passes.

## 24. Legacy Migration

Migration is a compatible extension, not a rewrite of all history:

1. Register each old finding under its existing owner and stable ID where
   identity can be established.
2. Preserve original text, evidence, source/baseline, and report provenance.
3. Apply this evidence hierarchy:
   - **Tier 1 — mechanical:** explicit accepted owner lifecycle/status record
     with stable identity and owner binding.
   - **Tier 2 — mechanical when complete:** accepted resolution or supersession
     record with exact finding identity, owner, and accepted source binding.
   - **Tier 3 — owner adjudication required:** accepted remediation verification
     explicitly tied to the finding, but lacking an accepted lifecycle record;
     it is evidence for adjudication, not an automatic lifecycle mutation.
   - **Tier 4 — insufficient:** projection/report text alone, including “fixed”.
   - **Tier 5 — insufficient:** commit messages, code absence, timestamps, or
     inference without accepted owner evidence.
4. Reconstruct lifecycle mechanically only from Tier 1 or complete Tier 2;
   route Tier 3 to the Architecture or Code Quality owner for adjudication.
5. If no lifecycle evidence exists, derive `LEGACY_STATUS_UNKNOWN` as a
   migration condition; do not silently default to ACTIVE forever or RESOLVED.
6. Keep unknown records out of definitive lifecycle and severity counts and out
   of `VERIFIED_CURRENT`; report them in a mandatory migration-uncertainty set
   that prevents a verified-zero/currently-resolved claim. They remain
   historical context until owner adjudication creates an accepted revision.
7. Do not infer accepted risk from “won’t fix” prose unless the owning contract
   supplies decision, rationale, scope, and approver provenance.
8. Create/verify any affected projection registration using the existing
   legacy `PRJ-*` path; mark old projections non-current until V1–V4 pass.
9. Requalify Product baselines whose consumed child lifecycle/revision binding
   cannot be proven; preserve the old baseline and record the limitation.

Manual adjudication is required for ambiguous identity, conflicting owner
records, inferred resolution, or unclear accepted-risk decisions. No legacy
record is deleted or upgraded by report text alone. Legacy migration is
additive: old packages are not rewritten, but affected projections become
stale/non-current and Product acceptance cannot treat an unknown child as
verified resolved or as zero findings.

## 25. Pressure Scenarios

| ID | Scenario | Expected result |
|---|---|---|
| FL-01 | ACTIVE → RESOLVED | Owner evidence and adjudication create resolved revision; current exclusion follows. |
| FL-02 | RESOLVED remains historical | Identity/revisions/evidence remain addressable. |
| FL-03 | RESOLVED excluded from Current Findings | Excluded from current stock, counted in historical/progress views. |
| FL-04 | ACTIVE → SUPERSEDED | Replacement link and new authority required. |
| FL-05 | SUPERSEDED not resolved technical debt | Superseded flow is separate; no resolved credit. |
| FL-06 | Accepted risk still exists | Owner-approved disposition keeps the active finding current; treatment is separate from resolution. |
| FL-07 | RESOLVED → recurrence | Same identity active revision; derived REOPENED. |
| FL-08 | HIGH → MEDIUM | Same identity; severity decreased, no closure. |
| FL-09 | MEDIUM → HIGH | Same identity; severity increased, no new finding. |
| FL-10 | New finding between baselines | NEW flow and current inclusion at N+1. |
| FL-11 | Resolved finding between baselines | RESOLVED flow and historical retention. |
| FL-12 | Child resolves; Product baseline old | No automatic Product advance; semantic authority advancement detected. |
| FL-13 | Same source, newer accepted Architecture revision closes | Product detects semantic-authority advancement without source advancement and requalifies through the owner/Product gates. |
| FL-14 | Candidate Change Review potentially resolves | Candidate-only effect; current finding remains active. |
| FL-15 | Reconciliation accepts resolution | Owner accepts resolved revision; Product may later qualify it. |
| FL-16 | Stale projection shows old active row | Semantic authority remains correct; projection is STALE. |
| FL-17 | Regeneration updates current view | Explicit RG/V1–V4; no authority mutation. |
| FL-18 | Duplicate findings collapse | Old identity SUPERSEDED; not resolved; current replacement counted once. |
| FL-19 | REGISTERED grows while CURRENT falls | Valid; historical and current stocks are separate. |
| FL-20 | Accepted-risk shown separately | Current count is unchanged; accepted-risk-added changes classification and lowers actionable count only. |
| FL-21 | Legacy finding lacks lifecycle | Tiered evidence rules determine mechanical migration; otherwise `LEGACY_STATUS_UNKNOWN` is a mandatory uncertainty limitation. |
| FL-22 | Product member unavailable | No zero/unchanged claim; member limitation is visible and requiredness policy may block acceptance. |
| FL-23 | Child authority changes, source unchanged | Semantic advancement without source advancement. |
| FL-24 | PB-N vs PB-N+1 reproducibility | Exact qualified vector, owner revisions, and `CFV-1` canonical payload reproduce both snapshots. |
| FL-25 | Similar IDs across Projects | Member/owner qualification keeps them distinct. |
| FL-26 | Current severity table | Counts only included current findings. |
| FL-27 | Historical table | Includes historical resolved/superseded identities with labels. |
| FL-28 | Reopen and historical resolved statistics | Historical resolved-at-least-once remains true; current active is separate. |
| FL-29 | Count/transition reconciliation | Complete comparable pair satisfies the equation; stale-resolution uncertainty and incomplete members are explicit non-reconciled limitations. |
| FL-30 | Incomplete evidence | Cannot produce RESOLVED; remains stale/blocked active or unknown. |

All 30 scenarios are covered by this remediated model.

### Additional safety scenarios

| ID | Scenario | Deterministic expected behavior |
|---|---|---|
| FL-S1 | `RF-001` resolved for source B; source advances to C without RF revalidation | Historical resolution remains bound to B; C exposes `RESOLUTION_REVALIDATION_REQUIRED`, does not claim verified absence, and does not invent ACTIVE. Owner revalidation is required; Product preserves the limitation. |
| FL-S2 | `RF-002` active/high at B; source advances to C without revalidation | The active finding remains visible in technical current risk with `STALE`/revalidation-required qualification; it is not silently removed and is not asserted definitely applicable to C without evidence. |
| FL-S3 | `RF-003` ACTION_REQUIRED at PB-1; owner-approved ACCEPTED_RISK at PB-2 | Current count is unchanged; NEW/RESOLVED are zero; `ACCEPTED_RISK_ADDED=1`; actionable count decreases by one; residual accepted risk increases by one; Product only derives the comparison. |
| FL-S4 | `RF-004 ACTIVE/HIGH` with `remediation_status=BLOCKED` | Lifecycle remains ACTIVE; Current Findings includes it; it is not resolved or accepted risk; actionable work is blocked; Product shows the technical risk and blocked-remediation limitation. |
| FL-S5 | Legacy RF has stable ID/evidence and report text saying “fixed”, but no accepted owner resolution | No automatic RESOLVED migration; classify `LEGACY_STATUS_UNKNOWN`; expose uncertainty in historical/current qualification; Product cannot claim verified resolution. |
| FL-S6 | Same qualified source/owner revision with Markdown reorder/path move, then severity/lifecycle change | Same `CFV-1` fingerprint for wording/order/path-only changes; different fingerprint for HIGH→MEDIUM or ACTIVE→RESOLVED because semantic payload fields changed. |

## 26. Validation Strategy

Use one bounded Markdown contract artifact following existing test conventions,
for example a future `tests/finding-lifecycle-progress-reporting-validation.md`;
do not build a generic test framework. The artifact should fail first against
the current gap and then assert:

- owner authority and no Product lifecycle writes;
- stable identity, revision, source binding, and history retention;
- Current vs Historical separation and exact inclusion/exclusion;
- resolution evidence, supersession distinction, accepted-risk treatment;
- reopen and invalidated-resolution provenance;
- severity migration without false new/resolved counts;
- single-Project stock/flow reports and arithmetic;
- Product qualification, member isolation, unavailable-member limitations, and
  baseline N/N+1 reproducibility;
- stale resolution after source advancement, stale active risk, blocked
  remediation, and legacy “fixed” prose;
- accepted-risk treatment changes without lifecycle/count changes;
- `CFV-1` fingerprint invariance under Markdown/path-only changes and change
  under semantic severity/lifecycle changes;
- bottom-up child advancement and unchanged-source semantic advancement;
- Change Review non-authority;
- stale projection vs explicit regeneration;
- conservative legacy handling and required manual adjudication.

Validation must inspect actual owner records and projection/index freshness
before diagnosing historical/current discrepancies such as 29 vs 17 or 36 vs
20. A mismatch caused solely by stale INDEX/projection data is a projection or
coordination defect, not evidence that the finding lifecycle is wrong.

## 27. Backward Compatibility

Existing audits retain their IDs, accepted revisions, baselines, reports,
Product qualification, and single-project operation. Existing `CQ-*` lifecycle
and disposition semantics are reused without flattening `WONT_FIX` into
accepted risk. The existing Architecture RF ledger contract identified in § 6
is extended compatibly by explicit owner adjudication; no report silently
changes an old RF to resolved or accepted risk.

Product baselines that lack qualified owner revision/view bindings are not
retroactively rewritten. They remain historical and can be used as exact
historical inputs only where existing policy permits; otherwise they require
bounded migration/requalification. Legacy projections follow the existing
projection registration and freshness gates. A source advance invalidates the
verified-absence claim of a resolved finding until owner revalidation, while
preserving the old resolved fact historically.

## 28. YAGNI Boundaries

The design adds no event store, event type registry, counter database, generic
analytics layer, service, daemon, scheduler, integration, new capability,
intent, or Product authority. Transition labels are derived joins between two
accepted snapshots. Only owner revisions, dispositions, provenance, and
existing Product baseline references are persisted.

## 29. Files Likely Affected by Future Implementation

Prospective only; none are modified in this run:

- `references/artifacts.md` / `docs/reference/artifacts.md` — cross-family
  finding lifecycle and field vocabulary;
- `references/report-contract.md` — ledger/current/progress output contract;
- `references/evidence-and-severity.md` — shared resolution verification
  wording, if generalized;
- `references/revalidation-and-freshness.md` — accepted finding revision and
  semantic-authority advancement interaction;
- `references/review-modes-and-orchestration.md` — candidate/reconciliation
  boundary references;
- `references/product-multi-project-review.md` — qualified child Current
  Findings consumption and Product progress;
- `capabilities/code-quality-review/references/code-quality-lifecycle.md` —
  only if compatibility wording needs alignment;
- the Architecture Review contract/ledger reference where the RF lifecycle is
  currently absent;
- a bounded future validation Markdown artifact under `tests/`;
- selected output/projection references if current/progress sections are added.

No listed file was changed in this discovery/design run.

## 30. Open Questions

`NONE BLOCKING IMPLEMENTATION PLANNING`

The semantic choices raised by the independent review are resolved in §§ 6,
9, 14, 20, and 24. Non-blocking future work may choose a concrete hash
algorithm for the already versioned `CFV-1` canonical payload and may refine
human-facing labels, but neither choice changes authority, lifecycle,
freshness, migration, or accounting semantics.

## Independent Design Review Remediation

This appendix addresses the findings from
`/tmp/finding-lifecycle-progress-reporting-design-review.md` without claiming
independent re-review closure:

| Review Finding | Severity | Remediation | Design Section | Status |
|---|---:|---|---|---|
| F-001 | HIGH | Bind resolution to exact proving snapshot; source/dependency advancement creates revalidation-required uncertainty and cannot remain verified-resolved on the new state. | §§ 10, 14, 17, 21, FL-S1/S2 | `REMEDIATED_IN_DESIGN` |
| F-002 | MEDIUM | Identify `references/report-contract.md` § 4 and its Architecture-owned `02-authoritative-findings-ledger.md` as the RF contract boundary; preserve existing RF lifecycle vocabulary and owner gates. | § 6 | `REMEDIATED_IN_DESIGN` |
| F-003 | MEDIUM | Keep dispositions owner-qualified; map CQ `ACCEPTED_EXCEPTION` exactly, keep CQ `WONT_FIX` distinct, require Architecture owner adoption for RF accepted risk, and forbid Product governance. | § 9, FL-S3 | `REMEDIATED_IN_DESIGN` |
| F-004 | MEDIUM | Separate lifecycle, disposition, freshness, and remediation status; include active blocked findings in technical current risk and exclude them only from verified-current claims. | § 14, § 17, FL-S4 | `REMEDIATED_IN_DESIGN` |
| F-005 | MEDIUM | Define `CFV-1` as canonical fixed-order UTF-8 JSON over the qualified Current Findings snapshot, with stable ordering and volatile-field exclusions. | § 20, FL-S6 | `REMEDIATED_IN_DESIGN` |
| F-006 | MEDIUM | Scope this common model to RF/CQ; keep TE families under their existing owner-specific lifecycles and qualified views. | § 6 “Scope of the common reporting model” | `REMEDIATED_IN_DESIGN` |

The independent review must rerun the pressure matrix and targeted conclusions
before calling these findings closed.

## 31. Design Recommendation

Adopt a single minimal owner-controlled finding lifecycle—`ACTIVE`, `RESOLVED`,
`SUPERSEDED`—with `REOPENED` as a derived baseline transition and owner-
qualified accepted risk as an orthogonal disposition. Extend the existing
Architecture RF ledger contract by reference to the shared reporting rules;
reuse, do not duplicate, existing revision, evidence, freshness, Product
qualification, and projection contracts.

Derive Current Findings, Historical Findings, and baseline deltas from exact
accepted owner revisions and Product-qualified snapshots. Count active risk
including stale/blocked active findings, expose stale resolved uncertainty
without asserting it active or resolved on the newer source, retain accepted
risk visibly, exclude verified resolved/superseded records from current stock,
and report historical and flow metrics under explicit labels. Require owner
verification and reconciliation for resolution, preserve Product’s
composition-only role, and handle legacy unknowns conservatively. The next
step is targeted independent design re-review; no implementation is authorized
by this document.
