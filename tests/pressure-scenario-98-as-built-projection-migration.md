# PS-98 — As-Built authority migration

## Observed RED baseline

`main@10233b80eb6a46ff1f8d4348c4be890cf1d1f4a2` explicitly states that the
working As-Built is the technical source of truth
(`SKILL.md:80-81`; `references/review-modes-and-orchestration.md:604-610`). A
thematic contradiction creates `ARCH-CORRECTION-CANDIDATE`
(`references/review-modes-and-orchestration.md:556-579`), not the future
`TECH_FACT_CONFLICT` protocol. This is direct static RED evidence.

Observed verdict: `PS98_RED_AS_BUILT_STILL_SOURCE_OF_TRUTH`.

## Fixture

An accepted factual model contains topology, ownership, boundaries, flows,
lifecycle, persistence, trust, error, configuration, and runtime facts. A
thematic Architecture pass finds conflicting factual evidence.

## GREEN contract

```text
accepted STM = factual technical authority
As-Built Architecture = human-readable projection
Architecture Review consumes accepted/fresh STM
```

The thematic pass emits `TECH_FACT_CONFLICT`; it does not silently change
As-Built or STM. Migration preserves the material factual coverage currently
required by As-Built; removing old authority never permits loss of topology,
ownership, boundary, flow, lifecycle, or equivalent factual surface.

## Verdict vocabulary

```text
PS98_RED_DUAL_FACTUAL_AUTHORITY
PS98_RED_AS_BUILT_STILL_SOURCE_OF_TRUTH
PS98_RED_FACTUAL_PARITY_LOST
PS98_GREEN_AS_BUILT_PROJECTION_MIGRATION
PS98_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
