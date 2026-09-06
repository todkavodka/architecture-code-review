# Architecture Code Review

`architecture-code-review` — evidence-first Skill для глубокого анализа существующих программных систем.

Он объединяет три независимые capability:

- **Architecture Review** — как система действительно устроена, кто чем владеет, где находятся архитектурные риски и корневые проблемы;
- **Test Engineering** — какие существенные поведения действительно доказаны тестами, где есть пробелы и какие тестовые артефакты нужны;
- **Code Quality Review** — какие реализационные механизмы создают существенные последствия для сопровождаемости, надёжности, тестируемости, жизненного цикла, ресурсов, конкурентности, зависимостей и локализации.

Capability можно выбирать независимо в рамках одного Review Suite. Результаты опираются на общий evidence layer и Shared Technical Model, но **не смешивают semantic authority** разных областей.

Главный принцип Skill:

> **Ширина утверждения не должна превышать ширину доказательств.**

Если проверен один обработчик, это не доказывает корректность всей модели авторизации.  
Если обычный сценарий работает, это ещё не подтверждает корректность retries, recovery, concurrency или shutdown.  
Если доказательств недостаточно, Skill обязан оставить результат ограниченным, частичным или unresolved, а не превращать предположение в факт.

---

## Что умеет Skill

### Architecture Review

Architecture Review восстанавливает фактическую архитектуру системы и проверяет:

- компоненты и процессы;
- владение состоянием и ресурсами;
- жизненный цикл;
- конкурентное выполнение;
- retries, cancellation и recovery;
- доверительные и security-границы;
- контракты между компонентами;
- надёжность и отказоустойчивость;
- сопровождаемость;
- тестируемость;
- архитектурные root causes.

При необходимости Architecture Review может дополнительно сформировать:

- **Target Architecture**;
- **Remediation Roadmap**.

Архитектурные findings имеют собственную authority (`RF-*`) и не являются взаимозаменяемыми с Test Engineering или Code Quality findings.

---

### Test Engineering

Test Engineering отвечает не на вопрос «тесты зелёные или нет», а на более строгий:

> **Какие существенные поведения системы действительно подтверждены исполняемыми тестами, какие подтверждены частично, какие не доказаны и где тесты могут создавать ложное чувство уверенности?**

Пользователь может выбирать результаты независимо:

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

`Test Assurance` — базовое ядро Test Engineering.

Внутренние зависимости подключаются только когда они действительно нужны. Например:

- `Behavior Model` не является пользовательским переключателем;
- применимый `Contract Verification` выполняется автоматически, если существует существенный формализованный контракт;
- `Service Simulator Design` не включается автоматически только потому, что выбран E2E;
- необязательные пользовательские документы не создаются без необходимости или явного выбора.

Entrypoint:

[`capabilities/test-review/SKILL.md`](capabilities/test-review/SKILL.md)

---

### Code Quality Review

Code Quality Review — отдельная capability, а не подраздел Architecture Review.

Она ищет не «плохой стиль вообще», а **реализационные механизмы с доказуемым существенным последствием**.

Типичные области:

- дублирование и чрезмерная сложность;
- неправильные lifecycle/resource patterns;
- concurrency hazards;
- fragile error handling;
- плохие dependency boundaries;
- локализация и hardcoded user-facing values;
- framework-specific anti-patterns;
- testability problems;
- maintainability hotspots;
- реализационные дефекты, которые ещё не являются архитектурным root cause.

Code Quality Review владеет:

- `CQ-*` — принятыми Code Quality findings;
- `CQRA-*` — Code Quality remediation actions;
- ограниченным состоянием coverage/freshness самой capability.

При этом:

```text
tool warning != CQ finding
metric != CQ finding
smell != CQ finding
candidate != semantic authority
CQRA COMPLETED != CQ RESOLVED
```

Принятый `CQ-*` требует evidence-backed интерпретации и material consequence.

Code Quality Review использует language-neutral core. Языковые и framework-specific addenda могут уточнять анализ, но не становятся отдельной semantic authority.

Entrypoint:

[`capabilities/code-quality-review/SKILL.md`](capabilities/code-quality-review/SKILL.md)

---

## Review Suite

Architecture Review, Test Engineering и Code Quality Review могут использоваться:

- отдельно;
- вместе в одном запуске;
- добавляться позже через `EXTEND`;
- продолжаться через `RESUME`;
- точечно перепроверяться через `REVALIDATE`.

Capability selection и output selection — разные вещи.

Например:

```text
Architecture Review: ON
Test Engineering: ON
Code Quality Review: ON
```

не означает, что Skill автоматически создаст все возможные документы каждой capability.

Выбираются только необходимые пользовательские outputs, а внутренние зависимости подключаются минимально необходимым slice.

---

## Как начинается работа

Skill не должен автоматически запускать новый полный аудит.

Сначала определяется:

```text
repository
+ revision
+ working-tree state
        |
        v
existing audit discovery
        |
        v
authority / lineage / freshness
        |
        v
Project Profile
        |
        v
Session Intent
        |
        v
capability + output selection
        |
        v
minimum necessary work
```

### Session Intent

Поддерживаются:

| Intent | Когда используется |
|---|---|
| `USE_EXISTING` | использовать уже принятый и актуальный результат |
| `NEW` | начать новый аудит в заданных границах |
| `RESUME` | продолжить незавершённый workflow |
| `REVALIDATE` | перепроверить затронутую изменениями semantic slice |
| `EXTEND` | добавить новую capability или output без полного повторного аудита |
| `PROJECTION_REPAIR` | исправить только представление уже принятой семантики |

Типичная маршрутизация:

```text
предыдущего аудита нет               -> NEW
IN_PROGRESS                           -> RESUME
COMPLETE + тот же baseline            -> USE_EXISTING
COMPLETE + изменившийся baseline      -> REVALIDATE
нужна новая capability/output         -> EXTEND
сломаны только Markdown/links/wording -> PROJECTION_REPAIR
```

`PROJECTION_REPAIR` не заменяет `REVALIDATE`.

Если для исправления пользовательского документа приходится менять semantic authority, evidence, severity, ownership или accepted technical meaning, Skill должен перейти обратно в технический workflow.

---

## Shared Evidence и Shared Technical Model

Capability не должны независимо реконструировать одну и ту же систему каждая «для себя».

Общий factual substrate разделён на:

```text
WS-*   bounded investigation/workset
EV-*   addressable observation inside a workset
STM    accepted factual Shared Technical Model
```

Над этим слоем работают capability-specific interpretations:

```text
Shared Evidence / STM
        |
        +--> Architecture Review   -> RF-*
        |
        +--> Test Engineering      -> BC-* / CC-* / MAT-* / TM-* / GAP-* / TASK-*
        |
        +--> Code Quality Review   -> CQ-* / CQRA-*
```

Один и тот же факт может участвовать в нескольких интерпретациях, но ownership semantic records не переносится между capability.

### Ключевые границы authority

| Объект | Владелец |
|---|---|
| `WS-*`, `EV-*` | shared evidence layer |
| STM facts | Shared Technical Model |
| `RF-*` | Architecture Review |
| `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` | Test Engineering |
| `CQ-*`, `CQRA-*` | Code Quality Review |
| `working/INDEX.md` | workflow/coordinator state |
| пользовательские Markdown reports | projection, не semantic authority |

`working/INDEX.md` нужен для `RESUME`, но он не становится владельцем findings, contracts или factual model.

---

## Architecture Review: базовый flow

Упрощённо полный Architecture Review выглядит так:

```text
baseline
  -> Shared Evidence
  -> Shared Technical Model
  -> Technical Model Coverage Review
  -> Architecture thematic discovery
  -> Discovery Coverage Matrix
  -> Independent Coverage Review
  -> candidate verification
  -> root-boundary adjudication
  -> severity
  -> Authoritative Findings Ledger
  -> optional Target Architecture
  -> optional Remediation Roadmap
  -> projections / final package
  -> independent editorial verification
```

### Почему сначала As-Built / STM

Skill не должен искать проблемы только по названиям файлов, grep-совпадениям или общему впечатлению.

Сначала нужно понять:

- какие реальные компоненты существуют;
- какие процессы исполняются;
- кто владеет состоянием;
- где проходят boundary;
- какие существуют lifecycle transitions;
- какие execution paths существенны.

Только после этого можно надёжно формулировать findings.

---

## Test Engineering: Behavior Contract Model

Расширенный Test Engineering использует единую модель поведения, чтобы Test Plan, Contract Verification, Simulator и E2E не придумывали продуктовую семантику независимо.

```text
architecture / implementation / contracts / consumers
                        |
                        v
                 Behavior Model
                      BC-*
                        |
        +---------------+---------------+
        |               |               |
        v               v               v
 Contract Verification Test Design  Scenario Design
      CC-*                             /       \
                                  Simulator    E2E
```

Основные сущности:

```text
RF-*    Architecture/root finding
BC-*    Behavior Contract
CC-*    Contract Consistency Record
MAT-*   Material Assurance Target
TM-*    Test Mapping
GAP-*   Assurance Gap
TASK-*  Test Engineering remediation task
CQ-*    Code Quality finding
CQRA-*  Code Quality remediation action
```

Критические границы:

```text
BC != MAT
BC != RF
BC != GAP
CC != GAP
CQ != RF
CQ != GAP
CQRA != TASK
```

---

## Contract Verification

Если система публикует формализованный контракт, Skill сравнивает несколько представлений:

```text
DECLARED      OpenAPI / protobuf / AsyncAPI / docs
IMPLEMENTED   routes / handlers / DTO / auth / errors
CONSUMED      frontend / SDK / CLI / other services
TESTED        executable tests
```

Ни одно представление не получает автоматический приоритет только потому, что оно «официальное» или исполняемое.

При конфликте создаётся отдельное `CC-*`, после чего authority разрешается явно.

Contract drift и отсутствие тестового доказательства — разные проблемы: наличие `CC-*` не означает автоматическое создание `GAP-*`.

---

## Targeted `REVALIDATE`

Изменение Git HEAD само по себе не означает полный повтор аудита.

Базовый принцип:

```text
accepted baseline A
  -> current baseline B
  -> changed inputs
  -> impact analysis
  -> minimum affected semantic slice
  -> fresh evidence
  -> revalidation
  -> preserve unaffected accepted state
```

Это относится и к Code Quality:

```text
changed source/config/dependency/addendum/EV/STM
        |
        v
dependency impact
        |
        v
affected CQ records
        |
        v
targeted REVALIDATE
```

`REVALIDATE` не равен `RESUME` и не равен projection regeneration.

---

## Projections и пользовательские документы

Semantic authority и человекочитаемый документ — разные вещи.

Stage B использует стабильные `PRJ-*` projection identities, dependency tracking, freshness, validation и regeneration.

Основные правила:

```text
semantic authority != projection

semantic REVALIDATE != projection regeneration

PROJECTION_REPAIR != semantic remediation
```

Projection может быть `STALE`, пока semantic authority остаётся принятой.

И наоборот, `CURRENT` projection может честно отображать `PARTIAL` coverage — это не противоречие.

### Code Quality projections

Поддерживаются:

- **Code Quality Findings View**;
- **Code Quality Summary**;
- **Maintainability Hotspots**;
- **Code Quality Roadmap Contribution**.

Поддерживаемый output не означает автоматически выбранный output.

Package строится из:

```text
explicit selected outputs
+
dependency closure
```

и использует общие Stage B policies:

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

---

## Stack addenda

Для некоторых технологий существуют дополнительные проверки, например:

- Ansible;
- Django;
- Electron;
- FastAPI;
- Litestar;
- React;
- Tauri.

Они дополняют общий анализ, но не становятся отдельными верхнеуровневыми capability.

Наличие framework/tool signal не создаёт finding автоматически.

---

# Установка

## Codex, OpenCode и другие агенты с `~/.agents/skills`

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новую сессию агента, чтобы Skill был обнаружен заново.

### Обновление

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Проверить установленную ревизию:

```bash
git rev-parse HEAD
```

---

# Использование

Самый простой запрос:

```text
Используй architecture-code-review для этого проекта.
```

Skill должен сначала показать подходящий Session Intent и доступные capability/output choices, а не молча запускать максимальный аудит.

---

## Только Architecture Review

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review:
- depth: STANDARD_FULL
- result: REVIEW_ONLY

Test Engineering: OFF
Code Quality Review: OFF
```

Для более глубокого расследования:

```text
Architecture Review:
- depth: FORENSIC
- result: REVIEW_ONLY
```

---

## Architecture + Target Architecture + Roadmap

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review:
- depth: STANDARD_FULL
- result: REVIEW_PLUS_TARGET_AND_ROADMAP

Test Engineering: OFF
Code Quality Review: OFF
```

---

## Architecture + Test Engineering

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review:
- depth: STANDARD_FULL
- result: REVIEW_ONLY

Test Engineering:
- Test Assurance
- Test Plan
- Contract Consistency Report

Code Quality Review: OFF
```

---

## Только Code Quality Review

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review: OFF
Test Engineering: OFF

Code Quality Review:
- Findings View
- Summary
```

Например, такой запуск подходит для отдельного review реализации после большой переработки кода, когда архитектурная модель уже известна и задача состоит именно в качестве реализации.

---

## Architecture + Test Engineering + Code Quality

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review:
- depth: STANDARD_FULL
- result: REVIEW_ONLY

Test Engineering:
- Test Assurance
- Test Plan

Code Quality Review:
- Findings View
- Summary
- Maintainability Hotspots
```

---

## Добавить capability позже (`EXTEND`)

```text
Используй architecture-code-review.

EXTEND существующий принятый audit package.

Добавь Code Quality Review:
- Findings View
- Summary

Не перезапускай несвязанные принятые этапы.
```

Аналогично можно добавить Test Engineering outputs к уже принятому Architecture Review.

---

## Продолжить незавершённый аудит (`RESUME`)

```text
Используй architecture-code-review.

RESUME существующий незавершённый аудит.

Восстанови состояние из working/INDEX.md и owning artifacts.
Не используй chat history как semantic authority.
Продолжи с первого незавершённого валидного gate.
```

---

## Проверить изменения (`REVALIDATE`)

```text
Используй architecture-code-review.

REVALIDATE принятый audit package относительно текущего baseline.

Сначала выполни impact analysis.
Перепроверь только затронутую semantic slice.
Не запускай весь аудит заново без evidence необходимости.
```

---

## Исправить только документы (`PROJECTION_REPAIR`)

```text
Используй architecture-code-review.

PROJECTION_REPAIR принятого audit package.

Исправь только Markdown, Mermaid, ссылки, навигацию и wording.
Если требуется изменить technical semantics — остановись и запроси REVALIDATE.
```

---

## Изменённое рабочее дерево

Для воспроизводимого аудита предпочтителен committed `HEAD`:

```text
Используй architecture-code-review.
Проверяй committed HEAD.
Незакоммиченные изменения не включай в технические выводы.
```

Если необходимо сознательно анализировать локальные изменения:

```text
Используй architecture-code-review.
Включи рабочее дерево как EPHEMERAL snapshot.
```

Такой baseline должен быть явно помечен как невоспроизводимый обычным Git commit.

---

# Итоговые артефакты

По умолчанию audit package хранится под:

```text
docs/reviews/architecture-review/
```

Конкретный набор файлов зависит от выбранных capability и outputs.

Пользовательские документы должны отвечать на четыре вопроса:

> **Что происходит → почему это важно → к чему приводит → что менять**

Внутренние IDs нужны для provenance и трассировки, но не должны заменять нормальное техническое объяснение.

---

# Структура репозитория

Упрощённо:

```text
.
├── README.md
├── LICENSE
├── SKILL.md
│
├── capabilities/
│   ├── test-review/
│   │   ├── SKILL.md
│   │   └── references/
│   │
│   └── code-quality-review/
│       ├── SKILL.md
│       └── references/
│           ├── code-quality-contract.md
│           ├── code-quality-lifecycle.md
│           └── code-quality-projection.md
│
├── references/
│   ├── session-orchestration.md
│   ├── review-modes-and-orchestration.md
│   ├── shared-evidence-model.md
│   ├── shared-technical-model.md
│   ├── technical-model-coverage.md
│   ├── revalidation-and-freshness.md
│   ├── projection-lifecycle.md
│   ├── projection-gates-and-packages.md
│   ├── review-method.md
│   ├── discovery-coverage.md
│   ├── independent-verification.md
│   └── stacks/
│
├── tests/
│   └── pressure-scenario-*.md
│
└── docs/
    ├── roadmap.md
    └── superpowers/
        ├── specs/
        ├── plans/
        └── reviews/
```

`SKILL.md` — umbrella orchestrator.

Capability-specific semantics находятся в собственных `capabilities/*` entrypoints и references.

Shared evidence, orchestration, freshness и projection lifecycle находятся в общих `references/`.

---

# Проверка изменений Skill

Изменение Markdown-инструкций Skill может менять фактическое поведение агента так же сильно, как изменение production code.

Поэтому существенные изменения проходят evidence-driven цикл:

```text
design / contract
  -> implementation plan
  -> fail-first pressure evidence
  -> implementation
  -> deterministic checks
  -> independent review
  -> targeted remediation
  -> targeted re-review
  -> promotion readiness
  -> published-ref verification
  -> merge
  -> post-promotion verification
```

Pressure scenario относится к конкретной ревизии и конкретному контракту. Старый `GREEN` не является вечным доказательством корректности будущего `main`.

Validation должна оставаться пропорциональной риску: сначала targeted evidence, а отдельный harness создаётся только когда его долгосрочная ценность оправдывает стоимость поддержки.

---

# Язык итоговых документов

Язык пользовательских документов следует языку текущего запроса, если пользователь явно не выбрал другой.

Для русскоязычного пользователя итоговые документы должны быть написаны нормальным связным русским техническим языком.

Не переводятся без необходимости:

- точные идентификаторы и status tokens;
- имена файлов и пути;
- API, IPC и protocol names;
- формальные mode/entity names;
- символы и объекты исходного кода.

Внутренние ledger/handoff записи могут быть компактными, но финальный документ не должен выглядеть как черновик агента.

---

# Roadmap

Текущие направления развития:

[`docs/roadmap.md`](docs/roadmap.md)

---

# Лицензия

См. [`LICENSE`](LICENSE).
