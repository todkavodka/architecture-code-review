# Stage D Code Quality Review — Semantic and Capability Design

## 1. Baseline and authority inputs

Design baseline: `c9cba257659acc0fecabe654d6f6435c68da418e`.

Authoritative inputs:

- `docs/superpowers/specs/2026-09-05-stage-d-code-quality-discovery.md`
- `docs/superpowers/reviews/2026-09-05-stage-d-code-quality-discovery-review.md`
- `SKILL.md` and the accepted Architecture Review contracts;
- Shared Evidence (`WS-*`, `EV-*`) and Shared Technical Model contracts;
- Stage B projection, dependency, impact, package, and regeneration contracts;
- Test Engineering contracts under `capabilities/test-review/`.

This document resolves the semantic questions identified by the approved Discovery. It does not authorize implementation, select tools, or change Stage A, B, or C ownership.

## 2. Purpose and non-goals

Code Quality Review identifies evidence-backed, materially consequential implementation-quality issues that are not automatically Architecture findings and are not Test Engineering assurance records. It covers maintainability, duplication, assumptions, localization, dead code, complexity/cohesion, abstraction, errors, resources, asynchronous/concurrent behavior, framework and dependency use, lifecycle/API misuse, and testability when interpreted as implementation quality.

Code Quality does not own automatic refactoring or source modification, formatter or style-only lint enforcement, penetration testing, dependency-vulnerability scanning, performance benchmarking/profiling, test execution, simulator/environment execution, or Architecture redesign. Tooling may acquire evidence, but tooling does not own semantic findings.

## 3. Semantic authority model

### 3.1 Authoritative records

The capability owns the following minimum semantic records:

| Record | Owner and purpose | Authority and lifecycle |
|---|---|---|
| Code Quality Finding (`CQ-*`) | Code Quality Review; records one accepted materially consequential quality issue | Stable identity, evidence/source bindings, applicability, disposition, lifecycle, freshness, relationships, and remediation references are authoritative |
| Code Quality Remediation Action (`CQRA-*`) | Code Quality Review; records an independently actionable remediation that may address one or many findings | Independent action status and ownership are authoritative; many-to-many finding linkage is allowed |
| Finding relationship | Code Quality Review records an explicitly adjudicated relation to another CQ, RF, TE, or routed security/Architecture record | Relation type, endpoints, direction, rationale, and freshness bindings are authoritative; this is a bounded relation model, not a generic graph framework |

There is no accepted capability-neutral remediation authority to reuse: `TASK-*` is Test Engineering-owned and its assurance-work semantics are not interchangeable with Code Quality remediation. Therefore Code Quality owns `CQRA-*`. Applicability and adjudication are fields on a candidate or finding rather than separate authorities. Coverage limitation is a field on the Code Quality session/assessment authority (section 19), not a second factual model.

`working/INDEX.md` may reference these records and coordinator state but is not their semantic authority. Generated reports, summaries, hotspots, and roadmap views never replace the records.

### 3.2 Authority versus derived fields

Semantic authority includes identity, scope, category, mechanism, evidence references, consequence, materiality, severity, confidence, applicability/disposition, source and freshness bindings, lifecycle, relationship assertions, remediation links, and ownership. Derived/display fields include counts, rankings, labels, prose summaries, hotspot scores, report formatting, and roadmap ordering.

## 4. Finding identity

The canonical Code Quality finding family is **`CQ-*`**. It is distinct from Architecture `RF-*`, STM identifiers, and Test Engineering `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, and `TASK-*`.

The format is `CQ-<repository-scoped stable allocation>`. Allocation is stable and persistent; the identifier does not encode category, location, severity, or confidence. A candidate receives a `CQ-*` identity only when accepted as semantic authority. Revalidation retains the identity when the accepted issue remains the same semantic issue despite a move, rename, or equivalent refactor. A materially different issue receives a new identity; the old record may become `SUPERSEDED` or `RESOLVED` with evidence. Accidental duplicate candidates are represented by `DUPLICATE` adjudication and do not persist as competing authorities.

## 5. Finding schema and taxonomy

An accepted `CQ-*` record contains, at minimum:

- scope and affected files/symbols or other source bindings;
- one primary language-neutral category and a concise mechanism description;
- direct source evidence and `EV-*` references where observations are persisted;
- applicability, source baseline/revision, and relevant dependency/addendum bindings;
- material consequence and materiality rationale;
- severity and confidence, independently recorded;
- lifecycle, disposition, freshness, cross-capability relations, and remediation references.

The bounded taxonomy is:

`DUPLICATION`, `HARDCODED_ASSUMPTION`, `LOCALIZATION`, `DEAD_OR_OBSOLETE_CODE`, `COMPLEXITY_OR_COHESION`, `ABSTRACTION_MISUSE`, `ERROR_HANDLING`, `RESOURCE_MANAGEMENT`, `ASYNC_CONCURRENCY`, `FRAMEWORK_MISUSE`, `DEPENDENCY_USAGE`, `TESTABILITY`, `API_OR_LIFECYCLE_MISUSE`, and `MAINTAINABILITY`.

These are semantic lenses, not a rule catalog. Language/framework addenda specialize detection and applicability without adding another authority.

## 6. Architecture boundary

A local implementation issue remains CQ-only when its consequence is confined to the reviewed implementation and does not materially alter a system boundary, invariant, cross-component contract, trust boundary, ownership model, lifecycle, or system-level reliability/security mechanism.

A CQ finding may be `CORRELATED` with an `RF-*` when both authorities interpret the same mechanism differently; `CAUSAL` when the CQ mechanism materially contributes to an Architecture finding; and `ESCALATED` when the evidence may cross the material Architecture boundary. Architecture Review adjudicates any RF finding. Code Quality never creates, mutates, downgrades, closes, or suppresses an `RF-*` record. `DUPLICATE` means two authorities accidentally represent the same semantic issue and requires adjudication of one retained authority, not silent double counting. `INDEPENDENT` remains valid when shared evidence does not imply shared meaning.

The escalation threshold is material effect on a boundary, invariant, cross-component contract, trust boundary, ownership/lifecycle rule, or system-level reliability/security behavior. Size, repetition, or a tool label alone is insufficient.

## 7. Test Engineering boundary

Code Quality owns the implementation-quality interpretation of seams, isolation, nondeterminism, observability, dependency use, concurrency hazards, and fragile setup. Test Engineering owns `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, and `TASK-*` semantic authority and interprets whether behavior and executable evidence are adequately assured.

The same evidence may support a CQ finding and a TE record, but the records remain independently owned and are related explicitly. Code Quality cannot create or mutate TE authority, and TE does not turn a CQ finding into behavior truth automatically. A `CQRA-*` action is not a `TASK-*` generic project-management item.

## 8. Security boundary

There is currently no independent Security Review capability. Security-relevant mechanisms therefore route to the existing Architecture/security review semantics, evidence, and severity ownership. A quality-only issue may remain CQ-only when no traceable security consequence is established. A hardcoded secret, unsafe deserialization, weak cryptography, dangerous subprocess, insecure temporary-file behavior, authorization-affecting race, or input-validation weakness must be routed for Architecture/security adjudication when its security consequence is material.

Both interpretations may remain: CQ records the implementation-quality issue and Architecture/security records its security or architectural meaning, linked by `CORRELATED`, `CAUSAL`, or `ESCALATED` as applicable. Code Quality must not downgrade, replace, close, or suppress the Architecture/security interpretation. A future dedicated Security capability would require a separate architecture and design decision.

## 9. Cross-capability relationship model

Relations are bounded, explicit, and preserve independent identities:

| Relation | Source → target and direction | Symmetry/cardinality | Severity, lifecycle, freshness, role |
|---|---|---|---|
| `DUPLICATE` | duplicate candidate/record → retained authority | Directional during adjudication; many-to-one | No automatic severity change; duplicate is rejected/superseded; follows retained freshness; semantic collapse, not navigation |
| `CORRELATED` | distinct records sharing evidence/mechanism | Symmetric; many-to-many | No automatic transfer; each lifecycle/freshness remains independent; semantic and navigational |
| `CAUSAL` | contributing issue → materially affected issue | Directional; many-to-many | Informs reasoning but does not transfer severity/lifecycle; relation is rechecked when bindings change; semantic |
| `ESCALATED` | CQ finding → external Architecture/security/TE adjudication target | Directional; many-to-many | Target owner decides; no automatic severity transfer; independent lifecycle/freshness; semantic routing |
| `DERIVED` | accepted semantic record → derived semantic/view record | Directional; one-to-many | Derived record cannot mutate source; freshness depends on source; semantic lineage |
| `INDEPENDENT` | records intentionally distinct despite shared area/evidence | Symmetric; many-to-many | No automatic effects; navigation plus explicit independence assertion |

Design and implementation must support one CQ finding related to multiple external records and vice versa where evidence warrants. Relation cardinality, severity interaction, lifecycle interaction, freshness impact, and whether a relation is navigational or semantic are explicit properties; a relation never collapses identities by implication.

## 10. Materiality, severity, and confidence

**Materiality** is the persistence gate: a candidate becomes an accepted CQ finding only when evidence establishes a concrete maintainability, operational, reliability, security-adjacent, or testability consequence within the declared scope. A metric, threshold, warning, or style preference alone is not materiality.

**Severity** is assigned only to an already-material accepted CQ finding and uses the repository-compatible simple scale `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`:

- `CRITICAL`: an immediate, severe CQ consequence affecting system safety, data integrity, availability, or catastrophic release/maintainability risk; rare for a CQ-only interpretation;
- `HIGH`: a serious defect, reliability, security-adjacent, or change/maintenance risk with broad, recurring, or failure-prone impact;
- `MEDIUM`: a clear material maintainability, reliability, testability, or change-cost issue with bounded impact and non-urgent remediation;
- `LOW`: a real material issue with localized consequence and low urgency.

Severity reflects consequence breadth, blast radius, likelihood, recoverability, recurrence, and operational/security effect; maintainability cost may support a lower severity. Security relevance does not automatically make CQ severity `CRITICAL`, and Architecture/security severity remains owned by the receiving authority. Line count, warning/linter level, repetition count, category, or confidence alone does not determine severity. Non-material informational observations remain evidence or review notes and do not receive `CQ-*` authority; no separate `INFO` CQ finding class is introduced.

**Confidence** records certainty in the observation and interpretation, using `HIGH`, `MEDIUM`, `LOW`, or `UNKNOWN` for candidates. Accepted findings require sufficient confidence to defend the claim; confidence may qualify or block acceptance but does not reduce the actual consequence severity.

Materiality, severity, and confidence are separate fields and decisions. There is no elaborate composite score.

## 11. Evidence model

The evidence chain is:

`observation → heuristic/candidate → interpretation → material consequence`.

An accepted finding must identify the repository/source baseline, exact file and line/range or symbol where available, mechanism/pattern, applicable language/framework context, direct evidence or `EV-*` references, consequence, materiality rationale, and confidence. A static-analysis warning is evidence for review, not an accepted finding.

Minimum representative evidence:

| Category | Required defensible evidence |
|---|---|
| Duplication | comparable code regions, repeated behavior/logic, scope, and consequence beyond mere similarity |
| Complexity/cohesion | measured or observable structure plus responsibility/consequence analysis, not size alone |
| Dead code | unreachable/unused binding, relevant build/feature-flag context, and evidence it is not intentional compatibility code |
| Resource leak | acquisition/release path, exceptional path or lifecycle gap, and plausible resource consequence |
| Concurrency | shared state/scheduling path, unsafe ordering or isolation evidence, and plausible consequence even without an incident |
| Framework anti-pattern | applicable framework/version convention, concrete misuse, and consequence in this scope |
| Hardcoded localization | user-facing path, localization context, and affected locale behavior; internal constants are not automatically localization findings |
| Dependency misuse | dependency binding/version/use site, applicable contract, and concrete maintenance, reliability, security, or lifecycle consequence |

## 12. Shared Evidence and STM reuse

`WS-*` remains the Shared Evidence workset and `EV-*` remains an addressable observation within a workset. Code Quality may store source-local observations as `EV-*`; an observation is not itself a CQ finding or STM fact.

STM remains factual authority for accepted system/topology/interface/interaction/data/event/flow/auth/configuration/error facts (`COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, `FLOW-*`, `AUTH-*`, `CFG-*`, `ERR-*`). When a CQ interpretation depends on such facts, the Technical Model Gate requires an accepted, sufficiently covered, sufficiently fresh, and sufficiently resolved targeted STM slice. Missing, stale, disputed, or insufficiently covered STM blocks only the dependent CQ slice and routes through the existing STM workflow. Code Quality never reconstructs a private competing technical model.

## 13. Candidate, applicability, disposition, and freshness axes

These are five distinct concepts, not one status enum.

1. **Candidate state** is pre-authority and transient: `CANDIDATE` may result in `ACCEPTED_FINDING`, `REJECTED_FALSE_POSITIVE`, `NOT_APPLICABLE`, or `EXCLUDED`. A rejected candidate is not persistent CQ semantic authority. An audit trail may retain its evidence and decision separately.
2. **Finding lifecycle** applies only to persistent `CQ-*` records: `ACTIVE → RESOLVED` or `SUPERSEDED`. `CANDIDATE` is not a finding lifecycle state. Acceptance is an adjudication event that creates an `ACTIVE` finding, not a redundant `ACCEPTED` lifecycle state.
3. **Applicability** is `APPLICABLE`, `NOT_APPLICABLE`, or `EXCLUDED`. `NOT_APPLICABLE` means the rule/addendum does not apply to the target; `EXCLUDED` means the target is intentionally outside the selected scope or policy. Neither produces an accepted CQ finding.
4. **Disposition** is separate: `FALSE_POSITIVE` rejects a candidate and leaves no accepted finding; `ACCEPTED_EXCEPTION` records a real active finding intentionally accepted with rationale; `WONT_FIX` records a real active finding whose remediation is declined. Neither means `RESOLVED`.
5. **Freshness** is independent and uses `CURRENT`, `STALE`, or `BLOCKED`. It describes validity of bindings, not semantic lifecycle.

`SUPPRESSED` is not a hidden additional meaning: use `EXCLUDED` for intentional scope exclusion, or `ACCEPTED_EXCEPTION`/`WONT_FIX` for an accepted issue with rationale. Legal combinations include:

| Combination | Meaning |
|---|---|
| `ACTIVE + CURRENT` | accepted finding with valid bindings |
| `ACTIVE + WONT_FIX + CURRENT` | real current finding with declined remediation |
| `ACTIVE + ACCEPTED_EXCEPTION + CURRENT` | real current finding with explicit exception |
| `ACTIVE + STALE` | accepted finding requiring bounded revalidation |
| `RESOLVED + CURRENT` | resolution evidence is current and the issue is no longer present |
| `SUPERSEDED + CURRENT` | historical finding replaced by a materially different accepted record |

`FALSE_POSITIVE + ACTIVE` persistent CQ authority, `NOT_APPLICABLE +` accepted finding, and `EXCLUDED +` accepted finding are invalid. `RESOLVED + STALE` is also invalid for an active semantic record: if resolution evidence itself becomes unverifiable, the record is reopened through adjudication or retained as historical `SUPERSEDED`; it is not silently presented as resolved. An `ACTIVE` finding may have an active remediation; a completed remediation never substitutes for resolution evidence.

Generated code, vendored code, migrations, fixtures, framework boilerplate, compatibility shims, feature-flagged and transitional code, and performance-specialized code require applicability and ownership checks. They may default to `EXCLUDED` or `NOT_APPLICABLE` when justified, but exclusion is not proof that no quality risk exists; materially owned or risky generated/vendor behavior may remain reviewable.

## 14. Language/framework addenda

The semantic core is language-neutral. Optional addenda declare applicable language, framework, version, scope, and evidence requirements; provide idioms, detection guidance, and known false-positive patterns. They do not define semantic authority, change `CQ-*` identity, override core materiality/severity rules, or create findings without evidence and adjudication.

Unsupported languages/frameworks may still receive core review. An unsupported addendum is not `NOT_APPLICABLE` to the entire capability. When multiple addenda apply, their observations remain evidence; conflicting heuristics are explicitly adjudicated against core evidence and do not automatically create a finding. An inapplicable or lower-authority heuristic cannot override a material core consequence.

## 15. Finding lifecycle

Candidate detection is transient. A Code Quality writer proposes a candidate and evidence; a Code Quality adjudicator records an acceptance event that creates an `ACTIVE` `CQ-*`, or records rejection/applicability/exclusion without creating one. An active finding may become `RESOLVED` only with revalidation evidence, or `SUPERSEDED` when a materially different finding replaces it. Architecture/security and TE owners transition their own records. Freshness and disposition remain the independent axes defined in section 13.

## 16. Remediation ownership

**Decision: `CODE_QUALITY_OWNS_CQRA`.** No existing capability-neutral remediation authority is present: `TASK-*` is Test Engineering-owned and cannot safely represent CQ remediation. Code Quality therefore owns `CQRA-*` without creating a generic project-management system.

`CQRA-<repository-scoped stable allocation>` is allocated monotonically and session-safely, persists independently of report projections, and never encodes severity or category. The authoritative record contains: identity; action/title; linked `CQ-*` findings; scope and responsible owner; rationale and semantic basis/evidence; provenance and created/updated records; status; and relevant CQ/source/freshness dependencies.

Its minimal lifecycle is `PROPOSED → PLANNED → COMPLETED` or `CANCELLED`, with `SUPERSEDED` for an action replaced by a materially different action. Code Quality writers may propose; Code Quality adjudicators/owners accept or plan, cancel, supersede, and record completion. `COMPLETED` requires implementation evidence but does not resolve a CQ finding; CQ revalidation is still required. If the underlying CQ semantic basis changes, the action becomes `STALE` or requires re-evaluation until its links are reconciled. One `CQ-*` may link to many `CQRA-*` actions and one action may link to many findings. A CQRA action does not create or mutate `TASK-*`, RF, STM, TE authority, or projections.

## 17. Freshness and source bindings

Findings bind to the selected repository/dirty baseline, file revision, symbol identity/content fingerprint where available, relevant dependencies and versions, framework/configuration revisions, applicable addendum revision, targeted STM revision, and related RF/TE semantic records when those relations affect interpretation. Algorithms are an implementation decision.

The following can stale or require impact analysis: semantic refactor, symbol/file move or deletion, dependency/framework upgrade, configuration change, addendum change, generated-code regeneration, relevant STM revision, or related Architecture/TE authority change. A rename or equivalent refactor may preserve a finding when its semantic bindings remain equivalent; a changed binding is not assumed equivalent merely because prose looks unchanged.

## 18. NEW, EXTEND, REVALIDATE, and RESUME

- **NEW** selects Code Quality independently, acquires required evidence and targeted STM, and creates new CQ authority only after applicability, evidence, and materiality adjudication.
- **EXTEND** adds only the requested CQ scope/output to an accepted review, reusing valid evidence/STM and leaving unrelated accepted work untouched.
- **REVALIDATE** performs impact analysis and revalidates the minimum affected CQ semantic slice. It is not a full rerun and does not silently regenerate projections.
- **RESUME** restores selected CQ scope, outputs, current phase, accepted semantic references, blockers, freshness/verification state, and projection-impact state from persistent coordinator state compatible with `working/INDEX.md` plus owning records. It does not reconstruct state from chat/prose memory or silently restart a full review. Stale dependencies route through existing freshness/revalidation semantics, while valid upstream work remains reusable.

These fit the existing coordinator without compound modes. `working/INDEX.md` is coordinator workflow authority only; CQ finding/remediation records remain semantic authority.

## 19. Scope, coverage, and dirty state

Targetable scope includes repository, directory/module/package, component, file, symbol, changed files, category-focused review, and language/framework-filtered review. Scope is explicit and affects evidence bindings, claims, coverage, freshness, and projection completeness. A partial review must say what is covered and qualify summaries; unavailable evidence blocks only claims that require it, not unrelated slices.

The Code Quality session/assessment authority carries one minimal coverage limitation state; no separate factual model is needed. It records `requested_scope`, `reviewable_scope`, `excluded_scope`, `unavailable_scope`, `unsupported_scope`, any dirty/noncanonical scope, `coverage_status`, limitation reason, and affected claims/outputs. Coverage status is `COMPLETE`, `PARTIAL`, or `BLOCKED`: `PARTIAL` qualifies claims about unreviewed scope, while `BLOCKED` prevents claims requiring unavailable evidence. Neither invalidates independent accepted findings in an unaffected slice. A report or summary must disclose the limitation and cannot imply repository-wide coverage. Package completeness uses this authority: a required projection for an unavailable or blocked required slice remains blocked; unrelated CQ slices may proceed.

Dirty/uncommitted source may be reviewed only when explicitly selected. The result binds to a dirty-baseline marker and file/content bindings and carries a non-reproducible warning; dirty scope is never silently treated as canonical Git baseline. Mixed-ownership monorepos retain package/owner scope and route remediation to the responsible owner. Findings may cross ownership boundaries through explicit relations, but this capability does not become a Product Review aggregate. Binary or opaque artifacts are evidence/dependency context unless an applicable source interpretation is possible.

## 20. Output and projection model

| Output | Classification |
|---|---|
| CQ semantic finding records | **CORE AUTHORITY** |
| Code Quality Findings View/Report | **CORE PROJECTION** over accepted findings; the default useful report, not mandatory in every session |
| Code Quality Summary | **DERIVED PROJECTION**, never finding authority |
| Maintainability Hotspots | **OPTIONAL/DERIVED** unless distinct semantic need is proven |
| Code Quality Roadmap Contribution | **OPTIONAL/DERIVED** |

Findings are semantic state, not a report file. Each output is independently selectable; `CORE PROJECTION` means a default useful output, not a mandatory output in every CQ session. A summary, hotspot, or roadmap view cannot mutate or outrank a CQ finding.

## 21. Stage B projection integration

Every independently regeneratable CQ view/report reuses the shared Stage B lifecycle: stable `PRJ-*` identity, owning capability and projection contract revision, exact semantic dependencies, upstream projection dependencies where applicable, frozen dependency-resolution snapshot, candidate generation, V1–V4, canonical fingerprint, verified `PRJ-*@revN` publication, freshness state, and `RG-*` regeneration records. Semantic CQ findings and remediation actions do not receive PRJ identities merely because they persist.

Semantic changes flow through Projection Impact Analysis, which accounts for affected projections as `CURRENT`, `STALE`, or `BLOCKED`. Explicit regeneration is separate and requested only as required. For a named Stage D package, membership is an explicit finite declaration plus dependency-derived closure, never a global list of every possible output. It uses the shared policies exactly:

- `PERMISSIVE`: the selected package may be produced with optional/scoped CQ projections stale or blocked when limitations are declared;
- `REQUIRED_SCOPE_CURRENT`: every projection required by the selected CQ output/scope and its mandatory dependency closure is `CURRENT`; non-selected outputs may remain stale;
- `ALL_SCOPED_CURRENT`: every projection explicitly resolved as required in the scoped package is `CURRENT`; optional or unselected outputs do not become required.

For example, selecting the Findings View and Summary requires only their declared dependency closure; Hotspots and Roadmap Contribution are not required unless selected or dependency-required. Package membership and freshness govern projection usability, not semantic finding validity. `PROJECTION_IMPACT_ACCOUNTED` precedes the package gate, and no policy causes global regeneration. `PROJECTION_REPAIR` repairs projection state/presentation only and cannot change CQ semantic authority. Projection dependency direction remains consumer → prerequisite; semantic relations are not projection edges.

## 22. Candidate-to-finding flow

`Shared Evidence/STM → observation → transient candidate → applicability/filtering → evidence sufficiency → materiality adjudication → accepted CQ finding → cross-capability correlation/escalation → remediation action → bounded revalidation → Projection Impact Analysis → explicit projection generation`.

Tool output can enter as evidence at the observation/candidate stage. It cannot skip applicability, evidence, materiality, or ownership adjudication.

## 23. Tooling authority boundary

Linters, AST tools, grep, language servers, dependency analyzers, framework scanners, and other static tools may acquire observations and candidate evidence. `tool warning != accepted CQ finding`. Tool selection, parser choice, and analyzer configuration are implementation-plan decisions; a tool cannot define severity, materiality, lifecycle, suppression, Architecture escalation, or remediation authority.

## 24. Pressure-case resolution matrix

| # | Pressure case | Design behavior |
|---:|---|---|
| 1 | 100 duplicated lines in generated code | Check applicability/ownership; exclude when justified, otherwise require material consequence and evidence. |
| 2 | 3-line duplication across security-critical auth handlers | Small size does not defeat materiality; review and route security/Architecture implications. |
| 3 | 2000-line cohesive module | Size alone is insufficient; require responsibility/cohesion consequence. |
| 4 | 300-line generated parser function | Apply generated-code/addendum context; no automatic finding or proof of safety. |
| 5 | User-facing Russian string in localization-enabled UI | Require localized path evidence and consequence; likely CQ localization finding if applicable. |
| 6 | Hardcoded internal protocol constant | Not automatically localization; classify assumption/dependency only with material consequence. |
| 7 | Dead code behind feature flag | Inspect flag/build/reachability context; distinguish transitional or intentional code. |
| 8 | Intentional compatibility-shim duplication | Require rationale/applicability; accepted exception or exclusion may be appropriate. |
| 9 | Concurrency hazard without observed failure | Static mechanism and plausible consequence can establish materiality; incident is not required. |
| 10 | Resource leak only on exceptional path | Show acquisition/release path and consequence; accept only when evidence is sufficient. |
| 11 | Harmless framework anti-pattern at current scale | Applicability and material consequence are required; heuristic alone is rejected. |
| 12 | Smell already represented by RF-* | Correlate/causal/escalate or duplicate-adjudicate; do not create authority collision. |
| 13 | Testability issue already represented by TE GAP-* | Preserve CQ and TE meanings only when distinct; relate explicitly, never mutate GAP. |
| 14 | Same smell across 50 files | Scope/repeat evidence may raise materiality; deduplicate semantic issue without losing locations. |
| 15 | Vendored third-party source | Exclude by scope when appropriate; exclusion is not evidence of absence of risk. |
| 16 | Stale finding after refactor | Compare bindings and revalidate impacted slice; mark stale until resolved, superseded, or retained. |
| 17 | Code changed but semantics equivalent | Retain identity only when bindings/evidence establish equivalence; otherwise re-adjudicate. |
| 18 | Quality issue with security implications | Retain CQ interpretation and route security/Architecture interpretation; never downgrade it. |
| 19 | Mixed-language monorepo | Scope owners/languages and applicable addenda explicitly; aggregate views do not merge authority. |
| 20 | Changed-files-only review | Bind scope and claims to changed files plus required dependencies; do not claim repository completeness. |
| 21 | Incomplete source availability | Qualify coverage and block only dependent claims; record limitation explicitly. |
| 22 | Unsupported language/framework | Run core where possible; declare addendum unavailable, never silently apply it. |
| 23 | Mixed ownership | Preserve owner/scope and route remediation; cross-owner relations are explicit. |
| 24 | Dirty selected scope | Bind to dirty baseline/content and warn non-reproducibility; never call it canonical. |
| 25 | Binary/generated artifact referenced by source | Treat as opaque context or excluded applicability unless a source-backed interpretation is possible. |
| 26 | Conflicting framework heuristics | Preserve observations, adjudicate against core evidence, and do not create findings automatically. |

## 25. Deferred implementation decisions

No semantic decisions required for Design approval remain deferred: candidate versus finding, lifecycle, applicability, disposition, freshness, remediation authority, CQRA ownership, severity, package policy, coverage authority, semantic/projection boundary, and orchestration are defined above.

The following remain implementation-plan decisions: tool/parser and AST library selection, addenda rollout order, serialization/storage/index layout, exact selector syntax, CI integration, caching/parallelization, and incremental optimization. They must not alter the semantic contracts above.

## 26. Design invariants

- `CQ finding != Architecture RF finding`.
- `CQ finding != TE GAP/TASK/BC/CC/MAT/TM`.
- `tool warning != accepted CQ finding`.
- `evidence observation != semantic finding`.
- `semantic CQ authority != generated projection`.
- `working/INDEX.md != semantic authority`.
- `PROJECTION_REPAIR != semantic remediation`.
- `REVALIDATE != projection regeneration`.
- `confidence != severity`.
- `materiality != severity`.
- `WONT_FIX != FALSE_POSITIVE`.
- `ACCEPTED_EXCEPTION != RESOLVED`.
- `unsupported addendum != NOT_APPLICABLE to entire CQ capability`.
- `dirty scope != canonical Git baseline`.
- `generated/vendor exclusion != proof of absence of quality risk`.
- `CANDIDATE != persistent CQ finding lifecycle`.
- `package membership != semantic CQ authority`.
- `CQRA completion != CQ resolution`.

## 27. Design acceptance criteria

Independent Design Review may approve this Design only if it can verify that:

1. `CQ-*` authority is distinct from RF, STM, and TE authority and has defensible identity/lifecycle/freshness semantics.
2. Materiality, severity, confidence, evidence, applicability, disposition, and remediation are distinct and auditable.
3. Local quality issues can remain CQ-only while material architecture/security/test-assurance implications route to their owners without identity collapse.
4. Shared Evidence and targeted accepted/fresh STM are reused without a private factual model.
5. All six relationship types have explicit direction, cardinality, and effect semantics.
6. Candidate observations do not become findings without evidence and adjudication.
7. NEW, EXTEND, REVALIDATE, and RESUME preserve minimum-slice and persistent coordinator behavior.
8. Partial and dirty scopes make coverage/provenance limitations explicit.
9. Generated outputs use the shared Stage B lifecycle, impact accounting, freshness, and package policies; semantic work never silently regenerates projections.
10. The 26 pressure cases have coherent outcomes and no tool, framework, or exclusion rule becomes authority by implication.
