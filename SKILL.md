---
name: architecture-code-review
description: Use when performing a whole-project or subsystem architecture/code review where lifecycle, ownership, concurrency, trust boundaries, security, reliability, maintainability, or testability require evidence-backed analysis rather than a lint-style checklist.
---

# Architecture Code Review

## Overview

Проводить evidence-first архитектурный аудит существующей системы как управляемый, возобновляемый процесс. Сначала реконструировать фактическую архитектуру и владение, затем искать кандидатов, независимо проверять их, валидировать корневые причины и только после этого назначать критичность.

**Core principle:** архитектурное утверждение должно опираться на traced code path (прослеженный путь кода), ownership (владение) и concrete effect (конкретное последствие), а не на название директории, framework convention или stylistic preference.

## Start Gate — выбрать режим и результат

Перед существенным исследованием прочитай `references/review-modes-and-orchestration.md` и покажи пользователю рекомендацию с объяснением:

- `STANDARD_FULL (полный стандартный аудит)`;
- `FORENSIC (углублённое архитектурное расследование)`.

Пользователь отдельно выбирает endpoint:

- `REVIEW_ONLY`;
- `REVIEW_PLUS_TARGET_ARCHITECTURE`;
- `REVIEW_PLUS_TARGET_AND_ROADMAP`.

Не выбирай `FORENSIC` молча и не выводи Target Architecture/Roadmap из глубины режима автоматически.

## Persistent Workflow

Создай audit package и `working/INDEX.md` по `references/review-modes-and-orchestration.md`. `INDEX.md` — persistent workflow authority; resume-critical state не хранится только в чате.

Если host предоставляет native todo/task/plan tool, **обязательно реально вызывай этот tool** для создания и обновления видимого плана. Не считай текстовое описание плана, изменение `INDEX.md` или внутреннее reasoning заменой native tool call. После каждого material coordinator state transition сначала валидируй artifacts/handoffs и обнови `INDEX.md`, затем вызови native plan/todo tool с актуальной projection. После завершения batch subagents выполни ту же reconciliation последовательность. При resume восстанови состояние из `INDEX.md` и вызови native plan/todo tool до продолжения работы. Если native tool отсутствует — показывай компактный текстовый plan/status. Stability важнее максимальной параллельности.

Subagents могут исследовать независимые domains и сами писать свои `working/*.md`. Один файл имеет одного active writer. Каждый agent-owned artifact содержит persisted `HANDOFF SUMMARY`.

Если coordinator/reviewer собирается использовать `INDEX.md`, handoff или другой compact semantic record как замену чтению owning technical artifact, сначала проверь freshness/revision binding по `references/revalidation-and-freshness.md`. Stale compact state не является accepted downstream input.

## Required Review Flow

1. Зафиксируй repository baseline и применимые stack addenda.
2. По `references/review-method.md` создай substantive As-Built Architecture (фактическую архитектуру).
3. Выполни отдельное fresh-context review As-Built; автор не self-accepts.
4. После принятия As-Built проведи thematic discovery. Используй:
   - `references/ownership-and-scenarios.md`;
   - `references/boundary-contract-audit.md`;
   - `references/lifecycle-and-mermaid.md`;
   - applicable `references/stacks/*.md`.
5. Discovery создаёт `CAND-*`, `PC-*`, `OQ-*`, `AC-*`, но не final RF.
6. Независимо проверь кандидатов по `references/independent-verification.md`.
7. Проведи root-boundary adjudication по `references/root-boundary-adjudication.md`.
8. Только после этого назначь severity по `references/evidence-and-severity.md` и сформируй authoritative ledger.
9. Собери main review по `references/report-contract.md`.
10. Если endpoint включает Target Architecture — создай её и проведи review/correction/re-review по `references/target-architecture-review.md`.
11. Если endpoint включает Roadmap — создай его и проведи execution-consistency review/correction/re-review по `references/remediation-roadmap-review.md`.
12. После принятия всех requested artifacts собери final package.
13. Проведи issue-only editorial review → separate correction → fresh re-review по `references/final-editorial-review.md`; presentation-only correction использует `PROJECTION_REVALIDATION` по `references/revalidation-and-freshness.md`, пока technical semantics не изменились.

## Non-Negotiable Gates

- Technical As-Built working file — source of truth; финальный As-Built prose является производной проекцией.
- Тематический агент не переписывает As-Built: он создаёт `ARCH-CORRECTION-CANDIDATE`.
- `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED`, `BLOCKED` нельзя использовать как accepted downstream input.
- Compact persisted semantic state usable downstream только если он связан с текущей accepted owning-artifact revision; mismatch требует `AUTHORITY_RECONCILIATION_REQUIRED`.
- Presentation-only correction не перезапускает technical audit автоматически: используй `PROJECTION_REVALIDATION`; semantic drift требует `TECHNICAL_REVALIDATION_REQUIRED`.
- Major artifact author ≠ final judge. Review/correction/re-review — отдельные роли.
- Large Markdown artifacts записываются logical chunks (логическими частями) с проверкой; не полагайся на один giant write.
- Serious security finding требует attack chain; absence of hardening alone ≠ HIGH/CRITICAL.
- Severity отделена от correctness verification.
- Positive Controls сохраняются и учитываются в Target/Roadmap.
- Absence evidence, TODO, file length, framework choice, mocks, warnings и literals не являются findings без concrete impact.
- Working artifacts могут быть terse/machine-oriented; пользовательские финальные документы обязаны объяснять `что происходит → почему → к чему приводит → что менять` связным человеческим текстом. IDs и shorthand поддерживают объяснение, но не заменяют его.
- Не меняй production code проекта во время review.

## Language Contract

Пользовательские финальные документы — связный русский технический текст. При первом существенном употреблении допустимо `English term (русский аналог)`; exact identifiers, code, paths, API/IPC/protocol names и formal status tokens не переводятся.

Не переноси стиль `HANDOFF SUMMARY`, ledger rows и agent scratchpad в финальную прозу. Обычные понятия формулируй естественно по-русски; избегай гибридов вроде `prod-risks`, `негрейсфул shutdown`, `credential-ами`, если это не точный identifier. Для сложной topology/lifecycle/ownership/target-механики используй полезные Mermaid-диаграммы по соответствующим reference contracts.

## References — Authority Map

- modes / endpoint / INDEX / state / resume / subagents → `references/review-modes-and-orchestration.md`
- projection-only revalidation / compact-state freshness / stale projection reconciliation → `references/revalidation-and-freshness.md`
- core method / As-Built-first flow → `references/review-method.md`
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

Return `REVIEW_COMPLETE` only when all required gates for the selected mode/endpoint are `COMPLETE`, authoritative documents and cross-links are coherent, final editorial correction/re-review is accepted, and limitations are explicit.

Otherwise return `REVIEW_PARTIALLY_COMPLETE` with the exact blocked/missing gates from `working/INDEX.md`.
