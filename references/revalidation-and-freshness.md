# Revalidation and compact-state freshness

This file is the authoritative contract for three cross-cutting cases confirmed by pressure validation:

1. projection-only correction must not automatically restart a technical audit;
2. compact persisted state cannot be used downstream when it is stale relative to its owning accepted authority;
3. the dedicated `PROJECTION_REPAIR` intent repairs only user-facing projections of an accepted audit and stops when semantic drift is detected.

Stage B projection identity, verified revisions, fingerprints, freshness states, and required actions are owned by [Projection lifecycle authority](projection-lifecycle.md). This file owns cross-cutting revalidation routing and preserves the following distinction:

```text
semantic freshness != projection freshness
semantic workflow may finish with stale projections
projection stale != semantic false
```

For project-change `REVALIDATE`, the semantic closeout and baseline-advancement ordering in
[REVALIDATE closeout hardening](revalidate-closeout-hardening.md) is mandatory.
The overlay is proposed delta until owner gates accept it; projection impact and
regeneration cannot be used to accept semantic changes or advance the baseline.

Do not use this contract to redefine ordinary scope discipline, fresh-context review, or As-Built coverage; those behaviors are already governed by their existing reference contracts.

## 1. Projection-only revalidation

Use `PROJECTION_REVALIDATION` when a correction changes only the representation of already accepted technical semantics.

Typical cases include:

- rewriting shorthand into coherent user-facing prose;
- splitting an overloaded paragraph;
- correcting heading or table presentation;
- correcting a relative link;
- correcting Mermaid syntax or renderability without changing the mechanism shown;
- clarifying wording of an already accepted target or roadmap mechanism without changing owner, invariant, dependency, or activation behavior.

For such correction and re-review, the minimum input is:

```text
issue id
artifact + changed section
before/after or enough surrounding context
current accepted technical authority refs
immutable accepted semantics relevant to the changed section
```

Fresh context means independent judgment, not a mandatory full reread. Under `PROJECTION_REVALIDATION`, the reviewer checks the changed range, enough surrounding context, and current accepted authority references by default.

Do not reopen the source repository or rerun As-Built verification, candidate verification, root adjudication, severity adjudication, or Target technical review merely because the correction/re-review uses fresh context.

If projection review discovers a real contradiction that cannot be resolved without changing accepted technical semantics, return:

```text
TECHNICAL_REVALIDATION_REQUIRED
```

## 1.1 `PROJECTION_REPAIR` session flow

`PROJECTION_REPAIR` is an orchestration intent for re-entering an already accepted audit package when the user wants to repair only the quality of final or user-facing documents.

It uses `PROJECTION_REVALIDATION` as its validation mechanism, but differs from the ordinary editorial correction loop because it is a distinct startup intent and may be selected later, after `COMPLETE`.

Preconditions:

```text
accepted audit package exists
accepted technical authority is reusable and revision-bound
selected project baseline has no unresolved source change requiring REVALIDATE
requested work is presentation/projection-only
```

Minimum flow:

```text
PROJECTION_REPAIR
→ identify requested/broken final projections
→ bind each projection to current accepted authority refs
→ build projection issue list
→ repair only allowed presentation surface
→ validate links/Markdown/terminology/Mermaid/reference consistency
→ PROJECTION_REVALIDATION per changed projection
→ PROJECTION_REPAIR_COMPLETE | TECHNICAL_REVALIDATION_REQUIRED
```

Before asking for a repair target, resolve the selected accepted package's existing Stage B registration and show a view over its eligible registered projections:

```text
PROJECTION_REPAIR
├── Package
│   └── accepted revision-bound package
├── Eligible registered projections
│   ├── PRJ-* identity
│   ├── human-readable name
│   ├── declared artifact path
│   └── current revision/freshness when useful
└── Repair target
    ├── entire selected projection
    └── specific section / presentation issue
```

The list is derived from the selected package and existing projection registration/lifecycle records; it is not a hardcoded universal list or a new registry. Only presentation concerns such as language, wording, Markdown, Mermaid, links, navigation, cross-references, terminology, formatting, and representation of accepted meaning are eligible. `RF-*`, `CQ-*`, `CQRA-*`, `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, STM facts, severity, owners, evidence, security assumptions, target mechanisms, and lifecycle semantics may appear as provenance but are never editable repair targets.

Allowed scope includes:

- language, grammar, and readability;
- heading and section structure;
- Markdown tables, lists, and navigation;
- relative links and cross-links;
- orphaned or malformed references to existing RF/SER/TASK/target identifiers;
- duplicate and stale presentation when current accepted authority unambiguously identifies the replacement;
- Mermaid syntax, renderability, and layout without changing the accepted mechanism shown;
- terminology and naming consistency across final documents;
- rebuilding summaries, indexes, and navigation as projections of accepted authority.

The following are not allowed without returning to the technical gate:

- changing evidence;
- changing root identity or correction boundary;
- changing severity or exploitability;
- changing owner or lifecycle/target invariant;
- changing product-intent status;
- changing finding disposition;
- adding a new finding, root, or target mechanism;
- changing a roadmap prerequisite, dependency, or gate;
- changing a security assumption or safe-activation semantics;
- hiding source or baseline changes that require `REVALIDATE`.

For every changed artifact or section, record:

```text
artifact
changed_section_or_range
projection_issue_ids
accepted_authority_refs
validation_checks
projection_revalidation_result
```

Projection-level verification is selected according to the change and includes the applicable checks:

- relative links resolve;
- Markdown structure is coherent;
- identifiers and references exist and point to current accepted authority;
- no stale or superseded presentation survives;
- terminology and language are consistent;
- Mermaid blocks parse/render when compatible tooling is available;
- final status and summary wording remain consistent with accepted technical gates.

If no compatible Mermaid validator or renderer is available, persist `MERMAID_RENDER_VALIDATION_UNAVAILABLE`; do not claim render validation passed.

A successful projection repair returns:

```text
PROJECTION_REPAIR_COMPLETE
technical_semantics_changed: false
technical_gates_reopened: false
```

This does not mean fresh technical verification. The Project baseline does not change merely because review documents were repaired.

## 2. Semantic drift gate

A projection-only writer may not change:

- evidence;
- root identity or correction boundary;
- severity or exploitability;
- owner;
- lifecycle or target invariant;
- roadmap prerequisite, dependency, or gate;
- security assumption;
- safe-activation semantics.

If changed prose, a table, or a diagram diverges from accepted technical semantics, re-review returns:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

Do not modify technical authority or compact state merely to make them silently match new prose. Route the change back to the owning technical gate.

## 3. Compact persisted state is a projection, not authority

`INDEX.md`, `HANDOFF SUMMARY`, native plan UI, and any compact semantic or fingerprint records help route and resume the workflow, but they do not replace accepted owning technical artifacts.

If a compact record is used downstream as a semantic shortcut, it must contain at least:

```text
owning_artifact
owning_artifact_revision
owning_authority_status
projection_status: VALID | REVALIDATION_REQUIRED | SUPERSEDED
```

A `VALID` compact projection is usable downstream only when all of the following hold:

```text
owning_authority_status == COMPLETE
owning_artifact_revision == current accepted owning artifact revision
projection_status == VALID
```

If the owning artifact is corrected or revalidated, or its accepted revision changes, the previous compact projection cannot remain `VALID`.

Transition:

```text
VALID
→ REVALIDATION_REQUIRED
→ VALID(new revision) | SUPERSEDED
```

## 4. Downstream freshness gate

Before a dispatch relies on compact semantic state instead of reading the owning authority, the coordinator or reviewer verifies revision and status binding.

On mismatch, unknown revision, or conflict between `INDEX.md`, a handoff, or another compact record and the accepted owning artifact, return:

```text
AUTHORITY_RECONCILIATION_REQUIRED
```

Downstream dispatch using stale semantics is prohibited until reconciliation completes.

Reconciliation must restore the minimum current authority, update or invalidate compact state, and only then continue the workflow.

Do not create `VALID` compact semantic state from owning authority in any of these states:

```text
REVIEW_REQUIRED
CORRECTION_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
```

## 4.1 Context Orchestration v0.3

Canonical principle:

```text
Load the minimum fresh authoritative evidence needed for the current decision.
```

Optimization is subordinate to correctness and freshness; a shorter or newer projection is never substantive authority merely because it is compact.

Routing context decides where to look and may contain `INDEX`, handoffs, registries, candidate/evidence pointers, materiality/coverage projections, and revision bindings. Decision evidence supports a substantive claim and includes owning code/configuration, the accepted owning artifact, exact authority/contract evidence, and targeted runtime/test evidence. Routing context is not proof when owning evidence is required.

Progressive retrieval is:

```text
structure/inventory
→ materiality map
→ evidence pointers
→ targeted reads
→ deeper reads only for unresolved material questions
```

Do not blanket-preload all references, working artifacts, or repository contents. If a bounded review discovers a material omitted cross-boundary path, record `CONTEXT_EXPANSION_REQUIRED`, inspect that path, and preserve the reason and exact evidence pointer.

Dependency-sliced capability/subagent dispatch records:

```text
exact baseline/revision
exact mission/scope
forbidden scope
accepted dependency artifact pointers + revisions
required shared/reference contracts
output path
HANDOFF SUMMARY contract
```

Unrelated accepted artifacts are excluded by default. Expansion requires a concrete correctness trigger and is persisted in the handoff.

## 5. Resume

On resume, compact routing state is first checked for freshness relative to its referenced owning authority. The fact that a record appears in a newer file, `INDEX.md`, or handoff does not make it fresh.

If freshness cannot be established without reading the owning artifact, read only the required authority and perform reconciliation. Do not rerun the entire accepted audit.

## 6. Pressure-regression mapping

This contract exists for confirmed baseline gaps:

- PS-41 → `PROJECTION_REVALIDATION` prevents a source or technical-gate restart for presentation-only correction;
- PS-42B → revision/status binding blocks a stale compact projection before downstream dispatch;
- PS-80 → `PROJECTION_REPAIR` makes projection-only repair a first-class startup intent while preserving the semantic-drift gate;
- REVALIDATE-CLOSEOUT-01 → the real invalid closeout captured in `revalidate-closeout-hardening.md` requires proposed-delta owner acceptance, coherent baseline roles, registered projection targets, and V1-V4 before `CURRENT`.

PS-39, PS-40, and PS-43 were baseline-compliant and are not grounds for adding new orchestration restrictions.

## 7. Project-change targeted revalidation

`REVALIDATE` is accepted-state reevaluation, not Change Review reuse. The coordinator binds the previously accepted baseline A and the selected current source B, shows both exact bindings, and routes only the affected accepted authority slices through the existing revalidation and owner-adjudication gates. A complete `CR-*` is routing evidence about B: it cannot satisfy the `REVALIDATE` gate, substitute for fresh required evidence, or bypass the owning authority's adjudication. Candidate `CF-*`/`CRF-*` records likewise remain non-authoritative until their existing owners decide.

During this flow persist distinct baseline roles:

```text
accepted_baseline   # currently accepted semantic baseline
candidate_baseline  # exact source baseline under REVALIDATE/adjudication
source_head         # observed current source revision
```

The candidate may equal the observed source head while still differing from the accepted baseline. `accepted_baseline` MUST NOT move merely because the overlay is complete, impact is accounted, or a coordinator field was rewritten.

The bounded REVALIDATE overlay is explicitly:

```text
PROPOSED_REVALIDATION_DELTA
```

until every affected owner gate has adjudicated its slice. The overlay may route and preserve evidence but cannot itself create accepted STM/RF/CQ/TE/Target/Roadmap semantics, satisfy downstream authority, or advance the accepted baseline.

Every material delta item must be reconciled as one of:

```text
ACCEPTED_OWNER_CHANGE
ACCEPTED_PRESERVED
EVIDENCED_NON_MATERIAL
POLICY_PERMITTED_UNRESOLVED
BLOCKING_UNRESOLVED
```

`POLICY_PERMITTED_UNRESOLVED` requires an explicit applicable policy reference for that item or bounded class. A generic statement that open findings are allowed is not policy evidence.

Only after owner adjudication is complete and required Technical Model / coverage gates are accepted against the exact candidate baseline may the coordinator evaluate:

```text
BASELINE_ADVANCE_ALLOWED
```

The gate requires:

```text
exact candidate source binding remains current for the decision
all material delta is reconciled
all required owner adjudications are accepted
required Technical Model gates are accepted at candidate_baseline
required coverage gates are accepted at candidate_baseline
all remaining unresolved/unknown items are explicitly policy-permitted
```

Acceptance bound only to the previous baseline cannot satisfy this gate. If any condition fails, the accepted baseline remains unchanged and downstream work carries the blocker explicitly.

After the semantic delta reaches a stabilized accepted state and baseline advancement is accepted where applicable, projection freshness is accounted for by [Projection impact accounting](projection-impact.md). That pass consumes revision-bound semantic identities, selector resolution snapshots, and contract revisions; changed paths remain routing context rather than semantic proof. It persists direct impact and reverse-graph propagation before any separately requested regeneration. A successful pass returns `PROJECTION_IMPACT_ACCOUNTED`, which means impact is recorded, not that all projections are `CURRENT`. If accounting fails technically, accepted semantic authority is not rolled back, but projection-sensitive gates remain blocked until the impact record is durably reconciled.

This is one explicit post-semantic handoff per stabilized delta for `REVALIDATE`. The equivalent handoff is used at the end of `NEW` and `EXTEND` after their semantic work has stabilized. A retry after technical accounting failure is reconciliation under the idempotent impact rules, not implicit regeneration. No intent may turn Projection Impact Analysis into a content writer or start an `RG-*` session without a separate explicit output/package freshness request.

Before any such `RG-*` request proceeds, the mandatory preflight in [Projection regeneration workflow](projection-regeneration.md) applies. Semantic authority, unregistered files, and path-derived targets fail with `REGENERATION_TARGET_NOT_PROJECTION`; `ALL_STALE` resolves only active registered `PRJ-*` identities with persisted `STALE` projection freshness.

### 7.1 Operation-inventory delta routing

When `REVALIDATE` affects a detailed Provided/Consumed operation inventory, restore and preserve the previously requested bounded operation scope: exact Project/baseline (or pinned Product member/baseline), direction, interface kind, parent `IF-*` revisions, source/evidence scope, and selected output sections. `REVALIDATE` does not add outputs, enable Architecture Review, Test Engineering, or Code Quality Review, or become a new `EXTEND` configuration flow.

Route the minimum operation delta as:

```text
changed source/baseline
→ compare the matching operation-inventory snapshot
→ targeted STM/evidence revalidation for affected IF-owned children
→ accept/revise/supersede affected operation children through the Technical Model Gate
→ update matching OPERATION_INVENTORY accounting
→ record selector membership/revision/precision impact
→ PROJECTION_IMPACT_ACCOUNTED
```

For the matching bounded inventory, an added or removed operation changes membership; a method/path or parent change creates a revised parent-qualified identity with explicit history; and a precision change (`EXACT`, `RESOURCE_BOUNDED`, or `UNRESOLVED`) changes the inventory snapshot meaning. These changes make the matching detailed projection `STALE` under its existing Stage B dependency rules after impact accounting. A child removed from the current set remains in authoritative history as the prior revision with its accepted supersession/removal disposition; its identifier is not silently reused, and a current renderer does not retain it from an old snapshot.

Auth, boundary, schema, or other operation evidence revisions affect the operation and any other downstream record only where that consumer's owning dependency metadata declares the material edge. A matching detailed projection therefore receives the changed accepted detail or explicit limitation without turning projection freshness into a semantic verdict.

For Product scope, compare qualified Project/member revisions and the pinned Product baseline before classifying membership. Identical method/path text from different member revisions does not alias the operations; divergence, missing members, or unavailable evidence remains explicitly Product-qualified and may require `CONTEXT_EXPANSION_REQUIRED`. Unaffected Project/member slices remain preserved only when their direct dependency and freshness bindings support that claim.

Operation impact accounting changes freshness state only; it does not add a requested output or start generation/regeneration. Any fresh detailed output requires a separate explicit `RG-*` request with the accepted revised inventory/snapshot as input.

`REVALIDATE` binds the previous accepted baseline to the selected current baseline and produces a bounded, delta-oriented overlay:

```text
BASELINE_BINDING
→ CHANGE_INVENTORY
→ IMPACT_ANALYSIS
→ IMPACT_CLASSIFICATION
→ MINIMUM_DEPENDENCY_SLICE
→ TARGETED_FRESH_EVIDENCE
→ REVALIDATION / ADJUDICATION
→ DELTA_RECONCILIATION
```

The user-facing `REVALIDATE` presentation is explicitly read-only for the restored suite:

```text
REVALIDATE
├── Previous Review Suite [RESTORED / READ-ONLY]
│   ├── Architecture Review state
│   ├── Test Engineering state and outputs
│   └── Code Quality Review state and outputs
├── Previous baseline
├── Current baseline / changed input
├── Change inventory
├── Impact Analysis
├── Minimum affected dependency slice
├── Targeted evidence
├── Revalidation / adjudication
└── Projection Impact Analysis
```

The restored suite is context, not a configuration menu. During ordinary `REVALIDATE`, do not enable or disable capabilities, change Architecture depth or endpoint, or select new Test Engineering or Code Quality outputs. Those changes route to `EXTEND`; `REVALIDATE_DOES_NOT_BECOME_NEW`. Changed-input classification, dependency impact, affected capabilities/records, evidence refresh, and projection impact remain automatic and impact-driven.

The user may confirm baseline/change context and any genuinely ambiguous authority decision. If impact is `SYSTEMIC`, choosing whether to accept `FULL_REAUDIT_RECOMMENDED` remains an explicit user decision; it does not turn the restored suite into a new configuration flow.

Git diff, changed paths, and Project Profile delta are routing context only. They select where fresh evidence is needed; they are not substantive proof.

For STM and dependent capability/projection artifacts, refine `IMPACT_ANALYSIS` through the dependency contract:

```text
changed source/baseline
-> affected EV/STM candidates
-> affected direct dependencies/aspects
-> impact traversal
-> only affected capability semantics/projections
```

Generated indexes locate candidate reverse edges, but owning direct dependency metadata remains authoritative. `HARD`, `CONDITIONAL`, and `INFORMATIONAL` routes, selector dependencies, and bounded context traversal are defined in `technical-model-dependencies.md`. Unknown linkage requires targeted investigation and cannot be marked preserved.

### Impact classification

`LOCAL`, `BOUNDARY`, and `SYSTEMIC` are orchestration labels, not finding severity. `LOCAL` means no demonstrated material boundary, contract, or ownership change; fresh reads stay local unless evidence expands the scope. `BOUNDARY` means a material API, auth/trust, persistence, ownership, lifecycle, concurrency, IPC, external integration, or equivalent accepted boundary is touched; revalidate that boundary and its material dependencies. `SYSTEMIC` means multiple fundamental boundaries or the accepted architecture model changed enough that targeted completion is not trustworthy.

For `SYSTEMIC`, emit:

```text
FULL_REAUDIT_RECOMMENDED
reason: <why targeted scope is insufficient>
systemic_scope: <affected fundamental boundaries>
user_decision_required: true
```

Do not start a full audit until the user chooses it. If the user declines, finish with the systemic scope and unresolved items explicit; do not claim a fully revalidated audit.

### Affected and preserved sets

Impact analysis records affected architecture domains, accepted findings, candidate/evidence bindings, capabilities, and dependent artifacts, along with preserved accepted domains. An accepted domain is `preserved` only when the available dependency/evidence mapping finds no dependency requiring fresh verification. Unknown linkage requires targeted investigation and cannot be called preserved for context savings.

Unrelated accepted artifacts are excluded by default. If a material omitted dependency is discovered, persist:

```text
CONTEXT_EXPANSION_REQUIRED
correctness_trigger: <exact reason>
requested_expansion: <minimal dependency slice>
evidence_pointer: <path/authority pointer>
affected_decision_or_domain: <decision/domain>
```

Then inspect only that required dependency slice. Do not silently broaden the context or refuse a material cross-boundary read merely to protect a budget.

## 8. Product impact routing and bounded revalidation

When the selected context is Product mode, Product `REVALIDATE` uses the generic `REVALIDATE` flow and is applied to the pinned Product baseline vector without turning Product review into a full repository reread. The coordinator records this bounded chain:

```text
changed Project/source binding
→ Project-local impact root
→ qualified direct dependency traversal
→ affected cross-project relation/capability records
→ affected Product projections
→ resolved Product package evaluation
```

The changed binding and local impact root are routing inputs. Direct dependency metadata owned by the dependent artifact is verified before propagation; generated reverse indexes only locate candidates. Cross-project propagation occurs only across qualified evidence, STM relations, and explicit dependency edges bound to the selected Product revision and baseline. Unaffected accepted Project and Product state is recorded in `preserved_domains` only when its freshness and dependency mapping support that claim.

Product impact uses the existing `LOCAL`, `BOUNDARY`, and `SYSTEMIC` classification. A membership or shared-resource change is at least a Product boundary decision when it affects Product meaning; a source change remains local until evidence shows a cross-project edge. Missing or unavailable linkage prevents a preserved conclusion and records:

```text
CONTEXT_EXPANSION_REQUIRED
requested_expansion: <minimum qualified dependency/evidence slice>
```

`SYSTEMIC` emits `FULL_REAUDIT_RECOMMENDED` with an explicit user decision; it never starts a full Product review automatically. Product `REVALIDATE` preserves the prior accepted set, revalidates only the affected semantic slice, and separately accounts for projection freshness. It does not silently reopen unrelated Projects or regenerate projections.

Incomplete dependency coverage is `UNKNOWN_IMPACT`, not a preserved `UNAFFECTED` conclusion. Product candidate assessment uses the complete exact candidate Product vector paired with the complete exact accepted base vector. The required binding is the complete exact candidate Product vector.

Product `EXTEND` is additive. Adding a Project, capability, cross-project investigation, output, or shared-resource context preserves unaffected accepted state and resolves only the minimum new dependency/evidence slice. Removing or replacing a Project, changing its role, or changing a shared-resource declaration creates a new Product revision and requires explicit membership impact adjudication; it does not erase historical baselines or findings. A bounded downstream revalidation is required only for records that depend on the changed Product meaning.

### Bottom-up Product child advancement

When a child Project independently reaches an accepted source/authority state, qualified local state may satisfy the Product child-readiness dependency but does not advance the Product baseline directly. For a pinned Product baseline `PB-N` containing member A and a qualified local child accepted at B, route an accepted-state update through Product `REVALIDATE` over the pinned baseline and candidate member vector. When the user requests read-only candidate assessment instead, create a new Product `CHANGE_REVIEW` bound to the complete exact accepted base vector and complete exact candidate vector.

An older Product Change Review is not reusable when the complete qualified member vector, selected Product revision, or member qualification differs. `RECONCILE_CHANGE` remains contextual and is available only after the existing completed-review, exact-base-binding, material-delta, owner-completion, and explicit-confirmation gates. No direct child-adoption shortcut advances a Product baseline.

Source advancement and semantic-authority advancement are independent. A new accepted Architecture, Code Quality, Test Engineering, or STM owner revision on the same exact source binding leaves the Product member source vector unchanged. It may require only the bounded Product freshness/impact slice whose dependencies name that authority; it does not create a synthetic source change or trigger a full Product rescan.

### Delta reconciliation

The revalidation overlay/artifact contains at minimum:

```text
source_audit_revision
previous_baseline
current_baseline
change_range
impact_classification
changes_investigated
context_expansions
previous_accepted_evidence_preserved
findings_revalidated
findings_resolved
findings_still_valid
findings_changed
new_findings
capability_impacts
unresolved_items
```

For new state, prefer the unambiguous fields from the closeout hardening contract:

```text
accepted_baseline
candidate_baseline
source_head
```

If legacy overlay fields `previous_baseline` / `current_baseline` are retained,
`current_baseline` MUST be qualified as candidate/source context until
`BASELINE_ADVANCE_ALLOWED` is accepted; it must not silently mean accepted
baseline.

Link this overlay to the previous authoritative review rather than regenerating the entire report by default. `previous_accepted_evidence_preserved` means the impact analysis found no dependency requiring fresh verification. It does not mean freshly reread, runtime tested, independently reviewed, or newly proven.

Before `DELTA_RECONCILIATION` completes, each material row must carry its owner result and one of the allowed reconciliation outcomes defined above. The overlay itself remains proposed and cannot be consumed as accepted authority.

### Code Quality semantic revalidation

For a Code Quality `REVALIDATE`, the shared change inventory is refined through the direct bindings of accepted `CQ-*`, candidate, and `CQRA-*` records. The minimum semantic flow is:

```text
changed binding
  → resolve direct CQ dependency edges
  → identify affected CQ/CQRA identities
  → load the minimum affected EV/STM/context slice
  → mark affected accepted findings/actions STALE
  → revalidate and adjudicate only that slice
  → preserve unrelated accepted CQ authority
```

The direct binding categories are:

| Changed input | Affected Code Quality slice |
|---|---|
| file, symbol, or implementation mechanism | findings and candidates bound to that source/mechanism, including move, deletion, or regeneration |
| `EV-*` observation | findings whose evidence binding uses that observation |
| accepted STM fact | findings whose interpretation requires that fact |
| dependency, framework, runtime configuration, feature flag, or build mode | findings that declare the changed input as a material dependency |
| language/framework addendum or applicability revision | interpretations using that addendum or affected applicability decision |
| Architecture or Test Engineering authority | CQ relations and interpretations that explicitly depend on that authority |
| `CQRA-*` completion or semantic-basis change | every linked finding for that action, independently |

This is an evidence-backed dependency slice, not a new generic graph. Direct owning metadata is authoritative; changed paths, lockfiles, and diffs are routing context until the relevant dependency is established. An unknown link requires targeted investigation and cannot be classified as preserved merely to save work.

The revalidation overlay records at least the changed binding, affected CQ identities, preserved CQ identities, dependencies inspected, evidence loaded, and each finding's outcome. For each affected finding, the outcome is one of:

```text
same semantic issue
  → preserve CQ-* identity; revalidate to CURRENT or BLOCKED
issue absent
  → resolve CQ-* only with post-change evidence
materially different mechanism/meaning
  → SUPERSEDE old CQ-* and create a distinct replacement identity
insufficient evidence/context
  → retain lifecycle; set freshness BLOCKED
```

An equivalent refactor, rename, or file move may preserve identity when the mechanism, consequence, and relevant bindings remain semantically equivalent; the path change alone neither resolves nor invalidates the finding. A deleted source binding affects only findings depending on it. Dependency/configuration, addendum, STM, or related-authority changes affect only records with a material edge to that input. Unaffected CQ findings and their evidence are reused, not reconstructed.

`CQRA COMPLETED` marks remediation work complete and causes targeted revalidation of each linked finding; it never performs a bulk resolution. `REVALIDATE` remains separate from `RESUME`, `NEW`, and `EXTEND`, and it ends at semantic adjudication. It does not regenerate projections, register `PRJ-*`, run `RG-*`, or apply package policy. Any later projection freshness accounting uses the shared Stage B handoff after the semantic delta is stabilized.

### Test Engineering source-view routing

## Finding resolution freshness and semantic authority advancement

Finding lifecycle and freshness remain separate. An accepted `RESOLVED` revision is bound to the exact source, evidence, and dependency snapshot that proved absence. If a material source, STM fact, dependency, or resolution prerequisite advances, the old resolution remains historical but cannot prove absence on the new source.

The derived current view then exposes `RESOLUTION_REVALIDATION_REQUIRED` for that historical identity, excludes it from `RESOLVED + CURRENT` and verified-current absence, and does not invent `ACTIVE`. Owner revalidation must create the next accepted `ACTIVE` revision with `reopened_from` when the same root returns, or a qualified supersession outcome when the mechanism is materially different. Active findings on an advanced source remain visible with `STALE` or qualified `freshness=BLOCKED` limitation until owner revalidation.

`SOURCE_ADVANCEMENT` and `SEMANTIC_AUTHORITY_ADVANCEMENT` are independent. A new accepted owner revision on the same source can stale a dependent Product or projection state without changing the source vector or advancing Product baseline acceptance. A `remediation_status=BLOCKED` value remains orthogonal and never implies resolution or accepted risk.

Test Engineering records concrete revision bindings for each accepted BC and CC. A service and consumer may therefore have independent baselines:

```text
BC-042.source_bindings:
  architecture_revision
  declared_revision
  implementation_revision
  consumer_revision

CC-017.compared_views:
  declared_revision
  implementation_revision
  consumer_revision
  tested_revision
```

For a changed binding, route only the affected view and dependent slice:

```text
tests-only change
  → revalidate affected TM/MAT/GAP
  → BC remains valid unless independent semantic evidence says otherwise

implementation or declared-contract change
  → revalidate affected IMPLEMENTED/DECLARED views
  → run CC/BC impact analysis

consumer-only change with unchanged service repository
  → revalidate affected CONSUMED views
  → revalidate consumer-facing simulator/E2E projections as needed
```

A file/path diff is routing context, not semantic proof. Do not restart the whole Test Engineering package or unrelated Architecture Review without impact evidence.
