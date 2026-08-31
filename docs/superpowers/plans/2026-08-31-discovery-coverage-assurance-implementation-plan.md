# Discovery Coverage Assurance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an evidence-backed Discovery Coverage Assurance gate so `STANDARD_FULL` and `FORENSIC` reviews cannot infer completeness from finding count and cannot advance to candidate verification until material mechanism classes have accepted coverage evidence.

**Architecture:** Introduce one authoritative `references/discovery-coverage.md` contract, wire it into the existing review flow, orchestration state, and completion gates, and validate it with fail-first pressure scenarios. Preserve the existing candidate lifecycle: coverage review detects missing investigation classes; independent verification checks existing candidates; root/severity adjudication remain downstream and unchanged in role.

**Tech Stack:** Markdown-based ChatGPT Skill, Git/GitHub, existing pressure-scenario validation corpus.

**Spec:** `docs/superpowers/specs/2026-08-31-discovery-coverage-assurance-design.md`

## Global Constraints

- Target baseline is `main@fd7466a33362d04d964cb847d33c5a1e022ba48b`; implementation must begin from a fresh branch/worktree based on the then-current verified `main`, and stop if `main` has materially changed in overlapping contracts.
- Keep `SKILL.md` orchestration-oriented; normative Discovery Coverage semantics live in `references/discovery-coverage.md`.
- Both `STANDARD_FULL` and `FORENSIC` must produce a coverage matrix; `FORENSIC` requires explicit Independent Coverage Review before candidate verification.
- `DISCOVERY_COMPLETE` alone is insufficient; downstream candidate verification requires `COVERAGE_ACCEPTED`.
- `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, and `COVERAGE_AUTHORITY_DRIFT` are not accepted downstream states.
- `NOT_APPLICABLE` requires evidence-based justification.
- Finding count is never evidence of completeness; zero findings remains valid when coverage evidence is sufficient.
- Search/grep is inventory evidence, not semantic proof.
- High-risk domains require source/boundary/effect or equivalent semantic traces, not generic claims such as `security reviewed`.
- Candidate verification, root-boundary adjudication, and severity adjudication keep their existing roles and must not absorb Coverage Review responsibilities.
- Safe Reproduction / Evidence Validation is optional, authorized, non-destructive, minimal, and must not turn the public Skill into an exploitation playbook.
- No production code in audited repositories is modified by this Skill.
- No merge, tag, release, or publication to `main` is part of this plan.

---

## File Structure

**Create**
- `references/discovery-coverage.md` — sole normative contract for matrix schema, domain taxonomy, high-risk proof-of-coverage, Independent Coverage Review, correction/re-review, and coverage completion semantics.
- `tests/pressure-scenarios-45-53-discovery-coverage.md` — pressure scenarios PS-45 through PS-53, preserving the known RED baseline and adding cross-domain completeness/precision cases.

**Modify**
- `SKILL.md` — insert coverage gate into Required Review Flow, Non-Negotiable Gates, Authority Map, and Completion Gate.
- `references/review-method.md` — make thematic discovery coverage-driven and source/boundary/effect oriented.
- `references/review-modes-and-orchestration.md` — add coverage artifacts, INDEX projection, review/correction lifecycle, resume/revalidation semantics.
- `references/boundary-contract-audit.md` — broaden boundary language beyond IPC/process to interpreter/resource/authority boundaries without duplicating the new reference.
- `references/evidence-and-severity.md` — add narrowly scoped Safe Reproduction / Evidence Validation semantics while preserving attack-chain/severity separation.
- `references/final-editorial-review.md` — require status consistency with coverage acceptance, without making editorial review a technical re-audit.
- `tests/pressure-validation-matrix.md` — record RED/GREEN evidence and regression status for PS-45 through PS-53.

---

### Task 1: Persist the failing Discovery Coverage baseline

**Files:**
- Create: `tests/pressure-scenarios-45-53-discovery-coverage.md`
- Modify: `tests/pressure-validation-matrix.md`

**Interfaces:**
- Consumes: known production baseline `PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED` from the current installed Skill.
- Produces: stable PS-45 test contract and a validation-matrix row that future implementation must turn GREEN without changing the scenario to fit the fix.

- [ ] **Step 1: Write PS-45 as the immutable RED scenario**

Record the synthetic A–E sites exactly at the semantic level already validated:

```text
A: direct HTTP input -> f-string -> WhereRaw -> reachable boolean SQL effect
B: persisted value -> WhereRaw -> second-order provenance unresolved
C: hardcoded constant -> WhereRaw -> non-finding
D: finite allowlisted input -> OrderByRaw -> safe based on supplied evidence
E: f-string value -> structured ORM ilike() -> not raw SQL
```

Expected baseline verdict:

```text
PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED
```

The scenario must explicitly fail a Skill that can correctly adjudicate A–E after being shown them but lacks a systematic discovery mechanism for the class.

- [ ] **Step 2: Add the baseline evidence row to `tests/pressure-validation-matrix.md`**

Add fields consistent with the existing matrix style:

```text
PS-45
baseline: main@fd7466a33362d04d964cb847d33c5a1e022ba48b
baseline_result: RED
verdict: PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED
failure_boundary: thematic discovery
not_failing: independent verification; root adjudication; severity; final editorial
```

- [ ] **Step 3: Review the scenario for overfitting**

Confirm the pass condition is not `mentions WhereRaw` or `mentions SQL injection`; it must require a systematic interpreter/dynamic-construction source→sink coverage mechanism plus false-positive resistance.

- [ ] **Step 4: Commit**

```bash
git add tests/pressure-scenarios-45-53-discovery-coverage.md tests/pressure-validation-matrix.md
git commit -m "test: record discovery coverage RED baseline"
```

---

### Task 2: Add the authoritative Discovery Coverage contract

**Files:**
- Create: `references/discovery-coverage.md`

**Interfaces:**
- Consumes: approved design spec and existing evidence-first lifecycle terminology.
- Produces: authoritative definitions used by `SKILL.md`, orchestration, review method, and tests.

- [ ] **Step 1: Write the matrix contract**

Define the row schema exactly:

```text
domain
applicability
coverage_status
evidence_refs
inventory_summary
candidate_ids
positive_controls
open_questions
limitations
```

Applicability:

```text
YES | NO | CONDITIONAL
```

Coverage state:

```text
PENDING | IN_PROGRESS | COVERED | PARTIALLY_COVERED | BLOCKED | NOT_APPLICABLE
```

State invariants:

```text
PARTIALLY_COVERED != COMPLETE
BLOCKED != COMPLETE
NOT_APPLICABLE requires evidence-based reason
```

- [ ] **Step 2: Define all canonical coverage domains**

Include all 21 approved domains:

```text
ARCH-01 Architecture / responsibility
ARCH-02 Ownership / isolation / concurrency
ARCH-03 Lifecycle / cleanup / recovery
ARCH-04 Boundary contracts / IPC / API / process
SEC-01 Authentication / authorization / identity / scope
SEC-02 Interpreter / dynamic construction
SEC-03 Resource addressing / filesystem / paths
SEC-04 Outbound network target control
SEC-05 Parsing / deserialization / content handling
SEC-06 Secrets / sensitive-data propagation
SEC-07 Privilege / capability boundaries
DATA-01 Persistence / migrations / integrity
REL-01 Errors / fallback / fail-open behavior
REL-02 Availability / amplification / resource exhaustion
REL-03 Business abuse / replay / ordering / idempotency
OPS-01 Configuration / deployment assumptions
OPS-02 Supply chain / dynamic loading / update path
OPS-03 Observability / logging / privacy
COMP-01 Cross-version / legacy / compatibility surfaces
QUAL-01 Performance / blocking / queue/cache pressure
QUAL-02 Tests / testability / evidence quality
```

- [ ] **Step 3: Write high-risk proof-of-coverage contracts**

Include explicit minimum traces for:

```text
SEC-01 authorization + session/token lifecycle
SEC-02 interpreter/dynamic construction
SEC-03 resource addressing
SEC-04 outbound target control
SEC-05 parsing/deserialization
SEC-06 sensitive-data propagation
SEC-07 privilege/capabilities
REL-02 availability/amplification
REL-03 replay/order/idempotency
COMP-01 version/legacy projection
```

For `SEC-02`, preserve the source classification:

```text
direct untrusted
validated / allowlisted
hardcoded constant
persisted / second-order
unresolved provenance
```

- [ ] **Step 4: Add conditional crypto and supply-chain semantics**

State that crypto/signature/TLS mechanisms are reviewed under relevant domains when present, not as a mandatory standalone checklist. `OPS-02` depth is applicability-driven and may be evidence-backed `NOT_APPLICABLE`.

- [ ] **Step 5: Define Independent Coverage Review**

Require three bounded passes:

```text
As-Built reconciliation
→ evidence-quality challenge
→ bounded blind-spot probes
```

Verdicts:

```text
COVERAGE_ACCEPTED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
```

Explicitly state that Coverage Review does not assign severity and does not create final RF directly.

- [ ] **Step 6: Define targeted correction and freshness behavior**

Use:

```text
COVERAGE_CORRECTION_REQUIRED
→ targeted thematic pass
→ matrix update
→ impacted-domain re-review
→ COVERAGE_ACCEPTED | BLOCKED
```

If As-Built changes, require a coverage impact scan and revalidate only affected domains under the existing freshness contract.

- [ ] **Step 7: Commit**

```bash
git add references/discovery-coverage.md
git commit -m "feat: define discovery coverage assurance contract"
```

---

### Task 3: Wire coverage into the Skill and thematic discovery

**Files:**
- Modify: `SKILL.md`
- Modify: `references/review-method.md`
- Modify: `references/boundary-contract-audit.md`

**Interfaces:**
- Consumes: `references/discovery-coverage.md` as sole normative coverage authority.
- Produces: an orchestration path that actually invokes the new contract during normal review execution.

- [ ] **Step 1: Update `SKILL.md` Required Review Flow**

Change the discovery transition to:

```text
accepted As-Built
→ thematic discovery
→ Discovery Coverage Matrix closeout
→ Independent Coverage Review
→ COVERAGE_ACCEPTED
→ independent candidate verification
```

Do not duplicate the 21-domain taxonomy in `SKILL.md`.

- [ ] **Step 2: Add Non-Negotiable coverage gates**

Add rules equivalent to:

```text
finding count is not evidence of completeness
DISCOVERY_COMPLETE without COVERAGE_ACCEPTED is not accepted downstream input
coverage gaps trigger targeted correction, not automatic full-audit restart
```

- [ ] **Step 3: Add `discovery-coverage.md` to Authority Map and Completion Gate**

Completion must reject ordinary `REVIEW_COMPLETE` when material coverage remains partial, blocked, correction-required, or authority-drifted.

- [ ] **Step 4: Update `references/review-method.md`**

Require thematic discovery to update coverage evidence and state that security-sensitive discovery is source/boundary/effect oriented. Preserve existing attack-chain promotion semantics by referencing, not duplicating, `evidence-and-severity.md`.

- [ ] **Step 5: Broaden `references/boundary-contract-audit.md` terminology**

Add an explicit distinction such as:

```text
interaction boundaries
interpreter boundaries
resource-addressing boundaries
authority/capability boundaries
```

Keep detailed matrix/proof semantics delegated to `discovery-coverage.md`.

- [ ] **Step 6: Static contract check**

Search the changed files and confirm:

```text
COVERAGE_ACCEPTED
references/discovery-coverage.md
Independent Coverage Review
```

appear where required, and the full taxonomy appears only in its authoritative reference/spec/tests rather than being redundantly normative in multiple files.

- [ ] **Step 7: Commit**

```bash
git add SKILL.md references/review-method.md references/boundary-contract-audit.md
git commit -m "feat: gate discovery on accepted coverage"
```

---

### Task 4: Add coverage lifecycle to persistent orchestration

**Files:**
- Modify: `references/review-modes-and-orchestration.md`

**Interfaces:**
- Consumes: coverage verdict/state definitions from `references/discovery-coverage.md`.
- Produces: deterministic artifact layout, INDEX projection, resume, correction, and revalidation rules.

- [ ] **Step 1: Add STANDARD_FULL working artifacts**

Document:

```text
01-discovery-and-scenarios.md
01a-discovery-coverage-matrix.md
01b-independent-coverage-review.md
01c-coverage-correction.md       # conditional
01d-coverage-re-review.md        # conditional
02-independent-verification.md
```

- [ ] **Step 2: Add FORENSIC working artifacts**

Document:

```text
06a-discovery-coverage-matrix.md
06b-independent-coverage-review.md
06c-coverage-correction.md       # conditional
06d-coverage-re-review.md        # conditional
07-independent-verification.md
```

Preserve semantic ordering if numbering must adapt to existing files.

- [ ] **Step 3: Add compact `INDEX.md` coverage projection**

Define fields:

```text
coverage_artifact
coverage_review
baseline
domains.total
domains.covered
domains.not_applicable
domains.partial
domains.blocked
high_risk.applicable
high_risk.accepted
```

The full matrix remains owned by its working artifact.

- [ ] **Step 4: Add workflow transition rules**

Require:

```text
DISCOVERY_COMPLETE + COVERAGE_ACCEPTED
```

before candidate verification. Define correction/re-review as targeted stages and state that `COVERAGE_BLOCKED` or `COVERAGE_AUTHORITY_DRIFT` cannot be projected as complete.

- [ ] **Step 5: Add resume and revalidation semantics**

On resume, validate matrix/review baseline binding before trusting INDEX projection. On As-Built correction, perform domain impact scan rather than resetting unrelated accepted domains.

- [ ] **Step 6: Commit**

```bash
git add references/review-modes-and-orchestration.md
git commit -m "feat: persist discovery coverage workflow state"
```

---

### Task 5: Add Safe Reproduction / Evidence Validation without offensive expansion

**Files:**
- Modify: `references/evidence-and-severity.md`

**Interfaces:**
- Consumes: existing Observation/Interpretation/Risk evidence contract and independent verification lifecycle.
- Produces: optional runtime-evidence semantics that improve confidence without authorizing exploitation.

- [ ] **Step 1: Add a Safe Reproduction subsection**

Specify:

```text
optional, not mandatory
prefer existing tests/local fixtures/isolated test environments/synthetic input
authorized systems only
minimum effect necessary
no destructive actions
no persistence
no privilege escalation
no credential theft
no lateral movement
no data exfiltration
no unrelated external probing
no reusable offensive payload packs
```

- [ ] **Step 2: Define evidence labels/wording expectations**

Require reviewers to distinguish:

```text
STATICALLY_CONFIRMED
RUNTIME_REPRODUCED
RUNTIME_VALIDATION_UNAVAILABLE
```

These are evidence descriptions, not new severity levels or candidate lifecycle states. If equivalent existing terminology is already normative, reuse it instead of inventing parallel status tokens.

- [ ] **Step 3: Preserve severity separation**

State explicitly that successful reproduction can increase confidence/reachability evidence but does not bypass independent verification/root adjudication or automatically raise severity.

- [ ] **Step 4: Add injection example at a safe abstraction level**

Use only a principle-level example:

```text
prove harmless local/test boolean predicate manipulation or construction semantics;
do not extract data or chain privileges merely to demonstrate impact
```

Do not include reusable exploit payload collections.

- [ ] **Step 5: Commit**

```bash
git add references/evidence-and-severity.md
git commit -m "feat: define safe runtime evidence validation"
```

---

### Task 6: Keep editorial review status-consistent but non-technical

**Files:**
- Modify: `references/final-editorial-review.md`

**Interfaces:**
- Consumes: accepted coverage verdict from orchestration.
- Produces: final-package status consistency without reopening technical discovery.

- [ ] **Step 1: Add coverage-status consistency check**

Editorial review must verify that a package does not claim `REVIEW_COMPLETE` while coverage is non-accepted.

- [ ] **Step 2: Preserve the non-re-audit boundary**

Add explicit wording that Final Editorial Review does not independently search for missing technical vulnerability classes; that responsibility belongs to Independent Coverage Review.

- [ ] **Step 3: Commit**

```bash
git add references/final-editorial-review.md
git commit -m "docs: align final gate with coverage acceptance"
```

---

### Task 7: Add cross-domain RED/GREEN pressure scenarios

**Files:**
- Modify: `tests/pressure-scenarios-45-53-discovery-coverage.md`
- Modify: `tests/pressure-validation-matrix.md`

**Interfaces:**
- Consumes: new coverage contract.
- Produces: regression suite proving completeness gains without precision collapse.

- [ ] **Step 1: Add PS-46 Authorization Completeness**

Scenario must include protected point access plus a list/bulk scope omission and alternate token path. Add an auth/session lifecycle variant when issuance/refresh/revocation exists. Pass requires object/scope semantics, not merely middleware detection.

- [ ] **Step 2: Add PS-47 Outbound Target Control**

Mix static endpoints with one user-configurable target and redirect/proxy behavior. Pass requires provenance-to-network-zone trace; do not label every HTTP client SSRF.

- [ ] **Step 3: Add PS-48 Cross-Version Projection**

Place the same root mechanism across current, legacy/base, and compatibility paths. Pass requires projection search and root grouping rather than duplicate RF inflation.

- [ ] **Step 4: Add PS-49 Secrets Propagation**

Secret storage is correct, but an error/trace/log path propagates sensitive material. Pass requires source-to-export trace, not only secret-at-rest inspection.

- [ ] **Step 5: Add PS-50 Business Replay / Ordering**

Retry/replay causes duplicate durable business effect. Pass requires identity/idempotency/ordering/authoritative-state trace.

- [ ] **Step 6: Add PS-51 False-Positive Resistance**

Include many raw-looking sites:

```text
mostly constants
validated allowlists
structured ORM values
one direct unsafe sink
one unresolved persisted/second-order source
```

Pass requires exactly differentiated classifications, not `Raw == vulnerability`.

- [ ] **Step 7: Add PS-52 Availability / Amplification**

Include request-driven fan-out/unbounded work among ordinary performance code. Pass requires amplification/bounding/service-impact analysis and rejects generic `slow == security issue` reasoning.

- [ ] **Step 8: Add PS-53 Conditional Crypto / Transport**

One case contains real token/signature/TLS semantics and must be reviewed under relevant domains; control case has no such mechanism and must not invent crypto findings.

- [ ] **Step 9: Run fresh pressure validation**

Execute PS-45 through PS-53 with the modified Skill in fresh contexts. Record for each:

```text
baseline ref
candidate ref
model/runtime
verdict
failure or pass boundary
false-positive notes
```

PS-45 must change from RED to GREEN due to the systematic coverage contract, not because the scenario was edited to name the required fix.

- [ ] **Step 10: Commit**

```bash
git add tests/pressure-scenarios-45-53-discovery-coverage.md tests/pressure-validation-matrix.md
git commit -m "test: validate discovery coverage assurance"
```

---

### Task 8: Full contract regression and completion verification

**Files:**
- Modify only if a regression is found: files already listed above.

**Interfaces:**
- Consumes: all implementation tasks.
- Produces: evidence that the new gate does not break current orchestration, report, freshness, diagram, severity, or language contracts.

- [ ] **Step 1: Re-run prior pressure families**

At minimum revalidate existing scenarios covering:

```text
native plan projection
final report quality
Mermaid/prose quality
context orchestration/freshness
```

Use the repository's existing pressure-scenario documents as the canonical prompts/expectations.

- [ ] **Step 2: Perform authority duplication review**

Verify normative ownership remains:

```text
discovery coverage semantics -> discovery-coverage.md
workflow state/artifacts -> review-modes-and-orchestration.md
candidate verification -> independent-verification.md
severity/attack chain -> evidence-and-severity.md
editorial -> final-editorial-review.md
```

- [ ] **Step 3: Perform completion-gate simulation**

Validate these states:

```text
DISCOVERY_COMPLETE + COVERAGE_CORRECTION_REQUIRED -> cannot verify candidates
DISCOVERY_COMPLETE + COVERAGE_BLOCKED -> REVIEW_PARTIALLY_COMPLETE / blocked exact gate
DISCOVERY_COMPLETE + COVERAGE_ACCEPTED -> candidate verification allowed
accepted coverage + later impacted As-Built correction -> affected domains revalidation only
```

- [ ] **Step 4: Verify safe-reproduction boundary**

Confirm no new reference or pressure scenario contains instructions for destructive exploitation, credential theft, persistence, privilege escalation, lateral movement, exfiltration, or probing unrelated external targets.

- [ ] **Step 5: Review diff against the approved spec**

Every design acceptance criterion 1–22 must map to an implemented contract or pressure scenario. Record any intentionally deferred item; if any spec criterion is unimplemented, do not claim completion.

- [ ] **Step 6: Final branch verification**

Run:

```bash
git status --short
git log --oneline --decorate -12
git diff --check <verified-main>..HEAD
```

Expected:

```text
clean working tree
git diff --check: no output
```

Also compare changed filenames against the planned file set. Unexpected production/runtime files are a STOP condition.

- [ ] **Step 7: Commit any verification-only matrix updates**

```bash
git add tests/pressure-validation-matrix.md
git commit -m "test: record discovery coverage regression results"
```

Only commit if the matrix actually changed.

---

## Plan Completion Gate

Implementation is ready for independent review only when all are true:

```text
PS-45 GREEN
PS-46..PS-53 validated
existing pressure families remain accepted or explicitly adjudicated
both review modes have coverage matrix semantics
FORENSIC has explicit Independent Coverage Review gate
candidate verification cannot consume non-accepted coverage
Safe Reproduction boundary is non-offensive and optional
no severity/root/editorial role drift
diff-check clean
working tree clean
```

Do not merge, tag, release, or update the public `main` as part of execution. Stop after implementation and verification for an independent code/Skill review gate.
