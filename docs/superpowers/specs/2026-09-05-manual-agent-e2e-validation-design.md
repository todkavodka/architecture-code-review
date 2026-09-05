# Manual Agent E2E Validation + README Refresh

Status: DESIGN CANDIDATE

Baseline:

```text
main@b66123352a0b0e0f31b2a0b5c05bc823f30f0eea
```

## 1. Purpose

The repository already has strong static/contract pressure validation for Stage A and Stage B, but it does not have an executable Stage B coordinator, generator, or verifier. Therefore current claims correctly stop at `PASS_STATIC_CONTRACT` and `runtime_validation: UNAVAILABLE`.

This design adds a reproducible **manual agent-driven end-to-end acceptance layer** without pretending that a native runtime already exists.

The user runs each scenario manually in a fresh Codex session. The scenario uses the real `architecture-code-review` Skill against a prepared fixture repository, produces real audit artifacts, and is then checked by deterministic assertions plus a separate evaluator pass.

After the E2E results exist, the repository README is refreshed to describe the actual Stage A/B architecture, validation levels, current capabilities, and limitations.

This work is deliberately positioned before Stage C and must not implement Stage C runtime execution.

---

## 2. Validation taxonomy

The repository must distinguish four validation levels:

```text
STATIC_CONTRACT
  Markdown pressure scenarios and contract inspection

EXECUTABLE_CHECKS
  deterministic local scripts that inspect produced files/state

AGENT_E2E_ACCEPTANCE
  fresh Codex session executes the real Skill against a fixture repository

NATIVE_RUNTIME
  standalone executable coordinator/generator/verifier
```

Current expected state after this work:

```text
STATIC_CONTRACT       AVAILABLE
EXECUTABLE_CHECKS     AVAILABLE for E2E outputs
AGENT_E2E_ACCEPTANCE  AVAILABLE for approved scenarios
NATIVE_RUNTIME        UNAVAILABLE
```

`AGENT_E2E_ACCEPTANCE` must never be reported as `NATIVE_RUNTIME`.

---

## 3. Scope

Initial scope contains exactly three E2E scenarios:

```text
E2E-01 NEW
E2E-02 REVALIDATE + projection regeneration
E2E-03 RESUME
```

Out of scope for the first slice:

```text
EXTEND
PROJECTION_REPAIR-specific E2E
Test Engineering execution E2E
Service Simulator execution
E2E test execution against application services
native coordinator implementation
CI automation
parallel test execution
benchmarking/model comparison
```

Those may be added only after the first three scenarios prove the harness and acceptance workflow.

---

## 4. Fixture strategy

Use small deterministic fixture repositories committed under the test tree.

Recommended structure:

```text
tests/e2e/
├── README.md
├── common/
│   ├── result-contract.md
│   └── evaluator-prompt.txt
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
```

Fixture applications should be intentionally small but architecturally meaningful enough to exercise ownership, interfaces, persistence, trust boundaries, and failure behavior.

The fixtures are test data, not examples of preferred production architecture.

---

## 5. Isolation model

Every agent execution phase must start in a **fresh Codex session**.

No scenario may rely on hidden conversation context from a previous execution.

The only allowed continuity between phases is persisted repository state and explicit prompt input.

For example:

```text
E2E-02 phase 1
fresh Codex session
→ NEW audit
→ persisted audit package

fixture changes from before → after

E2E-02 phase 2
new fresh Codex session
→ REVALIDATE using persisted package

E2E-02 phase 3
new fresh Codex session
→ explicit projection regeneration
```

This is necessary to test the repository's resume/freshness/authority contracts rather than the model's memory.

---

## 6. Execution evidence

Each scenario run gets a unique local result directory outside the fixture source tree or in a gitignored test-results area.

Conceptual structure:

```text
tests/e2e-results/<scenario>/<run-id>/
├── execution-metadata.txt
├── codex-output.txt
├── verify-output.txt
├── evaluator-output.md
└── result.md
```

Do not commit raw transient run output by default.

The durable repository contract is the scenario definition, not one arbitrary execution transcript.

If a specific acceptance run is later chosen as release evidence, record only a bounded summary or approved evidence artifact.

---

## 7. Common result contract

Each scenario must finish with one of:

```text
PASS
FAIL
INCONCLUSIVE
```

`PASS` requires both:

```text
EXECUTABLE_CHECKS = PASS
INDEPENDENT_EVALUATION = PASS
```

`FAIL` is used when a required invariant is demonstrably violated.

`INCONCLUSIVE` is used when the execution cannot establish the result because of tooling/environment/model interruption without proving a Skill defect.

A scenario is never upgraded from `INCONCLUSIVE` to `PASS` by assumption.

---

## 8. Deterministic verification boundary

`verify.sh` must check only machine-verifiable facts.

Examples:

```text
required files exist
forbidden files do not exist
required headings/records exist
ID namespaces are syntactically valid
required direct references resolve
working/INDEX.md exists where required
projection lifecycle status is the expected value
specific stale/current markers are present
expected revision/fingerprint metadata exists
forbidden authority mutation did not occur
```

It must not attempt to grade nuanced architectural reasoning with grep heuristics.

Statements such as:

```text
"the root cause analysis is excellent"
"the architecture review is sufficiently deep"
```

belong to independent evaluator review, not shell assertions.

---

## 9. Independent evaluator

After the execution and deterministic checks, run a separate fresh Codex session as evaluator.

The evaluator receives:

```text
scenario contract
expected invariants
fixture repository state
produced audit artifacts
verify.sh result
```

It must not receive hidden execution-session context.

The evaluator checks semantic properties that deterministic scripts cannot reliably judge, including:

```text
authority boundaries preserved
evidence supports material claims
factual STM remains distinct from Architecture interpretation
projection content does not become semantic authority
scope is respected
resume/revalidate behavior follows persisted state rather than reconstruction
```

The evaluator returns structured PASS/FAIL findings.

The evaluator does not repair the result under review.

---

# 10. E2E-01 — NEW

## Goal

Prove that a fresh agent session can run a bounded new Architecture Review from scratch and persist a coherent audit package using the current Stage A/B contracts.

## Fixture requirements

The fixture should contain at minimum:

```text
one application entry point
one HTTP or equivalent external interface
one persistence mechanism
one external integration or fake downstream client
one authentication/trust boundary
one material failure/retry path
one intentionally review-worthy architecture issue
```

The issue must be real in the fixture implementation rather than stated only in test documentation.

## Execution

User starts a fresh Codex session in a clean working copy of the fixture and invokes the Skill with the scenario prompt.

The prompt requests a bounded `NEW` Architecture Review and the minimum outputs needed to exercise:

```text
Shared Evidence
Shared Technical Model
Architecture semantic authority
final projections
projection lifecycle metadata
```

## Required invariants

At minimum verify:

```text
1. evidence observations are represented using canonical Stage A evidence identities;
2. STM factual entities use canonical COMP/IF/INT/DS/EV/FLOW/AUTH/CFG/ERR namespaces;
3. Architecture findings/interpretation remain Architecture-owned;
4. generated projections are not treated as semantic authority;
5. working/INDEX.md remains coordinator workflow authority;
6. required final report/projection artifacts exist;
7. direct dependencies are represented using the current dependency contracts;
8. no legacy WS-as-evidence namespace is introduced;
9. no unsupported runtime PASS claim is emitted.
```

---

# 11. E2E-02 — REVALIDATE + projection regeneration

## Goal

Prove that a persisted audit can be revalidated against a controlled repository change and that semantic change and projection regeneration remain separate operations.

## Fixture states

Maintain two deterministic fixture revisions:

```text
fixture-before
fixture-after
```

`fixture-after` changes one material architectural/interface fact while leaving unrelated areas unchanged.

The changed fact should affect at least one projection through an exact or selector-backed dependency.

## Phase A — establish baseline

Fresh Codex session:

```text
fixture-before
→ NEW
→ accepted audit state
→ projections CURRENT
```

## Phase B — REVALIDATE

Fresh Codex session against `fixture-after` using the persisted audit package.

Required behavior:

```text
repository delta
→ semantic revalidation
→ affected accepted semantic identity/revision changes
→ Projection Impact Analysis
→ affected projection STALE
```

Forbidden behavior:

```text
semantic revalidation
→ silently regenerate all affected projections in the same operation
```

Unrelated semantic/projection state should remain reusable where dependencies prove it unaffected.

## Phase C — explicit regeneration

A third fresh Codex session explicitly requests regeneration of the affected projection scope.

Required behavior:

```text
STALE
→ explicit regeneration
→ V1..V4-equivalent contract verification
→ CURRENT
```

If output is unchanged after a legitimate stale condition, the scenario should accept the approved `NO_CHANGE` semantics and require no new projection revision.

## Required invariants

At minimum:

```text
1. REVALIDATE is impact-driven rather than full audit replay;
2. semantic mutation and projection regeneration are separate;
3. affected projection becomes STALE before explicit regeneration;
4. unrelated projection does not become stale without a dependency path;
5. dependency direction remains CONSUMER -> PREREQUISITE;
6. downstream impact follows the derived reverse dependency graph;
7. explicit regeneration restores CURRENT only after verification;
8. candidate/unverified output does not propagate accepted downstream revision impact;
9. runtime remains AGENT_E2E_ACCEPTANCE, not NATIVE_RUNTIME.
```

---

# 12. E2E-03 — RESUME

## Goal

Prove that a second fresh agent session can continue an intentionally interrupted audit from persisted workflow authority without relying on hidden conversation context.

## Fixture

Use a deterministic fixture large enough that the audit can stop at a defined intermediate gate.

## Phase A — start and stop

Fresh Codex session starts a `NEW` audit and is instructed to stop at a specific durable checkpoint before final completion.

The repository must contain persisted resume-critical state, including authoritative `working/INDEX.md` state where applicable.

## Phase B — resume

Start another fresh Codex session with only:

```text
repository path
instruction to invoke Skill and RESUME the existing audit
```

Do not paste the previous session transcript.

## Required invariants

At minimum:

```text
1. previous durable state is discovered from repository artifacts;
2. working/INDEX.md remains workflow authority and is not regenerated as PRJ-*;
3. accepted/fresh work is reused rather than reconstructed unnecessarily;
4. incomplete work resumes from the correct gate;
5. authority/freshness reconciliation occurs before continuing;
6. final package does not duplicate semantic identities from the first session;
7. hidden prior conversation context is unnecessary;
8. final result records the correct lineage/revision bindings.
```

---

## 13. Fixture mutation safety

Scenario runners must never modify the canonical fixture source in place unless the scenario contract explicitly requires the mutation.

Preferred execution model:

```text
fixture template
→ copied to isolated temp/worktree directory
→ scenario executed there
→ result retained or removed independently
```

This allows repeatable runs.

`verify.sh` must fail if the test accidentally changes the canonical source fixture.

---

## 14. Prompt contracts

Scenario prompts should be explicit about the user intent but must not over-script the expected internal answer.

Bad:

```text
Create COMP-001, IF-001, RF-001 and mark PRJ-002 stale.
```

This only tests prompt obedience.

Good:

```text
Run a new Architecture Review of this repository using the installed Skill.
Produce the normal persisted audit artifacts and stop after the requested gate.
```

Expected internal IDs and invariants are checked afterward.

The prompt may constrain scope and stop conditions, but it should not reveal the exact defect or exact semantic records expected from the fixture.

---

## 15. Reproducibility metadata

For each run capture at minimum:

```text
scenario ID
fixture revision/checksum
architecture-code-review Skill commit SHA
Codex/model identity where available
start/end timestamp
execution session result
verify result
evaluator result
```

This metadata is audit evidence, not an input into semantic authority.

Do not require token counts or performance benchmarking in this slice.

---

## 16. Failure classification

When an E2E scenario fails, classify before changing the Skill:

```text
FIXTURE_DEFECT
PROMPT_DEFECT
VERIFY_SCRIPT_DEFECT
EVALUATOR_DEFECT
SKILL_CONTRACT_DEFECT
AGENT_EXECUTION_VARIANCE
ENVIRONMENT_FAILURE
```

Do not automatically interpret every failed agent run as a product defect.

A confirmed `SKILL_CONTRACT_DEFECT` follows the normal remediation/review path.

---

## 17. Acceptance gate for this validation slice

The initial validation slice is successful when:

```text
E2E-01 PASS
E2E-02 PASS
E2E-03 PASS
```

with each PASS containing:

```text
EXECUTABLE_CHECKS PASS
INDEPENDENT_EVALUATION PASS
```

If one scenario remains `INCONCLUSIVE`, the slice is not fully accepted.

Repeated executions may be useful for confidence, but a statistical reliability benchmark is out of scope for the initial slice.

---

## 18. README refresh

README update happens **after** the E2E validation results are known, so documentation reflects evidence rather than aspiration.

The README refresh must correct current stale/high-risk documentation and describe the product as it actually exists after Stage A and Stage B.

Required topics:

```text
what architecture-code-review is
what it is not
current Architecture Review workflow
Stage A Shared Evidence / STM model
canonical evidence namespaces: ES-* and EVD-*
canonical STM namespaces: COMP/IF/INT/DS/EV/FLOW/AUTH/CFG/ERR
Architecture semantic authority vs projections
Test Engineering authority model
Stage B projection lifecycle
PRJ-* and RG-* identities
CURRENT / STALE / BLOCKED
Projection Impact Analysis
PROJECTION_IMPACT_ACCOUNTED
TARGETED / ALL_STALE regeneration
PROJECTION_REPAIR semantics
working/INDEX.md coordinator authority
NEW / RESUME / USE_EXISTING / REVALIDATE / EXTEND
validation taxonomy
current E2E acceptance evidence
native-runtime limitation
installation and real usage examples
repository structure
roadmap status
```

README must not claim capabilities that are only Stage C plans.

---

## 19. README validation claims

After successful initial E2E acceptance, README may truthfully state:

```text
Static contract validation: available
Executable scenario checks: available
Manual agent-driven E2E acceptance: validated for named scenarios
Standalone/native runtime: not implemented
```

It must name the validated scenarios rather than implying universal E2E coverage.

If a scenario has not passed, README must not describe it as validated.

---

## 20. Relationship to Stage C

This slice does not start Stage C.

Its purpose is to establish evidence about the current Skill before adding Test Engineering execution capabilities.

Stage C remains:

```text
PLANNED
```

After this slice, Stage C Discovery may use the E2E failures and limitations as factual input.

---

## 21. Git and repository boundaries

Implementation should occur on an isolated branch/worktree.

Do not alter Stage A/B semantic contracts merely to make a verifier easy to write.

Do not commit transient E2E result directories unless explicitly selected as bounded evidence.

Do not introduce a database, service, daemon, or generic workflow engine.

Prefer POSIX shell and repository-native text processing for deterministic verification. Add Python only where parsing complexity materially justifies it.

---

## 22. Success criteria

This work is complete when:

```text
1. three reproducible E2E scenario packs exist;
2. each scenario can be run manually by the user from documented instructions;
3. each execution phase requires a fresh Codex session;
4. deterministic verifier scripts check machine-verifiable invariants;
5. independent evaluator prompts check semantic invariants;
6. result taxonomy is PASS/FAIL/INCONCLUSIVE;
7. E2E-01, E2E-02, E2E-03 have real recorded acceptance results;
8. no result is mislabeled as native runtime validation;
9. README is refreshed only after acceptance evidence exists;
10. README accurately describes Stage A, Stage B, validation evidence, and current limitations;
11. Stage C remains PLANNED and unimplemented.
```

---

## 23. Core invariants

```text
Manual agent E2E != native runtime.

Fresh sessions are mandatory across continuation boundaries.

Persisted repository state, not conversation memory, must carry RESUME/REVALIDATE continuity.

Deterministic scripts verify structure/state, not nuanced architectural quality.

Independent evaluator checks semantic quality but never repairs the run being evaluated.

Fixture defects and execution variance must be distinguished from Skill defects.

README claims follow accepted evidence; evidence is not manufactured to match README claims.

This validation slice must not implement Stage C.
```
