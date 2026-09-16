# Lifecycle and Mermaid

Lifecycle reconstruction is mandatory wherever behavior depends on time, background work, connections, sessions, resources, retry/reconnect, or shutdown. Diagrams are required only when they add architectural information; there is no decorative quota. However, a substantial final report must not omit a visual explanation of material topology, lifecycle, or ownership merely because the writer did not draw one.

## 1. Required lifecycle questions

For every significant process, connection, task, session, or resource, answer:

- who creates it;
- which prerequisites are required;
- who owns it while it is active;
- which states actually exist;
- which events cause transitions;
- what happens on failure;
- who controls retry or reconnect;
- what cancels the work and what the cancellation scope is;
- what happens on logout, reconfiguration, window close, or process shutdown;
- which resources must be released;
- whether multiple instances can accidentally exist;
- what happens to in-flight work when owner or generation changes;
- which completion is stale and how stale completion is suppressed.

Connect these answers to the ownership matrix and adversarial scenarios in `ownership-and-scenarios.md`.

## 2. Choosing diagrams

Create a diagram when it helps prove or explain a material mechanism.

### Architecture flowchart

Show processes/components, state stores, external systems, and trust-relevant boundaries. Do not draw a directory tree.

### Overall lifecycle / state diagram

Use `stateDiagram-v2` when real states and transitions exist. Include failure, recovery, cancellation, and shutdown rather than only the happy path.

### Startup

Show configuration loading, restoration, dependency construction, handler registration, background startup, UI/readiness, and startup failure behavior when material.

### Runtime sequence

Use `sequenceDiagram` with real component names for a material end-to-end flow: initiator → boundaries → side effect → completion/error.

### Background task / retry / reconnect

Show creation, running/waiting, cancellation, retry/backoff, terminal failure, and ownership. If the system has no relevant background work, do not invent a diagram.

### Shutdown

Show rejection of new work where applicable, cancellation/drain/flush, persistence, socket/process/database cleanup, and final exit. Explicitly mark fire-and-forget cleanup and APIs that the runtime may not await.

### Trust boundaries

Show untrusted input and validation/authorization points: UI/native, network, filesystem, external process, plugin, deep link, uploaded content, and similar boundaries.

### Before → After architecture

Use two compact diagrams, or one clearly partitioned diagram, when remediation or target state changes ownership, lifecycle, boundary, ordering, or source of truth. The reader must be able to see not only the new component, but **which problematic dependency disappears**.

### Roadmap dependencies

For a non-trivial dependency graph, show prerequisites, gates, and the safe-activation boundary. Do not draw a purely sequential chain when tasks can actually proceed in parallel.

## 3. Visual coverage contract for final artifacts

For a substantial `STANDARD_FULL` or `FORENSIC` final package, expect the following visual coverage when the corresponding complexity exists in the project:

1. **As-Built component/boundary view** — when multiple material runtime components, processes, or external systems exist.
2. **Material runtime/lifecycle view** — when ordering, ownership, concurrency, retry, startup, or shutdown affects correctness.
3. **Target Architecture view** — when the endpoint includes target state and the target materially changes boundaries, ownership, or flows.
4. **Before → After view** — for a material correction that is difficult to understand from prose alone.
5. **Roadmap dependency view** — when prerequisites or safe activation are non-linear.

This is not a mechanical quota. If an item is not applicable, no diagram is required. But if a substantial report contains complex topology, lifecycle, or target mechanics and no useful diagram, the final writer/reviewer must explicitly justify why visualization would add no information.

Diagrams are part of user-facing explanation. Working artifacts may contain more or fewer visualizations as needed.

## 4. Diagrams must match evidence

Every material arrow or transition must have a confirmed code path or an explicitly marked assumption.

Do not:

- show target behavior as if it were current behavior;
- invent a state merely to make a cleaner FSM;
- hide a race or interleaving by turning concurrent operations into a linear sequence;
- use a diagram as the only evidence for a finding;
- draw generic boxes with no relation to real subsystem names;
- reproduce a directory tree instead of runtime architecture.

## 5. Diagram explanation contract

Every material diagram must be accompanied by a short prose block explaining:

- what the diagram shows;
- which mechanism or risk becomes visible;
- which state is current and which is target;
- which conclusion the reader should draw from it.

Do not insert Mermaid without context or force the reader to infer the meaning of arrows independently.

## 6. Consistency check

Before accepting a document, compare:

```text
prose
↔ ownership matrix
↔ state tables
↔ Mermaid
↔ authoritative findings
```

A mismatch is a consistency issue, not an editorial detail.

## 7. Mermaid render-validation gate

Mermaid in final user-facing artifacts is considered render-validated only after actual parser/render validation when a compatible tool is available in the environment.

Required sequence:

```text
enumerate all final Mermaid blocks
→ assign stable document/location identity
→ validate each block independently
→ record PASS/FAIL per block
→ correct every failed block
→ re-run validation for corrected blocks
→ only then accept diagram gate
```

Suitable tools include `mmdc`, a project-provided Mermaid validator/parser, a documentation build pipeline, or another compatible renderer. Do not bind the Skill to one vendor tool; prefer the toolchain actually used by the project or its Markdown/docs workflow.

If a renderer/parser is available, **actually invoke it**. Visual inspection of source text, a statement that “syntax looks valid”, or validation of only one sample diagram is not executable validation.

If no renderer/parser is available:

- record `MERMAID_RENDER_VALIDATION_UNAVAILABLE`;
- perform the strongest available structural review;
- do not claim that diagram render validation passed;
- state the limitation explicitly in the final verification record.

Any known parser/render failure is a `DIAG-*` issue and blocks `FINAL_PACKAGE_ACCEPTED` until the diagram is corrected and passes re-validation.

For compatibility, prefer simple stable Mermaid syntax. Avoid exotic directives/extensions without necessity and handle special characters, punctuation, multiline labels, and state aliases carefully. Syntax simplification must not change the architectural meaning of the diagram.

## 8. Mermaid quality

- Use simple standard Mermaid syntax.
- Use real subsystem names, not `Service1` or `Component2`.
- Do not encode large code listings in a diagram.
- Label owner/scope where important to understanding.
- Verify that arrows and states reflect the actual path.
- Render validation and semantic consistency are separate gates: a diagram that renders successfully but is technically wrong still fails.