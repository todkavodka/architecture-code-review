# PS-142 — Targeted Product `REVALIDATE`

## Input state

A source binding for Project B advances within an accepted Product baseline;
the Product has qualified dependencies from B to a subset of Project A.

## Expected semantic behavior

`REVALIDATE` starts with the exact previous/current baseline bindings, finds
B's local impact root, verifies direct dependency metadata, traverses only the
qualified affected slice, and records affected versus preserved state. Missing
material linkage records `CONTEXT_EXPANSION_REQUIRED`; `SYSTEMIC` may emit
`FULL_REAUDIT_RECOMMENDED` for explicit user choice.

## Forbidden behavior

- rereading every Product repository by default;
- treating a reverse index or relation as dependency authority;
- marking unknown linkage preserved;
- automatically executing a full Product review or regeneration.

## Affected authority

Revalidation owns impact routing and delta reconciliation; Evidence/STM and
capability owners adjudicate refreshed semantics; projection impact owns
freshness accounting.

## Expected impact scope

Project B and directly dependent qualified Product records only, expanding to
the minimum evidenced boundary when required; unaffected accepted state is
preserved.

## Package/projection outcome

Affected resolved package members may become stale or blocked after impact
accounting. Unrelated package members remain governed independently.

## Verdict

`PS142_PASS_BOUNDED_PRODUCT_REVALIDATE`
