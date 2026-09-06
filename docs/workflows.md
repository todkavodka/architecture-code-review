# Architecture Code Review — workflows

Этот документ объясняет, **как Skill ведёт review во времени**: как начинается новый audit, как продолжается незавершённый, как проверяются изменения и как добавляются новые outputs без полного повторного анализа.

## 1. Общий startup flow

Перед substantive review Skill сначала определяет контекст:

```text
repository identity
    -> previous audit discovery
    -> lineage / usability check
    -> baseline + dirty state
    -> Project Profile
    -> Session Intent
    -> Review Suite configuration
    -> minimum required work
```

Session Intent не является режимом глубины Architecture Review. Это решение о том, **что делать с уже существующим состоянием review**.

Поддерживаются:

```text
USE_EXISTING
NEW
RESUME
REVALIDATE
EXTEND
PROJECTION_REPAIR
```

## 2. Как выбирается Session Intent

Типичная recommendation matrix:

| Состояние | Рекомендуемый intent |
|---|---|
| предыдущего audit нет | `NEW` |
| audit `IN_PROGRESS`, тот же baseline | `RESUME` |
| audit `IN_PROGRESS`, baseline изменился | `RESUME` с reconciliation |
| audit `COMPLETE`, baseline тот же, нужно использовать результат | `USE_EXISTING` |
| audit `COMPLETE`, baseline изменился | `REVALIDATE` |
| нужен новый capability/output/endpoint | `EXTEND` |
| нужно исправить только presentation | `PROJECTION_REPAIR` |

Рекомендация не должна скрывать альтернативы, если пользователь явно хочет другой путь.

## 3. `NEW`

`NEW` создаёт новый review package и новый persisted workflow state.

Сначала показывается Review Suite:

```text
NEW
└── Review Suite
    ├── [ ] Architecture Review
    ├── [ ] Test Engineering
    └── [ ] Code Quality Review
```

Действует:

```text
AT_LEAST_ONE_TOP_LEVEL_CAPABILITY_SELECTED
```

### Architecture Review

Если выбрана Architecture capability:

```text
Depth:
  STANDARD_FULL
  FORENSIC

Result:
  REVIEW_ONLY
  REVIEW_PLUS_TARGET_ARCHITECTURE
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

Если Architecture не выбрана, её depth/endpoint отсутствуют по contract.

### Test Engineering

Если выбрана Test Engineering capability:

```text
Test Assurance                    required
Test Plan                         optional
Contract Consistency Report       optional
Test Environment Design           optional
Service Simulator Design          optional
Service Simulator Implementation Plan optional
E2E Test Plan                     optional
```

Behavior Model и applicable Contract Verification подключаются внутренне.

### Code Quality Review

Если выбрана Code Quality capability, пользователь выбирает нужные projections:

```text
Findings View/Report
Code Quality Summary
Maintainability Hotspots
Roadmap Contribution
```

Эти outputs user-selectable, хотя сами документы являются derived projections.

## 4. Что создаёт `NEW` до анализа

`NEW` не обязан сразу строить полный factual model.

Он должен создать persistent STM baseline/manifest и coordinator state:

```text
always create model baseline
!=
always fully populate model
```

Нужная глубина фактической модели определяется выбранным downstream work.

Например:

- полный Architecture Review потребует full STM coverage;
- узкий Code Quality Review может потребовать только relevant STM slice;
- Test Engineering может добавить factual slice, нужный конкретным contracts.

## 5. `RESUME`

`RESUME` используется для незавершённого persisted workflow.

```text
RESUME
├── read working/INDEX.md
├── validate refs/revisions/freshness
├── restore Review Suite [READ-ONLY]
├── reconcile owning artifacts
└── continue first non-accepted durable boundary
```

Главный принцип:

> `RESUME` продолжает существующую работу, а не заново конфигурирует audit.

Поэтому уже выбранные capability/output показываются как restored context, а не как новый checkbox menu.

Если пользователь хочет добавить новый output во время resume, это новый scope и должен быть маршрутизирован в `EXTEND`.

### Почему одного `INDEX.md` недостаточно

`INDEX.md` — coordinator authority, но substantive semantics принадлежат owning artifacts.

При resume:

```text
INDEX
  -> owning artifact
  -> revision/freshness check
  -> continue
```

Если compact state противоречит owning artifact, требуется reconciliation.

## 6. `REVALIDATE`

`REVALIDATE` используется, когда accepted baseline изменился и нужно определить, что действительно стало stale.

```text
accepted baseline A
       |
       v
current baseline B
       |
       v
change inventory
       |
       v
impact analysis
       |
       v
minimum affected dependency slice
       |
       v
fresh evidence
       |
       v
revalidation / adjudication
```

### Review Suite в REVALIDATE

Предыдущая конфигурация восстанавливается **read-only**:

```text
REVALIDATE
├── Previous Review Suite [READ-ONLY]
├── previous/current baseline
├── impact analysis
└── affected slice
```

REVALIDATE не показывает NEW-style capability menu.

```text
REVALIDATE_DOES_NOT_BECOME_NEW
```

### Что выбирает пользователь

Пользователь может подтвердить baseline/change context или принять решение при действительно systemic impact.

Но affected capability/finding slice определяется impact analysis, а не ручным повторным выбором outputs.

### Примеры

Только тесты изменились:

```text
tests changed
  -> TM revalidation
  -> MAT assurance may change
  -> GAP may open/close
```

Это не делает автоматически stale все `BC-*`.

Изменился API implementation:

```text
implementation changed
  -> relevant STM / IMPLEMENTED view
  -> Contract Verification when applicable
  -> BC/CQ/Architecture impact where dependencies exist
```

## 7. Projection Impact Analysis после semantic work

После `NEW`, `EXTEND` или `REVALIDATE`, когда semantic state стабилизирована, выполняется Projection Impact Analysis.

```text
semantic delta accepted
    -> Projection Impact Analysis
    -> PROJECTION_IMPACT_ACCOUNTED
    -> affected PRJ freshness updated
```

Это accounting step.

Он **не запускает regeneration автоматически**.

```text
impact accounting != regeneration
```

Если нужен fresh output, запускается отдельный `RG-*` workflow.

## 8. `EXTEND`

`EXTEND` добавляет новый scope к accepted package.

Базовое presentation:

```text
EXTEND
├── Existing / preserved [READ-ONLY]
└── Available additions [USER_SELECTABLE]
```

Результат:

```text
previous accepted selection
UNION
explicit additions
UNION
structurally required dependencies
```

### Добавление новой capability

Если capability отсутствовала, она может быть добавлена как новая.

Например:

```text
Existing:
  Test Engineering

Available:
  Architecture Review
  Code Quality Review
```

При добавлении Architecture только тогда спрашиваются depth/result.

### Architecture endpoint extension

Для уже принятой Architecture действует monotonic flow:

```text
REVIEW_ONLY
  -> REVIEW_PLUS_TARGET_ARCHITECTURE
  -> REVIEW_PLUS_TARGET_AND_ROADMAP
```

Допустимо также из `REVIEW_ONLY` сразу запросить Target + Roadmap.

Но ordinary EXTEND не должен менять существующий depth:

```text
STANDARD_FULL -> FORENSIC   not an ordinary additive output change
FORENSIC -> STANDARD_FULL   not an ordinary additive output change
```

### Test Engineering extension

Уже выбранные outputs сохраняются, показываются только доступные additions.

Если пользователь выбирает Simulator Implementation Plan, требуемый accepted/fresh Simulator Design входит как structural prerequisite.

E2E не включает Simulator автоматически, если topology этого не требует.

### Code Quality extension

То же правило:

```text
existing CQ outputs [read-only]
+
new selected projections
```

## 9. `USE_EXISTING`

`USE_EXISTING` нужен, когда accepted result подходит без новой технической работы.

```text
USE_EXISTING
├── validate accepted package
├── validate required projections/refs
├── choose deliverable if needed
└── consume result
```

Нельзя использовать его для добавления нового capability/output.

Новый scope -> `EXTEND`.

Changed project -> обычно `REVALIDATE`.

## 10. `PROJECTION_REPAIR`

`PROJECTION_REPAIR` чинит presentation уже принятого смысла.

```text
PROJECTION_REPAIR
├── accepted revision-bound package
├── eligible registered PRJ-* projections
├── select document / section / issue
├── presentation-only repair
└── PROJECTION_REVALIDATION
```

Target list строится из реально зарегистрированных projections package, а не из hardcoded списка capability outputs.

Пользователь может чинить:

- язык;
- wording;
- Markdown;
- Mermaid;
- таблицы;
- ссылки;
- navigation;
- cross-references;
- representation уже принятого meaning.

Но не может через PROJECTION_REPAIR менять:

- evidence;
- STM facts;
- RF/CQ/BC semantics;
- severity;
- ownership;
- target mechanism;
- remediation dependencies.

Если edit требует semantic change:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

## 11. Regeneration `RG-*`

Regeneration — отдельный operational workflow.

Пример:

```text
PRJ-01 STALE
PRJ-02 CURRENT
PRJ-03 STALE

requested fresh output: PRJ-03
        |
        v
TARGETED RG-* plan
        |
        +--> required stale prerequisites
        +--> requested projection
```

Downstream stale outputs не добавляются молча в targeted execution.

## 12. Package closeout

После semantic completion и impact accounting применяется package policy.

```text
semantic gates accepted
  -> PROJECTION_IMPACT_ACCOUNTED
  -> package membership resolved
  -> required projections current according to policy
  -> closeout
```

Policies:

```text
PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

Это позволяет, например, завершить узкий Code Quality update, даже если несвязанный старый Architecture projection остаётся stale, если policy это допускает.

## 13. Dirty working tree

Для воспроизводимости default baseline — committed HEAD.

Обычно доступны варианты:

```text
1. committed HEAD only
2. EPHEMERAL working-tree snapshot
3. stop
```

EPHEMERAL baseline должен быть явно fingerprinted и не представляться как обычный Git commit.

## 14. Legacy packages

Старые packages не считаются автоматически broken.

Compatibility обрабатывается консервативно.

Например legacy Test Review:

```text
REVIEW_ONLY
  -> Test Assurance = true
  -> optional outputs = false

REVIEW_PLUS_TEST_PLAN
  -> Test Assurance = true
  -> Test Plan = true
  -> other optional outputs = false
```

Эти values — compatibility input, не современное user menu.

Legacy projection без `PRJ-*` lifecycle metadata не становится `CURRENT` только потому, что файл существует. Его нужно зарегистрировать и связать с current authority.

## 15. Какой intent выбрать — короткая шпаргалка

```text
Начинаю новый audit
  -> NEW

Вернулся к незавершённому audit
  -> RESUME

Код изменился после accepted review
  -> REVALIDATE

Нужно добавить E2E / CQ / Target Architecture
  -> EXTEND

Нужен уже готовый accepted report
  -> USE_EXISTING

Сломаны только Markdown/Mermaid/links
  -> PROJECTION_REPAIR
```

## 16. Что читать дальше

- [Architecture](architecture.md) — conceptual model и authority boundaries;
- [Artifacts and State](artifacts-and-state.md) — persisted files, IDs и registries;
- [Output Guide](output-guide.md) — какой user-facing output выбирать;
- `references/session-orchestration.md` — normative startup contract;
- `references/revalidation-and-freshness.md` — normative impact/revalidation rules.