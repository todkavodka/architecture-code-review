---
name: test-review
description: Use when assessing whether an existing software test suite actually proves material system behavior, or when deciding whether current test evidence is sufficient for a broader assurance or release-readiness claim.
---

# Test Review

Core question: which material system contracts are actually supported by executable evidence, which are only partly supported, which are not supported, and which evidence may mislead the reviewer?

## User-facing language

When Test Review is attached to `architecture-code-review`, inherit the umbrella Skill's user-facing language contract.

When invoked standalone, use the language of the user's current substantive request unless the user explicitly asks for another language. Menus, questions, recommendations, explanations, progress/status messages, and final user-facing narrative all use that language consistently.

Keep formal identifiers, status tokens, exact code identifiers, paths, API/IPC names, and contract field names unchanged. A formal token may be followed by a natural explanation in the user's language. Do not switch to English merely because this Skill document is written in English, and do not translate canonical tokens into localized substitutes.

## Assurance completeness gate

Before making an overall test-assurance, test-system-quality, or release-readiness claim, establish:

1. a bounded inventory of every material assurance target; and
2. enough test and harness topology to identify the evidence universe being assessed.

Every material target in that bounded inventory must be represented in the accounting before the overall conclusion. Record at least:

```text
Material targets: N
Adequately evidenced: N
Partially evidenced: N
Not evidenced: N
Unknown/unreviewed: N
```

Use terminology equivalent to these labels only when it preserves the same distinctions. Do not infer completeness from test count, line or branch coverage, green-suite status, sampled-test count, representative directories or families, or the absence of problems in a sample.

## Candidate decomposition and target reconciliation

Before applying a terminal disposition to a candidate, decompose it into materially distinct claims: candidate container, implementation mechanism or smell, and any material behavioral contract. Rejecting an implementation detail applies only to that detail; it must not silently discard a separately recognized contract.

For every material contract recognized during candidate analysis, record an explicit final disposition before completing the bounded target inventory: include it as a target, mark it already represented by an accepted target, preserve it as `AUTHORITY_UNRESOLVED`, or reject it as non-material with a reason. Reconcile these dispositions before overall assurance accounting so no recognized material contract disappears when its surrounding mechanism is rejected. Do not promote mechanisms to targets or invent missing authority.

When conflicting sources would lead to different implementation-versus-test verdicts and their precedence, supersession, approval, or equivalent authority evidence is unresolved, preserve the conclusion as `UNKNOWN`/`AUTHORITY_UNRESOLVED`. Record the observable disagreement separately, identify the minimum authoritative evidence needed to resolve it, and do not issue a defect verdict based on urgency, CI or release pressure, convenience, or recency alone.

## Accounting and evidence inspection

Target accounting and evidence inspection are separate activities. Sampling is useful for investigating test families, discovering harness behavior, assessing evidence quality, and choosing where to drill deeper. It is not a substitute for accounting for the bounded material target set.

Do not turn representative or risk-based sampling into a completeness claim. Also do not require exhaustive deep review of every individual test. Group routine tests by test family, runtime path, shared harness, shared contract, or materially equivalent evidence contribution. Selectively inspect material, unique, conflicting, misleading, anomalous, or otherwise decision-relevant evidence and map the relevant evidence families to the accounted targets.

Pressure-test-derived invariant: overall assurance is valid only when bounded completeness of material-target accounting is combined with selective evidence inspection; a sample may inform evidence quality but cannot establish unreviewed targets as complete.

## Current capability boundary

Test Review evaluates existing test evidence and may optionally produce a Test Plan.

It does not modify production code or permanent tests during review.

When embedded in an umbrella audit, shared authority/freshness/artifact rules are inherited from architecture-code-review.
