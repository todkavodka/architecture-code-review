# Пример: архитектурный аудит legacy backend

Этот пример показывает end-to-end использование Architecture Review на существующем backend перед модернизацией.

## Исходная ситуация

Команда наследует сервис заказов. Документация неполная, часть business logic живёт в background workers, наблюдаются редкие duplicate events после timeout/retry.

Пользователь просит:

```text
Используй architecture-code-review.
Нужно понять фактическую архитектуру сервиса заказов, корневые причины duplicate completion events и получить Target Architecture с планом исправлений.
```

## Startup

Skill обнаруживает:

- previous accepted audit отсутствует;
- committed baseline: `a1b2c3d`;
- working tree clean.

Recommendation:

```text
Session Intent: NEW
```

Review Suite:

```text
Architecture Review: ON
  Depth: FORENSIC
  Endpoint: REVIEW_PLUS_TARGET_AND_ROADMAP

Test Engineering: OFF
Code Quality Review: OFF
```

`FORENSIC` выбран из-за concurrency/retry/failure-sensitive behavior. Endpoint независим от depth, поэтому Target + Roadmap допустимы.

## Evidence discovery

Создаются worksets, например:

```text
WS-001-runtime-topology
WS-002-order-state-ownership
WS-003-completion-publication
WS-004-timeout-retry
WS-005-shutdown-recovery
```

В `WS-003`:

```text
EV-004
source: src/orders/service.py
symbol: complete_order
observed: transaction is committed before event publish call

EV-007
source: src/events/publisher.py
symbol: publish_completion
observed: timeout result does not prove whether broker accepted the message
```

В `WS-004`:

```text
EV-003
source: src/workers/retry.py
observed: retry path calls publish_completion again after ambiguous timeout
```

Ни одно observation само по себе не объявляется архитектурным finding.

## Shared Technical Model

Technical Model Gate принимает facts:

```text
COMP-API
COMP-WORKER
DS-ORDERS
EVENT-ORDER-COMPLETED
INT-COMPLETE-TRANSACTION
INT-PUBLISH-COMPLETION
FLOW-ORDER-COMPLETION
```

Relations показывают, что API и retry worker участвуют в одном material publication flow, а ownership terminal publication не закреплён отдельным механизмом.

## Architecture discovery

После factual coverage accepted Architecture Review анализирует lifecycle и ownership.

Candidate:

> Несколько execution paths могут инициировать terminal publication после ambiguous timeout.

Independent verification пытается опровергнуть candidate:

- ищет broker-side idempotency;
- ищет unique publication key;
- проверяет transaction/outbox mechanism;
- проверяет consumer deduplication contract;
- проверяет retry generation ownership.

Допустим, ни один mechanism не обеспечивает system-level uniqueness.

## Accepted finding

Появляется `RF-*`, например:

```text
RF-007
root boundary: terminal event publication ownership
material consequence: ambiguous timeout can cause repeated publication attempts without a single authoritative publication owner
severity: HIGH
supporting refs:
  INT-PUBLISH-COMPLETION@rev2
  WS-003#EV-007
  WS-004#EV-003
```

Finding не формулируется как «retry code плохой». Root boundary — ownership terminal publication.

## Target Architecture

Target может предложить, например, transactional outbox + single publication ownership, если это следует из accepted constraints и прошло target review.

Traceability:

```text
RF-007
  -> target invariant: one durable publication intent per terminal transition
  -> target mechanism: transactional outbox owned by order state transition
```

## Remediation Roadmap

Roadmap не начинается с «переписать publisher».

Возможный порядок:

1. зафиксировать publication identity/invariant;
2. добавить durable outbox state;
3. перевести producer path на outbox write inside transaction;
4. внедрить publisher ownership/retry semantics;
5. добавить observability and migration checks;
6. только после acceptance удалить старые direct publish paths.

Для каждого этапа определяются prerequisites и evidence gate.

## Итоговый package

Пользователь получает:

```text
Architecture Review
Authoritative Findings Ledger
Target Architecture
Remediation Roadmap
working/INDEX.md
evidence/WS-*.md
technical-model/...
```

## Через месяц

После изменений пользователь не запускает новый forensic audit автоматически:

```text
Используй существующий audit package и REVALIDATE изменения после текущего HEAD.
```

Impact analysis должен проверить только affected facts/findings/target assumptions и сохранить unaffected accepted state.

## Что показывает этот пример

- evidence отделено от interpretation;
- factual model переиспользуется;
- finding требует falsification и root adjudication;
- Target строится после accepted review;
- Roadmap связан с findings/target;
- изменения проекта обрабатываются через bounded `REVALIDATE`.
