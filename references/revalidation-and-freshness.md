# Revalidation and compact-state freshness

Этот файл является авторитетным контрактом для трёх cross-cutting случаев, подтверждённых pressure validation:

1. projection-only correction не должна автоматически перезапускать technical audit;
2. compact persisted state не может использоваться downstream, если он stale относительно owning accepted authority;
3. отдельный `PROJECTION_REPAIR` intent должен исправлять только пользовательскую проекцию принятого аудита и останавливаться при semantic drift.

Stage B projection identity, verified revisions, fingerprints, freshness
states, and required actions are owned by [Projection lifecycle authority](projection-lifecycle.md).
This file owns the cross-cutting revalidation routing and preserves the
following distinction:

```text
semantic freshness != projection freshness
semantic workflow may finish with stale projections
projection stale != semantic false
```

Не применяй этот контракт для переопределения обычной scope discipline, fresh-context review или As-Built coverage: эти поведения уже покрываются существующими reference contracts.

## 1. Projection-only revalidation

Используй `PROJECTION_REVALIDATION`, когда correction меняет только представление уже принятой технической семантики.

Типичные случаи:

- переписать shorthand в связный русский текст;
- разделить перегруженный абзац;
- исправить heading/table presentation;
- исправить relative link;
- исправить Mermaid syntax/renderability без изменения изображённого механизма;
- уточнить формулировку уже принятого target/roadmap механизма без изменения owner, invariant, dependency или activation behavior.

Для такого correction/re-review минимальный вход:

```text
issue id
artifact + changed section
before/after or enough surrounding context
current accepted technical authority refs
immutable accepted semantics relevant to the changed section
```

Fresh-context означает независимое judgement, а не обязательный полный reread. При `PROJECTION_REVALIDATION` reviewer по умолчанию проверяет changed range + достаточный surrounding context + current accepted authority refs.

Не открывай заново source repository и не перезапускай As-Built verification, candidate verification, root adjudication, severity adjudication или Target technical review только потому, что correction/re-review fresh-context.

Если во время projection review обнаружено реальное противоречие, которое нельзя разрешить без изменения принятой технической семантики, верни:

```text
TECHNICAL_REVALIDATION_REQUIRED
```

## 1.1 `PROJECTION_REPAIR` session flow

`PROJECTION_REPAIR` — orchestration intent для повторного входа в уже принятый audit package, когда пользователь хочет исправить только качество финальных/пользовательских документов.

Он использует `PROJECTION_REVALIDATION` как validation mechanism, но отличается от обычного editorial correction loop тем, что является отдельным startup intent и может быть выбран позже, уже после `COMPLETE`.

Предусловия:

```text
accepted audit package exists
accepted technical authority is reusable and revision-bound
selected project baseline has no unresolved source change requiring REVALIDATE
requested work is presentation/projection-only
```

Минимальный flow:

```text
PROJECTION_REPAIR
→ identify requested/broken final projections
→ bind each projection to current accepted authority refs
→ build projection issue list
→ repair only allowed presentation surface
→ validate links/Markdown/terminology/Mermaid/reference consistency
→ PROJECTION_REVALIDATION per changed projection
→ PROJECTION_REPAIR_COMPLETE | TECHNICAL_REVALIDATION_REQUIRED
```

Разрешённая область включает:

- язык, грамматику и читаемость;
- структуру заголовков и секций;
- Markdown tables/lists/navigation;
- relative links и cross-links;
- orphan/malformed references к уже существующим RF/SER/TASK/target identifiers;
- дубликаты и stale presentation, если current accepted authority однозначно указывает замену;
- Mermaid syntax/renderability и layout без изменения изображённого accepted mechanism;
- согласование терминологии и названий между финальными документами;
- пересборку summary/index/navigation как projection accepted authority.

Не разрешено без возврата в technical gate:

- менять evidence;
- менять root identity/boundary;
- менять severity/exploitability;
- менять owner или lifecycle/target invariant;
- менять product-intent status;
- менять finding disposition;
- добавлять новый finding/root/target mechanism;
- менять roadmap prerequisite/dependency/gate;
- менять security assumption или safe-activation semantics;
- скрывать source/baseline changes, которые требуют `REVALIDATE`.

Для каждого изменённого artifact/section зафиксируй:

```text
artifact
changed_section_or_range
projection_issue_ids
accepted_authority_refs
validation_checks
projection_revalidation_result
```

Projection-level verification выбирается по изменению, но включает применимые проверки:

- relative links resolve;
- Markdown structure coherent;
- identifiers/references exist and point to current accepted authority;
- no stale/superseded projection survives;
- terminology/language consistent;
- Mermaid blocks parse/render when compatible tooling is available;
- final status/summary wording remains consistent with accepted technical gates.

Если совместимый Mermaid validator/renderer отсутствует, сохрани `MERMAID_RENDER_VALIDATION_UNAVAILABLE`; не называй render validation успешной.

Успешный projection repair возвращает:

```text
PROJECTION_REPAIR_COMPLETE
technical_semantics_changed: false
technical_gates_reopened: false
```

Это не означает fresh technical verification. Project baseline не меняется только потому, что review-документы были исправлены.

## 2. Semantic drift gate

Projection-only writer не имеет права менять:

- evidence;
- root identity/boundary;
- severity or exploitability;
- owner;
- lifecycle/target invariant;
- roadmap prerequisite/dependency/gate;
- security assumption;
- safe-activation semantics.

Если changed prose/table/diagram расходится с принятой технической семантикой, re-review возвращает:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

Не исправляй technical authority или compact projection так, чтобы они молча совпали с новой prose. Возвращай изменение в owning technical gate.

## 3. Compact persisted state is a projection, not authority

`INDEX.md`, `HANDOFF SUMMARY`, native plan UI и любые compact semantic/fingerprint records помогают route/resume workflow, но не заменяют accepted owning technical artifact.

Если compact record используется downstream как semantic shortcut, он обязан содержать минимум:

```text
owning_artifact
owning_artifact_revision
owning_authority_status
projection_status: VALID | REVALIDATION_REQUIRED | SUPERSEDED
```

`VALID` compact projection usable downstream только когда одновременно выполнено:

```text
owning_authority_status == COMPLETE
owning_artifact_revision == current accepted owning artifact revision
projection_status == VALID
```

Если owning artifact был corrected/revalidated или его accepted revision изменился, старый compact projection нельзя продолжать считать `VALID`.

Переход:

```text
VALID
→ REVALIDATION_REQUIRED
→ VALID(new revision) | SUPERSEDED
```

## 4. Downstream freshness gate

До dispatch, который собирается полагаться на compact semantic state вместо чтения owning authority, coordinator/reviewer проверяет revision/status binding.

При mismatch, unknown revision или конфликте INDEX/handoff/compact record с accepted owning artifact:

```text
AUTHORITY_RECONCILIATION_REQUIRED
```

Downstream dispatch на stale semantics запрещён до reconciliation.

Reconciliation должна восстановить minimum current authority, обновить/invalidated compact state и только затем продолжить workflow.

Не создавай `VALID` compact semantic state из owning authority в статусе:

```text
REVIEW_REQUIRED
CORRECTION_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
```

## 4.1 Context Orchestration v0.3

Canonical principle:

```text
Load the minimum fresh authoritative evidence needed for the current decision.
```

Optimization is subordinate to correctness and freshness; a shorter or newer
projection is never substantive authority merely because it is compact.

Routing context decides where to look and may contain `INDEX`, handoffs,
registries, candidate/evidence pointers, materiality/coverage projections, and
revision bindings. Decision evidence supports a substantive claim and includes
owning code/configuration, the accepted owning artifact, exact authority/contract
evidence, and targeted runtime/test evidence. Routing context is not proof when
owning evidence is required.

Progressive retrieval is:

```text
structure/inventory
→ materiality map
→ evidence pointers
→ targeted reads
→ deeper reads only for unresolved material questions
```

Do not blanket-preload all references, working artifacts, or repository contents.
If a bounded review discovers a material omitted cross-boundary path, record
`CONTEXT_EXPANSION_REQUIRED`, inspect that path, and preserve the reason and exact
evidence pointer.

Dependency-sliced capability/subagent dispatch records:

```text
exact baseline/revision
exact mission/scope
forbidden scope
accepted dependency artifact pointers + revisions
required shared/reference contracts
output path
HANDOFF SUMMARY contract
```

Unrelated accepted artifacts are excluded by default. Expansion requires a
concrete correctness trigger and is persisted in the handoff.

## 5. Resume

При resume compact routing state сначала проверяется на freshness относительно referenced owning authority. Сам факт того, что запись находится в более новом файле, INDEX или handoff, не делает её свежей.

Если freshness нельзя установить без чтения owning artifact, прочитай только необходимую authority и выполни reconciliation. Не перезапускай уже принятый audit целиком.

## 6. Pressure-regression mapping

Этот контракт существует для подтверждённых baseline gaps:

- PS-41 → `PROJECTION_REVALIDATION` предотвращает source/technical-gate restart для presentation-only correction;
- PS-42B → revision/status binding блокирует stale compact projection до downstream dispatch;
- PS-80 → `PROJECTION_REPAIR` делает projection-only repair first-class startup intent и сохраняет semantic drift gate.

PS-39, PS-40 и PS-43 были baseline-compliant и не являются основанием для добавления новых orchestration restrictions.

## 7. Project-change targeted revalidation

After the semantic delta reaches a stabilized accepted state, projection
freshness is accounted for by [Projection impact accounting](projection-impact.md).
That pass consumes revision-bound semantic identities, selector resolution
snapshots, and contract revisions; changed paths remain routing context rather
than semantic proof. It persists direct impact and reverse-graph propagation
before any separately requested regeneration. A successful pass returns
`PROJECTION_IMPACT_ACCOUNTED`, which means impact is recorded, not that all
projections are `CURRENT`. If accounting fails technically, accepted semantic
authority is not rolled back, but projection-sensitive gates remain blocked
until the impact record is durably reconciled.

This is one explicit post-semantic handoff per stabilized delta for `REVALIDATE`.
The equivalent handoff is used at the end of `NEW` and `EXTEND` after their
semantic work has stabilized. A retry after technical accounting failure is
reconciliation under the idempotent impact rules, not implicit regeneration.
No intent may turn Projection Impact Analysis into a content writer or start an
`RG-*` session without a separate explicit output/package freshness request.

`REVALIDATE` binds the previous accepted baseline to the selected current
baseline and produces a bounded, delta-oriented overlay:

```text
BASELINE_BINDING
→ CHANGE_INVENTORY
→ IMPACT_ANALYSIS
→ IMPACT_CLASSIFICATION
→ MINIMUM_DEPENDENCY_SLICE
→ TARGETED_FRESH_EVIDENCE
→ REVALIDATION / ADJUDICATION
→ DELTA_RECONCILIATION
```

Git diff, changed paths, and Project Profile delta are routing context only.
They select where fresh evidence is needed; they are not substantive proof.

For STM and dependent capability/projection artifacts, refine `IMPACT_ANALYSIS`
through the dependency contract:

```text
changed source/baseline
-> affected EV/STM candidates
-> affected direct dependencies/aspects
-> impact traversal
-> only affected capability semantics/projections
```

Generated indexes locate candidate reverse edges, but owning direct dependency
metadata remains authoritative. `HARD`, `CONDITIONAL`, and `INFORMATIONAL`
routes, selector dependencies, and bounded context traversal are defined in
`technical-model-dependencies.md`. Unknown linkage requires targeted
investigation and cannot be marked preserved.

### Impact classification

`LOCAL`, `BOUNDARY`, and `SYSTEMIC` are orchestration labels, not finding
severity. `LOCAL` means no demonstrated material boundary, contract, or
ownership change; fresh reads stay local unless evidence expands the scope.
`BOUNDARY` means a material API, auth/trust, persistence, ownership, lifecycle,
concurrency, IPC, external integration, or equivalent accepted boundary is
touched; revalidate that boundary and its material dependencies. `SYSTEMIC`
means multiple fundamental boundaries or the accepted architecture model changed
enough that targeted completion is not trustworthy.

For `SYSTEMIC`, emit:

```text
FULL_REAUDIT_RECOMMENDED
reason: <why targeted scope is insufficient>
systemic_scope: <affected fundamental boundaries>
user_decision_required: true
```

Do not start a full audit until the user chooses it. If the user declines,
finish with the systemic scope and unresolved items explicit; do not claim a
fully revalidated audit.

### Affected and preserved sets

Impact analysis records affected architecture domains, accepted findings,
candidate/evidence bindings, capabilities, and dependent artifacts, along with
preserved accepted domains. An accepted domain is `preserved` only when the
available dependency/evidence mapping finds no dependency requiring fresh
verification. Unknown linkage requires targeted investigation and cannot be
called preserved for context savings.

Unrelated accepted artifacts are excluded by default. If a material omitted
dependency is discovered, persist:

```text
CONTEXT_EXPANSION_REQUIRED
correctness_trigger: <exact reason>
requested_expansion: <minimal dependency slice>
evidence_pointer: <path/authority pointer>
affected_decision_or_domain: <decision/domain>
```

Then inspect only that required dependency slice. Do not silently broaden the
context or refuse a material cross-boundary read merely to protect a budget.

### Delta reconciliation

The revalidation overlay/artifact contains at minimum:

```text
source_audit_revision
previous_baseline
current_baseline
change_range
impact_classification
changes_investigated
context_expansions
previous_accepted_evidence_preserved
findings_revalidated
findings_resolved
findings_still_valid
findings_changed
new_findings
capability_impacts
unresolved_items
```

Link this overlay to the previous authoritative review rather than regenerating
the entire report by default. `previous_accepted_evidence_preserved` means the
impact analysis found no dependency requiring fresh verification. It does not
mean freshly reread, runtime tested, independently reviewed, or newly proven.

### Test Engineering source-view routing

Test Engineering records concrete revision bindings for each accepted BC and
CC. A service and consumer may therefore have independent baselines:

```text
BC-042.source_bindings:
  architecture_revision
  declared_revision
  implementation_revision
  consumer_revision

CC-017.compared_views:
  declared_revision
  implementation_revision
  consumer_revision
  tested_revision
```

For a changed binding, route only the affected view and dependent slice:

```text
tests-only change
  → revalidate affected TM/MAT/GAP
  → BC remains valid unless independent semantic evidence says otherwise

implementation or declared-contract change
  → revalidate affected IMPLEMENTED/DECLARED views
  → run CC/BC impact analysis

consumer-only change with unchanged service repository
  → revalidate affected CONSUMED views
  → revalidate consumer-facing simulator/E2E projections as needed
```

A file/path diff is routing context, not semantic proof. Do not restart the
whole Test Engineering package or unrelated architecture review without impact
evidence.
