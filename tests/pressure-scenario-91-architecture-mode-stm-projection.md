# PS-91 — Architecture mode to STM projection

## Observed RED baseline

`main@10233b80eb6a46ff1f8d4348c4be890cf1d1f4a2` distinguishes compact
`STANDARD_FULL` artifacts from deeper `FORENSIC` artifacts
(`references/review-modes-and-orchestration.md:10-15,47-115`) and requires a
compact Architecture Discovery Coverage closeout in standard mode
(`references/review-method.md:216-222`). It defines no STM coverage/depth
projection, shared schema, or compact-to-forensic enrichment path. Therefore
the baseline cannot establish `STANDARD_FULL -> FULL / COMPACT` STM coverage.

Observed verdict: `PS91_RED_STANDARD_NOT_FULL`.

## Fixture

Evaluate the same material system under `STANDARD_FULL`, then enrich its
accepted model under `FORENSIC`.

## GREEN contract

```text
STANDARD_FULL -> FULL / COMPACT
FORENSIC      -> FULL / FORENSIC
FULL/FORENSIC satisfies FULL/COMPACT
STANDARD_FULL -> FORENSIC is enrichment, not a restart
same STM schema in both modes
```

Both modes cover every material applicable technical domain. They differ only
in population depth, evidence granularity, decomposition, and review rigor.

## Failure conditions

- `STANDARD_FULL` has less than full applicable factual coverage;
- the modes create incompatible STM schemas;
- upgrading to `FORENSIC` discards valid accepted facts and restarts discovery.

## Verdict vocabulary

```text
PS91_RED_STANDARD_NOT_FULL
PS91_RED_SEPARATE_MODE_SCHEMAS
PS91_RED_FORENSIC_RESTART
PS91_GREEN_MODE_PROJECTION
PS91_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
