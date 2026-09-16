# Документация Architecture Code Review

`architecture-code-review` — набор skills для инженерного анализа существующих программных систем. Документация разделена по задачам: сначала — установка и первый запуск, затем — рабочие сценарии, после этого — концепции, справочники и эксплуатация самого skill.

Если вы впервые здесь, начните не с `references/`, а с пользовательских руководств ниже.

## Быстрый маршрут

1. [Установка](getting-started/installation.md)
2. [Быстрый старт](getting-started/quick-start.md)
3. [Первый полный аудит](getting-started/first-review.md)
4. [Жизненный цикл аудита](guides/audit-lifecycle.md)
5. [Что делать после изменения кода](guides/after-code-changes.md)
6. [Практические рецепты](guides/common-recipes.md)

## Текущий статус разработки skill

Актуальная принятая базовая точка, завершённые этапы и последнее promotion:
[Current Project Status](current-status.md).

Текущий baseline включает federated Product coordination и Finding Lifecycle & Progress Reporting: current/historical views, baseline progress, accepted risk и conservative stale-resolution handling.

## Что читать в зависимости от задачи

| Задача | Документ |
|---|---|
| Установить skill | [Установка](getting-started/installation.md) |
| Быстро начать работу | [Быстрый старт](getting-started/quick-start.md) |
| Провести первый серьёзный запуск | [Первый полный аудит](getting-started/first-review.md) |
| Понять весь жизненный цикл работы | [Жизненный цикл аудита](guides/audit-lifecycle.md) |
| Код изменился после аудита | [Что делать после изменения кода](guides/after-code-changes.md) |
| Нужен готовый пример запроса | [Практические рецепты](guides/common-recipes.md) |
| Понять, что хранится в пакете | [Структура пакета аудита](guides/audit-package-structure.md) |
| Провести Architecture Review | [Architecture Review](guides/architecture-review.md) |
| Проверить Test Engineering | [Test Engineering](guides/test-engineering.md) |
| Провести Code Quality Review | [Code Quality Review](guides/code-quality-review.md) |
| Проверить branch/commit/PR | [Change Review](guides/change-review.md) |
| Переиспользовать старый аудит или Product state | [Повторное использование и изменения](guides/reuse-and-change.md) |
| Найти точный Session Intent | [Справочник процессов](reference/workflows.md) |
| Найти точный артефакт или ID | [Справочник артефактов](reference/artifacts.md) |
| Обновить сам skill | [Обновление самого skill и откат](operations/upgrade-and-rollback.md) |
| Разобраться с несовместимостью | [Совместимость и миграция](operations/compatibility-and-migration.md) |
| Диагностировать проблему | [Диагностика проблем](operations/troubleshooting.md) |

## Основные понятия

- [Review Suite и модули проверки](concepts/review-suite.md) — что можно выбрать и как независимые проверки работают вместе.
- [Доказательства и Shared Technical Model](concepts/evidence-and-technical-model.md) — как фиксируются наблюдения и принимаются общие технические факты.
- [Источники истины и происхождение выводов](concepts/authority-and-provenance.md) — кто владеет смыслом и как проследить conclusion до source.
- [Жизненный цикл и актуальность](concepts/lifecycle-and-freshness.md) — `ACTIVE`, `RESOLVED`, `SUPERSEDED`, freshness, reopening, progress и accepted risk.
- [Проекции и пакеты результатов](concepts/projections-and-packages.md) — почему человекочитаемый документ не является semantic authority.

## Практические руководства

### [Жизненный цикл аудита](guides/audit-lifecycle.md)

Общий путь от первого запуска до длительного сопровождения:

```text
NEW
→ evidence
→ Shared Technical Model
→ capability authorities
→ projections
→ source change
→ CHANGE_REVIEW / REVALIDATE
→ reconciliation
→ next accepted baseline
```

Это основной документ, если нужно понять систему целиком.

### [Что делать после изменения кода](guides/after-code-changes.md)

Пошаговая инструкция для branch, commit, pull request, merge, dependency/config change, Product child update, stale findings и projection regeneration.

Главное различие:

```text
candidate change   → CHANGE_REVIEW
current source     → REVALIDATE
accepted candidate → RECONCILE_CHANGE
```

### [Практические рецепты](guides/common-recipes.md)

Готовые prompts для обычных задач: первый аудит, PR review, revalidation после merge, добавление Target Architecture, API documentation, Product coordination и другие сценарии.

### [Структура пакета аудита](guides/audit-package-structure.md)

Объясняет человеческим языком, что такое `working/INDEX.md`, `WS-*`, `EV-*`, STM, `RF-*`, Test Engineering, `CQ-*`, `PRJ-*` и Product state.

### Capability guides

- [Architecture Review](guides/architecture-review.md)
- [Test Engineering](guides/test-engineering.md)
- [Code Quality Review](guides/code-quality-review.md)
- [Change Review](guides/change-review.md)
- [Повторное использование, изменения и Product coordination](guides/reuse-and-change.md)

## Справочник

Справочники нужны, когда уже понятен общий процесс и требуется точное правило.

- [Артефакты и состояние](reference/artifacts.md)
- [Процессы и `Session Intent`](reference/workflows.md)
- [Итоговые документы](reference/outputs.md)
- [Идентификаторы и статусы](reference/identifiers-and-statuses.md)
- [Глоссарий](reference/glossary.md)

## Эксплуатация самого skill

Раздел `operations/` относится прежде всего к **самому установленному `architecture-code-review`**, а не к изменению исходного кода анализируемого проекта.

- [Обновление самого skill и откат](operations/upgrade-and-rollback.md)
- [Совместимость и миграция](operations/compatibility-and-migration.md)
- [Диагностика проблем](operations/troubleshooting.md)

Если изменился анализируемый проект, используйте [Что делать после изменения кода](guides/after-code-changes.md), а не руководство по `git pull` самого skill.

## Сквозные примеры

- [Архитектурный аудит устаревшей серверной системы](examples/architecture-review.md)
- [Анализ качества тестов](examples/test-engineering.md)
- [Code Quality Review](examples/code-quality-review.md)
- [Повторная проверка после изменений](examples/revalidation.md)

## Где искать подробные правила

Чтобы одинаковые правила не расходились между руководствами, у каждой темы есть предпочтительный источник для человека:

- `Session Intent`, условия входа и остановки — [reference/workflows.md](reference/workflows.md);
- lifecycle/freshness — [concepts/lifecycle-and-freshness.md](concepts/lifecycle-and-freshness.md);
- projections — [concepts/projections-and-packages.md](concepts/projections-and-packages.md);
- сохраняемые записи — [reference/artifacts.md](reference/artifacts.md);
- outputs — [reference/outputs.md](reference/outputs.md);
- изменение исходного кода — [guides/after-code-changes.md](guides/after-code-changes.md);
- длительный цикл аудита — [guides/audit-lifecycle.md](guides/audit-lifecycle.md);
- Product coordination — [guides/reuse-and-change.md](guides/reuse-and-change.md).

## Как читать результаты

Удобный путь от общего к доказательствам:

```text
summary / report
  ↓
owner semantic record
  ↓
Shared Technical Model или связанная authority
  ↓
WS-* / EV-*
  ↓
source
```

Подробно: [Структура пакета аудита](guides/audit-package-structure.md).

## Нормативные источники

Документы в `docs/` и `README.md` предназначены для человека. Они объясняют уже принятую модель, но не являются исполняемыми контрактами агента.

Нормативная семантика находится в:

```text
SKILL.md
references/
capabilities/test-review/
capabilities/code-quality-review/
```

Если пользовательская документация расходится с нормативным контрактом, приоритет имеет нормативный контракт. Такое расхождение считается дефектом документации и должно быть исправлено.
