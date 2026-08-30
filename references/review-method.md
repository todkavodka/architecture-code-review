# Метод архитектурного и кодового аудита

Этот файл задаёт общую evidence-first методику. Режимы/статусы/INDEX описаны в `review-modes-and-orchestration.md`; ownership/scenarios — в `ownership-and-scenarios.md`; boundary dimensions — в `boundary-contract-audit.md`.

## 1. Сначала фактическая система, потом суждение

Прочитай repository-local instructions, manifests/lockfiles, CI, packaging/deployment, configuration, tests, service definitions и актуальные архитектурные документы. Зафиксируй exact repository path, branch/ref, commit и dirty state.

Не выводи архитектуру из названий директорий. Проследи реальные entry points, object/service construction, state ownership, boundaries и side effects.

## 2. As-Built Architecture — первый крупный результат

До глубокого thematic discovery создай технический As-Built source of truth в `working/00-...as-built.md`.

Он должен позволять техническому лидеру понять систему без повторного открытия source tree. Для medium project глубина обычно эквивалентна substantial 5–10 page chapter, но acceptance определяется содержанием, а не page count.

Покрой, где применимо:

1. назначение системы и ключевые сценарии;
2. процессы/applications/runtime components;
3. основные компоненты и responsibilities;
4. ownership state/resources;
5. major data/control flows;
6. external systems/native/child processes;
7. IPC/API/native/process boundaries;
8. startup/initialization/steady-state/background/failure/recovery/shutdown;
9. concurrency model;
10. storage/configuration;
11. trust boundaries/security model;
12. platform-specific behavior;
13. positive controls;
14. краткие архитектурные свойства/ограничения.

Используй ownership matrix и evidence-driven diagrams, если они улучшают понимание.

As-Built проходит независимое fresh-context review в обоих режимах. Только accepted As-Built является базой зависимых thematic passes.

## 3. Representative flows

Проследи несколько end-to-end paths, выбирая их по архитектурной значимости:

- startup/readiness;
- auth/session restoration;
- central user operation;
- background/scheduled work;
- network failure/reconnect;
- persistent write;
- shutdown;
- security-sensitive update/process/native flow.

Для каждого flow зафиксируй initiator, owner, crossed boundaries, suspension points, failure paths, cleanup и authoritative state changes.

## 4. Тематическое discovery

Discovery создаёт `CAND-*`, positive controls, open questions и architecture-correction candidates — не final findings.

### Architecture / responsibility

Проверяй dependency direction, responsibility, hidden global state, service locators, overly broad APIs, cross-layer business rules, duplicated truth. Не требуй Clean Architecture по названию patterns.

### Ownership / isolation / concurrency

Применяй `ownership-and-scenarios.md`: owner/writer/reader/lifetime/scope, A+A/A+B/cancel/disconnect/stale completion/shutdown/interleavings.

### Boundaries

Применяй `boundary-contract-audit.md` для significant IPC/API/RPC/native/process/event boundaries.

### Lifecycle / resources

Проверяй create→run→failure/retry→cancel→dispose/shutdown для sockets, child processes, files, timers, listeners, locks, database/session resources, temporary paths/ports.

### Errors

Проследи error classification/context across boundaries. Ищи swallowed failures, global process termination from local cleanup, retry without classification, fallback hiding failures, inconsistent error contracts.

### Security

Map trust boundaries, credentials, TLS, remote content, preload/native capabilities, child processes, filesystem, update chain, deserialization, URL/path validation. Serious promotion требует attack chain из `evidence-and-severity.md`.

### Configuration / localization / duplication

Ищи conflicting authoritative sources, unsafe defaults, secrets, platform paths, duplicated semantic knowledge, protocol/user-visible string mixing. Не продвигай hardcode/duplicate только из-за внешнего сходства.

### Networking / persistence / observability / performance

Review timeout/cancel/retry/idempotency/TLS/proxy, atomic writes/migrations/locking, structured correlation and sensitive logging, blocking/event-loop risks, unbounded queues/caches and lock contention — только в контексте реального impact.

### Tests / testability

Определи, какие risks реально защищены existing tests. Raw test count и отсутствие локальных tests сами по себе не доказывают runtime defect.

## 5. Safe verification

Запускай existing non-destructive checks, если среда позволяет. Не устанавливай/обновляй dependencies и не запускай fixers только ради зелёного отчёта без разрешения.

Для каждой команды фиксируй result и limitation.

## 6. Независимая проверка и adjudication

После discovery:

```text
candidates
→ independent verification
→ root-boundary adjudication
→ severity adjudication
→ authoritative ledger
```

Следуй `independent-verification.md`, `root-boundary-adjudication.md`, `evidence-and-severity.md`.

Не назначай окончательную severity во время discovery.

## 7. Architecture corrections

Если thematic pass опровергает accepted As-Built, он создаёт `ARCH-CORRECTION-CANDIDATE` и продолжает в рамках собственного scope. Исправление базы выполняется отдельным review/correction/impact/revalidation loop из orchestration contract.

## 8. Positive controls и non-findings

Поддерживай registry механизмов, которые следует сохранить. Также сохраняй considered-but-not-promoted conclusions, когда они предотвращают повторное появление false positives.

Не считать finding без contextual impact:

- TODO/comments;
- file/function size;
- framework choice;
- raw warning count;
- `unwrap`/`clone`/mocks;
- hardcoded literal;
- отсутствие тестов.

## 9. Режимы

`STANDARD_FULL` использует те же correctness gates, но может объединять тематические working passes.

`FORENSIC` разделяет ownership/lifecycle/boundaries/frontend/security/maintainability и последующие adjudication stages явнее, сохраняя более подробный evidence trail.

В обоих режимах не возвращайся к одному giant prompt/report pass.

## 10. Separation of diagnosis and design

Если endpoint = `REVIEW_ONLY`, остановись после принятого authoritative audit package.

Target Architecture и detailed Remediation Roadmap создаются только по выбранному endpoint и проходят собственные независимые reviews.
