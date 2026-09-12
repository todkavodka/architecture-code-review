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

Актуальная сводка текущего состояния вынесена в
[Current Project Status](current-status.md). На принятой семантической базе уже
завершены:

```text
Discovery Coverage Assurance                       COMPLETE
Umbrella Review Suite Integration                  COMPLETE
Orchestrator v0.3                                  COMPLETE
Shared Technical Model Foundation                  DONE
Audit Projection & Regeneration                    DONE
Test Engineering                                   DONE
Code Quality Review                                DONE
Product / Multi-Project Review                     DONE
Interface, API & Data Integration Catalog          DONE
API Operation Completeness                         DONE
Change Review & Baseline Reconciliation            DONE
Federated Product Audit Coordination               DONE
```

Это означает, что в репозитории описаны, проверены и продвинуты соответствующие
методологические и orchestration-контракты. Это не означает, что Skill уже
реализует выполнение тестов, реализацию симуляторов, provisioning окружения,
runtime source scanner или другие execution-функции.

Текущая основа сохраняет evidence-first review, authority и freshness bindings,
минимально необходимую работу для `EXTEND` и `REVALIDATE`, независимые
capabilities, operation-completeness gates, отдельную модель candidate Change
Review и federated Product coordination поверх нескольких child repositories.
`Behavior Model` и применимая `Contract Verification` остаются внутренними
зависимостями и сохраняют собственное authority.

## Forward Roadmap

Порядок ниже определяется зависимостями и уменьшением риска, а не жёстким
расписанием. Этапы могут частично пересекаться после того, как их зависимости
будут подтверждены отдельными Discovery и Design.

```text
Current Foundation
       |
       +--> Stage A Shared Technical Model Foundation [DONE]
       |
       +--> Stage B Audit Projection & Regeneration [DONE]
       |
       +--> Stage C Test Engineering Execution [DONE]
       |
       +--> Stage D Code Quality Review [DONE]
       |
       +-----------------------------+
                                     |
                                     v
                    Stage E Product / Multi-Project Review [DONE]
                                     |
                                     v
                    Stage F Interface, API & Data Integration Catalog [DONE]
                                     |
                                     v
                    Cross-cutting Change Review & Baseline Reconciliation [DONE]
                                     |
                                     v
                    Cross-cutting Federated Product Audit Coordination [DONE]
```

Stage B особенно важен для надёжности генерируемых результатов Stage A, C и D,
но его наличие не отменяет независимые authority и freshness gates этих этапов.
Change Review и Federated Product Audit Coordination являются cross-cutting
orchestration lifecycles, а не новыми semantic capabilities или Stage G
authority.

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

**Status: `DONE`**

Stage B реализован, независимо проверен и продвинут в canonical `main`.

### Purpose

Сделать надёжным повторное построение финальных audit documents после
`REVALIDATE`, `EXTEND`, remediation, resolution findings, изменений severity или
semantic records, `PROJECTION_REPAIR` и legacy audit reconciliation.

Это не reindexing: этап не посвящён vector/RAG indexing. Речь идёт об impact-driven
regeneration проекций из принятого semantic authority.

### Completed scope

Завершённая реализация фиксирует следующие возможности высокого уровня:

- explicit projection identity, lifecycle, freshness, revisions, fingerprints,
  and bounded `PROJECTION_REPAIR`;
- dependency and selector contracts with persisted impact analysis and
  deterministic targeted/all-stale regeneration planning;
- verified generation, revision publication, downstream invalidation, and
  gate-scoped projection packages;
- safe projection contracts for Architecture Review, Technical Documentation,
  and Test Engineering that preserve upstream semantic authority;
- protection of coordinator `working/INDEX.md`, distinct operational views,
  conservative legacy registration, and NEW/EXTEND/REVALIDATE orchestration;
- auditable static/contract validation for the Stage B pressure scenarios.

Runtime validation координатора остаётся `UNAVAILABLE`, поскольку репозиторий
основан на Markdown Skill/reference и не содержит исполняемого координатора
Stage B.

Последовательность и статусы Stage C, Stage D и Stage E сохраняются; Stage B
не авторизует реализацию Stage C.

### Completion evidence

Promotion merge: `d3f856a948a03b33faafa454e0b6cd7f4f65f491`.
Promoted feature HEAD: `0c9a4b02d7ac49fcd9c3803fe017b997c290f564`.
Stage B pressure validation: `PS-100..PS-116` — `PASS_STATIC_CONTRACT`.
Stage A regressions: `PASS_STATIC_CONTRACT`.
Independent implementation review: `APPROVED`.
Critical findings: `0`; Important findings: `0`; Minor findings: `0`.
Runtime validation remains `UNAVAILABLE` because the repository does not
contain an executable Stage B coordinator, generator, or verifier; this is not
a runtime pass.

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

**Status: `DONE`**

### Purpose

Завершить принятую Test Engineering Foundation безопасным contract-first
workflow для assurance, behavior/contract reasoning, revalidation и
projection-aware orchestration. Реализация сохраняет границу между
Test Engineering semantic authority и factual STM authority; этот этап не
включает выполнение продуктовых тестов, реализацию симуляторов или
provisioning окружения.

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

### Completion evidence

Stage C implementation is accepted in canonical `main`: the fail-first
PS-81..PS-86 chain is preserved, the Test Engineering semantic and STM
prerequisite contracts are established, output selection/resume and
impact-driven revalidation are wired, and Stage B projection lifecycle
integration is defined and validated. Final acceptance found no blocking
findings; runtime coordinator/test execution remains `UNAVAILABLE` because
this repository is a Markdown Skill/reference system, not an executable
coordinator.

Canonical closeout checkpoint: `f165fb02b9e50971d6180ba495280432d3d0b2ef`.
The accepted implementation lineage was already present in canonical `main`;
no implementation merge was required. The separate `smevals` experiment remains
post-Stage-C and is not part of this completion evidence.

## Stage D — Code Quality Review

**Status: `DONE`**

### Purpose

Добавить отдельную capability для code-quality и bad-practice concerns,
которые важны для сопровождаемости и надёжности, но не обязательно являются
архитектурными findings.

### Completed scope

Stage D delivered:

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

The implementation defines finding identity, severity, evidence
requirements, false-positive controls, language/framework addenda, отношение к
`RF-*` и включение в remediation roadmap.

```text
Code Quality finding
    != automatically Architecture finding
```

На уровне Review Suite aggregate может включать Architecture Review,
Code Quality Review и Test Engineering, но semantic ownership каждой capability
должен остаться явным.

### Completion evidence

Stage D was implemented, independently reviewed, remediated, and promoted.
Pressure scenarios `PS-117..PS-131` passed, with no remaining material review
findings. Promotion merge: `71ef6885a9607fa53d008837c0b57bb9a6aad7f5`.

## Stage E — Product / Multi-Project Review

**Status: `DONE`**

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

### Completed scope

Stage E delivered bounded Product / Multi-Project Review support, including:

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

The implementation defines Product identity, membership, shared resources,
baseline/freshness/lineage across repositories, partial project availability,
large-context budgeting, multi-repository dirty state, cross-project evidence и
aggregate projections while preserving mature single-project Architecture Review
and orchestration/revalidation boundaries.

Product mode remains optional, and single-project operation remains first-class.
The implementation preserves qualified cross-project evidence and STM,
bounded `REVALIDATE` / additive `EXTEND`, Stage B projection/package reuse, and
existing capability authority boundaries. Pressure scenarios `PS-132..PS-149`,
integrated contract validation, and backward-compatibility validation passed.
Promotion merge: `c0cb853e9c7656f0e045816773c9e79d650186fb`.

## Stage F — Interface, API & Data Integration Catalog

**Status: `DONE`**

### Purpose

Extend the evidence-first review workflow with bounded interface, API,
integration, event, persistence, and data-access catalog projections while
preserving existing STM, Test Engineering, Product, and single-project
authority boundaries.

### Completed scope

Stage F completed its approved Discovery, Design, implementation planning,
isolated implementation, independent review, and promotion cycle. The
implementation provides:

- qualified IF/INT/DS/EVENT/FLOW semantics and precise INT-backed data access;
- evidence support and safe technical-identifier/redaction boundaries;
- Service Technical Documentation and Product-qualified catalog projections;
- compatibility display derived from existing Test Engineering `CC-*` authority;
- bounded orchestration, selector, projection-lifecycle, and Product
  qualification integration;
- static pressure and integrated validation covering the complete Stage F
  contract and backward compatibility.

Product remains optional, single-project operation remains first-class, and no
new factual identity family or compatibility authority was introduced.

### Completion evidence

Approved implementation-plan checkpoint: `dc9ffd6021b2484f64cd1237b1286572c91b629c`.
Approved feature HEAD: `54d9ae6ad5c14b59684c5513dffb6e4ec5bff57a`.
Final implementation verification: `STAGE_F_IMPLEMENTATION_COMPLETE`.
Independent implementation verdict: `STAGE_F_IMPLEMENTATION_APPROVED`.
Promotion merge: `9b8347bc263ef21fd2351a3c9295ab04a6992a42`.

Pressure scenarios `PS-F01..PS-F26`: `26/26 GREEN`.
Integrated contract validation: `PASS`.
Backward compatibility: `PASS`.
Migration: `COMPATIBLE_EXTENSION`.
New factual identity family: `NO`.
Authority conflicts: `0`.
No automatic projection regeneration was introduced; existing `CC-*`
compatibility authority remains authoritative.

## Cross-Cutting Milestone — Change Review & Baseline Reconciliation

**Status: `DONE`**

### Purpose

Добавить first-class pre-acceptance review source changes без смешения
candidate state с canonical semantic authority. Lifecycle позволяет проверять
branch, commit или pull request относительно immutable accepted baseline,
оценивать влияние, а затем отдельно и явно reconcile выбранный candidate через
существующих владельцев.

### Completed scope

Завершённая реализация включает:

- новый orchestration intent `CHANGE_REVIEW`, не являющийся capability;
- immutable base/candidate repository/Project/Product-qualified bindings;
- review-local `CR-*`, `CF-*`, `CRF-*` с жёстким candidate authority barrier;
- factual Change Inventory и bounded delta discovery с `CONTEXT_EXPANSION_REQUIRED`;
- candidate Architecture/CQ/TE/Contract Verification assessment без canonical mutation;
- exact reuse states `EXACT`, `TREE_EQUIVALENT`, `ADVANCED`, `DIVERGED`, `UNAVAILABLE`;
- proof-gated `WHOLE_TREE_EQUAL` и `FROZEN_RELEVANT_SCOPE_EQUAL`;
- contextual `RECONCILE_CHANGE` через существующих semantic owners;
- hard requirement, что review base соответствует текущему accepted baseline либо missing delta полностью покрыт linked/supplemental review chain;
- `BASELINE_ADVANCE_ALLOWED`, который запрещает full baseline advancement после partial reconciliation;
- explicit mismatch guards для `RESUME`, `EXTEND` и current `PROJECTION_REPAIR`;
- separation candidate projection prediction от actual Stage B Projection Impact;
- сохранение explicit `RG-*` regeneration;
- Product/member qualification, single-project compatibility и существующую API operation completeness authority.

### Completion evidence

```text
Approved design HEAD:
bc3d7410652a3c73ddb74da6de7e49a1815ec5b9

Approved plan HEAD:
e61f53ba560b50d3ca21475b40f572c9ac8c9085

Approved feature HEAD:
d870198eacaf1c2cd4d4ff685212fdb48491c3d7

Promotion merge:
2091a44622371bbc39fb913c00c1876d7f182dec
```

Final independent remediation re-review: `0 HIGH / 0 MEDIUM / 0 LOW`, no new
findings. Validation preserved `36/36` Change Review scenarios, `10/10`
merge/reuse scenarios, `5/5` partial reconciliation cases, `8/8` authority
barrier cases, `10/10` intent-routing cases, `6/6` projection cases and `6/6`
Product cases. Migration remains `COMPATIBLE_EXTENSION`; validation remains
`DO_NOT_BUILD_HARNESS`.

Closeout evidence:
[Change Review & Baseline Reconciliation — Closeout](superpowers/reviews/2026-09-11-change-review-baseline-reconciliation-closeout.md).

## Cross-Cutting Milestone — Federated Product Audit Coordination

**Status: `DONE`**

### Purpose

Расширить Stage E/Product orchestration для большого продукта, чьи child
repositories могут жить под общим non-Git Coordination Root и независимо
обновлять свои локальные аудиты. Координатор должен переиспользовать уже
принятые child результаты, выполнять только недостающую работу и принимать
новый Product baseline только после exact qualification и explicit gates.

### Completed scope

Принятая реализация определяет:

- non-Git Coordination Root как locator/discovery boundary, а не новую identity
  или authority;
- bounded metadata discovery с repository-boundary stop, cycle/symlink guards,
  explicit handling nested repos, submodules и worktrees;
- явное различие `Project != repository`, включая один Project в нескольких
  repos и несколько Projects в одном monorepo;
- immutable/frozen Product Coordination Plan, связывающий Product revision,
  membership snapshot, base Product baseline, exact member/source/scope
  qualifications, child actions, requested work и authorization;
- qualified reuse independently-created accepted child audits;
- stable child barrier и serialization только для реально конфликтующих writer
  scopes;
- derived dependency/output readiness без новой Product lifecycle authority;
- exact Product baseline candidate и обязательную final requalification перед
  Product Baseline Acceptance;
- deterministic race handling: `B` не может быть представлен как current `C`
  после source advancement;
- bottom-up adoption через Product `REVALIDATE` или новый complete-vector
  Product `CHANGE_REVIEW`, без direct child-to-Product baseline advancement;
- независимые оси source advancement и semantic-authority advancement;
- bounded derived impact `UNAFFECTED | AFFECTED | UNKNOWN_IMPACT` поверх
  существующих dependency/freshness/capability owners;
- policy-bound behavior для optional и required unavailable members;
- сохранение единого `working/INDEX.md` и Product-qualified
  `working/products/<PROD-key>/` namespace;
- отсутствие новых Session Intent, capability, Product STM, `PIA-*` authority,
  automatic membership, reconciliation или projection regeneration.

### Completion evidence

```text
Approved design remediation:
e8494f720d2cca7d53b57a4da08ed21dc9ca609a

Approved implementation-plan remediation / implementation base:
9bf5c4c33034826a916b88b033ee4b8f1011bc18

Approved feature HEAD:
9422f77c9cc0c2ecdcc66c217ce7006d4e57ff49

Promotion merge:
adb576e16067ec3113182f5b4f9a865a4ca7e062
```

Independent implementation review: `APPROVE / READY_FOR_PROMOTION` with
`0 HIGH / 0 MEDIUM / 0 LOW` findings. Validation closed `FC01..FC24` as
`24/24`, pressure scenarios `PV01..PV13` as `13/13 PASS`, and backward
compatibility `BC01..BC12` as `12/12 PASS`.

Validation remains contract-level Markdown evidence and smoke checking. The
milestone does not claim live repository crawling, automatic child execution,
SCM adapter execution, owner adjudication, baseline mutation or runtime
projection regeneration.

## Cross-Stage Architectural Principles

### Evidence first

Каждое substantive claim остаётся привязанным к проверяемому evidence.

### Semantic authority before projections

Generated reports являются projections принятого semantic state, а не его
заменой.

### Candidate state before canonical reconciliation

Candidate review может оценивать изменения и прогнозировать влияние, но не
становится canonical authority и не продвигает baseline без явной reconciliation
через существующих владельцев.

### Freshness and provenance

Переиспользуемые artifacts должны оставаться привязанными к revision и
baseline, с понятной provenance.

### Minimum necessary work

`EXTEND`, `REVALIDATE`, Change Review и federated Product coordination продолжают
использовать наименьший корректный dependency/evidence slice и явно расширяют
контекст только при необходимости.

### No silent escalation

Bounded operation не должна молча превращаться в full audit, product-wide review,
simulator implementation, E2E execution, automatic reconciliation или полный
перезапуск всех child repositories.

### Single-project remains first class

Product-level support расширяет, а не заменяет project-level workflow.
Federated coordination также остаётся explicit Product mode и не перехватывает
обычный single-project startup.

### Independent capabilities

Architecture Review, Code Quality Review и Test Engineering могут совместно
использовать evidence, но сохраняют явное semantic ownership. Technical
Documentation остаётся projection layer, а не четвёртой capability.

### Human-controlled execution

Любая будущая реализация code/test/simulator/environment, reconciliation,
Product baseline acceptance или projection regeneration требует explicit
authorization и соответствующих verification gates.

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
    A, C, D, E and post-reconciliation projection refresh

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

Stage F Interface, API & Data Integration Catalog
  depends on:
    STM/evidence foundation
    Product qualification where Product mode is selected

Change Review & Baseline Reconciliation
  depends on:
    accepted baseline semantics
    STM/owner authority boundaries
    projection impact lifecycle
  reuses:
    Product qualification
    API operation completeness

Federated Product Audit Coordination
  depends on:
    Stage E Product identity/membership/baseline semantics
    existing Session Intent and revalidation orchestration
    Change Review complete-vector/base-binding semantics
  reuses:
    STM/Technical Model Gate authority
    capability-local accepted state
    Product qualification and freshness/dependency contracts
```

`depends on` здесь означает необходимую основу. `supports`, `reuses` и
`benefits strongly from` обозначают полезную связь, но не жёсткое требование
последовательного завершения всех перечисленных этапов.

## Stage Entry Rule

Каждый будущий forward stage начинается со статуса `PLANNED` и остаётся в нём
до отдельного Discovery. Допустимые последующие статусы:

```text
PLANNED
DISCOVERY
DESIGN
IMPLEMENTATION
```

Roadmap bullets — candidate scope для Discovery, а не accepted detailed
requirements. Отдельная стадия не получает статус `DESIGN` только потому, что
в этом документе перечислены её идеи. Cross-cutting milestone не создаёт новую
semantic capability только потому, что отражён в roadmap.
