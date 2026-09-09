# PS-173 — Stage F historical store-level DS

## Design mapping

`PS-F20`: a historical store-level DS remains valid without entity enrichment.

## Setup / evidence shape

An accepted historical `DS-*` identifies a database/store and technology but
does not identify tables, child resources, access mode, or migration authority.
Its original Project/revision and evidence bindings are preserved.

## Expected accepted semantic records

The Technical Model Gate continues to accept the store-level DS. Missing child
resource and access qualifiers remain absent or unknown. A later table or INT
observation creates separately evidenced additive state.

## Prohibited inference / authority result

- store presence does not imply table/resource access;
- parent/resource containment does not imply ownership, dependency, or
  migration authority;
- absent access mode is not READ or WRITE;
- historical DS is not rewritten or globally enriched.

## Expected projection behavior

Data and Product projections may render the store-level DS and an explicit
entity-enrichment limitation. They do not list invented child resources or
access relationships.

## Backward-compatibility constraint

The historical store-level record remains valid as a compatible extension.
No bulk STM rewrite, forced precision, Product conversion, or automatic
regeneration occurs.

## GREEN criteria

GREEN iff the old DS remains accepted with its original meaning, absent child
and access fields remain unknown/absent, and projections avoid inferred detail.

## Verdict

`PS173_PASS_HISTORICAL_DS_COMPATIBILITY`
