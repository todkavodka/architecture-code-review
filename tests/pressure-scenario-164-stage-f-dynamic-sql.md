# PS-164 — Stage F dynamic SQL

## Design mapping

`PS-F11`: dynamic raw SQL records known store/resource bounds and an unresolved
target without fabricating an exact child resource.

## Setup / evidence shape

An application executes raw SQL against a known PostgreSQL database, but table
or schema names are assembled dynamically and cannot be resolved at the exact
source revision. Evidence identifies the store and operation, with an explicit
dynamic-target limitation.

## Expected accepted semantic records

STM may accept a DS store or bounded resource and an `INT-*` DATA_ACCESS record
with the evidenced access mode and `precision=RESOURCE_BOUNDED` or
`UNRESOLVED`. The target is not fabricated as a particular TABLE. A later exact
observation may create a new revision.

## Prohibited inference / authority result

- a database connection or raw SQL string does not prove a specific table;
- dynamic SQL cannot be parsed into an exact target by projection prose;
- bounded precision cannot silently become EXACT;
- no SQL parser or runtime scanner is introduced by the scenario.

## Expected projection behavior

The data projection shows the known store/bounded resource, access operation,
precision, and dynamic limitation. It does not list an invented table or emit a
clean empty result.

## Backward-compatibility constraint

Historical store-level DS facts remain valid without child-resource enrichment;
new evidence is additive and does not rewrite prior broad records.

## GREEN criteria

GREEN iff the accepted target remains bounded/unresolved at the supported
precision, the access authority is INT when an operation is evidenced, and no
exact child resource is fabricated.

## Verdict

`PS164_PASS_DYNAMIC_SQL_BOUNDARY`
