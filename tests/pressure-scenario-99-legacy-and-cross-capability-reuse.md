# PS-99 — Legacy reconciliation and cross-capability reuse

## Observed RED baseline

The baseline treats missing modern session fields as additive legacy
reconciliation rather than corruption (`references/session-orchestration.md:425-436`)
and keeps Test Engineering's `BC-*`, `CC-*`, `MAT-*`, `TM-*`, and `GAP-*`
semantics separate (`capabilities/test-review/references/test-engineering-contract.md:9-28,74-99`).
It has no STM, no legacy As-Built-to-STM validation route, and no STM reuse
contract. The baseline is compliant with the two preserved-boundary parts, but
there is no credible static evidence that it silently promotes legacy As-Built
or independently rediscovers an existing STM.

Observed verdict: `PS99_INCONCLUSIVE`.

## Fixtures

- **A:** a legacy `COMPLETE` package has accepted As-Built, no STM, and the
  same baseline.
- **B:** Test Engineering attaches after an STM exists.

## GREEN contract

```text
legacy As-Built -> candidate STM seed only -> evidence/baseline validation -> accepted STM
```

```text
Test Engineering -> reuse relevant accepted STM facts -> preserve BC/CC/MAT/TM/GAP ownership
```

## Failure conditions

- old As-Built is relabeled as accepted STM without evidence validation;
- STM absence alone marks a legacy package corrupt;
- STM replaces Behavior Contracts or Test Assurance semantics;
- a capability rereads/reconstructs a technical surface already supplied by
  accepted, fresh STM without a correctness trigger.

## Verdict vocabulary

```text
PS99_RED_LEGACY_AS_BUILT_SILENTLY_PROMOTED
PS99_RED_STM_ABSORBS_TEST_ENGINEERING
PS99_RED_DUPLICATE_CROSS_CAPABILITY_DISCOVERY
PS99_GREEN_LEGACY_AND_CROSS_CAPABILITY_REUSE
PS99_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
