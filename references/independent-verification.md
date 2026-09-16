# Independent Candidate Verification

This file defines Independent Verification for discovery candidates. Discovery output consists of hypotheses; the verifier must independently re-check the code/path and actively attempt to falsify each conclusion.

## 1. Input

The verifier receives:

- the exact repository baseline;
- `working/INDEX.md`;
- the list of `CAND-*` records and links to their source working artifacts;
- the accepted As-Built Architecture;
- relevant Positive Controls and open questions;
- a narrow task: confirm, correct, or refute candidates, not design remediation.

Do not trust a candidate statement merely because it was produced by an earlier pass.

## 2. Allowed outcomes

```text
CONFIRMED
CORRECTED
REFUTED
UNVERIFIED
NEW_ADJACENT
```

`NEW_ADJACENT` is allowed when verification of a specific candidate reveals a neighboring mechanism. Do not turn verification into a new unbounded discovery pass.

## 3. Minimum falsification contract

For every candidate, explicitly ask:

- is the state or resource actually shared?
- is global scope intentional?
- does another layer or path provide a guard?
- is the alleged stale completion actually reachable?
- does the event or boundary already carry owner/request identity?
- does the consumer actually discard that identity?
- is the selected state a snapshot or a live observable?
- is the resource globally fixed, or isolated by another mechanism?
- is cleanup actually not awaited, or does the runtime guarantee waiting?
- is the security entry point reachable from attacker-controlled input?

If falsification requires unknown product intent, do not invent it. Preserve an open question or `PENDING_PRODUCT_INTENT` downstream.

## 4. Evidence shape

For `CONFIRMED` or `CORRECTED`, record:

```text
candidate ID
current mechanism
reachable path/scenario
code evidence
falsification attempted
why guard/alternative does not invalidate it
concrete effect
result
```

For `REFUTED`, explain the exact falsifier rather than merely saying “not confirmed”.

For `UNVERIFIED`, identify the evidence that is missing or unavailable.

## 5. Correction propagation

When the verified mechanism differs from an earlier pass:

```text
old statement
→ corrected statement
→ evidence
→ affected candidate/findings searched
→ stale contradictory wording marked superseded
```

A common failure mode is using an intuitive model of library/runtime semantics — for example `once`, cancellation, or shutdown — instead of the actual semantics. When uncertain, verify real API guarantees or code behavior.

## 6. Role of verification

Verification answers the question **“is this actually true?”**

It must not:

- assign final severity;
- merge different mechanisms into an attractive root without the root-boundary gate;
- design Target Architecture;
- rewrite As-Built directly;
- treat absence evidence as proof of a defect.

## Product RF verification

For a Product-scoped Architecture candidate, independent verification must confirm the joint scope tuple before Architecture adjudication:

```text
Product identity/revision + immutable Product baseline
→ affected Projects
→ qualified WS-*/EV-* evidence
→ accepted STM facts/relations
→ material Product architectural consequence
```

Verification must also confirm that the candidate uses the existing `RF-*` family, remains Architecture-owned, and is not merely a Project-local RF, aggregate report, projection, or generated index. A missing or conflicting tuple is `UNVERIFIED` / bounded evidence, not Product RF acceptance.

## 7. Handoff

The working verification artifact ends with the persisted `HANDOFF SUMMARY` required by `review-modes-and-orchestration.md`, including the outcome of every `CAND-*`, any new `AC-*` / `OQ-*`, and supersessions.