# Finding Lifecycle & Progress Reporting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved Finding Lifecycle & Progress Reporting semantics so Architecture and Code Quality findings preserve historical authority while Current Findings, accepted risk, freshness, legacy migration, Product aggregation, and baseline-to-baseline progress are reported deterministically.

**Architecture:** Extend existing owner-specific finding contracts rather than creating a new finding authority. Derive current/historical/progress views from accepted owner revisions, preserve lifecycle/freshness/disposition as orthogonal dimensions, and let Product aggregate only qualified child views bound to exact accepted Product baselines.

**Tech Stack:** Markdown skill/reference contracts, existing repository validation conventions, shell/static validation only where already used.

**Spec:** `docs/superpowers/specs/2026-09-16-finding-lifecycle-progress-reporting-design.md`

## Global Constraints

- Preserve exactly the existing Session Intents: `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `CHANGE_REVIEW`, and `PROJECTION_REPAIR`. `RECONCILE_CHANGE` remains contextual.
- Preserve exactly the existing top-level semantic capabilities: Architecture Review, Test Engineering, and Code Quality Review. Technical Documentation remains an output/projection.
- Architecture Review remains the sole authority for `RF-*` lifecycle, disposition, severity, revisions, resolution, reopening, and supersession.
- Code Quality Review remains the sole authority for `CQ-*` lifecycle, disposition, severity, revisions, resolution, reopening, and supersession.
- Do not create a generic Finding Management capability, Progress capability, Risk capability, shared cross-capability finding owner, Product finding authority, or Progress authority.
- Product only qualifies, composes, aggregates, compares, and presents accepted child state. Product never resolves, supersedes, reseveritizes, re-dispositions, reopens, or adjudicates a child finding.
- Historical finding identities and revisions remain traceable. No historical ledger record is deleted or rewritten to improve a metric.
- Current Findings is a derived view. Qualified current `RESOLVED` and `SUPERSEDED` findings are excluded from current technical stock; uncertainty caused by stale resolution, legacy unknown state, or unavailable qualification is shown separately.
- `ACTIVE` findings remain visible when stale or remediation-blocked. Staleness limits certainty; it does not hide known technical risk.
- A `RESOLVED` finding proven on source B does not prove absence on advanced source C without owner revalidation. The design must not synthesize `ACTIVE` or verified absence from missing evidence.
- Accepted risk is a disposition/treatment decision, not resolution. Accepted-risk findings remain materially current and are separately classified from actionable findings.
- `BLOCKED` remediation/execution status is orthogonal to lifecycle, disposition, and freshness. It never implies `RESOLVED` or `ACCEPTED_RISK`.
- `REOPENED` is a derived baseline transition. The accepted owner state is a newer `ACTIVE` revision with the prior resolution reference where the same root issue remains the same.
- Legacy lifecycle absence is represented as `LEGACY_STATUS_UNKNOWN`, a migration/qualification condition rather than an implicit `ACTIVE` or `RESOLVED` lifecycle value.
- The qualified-view fingerprint is deterministic, schema-versioned, canonical, and independent of Markdown wording, row order, timestamps, and workspace paths.
- Product baseline semantics remain the immutable exact qualified member/source/authority vector. The approved qualified-view fingerprint is an additional derived reproducibility reference, not a child-ledger copy.
- Source advancement and semantic-authority advancement remain separate axes. Child authority advancement does not silently advance an accepted Product baseline.
- Change Review `POTENTIALLY_RESOLVES` remains candidate-only. Reconciliation and owner adjudication are required before an accepted finding can become `RESOLVED`.
- Accepted semantic changes can stale dependent projections. Projection regeneration remains explicit; projections never mutate authority and never override authority.
- Legacy packages are handled conservatively without forced historical package rewrites, renumbering, or automatic Product baseline advancement.
- Do not add a database, runtime registry service, event-sourcing framework, persisted generic `FindingEvent` system, dashboard backend, analytics store, scheduler, watcher, automatic ticket integration, or automatic remediation engine.

## Repository Base and Discovery Record

The implementation plan is based on the following verified state:

| Item | Value |
|---|---|
| Working branch | `main` |
| Local `HEAD` | `adb576e16067ec3113182f5b4f9a865a4ca7e062` |
| `origin/main` | `2f794499693d789ad654e23056fc449f06586be6` |
| Approved design base | `2f794499693d789ad654e23056fc449f06586be6` |
| Working-tree condition | Existing unrelated untracked files preserved; no tracked files modified by planning |

`origin/main` has no material finding-lifecycle, Product-baseline, freshness,
Change Review, projection, or reporting change beyond the approved design base.
The local merge descendant contains the already reviewed federated Product
coordination lineage and does not invalidate the approved design.

The exact current owner boundaries used by the plan are:

- `references/report-contract.md` §2.1 and §4: Architecture report and `02-authoritative-findings-ledger.md` authority boundary.
- `references/evidence-and-severity.md` §§2, 6, 8, and 10: candidate/evidence/severity/identity foundations and existing RF authority reference.
- `capabilities/code-quality-review/references/code-quality-lifecycle.md`: existing CQ lifecycle, dispositions, freshness, and resolution rules; this contract is consumed unchanged unless validation proves a compatibility wording defect.
- `references/ownership-and-scenarios.md` §7.1 and `references/review-modes-and-orchestration.md` §§29–31 and §231: candidate Change Review and contextual reconciliation boundary.
- `references/revalidation-and-freshness.md` §§6–7 and §499: freshness, semantic-authority advancement, and Product revalidation routing.
- `references/product-multi-project-review.md` §§1, 5, 7–9: Product composition authority, exact baseline vector, qualification, availability, and bottom-up advancement.
- `references/projection-impact.md` and `references/projection-regeneration.md`: derived impact and explicit Stage B regeneration.
- `tests/*-validation.md` and `tests/*-backward-compatibility.md`: repository-style bounded Markdown contract validation; no generic test harness is planned.

## Planned File Map

| Path | Action | Responsibility in this feature | Owning task |
|---|---|---|---|
| `tests/finding-lifecycle-progress-reporting-validation.md` | CREATE | Fail-first and post-change static assertions for owner lifecycle, views, freshness, progress, Product qualification, fingerprint, Change Review, and projection boundaries | Task 1, Task 7 |
| `tests/finding-lifecycle-progress-reporting-backward-compatibility.md` | CREATE | Compatibility matrix for RF, CQ, TE, single-Project, Product, Change Review, revalidation, projection, and legacy packages | Task 1, Task 7 |
| `references/report-contract.md` | MODIFY | Architecture RF ledger extension boundary; derived current/historical/progress report contract; legacy qualification; accepted Product view reference | Task 2, Task 3, Task 4, Task 6 |
| `references/evidence-and-severity.md` | MODIFY | RF owner resolution gate, revision-bound evidence, severity revision rules, and shared vocabulary cross-reference | Task 2 |
| `docs/reference/artifacts.md` | MODIFY | Reader-facing RF/CQ lifecycle, disposition, freshness, remediation, lineage, and derived-view vocabulary | Task 2, Task 4 |
| `docs/reference/identifiers-and-statuses.md` | MODIFY | Cross-family dimension table and explicit RF/CQ/TE scope boundary | Task 3, Task 4 |
| `references/revalidation-and-freshness.md` | MODIFY | Stale active/resolved rules, source versus authority advancement, uncertainty qualification, and Product inheritance | Task 3 |
| `references/ownership-and-scenarios.md` | MODIFY | RF resolution/supersession/disposition authority barrier and candidate-to-owner reconciliation route | Task 2, Task 6 |
| `references/product-multi-project-review.md` | MODIFY | Qualified child Current Findings consumption, `CFV-1` binding, reproducible Product comparison, and unavailable-member limitations | Task 5 |
| `references/projection-impact.md` | MODIFY | Finding lifecycle/disposition semantic impact classification without projection authority | Task 6 |
| `references/projection-regeneration.md` | MODIFY | Explicit regeneration after accepted finding-view changes and stale projection verification | Task 6 |
| `docs/reference/outputs.md` | MODIFY | Human-readable separation of current state, progress, history, accepted residual risk, and uncertainty | Task 6 |

The existing `capabilities/code-quality-review/references/code-quality-lifecycle.md`,
`references/review-modes-and-orchestration.md`, and Test Engineering contracts
are validation inputs in this plan. They are not listed as modifications because
their current owner semantics already satisfy the approved compatibility
boundary.

## Implementation Plan

### Task 1: Establish the bounded fail-first lifecycle and progress validation contract

**Files:**
- Create: `tests/finding-lifecycle-progress-reporting-validation.md`
- Create: `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`
- Test: `references/report-contract.md`, `references/evidence-and-severity.md`, `references/revalidation-and-freshness.md`, `references/product-multi-project-review.md`, `capabilities/code-quality-review/references/code-quality-lifecycle.md`, `references/review-modes-and-orchestration.md`, `references/projection-regeneration.md`

**Purpose:** Establish a repository-style Markdown evidence surface whose rows
name the exact owner contract, required outcome, forbidden outcome, and static
verification evidence. The pre-change rows must demonstrate that the approved
finding-lifecycle model is not yet fully expressed, without modifying authority
contracts in this task.

**Interfaces / Contracts:**
- Consumes: Current RF authority in `references/report-contract.md` §4, current CQ axes in `capabilities/code-quality-review/references/code-quality-lifecycle.md`, current Product vector in `references/product-multi-project-review.md`, and current projection/reconciliation contracts.
- Produces: Stable validation IDs and exact assertions that Tasks 2–7 close; no runtime test framework and no persisted finding event model.

- [ ] **Step 1: Define pre-change validation rows.** Add rows for RF owner lifecycle, resolution gate, supersession, accepted-risk classification, `ACTIVE + BLOCKED`, stale active, stale resolved, reopen, severity migration, legacy unknown, current versus historical stock, all baseline transition flows, Product qualification, unavailable member handling, `CFV-1`, bottom-up advancement, Change Review candidate authority, projection freshness, the PB-1/PB-2 accounting case, FL-01 through FL-30, and FL-S1 through FL-S6.
- [ ] **Step 2: Define compatibility rows.** Add rows proving preservation of RF IDs, CQ IDs and statuses, TE-owned `BC-*`/`CC-*`/`MAT-*`/`TM-*`/`GAP-*`/`TASK-*` semantics, single-Project mode, Product mode, existing seven Session Intents, contextual `RECONCILE_CHANGE`, `REVALIDATE`, `EXTEND`, explicit projection regeneration, legacy packages, and no automatic Product advancement.
- [ ] **Step 3: Run the fail-first assertion set.** Run:
  ```bash
  rg -n 'Architecture RF Lifecycle Ownership' references/report-contract.md
  rg -n 'RESOLUTION_REVALIDATION_REQUIRED' references/revalidation-and-freshness.md
  rg -n 'CFV-1' references/product-multi-project-review.md
  ```
  Expected: each command exits with status 1 because the new owner subsection, stale-resolution qualification, and qualified-view fingerprint are not yet present in the pre-change normative contracts; record those three failures in the validation artifact's pre-change evidence section.
- [ ] **Step 4: Verify the artifacts remain static contracts.** Run:
  ```bash
  rg -n 'runtime database|event-sourcing|dashboard|automatic projection regeneration|Product.*resolve|Product.*supersede' tests/finding-lifecycle-progress-reporting-validation.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  ```
  Expected: every match is an explicit forbidden-outcome assertion, not a proposed implementation component.
- [ ] **Step 5: Record the proposed commit boundary.** Proposed commit message: `test: define finding lifecycle progress contract`. Do not create a commit during plan execution.

### Task 2: Add Architecture RF owner lifecycle, disposition, and resolution authority

**Files:**
- Modify: `references/report-contract.md`
- Modify: `references/evidence-and-severity.md`
- Modify: `docs/reference/artifacts.md`
- Modify: `references/ownership-and-scenarios.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`, `capabilities/code-quality-review/references/code-quality-lifecycle.md`

**Purpose:** Extend the existing Architecture-owned `02-authoritative-findings-ledger.md`
contract with explicit RF lifecycle/revision/disposition rules while reusing
the existing owner-qualified vocabulary. The Architecture Review owner remains
the only writer of accepted RF meaning.

**Interfaces / Contracts:**
- Consumes: `references/report-contract.md` §2 authority map and §4 ledger boundary; `references/evidence-and-severity.md` §§2, 6, 8, 10; CQ vocabulary from `capabilities/code-quality-review/references/code-quality-lifecycle.md`.
- Produces: Implementation-ready RF owner rules for `ACTIVE`, `RESOLVED`, `SUPERSEDED`, same-identity revision changes, owner-qualified disposition, and the accepted resolution gate.

- [ ] **Step 1: Add the RF owner subsection at the existing ledger boundary.** In `references/report-contract.md` §4, state that Architecture Review alone accepts or changes RF lifecycle, severity, disposition, revision, resolution, reopening, and supersession. Name the Architecture-owned `02-authoritative-findings-ledger.md` as the exact extension target and preserve Product's composition-only boundary.
- [ ] **Step 2: Specify the RF finding record.** Define stable RF identity, accepted owner revision, lifecycle, owner-qualified disposition, severity, evidence references, exact source/dependency binding, supersession lineage, and `reopened_from` provenance. State that a same-root severity or lifecycle change creates a new revision rather than a new identity.
- [ ] **Step 3: Specify transition authorities and gates.** Define that Architecture owner adjudicators accept `ACTIVE -> RESOLVED`, `ACTIVE -> SUPERSEDED`, `RESOLVED -> ACTIVE`, severity changes, and disposition changes. Require accepted evidence, owner revalidation, owner adjudication, exact proving source/dependency binding, and an accepted owner revision for resolution. Explicitly reject developer assertion, commit message, candidate Change Review, Product inference, and projection prose as resolution authority.
- [ ] **Step 4: Specify owner-qualified disposition.** Define `ACTION_REQUIRED` and Architecture's accepted-risk treatment in the RF owner contract without claiming that CQ terminology is automatically RF terminology. Cross-reference CQ's existing `ACCEPTED_EXCEPTION` and `WONT_FIX` semantics without rewriting them.
- [ ] **Step 5: Add authority-barrier assertions.** Require `references/ownership-and-scenarios.md` to state that Product cannot perform any RF transition and that `CHANGE_REVIEW`/`POTENTIALLY_RESOLVES` must route through contextual reconciliation to Architecture owner adjudication before accepted mutation.
- [ ] **Step 6: Run owner validation.** Run:
  ```bash
  rg -n 'Architecture Review.*sole|02-authoritative-findings-ledger.md|ACTIVE.*RESOLVED|ACTIVE.*SUPERSEDED|accepted owner revision|owner adjudication|Product.*must not|POTENTIALLY_RESOLVES' references/report-contract.md references/evidence-and-severity.md references/ownership-and-scenarios.md tests/finding-lifecycle-progress-reporting-validation.md
  ```
  Expected: PASS; each RF transition has Architecture ownership, accepted evidence, and revision provenance, and no Product transition is permitted.
- [ ] **Step 7: Run CQ regression inspection.** Run:
  ```bash
  rg -n 'ACTIVE -> RESOLVED|ACTIVE -> SUPERSEDED|ACCEPTED_EXCEPTION|WONT_FIX|RESOLVED.*STALE|COMPLETED.*never resolves' capabilities/code-quality-review/references/code-quality-lifecycle.md
  ```
  Expected: PASS; CQ's existing lifecycle and disposition remain unchanged and are not flattened into RF authority.
- [ ] **Step 8: Record the proposed commit boundary.** Proposed commit message: `feat: define architecture finding lifecycle authority`. Do not create a commit during plan execution.

### Task 3: Define orthogonal dimensions, current/historical views, and freshness-safe progress

**Files:**
- Modify: `references/report-contract.md`
- Modify: `references/revalidation-and-freshness.md`
- Modify: `docs/reference/identifiers-and-statuses.md`
- Modify: `docs/reference/artifacts.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`

**Purpose:** Make current technical risk, historical identity history, freshness,
remediation status, and baseline deltas deterministic derived views. The
contract must keep stale risk visible and prevent a stale resolution from
claiming absence on an advanced source.

**Interfaces / Contracts:**
- Consumes: RF/CQ accepted owner revisions from Task 2; existing CQ freshness `CURRENT|STALE|BLOCKED`; existing source/semantic-authority advancement rules in `references/revalidation-and-freshness.md`.
- Produces: The `Current Findings View`, `Historical Findings View`, verified-current qualification, stock/flow/classification rules, and source-bound stale-resolution behavior.

- [ ] **Step 1: Add the four-dimension model.** In `docs/reference/identifiers-and-statuses.md` and the reader-facing artifact reference, define independent dimensions: lifecycle (`ACTIVE|RESOLVED|SUPERSEDED`), owner-qualified disposition, freshness (`CURRENT|STALE|BLOCKED`), and owner-specific remediation/execution status. State that Test Engineering families retain their existing semantics.
- [ ] **Step 2: Define the Current Findings predicate.** In `references/report-contract.md`, specify inclusion for qualified `ACTIVE + CURRENT`, `ACTIVE + STALE`, `ACTIVE + BLOCKED`, and active accepted-risk findings; exclusion for `RESOLVED + CURRENT`, `SUPERSEDED`, candidate-only records, and unqualified members; and separate uncertainty reporting for `RESOLVED + STALE`, `LEGACY_STATUS_UNKNOWN`, and unavailable members. State that stale active findings remain visible but are not verified-current.
- [ ] **Step 3: Define the Historical Findings View.** Specify historical registered identities/revisions, resolved history, superseded history, prior accepted-risk classifications, reopen provenance, and legacy uncertainty. State that historical categories may overlap as views and must not be added as mutually exclusive stocks unless the row-level predicate proves exclusivity.
- [ ] **Step 4: Add the source-bound freshness rule.** In `references/revalidation-and-freshness.md`, state that resolution is proven only for its accepted source/dependency snapshot. When the source or relevant dependency advances, retain the historical resolved fact, expose `RESOLUTION_REVALIDATION_REQUIRED`, withhold verified-current absence, do not synthesize `ACTIVE`, and route owner revalidation. State the parallel rule that stale active risk remains visible with a revalidation limitation.
- [ ] **Step 5: Define same-source authority advancement.** Preserve the independent `SOURCE ADVANCEMENT` and `SEMANTIC AUTHORITY ADVANCEMENT` axes. A newer accepted owner revision on the same source changes dependent semantic freshness without fabricating source advancement or silently advancing Product state.
- [ ] **Step 6: Define progress transitions.** In `references/report-contract.md`, define `NEW`, `RESOLVED`, `REOPENED`, `SUPERSEDED`, `SEVERITY_INCREASED`, `SEVERITY_DECREASED`, `UNCHANGED`, `ACCEPTED_RISK_ADDED`, and `ACCEPTED_RISK_REMOVED` as derived comparisons between two accepted comparable states. Mark current views as stock, lifecycle transitions as flows, and severity/disposition transitions as classifications.
- [ ] **Step 7: Define blocked remediation.** State that `ACTIVE + remediation_status: BLOCKED` remains in Current Findings, counts as technical risk, is not resolved, and is not accepted risk without an independent disposition. Freshness `BLOCKED` remains visible technical risk but is excluded from `VERIFIED_CURRENT`.
- [ ] **Step 8: Run freshness and accounting validation.** Run:
  ```bash
  rg -n 'ACTIVE.*CURRENT|ACTIVE.*STALE|ACTIVE.*BLOCKED|RESOLVED.*CURRENT|RESOLVED.*STALE|SUPERSEDED|LEGACY_STATUS_UNKNOWN|RESOLUTION_REVALIDATION_REQUIRED|SOURCE ADVANCEMENT|SEMANTIC AUTHORITY ADVANCEMENT' references/report-contract.md references/revalidation-and-freshness.md docs/reference/identifiers-and-statuses.md tests/finding-lifecycle-progress-reporting-validation.md
  ```
  Expected: PASS; every lifecycle/freshness combination has an inclusion or uncertainty outcome and source advancement cannot turn stale resolution into verified absence.
- [ ] **Step 9: Run the exact PB-1/PB-2 accounting assertion.** Run:
  ```bash
  rg -n 'historical identities.*4|current.*3.*3|NEW.*1|RESOLVED.*1|severity decreased.*1|HIGH.*2.*1|MEDIUM.*1.*2' tests/finding-lifecycle-progress-reporting-validation.md
  ```
  Expected: PASS; the accounting example keeps current stock at `3 -> 3`, reports one new finding, one resolved finding, and one severity decrease without double counting.
- [ ] **Step 10: Record the proposed commit boundary.** Proposed commit message: `feat: define current historical and progress views`. Do not create a commit during plan execution.

### Task 4: Add conservative legacy migration and compatibility qualification

**Files:**
- Modify: `references/report-contract.md`
- Modify: `docs/reference/identifiers-and-statuses.md`
- Modify: `docs/reference/artifacts.md`
- Test: `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`, `tests/finding-lifecycle-progress-reporting-validation.md`, `references/projection-lifecycle.md`

**Purpose:** Make legacy findings and legacy projections safe to consume without
silently activating or resolving records. Preserve old packages and route
ambiguous records to owner adjudication and bounded requalification.

**Interfaces / Contracts:**
- Consumes: Existing legacy Architecture registration in `references/report-contract.md` §2.2, projection legacy registration in `references/projection-lifecycle.md` §1.2, RF owner gate from Task 2, and derived views from Task 3.
- Produces: A deterministic evidence hierarchy, `LEGACY_STATUS_UNKNOWN` qualification behavior, migration outcomes, projection freshness behavior, and Product requalification conditions.

- [ ] **Step 1: Define the evidence hierarchy.** In `references/report-contract.md` §2.2 and the RF ledger section, define Tier 1 as explicit accepted owner lifecycle/status with complete identity/owner binding; Tier 2 as complete accepted resolution/supersession with identity, owner, and exact source binding; Tier 3 as finding-tied accepted remediation verification requiring owner adjudication when lifecycle authority is absent; Tier 4 as report/projection prose; Tier 5 as commit messages, code absence, timestamps, or inference.
- [ ] **Step 2: Define migration outcomes.** Permit mechanical migration only for complete Tier 1 and Tier 2 evidence. Route Tier 3 to Architecture or CQ owner adjudication. Reject Tier 4 and Tier 5 as lifecycle authority. Use `LEGACY_STATUS_UNKNOWN` as a derived migration/qualification condition, never as a permanent lifecycle state unless an owner contract explicitly requires storage.
- [ ] **Step 3: Define unknown reporting.** State that unknown legacy records are excluded from definitive current/resolved/severity counts, shown in a mandatory uncertainty set, cannot be treated as zero risk or verified resolved by Product, and require owner adjudication for strong current claims.
- [ ] **Step 4: Define preservation behavior.** State that old ledgers and packages are not rewritten automatically, old RF/CQ IDs remain stable, affected projections are marked non-current/stale through existing projection rules, and Product baseline requalification is required when child binding or qualified-view evidence cannot be proven.
- [ ] **Step 5: Add negative migration assertions.** Require the validation artifact to reject an old report saying “fixed” without accepted owner resolution, missing lifecycle metadata defaulted to `ACTIVE`, and missing lifecycle metadata defaulted to `RESOLVED`.
- [ ] **Step 6: Run legacy validation.** Run:
  ```bash
  rg -n 'Tier 1|Tier 2|Tier 3|Tier 4|Tier 5|LEGACY_STATUS_UNKNOWN|fixed|not.*ACTIVE|not.*RESOLVED|owner adjudication|Product.*requalification|not.*rewrite' references/report-contract.md docs/reference/identifiers-and-statuses.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md tests/finding-lifecycle-progress-reporting-validation.md
  ```
  Expected: PASS; the evidence threshold and all conservative outcomes are explicit.
- [ ] **Step 7: Run projection compatibility inspection.** Run:
  ```bash
  rg -n 'legacy|non-current|STALE|semantic authority|projection.*not.*authority|do not.*overwrite' references/projection-lifecycle.md references/report-contract.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  ```
  Expected: PASS; legacy registration and projection status remain separate from finding lifecycle authority.
- [ ] **Step 8: Record the proposed commit boundary.** Proposed commit message: `feat: define conservative legacy finding migration`. Do not create a commit during plan execution.

### Task 5: Integrate qualified Product current views and deterministic `CFV-1` fingerprints

**Files:**
- Modify: `references/product-multi-project-review.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`, `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`, `references/revalidation-and-freshness.md`

**Purpose:** Let Product compare qualified child current state reproducibly
without copying child ledgers or gaining child lifecycle authority.

**Interfaces / Contracts:**
- Consumes: Task 3 Current Findings View and freshness/limitation rules; existing Product exact vector and bottom-up advancement rules in `references/product-multi-project-review.md` §§5, 7–9.
- Produces: Member-qualified Product current aggregation, exact `CFV-1` canonical payload, and minimum Product baseline binding for baseline-to-baseline progress.

- [ ] **Step 1: Define qualified child input.** In `references/product-multi-project-review.md`, require each Product row to retain member key, Project identity, owner capability/finding family, accepted child owner revision, exact source/baseline binding, freshness, disposition, and limitation references. State that bare RF/CQ IDs are not Product-global identities.
- [ ] **Step 2: Define Product current aggregation.** Specify that Product consumes each qualified child Current Findings View, preserves unavailable/unknown members as limitations rather than zero rows, and derives current risk, actionable count, accepted residual risk, verified-current count, and uncertainty count. Product never changes child lifecycle or disposition.
- [ ] **Step 3: Define `CFV-1` scope.** Specify that `CFV-1` covers only the qualified Current Findings snapshot, not the historical registry. Include Product/member qualification context, member/project identity, owner capability, finding family, finding ID, accepted owner revision, lifecycle, owner-qualified disposition, severity, freshness classification where it changes interpretation, exact source/content binding, and interpretation-changing limitation markers. Exclude timestamps, workspace paths, Markdown text, rendering order, and volatile presentation metadata.
- [ ] **Step 4: Define canonical serialization.** Require UTF-8 canonical JSON with fixed field order, no insignificant whitespace, normalized strings, explicit `null` values, schema/version marker `CFV-1`, and rows sorted lexicographically by `member_key`, `project_key`, `owner_capability`, `finding_family`, `finding_id`, and `accepted_owner_revision`. State that semantic severity, lifecycle, disposition, freshness, source binding, qualification, or limitation changes alter the payload; Markdown wording/order and workspace path changes do not.
- [ ] **Step 5: Bind the fingerprint to Product baselines.** Preserve the immutable Product member/source vector and accepted child authority references. Add only the `CFV-1` qualified-view fingerprint/reference and its schema identifier; do not embed historical child ledgers. Require PB-N and PB-N+1 to compare exact accepted qualified bindings and fingerprints.
- [ ] **Step 6: Preserve bottom-up advancement.** State that child authority revision advancement, including same-source `ACTIVE -> RESOLVED`, makes the accepted Product state stale/needs revalidation. Only accepted Product `REVALIDATE` or complete-vector `CHANGE_REVIEW` followed by Product Baseline Acceptance creates the next Product baseline.
- [ ] **Step 7: Add fingerprint scenarios.** Require assertions for identical child source/owner revision and canonical view producing the same fingerprint; Markdown wording/order and workspace path changes preserving it; severity/lifecycle/disposition/member qualification/source binding changes altering it; and historical records remaining outside the payload.
- [ ] **Step 8: Run Product validation.** Run:
  ```bash
  rg -n 'member_key|project_key|accepted owner revision|CFV-1|canonical JSON|UTF-8|fixed field order|workspace path|historical.*not|unavailable.*not.*zero|Product.*must not|baseline.*fingerprint' references/product-multi-project-review.md tests/finding-lifecycle-progress-reporting-validation.md
  ```
  Expected: PASS; Product aggregation is qualified, fingerprint semantics are deterministic, and the baseline remains a reference to child authority rather than a copied ledger.
- [ ] **Step 9: Run bottom-up advancement validation.** Run:
  ```bash
  rg -n 'rev5|rev6|same source|child.*RESOLVED|Product.*unchanged|Product.*revalidation|Product Baseline Acceptance' references/product-multi-project-review.md references/revalidation-and-freshness.md tests/finding-lifecycle-progress-reporting-validation.md
  ```
  Expected: PASS; child semantic authority advancement cannot auto-advance PB-10.
- [ ] **Step 10: Record the proposed commit boundary.** Proposed commit message: `feat: add qualified Product finding progress views`. Do not create a commit during plan execution.

### Task 6: Align Change Review, projection freshness, and report presentation

**Files:**
- Modify: `references/ownership-and-scenarios.md`
- Modify: `references/projection-impact.md`
- Modify: `references/projection-regeneration.md`
- Modify: `docs/reference/outputs.md`
- Test: `references/review-modes-and-orchestration.md`, `tests/finding-lifecycle-progress-reporting-validation.md`

**Purpose:** Connect accepted finding-view changes to existing candidate,
impact, and projection workflows while keeping candidate assessment and
human-readable output non-authoritative.

**Interfaces / Contracts:**
- Consumes: Task 2 owner gate, Task 3 derived views, Task 5 Product qualified view, existing Change Review in `references/review-modes-and-orchestration.md`, and existing projection V1–V4/regeneration contracts.
- Produces: Candidate-only `POTENTIALLY_RESOLVES`, explicit semantic impact, explicit regeneration, and unambiguous report labels for current state, progress, history, accepted risk, and uncertainty.

- [ ] **Step 1: Preserve candidate-only resolution.** In `references/ownership-and-scenarios.md`, state that `CHANGE_REVIEW: POTENTIALLY_RESOLVES` may appear only in candidate assessment; accepted Current Findings remains unchanged until `RECONCILE_CHANGE` dispatches to the owning Architecture or Code Quality authority and the owner accepts evidence.
- [ ] **Step 2: Connect finding changes to impact accounting.** In `references/projection-impact.md`, classify accepted lifecycle, severity, disposition, source-binding, and qualified-view changes as semantic inputs for derived impact analysis. State that the impact record predicts affected projections and does not mutate finding authority.
- [ ] **Step 3: Preserve explicit projection regeneration.** In `references/projection-regeneration.md`, state that accepted owner changes may mark dependent projections stale, regeneration requires an explicit existing regeneration session and V1–V4 checks, and old Markdown cannot override accepted owner state. Prohibit automatic regeneration.
- [ ] **Step 4: Define human-readable output sections.** In `docs/reference/outputs.md`, require separate sections for `CURRENT STATE`, `PROGRESS SINCE PREVIOUS ACCEPTED BASELINE`, `HISTORICAL`, and `RESIDUAL ACCEPTED RISK`, with stale/unknown/unavailable limitations. Define current severity distribution as the distribution over qualified included Current Findings only.
- [ ] **Step 5: Add negative Change Review assertions.** Require validation to prove that candidate `POTENTIALLY_RESOLVES` does not remove an accepted RF/CQ row, change current severity, close a finding, or advance Product baseline.
- [ ] **Step 6: Add projection assertions.** Require validation to prove owner authority changes first, dependent projections may become stale, explicit regeneration updates only presentation, and projection wording never creates resolution or Product advancement.
- [ ] **Step 7: Run cross-boundary validation.** Run:
  ```bash
  rg -n 'POTENTIALLY_RESOLVES|RECONCILE_CHANGE|owner.*accept|semantic impact|V1|V2|V3|V4|explicit.*regeneration|automatic.*regeneration|CURRENT STATE|PROGRESS SINCE|HISTORICAL|RESIDUAL ACCEPTED RISK' references/ownership-and-scenarios.md references/review-modes-and-orchestration.md references/projection-impact.md references/projection-regeneration.md docs/reference/outputs.md tests/finding-lifecycle-progress-reporting-validation.md
  ```
  Expected: PASS; candidate, semantic authority, Product baseline, and projection presentation remain separate.
- [ ] **Step 8: Record the proposed commit boundary.** Proposed commit message: `docs: align finding progress and projection reporting`. Do not create a commit during plan execution.

### Task 7: Close bounded validation and backward-compatibility evidence

**Files:**
- Modify: `tests/finding-lifecycle-progress-reporting-validation.md`
- Modify: `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`
- Test: `SKILL.md`, `references/review-modes-and-orchestration.md`, `references/revalidation-and-freshness.md`, `references/product-multi-project-review.md`, `capabilities/code-quality-review/references/code-quality-lifecycle.md`, `capabilities/test-review/SKILL.md`, `references/projection-lifecycle.md`, `references/projection-regeneration.md`

**Purpose:** Convert the fail-first matrices into bounded post-change evidence
covering every approved pressure scenario and compatibility boundary. This task
does not add a generic harness or change Test Engineering ownership.

**Interfaces / Contracts:**
- Consumes: All normative changes from Tasks 2–6 and existing unchanged owner contracts.
- Produces: Static PASS evidence for FL-01 through FL-30, FL-S1 through FL-S6, authority barriers, accounting, legacy handling, and backward compatibility.

- [ ] **Step 1: Close the lifecycle scenario matrix.** Update each FL-01 through FL-30 row with exact owner, accepted-state precondition, derived view result, freshness/qualification result, accounting result, and Product/projection boundary. Mark each row `PASS` only when its cited contract clause supplies all required dimensions.
- [ ] **Step 2: Close the safety scenario matrix.** Mark FL-S1 stale resolution, FL-S2 stale active, FL-S3 accepted risk, FL-S4 blocked remediation, FL-S5 legacy “fixed” prose, and FL-S6 fingerprint determinism `PASS` with exact evidence references.
- [ ] **Step 3: Close compatibility rows.** Mark PASS for existing RF/CQ IDs, CQ lifecycle/dispositions, TE-specific families, seven Session Intents, three capabilities, single-Project reporting, Product composition, Product baseline immutability, Change Review, `REVALIDATE`, `EXTEND`, projection lifecycle, explicit regeneration, legacy package preservation, and no automatic advancement.
- [ ] **Step 4: Run the static validation command set.** Run:
  ```bash
  rg -n '^\| FL-(0[1-9]|1[0-9]|2[0-9]|30) \| PASS \|' tests/finding-lifecycle-progress-reporting-validation.md
  rg -n '^\| FL-S[1-6] \| PASS \|' tests/finding-lifecycle-progress-reporting-validation.md
  rg -n '^\| BC[0-9]+ \|.*PASS' tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  rg -n 'Product.*(never|must not).*resolve|Product.*(never|must not).*supersede|POTENTIALLY_RESOLVES|LEGACY_STATUS_UNKNOWN|RESOLUTION_REVALIDATION_REQUIRED|CFV-1' tests/finding-lifecycle-progress-reporting-validation.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  ```
  Expected: 30 FL rows, 6 safety rows, and every compatibility row report `PASS`; the negative authority assertions are present.
- [ ] **Step 5: Inspect the Test Engineering boundary.** Run:
  ```bash
  rg -n 'BC-|CC-|MAT-|TM-|GAP-|TASK-|TASK.*never resolves.*GAP|Test Engineering' capabilities/test-review/SKILL.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  ```
  Expected: PASS; TE artifacts retain owner-specific semantics and are not assigned RF/CQ lifecycle.
- [ ] **Step 6: Run repository-wide hygiene checks.** Run:
  ```bash
  git diff --check
  rg -n 'FEDERATED_|Finding Management capability|Progress capability|Risk capability|Product.*finding authority|FindingEvent|automatic.*baseline|automatic.*projection' SKILL.md references docs/reference capabilities tests/finding-lifecycle-progress-reporting-validation.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  ```
  Expected: `git diff --check` passes; any semantic-term matches are explicit compatibility prohibitions or existing legitimate terms, with no new intent, capability, authority, event framework, or automatic mutation.
- [ ] **Step 7: Record the proposed commit boundary.** Proposed commit message: `test: close finding lifecycle progress compatibility matrix`. Do not create a commit during plan execution.

### Task 8: Perform final documentation verification and handoff

**Files:**
- Test: `docs/superpowers/specs/2026-09-16-finding-lifecycle-progress-reporting-design.md`, `docs/superpowers/plans/2026-09-16-finding-lifecycle-progress-reporting-implementation-plan.md`, `tests/finding-lifecycle-progress-reporting-validation.md`, `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`

**Purpose:** Verify that the implementation result can be reviewed against the
approved design, that no task has introduced an architecture decision, and that
the plan's contract vocabulary is internally consistent.

**Interfaces / Contracts:**
- Consumes: Approved design §§6, 9, 14, 20, 24 and all Task 1–7 validation evidence.
- Produces: A review-ready implementation handoff with no unresolved semantic choice and no implementation performed in the planning session.

- [ ] **Step 1: Run the spec-to-plan coverage check.** Run:
  ```bash
  rg -n '^## (6|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31)' docs/superpowers/specs/2026-09-16-finding-lifecycle-progress-reporting-design.md
  rg -n '^### Task [1-8]:' docs/superpowers/plans/2026-09-16-finding-lifecycle-progress-reporting-implementation-plan.md
  ```
  Expected: every major approved design section is mapped to one or more tasks and all eight tasks are present.
- [ ] **Step 2: Run the forbidden-placeholder scan.** Run:
  ```bash
  rg -n -i '[T]BD|T[O]DO|la[t]er|simil[a]r|appropri[a]te|as [n]eeded|e[t]c\.|relevant [f]iles' docs/superpowers/plans/2026-09-16-finding-lifecycle-progress-reporting-implementation-plan.md
  ```
  Expected: no matches.
- [ ] **Step 3: Run the task vocabulary consistency check.** Run:
  ```bash
  rg -n 'ACTIVE|RESOLVED|SUPERSEDED|ACTION_REQUIRED|ACCEPTED_RISK|BLOCKED|STALE|CURRENT|LEGACY_STATUS_UNKNOWN|RESOLUTION_REVALIDATION_REQUIRED|REOPENED|CFV-1|POTENTIALLY_RESOLVES' docs/superpowers/plans/2026-09-16-finding-lifecycle-progress-reporting-implementation-plan.md
  ```
  Expected: each term is used with the exact approved meaning and no task introduces a competing enum or authority.
- [ ] **Step 4: Verify scope restriction.** Run:
  ```bash
  git status --short
  git diff --name-only -- SKILL.md references capabilities tests docs/current-status.md docs/roadmap.md
  ```
  Expected: the planning session has not modified restricted implementation/contract files; only the two permitted plan/report artifacts are created or modified.
- [ ] **Step 5: Record the proposed handoff boundary.** Proposed commit message: `docs: add finding lifecycle progress implementation plan`. Do not create a commit during plan execution.

## Implementation Review Gates

### Gate 1: Owner lifecycle contract

Review after Task 1 and Task 2. Confirm that the exact Architecture ledger
extension target is named, RF and CQ authorities remain separate, resolution is
evidence/revalidation/adjudication/revision gated, and all fail-first owner
assertions pass.

### Gate 2: Freshness, views, and legacy qualification

Review after Task 3 and Task 4. Confirm that current stock, historical views,
freshness, blocked remediation, stale resolution, stale active findings, and
legacy unknown records have deterministic inclusion and uncertainty behavior.

### Gate 3: Product qualified views and fingerprint

Review after Task 5. Confirm that Product binds qualified child authority and
`CFV-1` without copying child ledgers, that unavailable members are not zero,
and that bottom-up authority advancement does not advance a Product baseline.

### Gate 4: Integrated compatibility and reporting

Review after Task 6 and Task 7. Confirm Change Review candidate-only behavior,
explicit projection regeneration, single-Project reporting, federated Product
aggregation, TE boundary, accounting scenarios, all FL rows, all safety rows,
and all compatibility rows.

## Final Verification Matrix

| Requirement | Validation artifact | Task | Expected result |
|---|---|---:|---|
| RF lifecycle authority | `tests/finding-lifecycle-progress-reporting-validation.md` | 2, 7 | Architecture owner alone accepts lifecycle/revision transitions. |
| CQ compatibility | `tests/finding-lifecycle-progress-reporting-backward-compatibility.md` | 2, 7 | Existing CQ lifecycle, dispositions, freshness, and CQRA separation remain intact. |
| Accepted risk | Both lifecycle artifacts | 2, 3, 7 | Accepted risk is current technical risk with separate actionable/residual classification and no resolution credit. |
| `ACTIVE + BLOCKED` | Lifecycle validation FL-S4 | 3, 7 | Finding remains current technical risk; blocked remediation is not resolution or acceptance. |
| Stale active | Lifecycle validation FL-S2 | 3, 7 | Finding remains visible with revalidation limitation. |
| Stale resolved | Lifecycle validation FL-S1 | 3, 7 | Historical resolution remains bound to B; C has uncertainty and no invented active/verified absence. |
| Legacy unknown | Backward compatibility matrix and FL-S5 | 4, 7 | Missing or weak evidence is unknown, never implicit active or resolved. |
| Reopen | Lifecycle validation FL-07 and FL-28 | 2, 3, 7 | Same identity uses newer accepted active revision; derived reopen preserves prior resolution history. |
| Severity changes | FL-08, FL-09, FL-26 and PB-1/PB-2 row | 2, 3, 7 | Severity migration preserves identity and is not counted as delete plus create. |
| Current versus historical | FL-02, FL-03, FL-19, FL-27 | 3, 7 | Current stock excludes qualified resolved/superseded records; history retains them. |
| Product qualification | FL-12, FL-13, FL-22, FL-23, FL-25 | 5, 7 | Member/project/owner/source qualification is preserved and unavailable members are limited, not zero. |
| `CFV-1` fingerprint | FL-S6 and Product fingerprint rows | 5, 7 | Canonical semantic payload is stable for presentation/path changes and changes for semantic changes. |
| Bottom-up authority advancement | FL-12, FL-13, FL-23, FL-24 | 5, 7 | Child advancement stales Product state; Product acceptance is required for the next baseline. |
| Change Review | FL-14, FL-15 and negative candidate assertions | 2, 6, 7 | Candidate potential never mutates accepted lifecycle or Product baseline. |
| Projection freshness | FL-16, FL-17 | 6, 7 | Authority changes first; projections become stale and regenerate only explicitly. |
| Single-Project compatibility | Backward compatibility matrix | 7 | Single Project reports current, history, progress, risk disposition, and uncertainty without Product mode. |
| Federated Product compatibility | Backward compatibility matrix and Product rows | 5, 7 | Product composes qualified child views without becoming child authority. |
| Historical accounting | FL-02, FL-05, FL-18, FL-19, FL-27, FL-28, FL-29 | 3, 7 | Historical count may increase while current risk decreases; flows and classifications do not double count. |
| Authority/YAGNI | Compatibility matrix and repository hygiene command | 6, 7 | No new authority, capability, intent, runtime framework, event system, or automatic mutation appears. |

## Plan Completion Criteria

The implementation session is complete only when all tasks have passed their
targeted static validations, the final matrix has no GAP row, all FL-01 through
FL-30 and FL-S1 through FL-S6 rows are `PASS`, restricted files remain
unchanged outside approved implementation work, and no new authority or runtime
framework has been introduced. The executor must stop with
`DO_NOT_BUILD_HARNESS` if a validation request would require a new runtime test
harness, and must stop with `STOP_HARNESS_EXPANSION` if static Markdown evidence
cannot express the requested assertion without a materially new framework.
