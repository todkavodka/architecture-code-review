# PS-92 — Fact, interpretation, and single-writer authority

## Observed RED baseline

The baseline correctly separates a thematic correction from direct As-Built
editing (`SKILL.md:80-81`; `references/review-method.md:193-197`), but it makes
the Architecture Review's As-Built artifact the technical factual source of
truth (`references/review-modes-and-orchestration.md:604-610`). It has no STM
fact owner or `TECH_FACT_*` protocol. Under the Stage A boundary, architecture
therefore owns both the factual model and its interpretations.

Observed verdict: `PS92_RED_FACT_AND_FINDING_COLLAPSED`.

## Fixture

The factual observation is `OrdersService synchronously calls PaymentService`.
An Architecture Review concludes `availability coupling risk`; Test Engineering
assesses assurance; a future Code Quality capability observes duplication.

## GREEN contract

```text
fact -> STM
architecture judgement -> Architecture Review
assurance judgement -> Test Engineering
code-quality judgement -> future Code Quality
```

Architecture Review and Test Engineering may emit:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

Only the Technical Model Gate accepts or changes accepted STM facts. Capability
artifacts may not silently rewrite them.

## Failure conditions

- a factual observation is collapsed into a finding or assurance conclusion;
- a capability silently rewrites an accepted STM fact instead of using the
  candidate, conflict, or revalidation request protocol.

## Verdict vocabulary

```text
PS92_RED_FACT_AND_FINDING_COLLAPSED
PS92_RED_CAPABILITY_REWRITES_STM
PS92_GREEN_FACT_INTERPRETATION_BOUNDARY
PS92_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
