# Руководство по Test Engineering

Test Engineering отвечает не на вопрос «тесты зелёные?», а на вопрос:

> Какие существенные поведения системы действительно доказаны исполняемыми тестами, какие доказаны частично и где остаются пробелы?

## Когда выбирать

Используйте Test Engineering, если нужно:

- оценить реальную доказательную силу test suite;
- понять, какие material behaviors не подтверждены;
- проверить consistency формализованных контрактов;
- построить Test Plan;
- спроектировать test environment;
- спроектировать service simulator;
- спланировать E2E scenarios.

Architecture Review при этом может быть выключен.

## User-facing outputs

При включённой capability `Test Assurance` обязателен.

```text
Test Assurance                    required
Test Plan                         optional
Contract Consistency Report       optional
Test Environment Design           optional
Service Simulator Design          optional
Service Simulator Implementation Plan optional
E2E Test Plan                     optional
```

## Internal dependencies

Некоторые сущности не являются user checkbox:

- Behavior Model;
- Contract Verification, когда существует material formal contract;
- E2E Design;
- required STM/evidence slice.

Skill подключает их по необходимости.

## Semantic model

### `BC-*` — Behavior Contract

Одно существенное независимо проверяемое поведение.

Пример:

```text
BC-042
Only the current generation may publish terminal state.
```

### `MAT-*` — Material Assurance Target

Что именно должно быть доказано test evidence.

```text
MAT-017
Publication uniqueness must hold under timeout and retry.
```

### `TM-*` — Test Mapping

Связь assurance target с executable test evidence и verdict.

### `GAP-*` — Assurance Gap

Отсутствующее, частичное или недостаточное доказательство.

### `CC-*` — Contract Consistency Record

Расхождение между representations контракта.

### `TASK-*`

Remediation work, принадлежащее Test Engineering.

## Contract Verification

Если существует materially applicable formal contract, Skill сравнивает:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

Ни одно representation не получает автоматический приоритет.

Например, OpenAPI и backend implementation могут расходиться. Это создаёт authority question, а не автоматический verdict «spec wrong» или «code wrong».

`Contract Verification` — internal gate. `Contract Consistency Report` — optional human-facing projection.

## Test Assurance

Test Assurance обычно включает summary и assurance map.

Он должен отвечать:

- какие material targets выявлены;
- какие подтверждены;
- какие подтверждены частично;
- какие не доказаны;
- где tests могут создавать false confidence;
- какие gaps наиболее существенны.

## Test Plan

Test Plan должен выводиться из accepted targets/gaps.

Плохой вариант:

> добавить unit, integration и E2E tests.

Хороший план фиксирует:

- behavior/target;
- минимальную test boundary;
- dependencies/fixtures;
- failure/retry/concurrency variants;
- observable assertions;
- acceptance evidence.

## Test Environment Design

Выбирается, когда test quality зависит от environment fidelity.

Для dependency выбирается осознанный strategy, например:

```text
REAL_DISPOSABLE
SERVICE_EMULATOR
CONTROLLABLE_MOCK
IN_PROCESS_DOUBLE
TEMP_RESOURCE
NOT_REQUIRED
```

Нельзя подменить проверяемое behavior удобным mock и затем считать target доказанным.

## Service Simulator

Simulator нужен, когда consumer должен воспроизводимо работать с contract semantics unavailable/expensive service.

Он может включать:

- contract API;
- state store;
- scenario engine;
- fault injection;
- event emitter;
- control API;
- reset/seed/health operations.

Service Simulator Design не должен слепо копировать одну declaration, если accepted behavior model показывает другую семантику.

## E2E

E2E используется только для guarantees, которые действительно требуют нескольких реальных компонентов.

«Самый полный» тест не означает «лучший» тест. Boundary выбирается минимальной, но достаточной для доказательства target.

## Повторное использование

После accepted Test Engineering package:

- tests/code changed → `REVALIDATE` affected mappings/targets;
- нужен новый Test Plan/Simulator/E2E output → `EXTEND`;
- unfinished review → `RESUME`;
- нужен existing accepted assurance → `USE_EXISTING`.

## Связанные документы

- [Test Engineering example](../examples/test-engineering.md)
- [Output Reference](../reference/outputs.md)
- [Artifact Reference](../reference/artifacts.md)
