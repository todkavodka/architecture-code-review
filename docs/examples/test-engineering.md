# Пример: анализ качества тестов

## Исходная ситуация

Backend имеет 1200 тестов и зелёный CI. Команда готовится менять retry logic и хочет понять, действительно ли тесты доказывают material behavior, а не просто покрывают happy path.

Запрос:

```text
Используй architecture-code-review.
Нужен только Test Engineering review: Test Assurance и Test Plan.
Architecture Review и Code Quality Review не включай.
```

## Review Suite

```text
Architecture Review: OFF
Test Engineering: ON
  Test Assurance
  Test Plan
Code Quality Review: OFF
```

Architecture OFF не мешает Test Engineering использовать required accepted STM slice.

## Behavior discovery

Анализ выявляет material behavior:

```text
BC-021
Retry after an ambiguous timeout must not create a second order.

BC-022
Only one terminal completion event may be observable for one order generation.
```

Далее формируются assurance targets:

```text
MAT-011
Prove order uniqueness after timeout before response is received.

MAT-012
Prove completion publication uniqueness under retry.
```

## Existing tests

Допустим, найдено:

```text
TM-031
maps MAT-011 -> test_retry_after_500
verdict: PARTIAL
reason: test covers explicit HTTP 500, not ambiguous timeout after server-side commit
```

Для `MAT-012` executable evidence не найдено.

## Assurance gaps

```text
GAP-008
MAT-011 lacks evidence for commit-success/response-timeout path.

GAP-009
MAT-012 has no executable proof for repeated publication attempts.
```

Зелёный CI не отменяет gaps: tests доказывают только фактически проверяемые scenarios.

## Test Assurance output

Summary должен объяснить человеку:

- broad suite exists and is stable;
- normal retry cases covered;
- ambiguous outcome path remains unproven;
- terminal publication uniqueness is not executable-proven;
- confidence в retry migration ограничена этими gaps.

Assurance Map показывает exact `MAT -> BC -> TM/GAP` traceability.

## Test Plan

Для `GAP-008` план может потребовать integration test boundary с реальной transaction behavior и controllable response interruption.

Для `GAP-009` — scenario с ambiguous broker acknowledgement или controllable publisher boundary, если это минимальная faithful test boundary.

План не должен просто писать «добавить integration test»; он фиксирует stimulus, failure point, assertions и acceptance evidence.

## Что не произошло

- Architecture Review не был молча включён.
- Behavior Model не показывался пользователю как optional checkbox.
- Contract Verification не запускался, если нет material formal contract.
- E2E не был добавлен только потому, что проблема сложная.

## После исправления тестов

Пользователь запускает `REVALIDATE` existing package.

Impact может затронуть `TM-*`, `MAT-*` verdicts и `GAP-*`, но не обязан revalidate unrelated behaviors.

Если новый test evidence закрывает `GAP-009`, record закрывается только после accepted revalidation, а не потому, что test file появился в Git diff.

## Снимок принятого результата

```text
baseline: a1b2c3d
Review Suite: Test Engineering = ON
selected menu documents: Test Assurance, Test Plan
package members: PRJ-TEST-REVIEW-00-ASSURANCE-SUMMARY,
                 PRJ-TEST-REVIEW-01-ASSURANCE-MAP,
                 PRJ-TEST-REVIEW-02-TEST-PLAN
freshness: CURRENT for the resolved package
```

Путь проверки одного утверждения:

```text
PRJ-TEST-REVIEW-00-ASSURANCE-SUMMARY
  -> GAP-009
  -> MAT-012 -> BC-022
  -> relevant STM facts / executable-test inventory
  -> source and test files at a1b2c3d
```

`Behavior Contract Model` может входить в пакет как требуемая проекция модуля,
но не становится отдельным выбором пользователя.
