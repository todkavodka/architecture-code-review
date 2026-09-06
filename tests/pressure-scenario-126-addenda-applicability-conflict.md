# PS-126 — Addenda applicability and conflict are bounded

## Observed RED baseline

The baseline has no Code Quality language/framework addenda contract. Existing
stack guidance cannot declare unsupported applicability, resolve conflicting
heuristics, or guarantee fallback to the language-neutral CQ core.

Observed verdict: `PS126_PASS_AS_RED`

## Setup / input state

Review an unsupported framework, a source file where a framework heuristic is
irrelevant, and a target where two applicable addenda disagree.

## Required semantic behavior

Applicability is declared explicitly. Unsupported or conflicting addenda do
not silently create findings; core CQ semantics remain authoritative and the
review falls back or qualifies coverage as appropriate.

## Forbidden behavior

- treating an unsupported addendum as `NOT_APPLICABLE` for all CQ review;
- allowing addenda to bypass evidence, materiality, identity, or severity;
- resolving heuristic disagreement by automatically creating authority.

## Expected post-implementation invariant

Addenda specialize detection and applicability only; they cannot replace the
core semantic contract.

## Verdict vocabulary

`PS126_PASS_AS_RED`
`PS126_GREEN_ADDENDA_APPLICABILITY_CONTROLLED`
