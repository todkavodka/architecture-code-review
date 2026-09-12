---
name: architecture-code-review
description: Use when performing a whole-project or subsystem architecture/code review where lifecycle, ownership, concurrency, trust boundaries, security, reliability, maintainability, or testability require evidence-backed analysis rather than a lint-style checklist.
---

# Architecture Code Review

## Overview

Проводить evidence-first архитектурный аудит существующей системы как управляемый, возобновляемый процесс. Сначала реконструировать фактическую архитектуру и владение, затем искать кандидатов, независимо проверять полноту discovery и сами кандидаты, валидировать корневые причины и только после этого назначать критичность.

**Core principle:** архитектурное утверждение должно опираться на traced code path (прослеженный путь кода), ownership (владение) и concrete effect (конкретное последствие), а полнота discovery — на mechanism coverage (покрытие классов механизмов), а не на количество найденных замечаний.

## Start Gate — Session Orchestration

Перед существенным исследованием прочитай `references/session-orchestration.md`.
Определи/reconcile предыдущий audit package, зафиксируй baseline и dirty state,
собери или backfill локальный Project Profile, затем покажи рекомендованный
Session Intent и только относящиеся к нему configuration choices. Не начинай
существенную работу для `NEW`, `RESUME`, `REVALIDATE`, `EXTEND` или
`PROJECTION_REPAIR`, пока требуемый пользовательский выбор не разрешён.

`PROJECTION_REPAIR` используется только для исправления пользовательских/финальных
проекций уже принятого аудита. Он не является техническим re-audit: исправляй
язык, структуру, ссылки, Markdown/Mermaid, навигацию, терминологию и
cross-references по принятой authority. Каждый changed projection проходит
`PROJECTION_REVALIDATION`; semantic drift требует
`SEMANTIC_DRIFT_DETECTED` + `TECHNICAL_REVALIDATION_REQUIRED`.

Product / multi-project mode is an explicit opt-in route governed by
`references/product-multi-project-review.md`. The coordinator may select and
pin an accepted Product revision and exact baseline only after separate
Product Context Workflow authorization. Source-read, dirty-admission,
semantic-write, test, code, worktree, commit, push, PR, and deployment actions
remain independently authorized; Product membership grants none of them.
Product `REVALIDATE` is impact-driven and bounded, and Product `EXTEND` is
additive. Neither implies a full Product reread or automatic projection
regeneration. Product-free single-project sessions retain the existing route
and do not require Product state.

From a non-Git Coordination Root, Product requests such as `покажи состояние
продукта`, `обнови существующие дочерние аудиты`, `доведи весь продукт до
актуального аудита`, `что изменилось с прошлого общего аудита?`, `покажи
влияние изменений backend`, `обнови backend и оцени влияние на продукт`, or
`я уже обновил backend отдельно, подхвати изменения` are normalized to the
existing Product/requested-work/child-intent semantics. These phrases are
illustrative natural-language examples, not a formal CLI grammar or persisted
command vocabulary. Membership and requested work are resolved and confirmed
before substantive work; a broad request never silently selects every
discovered repository, capability, or full Product review.

The top-level semantic capabilities remain exactly Architecture Review, Test
Engineering, and Code Quality Review. Federated coordination, Technical
Documentation, and dependency/readiness views are orchestration or output
concerns, not additional capabilities.

## Stage F Interface, API, and Data Integration Routing

When a review includes interface, API, integration, event, persistence, or
data-access scope, acquire and qualify bounded observations through
[`shared-evidence-model.md`](references/shared-evidence-model.md). Preserve
`DIRECT_DECLARATION`, `STRONG_INFERENCE`, and `WEAK_HINT` as evidence metadata;
they do not accept facts. Route candidates and limitations to the Technical
Model Gate, which remains the sole authority for accepted `IF-*`, `INT-*`,
`DS-*`, `EVENT-*`, and `FLOW-*` facts. Use the Stage F extensions in
[`shared-technical-model.md`](references/shared-technical-model.md), including
the distinction between interactions and relations, precise access authority
in `INT-*`, and `MIGRATION` versus `MIGRATION_AUTHORITY`.

For a materially relevant declared external contract, invoke the existing
automatic Contract Verification route in
[`test-engineering-contract.md`](capabilities/test-review/references/test-engineering-contract.md).
`CC-*` remains the Test Engineering authority for compatibility; the umbrella
workflow does not match interfaces or adjudicate `COMPATIBLE` or
`INCOMPATIBLE`.

After required accepted and fresh semantic inputs are available, route Stage F
outputs through the Technical Documentation projections in
[`technical-documentation.md`](references/technical-documentation.md). They
remain derived projections, with no projection-prose feedback into STM and no
automatic regeneration. When Product mode is explicitly selected, reuse the
existing Stage E qualification in
[`product-multi-project-review.md`](references/product-multi-project-review.md);
Product is optional, single-project review remains first-class, and Product
does not become a factual authority or permission boundary.

Before user-facing projection output, apply the owning evidence and rendering
safety contracts: omit `SECRET`, redact or safely alias `SENSITIVE_INTERNAL`,
and render `SAFE_TECHNICAL_IDENTIFIER` only when permitted. Dynamic operations,
unresolved targets or comparison inputs, partial or unavailable sources, stale
projections, and unresolved CC state remain explicit limitations; orchestration
must not turn them into exact, compatible, clean, empty, or not-applicable
results without the owning authority.

Stage F routing does not introduce an automatic API compatibility engine,
runtime database scanner, SQL parser, distributed tracing system, external
discovery crawler, or projection-regeneration system. Any such capability
requires a separate approved architecture and implementation decision.

Stage B session intents converge on the same explicit projection handoff:
`NEW` and `EXTEND` finish the requested semantic work first, while
`REVALIDATE` finishes its impact-driven semantic delta. Once that semantic state
is stabilized, run Projection Impact Analysis and persist
`PROJECTION_IMPACT_ACCOUNTED`; this accounts for freshness but never regenerates
projection content. If a requested output or package requires fresh projection
content, invoke a separate `RG-*` regeneration workflow with the appropriate
scope. Closeout uses the named package and gate policy, so unrelated stale
projections remain visible without blocking an unrelated gate. The detailed
intent and closeout routing is owned by `references/session-orchestration.md` and
`references/review-modes-and-orchestration.md`.

## Persistent Workflow

Создай audit package и `working/INDEX.md` по `references/review-modes-and-orchestration.md`. `INDEX.md` — persistent workflow authority; resume-critical state не хранится только в чате.

Если host предоставляет native todo/task/plan tool, **обязательно реально вызывай этот tool** для создания и обновления видимого плана. Не считай текстовое описание плана, изменение `INDEX.md` или внутреннее reasoning заменой native tool call. После каждого material coordinator state transition сначала валидируй artifacts/handoffs и обнови `INDEX.md`, затем вызови native plan/todo tool с актуальной projection. После завершения batch subagents выполни ту же reconciliation последовательность. При resume восстанови состояние из `INDEX.md` и вызови native plan/todo tool до продолжения работы. Если native tool отсутствует — показывай компактный текстовый plan/status. Stability важнее максимальной параллельности.

Subagents могут исследовать независимые domains и сами писать свои `working/*.md`. Один файл имеет одного active writer. Каждый agent-owned artifact содержит persisted `HANDOFF SUMMARY`.

Если coordinator/reviewer собирается использовать `INDEX.md`, handoff или другой compact semantic record как замену чтению owning technical artifact, сначала проверь freshness/revision binding по `references/revalidation-and-freshness.md`. Stale compact state не является accepted downstream input.

При resume/reconciliation `COVERAGE_ACCEPTED` не является exception authority над owning Discovery Coverage Matrix. Если independent coverage review утверждает `COVERAGE_ACCEPTED`, но material row в owning matrix остаётся `PARTIALLY_COVERED`, `BLOCKED` или `REVALIDATION_REQUIRED`, считай coverage authority противоречивой: downstream progression блокируется до evidence-backed correction/re-review. Не рационализируй такое расхождение формулировкой «partial coverage acceptable for this scope» и не переписывай INDEX вперёд к `COMPLETE`.

Перед downstream use компактной Discovery Coverage projection проверь её структурную целостность. Если `domains.total` не равен сумме представленных mutually-exclusive status buckets, projection невалидна: используй authority reconciliation против owning matrix/review, а не доверяй арифметически противоречивому INDEX.

## Required Review Flow

Test Review is a composable capability. It may be selected initially, recommended
when discovery identifies a material automated-test surface, or attached later to
an existing audit. Its specialist methodology lives in
`capabilities/test-review/SKILL.md`; the umbrella orchestrator retains shared
authority, freshness, artifact-ownership, and completion gates.

Test Engineering output selection is persisted as independent booleans and
executes a minimum dependency slice. `Test Assurance` remains the compatibility
core; `Behavior Model` is an internal dependency and applicable `Contract
Verification` is automatic. Optional output projections and ownership are
defined by the capability contract and recorded as coordinator routing state
in `working/INDEX.md`; that record is not the generated Stage B projection
registry.

For a full Architecture Review, construct the required `FULL` Shared Technical
Model and accept `TECHNICAL_MODEL_COVERAGE_ACCEPTED` before Architecture
thematic discovery or another consumer that requires complete factual
substrate. `STANDARD_FULL` requires `FULL/COMPACT`; `FORENSIC` requires
`FULL/FORENSIC`. The factual coverage matrix and independent gate are separate
from Architecture Discovery Coverage and are authoritative in
`references/technical-model-coverage.md`.

1. Зафиксируй repository baseline и применимые stack addenda. Для `NEW` до запуска capability создай persistent Shared Technical Model baseline по `references/shared-technical-model.md`; создание модели не означает обязательное полное заполнение всех factual slices.
2. Собери/revalidate required Shared Evidence и factual STM slices по `references/shared-evidence-model.md` и `references/shared-technical-model.md`.
3. Пройди independent Technical Model Coverage Review и прими required full STM; автор factual model не self-accepts.
4. Только после accepted/fresh required STM проведи Architecture thematic discovery. Используй:
   - `references/ownership-and-scenarios.md`;
   - `references/boundary-contract-audit.md`;
   - `references/lifecycle-and-mermaid.md`;
   - `references/discovery-coverage.md`;
   - applicable `references/stacks/*.md`.
5. Discovery создаёт `CAND-*`, `PC-*`, `OQ-*`, `AC-*`, но не final RF, и обновляет Discovery Coverage Matrix по `references/discovery-coverage.md`.
6. Закрой Discovery Coverage Matrix и проведи отдельный Independent Coverage Review. Если есть gap — targeted coverage correction/re-review. Candidate verification начинается только после `DISCOVERY_COMPLETE` + `COVERAGE_ACCEPTED`.
7. Независимо проверь кандидатов по `references/independent-verification.md`.
8. Проведи root-boundary adjudication по `references/root-boundary-adjudication.md`.
9. Только после этого назначь severity по `references/evidence-and-severity.md` и сформируй authoritative ledger.
10. Собери As-Built и main review projections по `references/report-contract.md` из accepted/fresh STM и accepted Architecture Review authority. Для каждого независимо регенерируемого projection, который производит выбранный workflow, первая генерация обязана пройти полный Stage B handoff: establish/register stable `PRJ-*` identity → bind owning capability and projection-contract revision → bind semantic and upstream projection dependencies → freeze/persist the required dependency-resolution snapshot → generate candidate content → pass `V1`–`V4` → compute the canonical fingerprint → publish the initial verified `PRJ-*@revN` → persist freshness (`CURRENT`, `STALE`, or `BLOCKED`). Только после этого projection считается valid generated projection; raw Markdown without accepted lifecycle metadata is not `CURRENT`. This uses the existing lifecycle and verification contracts and does not create an `RG-*` session for first generation unless those contracts explicitly require one.
11. Если endpoint включает Target Architecture — создай её и проведи review/correction/re-review по `references/target-architecture-review.md`.
12. Если endpoint включает Roadmap — создай его и проведи execution-consistency review/correction/re-review по `references/remediation-roadmap-review.md`.
13. После принятия всех requested artifacts собери final package.
14. Проведи issue-only editorial review → separate correction → fresh re-review по `references/final-editorial-review.md`; presentation-only correction использует `PROJECTION_REVALIDATION` по `references/revalidation-and-freshness.md`, пока technical semantics не изменились.
15. Перед `REVIEW_COMPLETE` выполни `FINAL_WORKFLOW_AUTHORITY_RECONCILED`: reconcile `working/INDEX.md` with the accepted final artifacts and package state. At minimum, verify current phase/status, selected mode/endpoint, technical-model and Discovery Coverage gate states, artifact registry, candidate/finding mappings, positive-controls registry, open questions, architecture-correction candidates, authoritative-document registry, projection state relevant to the selected package, and capability status. This reconciles compact coordinator state and references; it does not copy semantic authority into `INDEX.md`. Any stored aggregate counts/lists must match their owning authoritative artifacts. `project_profile.status` is routing-only metadata and may remain `PENDING` when its profile reference is internally valid; it is not a mandatory completion gate unless the selected workflow explicitly makes it one.

## Non-Negotiable Gates

- Accepted/fresh Shared Technical Model — factual technical authority. Human-readable As-Built — projection accepted/fresh STM плюс architecture-oriented synthesis.
- Capability не переписывает accepted STM или As-Built projection как способ исправить факт: он создаёт `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT` или `TECH_FACT_REVALIDATION_REQUEST` для Technical Model Gate. `ARCH-CORRECTION-CANDIDATE` остаётся только для Architecture-owned interpretation.
- `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED`, `BLOCKED` нельзя использовать как accepted downstream input.
- Compact persisted semantic state usable downstream только если он связан с текущей accepted owning-artifact revision; mismatch требует `AUTHORITY_RECONCILIATION_REQUIRED`.
- Shared assurance principles apply across capabilities: resolve material authority before a substantive verdict, and keep claim scope within directly evidenced material scope.
- Context Orchestration v0.3 loads minimum fresh decision evidence through dependency-sliced routing; see `references/revalidation-and-freshness.md`.
- Presentation-only correction не перезапускает technical audit автоматически: используй `PROJECTION_REVALIDATION`; semantic drift требует `TECHNICAL_REVALIDATION_REQUIRED`.
- `PROJECTION_REPAIR` не используется для сокрытия changed source/baseline; project-change freshness принадлежит `REVALIDATE`.
- Major artifact author ≠ final judge. Review/correction/re-review — отдельные роли.
- Large Markdown artifacts записываются logical chunks (логическими частями) с проверкой; не полагайся на один giant write.
- Количество и severity найденных `CAND-*`/`RF-*` не являются evidence полноты discovery.
- `DISCOVERY_COMPLETE` без `COVERAGE_ACCEPTED` не является accepted downstream input для candidate verification.
- Для full Architecture Review `TECHNICAL_MODEL_COVERAGE_ACCEPTED` обязателен до thematic discovery; `PARTIAL`, `BLOCKED` или `UNKNOWN` material STM coverage нельзя override prose verdict.
- Coverage gap исправляется targeted pass/re-review; не перезапускай весь technical audit без impact evidence.
- `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, `COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT` не являются принятым coverage state.
- Independent Coverage Review валидирует owning matrix, но не отменяет её hard row semantics: prose `COVERAGE_ACCEPTED` не может сделать material `PARTIALLY_COVERED`, `BLOCKED` или `REVALIDATION_REQUIRED` accepted downstream state.
- Арифметически или структурно противоречивая Discovery Coverage projection не является accepted persisted authority; сначала reconcile её с owning matrix/review.
- Serious security finding требует attack chain; absence of hardening alone ≠ HIGH/CRITICAL.
- Severity отделена от correctness verification.
- Positive Controls сохраняются и учитываются в Target/Roadmap.
- Absence evidence, TODO, file length, framework choice, mocks, warnings и literals не являются findings без concrete impact.
- Working artifacts могут быть terse/machine-oriented; пользовательские финальные документы обязаны объяснять `что происходит → почему → к чему приводит → что менять` связным человеческим текстом. IDs и shorthand поддерживают объяснение, но не заменяют его.
- Не меняй production code проекта во время review.

Stage B projections are explicitly classified, stable `PRJ-*` identities; lifecycle state and verified revisions follow `references/projection-lifecycle.md`. `working/INDEX.md` is `COORDINATOR_WORKFLOW_AUTHORITY`: it owns resume-critical session, gate, handoff, and coordinator state and is outside every Stage B projection mechanic. It must not receive a `PRJ-*` identity, projection fingerprint or drift result, regeneration or `RG-*` execution state, projection freshness state, or `ACTIVE`/`RETIRED` lifecycle transition. Semantic authorities are likewise outside automatic projection classification.

Operational Stage B views are non-authoritative projections and use clearly
scoped paths under `working/projections/`, such as the generated registry,
impact view, and per-session `RG-*.md` records. They summarize their owning
projection/impact/regeneration records; they never replace `working/INDEX.md`,
the direct dependency authority, or semantic authority. Path and filename do
not classify an artifact as a projection.

Semantic workflow may complete with projections `STALE`; projection freshness is not semantic truth, and regeneration never mutates semantic authority.

`PROJECTION_REPAIR` remains a bounded presentation-only operation. It may repair
the representation of unchanged accepted meaning, but it cannot mutate semantic
authority, hide a source/baseline change, or create a persistent human-owned
section in a fully generated projection.

`01-architecture-review.md` may be fully generated only after
`report-contract.md` maps every persistent Architecture meaning to an accepted
upstream owner; otherwise return
`PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY` and do not regenerate the
unmapped content.

## Language Contract

Язык пользовательского интерфейса Skill определяется текущим языком пользователя. Явная просьба использовать конкретный язык имеет приоритет. Если явной просьбы нет, используй язык последнего содержательного запроса пользователя; не переходи на английский только потому, что инструкции Skill или reference-файлы написаны по-английски.

На выбранном пользовательском языке должны быть все меню, вопросы, рекомендации, пояснения, сообщения о ходе работы и статусе, а также итоговые пользовательские документы. Это правило распространяется на весь umbrella workflow и на подключённые capabilities, включая Test Review.

Формальные идентификаторы сохраняй без перевода: `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `PROJECTION_REPAIR`, `STANDARD_FULL`, `FORENSIC`, endpoint/status tokens, точные идентификаторы кода, пути, API/IPC/protocol names и имена файлов. При необходимости после формального токена давай естественное пояснение на языке пользователя, например: `PROJECTION_REPAIR — исправить только финальные документы без повторного технического аудита`.

Постоянные machine-oriented поля, ключи `INDEX.md`, ledger rows и другие канонические технические токены могут оставаться на английском там, где это часть контракта. Объясняющий их пользовательский текст должен оставаться на выбранном языке. Смена языка пользователем действует со следующего ответа; уже сохранённые технические артефакты не переписывай только ради перевода, если пользователь этого не попросил.

Для русскоязычного пользователя финальные документы — связный русский технический текст. При первом существенном употреблении допустимо `English term (русский аналог)`; exact identifiers, code, paths, API/IPC/protocol names и formal status tokens не переводятся.

Не переноси стиль `HANDOFF SUMMARY`, ledger rows и agent scratchpad в финальную прозу. Обычные понятия формулируй естественно по-русски; избегай гибридов вроде `prod-risks`, `негрейсфул shutdown`, `credential-ами`, если это не точный identifier. Для сложной topology/lifecycle/ownership/target-механики используй полезные Mermaid-диаграммы по соответствующим reference contracts.

## References — Authority Map

- startup / previous-audit selection / session intent / Review Suite startup / Project Profile / dirty baseline → `references/session-orchestration.md`
- modes / endpoint / INDEX / state / resume / subagents → `references/review-modes-and-orchestration.md`
- projection repair / projection-only revalidation / compact-state freshness / stale projection reconciliation → `references/revalidation-and-freshness.md`
- Stage B projection identity, lifecycle, revision, freshness, drift, and required-action authority → `references/projection-lifecycle.md`
- Stage B projection dependency kinds, selector contracts, resolution snapshots, and projection DAG → `references/projection-dependencies.md`
- shared authority, evidence scope, bounded accounting and candidate decomposition → `references/shared-assurance-principles.md`
- shared evidence worksets / observations / provenance / cross-capability reuse → `references/shared-evidence-model.md`
- Shared Technical Model facts / lifecycle / Technical Model Gate / persistence → `references/shared-technical-model.md`
- STM factual-domain coverage / `STANDARD_FULL` and `FORENSIC` projection / Technical Model Coverage Review → `references/technical-model-coverage.md`
- capability state/resume/artifact ownership → `references/review-modes-and-orchestration.md`
- core method / STM-first Architecture Review flow → `references/review-method.md`
- discovery completeness / coverage matrix / independent coverage review → `references/discovery-coverage.md`
- ownership / invariants / adversarial scenarios → `references/ownership-and-scenarios.md`
- boundary contracts → `references/boundary-contract-audit.md`
- verification → `references/independent-verification.md`
- root boundaries → `references/root-boundary-adjudication.md`
- evidence / security chain / severity → `references/evidence-and-severity.md`
- lifecycle diagrams → `references/lifecycle-and-mermaid.md`
- final package / links / chunked writing → `references/report-contract.md`
- target review → `references/target-architecture-review.md`
- roadmap review → `references/remediation-roadmap-review.md`
- editorial gate → `references/final-editorial-review.md`

## Completion Gate

Return `REVIEW_COMPLETE` only when all required gates for the selected mode/endpoint are accepted, required full STM coverage is `TECHNICAL_MODEL_COVERAGE_ACCEPTED`, Architecture Discovery Coverage is `COVERAGE_ACCEPTED`, authoritative documents and cross-links are coherent, required independent verification/adjudication gates are accepted, required first-generation or regeneration Stage B projection lifecycle obligations are satisfied, `FINAL_WORKFLOW_AUTHORITY_RECONCILED` is accepted, final editorial correction/re-review is accepted, and limitations are explicit. When the selected endpoint has a projection-sensitive package gate, also require `PROJECTION_IMPACT_ACCOUNTED`, resolved package membership, and the package policy's scoped projections to be `CURRENT`; a `PERMISSIVE` gate may close with unrelated projections `STALE` and deferred.

Если material coverage остаётся `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, `COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT` или `REVALIDATION_REQUIRED`, ordinary `REVIEW_COMPLETE` запрещён.

Otherwise return `REVIEW_PARTIALLY_COMPLETE` with the exact blocked/missing gates from `working/INDEX.md`.

## Requested-work output routing

For startup, load requested-work state from `references/session-orchestration.md`
and persisted intent/dependency state from `references/review-modes-and-orchestration.md`.
Route standalone documentation to `references/technical-documentation.md`,
Product qualification to `references/product-multi-project-review.md`, and
compatibility to Test Engineering Contract Verification and `CC-*`. Shared
Evidence, STM, and Stage B contracts remain factual and lifecycle authority.

The resolved-plan confirmation shows `Session Intent`, `Scope Context`,
`Review Capabilities`, `Requested Outputs`, `Required Internal Work`, and
`Authorization / Execution Boundaries`. `Requested Outputs != Required Internal
Work`; Product Context != Requested Outputs. Routing classes are orchestration
labels only and do not create capabilities, factual families, projection
identities, lifecycle states, or authority. Selection grants no source-read,
semantic-write, test, code, Git, worktree, commit, push, PR, deployment, E2E,
simulator, environment, database-scan, SQL, tracing, or crawling permission.
