# Menu Output Routing Remediation — Architecture Design

## 1. Status and purpose

| Field | Value |
|---|---|
| Artifact type | Bounded workflow/menu architecture design specification |
| Date | 2026-09-09 |
| Repository | `/home/tod/skills/architecture-code-review` |
| Canonical base | `8475e67161b45554f8cc4ffc1bddbe6bda6eb0fa` |
| Current acceptance verdict | `MENU_ACCEPTANCE_REMEDIATION_REQUIRED` |
| Findings addressed | `MENU-HIGH-001`, `MENU-MEDIUM-001`, `MENU-LOW-001` |
| Proposed migration | `COMPATIBLE_EXTENSION` |
| New semantic capability | `NO` |
| New factual authority | `NO` |

This design resolves the menu/output reachability defects identified by the
post-Stage-F acceptance review. It introduces a requested-work layer that
separates user-requested capabilities from user-requested standalone
projections and documentation outputs. It does not create a fourth semantic
capability, alter factual authority, change projection ownership, or authorize
runtime execution.

This is a design specification, not an implementation plan. It defines the
target semantics, boundaries, routing rules, and acceptance behavior required
for a later implementation plan.

## 2. Fail-first design basis

The current contracts reproduce the acceptance contradiction:

1. The `NEW` Review Suite currently requires at least one top-level capability:
   Architecture Review, Test Engineering, or Code Quality Review. Zero is
   invalid.
2. Technical Documentation is not one of those three semantic capabilities.
3. Stage A and Stage F define user-facing Technical Documentation projections,
   including provided interfaces, consumed interfaces, integrations/events, and
   data/persistence, plus Product-qualified catalog views.
4. Technical Documentation section membership is persisted as an explicit
   scope selection, and Product output selection is explicitly required.
5. Therefore a request such as “Interface Catalog only, without Architecture
   Review” cannot be represented cleanly under the current top-level
   capability rule. Selecting an unrelated capability would misstate the
   requested semantic work; relying on projection registration would confuse
   existence with requestability.
6. Product mode does not solve the contradiction. Product is explicit context
   and composition state, not a semantic capability, factual authority, or
   permission grant.

The design therefore changes the validity predicate for requested work while
preserving the exact three semantic capabilities.

## 3. Design goals

- Make standalone Stage F and Technical Documentation outputs cleanly
  requestable.
- Make Technical Documentation directly requestable where the selected output
  is valid for the chosen scope.
- Preserve all existing capability-only flows and their ownership.
- Keep Product optional and keep single-project mode first-class.
- Resolve only the minimum accepted/fresh dependency slice required by the
  requested work.
- Preserve the distinction between a selected capability and an internal
  dependency.
- Preserve the distinction between requested work and resolved dependency work.
- Keep capability-owned outputs under their existing owning capabilities.
- Preserve the non-execution boundary for tests, simulators, environments,
  database scanning, and external discovery.
- Introduce no semantic authority or factual identity family.
- Give the startup journey stable conceptual labels without prescribing a UI
  framework or terminal widget.

## 4. Non-goals

This design does not introduce:

- a fourth Technical Documentation semantic capability;
- a new Stage F semantic authority or catalog fact family;
- an API, database, SQL, runtime scanner, tracing system, or crawler;
- runtime test execution, simulator runtime, or environment provisioning;
- a new projection lifecycle or replacement for Stage B;
- a new Product lifecycle or Product factual authority;
- replacement of Test Engineering output ownership;
- redesign of Architecture semantics, Target Architecture, or Roadmap;
- roadmap changes or Stage G Discovery;
- implementation code, menu/UI code, runtime orchestration, or tests;
- automatic projection regeneration;
- implicit source-read, test, code, Git, deployment, or publication permission.

## 5. Target requested-work model

The coordinator distinguishes user intent from dependency closure:

```text
requested_work
├── capabilities
│   ├── architecture_review
│   ├── test_engineering
│   └── code_quality_review
└── standalone_outputs
    ├── technical_documentation
    ├── provided_interfaces
    ├── consumed_interfaces
    ├── interface_catalog
    ├── integration_map
    ├── events_messages
    ├── data_access_map
    ├── persistence_data_resources
    ├── migration_responsibility
    ├── external_integrations_catalog
    └── provider_consumer_matrix

requested_work
    ↓ owning-contract resolution
resolved_work
    ├── semantic/factual dependency slice
    ├── required gates
    ├── selected projections/packages
    └── explicit limitations and authorization requirements
```

The exact serialized field names remain implementation-defined unless a
current owning contract requires a particular field. The semantic distinction
is normative:

```text
requested_work != resolved_work
internal dependency != selected capability
```

`requested_work.capabilities` records only capabilities explicitly selected by
the user or confirmed through normalization. It must not be populated merely
because an STM, Evidence, Behavior Model, Contract Verification, or other
dependency is needed.

`requested_work.standalone_outputs` records only valid user-facing outputs
explicitly selected or confirmed by the user. It must not be populated merely
because a projection is a dependency of another output.

`resolved_work` is a coordinator routing result. It may include shared
Evidence, STM facts, targeted coverage, Contract Verification, Product
qualification, projection prerequisites, and package members. Resolved work is
not retroactively presented as requested capability work.

### 5.1 Requested-work records

Every session records:

```text
requested_work:
  capabilities: [<canonical capability ids>]
  standalone_outputs: [<canonical output ids>]
  scope: PROJECT | PRODUCT
  confirmation_status: CANDIDATE | CONFIRMED
```

The record is routing state. It is not semantic authority, an STM record, a
capability finding ledger, or a projection identity.

The coordinator also records the resolved dependency plan separately:

```text
resolved_work:
  dependency_slice: [<accepted/fresh or required refs>]
  required_gates: [<owning gate states>]
  projection_members: [<selected PRJ refs and package conditions>]
  limitations: [<availability, coverage, freshness, authority limits>]
  authorization_requirements: [<separately authorized actions>]
```

The resolver deduplicates shared dependency acquisition across requested items.
It never broadens scope merely because several outputs share STM or Evidence.

## 6. Requested-work validity

The conceptual validity rule changes from:

```text
at least one top-level capability must be selected
```

to:

```text
at least one requested work item must be selected
```

A requested work item is either a selected semantic capability or a selected
valid standalone output.

| Capabilities | Standalone outputs | Validity |
|---:|---:|---|
| 0 | 0 | `INVALID` — `NO_REVIEW_SCOPE_SELECTED` |
| 1 or more | 0 | `VALID` |
| 0 | 1 or more valid outputs | `VALID` |
| 1 or more | 1 or more valid outputs | `VALID` |
| 0 | unsupported output | `INVALID` — `REQUESTED_OUTPUT_UNSUPPORTED` |
| 0 | ambiguous output request | `INVALID` until confirmed — `REQUESTED_OUTPUT_AMBIGUOUS` |
| 0 | Product context only | `INVALID` — Product is not requested work |

The valid standalone-output rule does not weaken any owning dependency or gate.
It changes only whether a user may request a projection/documentation package
without selecting an unrelated semantic capability.

## 7. Work-item taxonomy and ownership

### 7.1 Capability-owned work and outputs

Capability-owned outputs continue to route through their existing capability.
They are not duplicated as standalone authority records.

| Capability | Capability-owned work/output | Routing rule |
|---|---|---|
| Architecture Review | Architecture Report / `REVIEW_ONLY` | Select Architecture Review and preserve its depth/endpoint model |
| Architecture Review | Target Architecture | Normalize into the existing Architecture endpoint |
| Architecture Review | Remediation Roadmap | Normalize into the existing Architecture endpoint |
| Test Engineering | Test Assurance | Required core whenever Test Engineering is selected |
| Test Engineering | Test Plan | Set existing Test Engineering output selection |
| Test Engineering | Contract Consistency Report | Set existing output selection; `CC-*` remains authority |
| Test Engineering | Test Environment Design | Set existing output selection |
| Test Engineering | Service Simulator Design | Set existing output selection |
| Test Engineering | Service Simulator Implementation Plan | Set existing output selection plus required simulator design dependency |
| Test Engineering | E2E Test Plan | Set existing output selection plus minimum E2E dependency slice |
| Code Quality Review | Code Quality Findings | Select Code Quality Review; `CQ-*` remains authority |
| Code Quality Review | Code Quality Summary | Set existing CQ output selection |
| Code Quality Review | Maintainability Hotspots | Set existing CQ output selection |
| Code Quality Review | Code Quality Roadmap Contribution | Set existing CQ output selection; no Architecture Roadmap implication |

Direct natural-language requests for these items may normalize into the owning
capability configuration. They never create a second output identity or a
second semantic owner.

### 7.2 Standalone projection/documentation outputs

The following are canonical requested-output identities. They are user-facing
projection/documentation requests, not semantic capabilities:

| Canonical output | Existing projection/section family | Scope |
|---|---|---|
| Technical Documentation | `PRJ-TECH-DOC-*` package | Project or Product |
| Provided Interfaces | `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` | Project or Product-qualified |
| Consumed Interfaces | `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` | Project or Product-qualified |
| Interface Catalog | Provided + Consumed Interface projections | Project or Product-qualified |
| Integration Map | `PRJ-TECH-DOC-04-INTEGRATIONS` | Project or Product-qualified |
| Events / Messages | Event content in `PRJ-TECH-DOC-04-INTEGRATIONS` | Project or Product-qualified |
| Data Access Map | `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` | Project or Product-qualified |
| Persistence / Data Resources | DS and persistence content in section 05 | Project or Product-qualified |
| Migration Responsibility | `MIGRATION_AUTHORITY` content in section 05 | Project or Product-qualified |
| External Integrations Catalog | External subsection of section 04, with section 07 when selected | Project or Product-qualified |
| Provider / Consumer Matrix | Qualified interface/integration view | Project or Product-qualified |

These names are menu work-item identities, not new `PRJ-*` identities. Existing
projection identity, selector, contract, package, and lifecycle records remain
the authority for generated artifacts.

`Technical Documentation` may be requested as a package-level output. A
focused output such as `Interface Catalog` selects the minimum relevant
documentation sections rather than silently selecting every Technical
Documentation section. A complete documentation request may select the
existing overview plus the user-confirmed section scope under the existing
`TECH-DOC-SCOPE-*` contract.

## 8. Architecture ownership preservation

Architecture Review remains exactly one capability with the existing choices:

```text
Depth:
  STANDARD_FULL | FORENSIC

Endpoint:
  REVIEW_ONLY
  REVIEW_PLUS_TARGET_ARCHITECTURE
  REVIEW_PLUS_TARGET_AND_ROADMAP
```

The six depth/endpoint combinations remain valid. A direct request for Target
Architecture or Remediation Roadmap normalizes into the existing Architecture
endpoint; it does not create a standalone Target or Roadmap authority.

If natural-language normalization proposes an Architecture endpoint and an
explicit confirmed endpoint conflicts with it, the explicit confirmed choice
wins only after the conflict is surfaced. The coordinator must either request
reconciliation or preserve the explicit endpoint and show the normalized
request as rejected/overridden. It must not silently create contradictory
endpoint state.

Examples:

| Request | Canonical result |
|---|---|
| “Architecture review” | Architecture Review + user-selected/recommended depth and endpoint |
| “Target Architecture only” | Architecture Review with `REVIEW_PLUS_TARGET_ARCHITECTURE`; the review remains required by the existing endpoint semantics |
| “Architecture and target, no roadmap” | Architecture Review with `REVIEW_PLUS_TARGET_ARCHITECTURE` |
| “Roadmap” in an Architecture context | Architecture Review with `REVIEW_PLUS_TARGET_AND_ROADMAP`; no independent Roadmap capability |

The design does not claim that a target or roadmap can be generated without
the accepted upstream Architecture artifacts required by their existing
contracts.

## 9. Test Engineering ownership preservation

Direct requests such as “give me a Test Plan” or “make an E2E Test Plan” are
normalized into Test Engineering configuration:

```text
Test Engineering selected
Test Assurance = true
requested output boolean = true
```

Behavior Model remains an internal dependency. Applicable Contract
Verification remains automatic under its existing material-applicability rule.
The output selection and `BC-*`/`CC-*`/`MAT-*`/`TM-*`/`GAP-*` authority remain
owned by Test Engineering.

The following are planning/design outputs only:

- Test Plan;
- Test Environment Design;
- Service Simulator Design;
- Service Simulator Implementation Plan;
- E2E Test Plan.

They do not implement or execute tests, a simulator, or an environment.

## 10. Code Quality ownership preservation

Code Quality Review remains a separate semantic capability owning `CQ-*` and
`CQRA-*`. A direct request for Code Quality Summary, Findings View/Report, or
Maintainability Hotspots normalizes into Code Quality Review and its existing
output booleans. The projection alone is not a new semantic capability.

Code Quality Roadmap Contribution remains CQ-owned. It does not imply
Architecture Review or the Architecture Remediation Roadmap endpoint.

## 11. Standalone Stage F routing

Standalone output resolution uses existing evidence, STM, Technical Model Gate,
Test Engineering compatibility, Technical Documentation, Product, and Stage B
contracts. It adds a routing entry point; it does not duplicate those contracts.

| Requested output | Required conceptual semantic slice | Owning projection route |
|---|---|---|
| Interface Catalog | Shared Evidence → accepted `IF-*` provided/consumed records and applicable `INT-*` relations → Technical Model Gate | Sections 02 and 03; existing service projections or Product-qualified view |
| Provided Interfaces | Evidence → `IF.direction=PROVIDED` → Technical Model Gate | `PRJ-TECH-DOC-02-PROVIDED-INTERFACES` |
| Consumed Interfaces | Evidence → `IF.direction=CONSUMED` → Technical Model Gate | `PRJ-TECH-DOC-03-CONSUMED-INTERFACES` |
| Integration Map | Evidence → accepted `INT-*` relations and applicable `EVENT-*`/`IF-*` facts → Technical Model Gate | `PRJ-TECH-DOC-04-INTEGRATIONS` |
| Events / Messages | Evidence → accepted `EVENT-*` and applicable interaction/interface facts → Technical Model Gate | Event content in section 04 |
| Data Access Map | Evidence → accepted `DS-*` plus `INT.interaction_kind=DATA_ACCESS` and precise access modes → Technical Model Gate | `PRJ-TECH-DOC-05-DATA-AND-PERSISTENCE` |
| Persistence / Data Resources | Evidence → accepted `DS-*` and controlled persistence relations → Technical Model Gate | Section 05 |
| Migration Responsibility | Evidence → accepted `MIGRATION_AUTHORITY` relation → Technical Model Gate | Section 05; does not infer runtime migration |
| External Integrations Catalog | Qualified existing `COMP-*`/`IF-*`/`INT-*`/`DS-*`/`AUTH-*` facts and safe external bindings | External section 04 subsection, section 07 when auth is selected |
| Provider / Consumer Matrix | Qualified provider/consumer IF views and available matching context | Existing interface/integration projections; no new factual family |

The resolver may acquire a targeted STM slice for a standalone output. It may
not interpret a projection as factual authority, promote a weak hint, infer
database access from a connection, infer an API call from a configured URL, or
turn a migration declaration into runtime access.

### 11.1 Standalone output limitations

An output request can complete with explicit limitations where accepted facts
are partial, unavailable, stale, unresolved, or not applicable. It must not
turn those states into an empty, exact, compatible, clean, or failed result.
The existing evidence sensitivity boundary remains in force:

- `SECRET` values are omitted;
- `SENSITIVE_INTERNAL` values are safely aliased or redacted;
- `SAFE_TECHNICAL_IDENTIFIER` values render only when permitted.

## 12. Compatibility boundary

```text
Provider / Consumer Matrix != compatibility verdict
```

A matrix-only request renders exact provider/consumer views, candidate matching
context, and bounded “not established” or “indeterminate” states. It does not
automatically require or create a compatibility adjudication.

A compatibility request routes to existing Test Engineering Contract
Verification when the material-applicability rule is met. The accepted
`CC-*` record remains the sole owner of status, classification, adjudication,
lifecycle, and historical meaning.

| Request | Required behavior |
|---|---|
| Matrix only | Render provider/consumer records and matching context; no automatic compatibility verdict |
| “Are they compatible?” | Require exact provider/consumer inputs and applicable fresh accepted `CC-*`; return the existing normalized result or `INDETERMINATE` |
| Missing or unresolved pair | Do not infer compatibility; preserve candidate/indeterminate limitation |

Stage F does not match interfaces or adjudicate `COMPATIBLE` or
`INCOMPATIBLE`. Product views consume qualified CC-owned results only.

## 13. Dependency resolution

The routing sequence is:

```text
requested work
  → owning contract resolution
  → minimum accepted dependency slice
  → resolve missing/stale material inputs
  → owning semantic gates
  → selected projection/package output
```

For multiple requested items, the coordinator computes a dependency union and
deduplicates shared Evidence, STM, coverage, and Product qualification work.
The union is still bounded by the requested output predicates and exact
Product scope. It does not become a complete Review Suite.

The resolver must never perform this implicit escalation:

```text
requested standalone output → complete Architecture + Test + CQ Review Suite
```

If a requested output requires an unavailable or unresolved material authority,
the output remains blocked or limited under its owning contract. Selecting a
standalone output does not authorize reading another repository or accepting
unavailable facts.

## 14. Resolved-plan confirmation

Before substantive work, the coordinator shows a compact confirmation in the
user's language. It contains:

```text
Requested capabilities:
  <confirmed capability list, possibly empty>

Requested standalone outputs:
  <confirmed output list>

Scope:
  single Project | Product <qualified identity/revision/baseline when Product>

Required internal dependencies:
  <minimum Evidence/STM/coverage/CC/Product qualification slice>

Excluded work:
  <capabilities, endpoints, outputs, or runtime operations not requested>

Authorization / execution boundaries:
  <separate approvals still required>
```

For example:

```text
Requested capabilities:
  none

Requested standalone outputs:
  Interface Catalog
  Data Access Map

Scope:
  single Project

Required internal dependencies:
  targeted Shared Evidence
  IF/INT/DS Shared Technical Model slices
  Technical Model Gate
  Technical Documentation projections

Excluded work:
  Architecture thematic review
  Code Quality Review
  broad Test Engineering
  Target Architecture
  Remediation Roadmap
  runtime test execution
```

Internal `PRJ-*` identifiers are omitted unless useful to explain a limitation
or confirm an already registered projection. Confirmation is the boundary
between a natural-language candidate and persisted `requested_work`.

## 15. Natural-language normalization

Natural-language requests are first-class input but not authority:

```text
natural language
  → candidate canonical requested_work
  → user-visible confirmation
  → persisted confirmed selection
```

Aliases map to existing canonical work-item identities and never create new
output identities.

| Example request | Candidate normalization |
|---|---|
| “API карта”, “каталог API”, “интерфейсы сервисов” | `Interface Catalog` |
| “Покажи предоставляемые API” | `Provided Interfaces` |
| “Покажи потребляемые API” | `Consumed Interfaces` |
| “Все интеграции” | `Integration Map` |
| “События и сообщения” | `Events / Messages` |
| “Кто пишет в БД”, “доступ к таблицам” | `Data Access Map` |
| “Какие ресурсы хранения есть” | `Persistence / Data Resources` |
| “Кто отвечает за миграции” | `Migration Responsibility` |
| “Внешние интеграции” | `External Integrations Catalog` |
| “Сравни provider и consumer API” | `Provider / Consumer Matrix` |
| “Скажи, совместимы ли provider и consumer” | Matrix plus compatibility request routed to applicable `CC-*` authority |
| “Дай Test Plan” | Test Engineering + `test_plan=true` |
| “Покажи Maintainability Hotspots” | Code Quality Review + `maintainability_hotspots=true` |
| “Сделай Target Architecture” | Architecture Review with `REVIEW_PLUS_TARGET_ARCHITECTURE` |

If a phrase plausibly means materially different outputs, the coordinator
returns `REQUESTED_OUTPUT_AMBIGUOUS` and presents the alternatives. It does not
guess between Interface Catalog and Integration Map, or between a matrix and a
compatibility verdict.

## 16. Product behavior

Product remains explicit opt-in context. The same canonical output identity is
used in Project and Product scope:

```text
output = Interface Catalog
scope = PROJECT | PRODUCT
```

The design does not create separate menu work-item identities such as
`Product Interface Catalog`. “Product Interface Catalog” is a rendering label
for `Interface Catalog` with `scope=PRODUCT` and existing Product-qualified
selectors.

Product-qualified projection state retains:

- accepted Product revision;
- immutable exact Product baseline vector;
- Project/source revision qualification;
- member availability and limitations;
- accepted STM/evidence coverage;
- projection freshness and package status.

Product context alone is not requested work. Selecting Product grants no
repository, source-read, semantic-write, test, code, Git, commit, push, PR, or
deployment permission.

## 17. Single-project behavior

Single-project mode remains the default-compatible route. No Product parent is
required. Every standalone output valid for one Project remains requestable
without Product identity, membership, Product baseline, or cross-project
evidence.

Product-qualified views are additive. They do not make the Project route a
degraded Product route, and Product selection is never inferred from a request
for a normal service catalog.

## 18. Session Intent behavior

### `NEW`

`NEW` may select capabilities, standalone outputs, or both. It must apply the
requested-work validity rule and show resolved-plan confirmation before
substantive work. A zero-capability, non-empty-output request is valid when
every selected output is supported and scoped.

### `USE_EXISTING`

`USE_EXISTING` may consume an accepted/current requested output. It must not
fabricate an output that was never generated, accepted, or registered under the
applicable projection lifecycle. If the user asks for a new output, the route
is `EXTEND`, not a metadata-only `USE_EXISTING` action.

### `RESUME`

`RESUME` restores persisted `requested_work`, resolved dependency/gate state,
and relevant baseline bindings. It does not ask for the entire scope again
unless authority or freshness reconciliation requires it. A materially new
output or capability is an extension, not a silent scope change.

### `REVALIDATE`

`REVALIDATE` preserves previous `requested_work` and revalidates only impacted
semantic, dependency, and projection slices. It does not rerun the complete
Review Suite automatically. A newly requested output routes to `EXTEND`.

### `EXTEND`

`EXTEND` may add a capability, capability-owned output, or standalone output.
Existing requested work is shown read-only; only additions are offered. Fresh
accepted dependencies are reused, and unrelated accepted work is not reopened.
Adding `Data Access Map` to an accepted Architecture session does not reopen
Architecture unless impact evidence requires it for the selected output.

### `PROJECTION_REPAIR`

`PROJECTION_REPAIR` applies to standalone and capability-owned projections when
the correction is presentation-only. It uses existing registered projections,
accepted authority, and `PROJECTION_REVALIDATION`. Semantic drift still returns:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

It cannot hide a source/baseline change, change a provider, alter access or
migration authority, adjudicate compatibility, or create a new semantic fact.

## 19. Projection lifecycle preservation

All standalone outputs continue to use the existing Stage B lifecycle:

```text
PRJ identity
  → owning contract and contract revision
  → semantic/dependency/selector resolution snapshot
  → candidate generation
  → V1 STRUCTURAL
  → V2 DEPENDENCY / PROVENANCE
  → V3 CONTRACT COMPLETENESS
  → V4 AUTHORITY CONSISTENCY
  → canonical fingerprint
  → verified revision
  → CURRENT | STALE | BLOCKED
```

The requested-work record is not a `PRJ-*` record and does not make an output
current. A requested output is not accepted merely because it was requested.
`RG-*` remains the explicit regeneration session. Projection Impact Analysis
accounts for impact and freshness; it does not regenerate content.

## 20. Freshness and revalidation

If the required STM, evidence, coverage, semantic, and projection dependencies
are accepted and fresh, the resolver reuses them. If one required slice is
stale or disputed, it routes only that minimum slice through the owning
revalidation and authority gate. It does not reopen unrelated capability work.

`REVALIDATE` and `EXTEND` persist affected and preserved requested outputs and
their dependency bindings as appropriate. A projection may remain `STALE` after
semantic work until a separate regeneration request; stale projection state is
not semantic falsity.

For Product, the exact accepted Product revision and immutable baseline remain
pinned. Member availability, review coverage, semantic availability,
projection freshness, and package status remain separate dimensions.

## 21. Technical Documentation boundary

Technical Documentation remains the projection owner for its existing
`PRJ-TECH-DOC-*` identities, selectors, section scope, package membership,
redaction rules, and lifecycle dependencies. It is not:

- factual STM authority;
- a semantic review capability;
- compatibility authority;
- Product authority;
- a replacement for Architecture, Test Engineering, or Code Quality.

The new routing layer permits a user to request Technical Documentation or a
focused Stage F output directly. It does not alter how Technical Documentation
accepts facts, resolves selectors, renders limitations, or publishes a
projection.

## 22. Authorization boundary

Selecting a capability or standalone output grants no implicit permission to:

- read additional repositories or external sources;
- select a new revision or admit dirty source;
- write STM, capability semantic records, or Product semantic records;
- generate or publish a projection where separate authorization is required;
- run tests or execute a simulator/environment;
- modify code;
- create or remove worktrees or branches;
- commit, push, create a PR, or deploy.

Each permission remains separately authorized under the existing Product,
evidence, semantic, projection, and execution contracts.

## 23. Runtime boundary

The current Skill remains a review/design/projection workflow. It does not
execute:

- runtime E2E tests;
- Service Simulator runtime;
- environment provisioning;
- runtime database scanning;
- SQL execution;
- distributed tracing;
- external discovery crawling.

Planning and design outputs must continue to say what is planned or designed,
not what was executed. Requests to “run E2E” or “raise the simulator and test
the consumer” normalize to an explicit unsupported-execution explanation plus
any valid planning/design output the user confirms.

## 24. Backward compatibility

The change is additive:

- Architecture-only, Test Engineering-only, Code Quality-only, and every prior
  non-empty capability combination remain valid.
- Product opt-in and Product-free single-project sessions remain valid.
- `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, and `PROJECTION_REPAIR` retain their
  intent identities and existing boundaries.
- Existing capability output booleans remain the authority for capability-owned
  output selection.
- Existing `PRJ-*`, `CC-*`, STM, Evidence, Product, package, and freshness
  identities remain unchanged.
- Existing sessions without explicit standalone-output state are interpreted
  conservatively as having no requested standalone outputs; their existing
  capability selections and accepted package state remain authoritative.
- A legacy session is not silently enriched with new documentation outputs.
  Adding one is an explicit `EXTEND` request.
- No destructive migration of accepted audit packages is required.

If an old compact record cannot distinguish a legacy projection from a current
requested output, authority and revision binding are reconciled through the
existing freshness contract. Ambiguity blocks downstream use rather than
inventing a selection.

## 25. Canonical menu labels

The following conceptual labels close the current startup-label ambiguity while
remaining independent of terminal/widget implementation:

```text
Session Intent
Scope Context
Review Capabilities
Requested Outputs
Resolved Plan / Required Internal Work
Authorization / Execution Boundaries
```

The labels are stable conceptual names. Formal tokens remain exact:
`USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`,
`PROJECTION_REPAIR`, `STANDARD_FULL`, `FORENSIC`, and endpoint/status tokens.

The target configuration shape is:

```text
Session Intent
  <intent and recommendation>

Scope Context
  Single Project | Product <explicit accepted revision/baseline when Product>

Review Capabilities
  [ ] Architecture Review
  [ ] Test Engineering
  [ ] Code Quality Review

Requested Outputs
  capability-owned additions shown under selected capability
  standalone Technical Documentation / Stage F outputs

Resolved Plan / Required Internal Work
  minimum dependency slice and limitations

Authorization / Execution Boundaries
  separately authorized actions and unsupported runtime operations
```

The menu must not present internal Behavior Model, STM, Evidence, or automatic
Contract Verification as user-selected capabilities.

## 26. Failure states

The design uses the following bounded routing outcomes, reusing existing
authority/freshness states wherever they already apply:

| Status | Meaning | Boundary |
|---|---|---|
| `NO_REVIEW_SCOPE_SELECTED` | No capability and no valid standalone output confirmed | Routing validation; Product context alone is insufficient |
| `REQUESTED_OUTPUT_UNSUPPORTED` | Requested output is outside the current supported output taxonomy | Routing validation; no dependency work starts |
| `REQUESTED_OUTPUT_AMBIGUOUS` | Natural-language request maps to materially different outputs | User confirmation required; no silent guess |
| `REQUESTED_WORK_CONFLICT` | Explicit choices conflict, such as endpoint versus normalized target/roadmap request | Reconcile before persistence |
| `DEPENDENCY_RESOLUTION_REQUIRED` | Required accepted/fresh dependency slice is missing, stale, blocked, or authority-unresolved | Owning gate/freshness contract decides block or bounded acquisition |
| `AUTHORIZATION_REQUIRED` | Requested work needs a separate source, semantic-write, projection, test, code, Git, or deploy authorization | No permission inferred from selection |

Existing statuses such as `BLOCKED`, `REVALIDATION_REQUIRED`,
`TECHNICAL_REVALIDATION_REQUIRED`, `SEMANTIC_DRIFT_DETECTED`, and Product
availability limitations retain their current meanings and are not replaced by
these routing outcomes.

## 27. Migration classification

Migration classification: `COMPATIBLE_EXTENSION`.

Reasons:

1. Existing capability choices and endpoint combinations remain valid.
2. Existing semantic authority and ownership are unchanged.
3. Existing projection identities, selectors, package mechanics, and lifecycle
   states are unchanged.
4. New valid requested-work paths are additive: standalone outputs can now be
   requested without artificial capability selection.
5. Existing session state remains interpretable conservatively.
6. Product context remains optional and does not become requested work.
7. No existing accepted result is rewritten or silently enriched.

The classification does not mean implementation is risk-free. Later
implementation must prove compatibility through contract and acceptance
validation before any normative contract is promoted.

## 28. Acceptance matrix

The first twenty scenarios are retained from menu acceptance. The design result
is shown as `PASS` when the requested user outcome is cleanly routed under the
new model.

| ID | Scenario | Expected design route | Result |
|---|---|---|---|
| M01 | Fresh: “Проверь архитектуру проекта.” | `NEW` → Architecture Review → depth/endpoint | PASS |
| M02 | Fresh: “Проверь только качество кода.” | `NEW` → Code Quality Review only | PASS |
| M03 | Fresh: “Анализ тестирования и тест-план.” | `NEW` → Test Engineering + Test Plan | PASS |
| M04 | Full architecture + target, no roadmap | Architecture endpoint `REVIEW_PLUS_TARGET_ARCHITECTURE` | PASS |
| M05 | Forensic audit + roadmap | `FORENSIC` + `REVIEW_PLUS_TARGET_AND_ROADMAP` | PASS |
| M06 | Existing complete, unchanged: show result | `USE_EXISTING` | PASS |
| M07 | Existing complete, source changed: check changes | `REVALIDATE`, impact-driven | PASS |
| M08 | Add Code Quality without rechecking architecture | `EXTEND` adds CQ only | PASS |
| M09 | Broken Mermaid only | `PROJECTION_REPAIR` | PASS |
| M10 | Show provided and consumed APIs | Standalone `Interface Catalog` | PASS |
| M11 | Show DB/table access and writers | Standalone `Data Access Map` | PASS |
| M12 | Show external integrations | Standalone `External Integrations Catalog` | PASS |
| M13 | Product API map | `Integration Map` or `Interface Catalog`, scope `PRODUCT`, after confirmation | PASS |
| M14 | Product data access and migration ownership | `Data Access Map` + `Migration Responsibility`, scope `PRODUCT` | PASS |
| M15 | Product with unavailable repository | Product-qualified output with explicit availability limitations | PASS |
| M16 | “Run E2E tests.” | Unsupported execution; optionally confirm E2E Test Plan | PASS |
| M17 | “Raise simulator and test consumer.” | Unsupported runtime; optionally confirm simulator design/plan | PASS |
| M18 | Compare provider/consumer compatibility | Matrix plus applicable `CC-*` Contract Verification | PASS |
| M19 | Formatting-only report repair | `PROJECTION_REPAIR` | PASS |
| M20 | Interface Catalog without Architecture Review | Zero capabilities + valid standalone output | PASS |

### Focused remediation scenarios

| ID | Scenario | Expected design route | Result |
|---|---|---|---|
| MR01 | Standalone Technical Documentation | `standalone_outputs=[technical_documentation]`; confirm section scope | PASS |
| MR02 | Standalone Interface Catalog | Sections 02 + 03, no capability selected | PASS |
| MR03 | Standalone Integration Map | Section 04, no capability selected | PASS |
| MR04 | Standalone Data Access Map | Section 05, no capability selected | PASS |
| MR05 | Standalone External Integrations Catalog | Section 04 external subsection, section 07 when selected | PASS |
| MR06 | Matrix without compatibility verdict | Render qualified provider/consumer matrix only | PASS |
| MR07 | Matrix plus compatibility question | Matrix plus applicable exact `CC-*` route | PASS |
| MR08 | Product Interface Catalog | Canonical `Interface Catalog`, `scope=PRODUCT`; no duplicate identity | PASS |
| MR09 | No capability and no output | `NO_REVIEW_SCOPE_SELECTED` | PASS |
| MR10 | Product context only | Invalid; Product is not requested work | PASS |
| MR11 | Direct Test Plan request | Normalize to Test Engineering + existing `test_plan` output | PASS |
| MR12 | Direct Target Architecture request | Normalize to Architecture endpoint | PASS |
| MR13 | Interface Catalog must not select Architecture | Standalone output remains capability-free | PASS |
| MR14 | Multiple standalone outputs | Deduplicate Evidence/STM/coverage acquisition | PASS |
| MR15 | EXTEND adds Data Access Map | Add output and minimum slice; preserve Architecture | PASS |
| MR16 | REVALIDATE impacted Data Access slice | Revalidate affected DS/INT/projection only | PASS |
| MR17 | RESUME preserves requested output state | Restore requested and resolved state | PASS |
| MR18 | USE_EXISTING missing requested output | Route to `EXTEND`, do not fabricate output | PASS |
| MR19 | Stage F formatting repair | `PROJECTION_REPAIR` | PASS |
| MR20 | Stage F semantic correction | `SEMANTIC_DRIFT_DETECTED` + `TECHNICAL_REVALIDATION_REQUIRED` | PASS |

Acceptance scenarios: `40` total, `40 PASS` by design.

## 29. Design-level pressure set

| ID | Pressure scenario | Explicit prevention |
|---|---|---|
| MD-P01 | Output-only request rejected by old zero-capability rule | Validity is based on at least one capability OR valid standalone output |
| MD-P02 | Internal STM dependency selects Architecture | Requested capabilities are separate from `resolved_work.dependency_slice` |
| MD-P03 | Target Architecture gets two competing owners | Direct request normalizes into the Architecture endpoint; no standalone Target authority |
| MD-P04 | Test Plan gets two competing owners | Direct request normalizes into Test Engineering `outputs.test_plan` |
| MD-P05 | Product mode counted as requested work | Product context is scope only; it cannot satisfy requested-work validity |
| MD-P06 | Product output receives duplicate identity | Canonical output identity plus `scope=PRODUCT`; reuse existing qualified views |
| MD-P07 | Matrix-only request triggers compatibility verdict | Matrix and compatibility are separate requested outcomes |
| MD-P08 | Compatibility generated without CC authority | Compatibility request requires exact applicable accepted/fresh `CC-*` |
| MD-P09 | Standalone output triggers full Review Suite | Dependency resolution is minimum-slice and cannot escalate to full suite implicitly |
| MD-P10 | Stale DS causes full architecture re-audit | `REVALIDATE` targets affected DS/INT/projection slice only |
| MD-P11 | `USE_EXISTING` fabricates never-generated output | It may consume only accepted/current registered output; new output routes to `EXTEND` |
| MD-P12 | `RESUME` silently changes requested scope | Persisted requested work is restored; additions route to `EXTEND` |
| MD-P13 | `EXTEND` reopens unrelated capability | Existing selections are read-only; dependency impact remains bounded |
| MD-P14 | `PROJECTION_REPAIR` changes semantic provider | Semantic drift gate returns technical revalidation |
| MD-P15 | Runtime E2E request falsely accepted | Planning/execution boundary is explicit; no runtime execution support |
| MD-P16 | Requested output grants test/Git permission | Authorization is separate and recorded as a boundary |
| MD-P17 | Old persisted session becomes unreadable | Legacy state defaults to no standalone outputs and preserves existing capability state |
| MD-P18 | Alias becomes a new output identity | Natural-language aliases normalize only to canonical identities |
| MD-P19 | Conflicting endpoint/output request silently resolved | `REQUESTED_WORK_CONFLICT` requires reconciliation; explicit confirmed choice is preserved |
| MD-P20 | Unclassified secret appears in catalog | Existing Stage F sensitivity classification and redaction rules remain mandatory |

## 30. Finding closure mapping

The design addresses all three findings but does not close them. Closure
requires a later implementation and a fresh menu acceptance review.

| Finding | Root cause | Design mechanism | Expected closure | Later verification |
|---|---|---|---|---|
| `MENU-HIGH-001` | Review Suite validity only counted the three capabilities; standalone Stage F outputs had no requested-work representation | `requested_work.standalone_outputs` plus capability-or-output validity | Interface/API/data catalog can be selected with zero semantic capabilities while retaining existing authority | Fresh M10/M20 acceptance and standalone output routing review |
| `MENU-MEDIUM-001` | Technical Documentation and Product views had semantic selection contracts but no startup/EXTEND entry point | Canonical Requested Outputs menu, scope-aware canonical identities, resolved-plan confirmation | Users can request Project or Product documentation outputs through an explicit route | Fresh M10–M15 and MR01–MR08 acceptance |
| `MENU-LOW-001` | Startup stages were semantically defined but several user-facing labels were not canonical | Stable labels: Session Intent, Scope Context, Review Capabilities, Requested Outputs, Resolved Plan / Required Internal Work, Authorization / Execution Boundaries | Menu reconstruction has stable conceptual labels without UI implementation assumptions | Menu contract review and language/label acceptance |

## 31. Design invariants

| ID | Invariant |
|---|---|
| INV-M01 | At least one requested capability OR valid standalone output is required. |
| INV-M02 | An internal dependency never implies a user-selected capability. |
| INV-M03 | Requested work and resolved work are separate persisted concepts. |
| INV-M04 | Capability-owned output remains owned by its capability. |
| INV-M05 | Standalone Stage F/Technical Documentation output does not require artificial Architecture, Test, or CQ selection. |
| INV-M06 | Technical Documentation remains derived projection owner, not semantic authority. |
| INV-M07 | Product is context, not work item, capability, authority, or permission. |
| INV-M08 | Single-project mode remains first-class. |
| INV-M09 | Compatibility verdict remains `CC-*`-owned. |
| INV-M10 | Provider/Consumer Matrix alone does not adjudicate compatibility. |
| INV-M11 | Stage B projection lifecycle is reused unchanged in meaning. |
| INV-M12 | Output request does not imply automatic regeneration. |
| INV-M13 | Runtime execution remains unsupported. |
| INV-M14 | `EXTEND` and `REVALIDATE` remain minimum-slice and impact-driven. |
| INV-M15 | No existing capability semantics are weakened. |
| INV-M16 | No new factual identity family is introduced. |
| INV-M17 | No secret or sensitive rendering boundary is weakened. |
| INV-M18 | No requested output grants source-read, test, code, Git, or deployment permission. |
| INV-M19 | A natural-language alias never creates a new output identity. |
| INV-M20 | Explicit confirmed choices cannot be silently contradicted by normalization. |
| INV-M21 | Product-qualified outputs retain exact Product revision, baseline, Project qualification, availability, coverage, and freshness. |
| INV-M22 | `USE_EXISTING` cannot fabricate a projection that was never generated and accepted. |

## 32. Scope ownership matrix

| Concern | Owning contract | Changed by this design? | Reason |
|---|---|---:|---|
| Session selection | Session Orchestration / Review Modes | Yes, routing extension | Adds output-aware requested-work selection while preserving six intents |
| Requested work | Session coordinator routing state | Yes | Adds capability/output distinction and validity predicate |
| Architecture semantics | Architecture contracts and endpoint reviews | No | Direct requests normalize into existing endpoint semantics |
| Test Engineering semantics | Test Review and Test Engineering contract | No | Existing output booleans, BC/CC/MAT/TM/GAP authority remain intact |
| Code Quality semantics | Code Quality contracts | No | Existing CQ/CQRA authority and projections remain intact |
| Technical Documentation | Technical Documentation projection contract | Minimal cross-reference only | Adds routing entry point; does not change facts, selectors, packages, or authority |
| Stage F factual semantics | Shared Evidence / STM / Technical Model Gate | No | Existing IF/INT/DS/EVENT/FLOW authority remains sole factual source |
| Product qualification | Product / Multi-Project Review | Minimal cross-reference only | Reuses canonical output IDs with Product scope and existing qualified snapshots |
| Compatibility | Test Engineering Contract Verification / `CC-*` | No | Matrix-only and compatibility requests are separated; CC remains authority |
| Projection lifecycle | Stage B projection lifecycle/dependency/package contracts | No | Standalone outputs reuse `PRJ-*`, V1–V4, fingerprints, freshness, and `RG-*` |
| Freshness/revalidation | Revalidation and Freshness | Minimal cross-reference only | New output requests use `EXTEND`; changed inputs use bounded `REVALIDATE` |
| Authorization | Session/Product/evidence/semantic/execution contracts | No | Selection grants no permission |
| Runtime execution | Test Engineering boundary and roadmap constraints | No | Unsupported runtime remains unsupported |

## 33. Candidate future implementation surface

This design identifies likely contract touchpoints for a later implementation
plan; it does not prescribe line-by-line edits or require every file to change.

Potential primary routing surface:

- `SKILL.md`;
- `references/session-orchestration.md`;
- `references/review-modes-and-orchestration.md`.

Potential bounded cross-references:

- `references/technical-documentation.md`;
- `references/product-multi-project-review.md`;
- `capabilities/test-review/SKILL.md`.

The exact file set, compatibility migration details, and validation commands
must be derived by a later implementation plan. Normative contracts listed in
the task remain unmodified by this design task.

## 34. Self-review

### Placeholder check

No `TODO`, `TBD`, or unresolved placeholder is used as a design dependency.
Terms such as “implementation-defined” are limited to serialization and UI
mechanics that are intentionally outside this design; the semantic rules are
specified.

### Contradiction check

- Capability-owned outputs and standalone outputs are disjoint by ownership.
- Target Architecture and Roadmap remain Architecture endpoint outputs.
- Test Plan and other test documents remain Test Engineering outputs.
- Product is scope, not requested work.
- Matrix-only and compatibility requests have separate routes.
- `USE_EXISTING`, `EXTEND`, `REVALIDATE`, and `PROJECTION_REPAIR` retain their
  existing boundaries.
- Requested work is distinct from resolved dependencies.

### Authority check

No second owner is introduced for STM facts, Evidence observations, `CC-*`,
`CQ-*`, Test Engineering records, Architecture findings, Product meaning, or
`PRJ-*` lifecycle state.

### Migration check

Existing sessions remain interpretable without standalone-output state. New
standalone output requests are additive and explicit.

### Scope check

The design contains no Stage G discovery, runtime execution, implementation
plan, code/UI implementation, tests, or roadmap work.

### Pressure and finding coverage

All material failure pressures have an explicit prevention, and all three menu
findings have a design-address mapping. Findings remain open pending
implementation and fresh acceptance.
