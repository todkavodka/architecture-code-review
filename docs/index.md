# Документация Architecture Code Review

`architecture-code-review` — набор skills для инженерного анализа существующих программных систем. Документация организована по задачам: сначала установка и первый запуск, затем рабочие сценарии, после этого — объяснение модели, справочники и эксплуатация самого skill.

Если вы впервые знакомитесь с проектом, начинайте не с `references/`, а с пользовательских руководств.

## Быстрый маршрут

1. [Установка](getting-started/installation.md)
2. [Быстрый старт](getting-started/quick-start.md)
3. [Первый полный аудит](getting-started/first-review.md)
4. [Жизненный цикл аудита](guides/audit-lifecycle.md)
5. [Что делать после изменения кода](guides/after-code-changes.md)
6. [Практические рецепты](guides/common-recipes.md)

## Текущий статус разработки skill

Актуальная принятая точка, завершённые этапы и последнее продвижение изменений в `main` описаны в [Current Project Status](current-status.md).

Текущая версия поддерживает в том числе:

- координацию Product, состоящего из нескольких дочерних репозиториев;
- переиспользование принятых дочерних аудитов;
- раздельное отображение текущих и исторических findings;
- прогресс между принятыми baseline;
- отдельное отображение принятого остаточного риска;
- безопасную повторную проверку ранее закрытых findings после изменения исходного кода.

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
| Проверить достаточность тестов | [Test Engineering](guides/test-engineering.md) |
| Провести Code Quality Review | [Code Quality Review](guides/code-quality-review.md) |
| Проверить ветку, commit или pull request | [Change Review](guides/change-review.md) |
| Переиспользовать существующий аудит или Product state | [Повторное использование и изменения](guides/reuse-and-change.md) |
| Найти точный `Session Intent` | [Справочник процессов](reference/workflows.md) |
| Найти точный артефакт или идентификатор | [Справочник артефактов](reference/artifacts.md) |
| Обновить сам skill | [Обновление самого skill и откат](operations/upgrade-and-rollback.md) |
| Разобраться с несовместимостью | [Совместимость и миграция](operations/compatibility-and-migration.md) |
| Диагностировать проблему | [Диагностика проблем](operations/troubleshooting.md) |

## Основные понятия

- [Review Suite и направления проверки](concepts/review-suite.md) — что можно выбрать и как независимые направления работают вместе.
- [Доказательства и Shared Technical Model](concepts/evidence-and-technical-model.md) — как фиксируются наблюдения и принимаются общие технические факты.
- [Источники истины и происхождение выводов](concepts/authority-and-provenance.md) — кто владеет смыслом записи и как проследить вывод до исходного источника.
- [Жизненный цикл и актуальность](concepts/lifecycle-and-freshness.md) — `ACTIVE`, `RESOLVED`, `SUPERSEDED`, freshness, повторное открытие, прогресс и принятый риск.
- [Проекции и пакеты результатов](concepts/projections-and-packages.md) — почему человекочитаемый документ не является семантическим источником истины.

## Практические руководства

### [Жизненный цикл аудита](guides/audit-lifecycle.md)

Общий путь от первого запуска до длительного сопровождения:

```text
NEW
→ доказательства
→ Shared Technical Model
→ владельцы семантического состояния
→ человекочитаемые проекции
→ изменение исходного кода
→ CHANGE_REVIEW / REVALIDATE
→ принятие изменений
→ следующий accepted baseline
```

Это основной документ, если нужно понять систему целиком.

### [Что делать после изменения кода](guides/after-code-changes.md)

Пошаговая инструкция для ветки, commit, pull request, merge, изменения зависимостей и конфигурации, обновления дочернего Project, устаревших findings и повторной генерации документов.

Главное различие:

```text
изменение ещё candidate        → CHANGE_REVIEW
код уже является current source → REVALIDATE
проверенный candidate принят    → RECONCILE_CHANGE
```

### [Практические рецепты](guides/common-recipes.md)

Готовые запросы для обычных задач: первый аудит, проверка PR, повторная проверка после merge, добавление Target Architecture, технической документации API, координация Product и другие сценарии.

### [Структура пакета аудита](guides/audit-package-structure.md)

Объясняет человеческим языком, что такое `working/INDEX.md`, `WS-*`, `EV-*`, Shared Technical Model, `RF-*`, Test Engineering, `CQ-*`, `PRJ-*` и состояние Product.

### Руководства по направлениям проверки

- [Architecture Review](guides/architecture-review.md)
- [Test Engineering](guides/test-engineering.md)
- [Code Quality Review](guides/code-quality-review.md)
- [Change Review](guides/change-review.md)
- [Повторное использование, изменения и координация Product](guides/reuse-and-change.md)

## Справочник

Справочник нужен, когда общий процесс уже понятен и требуется точное правило.

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

- [Архитектурный аудит сервиса заказов](examples/architecture-review.md)
- [Проверка достаточности тестов](examples/test-engineering.md)
- [Проверка качества реализации](examples/code-quality-review.md)
- [Адресная повторная проверка после изменения кода](examples/revalidation.md)

## Где искать точные правила

Чтобы одинаковые правила не расходились между руководствами, у каждой темы есть предпочтительный источник для человека:

- `Session Intent`, условия входа и остановки — [reference/workflows.md](reference/workflows.md);
- жизненный цикл и актуальность — [concepts/lifecycle-and-freshness.md](concepts/lifecycle-and-freshness.md);
- проекции — [concepts/projections-and-packages.md](concepts/projections-and-packages.md);
- сохраняемые записи — [reference/artifacts.md](reference/artifacts.md);
- итоговые документы — [reference/outputs.md](reference/outputs.md);
- изменение исходного кода — [guides/after-code-changes.md](guides/after-code-changes.md);
- длительный жизненный цикл аудита — [guides/audit-lifecycle.md](guides/audit-lifecycle.md);
- координация Product — [guides/reuse-and-change.md](guides/reuse-and-change.md).

## Как читать результаты

Удобный путь от общего к доказательствам:

```text
краткое резюме или отчёт
  ↓
владеющая семантическая запись
  ↓
Shared Technical Model или связанная authority
  ↓
WS-* / EV-*
  ↓
исходный код или другой источник
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
