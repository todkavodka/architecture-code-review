# PS-96 — Incremental STM EXTEND and REVALIDATE

## Observed RED baseline

The baseline already requires `EXTEND` and `REVALIDATE` to reuse the minimum
accepted/fresh dependency slice and not restart unrelated stages
(`references/session-orchestration.md:73,136-139`). It has no STM slices,
interaction/flow impact route, or `COMPACT -> FORENSIC` STM enrichment model.
The reusable-slice principle is baseline-compliant; STM-specific replay or
enrichment behavior cannot be evaluated without an STM.

Observed verdict: `PS96_INCONCLUSIVE`.

## Fixtures

- **A:** accepted full/compact STM; later Test Engineering `EXTEND` needs only
  interfaces, errors, and test-relevant views.
- **B:** a source change touches one accepted interaction and one flow.
- **C:** an accepted `STANDARD_FULL` model is upgraded to `FORENSIC`.

## GREEN contract

```text
EXTEND -> reuse accepted+VALID slices; build/revalidate only missing/stale required slice
REVALIDATE -> diff routes affected evidence/facts/aspects; no whole-STM replay without impact evidence
COMPACT -> FORENSIC -> enrich affected/all required depth gaps, preserve accepted facts where still valid
```

## Verdict vocabulary

```text
PS96_RED_FULL_STM_REPLAY_ON_EXTEND
PS96_RED_GLOBAL_STM_REVALIDATION
PS96_RED_FORENSIC_RESTART
PS96_GREEN_STM_INCREMENTAL_REUSE
PS96_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
