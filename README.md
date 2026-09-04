# Architecture Code Review

`architecture-code-review` — Skill для глубокого архитектурного и кодового аудита существующих систем с опорой на проверяемые доказательства.

Его задача — не собрать длинный список «подозрительных мест», а восстановить, **как система действительно устроена и работает**, определить владельцев состояния и ресурсов, проследить важные сценарии исполнения и только после этого формулировать выводы.

В основе методологии лежит простой принцип:

> **Ширина утверждения не должна превышать ширину доказательств.**

Если проверен один обработчик, это не доказывает корректность всей модели авторизации. Если работает обычный сценарий, это ещё не подтверждает правильность повторных попыток, восстановления после сбоя, конкурентного выполнения или остановки процесса. Если доказательств недостаточно, результат остаётся `PARTIAL`, `NOT_PROVEN`, `UNKNOWN` или `AUTHORITY_UNRESOLVED`, а не превращается в предположение, выданное за факт.

Skill подходит для аудита всего репозитория, отдельной подсистемы и повторной проверки уже проаудированного проекта.

---

## Оглавление

- [Основные возможности](#основные-возможности)
- [Как начинается работа](#как-начинается-работа)
  - [Session Intent](#session-intent)
  - [Новый аудит](#новый-аудит-new)
  - [Совместимость со старым Test Review](#совместимость-со-старым-test-review)
- [Как устроен Architecture Review](#как-устроен-architecture-review)
- [Test Assurance и Test Engineering](#test-assurance-и-test-engineering)
  - [Test Assurance](#test-assurance)
  - [Behavior Contract Model](#behavior-contract-model)
  - [Идентификаторы](#идентификаторы)
  - [Владение BC и CC](#владение-bc-и-cc)
  - [Жизненный цикл, актуальность и authority](#жизненный-цикл-актуальность-и-authority)
  - [Contract Verification](#contract-verification)
  - [Contract drift и Test Gap](#contract-drift-и-test-gap)
  - [Граф зависимостей Test Engineering](#граф-зависимостей-test-engineering)
  - [Сохранение выбранных результатов](#сохранение-выбранных-результатов)
  - [Точечная повторная проверка](#точечная-повторная-проверка)
  - [Test Environment Design](#test-environment-design)
  - [Service Simulator Design](#service-simulator-design)
  - [E2E Design](#e2e-design)
  - [Артефакты Test Engineering](#артефакты-test-engineering)
- [Общие принципы доказательности](#общие-принципы-доказательности)
- [Повторный запуск и актуальность](#повторный-запуск-и-актуальность)
- [PROJECTION_REPAIR](#projection_repair)
- [Project Profile и изменённое рабочее дерево](#project-profile-и-изменённое-рабочее-дерево)
- [Итоговый пакет аудита](#итоговый-пакет-аудита)
- [Установка](#установка)
- [Использование](#использование)
- [Структура репозитория](#структура-репозитория)
- [Roadmap](docs/roadmap.md)
- [Проверка изменений Skill](#проверка-изменений-skill)
- [Язык итоговых документов](#язык-итоговых-документов)
- [Лицензия](#лицензия)

---

## Основные возможности

Skill объединяет несколько связанных, но не смешанных областей работы:

- **Architecture Review** — восстановление фактической архитектуры, проверка границ ответственности, владения состоянием, жизненного цикла, конкурентного выполнения, доверительных границ, надёжности, сопровождаемости и тестируемости;
- **Target Architecture** — проектирование целевой архитектуры после подтверждения проблем;
- **Remediation Roadmap** — определение порядка исправлений и зависимостей между ними;
- **Test Assurance** — оценка того, какие существенные поведения действительно подтверждаются существующими тестами;
- **Test Engineering** — проектирование недостающих тестов, проверка контрактов, проектирование тестового окружения, Service Simulator и E2E-сценариев;
- **`REVALIDATE` / `EXTEND` / `PROJECTION_REPAIR`** — повторное использование уже принятой работы без автоматического полного аудита заново.

Для Tauri, Electron, React, Django, FastAPI, Litestar и Ansible предусмотрены дополнительные технологические проверки. Они дополняют общую методологию, но не становятся отдельными верхнеуровневыми capabilities.

---

## Как начинается работа

Начиная с Orchestrator v0.3, Skill не начинает новый аудит автоматически. Сначала он определяет репозиторий и выбранную ревизию, проверяет состояние рабочего дерева, ищет предыдущие пакеты аудита и согласует их актуальность.

Упрощённо запуск выглядит так:

```text
репозиторий + ревизия + рабочее дерево
        |
        v
поиск предыдущих аудитов
        |
        v
проверка authority / lineage / freshness
        |
        v
Project Profile
        |
        v
Session Intent
        |
        v
выбор требуемых результатов
        |
        v
минимально необходимая техническая работа
```

Повторный запуск Skill не означает автоматический повтор всего аудита.

### Session Intent

Поддерживаются шесть вариантов:

- `USE_EXISTING` — использовать уже принятый аудит для той же зафиксированной ревизии;
- `NEW` — начать новый аудит в явно заданных границах;
- `RESUME` — продолжить незавершённый аудит после проверки состояния, authority и актуальности;
- `REVALIDATE` — проверить изменения относительно принятой ревизии;
- `EXTEND` — добавить новый результат или capability, не повторяя несвязанные принятые этапы;
- `PROJECTION_REPAIR` — исправить только финальные пользовательские документы без изменения принятой технической семантики.

Типичные рекомендации:

```text
предыдущего аудита нет                         -> NEW
IN_PROGRESS                                    -> RESUME
COMPLETE + тот же HEAD                         -> USE_EXISTING
COMPLETE + изменившийся HEAD                   -> REVALIDATE
нужен новый результат или capability           -> EXTEND
нужно исправить только финальные документы     -> PROJECTION_REPAIR
```

`RESUME_WITH_RECONCILIATION` — внутренний вариант выполнения `RESUME`, а не отдельный сохраняемый Session Intent.

`PROJECTION_REPAIR` не заменяет `REVALIDATE`. Если для исправления Markdown-документа требуется изменить evidence, root cause, severity, ownership, invariant, `BC-*`, `CC-*`, Target Architecture или Roadmap, Skill должен остановить редакционный путь с `SEMANTIC_DRIFT_DETECTED` и `TECHNICAL_REVALIDATION_REQUIRED`.

### Новый аудит (`NEW`)

Architecture Review и Test Engineering настраиваются независимо.

#### Глубина Architecture Review

```text
STANDARD_FULL
FORENSIC
```

`STANDARD_FULL` подходит для большинства полноценных архитектурных проверок.

`FORENSIC` используется, когда требуется более глубокое расследование сложного жизненного цикла, конкурентности, восстановления после сбоев, нескольких процессов или неоднозначных доверительных границ.

Выбор `FORENSIC` сам по себе не означает, что нужно строить Target Architecture или Roadmap.

#### Итоговый результат Architecture Review

```text
REVIEW_ONLY
REVIEW_PLUS_TARGET_ARCHITECTURE
REVIEW_PLUS_TARGET_AND_ROADMAP
```

#### Результаты Test Engineering

Современная модель Test Engineering хранит каждый запрошенный результат отдельно:

```text
Test Engineering: OFF
или:
[x] Test Assurance
[ ] Test Plan
[ ] Contract Consistency Report
[ ] Test Environment Design
[ ] Service Simulator Design
[ ] Service Simulator Implementation Plan
[ ] E2E Test Plan
```

Например, в первом запуске пользователь может включить Test Engineering и
выбрать `Test Assurance`, `Test Environment Design` и `E2E Test Plan`, оставив
остальные результаты выключенными. Этот выбор сохраняется напрямую в
независимых полях `outputs`; он не кодируется через legacy endpoint.

`Test Assurance` остаётся обязательным ядром Test Engineering.

`Behavior Model` не является пользовательским переключателем. Он подключается как внутренняя зависимость, когда выбранным результатам нужна единая модель существенного поведения.

`Contract Verification` также не является необязательным пользовательским выбором. Если существует существенный внешний контракт — например OpenAPI/Swagger, protobuf/gRPC schema, AsyncAPI или другой формализованный интерфейс, — Skill автоматически сравнивает четыре представления: `DECLARED`, `IMPLEMENTED`, `CONSUMED` и `TESTED`.

`Contract Consistency Report` при этом остаётся необязательным пользовательским документом: саму проверку контракта нельзя отключить, если она действительно применима, но отдельный отчёт создавать не обязательно.

Skill может рекомендовать дополнительные результаты, однако не должен молча включать существенный объём дополнительной работы.

### Совместимость со старым Test Review

Старые пакеты аудита могут хранить режимы:

```text
REVIEW_ONLY
REVIEW_PLUS_TEST_PLAN
```

Они по-прежнему поддерживаются при `RESUME`, `USE_EXISTING` и reconciliation, но больше не являются основной моделью настройки Test Engineering.

Нормализация выполняется консервативно:

```text
legacy REVIEW_ONLY
  -> test_assurance=true
  -> все необязательные результаты Test Engineering=false

legacy REVIEW_PLUS_TEST_PLAN
  -> test_assurance=true
  -> test_plan=true
  -> все остальные необязательные результаты=false
```

Старое состояние никогда не должно само включать E2E, Service Simulator, Test Environment Design или Contract Consistency Report.

---

## Как устроен Architecture Review

Базовый поток нового полного аудита выглядит так:

```text
зафиксированная ревизия
  -> As-Built Architecture
  -> независимая проверка As-Built
  -> тематическое исследование
  -> Discovery Coverage Matrix
  -> Independent Coverage Review
  -> независимая проверка кандидатов
  -> root-boundary adjudication
  -> назначение severity
  -> Authoritative Findings Ledger
  -> при необходимости Target Architecture
  -> при необходимости Remediation Roadmap
  -> сборка итогового пакета
  -> редакционная проверка и повторная проверка
```

### As-Built Architecture

До поиска проблем агент восстанавливает фактическую систему: основные компоненты и процессы, владельцев состояния, потоки данных, ключевые границы и существенные сценарии выполнения.

Это не пересказ README проекта и не предположение по названиям директорий. Существенные архитектурные утверждения должны опираться на реальные пути исполнения и конкретные источники.

### Discovery Coverage

Полнота аудита не измеряется количеством найденных замечаний.

Перед общим выводом формируется ограниченный перечень существенных областей и механизмов в заявленных границах проверки. Для каждой области должно быть понятно, чем она покрыта, почему неприменима, что заблокировано и что осталось неизвестным.

Выборочное глубокое исследование допустимо для получения качественных доказательств, но случайная выборка сама по себе не доказывает полноту.

### Независимая проверка

Кандидат становится подтверждённой проблемой только после проверки фактического пути исполнения, владения состоянием или ресурсом, существующих защитных механизмов и конкретного последствия.

Severity назначается после проверки корректности самого finding, а не по первому впечатлению.

Для серьёзного security finding нужна правдоподобная цепочка атаки: кто атакует, через какую поверхность, при каких предпосылках и к какому результату это приводит. Само по себе отсутствие дополнительного hardening не является основанием для HIGH или CRITICAL.

---

# Test Assurance и Test Engineering

## Test Assurance

Test Assurance отвечает не на вопрос «тесты зелёные или нет», а на более строгий вопрос:

> Какие существенные поведения системы действительно подтверждены исполняемыми тестами, какие подтверждены частично, какие не подтверждены и какие тесты могут создавать ложное чувство уверенности?

Для общего вывода нужен явный ограниченный перечень существенных целей проверки. Test Assurance сохраняет совместимые документы:

```text
00-test-assurance-summary.md
01-test-assurance-map.md
02-test-plan.md              # необязательный
```

`00-test-assurance-summary.md` — короткое пользовательское резюме. Оно должно быстро отвечать на вопросы: можно ли доверять текущей системе тестов, что защищено хорошо, где находятся основные пробелы и что стоит исправлять первым.

`01-test-assurance-map.md` — подробная карта доказательств, authority и покрытия.

`02-test-plan.md` — инженерный план тестовых работ, если пользователь его выбрал.

---

## Behavior Contract Model

Расширенный Test Engineering использует единую модель поведения, чтобы Test Plan, Contract Verification, Service Simulator и E2E не могли независимо придумывать продуктовую семантику.

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

`BC-*` фиксирует одно существенное поведение, которое можно проверить независимо от других поведений.

Например:

```text
BC-001 Неаутентифицированный POST /orders отклоняется.
BC-002 Тайм-аут оплаты не создаёт второй заказ.
BC-003 Повторная попытка может перевести тот же заказ в COMPLETED.
BC-004 На один заказ публикуется не более одного события завершения.
```

Большие формулировки вроде «обработка заказов работает правильно с учётом авторизации, retries, событий и ошибок» должны раскладываться на отдельные `BC-*`.

### Идентификаторы

```text
RF-*    Architecture/root finding
        Подтверждённая архитектурная или корневая проблема.

BC-*    Behavior Contract
        Одно независимо проверяемое существенное поведение.

CC-*    Contract Consistency Record
        Зафиксированное расхождение между представлениями контракта.

MAT-*   Material Assurance Target
        Существенная цель, которую Test Assurance обязан учесть.

TM-*    Test Mapping
        Исполняемое доказательство, привязанное к MAT/BC.

GAP-*   Assurance Gap
        Отсутствующее, частичное, вводящее в заблуждение или недостаточное доказательство.

TASK-*  Test Engineering remediation task
        Инженерная работа, необходимая для устранения подтверждённого пробела.

WS-*    Working-set / investigation record
        Временное рабочее состояние исследования.
```

Нормативные границы:

```text
BC != MAT
BC != RF
BC != GAP
CC != GAP
```

`BC-*` отвечает на вопрос: **«Какое поведение должно выполняться?»**

`TM-*` отвечает на вопрос: **«Какое исполняемое доказательство подтверждает это поведение?»**

Поэтому сведения о существующих тестах и их результатах не хранятся внутри `BC-*`.

Один архитектурный finding может породить несколько отдельных поведений:

```text
RF-012 stale generation can overwrite terminal state
  -> BC-027 only current generation may publish terminal state
  -> BC-028 superseded completion must not mutate authoritative state
  -> BC-029 cancellation/retry must not transfer publication ownership
```

---

### Владение BC и CC

Принятую семантику `BC-*` может менять только Behavior Model gate.

Остальные части capability могут создавать:

```text
BC_CANDIDATE
BC_REVALIDATION_REQUEST
BC_CONFLICT_OBSERVED
```

но не могут напрямую переписывать принятый Behavior Contract.

Состояние и классификация `CC-*` принадлежат Contract Verification. Другие этапы могут сообщить `CONTRACT_CONFLICT_OBSERVED`, но не назначают окончательную классификацию самостоятельно.

Это предотвращает ситуацию, когда Test Plan, Service Simulator или E2E незаметно меняют продуктовую семантику ради собственного сценария.

---

### Жизненный цикл, актуальность и authority

Для Behavior Contract используются три независимые оси, а не один общий статус.

Жизненный цикл:

```text
CANDIDATE
UNDER_REVIEW
ACCEPTED
SUPERSEDED
REJECTED
```

Актуальность:

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

Если смысл поведения сохраняется, его идентификатор остаётся стабильным, а изменения отражаются ревизиями:

```text
BC-042@rev1
BC-042@rev2
BC-042@rev3
```

Если изменилось само поведение, старый BC может получить статус `SUPERSEDED`, а новое поведение — новый идентификатор.

Зависимые артефакты должны ссылаться на конкретную ревизию там, где это важно для актуальности и provenance.

---

## Contract Verification

Если проект публикует формализованный внешний контракт, Skill не считает его автоматически единственным источником истины.

Сравниваются четыре представления:

```text
DECLARED      OpenAPI / Swagger / protobuf / AsyncAPI / документация
IMPLEMENTED   реальные routes / handlers / DTO / serializers / auth / errors
CONSUMED      frontend / SDK / CLI / другие сервисы
TESTED        тесты, которые кодируют или проверяют это поведение
```

Это разные представления одного контракта, а не иерархия authority.

Swagger не получает автоматический приоритет. Код тоже не считается нормативным только потому, что он исполняется. Поведение потребителя и существующие тесты также не становятся источником истины автоматически.

Если представления расходятся, создаётся `CC-*`, после чего конфликт проходит отдельное разрешение authority.

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

Когда контракт это позволяет, сравниваются не только method и path, но также:

- схемы запросов и ответов;
- обязательные и необязательные поля;
- типы, `nullable` и значения по умолчанию;
- enum-значения;
- status codes;
- headers;
- authentication и authorization;
- формат ошибок;
- pagination и versioning;
- события и сообщения;
- переходы состояния;
- побочные эффекты;
- порядок операций;
- idempotency;
- retries и cancellation.

Возможные классификации включают:

```text
DECLARATION_STALE
IMPLEMENTATION_DEFECT
CONSUMER_DEPENDS_ON_UNDECLARED_BEHAVIOR
TEST_ENCODES_STALE_CONTRACT
INTENTIONAL_COMPATIBILITY_BEHAVIOR
CONTRACT_UNRESOLVED
AUTHORITY_UNRESOLVED
```

Разрешение `CC-*` не переписывает Behavior Contract автоматически:

```text
CC resolved
    |
    v
BC impact analysis
    |
    +-- semantics unchanged -> BC remains valid
    |
    +-- semantic impact -> BC freshness = REVALIDATION_REQUIRED
```

Новую ревизию `BC-*` выпускает только Behavior Model.

---

## Contract drift и Test Gap

Расхождение между контрактами и отсутствие тестового доказательства — разные проблемы.

Например:

```text
Swagger не описывает 409
implementation возвращает 409
consumer обрабатывает 409
тесты полностью подтверждают поведение 409
```

В этом случае существует `CC-*`, но `GAP-*` не создаётся автоматически: контракт расходится, однако само поведение тестами доказано.

Если 409 ещё и не проверяется исполняемыми тестами, могут одновременно существовать две независимые проблемы:

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

## Граф зависимостей Test Engineering

Test Engineering не является обязательным линейным конвейером. Каждому запрошенному результату соответствует минимально необходимая цепочка зависимостей.

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

Если пользователь выбирает только `E2E Test Plan`, Skill может подключить Test Assurance, Behavior Model и применимый Contract Verification, но не обязан автоматически проектировать Service Simulator.

`EXTEND` переиспользует уже принятые и актуальные зависимости вместо полного повторного аудита.

`USE_EXISTING` разрешён только тогда, когда необходимая часть графа принята, актуальна и имеет достаточно разрешённый authority.

---

## Сохранение выбранных результатов

Выбор результатов Test Engineering сохраняется в состоянии capability и `working/INDEX.md`. Это необходимо, чтобы `RESUME`, `EXTEND`, `USE_EXISTING` и `REVALIDATE` могли восстановить именно тот набор работы, который был выбран пользователем.

Пример:

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

Эти поля независимы друг от друга. Skill не создаёт составные режимы вроде `REVIEW_PLUS_SIMULATOR_PLUS_E2E`.

---

## Точечная повторная проверка

`REVALIDATE` определяет затронутую область по смыслу изменений, а не просто по факту появления нового Git HEAD.

### Изменились только тесты

```text
tests changed
  -> TM revalidation
  -> MAT assurance may change
  -> GAP may close/open
```

Такое изменение обычно **не делает `BC-*` автоматически неактуальным**.

### Изменилась реализация или OpenAPI

```text
implementation or declared contract changed
  -> affected IMPLEMENTED / DECLARED views
  -> Contract Verification when relevant
  -> BC impact analysis
```

### Изменился только потребитель

```text
service unchanged
consumer changed
  -> CONSUMED view revalidation
  -> CC may change
  -> consumer-facing simulator scenarios may change
  -> affected E2E may require revalidation
```

Поэтому актуальность Test Engineering может зависеть от нескольких репозиториев, а не только от HEAD сервиса.

---

## Test Environment Design

Для каждой зависимости проверяемого сервиса выбирается отдельная стратегия:

```text
REAL_DISPOSABLE
SERVICE_EMULATOR
CONTROLLABLE_MOCK
IN_PROCESS_DOUBLE
TEMP_RESOURCE
NOT_REQUIRED
```

Основное правило:

> **Подменяйте внешнюю неопределённость, а не само проверяемое поведение.**

Если существенное поведение зависит от реальных транзакций, сроков истечения, порядка операций, ограничений базы данных или семантики хранения, нельзя автоматически заменять его удобным mock.

Например, PostgreSQL или Redis часто разумнее поднимать как временную реальную зависимость, а время или нестабильный внешний API — контролировать через соответствующий double или mock.

---

## Service Simulator Design

Skill различает две принципиально разные задачи:

```text
A) подмены зависимостей проверяемого сервиса
B) Service Simulator самого проверяемого сервиса для его потребителей
```

Это не один и тот же слой.

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

Интерфейс, которым пользуется реальный consumer, должен воспроизводить существенную часть реального протокола сервиса.

Тестовый интерфейс управления симулятором должен оставаться отдельным. Например:

```text
/__test/health
/__test/reset
/__test/scenario
/__test/state
/__test/seed
```

Service Simulator не генерируется слепо из Swagger:

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

`Service Simulator Implementation Plan` — отдельный явно выбранный результат. Он допустим только после принятого и актуального Service Simulator Spec.

Во время обычного review Skill проектирует симулятор, но не реализует его runtime автоматически.

---

## E2E Design

E2E нужен только там, где существенная гарантия действительно зависит от совместной работы нескольких реальных компонентов и не может быть доказана на меньшей границе с той же или большей надёжностью.

Каждый E2E-сценарий должен фиксировать:

- исходный `BC-*` и его ревизию;
- реальные участвующие компоненты;
- допустимые simulator/fake-компоненты;
- начальное состояние;
- стимул;
- существенные проверки результата;
- наблюдаемость ошибки;
- очистку и сброс состояния;
- пригодность для CI;
- стоимость выполнения, если она влияет на решение.

E2E не требует Service Simulator автоматически. Если тот же существенный контракт надёжнее и дешевле доказать интеграционным тестом на меньшей границе, предпочтение отдаётся меньшей границе.

---

## Артефакты Test Engineering

Совместимость Test Review сохраняется, а расширенная модель добавляет новые документы:

```text
test-review/
├── 00-test-assurance-summary.md
├── 01-test-assurance-map.md
├── 02-test-plan.md                              # необязательный, совместимость
├── 03-behavior-contract-model.md                # когда требуется расширенная модель
├── 04-contract-consistency-report.md            # необязательный пользовательский отчёт
├── 05-test-environment-design.md                 # необязательный
├── 06-service-simulator-spec.md                  # необязательный
├── 07-service-simulator-implementation-plan.md   # необязательный
├── 08-e2e-test-plan.md                           # необязательный
└── working/
    ├── INDEX.md
    ├── behavior-contracts.md                     # authoritative BC ledger
    ├── contract-verification.md                  # authoritative CC ledger
    ├── test-mappings.md
    ├── assurance-gaps.md
    └── ...
```

Нумерация файлов не задаёт порядок выполнения зависимостей.

`working/behavior-contracts.md` и `working/contract-verification.md` содержат авторитетное техническое состояние. `03-*` и `04-*` являются человекочитаемыми проекциями этого состояния, а не новым источником истины.

Отдельно различаются состояния:

```text
NOT_APPLICABLE
NOT_VERIFIED
VERIFIED_NO_MATERIAL_ISSUES
```

Например, отсутствие применимого declared contract означает `NOT_APPLICABLE`, а не `NOT_VERIFIED`.

---

## Общие принципы доказательности

**Сначала authority, потом verdict.** Если значимые источники противоречат друг другу и не определено, какой из них нормативный, результат остаётся unresolved.

**Ширина вывода не превышает ширину доказательств.** Узкая проверка даёт узкий вывод.

**Полнота требует явного ограниченного учёта.** Случайная выборка не является доказательством полноты.

**`RF-*`, `BC-*`, `MAT-*`, `TM-*`, `GAP-*` и `CC-*` не взаимозаменяемы.** У каждого идентификатора своя ответственность.

**Пользовательский документ не становится authority только потому, что он написан позже или выглядит аккуратнее.** Человекочитаемые документы выводятся из принятого технического состояния.

---

## Повторный запуск и актуальность

`REVALIDATE` по умолчанию проверяет только затронутую область:

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

`preserved` означает только то, что анализ влияния не обнаружил зависимости, требующей новой проверки. Это не новый `GREEN` и не повторное доказательство корректности.

Если изменение оказалось системным, Skill может вернуть `FULL_REAUDIT_RECOMMENDED`, но не превращает `REVALIDATE` в `NEW` без решения пользователя.

---

## PROJECTION_REPAIR

Этот режим предназначен только для исправления представления уже принятого результата:

- языка;
- структуры;
- Markdown;
- Mermaid;
- ссылок и cross-references;
- таблиц;
- навигации;
- терминологии;
- устаревшего пользовательского текста.

Он не может менять:

- семантику `BC-*`;
- классификацию `CC-*`;
- учёт `MAT-*`;
- verdict `TM-*`;
- существование `GAP-*`;
- смысловой приоритет `TASK-*`;
- принятые findings и severity;
- поведение сценариев Service Simulator;
- семантику E2E-топологии.

Если требуется техническое изменение, Skill должен вернуть `TECHNICAL_REVALIDATION_REQUIRED`.

---

## Project Profile и изменённое рабочее дерево

Project Profile — локальные метаданные для маршрутизации и оценки объёма проекта, а не архитектурное доказательство.

Профиль включает:

- количество существенных отслеживаемых Git файлов;
- строки и символы;
- распределение по языкам;
- отдельный учёт generated, vendor/dependency, build и binary material.

При изменённом рабочем дереве рекомендуемая воспроизводимая основа аудита — committed `HEAD`.

```text
1. Audit committed HEAD only — recommended
2. Include working-tree changes as EPHEMERAL snapshot
3. Stop
```

Если пользователь сознательно выбирает `EPHEMERAL`, Skill сохраняет детерминированный fingerprint рабочего дерева. Такой baseline нельзя представлять как обычную воспроизводимую Git-ревизию.

---

## Итоговый пакет аудита

По умолчанию результаты сохраняются в:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md                      # необязательный
├── 04-remediation-roadmap.md                      # необязательный
├── test-review/
│   ├── 00-test-assurance-summary.md
│   ├── 01-test-assurance-map.md
│   ├── 02-test-plan.md                            # необязательный
│   ├── 03-behavior-contract-model.md              # необязательный
│   ├── 04-contract-consistency-report.md          # необязательный
│   ├── 05-test-environment-design.md              # необязательный
│   ├── 06-service-simulator-spec.md                # необязательный
│   ├── 07-service-simulator-implementation-plan.md # необязательный
│   ├── 08-e2e-test-plan.md                         # необязательный
│   └── working/
│       └── ... capability authority/evidence
└── working/
    └── ... umbrella audit authority/evidence
```

Финальные документы предназначены для человека. Из них должно быть понятно: **что происходит → почему это важно → к чему приводит → что менять**.

Внутренние идентификаторы помогают трассировке, но не должны заменять нормальное техническое объяснение.

---

# Установка

## Codex, OpenCode и другие агенты с `~/.agents/skills`

Клонируйте репозиторий в каталог пользовательских Skills:

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новую сессию агента, чтобы он заново обнаружил Skill.

Обновление уже установленного Skill:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Проверить установленную ревизию:

```bash
cd ~/.agents/skills/architecture-code-review
git rev-parse HEAD
```

Если для воспроизводимости используется конкретный выпуск, можно перейти на соответствующий tag, если он существует:

```bash
git fetch --tags
git checkout <release-tag>
```

Вернуться на актуальный `main`:

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

Skill сам найдёт применимый предыдущий аудит, если он существует, и предложит подходящий Session Intent.

## Новый Architecture Review без Test Engineering

```text
Используй architecture-code-review.
Начни NEW аудит.
Architecture Review: STANDARD_FULL.
Результат: REVIEW_ONLY.
Test Engineering: OFF.
```

Для максимальной глубины:

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

## Полный набор Test Engineering

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

Skill должен сам подключить необходимые внутренние зависимости, но не должен включать необязательные пользовательские результаты без необходимости или явного выбора.

## Добавить Contract Consistency Report к принятому Test Assurance

```text
Используй architecture-code-review.
EXTEND существующий принятый пакет аудита.
Добавь Test Engineering output:
- Contract Consistency Report
Не переоткрывай несвязанные принятые этапы.
```

## Добавить Service Simulator Design

```text
Используй architecture-code-review.
EXTEND существующий принятый Test Assurance.
Добавь:
- Service Simulator Design
Переиспользуй принятые и актуальные Behavior Contracts и результаты Contract Verification.
Не перезапускай весь Architecture Review.
```

## Добавить E2E Test Plan без автоматического Service Simulator

```text
Используй architecture-code-review.
EXTEND существующий принятый пакет аудита.
Уже включено:
- Test Assurance
- Test Plan
Добавь:
- E2E Test Plan
Не включай Service Simulator Design автоматически, если выбранная топология его не требует.
```

При `EXTEND` уже выбранные результаты показываются отдельно и переиспользуются;
пользователь выбирает только доступные добавления. Если Test Engineering ещё
не был включён, показывается современный независимый список результатов с
обязательным `Test Assurance` при включении. `Service Simulator Design` может
добавиться автоматически только как явно объяснённая структурная зависимость
для `Service Simulator Implementation Plan`.

## Продолжить незавершённый аудит (`RESUME`)

```text
Используй architecture-code-review.
RESUME существующий незавершённый аудит.
Сначала проверь INDEX, authority bindings, baseline и сохранённый выбор Test Engineering outputs.
Продолжи с первого незавершённого валидного gate.
```

## Использовать уже принятый аудит (`USE_EXISTING`)

```text
Используй architecture-code-review.
USE_EXISTING для текущего принятого аудита.
Техническую работу заново не запускай.
Используй только принятую, актуальную и достаточно authority-resolved часть зависимостей.
```

## Проверить проект после изменений (`REVALIDATE`)

```text
Используй architecture-code-review.
REVALIDATE предыдущий принятый аудит относительно текущего HEAD.
Сначала выполни impact analysis.
Не инвалидируй все BC/TM/GAP/scenarios автоматически только из-за изменения HEAD.
```

## Исправить только финальные документы (`PROJECTION_REPAIR`)

```text
Используй architecture-code-review.
PROJECTION_REPAIR принятого пакета аудита.
Исправь только пользовательские Markdown/Mermaid/links/wording.
Если нужно изменить technical semantics, остановись с TECHNICAL_REVALIDATION_REQUIRED.
```

## Изменённое рабочее дерево

Проверить только воспроизводимую зафиксированную ревизию:

```text
Используй architecture-code-review.
Проверяй только committed HEAD.
Незакоммиченные изменения не включай в технические выводы.
```

Или сознательно включить текущие локальные изменения:

```text
Используй architecture-code-review.
Включи текущее рабочее дерево как EPHEMERAL snapshot.
Я понимаю, что это не обычный воспроизводимый commit baseline.
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
│   ├── pressure-scenario-88-new-test-engineering-selection.md
│   ├── pressure-scenario-89-extend-test-engineering-selection.md
│   └── test-engineering-capability-validation.md
└── docs/
    └── superpowers/
        ├── specs/
        └── plans/
```

`SKILL.md` остаётся компактным общим оркестратором.

Подробная семантика Test Engineering находится в `capabilities/test-review/references/test-engineering-contract.md`.

Правила запуска и выбора Session Intent находятся в `references/session-orchestration.md`.

Сохраняемое состояние capability и граф зависимостей описаны в `references/review-modes-and-orchestration.md`.

Правила актуальности и точечной повторной проверки находятся в `references/revalidation-and-freshness.md`.

---

# Проверка изменений Skill

Изменение Markdown-инструкций Skill считается изменением поведения, даже если технически production code не меняется.

Поэтому существенные изменения проходят последовательность:

```text
проектирование
  -> план реализации
  -> RED pressure contract
  -> реализация
  -> свежий независимый pressure run
  -> независимый review
  -> точечное исправление замечаний
  -> fresh re-review
  -> promotion readiness
  -> merge
```

Для Test Engineering в репозитории есть отдельные pressure scenarios:

```text
PS-81  границы BC относительно MAT/RF/GAP/TM
PS-82  authority контракта и запрет автоматического приоритета Swagger
PS-83  различие между contract drift и assurance gap
PS-84  минимально необходимая цепочка зависимостей
PS-85  точечная повторная проверка по влиянию изменений
PS-86  границы Service Simulator и E2E
PS-87  сохранение независимого выбора результатов
PS-88  независимый выбор Test Engineering при NEW
PS-89  выбор Test Engineering при EXTEND
```

Результат проверки всегда относится к конкретной ревизии и конкретному сценарию. Старый `GREEN` нельзя считать вечным доказательством для любого будущего `main`.

Статическая проверка текста контрактов и свежий независимый запуск агента — разные виды доказательств и должны фиксироваться отдельно.

У этого Markdown Skill может не существовать отдельного исполняемого application/coordinator runtime. В таком случае runtime-проверка имеет состояние `NOT_APPLICABLE`, но это не мешает выполнять реальные agent-level pressure scenarios.

---

# Язык итоговых документов

Пользовательский язык следует языку текущего запроса, если пользователь явно не выбрал другой.

Для русскоязычного пользователя финальные документы должны быть написаны связным русским техническим языком. Английские слова не следует использовать там, где есть естественный русский эквивалент.

При этом не переводятся:

- точные идентификаторы и status tokens;
- имена файлов и пути;
- названия API, IPC и протоколов;
- названия формальных режимов и сущностей, если они являются частью контракта;
- имена символов и объектов исходного кода.

Внутренние сокращения и записи ledger/handoff допустимы для трассировки, но не должны превращать финальный отчёт в черновик агента.

---

# Лицензия

См. `LICENSE`.
