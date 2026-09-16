# Remediation Roadmap and Execution-Consistency Review

This stage runs only for `REVIEW_PLUS_TARGET_AND_ROADMAP` and only after Target Architecture has been accepted.

## 1. Build the roadmap from dependencies, not severity

Severity helps prioritize risk, but implementation order is determined by prerequisites and safe activation.

Every material task must contain two layers: first a human-readable explanation of the architectural problem and intended result, then an implementation contract.

### 1.1 Human-readable task layer

Before listing files, tests, prerequisites, or rollback details, every material task explains:

1. **Problem.** What currently behaves incorrectly or unreliably.
2. **Why it happens.** Which ownership, lifecycle, boundary, or state mechanism causes it.
3. **Practical consequence.** Which runtime, security, reliability, or testability effect occurs.
4. **What must change.** Which target mechanism is introduced or which responsibility moves.
5. **Why this closes the root cause.** Which causal link disappears after the change.
6. **What the system gains.** How observable system behavior changes after remediation.

Write the human-readable layer as connected prose. For material explanatory prose, follow the rule **one primary mechanism per paragraph**: one paragraph may contain evidence and consequences of one mechanism, but it must not explain several independent root causes at the same time.

Explain a specialized term in plain language before using it as shorthand when its meaning is not obvious from context. Do not turn the text into a glossary and do not translate exact identifiers.

**Technical shorthand is not an explanation.** Terms such as `eager startup`, `registered shutdown`, `drain+close`, `in-flight`, `producer-miss`, or `single-flight` may be precise, but the reader must first understand which observable system behavior they denote.

Transformation pattern:

```text
Poor:
NATS gets eager startup + registered shutdown + drain.

Better:
At startup the application checks NATS availability before declaring itself
ready. If the connection cannot be established, startup fails instead of
publishing a false-ready state. During shutdown the application first lets
already-started operations finish and only then closes the connection. After
that explanation, the behavior may be referred to briefly as fail-fast startup
and graceful drain.
```

The exact wording of the example is non-normative. The normative ordering is:

```text
mechanism explanation → specialized term
```

If a change materially alters topology, ownership, lifecycle, ordering, or a trust boundary, add a Before → After Mermaid/flow diagram or link to the corresponding target diagram.

Do not start a task with class, registry, or function names. The reader must first understand why the task exists.

A material task title must be human-readable and describe the intended result. Do not put `[prereq: ...]`, RF/SER metadata, or other execution metadata in the title. That information belongs in the technical contract.

### 1.2 Implementation contract

After the human-readable layer, **always** create a dedicated subsection whose heading means “Implementation Contract” in the selected user-facing language.

For Russian output, the exact heading remains:

```markdown
### Технический контракт реализации
```

For another user-facing language, use the natural equivalent while preserving the same document boundary and semantics.

Only after this boundary should the roadmap place:

```text
TASK ID
RF/SER addressed
target mechanism
prerequisites
invariant transition
regression test first where applicable
allowed implementation boundary
forbidden scope
verification
exit criteria
rollback/fail-closed consideration where relevant
```

Prefer a table or another clearly reference-oriented block. Implementation details must be precise, but they do not replace explanatory prose.

Example structure for Russian output:

```markdown
## TASK-F — Сделать жизненный цикл NATS управляемым

### Что сейчас не так
<connected prose>

### Почему это происходит
<ownership/lifecycle mechanism>

### Практическое последствие
<runtime consequence>

### Что предлагаем изменить
<target mechanism described in natural language first>

### Почему это закрывает корневую причину
<causal explanation>

### Что получим после исправления
<observable resulting behavior>

### Технический контракт реализации

| Параметр | Требование |
|---|---|
| Связанные замечания | RF-F |
| Целевой механизм | `CacheLifecycleManager` |
| Зависимости | Нет |
| Инвариант | ... |
| Регрессионные тесты | ... |
| Допустимая область изменений | ... |
| Запрещённая область | ... |
| Проверка | ... |
| Критерий завершения | ... |
| Откат / безопасная активация | ... |
```

Equivalent table contents are allowed, but the dedicated Implementation Contract boundary is mandatory for every material roadmap task.

An unresolved product or deployment decision blocks only the tasks that depend on it.

## 2. Semantic invariant → concrete representation

The roadmap must translate target semantics into a real runtime representation.

Check, for example:

- semantic composite key vs equality semantics of the concrete language, Map, or dictionary;
- generation/version identity vs mutable object reference;
- cancellation scope vs a global abort primitive;
- ownership model vs actual storage/index keys;
- durable idempotency vs process-local memory.

A well-designed semantic type does not guarantee correct runtime behavior.

## 3. Dependency isolation

Do not create a global phase gate when a decision affects only a few tasks.

Acceptable:

```text
Decision D2
→ blocks TASK-61 only

Independent TASK-31/32
→ may proceed
```

Not acceptable: the entire phase is blocked by every decision merely “for simplicity”.

## 4. Safe activation boundary

For security, ownership, and lifecycle changes, define the allowed intermediate state explicitly.

Examples of risk:

- a fake verifier exists before production trust authority and accidentally enables execution;
- a new authorization path is enabled before identity/state migration;
- a new cancellation protocol is partly activated while the old global cancellation path remains active;
- signing or checksum enforcement is enabled inconsistently.

If no safe intermediate combination exists, activate dependent production pieces atomically or preserve fail-closed / old-safe behavior until full cutover.

A test fake or fixture never becomes production trust authority.

## 5. Execution Consistency Review

A fresh-context reviewer checks the chain:

```text
semantic invariant
→ concrete runtime representation
→ dependency isolation
→ safe production activation boundary
```

The reviewer also checks that:

- the task covers an actual RF, SER, or target requirement rather than introducing new scope;
- the task title communicates the engineering goal without bracketed prerequisite metadata;
- the human-readable layer explains the current problem, root mechanism, consequence, and target result;
- material paragraphs do not mix multiple independent root mechanisms;
- specialized shorthand is not used instead of explanation;
- every material task contains the dedicated Implementation Contract heading in the selected user-facing language;
- execution metadata appears after that heading;
- the regression test actually checks the mechanism;
- dependencies are acyclic or explicitly explainable;
- the task boundary is small enough for independent review;
- a product decision is not hidden as an implementation detail;
- platform and deployment constraints are accounted for;
- rollback or fail-closed behavior is defined for risky activation;
- a Before/After diagram is present when a material ownership or lifecycle transition is otherwise difficult to understand;
- Mermaid diagrams included in the final roadmap pass the render-validation gate from `lifecycle-and-mermaid.md`.

## 6. Review lifecycle

```text
roadmap author
→ self-check
→ fresh-context execution-consistency review
→ ROADMAP_ACCEPTED
   or ROADMAP_CORRECTION_REQUIRED
      → separate correction pass
      → fresh-context re-review
      → ACCEPTED | BLOCKED
```

The reviewer produces issues rather than editing the roadmap directly.

## 7. Acceptance

The roadmap is accepted only when:

- all material RF/SER target coverage is traceable;
- material task titles are human-readable and free of bracketed execution metadata;
- tasks contain a human-readable problem/result explanation and a concrete implementation contract;
- every material task contains the dedicated Implementation Contract boundary before execution metadata;
- specialized shorthand does not replace mechanism explanation;
- tasks define a concrete representation and verification;
- independent tasks are not blocked by unrelated gates;
- unsafe intermediate activation is prevented;
- unresolved decisions are isolated;
- correction/re-review history is preserved;
- executable sections contain no `TBD`, `TODO`, or `implement later` placeholders;
- dense internal shorthand does not replace an explanation of what the task solves and why;
- roadmap explanatory prose has no known paragraph-overload issues;
- every final roadmap Mermaid diagram satisfies the diagram render-validation contract.