# Stage D — Code Quality Review Discovery

## 1. Baseline and scope

Discovery baseline is canonical `main` at
`5c7eea3b0174c1f7608fb438fc37e0f2dc35e44c`, with roadmap status:

```text
Stage A: DONE
Stage B: DONE
Stage C: DONE
Stage D: PLANNED
Stage E: PLANNED
```

This document records Discovery only. It identifies boundaries, evidence
needs, unresolved semantic choices, and pressure questions for a future Design.
It does not define an approved Code Quality contract, implementation plan, or
finding taxonomy.

The current repository is a Markdown Skill/reference system. Existing review
contracts provide methodology and orchestration semantics, not a Code Quality
runtime.

## 2. Current-state findings

No separate Code Quality capability, semantic contract, implementation plan,
Code Quality-specific pressure suite, or implementation was found in current
main or reachable branch history. No dedicated `CQ-*`, `QF-*`, or `SMELL-*`
authority is present.

Relevant partial precursors are:

| Artifact | Current purpose | Stage D equivalence |
|---|---|---|
| `docs/roadmap.md` | Candidate Stage D scope and open design questions | PARTIAL |
| `docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md` §22 | Future Code Quality consumers, ownership boundary, and reuse of STM/evidence | PARTIAL |
| `references/review-method.md` | Architecture-review passes for configuration, localization, duplication, errors, resource/lifecycle, concurrency, and testability | PARTIAL |
| `references/evidence-and-severity.md` | Materiality, evidence, confidence, and severity safeguards shared by Architecture Review | PARTIAL |
| `tests/pressure-scenarios.md` and related scenarios | Architecture-review controls against smell-only promotion and severity inflation | PARTIAL |
| `capabilities/test-review/**` | Test assurance and Test Engineering semantics | NONE as Code Quality authority |

Quality-related history (`PS-34..38`, materiality and report-quality checks)
concerns review quality, architecture-review false-positive controls, or
presentation. It does not constitute a Code Quality capability. No historical
Code Quality merge or rename was found.

## 3. Ownership boundaries

### Candidate concern classification

The category is contextual where the same mechanism can have different effects.
The following is a Discovery classification, not a final routing algorithm.

| Concern | Primary Discovery category | Boundary note |
|---|---|---|
| duplication, copy-paste logic | CODE_QUALITY | ARCHITECTURE when duplicated semantics cross ownership/bounded-context or create material drift risk |
| hardcoded values | CODE_QUALITY | ARCHITECTURE/security when the value encodes an unsafe system boundary, deployment, trust, or lifecycle assumption |
| configuration practices | CROSS_CAPABILITY_WITH_DISTINCT_INTERPRETATION | Code Quality inspects implementation practice; STM/Architecture own factual topology and architectural risk |
| localization practices | CODE_QUALITY | ARCHITECTURE only when it reflects a material product/boundary contract or systemic delivery risk |
| dead/obsolete code | CODE_QUALITY | ARCHITECTURE when it preserves a stale authority, unsafe path, or material lifecycle/security mechanism |
| oversized functions/classes/modules | CODE_QUALITY | Size is a signal; promotion requires cohesion/responsibility or change-risk evidence |
| poor/excessive abstraction boundaries | CODE_QUALITY | ARCHITECTURE when the boundary crosses material system ownership, trust, or dependency semantics |
| error handling | CROSS_CAPABILITY_WITH_DISTINCT_INTERPRETATION | Code Quality evaluates implementation handling; Architecture owns systemic failure contracts; Security owns security effects where applicable |
| resource management | CROSS_CAPABILITY_WITH_DISTINCT_INTERPRETATION | Code Quality evaluates local misuse; Architecture owns systemic lifecycle/resource failure |
| async misuse, concurrency misuse | CODE_QUALITY | ARCHITECTURE/security when it creates cross-component, trust, availability, or shared-state risk |
| framework anti-patterns | CODE_QUALITY | ARCHITECTURE when framework use changes a material boundary or system invariant |
| maintainability smells | CODE_QUALITY | May support an Architecture finding but is not automatically one |
| security-adjacent code smells | AMBIGUOUS_REQUIRES_DESIGN | Route to security ownership when a traceable security consequence exists |
| dependency misuse | CODE_QUALITY | ARCHITECTURE when dependency topology or trust boundary is materially affected |
| inconsistent implementation patterns | CODE_QUALITY | ARCHITECTURE when inconsistency breaks a shared contract or cross-component invariant |
| testability | CROSS_CAPABILITY_WITH_DISTINCT_INTERPRETATION | Code Quality assesses design friction; Test Engineering assesses assurance/evidence impact |
| complexity | CODE_QUALITY | Complexity alone is not a finding; material change, defect, or comprehension cost is required |
| naming/clarity issues | CODE_QUALITY | Style-only observations require a materiality threshold or are omitted |
| API misuse | CODE_QUALITY | ARCHITECTURE/security when it violates a material system or trust contract |
| lifecycle misuse | CROSS_CAPABILITY_WITH_DISTINCT_INTERPRETATION | Code Quality handles local implementation misuse; Architecture handles systemic lifecycle semantics |
| unused dependencies | CODE_QUALITY | Also consider supply-chain/security ownership when dependency presence creates material exposure |
| unsafe defaults | CODE_QUALITY | ARCHITECTURE/security when the default changes a material trust, data, or operational boundary |

### Architecture Review boundary

A code-level issue becomes an Architecture finding only when evidence connects
the implementation mechanism to a material architectural boundary, invariant,
cross-component contract, lifecycle, trust boundary, or system-level
reliability/security effect. Examples include duplicated authority across
services, a module that collapses ownership of a system boundary, or local
concurrency misuse that corrupts shared state.

The following are not sufficient by themselves: one helper's duplication, one
hardcoded string, a large but cohesive module, a large generated function, a
local framework idiom, or an unobserved concurrency concern. The current
Architecture method already examines maintainability, configuration,
duplication, errors, resources, concurrency, and testability, but its
promotion rules require contextual material impact. This is compatible with:

```text
Code Quality finding != automatically Architecture finding
```

Architecture `RF-*` remains Architecture-owned. Code Quality may reference a
related `RF-*` after independent adjudication, but must not create or rewrite
one to make a quality concern fit the Architecture ledger.

There is currently no independent Security Review capability in this
repository. Until a separate capability is introduced by an explicit
architecture/design decision, security-relevant mechanisms use the existing
Architecture Review security semantics and evidence/severity gates. Code
Quality may retain an independently owned quality interpretation of the same
evidence, but it must not downgrade, replace, or close the Architecture/security
interpretation. A future dedicated Security capability would require its own
authority and integration decision.

### Test Engineering boundary

Code Quality and Test Engineering can observe the same implementation seam but
answer different questions:

| Shared subject | Code Quality interpretation | Test Engineering interpretation |
|---|---|---|
| testability/seams | Is the implementation unnecessarily coupled or difficult to maintain/change? | Which `BC-*`/`MAT-*` behavior lacks reliable executable evidence? |
| nondeterminism/concurrency | Is the implementation pattern fragile or unsafe? | Can assurance execute and observe the relevant behavior reliably? |
| dependency usage | Is the dependency boundary or use unnecessarily complex/misused? | Which environment strategy or simulator/E2E boundary proves the behavior? |
| error observability | Is failure handling locally unclear or swallowed? | Is a material behavior's failure observable and mapped by `TM-*`? |

Both findings may legitimately exist. They should cross-reference the other's
accepted record or evidence, not collapse identity. Code Quality must not write
`BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, or `TASK-*`; Test Engineering must not
adopt a Code Quality smell as semantic behavior truth.

Design must define the meaning of each cross-capability relationship, at least:

```text
DUPLICATE    same semantic issue represented twice accidentally; do not retain two authorities
CORRELATED   distinct findings share evidence or a mechanism
CAUSAL       one issue materially contributes to another
ESCALATED    a local quality issue crosses another capability's material authority boundary
DERIVED      one semantic record is produced from another accepted semantic record
INDEPENDENT  shared area/evidence, but distinct interpretation and authority
```

Design must also decide whether one Code Quality finding may relate to multiple
Architecture, security, or Test Engineering records, and whether these
relationships affect severity, lifecycle, freshness, or only navigation. A
relationship must not silently merge identities or ledgers.

## 4. Shared Evidence and STM reuse

Code Quality should reuse the Stage A factual substrate:

```text
WS-* / EV-*       shared evidence worksets and observations
COMP-* IF-* INT-* DS-* EVENT-* FLOW-* AUTH-* CFG-* ERR-*   STM facts
```

Accepted/fresh STM can provide topology, ownership, interfaces, interactions,
data stores, events, flows, trust/authentication boundaries, configuration
facts, and error contracts. These facts can bound the scope and consequence of
a quality observation without becoming a private quality model.

Direct source-code observations are still required for many Code Quality
claims: exact symbols, repeated structures, call paths, framework usage,
unused paths, local resource handling, and source revisions. Such observations
should use `EV-*` with provenance where they are evidence observations; this
does not redefine `EV-*` or turn a Code Quality interpretation into STM fact.

Position:

```text
new_private_fact_model_needed: NO
```

Design must resolve the record shape and authority for source-local
observations, but it must preserve one shared factual universe and separate
Code Quality interpretation from STM facts.

## 5. Candidate finding model

A Code Quality finding needs an identity independent of Architecture `RF-*`.
Reusing `RF-*` would conflate local maintainability judgments with Architecture
root-boundary adjudication, distort Architecture severity and ownership, and
make cross-capability aggregation ambiguous. A dedicated prefix is recommended
but unresolved; `CQ-*`, `QF-*`, and `SMELL-*` remain candidates for Design.

The finding identity should be stable across revalidation and carry, directly
or through owning records:

- bounded review scope and repository/project identity;
- source bindings for files, symbols, revisions, and relevant dependency or
  configuration context;
- language/framework applicability;
- mechanism/smell classification and concrete consequence;
- severity/materiality and confidence as separate concepts;
- status/lifecycle and adjudication state;
- a deterministic deduplication key;
- optional references to `RF-*`, TE records, shared `EV-*`, and remediation;
- supersession/freshness information after refactors or framework changes.

The exact schema, prefix, and whether identity is source-location-first or
mechanism/scope-first are MUST_RESOLVE_BEFORE_DESIGN_APPROVAL decisions.

## 6. Severity analysis

Existing Architecture severity/evidence principles are reusable as guardrails,
but the Architecture scale should not be copied blindly. Code Quality may need
to distinguish:

- material operational/security/reliability impact;
- blast radius and recurrence;
- defect likelihood or change-induced risk;
- maintainability/change cost;
- remediation urgency;
- confidence and evidence completeness.

A single scalar can be a presentation result, but Discovery does not establish
that it is sufficient for adjudication. The Design must decide whether
materiality, confidence, impact, and urgency are independent axes, and how a
local maintainability issue differs from a security or operational defect.
Smell count, line count, warning count, or subjective inconvenience must not
drive severity alone.

## 7. Evidence requirements

Every defensible finding should identify the exact observation and its scope.
Minimum evidence varies by claim:

| Claim | Minimum defensible evidence to define in Design |
|---|---|
| duplicated logic | repeated files/symbols or normalized structure, semantic equivalence/overlap, and material drift/change consequence |
| oversized module/function/class | exact scope, responsibilities, cohesion/coupling evidence, and a concrete maintenance/change/test consequence |
| unsafe resource handling | resource acquisition/release path, exceptional path or lifecycle trace, and leak/exhaustion/corruption consequence |
| concurrency misuse | shared state/ordering/async path, synchronization assumption, and demonstrated or credible race/liveness/corruption consequence |
| framework anti-pattern | applicable framework rule/version, exact usage, and concrete behavior/maintenance/security consequence |
| hardcoded localization | user-visible source and localization context, affected locale behavior, and product consequence |
| dead code | reachability/configuration evidence, feature-flag/build context, and why stale code has material maintenance or safety impact |

Generic file size, one literal, a linter warning, an absent test, or a smell
label without context is not sufficient. Source line/range and symbol should be
recorded when available; AST/static structure, call path, cross-file evidence,
configuration context, and runtime/test consequence are added according to the
claim rather than required universally.

## 8. False-positive controls

Design must provide explicit controls for:

- generated/codegen output, vendored third-party code, migrations, tests, and
  fixtures;
- intentional duplication, compatibility shims, transitional code, and
  performance-critical structures;
- framework boilerplate and language idioms;
- small repositories where size thresholds are misleading;
- feature flags, conditional builds, and domain-specific conventions;
- findings already represented by Architecture or Test Engineering records;
- source/configuration revisions that make a prior observation stale.

Likely required concepts are applicability, confidence, bounded scope,
materiality threshold, repeat-count/context where relevant, and a recorded
suppression or accepted-exception reason. Suppression must not be an invisible
filter: false positive, accepted exception, and `WONT_FIX` have different
meanings and should remain auditable. Exact suppression syntax is deferred to
Design/implementation.

## 9. Language/framework strategy

The core contract should be language-neutral: evidence, ownership, scope,
materiality, confidence, lifecycle, cross-capability references, and projection
rules. Optional language/framework addenda can define applicability and
heuristics for Python, JavaScript/TypeScript, React/Next.js, Rust/Tauri, Java,
Go, and other stacks as evidence requires.

An addendum must declare its language/framework/version applicability and the
evidence required for a heuristic. It may identify a candidate smell but cannot
override core ownership, severity, authority, or false-positive rules. The
Design should start with only stacks supported by observed repository scope,
not pre-create a catalog of speculative rules.

## 10. Scope and revalidation

Code Quality should support bounded analysis over repository, package,
component, module, file, class, function/symbol, dependency, and configuration
unit, with the chosen unit recorded explicitly. A review such as “changed files
only” must not silently imply that unchanged dependency context is irrelevant.

At entry level:

- `NEW` selects an explicit scope and applicable quality domains;
- `EXTEND` reuses accepted/fresh evidence and adds only the requested scope or
  quality domain;
- `RESUME` restores the selected Code Quality scope and outputs, accepted
  semantic references, current phase, blockers, and required verification state
  from persistent coordinator state compatible with `working/INDEX.md`; it
  never reconstructs state from chat history, silently restarts the full
  review, or promotes `INDEX.md` to semantic authority. Stale dependencies
  discovered during resume route through existing freshness/revalidation
  semantics, while accepted/fresh upstream work remains reusable;
- `REVALIDATE` loads the minimum fresh source, dependency, configuration,
  framework, STM, and related Architecture/TE bindings affected by change.

Likely stale triggers include file/symbol revision changes, dependency or
configuration changes, framework/version changes, relevant STM revision changes,
architecture-boundary changes, and changed source context used to deduplicate a
finding. A refactor that preserves the observed mechanism's semantics should be
able to revalidate or retain a finding without forced whole-repository replay.
Exact fingerprints and impact algorithms are deferred.

## 11. Remediation integration

Code Quality findings need actionable remediation linkage, but must not silently
reuse Test Engineering `TASK-*` as their own authority. Design must decide
whether a distinct Code Quality work-item family is required, or whether a
shared remediation record can reference independently owned findings.

The model must support one remediation action resolving multiple findings and
one finding requiring multiple ordered actions. It must distinguish:

```text
false positive != accepted exception != WONT_FIX != resolved
```

Remediation status must not rewrite finding evidence or Architecture/TE
semantic authority. A finding may reference an Architecture roadmap item or TE
task where the owner accepts the cross-capability relationship, but ownership
and closeout remain explicit.

## 12. Stage B and projection reuse

Future Code Quality summaries, findings views, or roadmap contributions that are
independently regeneratable should reuse the shared Stage B lifecycle:

```text
PRJ-* identity
projection contract revision
semantic/source/evidence dependencies
dependency-resolution snapshot
candidate generation
V1 -> V2 -> V3 -> V4
canonical fingerprint
verified PRJ-*@revN
CURRENT | STALE | BLOCKED
```

Projection dependencies must retain the canonical `CONSUMER -> PREREQUISITE`
direction and keep semantic dependencies distinct from projection edges.
Impact accounting uses the shared `Projection Impact Analysis` and
`PROJECTION_IMPACT_ACCOUNTED`; regeneration is an explicit `RG-*` workflow.
There is no Discovery evidence for a parallel Code Quality projection model.

Specific projection IDs, package membership, selectors, and output contracts
are unresolved Design work. The existing Stage B lifecycle is sufficient as the
preferred foundation.

## 13. Review Suite integration

The future suite should expose Architecture Review, Code Quality Review, and
Test Engineering as independently selectable capabilities. Each retains its
semantic authority, scope, freshness, and optional outputs. An aggregate may
summarize cross-capability references, but it must not merge `RF-*`, Code
Quality findings, or TE records into one ledger by convenience.

Shared `WS-*`/`EV-*` evidence and accepted STM can be reused. Code Quality,
Architecture, and Test Engineering require independent authority and
revalidation decisions. Separate projection identities are expected if each
capability produces independently regeneratable output; the exact aggregate
projection and deduplication rules require Design.

## 14. Security-adjacent boundary

Security-adjacent code smells remain contextual. A weak crypto call, hardcoded
secret, dangerous deserialization, missing validation, unsafe temporary file,
subprocess misuse, or race condition can begin as a Code Quality observation,
but a traceable confidentiality, integrity, availability, authentication, or
authorization consequence routes to the existing Architecture Review security
semantics and evidence/severity gates. There is no independent Security Review
capability today. It must not be downgraded to a style finding.

Code Quality may retain a quality finding and reference the Architecture
security interpretation or emit a candidate for its adjudication. It must not
duplicate, weaken, or close that authority. The Design must define the handoff
trigger and precedence when both interpretations are present. A future
dedicated Security capability, if proposed, requires a separate
architecture/design decision; none is created by Stage D Discovery.

## 15. Candidate outputs

| Candidate output | Discovery classification | Rationale |
|---|---|---|
| Code Quality semantic finding records | CORE AUTHORITY | stable scoped findings with evidence, lifecycle, relationships, and remediation linkage |
| Code Quality Findings View / Report | CORE PROJECTION | regeneratable view over accepted semantic findings; never semantic authority |
| Code Quality Summary | DERIVED | human-facing synthesis of accepted findings and limitations |
| Remediation Recommendations | DERIVED or OPTIONAL | useful only when findings are accepted and recommendations remain non-authoritative |
| Maintainability Hotspots | OPTIONAL or DERIVED | useful navigation projection, not a second finding authority |
| Code Quality Roadmap Contribution | OPTIONAL or DERIVED | should be generated only when a roadmap endpoint is selected |

The semantic finding records are the CORE authority. The Findings View/Report,
Summary, Hotspots, and Roadmap Contribution are projections or derived views;
none can accept, revise, resolve, or supersede semantic finding state merely by
being rendered. The Design should avoid separate ledgers for every presentation
and must still decide the final user-facing output selection.

## 16. Candidate execution workflow

Discovery-level workflow shape:

```text
scope selection
→ accepted/fresh STM and shared evidence routing
→ source evidence acquisition
→ applicability and exclusion filtering
→ quality analysis
→ candidate grouping/deduplication
→ materiality, confidence, and authority adjudication
→ cross-capability correlation
→ accepted findings and remediation references
→ Stage B projection/impact handoff
```

Design must decide authority writers, lifecycle states, finding identity,
severity dimensions, source binding/fingerprint rules, false-positive and
exception handling, security handoff, output selection, and the exact point at
which an accepted semantic update triggers projection impact accounting.

## 17. Pressure questions for Design

The following cases are required Design pressure questions, not tests or
approved behavior yet:

1. 100 duplicated lines in generated code.
2. Three-line duplication across security-critical authentication handlers.
3. A cohesive 2,000-line module.
4. A 300-line parser-generated function.
5. A hardcoded user-facing Russian string in a localization-enabled UI.
6. A hardcoded internal protocol constant.
7. Dead code behind a feature flag.
8. An intentionally duplicated compatibility shim.
9. A concurrency hazard with no observed failure.
10. A resource leak only on an exceptional path.
11. A framework anti-pattern harmless at the current scale.
12. A smell already represented by an Architecture finding.
13. A testability issue already represented by a TE gap.
14. The same smell repeated across 50 files.
15. Vendored third-party source.
16. A stale finding after refactor.
17. Code changed while the underlying quality semantics did not.
18. A Code Quality issue with security implications.
19. A monorepo containing multiple languages/frameworks.
20. A targeted review of changed files only.
21. Incomplete source availability in the selected scope: whether review can
    proceed partially, how coverage limitations are represented, and when the
    result must be blocked versus qualified.
22. An unsupported language or framework: whether the language-neutral core can
    run, how unavailable heuristics are declared, and how irrelevant addenda
    are prevented.
23. A mixed-ownership monorepo: how boundaries and cross-owner findings are
    represented and who owns remediation.
24. A dirty or uncommitted selected scope: what baseline/provenance applies and
    how non-reproducible evidence is represented.
25. A binary or generated artifact referenced by source: what is evidence versus
    opaque dependency and when Code Quality is not applicable.
26. Conflicting language/framework heuristics: how core semantics are
    protected and why heuristic disagreement does not itself create a finding.

For each case Design must show evidence threshold, applicability, ownership,
identity/deduplication, severity/confidence, and revalidation behavior.

## 18. Explicit non-goals

The following are likely outside Stage D unless a later approved Design proves a
bounded need:

- automatic refactoring or automatic code modification;
- replacing style lint/formatting enforcement;
- security penetration testing or vulnerability scanning;
- performance benchmarking or runtime profiling;
- full test execution as a Code Quality gate;
- architecture redesign;
- automatic simulator/environment implementation;
- treating raw warning, smell, file-size, or dependency counts as findings;
- creating a second factual model, package manager, or projection lifecycle.

Static analysis tools may be evidence sources, but tool output alone is not
accepted semantic authority.

## 19. Open questions

### MUST_RESOLVE_BEFORE_DESIGN_APPROVAL

1. What dedicated finding family and stable identity semantics should Code
   Quality use, and what is the deduplication key?
2. Which authority writes, accepts, supersedes, and closes a Code Quality
   finding?
3. What are the materiality/severity/confidence axes and their relationship to
   Architecture severity?
4. What exact evidence is mandatory for each material smell class?
5. What are the exclusion, applicability, suppression, accepted-exception, and
   `WONT_FIX` semantics?
6. How is security handoff triggered to the current Architecture Review security
   authority, and how would a future dedicated Security capability change that
   boundary without duplicating findings?
7. What source/STM/dependency bindings make a finding fresh or stale?
8. Which Code Quality outputs are core, and which are optional projections?
9. How are `DUPLICATE`, `CORRELATED`, `CAUSAL`, `ESCALATED`, `DERIVED`, and
   `INDEPENDENT` relationships represented without merging semantic ledgers,
   and which affect severity, lifecycle, or freshness?
10. Is remediation represented by a distinct Code Quality task family or a
    shared remediation record with separate ownership?

### CAN_DEFER_TO_IMPLEMENTATION_PLAN

1. Concrete parser/AST/static-analysis tool choice.
2. Exact file/line serialization and UI formatting.
3. Addenda rollout order for observed languages/frameworks.
4. Storage/index implementation details once authority and identity are fixed.
5. Incremental computation optimization after source bindings are accepted.
6. CI wiring, caching, and operational scheduling.
7. Exact Stage B selector syntax after output membership is decided.

## 20. Recommended Design entry criteria

Design may begin after an independent review confirms:

- Code Quality is a distinct capability with an explicit Architecture and TE
  boundary;
- shared `WS-*`/`EV-*` evidence and accepted/fresh STM are sufficient
  foundations, with no private factual universe;
- a candidate independent finding identity and authority owner are selected;
- materiality, severity, confidence, evidence, and false-positive questions are
  resolved enough to write pressure scenarios;
- security handoff to the current Architecture Review security authority and
  any future-capability boundary are explicit;
- `NEW`, `EXTEND`, `RESUME`, and `REVALIDATE` scope/freshness semantics are
  bounded;
- semantic finding authority is separated from Findings View/Report, Summary,
  Hotspots, and Roadmap projections;
- cross-capability relationship semantics and their effect on lifecycle,
  freshness, severity, and navigation are defined;
- core/optional outputs and Review Suite selection are defined;
- Stage B reuse, projection ownership, and impact-accounting boundaries are
  accepted;
- the 26 pressure questions have Design-level expected outcomes, including
  source availability, unsupported stacks, ownership, provenance, opaque
  artifacts, and conflicting heuristics;
- explicit non-goals prevent automatic refactoring, runtime claims, and
  duplicate Architecture/TE authority.

Until those criteria are met, the recommended next gate is independent review
of this Discovery artifact, not Stage D implementation or roadmap closeout.
