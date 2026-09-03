# Orchestrator v0.3 — Session, Revalidation и Project Profile

Дата: 2026-09-03

Статус: DESIGN APPROVED IN CHAT, RECORDED FOR REVIEW

Базовая ветка: `main`

Базовый commit: `6076074ba3783f1ad1584d095b711c78c3957b25`

## 1. Цель

Orchestrator v0.3 меняет верхний слой запуска `architecture-code-review` так, чтобы повторный запуск Skill не означал автоматический повтор полного аудита.

Основная цель — сохранить evidence-first correctness и при этом радикально снизить стоимость повторных запусков на изменившемся проекте. Повторный запуск должен сначала определить, что именно изменилось относительно уже принятого аудита, затем загрузить только минимальный свежий authoritative evidence, необходимый для проверки затронутых областей.

Вторичная цель — сделать выбор дополнительных review capabilities, прежде всего Test Review, явной частью orchestration UX, а не скрытым следствием формулировки пользовательского prompt.

Третья цель — добавить дешёвый `Project Profile`: статистику файлов, строк, символов и языков проекта, которая собирается локально, хранится как versioned metadata и может backfill-иться в старые audit package без повторного technical review.

## 2. Не-цели

В v0.3 не создаётся dynamic plugin framework, generic capability resolver или отдельный runtime service.

Не меняется evidence-first методология Architecture Review, Discovery Coverage, independent candidate verification, root-boundary adjudication, severity adjudication, Target Architecture или Roadmap review.

Не вводится правило, по которому количество файлов или строк является доказательством архитектурной materiality.

Не допускается автоматическое превращение targeted revalidation в новый полный аудит.

Не переписывается root `SKILL.md` в монолит. Он остаётся тонким orchestrator entrypoint.

## 3. Архитектурный подход

Выбран подход с отдельным Session Orchestration layer.

Новый авторитетный reference contract:

`references/session-orchestration.md`

Он владеет:

- startup/session gate;
- обнаружением предыдущих audit package;
- repository identity и lineage selection;
- session intent;
- repeated-run UX;
- Review Suite Configuration startup behavior;
- Project Profile lifecycle;
- dirty-working-tree baseline choice;
- правилами metadata backfill/migration.

`references/review-modes-and-orchestration.md` продолжает владеть:

- review depth;
- architecture endpoint;
- workflow state;
- artifact package;
- `working/INDEX.md`;
- capability registry;
- persisted handoff;
- visible plan projection;
- execution/resume mechanics после выбора session intent.

`references/revalidation-and-freshness.md` продолжает владеть freshness/revision-binding semantics и расширяется точным контрактом project-change revalidation.

Root `SKILL.md` только направляет запуск через Session Orchestration и затем в существующий review workflow.

## 4. Основные инварианты

### 4.1 Повторный запуск не равен повторному аудиту

Если существует пригодный предыдущий audit package, Skill сначала определяет его отношение к текущему repository state.

Полный новый аудит не является default для изменившегося проекта.

### 4.2 Claim scope не может превышать fresh evidence scope

Targeted revalidation экономит контекст, но не ослабляет evidence discipline.

Routing context может решить, куда смотреть. Он не является substantive proof, если решение требует owning code/configuration или принятого owning artifact.

### 4.3 Revalidation не может молча стать full audit

Если targeted scope оказывается недостаточным, используется явное scope expansion с сохранённой причиной.

Если изменения системные, orchestrator возвращает `FULL_REAUDIT_RECOMMENDED`. Только пользователь решает начать полный аудит.

### 4.4 Accepted evidence сохраняется, а не переутверждается без проверки

Если change-impact analysis не обнаружил зависимости между изменениями и ранее принятой областью, эта область может сохранить previous accepted evidence.

Это не новое доказательство и не должно формулироваться как «повторно проверено».

### 4.5 Metadata evolution не инвалидирует technical authority

Обновление версии orchestrator или schema Project Profile может дополнять routing/metadata state старого аудита без открытия уже принятых technical gates.

### 4.6 `INDEX.md` остаётся compact workflow state, а не substantive authority

Новые session/profile/revalidation поля в `INDEX.md` являются persisted state/projection. Они не заменяют owning artifacts и не обходят freshness/revision binding.

## 5. Startup pipeline

До substantive investigation orchestrator выполняет дешёвый startup pipeline:

```text
START
  ↓
Repository Identity
  ↓
Previous Audit Discovery
  ↓
Audit Package Usability / Lineage Check
  ↓
Git Baseline + Dirty State
  ↓
Project Profile reuse / refresh / backfill
  ↓
Session Intent
  ↓
Review Suite Configuration
  ↓
Persist INDEX / reconcile existing INDEX
  ↓
Substantive Review
```

Startup reconnaissance не должен blanket-read repository contents. Его задача — выбрать правильный workflow и подготовить routing metadata.

## 6. Repository identity и предыдущие аудиты

Presence старого `INDEX.md` само по себе не означает, что `RESUME` безопасен.

До использования previous audit orchestrator проверяет минимум:

- repository identity соответствует текущему проекту;
- referenced baseline известен;
- `INDEX.md` читаем;
- referenced owning artifacts существуют либо их отсутствие явно объяснимо;
- revision/status bindings достаточно coherent для выбранного действия;
- audit status и lineage не противоречат друг другу.

Если обнаружен audit package, но безопасное использование установить нельзя, orchestrator не должен молча resume/revalidate его.

Используется явный state наподобие:

`PREVIOUS_AUDIT_RECONCILIATION_REQUIRED`

### 6.1 Несколько audit package

При нескольких пакетах нельзя выбирать только по timestamp.

Selection учитывает:

- repository identity;
- audit authority status;
- baseline ancestry/lineage;
- пригодность для `RESUME`, `REVALIDATE` или `USE_EXISTING`.

Типичный случай:

```text
Audit A
  status: COMPLETE
  baseline: abc123
  suitable_for: REVALIDATE

Audit B
  status: IN_PROGRESS
  baseline: def000
  suitable_for: RESUME
```

Если выбор неоднозначен, пользователь видит оба варианта. Orchestrator не должен молча предпочитать более новый файл.

## 7. Session Intent

Вводится верхнеуровневый persisted intent:

```text
USE_EXISTING
NEW
RESUME
REVALIDATE
EXTEND
```

### 7.1 `USE_EXISTING`

Используется для `COMPLETE` audit, когда текущий committed baseline совпадает с audited baseline и нет причины открывать technical gates.

Technical work: none.

Разрешены metadata refresh/backfill/migration и просмотр существующих результатов.

### 7.2 `NEW`

Создаёт новый full bounded audit на выбранном baseline и проходит полный Review Suite Configuration.

`NEW` всегда доступен как явный выбор пользователя, но не является default повторного запуска.

### 7.3 `RESUME`

Продолжает существующий `IN_PROGRESS` audit.

По умолчанию не спрашивает заново depth/endpoints/capabilities. Конфигурация восстанавливается из persisted state после freshness/reconciliation.

Если repository state изменился после начала audit, используется resume with change reconciliation до продолжения зависимых gates.

### 7.4 `REVALIDATE`

Используется для `COMPLETE` audit, когда repository baseline изменился.

Default behavior — change-impact analysis и targeted fresh revalidation, а не полный rerun.

### 7.5 `EXTEND`

Используется, когда system может не измениться, но assurance scope расширяется.

Примеры:

- добавить Test Review к уже завершённому Architecture Review;
- добавить Target Architecture;
- добавить Roadmap;
- позже добавить новую capability.

`EXTEND` загружает только минимальный accepted dependency slice для нового endpoint/capability и не перезапускает unrelated accepted work.

## 8. Default recommendation matrix

```text
No previous audit
  → NEW

IN_PROGRESS + same baseline
  → RESUME recommended

IN_PROGRESS + repository changed
  → RESUME_WITH_RECONCILIATION recommended

COMPLETE + HEAD == audited baseline
  → USE_EXISTING recommended

COMPLETE + HEAD != audited baseline
  → REVALIDATE recommended

User wants additional capability/endpoint
  → EXTEND
```

Пользователь всегда может явно выбрать `NEW`, если хочет полный новый аудит.

## 9. Review Suite Configuration

Session Intent выбирается до Review Suite Configuration.

### 9.1 `NEW`

Показывается явная конфигурация:

```text
Architecture Review
  depth:
    STANDARD_FULL
    FORENSIC

  endpoint:
    REVIEW_ONLY
    REVIEW_PLUS_TARGET_ARCHITECTURE
    REVIEW_PLUS_TARGET_AND_ROADMAP

Capabilities
  Test Review:
    OFF
    REVIEW_ONLY
    REVIEW_PLUS_TEST_PLAN

Stack Addenda
  auto-detected
  confirmed before substantive use
```

Test Review должен быть видимым пунктом меню всегда. Lightweight reconnaissance может рекомендовать его при substantial test surface, но не включает capability без выбора пользователя.

Stack addenda не являются capabilities. Они остаются lenses для соответствующего technology stack.

### 9.2 `RESUME`

Existing Review Suite Configuration загружается из accepted/reconciled persisted state.

Полное меню не показывается заново по умолчанию.

Добавление нового endpoint/capability должно быть явным изменением assurance scope и семантически соответствует `EXTEND`.

### 9.3 `REVALIDATE`

Предыдущая suite-конфигурация предлагается как default.

Пользователь может изменить capabilities/endpoints, но это не даёт права повторно запускать unaffected Architecture Review. Добавленная assurance scope обрабатывается как extension поверх revalidation.

### 9.4 `EXTEND`

Показываются только доступные additions, а не первоначальная конфигурация целиком.

## 10. Project-change Revalidation

`REVALIDATE` использует отдельную state machine:

```text
BASELINE_BINDING
  ↓
CHANGE_INVENTORY
  ↓
IMPACT_ANALYSIS
  ↓
IMPACT_CLASSIFICATION
  ↓
MINIMUM_DEPENDENCY_SLICE
  ↓
TARGETED_FRESH_EVIDENCE
  ↓
REVALIDATION / ADJUDICATION
  ↓
DELTA_RECONCILIATION
```

### 10.1 Change inventory

Change inventory определяет фактический диапазон изменений между previous accepted baseline и current selected baseline.

Он может использовать Git diff, changed paths, structural information и existing evidence pointers как routing context.

Сам diff не доказывает корректность изменённого механизма.

### 10.2 Impact classification

Используются orchestration-классы:

`LOCAL`

Изменение локально и не демонстрирует изменение material boundary/contract/ownership semantics.

`BOUNDARY`

Изменение затрагивает material API, trust/auth boundary, persistence contract, ownership, lifecycle, concurrency, IPC, external integration или другую принятую архитектурную границу.

`SYSTEMIC`

Изменения затрагивают несколько фундаментальных границ или делают previous architecture model недостаточно надёжной основой для targeted revalidation.

Эти labels не являются finding severity.

### 10.3 Affected-set construction

Impact analysis строит минимум:

- affected architecture domains;
- affected accepted findings;
- affected candidate/evidence bindings;
- affected capabilities;
- affected dependent artifacts;
- preserved accepted domains.

Если возможно, старые findings/artifacts должны иметь dependency/evidence pointers, позволяющие определить dependency hit без blanket reread.

### 10.4 Minimal dependency slice

Fresh context включает только material dependencies, необходимые для текущего решения.

Unrelated accepted artifacts исключены по умолчанию.

Если во время targeted pass обнаружена material dependency вне текущего scope:

```text
CONTEXT_EXPANSION_REQUIRED
```

Должны быть сохранены:

- exact correctness trigger;
- requested expansion;
- evidence pointer/path;
- affected decision/domain.

После этого scope расширяется только на необходимый dependency slice.

### 10.5 Systemic escalation

`SYSTEMIC` не запускает полный аудит автоматически.

Orchestrator возвращает:

```text
FULL_REAUDIT_RECOMMENDED
```

с причиной и кратким описанием того, почему previous accepted model больше нельзя безопасно использовать как основу targeted revalidation.

Пользователь выбирает, продолжать ли полный новый аудит.

## 11. Revalidation output

Основной результат повторной проверки — delta-oriented artifact/report, а не автоматическое переписывание всего previous final report.

Минимальная семантика:

```text
source audit revision
previous baseline
current baseline
change range
impact classification
changes investigated
context expansions
previous accepted evidence preserved
findings revalidated
findings resolved
findings still valid
findings changed
new findings
capability impacts
unresolved items
```

При необходимости authoritative audit получает новую revision или связанный revalidation overlay. Implementation plan должен выбрать конкретное файловое представление, не меняя эту семантику.

## 12. Preserved evidence semantics

`preserved` означает:

> change-impact analysis не обнаружил зависимости, требующей повторной проверки этой ранее принятой области.

`preserved` не означает:

- область заново прочитана;
- поведение заново доказано;
- свежий runtime test выполнен;
- новый independent review прошёл.

Если связь с changed area неизвестна или dependency graph/evidence pointers недостаточны, область нельзя объявлять preserved только ради экономии context. Требуется targeted investigation или scope expansion.

## 13. Project Profile

Project Profile — локально вычисляемая routing/estimation metadata projection.

Он не требует передачи полного содержимого файлов LLM и не должен сам по себе расходовать существенный model context.

### 13.1 Primary statistics

Primary profile считает substantive tracked project material:

```text
files
lines
characters
languages:
  per language:
    files
    lines
    characters
```

### 13.2 Excluded statistics

Отдельно учитываются минимум:

- generated files;
- vendored/dependency files;
- build artifacts;
- binaries.

Они не должны загрязнять primary totals.

Правила классификации должны быть детерминированными и проверяемыми. Implementation plan должен определить минимальный практичный collector и fallback semantics для неизвестных расширений/языков.

### 13.3 Versioning

Project Profile хранит минимум:

```text
schema_version
collector_version
collected_for_revision
collected_at
baseline_type
substantive totals
language breakdown
excluded breakdown
```

### 13.4 Lifecycle

```text
MISSING
  → COLLECTED

OUTDATED
  → REFRESHED

OLD_SCHEMA
  → MIGRATED | BACKFILLED

CURRENT
  → REUSED
```

### 13.5 Historical backfill

Если старый audit создан до появления Project Profile, v0.3 может вычислить profile для его historical commit, если этот commit доступен.

Это `METADATA_BACKFILL`, а не technical revalidation.

Если historical commit недоступен:

```text
HISTORICAL_PROFILE_UNAVAILABLE
```

Current profile всё равно может быть собран. Старый technical audit от отсутствия historical profile не становится invalid.

### 13.6 Project Profile Delta

При `REVALIDATE`, если доступны оба profile:

```text
previous profile
  +
current profile
  ↓
Project Profile Delta
```

Delta может показывать:

- files added/removed/net;
- lines delta;
- characters delta;
- language footprint delta.

Эта информация помогает routing и estimation, но не определяет architecture materiality.

## 14. Orchestrator/schema upgrades

Upgrade orchestrator может enrich/migrate routing metadata без повторного technical review.

Пример:

```text
Existing audit:
  orchestrator_version: 0.2
  status: COMPLETE
  baseline: abc123

Current orchestrator:
  version: 0.3

Project Profile:
  MISSING

HEAD:
  abc123
```

Result:

```text
session_intent: USE_EXISTING
technical_review: NONE
metadata_action: METADATA_BACKFILL
audit_status: COMPLETE
```

Future Profile schema additions должны использовать тот же принцип, если новая metadata не изменяет substantive technical authority.

## 15. Dirty working tree

Audit baseline по умолчанию привязывается к точному Git commit.

Если working tree dirty, пользователь получает явный выбор:

```text
1. Audit committed HEAD only — recommended
2. Include working-tree changes as EPHEMERAL snapshot
3. Stop
```

### 15.1 Committed HEAD only

Uncommitted changes не включаются в evidence baseline. Artifact должен явно записывать dirty-state, чтобы не создавалось впечатление, что локальные изменения были проверены.

### 15.2 Ephemeral snapshot

Если пользователь выбирает включение working tree:

```text
git_revision: <commit>
working_tree_snapshot: <deterministic fingerprint>
baseline_type: EPHEMERAL
```

Такой baseline нельзя представлять как обычный reproducible commit baseline.

Если snapshot material больше недоступен, будущий resume/revalidation обязан это учитывать и не делать вид, что исходное состояние полностью восстанавливаемо.

## 16. `INDEX.md` additions

`INDEX.md` должен получить compact session state без превращения в technical report.

Conceptual fields:

```text
orchestrator_version
session_intent
repository_identity

source_audit
source_audit_revision

previous_baseline
current_baseline
baseline_type
working_tree_snapshot

review_suite
capabilities
stack_addenda

project_profile:
  schema_version
  collector_version
  collected_for_revision
  status
  artifact_or_projection_ref

revalidation:
  change_range
  impact_status
  impact_classification
  affected_domains
  affected_findings
  affected_capabilities
  preserved_domains
  context_expansions
```

Exact Markdown/YAML-like formatting определяется implementation plan. Semantic fields выше являются design requirement.

Любая compact projection, которая используется downstream как shortcut, остаётся под существующим revision/status freshness contract.

## 17. Capability integration

Existing capability registry остаётся owner capability state.

Test Review становится first visible capability в Start Gate, но не становится core-required.

Он может быть:

- selected at `NEW` startup;
- recommended после lightweight reconnaissance;
- preserved/revalidated как часть existing suite;
- attached later через `EXTEND`.

Late attachment следует уже принятому принципу:

```text
resume/reconcile INDEX
→ verify baseline/freshness
→ register capability
→ determine minimal accepted dependency slice
→ execute capability-owned pass
→ review/adjudicate capability output
→ reconcile shared findings/corrections
→ targeted revalidation only where dependencies require it
```

Future capabilities должны использовать тот же orchestration pattern без необходимости вводить generic plugin runtime в v0.3.

## 18. Error and safety behavior

### 18.1 Unsafe resume

Если previous audit найден, но identity/bindings невозможно надёжно reconciliate:

`PREVIOUS_AUDIT_RECONCILIATION_REQUIRED`

До устранения неоднозначности нельзя downstream-use stale compact state.

### 18.2 Unknown impact

Если change impact нельзя ограничить имеющимся routing information, orchestrator расширяет только необходимое исследование и фиксирует причину. Он не маркирует области preserved по умолчанию.

### 18.3 Missing historical commit

Historical Project Profile становится unavailable; technical audit не invalidated автоматически.

### 18.4 Stale capability dependency

Capability не может использовать stale/disputed dependency как accepted input. Применяется existing freshness contract.

### 18.5 User refuses full reaudit

Если `FULL_REAUDIT_RECOMMENDED`, а пользователь не разрешает full audit, revalidation заканчивается честным ограниченным статусом с перечислением unresolved/systemic scope. Нельзя project результат как полностью revalidated audit.

## 19. Context-cost discipline

Orchestrator v0.3 должен иметь явную behavioral цель: small repository change не должен приводить к blanket repository reread.

Практические правила:

- startup использует metadata/routing context;
- diff используется для routing, не как complete evidence;
- accepted unaffected artifacts не preload-ятся;
- fresh reads выполняются по affected dependency slice;
- expansion требует correctness trigger;
- full reaudit требует user decision;
- Project Profile считается локально и не требует LLM анализа каждого файла.

Не вводится жёсткий универсальный token/file budget, который мог бы ухудшить correctness. Вместо этого проверяется bounded expansion behavior.

## 20. Validation strategy

Implementation должен быть защищён pressure scenarios, проверяющими прежде всего orchestration behavior и context economy.

Минимальный набор сценариев:

1. `COMPLETE + same HEAD` → `USE_EXISTING`; substantive repository reread не выполняется.
2. v0.2 `COMPLETE + same HEAD + no Project Profile` → metadata backfill без открытия technical gates.
3. `COMPLETE + small local diff` → `REVALIDATE`, bounded affected slice, без full audit.
4. Boundary-changing diff → affected boundary/dependencies revalidated, unrelated accepted domains preserved.
5. Material omitted dependency обнаружена mid-pass → `CONTEXT_EXPANSION_REQUIRED` с точной причиной.
6. Systemic architectural change → `FULL_REAUDIT_RECOMMENDED`, но full audit не стартует без user decision.
7. `EXTEND` с Test Review → Architecture Review не rerun; загружается minimal accepted dependency slice.
8. Multiple previous audits → lineage/status selection, без timestamp-only auto-choice.
9. `IN_PROGRESS + changed HEAD` → resume reconciliation до downstream continuation.
10. Dirty tree → committed-HEAD default и explicit EPHEMERAL option.
11. Historical baseline unavailable → current Project Profile usable, historical delta unavailable, accepted audit не invalidated только по этой причине.
12. Preserved-domain wording не утверждает fresh verification, если fresh evidence не читался.

Regression validation также должна подтвердить, что existing authority/freshness/capability contracts не ослаблены.

## 21. Planned file-level integration

Design ожидает минимум следующие изменения при реализации:

Create:

- `references/session-orchestration.md`

Modify:

- `SKILL.md` — thin entry routing через Session Orchestration;
- `references/review-modes-and-orchestration.md` — integration points, INDEX/session state и capability UX alignment;
- `references/revalidation-and-freshness.md` — project-change targeted revalidation semantics;
- `README.md` — пользовательское описание repeated-run behavior, Test Review menu и Project Profile;
- pressure scenario / validation documents — сценарии v0.3.

Project Profile не получает отдельный reference file в v0.3, если implementation planning не обнаружит реальную необходимость вынести существенно большой самостоятельный contract. YAGNI default — держать profile contract внутри `session-orchestration.md`.

## 22. Compatibility

Existing complete audit packages должны оставаться usable.

Migration должна быть additive там, где это возможно:

- отсутствие новых INDEX fields означает legacy state, а не автоматически corrupt state;
- legacy audit может получить metadata backfill;
- existing capability registry semantics сохраняются;
- existing accepted artifact revisions не меняются только из-за v0.3;
- existing revalidation/freshness invariants остаются сильнее compact projections.

## 23. Success criteria

Orchestrator v0.3 считается архитектурно успешным, если одновременно выполняется следующее:

- пользователь явно видит, что Skill умеет `USE_EXISTING`, `RESUME`, `REVALIDATE`, `EXTEND` и `NEW`;
- повторный запуск на changed project по умолчанию рекомендует targeted `REVALIDATE`;
- full rerun не происходит без доказанной системной причины и user decision;
- Test Review доступен через явную Review Suite Configuration;
- Project Profile показывает substantive files/lines/characters/languages и отдельные excluded categories;
- Project Profile можно backfill/migrate независимо от technical audit;
- repeated revalidation использует minimal fresh authoritative evidence и записывает scope expansion;
- multiple prior audits и dirty working tree обрабатываются без скрытого выбора baseline;
- existing evidence-first, independent verification, severity и authority contracts не ослаблены;
- pressure validation показывает, что small changes не вызывают blanket reread accepted repository state.

## 24. Design decisions summary

Приняты следующие решения:

- отдельный Session Orchestration contract вместо раздувания root `SKILL.md`;
- никаких dynamic plugin mechanics в v0.3;
- first-class session intents: `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`;
- `COMPLETE + same HEAD` → reuse, а не rerun;
- `COMPLETE + changed HEAD` → targeted revalidation by default;
- `REVALIDATE` строится вокруг change inventory, impact analysis и minimal dependency slice;
- impact classes `LOCAL`, `BOUNDARY`, `SYSTEMIC` являются orchestration labels, не severity;
- `SYSTEMIC` → recommendation, не автоматический full audit;
- Test Review всегда виден в capability menu;
- stack addenda остаются separate lenses;
- Project Profile — versioned local metadata с historical backfill/delta;
- generated/vendor/build/binary material учитывается отдельно;
- metadata/schema upgrade не invalidates accepted technical evidence;
- dirty working tree поддерживает committed HEAD default и explicit EPHEMERAL snapshot;
- delta report является основным продуктом targeted revalidation;
- preserved previous evidence не должно маскироваться под fresh verification.
