# Evidence, Candidate Lifecycle, and Severity

This file is the authoritative reference for the evidence contract, candidate promotion lifecycle, security attack-chain gate, Safe Reproduction / Evidence Validation, and severity adjudication.

## 1. Evidence contract

A material finding must separate:

1. **Observation** — what the code demonstrably does.
2. **Interpretation** — why the mechanism is architecturally significant.
3. **Risk/impact** — the concrete failure, security, or consistency effect.
4. **Recommendation direction** — without prematurely designing the To-Be architecture.

For cross-layer claims, provide evidence from every material boundary. One line naming a class does not prove an architectural problem.

Evidence format:

```text
src/module/file.py:120-168
src/other/file.ts:41-77
```

## 2. Candidate lifecycle

Discovery does not create an authoritative finding directly.

Normal flow:

```text
CANDIDATE
→ independent verification
→ CONFIRMED | CORRECTED | REFUTED | UNVERIFIED
→ root-boundary adjudication
→ authoritative RF / projection / SER / open question
→ severity adjudication
→ authoritative ledger
```

`REFUTED` candidates and superseded formulations must remain in the working evidence trail so they are not accidentally resurrected later.

Discovery Coverage Review does not replace this flow: it checks completeness of mechanism-class investigation, not correctness of an already discovered candidate.

## 3. Evidence strength

Track confidence separately from severity:

- `HIGH` — the mechanism and reachable flow are established by code; preferably also confirmed by verification or runtime evidence.
- `MEDIUM` — strong static evidence exists, but a key runtime condition has not been reproduced.
- `LOW` — plausible but incomplete evidence; normally an open question or `UNVERIFIED`, not a headline finding.

Do not raise severity merely because confidence is high. Confidence answers “is this true?”; severity answers “how bad is it?”.

For clarity, evidence descriptions may include:

```text
STATICALLY_CONFIRMED
RUNTIME_REPRODUCED
RUNTIME_VALIDATION_UNAVAILABLE
```

These are **not lifecycle states or severity levels**. They describe the type of factual evidence only.

Use `RUNTIME_REPRODUCED` only when a runtime check was actually executed and its result was recorded. If no runtime check was performed, do not use wording that implies factual reproduction.

## 4. Safe Reproduction / Evidence Validation

Runtime reproduction can increase confidence and establish reachability or semantics, but the architecture audit Skill is not a penetration-testing or exploitation framework.

Safe Reproduction is an **optional** way to strengthen evidence. It is not a prerequisite for every finding.

### Allowed purpose

Demonstrate the minimum harmless effect needed to distinguish:

```text
the mechanism actually exists
vs
the static interpretation was wrong
```

Prefer, in order:

1. an existing non-destructive test;
2. an existing local fixture or harness;
3. an isolated test environment;
4. synthetic input or local semantic reproduction.

### Authorization boundary

Perform runtime reproduction only on a system, environment, or repository the user is authorized to test.

Do not use an audit as justification for probing unrelated external targets or third-party infrastructure.

### Hard safety boundary

Safe Reproduction does not include:

- destructive actions;
- persistence;
- privilege escalation;
- credential theft;
- lateral movement;
- data exfiltration;
- modification or corruption of real production data;
- probing unrelated external targets;
- reusable offensive payload packs.

Demonstrate the **minimum effect necessary**. Do not expand reproduction merely because the first exploit primitive has already been established.

### Injection-like mechanisms

For an injection-like candidate, prefer proving:

```text
construction semantics
or
harmless local/test predicate manipulation
```

Do not extract real data or chain privileges merely to demonstrate severity.

### When reproduction is unavailable

If a safe runtime check is not possible, do not force a PoC.

Instead:

```text
preserve static evidence
→ state runtime limitation
→ keep confidence proportional to actual evidence
```

`RUNTIME_VALIDATION_UNAVAILABLE` does not mean a static finding is automatically false or low severity. It describes a limitation of the evidence channel.

### Relationship to candidate lifecycle and severity

Successful Safe Reproduction may:

- increase confidence;
- confirm a reachable condition;
- falsify an incorrect static interpretation.

It does **not**:

- bypass independent verification;
- bypass root-boundary adjudication;
- assign severity by itself;
- automatically increase severity;
- turn a conditional capability into a direct exploit without evidence.

## 5. Security attack-chain gate

A serious security finding (`HIGH` or `CRITICAL`) requires an evidenced chain where applicable:

```text
attacker capability
→ entry point
→ trust boundary crossed
→ failed/missing control
→ privileged effect
→ concrete impact
```

Classify exploitability separately:

```text
DIRECT
CONDITIONAL
DEFENSE_IN_DEPTH
```

The absence of a hardening control is not by itself a `HIGH` or `CRITICAL` vulnerability. A conditional post-compromise capability does not automatically inherit the severity of a hypothetical prerequisite compromise.

Runtime reproduction does not need to reach a complete offensive attack chain. The chain may be established through a combination of static and runtime evidence as long as every material link is supported.

## 6. Severity adjudication

Assign severity **after** verification and the root-boundary gate.

Evaluate:

- impact;
- reachability;
- blast radius;
- recoverability;
- frequency/exposure;
- prerequisites;
- attacker model for security findings;
- dependency on product intent.

For every material finding, explicitly ask:

```text
Why not one level higher?
Why not one level lower?
```

### CRITICAL

Use only for evidence-backed catastrophic or systemic outcomes, such as practical RCE or elevated code execution, broad authentication bypass, likely material loss/corruption of data, unrecoverable secret exposure, or systemic outage without reasonable containment. Do not use it as rhetorical emphasis.

### HIGH

Serious realistic production impact: wrong-owner mutation, process-wide crash through a reachable path, major authorization/permission flaw, severe lifecycle/concurrency/data-consistency failure, or a security exploit with a strong attack chain that does not reach `CRITICAL`.

### MEDIUM

Material but bounded reliability, security, maintainability, or testability problem: lifecycle/resource leak, conditional security weakness, substantial fragility, or localized wrong behavior with a limited blast radius.

### LOW

Localized problem with limited practical impact.

### INFORMATIONAL

Defense-in-depth or architectural note with no evidenced material incorrect behavior, but useful for hardening or clarity.

### PENDING_PRODUCT_INTENT

Use when correctness or severity depends on unresolved product intent. Do not invent policy.

## 7. Supporting Engineering Risks

`SER-*` represents recurrence or non-detection risk, not necessarily a runtime defect. Examples include ownership identity not encoded, lifecycle state spread across flags, or missing deterministic local regression tests.

An SER may receive remediation priority, but it must not automatically inherit the severity of the nearest RF.

## 8. Finding shape

```markdown
## RF-012 — Short human-readable title

**Severity:** HIGH
**Confidence:** HIGH
**Exploitability:** DIRECT | CONDITIONAL | DEFENSE_IN_DEPTH | N/A

**Root mechanism.** ...

**Evidence:**
- `path/file.ext:10-40`
- `path/other.ext:80-120`

**Evidence validation:** STATICALLY_CONFIRMED | RUNTIME_REPRODUCED | RUNTIME_VALIDATION_UNAVAILABLE

**Reachable scenario.** ...

**Practical consequence.** ...

**Why not higher / lower.** ...

**Projections.** ...

**Related SER / open questions.** ...
```

`Evidence validation` describes the actual evidence mode and is not mandatory when the active report contract already expresses that distinction more clearly. Do not create a parallel lifecycle state machine.

Recommendation direction may be brief. Detailed Target Architecture is created only when the selected endpoint requests it.

## 9. Anti-noise rules

Do not promote any of the following to a material finding without concrete impact:

- file length;
- `unwrap`, `clone`, or mocks;
- TODO/comment;
- framework choice;
- lint warning count;
- hardcoded literal;
- absence of a test;
- broad API surface without a reachable misuse path;
- raw-looking API name without provenance/effect;
- mere inability to produce a PoC.

Absence evidence ≠ defect evidence.

Runtime reproduction unavailable ≠ finding false.

Runtime reproduction successful ≠ severity automatically higher.

## 10. Stable identity

Before adjudication, use `CAND-*`. After the root-boundary gate, use stable `RF-*` identifiers for roots, `SER-*` for Supporting Engineering Risks, and `OQ-*` for open questions. Do not create separate root IDs for one mechanism merely because it appears in different files or layers.

## Product RF evidence and severity binding

For a Product-scoped Architecture finding, severity adjudication consumes the independently verified Product revision and immutable baseline, affected Projects, qualified `WS-*`/`EV-*` observations, accepted STM facts/relations, and the material Product consequence. Product membership or report aggregation is not sufficient evidence.

The existing Architecture Review `RF-*` lifecycle and severity vocabulary remain authoritative; no Product severity family is introduced. Conflicting or unavailable evidence remains an explicit limitation and cannot be silently promoted to an accepted Product finding.

## Architecture RF resolution and revision gate

Architecture Review alone accepts RF lifecycle, severity, disposition, and revision changes. An RF `RESOLVED` revision requires accepted evidence, revalidation against the exact proving source/evidence/dependency binding, owner adjudication, and retained provenance to the prior revision. A changed severity or disposition is a new accepted revision of the same stable identity when the root mechanism and correction boundary remain valid.

Developer assertion, commit message, candidate Change Review, Product inference, projection prose/omission, or completed remediation alone cannot create `RESOLVED`. A materially different mechanism uses qualified supersession authority; recurrence of the same mechanism uses a newer `ACTIVE` revision with `reopened_from` provenance.