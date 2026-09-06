# Источники истины и происхождение выводов

`architecture-code-review` намеренно не хранит весь смысл в одном Markdown-файле.
Разные виды данных имеют разных владельцев, потому что они отвечают на разные
вопросы и проходят разные жизненные циклы.

## Зачем нужна карта источников истины

Без явного разграничения ответственности легко получить три класса ошибок:

1. краткое резюме начинают считать источником истины;
2. модуль проверки переписывает фактическую модель под собственный вывод;
3. старое компактное состояние продолжают использовать после изменения основного артефакта.

Поэтому для каждого типа данных определён источник истины.

## Карта источников истины

| Объект | За что отвечает | Является источником истины? |
|---|---|---|
| `working/INDEX.md` | состояние координации процесса | да, только для маршрутизации и состояния процесса |
| `WS-*`, `EV-*` | наблюдения, привязанные к базовой ревизии | источник наблюдений, но не выводов |
| STM `COMP/IF/INT/...` | принятые технические факты | да |
| `RF-*` | архитектурные выводы | да |
| `BC/CC/MAT/TM/GAP/TASK` | семантика Test Engineering | да |
| `CQ-*`, `CQRA-*` | семантика Code Quality Review | да |
| документы `PRJ-*` | человекочитаемое представление | нет, производная проекция |
| `RG-*` | состояние сеанса пересборки | операционное состояние, не семантический источник истины |

## `working/INDEX.md`

`INDEX.md` — источник истины для координации процесса. Он хранит то, что нужно для возобновления работы:

- базовую ревизию;
- Session Intent;
- выбранные модули проверки;
- конфигурацию итоговых документов;
- этапы и проверки;
- реестр артефактов;
- передачу состояния;
- blockers;
- projection/package routing state.

Но `INDEX.md` не является второй STM и не хранит выводы как источник истины.

Если компактная запись INDEX расходится с основным артефактом, последующее существенное решение должно остановиться и выполнить согласование.

Концептуально:

```text
INDEX says COMPLETE
owning artifact says REVALIDATION_REQUIRED

=> INDEX cannot override owning artifact
=> AUTHORITY_RECONCILIATION_REQUIRED
```

## Цепочка происхождения

Принятый вывод должен позволять ответить:

> Почему мы считаем это утверждение верным?

Цепочка может выглядеть так:

```text
RF-007
  -> INT-014@rev2
  -> WS-012#EV-003
  -> src/payment/retry.py@<baseline>
```

Для Test Engineering:

```text
GAP-008
  -> MAT-017
  -> BC-042
  -> относящиеся к делу факты STM / доказательства
  -> перечень исполняемых тестов
```

Для Code Quality:

```text
CQ-014
  -> механизм реализации
  -> WS/EV or source refs
  -> существенное последствие
```

## Проекция не становится источником истины

Даже если итоговый отчёт прошёл редакционную проверку, его текст остаётся представлением принятой семантики.

Например:

```text
CQ-017 accepted finding
  -> PRJ-CQ-00 Findings View
  -> PRJ-CQ-01 Summary
```

Если краткое резюме устарело, `CQ-017` не исчезает. Если человек вручную переписал резюме, это не изменяет `CQ-017`.

## Что делать при семантическом расхождении

Если правка представления требует изменить принятый смысл, она больше не является исправлением проекции.

Например, нельзя через `PROJECTION_REPAIR`:

- поменять severity;
- заменить владельца;
- изменить root boundary;
- убрать принятый вывод;
- изменить target mechanism;
- изменить roadmap prerequisite;
- переписать факт STM.

Вместо этого workflow возвращает:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

## Compact state и freshness

Compact records допустимы как routing shortcut, только если связаны с current owning authority.

Минимальная логика:

```text
owning authority accepted
+
revision matches
+
compact record VALID
=
compact state usable downstream
```

Если revision изменилась, старый compact record должен перейти в `REVALIDATION_REQUIRED` или быть superseded.

## Cross-capability references

Capabilities могут ссылаться на records друг друга, но reference не передаёт ownership.

Например, `CQ-*` может ссылаться на `RF-*`, если один implementation mechanism связан с architecture root cause. Code Quality не получает право менять `RF-*`.

Точно так же `TASK-*` и `CQRA-*` могут быть связаны, но остаются remediation objects разных capabilities.

## Authority conflict example

Допустим:

- OpenAPI declares `POST /orders` returns 201;
- backend implementation иногда возвращает 202;
- frontend обрабатывает только 201;
- tests ожидают 202.

Это не решается правилом «код всегда главный» или «spec всегда главный».

Observed views фиксируются, затем Contract Verification создаёт/обновляет `CC-*` и явно adjudicates authority в bounded context.

## Практическое правило чтения

Для навигации:

```text
INDEX -> report/summary
```

Для инженерного решения:

```text
INDEX -> owning semantic artifact -> evidence -> source
```

## Что читать дальше

- [Evidence и STM](evidence-and-technical-model.md)
- [Lifecycle и freshness](lifecycle-and-freshness.md)
- [Artifact Reference](../reference/artifacts.md)
