# Architecture Code Review — guide по итоговым документам

Этот документ объясняет, **какие user-facing outputs может создать Review Suite, чем они отличаются и когда их выбирать**.

Главная идея:

```text
capability selection != output selection
```

Включить Architecture, Test Engineering или Code Quality — не значит автоматически заказать все документы этой capability.

## 1. Architecture Review outputs

### Architecture Review

Основной человекочитаемый архитектурный отчёт.

Обычно отвечает на вопросы:

- как реально устроена система;
- где находятся component/process boundaries;
- кто владеет state/resources;
- как проходят ключевые flows;
- какие lifecycle/concurrency/failure/security свойства существенны;
- какие подтверждённые architecture/root findings существуют;
- какие ограничения evidence/coverage остаются.

Выбирайте, когда нужен ответ:

> Что с архитектурой системы происходит сейчас и какие архитектурные проблемы реально доказаны?

### Authoritative Findings Ledger

Подробный реестр принятых `RF-*` findings.

Нужен для:

- traceability;
- последующего remediation;
- revalidation;
- связи Target Architecture/Roadmap с конкретными findings;
- сохранения history/supersession.

Читать ledger вместо основного отчёта обычно неудобно; он инженерный authority artifact, а не executive summary.

### Target Architecture

Выбирается через:

```text
REVIEW_PLUS_TARGET_ARCHITECTURE
```

или как additive Architecture extension после принятого `REVIEW_ONLY`.

Target Architecture отвечает:

> Как должна быть устроена система, если исправить подтверждённые архитектурные причины?

Она не должна проектироваться из предположительных findings до их принятия.

### Remediation Roadmap

Выбирается через:

```text
REVIEW_PLUS_TARGET_AND_ROADMAP
```

Roadmap отвечает:

- в каком порядке выполнять изменения;
- какие prerequisites существуют;
- какие changes можно делать независимо;
- какие gates/evidence нужны перед следующим шагом;
- какие риски нельзя исправлять локальным patch без более раннего structural change.

Он должен опираться на accepted Architecture и Target Architecture, а не быть generic backlog.

## 2. Test Assurance

`Test Assurance` обязателен, когда Test Engineering включён.

Основные outputs:

```text
00-test-assurance-summary.md
01-test-assurance-map.md
```

### Assurance Summary

Короткий user-facing документ.

Отвечает:

- можно ли доверять текущей системе тестов;
- какие material behaviors доказаны;
- где наиболее опасные gaps;
- что исправлять первым.

### Assurance Map

Подробная карта:

```text
Material Assurance Target
  -> Behavior Contract
  -> executable Test Mapping
  -> verdict / gap
```

Она нужна для трассировки и последующей revalidation.

## 3. Test Plan

Optional output.

Выбирайте, когда после assurance анализа нужен **конкретный план тестовых работ**.

Он должен выводиться из подтверждённых gaps/targets, а не превращаться в универсальный список «добавить unit/integration/e2e tests».

Хороший Test Plan показывает:

- какое поведение нужно доказать;
- на какой минимальной test boundary;
- какие fixtures/dependencies нужны;
- какие failure/concurrency/retry cases существенны;
- как понять, что gap закрыт.

## 4. Contract Consistency Report

Optional user-facing report.

Важно различать:

```text
Contract Verification
        !=
Contract Consistency Report
```

Contract Verification — internal automatic gate, когда существует materially applicable contract.

Он сравнивает:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

`Contract Consistency Report` — отдельная проекция этих результатов для человека.

Выбирайте её, когда нужно:

- отдельно обсудить API/schema drift;
- передать findings владельцам producer/consumer;
- видеть `CC-*` records в удобном документе;
- использовать результат как migration/integration input.

## 5. Behavior Contract Model

Behavior Model не является обычным пользовательским output checkbox.

Он создаётся/используется внутренне, когда другим Test Engineering outputs нужна единая модель существенного поведения.

Человекочитаемая projection может появиться в package, но semantic authority принадлежит accepted `BC-*` records.

Пример:

```text
BC-021 unauthenticated POST /orders is rejected
BC-022 retry must not create another order
BC-023 only one completion event is published
```

## 6. Test Environment Design

Optional output.

Нужен, когда проблема не только в самих test cases, но и в **среде, в которой их можно надёжно запускать**.

Для каждой dependency выбирается подход вроде:

```text
REAL_DISPOSABLE
SERVICE_EMULATOR
CONTROLLABLE_MOCK
IN_PROCESS_DOUBLE
TEMP_RESOURCE
NOT_REQUIRED
```

Основной принцип:

> Подменяйте внешнюю неопределённость, а не само проверяемое поведение.

Например, если поведение зависит от реальных транзакций PostgreSQL, SQLite/mock может быть недостаточным доказательством.

## 7. Service Simulator Design

Optional output.

Service Simulator предназначен для потребителей проверяемого сервиса и воспроизводит существенную контрактную семантику.

Типичные части:

```text
Contract API
State Store
Scenario Engine
Fault Injection
Event Emitter
Control API
Health / Reset / Seed
```

Выбирайте, когда:

- consumer development зависит от unavailable/expensive service;
- нужны воспроизводимые error/failure scenarios;
- необходимо тестировать consumer behavior без production dependency;
- contract достаточно сложный, чтобы обычного stub/mock было мало.

Simulator не должен слепо генерироваться из Swagger — accepted behavior важнее одной declaration.

## 8. Service Simulator Implementation Plan

Optional output, но структурно зависит от принятого/fresh Simulator Design.

Он отвечает:

- из каких компонентов строить simulator;
- какие endpoints/control APIs нужны;
- как хранить scenario state;
- как реализовать faults/events;
- как тестировать сам simulator;
- как внедрить его в CI/consumer workflow.

Review Suite проектирует этот план, но не обязана автоматически реализовывать simulator runtime.

## 9. E2E Test Plan

Optional output.

E2E нужен только там, где material guarantee действительно требует совместной работы нескольких реальных компонентов.

Не следует выбирать E2E только потому, что это «самый полный» тип теста.

Каждый meaningful scenario должен описывать:

- исходный behavior (`BC-*`);
- participating components;
- real vs simulated dependencies;
- initial state;
- stimulus;
- assertions;
- failure observability;
- cleanup/reset;
- CI suitability.

Service Simulator не включается автоматически для каждого E2E. Он появляется только если выбранная topology действительно его требует.

## 10. Code Quality Findings View / Report

User-selectable derived projection.

Это основной подробный документ по принятым `CQ-*` findings.

Он полезен, когда нужно видеть:

- конкретный implementation mechanism;
- evidence/provenance;
- material consequence;
- severity/confidence;
- applicability/disposition;
- relationship к другим CQ/Architecture/Test records;
- remediation/revalidation state.

Название «derived» означает, что документ строится из accepted CQ authority. Это **не означает**, что output включается автоматически.

## 11. Code Quality Summary

User-selectable derived projection.

Более короткий документ для понимания общей картины:

- где сосредоточен material code-quality risk;
- какие classes проблем доминируют;
- какие findings наиболее существенны;
- что требует внимания раньше остальных.

Выбирайте, когда Findings View слишком детален для первого чтения.

## 12. Maintainability Hotspots

User-selectable derived projection.

Группирует accepted Code Quality evidence/findings вокруг участков системы, где концентрируется maintenance burden.

Важно: hotspot не должен строиться только по LOC/complexity metric. Он должен опираться на accepted material interpretation.

Полезен для:

- refactoring prioritization;
- ownership discussion;
- планирования decomposition;
- выявления областей с несколькими связанными CQ findings.

## 13. Code Quality Roadmap Contribution

User-selectable derived projection.

Не является отдельным глобальным Remediation Roadmap.

Он формирует Code Quality contribution для дальнейшего planning:

- связанные `CQRA-*`;
- dependencies;
- ordering constraints;
- recommended remediation groups;
- revalidation expectations.

Architecture Roadmap и CQ Roadmap Contribution могут быть связаны, но не переписывают authority друг друга.

## 14. Projection vs semantic authority

Пользовательские документы — удобные представления, но источник технического смысла находится глубже.

Например:

```text
CQ-017 accepted finding
    |
    +--> Code Quality Findings View
    +--> Summary
    +--> Hotspots
```

Если Summary устарел, это не удаляет `CQ-017`.

Если Markdown вручную отредактирован, это не должно менять `CQ-017`.

Для presentation-only ремонта используется `PROJECTION_REPAIR`.

## 15. Как выбрать outputs — примеры

### Нужен только архитектурный диагноз

```text
Architecture Review: ON
  STANDARD_FULL
  REVIEW_ONLY

Test Engineering: OFF
Code Quality Review: OFF
```

### Нужна архитектура и порядок исправлений

```text
Architecture Review: ON
  STANDARD_FULL
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

### Нужно понять качество тестов

```text
Test Engineering:
  Test Assurance
```

### Нужен actionable test backlog

```text
Test Engineering:
  Test Assurance
  Test Plan
```

### Нужен анализ интеграционного контракта

```text
Test Engineering:
  Test Assurance
  Contract Consistency Report
```

### Нужно спроектировать consumer simulator

```text
Test Engineering:
  Test Assurance
  Service Simulator Design
```

### Нужен implementation plan simulator

```text
Test Engineering:
  Test Assurance
  Service Simulator Design
  Service Simulator Implementation Plan
```

### Нужен только review качества реализации

```text
Code Quality Review:
  Findings View/Report
  Summary
```

Architecture и Test Engineering при этом могут быть OFF.

### Нужна полная инженерная картина

```text
Architecture Review:
  STANDARD_FULL
  REVIEW_PLUS_TARGET_AND_ROADMAP

Test Engineering:
  Test Assurance
  Test Plan
  Contract Consistency Report
  E2E Test Plan

Code Quality Review:
  Findings View/Report
  Summary
  Maintainability Hotspots
  Roadmap Contribution
```

Это допустимо, но не является default: Skill должен избегать ненужного scope.

## 16. Как outputs переиспользуются

После принятия outputs они не обязаны генерироваться заново в каждой сессии.

```text
same accepted state
  -> USE_EXISTING

new output needed
  -> EXTEND

project changed
  -> REVALIDATE affected slice

presentation broken
  -> PROJECTION_REPAIR
```

Projection freshness проверяется отдельно от semantic freshness.

## 17. Как читать package

Для большинства людей удобный порядок:

```text
1. summary / main report
2. detailed map / findings view
3. target / plan if selected
4. owning semantic records when нужна трассировка
5. WS/EV evidence when нужно проверить происхождение вывода
```

Для debugging/revalidation инженер может идти наоборот:

```text
INDEX
 -> semantic record
 -> evidence
 -> raw source
```

## 18. Связанные документы

- [Architecture](architecture.md) — модель Review Suite и ownership;
- [Artifacts and State](artifacts-and-state.md) — какие IDs/files создаются;
- [Workflows](workflows.md) — как outputs живут между сессиями;
- [Roadmap](roadmap.md) — дальнейшее развитие.