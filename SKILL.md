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
defined by the capability contract and registered in `working/INDEX.md`.

1. Зафиксируй repository baseline и применимые stack addenda. Для `NEW` до запуска capability создай persistent Shared Technical Model baseline по `references/shared-technical-model.md`; создание модели не означает обязательное полное заполнение всех factual slices.
2. По `references/review-method.md` создай substantive As-Built Architecture (фактическую архитектуру).
3. Выполни отдельное fresh-context review As-Built; автор не self-accepts.
4. После принятия As-Built проведи thematic discovery. Используй:
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
10. Собери main review по `references/report-contract.md`.
11. Если endpoint включает Target Architecture — создай её и проведи review/correction/re-review по `references/target-architecture-review.md`.
12. Если endpoint включает Roadmap — создай его и проведи execution-consistency review/correction/re-review по `references/remediation-roadmap-review.md`.
13. После принятия всех requested artifacts собери final package.
14. Проведи issue-only editorial review → separate correction → fresh re-review по `references/final-editorial-review.md`; presentation-only correction использует `PROJECTION_REVALIDATION` по `references/revalidation-and-freshness.md`, пока technical semantics не изменились.

## Non-Negotiable Gates

- Technical As-Built working file — source of truth; финальный As-Built prose является производной проекцией.
- Тематический агент не переписывает As-Built: он создаёт `ARCH-CORRECTION-CANDIDATE`.
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
- shared authority, evidence scope, bounded accounting and candidate decomposition → `references/shared-assurance-principles.md`
- shared evidence worksets / observations / provenance / cross-capability reuse → `references/shared-evidence-model.md`
- Shared Technical Model facts / lifecycle / Technical Model Gate / persistence → `references/shared-technical-model.md`
- capability state/resume/artifact ownership → `references/review-modes-and-orchestration.md`
- core method / As-Built-first flow → `references/review-method.md`
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

Return `REVIEW_COMPLETE` only when all required gates for the selected mode/endpoint are accepted, Discovery Coverage is `COVERAGE_ACCEPTED`, authoritative documents and cross-links are coherent, final editorial correction/re-review is accepted, and limitations are explicit.

Если material coverage остаётся `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, `COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT` или `REVALIDATION_REQUIRED`, ordinary `REVIEW_COMPLETE` запрещён.

Otherwise return `REVIEW_PARTIALLY_COMPLETE` with the exact blocked/missing gates from `working/INDEX.md`.
