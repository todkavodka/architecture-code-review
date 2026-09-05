# PS-127 — Dirty and partial coverage is qualified

## Observed RED baseline

The baseline has no Code Quality session/assessment coverage authority and no
CQ provenance model for dirty tracked content, untracked source, or unavailable
files. It cannot qualify claims while preserving unaffected findings.

Observed verdict: `PS127_PASS_AS_RED`

## Setup / input state

The selected scope contains staged and unstaged tracked changes, an untracked
source file, and a missing or unreadable subdirectory. Some findings are
supported by reviewable unchanged files.

## Required semantic behavior

The assessment records requested, reviewable, excluded, unavailable,
unsupported, and dirty/noncanonical scope with `COMPLETE`, `PARTIAL`, or
`BLOCKED` coverage. Claims and projections are qualified; unaffected accepted
findings remain usable when their dependencies remain sufficient.

## Forbidden behavior

- presenting dirty content as the canonical Git baseline;
- claiming repository-wide coverage from a partial review;
- invalidating every accepted finding because one dependent slice is blocked.

## Expected post-implementation invariant

Coverage limitation is authoritative session state, not an implicit absence
claim or a private factual model.

## Verdict vocabulary

`PS127_PASS_AS_RED`
`PS127_GREEN_COVERAGE_AND_PROVENANCE_QUALIFIED`
