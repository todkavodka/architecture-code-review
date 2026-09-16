# Пример: адресная повторная проверка после изменения кода

Этот пример показывает, как переиспользовать уже принятый пакет аудита после изменения системы. Главное — не запускать всё заново, а определить, **что именно стало потенциально неактуальным**.

Пути, идентификаторы и ревизии условны.

## Исходное принятое состояние

Месяц назад команда завершила аудит сервиса заказов на baseline `A`.

В пакете были:

```text
Architecture Review
Test Engineering
```

Принятое состояние:

```text
STM:
  INT-PUBLISH-COMPLETION@rev2
  EVENT-ORDER-COMPLETED

Architecture Review:
  RF-007 ACTIVE HIGH

Test Engineering:
  BC-022
  MAT-012
  TM-044
  GAP-009

Projections:
  Architecture Review                       CURRENT
  Test Assurance Summary                    CURRENT
  Test Assurance Map                        CURRENT
  Contract Consistency Report               CURRENT
```

Это состояние корректно описывает baseline `A`.

Оно не обязано оставаться корректным для будущего кода.

## Что изменилось

Появился новый baseline `B`.

Изменены:

```text
src/retry/coordinator.py
src/events/publisher.py
tests/integration/retry_publication.spec.ts
```

Не менялись:

```text
authentication
user interface
billing
```

Команда хочет обновить существующий аудит.

Правильный сценарий:

```text
REVALIDATE
```

а не новый `NEW`.

## Почему нельзя смотреть только на список файлов

Файл сам по себе не является семантической границей.

Изменение `publisher.py` может повлиять на:

- взаимодействие STM;
- архитектурный finding;
- контракт поведения;
- test mapping;
- gap;
- человекочитаемые отчёты.

Поэтому skill строит влияние по зависимостям.

## Новые доказательства

На baseline `B` собираются свежие наблюдения:

```text
WS-014-retry-publication

EV-061
source: src/retry/coordinator.py
observed:
  retry теперь передаёт устойчивый publication key

EV-062
source: src/events/publisher.py
observed:
  publication key сохраняется до отправки брокеру

EV-063
source: tests/integration/retry_publication.spec.ts
observed:
  тест воспроизводит timeout после принятия сообщения брокером
```

## Повторная проверка Shared Technical Model

Прежнее взаимодействие:

```text
INT-PUBLISH-COMPLETION@rev2
```

затронуто изменением.

После проверки принимается новая редакция:

```text
INT-PUBLISH-COMPLETION@rev3
status: ACCEPTED
freshness: VALID
```

Не связанные STM-факты не открываются повторно без необходимости.

## Определение затронутого среза

От нового взаимодействия идут зависимости:

```text
INT-PUBLISH-COMPLETION@rev3
    ↓
RF-007
    ↓
BC-022
    ↓
MAT-012
    ↓
TM-044 / GAP-009
```

Именно этот срез требует повторной проверки.

Подсистема аутентификации не затронута только потому, что находится в том же репозитории.

## Что происходит с RF-007

На baseline `A` было:

```text
RF-007 ACTIVE HIGH
```

Новый код выглядит как исправление, но сам факт изменения файла не закрывает finding.

Architecture Review получает новые доказательства и проверяет корневую проблему.

Если доказано, что:

- publication key устойчив;
- retry не создаёт второй логический event;
- неоднозначный timeout не ломает идемпотентность;
- relevant path действительно использует новый механизм;

то владелец может принять:

```text
RF-007 ACTIVE → RESOLVED
```

Если доказательств недостаточно, finding остаётся `ACTIVE` или получает freshness limitation.

Если механизм изменился настолько, что прежняя идентичность больше не описывает текущую проблему, может потребоваться `SUPERSEDED` с новой записью.

## Что происходит с Test Engineering

Новый интеграционный тест существует, но сначала нужно установить, что он действительно доказывает `BC-022`.

Проверка может изменить `TM-044`:

```text
до:
  PARTIAL

после:
  FULL / sufficient evidence
```

Только после принятого execution evidence можно повторно оценить `GAP-009`.

Если доказательство достаточно:

```text
GAP-009 → resolved according to TE owner semantics
```

Не потому, что файл теста появился, а потому, что существенное поведение теперь действительно доказано.

## Проекции после семантического изменения

После принятия новых owner records сами Markdown-отчёты могут остаться старыми.

Например:

```text
Architecture Review                       STALE
Test Assurance Summary                    STALE
Test Assurance Map                        STALE
Contract Consistency Report               CURRENT
```

Это нормальная ситуация.

Семантическое состояние уже обновлено, а человекочитаемые представления ещё нет.

Анализ влияния на проекции отвечает только на вопрос:

> Какие документы теперь не соответствуют принятому состоянию?

Он не пересобирает их автоматически.

## Явная регенерация

Если пользователю нужны свежие отчёты, запускается явная адресная регенерация затронутых проекций.

После неё:

```text
Architecture Review                       CURRENT
Test Assurance Summary                    CURRENT
Test Assurance Map                        CURRENT
Contract Consistency Report               CURRENT
```

Регенерация не меняет `RF-*`, `BC-*`, `TM-*` или `GAP-*`. Она только отображает уже принятое состояние.

## Как выглядит прогресс

Предположим, между baseline `A` и `B` произошло следующее:

```text
RF-007 HIGH ACTIVE → RESOLVED
```

Тогда отчёт о прогрессе может показывать:

```text
Current RF:
1 → 0

Resolved:
1

Historical registered RF:
1
```

История не удаляется.

## Пример изменения серьёзности без закрытия

Другой вариант: проблема всё ещё существует, но новый механизм уменьшил последствие.

```text
RF-007 HIGH ACTIVE
    ↓
RF-007 MEDIUM ACTIVE
```

Тогда:

```text
NEW: 0
RESOLVED: 0
SEVERITY_DECREASED: 1
```

Это та же проблема, а не новая запись.

## Пример stale resolved finding

Допустим, на baseline `B` `RF-007` был принят как `RESOLVED`.

Позже появился baseline `C`, где снова изменился publisher.

Пока владелец не провёл revalidation, нельзя утверждать:

```text
RF-007 RESOLVED на C
```

Но нельзя и автоматически утверждать:

```text
RF-007 ACTIVE на C
```

Корректно сохранить исторический факт:

```text
RF-007 был RESOLVED для B
```

и отдельно показать:

```text
RESOLUTION_REVALIDATION_REQUIRED для C
```

После новой проверки Architecture Review принимает текущее состояние.

## Пример принятого риска

Предположим, finding не исправлен, но команда формально принимает риск.

```text
RF-010 ACTIVE ACTION_REQUIRED
    ↓
RF-010 ACTIVE ACCEPTED_RISK
```

Это не resolution.

Прогресс:

```text
Current findings:
1 → 1

Resolved:
0

Accepted risk added:
1

Actionable:
1 → 0

Residual accepted risk:
0 → 1
```

## Если изменение ещё не принято

Если baseline `B` пока существует только как pull request, `REVALIDATE` не нужен.

Сначала:

```text
CHANGE_REVIEW A → B
```

Он может показать потенциальное влияние, например:

```text
RF-007 POTENTIALLY_RESOLVES
GAP-009 likely affected
Architecture Review projection likely stale if accepted
```

Но accepted state остаётся привязанным к `A` до явного принятия изменения.

## Если изменился один child repository продукта

Пусть Product baseline содержит:

```text
PB-10
  backend rev5
  frontend rev8
```

Backend независимо переходит на `rev6` и закрывает локальный finding.

Это не меняет `PB-10` автоматически.

Product должен:

1. обнаружить semantic authority advancement child;
2. повторно квалифицировать child result;
3. выполнить Product `REVALIDATE` или полный-vector Change Review по выбранному сценарию;
4. проверить остальные member bindings;
5. только затем принять новый Product baseline.

## Итог

Главная идея `REVALIDATE`:

```text
не "запустить аудит ещё раз"

а

"найти затронутое принятое состояние,
получить свежие доказательства
и перепроверить только необходимый срез"
```

Так пакет аудита может жить вместе с проектом длительное время, не превращаясь ни в устаревший архив, ни в постоянно повторяемый полный аудит.

## Что читать дальше

- [Что делать после изменения кода](../guides/after-code-changes.md)
- [Жизненный цикл аудита](../guides/audit-lifecycle.md)
- [Практические рецепты](../guides/common-recipes.md)
- [Жизненный цикл и актуальность](../concepts/lifecycle-and-freshness.md)
