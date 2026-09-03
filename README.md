# Architecture Code Review

`architecture-code-review` — Skill для глубокого evidence-first архитектурного и кодового аудита существующих систем.

Его задача — не собрать длинный список «подозрительных мест», а восстановить, **как система реально устроена и работает**, проверить границы ответственности и владение состоянием, проследить важные сценарии исполнения и только после этого формулировать выводы.

В основе подхода — принцип:

> **Ширина утверждения не должна превышать ширину доказательств.**

Если проверен один обработчик, это не доказывает корректность всей модели авторизации. Если работает обычный сценарий, это ещё не доказывает корректность повторов, восстановления после сбоя, конкурентного выполнения или остановки процесса. Если доказательств недостаточно, результат остаётся `PARTIAL`, `NOT_PROVEN`, `UNKNOWN` или `AUTHORITY_UNRESOLVED`, а не превращается в выдуманный дефект.

Skill подходит для аудита всего репозитория, отдельной подсистемы и повторных проверок уже проаудированного проекта.

---

## Основные возможности

Skill объединяет несколько связанных, но не смешанных областей:

- **Architecture Review** — фактическая архитектура, ownership, lifecycle, concurrency, trust boundaries, reliability, maintainability и testability;
- **Target Architecture** — целевая архитектура после подтверждённых findings;
- **Remediation Roadmap** — порядок исправлений и зависимости между ними;
- **Test Assurance** — насколько существующие тесты реально подтверждают существенное поведение;
- **Test Engineering** — проектирование недостающих тестов, контрактная проверка, окружение тестов, Service Simulator и E2E;
- **REVALIDATE / EXTEND / PROJECTION_REPAIR** — повторное использование принятой работы без автоматического полного rerun.

Технологические дополнения для Tauri, Electron, React, Django, FastAPI, Litestar и Ansible остаются стековыми линзами, а не отдельными верхнеуровневыми capabilities.

---

## Как начинается работа

Начиная с Orchestrator v0.3, запуск Skill начинается не с безусловного нового аудита. Сначала Session Orchestrator определяет репозиторий, baseline, состояние рабочего дерева и уже существующие audit packages.

```text
repository + baseline + working tree
        |
        v
previous audit discovery
        |
        v
authority / lineage / freshness reconciliation
        |
        v
Project Profile
        |
        v
Session Intent
        |
        v
requested outputs / capabilities
        |
        v
minimum necessary technical work
```

Повторный запуск Skill не означает автоматический повтор всего аудита.

### Session Intent

Поддерживаются:

- `USE_EXISTING` — использовать уже принятый аудит для того же committed baseline;
- `NEW` — начать новый ограниченный аудит;
- `RESUME` — продолжить незавершённый аудит после reconciliation;
- `REVALIDATE` — проверить изменения относительно принятого baseline;
- `EXTEND` — добавить новую capability/output, не повторяя несвязанные принятые части;
- `PROJECTION_REPAIR` — исправить только финальные пользовательские документы без изменения технической семантики.

Типичные рекомендации:

```text
previous audit отсутствует                      -> NEW
IN_PROGRESS                                     -> RESUME
COMPLETE + тот же HEAD                          -> USE_EXISTING
COMPLETE + изменившийся HEAD                    -> REVALIDATE
нужен новый capability/output                   -> EXTEND
нужен только ремонт финальных документов        -> PROJECTION_REPAIR
```

`RESUME_WITH_RECONCILIATION` — внутренний вариант `RESUME`, а не отдельный persisted Session Intent.

`PROJECTION_REPAIR` не заменяет `REVALIDATE`: если для исправления финального Markdown нужно изменить evidence, root cause, severity, ownership, invariant, `BC-*`, `CC-*`, Target Architecture или Roadmap, Skill должен остановить presentation-only путь с `SEMANTIC_DRIFT_DETECTED` / `TECHNICAL_REVALIDATION_REQUIRED`.

---

## Новый аудит (`NEW`)

Architecture Review и Test Engineering конфигурируются независимо.

### Глубина Architecture Review

```text
STANDARD_FULL
FORENSIC
```

### Итоговый результат Architecture Review

```text
REVIEW_ONLY
REVIEW_PLUS_TARGET_ARCHITECTURE
REVIEW_PLUS_TARGET_AND_ROADMAP
```

`FORENSIC` не означает автоматическое построение Target Architecture или Roadmap.

### Test Engineering outputs

Современная конфигурация Test Engineering хранит outputs независимо:

```text
[x] Test Assurance
[ ] Test Plan
[ ] Contract Consistency Report
[ ] Test Environment Design
[ ] Service Simulator Design
[ ] Service Simulator Implementation Plan
[ ] E2E Test Plan
```

`Test Assurance` — evidence-first ядро capability.

`Behavior Model` не является пользовательским checkbox: он подключается как внутренняя зависимость, когда выбранным outputs нужна единая модель существенного поведения.

`Contract Verification` также не является optional checkbox. Если существует materially relevant declared contract — например OpenAPI/Swagger, protobuf/gRPC schema, AsyncAPI или другой машинно-читаемый внешний контракт — проверка `DECLARED ↔ IMPLEMENTED ↔ CONSUMED ↔ TESTED` запускается как внутренний gate. Пользовательский `Contract Consistency Report` при этом остаётся необязательной проекцией.

Skill может рекомендовать дополнительные outputs, но не должен молча включать существенную работу.

### Legacy Test Review compatibility

Старые audit packages могут содержать:

```text
REVIEW_ONLY
REVIEW_PLUS_TEST_PLAN
```

Они остаются поддерживаемым входом для resume/reconciliation, но больше не являются основной моделью конфигурации Test Engineering.

Нормализация консервативная:

```text
legacy REVIEW_ONLY
  -> test_assurance=true
  -> все optional Test Engineering outputs=false

legacy REVIEW_PLUS_TEST_PLAN
  -> test_assurance=true
  -> test_plan=true
  -> все остальные optional outputs=false
```

Legacy состояние никогда не должно само включать E2E, simulator, environment design или contract report.

---

## Как устроен Architecture Review

Базовый поток нового полного аудита:

```text
committed baseline
  -> As-Built Architecture
  -> independent As-Built review
  -> thematic discovery
  -> Discovery Coverage Matrix
  -> Independent Coverage Review
  -> independent candidate verification
  -> root-boundary adjudication
  -> severity assignment
  -> Authoritative Findings Ledger
  -> optional Target Architecture
  -> optional Remediation Roadmap
  -> final package
  -> editorial review / correction / re-review
```

### As-Built Architecture

До поиска проблем агент восстанавливает фактические компоненты, процессы, owners, state, data flows и material execution scenarios. Это не пересказ README проекта и не вывод по именам папок.

### Discovery Coverage

Полнота не измеряется количеством найденных замечаний. Нужен bounded inventory существенных механизмов в scope. Для каждого должно быть ясно: покрыт, частично покрыт, неприменим, заблокирован или неизвестен.

Sampling может использоваться для качества evidence, но не является доказательством completeness.

### Independent verification

Candidate становится finding только после проверки фактического пути исполнения, ownership, существующих controls и concrete consequence. Severity назначается после correctness verification.

Для серьёзного security finding требуется правдоподобная attack chain; отсутствие hardening само по себе не является HIGH/CRITICAL.

---

# Test Assurance и Test Engineering

## Test Assurance

Test Assurance отвечает не на вопрос «тесты зелёные или нет», а на более строгий вопрос:

> Какие существенные поведения системы реально подтверждены исполняемыми доказательствами, какие подтверждены частично, какие не подтверждены и какие тесты могут создавать ложную уверенность?

Для общего verdict нужен bounded inventory material assurance targets. Test Assurance сохраняет существующие совместимые outputs:

```text
00-test-assurance-summary.md
01-test-assurance-map.md
02-test-plan.md              # optional
```

`00-test-assurance-summary.md` — короткий пользовательский decision layer: verdict, сильные стороны, главные слабости, bounded accounting, приоритеты и важные limitations.

`01-test-assurance-map.md` — подробная evidence/authority карта.

`02-test-plan.md` — инженерный план тестовых работ, когда он выбран.

---

## Единая Behavior Contract Model

Расширенный Test Engineering не позволяет Test Plan, Contract Verification, Simulator и E2E независимо придумывать продуктовую семантику.

Используется один bounded Behavior Contract Model:

```text
accepted architecture / observed implementation / declared contracts / consumers
                              |
                              v
                     Behavior Contract Model
                           BC-*
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
 Contract Verification   Test Design       Scenario Design
       CC-*                  |              /          \
                             v             v            v
                    Test Environment   Simulator       E2E
                         Design          Design        Design
```

### Идентификаторы

```text
RF-*    Architecture/root finding
        Почему механизм или архитектурная граница проблемны.

BC-*    Behavior Contract
        Одно independently verifiable material behavior.

CC-*    Contract Consistency Record
        Наблюдаемое расхождение между contract views.

MAT-*   Material Assurance Target
        Что Test Assurance обязуется учесть в bounded inventory.

TM-*    Test Mapping
        Исполняемое evidence, привязанное к MAT/BC.

GAP-*   Assurance Gap
        Missing / partial / misleading / inadequate evidence.

TASK-*  Test Engineering remediation task.

WS-*    Working-set / investigation record.
```

Нормативные границы:

```text
BC != MAT
BC != RF
BC != GAP
CC != GAP
```

`BC-*` отвечает на вопрос **«какое поведение?»**.

`TM-*` отвечает на вопрос **«что это поведение доказывает?»**.

Поэтому executable evidence не хранится внутри `BC-*`.

Один architectural finding может породить несколько отдельных behaviors:

```text
RF-012 stale generation can overwrite terminal state
  -> BC-027 only current generation may publish terminal state
  -> BC-028 superseded completion must not mutate authoritative state
  -> BC-029 cancellation/retry must not transfer publication ownership
```

Один BC — одно независимо проверяемое существенное поведение. Большие «контракты-комбайны» вроде «order processing works correctly including auth/retries/events/errors» должны раскладываться на отдельные BC.

---

## Ownership BC и CC

Принятую семантику `BC-*` может менять только Behavior Model gate.

Другие части capability могут создавать:

```text
BC_CANDIDATE
BC_REVALIDATION_REQUEST
BC_CONFLICT_OBSERVED
```

но не переписывают accepted BC напрямую.

Аналогично authoritative state/classification `CC-*` принадлежит Contract Verification. Другие gates могут сообщить `CONTRACT_CONFLICT_OBSERVED`, но не назначают окончательную классификацию сами.

Это предотвращает скрытое изменение product semantics из Test Plan, Simulator или E2E.

---

## Lifecycle, freshness и authority

Для Behavior Contract используются отдельные оси, а не один гигантский status enum.

Semantic lifecycle:

```text
CANDIDATE
UNDER_REVIEW
ACCEPTED
SUPERSEDED
REJECTED
```

Freshness:

```text
VALID
REVALIDATION_REQUIRED
UNKNOWN
```

Authority:

```text
RESOLVED
UNRESOLVED
```

Стабильная semantic identity сохраняется через revisions:

```text
BC-042@rev1
BC-042@rev2
BC-042@rev3
```

Если изменилось уже само поведение, старый BC может стать `SUPERSEDED`, а новый получить другой ID.

Downstream artifacts должны ссылаться на конкретную revision, когда это важно для freshness/provenance.

---

## Contract Verification: Swagger/OpenAPI vs code vs consumers vs tests

Если проект публикует declared contract, Skill не считает его автоматически истинным.

Сравниваются четыре представления:

```text
DECLARED      OpenAPI / Swagger / protobuf / AsyncAPI / docs
IMPLEMENTED   реальные routes / handlers / DTO / serializer / auth / errors
CONSUMED      frontend / SDK / CLI / peer services
TESTED        тесты, которые кодируют или утверждают поведение
```

Это **views**, а не levels of authority.

Swagger не получает автоматический приоритет.

Код не получает автоматический приоритет.

Consumer behavior и tests тоже не получают автоматический приоритет.

При конфликте создаётся `CC-*` и отдельно выполняется authority resolution.

Пример:

```text
CC-017
subject:
  POST /orders duplicate-order response
related_behavior:
  BC-044
DECLARED:
  OpenAPI: 201, 400
IMPLEMENTED:
  code: 201, 400, 409 DuplicateOrder
CONSUMED:
  checkout-ui handles 409 DuplicateOrder
TESTED:
  integration tests cover 201, 400
classification:
  AUTHORITY_UNRESOLVED
```

Материально проверяются не только method/path, но и при наличии соответствующего контракта:

- request/response schemas;
- required/optional/nullable/default semantics;
- enum values;
- status codes;
- headers;
- authentication/authorization;
- error contracts;
- pagination/versioning;
- events/messages;
- state transitions;
- side effects;
- ordering;
- idempotency;
- retries/cancellation.

Возможные classified outcomes включают:

```text
DECLARATION_STALE
IMPLEMENTATION_DEFECT
CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR
TEST_ENCODES_STALE_CONTRACT
INTENTIONAL_COMPATIBILITY_BEHAVIOR
CONTRACT_UNRESOLVED
AUTHORITY_UNRESOLVED
```

### CC resolution не переписывает BC

```text
CC resolved
    |
    v
BC impact analysis
    |
    +-- no semantic change -> BC remains valid
    |
    +-- semantic impact -> BC freshness = REVALIDATION_REQUIRED
```

Только Behavior Model может выпустить новую BC revision.

---

## Contract drift и Test Gap — разные вещи

Контрактное расхождение не равно отсутствию тестового evidence.

Например:

```text
Swagger не описывает 409
implementation возвращает 409
consumer умеет 409
тесты полностью доказывают 409 behavior
```

Тогда существует `CC-*`, но `GAP-*` создавать автоматически не нужно.

Если 409 ещё и не подтверждён тестами, могут существовать обе независимые проблемы:

```text
CC-017
  |
  +-- BC-044
        |
        +-- MAT-031
              |
              +-- GAP-012
```

---

## Test Engineering dependency DAG

Capability не является фиксированным линейным pipeline.

```text
Test Assurance
    |
    +-- Test Plan
    |
    +-- Behavior Model [internal when needed]
           |
           +-- Contract Verification [automatic when applicable]
           |
           +-- Test Environment Design
           |
           +-- Service Simulator Design
           |       |
           |       +-- Service Simulator Implementation Plan
           |
           +-- E2E Test Plan
```

Выполняется **minimum necessary dependency slice**.

Например, если пользователь выбирает только `E2E Test Plan`, Skill может подключить Test Assurance, Behavior Model и применимый Contract Verification, но не обязан автоматически проектировать Service Simulator.

`EXTEND` переиспользует accepted/fresh upstream artifacts вместо полного rerun.

`USE_EXISTING` разрешён только если требуемый slice accepted, fresh и достаточно authority-resolved.

---

## Persisted Test Engineering outputs

Выбор outputs является частью persisted capability state/`working/INDEX.md`, чтобы `RESUME`, `EXTEND`, `USE_EXISTING` и `REVALIDATE` могли восстановить тот же requested slice.

Концептуально:

```yaml
outputs:
  test_assurance: true
  test_plan: false
  contract_consistency_report: false
  test_environment_design: false
  service_simulator_design: false
  service_simulator_implementation_plan: false
  e2e_test_plan: true
```

Эти поля независимы. Не создаются compound modes вроде `REVIEW_PLUS_SIMULATOR_PLUS_E2E`.

---

## Impact-driven REVALIDATE

Freshness считается по affected semantics, а не просто по факту смены Git HEAD.

### Tests-only change

```text
tests changed
  -> TM revalidation
  -> MAT assurance may change
  -> GAP may close/open
```

Это обычно **не означает автоматическую invalidation BC**.

### Implementation / OpenAPI change

```text
implementation or declared contract changed
  -> affected IMPLEMENTED / DECLARED views
  -> Contract Verification when relevant
  -> BC impact analysis
```

### Consumer-only change

```text
service unchanged
consumer changed
  -> CONSUMED view revalidation
  -> CC may change
  -> consumer-facing simulator scenarios may change
  -> affected E2E may require revalidation
```

Поэтому multi-repository bindings — first-class freshness inputs.

---

## Test Environment Design

Для зависимостей **reviewed service** стратегия выбирается отдельно для каждой dependency:

```text
REAL_DISPOSABLE
SERVICE_EMULATOR
CONTROLLABLE_MOCK
IN_PROCESS_DOUBLE
TEMP_RESOURCE
NOT_REQUIRED
```

Правило:

> **Mock external uncertainty, not the behavior under test.**

Если существенное поведение зависит от реальных транзакций, expiry, ordering, constraints или persistence semantics, нельзя автоматически заменить его удобным mock.

---

## Service Simulator Design

Skill различает две разные задачи:

```text
A) substitutes for dependencies OF reviewed service
B) simulator OF reviewed service FOR its consumers
```

Service Simulator может включать:

```text
Contract API
State Store
Scenario Engine
Fault Injection
Event Emitter
Control API
Health / Reset / Seed
```

Consumer plane должен соответствовать materially relevant real protocol.

Test-only control plane должен оставаться отдельным, например:

```text
/__test/health
/__test/reset
/__test/scenario
/__test/state
/__test/seed
```

Simulator не генерируется слепо из Swagger:

```text
Swagger + implementation + consumers
        |
        v
Contract Verification
        |
        v
accepted BC
        |
        v
Simulator scenarios
```

`Service Simulator Implementation Plan` — отдельный explicit output после accepted/fresh Simulator Spec. Сам review Skill не пишет simulator runtime автоматически.

---

## E2E Design

E2E нужен только там, где assurance действительно зависит от нескольких реальных компонентов и не может быть доказан на меньшей границе с той же или лучшей надёжностью.

Каждый E2E scenario должен фиксировать:

- source BC revision;
- participating real components;
- allowed simulators/fakes;
- initial state;
- stimulus;
- material assertions;
- failure observability;
- cleanup/reset;
- CI suitability;
- execution cost, когда это существенно.

E2E не требует Service Simulator автоматически.

---

## Test Engineering artifacts

Совместимость Test Review сохраняется, а расширенная модель добавляет новые projections:

```text
test-review/
├── 00-test-assurance-summary.md
├── 01-test-assurance-map.md
├── 02-test-plan.md                              # optional, compatibility
├── 03-behavior-contract-model.md                # when extended model is needed
├── 04-contract-consistency-report.md            # optional user-facing projection
├── 05-test-environment-design.md                 # optional
├── 06-service-simulator-spec.md                  # optional
├── 07-service-simulator-implementation-plan.md   # optional
├── 08-e2e-test-plan.md                           # optional
└── working/
    ├── INDEX.md
    ├── behavior-contracts.md                     # authoritative BC ledger
    ├── contract-verification.md                  # authoritative CC ledger
    ├── test-mappings.md
    ├── assurance-gaps.md
    └── ...
```

Нумерация не задаёт dependency order.

`working/behavior-contracts.md` и `working/contract-verification.md` — semantic authority. `03-*` и `04-*` — human-readable projections.

Различаются состояния:

```text
NOT_APPLICABLE
NOT_VERIFIED
VERIFIED_NO_MATERIAL_ISSUES
```

Отсутствие применимого declared contract — это `NOT_APPLICABLE`, а не `NOT_VERIFIED`.

---

## Общие принципы доказательности

**Сначала authority, потом verdict.** Если значимые источники противоречат друг другу и precedence не определён, результат остаётся unresolved.

**Claim scope <= evidence scope.** Узкая проверка даёт узкий вывод.

**Completeness требует bounded accounting.** Случайная выборка не является доказательством полноты.

**RF, BC, MAT, TM, GAP и CC не взаимозаменяемы.** Каждый identifier имеет собственную ответственность.

**Projection не становится authority только потому, что выглядит красиво.** Human-readable документы выводятся из accepted technical state.

---

## Повторный запуск и freshness

`REVALIDATE` по умолчанию работает только с affected slice:

```text
accepted baseline A
  -> current baseline B
  -> changed inputs
  -> impact analysis
  -> minimum affected semantic slice
  -> fresh evidence
  -> revalidation
  -> preserved unaffected state
```

`preserved` означает только отсутствие найденной зависимости, требующей fresh verification. Это не новый GREEN.

Если изменение системное, Skill может вернуть `FULL_REAUDIT_RECOMMENDED`, но не превращает `REVALIDATE` в `NEW` без решения пользователя.

---

## PROJECTION_REPAIR

Этот режим предназначен только для presentation-level исправлений:

- язык;
- структура;
- Markdown;
- Mermaid;
- ссылки/cross-references;
- таблицы;
- навигация;
- терминология;
- устаревшая пользовательская проекция.

Он не может менять:

- BC semantics;
- CC classification;
- MAT accounting;
- TM verdict;
- GAP existence;
- TASK semantic priority;
- accepted findings/severity;
- simulator scenario behavior;
- E2E topology semantics.

Если semantic change необходим — `TECHNICAL_REVALIDATION_REQUIRED`.

---

## Project Profile и dirty working tree

Project Profile — локальная routing/estimation metadata, а не substantive architecture evidence. Он включает количество substantive tracked files, строки, символы, language footprint и отдельный учёт generated/vendor/build/binary material.

При dirty working tree рекомендуемый baseline — committed `HEAD`.

```text
1. Audit committed HEAD only — recommended
2. Include working-tree changes as EPHEMERAL snapshot
3. Stop
```

`EPHEMERAL` должен сохранять deterministic fingerprint и не представляться как обычный reproducible Git commit baseline.

---

## Итоговый audit package

По умолчанию:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md                    # optional
├── 04-remediation-roadmap.md                    # optional
├── test-review/
│   ├── 00-test-assurance-summary.md
│   ├── 01-test-assurance-map.md
│   ├── 02-test-plan.md                          # optional
│   ├── 03-behavior-contract-model.md            # optional
│   ├── 04-contract-consistency-report.md        # optional
│   ├── 05-test-environment-design.md            # optional
│   ├── 06-service-simulator-spec.md              # optional
│   ├── 07-service-simulator-implementation-plan.md # optional
│   ├── 08-e2e-test-plan.md                       # optional
│   └── working/
│       └── ... capability authority/evidence
└── working/
    └── ... umbrella audit authority/evidence
```

Финальные документы предназначены для человека: **что происходит → почему это важно → к чему приводит → что менять**. Internal IDs помогают трассировке, но не заменяют объяснение.

---

# Установка

## Codex, OpenCode и другие агенты с `~/.agents/skills`

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новую agent session, чтобы Skill был заново обнаружен.

Обновление:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Проверка установленной ревизии:

```bash
cd ~/.agents/skills/architecture-code-review
git rev-parse HEAD
```

Для воспроизводимого historical release можно checkout конкретный tag, если он существует:

```bash
git fetch --tags
git checkout <release-tag>
```

Вернуться на `main`:

```bash
git switch main
git pull --ff-only
```

---

# Использование

Самый простой запрос:

```text
Используй architecture-code-review для этого проекта.
```

Skill сам обнаружит applicable previous audit и предложит Session Intent.

## Новый Architecture Review без Test Engineering

```text
Используй architecture-code-review.
Начни NEW аудит.
Architecture Review: STANDARD_FULL.
Результат: REVIEW_ONLY.
Test Engineering: OFF.
```

Максимальная глубина:

```text
Используй architecture-code-review.
Начни NEW аудит.
Architecture Review: FORENSIC.
Результат: REVIEW_ONLY.
Test Engineering: OFF.
```

## Architecture Review + Target Architecture + Roadmap

```text
Используй architecture-code-review.
Начни NEW аудит.
Architecture Review: STANDARD_FULL.
Результат: REVIEW_PLUS_TARGET_AND_ROADMAP.
Test Engineering: OFF.
```

## Test Assurance + Test Plan

```text
Используй architecture-code-review.
Начни NEW аудит.
Architecture Review: STANDARD_FULL.
Результат: REVIEW_ONLY.
Test Engineering outputs:
- Test Assurance
- Test Plan
```

## Полный Test Engineering design

```text
Используй architecture-code-review.
Начни NEW аудит.
Architecture Review: STANDARD_FULL.
Результат: REVIEW_ONLY.
Test Engineering outputs:
- Test Assurance
- Test Plan
- Contract Consistency Report
- Test Environment Design
- Service Simulator Design
- Service Simulator Implementation Plan
- E2E Test Plan
```

Skill должен сам разрешить внутренние зависимости, но не включать невыбранные substantial outputs без необходимости.

## Только Contract Consistency Report поверх принятого Test Assurance

```text
Используй architecture-code-review.
EXTEND существующий принятый audit package.
Добавь Test Engineering output:
- Contract Consistency Report
Не переоткрывай несвязанные принятые gates.
```

## Добавить Service Simulator Design

```text
Используй architecture-code-review.
EXTEND существующий принятый Test Assurance.
Добавь:
- Service Simulator Design
Переиспользуй accepted/fresh Behavior Contracts и Contract Verification.
Не перезапускай весь Architecture Review.
```

## Добавить E2E Plan без автоматического simulator

```text
Используй architecture-code-review.
EXTEND существующий принятый audit package.
Добавь:
- E2E Test Plan
Не включай Service Simulator Design автоматически, если выбранная topology его не требует.
```

## RESUME

```text
Используй architecture-code-review.
RESUME существующий незавершённый аудит.
Сначала reconcile INDEX, authority bindings, baseline и persisted Test Engineering outputs.
Продолжи с первого незавершённого valid gate.
```

## USE_EXISTING

```text
Используй architecture-code-review.
USE_EXISTING для текущего принятого аудита.
Техническую работу заново не запускай.
Используй только accepted/fresh/sufficiently-resolved dependency slice.
```

## REVALIDATE

```text
Используй architecture-code-review.
REVALIDATE предыдущий принятый аудит относительно текущего HEAD.
Сначала выполни impact analysis.
Не инвалидируй все BC/TM/GAP/scenarios автоматически только из-за изменения HEAD.
```

## PROJECTION_REPAIR

```text
Используй architecture-code-review.
PROJECTION_REPAIR принятого audit package.
Исправь только пользовательские Markdown/Mermaid/links/wording.
Если нужно изменить technical semantics, остановись с TECHNICAL_REVALIDATION_REQUIRED.
```

## Dirty working tree

Проверить только reproducible committed baseline:

```text
Используй architecture-code-review.
Проверяй только committed HEAD.
Незакоммиченные изменения не включай в technical conclusions.
```

Включить текущее рабочее дерево сознательно:

```text
Используй architecture-code-review.
Включи текущее рабочее дерево как EPHEMERAL snapshot.
Я понимаю, что это не обычный reproducible commit baseline.
```

---

# Структура репозитория

```text
.
├── README.md
├── LICENSE
├── SKILL.md
├── capabilities/
│   └── test-review/
│       ├── SKILL.md
│       └── references/
│           └── test-engineering-contract.md
├── references/
│   ├── session-orchestration.md
│   ├── review-modes-and-orchestration.md
│   ├── revalidation-and-freshness.md
│   ├── shared-assurance-principles.md
│   ├── review-method.md
│   ├── discovery-coverage.md
│   ├── ownership-and-scenarios.md
│   ├── boundary-contract-audit.md
│   ├── independent-verification.md
│   ├── root-boundary-adjudication.md
│   ├── evidence-and-severity.md
│   ├── lifecycle-and-mermaid.md
│   ├── report-contract.md
│   ├── target-architecture-review.md
│   ├── remediation-roadmap-review.md
│   ├── final-editorial-review.md
│   └── stacks/
│       ├── ansible.md
│       ├── django.md
│       ├── electron.md
│       ├── fastapi.md
│       ├── litestar.md
│       ├── react.md
│       └── tauri.md
├── tests/
│   ├── pressure-scenario-79-test-assurance-summary.md
│   ├── pressure-scenario-81-behavior-contract-boundary.md
│   ├── pressure-scenario-82-contract-verification-authority.md
│   ├── pressure-scenario-83-contract-drift-vs-test-gap.md
│   ├── pressure-scenario-84-test-engineering-dependency-slice.md
│   ├── pressure-scenario-85-test-engineering-revalidation.md
│   ├── pressure-scenario-86-service-simulator-e2e-boundaries.md
│   ├── pressure-scenario-87-output-selection-persistence.md
│   └── test-engineering-capability-validation.md
└── docs/
    └── superpowers/
        ├── specs/
        └── plans/
```

`SKILL.md` остаётся компактным umbrella orchestrator.

Detailed Test Engineering semantics принадлежат `capabilities/test-review/references/test-engineering-contract.md`.

Session/startup policy принадлежит `references/session-orchestration.md`.

Persisted capability state и dependency orchestration принадлежат `references/review-modes-and-orchestration.md`.

Freshness/impact-driven revalidation принадлежит `references/revalidation-and-freshness.md`.

---

# Проверка изменений Skill

Изменение Markdown-инструкций Skill считается изменением поведения.

Поэтому существенные изменения проходят дисциплину:

```text
design
  -> implementation plan
  -> RED pressure contract
  -> implementation
  -> fresh independent pressure execution
  -> independent review
  -> targeted remediation
  -> fresh re-review
  -> promotion readiness
  -> merge
```

Для Test Engineering в репозитории есть отдельные pressure scenarios:

```text
PS-81  BC vs MAT/RF/GAP/TM boundary
PS-82  contract authority / no automatic Swagger winner
PS-83  contract drift vs assurance gap
PS-84  minimum dependency slice
PS-85  impact-driven revalidation
PS-86  Service Simulator / E2E boundaries
PS-87  persisted independent output selection
```

Validation evidence revision-bound. Нельзя считать старый GREEN вечным доказательством для любого будущего `main`.

Статическая проверка contract text и fresh independent agent execution — разные виды evidence и должны отмечаться отдельно.

Для этого Markdown Skill application/coordinator runtime может быть `NOT_APPLICABLE`; это не мешает выполнять fresh agent-level behavioral pressure scenarios.

---

# Язык итоговых документов

Пользовательский язык следует языку текущего запроса пользователя, если он явно не попросил другой.

Для русскоязычного пользователя финальные документы должны быть нормальным связным русским техническим текстом.

Не переводятся exact identifiers, paths, API/IPC/protocol names, formal status tokens и имена файлов.

Internal ledger/handoff shorthand используется для traceability, но не должен превращать финальный отчёт в agent scratchpad.

---

# Лицензия

См. `LICENSE`.
