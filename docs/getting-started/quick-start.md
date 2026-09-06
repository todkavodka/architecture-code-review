# Быстрый старт

Этот раздел показывает минимальный путь от запроса к первому полезному результату без необходимости заранее понимать внутренние идентификаторы Skill.

## 1. Откройте repository

Запустите агента в корне проекта, который нужно проверить.

## 2. Попросите использовать Skill

Минимальный запрос:

```text
Используй architecture-code-review для этого проекта.
```

Skill сначала определит repository, baseline, существующие audit packages и рекомендуемый Session Intent. Он не должен автоматически начинать новый полный аудит, если уже существует пригодное состояние.

## 3. Выберите, что нужно проверить

Для `NEW` показывается Review Suite:

```text
Review Suite

[ ] Architecture Review
[ ] Test Engineering
[ ] Code Quality Review
```

Нужно выбрать хотя бы одну capability.

### Architecture Review

Если нужна архитектурная диагностика, выберите depth и endpoint независимо:

```text
Depth:
  STANDARD_FULL
  FORENSIC

Endpoint:
  REVIEW_ONLY
  REVIEW_PLUS_TARGET_ARCHITECTURE
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

`STANDARD_FULL` подходит для большинства полных аудитов. `FORENSIC` нужен, когда особенно важны спорные границы, конкурентность, security-sensitive paths, сложные lifecycle и детальная история доказательств.

### Test Engineering

`Test Assurance` обязателен при включённой Test Engineering. Остальные документы выбираются по задаче:

```text
Test Assurance                    required
Test Plan                         optional
Contract Consistency Report       optional
Test Environment Design           optional
Service Simulator Design          optional
Service Simulator Implementation Plan optional
E2E Test Plan                     optional
```

### Code Quality Review

Выберите только нужные человекочитаемые проекции:

```text
Findings View/Report
Code Quality Summary
Maintainability Hotspots
Roadmap Contribution
```

Их выбор не создаёт findings автоматически. `CQ-*` появляется только после evidence-backed проверки material consequence.

## 4. Дайте Skill выполнить discovery

Во время анализа Skill создаёт или переиспользует:

- baseline-bound evidence;
- Shared Technical Model;
- capability-specific semantic records;
- workflow state в `working/INDEX.md`;
- выбранные итоговые документы.

Не нужно вручную просить создать `WS-*`, `EV-*` или STM. Это внутренние механизмы трассировки и повторного использования.

## 5. Читайте результат с верхнего уровня

Для первого чтения используйте основной report/summary выбранной capability. В owning semantic records и evidence переходите только когда нужно проверить происхождение конкретного вывода.

Типичный путь проверки:

```text
main report / summary
  -> finding or semantic record
  -> STM / evidence reference
  -> source code or external source
```

## 6. Не запускайте всё заново после каждого изменения

Если audit уже принят:

- проект изменился → `REVALIDATE`;
- нужен новый output или capability → `EXTEND`;
- нужно продолжить незавершённую работу → `RESUME`;
- нужен уже принятый результат → `USE_EXISTING`;
- сломан только Markdown/Mermaid/wording → `PROJECTION_REPAIR`.

Подробности: [Повторное использование и изменения](../guides/reuse-and-change.md).

## Три минимальных примера

### Только архитектурный аудит

```text
Используй architecture-code-review.
Нужен новый Architecture Review: STANDARD_FULL, REVIEW_ONLY.
Test Engineering и Code Quality не включай.
```

### Только качество тестов

```text
Используй architecture-code-review.
Нужен новый Test Engineering review: Test Assurance + Test Plan.
Architecture и Code Quality не включай.
```

### Только качество реализации

```text
Используй architecture-code-review.
Нужен новый Code Quality Review: Findings View + Summary.
Architecture и Test Engineering не включай.
```

## Дальше

Если это первый серьёзный запуск, прочитайте [Первый полный запуск](first-review.md). Для выбора итоговых документов используйте [Output Reference](../reference/outputs.md).
