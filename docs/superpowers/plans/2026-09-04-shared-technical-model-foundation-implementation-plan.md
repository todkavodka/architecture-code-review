# Shared Technical Model Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Introduce the approved Shared Evidence Layer and persistent Shared Technical Model (STM), migrate factual As-Built ownership out of Architecture Review, add factual Technical Documentation projections, and make `NEW`, `EXTEND`, and `REVALIDATE` reuse the smallest accepted/fresh technical dependency slice without weakening existing Architecture Review or Test Engineering gates.

**Architecture:** Preserve `SKILL.md` as the thin umbrella orchestrator. Add separate authoritative references for shared evidence, STM semantics, STM coverage, dependency/index semantics, and Technical Documentation. Store authoritative technical state as small semantically addressable artifacts; store direct typed dependencies with each owning artifact; derive reverse/global indexes from that metadata; keep human-readable As-Built and Technical Documentation as projections. Migrate Architecture Review in stages so the old As-Built authority is not silently relabeled as STM authority. Use fail-first pressure scenarios before behavior-changing guidance edits.

**Tech Stack:** Markdown-based ChatGPT/Codex Skill contracts, Git, repository-owned pressure scenarios, existing architecture-code-review orchestration/reference system. No new application runtime, service, database, vector/RAG index, or generic plugin framework.

**Spec:** `docs/superpowers/specs/2026-09-04-shared-technical-model-foundation-design.md`

## Global Constraints

- Design baseline is `main@10233b80eb6a46ff1f8d4348c4be890cf1d1f4a2`. Implementation must start from the then-current verified `main` in a fresh isolated worktree. If `origin/main` has moved and any planned authority/ownership surface changed materially, stop with `STM_IMPLEMENTATION_BASE_DRIFT`; do not automatically rebase, reset, merge, or rewrite history.
- **REQUIRED SUB-SKILLS for implementation:** use `superpowers:using-git-worktrees` before feature work; use `superpowers:test-driven-development` and `superpowers:writing-skills` for Skill/reference changes; use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to execute this plan; use `superpowers:verification-before-completion` before any completion claim.
- No behavior-changing Skill/reference edit may precede the corresponding fail-first pressure observation. Static contract inspection may establish a baseline gap, but it must be labeled as static/contract evidence rather than fabricated runtime evidence.
- No merge to `main`, tag, release, deployment, deletion of existing branches/worktrees, or force-push is authorized by this plan.
- Every `NEW` creates a persistent Shared Technical Model baseline. This does **not** mean every bounded `NEW` builds the complete model immediately.
- A full Architecture Review always requires full STM factual coverage:
  - `STANDARD_FULL` -> `coverage: FULL`, `depth: COMPACT`;
  - `FORENSIC` -> `coverage: FULL`, `depth: FORENSIC`.
- `FULL/FORENSIC` satisfies `FULL/COMPACT`; an upgrade from standard to forensic is enrichment, not a restart.
- Coverage and depth are separate axes. `FULL` is complete bounded material-domain accounting, not exhaustive per-function call-graph extraction.
- Shared Evidence is common across capabilities; interpretation remains capability-owned.
- `Technical Fact != Finding != Risk != Test Gap != Recommendation`.
- Architecture Review must not maintain a parallel factual model once an equivalent STM slice is accepted and fresh.
- Test Engineering keeps its existing semantic authorities (`BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`). STM supplies reusable factual substrate; it does not absorb or rewrite those semantics.
- Preserve `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED` observations without an automatic winner. Authority resolution remains explicit and capability-owned where needed.
- Shared technical facts use a single-writer acceptance boundary: capabilities may emit `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT`, or `TECH_FACT_REVALIDATION_REQUEST`; the Technical Model Gate alone accepts, revises, rejects, or supersedes shared facts.
- Keep lifecycle, freshness, and authority distinct. Persisted does not imply fresh; accepted does not imply complete.
- Authoritative STM state must be split into small semantically addressable artifacts. Do not introduce one monolithic `technical-model.md`.
- `EV-*` remains a logical addressable observation inside bounded `WS-*` worksets by default. Do not create one physical file per evidence observation without a demonstrated need.
- Generated indexes are navigational/impact infrastructure, never substantive semantic authority. They must be reconstructable from authoritative artifact metadata.
- The direct dependency edge is owned by the source artifact; reverse/global dependency indexes are generated projections.
- A changed dependency does not automatically make a dependent semantic claim false. It triggers the dependency-specific impact state (`IMPACT_REVIEW_REQUIRED` or `REVALIDATION_REQUIRED`) according to the accepted impact contract.
- `REVALIDATE` remains impact-driven. Git/path/profile deltas route investigation; they do not prove semantic change and do not automatically rebuild the full STM.
- `EXTEND` reuses accepted/fresh STM slices and builds/revalidates only the minimum new factual dependency slice required by the requested capability/output.
- Technical Documentation is factual analytical documentation from accepted STM. It is **not** onboarding, local setup, “how to run,” “how to modify,” or developer tutorial content.
- Human-readable As-Built and Technical Documentation are projections. Neither becomes technical authority merely because it is newer, longer, or easier to read.
- `TECHNICAL_MODEL_COVERAGE_ACCEPTED` and Architecture `COVERAGE_ACCEPTED` are separate gates answering different questions. Never substitute one for the other.
- Legacy packages with accepted As-Built and no STM are valid legacy state, not corruption. As-Built may seed candidate technical facts, but those facts require evidence/baseline validation before becoming accepted STM authority.
- Do not silently rename/reclassify the old As-Built authority into STM authority.
- Preserve existing Architecture Review candidate verification, root-boundary adjudication, severity, Target Architecture, Remediation Roadmap, final editorial review, `PROJECTION_REPAIR`, and Test Engineering semantics unless an explicit Stage A pressure scenario demonstrates the required integration point.
- Context optimization is subordinate to correctness. Use `INDEX -> semantic artifact -> EV -> raw source`; expand only when accepted/fresh state is insufficient, disputed, or missing.
- Do not implement Stage B projection regeneration, Stage C Test Engineering execution, Stage D Code Quality Review, or Stage E Product/Multi-Project Review in this stage. Stage A may expose stable shared interfaces that those future stages can consume.

---

## Planned File Structure

### Create

- `references/shared-evidence-model.md` — shared `WS-*` / `EV-*` evidence contract, provenance, history, bounded worksets, and cross-capability reuse.
- `references/shared-technical-model.md` — STM entity families, relations, lifecycle/freshness/authority, Technical Model Gate, persistence layout, and mode-independent schema.
- `references/technical-model-coverage.md` — 18-domain coverage model, `FULL/TARGETED`, `COMPACT/FORENSIC`, closeout, review, and downstream gate semantics.
- `references/technical-model-dependencies.md` — direct typed dependency metadata, impact strength, generated reverse indexes, selector dependencies, and context/impact traversal.
- `references/technical-documentation.md` — factual human projection contract from accepted STM.
- `tests/pressure-scenario-90-persistent-stm-bootstrap.md`
- `tests/pressure-scenario-91-architecture-mode-stm-projection.md`
- `tests/pressure-scenario-92-fact-interpretation-authority.md`
- `tests/pressure-scenario-93-shared-evidence-layer.md`
- `tests/pressure-scenario-94-stm-vs-architecture-coverage.md`
- `tests/pressure-scenario-95-hybrid-dependency-graph.md`
- `tests/pressure-scenario-96-stm-extend-revalidate.md`
- `tests/pressure-scenario-97-technical-documentation-projection.md`
- `tests/pressure-scenario-98-as-built-projection-migration.md`
- `tests/pressure-scenario-99-legacy-and-cross-capability-reuse.md`
- `tests/shared-technical-model-foundation-validation.md`

### Modify

- `SKILL.md`
- `references/session-orchestration.md`
- `references/review-modes-and-orchestration.md`
- `references/revalidation-and-freshness.md`
- `references/review-method.md`
- `references/discovery-coverage.md`
- `references/ownership-and-scenarios.md`
- `references/boundary-contract-audit.md`
- `references/report-contract.md`
- `references/shared-assurance-principles.md`
- `capabilities/test-review/SKILL.md`
- `capabilities/test-review/references/test-engineering-contract.md`
- `tests/pressure-validation-matrix.md`
- `README.md`
- `docs/roadmap.md`

### Do not create unless a failing pressure scenario proves necessity

- a database/schema/runtime service for STM;
- a vector/RAG index;
- one file per `EV-*`;
- separate STM schemas for `STANDARD_FULL` and `FORENSIC`;
- duplicate capability-specific copies of shared evidence;
- first-class `ENTRYPOINT-*`, `STATE-*`, `LIFECYCLE-*`, `CONCURRENCY-*`, `DEPLOYMENT-*`, or `OBSERVABILITY-*` families;
- a Code Quality capability;
- a Stage B projection engine.

---

## Task 1: Freeze Stage A fail-first pressure contracts

**Files:**
- Create: `tests/pressure-scenario-90-persistent-stm-bootstrap.md`
- Create: `tests/pressure-scenario-91-architecture-mode-stm-projection.md`
- Create: `tests/pressure-scenario-92-fact-interpretation-authority.md`
- Create: `tests/pressure-scenario-93-shared-evidence-layer.md`
- Create: `tests/pressure-scenario-94-stm-vs-architecture-coverage.md`
- Create: `tests/pressure-scenario-95-hybrid-dependency-graph.md`
- Create: `tests/pressure-scenario-96-stm-extend-revalidate.md`
- Create: `tests/pressure-scenario-97-technical-documentation-projection.md`
- Create: `tests/pressure-scenario-98-as-built-projection-migration.md`
- Create: `tests/pressure-scenario-99-legacy-and-cross-capability-reuse.md`
- Modify: `tests/pressure-validation-matrix.md`

**Interfaces:**
- Consumes: approved Stage A design spec and unchanged production Skill baseline.
- Produces: immutable Stage A RED/GREEN behavioral contracts and verdict tokens used by later tasks.

- [ ] **Step 1: Write PS-90 — persistent STM bootstrap**

Fixture A: `NEW` full Architecture Review. Fixture B: `NEW` bounded capability that requires only a limited factual slice.

Required GREEN behavior:

```text
Every NEW creates a persisted STM baseline.
Full Architecture Review requires FULL STM.
Bounded NEW may create a partial STM and build only required slices.
always create model != always build complete model
```

Forbidden behavior:

- no persisted STM exists after `NEW`;
- bounded `NEW` is forced to build all 18 full domains merely because STM exists;
- STM is represented only as chat state or a final Markdown report.

Verdicts:

```text
PS90_RED_NO_PERSISTENT_STM
PS90_RED_FULL_MODEL_FORCED_FOR_BOUNDED_NEW
PS90_GREEN_PERSISTENT_STM_BOOTSTRAP
PS90_INCONCLUSIVE
```

- [ ] **Step 2: Write PS-91 — Architecture mode -> STM requirement mapping**

Required GREEN behavior:

```text
STANDARD_FULL -> FULL / COMPACT
FORENSIC      -> FULL / FORENSIC
FULL/FORENSIC satisfies FULL/COMPACT
STANDARD_FULL -> FORENSIC is enrichment, not a restart
same STM schema in both modes
```

Both modes must cover all material applicable technical domains; the difference is population depth/evidence granularity/review rigor.

Verdicts:

```text
PS91_RED_STANDARD_NOT_FULL
PS91_RED_SEPARATE_MODE_SCHEMAS
PS91_RED_FORENSIC_RESTART
PS91_GREEN_MODE_PROJECTION
PS91_INCONCLUSIVE
```

- [ ] **Step 3: Write PS-92 — fact/interpretation boundary and single-writer authority**

Fixture includes facts such as `OrdersService synchronously calls PaymentService` and interpretations such as `availability coupling risk`.

Required GREEN behavior:

```text
fact -> STM
architecture judgement -> Architecture Review
assurance judgement -> Test Engineering
code-quality judgement -> future Code Quality
```

Architecture/Test Engineering may emit:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

but may not silently rewrite accepted STM facts.

Verdicts:

```text
PS92_RED_FACT_AND_FINDING_COLLAPSED
PS92_RED_CAPABILITY_REWRITES_STM
PS92_GREEN_FACT_INTERPRETATION_BOUNDARY
PS92_INCONCLUSIVE
```

- [ ] **Step 4: Write PS-93 — shared evidence layer**

Required GREEN behavior:

- shared cross-capability `WS-*` worksets;
- logical globally addressable `EV-*` observations inside worksets;
- baseline/provenance binding;
- old evidence remains historical evidence after HEAD changes;
- capability semantics may reference the same evidence without duplicating it;
- normal retrieval order is index -> semantic object -> evidence -> raw source.

Forbidden behavior:

- separate architecture/test evidence silos for the same observation;
- treating an `EV-*` as a finding or accepted technical fact;
- rewriting old evidence to match a new baseline;
- requiring one physical Markdown file per EV record.

Verdicts:

```text
PS93_RED_EVIDENCE_SILOED_OR_REWRITTEN
PS93_RED_EVIDENCE_BECOMES_SEMANTIC_AUTHORITY
PS93_GREEN_SHARED_EVIDENCE_LAYER
PS93_INCONCLUSIVE
```

- [ ] **Step 5: Write PS-94 — STM coverage and Architecture coverage separation**

Required order for full Architecture Review:

```text
Shared Evidence
-> FULL STM
-> STM Coverage Review
-> TECHNICAL_MODEL_COVERAGE_ACCEPTED
-> Architecture thematic discovery
-> Architecture Discovery Coverage
-> COVERAGE_ACCEPTED
-> candidate verification
```

Required distinction:

```text
STM coverage: factual system surface completeness
Architecture coverage: material architecture/risk mechanism analysis completeness
```

Verdicts:

```text
PS94_RED_COVERAGE_MODELS_COLLAPSED
PS94_RED_ARCHITECTURE_STARTS_WITH_UNACCEPTED_FULL_STM
PS94_GREEN_COVERAGE_SEPARATION
PS94_INCONCLUSIVE
```

- [ ] **Step 6: Write PS-95 — hybrid dependency graph**

Required GREEN behavior:

- each authoritative artifact owns direct outbound typed dependencies;
- generated central indexes provide reverse and aggregate traversal;
- index loss/staleness is repairable from authoritative metadata;
- direct semantic dependency metadata is not reconstructed from an index as authority;
- dependency change triggers impact assessment/revalidation according to impact strength, not automatic falsification;
- projections may depend on explicit IDs and selector/set dependencies so newly created matching objects can make a projection stale.

Minimum initial dependency vocabulary in the scenario:

```text
EVIDENCED_BY
DERIVED_FROM
DEPENDS_ON
REFERENCES
SUPERSEDES
PROJECTS_FROM
```

Minimum impact vocabulary:

```text
HARD
CONDITIONAL
INFORMATIONAL
```

Verdicts:

```text
PS95_RED_INDEX_BECOMES_AUTHORITY
PS95_RED_DEPENDENCY_CHANGE_MEANS_FALSE
PS95_RED_NEW_OBJECT_NOT_SEEN_BY_PROJECTION_SELECTOR
PS95_GREEN_HYBRID_DEPENDENCY_GRAPH
PS95_INCONCLUSIVE
```

- [ ] **Step 7: Write PS-96 — incremental EXTEND and REVALIDATE**

Fixture A: accepted full/compact STM + later Test Engineering `EXTEND` requires only interfaces/errors/test-relevant views.
Fixture B: a source change touches one accepted interaction and one flow.
Fixture C: `STANDARD_FULL` accepted model is upgraded to `FORENSIC`.

Required GREEN behavior:

```text
EXTEND -> reuse accepted+VALID slices; build/revalidate only missing/stale required slice
REVALIDATE -> diff routes affected evidence/facts/aspects; no whole-STM replay without impact evidence
COMPACT -> FORENSIC -> enrich affected/all required depth gaps, preserve accepted facts where still valid
```

Verdicts:

```text
PS96_RED_FULL_STM_REPLAY_ON_EXTEND
PS96_RED_GLOBAL_STM_REVALIDATION
PS96_RED_FORENSIC_RESTART
PS96_GREEN_STM_INCREMENTAL_REUSE
PS96_INCONCLUSIVE
```

- [ ] **Step 8: Write PS-97 — Technical Documentation projection**

Required GREEN behavior:

- technical docs are generated/synthesized from accepted STM facts;
- they are human-readable factual projections and do not become semantic authority;
- docs may cover system overview, components, provided/consumed interfaces, integrations, data/persistence, runtime/deployment, auth/trust, material flows, and failure behavior;
- docs do **not** introduce onboarding, local setup, “how to run,” “how to change,” or tutorial semantics as Stage A scope;
- a projection cannot resolve a factual authority conflict by prose.

Verdicts:

```text
PS97_RED_DOCUMENTATION_BECOMES_AUTHORITY
PS97_RED_DEVELOPER_HOWTO_SCOPE
PS97_RED_PROJECTION_RESOLVES_FACT_CONFLICT
PS97_GREEN_TECHNICAL_DOCUMENTATION_PROJECTION
PS97_INCONCLUSIVE
```

- [ ] **Step 9: Write PS-98 — As-Built authority migration**

Required GREEN behavior:

```text
accepted STM = factual technical authority
As-Built Architecture = human-readable projection
Architecture Review consumes accepted/fresh STM
```

A thematic architecture pass that sees conflicting factual evidence must emit `TECH_FACT_CONFLICT` rather than silently changing As-Built/STM.

The migration must preserve the material factual content currently required by As-Built; removing old authority does not permit losing topology/ownership/boundary/flow/lifecycle/etc. coverage.

Verdicts:

```text
PS98_RED_DUAL_FACTUAL_AUTHORITY
PS98_RED_AS_BUILT_STILL_SOURCE_OF_TRUTH
PS98_RED_FACTUAL_PARITY_LOST
PS98_GREEN_AS_BUILT_PROJECTION_MIGRATION
PS98_INCONCLUSIVE
```

- [ ] **Step 10: Write PS-99 — legacy reconciliation and cross-capability reuse**

Case A: legacy `COMPLETE` package has accepted As-Built, no STM, same baseline.
Case B: Test Engineering is attached after STM exists.

Required GREEN behavior:

```text
legacy As-Built -> candidate STM seed only -> evidence/baseline validation -> accepted STM
```

and:

```text
Test Engineering -> reuse relevant accepted STM facts -> preserve BC/CC/MAT/TM/GAP ownership
```

Forbidden:

- relabel old As-Built as accepted STM without evidence validation;
- mark legacy package corrupt solely because STM is absent;
- make STM replace Behavior Contracts or Test Assurance semantics;
- reread/reconstruct technical surface independently when accepted fresh STM already supplies it, absent a correctness trigger.

Verdicts:

```text
PS99_RED_LEGACY_AS_BUILT_SILENTLY_PROMOTED
PS99_RED_STM_ABSORBS_TEST_ENGINEERING
PS99_RED_DUPLICATE_CROSS_CAPABILITY_DISCOVERY
PS99_GREEN_LEGACY_AND_CROSS_CAPABILITY_REUSE
PS99_INCONCLUSIVE
```

- [ ] **Step 11: Register PS-90..99 in `tests/pressure-validation-matrix.md`**

Add scenario locations, mandatory evidence, PASS criteria, and applicable global forbidden behaviors:

```text
- a capability silently mutates accepted STM facts;
- Architecture Review maintains a second factual model after STM migration;
- `FULL` Architecture Review proceeds without accepted required STM coverage;
- generated dependency/index state is treated as semantic authority;
- Technical Documentation changes factual semantics;
- legacy As-Built is silently relabeled as accepted STM;
- `EXTEND`/`REVALIDATE` globally replay accepted STM without impact evidence;
```

- [ ] **Step 12: Run fail-first baseline observations against unchanged `main`**

Use fresh independent Skill contexts against the verified pre-Stage-A baseline. At minimum run representative probes for PS-90, PS-91, PS-92, PS-94, PS-97, PS-98, and PS-99. Use static contract checks for parts that cannot be executed by a repository runtime and label them accurately.

If a scenario already passes current guidance, record baseline-compliant behavior rather than inventing a RED. The later implementation must not add redundant/conflicting guidance merely to force a narrative of change.

If no credible fail-first evidence can be obtained for a behavior that would require a Skill guidance edit, stop that edit and record `STM_RED_EVIDENCE_REQUIRED`.

- [ ] **Step 13: Commit pressure contracts before production guidance edits**

Verify:

```bash
git diff --check
git diff -- SKILL.md references/ capabilities/
git status --short
```

Expected before commit: Stage A pressure tests/matrix only; no production Skill/reference changes.

Commit:

```bash
git add tests/pressure-scenario-90-*.md \
        tests/pressure-scenario-91-*.md \
        tests/pressure-scenario-92-*.md \
        tests/pressure-scenario-93-*.md \
        tests/pressure-scenario-94-*.md \
        tests/pressure-scenario-95-*.md \
        tests/pressure-scenario-96-*.md \
        tests/pressure-scenario-97-*.md \
        tests/pressure-scenario-98-*.md \
        tests/pressure-scenario-99-*.md \
        tests/pressure-validation-matrix.md
git commit -m "test: define Shared Technical Model pressure contracts"
```

---

## Task 2: Add the Shared Evidence authority

**Files:**
- Create: `references/shared-evidence-model.md`
- Modify: `references/shared-assurance-principles.md` only for the minimal cross-capability pointer/invariant needed to establish shared evidence reuse.
- Modify: `SKILL.md` only to add the authority-map routing entry when the reference is ready.

**Interfaces:**
- Consumes: raw repository/external sources and baseline identity.
- Produces: baseline-bound shared `WS-*` worksets containing addressable `EV-*` observations for STM and capability consumers.

- [ ] **Step 1: Define Shared Evidence ownership**

`shared-evidence-model.md` must state:

```text
WS-* = bounded investigation/workset and physical evidence grouping
EV-* = logical addressable observation within a WS
```

Evidence records are observations, not findings, technical facts, Behavior Contracts, or assurance targets.

- [ ] **Step 2: Define minimum Workset contract**

Required fields/concepts:

```text
id
name
scope
baseline / baseline_type
status
investigated_sources
limitations
EV records
HANDOFF SUMMARY
```

Use existing one-active-writer and persisted handoff discipline.

- [ ] **Step 3: Define minimum EV contract**

Required concepts:

```text
EV id
source type
repository/path
symbol or range when available
baseline binding
observed fact/behavior
optional short excerpt only when useful
```

Do not duplicate large source blocks. Raw source remains the ultimate source and is reopened when evidence is insufficient/disputed/stale for the current decision.

- [ ] **Step 4: Define historical evidence semantics**

Old `EV-*` remains evidence of the baseline at which it was observed. A new baseline creates new observations as needed; do not rewrite old observations to make history look current.

- [ ] **Step 5: Define shared reuse and reading hierarchy**

```text
INDEX
-> semantic artifact
-> WS#EV
-> raw source
```

Capabilities may add new shared evidence worksets, but capability-specific conclusions remain in capability-owned semantic artifacts.

- [ ] **Step 6: Re-run PS-93**

Expected: `PS93_GREEN_SHARED_EVIDENCE_LAYER`.

- [ ] **Step 7: Commit Shared Evidence contract**

```bash
git add references/shared-evidence-model.md references/shared-assurance-principles.md SKILL.md
git commit -m "feat: define shared evidence layer"
```

---

## Task 3: Add the Shared Technical Model semantic contract and persistence model

**Files:**
- Create: `references/shared-technical-model.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/session-orchestration.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: accepted/bounded shared evidence.
- Produces: persistent accepted factual artifacts, revision/freshness state, model manifest, and Technical Model Gate behavior.

- [ ] **Step 1: Define first-class STM families**

Use exactly the approved initial families:

```text
COMP-*    Component / Runtime Unit
IF-*      Interface
INT-*     Interaction
DS-*      Data Store
EVENT-*   Event / Message
FLOW-*    Material Flow
AUTH-*    Auth / Trust Boundary
CFG-*     Configuration Fact
ERR-*     Error / Failure Contract
```

Do not create one component per trivial class/function. Preserve materiality.

- [ ] **Step 2: Define controlled relation vocabulary**

Initial vocabulary:

```text
PROVIDES
CONSUMES
CALLS
PUBLISHES
SUBSCRIBES
READS_FROM
WRITES_TO
OWNS_STATE
PROTECTED_BY
CONFIGURED_BY
EMITS_ERROR
PARTICIPATES_IN
DEPLOYS_AS
DEPENDS_ON
```

Relations are semantically meaningful links even if physically stored as object metadata.

- [ ] **Step 3: Define intentionally embedded concerns**

Do not introduce first-class families for these initially:

```text
ENTRYPOINT
STATE
LIFECYCLE
CONCURRENCY
DEPLOYMENT
OBSERVABILITY
```

Represent them using properties/relations on accepted first-class artifacts until repeated cross-capability usage justifies promotion.

- [ ] **Step 4: Define fact lifecycle/freshness/authority**

Use separate axes:

```text
status:
  CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED

freshness:
  VALID | REVALIDATION_REQUIRED | UNKNOWN

authority where applicable:
  RESOLVED | UNRESOLVED
```

Define stable identity/revisions such as `IF-021@rev3` and `supersedes` links.

- [ ] **Step 5: Define multi-view observations**

STM may preserve:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

without imposing source precedence. Explicitly state that STM stores observed representations; contract authority adjudication remains outside a projection and may be delegated to an appropriate specialist gate.

- [ ] **Step 6: Define Technical Model Gate sole-writer rules**

Only the gate accepts/revises/rejects/supersedes shared facts. Other capabilities emit:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

A capability may continue within an unaffected bounded scope while the conflicting fact/dependency is reconciled, but it may not use a disputed required fact as accepted downstream truth.

- [ ] **Step 7: Define physical persisted package shape**

Specify a recommended structure such as:

```text
working/
  evidence/
    INDEX.md
    WS-*.md
  technical-model/
    INDEX.md
    coverage.md
    components/COMP-*.md
    interfaces/IF-*.md
    interactions/INT-*.md
    data-stores/DS-*.md
    events/EVENT-*.md
    flows/FLOW-*.md
    auth/AUTH-*.md
    errors/ERR-*.md
    configuration/CFG-*.md
  indexes/
    ... generated projections ...
```

Paths are a recommended convention; semantic ownership/revision binding is the invariant.

- [ ] **Step 8: Add STM bootstrap to `NEW` orchestration**

`NEW` flow must create the persistent STM baseline before capability execution. Full model population depends on selected downstream requirements.

`INDEX.md` compact projection should gain minimum STM routing fields such as:

```text
technical_model:
  owning_manifest
  model_revision
  baseline
  coverage_requirement
  depth_requirement
  coverage_status
  freshness
```

Do not put the actual technical model into `INDEX.md`.

- [ ] **Step 9: Re-run PS-90 and PS-92**

Expected:

```text
PS90_GREEN_PERSISTENT_STM_BOOTSTRAP
PS92_GREEN_FACT_INTERPRETATION_BOUNDARY
```

- [ ] **Step 10: Commit STM semantic foundation**

```bash
git add references/shared-technical-model.md \
        references/review-modes-and-orchestration.md \
        references/session-orchestration.md \
        SKILL.md
git commit -m "feat: define Shared Technical Model authority"
```

---

## Task 4: Add STM coverage and `STANDARD_FULL` / `FORENSIC` projection rules

**Files:**
- Create: `references/technical-model-coverage.md`
- Modify: `references/session-orchestration.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/shared-assurance-principles.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: STM facts/slices plus the selected downstream review/capability scope.
- Produces: bounded technical-domain accounting and `TECHNICAL_MODEL_COVERAGE_ACCEPTED` gate.

- [ ] **Step 1: Define the 18 full technical domains**

Use the approved domains exactly:

```text
1. System Context
2. Components / Runtime Units
3. Entry Points
4. Provided Interfaces
5. Consumed Interfaces
6. Interactions
7. Events / Messaging
8. Data Stores / Persistence
9. State Ownership
10. Material Flows
11. Lifecycle / State Machines
12. Authentication / Authorization / Trust
13. Error / Failure Contracts
14. Configuration Surface
15. Concurrency / Serialization / Idempotency Mechanisms
16. Deployment / Runtime Topology
17. Observability Mechanisms
18. Platform-Specific Behavior
```

- [ ] **Step 2: Define coverage states**

Use a closed vocabulary:

```text
PENDING
IN_PROGRESS
ACCEPTED
PARTIAL
BLOCKED
NOT_APPLICABLE
UNKNOWN
```

`PARTIAL`, `BLOCKED`, and `UNKNOWN` are not complete. Require evidence-based reason plus downstream impact for non-accepted terminal/non-terminal states.

- [ ] **Step 3: Define `FULL` semantics**

`FULL` means every material applicable domain is bounded and classified with sufficient evidence for the requested depth. It does not require a record for every private helper/function.

For interfaces/interactions, `FULL` means all known material externally visible or architecturally relevant surfaces within the evidence-bounded scope.

- [ ] **Step 4: Define mode mapping**

```text
STANDARD_FULL:
  coverage: FULL
  depth: COMPACT
  evidence: MATERIAL
  flows: REPRESENTATIVE
  contradictions: MATERIAL
  review: full-model independent review

FORENSIC:
  coverage: FULL
  depth: FORENSIC
  evidence: GRANULAR
  flows: MECHANISM_COMPLETE_WHERE_MATERIAL
  contradictions: EXPLICIT_MULTI_VIEW
  review: critical-slice review where material + full-model integration review
```

Preserve one schema.

- [ ] **Step 5: Define Technical Model Coverage review gate**

For a full architecture review, capability execution requiring complete factual substrate is blocked until required technical coverage is accepted. Do not let a prose reviewer verdict override `PARTIAL/BLOCKED/UNKNOWN` rows without correction/re-review.

- [ ] **Step 6: Keep Architecture Discovery Coverage separate**

Add explicit cross-reference only; do not move `ARCH/SEC/DATA/REL/OPS/COMP/QUAL` mechanism analysis into STM coverage.

- [ ] **Step 7: Re-run PS-91 and PS-94**

Expected:

```text
PS91_GREEN_MODE_PROJECTION
PS94_GREEN_COVERAGE_SEPARATION
```

- [ ] **Step 8: Commit coverage model**

```bash
git add references/technical-model-coverage.md \
        references/session-orchestration.md \
        references/review-modes-and-orchestration.md \
        references/shared-assurance-principles.md \
        SKILL.md
git commit -m "feat: add Shared Technical Model coverage gate"
```

---

## Task 5: Add hybrid dependency/index and impact semantics

**Files:**
- Create: `references/technical-model-dependencies.md`
- Modify: `references/revalidation-and-freshness.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/shared-technical-model.md`

**Interfaces:**
- Consumes: authoritative evidence/STM/capability artifact metadata and projection selectors.
- Produces: direct dependency authority, generated reverse indexes, bounded context retrieval, and impact propagation.

- [ ] **Step 1: Define typed direct dependencies**

Initial edge vocabulary:

```text
EVIDENCED_BY
DERIVED_FROM
DEPENDS_ON
REFERENCES
SUPERSEDES
PROJECTS_FROM
```

Clarify semantic differences; especially keep `SUPERSEDES` as revision/history relation rather than ordinary invalidation dependency.

- [ ] **Step 2: Define impact strength**

Initial impact vocabulary:

```text
HARD
CONDITIONAL
INFORMATIONAL
```

Required behavior:

```text
HARD change -> REVALIDATION_REQUIRED for dependent semantic use
CONDITIONAL change -> IMPACT_REVIEW_REQUIRED
INFORMATIONAL change -> no semantic invalidation by default
```

This is an impact-routing default, not proof that a dependent conclusion changed.

- [ ] **Step 3: Define artifact-level first implementation with extensible aspects**

Allow optional future shape such as:

```text
dependency:
  artifact: IF-021
  aspects: [auth, responses]
```

but do not require field-level dependency completeness in the first implementation. The first accepted implementation may remain artifact-level if the schema leaves a safe extension path.

- [ ] **Step 4: Define generated indexes**

Require reproducible generated projections for at least:

```text
artifact registry
reverse dependencies
capability/dependency lookup
stale/impact lookup
projection dependencies
```

Exact file names may follow repository convention. Index content must be reconstructable from authoritative metadata.

- [ ] **Step 5: Define projection selector dependencies**

Support both:

```text
explicit object IDs
selector/set dependency
```

Example: “all STM interfaces where direction=CONSUMED.” A newly accepted matching object can stale/regenerate a projection even if that object did not exist at the previous projection revision.

- [ ] **Step 6: Integrate dependency traversal with context orchestration**

A bounded agent should be able to request conceptually:

```text
current semantic object
+ HARD dependencies
+ unresolved CONDITIONAL dependencies
+ required evidence
```

without loading unrelated accepted artifacts.

- [ ] **Step 7: Integrate with `REVALIDATE`**

Route:

```text
changed source/baseline
-> affected EV/STM candidates
-> affected direct dependencies/aspects
-> impact traversal
-> only affected capability semantics/projections
```

Unknown linkage triggers targeted investigation, not a false “preserved” conclusion.

- [ ] **Step 8: Re-run PS-95 and PS-96**

Expected:

```text
PS95_GREEN_HYBRID_DEPENDENCY_GRAPH
PS96_GREEN_STM_INCREMENTAL_REUSE
```

- [ ] **Step 9: Commit dependency/impact model**

```bash
git add references/technical-model-dependencies.md \
        references/revalidation-and-freshness.md \
        references/review-modes-and-orchestration.md \
        references/shared-technical-model.md
git commit -m "feat: add Shared Technical Model dependency graph"
```

---

## Task 6: Add Technical Documentation as the first human projection of STM

**Files:**
- Create: `references/technical-documentation.md`
- Modify: `references/report-contract.md`
- Modify: `references/session-orchestration.md` only if startup/output routing needs an explicit Technical Documentation selection/endpoint according to the approved design.
- Modify: `README.md` later only after the technical contract is GREEN; avoid duplicating detailed rules prematurely.

**Interfaces:**
- Consumes: accepted/fresh STM facts and required technical-domain coverage.
- Produces: human-readable factual documentation optimized for comprehension, not authority.

- [ ] **Step 1: Define purpose and forbidden scope**

Technical Documentation documents verified technical facts such as system/component/interface/integration/data/runtime/auth/flow/failure structure.

Explicitly exclude from Stage A output ownership:

```text
onboarding tutorials
local environment setup instructions
how to run the application
how to modify/extend code
step-by-step developer guides
```

Configuration facts may be documented as behaviorally relevant facts; this does not turn them into setup instructions.

- [ ] **Step 2: Define projection source rules**

Only accepted/fresh required STM authority may be synthesized as current fact. `PARTIAL`, `UNKNOWN`, unresolved views, and limitations remain visible and are not normalized into certainty by prose.

- [ ] **Step 3: Define recommended document projections**

Permit a human package such as:

```text
00-system-overview.md
01-components.md
02-provided-interfaces.md
03-consumed-interfaces.md
04-integrations.md
05-data-and-persistence.md
06-runtime-and-deployment.md
07-auth-and-trust.md
08-material-flows.md
09-failure-behavior.md
```

This is a projection taxonomy, not semantic authority and not necessarily a mandatory physical file per section for every project.

- [ ] **Step 4: Define human synthesis quality**

Use coherent prose, tables, cross-links, and Mermaid when useful. Internal IDs support traceability but must not replace explanation. A human document may summarize multiple STM artifacts without copying every evidence record.

- [ ] **Step 5: Define projection dependency metadata**

Technical Documentation must declare/record enough `PROJECTS_FROM` selector/object dependencies to become an input to future Stage B regeneration.

Do not implement the Stage B regeneration engine here.

- [ ] **Step 6: Re-run PS-97**

Expected: `PS97_GREEN_TECHNICAL_DOCUMENTATION_PROJECTION`.

- [ ] **Step 7: Commit Technical Documentation contract**

```bash
git add references/technical-documentation.md references/report-contract.md references/session-orchestration.md
git commit -m "feat: define technical documentation projection"
```

---

## Task 7: Migrate As-Built from factual authority to STM projection

**Files:**
- Modify: `SKILL.md`
- Modify: `references/review-method.md`
- Modify: `references/report-contract.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/ownership-and-scenarios.md`
- Modify: `references/boundary-contract-audit.md`
- Modify: `references/shared-technical-model.md`

**Interfaces:**
- Consumes: accepted required STM facts/coverage.
- Produces: Architecture Review that uses STM as factual source, plus human-readable As-Built projection with factual parity.

- [ ] **Step 1: Replace the root `SKILL.md` factual authority statement**

Current invariant “Technical As-Built working file — source of truth” must become an STM authority rule.

Required future invariant:

```text
Accepted Shared Technical Model = factual technical authority.
Human-readable As-Built = projection of accepted STM plus architecture-oriented synthesis.
```

Keep `SKILL.md` thin; detailed rules belong in shared references.

- [ ] **Step 2: Rewrite the Required Review Flow boundary, not the whole method**

For a full review:

```text
baseline/session orchestration
-> required Shared Evidence/STM build
-> independent STM coverage/review gate
-> accepted full STM
-> Architecture thematic discovery
-> Architecture coverage closeout
-> candidate verification/root/severity
-> projections
```

Do not remove existing post-discovery verification/adjudication gates.

- [ ] **Step 3: Preserve existing As-Built factual requirements as STM coverage/content**

Map current As-Built material content into STM facts/coverage. Ensure migration preserves at least:

```text
purpose/key scenarios
runtime/deployment topology
state ownership/authority facts
API/IPC/process/persistence/trust boundaries
command/read/async/external flows
state/lifecycle transitions
startup/readiness/shutdown/retry/recovery
concurrency/shared-state/serialization/idempotency mechanisms
failure/partial-failure mechanics
auth/authz/trust mechanisms
configuration/secrets surface
persistence/migration/consistency mechanisms
observability mechanisms
platform-specific behavior
```

Architecture properties/judgements remain Architecture-owned.

- [ ] **Step 4: Split ownership matrices**

`ownership-and-scenarios.md` should treat owner/writers/readers/lifetime/scope as factual STM material. Architectural invariants, adverse-scenario interpretation, race conclusions, and `SER-*` remain Architecture-owned.

Do not make a factual owner/writer matrix itself a finding.

- [ ] **Step 5: Split boundary facts from boundary analysis**

`boundary-contract-audit.md` should consume factual boundary objects/views from STM where accepted/fresh, then analyze identity/correlation/order/concurrency/cancel/auth/validation/etc. quality. It may request missing factual expansion but must not silently maintain a parallel boundary inventory.

- [ ] **Step 6: Generalize factual correction protocol**

Replace factual As-Built correction ownership with:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

Preserve architecture-specific correction/adjudication where the change is genuinely an architectural interpretation rather than a factual STM correction.

- [ ] **Step 7: Keep As-Built as a useful substantial human projection**

Do not degrade the human report. It should still allow a technical lead to understand the factual system without manually opening the source tree, but its facts are traceable to STM authority rather than being a competing authority.

- [ ] **Step 8: Re-run PS-92 and PS-98**

Expected:

```text
PS92_GREEN_FACT_INTERPRETATION_BOUNDARY
PS98_GREEN_AS_BUILT_PROJECTION_MIGRATION
```

Also run regression canaries covering existing As-Built completeness, independent review, correction boundaries, context orchestration, and long-run authority integrity (including applicable existing PS-9, PS-10, PS-14, PS-39..43, PS-54, PS-56).

- [ ] **Step 9: Commit As-Built/Architecture ownership migration**

```bash
git add SKILL.md \
        references/review-method.md \
        references/report-contract.md \
        references/review-modes-and-orchestration.md \
        references/ownership-and-scenarios.md \
        references/boundary-contract-audit.md \
        references/shared-technical-model.md
git commit -m "refactor: make architecture review consume Shared Technical Model"
```

---

## Task 8: Split Technical Model Coverage from Architecture Discovery Coverage cleanly

**Files:**
- Modify: `references/discovery-coverage.md`
- Modify: `references/technical-model-coverage.md`
- Modify: `references/review-method.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: accepted STM coverage plus Architecture thematic discovery artifacts.
- Produces: two independent completeness authorities with explicit sequencing and no duplicated domain ownership.

- [ ] **Step 1: Preserve current Architecture Discovery Coverage taxonomy**

Keep current mechanism-oriented domains (`ARCH-*`, `SEC-*`, `DATA-*`, `REL-*`, `OPS-*`, `COMP-*`, `QUAL-*`) as Architecture Review coverage.

Do not rename STM technical domains into security/risk domains.

- [ ] **Step 2: Define explicit cross-gate sequencing**

For full Architecture Review:

```text
TECHNICAL_MODEL_COVERAGE_ACCEPTED
required before architecture thematic analysis claims the full factual substrate

COVERAGE_ACCEPTED
required before candidate verification
```

A targeted/bounded capability may have a targeted STM requirement rather than a full-model gate.

- [ ] **Step 3: Preserve independent review roles**

`STANDARD_FULL` may use a compact full-model independent STM review plus existing Architecture coverage closeout. `FORENSIC` uses granular/critical STM slice review where material plus the existing explicit independent Architecture Coverage Review.

Do not let the same review artifact self-accept both factual completeness and architectural risk completeness without an explicit independent role boundary.

- [ ] **Step 4: Define blocked/partial semantics**

A required STM domain `PARTIAL/BLOCKED/UNKNOWN` cannot be hidden by Architecture `COVERAGE_ACCEPTED`; conversely, accepted STM factual coverage does not prove the architecture/security/reliability mechanisms were analyzed.

- [ ] **Step 5: Re-run PS-94 plus existing Discovery Coverage regression scenarios**

Expected Stage A: `PS94_GREEN_COVERAGE_SEPARATION`.

Also rerun representative Discovery Coverage canaries, especially the authority-integrity and high-risk mechanism cases currently registered in the matrix.

- [ ] **Step 6: Commit coverage split integration**

```bash
git add references/discovery-coverage.md \
        references/technical-model-coverage.md \
        references/review-method.md \
        references/review-modes-and-orchestration.md \
        SKILL.md
git commit -m "refactor: separate technical and architecture coverage gates"
```

---

## Task 9: Make Test Engineering consume STM without changing Test Engineering authority

**Files:**
- Modify: `capabilities/test-review/SKILL.md`
- Modify: `capabilities/test-review/references/test-engineering-contract.md`
- Modify: `references/revalidation-and-freshness.md` only if required for shared dependency routing.
- Modify: `references/review-modes-and-orchestration.md` only if capability dependency registration requires it.

**Interfaces:**
- Consumes: accepted/fresh STM factual slices plus Test Engineering's existing source/behavior evidence.
- Produces: smaller factual discovery context while preserving `BC/CC/MAT/TM/GAP` ownership and minimum dependency slicing.

- [ ] **Step 1: Replace “accepted architecture as factual substrate” dependency where appropriate**

Test Engineering should reuse accepted STM facts for components/interfaces/interactions/stores/auth/error/config/flow topology instead of reconstructing them from the As-Built projection.

Architecture `RF-*` may still motivate behavior contracts where the architecture finding itself is semantically relevant.

- [ ] **Step 2: Preserve Behavior Model ownership**

A technical interface fact such as `IF-021` does not become a `BC-*`. Behavior Model still defines independently verifiable behavior.

Keep:

```text
BC != IF/INT/FLOW
BC != MAT
BC != RF
BC != GAP
```

- [ ] **Step 3: Preserve Contract Verification ownership**

STM may carry observed `DECLARED/IMPLEMENTED/CONSUMED/TESTED` technical views. `CC-*` still owns contract mismatch classification/adjudication within Test Engineering. STM must not automatically classify `DECLARATION_STALE`, `IMPLEMENTATION_DEFECT`, etc.

- [ ] **Step 4: Integrate dependency-sliced reuse**

Test Engineering `EXTEND` should first query/reuse relevant accepted/fresh STM dependencies. It requests new technical discovery only when a required slice is missing/stale/disputed.

- [ ] **Step 5: Integrate revalidation**

Tests-only changes continue to affect `TM/MAT/GAP` first; implementation/declared/consumer changes may affect both STM technical views and downstream `CC/BC` according to dependency impact. Do not globally invalidate all Test Engineering semantics merely because one STM artifact changed.

- [ ] **Step 6: Re-run PS-99 and Test Engineering PS-81..89 compatibility suite**

Expected Stage A: `PS99_GREEN_LEGACY_AND_CROSS_CAPABILITY_REUSE`.

Required regressions: PS81–PS89 remain GREEN; no modern NEW/EXTEND output UX regression.

- [ ] **Step 7: Commit Test Engineering adoption**

```bash
git add capabilities/test-review/SKILL.md \
        capabilities/test-review/references/test-engineering-contract.md \
        references/revalidation-and-freshness.md \
        references/review-modes-and-orchestration.md
git commit -m "refactor: reuse Shared Technical Model in Test Engineering"
```

---

## Task 10: Add legacy STM reconciliation and session lifecycle integration

**Files:**
- Modify: `references/session-orchestration.md`
- Modify: `references/revalidation-and-freshness.md`
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `references/shared-technical-model.md`

**Interfaces:**
- Consumes: legacy audit package or persisted STM plus current session intent/baseline.
- Produces: conservative `RESUME/EXTEND/REVALIDATE/USE_EXISTING` routing without silent semantic promotion.

- [ ] **Step 1: Define legacy package detection**

Legacy condition:

```text
accepted As-Built exists
STM absent
```

This is supported legacy state.

- [ ] **Step 2: Define conservative backfill**

Allowed flow:

```text
legacy accepted As-Built
-> candidate technical extraction
-> locate/reuse original evidence where available
-> targeted source verification where required
-> bind to referenced/current baseline as appropriate
-> Technical Model Gate review
-> accepted STM facts
```

Do not mark facts accepted solely because the source As-Built was accepted under the old authority model.

- [ ] **Step 3: Define intent-specific behavior**

```text
USE_EXISTING:
  may continue consuming legacy accepted outputs when no new STM-dependent capability is requested; do not rewrite package merely to modernize it.

RESUME:
  reconcile required factual dependency at the first unfinished downstream gate; do not full-backfill unrelated model domains automatically.

EXTEND:
  backfill/build only the STM slice needed by the requested new capability/output, unless the new request itself structurally requires FULL.

REVALIDATE:
  use old As-Built/evidence as historical context; fresh acceptance follows impact-driven technical revalidation against the selected baseline.
```

- [ ] **Step 4: Define mode upgrade behavior**

If a legacy standard/full audit is explicitly upgraded to forensic, build/validate the required full forensic-depth STM rather than trusting compact old prose as forensic evidence.

- [ ] **Step 5: Preserve `PROJECTION_REPAIR` semantics**

Projection repair does not require STM backfill merely to fix presentation in a reusable legacy package. If repair exposes semantic drift requiring technical change, route to technical reconciliation/revalidation as before.

- [ ] **Step 6: Re-run PS-96, PS-99, PS-80, and session regression canaries**

Expected Stage A:

```text
PS96_GREEN_STM_INCREMENTAL_REUSE
PS99_GREEN_LEGACY_AND_CROSS_CAPABILITY_REUSE
```

Ensure PS80 `PROJECTION_REPAIR` remains GREEN and existing `USE_EXISTING/RESUME/REVALIDATE/EXTEND` semantics remain bounded.

- [ ] **Step 7: Commit lifecycle/legacy integration**

```bash
git add references/session-orchestration.md \
        references/revalidation-and-freshness.md \
        references/review-modes-and-orchestration.md \
        references/shared-technical-model.md
git commit -m "feat: add legacy Shared Technical Model reconciliation"
```

---

## Task 11: Update roadmap and public documentation to the accepted Stage A model

**Files:**
- Modify: `docs/roadmap.md`
- Modify: `README.md`
- Modify: `references/report-contract.md` if a public artifact index/cross-link needs final alignment.

**Interfaces:**
- Consumes: accepted Stage A implementation contracts.
- Produces: accurate user-facing repository documentation that no longer describes Stage A as generic Developer Documentation.

- [ ] **Step 1: Rename/reframe roadmap Stage A**

Change:

```text
Stage A — Developer Documentation
```

to:

```text
Stage A — Shared Technical Model Foundation
```

Document the accepted sub-stages:

```text
A1 Shared Evidence Layer
A2 Shared Technical Model
A3 Technical Model Coverage
A4 Dependency / Index Infrastructure
A5 Technical Documentation
A6 As-Built Projection Migration
A7 Architecture Review Integration
A8 Legacy Audit Reconciliation
```

- [ ] **Step 2: Remove rejected Stage A scope**

Roadmap/README must not claim Stage A owns developer onboarding, local setup, or “how to run/modify” guidance.

- [ ] **Step 3: Explain the architecture in user-facing terms**

README should explain compactly:

```text
shared evidence -> factual STM -> capability interpretations -> human projections
```

and the mode projection:

```text
STANDARD_FULL -> FULL/COMPACT
FORENSIC -> FULL/FORENSIC
```

- [ ] **Step 4: Preserve Stage B boundary**

Clarify that Stage A provides dependency/index metadata and projection provenance, while Stage B remains responsible for robust audit projection/regeneration workflows.

Do not claim Stage B is implemented.

- [ ] **Step 5: Verify terminology and link consistency**

Search for stale claims such as:

```text
Developer Documentation
Technical As-Built working file — source of truth
accepted As-Built is the factual authority
```

Classify each occurrence: legacy-history/context may remain if clearly historical; active contract wording must align with STM authority.

- [ ] **Step 6: Commit roadmap/public docs**

```bash
git add docs/roadmap.md README.md references/report-contract.md
git commit -m "docs: align roadmap with Shared Technical Model foundation"
```

---

## Task 12: Build the final Stage A validation record and run full regressions

**Files:**
- Create: `tests/shared-technical-model-foundation-validation.md`
- Modify: `tests/pressure-validation-matrix.md` with observed candidate results/status only.

**Interfaces:**
- Consumes: complete Stage A candidate and existing pressure-test corpus.
- Produces: auditable GREEN/FAIL evidence and known limitations before independent review.

- [ ] **Step 1: Run static integrity checks**

At minimum:

```bash
git diff --check
git status --short
git diff --name-only <implementation-base>...HEAD
```

Also inspect repository-relative links and obvious stale authority wording. Use available Markdown/link tooling if present; do not install new dependencies merely for validation without authorization.

- [ ] **Step 2: Run PS-90..99 in fresh independent contexts**

Record for each:

```text
run_id
candidate_head
scenario
execution_context
observed_response_summary
expected_behavior
violations
verdict
```

Expected terminal verdicts:

```text
PS90_GREEN_PERSISTENT_STM_BOOTSTRAP
PS91_GREEN_MODE_PROJECTION
PS92_GREEN_FACT_INTERPRETATION_BOUNDARY
PS93_GREEN_SHARED_EVIDENCE_LAYER
PS94_GREEN_COVERAGE_SEPARATION
PS95_GREEN_HYBRID_DEPENDENCY_GRAPH
PS96_GREEN_STM_INCREMENTAL_REUSE
PS97_GREEN_TECHNICAL_DOCUMENTATION_PROJECTION
PS98_GREEN_AS_BUILT_PROJECTION_MIGRATION
PS99_GREEN_LEGACY_AND_CROSS_CAPABILITY_REUSE
```

If the repository still has no executable coordinator/runtime, distinguish static/contract validation from fresh agent Skill pressure execution exactly as current validation records do.

- [ ] **Step 3: Run Architecture Review regression canaries**

At minimum include representative canaries for:

```text
As-Built/factual completeness parity
independent review role separation
Architecture Discovery Coverage
context orchestration / bounded expansion
workflow authority consistency
long-run authority integrity
projection repair
user-facing language/report quality
```

Use the existing pressure-validation matrix IDs rather than inventing duplicate tests where a current scenario already covers the invariant.

- [ ] **Step 4: Run Test Engineering PS-79 and PS-81..89 regressions**

Required: no semantic or startup/EXTEND regression introduced by STM reuse.

- [ ] **Step 5: Validate authority map coherence**

Check that each concept has one owning authority:

```text
Shared Evidence              -> shared-evidence-model.md
Shared Technical Model       -> shared-technical-model.md
STM Coverage                 -> technical-model-coverage.md
Dependency/Index semantics   -> technical-model-dependencies.md
Technical Documentation      -> technical-documentation.md
Architecture Discovery       -> review-method/discovery-coverage ownership as already defined
Test Engineering semantics   -> capability contracts
Final projection writing     -> report-contract.md
```

Root `SKILL.md` must orchestrate rather than duplicate these contracts.

- [ ] **Step 6: Validate no dual As-Built/STM authority remains**

Search active contracts for claims that accepted As-Built is still the technical source of truth. Any such active claim is a blocker unless it is explicitly describing legacy package semantics.

- [ ] **Step 7: Validate context/minimum-work behavior**

Confirm the guidance supports:

```text
INDEX -> object -> EV -> raw source
EXTEND minimum factual slice
REVALIDATE impact-driven slice
FORENSIC enrichment
```

and does not require blanket reload of all STM/evidence artifacts for routine bounded decisions.

- [ ] **Step 8: Write validation record**

`tests/shared-technical-model-foundation-validation.md` must separate:

```text
RED-before-GREEN provenance
static/contract checks
fresh independent Skill pressure results
Architecture regression results
Test Engineering regression results
known runtime/tooling limitations
remaining non-Stage-A roadmap work
```

- [ ] **Step 9: Commit validation evidence**

```bash
git add tests/shared-technical-model-foundation-validation.md tests/pressure-validation-matrix.md
git commit -m "test: validate Shared Technical Model foundation"
```

---

## Task 13: Independent review, remediation, and implementation-ready closeout

**Files:** only files required by accepted review findings; do not make opportunistic redesign changes.

**Interfaces:**
- Consumes: complete Stage A candidate and validation record.
- Produces: independent implementation review verdict, targeted fixes where required, and a promotion-readiness checkpoint.

- [ ] **Step 1: Run a fresh-context independent design/implementation conformity review**

Reviewer mission:

- compare implementation against the approved Stage A spec and this plan;
- verify ownership boundaries and absence of duplicate authorities;
- challenge `STANDARD_FULL` vs `FORENSIC` projection;
- challenge shared-evidence/STM/capability separation;
- challenge context savings against correctness/freshness;
- challenge legacy reconciliation for silent authority promotion;
- challenge As-Built factual parity and separate Architecture Coverage;
- challenge Test Engineering compatibility;
- identify over-modeling or accidental Stage B/C/D/E scope creep.

Reviewer must not silently edit implementation while reviewing.

- [ ] **Step 2: Classify findings before changing files**

Use explicit findings with evidence and severity/priority appropriate to repository process. Distinguish:

```text
BLOCKER / HIGH correctness-contract issue
MEDIUM integration/clarity issue
LOW editorial issue
NOT_A_FINDING / out-of-scope suggestion
```

Do not accept broad “clean up everything” feedback without a concrete contract failure.

- [ ] **Step 3: Apply targeted remediation with RED/GREEN evidence where behavior changes**

For any newly discovered behavioral gap, add or extend a pressure scenario before changing the governing contract when practical. Preserve correction history; do not erase failed review evidence.

- [ ] **Step 4: Re-run affected pressure tests plus full Stage A canaries**

At minimum rerun all PS-90..99 after any material remediation, plus directly impacted older regressions.

- [ ] **Step 5: Run final Git verification**

```bash
git diff --check
git status --short
git log --oneline --decorate -n 20
git rev-parse HEAD
git rev-parse origin/main
```

Confirm implementation history is reviewable and no unrelated files/secrets/build artifacts were committed.

- [ ] **Step 6: Produce final implementation checkpoint**

If every required gate is green, report:

```text
SHARED_TECHNICAL_MODEL_IMPLEMENTATION_APPROVED

implementation_base: <verified main SHA>
feature_head: <HEAD>
PS90-99: GREEN
Architecture regression: PASS
Test Engineering regression: PASS
independent review: ACCEPTED
known limitations: <explicit>
```

Do **not** merge or publish `main` under this plan.

If a material gate remains unresolved, report the exact blocker instead of promotion readiness. For example:

```text
FULL_STM_COVERAGE_BLOCKED
TECHNICAL_MODEL_AUTHORITY_CONFLICT
LEGACY_STM_RECONCILIATION_REQUIRED
```

Use only when the observed problem actually matches the token.

---

## Implementation Sequence Summary

The intended commit-level sequence is:

```text
1.  test: define Shared Technical Model pressure contracts
2.  feat: define shared evidence layer
3.  feat: define Shared Technical Model authority
4.  feat: add Shared Technical Model coverage gate
5.  feat: add Shared Technical Model dependency graph
6.  feat: define technical documentation projection
7.  refactor: make architecture review consume Shared Technical Model
8.  refactor: separate technical and architecture coverage gates
9.  refactor: reuse Shared Technical Model in Test Engineering
10. feat: add legacy Shared Technical Model reconciliation
11. docs: align roadmap with Shared Technical Model foundation
12. test: validate Shared Technical Model foundation
13. targeted review remediation commit(s), only if required
```

Each commit should be independently understandable and should not mix unrelated cleanup.

## Completion Checklist

Before claiming Stage A implementation complete, all of the following must be true:

- [ ] Every `NEW` has a persisted STM baseline contract.
- [ ] `STANDARD_FULL -> FULL/COMPACT` and `FORENSIC -> FULL/FORENSIC` are explicit and pressure-tested.
- [ ] Shared Evidence `WS/EV` semantics are accepted and cross-capability.
- [ ] STM first-class families/relations/lifecycle/freshness/authority are defined without premature ontology expansion.
- [ ] Technical Model Gate is the sole writer of accepted shared facts.
- [ ] All 18 full technical domains have explicit coverage accounting.
- [ ] `TECHNICAL_MODEL_COVERAGE_ACCEPTED` is distinct from Architecture `COVERAGE_ACCEPTED`.
- [ ] Hybrid direct-dependency + generated-reverse-index semantics are explicit and tested.
- [ ] Generated indexes are reproducible and non-authoritative.
- [ ] `EXTEND` and `REVALIDATE` reuse the minimum accepted/fresh technical slice.
- [ ] Technical Documentation is a factual human projection, not developer how-to guidance or authority.
- [ ] As-Built is a projection; STM is factual authority; no active dual-authority wording remains.
- [ ] Existing As-Built factual material has not been lost during migration.
- [ ] Architecture Review keeps interpretation/findings/root/severity/target/roadmap ownership.
- [ ] Test Engineering PS-81..89 semantics and UX remain green while reusing STM facts.
- [ ] Legacy packages reconcile conservatively without silent As-Built -> STM promotion.
- [ ] `PROJECTION_REPAIR` remains projection-only and does not force legacy STM backfill.
- [ ] Roadmap and README reflect Stage A — Shared Technical Model Foundation.
- [ ] PS-90..99 are GREEN in fresh candidate pressure validation.
- [ ] Existing representative Architecture and Test Engineering regressions pass.
- [ ] Independent review is accepted or all material findings are remediated and re-reviewed.
- [ ] `git diff --check` is clean.
- [ ] No merge/tag/release/main publication occurred under this implementation plan.
