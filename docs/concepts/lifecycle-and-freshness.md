# Жизненный цикл и актуальность

Это каноническое объяснение для пользователя жизненного цикла, актуальности и
различия между повторной проверкой технического смысла и пересборкой документов.

В `Review Suite` несколько независимых видов состояния. Они не должны
смешиваться в один глобальный статус.

## Почему одного статуса недостаточно

Фраза «документ актуален» может означать разные вещи:

- технический факт всё ещё подтверждён;
- вывод всё ещё применим;
- проекция соответствует принятому источнику истины;
- процесс завершён;
- пакет результатов можно публиковать.

Эти состояния проверяются отдельно.

## Жизненный цикл STM

Факт STM проходит собственный жизненный цикл:

```text
CANDIDATE
  -> UNDER_REVIEW
  -> ACCEPTED
  -> SUPERSEDED | REJECTED
```

Актуальность хранится отдельно:

```text
VALID
REVALIDATION_REQUIRED
UNKNOWN
```

Поэтому принятый факт может существовать исторически, но требовать повторной проверки для новой базовой ревизии.

## Жизненные циклы модулей проверки

`Architecture Review`, `Test Engineering` и `Code Quality Review` имеют собственные правила жизненного цикла.

Например, действие по устранению в `Code Quality Review` может быть `COMPLETED`, но вывод не становится автоматически `RESOLVED`:

```text
CQRA COMPLETED
  !=
CQ RESOLVED
```

После устранения требуется повторная проверка вывода на новых доказательствах.

## Актуальность проекций

У проекции есть отдельное измерение актуальности:

```text
CURRENT
STALE
BLOCKED
```

`STALE` означает: документ больше не подтверждён как актуальное представление своих зависимостей.

Это не означает:

```text
семантический источник истины неверен
```

И наоборот, проекция `CURRENT` может честно отображать частично известное или неизвестное семантическое состояние.

## Актуальность семантики не равна актуальности проекции

Ключевое различие:

```text
семантическая повторная проверка `REVALIDATE`
  !=
пересборка проекции
```

После принятого семантического изменения выполняется `Projection Impact Analysis`. Она отмечает затронутые проекции, но не переписывает их.

Если нужен новый актуальный документ, создаётся отдельный сеанс пересборки `RG-*`.

## Повторная проверка после изменения проекта

Для принятого пакета результатов используется ограниченная по области последовательность:

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

Git diff используется для маршрутизации, а не как доказательство.

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
