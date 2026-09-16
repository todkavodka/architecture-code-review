# Finding Lifecycle & Progress Reporting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved Finding Lifecycle & Progress Reporting semantics so Architecture and Code Quality findings preserve historical authority while Current Findings, accepted risk, freshness, legacy migration, Product aggregation, and baseline-to-baseline progress are reported deterministically.

**Architecture:** Extend existing owner-specific finding contracts rather than creating a new finding authority. Derive current/historical/progress views from accepted owner revisions, preserve lifecycle/freshness/disposition/remediation as orthogonal dimensions, and let Product aggregate only qualified child views bound to exact accepted Product baselines. Product remains composition-only.

**Tech Stack:** Markdown skill/reference contracts, repository-native Markdown validation artifacts, shell/static verification with `rg`, `git diff`, and `git diff --check`. No runtime harness.

**Spec:** `docs/superpowers/specs/2026-09-16-finding-lifecycle-progress-reporting-design.md`

## Global Constraints

- Preserve exactly the existing Session Intents: `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `CHANGE_REVIEW`, and `PROJECTION_REPAIR`. `RECONCILE_CHANGE` remains contextual.
- Preserve exactly the existing top-level semantic capabilities: Architecture Review, Test Engineering, and Code Quality Review. Technical Documentation remains an output/projection.
- Architecture Review remains the sole authority for `RF-*` lifecycle, disposition, severity, revisions, resolution, reopening, and supersession.
- Code Quality Review remains the sole authority for `CQ-*` lifecycle, disposition, severity, revisions, resolution, reopening, and supersession.
- Product only qualifies, composes, aggregates, compares, and presents accepted child state. Product never resolves, supersedes, reseveritizes, re-dispositions, reopens, or adjudicates a child finding.
- Historical finding identities and revisions remain traceable. No historical ledger record is deleted or rewritten to improve a metric.
- Current Findings is a derived view. Qualified current `RESOLVED` and `SUPERSEDED` findings are excluded from current technical stock; stale resolution, legacy unknown state, and unavailable qualification are disclosed separately.
- `ACTIVE` findings remain visible when stale or when remediation is blocked. Staleness limits certainty; it does not hide known technical risk.
- A `RESOLVED` finding proven on source B does not prove absence on advanced source C without owner revalidation. Missing evidence must not synthesize `ACTIVE` or verified absence.
- Accepted risk is a disposition/treatment decision, not lifecycle and not resolution. Accepted-risk findings remain materially current.
- Keep these dimensions distinct and use qualified names in all new normative text:
  - `lifecycle = ACTIVE | RESOLVED | SUPERSEDED`
  - `freshness = CURRENT | STALE | BLOCKED`
  - `disposition = owner-qualified treatment decision`
  - `remediation_status = owner-specific work/execution state`, including `BLOCKED` where applicable.
- The token `BLOCKED` MUST always be qualified as either `freshness=BLOCKED` or `remediation_status=BLOCKED` when both interpretations are possible. Do not introduce `ACTIVE_BLOCKED` or any combined lifecycle enum.
- `REOPENED` is a derived baseline transition. The accepted owner state is a newer `ACTIVE` revision with prior-resolution provenance where identity remains the same.
- Legacy lifecycle absence is `LEGACY_STATUS_UNKNOWN`, a migration/qualification condition, not implicit `ACTIVE` or `RESOLVED`.
- Product baseline semantics remain the immutable exact qualified member/source/authority vector. A qualified-view fingerprint is an additional derived reproducibility reference, not a copied child ledger.
- `CFV-1` uses SHA-256 over exact canonical UTF-8 JSON bytes as specified in Task 5. Serialized digest form is `sha256:<64 lowercase hex chars>`.
- Source advancement and semantic-authority advancement remain separate axes. Child authority advancement does not silently advance an accepted Product baseline.
- Change Review `POTENTIALLY_RESOLVES` remains candidate-only. Reconciliation and owner adjudication are required before accepted lifecycle mutation.
- Projection regeneration remains explicit. Projections never mutate authority and never override authority.
- Do not add a database, runtime registry service, event-sourcing framework, persisted generic `FindingEvent` system, dashboard backend, analytics store, scheduler, watcher, automatic remediation engine, new capability, new Session Intent, new Product authority, or automatic baseline/projection advancement.
- Stop with `DO_NOT_BUILD_HARNESS` if validation would require a new runtime test harness.
- Stop with `STOP_HARNESS_EXPANSION` if bounded static evidence starts expanding into a framework.
- Stop with `VALIDATION_BUDGET_EXCEEDED` if validation growth is no longer proportional to this contract-only change.

---

## Planned File Map

Exactly these implementation files are allowed to change. Task 8 verifies this allowlist.

| Path | Action | Responsibility | Task(s) |
|---|---|---|---|
| `tests/finding-lifecycle-progress-reporting-validation.md` | CREATE | Fail-first and post-change contract fixtures for lifecycle, current/history/progress, freshness, accounting, Product qualification, fingerprint, Change Review, and projection boundaries | 1, 7 |
| `tests/finding-lifecycle-progress-reporting-backward-compatibility.md` | CREATE | Compatibility matrix for RF/CQ/TE, single Project, Product, legacy, Change Review, revalidation, and projections | 1, 7 |
| `references/report-contract.md` | MODIFY | Architecture RF ledger lifecycle/disposition boundary; Current/Historical/Progress views; legacy qualification | 2, 3, 4, 6 |
| `references/evidence-and-severity.md` | MODIFY | RF resolution gate, revision-bound evidence, severity revision rules | 2 |
| `docs/reference/artifacts.md` | MODIFY | Reader-facing lifecycle/disposition/freshness/remediation/lineage vocabulary | 2, 3, 4 |
| `docs/reference/identifiers-and-statuses.md` | MODIFY | Orthogonal dimension table; RF/CQ scope; TE boundary | 3, 4 |
| `references/revalidation-and-freshness.md` | MODIFY | Stale-active/stale-resolved rules; source vs semantic authority advancement; Product inheritance | 3 |
| `references/ownership-and-scenarios.md` | MODIFY | RF authority barrier; candidate-to-owner reconciliation route | 2, 6 |
| `references/product-multi-project-review.md` | MODIFY | Qualified child Current Findings, `CFV-1`, exact Product comparison, unavailable-member limits | 5 |
| `references/projection-impact.md` | MODIFY | Finding lifecycle/disposition impact without projection authority | 6 |
| `references/projection-regeneration.md` | MODIFY | Explicit regeneration after accepted finding-view changes | 6 |
| `docs/reference/outputs.md` | MODIFY | Human-readable separation of current state, progress, history, residual accepted risk, uncertainty | 6 |

Validation inputs that MUST remain semantically unchanged unless a discovered contradiction blocks execution:

- `capabilities/code-quality-review/references/code-quality-lifecycle.md`
- `references/review-modes-and-orchestration.md`
- `capabilities/test-review/SKILL.md`
- `references/projection-lifecycle.md`
- `SKILL.md`

---

## Implementation Plan

### Task 1: Establish fail-first contract fixtures

**Files:**
- Create: `tests/finding-lifecycle-progress-reporting-validation.md`
- Create: `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`

**Interfaces:**
- Consumes: existing RF/CQ/Product/freshness/Change Review/projection contracts.
- Produces: named fixtures and assertions that Tasks 2–7 must make pass.

- [ ] **Step 1: Create the validation table with stable fixture IDs.** Include at least `FF-01..FF-10`, `FL-01..FL-30`, and `FL-S1..FL-S6`. Each row must have: precondition, accepted owner state, source/baseline, expected derived view, expected accounting, forbidden outcome, evidence path, status.

- [ ] **Step 2: Add these fail-first fixtures before changing normative contracts.**

  **FF-01 — stale resolved safety**
  ```text
  B: RF-001 HIGH RESOLVED + freshness=CURRENT
  C: relevant source/dependency advanced; no owner revalidation
  expected:
    historical: resolved on B
    C verified absence: NO
    C automatic ACTIVE: NO
    current uncertainty: RESOLUTION_REVALIDATION_REQUIRED
  ```

  **FF-02 — stale active visibility**
  ```text
  B: RF-002 HIGH ACTIVE + freshness=CURRENT
  C: relevant binding advanced; no revalidation
  expected:
    finding remains visible
    freshness=STALE or BLOCKED according to evidence availability
    verified-current claim: NO
    silent disappearance: forbidden
  ```

  **FF-03 — accepted-risk accounting**
  ```text
  PB-1: RF-003 HIGH ACTIVE disposition=ACTION_REQUIRED
  PB-2: RF-003 HIGH ACTIVE disposition=ACCEPTED_RISK
  expected:
    Current: 1 -> 1
    NEW: 0
    RESOLVED: 0
    ACCEPTED_RISK_ADDED: 1
    Actionable: 1 -> 0
    Residual accepted risk: 0 -> 1
  ```

  **FF-04 — remediation blocked is not freshness blocked**
  ```text
  RF-004 HIGH ACTIVE freshness=CURRENT remediation_status=BLOCKED
  expected:
    Current Findings: included
    RESOLVED: no
    ACCEPTED_RISK: no unless independent disposition exists
    reporting label: remediation blocked
  ```

  **FF-05 — PB accounting**
  ```text
  PB-1: RF-001 HIGH ACTIVE; RF-002 HIGH ACTIVE; RF-003 MEDIUM ACTIVE
  PB-2: RF-001 RESOLVED; RF-002 MEDIUM ACTIVE; RF-003 MEDIUM ACTIVE; RF-004 HIGH ACTIVE
  expected:
    historical identities = 4
    current = 3 -> 3
    NEW = 1
    RESOLVED = 1
    SEVERITY_DECREASED = 1
    HIGH = 2 -> 1
    MEDIUM = 1 -> 2
  ```

  **FF-06 — supersession accounting**
  ```text
  PB-1: RF-001 MEDIUM ACTIVE; RF-002 MEDIUM ACTIVE
  PB-2: RF-001 MEDIUM ACTIVE; RF-002 SUPERSEDED_BY RF-001
  expected:
    current = 2 -> 1
    RESOLVED = 0
    SUPERSEDED = 1
    historical identities = 2
  ```

  **FF-07 — unavailable Product member**
  ```text
  PB-N includes Project C
  PB-N+1 comparison cannot qualify Project C
  expected:
    Product result: LIMITED/UNKNOWN for affected aggregate
    Project C contribution: not zero, not unchanged
    limitation: mandatory
  ```

  **FF-08 — bottom-up semantic advancement**
  ```text
  PB-10 pins child owner rev5 / same source
  child accepts RF-017 ACTIVE -> RESOLVED at owner rev6
  expected:
    child local authority advances
    PB-10 unchanged
    semantic-authority advancement detected
    Product revalidation required before PB-11
  ```

  **FF-09 — fingerprint mutation**
  ```text
  same semantic rows + Markdown reorder/wording/path move => same fingerprint
  HIGH -> MEDIUM => different fingerprint
  ACTIVE -> RESOLVED => different fingerprint
  ACTION_REQUIRED -> ACCEPTED_RISK => different fingerprint
  member/source qualification change => different fingerprint
  ```

  **FF-10 — legacy weak evidence**
  ```text
  stable RF ID + old report text says "fixed" + no accepted owner resolution
  expected:
    not RESOLVED automatically
    LEGACY_STATUS_UNKNOWN / owner adjudication required
  ```

- [ ] **Step 3: Add backward-compatibility rows.** Cover stable RF/CQ IDs, existing CQ lifecycle/dispositions, TE-owned families, seven Session Intents, contextual `RECONCILE_CHANGE`, single-Project mode, Product mode, `REVALIDATE`, `EXTEND`, explicit projection regeneration, legacy package preservation, and no automatic Product advancement.

- [ ] **Step 4: Prove fail-first state.** Run:
  ```bash
  rg -n 'Architecture RF Lifecycle Ownership' references/report-contract.md
  rg -n 'RESOLUTION_REVALIDATION_REQUIRED' references/revalidation-and-freshness.md
  rg -n 'CFV-1' references/product-multi-project-review.md
  rg -n 'sha256:' references/product-multi-project-review.md
  ```
  Expected before implementation: all four searches fail because the approved contract is not yet fully encoded.

- [ ] **Step 5: Record actual failing evidence in the validation file.** Do not mark `FF-*` or `FL-*` PASS yet.

**Commit boundary:** combine with Task 2 as Commit 1.

---

### Task 2: Add Architecture RF lifecycle, disposition, and resolution authority

**Files:**
- Modify: `references/report-contract.md`
- Modify: `references/evidence-and-severity.md`
- Modify: `docs/reference/artifacts.md`
- Modify: `references/ownership-and-scenarios.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`

**Interfaces:**
- Consumes: Architecture RF ledger boundary and existing CQ lifecycle vocabulary.
- Produces: owner-local RF lifecycle/disposition semantics used by Tasks 3–6.

- [ ] **Step 1: Add `Architecture RF Lifecycle Ownership` at the existing `02-authoritative-findings-ledger.md` boundary.** Architecture Review alone accepts lifecycle, disposition, severity, revision, resolution, reopening, and supersession.

- [ ] **Step 2: Define accepted RF revision fields.** Include stable identity, accepted owner revision, lifecycle, owner-qualified disposition, severity, evidence refs, exact source/dependency binding, supersession lineage, and reopen provenance.

- [ ] **Step 3: Define transitions.** Support `ACTIVE -> RESOLVED`, `ACTIVE -> SUPERSEDED`, and `RESOLVED -> ACTIVE` on the same identity where root identity remains valid. Severity/disposition changes create new accepted revisions, not new IDs.

- [ ] **Step 4: Define the resolution gate.** Require accepted evidence + owner revalidation + owner adjudication + exact proving binding + accepted RF revision. Explicitly reject developer assertion, commit message, candidate Change Review, Product inference, and projection prose as resolution authority.

- [ ] **Step 5: Define RF treatment vocabulary.** Use `ACTION_REQUIRED` plus an Architecture-owned accepted-risk decision. Do not reinterpret CQ `WONT_FIX` as accepted risk. Preserve CQ `ACCEPTED_EXCEPTION` and `WONT_FIX` unchanged in their owner contract.

- [ ] **Step 6: Preserve authority barrier.** `POTENTIALLY_RESOLVES` routes through contextual reconciliation to the Architecture owner. Product cannot perform any RF transition.

- [ ] **Step 7: Verify Task 2.** Run:
  ```bash
  rg -n 'Architecture RF Lifecycle Ownership|02-authoritative-findings-ledger.md|ACTIVE.*RESOLVED|ACTIVE.*SUPERSEDED|RESOLVED.*ACTIVE|accepted owner revision|owner adjudication|POTENTIALLY_RESOLVES' references/report-contract.md references/evidence-and-severity.md references/ownership-and-scenarios.md
  rg -n 'ACCEPTED_EXCEPTION|WONT_FIX|ACTIVE -> RESOLVED|ACTIVE -> SUPERSEDED' capabilities/code-quality-review/references/code-quality-lifecycle.md
  git diff --check
  ```
  Expected: RF authority is explicit, CQ semantics remain unchanged, and diff check passes.

**Commit 1:**
```bash
git add tests/finding-lifecycle-progress-reporting-validation.md \
        tests/finding-lifecycle-progress-reporting-backward-compatibility.md \
        references/report-contract.md \
        references/evidence-and-severity.md \
        docs/reference/artifacts.md \
        references/ownership-and-scenarios.md
git commit -m "feat: define finding lifecycle authority contract"
```

---

### Task 3: Define Current/Historical/Progress views and freshness-safe accounting

**Files:**
- Modify: `references/report-contract.md`
- Modify: `references/revalidation-and-freshness.md`
- Modify: `docs/reference/identifiers-and-statuses.md`
- Modify: `docs/reference/artifacts.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`

**Interfaces:**
- Consumes: Task 2 accepted owner revisions.
- Produces: deterministic current/history/progress views and orthogonal state dimensions.

- [ ] **Step 1: Add the orthogonal dimension table.** Use the exact qualified forms `lifecycle`, `freshness`, `disposition`, and `remediation_status`. State explicitly that `freshness=BLOCKED` and `remediation_status=BLOCKED` are different axes.

- [ ] **Step 2: Define Current Findings inclusion.**
  - include `ACTIVE + freshness=CURRENT`;
  - include `ACTIVE + freshness=STALE` with revalidation limitation;
  - include `ACTIVE + freshness=BLOCKED` with evidence/freshness limitation;
  - include active accepted-risk findings in technical current risk, but classify them outside actionable remediation;
  - include `ACTIVE + remediation_status=BLOCKED` in technical current risk and mark remediation blocked;
  - exclude qualified `RESOLVED + CURRENT` from current stock;
  - exclude `SUPERSEDED` from current stock;
  - do not invent rows for unavailable members;
  - report `RESOLVED + stale proof` as `RESOLUTION_REVALIDATION_REQUIRED`, not verified absence and not synthetic ACTIVE;
  - report `LEGACY_STATUS_UNKNOWN` separately from definitive lifecycle counts.

- [ ] **Step 3: Define Historical Findings.** Preserve all accepted identities/revisions and separate `REGISTERED_RF`, `RESOLVED_RF_HISTORICALLY`, `SUPERSEDED_RF_HISTORICALLY`, `CURRENT_RF`, and `ACCEPTED_RISK_RF`. Explicitly state these are not a disjoint arithmetic partition.

- [ ] **Step 4: Define source-bound freshness.** Resolution is proven only for its accepted source/evidence/dependency snapshot. Source/dependency advancement invalidates the verified-absence claim until owner revalidation.

- [ ] **Step 5: Define progress transitions.** `NEW`, `RESOLVED`, `REOPENED`, `SUPERSEDED`, `SEVERITY_INCREASED`, `SEVERITY_DECREASED`, `UNCHANGED`, `ACCEPTED_RISK_ADDED`, `ACCEPTED_RISK_REMOVED` are derived baseline comparisons. Severity/disposition changes do not create fake new/resolved events.

- [ ] **Step 6: Encode the exact accounting fixtures from FF-03 through FF-06 in the validation artifact.** Ensure accepted-risk, severity movement, supersession, and current-stock arithmetic are asserted numerically.

- [ ] **Step 7: Verify Task 3.** Run:
  ```bash
  rg -n 'freshness=BLOCKED|remediation_status=BLOCKED|RESOLUTION_REVALIDATION_REQUIRED|LEGACY_STATUS_UNKNOWN|ACCEPTED_RISK_ADDED|SEVERITY_DECREASED|CURRENT_RF|REGISTERED_RF' references/report-contract.md references/revalidation-and-freshness.md docs/reference/identifiers-and-statuses.md tests/finding-lifecycle-progress-reporting-validation.md
  rg -n 'Current: 1 -> 1|Actionable: 1 -> 0|Residual accepted risk: 0 -> 1|current = 3 -> 3|NEW = 1|RESOLVED = 1|SEVERITY_DECREASED = 1|SUPERSEDED = 1' tests/finding-lifecycle-progress-reporting-validation.md
  git diff --check
  ```
  Expected: both BLOCKED dimensions are explicit and all accounting fixtures are present.

---

### Task 4: Add conservative legacy migration

**Files:**
- Modify: `references/report-contract.md`
- Modify: `docs/reference/identifiers-and-statuses.md`
- Modify: `docs/reference/artifacts.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`
- Test: `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`

**Interfaces:**
- Consumes: Task 2 owner gate and Task 3 view semantics.
- Produces: deterministic migration qualification without rewriting history.

- [ ] **Step 1: Define evidence tiers.** Tier 1 explicit accepted owner lifecycle/status; Tier 2 complete accepted resolution/supersession with identity/owner/source; Tier 3 accepted remediation verification requiring owner adjudication; Tier 4 report/projection prose; Tier 5 commit/code/timestamp inference.

- [ ] **Step 2: Permit mechanical migration only from complete Tier 1 and Tier 2.** Tier 3 requires owner adjudication. Tier 4/5 cannot mutate lifecycle.

- [ ] **Step 3: Define `LEGACY_STATUS_UNKNOWN`.** It is a migration/qualification condition, excluded from definitive lifecycle/severity counts and `VERIFIED_CURRENT`, shown as mandatory uncertainty, and never interpreted as zero risk or verified resolved.

- [ ] **Step 4: Preserve packages.** No mass rewrite, renumbering, or automatic Product baseline advancement. Requalify only affected Product baselines where child lifecycle/revision evidence cannot be proven.

- [ ] **Step 5: Verify FF-10.** Old report prose saying “fixed” without accepted owner resolution must remain `LEGACY_STATUS_UNKNOWN`/owner-adjudication-required.

- [ ] **Step 6: Verify Task 4.** Run:
  ```bash
  rg -n 'Tier 1|Tier 2|Tier 3|Tier 4|Tier 5|LEGACY_STATUS_UNKNOWN|owner adjudication|not.*RESOLVED|not.*ACTIVE|not.*rewrite' references/report-contract.md docs/reference/identifiers-and-statuses.md tests/finding-lifecycle-progress-reporting-validation.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  git diff --check
  ```

**Commit 2:**
```bash
git add references/report-contract.md \
        references/revalidation-and-freshness.md \
        docs/reference/identifiers-and-statuses.md \
        docs/reference/artifacts.md \
        tests/finding-lifecycle-progress-reporting-validation.md \
        tests/finding-lifecycle-progress-reporting-backward-compatibility.md
git commit -m "feat: define current findings freshness and legacy semantics"
```

---

### Task 5: Add qualified Product views and deterministic `CFV-1`

**Files:**
- Modify: `references/product-multi-project-review.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`
- Test: `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`

**Interfaces:**
- Consumes: Task 3 Current Findings and Task 4 legacy qualification.
- Produces: member-qualified Product aggregation, deterministic fingerprint, and reproducible PB-N/PB-N+1 comparison.

- [ ] **Step 1: Define qualified Product rows.** Retain member key, Project identity, owner capability/family, local finding ID, accepted owner revision, exact source/baseline binding, lifecycle, owner-qualified disposition, severity, freshness, and semantic limitation markers. Bare RF/CQ IDs are never Product-global.

- [ ] **Step 2: Define Product aggregation.** Product derives current technical risk, actionable, accepted residual risk, verified-current, and uncertainty counts from qualified child views. Unavailable/unqualified members are limitations, never zero rows or implicit unchanged state.

- [ ] **Step 3: Define `CFV-1` canonical payload.** Canonical JSON object fields, in this exact order:
  ```text
  schema
  product_revision
  product_baseline_key
  rows
  ```
  Each row uses this exact field order:
  ```text
  member_key
  project_key
  owner_capability
  finding_family
  finding_id
  accepted_owner_revision
  lifecycle
  owner_qualified_disposition
  severity
  freshness
  exact_source_or_content_binding
  semantic_limitation_marker
  ```
  Rows are sorted lexicographically by `member_key`, `project_key`, `owner_capability`, `finding_family`, `finding_id`, `accepted_owner_revision`.

- [ ] **Step 4: Define canonicalization exactly.**
  ```text
  encoding: UTF-8, no BOM
  Unicode normalization: NFC for every string before serialization
  insignificant whitespace: none
  absent optional field: explicit JSON null
  object field order: exactly CFV-1 schema order above
  array order: canonical sorted row order above
  numbers/booleans: standard JSON lexical form if ever present
  volatile exclusions: timestamps, Markdown wording, Markdown row order, workspace/filesystem paths, rendering metadata
  ```

- [ ] **Step 5: Define digest exactly.**
  ```text
  digest_algorithm = SHA-256
  digest_input = exact canonical UTF-8 JSON bytes
  digest_output = lowercase hexadecimal
  serialized_fingerprint = "sha256:" + 64 lowercase hex characters
  schema identifier = "CFV-1"
  ```
  A future canonical payload change MUST use a new schema identifier and cannot compare as `CFV-1`.

- [ ] **Step 6: Preserve Product baseline semantics.** Existing immutable Product member/source/authority vector remains authoritative. Add only `CFV-1` schema + fingerprint/reference. Do not embed historical child ledgers or replace owner revision refs.

- [ ] **Step 7: Preserve bottom-up semantics.** Same-source child owner rev5 -> rev6 is semantic-authority advancement; accepted Product PB-10 remains unchanged until Product revalidation/baseline acceptance.

- [ ] **Step 8: Add concrete Product fixtures.** Validation must include:
  - FF-07 unavailable member -> limited/unknown, not zero;
  - FF-08 child semantic advancement -> PB unchanged until acceptance;
  - FF-09 fingerprint invariance/mutation;
  - Project A `RF-001` and Project B `RF-001` remain distinct qualified rows.

- [ ] **Step 9: Verify Task 5.** Run:
  ```bash
  rg -n 'CFV-1|SHA-256|sha256:|UTF-8|NFC|no BOM|explicit.*null|member_key|project_key|accepted_owner_revision|workspace.*path|unavailable.*not.*zero|Product Baseline Acceptance' references/product-multi-project-review.md tests/finding-lifecycle-progress-reporting-validation.md
  git diff --check
  ```
  Expected: fingerprint is reproducible by independent implementations and Product remains composition-only.

**Commit 3:**
```bash
git add references/product-multi-project-review.md \
        tests/finding-lifecycle-progress-reporting-validation.md \
        tests/finding-lifecycle-progress-reporting-backward-compatibility.md
git commit -m "feat: add qualified Product finding progress fingerprint"
```

---

### Task 6: Align Change Review, projection freshness, and report presentation

**Files:**
- Modify: `references/ownership-and-scenarios.md`
- Modify: `references/projection-impact.md`
- Modify: `references/projection-regeneration.md`
- Modify: `docs/reference/outputs.md`
- Test: `tests/finding-lifecycle-progress-reporting-validation.md`

**Interfaces:**
- Consumes: Tasks 2–5.
- Produces: candidate-only resolution semantics, explicit projection staleness/regeneration, and current/progress/history output contract.

- [ ] **Step 1: Preserve candidate-only resolution.** `POTENTIALLY_RESOLVES` never mutates Current Findings. `RECONCILE_CHANGE` routes evidence to the owning capability.

- [ ] **Step 2: Define projection impact.** Accepted lifecycle/severity/disposition/source-binding/current-view changes may stale dependent projections; impact records do not mutate semantic authority.

- [ ] **Step 3: Preserve explicit regeneration.** Existing regeneration/V1–V4 rules remain explicit. Old Markdown cannot override accepted owner state.

- [ ] **Step 4: Define report sections.** Require `CURRENT STATE`, `PROGRESS SINCE PREVIOUS ACCEPTED BASELINE`, `HISTORICAL`, `RESIDUAL ACCEPTED RISK`, plus freshness/legacy/unavailable limitations. Current severity distribution counts only included current active findings under the approved freshness semantics.

- [ ] **Step 5: Verify Task 6.** Run:
  ```bash
  rg -n 'POTENTIALLY_RESOLVES|RECONCILE_CHANGE|explicit.*regeneration|V1|V2|V3|V4|CURRENT STATE|PROGRESS SINCE|HISTORICAL|RESIDUAL ACCEPTED RISK' references/ownership-and-scenarios.md references/projection-impact.md references/projection-regeneration.md docs/reference/outputs.md tests/finding-lifecycle-progress-reporting-validation.md
  git diff --check
  ```

---

### Task 7: Close all validation and backward compatibility evidence

**Files:**
- Modify: `tests/finding-lifecycle-progress-reporting-validation.md`
- Modify: `tests/finding-lifecycle-progress-reporting-backward-compatibility.md`
- Test: `SKILL.md`
- Test: `capabilities/code-quality-review/references/code-quality-lifecycle.md`
- Test: `capabilities/test-review/SKILL.md`
- Test: `references/review-modes-and-orchestration.md`
- Test: `references/projection-lifecycle.md`

**Interfaces:**
- Consumes: Tasks 2–6.
- Produces: bounded evidence that all approved scenarios and compatibility boundaries hold.

- [ ] **Step 1: Close FL-01..FL-30.** Each row gets exact owner, accepted-state precondition, current/history result, freshness/qualification result, accounting result, Product/projection boundary, and evidence path. Mark PASS only with cited normative support.

- [ ] **Step 2: Close FL-S1..FL-S6 and FF-01..FF-10.** All numeric/accounting/fingerprint/unavailable-member fixtures must have exact expected outcomes.

- [ ] **Step 3: Close backward compatibility.** Verify RF/CQ IDs, CQ lifecycle/dispositions, TE families, seven Session Intents, three capabilities, single-Project mode, Product mode, `CHANGE_REVIEW`, `REVALIDATE`, `EXTEND`, projection lifecycle, explicit regeneration, legacy preservation, and no automatic advancement.

- [ ] **Step 4: Verify TE boundary.** TE-owned `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` remain outside RF/CQ lifecycle normalization.

- [ ] **Step 5: Run static counts.** Run:
  ```bash
  test "$(rg -c '^\| FL-(0[1-9]|1[0-9]|2[0-9]|30) \|.*PASS' tests/finding-lifecycle-progress-reporting-validation.md)" -eq 30
  test "$(rg -c '^\| FL-S[1-6] \|.*PASS' tests/finding-lifecycle-progress-reporting-validation.md)" -eq 6
  test "$(rg -c '^\| FF-(0[1-9]|10) \|.*PASS' tests/finding-lifecycle-progress-reporting-validation.md)" -eq 10
  rg -n '^\| BC[0-9]+ \|.*PASS' tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  ```
  Expected: 30 FL PASS, 6 safety PASS, 10 fail-first fixtures now PASS, and every compatibility row PASS.

- [ ] **Step 6: Run authority/YAGNI hygiene.** Run:
  ```bash
  git diff --check
  rg -n 'Finding Management capability|Progress capability|Risk capability|Product.*finding authority|FindingEvent|automatic.*baseline|automatic.*projection' references docs/reference capabilities tests/finding-lifecycle-progress-reporting-validation.md tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  ```
  Expected: matches, if any, are only explicit prohibitions or pre-existing legitimate terms; no new authority/framework is introduced.

**Commit 4:**
```bash
git add references/ownership-and-scenarios.md \
        references/projection-impact.md \
        references/projection-regeneration.md \
        docs/reference/outputs.md \
        tests/finding-lifecycle-progress-reporting-validation.md \
        tests/finding-lifecycle-progress-reporting-backward-compatibility.md
git commit -m "test: close finding lifecycle progress compatibility"
```

---

### Task 8: Final verification and handoff

**Files:**
- Test only: all files in Planned File Map plus approved design and this plan.

**Interfaces:**
- Consumes: Tasks 1–7.
- Produces: implementation handoff only; no new architecture decision and normally no new commit.

- [ ] **Step 1: Verify all eight tasks remain present.** Run:
  ```bash
  test "$(rg -c '^### Task [1-8]:' docs/superpowers/plans/2026-09-16-finding-lifecycle-progress-reporting-implementation-plan.md)" -eq 8
  ```

- [ ] **Step 2: Run placeholder scan.** Run:
  ```bash
  ! rg -n -i '[T]BD|T[O]DO|fill in|implement later|handle edge cases|as needed|relevant files' docs/superpowers/plans/2026-09-16-finding-lifecycle-progress-reporting-implementation-plan.md
  ```

- [ ] **Step 3: Run final scenario counts and diff hygiene.** Re-run Task 7 Step 5 and `git diff --check`.

- [ ] **Step 4: Verify changed-file allowlist.** From the implementation base SHA, run:
  ```bash
  BASE_SHA=<implementation-base-sha>
  git diff --name-only "$BASE_SHA"..HEAD | sort > /tmp/finding-lifecycle-actual-files.txt
  cat > /tmp/finding-lifecycle-allowed-files.txt <<'EOF'
  docs/reference/artifacts.md
  docs/reference/identifiers-and-statuses.md
  docs/reference/outputs.md
  references/evidence-and-severity.md
  references/ownership-and-scenarios.md
  references/product-multi-project-review.md
  references/projection-impact.md
  references/projection-regeneration.md
  references/report-contract.md
  references/revalidation-and-freshness.md
  tests/finding-lifecycle-progress-reporting-backward-compatibility.md
  tests/finding-lifecycle-progress-reporting-validation.md
  EOF
  sort -o /tmp/finding-lifecycle-allowed-files.txt /tmp/finding-lifecycle-allowed-files.txt
  diff -u /tmp/finding-lifecycle-allowed-files.txt /tmp/finding-lifecycle-actual-files.txt
  ```
  Expected: no diff. The implementation changes exactly the 12 files in Planned File Map and no unrelated file.

- [ ] **Step 5: Verify immutable boundaries.** Run:
  ```bash
  git diff "$BASE_SHA"..HEAD -- SKILL.md \
    capabilities/code-quality-review/references/code-quality-lifecycle.md \
    capabilities/test-review/SKILL.md \
    references/review-modes-and-orchestration.md \
    references/projection-lifecycle.md
  ```
  Expected: empty diff.

- [ ] **Step 6: Verify commit shape.** Run:
  ```bash
  git log --oneline "$BASE_SHA"..HEAD
  ```
  Expected: four bounded semantic commits corresponding to Tasks 1–2, 3–4, 5, and 6–7. Task 8 creates no commit unless verification itself uncovers and fixes a real plan-covered defect.

- [ ] **Step 7: Produce implementation report.** Record base SHA, four commit SHAs, exact changed files, all validation counts, limitations, and final status. Do not claim completion unless every check above passes.

---

## Implementation Review Gates

Use four gates only; do not start a review loop after every task.

1. **Gate 1 — after Commit 1:** RF lifecycle/disposition authority + fail-first fixtures.
2. **Gate 2 — after Commit 2:** Current/history/progress, stale active/resolved, BLOCKED dimension separation, accepted-risk accounting, legacy qualification.
3. **Gate 3 — after Commit 3:** Product qualification, deterministic `CFV-1`, bottom-up semantic advancement.
4. **Gate 4 — final:** Change Review/projection/reporting + all scenario/compatibility/allowlist checks.

A gate checks the implemented slice. It does not reopen approved design unless implementation evidence exposes a genuine contradiction.

---

## Final Verification Matrix

| Requirement | Evidence | Task(s) | Expected result |
|---|---|---:|---|
| RF lifecycle authority | lifecycle validation + RF ledger contract | 1,2,7 | Architecture alone accepts RF lifecycle/revision transitions |
| CQ compatibility | backward-compatibility matrix | 2,7 | Existing CQ lifecycle/dispositions unchanged |
| Accepted risk accounting | FF-03 / FL-S3 | 1,3,7 | Current unchanged; resolved/new zero; actionable/residual split changes |
| `remediation_status=BLOCKED` | FF-04 / FL-S4 | 1,3,7 | Active risk remains; no resolution/acceptance inference |
| `freshness=BLOCKED` | Current Findings rows | 3,7 | visible with evidence limitation; not verified-current |
| Stale ACTIVE | FF-02 / FL-S2 | 1,3,7 | remains visible with revalidation limitation |
| Stale RESOLVED | FF-01 / FL-S1 | 1,3,7 | old resolution historical; new absence unverified; no synthetic ACTIVE |
| Legacy weak evidence | FF-10 / FL-S5 | 1,4,7 | no automatic resolution; owner adjudication required |
| Reopen | FL-07/FL-28 | 2,3,7 | same identity gets newer ACTIVE revision; derived REOPENED |
| Severity movement | FF-05 / FL-08/09 | 1,3,7 | no delete+create accounting |
| Supersession | FF-06 / FL-18 | 1,3,7 | current decreases; resolved remains zero |
| Product unavailable member | FF-07 / FL-22 | 1,5,7 | limited/unknown, never zero/unchanged |
| Bottom-up semantic advancement | FF-08 / FL-12/13/23/24 | 1,5,7 | child advances; accepted Product baseline does not |
| `CFV-1` determinism | FF-09 / FL-S6 | 1,5,7 | SHA-256 canonical JSON; presentation/path invariant; semantic changes alter digest |
| Cross-member identity | Product fixture | 5,7 | Project A RF-001 != Project B RF-001 |
| Change Review | FL-14/15 | 2,6,7 | candidate potential never mutates accepted lifecycle |
| Projection freshness | FL-16/17 | 6,7 | authority first; regeneration explicit |
| Single Project | compatibility matrix | 7 | reports current/history/progress without Product |
| TE boundary | compatibility matrix | 7 | TE families keep own semantics |
| Changed-file scope | Task 8 allowlist | 8 | exactly 12 planned implementation files |
| Authority/YAGNI | hygiene checks | 7,8 | no new intent/capability/authority/runtime framework |

---

## Definition of Done

Implementation is complete only when:

1. all `FF-01..FF-10`, `FL-01..FL-30`, and `FL-S1..FL-S6` fixtures are PASS;
2. every backward-compatibility row is PASS;
3. accepted-risk accounting, PB accounting, supersession, unavailable-member, bottom-up advancement, and fingerprint fixtures match exact expected results;
4. `freshness=BLOCKED` and `remediation_status=BLOCKED` are unambiguously separate;
5. `CFV-1` uses SHA-256 over exact canonical UTF-8 NFC-normalized JSON and serializes as `sha256:<64 lowercase hex>`;
6. Product remains composition-only and accepted Product baselines never auto-advance;
7. the implementation changes exactly the 12 allowlisted files;
8. the five immutable validation-input contracts remain unchanged;
9. `git diff --check` passes;
10. exactly four bounded semantic implementation commits exist unless a documented plan-covered fix required one additional corrective commit;
11. no new runtime harness/framework/authority/capability/intent is introduced.

After this plan is implemented, proceed to one final implementation review of the resulting diff and validation evidence. Do not start another design/plan review cycle unless implementation exposes a genuine architecture contradiction.
