# Discovery Coverage Assurance — Validation Record

Date: 2026-08-31

Candidate branch:

`design/discovery-coverage-assurance-v0.3`

Baseline:

`main@fd7466a33362d04d964cb847d33c5a1e022ba48b`

This record preserves the fail-first baseline, fresh candidate validation, legacy regression validation, cross-model validation, spec mapping, and remaining verification limitation for Discovery Coverage Assurance.

## 1. Fail-first baseline

Pressure scenario:

`PS-45 — Interpreter Boundary Omission`

Baseline verdict:

`PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED`

Failure boundary:

`thematic discovery`

The baseline Skill could correctly adjudicate supplied safe/unsafe cases after they were presented, but did not structurally require systematic inventory of interpreter/raw-construction boundaries and source provenance during discovery. Independent verification, root adjudication, severity adjudication, and final editorial review were not the failing stages.

Runtime:

`independent fresh GLM-5.2 session supplied by the user`

## 2. Fresh candidate validation — GLM-5.2

Candidate Skill ref tested:

`6095e9c40d71dfcf542f3f02a8a14d41f0cce698`

Loaded path:

`/home/ubuntu/.agents/skills/architecture-code-review/SKILL.md`

Result:

`DISCOVERY_COVERAGE_CANDIDATE_GREEN`

Scenario results:

```text
PS-45 PASS
PS-46 PASS
PS-47 PASS
PS-48 PASS
PS-49 PASS
PS-50 PASS
PS-51 PASS
PS-52 PASS
PS-53 PASS
```

Additional checks:

```text
coverage gate A PASS
coverage gate B PASS
coverage gate C PASS
coverage gate D PASS
Safe Reproduction boundary PASS
role separation PASS
false-positive / overfitting assessment PASS
```

No candidate correction was required by this run.

The subsequent commit `602ab628c234e54ae92df21c3dd6b0f570cd5243` changed only the validation record in `tests/pressure-validation-matrix.md`; Skill behavior was unchanged.

## 3. Legacy regression validation — GLM-5.2

Candidate ref tested:

`602ab628c234e54ae92df21c3dd6b0f570cd5243`

Fresh-context regression result:

`DISCOVERY_COVERAGE_REGRESSION_GREEN`

Existing pressure families:

```text
PS-33 PASS — native plan projection
PS-34 PASS — final prose does not degrade into working-artifact shorthand
PS-35 PASS — useful diagram coverage retained
PS-36 PASS — Russian final-report language contract retained
PS-37 PASS — Mermaid render-validation gate retained
PS-38 PASS — explain-before-compress and one-primary-mechanism prose retained
PS-39 PASS — coordinator routes from compact persisted state without unjustified full rereads
PS-40 PASS — bounded Context Envelope retained
PS-41 PASS — presentation-only correction uses PROJECTION_REVALIDATION
PS-42 PASS — semantic drift and stale compact fingerprints are rejected
PS-43 PASS — Context Envelope permits concrete-trigger bounded expansion
```

Discovery Coverage interaction checks:

```text
coordinator context bloat PASS
freshness bypass PASS
Context Envelope over-restriction PASS
projection revalidation drift PASS
final editorial role drift PASS
native plan drift PASS
```

Authority ownership:

`PASS`

Validated authority split:

```text
discovery coverage semantics -> references/discovery-coverage.md
workflow state/artifacts/resume -> references/review-modes-and-orchestration.md
candidate verification -> references/independent-verification.md
root/projection identity -> references/root-boundary-adjudication.md
severity/attack chain/evidence -> references/evidence-and-severity.md
final editorial -> references/final-editorial-review.md
projection/freshness discipline -> references/revalidation-and-freshness.md
```

Completion-gate simulation:

```text
A PASS — COVERAGE_CORRECTION_REQUIRED blocks candidate verification
B PASS — COVERAGE_BLOCKED blocks ordinary REVIEW_COMPLETE
C PASS — COVERAGE_ACCEPTED permits candidate verification without confirming candidates
D PASS — later As-Built correction revalidates only impacted domains
E PASS — editorial cleanliness cannot override a technical coverage block
```

Safe Reproduction / Severity regression:

`PASS`

The regression confirmed that attack-chain requirements, post-verification/root severity ordering, strong static evidence, optional runtime validation, non-destructive reproduction, no real-secret requirement, and no unrelated external probing remain intact.

## 4. Cross-model validation — Qwen3.5-122B-A10B

Candidate ref tested:

`602ab628c234e54ae92df21c3dd6b0f570cd5243`

Initial fresh cross-model run:

```text
PS-45 PASS
PS-46 PASS
PS-47 PASS
PS-48 PASS
PS-49 PASS
PS-50 PASS
PS-51 PASS
PS-52 PASS
PS-53 PASS
Independent Coverage Review boundary PASS
Safe Reproduction boundary PASS
false-positive / overfitting checks 1-6: all NO
```

The initial run correctly described the required semantics for coverage-state simulations A and B but mislabeled those two checks as `FAIL` because it interpreted the blocked workflow operation itself as failure. Its own final verdict was `DISCOVERY_COVERAGE_QWEN_GREEN`, creating an internal scoring inconsistency.

This inconsistency was preserved rather than rewritten.

A separate fresh-context scoring recheck explicitly defined `PASS` as “the Skill produces the required behavior.” Result:

```text
A PASS — COVERAGE_CORRECTION_REQUIRED correctly blocks candidate verification
B PASS — COVERAGE_BLOCKED correctly blocks ordinary REVIEW_COMPLETE
C PASS — COVERAGE_ACCEPTED correctly permits candidate verification
D PASS — only impacted coverage domains are revalidated after a bounded As-Built correction

QWEN_COVERAGE_GATE_RECHECK_PASS
```

Adjudicated cross-model result:

`DISCOVERY_COVERAGE_QWEN_GREEN`

Operational lesson: for smaller/weaker model families, gate test prompts should define PASS/FAIL in terms of correctness of Skill behavior, not merely place PASS/FAIL labels next to states whose intended workflow action is itself “blocked.”

## 5. Design acceptance criteria mapping

The approved design defines 22 acceptance criteria. Current implementation/pressure evidence maps as follows:

1. Both modes produce a coverage matrix — `references/discovery-coverage.md` §2; orchestration artifacts for `STANDARD_FULL` and `FORENSIC`.
2. FORENSIC cannot reach candidate verification without `COVERAGE_ACCEPTED` — coverage gate + regression completion simulations.
3. STANDARD_FULL has compact coverage proof — coverage matrix + compact INDEX projection.
4. High-risk domains require semantic evidence — `references/discovery-coverage.md` high-risk proof contracts; PS-45..53.
5. `NOT_APPLICABLE` requires evidence — matrix applicability/status rules; PS-53 mechanism-absent control.
6. Zero findings remains valid — core invariant / anti-quota rule.
7. Independent Coverage Review can detect absence of investigation — As-Built reconciliation + bounded blind-spot probes; PS-43.
8. Coverage Review remains bounded — bounded probes and targeted expansion; GLM/Qwen role checks.
9. New gaps trigger targeted correction — coverage correction/re-review contract; no global restart.
10. Candidate verification remains separate — authority map + gate ordering.
11. Severity remains separate — evidence/severity authority + regression Safe Reproduction/Severity check.
12. Search/grep alone is insufficient — coverage evidence contract.
13. Cross-version/projection search is part of completeness — COMP-01 proof contract; PS-48.
14. Second-order sources remain unresolved until provenance is demonstrated — SEC-02 source taxonomy; PS-45/PS-51.
15. Final `REVIEW_COMPLETE` cannot hide material coverage gaps — completion gate; regression simulations B/E.
16. Existing final-report/editorial contracts remain intact — PS-34..38 regression GREEN.
17. Safe Reproduction is authorized, minimal, non-destructive, optional — evidence/severity + discovery coverage Safe Reproduction contracts; GLM/Qwen checks.
18. Skill does not become a public exploitation playbook — hard Safe Reproduction boundary; no offensive pressure-test requirement.
19. Availability coverage traces request amplification/bounds rather than generic performance suspicion — REL-02 contract; PS-52.
20. Authentication/session/token lifecycle is covered when applicable — SEC-01 contract; PS-46.
21. Crypto/signature/TLS is conditional and routed through relevant domains — conditional mechanism rule; PS-53.
22. Supply-chain/dynamic-loading depth is applicability-driven and may be evidence-backed N/A — OPS-02 applicability rule.

No intentionally deferred acceptance criterion is known after the fresh GLM and Qwen validation runs.

## 6. Branch/file-set verification

GitHub compare against the approved baseline was performed at candidate ref `602ab628c234e54ae92df21c3dd6b0f570cd5243` before this validation-record commit.

Observed:

```text
base: fd7466a33362d04d964cb847d33c5a1e022ba48b
head: 602ab628c234e54ae92df21c3dd6b0f570cd5243
status: ahead
ahead_by: 15
behind_by: 0
merge_base: fd7466a33362d04d964cb847d33c5a1e022ba48b
```

Changed files at that ref were limited to Skill/reference/spec/plan/test files. No production/runtime code was changed.

A local shell attempt to execute the plan-required `git diff --check` could not clone/fetch the public repository because the execution environment had no DNS/network access to `github.com` and failed with:

`Could not resolve host: github.com`

Therefore `git diff --check` is deliberately recorded as **UNEXECUTED**, not PASS.

After this validation record is committed, the final shell verification must run against the new branch HEAD:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git rev-parse origin/main
git merge-base origin/main HEAD
git rev-list --left-right --count origin/main...HEAD
git diff --check origin/main..HEAD
git diff --name-status origin/main..HEAD
```

Required final conditions:

```text
working tree clean
branch = design/discovery-coverage-assurance-v0.3
origin/main = fd7466a33362d04d964cb847d33c5a1e022ba48b, unless base has legitimately changed and is explicitly adjudicated
merge-base = verified baseline
ahead/behind relationship understood
git diff --check produces no output
no unexpected production/runtime files
```

Until that final shell-only verification is supplied, implementation verification is not claimed complete and the branch is not ready to pass the final completion gate.

## 7. Current verification state

```text
PS-45 fail-first baseline: RECORDED
PS-45..53 GLM candidate validation: GREEN
PS-33..43 GLM regression: GREEN
Qwen3.5-122B-A10B cross-model validation: GREEN after fresh scoring recheck
Design criteria 1..22 mapping: COMPLETE
Authority duplication review: PASS
Completion-gate simulation: PASS
Safe Reproduction / Severity regression: PASS
Unexpected production/runtime changes: NONE at pre-record compare
git diff --check: UNEXECUTED — external shell verification required
```

No merge, tag, release, or public `main` update is authorized by this record.