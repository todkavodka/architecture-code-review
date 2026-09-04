# PS-90 — Persistent STM bootstrap

## Observed RED baseline

Static inspection of `main@10233b80eb6a46ff1f8d4348c4be890cf1d1f4a2` found
that `NEW` enters the existing Architecture Review flow
(`references/review-modes-and-orchestration.md:168-176`), whose first substantive
technical authority is As-Built (`SKILL.md:58-68`; `references/review-method.md:11-42`).
There is no persisted Shared Technical Model (STM), STM slice, or bounded-`NEW`
STM contract. This is a static contract observation, not runtime evidence.

Observed verdict: `PS90_RED_NO_PERSISTENT_STM`.

## Fixtures

- **A:** `NEW` full Architecture Review.
- **B:** `NEW` bounded capability requiring only a limited factual slice.

## GREEN contract

Every `NEW` creates a persisted STM baseline. Fixture A requires a `FULL` STM.
Fixture B may create a partial STM and build only its required slices:

```text
always create model != always build complete model
```

Persistence must survive chat loss and cannot be satisfied by chat state or a
final Markdown report alone.

## Failure conditions

- no persisted STM exists after `NEW`;
- bounded `NEW` builds all 18 full domains solely because STM exists;
- STM is represented only as chat state or final-report prose.

## Verdict vocabulary

```text
PS90_RED_NO_PERSISTENT_STM
PS90_RED_FULL_MODEL_FORCED_FOR_BOUNDED_NEW
PS90_GREEN_PERSISTENT_STM_BOOTSTRAP
PS90_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
