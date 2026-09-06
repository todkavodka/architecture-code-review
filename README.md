# Architecture Code Review

`architecture-code-review` — Skill для глубокого инженерного анализа существующих программных систем. Он помогает не просто собрать список замечаний, а построить проверяемую картину системы, связать выводы с доказательствами и сохранить результаты так, чтобы их можно было продолжать, перепроверять и расширять после изменений проекта.

Главный принцип:

> **Ширина утверждения не должна превышать ширину доказательств.**

## Для кого

Skill рассчитан на:

- архитекторов и технических лидов;
- senior/staff engineers;
- команды сопровождения legacy-систем;
- Test/QA Engineering;
- команды, готовящие модернизацию, миграцию или крупный refactoring;
- независимый технический аудит перед релизом, интеграцией или передачей системы.

## Какие задачи решает

Review Suite объединяет три независимые capability:

### Architecture Review

Восстанавливает фактическую архитектуру системы, проверяет ownership состояния и ресурсов, lifecycle, boundaries, concurrency, failure/recovery behavior, trust/security implications и подтверждённые архитектурные root problems.

При необходимости дополнительно строит Target Architecture и Remediation Roadmap.

### Test Engineering

Проверяет, какие существенные поведения действительно доказаны исполняемыми тестами, где остаются пробелы, согласованы ли contract representations и какие Test Plan, environment, simulator или E2E artifacts нужны.

### Code Quality Review

Находит не просто stylistic smells, а реализационные механизмы с доказуемым существенным последствием для сопровождаемости, надёжности, тестируемости, lifecycle, concurrency, dependencies, localization и других качеств.

Capability можно использовать отдельно или вместе. Ни одна из них не является обязательным родителем другой.

## Что вы получаете

В зависимости от выбранной конфигурации Skill может сформировать:

- Architecture Review;
- Authoritative Findings Ledger;
- Target Architecture;
- Remediation Roadmap;
- Test Assurance;
- Test Plan;
- Contract Consistency Report;
- Test Environment Design;
- Service Simulator Design;
- Service Simulator Implementation Plan;
- E2E Test Plan;
- Code Quality Findings View;
- Code Quality Summary;
- Maintainability Hotspots;
- Code Quality Roadmap Contribution.

Skill также сохраняет evidence, фактическую technical model, semantic records и coordinator state, чтобы последующие проверки не зависели от памяти конкретного чата или агента.

## Установка

Для Codex, OpenCode и других агентов, использующих `~/.agents/skills`:

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новую agent session.

Проверить установленную revision:

```bash
git -C ~/.agents/skills/architecture-code-review rev-parse HEAD
```

Подробно: [Установка, обновление и проверка](docs/getting-started/installation.md).

## Быстрый старт

Самый простой запрос:

```text
Используй architecture-code-review для этого проекта.
```

Skill сначала определит repository, baseline и существующие audit packages, затем предложит подходящий Session Intent.

Для нового аудита показывается Review Suite:

```text
[ ] Architecture Review
[ ] Test Engineering
[ ] Code Quality Review
```

Нужно выбрать хотя бы одну capability.

Architecture Review отдельно предлагает:

```text
Depth:
  STANDARD_FULL
  FORENSIC

Endpoint:
  REVIEW_ONLY
  REVIEW_PLUS_TARGET_ARCHITECTURE
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

Depth и endpoint независимы: любой из двух depth поддерживает любой из трёх endpoint.

## Примеры

### Архитектурный аудит

```text
Используй architecture-code-review.
Нужен новый Architecture Review: STANDARD_FULL, REVIEW_ONLY.
Test Engineering и Code Quality не включай.
```

### Анализ качества тестов

```text
Используй architecture-code-review.
Нужен Test Engineering review: Test Assurance + Test Plan.
Architecture и Code Quality не включай.
```

### Анализ качества реализации

```text
Используй architecture-code-review.
Нужен Code Quality Review: Findings View + Summary.
Architecture и Test Engineering не включай.
```

### Повторная проверка после изменений

```text
Используй существующий audit package и REVALIDATE изменения после прошлого accepted baseline.
```

Полные end-to-end scenarios: [Examples](docs/index.md#сквозные-примеры).

## Повторное использование результатов

Review Suite рассчитан на длительную жизнь audit package:

| Ситуация | Используйте |
|---|---|
| Начать новый аудит | `NEW` |
| Продолжить незавершённый | `RESUME` |
| Проверить изменения проекта | `REVALIDATE` |
| Добавить capability/output/endpoint | `EXTEND` |
| Использовать уже принятый результат | `USE_EXISTING` |
| Исправить только Markdown/Mermaid/wording | `PROJECTION_REPAIR` |

Изменившийся Git HEAD сам по себе не означает, что весь аудит нужно выполнять заново. `REVALIDATE` вычисляет затронутую область по dependency impact и сохраняет unaffected accepted state.

## Важные свойства

- Evidence и technical facts привязаны к конкретному baseline.
- Человекочитаемый report не становится источником истины только потому, что он существует.
- Semantic state и freshness итоговых документов отслеживаются отдельно.
- Новый output можно добавить через `EXTEND`, не повторяя unrelated accepted work.
- Presentation-only correction не имеет права менять accepted technical meaning.
- Legacy packages reconciles консервативно; старые результаты не переписываются молча.

## Документация

Начните с [Documentation Hub](docs/index.md).

Основные разделы:

- [Getting Started](docs/index.md#с-чего-начать)
- [Concepts](docs/index.md#основные-понятия)
- [Practical Guides](docs/index.md#практические-руководства)
- [Reference](docs/index.md#справочник)
- [Operations](docs/index.md#эксплуатация)
- [End-to-End Examples](docs/index.md#сквозные-примеры)

Терминология и canonical tokens: [Глоссарий](docs/reference/glossary.md).

Нормативные agent contracts находятся в `SKILL.md`, `references/` и `capabilities/*/references/`. Документация в `docs/` объясняет модель человеку и не создаёт параллельную authority.

## Лицензия

См. [`LICENSE`](LICENSE).
