# Жизненный цикл и актуальность

В Review Suite несколько независимых видов состояния. Они не должны смешиваться в один глобальный status.

## Почему одного статуса недостаточно

Фраза «документ актуален» может означать разные вещи:

- технический факт всё ещё подтверждён;
- finding всё ещё применим;
- projection соответствует accepted authority;
- workflow завершён;
- package можно публиковать.

Эти состояния проверяются отдельно.

## STM lifecycle

STM fact проходит semantic lifecycle:

```text
CANDIDATE
  -> UNDER_REVIEW
  -> ACCEPTED
  -> SUPERSEDED | REJECTED
```

Freshness хранится отдельно:

```text
VALID
REVALIDATION_REQUIRED
UNKNOWN
```

Поэтому accepted fact может существовать исторически, но требовать revalidation для нового baseline.

## Capability-owned lifecycle

Architecture, Test Engineering и Code Quality имеют собственные lifecycle rules.

Например, Code Quality remediation action может быть `COMPLETED`, но finding не становится автоматически `RESOLVED`:

```text
CQRA COMPLETED
  !=
CQ RESOLVED
```

После remediation требуется evidence-backed revalidation finding.

## Projection freshness

Projection имеет другой freshness axis:

```text
CURRENT
STALE
BLOCKED
```

`STALE` означает: документ больше не подтверждён как актуальное представление своих dependencies.

Это не означает:

```text
underlying semantic authority is false
```

И наоборот, `CURRENT` projection может честно отображать partial/unknown semantic state.

## Semantic freshness != projection freshness

Ключевое различие:

```text
semantic REVALIDATE
  !=
projection regeneration
```

После accepted semantic change выполняется Projection Impact Analysis. Она отмечает затронутые projections, но не переписывает их.

Если нужен новый fresh document, создаётся отдельная `RG-*` regeneration session.

## Revalidation после изменения проекта

Для accepted package используется bounded flow:

```text
previous baseline
  -> current baseline
  -> change inventory
  -> impact analysis
  -> impact classification
  -> minimum dependency slice
  -> targeted fresh evidence
  -> revalidation/adjudication
  -> delta reconciliation
```

Git diff используется как routing context, а не как доказательство.

## Impact classes

Нормативный revalidation contract использует orchestration labels:

```text
LOCAL
BOUNDARY
SYSTEMIC
```

Это не severity findings.

- `LOCAL` — нет доказанного существенного изменения boundary/contract/ownership; проверка остаётся локальной, пока evidence не расширит scope.
- `BOUNDARY` — затронута существенная API, auth/trust, persistence, lifecycle, concurrency, IPC или другая accepted boundary.
- `SYSTEMIC` — изменилось несколько фундаментальных boundaries или модель системы настолько, что targeted completion больше ненадёжна.

Для `SYSTEMIC` Skill рекомендует full reaudit и требует решения пользователя:

```text
FULL_REAUDIT_RECOMMENDED
user_decision_required: true
```

## Preservation unaffected state

`REVALIDATE` не должен уничтожать unaffected accepted state.

Если изменилась одна API boundary, нет основания автоматически revalidate unrelated storage subsystem.

Preservation допустим только когда dependency analysis действительно показывает отсутствие влияния. Unknown linkage нельзя объявлять preserved без targeted investigation.

## Supersession

Исторические records не переписываются так, чтобы казаться текущими.

Если сущность заменена:

```text
old record
  -> superseded_by -> new record
```

Это позволяет объяснить прошлые decisions и корректно revalidate dependent artifacts.

## Compact state

`INDEX.md` и handoffs должны проверяться против owning authority before downstream substantive use.

Если compact state старее owning artifact:

```text
AUTHORITY_RECONCILIATION_REQUIRED
```

Нельзя считать запись свежей только потому, что она лежит в более новом файле.

## Presentation-only change

Если меняется только язык, Markdown, таблица, Mermaid или ссылка без semantic change, используется `PROJECTION_REPAIR` и `PROJECTION_REVALIDATION`.

Если в процессе обнаружен semantic drift:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

## Практическая матрица

| Событие | Нужное действие |
|---|---|
| Код не менялся, нужен existing accepted report | `USE_EXISTING` |
| Workflow не закончен | `RESUME` |
| Project baseline изменился | `REVALIDATE` |
| Нужен новый capability/output | `EXTEND` |
| Изменилось только presentation | `PROJECTION_REPAIR` |
| Projection stale, semantics accepted | explicit `RG-*` regeneration when fresh output is required |

## Что читать дальше

- [Reuse and Change Guide](../guides/reuse-and-change.md)
- [Workflow Reference](../reference/workflows.md)
- [Projections and Packages](projections-and-packages.md)
