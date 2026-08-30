# Владение, инварианты и неблагоприятные сценарии

Этот файл является авторитетным источником для ownership (владения состоянием и ресурсами), derivation of invariants (вывода инвариантов) и adversarial scenarios (неблагоприятных сценариев конкурентности/жизненного цикла).

## 1. Матрица владения

Для значимых сущностей/ресурсов фиксируй:

| Entity/resource | Authoritative owner | Writers | Readers | Lifetime | Scope |
|---|---|---|---|---|---|

Владение выводится из реальных путей кода и runtime-поведения, а не из названий директорий или желаемой архитектуры.

Особенно проверяй:

- process-global singleton;
- per-connection/per-session ownership;
- frontend store vs backend/native state;
- временные файлы/порты/child processes;
- event listeners/subscriptions;
- locks/abort controllers/retry loops;
- persistent state/cache/configuration.

## 2. Инварианты

Инвариант — требуемое свойство системы, которое следует из реального продукта/контракта/поведения.

Хорошая форма:

```text
Наблюдение: profileId уникален только внутри connection.
Требование продукта: две connections могут существовать одновременно.
Инвариант: session state нельзя глобально идентифицировать только profileId.
```

Не придумывай инвариант только потому, что он сделал бы архитектуру «чище».

Для каждого инварианта укажи:

- источник требования;
- scope;
- владельца;
- что нарушит инвариант;
- какими flows он проверяется.

## 3. Неблагоприятная матрица сценариев

Для stateful/concurrent областей, где применимо, проверь минимум:

```text
A + A duplicate operation
A + B simultaneous owners
operation + cancel
operation + disconnect/dispose
old completion after replacement
retry + cancellation
shutdown during active work
duplicate event
missing event
same local ID under two parent owners
```

Не превращай список в механическую квоту. Выбирай сценарии по реальным capability/ownership boundaries.

## 4. Race/interleaving evidence

Race finding обычно требует конкретной последовательности:

```text
A starts
→ A suspends/awaits/subscribes
→ B mutates relevant shared state
→ A resumes
→ stale/invalid mutation or wrong-owner effect
```

Без достижимой последовательности это кандидат, а не подтверждённый race.

Для каждого сценария укажи:

- initial state;
- actors/owners;
- suspension/interleaving point;
- state mutation;
- resumed behavior;
- concrete consequence;
- existing guards/falsification attempt.

## 5. Positive controls

Фиксируй механизмы, которые правильно обеспечивают ownership/isolation/concurrency:

- корректные owner keys;
- locks;
- generation/version checks;
- cancellation tokens;
- scoped DI/object graph;
- idempotency;
- dynamic resource allocation.

Positive Control не является «похвалой ради баланса»; это механизм, который целевая архитектура и remediation не должны случайно сломать.

## 6. Architecture correction candidate

Если тематическое исследование противоречит принятой As-Built Architecture, **не редактируй As-Built напрямую**.

Запиши:

```markdown
## ARCH-CORRECTION-CANDIDATE AC-###

**Текущее утверждение:** ...
**Наблюдаемое противоречие:** ...
**Доказательства:** ...
**Предполагаемое влияние:** ...
**Затронутые области:** ...

Статус: ARCH_CORRECTION_CANDIDATE
```

Дальше применяется correction protocol из `review-modes-and-orchestration.md`.

## 7. Supporting Engineering Risks

Broad structural patterns могут повышать вероятность повторения дефектов, не являясь сами одним runtime root finding:

- semantic owner не закодирован в identity;
- lifecycle размазан по нескольким флагам;
- event переносит identity, но consumer её выбрасывает;
- shared resource не owner-keyed;
- нет локального deterministic regression suite.

Такие наблюдения можно вести как `SER-*`; не присваивай им автоматически severity продуктового дефекта.
