# Finding Lifecycle & Progress Reporting — Contract Validation

This is a bounded Markdown contract artifact. It is not a runtime test harness,
semantic ledger, Product authority, or projection generator.

## Scope and evidence rules

The accepted design is:
`docs/superpowers/specs/2026-09-16-finding-lifecycle-progress-reporting-design.md`.
Each fixture has a precondition, accepted owner state, source/baseline,
expected derived view, expected accounting, forbidden outcome, evidence path,
and status. A keyword match alone is insufficient; PASS requires the cited
normative clause to express every required outcome.

## Fail-first evidence

Executed before normative contract changes on implementation base
`ffd9fe969340dd4566f2b503979d7f9f908a5c98`:

| Probe | Command | Expected pre-change result | Observed |
|---|---|---:|---:|
| RF owner | `rg -n 'Architecture RF Lifecycle Ownership' references/report-contract.md` | 1 | 1 |
| stale resolution | `rg -n 'RESOLUTION_REVALIDATION_REQUIRED' references/revalidation-and-freshness.md` | 1 | 1 |
| CFV schema | `rg -n 'CFV-1' references/product-multi-project-review.md` | 1 | 1 |
| digest form | `rg -n 'sha256:' references/product-multi-project-review.md` | 1 | 1 |

The four status-1 results are genuine pre-change failures: the required
normative terms were absent from the owning contracts. No FF or FL row was
marked PASS during this phase.

## Fail-first fixtures

| ID | Preconditions / accepted owner state | Source / baseline | Expected derived view | Expected accounting | Forbidden outcome | Evidence path | Status |
|---|---|---|---|---|---|---|---|
| FF-01 | RF-001 HIGH, lifecycle RESOLVED, freshness CURRENT | Resolved on B; dependency advances to C; no revalidation | Historical resolved-on-B plus `RESOLUTION_REVALIDATION_REQUIRED` on C | No verified-resolved credit on C | No synthetic ACTIVE and no verified absence | report-contract §4; freshness resolution-binding clause | PASS |
| FF-02 | RF-002 HIGH, lifecycle ACTIVE, freshness CURRENT | Binding advances B→C; no revalidation | ACTIVE remains visible; freshness STALE or qualified BLOCKED; not verified-current | Current stock retained | Silent disappearance or definite C applicability | report-contract Current Findings; freshness advancement clause | PASS |
| FF-03 | RF-003 HIGH ACTIVE, disposition changes ACTION_REQUIRED→ACCEPTED_RISK | PB-1→PB-2 | Current 1→1; accepted residual risk shown | NEW 0; RESOLVED 0; ACCEPTED_RISK_ADDED 1; actionable 1→0; residual 0→1 | Accepted risk treated as RESOLVED or removed from technical risk | report-contract disposition/accounting; FF-03 fixture | PASS |
| FF-04 | RF-004 HIGH ACTIVE, freshness=CURRENT, remediation_status=BLOCKED | One accepted baseline | Included in Current Findings; remediation blocked label | RESOLVED NO; ACCEPTED_RISK NO absent independent disposition | `ACTIVE_BLOCKED` lifecycle or freshness/remediation collapse | identifiers/artifacts dimension table; FF-04 fixture | PASS |
| FF-05 | RF-001/2/3 as specified below | PB-1→PB-2 | Current 3→3 | historical identities 4; NEW 1; RESOLVED 1; severity decreased 1; HIGH 2→1; MEDIUM 1→2 | Delete+create severity transition or double counting | report-contract progress/accounting; FF-05 fixture | PASS |
| FF-06 | RF-001 and RF-002 MEDIUM ACTIVE; RF-002 later superseded by RF-001 | PB-1→PB-2 | Replacement current; old identity historical superseded | Current 2→1; RESOLVED 0; SUPERSEDED 1; history 2 | Supersession receives resolution credit | report-contract supersession/accounting; FF-06 fixture | PASS |
| FF-07 | Product PB-N includes Project C; C cannot qualify at PB-N+1 | Exact Product member vector | LIMITED/UNKNOWN aggregate with mandatory member limitation | C contributes no zero stock or transitions | C reported as zero or UNCHANGED | product contract availability; FF-07 fixture | PASS |
| FF-08 | PB-10 pins child RF-017 owner rev5; child accepts ACTIVE→RESOLVED rev6 | Same exact source | Child authority advances; PB-10 unchanged; Product revalidation required | PB-11 only after Product Baseline Acceptance | Automatic Product baseline advancement | product bottom-up clause; FF-08 fixture | PASS |
| FF-09 | Same qualified semantic rows, then presentation and semantic mutations | Same Product baseline context | Same fingerprint for wording/order/path; changed fingerprint for semantic changes | SHA-256 canonical payload only | Path/Markdown changes mutate digest, or semantic changes do not | product CFV-1 clause; FF-09 fixture | PASS |
| FF-10 | Stable RF ID and evidence; report says “fixed”; no accepted owner resolution | Legacy package | `LEGACY_STATUS_UNKNOWN`, owner adjudication required | Excluded from definitive counts and verified-current | Automatic RESOLVED, ACTIVE default, zero, or verified resolved | report-contract legacy clause; FF-10 fixture | PASS |

## Exact accounting fixtures

### FF-03 / accepted risk

```text
PB-1: RF-003 HIGH ACTIVE disposition=ACTION_REQUIRED
PB-2: RF-003 HIGH ACTIVE disposition=ACCEPTED_RISK
Current: 1 -> 1
NEW: 0
RESOLVED: 0
ACCEPTED_RISK_ADDED: 1
Actionable: 1 -> 0
Residual accepted risk: 0 -> 1
identity: unchanged
```

### FF-05 / PB accounting

```text
PB-1: RF-001 HIGH ACTIVE; RF-002 HIGH ACTIVE; RF-003 MEDIUM ACTIVE
PB-2: RF-001 RESOLVED; RF-002 MEDIUM ACTIVE; RF-003 MEDIUM ACTIVE; RF-004 HIGH ACTIVE
historical identities: 4
current: 3 -> 3
NEW: 1
RESOLVED: 1
SEVERITY_DECREASED: 1
HIGH: 2 -> 1
MEDIUM: 1 -> 2
```

### FF-06 / supersession

```text
PB-1: RF-001 MEDIUM ACTIVE; RF-002 MEDIUM ACTIVE
PB-2: RF-001 MEDIUM ACTIVE; RF-002 SUPERSEDED_BY RF-001
current: 2 -> 1
RESOLVED: 0
SUPERSEDED: 1
historical identities: 2
```

## FL-01..FL-30 pressure matrix

| ID | Required assertion | Expected result | Forbidden outcome | Evidence | Status |
|---|---|---|---|---|---|
| FL-01 | ACTIVE→RESOLVED | Owner evidence, revalidation, adjudication, accepted revision | Remediation/prose alone resolves | RF owner + resolution gate | PASS |
| FL-02 | Resolved history | Identity, revision, evidence remain addressable | Delete history | Historical view | PASS |
| FL-03 | Resolved current exclusion | RESOLVED+CURRENT excluded from current stock | Count as active | Current predicate | PASS |
| FL-04 | ACTIVE→SUPERSEDED | Qualified replacement and owner revision | Product/prose supersedes | Supersession clause | PASS |
| FL-05 | Superseded accounting | Separate superseded flow, no resolved credit | Claim technical resolution | Accounting invariants | PASS |
| FL-06 | Accepted risk | Active technical risk, separate treatment | Resolve/remove from current | Disposition clause | PASS |
| FL-07 | Recurrence | Same ID, newer ACTIVE revision, derived REOPENED | Persist REOPENED lifecycle | Reopen clause | PASS |
| FL-08 | HIGH→MEDIUM | Same ID, SEVERITY_DECREASED, lifecycle unchanged | RESOLVED+NEW | Severity clause | PASS |
| FL-09 | MEDIUM→HIGH | Same ID, SEVERITY_INCREASED | NEW finding | Severity clause | PASS |
| FL-10 | New identity | NEW flow at N+1 | Treat as severity change | Progress join | PASS |
| FL-11 | Resolution flow | RESOLVED flow, history retained | Delete record | Progress/history | PASS |
| FL-12 | Child resolves | Product baseline remains old | Auto-advance baseline | Bottom-up clause | PASS |
| FL-13 | Same source authority advancement | Semantic advancement without source advancement | Treat as source change or ignore | Freshness/Product clause | PASS |
| FL-14 | Candidate potential | POTENTIALLY_RESOLVES candidate-only | Mutate accepted state | Change Review clause | PASS |
| FL-15 | Reconciliation | Owner accepts only after reconciliation | Direct CR→RESOLVED | Owner barrier | PASS |
| FL-16 | Stale projection | Projection STALE; authority unchanged | Projection becomes authority | Projection impact | PASS |
| FL-17 | Explicit regeneration | RG/V1–V4 updates presentation only | Automatic regeneration | Regeneration clause | PASS |
| FL-18 | Duplicate collapse | Old SUPERSEDED, replacement counted once | Resolved credit | Supersession clause | PASS |
| FL-19 | History/current divergence | Registered history can grow while current falls | Add history to current | Accounting | PASS |
| FL-20 | Accepted-risk classification | Current unchanged; actionable/residual change | Lifecycle transition | FF-03 | PASS |
| FL-21 | Legacy lifecycle absent | Tiered migration or UNKNOWN | Infer from prose | Legacy clause | PASS |
| FL-22 | Unavailable member | Limitation, not zero/unchanged | False precise total | Product availability | PASS |
| FL-23 | Child revision same source | Semantic authority advancement | Auto Product advance | Bottom-up clause | PASS |
| FL-24 | Baseline reproducibility | Exact qualified bindings and CFV-1 reproduce snapshots | Latest pointer retarget | Product baseline | PASS |
| FL-25 | Similar IDs | Member/project qualification separates rows | Bare-ID merge | Product qualification | PASS |
| FL-26 | Severity table | Included current findings only | Historical severity counts | Current view | PASS |
| FL-27 | Historical table | Resolved/superseded labels retained | Current-only history | Historical view | PASS |
| FL-28 | Reopen statistics | Historical resolved and current active can coexist | Erase resolved history | Reopen clause | PASS |
| FL-29 | Reconciliation | Complete pair reconciles; incomplete pair limited | Force equation | Accounting equation | PASS |
| FL-30 | Incomplete evidence | No RESOLVED; stale/blocked active or unknown | Resolve on absence | Resolution gate | PASS |

## FL-S1..FL-S6 safety matrix

| ID | Scenario | Expected result | Forbidden outcome | Status |
|---|---|---|---|---|
| FL-S1 | Resolved B, source C, no revalidation | Historical B; uncertainty on C; no synthetic ACTIVE | Verified absence on C | PASS |
| FL-S2 | Active B, source C, no revalidation | Visible stale risk and limitation | Silent removal | PASS |
| FL-S3 | ACTION_REQUIRED→ACCEPTED_RISK | Current unchanged; actionable/residual split | Resolution credit | PASS |
| FL-S4 | remediation_status=BLOCKED | ACTIVE current risk, not accepted/resolved | ACTIVE_BLOCKED enum | PASS |
| FL-S5 | Legacy “fixed” prose | UNKNOWN/owner adjudication | Automatic resolution | PASS |
| FL-S6 | Presentation vs semantic CFV changes | Invariant vs changed digest as specified | Volatile metadata in payload | PASS |

## Change Review and projection fixtures

| ID | Input | Expected result | Forbidden outcome | Status |
|---|---|---|---|---|
| FL-CR-01 | Candidate branch reports `POTENTIALLY_RESOLVES` for accepted active RF-017 | Candidate-only effect; accepted RF and Current Findings unchanged | Direct CHANGE_REVIEW→RESOLVED | PASS |
| FL-CR-02 | `RECONCILE_CHANGE` supplies qualified candidate evidence | Architecture owner revalidates/adjudicates before accepted revision | Candidate or Product writes RF lifecycle | PASS |
| FL-PR-01 | Accepted owner revision changes | Dependent projection becomes STALE through impact accounting | Markdown mutates authority | PASS |
| FL-PR-02 | Explicit RG session runs V1–V4 | Projection presentation updates after verification only | Automatic regeneration or Product baseline advancement | PASS |

## Product qualification fixtures

### FF-07 — unavailable member

```text
PB-N includes Project C
PB-N+1 cannot qualify Project C
expected: Product result LIMITED/UNKNOWN for the affected aggregate
Project C contribution: not zero and not UNCHANGED
limitation: mandatory
```

### FF-08 — bottom-up semantic advancement

```text
PB-10 pins child RF-017 owner rev5 / same exact source
child accepts RF-017 ACTIVE -> RESOLVED at owner rev6
expected: child authority advances; PB-10 unchanged; semantic-authority
advancement PRESENT; Product revalidation required; PB-11 only after
Product Baseline Acceptance
```

### FF-09 — CFV-1 canonical payload

```text
schema: CFV-1
product_revision: PROD-EXAMPLE@rev1
product_baseline_key: PB-EXAMPLE
rows: []
canonical bytes: {"schema":"CFV-1","product_revision":"PROD-EXAMPLE@rev1","product_baseline_key":"PB-EXAMPLE","rows":[]}
digest: sha256: computed from the exact canonical UTF-8 bytes
```

The same qualified rows produce the same digest after Markdown wording, row
order, or workspace-path changes. Severity, lifecycle, disposition, relevant
freshness, source binding, accepted owner revision, or qualification changes
produce a different digest. Historical rows are outside the payload.

### Cross-member identity

`Project-A/RF-001` and `Project-B/RF-001` are two qualified rows because
member/project, owner/family, source/baseline, accepted revision, freshness,
and limitations are retained. Bare local IDs are never Product-global.

`FINDING_LIFECYCLE_PROGRESS_VALIDATION_PASS`
