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

Before asking for a repair target, resolve the selected accepted package's
existing Stage B registration and show a view over its eligible registered
projections:

```text
PROJECTION_REPAIR
├── Package
│   └── accepted revision-bound package
├── Eligible registered projections
│   ├── PRJ-* identity
│   ├── human-readable name
│   ├── declared artifact path
│   └── current revision/freshness when useful
└── Repair target
    ├── entire selected projection
    └── specific section / presentation issue
```

The list is derived from the selected package and existing projection
registration/lifecycle records; it is not a hardcoded universal list or a new
registry. Only presentation concerns such as language, wording, Markdown,
Mermaid, links, navigation, cross-references, terminology, formatting, and
representation of accepted meaning are eligible. `RF-*`, `CQ-*`, `CQRA-*`,
`BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, STM facts, severity, owners, evidence,
security assumptions, target mechanisms, and lifecycle semantics may appear as
provenance but are never editable repair targets.

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

The user-facing `REVALIDATE` presentation is explicitly read-only for the
restored suite:

```text
REVALIDATE
├── Previous Review Suite [RESTORED / READ-ONLY]
│   ├── Architecture Review state
│   ├── Test Engineering state and outputs
│   └── Code Quality Review state and outputs
├── Previous baseline
├── Current baseline / changed input
├── Change inventory
├── Impact Analysis
├── Minimum affected dependency slice
├── Targeted evidence
├── Revalidation / adjudication
└── Projection Impact Analysis
```

The restored suite is context, not a configuration menu. During ordinary
`REVALIDATE`, do not enable or disable capabilities, change Architecture depth
or endpoint, or select new Test Engineering or Code Quality outputs. Those
changes route to `EXTEND`; `REVALIDATE_DOES_NOT_BECOME_NEW`. Changed-input
classification, dependency impact, affected capabilities/records, evidence
refresh, and projection impact remain automatic and impact-driven.

The user may confirm baseline/change context and any genuinely ambiguous
authority decision. If impact is `SYSTEMIC`, choosing whether to accept
`FULL_REAUDIT_RECOMMENDED` remains an explicit user decision; it does not turn
the restored suite into a new configuration flow.

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

### Code Quality semantic revalidation

For a Code Quality `REVALIDATE`, the shared change inventory is refined through
the direct bindings of accepted `CQ-*`, candidate, and `CQRA-*` records. The
minimum semantic flow is:

```text
changed binding
  → resolve direct CQ dependency edges
  → identify affected CQ/CQRA identities
  → load the minimum affected EV/STM/context slice
  → mark affected accepted findings/actions STALE
  → revalidate and adjudicate only that slice
  → preserve unrelated accepted CQ authority
```

The direct binding categories are:

| Changed input | Affected Code Quality slice |
|---|---|
| file, symbol, or implementation mechanism | findings and candidates bound to that source/mechanism, including move, deletion, or regeneration |
| `EV-*` observation | findings whose evidence binding uses that observation |
| accepted STM fact | findings whose interpretation requires that fact |
| dependency, framework, runtime configuration, feature flag, or build mode | findings that declare the changed input as a material dependency |
| language/framework addendum or applicability revision | interpretations using that addendum or affected applicability decision |
| Architecture or Test Engineering authority | CQ relations and interpretations that explicitly depend on that authority |
| `CQRA-*` completion or semantic-basis change | every linked finding for that action, independently |

This is an evidence-backed dependency slice, not a new generic graph. Direct
owning metadata is authoritative; changed paths, lockfiles, and diffs are
routing context until the relevant dependency is established. An unknown link
requires targeted investigation and cannot be classified as preserved merely
to save work.

The revalidation overlay records at least the changed binding, affected CQ
identities, preserved CQ identities, dependencies inspected, evidence loaded,
and each finding's outcome. For each affected finding, the outcome is one of:

```text
same semantic issue
  → preserve CQ-* identity; revalidate to CURRENT or BLOCKED
issue absent
  → resolve CQ-* only with post-change evidence
materially different mechanism/meaning
  → SUPERSEDE old CQ-* and create a distinct replacement identity
insufficient evidence/context
  → retain lifecycle; set freshness BLOCKED
```

An equivalent refactor, rename, or file move may preserve identity when the
mechanism, consequence, and relevant bindings remain semantically equivalent;
the path change alone neither resolves nor invalidates the finding. A deleted
source binding affects only findings depending on it. Dependency/configuration,
addendum, STM, or related-authority changes affect only records with a material
edge to that input. Unaffected CQ findings and their evidence are reused, not
reconstructed.

`CQRA COMPLETED` marks remediation work complete and causes targeted
revalidation of each linked finding; it never performs a bulk resolution.
`REVALIDATE` remains separate from `RESUME`, `NEW`, and `EXTEND`, and it ends at
semantic adjudication. It does not regenerate projections, register `PRJ-*`,
run `RG-*`, or apply package policy. Any later projection freshness accounting
uses the shared Stage B handoff after the semantic delta is stabilized.

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
