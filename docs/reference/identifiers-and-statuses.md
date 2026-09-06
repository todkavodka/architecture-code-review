# Идентификаторы и статусы

Этот справочник объясняет основные canonical identifiers и status tokens, которые встречаются в audit package. Он не заменяет нормативные contracts; задача документа — помочь человеку быстро понять роль записи.

## Shared Evidence

| Prefix | Роль |
|---|---|
| `WS-*` | Ограниченное исследование / workset. Группирует observations, scope, baseline, limitations и handoff. |
| `EV-*` | Адресуемое observation внутри `WS-*`. Фиксирует, что показал конкретный source на выбранном baseline. |

Типичная ссылка:

```text
WS-012-payment-retry#EV-003
```

## Shared Technical Model

| Prefix | Роль |
|---|---|
| `COMP-*` | Компонент или runtime unit |
| `IF-*` | Интерфейс |
| `INT-*` | Существенное взаимодействие |
| `DS-*` | Хранилище данных |
| `EVENT-*` | Событие или сообщение |
| `FLOW-*` | Существенный поток |
| `AUTH-*` | Граница аутентификации / доверия |
| `CFG-*` | Существенный конфигурационный факт |
| `ERR-*` | Контракт ошибки или отказа |

STM identity сохраняется при ревизии того же объекта. Если меняется сама семантическая сущность, создаётся новая identity и явная связь supersession.

### STM status

```text
CANDIDATE
UNDER_REVIEW
ACCEPTED
SUPERSEDED
REJECTED
```

### STM freshness

```text
VALID
REVALIDATION_REQUIRED
UNKNOWN
```

## Architecture Review

| Prefix | Роль |
|---|---|
| `RF-*` | Принятый архитектурный / root finding |

Architecture findings не заменяют STM facts: STM отвечает «что существует», `RF-*` — «что это означает архитектурно и какое существенное последствие доказано».

## Test Engineering

| Prefix | Роль |
|---|---|
| `BC-*` | Behavior Contract — одно независимо проверяемое существенное поведение |
| `CC-*` | Contract Consistency Record — зафиксированное расхождение представлений контракта |
| `MAT-*` | Material Assurance Target — что именно должно быть доказано тестами |
| `TM-*` | Test Mapping — связь target с исполняемым test evidence |
| `GAP-*` | Assurance Gap — отсутствующее, частичное или недостаточное доказательство |
| `TASK-*` | Test Engineering remediation task |

Ключевые различия:

```text
BC != MAT
BC != GAP
CC != GAP
TM != BC
```

## Code Quality Review

| Prefix | Роль |
|---|---|
| `CQ-*` | Принятый Code Quality finding |
| `CQRA-*` | Code Quality remediation action |

Важно:

```text
CQRA COMPLETED != CQ RESOLVED
```

Завершённое remediation action требует отдельной evidence-backed revalidation перед закрытием finding.

## Projections

| Prefix | Роль |
|---|---|
| `PRJ-*` | Stable identity человекочитаемой или операционной projection |
| `RG-*` | Session пересборки projections |

### Projection freshness

```text
CURRENT
STALE
BLOCKED
```

`STALE` означает, что документ больше не подтверждён как актуальное представление authority. Это не утверждение о ложности underlying semantic records.

## Workflow intents

```text
USE_EXISTING
NEW
RESUME
REVALIDATE
EXTEND
PROJECTION_REPAIR
```

Подробные preconditions и postconditions: [Workflow Reference](workflows.md).

## Architecture configuration

Depth:

```text
STANDARD_FULL
FORENSIC
```

Endpoint:

```text
REVIEW_ONLY
REVIEW_PLUS_TARGET_ARCHITECTURE
REVIEW_PLUS_TARGET_AND_ROADMAP
```

Depth и endpoint — независимые оси. Любой из двух depth поддерживает любой из трёх endpoint.

## Projection package policies

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

- `PERMISSIVE` — не связанные с текущим gate stale projections не блокируют semantic closeout.
- `REQUIRED_SCOPE_CURRENT` — requested projection и обязательные prerequisites должны быть `CURRENT`.
- `ALL_SCOPED_CURRENT` — все required members resolved package должны быть `CURRENT`.

## Workflow status vocabulary

Конкретный набор допустимых workflow statuses определяется нормативными contracts. На практике в `INDEX.md` и capability registry встречаются состояния вроде:

```text
PENDING
IN_PROGRESS
REVIEW_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
COMPLETE
NOT_APPLICABLE
```

Не следует интерпретировать одно status token вне owning context. Например, projection `BLOCKED` и capability `BLOCKED` — разные состояния разных слоёв.
