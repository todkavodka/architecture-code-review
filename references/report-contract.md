# Контракт итоговых документов

Финальные документы пишутся на русском связном техническом языке и собираются **только из принятого авторитетного состояния**, а не напрямую из raw discovery notes.

Technical Documentation is a separate human-facing factual projection from
accepted, fresh Shared Technical Model authority. Its scope, non-authority,
source, and `PROJECTS_FROM` dependency rules are defined by
[`technical-documentation.md`](technical-documentation.md). It is not an
Architecture Review finding ledger or a developer how-to package.

## 1. Пакет

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md          # если заказано
├── 04-remediation-roadmap.md          # если заказано
└── working/
    ├── README.md
    ├── INDEX.md
    └── ... evidence/review artifacts ...
```

Если в репозитории уже есть established review directory, используй её, сохраняя внутренние роли файлов.

When composable capabilities are selected, keep their substantial detail in
capability-owned artifacts, registered in `working/INDEX.md`, for example:

```text
capabilities/test-review/01-test-assurance-map.md
capabilities/test-review/02-test-plan.md                 # optional
working/capabilities/test-review/...
```

The specialist artifact remains authoritative for its detailed evidence and
assurance map. The umbrella report may synthesize and link an adjudicated
cross-capability conclusion, but must not copy the complete specialist report.

For Test Engineering, preserve the compatible `00-test-assurance-summary.md`,
`01-test-assurance-map.md`, and optional `02-test-plan.md` projections. Extended
outputs are capability-owned projections `03` through `08`; authoritative
`BC-*`, `CC-*`, `TM-*`, and `GAP-*` ledgers remain under capability `working/`.
The numbered files do not become product-behavior authority merely because they
are generated later.

## 2. Authority map

- Технические факты во время исследования: accepted/fresh Shared Technical Model по `shared-technical-model.md` и required coverage acceptance по `technical-model-coverage.md`.
- Human-readable As-Built: substantial projection accepted/fresh STM плюс architecture-oriented synthesis; она не является competing factual authority.
- `01-architecture-review.md`: authoritative user-facing report; его factual As-Built chapter — производная STM projection, а architectural properties/findings — Architecture Review authority.
- `02-authoritative-findings-ledger.md`: единственный авторитетный источник final RF wording, evidence status, severity, projections, SER/open questions и supersessions.
- `03-target-architecture.md`: авторитетный источник target mechanisms/invariants/feasibility, когда endpoint это включает.
- `04-remediation-roadmap.md`: авторитетный источник implementation sequence/tasks/gates, когда endpoint это включает.

Если accepted STM revision, required factual coverage или projection selector меняется,
все зависимые As-Built/final sections считаются stale до повторной
synthesis/review. `PROJECTION_REPAIR` может исправлять presentation только по
неизменённой accepted authority; semantic drift маршрутизируется в technical
revalidation, а не скрывается prose repair.

## 3. `01-architecture-review.md`

Основной читаемый документ.

Рекомендуемая структура:

```markdown
# Архитектурное и кодовое ревью

## 1. Резюме
## 2. Объём, baseline и ограничения
## 3. Методика
## 4. Фактическая архитектура
### 4.1 Назначение и ключевые сценарии
### 4.2 Процессы и runtime-компоненты
### 4.3 Ответственность и владение
### 4.4 Основные data/control flows
### 4.5 IPC/API/native/process boundaries
### 4.6 Жизненный цикл
### 4.7 Конкурентность и фоновые операции
### 4.8 Хранение и конфигурация
### 4.9 Trust boundaries и security model
### 4.10 Platform-specific behavior
### 4.11 Положительные механизмы
## 5. Архитектурные свойства и ключевые выводы
## 6. Наиболее существенные подтверждённые замечания
## 7. Положительные механизмы, которые следует сохранить
## 8. Приоритеты и зависимости исправления
## 9. Выполненные проверки
## 10. Открытые вопросы и product-intent decisions
## 11. Ограничения исследования
## 12. Итоговый статус
```

Фактическая архитектура — substantial first-class chapter, traceable to
accepted/fresh STM facts and required coverage. Для medium project ориентир по
информационной плотности примерно соответствует 5–10 страницам, но gate —
semantic completeness, а не количество строк. Она сохраняет purpose/scenarios,
topology, ownership, boundaries, flows, lifecycle, concurrency, failure,
trust, configuration, persistence, observability и platform-specific material;
architecture properties and findings остаются отдельной Architecture authority.

Основной отчёт обычно раскрывает 10–20 наиболее важных RF в читаемом виде и ссылается на полный ledger вместо копирования всех деталей.

### 3.1 Human-readable synthesis contract

Финальный report объясняет архитектурные механизмы человеку, а не пересказывает внутренний ledger.

Для каждого material conclusion читатель должен без открытия working-файлов понять:

1. **Что происходит сейчас.** Как работает текущий mechanism/flow/ownership.
2. **Почему это происходит.** Какая граница, ответственность или lifecycle-модель создаёт поведение.
3. **К чему это приводит.** Конкретный runtime/security/reliability/testability effect.
4. **Что следует изменить.** Направление correction или target mechanism без преждевременного превращения вывода в кодовый patch.

Предпочтительный narrative pattern:

```text
current mechanism
→ code/evidence basis
→ practical consequence
→ architectural correction direction
```

`RF-*`, `SER-*`, `PC-*`, `OQ-*` и `TASK-*` являются навигацией и traceability. Они **не заменяют объяснение**.

Неприемлемая форма финальной прозы:

```text
error-boundary leaks credentials (RF-A/C);
test-app != prod-app -> risks untestable;
shutdown non-graceful;
cache-first pattern.
```

Такая запись допустима во внутренних registry/handoff, но пользовательский документ должен раскрыть причинно-следственную связь нормальными предложениями и абзацами.

### 3.2 Executive synthesis is not a ledger dump

Executive summary и раздел «ключевые выводы» не должны быть длинной нумерованной строкой из shorthand labels.

Сначала дай 3–7 связных абзацев, которые группируют проблемы по системным причинам: ownership/lifecycle, trust boundaries, data integrity, testability, coupling и т.п. После объяснения можно дать компактную таблицу или список RF-ссылок.

Читатель должен понять overall architectural health, системные причины и приоритеты даже если он не знает внутреннюю taxonomy Skill-а.

## 4. `02-authoritative-findings-ledger.md`

Для каждого root:

```text
stable RF ID
final title
severity
confidence
exploitability where applicable
root mechanism
reachable scenario
code evidence
projections
SER links
open/product-intent status
superseded candidate/wording references
links to main report
target link when applicable
roadmap task links when applicable
```

Отдельно сохраняй registries `SER-*`, `PC-*`, `OQ-*` и explicit supersessions.

Ledger может быть плотным и структурированным. Это не лицензия переносить его terse style в пользовательские narrative sections.

## 5. Cross-link contract

Используй относительные ссылки внутри audit package.

Навигационная цепочка:

```text
main report
→ authoritative RF
→ working evidence / verification
→ target mechanism
→ remediation task
```

Где полезно, добавляй обратные ссылки.

Stable headings начинай с ID:

```markdown
## RF-012 — ...
```

Не полагайся только на длинные translated headings как anchors.

Финальная проверка должна выявлять:

- orphan RF/SER/TASK;
- broken/missing relative links;
- target mechanism без motivating RF/SER/invariant;
- roadmap task без target/RF link;
- working claim, который superseded, но не ведёт к текущей authority.

## 6. Технический черновик vs финальная сборка

После authoritative findings ledger можно создать `MAIN REVIEW TECHNICAL DRAFT` для `01-architecture-review.md`.

Если endpoint включает target/roadmap, этот draft **не является финальным пакетом**.

`FINAL PACKAGE ASSEMBLY` выполняется после того, как все заказанные endpoint artifacts приняты:

```text
accepted audit
+ accepted target (если заказан)
+ accepted roadmap (если заказан)
→ inject final navigation/cross-links/status
→ editorial review
```

Для `REVIEW_ONLY` technical draft и final assembly могут естественно совпасть.

## 7. Chunked writing

Большой Markdown-документ не записывай одним giant write, если есть риск truncation/лимита.

Нормальный pattern:

```text
CREATE SKELETON
→ WRITE LOGICAL CHUNK A
→ VERIFY headings/content
→ WRITE CHUNK B
→ VERIFY previous content preserved
→ WRITE CHUNK C
→ VERIFY IDs/links
→ FINAL READ
```

Chunk определяется логическим разделом, не случайным количеством символов.

При write failure/truncation:

```text
inspect existing file
→ identify last complete logical boundary
→ resume from there
→ do not blindly overwrite whole large artifact
→ final read
```

Один final artifact имеет одного active writer за раз.

## 8. Writing style and terminology

Narrative — русский. На первом существенном употреблении допустимо `English term (русский аналог)`, дальше предпочитай русский термин, если точность не теряется.

Не переводи exact identifiers, class/function/type names, filenames, API/IPC/protocol names, runtime states, verdict/status tokens, commands/code.

Пиши абзацами `механизм → evidence → consequence → correction direction`. Таблицы и Mermaid дополняют анализ, а не заменяют его.

### 8.1 Working-artifact style must not leak into final prose

Working artifacts, candidate registries, HANDOFF SUMMARY и verification notes могут быть terse/machine-oriented. Пользовательские финальные документы — нет.

В final narrative избегай как основной формы:

- стрелочного shorthand `X -> Y -> broken`;
- длинных цепочек через `+`, `/`, `!=` и скобки;
- sentence fragments вместо предложений;
- English/Russian hybrids, когда есть естественная русская формулировка;
- перечней implementation identifiers до объяснения проблемы;
- RF/SER/TASK IDs как замены subject/predicate/consequence.

Например, вместо:

```text
test-app structurally != prod-app -> prod-risks untestable
```

нужно объяснить, что тестовое приложение собирается иначе, чем production-приложение, какие runtime paths из-за этого не воспроизводятся и почему зелёный test suite не доказывает отсутствие соответствующих регрессий.

### 8.2 Terminology quality

Предпочитай естественный русский технический язык, не буквальный перевод и не транслит.

Плохо:

```text
негрейсфул shutdown
credential-ами
prod-risks
designated owner отсутствует
runtime-drift
```

Лучше:

```text
некорректное/неполное завершение работы
учётные данные
риски production-конфигурации
явный владелец ресурса
расхождение поведения между версиями во время выполнения
```

Если английский термин является точным именем концепта, API или established term и русский аналог ухудшает точность, оставь его и при первом употреблении кратко поясни.

Избегай необъяснённых labels вроде `god object`, `spaghetti`, `bad practice`, а также риторических усилителей, не подтверждённых severity.

## 9. Diagram contract

Диаграмма нужна не ради квоты, а когда без неё хуже понимаются topology, ordering, lifecycle, ownership, trust boundaries, state transitions или Before/After architecture.

Для substantial `STANDARD_FULL`/`FORENSIC` final package ожидается полезное визуальное покрытие, если соответствующие механизмы существуют в системе:

- **As-Built:** минимум одна component/boundary diagram, когда система имеет несколько существенных runtime-компонентов/процессов/внешних зависимостей;
- **Runtime/lifecycle:** sequence/state/flow diagram для хотя бы одного material flow или lifecycle-механизма, если ordering/ownership влияет на correctness;
- **Target Architecture:** обязательная target component/boundary diagram, если endpoint включает target и target существенно меняет ownership/boundaries/flows;
- **Before → After:** для material architectural change, которое трудно понять только текстом;
- **Roadmap dependencies:** dependency diagram, когда порядок задач имеет нетривиальные prerequisites или safe-activation boundary.

Если substantial report не содержит useful diagrams, final writer/reviewer должен явно объяснить, почему визуализация не добавила бы архитектурной информации. Это исключение должно быть evidence-based, а не результатом того, что диаграммы просто забыли.

Для syntax/evidence rules следуй `lifecycle-and-mermaid.md`.

## 10. Executive summary

В начале за 1–2 страницы должно быть понятно:

- overall architectural health;
- top 3–7 risks;
- security/data-integrity blockers;
- lifecycle/resource ownership quality;
- incremental remediation viability;
- есть ли причины блокировать feature development;
- какой endpoint выполнен и какие документы являются authority.

Executive summary сначала объясняет системную картину человеческим языком; таблицы/ID идут после narrative synthesis.

## 11. Verification table

```markdown
| Команда/проверка | Результат | Ограничение/комментарий |
|---|---|---|
```

Не скрывай недоступные проверки.

## 12. Final status

`REVIEW_COMPLETE` допускается только после completion gates `SKILL.md`, включая independent verification/adjudication, cross-link check и editorial correction/re-review.

Иначе `REVIEW_PARTIALLY_COMPLETE` с точным перечислением missing evidence/gates.
