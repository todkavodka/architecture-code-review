# Что делать после изменения кода

Этот документ — практическая инструкция для ситуации, когда проект уже проходил аудит, а затем его исходный код, конфигурация, зависимости или структура изменились.

Главный принцип:

> **Не запускайте полный аудит автоматически. Сначала определите статус изменения и затронутый принятый контекст.**

Ниже описан выбор между `CHANGE_REVIEW`, `REVALIDATE`, `RECONCILE_CHANGE`, `RESUME`, `EXTEND` и `PROJECTION_REPAIR`.

## 1. Быстрое решение

Начните с одного вопроса:

> Изменение ещё является кандидатом или уже считается новым текущим состоянием проекта?

```text
изменение ещё не принято
        ↓
   CHANGE_REVIEW
        ↓
пользователь решил принять candidate
        ↓
контекстный RECONCILE_CHANGE
        ↓
owner adjudication
        ↓
новое accepted state

изменение уже считается текущим source
        ↓
     REVALIDATE
        ↓
impact analysis
        ↓
затронутые owner records
        ↓
адресная повторная проверка
```

Если изменилось только представление, а не технический смысл, используется `PROJECTION_REPAIR` или явная regeneration соответствующей проекции.

## 2. Таблица выбора

| Ситуация | Что использовать | Что происходит |
|---|---|---|
| Feature branch ещё не merged | `CHANGE_REVIEW` | Candidate сравнивается с принятым baseline без изменения accepted state. |
| Pull request ещё не принят | `CHANGE_REVIEW` | Оценивается delta и возможное влияние. |
| Отдельный commit ещё не принят как текущий source | `CHANGE_REVIEW` | То же, что для branch/PR. |
| Изменение merged и считается новым current source | `REVALIDATE` | Перепроверяется затронутая accepted authority. |
| Есть завершённый пригодный Change Review и candidate принимается | `RECONCILE_CHANGE` | Candidate evidence передаётся владельцам для принятия решений. |
| Нужно продолжить незавершённый аудит, baseline не менялся | `RESUME` | Продолжается существующая работа. |
| Нужен дополнительный output или capability | `EXTEND` | Добавляется новая работа поверх принятого состояния. |
| Изменились Markdown/Mermaid/навигация без изменения смысла | `PROJECTION_REPAIR` | Исправляется presentation layer. |
| Нужен уже принятый результат | `USE_EXISTING` | Новая техническая работа не запускается. |

## 3. Сценарий: обычный commit после принятого аудита

Предположим, был принят аудит на commit `A`, а затем проект перешёл на commit `B`.

Если `B` уже считается текущим состоянием проекта, запрос должен вести к `REVALIDATE`:

```text
Используй существующий пакет architecture-code-review.
Текущий source изменился с принятого baseline до текущего HEAD.
Выполни REVALIDATE только затронутого состояния.
```

Skill должен:

1. определить delta `A → B`;
2. найти затронутые зависимости;
3. пометить требующие повторной проверки записи;
4. переиспользовать незатронутое accepted state;
5. перепроверить минимальный необходимый slice;
6. принять новые owner revisions только там, где это действительно требуется;
7. отдельно определить влияние на projections.

Не следует автоматически создавать новый полный пакет.

## 4. Сценарий: feature branch до merge

Используйте `CHANGE_REVIEW`:

```text
Используй architecture-code-review.
Сравни принятый baseline с branch feature/payment-retry.
Нужен CHANGE_REVIEW без изменения accepted state.
```

Skill должен разрешить `BASE` и `CANDIDATE` в immutable состояния и построить структурный delta.

Результат может показать:

- новые потенциальные проблемы;
- усиление существующего риска;
- возможное устранение существующей finding;
- влияние на интерфейсы, данные, auth, configuration и failure behavior;
- потенциальное влияние на Test Engineering и Code Quality;
- проекции, которые станут затронутыми при принятии candidate.

Но всё это остаётся candidate review.

## 5. Сценарий: pull request

PR обрабатывается как candidate.

Пример:

```text
Используй architecture-code-review.
Сделай CHANGE_REVIEW принятого baseline против pull request #123.
Покажи влияние на существующие RF, CQ, Test Engineering state и projections.
Ничего не reconcile автоматически.
```

Если PR обновился после review, предыдущий candidate review нельзя молча считать review новой версии PR. Нужно проверить exact candidate binding.

## 6. Сценарий: после merge

После merge сначала проверьте, совпадает ли merged tree с проверенным candidate.

Возможны четыре типовых случая.

### Fast-forward

Если merged result идентичен проверенному candidate, reuse обычно наиболее прямой.

### No-ff merge

Commit identity может измениться, но дерево может остаться эквивалентным. Для reuse требуется доказательство равенства соответствующего дерева или релевантного замороженного slice.

### Squash merge

SHA почти наверняка будет другим. Это не означает, что review обязательно бесполезен. Если доказано равенство содержимого релевантного дерева, candidate evidence можно переиспользовать.

### Merge с разрешением конфликтов

Conflict resolution может изменить код относительно проверенного candidate. В этом случае reuse без дополнительной проверки опасен.

Ключевое правило:

> Совпадение названия ветки или ancestry не заменяет доказательство эквивалентности содержимого.

## 7. Сценарий: принять ранее проверенный candidate

Если Change Review завершён и candidate действительно соответствует принимаемому состоянию, пользователь может подтвердить `RECONCILE_CHANGE`.

Пример:

```text
Используй завершённый CHANGE_REVIEW для этого merge.
Эквивалентность candidate подтверждена.
Запусти RECONCILE_CHANGE и направь затронутые записи их владельцам.
```

`RECONCILE_CHANGE` не закрывает findings сам.

Он маршрутизирует работу:

```text
candidate delta
   ↓
Technical Model Gate / Architecture / Test Engineering / Code Quality
   ↓
owner revalidation
   ↓
owner adjudication
   ↓
accepted revisions
```

## 8. Сценарий: изменение dependency

Изменение библиотеки, runtime, framework или внешнего сервиса может влиять на систему без крупного изменения собственного кода.

Пример:

```text
Обновили framework с версии X до Y.
Выполни REVALIDATE зависимых technical facts, findings, test evidence и Code Quality state.
Не открывай несвязанные области.
```

Следует проверить как минимум зависимости, которые участвуют в:

- lifecycle;
- concurrency;
- serialization;
- auth;
- transport;
- persistence;
- error handling;
- testing behavior.

## 9. Сценарий: изменение конфигурации

Configuration может быть частью технического поведения.

Изменения в:

- environment variables;
- feature flags;
- deployment manifests;
- reverse proxy;
- timeouts;
- retry policies;
- resource limits;
- auth settings;

могут требовать `REVALIDATE`, даже если application code почти не изменился.

## 10. Сценарий: изменение только документации проекта

Нужно определить, меняет ли документация только описание или является источником заявленного контракта.

Если это обычная README-правка без semantic effect на анализируемую систему, техническая revalidation может не потребоваться.

Если документация является declared contract, например API schema или configuration contract, она может затронуть Contract Verification и связанные records.

Не классифицируйте изменение как presentation-only только по расширению файла.

## 11. Сценарий: изменился только один child repository в Product

Допустим, Product состоит из:

```text
backend
frontend
gateway
shared
```

и изменился только `backend`.

Правильный путь:

1. определить изменение backend;
2. обновить или revalidate только его локальное audit state;
3. сохранить принятый child result;
4. Product обнаруживает source/semantic authority advancement;
5. Product выполняет impact-driven revalidation;
6. остальные children переиспользуются, если их bindings всё ещё пригодны;
7. новый Product baseline принимается отдельно.

Нельзя просто заменить backend revision внутри Product baseline и объявить новый baseline текущим.

## 12. Сценарий: child audit обновился независимо

Это bottom-up flow.

Пример:

```text
backend audit обновился самостоятельно
Product baseline всё ещё ссылается на backend owner rev5
backend теперь имеет accepted owner rev6
```

Product должен обнаружить advancement.

Если source тот же, но owner revision изменился, это всё равно semantic authority advancement.

Product baseline остаётся прежним, пока не пройдёт существующий Product acceptance flow.

## 13. Сценарий: найдено, что finding исправлен

Нельзя закрывать finding по diff или словам разработчика.

Для `RF-*` и `CQ-*` resolution требует owner-controlled revalidation.

Правильная последовательность:

```text
изменение выглядит как исправление
  ↓
candidate effect: POTENTIALLY_RESOLVES
  ↓
accepted source / reconciliation
  ↓
owner revalidation
  ↓
доказательство отсутствия той же проблемы
  ↓
owner adjudication
  ↓
RESOLVED revision
```

## 14. Сценарий: finding всё ещё актуален

Если targeted revalidation показывает, что механизм проблемы сохранился:

- ID обычно сохраняется;
- lifecycle остаётся `ACTIVE`;
- принимается новая revision, если изменились bindings/evidence;
- severity может измениться только при отдельной owner adjudication;
- progress не должен считать finding новой только потому, что evidence обновилось.

## 15. Сценарий: stale ACTIVE

Если accepted active finding относится к старому source и зависимый source изменился, finding не исчезает.

Он остаётся видимым как известный риск, но current applicability к новому source требует revalidation.

Нельзя использовать отсутствие свежего доказательства как доказательство отсутствия риска.

## 16. Сценарий: stale RESOLVED

Это особенно важный случай.

```text
RF-010 был RESOLVED на B
source изменился до C
revalidation ещё не проведена
```

Правильное представление:

- историческая resolution на B сохраняется;
- отсутствие проблемы на C не доказано;
- finding не становится автоматически `ACTIVE`;
- он также не должен показываться как `RESOLVED + CURRENT` для C;
- показывается uncertainty / `RESOLUTION_REVALIDATION_REQUIRED`;
- owner revalidation определяет следующий accepted state.

## 17. Сценарий: изменилась только severity

Если корневая finding та же, изменение `HIGH → MEDIUM` не создаёт новую finding.

Нужно сохранить identity и показать `SEVERITY_DECREASED` на сравнении baseline.

Аналогично `MEDIUM → HIGH` даёт `SEVERITY_INCREASED`.

## 18. Сценарий: remediation заблокирована

`remediation_status=BLOCKED` не означает, что finding stale или resolved.

Пример:

```text
lifecycle = ACTIVE
freshness = CURRENT
remediation_status = BLOCKED
```

Finding остаётся текущим техническим риском.

Не путайте это с `freshness=BLOCKED`, где проблема состоит в невозможности получить достаточно свежие evidence/dependencies.

## 19. Сценарий: принят риск

Accepted risk не закрывает finding.

```text
ACTIVE + ACTION_REQUIRED
        ↓ owner disposition change
ACTIVE + ACCEPTED_RISK
```

На progress view это изменение disposition, а не `RESOLVED`.

## 20. Сценарий: нужно только обновить отчёт

Если semantic state уже принято и нужно только получить свежее человекочитаемое представление:

1. проверить freshness semantic authority;
2. определить состояние projection;
3. выполнить explicit regeneration, если она разрешена;
4. пройти verification projection;
5. не менять owner authority.

Если исходный source изменился, одной regeneration недостаточно.

## 21. Что происходит с projections

Принятое semantic изменение может сделать зависимые projections stale.

Последовательность:

```text
accepted semantic change
  ↓
projection impact analysis
  ↓
affected PRJ-* becomes STALE
  ↓
explicit RG-* regeneration
  ↓
verification
  ↓
CURRENT projection
```

Regeneration не заменяет semantic revalidation.

## 22. Когда нельзя использовать RESUME

`RESUME` предназначен для незавершённой работы на совместимом baseline.

Если source baseline изменился, продолжать старую работу как будто ничего не произошло нельзя.

В таком случае процесс должен остановить обычный resume и предложить подходящий change/revalidation route.

## 23. Когда использовать EXTEND

`EXTEND` используется, если source состояние пригодно, но нужно добавить работу.

Примеры:

- добавить Code Quality Review к уже принятому Architecture Review;
- получить Target Architecture;
- добавить Remediation Roadmap;
- получить подробные Provided Interfaces;
- расширить operation inventory;
- получить дополнительную Technical Documentation.

Если baseline reconciliation не завершена, extension текущего пакета может быть заблокирована.

## 24. Минимальный рабочий процесс команды

Для обычной разработки удобно придерживаться такого процесса:

```text
1. Есть accepted audit baseline.
2. Разработчик создаёт branch.
3. Перед merge запускается CHANGE_REVIEW.
4. Review issues исправляются в branch.
5. Candidate перепроверяется при необходимости.
6. Branch merge.
7. Проверяется equivalence merged result и reviewed candidate.
8. RECONCILE_CHANGE или REVALIDATE принимает новое состояние.
9. Owner records обновляются.
10. Projection impact определяет устаревшие документы.
11. Нужные документы регенерируются явно.
```

## 25. Быстрые prompts

### Проверить branch

```text
Используй architecture-code-review.
Сделай CHANGE_REVIEW accepted baseline против branch feature/example.
Покажи impact, но ничего не reconcile автоматически.
```

### Проверить PR

```text
Используй architecture-code-review.
Сделай CHANGE_REVIEW accepted baseline против pull request #123.
```

### После merge

```text
Используй существующий пакет аудита.
Код уже принят в main.
Выполни REVALIDATE только затронутого accepted state и затем покажи projection impact.
```

### Принять эквивалентный проверенный candidate

```text
Проверенный candidate эквивалентен принятому merge result.
Используй завершённый CHANGE_REVIEW как evidence input и выполни RECONCILE_CHANGE через существующих owners.
```

### Обновить один child

```text
Обновился только backend Project.
Переиспользуй пригодные состояния остальных Product members, обнови backend локально, затем выполни Product revalidation и не продвигай Product baseline автоматически.
```

## 26. Что не делать

Не следует:

- запускать `NEW` после каждого commit;
- закрывать findings по тексту commit message;
- считать merged branch автоматически reconciled;
- считать новый Markdown текущим только потому, что он новый;
- использовать `PROJECTION_REPAIR` для semantic change;
- превращать отсутствующий child member в нулевые показатели;
- принимать Product baseline только по факту локального child update;
- считать accepted risk resolved;
- считать remediation completion доказательством finding resolution.

## 27. Связанные документы

- [Жизненный цикл аудита](audit-lifecycle.md)
- [Change Review](change-review.md)
- [Повторное использование и изменения](reuse-and-change.md)
- [Практические рецепты](common-recipes.md)
- [Жизненный цикл и актуальность](../concepts/lifecycle-and-freshness.md)
- [Справочник процессов](../reference/workflows.md)
