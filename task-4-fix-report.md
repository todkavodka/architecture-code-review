# Task 4 fix report

Scope was limited to `references/projection-impact.md` and this report. Later
tasks and production code were not changed.

## Fixed findings

- Replaced non-canonical impact reasons with the controlled base-design
  vocabulary and documented deterministic mapping for `ADDED`, `REMOVED`,
  `SUPERSEDED`, `REVISION_CHANGED`, and `STATUS_CHANGED`.
- Added explicit projection-contract and selector-contract reason handling.
- Added direct and propagated `UPSTREAM_PROJECTION_BLOCKED` handling, keeping
  blocked consumers blocked and routing them to the blocker’s owning gate.
- Added `contract_change_id`, contract kind/selector identity, and previous /
  current contract revisions to the stabilized input. Selector resolutions are
  now explicitly bound to the matching contract change and checked for current
  revision consistency.

## Checks

- Focused vocabulary/predicate checks passed.
- Deprecated reason-name check passed.
- `git diff --check` passed.
