# Справочник workflows

Каждый Session Intent описан в одинаковой форме: назначение, условия входа, пользовательские решения, автоматические действия, чтение/запись состояния, gates, stop conditions и postconditions.

## `NEW`

**Назначение:** создать новый review package на выбранном baseline.

**Entry conditions:** нет пригодного accepted/in-progress package для текущей задачи либо пользователь явно запросил новый audit.

**User choices:**

- baseline, если он неоднозначен;
- capabilities;
- Architecture depth/endpoint, если Architecture выбрана;
- user-facing outputs Test Engineering/Code Quality.

**Automatic:** repository/profile discovery, persistent STM bootstrap, dependency resolution, capability orchestration, impact accounting.

**Reads:** repository, previous audit discovery metadata, applicable contracts.

**Writes:** `working/INDEX.md`, evidence, STM, selected capability semantics, projection/package state.

**Gates:** capability-specific technical gates, Projection Impact Analysis, package policy.

**Stops:** ambiguous baseline/authority, insufficient evidence, blocked dependency, failed required review gate.

**Postcondition:** accepted semantic state for selected scope; projections may still be `STALE` unless package requires current deliverables.

---

## `RESUME`

**Назначение:** продолжить незавершённый persisted workflow.

**Entry conditions:** package имеет unfinished durable boundary.

**User choices:** подтвердить package/baseline reconciliation при реальной неоднозначности.

**Automatic:** validate INDEX against owning artifacts, restore Review Suite read-only, find first non-accepted durable boundary.

**Reads:** `INDEX.md`, owning artifacts/revisions, handoffs, relevant dependencies.

**Writes:** continued workflow state and newly completed artifacts.

**Gates:** freshness/authority reconciliation before substantive continuation.

**Stops:** stale/contradictory compact state, missing owning artifact, changed baseline requiring reconciliation.

**Postcondition:** workflow продолжается без повторного выполнения уже accepted unrelated work.

**Нельзя:** использовать `RESUME` как новый capability/output configurator. New scope → `EXTEND`.

---

## `REVALIDATE`

**Назначение:** повторно проверить только semantic state, затронутый изменением accepted baseline или dependencies.

**Entry conditions:** существует accepted package и новый current baseline/change context.

**User choices:** подтвердить baseline/change context; принять решение при genuinely ambiguous authority; решить, принимать ли `FULL_REAUDIT_RECOMMENDED` при `SYSTEMIC` impact.

**Read-only context:** previous Review Suite configuration.

**Automatic:**

```text
CHANGE_INVENTORY
IMPACT_ANALYSIS
IMPACT_CLASSIFICATION
MINIMUM_DEPENDENCY_SLICE
TARGETED_FRESH_EVIDENCE
REVALIDATION / ADJUDICATION
DELTA_RECONCILIATION
Projection Impact Analysis
```

**Reads:** previous accepted authority, dependency metadata/indexes, current changed sources.

**Writes:** revalidated/superseded semantic records, impact state, projection freshness accounting.

**Impact classes:** `LOCAL | BOUNDARY | SYSTEMIC`.

**Stops:** unknown linkage requiring targeted investigation; disputed required fact; systemic impact without user decision; technical accounting failure blocks projection-sensitive gate.

**Postcondition:** affected state reconciled; unaffected accepted state preserved where dependency evidence supports preservation.

**Нельзя:** добавлять capabilities/outputs как часть ordinary `REVALIDATE`. New work → `EXTEND`.

---

## `EXTEND`

**Назначение:** добавить capability, output или Architecture endpoint к accepted package без повторного выполнения unrelated accepted work.

**Entry conditions:** accepted reusable package exists.

**User choices:** only available additions.

**Presentation:**

```text
Existing / preserved [READ-ONLY]
Available additions [USER SELECTABLE]
```

**Automatic:** required dependency closure, targeted backfill/revalidation, impact accounting.

**Reads:** accepted capability registry, owning artifacts, freshness/dependency state.

**Writes:** union of previous selection + explicit additions + structural prerequisites.

**Architecture rules:**

- absent capability → may add and select depth/endpoint;
- existing depth remains read-only;
- endpoint extension is monotonic:
  `REVIEW_ONLY -> TARGET -> TARGET+ROADMAP`.

**Stops:** requested addition requires changing accepted semantics rather than additive work; prerequisite unavailable/blocked.

**Postcondition:** accepted package extended without deleting prior accepted selections.

---

## `USE_EXISTING`

**Назначение:** consume existing accepted result без новой technical work.

**Entry conditions:** accepted reusable package exists; baseline/authority/projection requirements suitable for requested consumption.

**User choices:** package/deliverable if several valid choices exist.

**Automatic:** validate package, authority bindings, projection registration/freshness and gate policy.

**Reads:** accepted package and projection lifecycle metadata.

**Writes:** только metadata reconciliation, если contract это допускает; substantive semantic work не создаётся.

**Stops:** requested deliverable stale/blocked under required policy; source change requires `REVALIDATE`; requested new output requires `EXTEND`.

**Postcondition:** existing accepted deliverable consumed.

---

## `PROJECTION_REPAIR`

**Назначение:** исправить представление accepted meaning без изменения semantic authority.

**Entry conditions:** accepted revision-bound package; нет unresolved source change requiring `REVALIDATE`; requested change presentation-only.

**User choices:** eligible registered `PRJ-*` projection, document/section/presentation issue.

**Automatic:** authority binding, presentation validation, `PROJECTION_REVALIDATION`.

**Reads:** selected projection record, current accepted authority refs.

**Writes:** corrected projection + projection verification/lifecycle state.

**Allowed changes:** language, Markdown, Mermaid syntax/layout, links, navigation, tables, terminology, cross-references, representation of accepted meaning.

**Stops:** semantic drift.

Return:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

**Postcondition:** repaired projection; technical semantics and technical gates unchanged.

---

## `RG-*` regeneration

`RG-*` не является Session Intent.

**Назначение:** пересобрать requested stale projection/package from accepted authority.

**Entry:** explicit fresh-output request.

**Automatic:** resolve stale prerequisites, freeze execution scope, generate, verify, fingerprint/revision decision.

**Stops:** missing/blocked semantic prerequisite, projection contract failure, failed verification.

**Postcondition:** requested projection becomes `CURRENT` only after required verification.

---

## Общие routing invariants

```text
RESUME != NEW
REVALIDATE != NEW
REVALIDATE != regeneration
PROJECTION_REPAIR != semantic remediation
EXTEND preserves accepted selection
USE_EXISTING creates no new scope
```

## См. также

- [Reuse and Change Guide](../guides/reuse-and-change.md)
- [Lifecycle and Freshness](../concepts/lifecycle-and-freshness.md)
- [Troubleshooting](../operations/troubleshooting.md)
