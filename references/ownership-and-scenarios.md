# Владение, инварианты и неблагоприятные сценарии

Этот файл является авторитетным источником для Architecture Review interpretation
ownership (владения состоянием и ресурсами), derivation of invariants (вывода
инвариантов) и adversarial scenarios (неблагоприятных сценариев
конкурентности/жизненного цикла). Factual owner/writer/reader/lifetime/scope
records принадлежат accepted/fresh Shared Technical Model (STM), а здесь
используются как factual input для architecture analysis.

## 1. Матрица владения

Для значимых сущностей/ресурсов STM фиксирует factual matrix:

| Entity/resource | Authoritative owner | Writers | Readers | Lifetime | Scope |
|---|---|---|---|---|---|

Владение выводится из реальных путей кода и runtime-поведения, а не из названий
директорий или желаемой архитектуры. Матрица с owner/writers/readers/lifetime/
scope — STM fact with evidence/provenance, не architecture finding и не
`SER-*`. Если required factual row missing, stale или conflicting, запроси
`TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT` или
`TECH_FACT_REVALIDATION_REQUEST`; не создавай parallel ownership inventory.

Особенно проверяй:

- process-global singleton;
- per-connection/per-session ownership;
- frontend store vs backend/native state;
- временные файлы/порты/child processes;
- event listeners/subscriptions;
- locks/abort controllers/retry loops;
- persistent state/cache/configuration.

## 2. Инварианты

Инвариант — требуемое свойство системы, которое следует из реального продукта/контракта/поведения.

Хорошая форма:

```text
Наблюдение: profileId уникален только внутри connection.
Требование продукта: две connections могут существовать одновременно.
Инвариант: session state нельзя глобально идентифицировать только profileId.
```

Не придумывай инвариант только потому, что он сделал бы архитектуру «чище».

Для каждого инварианта укажи:

- источник требования;
- scope;
- владельца;
- что нарушит инвариант;
- какими flows он проверяется.

## 3. Неблагоприятная матрица сценариев

Для stateful/concurrent областей, где применимо, проверь минимум:

```text
A + A duplicate operation
A + B simultaneous owners
operation + cancel
operation + disconnect/dispose
old completion after replacement
retry + cancellation
shutdown during active work
duplicate event
missing event
same local ID under two parent owners
```

Не превращай список в механическую квоту. Выбирай сценарии по реальным capability/ownership boundaries.

## 4. Race/interleaving evidence

Race finding обычно требует конкретной последовательности:

```text
A starts
→ A suspends/awaits/subscribes
→ B mutates relevant shared state
→ A resumes
→ stale/invalid mutation or wrong-owner effect
```

Без достижимой последовательности это кандидат, а не подтверждённый race.

Для каждого сценария укажи:

- initial state;
- actors/owners;
- suspension/interleaving point;
- state mutation;
- resumed behavior;
- concrete consequence;
- existing guards/falsification attempt.

## 5. Positive controls

Фиксируй механизмы, которые правильно обеспечивают ownership/isolation/concurrency:

- корректные owner keys;
- locks;
- generation/version checks;
- cancellation tokens;
- scoped DI/object graph;
- idempotency;
- dynamic resource allocation.

Positive Control не является «похвалой ради баланса»; это механизм, который целевая архитектура и remediation не должны случайно сломать.

## 6. Factual correction request

Если тематическое исследование противоречит accepted/fresh STM ownership fact,
**не редактируй STM или As-Built projection напрямую**. Запроси Technical Model
Gate:

Запиши:

```markdown
## TECH_FACT_CONFLICT TFC-###

**Текущий STM факт/revision:** ...
**Наблюдаемое противоречие:** ...
**Доказательства:** ...
**Предполагаемое влияние:** ...
**Затронутые области:** ...

Статус: TECH_FACT_CONFLICT
```

Используй `TECH_FACT_CANDIDATE` для нового factual material и
`TECH_FACT_REVALIDATION_REQUEST` для stale/impact-affected factual material.
Дальше применяется Technical Model Gate из `shared-technical-model.md`.

## 7. Architecture correction candidate

Если factual input accepted/fresh, но Architecture-owned invariant, adverse
scenario interpretation, race conclusion, `SER-*`, finding/root/severity или
remediation implication требует correction, используй
`ARCH-CORRECTION-CANDIDATE`. Он не меняет factual owner/writer matrix и следует
architecture correction/adjudication protocol.

## 7.1 Change Review candidate Architecture assessment

In `CHANGE_REVIEW_CANDIDATE` mode, Architecture records interpretation only:

```text
architecture_candidate_assessment:
  candidate_origin: CR-*/CRF-*
  affected_accepted_refs: [<accepted STM/Architecture refs>]
  candidate_fact_refs: [<CR-*/CF-* refs>]
  assessment_effect: INTRODUCES_RISK | WORSENS_EXISTING | MITIGATES |
                     POTENTIALLY_RESOLVES | NO_MATERIAL_IMPACT | UNKNOWN_IMPACT
  interpretation
  limitations
```

This assessment cannot create an accepted Architecture finding, root,
severity, invariant, or STM fact. `RESOLVED`, `CLOSED`, and `ACCEPTED` are not
candidate Architecture outcomes; they may only quote an existing canonical
state. An explicit `RECONCILE_CHANGE` dispatch routes the qualified input to
Architecture authority, which independently adjudicates and creates or links
the canonical record while retaining `candidate_origin` traceability.

`CHANGE_REVIEW_CANDIDATE` is the Architecture candidate mode for a selected
Change Review. It may interpret changed accepted references, including
parent-qualified API operation, property, and boundary evidence, but it must
remain review-local: it cannot allocate or mutate an accepted `RF-*`, STM
fact, invariant, root, severity, or lifecycle state. The later Architecture
authority decision is the only path to canonical acceptance.

## 8. Supporting Engineering Risks

Broad structural patterns могут повышать вероятность повторения дефектов, не являясь сами одним runtime root finding:

- semantic owner не закодирован в identity;
- lifecycle размазан по нескольким флагам;
- event переносит identity, но consumer её выбрасывает;
- shared resource не owner-keyed;
- нет локального deterministic regression suite.

Такие наблюдения можно вести как `SER-*`; не присваивай им автоматически severity продуктового дефекта.

## Product Architecture Review boundary

In Product mode, a Product-scoped `RF-*` is an Architecture Review semantic
record only when it has an independently adjudicated cross-project
architectural consequence. Its evidence packet names the accepted Product
revision and immutable baseline, affected Projects, qualified `WS-*`/`EV-*`
observations, accepted STM facts/relations, lifecycle, severity, provenance,
and direct dependencies. Product membership or a generated aggregation does
not promote a Project-local RF. Product report/projection content is
navigation only and cannot write the RF.
