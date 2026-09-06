# Быстрый старт

Этот раздел показывает минимальный путь от запроса к первому полезному результату без необходимости заранее разбираться во внутренних идентификаторах Skill.

## 1. Откройте репозиторий

Запустите агента в корне проекта, который нужно проверить.

## 2. Попросите использовать Skill

Минимальный запрос:

```text
Используй architecture-code-review для этого проекта.
```

Skill сначала определит репозиторий, базовую ревизию, существующие пакеты аудита и рекомендуемый Session Intent. Новый полный аудит не должен запускаться автоматически, если уже существует пригодное сохранённое состояние.

## 3. Выберите, что нужно проверить

Для `NEW` показывается Review Suite:

```text
Review Suite

[ ] Architecture Review
[ ] Test Engineering
[ ] Code Quality Review
```

Нужно выбрать хотя бы один модуль проверки.

### Architecture Review

Если нужна архитектурная диагностика, отдельно выберите глубину и конечный результат:

```text
Depth:
  STANDARD_FULL
  FORENSIC

Endpoint:
  REVIEW_ONLY
  REVIEW_PLUS_TARGET_ARCHITECTURE
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

`STANDARD_FULL` подходит для большинства полных аудитов. `FORENSIC` нужен, когда особенно важны спорные границы, конкурентность, чувствительные к безопасности пути выполнения, сложный жизненный цикл и подробная история доказательств.

### Test Engineering

`Test Assurance` обязателен при включённом Test Engineering. Остальные документы выбираются по задаче:

```text
Test Assurance                         required
Test Plan                              optional
Contract Consistency Report            optional
Test Environment Design                optional
Service Simulator Design               optional
Service Simulator Implementation Plan  optional
E2E Test Plan                          optional
```

### Code Quality Review

Выберите только те человекочитаемые документы, которые действительно нужны:

```text
Findings View/Report
Code Quality Summary
Maintainability Hotspots
Roadmap Contribution
```

Выбор документа не создаёт `CQ-*` автоматически. `CQ-*` появляется только после того, как конкретный механизм реализации подтверждён доказательствами и для него установлено существенное последствие.

## 4. Дайте Skill провести исследование

Во время анализа Skill создаёт или переиспользует:

- доказательства, привязанные к базовой ревизии;
- Shared Technical Model;
- записи выбранных модулей проверки;
- состояние процесса в `working/INDEX.md`;
- выбранные итоговые документы.

Не нужно вручную просить создать `WS-*`, `EV-*` или STM. Это внутренние механизмы трассировки и повторного использования результатов.

## 5. Читайте результат с верхнего уровня

Для первого чтения используйте основной отчёт или краткое резюме выбранного модуля. К авторитетным semantic records и evidence следует переходить только тогда, когда нужно проверить происхождение конкретного вывода.

Типичный путь проверки:

```text
основной отчёт / summary
  -> finding или другая semantic record
  -> STM / ссылка на evidence
  -> исходный код или внешний источник
```

Термины `semantic record`, `finding` и `evidence` подробно объяснены в [глоссарии](../reference/glossary.md); в нормативных контрактах эти canonical terms сохраняются без переименования.

## 6. Не запускайте всё заново после каждого изменения

Если аудит уже принят:

- проект изменился → `REVALIDATE`;
- нужен новый итоговый документ или модуль проверки → `EXTEND`;
- нужно продолжить незавершённую работу → `RESUME`;
- нужен уже принятый результат → `USE_EXISTING`;
- сломано только оформление, Markdown, Mermaid или формулировки → `PROJECTION_REPAIR`.

Подробности: [Повторное использование и изменения](../guides/reuse-and-change.md).

## Три минимальных примера

### Только архитектурный аудит

```text
Используй architecture-code-review.
Нужен новый Architecture Review: STANDARD_FULL, REVIEW_ONLY.
Test Engineering и Code Quality Review не включай.
```

### Только качество тестов

```text
Используй architecture-code-review.
Нужен Test Engineering: Test Assurance + Test Plan.
Architecture Review и Code Quality Review не включай.
```

### Только качество реализации

```text
Используй architecture-code-review.
Нужен Code Quality Review: Findings View + Summary.
Architecture Review и Test Engineering не включай.
```

## Дальше

Если это первый серьёзный запуск, прочитайте [Первый полный запуск](first-review.md). Для выбора итоговых документов используйте [справочник итоговых документов](../reference/outputs.md).
