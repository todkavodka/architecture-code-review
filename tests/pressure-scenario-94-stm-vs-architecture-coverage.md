# PS-94 — STM coverage versus Architecture coverage

## Observed RED baseline

The unchanged flow starts thematic discovery after accepted As-Built
(`references/review-modes-and-orchestration.md:537-552`) and requires only the
Architecture Discovery Coverage Matrix before candidate verification
(`references/review-method.md:147-160`). No accepted full STM or Technical
Model Coverage Review exists. The current factual As-Built is substantial
(`references/review-method.md:17-42`), but it is not an accepted full STM
coverage gate.

Observed verdict: `PS94_RED_ARCHITECTURE_STARTS_WITH_UNACCEPTED_FULL_STM`.

## Fixture

Run a full Architecture Review with material interfaces, flows, persistence,
trust, lifecycle, and deployment surfaces.

## GREEN contract

```text
Shared Evidence
-> FULL STM
-> STM Coverage Review
-> TECHNICAL_MODEL_COVERAGE_ACCEPTED
-> Architecture thematic discovery
-> Architecture Discovery Coverage
-> COVERAGE_ACCEPTED
-> candidate verification
```

`STM coverage` measures factual system-surface completeness. `Architecture
coverage` measures material architecture/risk-mechanism analysis completeness.
Neither gate accepts or replaces the other.

## Failure conditions

- one coverage model is used as both factual and architecture-risk coverage;
- Architecture thematic discovery starts with a required full STM whose
  coverage is not accepted.

## Verdict vocabulary

```text
PS94_RED_COVERAGE_MODELS_COLLAPSED
PS94_RED_ARCHITECTURE_STARTS_WITH_UNACCEPTED_FULL_STM
PS94_GREEN_COVERAGE_SEPARATION
PS94_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
