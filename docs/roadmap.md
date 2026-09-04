# architecture-code-review — Product Roadmap

Этот документ описывает возможное дальнейшее развитие `architecture-code-review`.
Он является стратегическим ориентиром, а не детальным implementation plan,
design specification, календарём релизов или обещанием конкретных сроков.
Текущие контракты Skill, отдельные design-документы и планы реализации остаются
авторитетными в своих областях.

Каждый будущий этап требует собственного цикла:

```text
Discovery
→ Design
→ independent design review
→ implementation planning
→ fail-first validation
→ isolated implementation
→ independent review
→ promotion
```

Пункты ниже — кандидатная область для Discovery, а не принятые подробные
требования. Статус этапа не поднимается выше `PLANNED`, пока его отдельный
процесс не пройдёт необходимые ворота.

## Current Baseline

На текущем `main` уже приняты следующие основы:

```text
Discovery Coverage Assurance                 COMPLETE
Umbrella Review Suite Integration            COMPLETE
Orchestrator v0.3                            COMPLETE
Test Engineering Foundation                 COMPLETE
Test Engineering NEW / EXTEND output UX     COMPLETE
```

Это означает, что в репозитории описаны и проверены соответствующие
методологические и orchestration-контракты. Это не означает, что Skill уже
реализует выполнение тестов, реализацию симуляторов, provisioning окружения
или другие будущие execution-функции.

Текущая основа сохраняет evidence-first review, authority и freshness bindings,
минимально необходимую работу для `EXTEND` и `REVALIDATE`, независимые
capabilities и отдельную модель Test Engineering outputs. `Behavior Model` и
применимая `Contract Verification` остаются внутренними зависимостями.

## Forward Roadmap

Порядок ниже определяется зависимостями и уменьшением риска, а не жёстким
расписанием. Этапы могут частично пересекаться после того, как их зависимости
будут подтверждены отдельными Discovery и Design.

```text
Current Foundation
       |
       +--> Stage A Shared Technical Model Foundation [DONE]
       |
       +--> Stage B Audit Projection & Regeneration [NEXT]
       |
       +--> Stage C Test Engineering Execution
       |
       +--> Stage D Code Quality Review
       |
       +-----------------------------+
                                     |
                                     v
                    Stage E Product / Multi-Project Review
```

Stage B особенно важен для надёжности генерируемых результатов Stage A, C и D,
но его наличие не отменяет независимые authority и freshness gates этих этапов.

## Stage A — Shared Technical Model Foundation

**Status: `DONE`**

### Purpose

Создать общий слой evidence и устойчивую factual Shared Technical Model (STM),
которую могут использовать Architecture Review, Test Engineering и Technical
Documentation. Факты отделены от capability-specific interpretation, а
человеческие документы остаются проекциями.

Принятые подэтапы:

```text
A1 Shared Evidence Layer
A2 Shared Technical Model
A3 Technical Model Coverage
A4 Dependency / Index Infrastructure
A5 Technical Documentation
A6 As-Built Projection Migration
A7 Architecture Review Integration
A8 Legacy Audit Reconciliation
```

### Scope boundary

Stage A не включает developer onboarding, local setup, “how to run/modify”,
туториалы или operations handbook. Factual Technical Documentation может
описывать topology, interfaces, integrations, persistence, trust, flows,
configuration и failure contracts. Эти ограничения являются частью принятого
Stage A контракта.

### Completion evidence

Stage A delivered the Shared Evidence Layer, persistent Shared Technical Model,
STM coverage and Technical Model Gate, dependency/index infrastructure,
Technical Documentation projections, As-Built projection migration,
Architecture Review integration, mandatory targeted STM acquisition for Test
Engineering, conservative legacy reconciliation, and impact-driven `EXTEND` /
`REVALIDATE` foundations.

Promotion merge: `6759539ef8eb1b7d8634bb648772168715e02785`.
Promoted feature HEAD: `ce9e1c410bc4924568d6e68f1c82875b90371161`.
Static/contract validation passed. Executable coordinator/runtime validation
remains `UNAVAILABLE` and is an environment limitation, not a runtime pass.

## Stage B — Audit Projection & Regeneration

**Status: `PLANNED`**

Stage B is the next planned stage and will be handled by a separate
Discovery/design gate.

### Purpose

Сделать надёжным повторное построение финальных audit documents после
`REVALIDATE`, `EXTEND`, remediation, resolution findings, изменений severity или
semantic records, `PROJECTION_REPAIR` и legacy audit reconciliation.

Это не reindexing: этап не посвящён vector/RAG indexing. Речь идёт об impact-driven
regeneration проекций из принятого semantic authority.

### Candidate Discovery scope

Discovery может рассмотреть:

- projection dependency map;
- обнаружение stale projections;
- impact-driven regeneration;
- full regeneration, когда она структурно необходима;
- revision-bound projections;
- cross-document consistency verification;
- idempotent regeneration;
- legacy audit reconciliation;
- preservation policy для human-authored content;
- `PROJECTION_REPAIR 2.0`.

Целевая схема:

```text
semantic authority
      |
      v
projection impact analysis
      |
      v
affected final documents
      |
      v
regeneration
      |
      v
cross-document consistency validation
```

Final Markdown projection никогда не становится semantic authority только
потому, что она существует дольше или выглядит убедительнее. Этап должен
предотвращать, например, ситуацию, когда finding уже resolved в authority,
summary обновлён, а roadmap, другой report или `INDEX` остались на старой
revision.

## Stage C — Test Engineering Execution

**Status: `PLANNED`**

### Purpose

Продолжить уже принятую Test Engineering Foundation от
analysis/design/planning к безопасному исполняемому engineering workflow.
Текущая foundation не должна описываться как уже реализованное выполнение.

### Candidate Discovery scope

Возможные направления:

- Service Simulator implementation lifecycle;
- Service Simulator verification;
- consumer acceptance against simulator;
- Test Environment provisioning and execution;
- E2E implementation and execution;
- runtime evidence capture;
- преобразование `GAP-*` в executable test tasks;
- integration test-result evidence.

Потенциальные lifecycle-направления могут выглядеть так:

```text
Behavior Contract Model
        ↓
Contract Verification
        ↓
Simulator Spec
        ↓
Implementation Authorization
        ↓
Simulator Implementation
        ↓
Contract Verification
        ↓
Consumer Acceptance
```

И отдельно:

```text
E2E Plan
   ↓
E2E Implementation
   ↓
Environment Preparation
   ↓
Execution
   ↓
Evidence Capture
   ↓
Assurance Result
```

Существующие границы сохраняются: accepted `BC-*` остаётся authority для
simulator design; Contract Verification не смешивается с simulator
implementation; implementation требует accepted/fresh specification и явного
authorization; E2E не требует simulator автоматически; внешнюю неопределённость
можно подменять, но не поведение под тестом. Точные execution permissions и
safety boundaries определяются только на Stage C Discovery/Design.

## Stage D — Code Quality Review

**Status: `PLANNED`**

### Purpose

Добавить отдельную capability для code-quality и bad-practice concerns,
которые важны для сопровождаемости и надёжности, но не обязательно являются
архитектурными findings.

### Candidate Discovery scope

Discovery может проверить:

- duplication и hardcoded values;
- configuration и localization practices;
- dead/obsolete code;
- oversized functions, classes и modules;
- плохие или избыточные abstraction boundaries;
- error handling и resource management;
- async/concurrency misuse;
- framework anti-patterns;
- maintainability smells;
- security-adjacent code smells;
- dependency usage, inconsistent patterns и testability.

Отдельно должны быть определены finding identity, severity, evidence
requirements, false-positive controls, language/framework addenda, отношение к
`RF-*` и включение в remediation roadmap.

```text
Code Quality finding
    != automatically Architecture finding
```

На уровне Review Suite будущий aggregate может включать Architecture Review,
Code Quality Review и Test Engineering, но semantic ownership каждой capability
должен остаться явным.

## Stage E — Product / Multi-Project Review

**Status: `PLANNED`**

### Purpose

Дать Skill возможность работать над уровнем продукта и нескольких проектов,
сохраняя полноценную single-project operation.

```text
Product
├── Project A
├── Project B
├── Project C
└── Shared Components / Infrastructure
```

`Project != Product`. Наличие product-level режима не должно требовать Product
parent для каждого обычного аудита.

### Candidate Discovery scope

Возможные направления:

- product inventory и project discovery;
- project identity и membership;
- cross-project architecture и dependency graph;
- cross-project contracts;
- shared component ownership;
- duplicated responsibility detection;
- version/compatibility analysis;
- product-level findings;
- product-level developer documentation;
- product-level Test Engineering;
- cross-project E2E scenarios;
- product-level Code Quality aggregation;
- product-wide remediation roadmap.

Трассируемость должна сохраняться между project-local evidence,
cross-project evidence и product-level inference. Product-level finding нельзя
получать простым concatenation project reports.

Discovery должен определить Product identity, membership, shared resources,
baseline/freshness/lineage across repositories, partial project availability,
large-context budgeting, multi-repository dirty state, cross-project evidence и
aggregate projections. Это крупнейший будущий этап, поэтому он опирается на
зрелые single-project Architecture Review и orchestration/revalidation.

## Cross-Stage Architectural Principles

### Evidence first

Каждое substantive claim остаётся привязанным к проверяемому evidence.

### Semantic authority before projections

Generated reports являются projections принятого semantic state, а не его
заменой.

### Freshness and provenance

Переиспользуемые artifacts должны оставаться привязанными к revision и
baseline, с понятной provenance.

### Minimum necessary work

`EXTEND` и `REVALIDATE` продолжают использовать наименьший корректный
dependency slice.

### No silent escalation

Bounded operation не должна молча превращаться в full audit, product-wide review,
simulator implementation или E2E execution.

### Single-project remains first class

Product-level support расширяет, а не заменяет project-level workflow.

### Independent capabilities

Architecture Review, Code Quality Review, Test Engineering и Developer
Documentation могут совместно использовать evidence, но сохраняют явное
semantic ownership.

### Human-controlled execution

Любая будущая реализация code/test/simulator/environment требует explicit
authorization и verification gates.

## Dependency and Sequencing

Likely dependencies:

```text
Stage A Shared Technical Model Foundation
  depends on:
    existing architecture/evidence model

Stage B Audit Projection & Regeneration
  depends on:
    current artifact/projection semantics
  supports:
    A, C, D, E

Stage C Test Engineering Execution
  depends on:
    Test Engineering Foundation

Stage D Code Quality Review
  depends on:
    evidence/discovery foundation

Stage E Product / Multi-Project Review
  depends on:
    mature project-level Architecture Review
    mature orchestration/revalidation
  benefits strongly from:
    A, B, C, D
```

`depends on` здесь означает необходимую основу. `supports` и `benefits strongly
from` обозначают полезную связь, но не жёсткое требование последовательного
завершения всех перечисленных этапов.

## Stage Entry Rule

Каждый forward stage начинается со статуса `PLANNED` и остаётся в нём до
отдельного Discovery. Допустимые последующие статусы:

```text
PLANNED
DISCOVERY
DESIGN
IMPLEMENTATION
```

Roadmap bullets — candidate scope для Discovery, а не accepted detailed
requirements. Отдельная стадия не получает статус `DESIGN` только потому, что
в этом документе перечислены её идеи.
