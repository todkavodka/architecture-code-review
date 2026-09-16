# Target Architecture and Independent Review

This stage runs only for the `REVIEW_PLUS_TARGET_ARCHITECTURE` or `REVIEW_PLUS_TARGET_AND_ROADMAP` endpoint, and only after the authoritative audit state has been accepted.

## 1. Target Architecture input

Target Architecture is derived from:

```text
verified RF roots
+ architectural invariants
+ SER
+ Positive Controls
+ explicit product decisions
```

Do not design an “ideal system” from scratch.

For every material new abstraction or mechanism, answer:

> Which RF, SER, invariant, or product requirement requires this change?

If there is no answer, remove the abstraction unless the existing product genuinely requires it.

## 2. Required content

Where applicable, the target document describes:

- target component and responsibility boundaries;
- authoritative ownership and identity model;
- state and lifecycle transitions;
- cancellation, retry, and shutdown semantics;
- boundary contracts;
- security and trust model;
- resource ownership and allocation;
- migration and compatibility constraints;
- Positive Controls that must be preserved;
- unresolved product or deployment decisions;
- an RF/SER/invariant coverage matrix.

## 3. Feasibility classification

Classify material assumptions as:

```text
PROVEN_FEASIBLE
PLAUSIBLE_NEEDS_REMEDIATION_VALIDATION
PRODUCT_OR_DEPLOYMENT_DECISION
```

Do not present a plausible implementation option as a fact about the current deployment or infrastructure.

## 4. Independent Target Review

The Target Architecture author does not accept their own document.

A fresh-context reviewer checks:

- prose ↔ diagrams ↔ state tables;
- target ownership is internally consistent;
- completion and cancellation semantics are internally consistent;
- Positive Controls are not removed accidentally;
- every material target mechanism is motivated by an RF, SER, or invariant;
- product intent is not “resolved” by the author without evidence;
- feasibility assumptions are classified honestly;
- the target does not introduce a new unsupported service, boundary, or dependency without necessity;
- the security design does not assume a non-existent trust anchor or signing capability;
- As-Built facts are not confused with target-state facts.

## 5. Review outcomes

```text
TARGET_ACCEPTED
TARGET_CORRECTION_REQUIRED
TARGET_BLOCKED_BY_DECISION
```

When correction is required:

```text
author artifact
→ independent review issue list
→ separate correction pass
→ fresh-context re-review
```

Correction must not hide the history of the original review.

## 6. Review artifact

For every issue, the review records:

```text
ID
severity of design inconsistency
location
contradiction/unsupported assumption
required correction
RF/SER/invariant affected
```

The reviewer must not rewrite the target document during the review pass.

## 7. Acceptance

Target Architecture is accepted only when:

- no unresolved internal contradictions remain;
- feasibility assumptions are classified;
- RF/SER/invariant coverage is traceable;
- Positive Controls are accounted for;
- required correction and re-review work is closed;
- blocked product/deployment decisions are explicitly isolated and are not disguised as technical facts.