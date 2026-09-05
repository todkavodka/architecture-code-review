# Code Quality semantic contract

This reference defines the semantic authority owned by Code Quality Review. It
does not implement orchestration, projection generation, source modification,
or a static-analysis toolchain.

## Authority and identity

Code Quality owns accepted, materially consequential implementation-quality
findings identified as `CQ-*`. It also owns Code Quality remediation actions
identified as `CQRA-*`; their lifecycle and state axes are defined in
`code-quality-lifecycle.md`.

The following are not Code Quality semantic authority:

- tool warnings, metrics, grep hits, AST matches, or heuristic hits;
- `EV-*` observations or `WS-*` worksets;
- STM facts;
- Architecture `RF-*` findings;
- Test Engineering `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, or `TASK-*`;
- generated reports, summaries, hotspots, package manifests, or
  `working/INDEX.md`.

`CQ-<repository-scoped stable allocation>` is stable, persistent, and carries
no category, severity, location, or confidence. A candidate receives a CQ
identity only when accepted as semantic authority. Revalidation retains the
identity when the mechanism remains the same across a move, rename, or
semantics-preserving refactor. A materially different mechanism receives a new
identity; supersession records the relationship rather than mutating one
finding into another.

## Accepted finding contract

An accepted `CQ-*` record must contain, or reference, all of the following:

| Field | Semantic requirement |
|---|---|
| `identity` | Stable `CQ-*` identity. |
| `scope` | Explicit repository, package, component, file, symbol, or focused scope. |
| `category` | One primary language-neutral taxonomy category; secondary tags may add context. |
| `mechanism` | Concrete implementation pattern or mechanism under review. |
| `evidence` | Direct source evidence and addressable `EV-*` observations where used. |
| `consequence` | Concrete maintainability, change-cost, defect, reliability, testability, operational, or security-adjacent consequence. |
| `materiality` | Adjudication that the issue warrants persistent CQ authority. |
| `severity` | CQ consequence severity, independent of materiality and confidence. |
| `confidence` | Certainty of the observation and interpretation. |
| `applicability` | `APPLICABLE`, `NOT_APPLICABLE`, or `EXCLUDED`. |
| `disposition` | `FALSE_POSITIVE`, `ACCEPTED_EXCEPTION`, or `WONT_FIX` where applicable. |
| `source_bindings` | Baseline, file/symbol/content, dependency, framework/configuration, and addendum bindings. |
| `freshness` | `CURRENT`, `STALE`, or `BLOCKED`. |
| `lifecycle` | `ACTIVE`, `RESOLVED`, or `SUPERSEDED`. |
| `relationships` | Explicit bounded relations to other semantic records. |
| `remediation` | Links to zero or more `CQRA-*` actions. |
| `provenance` | Author, evidence revision, adjudication, and update provenance. |

Counts, rankings, hotspot scores, labels, and prose summaries are derived or
display fields, not substitutes for these fields.

## Candidate-to-finding rule

The semantic flow is:

```text
WS/EV observation
  -> transient candidate
  -> applicability and evidence sufficiency
  -> materiality adjudication
  -> accepted CQ-* finding
```

`CANDIDATE` is pre-authority and transient. It may be rejected as
`FALSE_POSITIVE`, marked `NOT_APPLICABLE`, or marked `EXCLUDED`; none of those
outcomes creates an active CQ finding. A warning, metric, line count, repeated
text fragment, or framework rule cannot bypass evidence and materiality.

## Language-neutral taxonomy

The bounded primary categories are:

```text
DUPLICATION
HARDCODED_ASSUMPTION
LOCALIZATION
DEAD_OR_OBSOLETE_CODE
COMPLEXITY_OR_COHESION
ABSTRACTION_MISUSE
ERROR_HANDLING
RESOURCE_MANAGEMENT
ASYNC_CONCURRENCY
FRAMEWORK_MISUSE
DEPENDENCY_USAGE
TESTABILITY
API_OR_LIFECYCLE_MISUSE
MAINTAINABILITY
```

Categories are semantic lenses, not a framework-rule catalog. One semantic
issue has one primary category and may use secondary tags; symptoms do not
automatically create duplicate findings.

## Materiality, severity, and confidence

Materiality answers whether an observation deserves persistent CQ identity. A
metric, LOC threshold, warning level, duplication count, or style preference
alone is not materiality.

Severity applies only after materiality is accepted:

- `CRITICAL`: rare, immediate and severe CQ consequence affecting safety, data
  integrity, availability, or catastrophic release/maintainability risk;
- `HIGH`: serious quality, reliability, security-adjacent, or change-risk
  consequence with broad, recurring, or failure-prone impact;
- `MEDIUM`: clear material maintainability, reliability, testability, or
  change-cost issue with bounded impact and non-urgent remediation;
- `LOW`: real material issue with localized consequence and low urgency.

Severity reflects the CQ consequence, breadth, blast radius, likelihood,
recoverability, recurrence, and urgency. Size, count, linter severity, category,
confidence, or security relevance alone does not determine it. Security and
Architecture owners retain their own severity semantics; security relevance
does not automatically make a CQ finding `CRITICAL`.

Confidence records certainty of evidence and interpretation as `HIGH`,
`MEDIUM`, `LOW`, or `UNKNOWN`. Confidence may qualify or block acceptance but
does not reduce the consequence severity. Informational or non-material notes
remain evidence/review notes and do not receive `CQ-*` identity.

## Evidence contract

Accepted findings must answer: what code, where, what mechanism, what evidence,
why it is materially problematic, under which applicability, and with what
expected or observed consequence.

Minimum evidence by category:

| Category | Minimum evidence |
|---|---|
| `DUPLICATION` | Comparable regions, repeated behavior/logic, scope, and consequence beyond similarity. |
| `COMPLEXITY_OR_COHESION` | Observable structure plus responsibility or change consequence; size alone is insufficient. |
| `DEAD_OR_OBSOLETE_CODE` | Reachability/usage and build or feature-flag context, including intentional compatibility checks. |
| `RESOURCE_MANAGEMENT` | Acquisition/release path, exceptional or lifecycle path, and plausible resource consequence. |
| `ASYNC_CONCURRENCY` | Shared state/scheduling path, unsafe ordering or isolation, and plausible consequence; an incident is not required. |
| `FRAMEWORK_MISUSE` | Applicable framework/version rule, concrete misuse, and consequence in scope. |
| `LOCALIZATION` | User-facing path, localization context, affected locale behavior, and consequence. |
| `DEPENDENCY_USAGE` | Dependency/version/use site, applicable contract, and concrete maintenance, reliability, security, or lifecycle consequence. |

Observation, interpretation, and consequence remain distinguishable. A static
tool result is evidence for adjudication, never an accepted finding by itself.

## Shared Evidence and STM

`WS-*` is the Shared Evidence workset and `EV-*` is an addressable observation
within that workset. Code Quality may store source-local facts as `EV-*`; an
observation is not a CQ finding and is not an STM fact.

STM remains factual authority for accepted system/topology/interface/interaction/
data/event/flow/auth/configuration/error facts:

```text
COMP-* IF-* INT-* DS-* EVENT-* FLOW-* AUTH-* CFG-* ERR-*
```

When a CQ interpretation depends on system-level facts, it requires the
accepted, sufficiently covered, sufficiently fresh, and sufficiently resolved
targeted STM slice. Missing, stale, disputed, or insufficiently covered STM
blocks only the dependent CQ interpretation and routes through the existing STM
workflow. Code Quality never rewrites STM or reconstructs a private factual
model.

## Architecture, Test Engineering, and security boundaries

`CQ-* != RF-*`. A local issue remains CQ-only when its consequence does not
materially alter a system boundary, invariant, cross-component contract, trust
boundary, ownership/lifecycle rule, or system-level reliability/security
mechanism. Code Quality never creates, mutates, closes, downgrades, or
suppresses `RF-*`; an Architecture escalation is a request for Architecture
adjudication.

`CQ-* != BC/CC/MAT/TM/GAP/TASK`. Code Quality may interpret implementation
quality around seams, isolation, nondeterminism, observability, dependency use,
concurrency, and fragile setup. Test Engineering owns its behavior, contract,
assurance, evidence, gap, and task records. Shared evidence may support both
interpretations, but Code Quality cannot create or mutate TE authority.

There is currently no independent Security Review capability. Security-relevant
mechanisms route through existing Architecture/security semantics and severity
ownership. Code Quality may retain a distinct quality finding when that
interpretation is independently valid; it must not downgrade, replace, close,
or suppress the security interpretation. A future dedicated Security
capability requires a separate architecture/design decision.

## Bounded cross-capability relations

Relations preserve independent identities and are not a generic graph
framework:

| Relation | Meaning and effects |
|---|---|
| `DUPLICATE` | Same semantic issue represented twice; directional during adjudication, many-to-one, no automatic severity change, and one retained authority. |
| `CORRELATED` | Distinct records share evidence or mechanism; symmetric, many-to-many, no lifecycle/severity transfer. |
| `CAUSAL` | Source issue materially contributes to target issue; directional, many-to-many, informs reasoning without ownership transfer. |
| `ESCALATED` | CQ evidence requests external Architecture/security/TE adjudication; directional, many-to-many, target owner decides. |
| `DERIVED` | A downstream semantic/view record is produced from an accepted source; directional, one-to-many, source remains authoritative. |
| `INDEPENDENT` | Same evidence or area, intentionally distinct interpretations; symmetric, many-to-many, no automatic effect. |

Relations carry endpoints, rationale, direction/cardinality where applicable,
and freshness bindings. They do not copy severity, couple lifecycles, or make a
projection authoritative. `CQRA-*` is not `TASK-*` and does not change these
boundaries.

## Applicability and addenda

The core is language-neutral. Optional language/framework addenda may declare
language, framework, version, scope, applicability, idioms, evidence
expectations, and known false positives. They do not define authority, identity,
materiality, severity, lifecycle, or remediation.

Unsupported addenda fall back to core review where possible and do not make the
whole capability `NOT_APPLICABLE`. Conflicting addenda produce observations for
adjudication; they do not automatically create a CQ finding. Generated,
vendored, migration, fixture, boilerplate, compatibility, feature-flagged,
transitional, and performance-specialized code requires applicability and
ownership checks. Exclusion is not proof of no quality risk.

## Invariants

- `CQ finding != Architecture RF finding`.
- `CQ finding != TE GAP/TASK/BC/CC/MAT/TM`.
- `CQRA-* != TASK-*`.
- `tool warning != accepted CQ finding`.
- `evidence observation != semantic finding`.
- `semantic CQ authority != generated projection`.
- `working/INDEX.md != semantic authority`.
- `PROJECTION_REPAIR != semantic remediation`.
- `REVALIDATE != projection regeneration`.
- `confidence != severity` and `materiality != severity`.
- `WONT_FIX != FALSE_POSITIVE` and `ACCEPTED_EXCEPTION != RESOLVED`.
- `generated/vendor exclusion != proof of absence of quality risk`.
