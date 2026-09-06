# Документация Architecture Code Review

`architecture-code-review` — набор инженерных проверок для анализа существующих
программных систем. Документация построена по принципу постепенного раскрытия:
от первого запуска и типовых сценариев — к модели работы, затем к справочникам
и эксплуатационным процедурам.

## С чего начать

Если вы используете Skill впервые:

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
- [Повторное использование, изменения и расширение](guides/reuse-and-change.md)

## Справочник

- [Артефакты и состояние](reference/artifacts.md)
- [Процессы и `Session Intent`](reference/workflows.md)
- [Итоговые документы](reference/outputs.md)
- [Идентификаторы и статусы](reference/identifiers-and-statuses.md)
- [Глоссарий](reference/glossary.md)

## Эксплуатация

- [Обновление и откат](operations/upgrade-and-rollback.md)
- [Совместимость и миграция](operations/compatibility-and-migration.md)
- [Диагностика проблем](operations/troubleshooting.md)

## Сквозные примеры

- [Архитектурный аудит legacy backend](examples/architecture-review.md)
- [Анализ качества тестов](examples/test-engineering.md)
- [Code Quality Review](examples/code-quality-review.md)
- [Повторная проверка после изменений](examples/revalidation.md)

## Нормативные источники

Документы в `docs/` предназначены для человека. Они объясняют устройство и использование Skill, но не являются исполняемыми контрактами агента.

Нормативная семантика находится в:

```text
SKILL.md
references/
capabilities/test-review/
capabilities/code-quality-review/
```

Если объяснение в `docs/` расходится с нормативным контрактом, приоритет имеет нормативный контракт. Такое расхождение считается дефектом документации и должно быть исправлено.
