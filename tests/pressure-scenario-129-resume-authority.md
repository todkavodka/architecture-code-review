# PS-129 — RESUME restores persistent Code Quality authority references

## Observed RED baseline

The baseline has no CQ orchestration registration or persisted CQ scope,
output, blocker, or semantic-reference state. Existing `working/INDEX.md`
semantics cannot yet restore a Code Quality session.

Observed verdict: `PS129_PASS_AS_RED`

## Setup / input state

A session stops after selecting a CQ scope and outputs and after recording
partial semantic work, blockers, and prerequisite state.

## Required semantic behavior

`RESUME` restores selected scope, selected outputs, blockers, phase, and owning
CQ semantic references from persistent coordinator state. Stale dependencies
route through existing freshness/revalidation semantics.

## Forbidden behavior

- reconstructing workflow state from chat or prose memory;
- silently restarting the full review;
- treating `working/INDEX.md` as CQ semantic authority.

## Expected post-implementation invariant

`working/INDEX.md` remains coordinator workflow authority only; accepted CQ
records remain authoritative in their owning records.

## Verdict vocabulary

`PS129_PASS_AS_RED`
`PS129_GREEN_RESUME_STATE_RESTORED`
