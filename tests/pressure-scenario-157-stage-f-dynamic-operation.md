# PS-157 — Stage F dynamic operation precision

## Design mapping

`PS-F04`: a known provider with a dynamic operation remains unresolved at
operation precision.

## Setup / evidence shape

A provider service and base endpoint are known, but the operation path or
method is assembled dynamically and cannot be resolved at the accepted source
revision. Evidence records the known provider and bounded dynamic limitation;
it does not provide a fabricated operation identity.

## Expected accepted semantic records

The Technical Model Gate may accept a provided IF with known interface kind and
safe bounded address, `precision=RESOURCE_BOUNDED` or `UNRESOLVED`, and the
dynamic limitation. An operation-level INT or exact operation field is absent
unless separately evidenced.

## Prohibited inference / authority result

- a base URL does not prove an exact operation;
- dynamic string construction does not become an exact path;
- bounded precision cannot silently upgrade to `EXACT`;
- no compatibility comparison uses an invented operation.

## Expected projection behavior

Technical Documentation renders the known provider/bounded interface and
explicit unresolved-operation limitation. It does not render an empty clean
operation list or a false exact operation.

## Backward-compatibility constraint

Historical broad IF records remain valid without operation fields. Later
resolution creates a new revision or enrichment and preserves the prior
limitation.

## GREEN criteria

GREEN iff the provider is represented only at evidenced precision, dynamic
operation details remain absent or unresolved, and projections visibly retain
the limitation without inventing exactness.

## Verdict

`PS157_PASS_DYNAMIC_OPERATION_LIMIT`
