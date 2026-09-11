# Повторное использование, изменения и расширение

`Review Suite` рассчитан на длительное использование пакета аудита. Полные
правила сценариев, условий входа и остановок приведены в
[справочнике процессов](../reference/workflows.md); это руководство объясняет
только, какой сценарий выбрать в практической ситуации.

| Ситуация | Сценарий | Последствие |
|---|---|---|
| Нет предыдущего аудита | `NEW` | Создаётся новый пакет и область проверки. |
| Работа не завершена и baseline совпадает | `RESUME` | Продолжается первая непринятая устойчивая граница. |
| Нужно оценить branch, commit или pull request до принятия | `CHANGE_REVIEW` | Создаётся read-only candidate review без изменения canonical state. |
| Проект изменился и новое состояние намеренно считается текущим | `REVALIDATE` | Повторно проверяется только затронутый accepted state. |
| Есть пригодный завершённый Change Review и изменение нужно принять | контекстный `RECONCILE_CHANGE` | Candidate evidence передаётся существующим владельцам для canonical adjudication. |
| Нужен модуль или документ | `EXTEND` | Добавляется только новое; прежний выбор сохраняется. |
| Нужен уже принятый результат | `USE_EXISTING` | Новая техническая работа не создаётся. |
| Исправлено только оформление | `PROJECTION_REPAIR` | Технический смысл не меняется. |

## После изменения проекта

Сначала определите, нужно ли **оценить candidate** или **переоценить уже
предназначенный текущий baseline**.

Для ветки, commit или pull request, который ещё не должен считаться принятым
состоянием, используйте `CHANGE_REVIEW`. Он сравнивает immutable `BASE` и
`CANDIDATE`, но не меняет STM, findings, Test Engineering state, Contract
Verification или projection freshness.

Для принятого пакета и source state, которое уже считается текущим, используйте
`REVALIDATE`. Он определяет затронутую часть зависимостей и повторно проверяет
только необходимое. Завершённый Change Review может быть routing/evidence input,
но не заменяет owner adjudication.

Если baseline изменился, обычный `RESUME` не продолжает работу как будто старое
accepted state всё ещё описывает текущий source. Он останавливается с
`SOURCE_BASELINE_MISMATCH` и предлагает `CHANGE_REVIEW`, `REVALIDATE` и, при
выполненных условиях, контекстный `RECONCILE_CHANGE`.

Подробности: [Change Review](change-review.md),
[справочник процессов](../reference/workflows.md) и
[жизненный цикл и актуальность](../concepts/lifecycle-and-freshness.md).

## Принятие уже проверенного изменения

`RECONCILE_CHANGE` не является startup intent. Оно доступно только после
завершённого пригодного Change Review и явного подтверждения пользователя.

Candidate slices направляются существующим владельцам STM, Architecture, Code
Quality, Test Engineering и Contract Verification. Review-local `CR-*`, `CF-*`
и `CRF-*` сами по себе не становятся canonical records.

Review base должен соответствовать текущему accepted baseline. Если accepted
baseline успел измениться независимо, старого `A → B` review недостаточно для
`A' → B`: нужен новый review или полностью доказанная linked/supplemental chain.
Partial reconciliation не продвигает весь baseline.

## Добавление результата

Для нового документа, модуля или дополнительного результата `Architecture
Review` используйте `EXTEND`. Уже принятые элементы показываются только для
чтения и не снимаются автоматически. Глубина существующего `Architecture
Review` не меняется; его результат можно только расширить от `REVIEW_ONLY` к
`REVIEW_PLUS_TARGET_ARCHITECTURE`, а затем к
`REVIEW_PLUS_TARGET_AND_ROADMAP`.

Если source baseline изменился и ещё не reconciled, `EXTEND` блокируется с
`BASELINE_RECONCILIATION_REQUIRED`.

Полные правила добавления: [раздел `EXTEND`](../reference/workflows.md#extend).

## Использование прежнего результата

`USE_EXISTING` подходит, если выбранный документ и его источники истины
пригодны по политике пакета. Старый принятый пакет можно использовать как
исторический результат, но нельзя представлять его как current state для нового
source baseline без reconciliation.

## Оформление и пересборка

`PROJECTION_REPAIR` подходит только для языка, Markdown, Mermaid, навигации,
таблиц и других изменений представления. Если текущий source baseline отличается
от accepted baseline, repair текущего представления блокируется до source
reconciliation.

Если исправление меняет технический смысл, процесс возвращает
`SEMANTIC_DRIFT_DETECTED` и требует технической повторной проверки.

Анализ влияния на проекции не пересобирает документы. Candidate Change Review
может только прогнозировать влияние. Фактический `Projection Impact Analysis`
выполняется после принятой reconciliation, а получение свежего документа требует
отдельного явного `RG-*` regeneration.

Подробности: [модель жизненного цикла](../concepts/lifecycle-and-freshness.md) и
[модель проекций и пакетов](../concepts/projections-and-packages.md).

## Переиспользование Change Review после merge

Переиспользование не определяется совпадением branch name или commit ancestry.
Для `TREE_EQUIVALENT` требуется доказанный `WHOLE_TREE_EQUAL` либо
`FROZEN_RELEVANT_SCOPE_EQUAL`. Поэтому clean no-ff или squash merge может
переиспользовать review, а conflict resolution, divergence или недоказанный
partial cherry-pick требуют дополнительной проверки.

## См. также

- [Change Review](change-review.md)
- [Справочник процессов](../reference/workflows.md)
- [Пример повторной проверки](../examples/revalidation.md)
- [Текущий статус проекта](../current-status.md)
