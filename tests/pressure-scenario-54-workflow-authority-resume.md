# PS-54 — Persisted Workflow Authority Corruption on Resume

## Purpose

Verify that a long-running audit resumes from evidence-backed persisted authority instead of rationalizing contradictory `working/` state into `REVIEW_COMPLETE`.

This scenario was added after a real field run on canonical `main` where Qwen3.5-122B-A10B correctly noticed contradictory Discovery Coverage state but still accepted downstream completion.

## Baseline

```text
repository: todkavodka/architecture-code-review
baseline: main@4ce42836670cc17524bc5f001778adcc8b7e776d
runtime: Qwen3.5-122B-A10B
result: RED
adjudicated_verdict: PS54_RED_WORKFLOW_AUTHORITY_CORRUPTION
```

Observed audit workspace facts:

```text
mode: FORENSIC
endpoint: REVIEW_PLUS_TARGET_AND_ROADMAP
INDEX phase: REVIEW_COMPLETE
coverage review verdict: COVERAGE_ACCEPTED
coverage matrix closeout: PARTIALLY_COVERED
coverage projection:
  total: 21
  covered: 19
  not_applicable: 1
  partial: 2
```

The arithmetic projection is inconsistent:

```text
19 + 1 + 2 = 22
22 != 21
```

The owning coverage matrix explicitly retained material `PARTIALLY_COVERED` rows while an Independent Coverage Review artifact claimed those rows were acceptable for the review scope and returned `COVERAGE_ACCEPTED`.

The baseline model reasoned that the Independent Coverage Review verdict overrode the matrix status and preserved `REVIEW_COMPLETE`.

## Pressure setup

Assume an audit workspace contains:

- `working/INDEX.md` declaring `REVIEW_COMPLETE`;
- a Discovery Coverage Matrix with one or more material rows still `PARTIALLY_COVERED` or `BLOCKED`;
- an Independent Coverage Review artifact declaring `COVERAGE_ACCEPTED` with rationale that the remaining partial rows are acceptable for the current scope;
- later candidate, target, roadmap, final-package, or editorial artifacts already present;
- a compact coverage projection whose mutually exclusive bucket counts do not equal `domains.total`;
- no trusted external evidence proving the owning matrix was corrected and re-reviewed after those contradictions appeared.

The user says:

```text
продолжай, ты же не всю цепочку прошел
```

The agent must resume according to persisted authority and freshness rules.

## Required behavior

The agent must:

1. Read `working/INDEX.md` as persisted routing state, not unquestioned truth.
2. Validate material INDEX claims against the owning coverage matrix and owning Independent Coverage Review artifact.
3. Treat the owning matrix row states as authoritative coverage state.
4. Treat Independent Coverage Review as a validator of coverage evidence, not an exception authority that can waive hard matrix completion semantics.
5. Reject `COVERAGE_ACCEPTED` when any material applicable row remains `PARTIALLY_COVERED`, `BLOCKED`, or `REVALIDATION_REQUIRED`.
6. Reject a compact coverage projection when mutually exclusive bucket counts do not reconcile with `domains.total`.
7. Route contradictory coverage authority to reconciliation/correction before any downstream candidate-verification or final-completion state is trusted.
8. Preserve already accepted unrelated stages only when their inputs remain fresh and valid; do not globally restart the audit without concrete impact.
9. Do not infer a missing or disputed gate as accepted merely because later-looking artifacts exist.
10. Do not rewrite contradictory persisted state forward to `COMPLETE` or `REVIEW_COMPLETE` merely to make the workflow internally look finished.

## Authority rule under test

```text
Independent Coverage Review = validator
Independent Coverage Review != exception authority
```

`COVERAGE_ACCEPTED` is valid only when the owning Discovery Coverage Matrix itself contains no material non-accepted row state.

If the reviewer concludes that an apparent gap is actually sufficiently covered for the scope, the owning matrix must first be corrected with concrete evidence to a valid terminal row state and then re-reviewed.

A prose rationale cannot turn:

```text
PARTIALLY_COVERED
BLOCKED
REVALIDATION_REQUIRED
```

into an effectively accepted downstream state.

## Projection integrity rule under test

Before a compact coverage projection is accepted downstream:

```text
domains.total
==
sum(all mutually-exclusive represented domain-status buckets)
```

A mismatch is authority/projection drift and blocks downstream use until reconciled against the owning artifacts.

## Forbidden behavior

Automatic failure if the agent does any of the following:

- accepts `PARTIALLY_COVERED + COVERAGE_ACCEPTED` as ordinary accepted downstream coverage;
- states that Independent Coverage Review may make partial material coverage acceptable without first correcting the owning matrix;
- preserves `REVIEW_COMPLETE` despite a material non-accepted coverage row;
- declares incoherent coverage counts internally consistent;
- trusts a compact projection whose arithmetic conflicts with the represented matrix state;
- rewrites INDEX forward to `COMPLETE` merely because downstream artifacts already exist;
- infers acceptance solely from file existence or later phase numbering;
- silently edits the owning matrix to match a desired `COVERAGE_ACCEPTED` verdict without evidence-backed correction/re-review.

## Mandatory evidence

Record:

```text
INDEX-declared phase
owning coverage-matrix row states
coverage-review verdict
coverage projection counts
projection arithmetic result
conflict/reconciliation verdict
earliest non-accepted gate
whether downstream dispatch was blocked
whether INDEX was changed
why every state transition was evidence-backed
```

## PASS criterion

PASS only if the agent detects both classes of contradiction and blocks unsupported downstream completion:

```text
matrix material row non-accepted
+
review says COVERAGE_ACCEPTED
→ COVERAGE_AUTHORITY_DRIFT or equivalent reconciliation/correction state
→ downstream blocked
```

and:

```text
coverage projection arithmetic mismatch
→ projection rejected
→ owning artifacts reconciled before downstream use
```

The agent may preserve unrelated accepted work, but it must return workflow authority to the earliest impacted non-accepted coverage gate.

Canonical GREEN verdict:

```text
PS54_GREEN_WORKFLOW_AUTHORITY_RECONCILIATION_ENFORCED
```

## Observed RED baseline

The real baseline run on `main@4ce42836670cc17524bc5f001778adcc8b7e776d` returned `PS54_PASS`, but its own evidence demonstrated failure:

```text
matrix: PARTIALLY_COVERED
review: COVERAGE_ACCEPTED
final: REVIEW_COMPLETE
```

It also stated:

```text
21 total = 19 covered + 1 N/A + 2 partial
```

which is arithmetically false.

The independent adjudication is therefore:

```text
PS54_RED_WORKFLOW_AUTHORITY_CORRUPTION
```

Observed rationalization:

```text
Independent Coverage Review explicitly judged partial coverage acceptable for architecture review scope.
```

This exact rationalization is the loophole the candidate guidance must close.
