# Целевая архитектура и её независимое ревью

Этот этап выполняется только для endpoint `REVIEW_PLUS_TARGET_ARCHITECTURE` или `REVIEW_PLUS_TARGET_AND_ROADMAP` и только после принятия authoritative audit state.

## 1. Вход целевой архитектуры

Target Architecture (целевая архитектура) выводится из:

```text
verified RF roots
+ architectural invariants
+ SER
+ Positive Controls
+ explicit product decisions
```

Не проектируй «идеальную систему» с нуля.

Для каждого значимого нового abstraction/mechanism ответь:

> Какой RF/SER/invariant/product requirement требует это изменение?

Если ответа нет — убери abstraction, если она не нужна существующему продукту.

## 2. Обязательное содержание

Где применимо, target документ описывает:

- target component/responsibility boundaries;
- authoritative ownership и identity model;
- state/lifecycle transitions;
- cancellation/retry/shutdown semantics;
- boundary contracts;
- security/trust model;
- resource ownership/allocation;
- migration/compatibility constraints;
- Positive Controls, которые сохраняются;
- unresolved product/deployment decisions;
- RF/SER/invariant coverage matrix.

## 3. Feasibility classification

Значимые assumptions маркируй:

```text
PROVEN_FEASIBLE
PLAUSIBLE_NEEDS_REMEDIATION_VALIDATION
PRODUCT_OR_DEPLOYMENT_DECISION
```

Не выдавай plausible implementation option за факт текущего deployment/infrastructure.

## 4. Independent Target Review

Target author не принимает собственный документ.

Fresh-context reviewer проверяет:

- prose ↔ diagrams ↔ state tables;
- target ownership не противоречит самому себе;
- stale completion/cancellation semantics непротиворечивы;
- Positive Controls не удалены случайно;
- каждый material target mechanism мотивирован RF/SER/invariant;
- product intent не «решён» автором без evidence;
- feasibility assumptions честно классифицированы;
- target не вводит новый unsupported service/boundary/dependency без необходимости;
- security design не предполагает несуществующий trust anchor/signing capability;
- As-Built facts не перепутаны с target facts.

## 5. Review outcomes

```text
TARGET_ACCEPTED
TARGET_CORRECTION_REQUIRED
TARGET_BLOCKED_BY_DECISION
```

При correction:

```text
author artifact
→ independent review issue list
→ separate correction pass
→ fresh-context re-review
```

Correction не скрывает историю исходного review.

## 6. Review artifact

Review фиксирует для каждого issue:

```text
ID
severity of design inconsistency
location
contradiction/unsupported assumption
required correction
RF/SER/invariant affected
```

Reviewer не должен сам переписывать target document в рамках review pass.

## 7. Acceptance

Target считается accepted только когда:

- нет unresolved internal contradictions;
- feasibility assumptions классифицированы;
- RF/SER/invariant coverage traceable;
- Positive Controls accounted for;
- required correction/re-review закрыты;
- blocked product/deployment decisions явно изолированы и не замаскированы как technical facts.
