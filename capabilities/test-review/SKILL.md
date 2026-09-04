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

## Required Test Assurance Summary

Detailed evidence is not the primary user-facing answer. At completion of Test Review, produce a concise decision-oriented **Test Assurance Summary** before the detailed assurance map or Test Plan.

When capability artifacts are persisted, Test Review owns and writes:

```text
00-test-assurance-summary.md
```

The summary must let a reader understand in about one minute:

1. **Verdict** — can the current test system be trusted for the material behavior that matters? Use a plain decision token such as `TEST_ASSURANCE_SUFFICIENT`, `TEST_ASSURANCE_PARTIAL`, or `TEST_ASSURANCE_INSUFFICIENT`, followed by one sentence explaining why.
2. **What is working well** — only the few material strengths supported by accepted evidence.
3. **What is wrong** — the 3–7 most decision-relevant weaknesses, ordered by material consequence. Explicitly distinguish misleading/false-confidence tests from merely absent evidence when that distinction matters.
4. **Assurance state** — compact bounded accounting with the total: adequately evidenced, partially evidenced, not evidenced, unknown/unreviewed.
5. **What to do first** — a short ordered priority list, normally P0/P1/P2 or equivalent, derived from the accepted assurance map and Test Plan. Do not invent a second roadmap or change existing roadmap ownership.
6. **Important limitations** — only limitations that materially affect the verdict, such as unavailable runtime validation.
7. **Detailed evidence** — pointers to `01-test-assurance-map.md` and, when selected, `02-test-plan.md`.

The summary is a projection of accepted capability evidence. It may compress and prioritize, but MUST NOT strengthen, weaken, reclassify, or invent technical conclusions.

Do not turn the summary into another ledger. `MAT-*`, `GAP-*`, `RF-*`, `TM-*`, `TASK-*`, and `WS-*` identifiers may appear as compact traceability references after a human-readable statement, but they must not be the primary prose. Do not list every gap merely because it exists. Prefer the few weaknesses that explain why the verdict is what it is.

Recommended size: roughly one to two screens. If the reader must study the detailed map or plan before understanding the verdict, the major weaknesses, and the first actions, the Test Review presentation is not accepted.

When Test Review is embedded in an umbrella audit, the umbrella report should surface the Test Assurance Summary verdict and link to the capability-owned summary instead of reproducing the detailed Test Review evidence.

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

Before creating or materially revising any behavior, contract, assurance,
mapping, environment, simulator, or E2E artifact, Test Engineering must derive
and persist its minimum factual STM dependency slice. The slice must be
accepted, sufficiently fresh and resolved, and have its targeted coverage
accepted by an independent Technical Model Coverage Review after the facts
pass through the Technical Model Gate. For `NEW` this follows STM bootstrap; for
`EXTEND` it reuses qualifying existing facts and builds only missing ones; for
stale or disputed facts it performs Technical Model revalidation first. An
accepted/fresh `FULL` model satisfies the slice without a duplicate targeted
model. Until that precondition holds, Test Engineering cannot reach its
capability semantics.

Test Engineering reuses accepted/fresh STM observations instead of
reconstructing facts from the As-Built projection. STM facts remain distinct
from Test Engineering semantics: `IF-*` is not `BC-*`, `INT-*` is not `MAT-*`,
`ERR-*` is not `GAP-*`, and STM does not classify contract mismatches or test
gaps. Missing, stale, or disputed facts go through the Technical Model Gate;
the capability cannot rewrite accepted STM.

## Test Engineering extension

For Test Engineering outputs beyond the existing Test Assurance core, read
`capabilities/test-review/references/test-engineering-contract.md` before
constructing Behavior Contracts, Contract Verification records, environment
strategy, simulator design, or E2E design.

Selectable outputs are:

```text
Test Assurance [required]
Test Plan [optional]
Contract Consistency Report [optional projection]
Test Environment Design [optional]
Service Simulator Design [optional]
Service Simulator Implementation Plan [optional; requires accepted simulator spec]
E2E Test Plan [optional]
```

Behavior Model is an internal dependency, not a checkbox. Contract Verification
is automatic when materially applicable. The extension designs and plans test
capability; it does not implement product tests, a Service Simulator, or test
infrastructure during review.

Persist the selected outputs as independent fields. Existing `REVIEW_ONLY` and
`REVIEW_PLUS_TEST_PLAN` packages are legacy input and normalize conservatively:
the former selects only Test Assurance; the latter selects Test Assurance plus
Test Plan. Neither legacy value silently enables an extended output.

## Stage B projection boundary

The numbered, human-readable Test Review outputs are `PRJ-*` projections of
accepted Test Engineering semantics and the qualifying factual STM slice. They
may summarize, organize, and cross-link that authority, but cannot accept,
revise, classify, or resolve it. `BC-*`, `CC-*`, `MAT-*`, `TM-*`, and `GAP-*`
remain capability-owned semantic authority; their generated renderings do not
replace the authoritative records.

`working/INDEX.md` remains coordinator workflow authority. It is never a
projection, package member, semantic dependency substitute, fingerprinted
output, or regeneration target. Do not infer either projection status or
semantic authority from an output filename, an index, or a generated document.

The Test Review publication package always requires the Test Assurance Summary
and Map. Test Plan, Contract Consistency Report, Test Environment Design,
Service Simulator Design and Implementation Plan, E2E Test Plan, and the
human-readable Behavior Contract Model join the package only through their
explicit selected-output or capability-required conditions. Resolve that finite
membership snapshot before the package gate; an unselected optional document
does not block closeout. The projection IDs, direct exact/selector dependencies,
and condition-to-member rules are defined in
[`test-engineering-contract.md`](references/test-engineering-contract.md).

Select a dependency strategy per material dependency and justify it. Keep
dependency substitutes separate from a Service Simulator of the reviewed
service; simulator consumer protocols and its test-only control plane remain
separate. E2E is selected only when multi-component assurance adds material
value.
