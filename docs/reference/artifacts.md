# Справочник артефактов

Этот документ описывает persistent artifacts audit package с точки зрения человека: роль, ownership, создание, обновление, freshness и потребителей.

> Нормативная schema каждого объекта находится в `references/` и capability contracts. Этот справочник объясняет её назначение и практическое использование.

## 1. `working/INDEX.md`

**Роль:** coordinator workflow authority.

**Владелец/writer:** coordinator.

**Потребители:** startup routing, `RESUME`, `REVALIDATE`, `EXTEND`, handoff logic.

**Создаётся:** при `NEW` или reconciliation legacy package.

**Обновляется:** при изменении process/routing state, capabilities, gates, handoffs, blockers и package/projection routing.

**Не хранит:** substantive STM facts, findings и другой semantic meaning как единственный source of truth.

Типовые разделы:

```text
repository/baseline
session_intent
review_suite
current phase
execution plan
artifact registry
capability registry
coverage summaries
handoffs
blockers
revalidation state
projection/package routing
```

Если `INDEX.md` расходится с owning accepted artifact, downstream substantive work требует reconciliation.

---

## 2. `WS-*` — workset

**Роль:** physical grouping одного bounded investigation.

**Владелец:** Shared Evidence layer.

**Writer:** один active writer на workset.

**Потребители:** STM и capabilities.

**Создаётся:** когда требуется fresh investigation, которое полезно адресовать/переиспользовать.

**Минимальная информация:**

```text
id
name
scope
baseline
baseline_type
status
investigated_sources
limitations
EV records
HANDOFF SUMMARY
```

**Update rule:** исторический workset не переписывается под новый baseline так, чтобы старое evidence выглядело current.

---

## 3. `EV-*` — observation

**Роль:** адресуемое baseline-bound observation.

**Физическое размещение:** обычно внутри `WS-*`.

**Типичная identity:**

```text
WS-012-payment-retry#EV-003
```

**Required content:**

```text
id
source_type
repository path or external locator
symbol/range when available
baseline binding
observed fact/behavior
optional short excerpt
```

**Не является:** finding, severity decision, remediation или accepted STM fact.

---

## 4. STM facts

**Роль:** persistent shared factual authority.

**Владелец/writer:** Technical Model Gate.

**Потребители:** Architecture Review, Test Engineering, Code Quality Review, projections.

**Families:**

```text
COMP-*  component/runtime unit
IF-*    interface
INT-*   interaction
DS-*    data store
EVENT-* event/message
FLOW-*  material flow
AUTH-*  auth/trust boundary
CFG-*   configuration fact
ERR-*   error/failure contract
```

**Minimum semantic properties:** stable ID, revision, baseline, status, freshness, provenance refs, relations, relevant dependency metadata.

**Lifecycle:**

```text
CANDIDATE -> UNDER_REVIEW -> ACCEPTED -> SUPERSEDED | REJECTED
```

**Freshness:**

```text
VALID | REVALIDATION_REQUIRED | UNKNOWN
```

**Revision rule:** та же semantic identity → новая revision; новая semantic identity → новый ID + supersession link.

---

## 5. `RF-*` — Architecture finding

**Роль:** принятый architecture/root finding.

**Владелец:** Architecture Review.

**Создаётся:** после evidence/STM-backed discovery, independent verification и root-boundary adjudication.

**Typical fields:** identity, scope, root boundary, supporting refs, material consequence, severity, relationships/supersession.

**Потребители:** architecture report, Target Architecture, Remediation Roadmap, `REVALIDATE`.

**Не является:** raw observation или generic code smell.

---

## 6. Test Engineering records

### `BC-*`

**Роль:** одно независимо проверяемое существенное поведение.

**Потребители:** assurance targets, contract verification, simulator/E2E design.

### `CC-*`

**Роль:** inconsistency/adjudication record между DECLARED / IMPLEMENTED / CONSUMED / TESTED.

**Создаётся:** только при material contract question.

### `MAT-*`

**Роль:** material assurance target — что должно быть доказано test evidence.

### `TM-*`

**Роль:** mapping assurance target к executable test evidence и verdict.

### `GAP-*`

**Роль:** отсутствующее/частичное/недостаточное доказательство.

### `TASK-*`

**Роль:** Test Engineering remediation work.

**Ключевой boundary:** эти records не являются вариациями одного finding. Они отвечают на разные вопросы.

---

## 7. `CQ-*` — Code Quality finding

**Роль:** accepted material implementation-quality finding.

**Владелец:** Code Quality Review.

**Создаётся:** после evidence-backed chain `observation -> candidate -> interpretation -> material consequence -> accepted finding`.

**Typical data:** mechanism, evidence/provenance, consequence, severity, confidence, applicability/disposition, relationships, freshness.

**Не создаётся автоматически из:** lint warning, metric threshold, smell.

---

## 8. `CQRA-*` — Code Quality remediation action

**Роль:** remediation action для одного или нескольких `CQ-*`.

**Lifecycle:** capability-owned.

**Critical rule:**

```text
CQRA COMPLETED != CQ RESOLVED
```

Finding требует revalidation evidence.

---

## 9. `PRJ-*` — projection record

**Роль:** stable identity derived human-readable/operational projection.

**Владелец:** capability/endpoint, который публикует projection contract.

**Typical fields:**

```text
projection_id
owner
artifact_path
semantic_dependencies
projection_dependencies
contract_revision
verified_revision
fingerprint
freshness
```

**Freshness:** `CURRENT | STALE | BLOCKED`.

**Update trigger:** semantic/dependency/contract impact или explicit regeneration.

**Authority:** projection не становится semantic authority.

---

## 10. `RG-*` — regeneration session

**Роль:** frozen execution record пересборки projections.

**Создаётся:** только по explicit request свежего deliverable/пакета.

**Не является:** Session Intent, capability semantic state или finding.

**Typical content:** requested scope, resolved dependencies, execution plan, generation result, verification/fingerprint outcome.

---

## 11. Projection package

**Роль:** named deliverable scope для closeout gate.

**Owner:** capability/endpoint declaration.

**Contract:**

```text
package_id
owner
gate
freshness_policy
required_members
optional_members
conditional_members
```

**Resolved snapshot:** фиксируется перед gate и содержит конкретные `PRJ-*` revisions.

**Не является:** global projection registry или semantic authority.

---

## 12. Generated indexes

**Роль:** lookup/routing/dependency traversal.

**Writer:** generator/owning projection process согласно contract.

**Потребитель:** coordinator и bounded capability dispatch.

**Authority boundary:** generated index не заменяет owning direct metadata/semantic artifact.

Если index stale/ambiguous, требуется чтение owning authority и reconciliation.

---

## 13. Recommended package layout

Физический layout может адаптироваться к repository convention. Концептуально:

```text
docs/reviews/architecture-review/
  final reports / selected outputs
  working/
    INDEX.md
    evidence/
      INDEX.md
      WS-*.md
    technical-model/
      INDEX.md
      coverage.md
      components/
      interfaces/
      interactions/
      data-stores/
      events/
      flows/
      auth/
      errors/
      configuration/
    projections/
      registry.md
      impact.md
      sessions/RG-*.md
    capability-specific working state
```

Имена директорий менее важны, чем stable identity, ownership, revision binding и provenance.

## 14. Reading rules

Для быстрого понимания состояния:

```text
working/INDEX.md
```

Для substantive decision:

```text
INDEX -> owning semantic artifact -> WS#EV -> raw source
```

Для user-facing consumption:

```text
main report/summary -> supporting records as needed
```

## См. также

- [Identifiers and Statuses](identifiers-and-statuses.md)
- [Authority and Provenance](../concepts/authority-and-provenance.md)
- [Outputs](outputs.md)
