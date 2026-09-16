# Architecture and Code Review Method

This file defines the shared evidence-first review method. Modes, statuses, and `INDEX.md` are defined in `review-modes-and-orchestration.md`; ownership and scenarios in `ownership-and-scenarios.md`; boundary dimensions in `boundary-contract-audit.md`; and proof of discovery completeness in `discovery-coverage.md`.

## 1. Reconstruct the factual system before judging it

Read repository-local instructions, manifests and lockfiles, CI configuration, packaging/deployment, configuration, tests, service definitions, and current architecture documents. Record the exact repository path, branch/ref, commit, and working-tree state.

Do not infer architecture from directory names. Trace real entry points, object/service construction, state ownership, boundaries, and side effects.

## 2. Factual STM and the As-Built projection are the first major result

Before deep thematic discovery, collect or revalidate the required Shared Evidence and Shared Technical Model (STM) facts. Accepted, sufficiently fresh STM — not As-Built prose — is the factual technical authority. A full Architecture Review first requires a `FULL` STM and `TECHNICAL_MODEL_COVERAGE_ACCEPTED` according to `technical-model-coverage.md`.

Then build the human-readable As-Built projection from accepted, sufficiently fresh STM plus Architecture-oriented synthesis. It should let a technical lead understand the system without reopening the source tree. For a medium-sized project, useful depth often resembles a substantial 5–10 page chapter, but acceptance is based on content rather than page count.

Where applicable, cover:

1. system purpose and key scenarios;
2. deployment topology and runtime components/processes;
3. state ownership, lifecycle, and authority;
4. API, IPC, process, persistence, trust, and deployment boundaries;
5. command/write, read/query, asynchronous/background, and external-integration flows;
6. state machines and lifecycle transitions;
7. startup/readiness/shutdown, cancellation, retry, and recovery;
8. concurrency, shared state, serialization, and idempotency;
9. failure domains and partial failure;
10. authentication/authorization and trust contracts;
11. configuration and secrets;
12. persistence, migrations, and consistency;
13. observability and operability where material;
14. platform-specific behavior and Positive Controls;
15. concise architectural properties and constraints.

Items 1–14 belong to factual STM coverage/content: purpose and scenarios, topology, ownership, boundaries, flows, lifecycle, concurrency, failure, trust, configuration, persistence, observability, and platform facts. Item 15 is Architecture-owned interpretation, not an STM fact.

This is a materiality-driven model, not a universal checklist with equal depth for every item. Technical Model Coverage and the materiality map determine what applies, what receives bounded evidence, and what is recorded as `NOT_APPLICABLE` or `UNKNOWN` with a reason. The As-Built projection preserves factual parity, provenance, and visible limitations; it must not normalize `PARTIAL`, stale, or unresolved input into certainty.

Use an ownership matrix and evidence-driven diagrams when they improve understanding.

Technical Model Coverage Review independently accepts the factual substrate in both modes. Only accepted, sufficiently fresh required STM may feed dependent thematic passes. The As-Built projection passes its own projection/parity review but never becomes factual authority.

Architecture-owned interpretation is persisted separately from the factual projection. Accepted `RF-*` / `SER-*` and accepted properties/invariants belong to Architecture semantic authority defined by `report-contract.md`. `01-architecture-review.md` may render that meaning, but it cannot be the only record that survives a later fully generated assembly.

### Evidence-bounded architecture claims

The scope of an architectural claim must not exceed the directly investigated evidence scope:

```text
supported claim scope <= directly exercised / directly evidenced material scope
```

Read-path authorization evidence does not prove write, enumeration, background, or export authorization. Nominal success does not prove retry behavior, unknown-outcome recovery, restart durability, or concurrent duplicate safety. Missing evidence alone is not an implementation defect; preserve `PARTIAL`, `NOT_PROVEN`, or `UNKNOWN` where the wider claim was not exercised.

Search explicitly for material contradictions across:

- application code ↔ deployment/configuration;
- API contract ↔ persistence behavior;
- documented ownership ↔ actual state mutation path;
- auth middleware ↔ background/export paths;
- lifecycle assumptions ↔ service/container/Ansible definitions;
- retry claims ↔ persistence/queue semantics.

Factual contradictions first become `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT`, or `TECH_FACT_REVALIDATION_REQUEST` with provenance and impact. They are not automatic final findings and do not silently rewrite accepted STM or the As-Built projection. An Architecture-owned interpretation contradiction may instead become `OQ-*` or `ARCH-CORRECTION-CANDIDATE`.

## 3. Representative flows

Trace several end-to-end paths selected for architectural significance, such as:

- startup/readiness;
- auth/session restoration;
- a central user operation;
- background or scheduled work;
- network failure/reconnect;
- a persistent write;
- shutdown;
- a security-sensitive update, process, or native flow.

For every flow, record the initiator, owner, crossed boundaries, suspension points, failure paths, cleanup, and authoritative state changes.

## 4. Thematic discovery

Discovery creates `CAND-*`, Positive Controls, open questions, and Architecture correction candidates — not final findings.

At the same time, thematic passes must accumulate coverage evidence according to `discovery-coverage.md`. Completeness is not inferred from candidate count.

A general security/correctness pattern for material source-driven risks is:

```text
source / capability
→ validation / transformation
→ boundary / interpreter / resource / authority decision
→ guard / ownership / parameterization
→ side effect
→ reachable consequence
```

This pattern is not a quota and does not replace domain-specific contracts. It helps prevent a security review from degenerating into a list of trust boundaries only.

### Architecture / responsibility

Check dependency direction, responsibility, hidden global state, service locators, overly broad APIs, cross-layer business rules, and duplicated sources of truth. Do not require “Clean Architecture” merely by pattern name.

### Ownership / isolation / concurrency

Apply `ownership-and-scenarios.md`: owner/writer/reader/lifetime/scope, A+A, A+B, cancellation, disconnect, stale completion, shutdown, and interleavings.

### Boundaries

Apply `boundary-contract-audit.md` to significant interaction, interpreter, resource-addressing, and authority/capability boundaries. Coverage completeness for these classes is governed by `discovery-coverage.md`.

### Lifecycle / resources

Check create → run → failure/retry → cancel → dispose/shutdown for sockets, child processes, files, timers, listeners, locks, database/session resources, temporary paths, and ports.

### Errors

Trace error classification and context across boundaries. Look for swallowed failures, process-wide termination from local cleanup, retry without classification, fallbacks that hide failures, and inconsistent error contracts.

### Security

Map trust boundaries, credentials, TLS, remote content, preload/native capabilities, child processes, filesystem, update chain, deserialization, URL/path validation, authentication/authorization scope, interpreter and dynamic-construction sinks, outbound-target control, secret propagation, privileged capabilities, and legacy/versioned surfaces — but only where those mechanisms actually exist.

Do not treat this list as proof of coverage. High-risk domains are closed according to the semantic contracts in `discovery-coverage.md`.

Serious promotion requires the attack chain defined in `evidence-and-severity.md`.

### Configuration / localization / duplication

Look for conflicting authoritative sources, unsafe defaults, secrets, platform paths, duplicated semantic knowledge, and mixing of protocol strings with user-visible text. Do not promote a hardcoded or duplicate value solely because it looks similar to another one.

### Networking / persistence / observability / performance

Review timeout, cancellation, retry, idempotency, TLS, proxies, atomic writes, migrations, locking, structured correlation, sensitive logging, blocking/event-loop risks, unbounded queues or caches, and lock contention only in the context of real impact.

Treat request-driven amplification/resource exhaustion and business replay/order/idempotency as mechanism classes, not merely as performance observations.

### Tests / testability

Determine which risks are actually protected by existing tests. Raw test count and absence of local tests do not by themselves prove a runtime defect.

### Discovery coverage closeout

After planned thematic passes:

```text
update Discovery Coverage Matrix
→ classify every applicable domain
→ record evidence / non-findings / candidates / OQ / limitations
→ Independent Coverage Review
→ targeted correction/re-review if needed
→ COVERAGE_ACCEPTED
```

`DISCOVERY_COMPLETE` without `COVERAGE_ACCEPTED` does not permit progression to candidate verification.

## 5. Safe verification

Run existing non-destructive checks when the environment permits. Do not install or upgrade dependencies and do not run fixers merely to obtain a green report without authorization.

For every command, record the result and any limitation.

Runtime reproduction for security or correctness evidence must stay within the safety boundaries in `evidence-and-severity.md`; a static finding does not require a forced PoC.

## 6. Independent verification and adjudication

After `COVERAGE_ACCEPTED`:

```text
candidates
→ independent verification
→ root-boundary adjudication
→ severity adjudication
→ authoritative ledger
```

Follow `independent-verification.md`, `root-boundary-adjudication.md`, and `evidence-and-severity.md`.

Coverage Review and candidate verification are different gates:

```text
Coverage Review: did investigation omit a material class?
Independent Verification: is an existing CAND actually real?
```

Do not assign final severity during discovery or coverage review.

## 7. Factual reconciliation and Architecture corrections

If a thematic pass discovers a factual contradiction with accepted, sufficiently fresh STM, it creates `TECH_FACT_CONFLICT` — or `TECH_FACT_CANDIDATE` / `TECH_FACT_REVALIDATION_REQUEST` as appropriate — and continues only in unaffected scope.

The Technical Model Gate performs evidence review, revision/rejection, and impact analysis. A capability does not modify STM or “repair” the As-Built projection as factual authority.

A confirmed STM correction requires targeted technical-coverage and projection-impact scanning. Do not invalidate unrelated accepted coverage without evidence of impact.

If the correction concerns an Architecture-owned invariant, causal interpretation, race conclusion, finding/root/severity, or remediation implication rather than an STM fact, use `ARCH-CORRECTION-CANDIDATE` and the existing Architecture review/correction/adjudication loop. Such a correction does not turn the factual matrix into a finding and does not rewrite STM.

After acceptance, the change is first persisted in the owning Architecture semantic authority: `02-authoritative-findings-ledger.md` for `RF-*`, `SER-*`, and properties/invariants; selected `03-target-architecture.md` for target semantics; or selected `04-remediation-roadmap.md` for roadmap semantics.

The semantic change then makes dependent report projections stale. A final-report writer or Stage B regeneration cannot apply the correction directly to `01-architecture-review.md` or use its prose to decide the semantic result.

## Product Architecture Review scope

Product Architecture Review may write a Product-scoped existing `RF-*` only after independent adjudication of a genuine cross-project architectural consequence. The Product RF record binds the accepted Product identity and revision, immutable Product baseline, affected Projects, qualified `WS-*` / `EV-*` evidence, accepted STM references, consequence, severity, lifecycle, dependencies, and provenance. Architecture Review remains the sole writer of that interpretation; STM and Shared Evidence remain factual authorities.

A Project-local RF is never promoted by membership, aggregation, correlation, or report rendering. A Product report, summary, or projection is navigation or derived presentation only and cannot create, revise, resolve, or supersede an RF.

Product-scoped RFs use the existing local `RF-*` family and local RF identity/lifecycle rules; no Product finding family is introduced. Product RF scope is independent of Code Quality and Test Engineering ownership.

## 8. Positive Controls and non-findings

Maintain a registry of mechanisms that should be preserved. Also retain considered-but-not-promoted conclusions when they prevent repeated false positives and serve as coverage evidence.

Do not treat the following as findings without contextual impact:

- TODOs or comments;
- file/function size;
- framework choice;
- raw warning count;
- `unwrap`, `clone`, or mocks;
- hardcoded literal;
- absence of tests;
- raw-looking API name without source/provenance/effect;
- HTTP client without evidenced control over destination;
- generic slowness without material resource impact.

## 9. Modes

`STANDARD_FULL` uses the same correctness gates. It may combine thematic working passes, but it still creates a compact coverage matrix and passes coverage closeout.

`FORENSIC` separates ownership, lifecycle, boundaries, frontend, security, maintainability, and subsequent adjudication stages more explicitly, preserves a more detailed evidence trail, and includes an explicit Independent Coverage Review gate.

Neither mode may collapse back into one giant prompt/report pass.

## 10. Separation of diagnosis and design

If the endpoint is `REVIEW_ONLY`, stop after the authoritative audit package is accepted.

Target Architecture and a detailed Remediation Roadmap are created only for endpoints that request them, and each passes its own independent review.