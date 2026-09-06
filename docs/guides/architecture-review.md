# Руководство по Architecture Review

Architecture Review предназначен для evidence-backed анализа фактической архитектуры существующей системы и архитектурных root problems.

## Когда выбирать

Используйте Architecture Review, если нужно понять:

- runtime/deployment topology;
- ownership состояния и ресурсов;
- API/IPC/process/persistence/trust boundaries;
- ключевые command/read/async/external flows;
- lifecycle, startup/readiness/shutdown;
- retries, recovery, idempotency;
- concurrency и shared-state behavior;
- failure/partial-failure behavior;
- configuration/secrets;
- observability;
- архитектурные root causes и remediation direction.

Если задача только в тестовом доказательстве поведения или implementation quality, Architecture Review не обязан быть включён.

## Выбор depth

### `STANDARD_FULL`

Стандартный полный аудит. Требует factual STM coverage уровня `FULL/COMPACT` перед full-model thematic discovery.

Подходит для большинства production repositories, когда нужен полный обзор системы без forensic-level evidence density.

### `FORENSIC`

Углублённое исследование. Требует `FULL/FORENSIC` factual depth.

Используйте, когда:

- система security-sensitive;
- существенны races/concurrency;
- boundaries спорны;
- есть сложные failure/recovery paths;
- необходимо более подробное сохранение evidence и correction history.

`FORENSIC` — это depth, а не endpoint. Он поддерживает все три результата.

## Выбор endpoint

### `REVIEW_ONLY`

Результат: Architecture Review + authoritative findings.

Выбирайте, если нужен диагноз current system без проектирования будущего состояния.

### `REVIEW_PLUS_TARGET_ARCHITECTURE`

Добавляет Target Architecture после принятия review.

Target должна отвечать на подтверждённые root problems и не проектироваться из непроверенных candidates.

### `REVIEW_PLUS_TARGET_AND_ROADMAP`

Добавляет Target Architecture и Remediation Roadmap.

Roadmap описывает ordering, prerequisites, gates и evidence, а не просто список пожеланий.

## Как проходит анализ

Высокоуровнево:

```text
baseline
-> Shared Evidence
-> accepted/fresh STM
-> Technical Model Coverage acceptance
-> thematic discovery
-> discovery coverage
-> independent candidate verification
-> root-boundary adjudication
-> severity
-> RF-* authority
-> optional Target Architecture
-> optional Roadmap
-> projections/package closeout
```

## Что считается Architecture finding

`RF-*` должен иметь evidence-backed material consequence и root boundary.

Плохой пример:

> В проекте много singleton classes.

Хороший архитектурный finding требует доказать, что конкретный mechanism создаёт architecture-level consequence, например нарушает ownership, isolation, lifecycle или failure semantics.

Implementation smell без architecture root cause может принадлежать Code Quality Review.

## As-Built и STM

As-Built Architecture — human-readable synthesis accepted STM и architecture-specific interpretation. Она полезна для чтения, но factual authority остаётся STM.

Если As-Built и STM расходятся, нельзя «починить факт» редактированием report. Нужно reconcile owning authority.

## Coverage discipline

Полный Architecture Review не должен строить global findings по локально исследованной области.

Coverage review фиксирует:

- covered domains;
- partial/blocked areas;
- high-risk domains;
- limitations;
- independent acceptance.

Недостаточная coverage должна быть видима в final report.

## Пример выбора

```text
Architecture Review: ON
Depth: FORENSIC
Endpoint: REVIEW_PLUS_TARGET_AND_ROADMAP
Test Engineering: OFF
Code Quality Review: ON
  Findings View/Report
```

Это означает глубокий architecture analysis и отдельный Code Quality analysis. Code Quality не становится частью Architecture authority.

## После accepted review

- новые commits → `REVALIDATE`;
- нужен Target после `REVIEW_ONLY` → `EXTEND`;
- нужен Roadmap после Target → `EXTEND`;
- broken Markdown/report links → `PROJECTION_REPAIR`;
- нужно просто прочитать accepted report → `USE_EXISTING`.

## Связанные документы

- [Review Suite](../concepts/review-suite.md)
- [Evidence и STM](../concepts/evidence-and-technical-model.md)
- [Output Reference](../reference/outputs.md)
- [Architecture Review example](../examples/architecture-review.md)
