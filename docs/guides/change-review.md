# Change Review: проверка ветки, commit или pull request

`CHANGE_REVIEW` нужен, когда код уже изменён или существует кандидатное изменение,
но вы ещё не хотите считать его новым принятым состоянием системы.

Типичные случаи:

- проверить feature branch до merge;
- оценить конкретный commit;
- проверить pull request;
- сравнить два кандидатных решения;
- понять, какие проблемы изменение вводит, ухудшает, смягчает или потенциально решает;
- заранее увидеть, какие тесты, контракты и итоговые документы могут быть затронуты.

`CHANGE_REVIEW` — это orchestration intent, а не четвёртый модуль Review Suite.
Architecture Review, Test Engineering и Code Quality Review по-прежнему остаются
тремя независимыми capability.

## Базовая модель

Проверка всегда связывается с двумя точными состояниями источника:

```text
BASE
  accepted/main/commit/tree

CANDIDATE
  branch/commit/PR/tree
```

Человек может указать удобные ref, но review сохраняет разрешённые immutable
commit/tree bindings. Перемещение ветки после завершения review не изменяет то,
что было проверено.

## Что делает Change Review

```text
BASE..CANDIDATE
      ↓
change inventory
      ↓
bounded delta discovery
      ↓
candidate facts / affected accepted facts
      ↓
selected assessment lenses
      ↓
review result
```

Change Inventory отвечает на вопрос «что изменилось в исходниках». Assessment
отдельно отвечает на вопрос «что это означает». Эти два слоя не смешиваются.

Review может показать:

- добавленные, изменённые, удалённые и перемещённые поверхности;
- новые candidate facts;
- затронутые принятые факты;
- candidate findings;
- влияние на существующие findings;
- архитектурное влияние;
- необходимые повторные доказательства Test Engineering;
- возможное влияние на provider/consumer contracts;
- прогноз того, какие projections будут затронуты после принятия изменения.

Changed paths — это точка входа в анализ, а не доказательство отсутствия других
зависимостей. Если значимая зависимость выходит за исходный diff, review должен
расширить только необходимый срез через `CONTEXT_EXPANSION_REQUIRED`.

## Что Change Review не делает

Сам `CHANGE_REVIEW` не может:

- менять принятые STM facts;
- закрывать или создавать canonical CQ/Architecture findings;
- присваивать Test Engineering состояние `TESTED`;
- принимать результат Contract Verification;
- продвигать accepted baseline;
- ставить projection в `STALE`;
- автоматически пересобирать документы;
- approve/merge pull request или release.

Review-local `CR-*`, `CF-*` и `CRF-*` могут использоваться только как evidence,
routing context, historical comparison или reconciliation input. Они не являются
canonical semantic authority.

## Влияние на существующие findings

Кандидатный review может записать только эффект, например:

```text
UNAFFECTED
POTENTIALLY_RESOLVES
MITIGATES
WORSENS
INVALIDATES_PRIOR_ASSUMPTION
UNKNOWN_IMPACT
```

Например, изменение может `POTENTIALLY_RESOLVES` существующий HIGH finding и
одновременно вводить новый MEDIUM candidate finding. До reconciliation старый
finding остаётся в своём canonical lifecycle, а новый остаётся candidate-only.

## После review: RECONCILE_CHANGE

Если candidate действительно становится предназначенным новым состоянием,
пользователь отдельно выбирает `RECONCILE_CHANGE`.

```text
completed reusable Change Review
        ↓
explicit RECONCILE_CHANGE
        ↓
Technical Model Gate / Architecture / CQ / TE / CC
        ↓
accepted semantic delta
        ↓
baseline advancement gate
        ↓
Projection Impact Analysis
```

`RECONCILE_CHANGE` не является startup intent. Оно доступно только контекстно и
только когда review пригоден для выбранного source state.

Review base должен соответствовать текущему accepted baseline. Если accepted
baseline успел независимо измениться, старый `A → B` review нельзя применять к
новому `A' → B` только потому, что candidate всё ещё равен `B`. Нужен новый
review или полностью доказанная linked/supplemental review chain, покрывающая
пропущенный delta.

Partial reconciliation не может объявить весь baseline согласованным.
Открытые findings при этом могут остаться открытыми, если существующая политика
не делает их блокирующими: baseline reconciliation не является release approval.

## Переиспользование после merge

Commit SHA сам по себе не определяет переиспользуемость.

Допустимы два доказательных пути:

```text
WHOLE_TREE_EQUAL
FROZEN_RELEVANT_SCOPE_EQUAL
```

Первый использует равенство полного дерева при совпадающей qualification.
Второй допускается только для заранее зафиксированного релевантного среза с
сохранённым manifest/fingerprint и доказательством, что исключённые paths не
влияют на рассмотренный scope.

Поэтому no-ff или squash merge может безопасно переиспользовать review, если
итоговое source state доказанно эквивалентно. Conflict resolution, material
branch advancement, divergence или недоказанный partial cherry-pick требуют
дополнительного или нового review.

## Что происходит с проекциями

Во время candidate review допустим только прогноз:

```text
NO_EXPECTED_IMPACT
LIKELY_AFFECTED
DEFINITELY_AFFECTED_IF_ACCEPTED
UNKNOWN_IMPACT
```

Он не меняет фактические `CURRENT`, `STALE` или `BLOCKED`.

После принятой reconciliation существующий `Projection Impact Analysis`
рассчитывает реальное влияние. Даже после этого regeneration не запускается
автоматически: пользователь отдельно выбирает нужные `RG-*` операции.

## Baseline mismatch и остальные сценарии

| Ситуация | Поведение |
|---|---|
| accepted baseline совпадает | `RESUME` / допустимый `EXTEND` работают обычно |
| accepted baseline отличается | `RESUME` останавливается с `SOURCE_BASELINE_MISMATCH` |
| `EXTEND` при mismatch | `BASELINE_RECONCILIATION_REQUIRED` |
| current `PROJECTION_REPAIR` при mismatch | блокируется до reconciliation |
| нужно оценить candidate до принятия | `CHANGE_REVIEW` |
| новое состояние уже намеренно считается текущим | `REVALIDATE` |
| есть пригодный завершённый review | контекстно можно выбрать `RECONCILE_CHANGE` |

## Примеры запросов

### Feature branch

```text
Используй architecture-code-review.
Сделай CHANGE_REVIEW accepted baseline против branch feature/auth-hardening.
Нужны Architecture impact, Code Quality impact и Test impact.
Ничего не reconcile автоматически.
```

### Pull request

```text
Сравни accepted baseline с pull request #123 через CHANGE_REVIEW.
Покажи новые риски, потенциально закрываемые существующие findings и влияние на API/tests.
```

### После merge

```text
Проверь, можно ли переиспользовать завершённый Change Review для текущего main.
Если source state доказанно эквивалентен, предложи RECONCILE_CHANGE, но не запускай regeneration автоматически.
```

## См. также

- [Повторное использование, изменения и расширение](reuse-and-change.md)
- [Справочник процессов](../reference/workflows.md)
- [Жизненный цикл и актуальность](../concepts/lifecycle-and-freshness.md)
- [Текущий статус проекта](../current-status.md)
