# Architecture Code Review — артефакты, состояние и индексы

Этот документ объясняет **что именно создаёт Skill на диске**, какие сущности считаются authority, какие являются evidence или projections, как они связаны и для чего потом используются.

Если нужна концептуальная модель Review Suite, сначала прочитайте [Architecture](architecture.md).

## 1. Типичный audit package

Рекомендуемый корень:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md              # optional
├── 04-remediation-roadmap.md              # optional
├── test-review/                            # when Test Engineering selected
│   └── ...
└── working/
    ├── INDEX.md
    ├── README.md
    ├── evidence/
    ├── technical-model/
    ├── projections/
    └── capability-specific working files
```

Локальная convention проекта имеет приоритет над этим расположением. Важны не имена директорий сами по себе, а ownership, stable identity, baseline/revision binding и provenance.

## 2. `working/INDEX.md`

`working/INDEX.md` — компактный coordinator state, который делает review возобновляемым.

Он хранит routing/process state, например:

```text
repository identity
current baseline
working-tree state
Session Intent
Review Suite selection
current phase
execution plan
artifact registry
capability registry
coverage/gate summaries
handoffs
blockers
projection/package routing
```

Пример capability registry:

```yaml
capabilities:
  - id: architecture-review
    selected: true
    status: IN_PROGRESS
    mode: STANDARD_FULL
    endpoint: REVIEW_ONLY
    owning_artifact: working/...

  - id: test-review
    selected: true
    status: COMPLETE
    outputs:
      test_assurance: true
      test_plan: true
      contract_consistency_report: false

  - id: code-quality-review
    selected: false
    status: NOT_APPLICABLE
```

Для Architecture поля `mode` и `endpoint` присутствуют только когда capability выбрана.

```text
architecture selected
  -> mode REQUIRED
  -> endpoint REQUIRED

architecture not selected
  -> mode ABSENT_BY_CONTRACT
  -> endpoint ABSENT_BY_CONTRACT
```

`INDEX.md` не является semantic authority для findings, STM facts или contracts. Он указывает, **где находится authority**, но не заменяет её.

## 3. Shared Evidence

Рекомендуемый layout:

```text
working/evidence/
├── INDEX.md
├── WS-001-*.md
├── WS-002-*.md
└── ...
```

### `WS-*`

`WS-*` — bounded investigation/workset.

Он фиксирует:

- scope;
- baseline;
- investigated sources;
- limitations;
- набор `EV-*` observations;
- handoff summary.

Пример:

```text
WS-018-worker-shutdown
scope: shutdown / cancellation / publication
baseline: 1a2b3c
status: COMPLETE

EV-001 ...
EV-002 ...
```

### `EV-*`

`EV-*` — адресуемое observation внутри workset.

Обычно содержит:

```text
id
source_type
repository path / external locator
symbol / range
baseline binding
observed fact or behavior
optional short excerpt
```

Evidence отвечает на вопрос:

> Что конкретно показал источник на выбранном baseline?

Evidence не назначает severity, не создаёт finding и не определяет remediation.

## 4. Shared Technical Model

Рекомендуемый layout:

```text
working/technical-model/
├── INDEX.md
├── coverage.md
├── components/
│   └── COMP-*.md
├── interfaces/
│   └── IF-*.md
├── interactions/
│   └── INT-*.md
├── data-stores/
│   └── DS-*.md
├── events/
│   └── EVENT-*.md
├── flows/
│   └── FLOW-*.md
├── auth/
│   └── AUTH-*.md
├── errors/
│   └── ERR-*.md
└── configuration/
    └── CFG-*.md
```

Основные families:

| ID | Значение |
|---|---|
| `COMP-*` | component / runtime unit |
| `IF-*` | interface |
| `INT-*` | interaction |
| `DS-*` | data store |
| `EVENT-*` | event/message |
| `FLOW-*` | material flow |
| `AUTH-*` | auth/trust boundary |
| `CFG-*` | configuration fact |
| `ERR-*` | error/failure contract |

Каждый accepted fact имеет stable identity, revision, baseline binding и provenance к `WS-*` / `EV-*`.

Пример:

```text
IF-021@rev3
status: ACCEPTED
freshness: VALID
baseline: abc123

PROVIDES: COMP-API
PROTECTED_BY: AUTH-004
DEPENDS_ON: CFG-012

provenance:
  WS-004-api#EV-017
  WS-009-auth#EV-006
```

## 5. Technical Model indexes

Generated indexes помогают не читать весь STM для каждой задачи.

Их роль:

```text
routing / lookup / dependency traversal
```

а не:

```text
new semantic authority
```

Упрощённый reading path:

```text
working/INDEX.md
    -> owning semantic artifact
    -> WS#EV
    -> raw source
```

Если compact/index state stale или конфликтует с owning artifact, приоритет у owning authority и требуется reconciliation.

## 6. Architecture Review artifacts

Человекочитаемые документы обычно включают:

```text
01-architecture-review.md
02-authoritative-findings-ledger.md
03-target-architecture.md          # optional
04-remediation-roadmap.md          # optional
```

### `RF-*`

`RF-*` — Architecture/root finding.

Authoritative ledger хранит подтверждённые findings, а не просто candidate list.

У finding обычно есть:

```text
identity
scope
root boundary
supporting evidence / STM refs
material consequence
severity
relationships / supersession when applicable
```

As-Built portion final report — projection фактической модели, а `RF-*` ledger — Architecture authority.

## 7. Test Engineering artifacts

Typical package:

```text
test-review/
├── 00-test-assurance-summary.md
├── 01-test-assurance-map.md
├── 02-test-plan.md                              # optional
├── 03-behavior-contract-model.md                # when needed
├── 04-contract-consistency-report.md            # optional user output
├── 05-test-environment-design.md                # optional
├── 06-service-simulator-spec.md                 # optional
├── 07-service-simulator-implementation-plan.md  # optional
├── 08-e2e-test-plan.md                          # optional
└── working/
    ├── behavior-contracts.md
    ├── contract-verification.md
    ├── test-mappings.md
    ├── assurance-gaps.md
    └── ...
```

Основные semantic IDs:

| ID | Что хранит |
|---|---|
| `BC-*` | одно независимо проверяемое существенное поведение |
| `CC-*` | расхождение между contract representations |
| `MAT-*` | material assurance target |
| `TM-*` | executable test evidence mapping |
| `GAP-*` | отсутствующее/частичное/недостаточное доказательство |
| `TASK-*` | Test Engineering remediation work |

### Пример цепочки

```text
BC-044
  -> MAT-031
      -> TM-019
      -> GAP-012
```

Это не четыре названия одной проблемы. Каждая запись отвечает на свой вопрос.

## 8. Code Quality artifacts

Code Quality semantic authority:

```text
CQ-*    accepted Code Quality finding
CQRA-*  Code Quality remediation action
```

Пример:

```text
CQ-014
mechanism: duplicated locale fallback logic
material consequence: divergent user-facing behavior across entrypoints
severity: MEDIUM
freshness: CURRENT
```

Связанный remediation action:

```text
CQRA-006
for: CQ-014
state: COMPLETED
```

Но:

```text
CQRA COMPLETED != CQ RESOLVED
```

Для `CQ RESOLVED` нужна отдельная revalidation evidence.

## 9. Projections: `PRJ-*`

Human-readable output — derived projection, если он зарегистрирован в Stage B projection lifecycle.

Projection record хранит:

- stable `PRJ-*` identity;
- owning capability;
- artifact path;
- semantic dependencies;
- projection dependencies;
- contract revision;
- verified revision;
- fingerprint;
- freshness.

Пример:

```text
PRJ-CQ-01-SUMMARY
path: working/projections/code-quality/summary.md
owner: code-quality-review
freshness: CURRENT
```

Code Quality имеет, например:

```text
PRJ-CQ-00-FINDINGS-VIEW
PRJ-CQ-01-SUMMARY
PRJ-CQ-02-HOTSPOTS
PRJ-CQ-03-ROADMAP-CONTRIBUTION
```

### Почему нужен `PRJ-*`

Без identity система не может надёжно понять:

- какой документ устарел;
- от каких facts/findings он зависит;
- нужно ли его регенерировать;
- является ли новый Markdown тем же output или другим документом.

## 10. Projection freshness

Для projections используются состояния:

```text
CURRENT
STALE
BLOCKED
```

`STALE` не означает, что underlying semantic authority неверна. Это значит, что отображающий её документ больше не подтверждён как актуальное представление.

## 11. Regeneration: `RG-*`

Projection regeneration выполняется отдельной session:

```text
RG-*
```

Operational views обычно располагаются под:

```text
working/projections/
├── registry.md
├── impact.md
└── sessions/
    └── RG-*.md
```

`RG-*` — execution record, а не новый Session Intent и не semantic authority.

Основной принцип:

```text
semantic change
  -> Projection Impact Analysis
  -> mark affected projections
  -> explicit regeneration if required
```

Impact analysis сама не переписывает output files.

## 12. Package membership

Пользователь выбирает outputs, но final package учитывает dependency closure.

```text
explicit selected outputs
        +
required projection dependencies
        =
resolved package membership
```

Поддерживаются policies:

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

Их смысл:

- `PERMISSIVE` — semantic closeout возможен при видимых stale projections;
- `REQUIRED_SCOPE_CURRENT` — используемый output и обязательные prerequisites должны быть current;
- `ALL_SCOPED_CURRENT` — весь resolved package scope должен быть current.

## 13. Как использовать audit package позже

### Быстро понять состояние

Начните с:

```text
working/INDEX.md
```

Он покажет baseline, selected suite, phase и refs.

### Проверить конкретный вывод

Перейдите из `INDEX.md` к owning semantic artifact, затем при необходимости — к `WS#EV` и source.

### Продолжить незавершённую работу

Используйте `RESUME`. Skill восстановит workflow state из persisted artifacts, а не из памяти чата.

### Проверить новую версию проекта

Используйте `REVALIDATE`. Старые facts/findings не удаляются автоматически: сначала определяется affected slice.

### Добавить новый документ или capability

Используйте `EXTEND`. Existing accepted state сохраняется, добавляется только новый scope и необходимые dependencies.

### Исправить Markdown без технического re-audit

Используйте `PROJECTION_REPAIR`, если semantics не меняются.

## 14. Authority map

Короткая шпаргалка:

| Объект | Роль | Authority? |
|---|---|---|
| `working/INDEX.md` | coordinator workflow state | да, только для routing/process |
| `WS-*`, `EV-*` | evidence | observation authority, не conclusions |
| STM `COMP/IF/...` | shared technical facts | да |
| `RF-*` | Architecture finding | да |
| `BC/CC/MAT/TM/GAP/TASK` | Test Engineering semantics | да |
| `CQ/CQRA` | Code Quality semantics | да |
| `PRJ-*` Markdown | derived presentation | нет, projection |
| `RG-*` | regeneration execution state | operational, не semantic |

## 15. Что читать дальше

- [Architecture](architecture.md) — почему слои разделены именно так;
- [Workflows](workflows.md) — как меняется и переиспользуется состояние;
- [Output Guide](output-guide.md) — какие документы выбирать пользователю;
- `references/` — normative contracts для агента.