# Документация Architecture Code Review

`architecture-code-review` — набор инженерных проверок для анализа существующих
программных систем. Документация построена по принципу постепенного раскрытия:
от первого запуска и типовых сценариев — к модели работы, затем к справочникам
и эксплуатационным процедурам.

## Текущий статус

Актуальная принятая базовая точка, завершённые этапы и последнее promotion:
[Current Project Status](current-status.md). Текущий baseline включает
Federated Product Audit Coordination для координации нескольких дочерних
репозиториев из общего non-Git Coordination Root без превращения этого каталога
в Product, Project или semantic authority.

## С чего начать

Если вы впервые используете этот инструмент:

1. [Установка](getting-started/installation.md)
2. [Быстрый старт](getting-started/quick-start.md)
3. [Первый полный запуск](getting-started/first-review.md)

## Основные понятия

- [Review Suite и модули проверки](concepts/review-suite.md) — что можно выбрать и как независимые проверки работают вместе.
- [Доказательства и Shared Technical Model](concepts/evidence-and-technical-model.md) — как фиксируются наблюдения и принимаются общие технические факты.
- [Источники истины и происхождение выводов](concepts/authority-and-provenance.md) — где хранится авторитетное состояние и как проследить вывод до исходного кода.
- [Жизненный цикл и актуальность](concepts/lifecycle-and-freshness.md) — что означают `CURRENT`, `STALE`, `VALID`, повторная проверка и замещение старых записей новыми.
- [Проекции и пакеты результатов](concepts/projections-and-packages.md) — как человекочитаемые документы отделены от семантического источника истины.

## Практические руководства

- [Architecture Review](guides/architecture-review.md)
- [Test Engineering](guides/test-engineering.md)
- [Code Quality Review](guides/code-quality-review.md)
- [Change Review: branch, commit и pull request](guides/change-review.md)
- [Повторное использование, изменения и Product coordination](guides/reuse-and-change.md) — включая top-down и bottom-up federated Product flow, переиспользование child audits и exact Product requalification.

## Справочник

- [Артефакты и состояние](reference/artifacts.md)
- [Процессы и `Session Intent`](reference/workflows.md)
- [Итоговые документы](reference/outputs.md)
- [Идентификаторы и статусы](reference/identifiers-and-statuses.md)
- [Глоссарий](reference/glossary.md)

## Где искать подробные правила

Чтобы одинаковые правила не расходились между руководствами, у каждого вида
подробного объяснения есть одна каноническая человеческая страница:

- [справочник процессов](reference/workflows.md) — сценарии `Session Intent`, включая `CHANGE_REVIEW` и контекстный `RECONCILE_CHANGE`;
- [жизненный цикл и актуальность](concepts/lifecycle-and-freshness.md) —
  состояние, повторная проверка и актуальность;
- [проекции и пакеты результатов](concepts/projections-and-packages.md) —
  проекции, пересборка и состав пакета;
- [справочник артефактов](reference/artifacts.md) — сохраняемые записи;
- [справочник итоговых документов](reference/outputs.md) — выбираемые и
  обязательные документы;
- [повторное использование, изменения и Product coordination](guides/reuse-and-change.md) — практический federated Product workflow. Нормативные правила Product membership, exact baseline, frozen coordination plan и revalidation остаются в `references/`.

Другие страницы дают контекст для своей аудитории и ссылаются на эти источники
за полными правилами.

## Эксплуатация

- [Обновление и откат](operations/upgrade-and-rollback.md)
- [Совместимость и миграция](operations/compatibility-and-migration.md)
- [Диагностика проблем](operations/troubleshooting.md)

## Сквозные примеры

- [Архитектурный аудит устаревшей серверной системы](examples/architecture-review.md)
- [Анализ качества тестов](examples/test-engineering.md)
- [Code Quality Review](examples/code-quality-review.md)
- [Повторная проверка после изменений](examples/revalidation.md)

Для pre-merge проверки branch/commit/PR используйте
[Change Review](guides/change-review.md), а не обычный `REVALIDATE`.

Для большого продукта из нескольких child repositories используйте Product
coordination: существующие принятые child audits сначала квалифицируются и
переиспользуются, а Product baseline принимается только после stable barrier и
точной requalification всего выбранного member/source vector.

## Нормативные источники

Документы в `docs/` предназначены для человека. Они объясняют устройство и
использование инструмента, но не являются исполняемыми контрактами агента.

Нормативная семантика находится в:

```text
SKILL.md
references/
capabilities/test-review/
capabilities/code-quality-review/
```

Если объяснение в `docs/` расходится с нормативным контрактом, приоритет имеет нормативный контракт. Такое расхождение считается дефектом документации и должно быть исправлено.
