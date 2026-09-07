# PS-143 — Stale Product projection only

## Input state

Accepted Product semantic state is unchanged, but one Product projection is
stale after impact accounting. A user requests a presentation repair or a
fresh selected output.

## Expected semantic behavior

The coordinator keeps Product semantic authority unchanged, records projection
freshness independently, and routes a selected fresh output through the
existing projection/regeneration contract. `PROJECTION_REPAIR` remains
presentation-only and cannot hide semantic drift.

## Forbidden behavior

- treating the projection as Product semantic authority;
- using stale projection state to invalidate unrelated semantics;
- regenerating automatically during impact analysis;
- turning presentation repair into full Product `REVALIDATE` without semantic
  drift evidence.

## Affected authority

Projection lifecycle and impact contracts own freshness/regeneration routing;
Product and capability semantic owners remain unchanged.

## Expected impact scope

Only the stale projection and its resolved dependency closure; unrelated
Product semantic records and projections remain unaffected.

## Package/projection outcome

The selected package gate evaluates its resolved required members. Unrelated
stale projections do not block an unrelated package under existing policy.

## Verdict

`PS143_PASS_PRODUCT_PROJECTION_FRESHNESS_ISOLATION`
