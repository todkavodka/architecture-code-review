# Первый полный запуск

Этот walkthrough показывает не только конфигурацию, но и жизненный цикл нового audit package.

## Исходная задача

Предположим, команда получила legacy backend и хочет понять:

- как система реально устроена;
- где находятся архитектурные риски;
- насколько текущие тесты подтверждают критические поведения;
- какие реализационные механизмы создают существенные проблемы сопровождения.

Запрос пользователю к агенту может быть простым:

```text
Используй architecture-code-review для этого repository.
Нужен полный инженерный аудит перед модернизацией.
```

## Шаг 1. Startup discovery

Skill сначала определяет:

```text
repository identity
previous audit packages
baseline
working-tree state
Project Profile
Session Intent
```

Если пригодного предыдущего audit нет, будет рекомендован `NEW`.

Если working tree содержит незакоммиченные изменения, агент должен явно определить, анализируется только committed HEAD, ephemeral snapshot или работа останавливается. Это важно для воспроизводимости evidence.

## Шаг 2. Review Suite

Для широкого первого аудита команда может выбрать:

```text
Architecture Review: ON
  Depth: STANDARD_FULL
  Endpoint: REVIEW_PLUS_TARGET_AND_ROADMAP

Test Engineering: ON
  Test Assurance
  Test Plan
  Contract Consistency Report

Code Quality Review: ON
  Findings View/Report
  Code Quality Summary
  Maintainability Hotspots
```

Это пример, а не обязательная default-конфигурация. Skill должен помогать ограничивать scope и не включать документы «на всякий случай».

## Шаг 3. Persistent baseline

До substantive capability work создаются coordinator state и persistent STM baseline. Это не значит, что вся система мгновенно описывается полностью.

Принцип:

```text
always create model baseline
!=
always fully populate model
```

Полный Architecture Review потребует принятой фактической модели достаточной ширины до тематического анализа. Более узкая capability может работать на bounded accepted slice.

## Шаг 4. Evidence

Исследование разбивается на worksets `WS-*`. Внутри них появляются observations `EV-*`, привязанные к baseline и source location.

Например:

```text
WS-007-order-publication
  scope: transaction + event publication
  baseline: <commit>

  EV-001
    source: src/orders/service.py
    symbol: complete_order
    observed: database commit happens before event publication
```

Observation ещё не является finding. Оно только фиксирует подтверждённое наблюдение.

## Шаг 5. Shared Technical Model

Из достаточных evidence принимаются технические факты STM:

```text
COMP-API
INT-ORDER-COMPLETE
DS-POSTGRES
EVENT-ORDER-COMPLETED
```

Они связываются provenance с `WS#EV` и друг с другом. Только Technical Model Gate может принять, пересмотреть, отклонить или supersede STM fact.

## Шаг 6. Capability analysis

Дальше каждая capability интерпретирует общие факты в собственной области.

Architecture Review может создать `RF-*` для архитектурного root problem.

Test Engineering может создать:

```text
BC-*
MAT-*
TM-*
GAP-*
```

Code Quality может создать `CQ-*`, если конкретный implementation mechanism имеет доказанное material consequence.

Один и тот же факт может участвовать во всех трёх анализах, но записи не превращаются друг в друга.

## Шаг 7. Проверки и gates

Перед публикацией выводов Skill проверяет достаточность coverage, независимую falsification/verification там, где её требует capability, и консистентность downstream outputs.

Недостаточная evidence должна ограничить ширину вывода, а не маскироваться уверенным prose.

## Шаг 8. Итоговый пакет

Конкретный layout зависит от repository convention и выбранных outputs. Концептуально пользователь получает:

```text
architecture report / findings ledger
optional target architecture
optional remediation roadmap

test assurance summary/map
optional test plan / contract report / environment / simulator / E2E

code quality findings / summary / hotspots

working/
  INDEX.md
  evidence/
  technical-model/
  projections/
  capability working state
```

## Шаг 9. Как читать результат

Руководителю или архитектору обычно достаточно начать с main report/summary и roadmap.

Инженер, который проверяет конкретный вывод, идёт глубже:

```text
report
  -> RF/CQ/GAP/other semantic record
  -> STM fact / WS#EV
  -> source
```

Так можно доказать происхождение вывода без повторного анализа всей системы.

## Шаг 10. Что происходит через месяц

Допустим, после аудита появилось 20 новых commits.

Не нужно запускать `NEW` только потому, что HEAD изменился. Для принятого audit package используется `REVALIDATE`:

```text
old baseline
  -> new baseline
  -> change inventory
  -> impact analysis
  -> minimum affected dependency slice
  -> fresh evidence
  -> revalidation
  -> projection impact accounting
```

Незатронутая accepted authority сохраняется.

## Следующие материалы

- [Review Suite](../concepts/review-suite.md)
- [Evidence и STM](../concepts/evidence-and-technical-model.md)
- [Workflow Reference](../reference/workflows.md)
- [Архитектурный пример](../examples/architecture-review.md)
