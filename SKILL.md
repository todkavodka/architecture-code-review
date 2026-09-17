---
name: architecture-code-review
description: Use when performing a whole-project or subsystem architecture/code review where lifecycle, ownership, concurrency, trust boundaries, security, reliability, maintainability, or testability require evidence-backed analysis rather than a lint-style checklist.
---

# Architecture Code Review

## Overview

Run an evidence-first architecture review of an existing software system as a controlled, resumable process. Reconstruct the factual architecture and ownership model first; then identify candidates, independently verify discovery coverage and candidate validity, adjudicate root causes, and only then assign severity.

**Core principle:** the scope of an architectural claim must never exceed the scope of the evidence that supports it. A material claim must be grounded in a traced code path, ownership, and a concrete effect. Discovery completeness is established through coverage of relevant mechanism classes, not by the number of findings produced.

## Start Gate — Session, Work, and Artifact Topology

Before substantive investigation **or any persistent review-package filesystem mutation**, read and enforce all three:

1. `references/session-orchestration.md`;
2. `references/review-modes-and-orchestration.md`;
3. `references/artifact-layout-and-package-completeness.md`.

Resolve any previous audit package, establish the repository baseline and working-tree state, construct or backfill the local Project Profile, then resolve the recommended `Session Intent` and all configuration choices required by that intent. Do not begin substantive work for `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, or `PROJECTION_REPAIR` until the required user decisions are resolved.

Before the first persistent review artifact or directory is created, resolve the exact requested work and output membership. For every selected capability or standalone output, read its owning contract early enough to resolve its exact artifact/projection paths. Then freeze and persist:

```text
ARTIFACT_LAYOUT_MANIFEST
```

according to `references/artifact-layout-and-package-completeness.md`.

The execution-critical invariant is:

```text
NO_PERSISTENT_WRITE_BEFORE_ARTIFACT_LAYOUT_MANIFEST
```

`working/INDEX.md` bootstrap may be created only as the coordinator artifact required to persist the resolved startup state and manifest; it does not authorize other paths. Do not create speculative directories, convenience reports, aggregate files, or future-use placeholders before their exact paths are declared.

If a required output path cannot be resolved from the frozen manifest or an owning contract, stop with:

```text
ARTIFACT_PATH_NOT_DECLARED
```

Do not invent a location to keep execution moving.

`PROJECTION_REPAIR` is limited to repairing user-facing or final projections of already accepted audit state. It is not a technical re-audit. It may correct language, structure, links, Markdown/Mermaid, navigation, terminology, and cross-references using accepted authority. Every changed projection must pass `PROJECTION_REVALIDATION`; semantic drift requires `SEMANTIC_DRIFT_DETECTED` and `TECHNICAL_REVALIDATION_REQUIRED`.

Product / multi-project mode is an explicit opt-in route governed by `references/product-multi-project-review.md`. The coordinator may select and pin an accepted Product revision and exact baseline only after separate Product Context Workflow authorization. Source-read, dirty-admission, semantic-write, test, code, worktree, commit, push, PR, and deployment actions remain independently authorized; Product membership grants none of them. Product `REVALIDATE` is impact-driven and bounded. Product `EXTEND` is additive. Neither implies a full Product reread or automatic projection regeneration. Single-project sessions remain first-class and do not require Product state.

From a non-Git Coordination Root, natural-language Product requests such as “show the current Product state”, “update existing child audits”, “bring the whole Product to a current audit state”, “what changed since the previous Product audit?”, “show the impact of backend changes”, “update backend and assess Product impact”, or “I already updated backend separately; incorporate that result” are normalized to the existing Product/requested-work/child-intent semantics. These are illustrative natural-language examples, not a formal CLI grammar or persisted command vocabulary. Membership and requested work must be resolved and confirmed before substantive work; a broad request never silently selects every discovered repository, capability, or a full Product review.

The top-level semantic capabilities remain exactly:

- Architecture Review
- Test Engineering
- Code Quality Review

Federated coordination, Technical Documentation, and dependency/readiness views are orchestration or output concerns, not additional capabilities.

### Selected-output path resolution

Before adding selected outputs to `ARTIFACT_LAYOUT_MANIFEST`, read the owning output contract:

- Test Engineering → `capabilities/test-review/SKILL.md` and, for extended outputs, `capabilities/test-review/references/test-engineering-contract.md`;
- Code Quality → `capabilities/code-quality-review/SKILL.md` and `capabilities/code-quality-review/references/code-quality-projection.md`;
- Technical Documentation → `references/technical-documentation.md`;
- Architecture package/endpoint outputs → `references/report-contract.md` plus the selected mode/endpoint artifact set in `references/review-modes-and-orchestration.md`.

“All outputs” means the finite selected set of owning-contract outputs, not one umbrella aggregate document containing all topics.

## Stage F — Interface, API, and Data Integration Routing

When the review includes interfaces, APIs, integrations, events, persistence, or data access, acquire and qualify bounded observations through [`shared-evidence-model.md`](references/shared-evidence-model.md). Preserve `DIRECT_DECLARATION`, `STRONG_INFERENCE`, and `WEAK_HINT` as evidence metadata; none of them accepts facts by itself.

Route candidates and limitations to the Technical Model Gate, which remains the sole authority for accepted `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, and `FLOW-*` facts. Use the Stage F extensions in [`shared-technical-model.md`](references/shared-technical-model.md), including the distinction between interactions and relations, precise access authority in `INT-*`, and `MIGRATION` versus `MIGRATION_AUTHORITY`.

For a materially relevant declared external contract, invoke the existing automatic Contract Verification route in [`test-engineering-contract.md`](capabilities/test-review/references/test-engineering-contract.md). `CC-*` remains the Test Engineering authority for compatibility. The umbrella workflow does not match interfaces or adjudicate `COMPATIBLE` or `INCOMPATIBLE`.

After the required accepted and sufficiently fresh semantic inputs are available, route Stage F outputs through the Technical Documentation projections defined in [`technical-documentation.md`](references/technical-documentation.md). These remain derived projections: projection prose cannot feed back into STM, and regeneration is never automatic.

When Product mode is explicitly selected, reuse the existing Stage E qualification in [`product-multi-project-review.md`](references/product-multi-project-review.md). Product remains optional, single-project review remains first-class, and Product does not become a factual authority or permission boundary.

Before producing user-facing projections, apply the owning evidence and rendering-safety contracts:

- omit `SECRET`;
- redact or safely alias `SENSITIVE_INTERNAL`;
- render `SAFE_TECHNICAL_IDENTIFIER` only when permitted.

Dynamic operations, unresolved targets or comparison inputs, partial or unavailable sources, stale projections, and unresolved `CC-*` state must remain explicit limitations. Orchestration must not convert them into exact, compatible, clean, empty, or not-applicable results without the owning authority.

Stage F routing does not introduce an automatic API compatibility engine, runtime database scanner, SQL parser, distributed tracing system, external discovery crawler, or projection-regeneration system. Any such capability requires a separate approved architecture and implementation decision.

Stage B session intents converge on the same explicit projection handoff. `NEW` and `EXTEND` complete requested semantic work first; `REVALIDATE` completes its impact-driven semantic delta. Once semantic state is stable, run Projection Impact Analysis and persist `PROJECTION_IMPACT_ACCOUNTED`. This accounts for freshness but never regenerates projection content.

For every project-change `REVALIDATE`, read and enforce `references/revalidate-closeout-hardening.md` before baseline advancement, Projection Impact Analysis closeout, or any `RG-*` request. The REVALIDATE overlay is proposed delta until the owning semantic gates accept the affected revisions; a changed baseline pointer, rewritten Markdown, or completed worker task is not acceptance evidence.

If a requested output or package requires fresh projection content, invoke a separate `RG-*` regeneration workflow with the appropriate scope. Closeout uses the named package and gate policy, so unrelated stale projections remain visible without blocking an unrelated gate. Detailed intent and closeout routing are owned by `references/session-orchestration.md` and `references/review-modes-and-orchestration.md`.

## Persistent Workflow

Create the audit package and `working/INDEX.md` only from the frozen `ARTIFACT_LAYOUT_MANIFEST` and owning path contracts. `INDEX.md` is the persistent workflow authority for coordinator state. Resume-critical state must not exist only in chat.

If the host provides a native todo/task/plan tool, **actually invoke that tool** to create and update the visible plan. A textual plan description, an `INDEX.md` update, or internal reasoning is not a substitute for a native tool call.

After every material coordinator state transition:

1. validate artifacts and handoffs;
2. update `working/INDEX.md`;
3. update the native plan/todo tool with the current projection of work.

After a batch of subagents completes, perform the same reconciliation sequence. On resume, restore state from `INDEX.md` and update the native plan/todo tool before continuing. If no native planning tool exists, show a compact text plan/status. Stability is more important than maximum parallelism.

### Worker/subagent artifact-write contract

Subagents may investigate independent domains, but they may persist review-package files only at paths explicitly assigned by the coordinator and permitted by the frozen manifest/owning contract. Every persistent worker dispatch that can write artifacts MUST contain:

```text
artifact_owner: <owning capability/contract>
allowed_output_paths: [<exact declared paths>]
required_output_paths: [<exact required paths for this dispatch>]
forbidden_output_policy: ALL_OTHER_PATHS
```

A file has one active writer. Every agent-owned artifact must contain a persisted `HANDOFF SUMMARY` where the owning artifact contract requires one.

Workers MUST NOT invent `working/*.md`, convenience summaries, aggregate capability reports, directory taxonomies, or speculative output paths. A worker that discovers a need for an undeclared persistent artifact must return `ARTIFACT_PATH_NOT_DECLARED` to the coordinator; it must not create the file first and reconcile it later.

Before using `INDEX.md`, a handoff, or another compact semantic record as a substitute for reading the owning technical artifact, verify freshness and revision binding through `references/revalidation-and-freshness.md`. Stale compact state is not accepted downstream input.

During resume or reconciliation, `COVERAGE_ACCEPTED` is not exception authority over the owning Discovery Coverage Matrix. If an independent coverage review says `COVERAGE_ACCEPTED` while a material row in the owning matrix remains `PARTIALLY_COVERED`, `BLOCKED`, or `REVALIDATION_REQUIRED`, coverage authority is contradictory. Downstream progression is blocked until evidence-backed correction and re-review. Do not rationalize the conflict as “partial coverage is acceptable for this scope”, and do not advance `INDEX.md` to `COMPLETE`.

Before downstream use of a compact Discovery Coverage projection, verify structural integrity. If `domains.total` does not equal the sum of the represented mutually exclusive status buckets, the projection is invalid. Reconcile it against the owning matrix/review instead of trusting an arithmetically contradictory `INDEX.md`.

## Required Review Flow

Test Review is a composable capability. It may be selected initially, recommended when discovery identifies a material automated-test surface, or attached later to an existing audit. Its specialist methodology lives in `capabilities/test-review/SKILL.md`. The umbrella orchestrator retains shared authority, freshness, artifact ownership, and completion gates.

Test Engineering output selection is persisted as independent booleans and executes a minimum dependency slice. `Test Assurance` remains the compatibility core. `Behavior Model` is an internal dependency. Applicable `Contract Verification` is automatic. Optional output projections and ownership are defined by the capability contract and recorded as coordinator routing state in `working/INDEX.md`; that record is not the generated Stage B projection registry.

For a full Architecture Review, construct the required `FULL` Shared Technical Model and accept `TECHNICAL_MODEL_COVERAGE_ACCEPTED` before Architecture thematic discovery or any other consumer that requires a complete factual substrate. `STANDARD_FULL` requires `FULL/COMPACT`; `FORENSIC` requires `FULL/FORENSIC`. The factual coverage matrix and independent gate are separate from Architecture Discovery Coverage and are authoritative in `references/technical-model-coverage.md`.

0. Resolve requested work and selected output membership; load every owning path contract needed by that selection; freeze and persist `ARTIFACT_LAYOUT_MANIFEST`. No subsequent persistent review artifact write is permitted outside that manifest/owning contracts.
1. Establish the repository baseline and applicable stack addenda. For `NEW`, create the persistent Shared Technical Model baseline from `references/shared-technical-model.md` at the manifest-declared path(s) before running a capability. Creating the baseline does not require every factual slice to be fully populated.
2. Collect or revalidate the required Shared Evidence and factual STM slices using `references/shared-evidence-model.md` and `references/shared-technical-model.md`, writing only manifest-declared artifacts.
3. Run an independent Technical Model Coverage Review and accept the required full STM. The author of the factual model must not self-accept it.
4. Only after the required STM is accepted and sufficiently fresh, perform Architecture thematic discovery using:
   - `references/ownership-and-scenarios.md`;
   - `references/boundary-contract-audit.md`;
   - `references/lifecycle-and-mermaid.md`;
   - `references/discovery-coverage.md`;
   - applicable `references/stacks/*.md`.
5. Discovery creates `CAND-*`, `PC-*`, `OQ-*`, and `AC-*`, but not final `RF-*`, and updates the Discovery Coverage Matrix according to `references/discovery-coverage.md`.
6. Close the Discovery Coverage Matrix and run a separate Independent Coverage Review. If there is a gap, perform targeted coverage correction and fresh re-review. Candidate verification begins only after `DISCOVERY_COMPLETE` and `COVERAGE_ACCEPTED`.
7. Independently verify candidates according to `references/independent-verification.md`.
8. Perform root-boundary adjudication according to `references/root-boundary-adjudication.md`.
9. Only then assign severity according to `references/evidence-and-severity.md` and construct the authoritative ledger.
10. Build As-Built and main review projections according to `references/report-contract.md` from accepted/fresh STM and accepted Architecture Review authority. For every independently regenerable projection produced by the selected workflow, first generation must complete the full Stage B handoff: establish/register stable `PRJ-*` identity → bind owning capability and projection-contract revision → bind semantic and upstream projection dependencies → freeze/persist the required dependency-resolution snapshot → generate candidate content → pass `V1`–`V4` → compute the canonical fingerprint → publish the initial verified `PRJ-*@revN` → persist freshness (`CURRENT`, `STALE`, or `BLOCKED`). Only then is the artifact a valid generated projection. Raw Markdown without accepted lifecycle metadata is not `CURRENT`. First generation uses the existing lifecycle and verification contracts and does not create an `RG-*` session unless those contracts explicitly require one.
11. If the selected endpoint includes Target Architecture, create it at the manifest-declared semantic-authority path and run review/correction/fresh re-review according to `references/target-architecture-review.md`.
12. If the selected endpoint includes Roadmap, create it at the manifest-declared semantic-authority path and run execution-consistency review/correction/fresh re-review according to `references/remediation-roadmap-review.md`.
13. Complete every selected capability and standalone output at its owning contract's exact declared path. One aggregate umbrella file does not satisfy multiple selected outputs unless an approved contract explicitly registers that aggregate.
14. Assemble the final package from the frozen manifest and run `ARTIFACT_PACKAGE_RECONCILIATION` against the actual filesystem tree, `working/INDEX.md` artifact registry, and owning contracts. Persist `ARTIFACT_PACKAGE_RECONCILED` only when the structural gate passes.
15. Only after `ARTIFACT_PACKAGE_RECONCILED`, run issue-only editorial review → separate correction → fresh re-review according to `references/final-editorial-review.md`. Any editorial correction that changes package paths requires package reconciliation again. Presentation-only correction uses `PROJECTION_REVALIDATION` from `references/revalidation-and-freshness.md` while technical semantics remain unchanged.
16. Before `REVIEW_COMPLETE`, establish `FINAL_WORKFLOW_AUTHORITY_RECONCILED`: reconcile `working/INDEX.md` against accepted final artifacts and package state. At minimum verify current phase/status, selected mode/endpoint, Technical Model and Discovery Coverage gate states, artifact registry, candidate/finding mappings, positive-controls registry, open questions, architecture-correction candidates, authoritative-document registry, projection state relevant to the selected package, capability status, and the accepted artifact-package reconciliation result. This reconciles compact coordinator state and references; it does not copy semantic authority into `INDEX.md`. Any stored aggregate counts/lists must match their owning authoritative artifacts. `project_profile.status` is routing-only metadata and may remain `PENDING` when its profile reference is internally valid; it is not a mandatory completion gate unless the selected workflow explicitly makes it one.

For `REVALIDATE` closeout, that reconciliation MUST also verify the exact `accepted_baseline`, `candidate_baseline` disposition, `source_head`, current-baseline Technical Model and coverage bindings, owner-adjudicated semantic revisions, unresolved-policy references, projection registry membership, accepted projection revisions/fingerprints, and resolved package membership. Contradictory baseline or coverage bindings force `FINAL_WORKFLOW_AUTHORITY_RECONCILED: NOT_ACCEPTED`.

## Non-Negotiable Gates

- `NO_PERSISTENT_WRITE_BEFORE_ARTIFACT_LAYOUT_MANIFEST`: except for the minimum coordinator bootstrap needed to persist startup state/manifest, no review-package file or directory may be created until the frozen manifest is resolved.
- A persistent writer may write only exact `allowed_output_paths` from its dispatch. All other paths are forbidden; discovering a new need returns `ARTIFACT_PATH_NOT_DECLARED`.
- Semantic taxonomy is not filesystem taxonomy. STM domains, discovery themes, capability names, and report topics do not authorize same-named directories or files.
- “All outputs” is a resolved set of registered/declared outputs, not permission to collapse them into one aggregate report.
- Accepted and sufficiently fresh Shared Technical Model is the factual technical authority. Human-readable As-Built is a projection of accepted/fresh STM plus architecture-oriented synthesis.
- A capability must not rewrite accepted STM or an As-Built projection to correct a fact. It emits `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT`, or `TECH_FACT_REVALIDATION_REQUEST` to the Technical Model Gate. `ARCH-CORRECTION-CANDIDATE` remains Architecture-owned interpretation only.
- `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED`, and `BLOCKED` are not accepted downstream input.
- Compact persisted semantic state is usable downstream only when bound to the current accepted revision of the owning artifact. A mismatch requires `AUTHORITY_RECONCILIATION_REQUIRED`.
- Shared assurance principles apply across capabilities: resolve material authority before a substantive verdict, and keep claim scope within directly evidenced material scope.
- Context Orchestration v0.3 loads the minimum fresh decision evidence through dependency-sliced routing; see `references/revalidation-and-freshness.md`.
- Presentation-only correction does not automatically restart the technical audit. Use `PROJECTION_REVALIDATION`; semantic drift requires `TECHNICAL_REVALIDATION_REQUIRED`.
- `PROJECTION_REPAIR` must not hide a changed source/baseline. Project-change freshness belongs to `REVALIDATE`.
- During `REVALIDATE`, `working/revalidation-overlay.md` (or equivalent) is proposed delta until affected owner gates accept it. `overlay complete != semantic authority accepted` and `baseline pointer changed != baseline accepted`.
- `RG-*` targets MUST be active explicitly registered `PRJ-*` identities. Semantic authority, `working/INDEX.md`, unregistered paths, and path-derived targets are forbidden and return `REGENERATION_TARGET_NOT_PROJECTION`.
- `ALL_STALE` means only active registered `PRJ-*` identities whose persisted projection freshness is `STALE`; it never means all stale-looking files or changed semantic authorities.
- `rewritten Markdown != CURRENT`, `RG completed != CURRENT`, and `registered identity != CURRENT`. `CURRENT` requires the accepted projection lifecycle evidence in `references/projection-lifecycle.md`, including V1-V4, canonical fingerprint, and accepted `PRJ-*@revN` or verified `NO_CHANGE`.
- Major artifact author and final judge must be separate roles. Review, correction, and fresh re-review are distinct stages.
- Write large Markdown artifacts in logical chunks with validation; do not rely on one giant write.
- The number or severity of discovered `CAND-*` / `RF-*` records is not evidence of discovery completeness.
- `DISCOVERY_COMPLETE` without `COVERAGE_ACCEPTED` is not accepted downstream input for candidate verification.
- A full Architecture Review requires `TECHNICAL_MODEL_COVERAGE_ACCEPTED` before thematic discovery. `PARTIAL`, `BLOCKED`, or `UNKNOWN` material STM coverage cannot be overridden by a prose verdict.
- Correct a coverage gap with a targeted pass and fresh re-review. Do not restart the whole technical audit without impact evidence.
- `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, `COVERAGE_BLOCKED`, and `COVERAGE_AUTHORITY_DRIFT` are not accepted coverage states.
- Independent Coverage Review validates the owning matrix but does not override its hard row semantics. A prose `COVERAGE_ACCEPTED` cannot make a material `PARTIALLY_COVERED`, `BLOCKED`, or `REVALIDATION_REQUIRED` row acceptable downstream state.
- An arithmetically or structurally contradictory Discovery Coverage projection is not accepted persisted authority. Reconcile it against the owning matrix/review first.
- A serious security finding requires an attack chain. Absence of hardening alone is not `HIGH` or `CRITICAL`.
- Severity is separate from correctness verification.
- Preserve and account for Positive Controls in Target Architecture and Roadmap work.
- Absence evidence, TODOs, file length, framework choice, mocks, warnings, and literals are not findings without concrete impact.
- Working artifacts may be terse and machine-oriented. User-facing final documents must explain `what happens → why it happens → what it causes → what should change` in coherent prose. IDs and shorthand support the explanation but do not replace it.
- Do not modify project production code during review.

Stage B projections are explicitly classified and have stable `PRJ-*` identities. Lifecycle state and verified revisions follow `references/projection-lifecycle.md`. `working/INDEX.md` is `COORDINATOR_WORKFLOW_AUTHORITY`: it owns resume-critical session, gate, handoff, and coordinator state and is outside every Stage B projection mechanism. It must not receive a `PRJ-*` identity, projection fingerprint or drift result, regeneration or `RG-*` execution state, projection freshness state, or `ACTIVE` / `RETIRED` lifecycle transition. Semantic authorities are likewise outside automatic projection classification.

Operational Stage B views are non-authoritative projections and use clearly scoped paths under `working/projections/`, such as the generated registry, impact view, and per-session `RG-*.md` records. They summarize their owning projection/impact/regeneration records. They never replace `working/INDEX.md`, direct dependency authority, or semantic authority. Path and filename do not classify an artifact as a projection.

Semantic workflow may complete while projections remain `STALE`. Projection freshness is not semantic truth, and regeneration never mutates semantic authority.

`PROJECTION_REPAIR` remains a bounded presentation-only operation. It may repair the representation of unchanged accepted meaning, but it cannot mutate semantic authority, hide a source/baseline change, or create a persistent human-owned section inside a fully generated projection.

`01-architecture-review.md` may be fully generated only after `report-contract.md` maps every persistent Architecture meaning to an accepted upstream owner. Otherwise return `PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY` and do not regenerate unmapped content.

## Language Contract

The user-facing language of the Skill follows the user’s current language. An explicit request for a particular language takes precedence. Otherwise use the language of the user’s most recent substantive request; do not switch to English merely because this Skill or its reference files are written in English.

All menus, questions, recommendations, explanations, progress/status messages, and final user-facing documents must use that selected language consistently. This applies to the entire umbrella workflow and attached capabilities, including Test Review.

Keep formal identifiers unchanged: `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `PROJECTION_REPAIR`, `STANDARD_FULL`, `FORENSIC`, endpoint/status tokens, exact code identifiers, paths, API/IPC/protocol names, and filenames. When useful, follow a formal token with a natural-language explanation in the user’s language.

Persisted machine-oriented fields, `INDEX.md` keys, ledger rows, and other canonical technical tokens may remain in English when that is part of the contract. Explanatory user-facing prose around them must stay in the selected language. A user language change applies from the next response onward; do not rewrite already persisted technical artifacts solely for translation unless the user asks.

For Russian-speaking users, final documents must be coherent Russian technical prose. On first substantial use, an `English term (Russian equivalent)` form is acceptable where useful; exact identifiers, code, paths, API/IPC/protocol names, and formal status tokens remain unchanged.

Do not copy the style of `HANDOFF SUMMARY`, ledger rows, or agent scratchpads into final prose. Express ordinary concepts naturally in the user’s language and avoid unnecessary hybrid wording. For complex topology, lifecycle, ownership, or target-state mechanics, use useful Mermaid diagrams according to the relevant reference contracts.

## References — Authority Map

- startup / previous-audit selection / session intent / Review Suite startup / Project Profile / dirty baseline → `references/session-orchestration.md`
- modes / endpoint / INDEX / state / resume / subagents → `references/review-modes-and-orchestration.md`
- artifact root / frozen layout manifest / writer paths / package completeness / filesystem reconciliation → `references/artifact-layout-and-package-completeness.md`
- projection repair / projection-only revalidation / compact-state freshness / stale projection reconciliation → `references/revalidation-and-freshness.md`
- REVALIDATE semantic closeout / proposed delta / baseline advancement / RG boundary regression guard → `references/revalidate-closeout-hardening.md`
- Stage B projection identity, lifecycle, revision, freshness, drift, and required-action authority → `references/projection-lifecycle.md`
- Stage B projection dependency kinds, selector contracts, resolution snapshots, and projection DAG → `references/projection-dependencies.md`
- shared authority, evidence scope, bounded accounting, and candidate decomposition → `references/shared-assurance-principles.md`
- shared evidence worksets / observations / provenance / cross-capability reuse → `references/shared-evidence-model.md`
- Shared Technical Model facts / lifecycle / Technical Model Gate / persistence → `references/shared-technical-model.md`
- STM factual-domain coverage / `STANDARD_FULL` and `FORENSIC` projection / Technical Model Coverage Review → `references/technical-model-coverage.md`
- capability state / resume / artifact ownership → `references/review-modes-and-orchestration.md`
- core method / STM-first Architecture Review flow → `references/review-method.md`
- discovery completeness / coverage matrix / independent coverage review → `references/discovery-coverage.md`
- ownership / invariants / adversarial scenarios → `references/ownership-and-scenarios.md`
- boundary contracts → `references/boundary-contract-audit.md`
- verification → `references/independent-verification.md`
- root boundaries → `references/root-boundary-adjudication.md`
- evidence / security chain / severity → `references/evidence-and-severity.md`
- lifecycle diagrams → `references/lifecycle-and-mermaid.md`
- final package / links / chunked writing → `references/report-contract.md`
- target review → `references/target-architecture-review.md`
- roadmap review → `references/remediation-roadmap-review.md`
- editorial gate → `references/final-editorial-review.md`

## Completion Gate

Return `REVIEW_COMPLETE` only when all required gates for the selected mode/endpoint are accepted, required full STM coverage is `TECHNICAL_MODEL_COVERAGE_ACCEPTED`, Architecture Discovery Coverage is `COVERAGE_ACCEPTED`, authoritative documents and cross-links are coherent, required independent verification/adjudication gates are accepted, required first-generation or regeneration Stage B projection lifecycle obligations are satisfied, final editorial correction/fresh re-review is accepted, limitations are explicit, and **both** of these are accepted:

```text
FINAL_WORKFLOW_AUTHORITY_RECONCILED
ARTIFACT_PACKAGE_RECONCILED
```

`FINAL_WORKFLOW_AUTHORITY_RECONCILED` cannot substitute for filesystem/package reconciliation. `ARTIFACT_PACKAGE_RECONCILED` cannot substitute for semantic/workflow authority reconciliation.

Before completion, verify the actual package root and filesystem tree against the frozen `ARTIFACT_LAYOUT_MANIFEST`, selected mode/endpoint artifact set, selected capability output membership, projection registrations, owning semantic roles, and `working/INDEX.md` artifact registry.

Any of the following forbids `REVIEW_COMPLETE`:

```text
ARTIFACT_PATH_NOT_DECLARED
REQUIRED_ARTIFACT_MISSING
ARTIFACT_LAYOUT_DRIFT
ARTIFACT_ROLE_MISMATCH
ARTIFACT_PACKAGE_RECONCILIATION_REQUIRED
selected output missing at its owning declared path
undeclared aggregate output substituted for selected outputs
undeclared generated directory remaining in the package
```

For `REVALIDATE`, also require that the accepted baseline was advanced only after `DELTA_RECONCILIATION` and `BASELINE_ADVANCE_ALLOWED`, and that Technical Model / coverage acceptance is bound to the accepted baseline rather than only the previous or candidate baseline. A coordinator pointer alone is never baseline acceptance.

When the selected endpoint has a projection-sensitive package gate, also require `PROJECTION_IMPACT_ACCOUNTED`, resolved package membership, and the package policy’s scoped projections to be `CURRENT`. Every such `CURRENT` projection must have an active registered `PRJ-*` identity, projection contract revision, accepted dependency/selector snapshot, V1-V4 pass records, canonical fingerprint, and accepted projection revision or verified `NO_CHANGE`. A `PERMISSIVE` gate may close with unrelated projections `STALE` and deferred.

If material coverage remains `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, `COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT`, or `REVALIDATION_REQUIRED`, ordinary `REVIEW_COMPLETE` is forbidden.

Otherwise return `REVIEW_PARTIALLY_COMPLETE` with the exact blocked or missing workflow/package gates from `working/INDEX.md` and the artifact-package reconciliation record.

## Requested-Work Output Routing

At startup, load requested-work state from `references/session-orchestration.md` and persisted intent/dependency state from `references/review-modes-and-orchestration.md`.

Route:

- standalone documentation → `references/technical-documentation.md`;
- Product qualification → `references/product-multi-project-review.md`;
- compatibility → Test Engineering Contract Verification and `CC-*`.

Shared Evidence, STM, and Stage B contracts remain factual and lifecycle authority.

The resolved-plan confirmation shows `Session Intent`, `Scope Context`, `Review Capabilities`, `Requested Outputs`, `Required Internal Work`, and `Authorization / Execution Boundaries`.

`Requested Outputs != Required Internal Work`.

Product Context != Requested Outputs.

Routing classes are orchestration labels only. They do not create capabilities, factual families, projection identities, lifecycle states, or authority. Selection grants no source-read, semantic-write, test, code, Git, worktree, commit, push, PR, deployment, E2E, simulator, environment, database-scan, SQL, tracing, or crawling permission.