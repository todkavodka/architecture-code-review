# PS-172 — Stage F historical broad interface

## Design mapping

`PS-F19`: a historical broad IF remains valid after Stage F extension.

## Setup / evidence shape

An accepted historical `IF-*` records a broad HTTP surface with direction and
identity but no Stage F operation, role, precision, or external qualification.
Its original baseline, revision, observed view, and provenance remain bound.

## Expected accepted semantic records

The Technical Model Gate continues to accept the historical IF under its
original contract. Missing Stage F fields remain absent/unknown; they are not
filled with false, exact, or default values.

## Prohibited inference / authority result

- absence of operation does not mean no operation exists;
- absence of precision does not mean `EXACT`;
- the old IF must not be rewritten into a new identity or provider/consumer
  role;
- a projection cannot reinterpret history against current revisions.

## Expected projection behavior

Technical Documentation renders the broad IF with an explicit historical or
missing-qualifier limitation. Selectors and snapshots preserve the old
definition/revision semantics and do not fabricate Stage F matches.

## Backward-compatibility constraint

This is a compatible extension: old IF identity, revision, observed view, and
meaning remain valid. No bulk enrichment, automatic regeneration, or
retroactive Product qualification occurs.

## GREEN criteria

GREEN iff the historical IF remains usable, every absent Stage F field stays
absent/unknown, and no current exactness, identity, or Product state is
fabricated.

## Verdict

`PS172_PASS_HISTORICAL_IF_COMPATIBILITY`
