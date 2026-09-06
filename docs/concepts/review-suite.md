# Review Suite

`Review Suite` объединяет три независимых модуля проверки. Они используют общие
доказательства и Shared Technical Model, но сохраняют собственные источники
технического смысла.

## Три модуля проверки

### Architecture Review

Отвечает на вопросы:

- как система реально устроена;
- где проходят существенные runtime и trust boundaries;
- кто владеет состоянием и ресурсами;
- как устроены lifecycle, concurrency, retries, recovery и failure behavior;
- какие архитектурные root findings доказаны;
- какую Target Architecture и Remediation Roadmap следует построить, если они запрошены.

Authority: `RF-*` и другие architecture-owned records.

### Test Engineering

Отвечает на вопросы:

- какие существенные поведения должны быть доказаны;
- какие из них действительно подтверждаются исполняемыми тестами;
- где test evidence недостаточно;
- расходятся ли DECLARED / IMPLEMENTED / CONSUMED / TESTED representations;
- какие Test Plan, environment, simulator или E2E artifacts нужны.

Authority: `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*`.

### Code Quality Review

Ищет не стилистические предупреждения сами по себе, а implementation mechanisms с доказуемым существенным последствием для сопровождения, надёжности, тестируемости, concurrency, dependencies, resource lifecycle и других качеств.

Authority: `CQ-*` и `CQRA-*`.

## Независимый выбор

Для `NEW` пользователь выбирает top-level capabilities независимо:

```text
[ ] Architecture Review
[ ] Test Engineering
[ ] Code Quality Review
```

Действует один обязательный инвариант:

```text
AT_LEAST_ONE_TOP_LEVEL_CAPABILITY_SELECTED
```

Допустимы все семь непустых комбинаций.

Architecture Review не является обязательным родителем Test Engineering или Code Quality. Если другой capability нужен accepted STM slice, он разрешается как factual dependency и не включает Architecture Review автоматически.

## Настройка модуля и выбор документов — разные вещи

Выбор capability определяет, какая semantic work должна выполняться. Выбор итоговых документов определяет, какие projections нужны пользователю.

Например:

```text
Code Quality Review: ON
  Findings View: ON
  Summary: OFF
  Hotspots: OFF
  Roadmap Contribution: OFF
```

означает, что Code Quality analysis выполняется, но пользователь заказал только один человекочитаемый output.

## Architecture: две независимые оси

Architecture Review имеет независимые depth и endpoint:

```text
Depth:
  STANDARD_FULL
  FORENSIC

Endpoint:
  REVIEW_ONLY
  REVIEW_PLUS_TARGET_ARCHITECTURE
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

Любой depth поддерживает любой endpoint. `FORENSIC` не означает `REVIEW_ONLY`.

## Общий factual substrate

Capabilities не должны независимо «изобретать» систему каждая для себя.

```text
Source
  -> Shared Evidence
  -> Shared Technical Model
       |        |        |
       v        v        v
 Architecture  Test   Code Quality
```

Shared layer хранит наблюдения и факты. Capability layer хранит интерпретации и решения своей области.

## Когда capabilities взаимодействуют

Один механизм может иметь несколько независимых последствий.

Например:

```text
INT-014 publication after commit
  |
  +--> RF-007 architecture ownership ambiguity
  +--> GAP-004 missing retry/concurrency proof
  +--> CQ-012 duplicated retry mechanism
```

Это не дублирование. Каждая запись отвечает на свой вопрос и имеет отдельный lifecycle.

## Stack Addenda

Языковые/framework-specific addenda — lenses, а не top-level capabilities. Они могут уточнять анализ для Rust, TypeScript, React, Tauri и других стеков, но не создают новую semantic authority и не должны молча включать capability.

## Что происходит после выбора

Для `NEW` последовательность концептуально такая:

```text
baseline
-> Review Suite selection
-> persistent STM bootstrap
-> minimum required evidence/model slice
-> selected capability work
-> semantic stabilization
-> Projection Impact Analysis
-> package resolution
-> requested deliverables
```

## Что читать дальше

- [Evidence и STM](evidence-and-technical-model.md)
- [Authority и provenance](authority-and-provenance.md)
- [Architecture Review guide](../guides/architecture-review.md)
- [Test Engineering guide](../guides/test-engineering.md)
- [Code Quality Review guide](../guides/code-quality-review.md)
