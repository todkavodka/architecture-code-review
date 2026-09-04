# Метод архитектурного и кодового аудита

Этот файл задаёт общую evidence-first методику. Режимы/статусы/INDEX описаны в `review-modes-and-orchestration.md`; ownership/scenarios — в `ownership-and-scenarios.md`; boundary dimensions — в `boundary-contract-audit.md`; доказательство полноты discovery — в `discovery-coverage.md`.

## 1. Сначала фактическая система, потом суждение

Прочитай repository-local instructions, manifests/lockfiles, CI, packaging/deployment, configuration, tests, service definitions и актуальные архитектурные документы. Зафиксируй exact repository path, branch/ref, commit и dirty state.

Не выводи архитектуру из названий директорий. Проследи реальные entry points, object/service construction, state ownership, boundaries и side effects.

## 2. Factual STM и As-Built projection — первый крупный результат

До глубокого thematic discovery собери/revalidate required Shared Evidence и
Shared Technical Model (STM) facts. Accepted/fresh STM, а не As-Built prose,
является factual technical authority. Для full Architecture Review сначала
требуется `FULL` STM и `TECHNICAL_MODEL_COVERAGE_ACCEPTED` по
`technical-model-coverage.md`.

После этого собери human-readable As-Built projection из accepted/fresh STM
плюс architecture-oriented synthesis. Она должна позволять техническому лидеру
понять систему без повторного открытия source tree. Для medium project глубина
обычно эквивалентна substantial 5–10 page chapter, но acceptance определяется
содержанием, а не page count.

Покрой, где применимо:

1. назначение системы и ключевые сценарии;
2. deployment topology и runtime components/processes;
3. ownership state, lifecycle и authority;
4. API/IPC/process/persistence/trust/deployment boundaries;
5. command/write, read/query, async/background и external-integration flows;
6. state machines и lifecycle transitions;
7. startup/readiness/shutdown, cancellation, retry и recovery;
8. concurrency, shared state, serialization и idempotency;
9. failure domains и partial failure;
10. authentication/authorization и trust contracts;
11. configuration/secrets;
12. persistence, migrations и consistency;
13. observability/operability, где они material;
14. platform-specific behavior и positive controls;
15. краткие архитектурные свойства/ограничения.

Пункты 1–14 — factual STM coverage/content: purpose/scenarios, topology,
ownership, boundaries, flows, lifecycle, concurrency, failure, trust,
configuration, persistence, observability и platform facts. Пункт 15 —
Architecture-owned interpretation, не STM fact. Это materiality-driven модель,
а не универсальный checklist с одинаковой глубиной для каждого пункта.
Technical Model Coverage и materiality map определяют, что применимо, что
получает bounded evidence, а что фиксируется как `NOT_APPLICABLE` или `UNKNOWN`
с причиной. As-Built projection сохраняет эту factual parity, provenance и
видимые limitations; она не нормализует `PARTIAL`, stale или unresolved input в
certainty.

Используй ownership matrix и evidence-driven diagrams, если они улучшают понимание.

Technical Model Coverage Review независимо принимает factual substrate в обоих
режимах. Только accepted/fresh required STM является базой зависимых thematic
passes. As-Built projection проходит отдельную projection/parity review, но не
становится factual authority.

### Evidence-bounded architecture claims

Architecture claim scope must not exceed directly investigated evidence scope:

```text
supported claim scope <= directly exercised / directly evidenced material scope
```

Read-path authorization evidence does not prove write, enumeration, background,
or export authorization. Nominal success does not prove retry, unknown-outcome
recovery, restart durability, or concurrent duplicate safety. Missing evidence
alone is not an implementation defect; preserve `PARTIAL`, `NOT_PROVEN`, or
`UNKNOWN` where the wider claim was not exercised.

Search explicitly for material contradictions across:

- application code ↔ deployment/configuration;
- API contract ↔ persistence behavior;
- documented ownership ↔ actual state mutation path;
- auth middleware ↔ background/export paths;
- lifecycle assumptions ↔ service/container/Ansible definitions;
- retry claims ↔ persistence/queue semantics.

Factual contradictions first become `TECH_FACT_CANDIDATE`,
`TECH_FACT_CONFLICT` или `TECH_FACT_REVALIDATION_REQUEST` with provenance and
impact. They are not automatic final findings and do not silently rewrite
accepted STM or an As-Built projection. An Architecture-owned interpretation
contradiction may instead become `OQ-*` or `ARCH-CORRECTION-CANDIDATE`.

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

Одновременно thematic passes обязаны накапливать coverage evidence по `discovery-coverage.md`. Полнота не выводится из количества кандидатов.

Общий security/correctness pattern для material source-driven risks:

```text
source / capability
→ validation / transformation
→ boundary / interpreter / resource / authority decision
→ guard / ownership / parameterization
→ side effect
→ reachable consequence
```

Этот pattern — не quota и не замена domain-specific contracts. Он помогает не ограничивать security только перечислением trust boundaries.

### Architecture / responsibility

Проверяй dependency direction, responsibility, hidden global state, service locators, overly broad APIs, cross-layer business rules, duplicated truth. Не требуй Clean Architecture по названию patterns.

### Ownership / isolation / concurrency

Применяй `ownership-and-scenarios.md`: owner/writer/reader/lifetime/scope, A+A/A+B/cancel/disconnect/stale completion/shutdown/interleavings.

### Boundaries

Применяй `boundary-contract-audit.md` для significant interaction, interpreter, resource-addressing и authority/capability boundaries. Coverage completeness для этих classes регулируется `discovery-coverage.md`.

### Lifecycle / resources

Проверяй create→run→failure/retry→cancel→dispose/shutdown для sockets, child processes, files, timers, listeners, locks, database/session resources, temporary paths/ports.

### Errors

Проследи error classification/context across boundaries. Ищи swallowed failures, global process termination from local cleanup, retry without classification, fallback hiding failures, inconsistent error contracts.

### Security

Map trust boundaries, credentials, TLS, remote content, preload/native capabilities, child processes, filesystem, update chain, deserialization, URL/path validation, authentication/authorization scope, interpreter/dynamic-construction sinks, outbound-target control, secrets propagation, privileged capabilities и legacy/versioned surfaces — только где соответствующие mechanisms реально присутствуют.

Не считай этот список достаточным proof-of-coverage. High-risk domains закрываются по semantic contracts из `discovery-coverage.md`.

Serious promotion требует attack chain из `evidence-and-severity.md`.

### Configuration / localization / duplication

Ищи conflicting authoritative sources, unsafe defaults, secrets, platform paths, duplicated semantic knowledge, protocol/user-visible string mixing. Не продвигай hardcode/duplicate только из-за внешнего сходства.

### Networking / persistence / observability / performance

Review timeout/cancel/retry/idempotency/TLS/proxy, atomic writes/migrations/locking, structured correlation and sensitive logging, blocking/event-loop risks, unbounded queues/caches and lock contention — только в контексте реального impact.

Request-driven amplification/resource exhaustion и business replay/order/idempotency рассматривай как mechanism classes, а не только как performance observations.

### Tests / testability

Определи, какие risks реально защищены existing tests. Raw test count и отсутствие локальных tests сами по себе не доказывают runtime defect.

### Discovery coverage closeout

После planned thematic passes:

```text
update Discovery Coverage Matrix
→ classify every applicable domain
→ record evidence / non-findings / candidates / OQ / limitations
→ Independent Coverage Review
→ targeted correction/re-review if needed
→ COVERAGE_ACCEPTED
```

`DISCOVERY_COMPLETE` без `COVERAGE_ACCEPTED` не разрешает переход к candidate verification.

## 5. Safe verification

Запускай existing non-destructive checks, если среда позволяет. Не устанавливай/обновляй dependencies и не запускай fixers только ради зелёного отчёта без разрешения.

Для каждой команды фиксируй result и limitation.

Runtime reproduction для security/correctness evidence выполняется только в безопасных рамках `evidence-and-severity.md`; static finding не требует forced PoC.

## 6. Независимая проверка и adjudication

После `COVERAGE_ACCEPTED`:

```text
candidates
→ independent verification
→ root-boundary adjudication
→ severity adjudication
→ authoritative ledger
```

Следуй `independent-verification.md`, `root-boundary-adjudication.md`, `evidence-and-severity.md`.

Coverage Review и candidate verification — разные gates:

```text
Coverage Review: не пропущен ли material class исследования?
Independent Verification: реален ли уже существующий CAND?
```

Не назначай окончательную severity во время discovery или coverage review.

## 7. Factual reconciliation and Architecture corrections

Если thematic pass обнаруживает factual contradiction с accepted/fresh STM, он
создаёт `TECH_FACT_CONFLICT` (или `TECH_FACT_CANDIDATE` /
`TECH_FACT_REVALIDATION_REQUEST`) и продолжает только в unaffected scope.
Technical Model Gate выполняет evidence review, revision/rejection и impact
analysis; capability не изменяет STM и не «чинит» As-Built projection как
factual authority.

Подтверждённая STM correction требует targeted technical-coverage и projection
impact scan; не сбрасывай unrelated accepted coverage без evidence влияния.

Если correction относится к Architecture-owned invariant, causal interpretation,
race conclusion, finding/root/severity или remedy implication, а не к факту STM,
используй `ARCH-CORRECTION-CANDIDATE` и существующий architecture
review/correction/adjudication loop. Такой correction не делает factual matrix
finding и не переписывает STM.

## 8. Positive controls и non-findings

Поддерживай registry механизмов, которые следует сохранить. Также сохраняй considered-but-not-promoted conclusions, когда они предотвращают повторное появление false positives и служат coverage evidence.

Не считать finding без contextual impact:

- TODO/comments;
- file/function size;
- framework choice;
- raw warning count;
- `unwrap`/`clone`/mocks;
- hardcoded literal;
- отсутствие тестов;
- raw-looking API name без source/provenance/effect;
- HTTP client без доказанного control over destination;
- generic slowness без material resource impact.

## 9. Режимы

`STANDARD_FULL` использует те же correctness gates, может объединять thematic working passes, но всё равно создаёт compact coverage matrix и проходит coverage closeout.

`FORENSIC` разделяет ownership/lifecycle/boundaries/frontend/security/maintainability и последующие adjudication stages явнее, сохраняет более подробный evidence trail и имеет явный Independent Coverage Review gate.

В обоих режимах не возвращайся к одному giant prompt/report pass.

## 10. Separation of diagnosis and design

Если endpoint = `REVIEW_ONLY`, остановись после принятого authoritative audit package.

Target Architecture и detailed Remediation Roadmap создаются только по выбранному endpoint и проходят собственные независимые reviews.
