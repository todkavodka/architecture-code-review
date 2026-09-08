# PS-166 — Stage F Redis store-only precision

## Design mapping

`PS-F13`: a Redis store is known while the key pattern is unknown, so
`STORE_ONLY` is valid only for the DS/store-bounded case.

## Setup / evidence shape

Evidence establishes a Redis store and a data-access interaction, but the key
pattern or child resource cannot be resolved. The source is Project-qualified
and records the unavailable target limitation without retaining credentials.

## Expected accepted semantic records

The Technical Model Gate may accept a Redis `DS-*` with `resource_kind=STORE`
and `precision=STORE_ONLY`; where a DATA_ACCESS INT is accepted with a known
parent store and unresolved child target, it may also use `precision=STORE_ONLY`
under the approved applicability rule. The access mode remains explicit if
evidenced.

## Prohibited inference / authority result

- `STORE_ONLY` must not be assigned to IF, EVENT, FLOW, or non-data INT;
- store presence does not identify a key pattern or exact child resource;
- parent containment does not imply access, ownership, or migration authority;
- no secret-bearing connection value is copied.

## Expected projection behavior

The data projection renders the safe logical Redis store, store-only precision,
any separately evidenced DATA_ACCESS INT, and the unresolved key-pattern
limitation. It does not render an exact key pattern or interface precision.

## Backward-compatibility constraint

Historical store-level DS records remain valid. Missing child-resource fields
are unknown/absent rather than false or exact, and no bulk enrichment occurs.

## GREEN criteria

GREEN iff `STORE_ONLY` appears only in its approved DS/DATA_ACCESS applicability,
the unknown key pattern remains bounded, secret safety is preserved, and no
containment-based access or ownership is inferred.

## Verdict

`PS166_PASS_REDIS_STORE_ONLY`
