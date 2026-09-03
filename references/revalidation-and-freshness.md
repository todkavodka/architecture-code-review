# Revalidation and compact-state freshness

Этот файл является авторитетным контрактом для двух cross-cutting случаев, подтверждённых pressure validation:

1. projection-only correction не должна автоматически перезапускать technical audit;
2. compact persisted state не может использоваться downstream, если он stale относительно owning accepted authority.

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

Этот контракт существует только для подтверждённых baseline gaps:

- PS-41 → `PROJECTION_REVALIDATION` предотвращает source/technical-gate restart для presentation-only correction;
- PS-42B → revision/status binding блокирует stale compact projection до downstream dispatch.

PS-39, PS-40 и PS-43 были baseline-compliant и не являются основанием для добавления новых orchestration restrictions.
