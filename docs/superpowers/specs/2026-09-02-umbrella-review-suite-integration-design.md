# Umbrella Review Suite Integration Design

Date: 2026-09-02
Status: DESIGN FOR USER REVIEW
Repository baseline: `main@4e8b79b1ebb3e4d06ce1dda2eaea0cd3244a5871`

## 1. Purpose

Evolve `architecture-code-review` into the intended umbrella review suite without turning the main Skill into a monolith.

This integration brings together four already-discussed directions:

1. integrate the validated Test Review methodology as a composable review capability;
2. add Ansible as one more stack/language addendum, not as a separate review subsystem;
3. extend the existing context orchestration/freshness model with more aggressive context-budget optimization;
4. deepen As-Built architecture reconstruction and cross-domain architectural reasoning.

The design deliberately reuses the current evidence-first workflow, persistent `working/INDEX.md`, independent review gates, authority map, correction/revalidation model, stack addenda, Discovery Coverage Assurance, and context orchestration v0.2. It does not replace those mechanisms.

## 2. Non-goals

This stage does not:

- replace the current `architecture-code-review` workflow with a new audit engine;
- make `SKILL.md` a repository-sized handbook;
- turn Ansible into a standalone review capability;
- embed Skill Lab into runtime review execution;
- require every optional capability on every review;
- restart a completed audit whenever a new capability is added;
- use line/branch coverage, test count, green CI, sampling, or file count as proof of completeness;
- change production code in repositories being reviewed.

Skill Lab remains validation infrastructure for developing Skills. It is not part of the end-user review suite.

## 3. Architectural shape

The product remains one umbrella orchestrator with shared review principles and independently understandable capability/reference modules.

```text
architecture-code-review
│
├── umbrella orchestrator (`SKILL.md`)
│
├── shared review kernel
│   ├── evidence / provenance
│   ├── authority resolution + UNKNOWN
│   ├── materiality
│   ├── coverage / bounded completeness
│   ├── independent verification
│   ├── candidate lifecycle
│   ├── freshness / revalidation
│   └── context orchestration
│
├── architecture/code review capability
│   ├── As-Built reconstruction
│   ├── thematic discovery
│   ├── candidate verification
│   ├── root-boundary adjudication
│   └── severity / report / target / roadmap
│
├── Test Review capability
│   ├── Test Assurance Map
│   ├── material assurance targets
│   ├── evidence universe and evidence families
│   ├── authority-first adjudication
│   ├── boundary-aware evidence scope
│   └── optional test-plan endpoint
│
└── stack addenda
    ├── Django
    ├── FastAPI
    ├── React
    ├── Electron
    ├── Tauri
    ├── ...
    └── Ansible
```

`SKILL.md` remains a thin orchestrator. Detailed normative behavior belongs in owning reference contracts or capability Skills. The same normative rule must not be maintained independently in multiple places.

## 4. Shared review kernel

### 4.1 Existing kernel stays authoritative

Existing contracts remain authoritative for their current responsibilities:

- modes, endpoints, workflow state, resume and subagent handoff;
- evidence-first review method;
- ownership and invariants;
- boundary contracts;
- discovery coverage;
- independent verification;
- root-boundary adjudication;
- evidence and severity;
- lifecycle diagrams;
- report, Target Architecture, Roadmap and editorial gates;
- freshness/revalidation/context orchestration.

The integration must extend these contracts only where a new invariant has proven to be cross-capability.

### 4.2 Test Review invariants promoted to shared principles

The validated Test Review work established several rules that are not test-specific and should be reusable across the suite:

#### Authority before substantive verdict

When materially conflicting authorities exist, the reviewer must determine whether precedence, supersession, approval, ownership decision, or another explicit authority mechanism is established before selecting a governing behavior.

If it is not established:

```text
AUTHORITY_STATUS = UNRESOLVED
SUBSTANTIVE_DISPOSITION = UNKNOWN / AUTHORITY_UNRESOLVED
```

The reviewer records the conflict and missing resolution evidence and does not call either side defective from that disagreement alone.

Urgency, recency, document names, implementation alignment, current tests, CI state, or apparent formality do not independently establish authority.

#### Claim scope must not exceed evidence scope

No review capability may make a system-level claim from narrower evidence without tracing the material boundaries on which the claim depends.

Examples:

- one API handler does not prove system-wide authorization isolation;
- nominal success does not prove retry/idempotency/restart/concurrency behavior;
- an in-process unit test does not prove a material process or transport boundary;
- one read path does not prove write, enumeration, background-processing or export paths.

Narrow evidence may prove a narrow claim. Missing wider evidence normally yields `PARTIAL`, `NOT_PROVEN`, or `UNKNOWN`, not an implementation defect by itself.

#### Completeness requires bounded material accounting

Completeness cannot be inferred from a sample.

Before a capability makes an overall assurance claim, it must establish a bounded material target/domain inventory appropriate to that capability and account for all material items in it. Selective deep inspection is still encouraged; exhaustive deep-reading of every file/test is not.

#### Candidate decomposition preserves material contracts

Rejecting a mechanism, smell, implementation detail, or over-specific assertion must not silently discard a separately material behavioral or architectural contract discovered inside the same candidate.

Every recognized material contract receives an explicit disposition.

## 5. Incrementally composable review capabilities

A capability may enter a review in three ways:

1. selected by the user at the initial review start;
2. recommended by discovery because a material surface makes it useful;
3. explicitly added later to an existing review package.

The suite must support the third case as a first-class workflow.

### 5.1 Adding a capability later

Adding a capability does not restart the audit by default.

The coordinator performs:

```text
read working/INDEX.md
→ verify repository baseline/current revision
→ verify freshness of required owning artifacts
→ identify minimal dependency slice
→ register the new capability and its artifacts
→ execute the capability
→ submit any architecture corrections/findings through normal adjudication
→ targeted revalidation of affected accepted artifacts only
→ reconcile umbrella ledger/report
```

If the repository baseline has changed materially, existing freshness/revalidation rules decide which prior artifacts require revalidation. The capability itself does not invent a parallel freshness model.

### 5.2 Capability ownership

Each substantial capability owns its detailed output.

The umbrella report does not copy the complete Test Review or other capability report. It synthesizes user-facing conclusions and links to owning evidence.

The authoritative findings ledger accepts final adjudicated findings that belong in the whole-system review. Capability-specific working detail stays in the owning capability artifact.

This preserves provenance, avoids conflicting duplicated authority and reduces repeated context loading.

## 6. Test Review integration

### 6.1 Status

Test Review is a real review capability, unlike a stack addendum. It has its own assurance model and can be requested independently or attached to an architecture review.

The integration must preserve the validated behavioral invariants rather than rewrite them from memory.

### 6.2 Runtime relationship to Architecture Review

When Test Review runs inside an existing umbrella review, it may reuse only accepted and fresh architecture artifacts as authoritative downstream input.

Typical dependency set:

- repository baseline/current revision;
- `working/INDEX.md`;
- accepted technical As-Built;
- accepted material boundaries/ownership facts relevant to assurance targets;
- relevant final or candidate findings where explicitly required.

It must not load the entire historical review package by default.

Test Review can produce:

- a Test Assurance Map;
- assurance target accounting;
- evidence-family mapping;
- test-specific candidates/findings;
- architecture-correction candidates if test investigation disproves accepted As-Built facts;
- optional Test Plan when requested by its endpoint.

Architecture correction still follows the umbrella correction/revalidation contract; Test Review never silently rewrites As-Built.

### 6.3 Test Review endpoint relationship

The architecture review endpoint and Test Review endpoint are independent selections.

A user may request, for example:

```text
Architecture: REVIEW_ONLY
Test Review: REVIEW_PLUS_TEST_PLAN
```

or attach Test Review later without retroactively changing the architecture endpoint.

### 6.4 Packaging cleanup

The integration stage must reconcile the published Test Review Skill package with the actually validated v1 behavior. Historical candidate-boundary wording that describes the Skill as an incomplete experimental candidate must not remain as current runtime truth if it conflicts with the validated release state.

Any such cleanup must preserve the validated behavioral digest/invariants semantically; it is packaging/status correction, not a license to redesign Test Review.

## 7. Ansible as a stack addendum

Ansible is handled exactly through the existing stack-addendum mechanism.

Target file:

```text
references/stacks/ansible.md
```

It should contain high-value Ansible-specific review guidance such as:

- playbook/role responsibility boundaries;
- inventory and host targeting;
- variable precedence and configuration ownership;
- handlers and restart/lifecycle semantics;
- task and role idempotency;
- `changed_when` / `failed_when` where materially relevant;
- privilege escalation (`become`) and trust boundaries;
- secrets/vault handling;
- templates and generated runtime configuration;
- retries, delegation, `run_once`, serial/rolling behavior where relevant;
- check-mode limitations;
- dependency/collection/module pinning and reproducibility;
- deployment failure/partial-application risks where the code path makes them material.

These are stack-specific prompts for evidence collection, not findings by themselves.

Ansible may also be evidence for the normal As-Built architecture (for example deployment topology, process configuration or service lifecycle), but the evidence is adjudicated through the normal architecture contracts.

## 8. Deeper As-Built architecture reconstruction

The existing As-Built-first approach stays intact. The improvement is to make the material architecture model more explicit and less vulnerable to shallow directory/framework inference.

### 8.1 Material architecture dimensions

For the reviewed scope, discovery determines which of these dimensions are material:

- deployment topology;
- runtime components/processes;
- ownership of state, lifecycle and authority;
- API/IPC/process/persistence/trust/deployment boundaries;
- command/write flows;
- read/query flows;
- asynchronous/background flows;
- external integration flows;
- state machines and lifecycle transitions;
- cancellation, retries and recovery;
- concurrency/shared-state/serialization/idempotency;
- failure domains and partial failure;
- authentication/authorization and other trust contracts;
- configuration/secrets;
- persistence/migrations/consistency;
- observability/operability where material.

This is not a mandatory checklist requiring equal depth everywhere. The Discovery Coverage Matrix/materiality model determines what must be investigated, what is `NOT_APPLICABLE`, and what remains explicitly `UNKNOWN`.

### 8.2 Architecture claims need traced support

An accepted As-Built claim should be traceable to concrete evidence appropriate to its scope: code path, configuration, runtime/deployment definition, persistence behavior, contract, ownership source, or other direct evidence.

Framework convention, filenames, directory names, comments, TODOs, or inferred intent are insufficient by themselves.

### 8.3 Cross-domain consistency

Architecture reconstruction must explicitly look for contradictions between material evidence surfaces, for example:

- application code vs deployment configuration;
- API contract vs persistence behavior;
- documented ownership vs actual state mutation path;
- auth middleware vs background/export paths;
- lifecycle assumptions vs systemd/container/Ansible behavior;
- retry assumptions vs persistence/queue semantics.

A contradiction does not automatically become a finding. It first becomes an open question or architecture-correction candidate and follows existing authority/verification gates.

## 9. Context Orchestration v0.3 delta

This stage extends v0.2; it does not replace freshness/revalidation semantics.

### 9.1 Principle

```text
Load the minimum fresh authoritative evidence needed for the current decision.
```

Optimization must never reduce correctness by treating a stale or lossy summary as substantive authority.

### 9.2 Two context classes

#### Routing context

Compact information used to decide what to read next:

- `working/INDEX.md`;
- artifact registry/statuses;
- handoff summaries;
- candidate IDs and evidence pointers;
- materiality/coverage maps;
- accepted revision bindings.

Routing context may be compacted aggressively.

#### Decision evidence

Owning source required to make or verify a substantive claim:

- source code/configuration;
- accepted owning review artifact;
- exact contract/authority evidence;
- targeted runtime/test evidence.

A substantive verdict must not rely solely on a compact routing projection when the owning evidence is required to support the claim.

### 9.3 Progressive retrieval

Each phase should use this pattern:

```text
structure / inventory
→ materiality map
→ evidence pointers
→ targeted reads
→ deeper reads only for unresolved material questions
```

Do not preload all reference files, all prior working artifacts, or broad repository contents merely because they may be relevant.

### 9.4 Dependency-sliced capability context

When invoking a subagent or later-added capability, the coordinator supplies:

- exact baseline/revision;
- narrow scope and forbidden scope;
- accepted dependency artifacts or the relevant sections/pointers;
- required shared contracts;
- output path and handoff contract.

Unrelated accepted artifacts are not included by default.

### 9.5 Freshness remains fail-closed

Compaction never overrides revision/freshness checks.

A compact projection that cannot be proven current relative to its owning artifact/repository baseline is routing-only and cannot authorize a substantive downstream conclusion.

### 9.6 Context optimization success criteria

The design succeeds when it reduces repeated broad reads while preserving:

- exact authority provenance;
- accepted-artifact revision binding;
- ability to recover/resume;
- ability to falsify a claim from owning evidence;
- targeted revalidation when upstream facts change.

Token reduction is desirable but is not allowed to weaken these properties.

## 10. Orchestrator changes

The main `SKILL.md` should change only enough to express orchestration responsibilities:

- advertise umbrella/composable review behavior;
- route to the Test Review capability when selected/recommended/added later;
- retain independent depth and endpoint choices;
- route to applicable stack addenda including Ansible;
- point to shared authority/context contracts;
- preserve current completion gates.

Detailed Test Review rules, Ansible guidance, and context methodology must not be copied wholesale into `SKILL.md`.

## 11. Artifact model

The existing package remains compatible. The design should add capability-owned artifacts without forcing a complete rename of current files.

A representative package may look like:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md              # optional
├── 04-remediation-roadmap.md              # optional
├── capabilities/
│   └── test-review/
│       ├── 01-test-assurance-map.md
│       └── 02-test-plan.md                 # optional
└── working/
    ├── INDEX.md
    ├── ... existing architecture working artifacts ...
    └── capabilities/
        └── test-review/
            └── ... capability working evidence ...
```

Existing project-local conventions may override exact paths. The important invariant is ownership and registry in `INDEX.md`, not one mandatory filesystem layout.

## 12. Error, conflict and stale-state handling

- Conflicting authority without established precedence → `UNKNOWN/AUTHORITY_UNRESOLVED`, not guessed truth.
- Capability discovers contradiction with accepted As-Built → `ARCH-CORRECTION-CANDIDATE`, not direct edit.
- Capability dependency is stale → `REVALIDATION_REQUIRED`/blocked execution according to existing freshness rules.
- Added capability needs evidence unavailable in current scope → explicit `UNKNOWN`/open question/limitation.
- Optional capability not requested and not required by the selected assurance claim → `NOT_APPLICABLE` or absent, not a completion failure.
- Context projection lacks verifiable freshness → cannot serve as substantive authority.

## 13. Validation strategy

Implementation follows Skill TDD, but this integration should avoid reopening already-proven infrastructure or running endless stochastic variants.

Validation should be targeted to genuinely new or changed behavior.

Required pressure/regression coverage should include at least:

1. later-added Test Review resumes an accepted audit without full restart;
2. stale upstream architecture state blocks or triggers targeted revalidation before Test Review depends on it;
3. Test Review authority conflict remains `UNKNOWN` rather than being overridden by umbrella assumptions;
4. cross-capability finding/correction is reconciled into the shared ledger without duplicating the full Test Review report;
5. Ansible surface loads Ansible stack guidance through the normal stack mechanism and does not create a separate Ansible capability;
6. context optimization does not permit a stale compact projection to replace owning evidence;
7. dependency-sliced subagent context still contains enough exact provenance to support/falsify its final claims;
8. deeper architecture reconstruction catches a deliberately asymmetric or cross-surface architecture claim that shallow discovery would over-generalize.

Existing Discovery Coverage, orchestration, freshness, authority-integrity and final-package regression scenarios must remain green.

Already validated Test Review pressure invariants should be reused as regression coverage where possible rather than rediscovered through new Skill versions.

## 14. Implementation decomposition

The subsequent implementation plan should treat this as one integration program with bounded workstreams, preferably in this order:

1. shared-kernel/integration contract and capability registry semantics;
2. Test Review packaging + umbrella orchestration integration;
3. incremental capability resume/revalidation/artifact ownership;
4. Ansible stack addendum;
5. deeper architecture-reconstruction delta;
6. Context Orchestration v0.3 delta;
7. targeted pressure/regression validation;
8. documentation/readme cleanup and final integration review.

The plan should avoid unnecessary Skill Lab changes unless a missing test-harness capability blocks a required scenario.

## 15. Acceptance criteria

The integration is design-complete when implementation can demonstrate all of the following:

- `architecture-code-review` remains a thin umbrella orchestrator;
- Test Review is available as a composable capability and can be added after an existing audit;
- capability-owned artifacts remain authoritative for their specialist detail;
- shared findings/architecture corrections flow through the existing authoritative ledger and revalidation gates;
- Ansible is implemented only as a normal stack addendum;
- architecture claims are bounded by investigated evidence/material surfaces;
- the suite preserves authority-first `UNKNOWN` semantics;
- bounded completeness is not inferred from samples;
- context loading is dependency-sliced and progressive;
- compact projections cannot silently replace stale or owning evidence;
- existing context-orchestration/freshness/coverage/authority regressions remain green;
- Skill Lab remains development/validation infrastructure rather than runtime review functionality.

## 16. Explicit design decisions

The following decisions are approved design invariants for this integration:

1. one umbrella suite under `architecture-code-review`;
2. `SKILL.md` remains an orchestrator, not a monolith;
3. Test Review is a first-class composable capability;
4. a capability can be selected initially, recommended during discovery, or added later;
5. adding a capability extends and selectively revalidates an existing audit rather than restarting it by default;
6. specialist detail stays in the owning capability artifact; the umbrella ledger/report aggregates adjudicated cross-system results;
7. Ansible is one more stack/language addendum;
8. context optimization extends v0.2 and must preserve freshness/revalidation correctness;
9. deeper architecture analysis uses materiality and bounded evidence scope rather than a universal checklist;
10. Skill Lab does not become part of end-user runtime review execution.
