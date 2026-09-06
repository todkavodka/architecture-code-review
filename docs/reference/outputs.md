# Справочник итоговых документов

Этот справочник описывает user-facing outputs: назначение, аудиторию, prerequisites, source authority, expected content, freshness и последующее использование.

## Architecture Review

**Audience:** architects, tech leads, senior engineers, engineering managers.

**Purpose:** показать фактическую архитектуру, существенные boundaries/flows/lifecycle properties, ограничения coverage и accepted `RF-*` findings.

**Prerequisites:** selected Architecture capability, accepted factual STM coverage требуемой depth, architecture review gates.

**Source authority:** STM + Architecture-owned semantic records.

**Expected sections:** scope/baseline, as-built synthesis, material boundaries/flows, lifecycle/failure/concurrency/security observations, findings summary, limitations/coverage, links to authoritative ledger.

**Freshness:** projection lifecycle `PRJ-*`; semantic changes могут сделать report `STALE`.

**How to consume:** сначала как system-level diagnosis; для доказательства отдельного claim переходить к `RF-*`/STM/evidence.

---

## Authoritative Findings Ledger

**Audience:** architects, remediation owners, reviewers.

**Purpose:** полный traceable registry accepted `RF-*`.

**Source authority:** Architecture Review itself; ledger хранит authoritative finding records, а не executive prose.

**Expected content per finding:** ID, scope/root boundary, evidence/STM refs, material consequence, severity, relationships/supersession, status.

**Use:** remediation planning, Target/Roadmap traceability, future `REVALIDATE`.

---

## Target Architecture

**Audience:** architects, implementation leads.

**Select when:** нужен design future state after accepted review.

**Prerequisites:** accepted Architecture findings and endpoint `REVIEW_PLUS_TARGET_ARCHITECTURE` or additive `EXTEND`.

**Source authority:** accepted architecture semantics + target technical review.

**Expected content:** target boundaries/owners, lifecycle/state mechanisms, transition-relevant invariants, mapping findings → target mechanisms, unresolved constraints.

**Do not select when:** нужен только diagnosis current system.

**Update:** findings/constraints change → targeted revalidation/target consistency review, not arbitrary prose edit.

---

## Remediation Roadmap

**Audience:** engineering leadership, program/technical leads.

**Prerequisites:** accepted Architecture + Target Architecture.

**Purpose:** безопасная последовательность изменений.

**Expected content:** remediation groups, prerequisites, dependencies, gates, evidence required before next step, rollback/activation considerations where applicable.

**Anti-pattern:** generic backlog без связи с accepted root findings/target mechanisms.

---

## Test Assurance Summary

**Audience:** tech leads, QA/test leads, engineering managers.

**Required when:** Test Engineering enabled.

**Source authority:** `BC-*`, `MAT-*`, `TM-*`, `GAP-*`, applicable `CC-*`.

**Purpose:** быстрый ответ на вопрос, насколько material behavior действительно доказано тестами.

**Expected content:** overall assurance posture, strongest proven areas, critical/important gaps, limitations, recommended next actions.

---

## Test Assurance Map

**Audience:** engineers/test engineers.

**Purpose:** detailed traceability.

**Expected relation:**

```text
MAT-* -> BC-* -> TM-* -> verdict / GAP-*
```

**Use:** понять, какой exact test доказывает какой target и где evidence недостаточно.

---

## Test Plan

**Audience:** test/feature implementation teams.

**Prerequisites:** accepted assurance targets/gaps.

**Purpose:** actionable plan доказательства missing/weak behaviors.

**Expected content per item:** target/behavior, minimal test boundary, fixtures/dependencies, scenario variants, assertions, observability, acceptance evidence.

**Do not select when:** нужен только assessment current test suite без remediation plan.

---

## Contract Consistency Report

**Audience:** API owners, producer/consumer teams, migration/integration leads.

**Prerequisites:** applicable Contract Verification and accepted `CC-*` records.

**Purpose:** human-readable projection discrepancies/adjudications across:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

**Important:** report ≠ Contract Verification. Verification is internal semantic gate; report is optional projection.

---

## Test Environment Design

**Audience:** test infrastructure/CI engineers.

**Purpose:** определить faithful environment strategy for material tests.

**Expected content:** dependency inventory, selected strategy per dependency, fidelity rationale, lifecycle/reset/isolation, secrets/config, observability, CI constraints.

**Typical strategies:** `REAL_DISPOSABLE`, `SERVICE_EMULATOR`, `CONTROLLABLE_MOCK`, `IN_PROCESS_DOUBLE`, `TEMP_RESOURCE`, `NOT_REQUIRED`.

---

## Service Simulator Design

**Audience:** consumer teams, test infrastructure engineers.

**Purpose:** design controllable simulator accepted contract behavior.

**Expected content:** Contract API, State Store, Scenario Engine, Fault Injection, Event Emitter, Control API, health/reset/seed, fidelity boundaries.

**Prerequisite:** accepted behavior/contract semantics sufficient to define simulator.

**Do not select when:** simple mock/stub already faithfully proves required behavior.

---

## Service Simulator Implementation Plan

**Audience:** engineers implementing simulator.

**Prerequisite:** accepted/fresh Simulator Design.

**Expected content:** component breakdown, APIs/control plane, state model, scenario/fault implementation, test strategy for simulator, CI integration, delivery gates.

**Scope:** plan, not automatic runtime implementation.

---

## E2E Test Plan

**Audience:** test/platform/product engineers.

**Purpose:** prove guarantees requiring multiple real components.

**Expected scenario fields:** source `BC-*`, participants, real/simulated dependencies, initial state, stimulus, assertions, failure observability, cleanup/reset, CI suitability.

**Anti-pattern:** выбирать E2E только потому, что он кажется «самым полным».

---

## Code Quality Findings View / Report

**Audience:** engineers, reviewers, maintainers.

**Source authority:** accepted `CQ-*` and related `CQRA-*` state.

**Purpose:** detailed engineering view material implementation-quality findings.

**Expected content:** mechanism, evidence/provenance, consequence, severity/confidence, applicability/disposition, relationships, remediation/revalidation state.

**Selection:** explicit. Derived projection не означает auto-required.

---

## Code Quality Summary

**Audience:** tech leads, engineering managers.

**Purpose:** compact picture of dominant material Code Quality risk.

**Expected content:** top findings/themes, concentration by area, key consequences, limitations and priorities.

**Difference from Findings View:** Summary агрегирует и объясняет; Findings View даёт detailed record-level traceability.

---

## Maintainability Hotspots

**Audience:** tech leads, refactoring/ownership teams.

**Purpose:** показать области, где концентрируется evidence-backed maintenance burden.

**Source:** accepted CQ semantics, а не LOC/complexity metrics alone.

**Expected content:** hotspot area, linked findings, mechanisms, combined consequence, ownership/context, remediation considerations.

---

## Code Quality Roadmap Contribution

**Audience:** technical planning owners.

**Purpose:** Code Quality contribution в broader remediation planning.

**Expected content:** linked `CQRA-*`, remediation groups, dependencies, ordering constraints, revalidation expectations.

**Boundary:** не является Architecture Remediation Roadmap и не переписывает Architecture authority.

---

## Freshness and update rules for all outputs

User-facing document может использоваться как fresh deliverable только если его projection lifecycle и package policy это разрешают.

```text
semantic change
  -> impact accounting
  -> projection may become STALE
  -> explicit RG-* if fresh output required
```

Presentation-only correction → `PROJECTION_REPAIR`.

Semantic correction → owning technical workflow / `REVALIDATE`.

## Как выбрать минимальный набор

- diagnosis architecture → Architecture Review;
- diagnosis + future design → + Target Architecture;
- execution sequence → + Roadmap;
- confidence in tests → Test Assurance;
- remediation test backlog → + Test Plan;
- API drift → + Contract Consistency Report;
- faithful environment → + Test Environment Design;
- controllable external service → + Simulator;
- multi-component guarantees → + E2E Test Plan;
- detailed implementation quality → CQ Findings View;
- management/first-read CQ picture → + Summary;
- refactoring concentration → + Hotspots;
- CQ planning input → + Roadmap Contribution.

Не выбирайте все outputs автоматически. Review Suite должен сохранять минимально достаточный scope.
