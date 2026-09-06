# Повторное использование, изменения и расширение

`Review Suite` рассчитан на длительную жизнь пакета аудита. Принятое состояние
не нужно выбрасывать после каждого нового commit или запроса пользователя.
Полные условия входа, автоматические действия, остановки и результаты каждого
`Session Intent` определяет [справочник процессов](../reference/workflows.md).

## Выбор Session Intent

| Ситуация | Intent |
|---|---|
| Нет предыдущего audit | `NEW` |
| Workflow не закончен | `RESUME` |
| Accepted baseline изменился | `REVALIDATE` |
| Нужен новый capability/output/endpoint | `EXTEND` |
| Нужен существующий accepted deliverable | `USE_EXISTING` |
| Нужно исправить только presentation | `PROJECTION_REPAIR` |

## `RESUME`

Используйте, когда работа остановилась до полного closeout.

```text
RESUME
  -> validate INDEX bindings
  -> restore Review Suite read-only
  -> reconcile owning artifacts
  -> continue first non-accepted durable boundary
```

`RESUME` не является новым конфигуратором. Если пользователь хочет добавить
итоговый документ, используется `EXTEND`.

## `REVALIDATE`

Используйте после изменения accepted baseline.

Предыдущая конфигурация `Review Suite` показывается только для чтения. Область
повторной проверки вычисляется автоматически по зависимостям.

```text
previous baseline
  -> current baseline
  -> change inventory
  -> impact analysis
  -> minimum dependency slice
  -> fresh evidence
  -> revalidation
  -> delta reconciliation
```

### Что выбирает пользователь

Пользователь подтверждает baseline/change context и принимает решения там, где authority действительно неоднозначна.

Пользователь не выбирает заново модули и флажки документов для обычного
`REVALIDATE`.

### `SYSTEMIC` impact

Если targeted completion больше нельзя считать надёжным, Skill возвращает:

```text
FULL_REAUDIT_RECOMMENDED
user_decision_required: true
```

Полный audit не запускается без решения пользователя.

## `EXTEND`

Используйте, когда accepted package нужно расширить.

```text
Existing / preserved [READ-ONLY]
Available additions [USER SELECTABLE]
```

Persisted result:

```text
previous accepted selection
UNION explicit additions
UNION required dependencies
```

### Добавление capability

Если Architecture Review отсутствовала, её можно добавить и выбрать depth/endpoint.

Если модуль уже существует, принятая конфигурация не открывается как новое меню
`NEW`.

### Architecture endpoint extension

Для existing Architecture endpoint extension monotonic:

```text
REVIEW_ONLY
  -> REVIEW_PLUS_TARGET_ARCHITECTURE
  -> REVIEW_PLUS_TARGET_AND_ROADMAP
```

Из `REVIEW_ONLY` можно сразу запросить Target + Roadmap.

Выбранная глубина остаётся доступной только для чтения. Смена
`STANDARD_FULL` ↔ `FORENSIC` не является обычным добавлением результата.

### Test/Code Quality additions

Показываются только ещё не выбранные документы. Уже выбранные документы
сохраняются.

## `USE_EXISTING`

Используйте, когда accepted state и required projections подходят без новой technical work.

Skill проверяет:

- package usability;
- authority/revision bindings;
- required projection freshness;
- выбранный deliverable.

Новый scope через `USE_EXISTING` не добавляется.

## `PROJECTION_REPAIR`

Используйте, если нужно исправить presentation уже принятого смысла:

- grammar/language;
- Markdown;
- Mermaid syntax/layout;
- links/navigation;
- table formatting;
- terminology;
- cross-references.

Target выбирается из eligible registered `PRJ-*` projections accepted package.

Если correction меняет technical meaning:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

## Projection regeneration

`REVALIDATE` и анализ влияния на проекции не пересобирают документы
автоматически.

Если после semantic change нужен fresh output:

```text
explicit freshness request
  -> RG-* session
  -> requested projection + stale prerequisites
  -> verification
```

## Пример жизненного цикла

```text
Day 1: NEW Architecture REVIEW_ONLY
Day 10: EXTEND -> add Target Architecture
Day 30: code changed -> REVALIDATE affected slice
Day 31: Summary became STALE -> explicit RG-* if fresh summary needed
Day 45: broken Mermaid -> PROJECTION_REPAIR
Day 60: USE_EXISTING accepted current report
```

## Что читать дальше

- [Workflow Reference](../reference/workflows.md)
- [Lifecycle and freshness](../concepts/lifecycle-and-freshness.md)
- [Revalidation example](../examples/revalidation.md)
