# Manual Agent E2E Validation + README Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build three reproducible manual agent-driven acceptance scenarios (NEW, REVALIDATE + projection regeneration, RESUME), deterministic verification scripts, independent evaluator contracts, and a README refresh that is updated only after named scenarios have actually passed.

**Architecture:** The repository remains a Markdown/Git Skill repository. E2E packs live under `tests/e2e/`; each pack copies a deterministic fixture into an isolated run directory, is executed manually in fresh Codex sessions, is checked by `verify.sh`, and is then reviewed by a separate fresh evaluator session. This work does not add a native coordinator/runtime and does not start Stage C.

**Tech Stack:** Markdown, POSIX shell, Git, small deterministic fixture applications, optional Python 3 only when shell parsing is materially insufficient.

**Spec:** `docs/superpowers/specs/2026-09-05-manual-agent-e2e-validation-design.md`

## Global Constraints

- Canonical implementation base is `main@b66123352a0b0e0f31b2a0b5c05bc823f30f0eea` unless remote `main` changes before execution; base drift requires STOP, not automatic rebase/reset.
- Initial E2E scope is exactly `E2E-01 NEW`, `E2E-02 REVALIDATE + explicit projection regeneration`, and `E2E-03 RESUME`.
- Every agent execution phase and every evaluator phase uses a fresh Codex session.
- Hidden conversation context is never part of scenario continuity; persisted repository state is the continuity mechanism.
- `STATIC_CONTRACT`, `EXECUTABLE_CHECKS`, `AGENT_E2E_ACCEPTANCE`, and `NATIVE_RUNTIME` remain distinct validation levels.
- `AGENT_E2E_ACCEPTANCE` must never be reported as `NATIVE_RUNTIME`.
- `NATIVE_RUNTIME` remains `UNAVAILABLE` in this slice.
- Deterministic verifiers check only machine-verifiable invariants; semantic quality is reviewed by the independent evaluator.
- Scenario prompts must not disclose the exact expected defect, semantic IDs, stale markers, or required answer structure beyond user intent and stop conditions.
- Canonical Stage A evidence identities are `ES-*` and `EVD-*`; do not reintroduce legacy `WS-*` as evidence.
- Canonical STM identities are `COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EV-*`, `FLOW-*`, `AUTH-*`, `CFG-*`, `ERR-*`.
- `working/INDEX.md` remains coordinator workflow authority and must never become `PRJ-*`.
- Projection dependency notation remains `CONSUMER -> PREREQUISITE`.
- Semantic mutation and projection regeneration remain separate operations.
- Canonical fixtures are immutable templates; scenario execution occurs on isolated copies/worktrees.
- Raw run results are transient and gitignored unless a later explicit decision promotes a bounded summary to durable evidence.
- README claims about E2E validation are added only after the corresponding scenario has actually reached `PASS` (`EXECUTABLE_CHECKS PASS` + `INDEPENDENT_EVALUATION PASS`).
- Do not introduce a database, service, daemon, generic workflow engine, CI requirement, benchmark harness, Stage C runtime, Service Simulator runtime, or native coordinator.

---

## File Structure

Create or modify the following bounded units:

```text
README.md                                      refreshed only after acceptance evidence exists
.gitignore                                     ignore transient E2E result directories

tests/e2e/
├── README.md                                  operator guide and fresh-session protocol
├── common/
│   ├── result-contract.md                     PASS/FAIL/INCONCLUSIVE semantics
│   ├── evaluator-prompt.txt                   common independent evaluator contract
│   ├── prepare-run.sh                         copy fixture to isolated run directory
│   └── write-metadata.sh                      reproducibility metadata helper
├── E2E-01-new/
│   ├── README.md
│   ├── fixture/
│   ├── prompt.txt
│   ├── expected-invariants.md
│   └── verify.sh
├── E2E-02-revalidate-regenerate/
│   ├── README.md
│   ├── fixture-before/
│   ├── fixture-after/
│   ├── prompt-new.txt
│   ├── prompt-revalidate.txt
│   ├── prompt-regenerate.txt
│   ├── expected-invariants.md
│   └── verify.sh
└── E2E-03-resume/
    ├── README.md
    ├── fixture/
    ├── prompt-start.txt
    ├── prompt-resume.txt
    ├── expected-invariants.md
    └── verify.sh

tests/manual-agent-e2e-validation.md           static contract/pressure validation for this harness

docs/validation/manual-agent-e2e.md            durable explanation of validation taxonomy and run protocol
```

Do not add committed `tests/e2e-results/` content.

---

### Task 1: Freeze Harness Contracts and Fail-First Validation

**Files:**
- Create: `tests/manual-agent-e2e-validation.md`
- Create: `tests/e2e/common/result-contract.md`
- Create: `docs/validation/manual-agent-e2e.md`

**Interfaces:**
- Consumes: approved design spec and current Stage A/B contracts.
- Produces: named validation levels, scenario result contract, fresh-session rule, failure classifications, and acceptance gate used by every later task.

- [ ] **Step 1: Write fail-first static validation records**

Add explicit checks covering at least:

```text
ME2E-001 validation taxonomy is four-level and non-collapsing
ME2E-002 PASS requires executable checks + independent evaluator PASS
ME2E-003 fresh session is mandatory per execution/evaluator phase
ME2E-004 raw run output is transient by default
ME2E-005 README claims are evidence-gated
ME2E-006 fixture source is immutable during runs
ME2E-007 Stage C/native runtime remains out of scope
```

Each record must name the exact future file/heading that is currently missing.

- [ ] **Step 2: Verify RED**

Run repository-native static/contract inspection for the new records.

Expected: the new checks report RED/missing because the E2E harness contracts do not yet exist.

- [ ] **Step 3: Add common result contract**

`tests/e2e/common/result-contract.md` must define exactly:

```text
PASS
  EXECUTABLE_CHECKS = PASS
  INDEPENDENT_EVALUATION = PASS

FAIL
  one or more required invariants demonstrably violated

INCONCLUSIVE
  execution/tooling/environment interruption prevents proof
  without proving a Skill defect
```

Also define failure classifications:

```text
FIXTURE_DEFECT
PROMPT_DEFECT
VERIFY_SCRIPT_DEFECT
EVALUATOR_DEFECT
SKILL_CONTRACT_DEFECT
AGENT_EXECUTION_VARIANCE
ENVIRONMENT_FAILURE
```

- [ ] **Step 4: Add durable validation taxonomy document**

`docs/validation/manual-agent-e2e.md` must distinguish:

```text
STATIC_CONTRACT
EXECUTABLE_CHECKS
AGENT_E2E_ACCEPTANCE
NATIVE_RUNTIME
```

and explicitly state native runtime remains unavailable.

- [ ] **Step 5: Re-run focused static validation**

Expected: ME2E-001..007 PASS at static/contract level.

- [ ] **Step 6: Commit**

```bash
git add tests/manual-agent-e2e-validation.md tests/e2e/common/result-contract.md docs/validation/manual-agent-e2e.md
git commit -m "test: define manual agent E2E validation contracts"
```

---

### Task 2: Common Isolated-Run Helpers and Git Hygiene

**Files:**
- Create: `tests/e2e/common/prepare-run.sh`
- Create: `tests/e2e/common/write-metadata.sh`
- Modify: `.gitignore`
- Create: `tests/e2e/README.md`

**Interfaces:**
- Consumes: Task 1 result contract.
- Produces: repeatable run directory creation and metadata capture shared by all scenarios.

- [ ] **Step 1: Add fail-first checks for helper behavior**

Extend `tests/manual-agent-e2e-validation.md` with checks that require:

```text
run directory is outside canonical fixture tree
source fixture checksum is captured before execution
prepare-run refuses an existing non-empty destination unless --reuse is explicit
result tree is ignored by Git
metadata records scenario ID, fixture checksum, Skill SHA, start timestamp
```

- [ ] **Step 2: Implement `prepare-run.sh`**

Contract:

```bash
./tests/e2e/common/prepare-run.sh \
  <scenario-id> \
  <fixture-source> \
  <run-root>
```

Behavior:

```text
validate source directory exists
create unique run directory
copy fixture preserving relative files
record source tree checksum in execution-metadata.txt
record source Git SHA when source belongs to current repo
print absolute run directory path as final stdout line
never mutate source fixture
```

Use deterministic sorted file hashing (`find ... -type f -print0 | sort -z`) and available checksum utility; document portability assumption.

- [ ] **Step 3: Implement `write-metadata.sh`**

Contract:

```bash
./tests/e2e/common/write-metadata.sh <metadata-file> KEY VALUE
```

It must append shell-safe `KEY=VALUE` records without rewriting earlier values silently; duplicate key attempts fail.

- [ ] **Step 4: Update `.gitignore`**

Ignore exactly the transient result root chosen by the harness, e.g.:

```text
tests/e2e-results/
```

Do not ignore scenario definitions or fixture templates.

- [ ] **Step 5: Write operator guide**

`tests/e2e/README.md` must explain:

```text
fresh Codex session requirement
prepare-run command
where to paste scenario prompt
how to save codex-output.txt
how to run verify.sh
how to start a new evaluator session
how to store evaluator-output.md
how to derive PASS/FAIL/INCONCLUSIVE
what never gets committed
```

- [ ] **Step 6: Test source immutability**

Create a temporary run from a fixture stub, modify only the run copy, and prove source checksum remains unchanged.

- [ ] **Step 7: Commit**

```bash
git add .gitignore tests/e2e/README.md tests/e2e/common/prepare-run.sh tests/e2e/common/write-metadata.sh tests/manual-agent-e2e-validation.md
git commit -m "test: add isolated E2E run harness"
```

---

### Task 3: E2E-01 NEW Fixture and Prompt

**Files:**
- Create: `tests/e2e/E2E-01-new/README.md`
- Create: `tests/e2e/E2E-01-new/fixture/**`
- Create: `tests/e2e/E2E-01-new/prompt.txt`
- Create: `tests/e2e/E2E-01-new/expected-invariants.md`

**Interfaces:**
- Consumes: common harness and Stage A/B identity/authority contracts.
- Produces: one small reviewable repository containing real architecture behavior and one real review-worthy defect.

- [ ] **Step 1: Define fixture architecture before code**

Use a tiny Python standard-library application so no dependency installation obscures the Skill test. Required components:

```text
HTTP-like request entry point
SQLite or file-backed persistence
fake external billing/client boundary
header/token trust boundary
retry/failure path
one intentional architecture defect observable in code
```

The defect must not be described in `prompt.txt`.

- [ ] **Step 2: Implement fixture files**

Keep fixture under roughly 8-12 source files. Include an application README describing only how the app is intended to work, not the hidden review finding.

- [ ] **Step 3: Write scenario prompt**

The prompt must request a bounded `NEW` Architecture Review using the installed Skill, normal persistent artifacts, and completion of the normal review package. It may define scope but must not name expected IDs or the intentional defect.

- [ ] **Step 4: Write expected invariants**

Include at least:

```text
ES-* and EVD-* evidence identities used
no WS-* evidence identities
STM IDs restricted to COMP/IF/INT/DS/EV/FLOW/AUTH/CFG/ERR
Architecture interpretation remains in Architecture-owned semantic artifacts
working/INDEX.md exists and remains coordinator authority
projection artifacts exist but are non-authoritative
required dependency records resolve
no NATIVE_RUNTIME PASS claim
```

- [ ] **Step 5: Commit fixture and contracts**

```bash
git add tests/e2e/E2E-01-new
git commit -m "test: add NEW agent E2E fixture"
```

---

### Task 4: E2E-01 Deterministic Verifier

**Files:**
- Create: `tests/e2e/E2E-01-new/verify.sh`
- Modify: `tests/manual-agent-e2e-validation.md`

**Interfaces:**
- Consumes: an executed E2E-01 run directory.
- Produces: deterministic `EXECUTABLE_CHECKS PASS|FAIL` with per-check diagnostics.

- [ ] **Step 1: Write verifier checks as explicit functions**

At minimum implement functions for:

```text
require_file
forbid_pattern
require_pattern
validate_id_namespaces
validate_reference_targets
validate_working_index_not_projection
validate_no_native_runtime_pass
validate_fixture_source_checksum
```

- [ ] **Step 2: Keep semantics out of grep**

Do not assert subjective quality such as finding depth. Only inspect concrete paths, IDs, references, statuses, and forbidden claims.

- [ ] **Step 3: Add negative self-test**

Run verifier against a deliberately incomplete temporary audit tree and require FAIL.

- [ ] **Step 4: Add positive synthetic self-test**

Create the minimum synthetic artifact tree that satisfies deterministic checks and require PASS. This is verifier testing, not E2E acceptance.

- [ ] **Step 5: Commit**

```bash
git add tests/e2e/E2E-01-new/verify.sh tests/manual-agent-e2e-validation.md
git commit -m "test: verify NEW agent E2E outputs"
```

---

### Task 5: E2E-02 REVALIDATE + Regeneration Fixture Pair

**Files:**
- Create: `tests/e2e/E2E-02-revalidate-regenerate/README.md`
- Create: `tests/e2e/E2E-02-revalidate-regenerate/fixture-before/**`
- Create: `tests/e2e/E2E-02-revalidate-regenerate/fixture-after/**`
- Create: `tests/e2e/E2E-02-revalidate-regenerate/prompt-new.txt`
- Create: `tests/e2e/E2E-02-revalidate-regenerate/prompt-revalidate.txt`
- Create: `tests/e2e/E2E-02-revalidate-regenerate/prompt-regenerate.txt`
- Create: `tests/e2e/E2E-02-revalidate-regenerate/expected-invariants.md`

**Interfaces:**
- Consumes: common harness and Stage B projection lifecycle contracts.
- Produces: deterministic before/after repository pair where one accepted fact changes and unrelated areas do not.

- [ ] **Step 1: Define one controlled material delta**

Choose one interface/integration behavior whose before→after change must affect a known projection class while leaving another projection unrelated. Example shape:

```text
before: client timeout/retry contract A
after: client timeout/retry contract B
```

Do not encode expected semantic IDs into prompts.

- [ ] **Step 2: Make fixture pair mechanically comparable**

The two trees must differ only in files necessary for the controlled delta. Add a documented command that proves the intended diff.

- [ ] **Step 3: Write three prompts**

`prompt-new.txt`: establish baseline audit on before state.

`prompt-revalidate.txt`: ask to `REVALIDATE` persisted state against after state and stop after semantic revalidation + Projection Impact Analysis, before projection regeneration.

`prompt-regenerate.txt`: in a third fresh session request explicit regeneration of the affected projection scope.

- [ ] **Step 4: Write expected invariants**

At minimum:

```text
REVALIDATE does not replay full unrelated audit
accepted affected semantic identity/revision changes
at least one affected projection becomes STALE before regeneration
unrelated projection remains reusable/current when no dependency path exists
CONSUMER -> PREREQUISITE notation preserved
explicit regeneration is separate phase
CURRENT restored only after verification
candidate/unverified output does not create accepted downstream revision impact
NO_CHANGE semantics accepted when applicable
```

- [ ] **Step 5: Commit**

```bash
git add tests/e2e/E2E-02-revalidate-regenerate
git commit -m "test: add REVALIDATE regeneration E2E fixture"
```

---

### Task 6: E2E-02 Deterministic Verifier

**Files:**
- Create: `tests/e2e/E2E-02-revalidate-regenerate/verify.sh`
- Modify: `tests/manual-agent-e2e-validation.md`

**Interfaces:**
- Consumes: one run directory containing phase-A baseline, phase-B revalidate, phase-C regeneration artifacts or snapshots.
- Produces: machine verification of separation and freshness transitions.

- [ ] **Step 1: Define required run layout**

Use explicit phase directories:

```text
run/phase-a-new/
run/phase-b-revalidate/
run/phase-c-regenerate/
```

or equivalent documented snapshots. The verifier must fail if phase evidence is missing.

- [ ] **Step 2: Verify transition facts**

Machine-check at minimum:

```text
baseline projection metadata CURRENT
phase-B affected projection STALE/BLOCKED as contract requires
phase-B output did not already publish a new accepted projection revision through hidden regeneration
unrelated projection revision/status unchanged when expected
phase-C affected projection CURRENT only with verification record
canonical dependency arrow notation appears where dependency metadata is emitted
```

- [ ] **Step 3: Verify source pair immutability**

Both canonical fixture trees must retain recorded checksums.

- [ ] **Step 4: Negative and synthetic positive self-tests**

Test both a broken transition and a minimal valid transition tree.

- [ ] **Step 5: Commit**

```bash
git add tests/e2e/E2E-02-revalidate-regenerate/verify.sh tests/manual-agent-e2e-validation.md
git commit -m "test: verify REVALIDATE regeneration transitions"
```

---

### Task 7: E2E-03 RESUME Fixture and Prompts

**Files:**
- Create: `tests/e2e/E2E-03-resume/README.md`
- Create: `tests/e2e/E2E-03-resume/fixture/**`
- Create: `tests/e2e/E2E-03-resume/prompt-start.txt`
- Create: `tests/e2e/E2E-03-resume/prompt-resume.txt`
- Create: `tests/e2e/E2E-03-resume/expected-invariants.md`

**Interfaces:**
- Consumes: current NEW/RESUME orchestration and authoritative `working/INDEX.md` contract.
- Produces: an intentionally interruptible audit scenario that can be resumed with no previous transcript.

- [ ] **Step 1: Select a durable stop gate**

Use a checkpoint that is guaranteed to have persisted meaningful accepted/in-progress state but precedes final package completion. Document exact stop condition in scenario README.

- [ ] **Step 2: Build fixture**

Fixture must be large enough to exercise more than one accepted work unit but still remain small and deterministic.

- [ ] **Step 3: Write start prompt**

Request `NEW`, persist normal state, then stop exactly at the chosen durable checkpoint. Do not ask the model to create synthetic resume state.

- [ ] **Step 4: Write resume prompt**

Keep it intentionally sparse:

```text
Invoke the installed architecture-code-review Skill for this repository.
Resume the existing incomplete audit from persisted repository state.
Do not rely on any previous conversation transcript.
```

Add only scope information actually needed to identify the repository/run.

- [ ] **Step 5: Write expected invariants**

Include:

```text
persisted state discovered from repository
working/INDEX.md not regenerated as projection
accepted/fresh earlier work reused
resume continues from correct gate
freshness/authority reconciled first
no duplicate semantic identities from restart
final lineage references original run/revision state
```

- [ ] **Step 6: Commit**

```bash
git add tests/e2e/E2E-03-resume
git commit -m "test: add RESUME agent E2E fixture"
```

---

### Task 8: E2E-03 Deterministic Verifier

**Files:**
- Create: `tests/e2e/E2E-03-resume/verify.sh`
- Modify: `tests/manual-agent-e2e-validation.md`

**Interfaces:**
- Consumes: phase-A interrupted state and phase-B resumed/completed state.
- Produces: machine evidence that persisted coordinator authority and lineage survive fresh-session resume.

- [ ] **Step 1: Define phase snapshot requirements**

Require explicit snapshots or copied audit-package states before and after resume.

- [ ] **Step 2: Verify machine-checkable resume facts**

At minimum:

```text
working/INDEX.md exists before resume
working/INDEX.md is not declared as PRJ-*
accepted IDs from phase A remain present after phase B
no duplicate ID definitions introduced by phase B
final package exists only after resume phase
lineage/revision binding fields reference persisted repository state
```

Do not use grep to judge whether reasoning was “good”.

- [ ] **Step 3: Negative and synthetic positive self-tests**

Broken case: duplicate a semantic ID or mark `working/INDEX.md` as projection; verifier must FAIL.

Valid synthetic case must PASS.

- [ ] **Step 4: Commit**

```bash
git add tests/e2e/E2E-03-resume/verify.sh tests/manual-agent-e2e-validation.md
git commit -m "test: verify RESUME agent E2E outputs"
```

---

### Task 9: Independent Evaluator Contract

**Files:**
- Create: `tests/e2e/common/evaluator-prompt.txt`
- Modify: `tests/e2e/README.md`
- Modify: each scenario `README.md`

**Interfaces:**
- Consumes: scenario expected invariants, fixture state, produced artifacts, and verify output.
- Produces: structured independent evaluation without repair.

- [ ] **Step 1: Write common evaluator prompt**

It must instruct a fresh evaluator session to read:

```text
scenario README
expected-invariants.md
fixture source/current run copy
produced audit artifacts
verify-output.txt
```

and return exactly:

```text
INDEPENDENT_E2E_EVALUATION
scenario:
verdict: PASS | FAIL | INCONCLUSIVE
critical_findings:
important_findings:
minor_findings:
findings:
authority_boundaries: PASS | FAIL
scope_control: PASS | FAIL
persisted_state_behavior: PASS | FAIL | N/A
projection_semantics: PASS | FAIL | N/A
evidence_support: PASS | FAIL
repair_performed: false
```

- [ ] **Step 2: Explicitly forbid repair**

Evaluator must not edit fixture, audit artifacts, prompts, expected invariants, or verifier.

- [ ] **Step 3: Define scenario-specific evaluator emphasis**

Scenario READMEs must point evaluator to the correct semantic questions:

```text
E2E-01: evidence/STM/Architecture/projection authority separation
E2E-02: impact-driven revalidation and explicit regeneration separation
E2E-03: resume from persisted authority rather than hidden context/reconstruction
```

- [ ] **Step 4: Commit**

```bash
git add tests/e2e/common/evaluator-prompt.txt tests/e2e/README.md tests/e2e/E2E-*/README.md
git commit -m "test: add independent E2E evaluator contract"
```

---

### Task 10: Manual Runbook and Result Recording

**Files:**
- Modify: `docs/validation/manual-agent-e2e.md`
- Create: `tests/e2e/common/result-template.md`
- Modify: `tests/e2e/README.md`

**Interfaces:**
- Consumes: all three scenario packs and evaluator contract.
- Produces: exact operator instructions the user can follow manually.

- [ ] **Step 1: Add per-run sequence**

Document this exact lifecycle:

```text
prepare isolated run
capture metadata
fresh Codex execution session
save codex output
run verify.sh > verify-output.txt
fresh Codex evaluator session
save evaluator-output.md
fill result.md using result-template.md
classify PASS/FAIL/INCONCLUSIVE
```

- [ ] **Step 2: Add reproducibility metadata fields**

Require:

```text
scenario_id
fixture_checksum
architecture_code_review_sha
codex_model_if_available
started_at
ended_at
execution_result
executable_checks_result
independent_evaluation_result
final_result
failure_classification_if_non_pass
```

- [ ] **Step 3: Add strict PASS derivation**

No manual override to PASS is permitted when either executable or evaluator result is not PASS.

- [ ] **Step 4: Commit**

```bash
git add docs/validation/manual-agent-e2e.md tests/e2e/README.md tests/e2e/common/result-template.md
git commit -m "docs: add manual E2E execution runbook"
```

---

### Task 11: Harness Self-Validation Before Real Agent Runs

**Files:**
- Modify: `tests/manual-agent-e2e-validation.md`
- Optional create only if repository pattern benefits: `tests/e2e/self-check.sh`

**Interfaces:**
- Consumes: complete harness definitions.
- Produces: confidence that the verifier/harness itself rejects obvious false positives before user spends Codex runs.

- [ ] **Step 1: Run all verifier negative self-tests**

Required: every verifier returns non-zero on its intentionally invalid synthetic tree.

- [ ] **Step 2: Run all verifier synthetic-positive self-tests**

Required: each verifier returns zero on its minimal contract-compliant synthetic tree.

- [ ] **Step 3: Run source mutation guard checks**

Required: canonical fixture checksums unchanged after preparation/self-tests.

- [ ] **Step 4: Run full repository static contract regressions**

At minimum include Stage A, Stage B (`PS-100..PS-116` or current canonical range), and the new ME2E checks. Preserve actual current ranges if repository evolved.

- [ ] **Step 5: Run `git diff --check` and inspect scope**

No README refresh yet. No native runtime claim. No Stage C changes.

- [ ] **Step 6: Commit any bounded self-check adjustments**

Commit message:

```text
test: validate manual E2E harness
```

---

### Task 12: Publish Harness Candidate for User-Run Acceptance

**Files:**
- No required content change; optional bounded status doc only if repository convention requires it.

**Interfaces:**
- Consumes: Tasks 1-11.
- Produces: a published feature branch/HEAD from which the user can run E2E-01..03 manually.

- [ ] **Step 1: Perform independent implementation review**

Review harness against the design and this plan. Critical/Important findings must be remediated before publication.

- [ ] **Step 2: Verify no README evidence claims were prematurely added**

README may still be stale in other ways, but it must not claim the new E2E scenarios passed before the user runs them.

- [ ] **Step 3: Publish exact feature branch**

Recommended branch:

```text
feature/manual-agent-e2e-validation
```

Publish without force-push and report exact HEAD.

- [ ] **Step 4: Return USER_RUN_READY contract**

Return:

```text
MANUAL_AGENT_E2E_USER_RUN_READY
feature_branch:
feature_head:
base_main:
scenario_packs:
  E2E-01 NEW
  E2E-02 REVALIDATE + regeneration
  E2E-03 RESUME
harness_self_checks:
static_regressions:
independent_review:
readme_refresh_performed: false
native_runtime: UNAVAILABLE
```

Stop. Do not run Codex E2E sessions on the user's behalf unless explicitly requested.

---

### Task 13: Record Actual User-Run Acceptance Results

**Files:**
- Create only after runs: `docs/validation/manual-agent-e2e-results.md`
- Modify only if necessary: scenario docs to correct confirmed harness defects

**Interfaces:**
- Consumes: actual user-run `result.md` summaries for all three scenarios.
- Produces: bounded durable evidence summary, not raw transcripts.

- [ ] **Step 1: Ingest only bounded result summaries**

Do not commit raw Codex transcripts or full transient result trees by default.

- [ ] **Step 2: Record each scenario separately**

For each:

```text
scenario
fixture checksum/revision
Skill SHA
execution result
EXECUTABLE_CHECKS result
INDEPENDENT_EVALUATION result
final PASS/FAIL/INCONCLUSIVE
confirmed findings if any
```

- [ ] **Step 3: Enforce slice acceptance rule**

Only declare initial E2E slice accepted if:

```text
E2E-01 PASS
E2E-02 PASS
E2E-03 PASS
```

An `INCONCLUSIVE` prevents full acceptance.

- [ ] **Step 4: Route failures before Skill changes**

Classify failures using the Task 1 taxonomy. Do not automatically modify Stage A/B contracts because an agent run failed.

- [ ] **Step 5: Commit evidence summary only when accurate**

Suggested commit:

```text
docs: record manual agent E2E acceptance results
```

---

### Task 14: Refresh README from Proven State

**Files:**
- Modify: `README.md`
- Reference: `docs/validation/manual-agent-e2e-results.md`

**Interfaces:**
- Consumes: actual accepted E2E results plus canonical Stage A/B contracts.
- Produces: current public README with no aspirational capability claims.

- [ ] **Step 1: Correct known stale Stage A terminology**

Replace any obsolete evidence wording such as `WS-* / EV-*` evidence identity with canonical:

```text
ES-* Evidence Set/container
EVD-* Evidence Observation
EV-* Event/Message (STM entity)
```

Do not confuse `EV-*` with evidence.

- [ ] **Step 2: Add concise Stage A model**

Explain:

```text
Shared Evidence
Shared Technical Model
Technical Model Gate
capability-owned interpretation
human projections
```

and list canonical STM namespaces.

- [ ] **Step 3: Add Stage B projection lifecycle**

Explain at public README depth:

```text
PRJ-* projection identity
RG-* regeneration session
ACTIVE/RETIRED
CURRENT/STALE/BLOCKED
Projection Impact Analysis
PROJECTION_IMPACT_ACCOUNTED
TARGETED / ALL_STALE
CONSUMER -> PREREQUISITE
NO_CHANGE/freshness reconciliation
V1..V4 verification
working/INDEX.md coordinator authority
bounded PROJECTION_REPAIR
```

- [ ] **Step 4: Clarify what the product does not implement**

Explicitly state no standalone/native coordinator/generator/verifier runtime exists yet and Stage C execution capabilities remain planned.

- [ ] **Step 5: Add validation taxonomy and actual named evidence**

README may state only scenarios that actually PASS. Format example:

```text
Static contract validation: available
Executable scenario checks: available
Manual agent-driven E2E acceptance: PASS for E2E-01 NEW, E2E-02 REVALIDATE + regeneration, E2E-03 RESUME
Standalone/native runtime: not implemented
```

If not all scenarios PASS, name only passing scenarios and explicitly mark the rest `FAIL` or `INCONCLUSIVE` rather than implying universal coverage.

- [ ] **Step 6: Refresh installation, usage, repository structure, and roadmap links**

Use actual current paths and current session intents:

```text
USE_EXISTING
NEW
RESUME
REVALIDATE
EXTEND
PROJECTION_REPAIR
```

Do not document Stage C candidate features as available behavior.

- [ ] **Step 7: Run README consistency scan**

Search for at least:

```text
WS-* evidence
EV-* evidence
IMPLEMENTATION CANDIDATE Stage B
review pending Stage B
runtime PASS
native coordinator available
```

Every stale/false occurrence must be removed or explicitly contextualized as legacy wording.

- [ ] **Step 8: Commit**

Suggested commit:

```bash
git add README.md docs/validation/manual-agent-e2e-results.md
git commit -m "docs: refresh README after manual agent E2E validation"
```

---

### Task 15: Final Evidence Review and Promotion Candidate

**Files:**
- No new files required unless review findings require bounded correction.

**Interfaces:**
- Consumes: harness, actual acceptance evidence, refreshed README.
- Produces: final promotion candidate with explicit validation claims.

- [ ] **Step 1: Independently review actual E2E evidence**

Verify result summaries match executable/evaluator outputs and no PASS was inferred from missing evidence.

- [ ] **Step 2: Independently review README claims**

Every validation/capability statement must map to current accepted repository authority or named E2E evidence.

- [ ] **Step 3: Run full static regressions and verifier self-checks**

Require current Stage A/Stage B static contracts and new harness static contracts PASS.

- [ ] **Step 4: Verify repository hygiene**

```bash
git status --short
git diff --check
```

Transient E2E result directories remain ignored/uncommitted.

- [ ] **Step 5: Return final candidate state**

Return:

```text
MANUAL_AGENT_E2E_VALIDATION_CANDIDATE
feature_head:
E2E-01:
E2E-02:
E2E-03:
initial_slice_accepted: true | false
static_contract_validation:
executable_checks:
agent_e2e_acceptance:
native_runtime: UNAVAILABLE
readme_refreshed: true | false
independent_review:
promotion_safe: true | false
```

Do not promote automatically.

---

## Self-Review Checklist

Before treating this plan as ready:

1. **Spec coverage:** Tasks 1-12 create a reproducible harness without claiming acceptance; Task 13 records real user-run evidence; Task 14 updates README only from evidence; Task 15 independently checks claims and promotion readiness.
2. **No hidden runtime:** No task creates a native coordinator, projection runtime, Service Simulator execution, or Stage C implementation.
3. **Fresh sessions:** E2E-02 explicitly requires three execution sessions; E2E-03 requires separate start/resume sessions; every evaluator is separate.
4. **Verifier boundary:** Shell checks only deterministic structure/state; semantic evaluation remains independent.
5. **Authority safety:** `working/INDEX.md`, STM, Architecture authority, projection non-authority, and dependency direction are explicitly checked.
6. **README evidence gate:** README refresh is intentionally after actual user-run results, never before.
7. **No placeholders:** The plan defines exact files, expected contracts, commands, state transitions, and acceptance outputs.
