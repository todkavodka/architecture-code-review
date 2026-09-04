# Shared Technical Model

The Shared Technical Model (STM) is the persistent semantic authority for
accepted shared technical facts. It consumes bounded, baseline-bound
observations from the [Shared Evidence Model](shared-evidence-model.md) and is
separate from capability interpretations and human-readable projections.

This contract owns STM families, relations, lifecycle, fact authority, and
persistence. Direct dependency metadata, generated dependency indexes, and
impact traversal belong to [Technical Model dependencies and impact](technical-model-dependencies.md).
Session routing and compact workflow state belong to
[Session Orchestration](session-orchestration.md) and
[Review Modes and Orchestration](review-modes-and-orchestration.md). Freshness
decisions remain subject to
[Revalidation and compact-state freshness](revalidation-and-freshness.md).

## 1. Scope and materiality

An STM fact records what the evidence-bounded system materially is or does. It
is not a finding, risk, recommendation, test gap, or product-behavior
authority. Those conclusions remain owned by the capability that makes them.

The initial schema is deliberately materiality-based. Do not create a component
for every class, function, or trivial helper; do not promote a new object family
until repeated cross-capability use requires stable identity and revisioning.

## 2. First-class facts and relations

Initial fact families are:

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

Relations are semantically meaningful links even when persisted as object
metadata rather than standalone artifacts. The initial controlled vocabulary is:

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

Do not use arbitrary free-form relation names as a substitute for this
vocabulary.

The following concerns are intentionally embedded as properties or relations
on accepted first-class facts, not separate families initially:

```text
ENTRYPOINT
STATE
LIFECYCLE
CONCURRENCY
DEPLOYMENT
OBSERVABILITY
```

## 3. Identity, provenance, and state

Each STM artifact has stable semantic identity, a revision, baseline binding,
and references to its supporting `WS-*` / `EV-*` observations. A minimum
semantic record includes its family ID, revision, status, freshness, applicable
authority state, relevant relations, and direct outbound dependency metadata.
The evidence contract owns the observation record itself; the STM records only
its provenance reference. Dependency/index authority and impact semantics are
defined in `technical-model-dependencies.md`.

Lifecycle, freshness, and authority are independent axes:

```text
status:
  CANDIDATE | UNDER_REVIEW | ACCEPTED | SUPERSEDED | REJECTED

freshness:
  VALID | REVALIDATION_REQUIRED | UNKNOWN

authority where applicable:
  RESOLVED | UNRESOLVED
```

Preserve identity when the same object is revised, for example `IF-021@rev3`.
When the semantic identity changes, preserve history with an explicit
`supersedes` / `superseded_by` link; do not rewrite a prior accepted revision to
look current.

## 4. Observed views and interpretation boundary

An STM fact may preserve multiple observed representations:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

These are observations, not an implicit source-precedence rule. The STM does
not decide whether declaration, implementation, consumers, or tests govern a
contract. A required authority decision is adjudicated outside the projection,
by the appropriate specialist gate (for example, Test Engineering Contract
Verification).

## 5. Technical Model Gate

The Technical Model Gate is the sole writer of accepted shared fact semantics:
only it may accept, revise, reject, or supersede an STM fact. Other capabilities
may emit exactly these requests:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

They must not directly rewrite accepted STM artifacts. A capability may continue
within an unaffected bounded scope while a conflict is reconciled, but it must
not consume a disputed required fact or dependency as accepted downstream truth.
This gate governs STM facts only; capability-owned interpretations retain their
own semantic authority.

## 6. Persistent package shape

The recommended package layout is:

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

Paths are a recommended convention, not the authority rule. Semantic ownership,
stable identity, revision binding, and provenance are the invariant. `INDEX.md`
and generated indexes route readers to owning artifacts; they do not contain a
second technical model or become semantic authority.

## 7. Bootstrap and reuse

Every `NEW` creates the persistent STM baseline before capability execution.
Creation records the selected baseline and model manifest even when the selected
downstream work requires only a partial factual slice:

```text
always create model != always build complete model
```

The selected downstream requirement determines later population, coverage, and
depth. Existing accepted facts are reusable only when their required revision,
authority, and freshness bindings remain suitable for the requested decision.

Legacy Architecture Review As-Built authority and its migration to an STM
projection are governed by the dedicated migration work; this foundation does
not silently relabel existing As-Built material as accepted STM fact.
