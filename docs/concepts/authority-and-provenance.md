# Источники истины и происхождение выводов

`architecture-code-review` намеренно не хранит весь смысл в одном Markdown-файле.
Разные виды данных имеют разных владельцев, потому что они отвечают на разные
вопросы и проходят разные жизненные циклы.

## Зачем нужна карта источников истины

Без явного ownership легко получить три класса ошибок:

1. summary начинает считаться источником истины;
2. capability переписывает factual model под собственный вывод;
3. старый compact state продолжает использоваться после изменения owning artifact.

Поэтому для каждого типа данных задаётся owning layer.

## Authority map

| Объект | За что отвечает | Является authority? |
|---|---|---|
| `working/INDEX.md` | coordinator workflow state | да, только для routing/process state |
| `WS-*`, `EV-*` | baseline-bound observations | observation authority, не conclusions |
| STM `COMP/IF/INT/...` | принятые технические факты | да |
| `RF-*` | Architecture findings | да |
| `BC/CC/MAT/TM/GAP/TASK` | Test Engineering semantics | да |
| `CQ-*`, `CQRA-*` | Code Quality semantics | да |
| `PRJ-*` documents | человекочитаемое представление | нет, derived projection |
| `RG-*` | состояние regeneration session | operational state, не semantic authority |

## `working/INDEX.md`

`INDEX.md` — coordinator workflow authority. Он хранит то, что нужно для возобновления работы:

- baseline;
- Session Intent;
- selected capabilities;
- output configuration;
- phase/gates;
- artifact registry;
- handoffs;
- blockers;
- projection/package routing state.

Но `INDEX.md` не является вторым STM и не владеет findings.

Если compact INDEX entry расходится с owning artifact, downstream substantive decision должен остановиться и выполнить reconciliation.

Концептуально:

```text
INDEX says COMPLETE
owning artifact says REVALIDATION_REQUIRED

=> INDEX cannot override owning artifact
=> AUTHORITY_RECONCILIATION_REQUIRED
```

## Provenance chain

Хороший accepted finding должен позволять ответить:

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
  -> relevant STM facts / evidence
  -> executable test inventory
```

Для Code Quality:

```text
CQ-014
  -> implementation mechanism
  -> WS/EV or source refs
  -> material consequence
```

## Projection не становится authority

Даже если итоговый report прошёл editorial review, его prose остаётся representation accepted semantics.

Например:

```text
CQ-017 accepted finding
  -> PRJ-CQ-00 Findings View
  -> PRJ-CQ-01 Summary
```

Если Summary устарел, `CQ-017` не исчезает. Если человек вручную переписал Summary, это не изменяет `CQ-017`.

## Что делать при semantic drift

Если presentation-only edit требует изменить accepted meaning, такой edit больше не является projection repair.

Например, нельзя через `PROJECTION_REPAIR`:

- поменять severity;
- заменить owner;
- изменить root boundary;
- убрать accepted finding;
- изменить target mechanism;
- изменить roadmap prerequisite;
- переписать STM fact.

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
