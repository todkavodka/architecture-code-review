# Быстрый старт

Этот раздел показывает минимальный путь от запуска skill до первого полезного результата. Здесь нет необходимости заранее разбираться во внутренних идентификаторах и форматах пакета аудита.

Точные имена состояний и процессов (`NEW`, `REVALIDATE`, `CHANGE_REVIEW` и другие) оставлены без перевода, потому что это нормативные идентификаторы. Обычное объяснение вокруг них дано на русском языке.

## 1. Откройте анализируемый проект

Запустите агента в корне проекта, который нужно проверить.

Для Product, состоящего из нескольких репозиториев, можно запускаться из общего каталога координации, но сам каталог не становится Product автоматически.

## 2. Попросите использовать skill

Минимальный запрос:

```text
Используй architecture-code-review для этого проекта.
```

Skill сначала должен определить:

- выбранный репозиторий или набор репозиториев;
- базовую ревизию;
- существующие пакеты аудита;
- возможность переиспользовать уже принятые результаты;
- подходящий сценарий работы.

Если пригодное состояние уже существует, новый полный аудит не должен запускаться автоматически.

## 3. Выберите, что нужно получить

Для нового аудита (`NEW`) доступны три независимых направления:

```text
[ ] Architecture Review
[ ] Test Engineering
[ ] Code Quality Review
```

Пользователь может выбрать один или несколько модулей либо допустимый самостоятельный итоговый документ. Главное — чтобы запрошенная работа была непустой.

### Architecture Review

Для архитектурной проверки выбираются глубина и конечный результат:

```text
Depth:
  STANDARD_FULL
  FORENSIC

Endpoint:
  REVIEW_ONLY
  REVIEW_PLUS_TARGET_ARCHITECTURE
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

`STANDARD_FULL` подходит для большинства полных аудитов. `FORENSIC` нужен там, где особенно важны спорные границы, конкурентность, чувствительные пути выполнения, сложный жизненный цикл и подробная история доказательств.

### Test Engineering

При включённом Test Engineering обязательна Test Assurance. Дополнительно можно запросить:

```text
Test Plan
Contract Consistency Report
Test Environment Design
Service Simulator Design
Service Simulator Implementation Plan
E2E Test Plan
```

Сгенерированный тестовый случай сам по себе не означает `TESTED`. Для этого нужны принятые доказательства фактического исполнения на нужной ревизии и в нужном окружении.

### Code Quality Review

Можно запросить:

```text
Findings View / Report
Code Quality Summary
Maintainability Hotspots
Roadmap Contribution
```

Code Quality Review создаёт finding только тогда, когда подтверждены конкретный механизм реализации и его существенное последствие.

## 4. При необходимости выберите техническую документацию

После настройки основных направлений можно запросить самостоятельные представления, например:

- Provided Interfaces;
- Consumed Interfaces;
- Integrations;
- Auth and Trust;
- Failure Behavior;
- другие зарегистрированные представления.

Это не четвёртый capability.

Если нужен подробный API Report, полнота интерфейсного списка должна быть доказана отдельно. Наличие нескольких найденных endpoints не даёт права объявлять список полным.

## 5. Подтвердите итоговую конфигурацию

Перед содержательной работой skill должен показать, что именно будет выполнено.

Проверьте:

- выбранные capabilities;
- выбранные outputs;
- архитектурную глубину и endpoint, если используется Architecture Review;
- текущий baseline;
- Product context, если он есть;
- ограничения и недоступные источники.

После подтверждения начинается исследование.

## 6. Что происходит во время анализа

Skill создаёт или переиспользует:

- доказательства;
- Shared Technical Model;
- записи выбранных направлений проверки;
- состояние координации;
- выбранные итоговые документы.

Не нужно вручную просить создать `WS-*`, `EV-*`, STM или finding IDs. Это внутренние механизмы трассировки и повторного использования.

## 7. Как читать результат

Начинайте с основного отчёта или summary.

Если нужно проверить происхождение конкретного вывода, двигайтесь глубже:

```text
summary / report
  ↓
semantic record
  ↓
Shared Technical Model
  ↓
evidence
  ↓
source
```

Подробно: [Структура пакета аудита](../guides/audit-package-structure.md).

## 8. После первого аудита не начинайте всё заново

После принятого аудита выбирайте сценарий по ситуации:

```text
незавершённая работа, тот же baseline → RESUME
ветка / commit / PR до принятия       → CHANGE_REVIEW
код уже стал текущим                  → REVALIDATE
принять проверенный candidate         → RECONCILE_CHANGE
добавить новую работу                 → EXTEND
использовать готовый результат        → USE_EXISTING
исправить только представление        → PROJECTION_REPAIR
```

Полный разбор: [Что делать после изменения кода](../guides/after-code-changes.md).

## 9. Три минимальных примера

### Только архитектурный аудит

```text
Используй architecture-code-review.
Нужен новый Architecture Review: STANDARD_FULL, REVIEW_ONLY.
Test Engineering и Code Quality Review не включай.
```

### Только Test Engineering

```text
Используй architecture-code-review.
Нужен Test Engineering: Test Assurance + Test Plan.
Architecture Review и Code Quality Review не включай.
```

### Только Code Quality

```text
Используй architecture-code-review.
Нужен Code Quality Review: Findings View + Summary.
Architecture Review и Test Engineering не включай.
```

## 10. Проверить pull request

```text
Используй architecture-code-review.
Сделай CHANGE_REVIEW принятого baseline против pull request #123.
Ничего не принимай автоматически.
```

## 11. После merge

Если код уже считается текущим состоянием:

```text
Используй существующий пакет аудита.
Код уже принят в main.
Выполни REVALIDATE только затронутого состояния и затем покажи влияние на итоговые документы.
```

## 12. Куда идти дальше

Если это первый серьёзный запуск:

- [Первый полный аудит](first-review.md)
- [Жизненный цикл аудита](../guides/audit-lifecycle.md)
- [Что делать после изменения кода](../guides/after-code-changes.md)
- [Практические рецепты](../guides/common-recipes.md)
- [Структура пакета аудита](../guides/audit-package-structure.md)

Если нужен точный справочник:

- [Session Intent и процессы](../reference/workflows.md)
- [Артефакты](../reference/artifacts.md)
- [Итоговые документы](../reference/outputs.md)
- [Идентификаторы и статусы](../reference/identifiers-and-statuses.md)
