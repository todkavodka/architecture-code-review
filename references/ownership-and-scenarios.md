# Ownership, Invariants, and Adversarial Scenarios

This file is the authoritative Architecture Review reference for interpretation of ownership, derivation of invariants, and adversarial concurrency/lifecycle scenarios. Factual owner, writer, reader, lifetime, and scope records belong to the accepted, sufficiently fresh Shared Technical Model (STM); this reference consumes them as factual input for architectural analysis.

## 1. Ownership matrix

For material entities and resources, STM records the factual matrix:

| Entity/resource | Authoritative owner | Writers | Readers | Lifetime | Scope |
|---|---|---|---|---|---|

Ownership is derived from real code paths and runtime behavior, not from directory names or desired architecture. The owner/writers/readers/lifetime/scope matrix is an STM fact with evidence and provenance; it is not an Architecture finding and not an `SER-*`.

If a required factual row is missing, stale, or conflicting, request `TECH_FACT_CANDIDATE`, `TECH_FACT_CONFLICT`, or `TECH_FACT_REVALIDATION_REQUEST`. Do not create a parallel ownership inventory.

Pay particular attention to:

- process-global singletons;
- per-connection and per-session ownership;
- frontend store vs backend/native state;
- temporary files, ports, and child processes;
- event listeners and subscriptions;
- locks, abort controllers, and retry loops;
- persistent state, caches, and configuration.

## 2. Invariants

An invariant is a required system property derived from real product requirements, contracts, or behavior.

A good form is:

```text
Observation: profileId is unique only within a connection.
Product requirement: two connections may exist simultaneously.
Invariant: session state cannot be identified globally by profileId alone.
```

Do not invent an invariant merely because it would make the architecture “cleaner”.

For every invariant, record:

- the source of the requirement;
- scope;
- owner;
- what would violate the invariant;
- which flows exercise it.

## 3. Adversarial scenario matrix

For stateful or concurrent areas, test at least the applicable scenarios from this set:

```text
A + A duplicate operation
A + B simultaneous owners
operation + cancel
operation + disconnect/dispose
old completion after replacement
retry + cancellation
shutdown during active work
duplicate event
missing event
same local ID under two parent owners
```

Do not turn this list into a mechanical quota. Select scenarios according to actual capability and ownership boundaries.

## 4. Race/interleaving evidence

A race finding normally requires a concrete sequence:

```text
A starts
→ A suspends/awaits/subscribes
→ B mutates relevant shared state
→ A resumes
→ stale/invalid mutation or wrong-owner effect
```

Without a reachable sequence, the issue is a candidate rather than a confirmed race.

For every scenario, record:

- initial state;
- actors/owners;
- suspension/interleaving point;
- state mutation;
- resumed behavior;
- concrete consequence;
- existing guards and falsification attempt.

## 5. Positive Controls

Record mechanisms that correctly enforce ownership, isolation, or concurrency, such as:

- correct owner keys;
- locks;
- generation/version checks;
- cancellation tokens;
- scoped DI/object graph;
- idempotency;
- dynamic resource allocation.

A Positive Control is not praise for balance. It is a mechanism that Target Architecture and remediation must not accidentally break.

## 6. Factual correction request

If thematic investigation conflicts with an accepted, sufficiently fresh STM ownership fact, **do not edit STM or the As-Built projection directly**. Request Technical Model Gate adjudication.

Record:

```markdown
## TECH_FACT_CONFLICT TFC-###

**Current STM fact/revision:** ...
**Observed contradiction:** ...
**Evidence:** ...
**Expected impact:** ...
**Affected areas:** ...

Status: TECH_FACT_CONFLICT
```

Use `TECH_FACT_CANDIDATE` for new factual material and `TECH_FACT_REVALIDATION_REQUEST` for stale or impact-affected factual material. The Technical Model Gate defined in `shared-technical-model.md` then applies.

## 7. Architecture correction candidate

If factual input is accepted and sufficiently fresh, but an Architecture-owned invariant, adverse-scenario interpretation, race conclusion, `SER-*`, finding/root/severity, or remediation implication requires correction, use `ARCH-CORRECTION-CANDIDATE`.

It does not change the factual owner/writer matrix and follows the Architecture correction/adjudication protocol.

## 7.1 Change Review candidate Architecture assessment

In `CHANGE_REVIEW_CANDIDATE` mode, Architecture records interpretation only:

```text
architecture_candidate_assessment:
  candidate_origin: CR-*/CRF-*
  affected_accepted_refs: [<accepted STM/Architecture refs>]
  candidate_fact_refs: [<CR-*/CF-* refs>]
  assessment_effect: INTRODUCES_RISK | WORSENS_EXISTING | MITIGATES |
                     POTENTIALLY_RESOLVES | NO_MATERIAL_IMPACT | UNKNOWN_IMPACT
  interpretation
  limitations
```

This assessment cannot create an accepted Architecture finding, root, severity, invariant, or STM fact. `RESOLVED`, `CLOSED`, and `ACCEPTED` are not candidate Architecture outcomes; they may only quote an existing canonical state.

An explicit `RECONCILE_CHANGE` dispatch routes qualified input to Architecture authority, which independently adjudicates and creates or links the canonical record while retaining `candidate_origin` traceability.

`CHANGE_REVIEW_CANDIDATE` is the Architecture candidate mode for a selected Change Review. It may interpret changed accepted references, including parent-qualified API operation, property, and boundary evidence, but it must remain review-local. It cannot allocate or mutate an accepted `RF-*`, STM fact, invariant, root, severity, or lifecycle state. The later Architecture authority decision is the only path to canonical acceptance.

## 8. Supporting Engineering Risks

Broad structural patterns can increase the probability of repeated defects without constituting one runtime root finding by themselves, for example:

- semantic ownership is not encoded in identity;
- lifecycle state is spread across several flags;
- an event carries identity but the consumer discards it;
- a shared resource is not owner-keyed;
- there is no local deterministic regression suite.

Such observations may be tracked as `SER-*`; do not automatically assign them the severity of a Product defect.

## Product Architecture Review boundary

In Product mode, a Product-scoped `RF-*` is an Architecture Review semantic record only when it has an independently adjudicated cross-project architectural consequence. Its evidence packet names the accepted Product revision and immutable baseline, affected Projects, qualified `WS-*`/`EV-*` observations, accepted STM facts/relations, lifecycle, severity, provenance, and direct dependencies.

Product membership or a generated aggregation does not promote a Project-local RF. Product report/projection content is navigation only and cannot write the RF.

### Finding lifecycle authority barrier

Architecture Review alone accepts or changes `RF-*` lifecycle, severity, disposition, revision, resolution, reopening, and supersession. `Product` qualification and aggregation may consume accepted child state but cannot perform an RF transition.

`CHANGE_REVIEW` may record candidate `POTENTIALLY_RESOLVES`; only contextual `RECONCILE_CHANGE` can route qualified evidence to Architecture owner adjudication, which must independently accept the new RF revision. Candidate assessment and projection prose never mutate accepted RF authority.