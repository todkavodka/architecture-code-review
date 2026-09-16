# Повторное использование, изменения и расширение

`Review Suite` рассчитан на длительную жизнь пакета аудита. После первого анализа проект продолжает меняться, а результаты проверки должны по возможности переиспользоваться, а не создаваться заново.

Если код уже изменился и нужен пошаговый маршрут, начните с отдельного руководства [Что делать после изменения кода](after-code-changes.md). Если нужно понять весь путь от первого запуска до следующих baseline, смотрите [Жизненный цикл аудита](audit-lifecycle.md).

Полные условия входа, остановки и права записи описаны в [справочнике процессов](../reference/workflows.md). Здесь объясняется, какой сценарий выбирать в обычной работе.

| Ситуация | Сценарий | Последствие |
|---|---|---|
| Нет предыдущего аудита | `NEW` | Создаётся новый пакет и область проверки. |
| Работа не завершена и baseline совпадает | `RESUME` | Продолжается существующая незавершённая работа. |
| Нужно оценить branch, commit или pull request до принятия | `CHANGE_REVIEW` | Создаётся read-only candidate review без изменения принятого состояния. |
| Проект изменился и новое состояние уже считается текущим | `REVALIDATE` | Повторно проверяется только затронутое принятое состояние. |
| Есть пригодный завершённый Change Review и изменение нужно принять | контекстный `RECONCILE_CHANGE` | Candidate evidence передаётся существующим владельцам для принятия решений. |
| Нужен дополнительный модуль или документ | `EXTEND` | Добавляется новая работа, прежний выбор сохраняется. |
| Нужен уже принятый результат | `USE_EXISTING` | Новая техническая работа не запускается. |
| Исправлено только представление | `PROJECTION_REPAIR` | Технический смысл не меняется. |

## После изменения проекта

Сначала определите, что именно нужно сделать:

```text
оценить ещё не принятое изменение → CHANGE_REVIEW
переоценить уже текущий source    → REVALIDATE
принять проверенный candidate     → RECONCILE_CHANGE
```

Для ветки, commit или pull request, который ещё не должен считаться принятым состоянием, используйте `CHANGE_REVIEW`. Он сравнивает immutable `BASE` и `CANDIDATE`, но не меняет STM, findings, Test Engineering state, Contract Verification или freshness проекций.

Для source state, которое уже считается текущим, используйте `REVALIDATE`. Он определяет затронутую часть зависимостей и повторно проверяет только необходимый срез. Завершённый Change Review может быть входом для маршрутизации и доказательств, но не заменяет owner adjudication.

Если baseline изменился, обычный `RESUME` не продолжает работу так, будто старое accepted state всё ещё описывает текущий source. Он должен остановиться с `SOURCE_BASELINE_MISMATCH` и предложить подходящий маршрут: `CHANGE_REVIEW`, `REVALIDATE` и, при выполненных условиях, контекстный `RECONCILE_CHANGE`.

Подробный разбор merge, squash, conflict resolution, stale findings, dependency/config changes и Product child updates находится в [руководстве после изменения кода](after-code-changes.md).

## Принятие уже проверенного изменения

`RECONCILE_CHANGE` не является startup intent. Оно доступно только после завершённого пригодного Change Review и явного подтверждения пользователя.

Candidate slices направляются существующим владельцам STM, Architecture, Code Quality, Test Engineering и Contract Verification. Review-local `CR-*`, `CF-*` и `CRF-*` сами по себе не становятся canonical records.

Review base должен соответствовать текущему accepted baseline. Если accepted baseline успел измениться независимо, старого `A → B` review недостаточно для `A' → B`: нужен новый review либо полностью доказанная linked/supplemental chain. Partial reconciliation не продвигает весь baseline.

## Добавление результата

Для нового документа, модуля или дополнительного результата Architecture Review используйте `EXTEND`.

Уже принятые элементы сохраняются. Глубина существующего Architecture Review не меняется; его endpoint можно только расширять:

```text
REVIEW_ONLY
  ↓
REVIEW_PLUS_TARGET_ARCHITECTURE
  ↓
REVIEW_PLUS_TARGET_AND_ROADMAP
```

Если source baseline изменился и ещё не reconciled, `EXTEND` блокируется с `BASELINE_RECONCILIATION_REQUIRED`.

Полные правила: [раздел `EXTEND`](../reference/workflows.md#extend).

## Использование прежнего результата

`USE_EXISTING` подходит, если выбранный результат и его источники истины пригодны по политике пакета.

Старый принятый пакет можно использовать как исторический результат, но нельзя представлять его как current state для нового source baseline без reconciliation/revalidation.

## Исправление и пересборка представлений

`PROJECTION_REPAIR` предназначен только для языка, Markdown, Mermaid, навигации, таблиц и других presentation-only defects.

Если исправление меняет технический смысл, процесс должен вернуться в semantic workflow, а не маскировать semantic change как repair.

Анализ влияния на проекции не пересобирает документы. Candidate Change Review может только прогнозировать влияние. После принятого semantic change выполняется Projection Impact Analysis, а свежий документ получается отдельной явной regeneration `RG-*`.

Подробности: [жизненный цикл и актуальность](../concepts/lifecycle-and-freshness.md) и [проекции и пакеты](../concepts/projections-and-packages.md).

## Переиспользование Change Review после merge

Переиспользование не определяется совпадением branch name или commit ancestry.

Для `TREE_EQUIVALENT` требуется доказанный `WHOLE_TREE_EQUAL` либо `FROZEN_RELEVANT_SCOPE_EQUAL`.

Поэтому:

- clean no-ff merge может переиспользовать review;
- squash merge может переиспользовать review;
- conflict resolution требует осторожности;
- divergence требует дополнительной проверки;
- недоказанный partial cherry-pick нельзя считать эквивалентным.

Главное — доказательство эквивалентности содержимого, а не форма Git-истории.

## Координация аудита продукта

Продукт можно координировать из обычного каталога без Git, например:

```text
/projects/
├── backend/
├── frontend/
├── gateway/
└── shared/
```

Каталог является только Coordination Root. Файловая структура не определяет Product membership и не создаёт новый Project или repository.

### Top-down

Product coordinator обнаруживает изменившийся child Project, показывает Product Coordination Plan, запускает существующий child workflow, принимает стабильный локальный результат, повторно квалифицирует точный Product vector и только затем предлагает принять новый Product baseline.

### Bottom-up

Независимо проверенный child сначала получает собственный локальный accepted result. Product позже обнаруживает source/semantic authority advancement и выбирает Product `REVALIDATE` или полный-векторный `CHANGE_REVIEW` для read-only оценки кандидата.

Product baseline принимается отдельно и явно.

Таблицы состояния и готовности Product — производные представления, а не новая semantic authority.

## Когда старый результат действительно можно переиспользовать

Перед reuse полезно проверить четыре вещи:

1. совпадает ли или доказанно эквивалентен source binding;
2. остаются ли действительными semantic dependencies;
3. не продвинулась ли owner authority на том же source;
4. не стала ли нужная projection stale.

Если один из этих вопросов не закрыт, старый файл на диске ещё не означает пригодный current result.

## Практическая подсказка

```text
NEW                — создать новый audit scope
RESUME             — продолжить незавершённое на том же baseline
CHANGE_REVIEW      — проверить candidate до принятия
REVALIDATE         — обновить accepted state для current source
RECONCILE_CHANGE   — принять проверенный candidate через owners
EXTEND             — добавить новую работу
USE_EXISTING       — использовать готовое accepted state
PROJECTION_REPAIR  — исправить только представление
```

Готовые prompts: [Практические рецепты](common-recipes.md).

## См. также

- [Жизненный цикл аудита](audit-lifecycle.md)
- [Что делать после изменения кода](after-code-changes.md)
- [Практические рецепты](common-recipes.md)
- [Структура пакета аудита](audit-package-structure.md)
- [Change Review](change-review.md)
- [Справочник процессов](../reference/workflows.md)
- [Пример повторной проверки](../examples/revalidation.md)
- [Текущий статус проекта](../current-status.md)
